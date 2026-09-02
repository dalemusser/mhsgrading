"""Temporal, scene-level, and sequence analysis (Steps 10-11).

* scene timeline: contiguous same-scene runs per session, with durations;
* ordering diagnostics: client-timestamp vs _id disagreement and
  client-vs-server clock skew (reported as INFO, not as defects);
* config-driven sequence checks: open/close `pairing` rules and
  start/finish `start_finish` rules, optionally grouped by a data field
  (e.g. per pieceId or per questID). No rule in config -> no check.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .model import Finding, Rec, fmt_seconds, INFO, PASS, WARNING, LOW, MEDIUM, SEV_INFO


def get_path(data, dotted: str):
    """Fetch a dotted path (without the leading 'data.') from a payload."""
    cur = data
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


@dataclass
class SceneRun:
    session_id: str
    scene: str
    first_ts: object
    last_ts: object
    n_events: int = 0
    event_types: Dict[str, int] = field(default_factory=dict)
    first_ref: str = ""
    last_ref: str = ""

    @property
    def duration_s(self) -> Optional[float]:
        if self.first_ts and self.last_ts:
            return (self.last_ts - self.first_ts).total_seconds()
        return None

    def to_row(self) -> dict:
        return {
            "session": self.session_id,
            "sceneName": self.scene,
            "first_timestamp": self.first_ts.isoformat() if self.first_ts else "",
            "last_timestamp": self.last_ts.isoformat() if self.last_ts else "",
            "duration": fmt_seconds(self.duration_s),
            "duration_s": round(self.duration_s, 1) if self.duration_s is not None else "",
            "n_events": self.n_events,
            "event_types": "; ".join(f"{k}:{v}" for k, v in
                                     sorted(self.event_types.items())),
        }


def scene_timeline(records: List[Rec]) -> List[SceneRun]:
    """Contiguous same-scene runs in chronological order, per session."""
    runs: List[SceneRun] = []
    current: Dict[str, SceneRun] = {}
    for rec in records:
        scene = rec.scene or "<missing sceneName>"
        run = current.get(rec.session_id)
        if run is None or run.scene != scene:
            run = SceneRun(session_id=rec.session_id, scene=scene,
                           first_ts=rec.ts, last_ts=rec.ts,
                           first_ref=rec.ref(), last_ref=rec.ref())
            runs.append(run)
            current[rec.session_id] = run
        run.n_events += 1
        run.event_types[rec.event_type or "?"] = \
            run.event_types.get(rec.event_type or "?", 0) + 1
        if rec.ts is not None:
            if run.first_ts is None or rec.ts < run.first_ts:
                run.first_ts = rec.ts
            if run.last_ts is None or rec.ts > run.last_ts:
                run.last_ts, run.last_ref = rec.ts, rec.ref()
    return runs


def timeline_findings(runs: List[SceneRun]) -> List[Finding]:
    findings: List[Finding] = []
    # single-event "flickers": one lone record of scene B sandwiched between
    # runs of the same scene A — possible scene-attribution glitch.
    for i in range(1, len(runs) - 1):
        a, b, c = runs[i - 1], runs[i], runs[i + 1]
        if (b.n_events == 1 and a.scene == c.scene and b.scene != a.scene
                and a.session_id == b.session_id == c.session_id
                and b.scene not in ("Transition", "MainMenu")):
            findings.append(Finding(
                status=WARNING, severity=LOW, category="temporal",
                summary="single event attributed to a different scene between "
                        "two runs of the same scene",
                observed=f"1 {list(b.event_types)[0]} record in {b.scene!r} "
                         f"inside a {a.scene!r} period",
                expected="scene-consistent attribution (or a real quick scene hop)",
                examples=[b.first_ref],
            ))
    return findings


def ordering_findings(records: List[Rec]) -> List[Finding]:
    """INFO diagnostics on record ordering and clock skew."""
    findings: List[Finding] = []
    with_oid = [r for r in records if r.oid and r.ts]
    by_oid = sorted(with_oid, key=lambda r: r.oid)
    inversions = 0
    worst = None
    for a, b in zip(by_oid, by_oid[1:]):
        if b.ts < a.ts:
            inversions += 1
            d = (a.ts - b.ts).total_seconds()
            if worst is None or d > worst[0]:
                worst = (d, a.ref(), b.ref())
    if inversions:
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="temporal",
            summary="_id (arrival) order disagrees with client-timestamp order",
            observed=f"{inversions} of {max(len(by_oid) - 1, 1)} adjacent _id pairs "
                     f"reverse in client time; worst {worst[0]:.1f}s",
            expected="expected for batched uploads; audits sort by client timestamp",
            examples=[worst[1], worst[2]],
        ))
    skews = sorted((r.ts - r.server_ts).total_seconds()
                   for r in records if r.ts and r.server_ts)
    if skews:
        mid = skews[len(skews) // 2]
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="temporal",
            summary="client vs server timestamp skew",
            observed=f"median {mid:+.2f}s, min {skews[0]:+.2f}s, "
                     f"max {skews[-1]:+.2f}s over {len(skews)} records",
            expected="small constant skew; large negatives = delayed uploads",
        ))
    no_ts = [r for r in records if r.ts is None]
    if no_ts:
        findings.append(Finding(
            status=WARNING, severity=MEDIUM, category="temporal",
            summary="records without a parseable client timestamp",
            observed=f"{len(no_ts)} records",
            examples=[r.ref() for r in no_ts[:3]],
        ))
    return findings


def _sequence_check(prof_records: List[Rec], rule: dict, kind: str,
                    event_type: str, spec: str) -> List[Finding]:
    """Shared engine for `pairing` (open/close) and `start_finish` rules."""
    fld = rule.get("field", "actionType")
    if kind == "pairing":
        open_v, close_v = rule.get("open_value"), rule.get("close_value")
        open_name, close_name = "open", "close"
    else:
        open_v, close_v = rule.get("start_value"), rule.get("finish_value")
        open_name, close_name = "start", "finish"
    group_by = rule.get("group_by")
    label = rule.get("label") or f"{open_v}/{close_v}"

    depth: Dict[tuple, int] = {}
    close_without_open: List[Rec] = []
    repeated_open: List[Rec] = []
    opens = closes = 0
    last_open: Dict[tuple, Rec] = {}
    for rec in prof_records:
        v = get_path(rec.data, fld)
        if v not in (open_v, close_v):
            continue
        g = (rec.session_id, str(get_path(rec.data, group_by)) if group_by else "")
        d = depth.get(g, 0)
        if v == open_v:
            opens += 1
            if d > 0 and kind == "pairing":
                repeated_open.append(rec)
            depth[g] = d + 1
            last_open[g] = rec
        else:
            closes += 1
            if d <= 0:
                close_without_open.append(rec)
            depth[g] = max(d - 1, 0)

    findings: List[Finding] = []
    unclosed = sum(v for v in depth.values() if v > 0)
    if close_without_open:
        findings.append(Finding(
            status=WARNING, severity=MEDIUM, category="sequence",
            event_type=event_type, fld=fld,
            summary=f"{label}: {close_name} without preceding {open_name}",
            observed=f"{len(close_without_open)} occurrence(s)",
            expected=f"every {close_v!r} preceded by {open_v!r}"
                     + (f" per {group_by}" if group_by else ""),
            examples=[r.ref() for r in close_without_open[:3]],
            spec_source=spec))
    if repeated_open:
        findings.append(Finding(
            status=WARNING, severity=LOW, category="sequence",
            event_type=event_type, fld=fld,
            summary=f"{label}: repeated {open_name} with no intervening {close_name}",
            observed=f"{len(repeated_open)} occurrence(s)",
            examples=[r.ref() for r in repeated_open[:3]],
            spec_source=spec))
    if unclosed:
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="sequence",
            event_type=event_type, fld=fld,
            summary=f"{label}: {open_name}(s) never {close_name}d "
                    "(may be legitimate at session end)",
            observed=f"{unclosed} unmatched {open_v!r} "
                     f"(totals: {opens} {open_name}, {closes} {close_name})",
            spec_source=spec))
    if not (close_without_open or repeated_open or unclosed) and (opens or closes):
        findings.append(Finding(
            status=PASS, severity=SEV_INFO, category="sequence",
            event_type=event_type, fld=fld,
            summary=f"{label}: {open_name}/{close_name} events pair correctly",
            observed=f"{opens} {open_name} / {closes} {close_name}",
            spec_source=spec))
    return findings


def sequence_findings(profiles, expectations) -> List[Finding]:
    findings: List[Finding] = []
    if not expectations:
        return findings
    for et in sorted(profiles):
        prof = profiles[et]
        rules = expectations.for_event(et)
        spec = rules.get("spec_source", "")
        for rule in rules.get("pairing") or []:
            findings.extend(_sequence_check(prof.records, rule, "pairing", et, spec))
        for rule in rules.get("start_finish") or []:
            findings.extend(_sequence_check(prof.records, rule, "start_finish", et, spec))
    return findings
