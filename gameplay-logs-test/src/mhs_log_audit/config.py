"""Loading of the two YAML configuration files.

* event_expectations.yaml — per-event-type expected logging behavior.
  All expectation-driven checks read ONLY from this file, so a logging-design
  change should normally be handled by editing the YAML, not the Python.

* coverage manifest (config/coverage/<build-id>.yaml) — which game content was
  actually exercised in the playthrough, so that "event absent" can be
  separated into "logging failure" vs "content not tested".

Recognized keys per event in event_expectations.yaml (all optional):
  purpose               str, used in the report
  spec_source           str, where the expectation comes from
  units                 list[int], game units this event's content belongs to
  expected_scenes       list[str]
  required_data_fields  list[dotted paths that every record must contain]
  optional_data_fields  list[paths that may legitimately be absent]
  conditional_fields    {path: {when: {path: value}, required: true,
                         forbidden_otherwise: false}}
  allowed_values        {dotted path: [allowed values]}
  field_types           {dotted path: string|number|bool|object|list}
  high_frequency        bool — exempt from near-duplicate detection
  continuous            {expected_interval_seconds, tolerance_seconds,
                         min_fraction_within_tolerance}
  pairing               [{label, field, open_value, close_value, group_by}]
  start_finish          [{label, field, start_value, finish_value, group_by}]
  event_key             {required: bool | required_when: {path: value},
                         format: "template with {data.x} placeholders"}
  semantics             [{question, satisfied_by: [paths]}] — content
                        sufficiency (Step 7): can the question be answered?
  known_issues          list[str] — previously seen quirks, reported as INFO
  notes                 str

Top-level (non-event) sections:
  meta                  free-form metadata about the config itself
  cross_event_rules     [{label, if: {event_type, where: {path: value}},
                          expect: {event_type, where}, severity}]
  thresholds            {near_duplicate_seconds, burst_seconds, long_gap_seconds}
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

DEFAULT_THRESHOLDS = {
    "near_duplicate_seconds": 1.0,
    "burst_seconds": 0.05,
    "long_gap_seconds": 600.0,
}


@dataclass
class Expectations:
    path: str = ""
    meta: dict = field(default_factory=dict)
    events: Dict[str, dict] = field(default_factory=dict)
    cross_event_rules: List[dict] = field(default_factory=list)
    thresholds: dict = field(default_factory=lambda: dict(DEFAULT_THRESHOLDS))
    warnings: List[str] = field(default_factory=list)

    def for_event(self, event_type: str) -> dict:
        return self.events.get(event_type, {})


_KNOWN_EVENT_KEYS = {
    "purpose", "spec_source", "units", "expected_scenes", "required_data_fields",
    "optional_data_fields", "conditional_fields", "allowed_values", "field_types",
    "high_frequency", "continuous", "pairing", "start_finish", "event_key",
    "semantics", "known_issues", "notes",
}


def load_expectations(path: Optional[str]) -> Expectations:
    """Read event_expectations.yaml; unknown keys produce warnings, not errors."""
    exp = Expectations(path=str(path) if path else "")
    if not path:
        return exp
    p = Path(path)
    if not p.is_file():
        exp.warnings.append(f"expectations config not found: {p}")
        return exp
    try:
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        exp.warnings.append(f"could not parse {p}: {e}")
        return exp
    if not isinstance(doc, dict):
        exp.warnings.append(f"{p}: top level must be a mapping")
        return exp
    exp.meta = doc.get("meta") or {}
    exp.cross_event_rules = doc.get("cross_event_rules") or []
    exp.thresholds = {**DEFAULT_THRESHOLDS, **(doc.get("thresholds") or {})}
    events = doc.get("events") or {}
    if not isinstance(events, dict):
        exp.warnings.append(f"{p}: 'events' must be a mapping of eventType -> rules")
        events = {}
    for et, rules in events.items():
        rules = rules or {}
        if not isinstance(rules, dict):
            exp.warnings.append(f"{p}: rules for {et!r} must be a mapping — ignored")
            continue
        for k in rules:
            if k not in _KNOWN_EVENT_KEYS:
                exp.warnings.append(f"{p}: {et}: unknown rule key {k!r} (typo?)")
        exp.events[et] = rules
    return exp


# ---------------------------------------------------------------- coverage --

COMPLETE, PARTIAL, SKIPPED, UNKNOWN = "complete", "partial", "skipped", "unknown"


@dataclass
class Coverage:
    """Per-unit playthrough coverage. `inferred` marks manifest-less runs."""

    build: str = ""
    tested_content: Dict[str, str] = field(default_factory=dict)  # "Unit1" -> status
    notes: List[str] = field(default_factory=list)
    inferred: bool = False
    path: str = ""
    warnings: List[str] = field(default_factory=list)

    def unit_status(self, unit: int) -> str:
        return self.tested_content.get(f"Unit{unit}", UNKNOWN)

    def units_tested(self, units: List[int]) -> bool:
        """True if at least one of the listed units was (even partially) played."""
        return any(self.unit_status(u) in (COMPLETE, PARTIAL) for u in units)

    def all_skipped(self, units: List[int]) -> bool:
        return bool(units) and all(self.unit_status(u) == SKIPPED for u in units)


_VALID_STATUSES = {COMPLETE, PARTIAL, SKIPPED}


def load_coverage(path: Optional[str]) -> Optional[Coverage]:
    """Load a coverage manifest; None when no path was given / file missing."""
    if not path:
        return None
    p = Path(path)
    if not p.is_file():
        return None
    cov = Coverage(path=str(p))
    try:
        doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        cov.warnings.append(f"could not parse {p}: {e}")
        return cov
    cov.build = str(doc.get("build", ""))
    cov.notes = [str(n) for n in (doc.get("notes") or [])]
    for unit, status in (doc.get("tested_content") or {}).items():
        status = str(status).lower()
        if status not in _VALID_STATUSES:
            cov.warnings.append(
                f"{p}: {unit}: status {status!r} not one of {sorted(_VALID_STATUSES)}")
        cov.tested_content[str(unit)] = status
    return cov


def infer_coverage(scene_units: Dict[str, List[int]], build_id: str) -> Coverage:
    """Cautious fallback when no manifest exists: a unit whose scenes appear in
    the log is marked 'partial' (we cannot know it was completed), everything
    else 'unknown'. The report labels this as an inference."""
    cov = Coverage(build=build_id, inferred=True)
    seen = sorted({u for units in scene_units.values() for u in units})
    for u in seen:
        cov.tested_content[f"Unit{u}"] = PARTIAL
    cov.notes.append(
        "coverage inferred from observed sceneName values only — no manifest supplied")
    return cov


def scene_to_units(scene: str) -> List[int]:
    """Extract game unit number(s) from a scene name like 'Unit 3 Dungeon Dev'."""
    import re
    return [int(m) for m in re.findall(r"[Uu]nit\s*(\d+)", scene or "")]
