"""Build-over-build regression analysis (Steps 14-15).

Every audit run writes a normalized `snapshot.json` into its report folder.
A later run can point `--baseline` at that folder (or directly at a
snapshot.json, or at a previous build's raw logs) and gets a diff of event
types, scenes, schemas, categorical values, volumes and cadence.

Differences are reported as *regression candidates requiring review*, never
automatically as defects — a redesign and a logging bug look identical here.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .model import Finding, INFO, WARNING, LOW, MEDIUM, SEV_INFO
from .profiling import EventProfile

SNAPSHOT_VALUE_CAP = 60      # categorical value lists larger than this are
                             # stored truncated and excluded from value diffs
COUNT_RATIO_FLAG = 3.0       # volume change ratio that gets flagged
CADENCE_RATIO_FLAG = 2.0     # median-interval change ratio that gets flagged


def build_snapshot(build_id: str, profiles: Dict[str, EventProfile],
                   interval_stats, load_result, created: str) -> dict:
    events = {}
    for et in sorted(profiles):
        p = profiles[et]
        fields = {}
        values = {}
        for path in sorted(p.fields):
            fp = p.fields[path]
            fields[path] = {"count": fp.count,
                            "types": sorted(t for t in fp.types)}
            if fp.values and not fp.values_truncated \
                    and len(fp.values) <= SNAPSHOT_VALUE_CAP:
                only_strings = all(t == "string" for (t, _) in fp.values)
                if only_strings or all(t in ("string", "bool") for (t, _) in fp.values):
                    values[path] = sorted(s for (_, s) in fp.values)
        st = interval_stats.get(et)
        events[et] = {
            "count": p.count,
            "scenes": {sc: n for sc, n in sorted(p.scenes.items())},
            "fields": fields,
            "values": values,
            "median_interval_s": round(st.median, 3)
            if st and st.n_intervals else None,
        }
    scenes: Dict[str, int] = {}
    for p in profiles.values():
        for sc, n in p.scenes.items():
            scenes[sc] = scenes.get(sc, 0) + n
    return {
        "snapshot_format": 1,
        "build_id": build_id,
        "created": created,
        "source_files": list(load_result.files),
        "game_versions": load_result.versions,
        "record_count": len(load_result.records),
        "session_count": len(load_result.sessions),
        "scenes": dict(sorted(scenes.items())),
        "event_types": events,
    }


def load_baseline(path: str) -> Tuple[Optional[dict], str]:
    """Accepts a report folder, a snapshot.json, or a raw-log file/folder.
    Returns (snapshot dict or None, note)."""
    p = Path(path)
    if p.is_dir():
        snap = p / "snapshot.json"
        if snap.is_file():
            return json.loads(snap.read_text(encoding="utf-8")), f"snapshot {snap}"
        json_files = [f for f in p.iterdir() if f.suffix.lower() == ".json"]
        if json_files:
            return _snapshot_from_raw(str(p)), f"raw logs in {p} (profiled on the fly)"
        return None, f"no snapshot.json or logs found in {p}"
    if p.is_file():
        if p.name == "snapshot.json":
            return json.loads(p.read_text(encoding="utf-8")), f"snapshot {p}"
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None, f"{p} is not JSON"
        if isinstance(doc, dict) and doc.get("snapshot_format"):
            return doc, f"snapshot {p}"
        return _snapshot_from_raw(str(p)), f"raw log {p} (profiled on the fly)"
    return None, f"baseline path not found: {p}"


def _snapshot_from_raw(path: str) -> dict:
    from .loader import load_logs
    from .profiling import build_profiles
    from .frequency import compute_interval_stats
    from .config import Expectations
    lr = load_logs(path)
    profiles = build_profiles(lr.records)
    stats = compute_interval_stats(profiles, {}, Expectations())
    return build_snapshot(Path(path).name, profiles, stats, lr, created="")


def _ratio(new: float, old: float) -> Optional[float]:
    if old <= 0 or new <= 0:
        return None
    return new / old


def diff_snapshots(current: dict, baseline: dict):
    """Returns (findings, diff_rows) — rows feed regression_diff.csv."""
    findings: List[Finding] = []
    rows: List[dict] = []
    base_id = baseline.get("build_id", "baseline")
    cur_ev = current.get("event_types", {})
    base_ev = baseline.get("event_types", {})

    def row(kind, event_type, item, base_val, cur_val):
        rows.append({"change": kind, "eventType": event_type, "item": item,
                     "baseline": str(base_val), "current": str(cur_val)})

    new_types = sorted(set(cur_ev) - set(base_ev))
    gone_types = sorted(set(base_ev) - set(cur_ev))
    for et in new_types:
        row("new_event_type", et, "", "-", cur_ev[et]["count"])
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="regression", event_type=et,
            summary=f"event type not present in baseline {base_id}",
            observed=f"{cur_ev[et]['count']} records this build",
            expected="new logging or newly exercised content — review"))
    for et in gone_types:
        row("removed_event_type", et, "", base_ev[et]["count"], "-")
        findings.append(Finding(
            status=WARNING, severity=MEDIUM, category="regression", event_type=et,
            summary=f"event type present in baseline {base_id} but absent now",
            observed="0 records this build",
            expected=f"{base_ev[et]['count']} records in baseline; check "
                     "coverage before treating as a logging regression"))

    new_scenes = sorted(set(current.get("scenes", {})) - set(baseline.get("scenes", {})))
    gone_scenes = sorted(set(baseline.get("scenes", {})) - set(current.get("scenes", {})))
    if new_scenes:
        row("new_scenes", "", "; ".join(new_scenes), "-", "")
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="regression",
            summary="scene name(s) not present in baseline",
            observed="; ".join(new_scenes),
            expected="renamed scene, new content, or new coverage"))
    if gone_scenes:
        row("removed_scenes", "", "; ".join(gone_scenes), "", "-")
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="regression",
            summary="baseline scene name(s) absent this build",
            observed="; ".join(gone_scenes),
            expected="renamed scene, removed content, or reduced coverage"))

    for et in sorted(set(cur_ev) & set(base_ev)):
        c, b = cur_ev[et], base_ev[et]
        r = _ratio(c["count"], b["count"])
        if r is not None and (r >= COUNT_RATIO_FLAG or r <= 1 / COUNT_RATIO_FLAG):
            row("volume_change", et, "record_count", b["count"], c["count"])
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="regression", event_type=et,
                summary=f"record volume changed {r:.1f}x vs baseline",
                observed=f"{c['count']} records", expected=f"{b['count']} in {base_id}",
                evidence="regression candidate: gameplay length, coverage, or "
                         "logging-rate change"))
        cm, bm = c.get("median_interval_s"), b.get("median_interval_s")
        rr = _ratio(cm or 0, bm or 0)
        if rr is not None and (rr >= CADENCE_RATIO_FLAG or rr <= 1 / CADENCE_RATIO_FLAG):
            row("cadence_change", et, "median_interval_s", bm, cm)
            findings.append(Finding(
                status=WARNING, severity=MEDIUM, category="regression", event_type=et,
                summary="median interval between records changed substantially",
                observed=f"{cm}s median", expected=f"{bm}s in {base_id}",
                evidence="regression candidate requiring review"))

        new_fields = sorted(set(c["fields"]) - set(b["fields"]))
        gone_fields = sorted(set(b["fields"]) - set(c["fields"]))
        for f in new_fields:
            row("new_field", et, f, "-", c["fields"][f]["count"])
        for f in gone_fields:
            row("removed_field", et, f, b["fields"][f]["count"], "-")
        if new_fields:
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="regression", event_type=et,
                summary="field(s) not present in baseline schema",
                observed="; ".join(new_fields)))
        if gone_fields:
            findings.append(Finding(
                status=WARNING, severity=MEDIUM, category="regression", event_type=et,
                summary="baseline field(s) absent this build",
                observed="; ".join(gone_fields),
                expected="schema change or conditional content — review"))
        for f in sorted(set(c["fields"]) & set(b["fields"])):
            ct = [t for t in c["fields"][f]["types"] if t != "null"]
            bt = [t for t in b["fields"][f]["types"] if t != "null"]
            if ct and bt and set(ct) != set(bt):
                row("type_change", et, f, "/".join(bt), "/".join(ct))
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="regression",
                    event_type=et, fld=f,
                    summary="field type changed vs baseline",
                    observed="/".join(ct), expected="/".join(bt)))
        for f in sorted(set(c.get("values", {})) & set(b.get("values", {}))):
            cv, bv = set(c["values"][f]), set(b["values"][f])
            newv, gonev = sorted(cv - bv), sorted(bv - cv)
            if newv:
                row("new_values", et, f, "", "; ".join(newv))
                findings.append(Finding(
                    status=INFO, severity=SEV_INFO, category="regression",
                    event_type=et, fld=f,
                    summary="categorical value(s) not seen in baseline",
                    observed="; ".join(newv),
                    expected="new design, renamed value, or new coverage — review"))
            if gonev:
                row("removed_values", et, f, "; ".join(gonev), "")
                findings.append(Finding(
                    status=INFO, severity=SEV_INFO, category="regression",
                    event_type=et, fld=f,
                    summary="baseline categorical value(s) not seen this build",
                    observed="; ".join(gonev),
                    expected="may simply not have been exercised — review"))
    if not findings:
        findings.append(Finding(
            status=INFO, severity=SEV_INFO, category="regression",
            summary=f"no structural differences vs baseline {base_id} detected"))
    return findings, rows
