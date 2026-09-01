"""Deep, generic profiling of every event type (observation side).

For each `eventType` this walks every record's `data` payload recursively and
accumulates, per dotted field path: presence, JSON types, null/empty counts,
and the observed value distribution (capped for high-cardinality fields).
No event-specific code — new event types are profiled automatically.

`consistency_findings` then derives schema-consistency observations that need
no configuration at all: field-name spelling/capitalization variants, value
case variants, mixed types, empty field names, and sometimes-present fields.
Nothing is auto-merged; variants are reported for a human to judge.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

from .model import Finding, Rec, INFO, WARNING, LOW, MEDIUM, SEV_INFO

VALUE_CAP = 2000          # distinct values tracked per field before truncating
EMPTY_KEY = "<empty>"     # display name for a literal "" field name


def type_name(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, (int, float)):
        return "number"
    if isinstance(v, str):
        return "string"
    if isinstance(v, dict):
        return "object"
    if isinstance(v, list):
        return "list"
    return type(v).__name__


def fmt_value(tname: str, text: str) -> str:
    """Render a stored (type, text) value pair for reports."""
    if tname == "string":
        return f'"{text}"'
    if tname == "bool":
        return text.lower()
    return text


@dataclass
class FieldProfile:
    path: str
    count: int = 0                      # records containing this path
    types: Counter = field(default_factory=Counter)      # type name -> records
    null_count: int = 0
    empty_string_count: int = 0
    values: Counter = field(default_factory=Counter)     # (type, str) -> occurrences
    values_truncated: bool = False
    numeric_min: Optional[float] = None
    numeric_max: Optional[float] = None

    def note_value(self, v: Any) -> None:
        t = type_name(v)
        if t == "null":
            self.null_count += 1
        if t == "string" and v == "":
            self.empty_string_count += 1
        if t == "number":
            f = float(v)
            self.numeric_min = f if self.numeric_min is None else min(self.numeric_min, f)
            self.numeric_max = f if self.numeric_max is None else max(self.numeric_max, f)
        if t in ("object", "list"):
            return
        key = (t, str(v))
        if key in self.values or len(self.values) < VALUE_CAP:
            self.values[key] += 1
        else:
            self.values_truncated = True

    @property
    def n_unique(self) -> int:
        return len(self.values)


@dataclass
class EventProfile:
    event_type: str
    count: int = 0
    scenes: Counter = field(default_factory=Counter)
    sessions: set = field(default_factory=set)
    first_ts: Optional[datetime] = None
    last_ts: Optional[datetime] = None
    scene_first: Dict[str, datetime] = field(default_factory=dict)
    scene_last: Dict[str, datetime] = field(default_factory=dict)
    fields: Dict[str, FieldProfile] = field(default_factory=dict)
    top_level_keys: Counter = field(default_factory=Counter)   # raw record keys
    key_sets: Counter = field(default_factory=Counter)         # sorted tuple of data keys
    key_set_examples: Dict[Tuple, str] = field(default_factory=dict)
    event_key_count: int = 0
    non_dict_data: Counter = field(default_factory=Counter)    # type name -> count
    records: List[Rec] = field(default_factory=list)           # chronological

    def field_profile(self, path: str) -> FieldProfile:
        if path not in self.fields:
            self.fields[path] = FieldProfile(path=path)
        return self.fields[path]


def _walk(value: Any, prefix: str, seen_paths: set, prof: EventProfile) -> None:
    """Recursively record `value` under dotted path `prefix`."""
    fp = prof.field_profile(prefix)
    if prefix not in seen_paths:
        fp.count += 1
        seen_paths.add(prefix)
    fp.types[type_name(value)] += 1
    fp.note_value(value)
    if isinstance(value, dict):
        for k, v in value.items():
            name = k if k != "" else EMPTY_KEY
            _walk(v, f"{prefix}.{name}", seen_paths, prof)
    elif isinstance(value, list):
        for item in value:
            _walk(item, f"{prefix}[]", seen_paths, prof)


def build_profiles(records: List[Rec]) -> Dict[str, EventProfile]:
    """Profile every event type in chronological record order."""
    profiles: Dict[str, EventProfile] = {}
    for rec in records:
        et = rec.event_type or "<missing eventType>"
        prof = profiles.setdefault(et, EventProfile(event_type=et))
        prof.count += 1
        prof.records.append(rec)
        prof.sessions.add(rec.session_id)
        prof.scenes[rec.scene or "<missing sceneName>"] += 1
        if rec.event_key is not None:
            prof.event_key_count += 1
        for k in rec.raw:
            prof.top_level_keys[k] += 1
        if rec.ts is not None:
            if prof.first_ts is None or rec.ts < prof.first_ts:
                prof.first_ts = rec.ts
            if prof.last_ts is None or rec.ts > prof.last_ts:
                prof.last_ts = rec.ts
            sc = rec.scene or "<missing sceneName>"
            if sc not in prof.scene_first or rec.ts < prof.scene_first[sc]:
                prof.scene_first[sc] = rec.ts
            if sc not in prof.scene_last or rec.ts > prof.scene_last[sc]:
                prof.scene_last[sc] = rec.ts
        if isinstance(rec.data, dict):
            key_set = tuple(sorted(k if k != "" else EMPTY_KEY for k in rec.data))
            prof.key_sets[key_set] += 1
            prof.key_set_examples.setdefault(key_set, rec.ref())
            seen: set = set()
            for k, v in rec.data.items():
                name = k if k != "" else EMPTY_KEY
                _walk(v, f"data.{name}", seen, prof)
        else:
            prof.non_dict_data[type_name(rec.data)] += 1
    return profiles


def _norm_name(name: str) -> str:
    return re.sub(r"[^0-9a-z]", "", name.lower())


def _examples_for(prof: EventProfile, pred, cap: int = 3) -> List[str]:
    out = []
    for rec in prof.records:
        if pred(rec):
            out.append(rec.ref())
            if len(out) >= cap:
                break
    return out


def consistency_findings(profiles: Dict[str, EventProfile],
                         expectations) -> List[Finding]:
    """Config-free schema-consistency observations. `expectations` is used only
    to suppress 'sometimes-present' noise for fields the config already
    declares as conditional or optional."""
    findings: List[Finding] = []

    # eventType names that differ only in case/punctuation
    by_norm: Dict[str, List[str]] = {}
    for et in profiles:
        by_norm.setdefault(_norm_name(et), []).append(et)
    for variants in by_norm.values():
        if len(variants) > 1:
            findings.append(Finding(
                status=WARNING, severity=LOW, category="schema",
                summary="eventType name variants that differ only in spelling/case",
                observed=", ".join(sorted(variants)),
                expected="one canonical eventType name",
                evidence=", ".join(f"{et}: {profiles[et].count} records"
                                   for et in sorted(variants)),
            ))

    # sceneName variants across the whole log
    scene_counts: Counter = Counter()
    for prof in profiles.values():
        scene_counts.update(prof.scenes)
    by_norm = {}
    for sc in scene_counts:
        by_norm.setdefault(_norm_name(sc), []).append(sc)
    for variants in by_norm.values():
        if len(variants) > 1:
            findings.append(Finding(
                status=WARNING, severity=LOW, category="scenes",
                summary="sceneName variants that differ only in spelling/case",
                observed=", ".join(sorted(variants)),
                expected="one canonical sceneName",
                evidence=", ".join(f"{sc}: {scene_counts[sc]} records"
                                   for sc in sorted(variants)),
            ))

    for et in sorted(profiles):
        prof = profiles[et]
        rules = expectations.for_event(et) if expectations else {}
        declared_conditional = set((rules.get("conditional_fields") or {}).keys())
        declared_optional = set(rules.get("optional_data_fields") or [])

        # data payload that is not an object
        if prof.non_dict_data:
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="schema", event_type=et,
                summary="`data` payload is not a JSON object",
                observed=", ".join(f"{t}: {c}" for t, c in
                                   sorted(prof.non_dict_data.items())),
                evidence=f"{sum(prof.non_dict_data.values())} of {prof.count} records",
                examples=_examples_for(prof, lambda r: not isinstance(r.data, dict)),
            ))

        # empty field name (a literal "" key)
        for path, fp in sorted(prof.fields.items()):
            if EMPTY_KEY in path:
                findings.append(Finding(
                    status=WARNING, severity=LOW, category="schema", event_type=et,
                    fld=path,
                    summary="field name is an empty string",
                    observed=f"path {path} in {fp.count} records",
                    expected="a descriptive field name",
                    evidence=f"types: {dict(sorted(fp.types.items()))}",
                    examples=_examples_for(
                        prof, lambda r: isinstance(r.data, dict) and "" in r.data),
                ))

        # field-name variants within the event type
        by_norm = {}
        for path in prof.fields:
            by_norm.setdefault(_norm_name(path), []).append(path)
        for variants in by_norm.values():
            if len(variants) > 1:
                findings.append(Finding(
                    status=WARNING, severity=LOW, category="schema", event_type=et,
                    summary="field-name variants that differ only in spelling/case",
                    observed=", ".join(sorted(variants)),
                    expected="one canonical field name",
                    evidence=", ".join(f"{p}: {prof.fields[p].count} records"
                                       for p in sorted(variants)),
                ))

        for path in sorted(prof.fields):
            fp = prof.fields[path]
            # mixed value types (int+float both count as "number")
            tnames = {t for t in fp.types if t != "null"}
            if len(tnames) > 1:
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="schema", event_type=et,
                    fld=path,
                    summary="field holds inconsistent value types",
                    observed=", ".join(f"{t}: {c}" for t, c in sorted(fp.types.items())),
                    expected="one consistent type",
                    evidence=f"{fp.count} records contain {path}",
                ))
            # value case variants for categorical string fields
            if not fp.values_truncated:
                vnorm: Dict[str, List[str]] = {}
                for (t, text) in fp.values:
                    if t == "string" and text:
                        vnorm.setdefault(_norm_name(text), []).append(text)
                for variants in vnorm.values():
                    if len(variants) > 1:
                        findings.append(Finding(
                            status=WARNING, severity=LOW, category="values",
                            event_type=et, fld=path,
                            summary="values that differ only in spelling/case",
                            observed=", ".join(
                                f'"{v}" ({fp.values[("string", v)]}x)'
                                for v in sorted(variants)),
                            expected="one canonical value (or documented aliases)",
                        ))

        # sometimes-present direct fields of data (descriptive; config-driven
        # checks decide whether that is acceptable)
        dict_count = prof.count - sum(prof.non_dict_data.values())
        for path in sorted(prof.fields):
            parts = path.split(".")
            if len(parts) != 2:      # only direct children of data
                continue
            fp = prof.fields[path]
            name = parts[1]
            if 0 < fp.count < dict_count and name not in declared_conditional \
                    and name not in declared_optional and f"data.{name}" not in declared_conditional:
                findings.append(Finding(
                    status=INFO, severity=SEV_INFO, category="schema", event_type=et,
                    fld=path,
                    summary="field present in only part of the records",
                    observed=f"{fp.count} of {dict_count} records contain {path}",
                    expected="declare as conditional/optional in config if intended",
                    examples=_examples_for(
                        prof, lambda r, n=name: isinstance(r.data, dict) and n not in r.data),
                ))
    return findings
