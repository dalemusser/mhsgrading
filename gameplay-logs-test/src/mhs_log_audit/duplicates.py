"""Duplicate / suspicious record detection (Step 17).

* exact duplicates: identical (eventType, sceneName, timestamp, data, user)
  — only _id/serverTimestamp may differ;
* near-duplicates: identical (eventType, sceneName, data, user) within a small
  time window. Event types marked `high_frequency: true` in the expectations
  config (key presses, position snapshots) are exempt from the near-duplicate
  rule, because rapid identical records are normal for them.

Suspicious records are exported for inspection; source logs are never touched.
"""

from __future__ import annotations

import json
from typing import Dict, List

from .model import Finding, Rec, INFO, WARNING, MEDIUM, SEV_INFO
from .profiling import EventProfile

EXPORT_CAP = 200  # rows exported per detector


def _data_key(rec: Rec) -> str:
    try:
        return json.dumps(rec.data, sort_keys=True, ensure_ascii=False)
    except TypeError:
        return repr(rec.data)


def find_duplicates(profiles: Dict[str, EventProfile], thresholds: dict,
                    expectations):
    """Returns (findings, duplicate_rows) — rows go to duplicate_events.csv."""
    near_s = float(thresholds.get("near_duplicate_seconds", 1.0))
    findings: List[Finding] = []
    rows: List[dict] = []

    for et in sorted(profiles):
        prof = profiles[et]
        rules = expectations.for_event(et) if expectations else {}
        exact: Dict[tuple, List[Rec]] = {}
        for rec in prof.records:
            key = (rec.scene, rec.raw.get("timestamp"), _data_key(rec), rec.user_id)
            exact.setdefault(key, []).append(rec)
        exact_groups = {k: v for k, v in exact.items() if len(v) > 1}
        if exact_groups:
            n_extra = sum(len(v) - 1 for v in exact_groups.values())
            examples = []
            for v in list(exact_groups.values())[:3]:
                examples.append(" == ".join(r.ref() for r in v[:2]))
            findings.append(Finding(
                status=WARNING, severity=MEDIUM, category="duplicates",
                event_type=et,
                summary="exact duplicate records (same timestamp, scene and data)",
                observed=f"{len(exact_groups)} group(s), {n_extra} redundant record(s)",
                expected="each gameplay moment logged once",
                examples=examples))
            for v in exact_groups.values():
                for r in v:
                    if len(rows) < EXPORT_CAP:
                        rows.append({"kind": "exact", "eventType": et,
                                     "ref": r.ref(), "scene": r.scene or "",
                                     "data": _data_key(r)[:300]})

        if rules.get("high_frequency"):
            continue
        near: List[tuple] = []
        last_seen: Dict[tuple, Rec] = {}
        for rec in prof.records:
            if rec.ts is None:
                continue
            key = (rec.scene, _data_key(rec), rec.user_id)
            prev = last_seen.get(key)
            if prev is not None and prev.raw.get("timestamp") != rec.raw.get("timestamp"):
                d = (rec.ts - prev.ts).total_seconds()
                if 0 <= d <= near_s:
                    near.append((d, prev, rec))
            last_seen[key] = rec
        if near:
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="duplicates",
                event_type=et,
                summary=f"near-duplicate records within {near_s:g}s "
                        "(identical data, different timestamp)",
                observed=f"{len(near)} pair(s)",
                expected="review whether the interaction really fired twice",
                examples=[f"{d * 1000:.0f}ms: {a.ref()} ~ {b.ref()}"
                          for d, a, b in near[:3]]))
            for d, a, b in near:
                if len(rows) < EXPORT_CAP:
                    rows.append({"kind": "near", "eventType": et,
                                 "ref": f"{a.ref()} ~ {b.ref()} ({d * 1000:.0f}ms)",
                                 "scene": a.scene or "",
                                 "data": _data_key(a)[:300]})
    return findings, rows
