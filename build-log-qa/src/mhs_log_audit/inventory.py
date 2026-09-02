"""Event inventory tables (Step 4 of the weekly audit).

Turns the generic profiles into flat, export-ready rows:
  * one row per eventType (counts, share, sessions, time span, scenes, fields);
  * one row per eventType x scene;
  * one row per eventType x field path;
  * one row per eventType x field x value (for reasonable cardinality).
"""

from __future__ import annotations

from typing import Dict, List

from .model import fmt_seconds
from .profiling import EventProfile, fmt_value

UNIQUE_VALUE_EXPORT_CAP = 60   # per field; larger sets export top values only


def event_type_rows(profiles: Dict[str, EventProfile], total: int) -> List[dict]:
    rows = []
    for et in sorted(profiles, key=lambda e: (-profiles[e].count, e)):
        p = profiles[et]
        span = None
        if p.first_ts and p.last_ts:
            span = (p.last_ts - p.first_ts).total_seconds()
        data_fields = sorted(f for f in p.fields if f.count(".") == 1)
        missing_fields = sum(fp.null_count for fp in p.fields.values())
        rows.append({
            "eventType": et,
            "record_count": p.count,
            "percent_of_total": round(100.0 * p.count / total, 2) if total else 0.0,
            "session_count": len(p.sessions),
            "first_timestamp": p.first_ts.isoformat() if p.first_ts else "",
            "last_timestamp": p.last_ts.isoformat() if p.last_ts else "",
            "active_span": fmt_seconds(span),
            "scene_count": len(p.scenes),
            "observed_scenes": "; ".join(sorted(p.scenes)),
            "eventKey_records": p.event_key_count,
            "data_fields": "; ".join(f.split(".", 1)[1] for f in data_fields),
            "null_value_count": missing_fields,
        })
    return rows


def event_scene_rows(profiles: Dict[str, EventProfile]) -> List[dict]:
    rows = []
    for et in sorted(profiles):
        p = profiles[et]
        for scene in sorted(p.scenes):
            first = p.scene_first.get(scene)
            last = p.scene_last.get(scene)
            span = (last - first).total_seconds() if first and last else None
            rows.append({
                "eventType": et,
                "sceneName": scene,
                "record_count": p.scenes[scene],
                "first_timestamp": first.isoformat() if first else "",
                "last_timestamp": last.isoformat() if last else "",
                "span_in_scene": fmt_seconds(span),
            })
    return rows


def field_rows(profiles: Dict[str, EventProfile]) -> List[dict]:
    rows = []
    for et in sorted(profiles):
        p = profiles[et]
        for path in sorted(p.fields):
            fp = p.fields[path]
            rng = ""
            if fp.numeric_min is not None:
                rng = f"{fp.numeric_min:g} .. {fp.numeric_max:g}"
            rows.append({
                "eventType": et,
                "field_path": path,
                "records_present": fp.count,
                "records_total": p.count,
                "types": "; ".join(f"{t}:{c}" for t, c in sorted(fp.types.items())),
                "null_count": fp.null_count,
                "empty_string_count": fp.empty_string_count,
                "unique_values": fp.n_unique,
                "values_truncated": fp.values_truncated,
                "numeric_range": rng,
            })
    return rows


def unique_value_rows(profiles: Dict[str, EventProfile]) -> List[dict]:
    """Full value lists for small-cardinality fields, top values otherwise."""
    rows = []
    for et in sorted(profiles):
        p = profiles[et]
        for path in sorted(p.fields):
            fp = p.fields[path]
            if not fp.values:
                continue
            items = fp.values.most_common()
            truncated = fp.values_truncated or len(items) > UNIQUE_VALUE_EXPORT_CAP
            if truncated:
                items = items[:UNIQUE_VALUE_EXPORT_CAP]
            for (tname, text), count in sorted(
                    items, key=lambda kv: (-kv[1], kv[0][1])):
                rows.append({
                    "eventType": et,
                    "field_path": path,
                    "value": fmt_value(tname, text),
                    "type": tname,
                    "count": count,
                    "value_list_truncated": truncated,
                })
    return rows
