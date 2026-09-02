"""Expectation-driven QA checks (Steps 6-8, 12-13) — everything here is
driven by event_expectations.yaml plus the coverage manifest; there is no
event-specific Python.

Key principle: absence of an event is NOT automatically a failure. When an
expected event type is missing, the coverage manifest decides between
NOT_TESTED (content skipped) and WARNING (content played, event absent).
Unexpected values are surfaced as INFO / "specification review required",
never hidden and never auto-normalized.
"""

from __future__ import annotations

from typing import Dict, List

from .config import Coverage, Expectations, scene_to_units
from .model import (Finding, FAIL, INFO, NOT_TESTED, PASS, WARNING,
                    HIGH, LOW, MEDIUM, SEV_INFO, SEV_NOT_TESTED)
from .profiling import EventProfile, fmt_value
from .temporal import get_path


def _units_for_event(rules: dict) -> List[int]:
    units = rules.get("units")
    if units:
        return [int(u) for u in units]
    inferred = sorted({u for sc in rules.get("expected_scenes") or []
                       for u in scene_to_units(sc)})
    return inferred


def _fmt_when(when: dict) -> str:
    return ", ".join(f"{k}={v!r}" for k, v in sorted(when.items()))


def _matches(data, where: dict) -> bool:
    """`where` values may be scalars (equality) or lists (membership)."""
    for k, v in (where or {}).items():
        actual = get_path(data, k)
        if isinstance(v, list):
            if actual not in v:
                return False
        elif actual != v:
            return False
    return True


def expectation_findings(profiles: Dict[str, EventProfile],
                         expectations: Expectations,
                         coverage: Coverage) -> List[Finding]:
    findings: List[Finding] = []

    # --- events with rules -------------------------------------------------
    for et in sorted(expectations.events):
        rules = expectations.events[et]
        spec = rules.get("spec_source", "")
        prof = profiles.get(et)

        if prof is None:
            units = _units_for_event(rules)
            if units and coverage.all_skipped(units):
                findings.append(Finding(
                    status=NOT_TESTED, severity=SEV_NOT_TESTED, category="coverage",
                    event_type=et,
                    summary="expected event type absent, but its content was "
                            "not exercised this playthrough",
                    expected=f"appears in Unit(s) {units}",
                    evidence=f"coverage manifest: {[coverage.unit_status(u) for u in units]}",
                    spec_source=spec))
            elif units and coverage.units_tested(units):
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="coverage",
                    event_type=et,
                    summary="expected event type absent although its content "
                            "was played — possible logging failure",
                    expected=f"appears in Unit(s) {units}",
                    evidence="coverage: " + ", ".join(
                        f"Unit{u}={coverage.unit_status(u)}" for u in units)
                        + ("; coverage inferred from scenes"
                           if coverage.inferred else ""),
                    spec_source=spec))
            else:
                findings.append(Finding(
                    status=NOT_TESTED, severity=SEV_NOT_TESTED, category="coverage",
                    event_type=et,
                    summary="expected event type absent; coverage for its "
                            "content is unknown",
                    expected="declare `units:` for this event or update the "
                             "coverage manifest to resolve",
                    spec_source=spec))
            continue

        # scenes ------------------------------------------------------------
        exp_scenes = rules.get("expected_scenes")
        if exp_scenes:
            unexpected = sorted(sc for sc in prof.scenes if sc not in exp_scenes)
            if unexpected:
                findings.append(Finding(
                    status=INFO, severity=SEV_INFO, category="scenes", event_type=et,
                    summary="event observed in scene(s) not listed in the "
                            "specification — specification review required",
                    observed="; ".join(f"{sc} ({prof.scenes[sc]} records)"
                                       for sc in unexpected),
                    expected="; ".join(sorted(exp_scenes)), spec_source=spec))
            missing = sorted(sc for sc in exp_scenes if sc not in prof.scenes)
            for sc in missing:
                units = scene_to_units(sc)
                if units and coverage.all_skipped(units):
                    status, sev = NOT_TESTED, SEV_NOT_TESTED
                    note = "scene's unit skipped this playthrough"
                else:
                    status, sev = INFO, SEV_INFO
                    note = ("unit played but event not seen there — may be "
                            "normal (activity not repeated) or a gap")
                findings.append(Finding(
                    status=status, severity=sev, category="scenes", event_type=et,
                    summary=f"expected scene {sc!r} has no records of this event",
                    expected=sc, evidence=note, spec_source=spec))
            both = sorted(sc for sc in prof.scenes if sc in exp_scenes)
            if both and not unexpected:
                findings.append(Finding(
                    status=PASS, severity=SEV_INFO, category="scenes", event_type=et,
                    summary="all observed scenes match the specification",
                    observed="; ".join(both), spec_source=spec))

        # required fields ---------------------------------------------------
        for path in rules.get("required_data_fields") or []:
            missing = [r for r in prof.records
                       if get_path(r.data, path) is None]
            if missing:
                findings.append(Finding(
                    status=FAIL, severity=HIGH, category="schema", event_type=et,
                    fld=f"data.{path}",
                    summary="required field missing or null in some records",
                    observed=f"{len(missing)} of {prof.count} records lack "
                             f"data.{path}",
                    expected=f"data.{path} present in every record",
                    examples=[r.ref() for r in missing[:3]], spec_source=spec))
            else:
                findings.append(Finding(
                    status=PASS, severity=SEV_INFO, category="schema", event_type=et,
                    fld=f"data.{path}",
                    summary="required field present in all records",
                    observed=f"{prof.count} of {prof.count}", spec_source=spec))

        # conditional fields ------------------------------------------------
        for path, cond in (rules.get("conditional_fields") or {}).items():
            when = cond.get("when") or {}
            applicable = [r for r in prof.records if _matches(r.data, when)]
            if cond.get("required", True):
                missing = [r for r in applicable if get_path(r.data, path) is None]
                if missing:
                    findings.append(Finding(
                        status=FAIL, severity=HIGH, category="schema", event_type=et,
                        fld=f"data.{path}",
                        summary=f"conditionally required field missing "
                                f"(when {_fmt_when(when)})",
                        observed=f"{len(missing)} of {len(applicable)} applicable "
                                 "records lack it",
                        examples=[r.ref() for r in missing[:3]], spec_source=spec))
                elif applicable:
                    findings.append(Finding(
                        status=PASS, severity=SEV_INFO, category="schema",
                        event_type=et, fld=f"data.{path}",
                        summary=f"conditional field present when {_fmt_when(when)}",
                        observed=f"{len(applicable)} applicable records",
                        spec_source=spec))
            if cond.get("forbidden_otherwise"):
                stray = [r for r in prof.records
                         if not _matches(r.data, when)
                         and get_path(r.data, path) is not None]
                if stray:
                    findings.append(Finding(
                        status=WARNING, severity=MEDIUM, category="schema",
                        event_type=et, fld=f"data.{path}",
                        summary=f"field present although condition "
                                f"({_fmt_when(when)}) does not hold",
                        observed=f"{len(stray)} record(s)",
                        examples=[r.ref() for r in stray[:3]], spec_source=spec))

        # allowed values ----------------------------------------------------
        for path, allowed in (rules.get("allowed_values") or {}).items():
            fp = prof.fields.get(f"data.{path}")
            if fp is None:
                continue
            allowed_strs = {str(v) for v in allowed}
            new = sorted((t, s) for (t, s) in fp.values
                         if s not in allowed_strs and t != "null")
            if new:
                findings.append(Finding(
                    status=INFO, severity=SEV_INFO, category="values", event_type=et,
                    fld=f"data.{path}",
                    summary="value(s) not in the current specification — "
                            "specification review required",
                    observed="; ".join(
                        f"{fmt_value(t, s)} ({fp.values[(t, s)]}x)" for t, s in new),
                    expected=", ".join(str(v) for v in allowed),
                    spec_source=spec))
            unseen = sorted(v for v in allowed_strs
                            if not any(s == v for (_, s) in fp.values))
            if unseen:
                findings.append(Finding(
                    status=INFO, severity=SEV_INFO, category="values", event_type=et,
                    fld=f"data.{path}",
                    summary="specified value(s) never observed this build",
                    observed=f"absent: {', '.join(unseen)}",
                    expected="may be normal if that interaction was not used",
                    spec_source=spec))
            if not new:
                findings.append(Finding(
                    status=PASS, severity=SEV_INFO, category="values", event_type=et,
                    fld=f"data.{path}",
                    summary="all observed values are within the specification",
                    observed="; ".join(
                        f"{fmt_value(t, s)} ({c}x)"
                        for (t, s), c in sorted(fp.values.items())),
                    spec_source=spec))

        # field types -------------------------------------------------------
        for path, expected_type in (rules.get("field_types") or {}).items():
            fp = prof.fields.get(f"data.{path}")
            if fp is None:
                continue
            observed_types = {t for t in fp.types if t != "null"}
            if observed_types and observed_types != {expected_type}:
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="schema", event_type=et,
                    fld=f"data.{path}",
                    summary="field type differs from specification",
                    observed=", ".join(sorted(observed_types)),
                    expected=expected_type, spec_source=spec))

        # eventKey ----------------------------------------------------------
        ek = rules.get("event_key")
        if ek:
            when = ek.get("required_when")
            applicable = [r for r in prof.records
                          if (when is None and ek.get("required"))
                          or (when is not None and _matches(r.data, when))]
            missing = [r for r in applicable if r.event_key is None]
            if missing:
                findings.append(Finding(
                    status=FAIL, severity=HIGH, category="schema", event_type=et,
                    fld="eventKey",
                    summary="eventKey missing on records that require it",
                    observed=f"{len(missing)} of {len(applicable)} applicable records",
                    examples=[r.ref() for r in missing[:3]], spec_source=spec))
            fmt = ek.get("format")
            if fmt:
                bad = []
                for r in applicable:
                    if r.event_key is None:
                        continue
                    try:
                        expect = fmt.format(**{
                            "data": _DotDict(r.data if isinstance(r.data, dict) else {})})
                    except (KeyError, AttributeError):
                        continue
                    if r.event_key != expect:
                        bad.append((r, expect))
                if bad:
                    findings.append(Finding(
                        status=WARNING, severity=MEDIUM, category="schema",
                        event_type=et, fld="eventKey",
                        summary="eventKey does not match its documented format",
                        observed=f"{len(bad)} mismatch(es); e.g. "
                                 f"{bad[0][0].event_key!r} vs expected {bad[0][1]!r}",
                        expected=fmt,
                        examples=[r.ref() for r, _ in bad[:3]], spec_source=spec))
                elif applicable:
                    findings.append(Finding(
                        status=PASS, severity=SEV_INFO, category="schema",
                        event_type=et, fld="eventKey",
                        summary="eventKey matches its documented format",
                        observed=f"{len(applicable)} records checked",
                        expected=fmt, spec_source=spec))

        # semantics: can the intended question be answered from the fields? --
        for sem in rules.get("semantics") or []:
            needed = sem.get("satisfied_by") or []
            have = [p for p in needed if f"data.{p}" in prof.fields]
            if len(have) == len(needed):
                findings.append(Finding(
                    status=PASS, severity=SEV_INFO, category="semantics",
                    event_type=et,
                    summary=f"sufficient information: {sem.get('question', '')}",
                    observed="fields present: " + ", ".join(needed),
                    spec_source=spec))
            else:
                lack = sorted(set(needed) - set(have))
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="semantics",
                    event_type=et,
                    summary=f"insufficient information: {sem.get('question', '')}",
                    observed=f"missing fields: {', '.join(lack)}",
                    expected=", ".join(needed), spec_source=spec))

        # known issues from previous builds --------------------------------
        for issue in rules.get("known_issues") or []:
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="semantics", event_type=et,
                summary=f"known issue (tracked in config): {issue}",
                expected="verify whether it still occurs in this build "
                         "(see schema/values findings)", spec_source=spec))

    # --- events without rules ---------------------------------------------
    for et in sorted(profiles):
        if et not in expectations.events:
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="coverage", event_type=et,
                summary="no expectation rules configured — descriptive "
                        "profiling only",
                observed=f"{profiles[et].count} records",
                expected="add the event to event_expectations.yaml to enable "
                         "expectation checks"))
    return findings


class _DotDict(dict):
    """Lets '{data.questID}'-style templates work with str.format."""

    def __getattr__(self, name):
        v = self.get(name)
        return _DotDict(v) if isinstance(v, dict) else v


def cross_event_findings(profiles: Dict[str, EventProfile],
                         expectations: Expectations) -> List[Finding]:
    """`cross_event_rules`: if events matching `if` exist in a session, events
    matching `expect` must exist there too."""
    findings: List[Finding] = []
    sessions = sorted({s for p in profiles.values() for s in p.sessions})
    for rule in expectations.cross_event_rules:
        cond, expect = rule.get("if") or {}, rule.get("expect") or {}
        label = rule.get("label", "cross-event rule")
        spec = rule.get("spec_source", "")
        cond_prof = profiles.get(cond.get("event_type", ""))
        exp_prof = profiles.get(expect.get("event_type", ""))
        for sess in sessions:
            triggers = [r for r in (cond_prof.records if cond_prof else [])
                        if r.session_id == sess and _matches(r.data, cond.get("where"))]
            if not triggers:
                continue
            matches = [r for r in (exp_prof.records if exp_prof else [])
                       if r.session_id == sess and _matches(r.data, expect.get("where"))]
            if matches:
                findings.append(Finding(
                    status=PASS, severity=SEV_INFO, category="cross-event",
                    summary=f"{label}: consistent",
                    observed=f"{len(triggers)} trigger(s), {len(matches)} "
                             f"matching record(s) in {sess}", spec_source=spec))
            else:
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="cross-event",
                    summary=f"{label}: expected corroborating events not found",
                    observed=f"{len(triggers)} record(s) match the trigger in "
                             f"{sess}, none match the expectation",
                    expected=f"{expect.get('event_type')} with "
                             f"{expect.get('where') or 'any data'}",
                    examples=[r.ref() for r in triggers[:3]], spec_source=spec))
    return findings
