"""Phase 2 — inventory what the current build actually logs.

Reads every *.json dump under the configured log folder and produces:

  outputs/current-log-inventory.json   (machine-readable)
  outputs/eventkey-inventory.csv       (one row per distinct eventKey)

The inventory keeps raw event names exactly as logged (no normalization) and
summarizes high-cardinality payloads by structure instead of dumping values.
"""

import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

# data fields whose values are high-cardinality — summarize, never enumerate
HIGH_CARDINALITY = {"position", "timestamp", "location", "answerSubmitted",
                    "designSelections", "Value"}
MAX_VALUES = 25


def _data_fields(data):
    if isinstance(data, dict):
        return tuple(sorted(data.keys()))
    return (f"<{type(data).__name__}>",)


def build_inventory(records, meta):
    et = {}
    for r in records:
        t = r.get("eventType")
        e = et.setdefault(
            t,
            {
                "count": 0,
                "scenes": Counter(),
                "first_ts": None,
                "last_ts": None,
                "schema_variants": Counter(),
                "field_values": defaultdict(Counter),
                "with_event_key": 0,
                "sample": None,
            },
        )
        e["count"] += 1
        e["scenes"][r.get("sceneName")] += 1
        ts = r.get("timestamp")
        if ts:
            e["first_ts"] = min(e["first_ts"] or ts, ts)
            e["last_ts"] = max(e["last_ts"] or ts, ts)
        data = r.get("data")
        e["schema_variants"][_data_fields(data)] += 1
        if isinstance(data, dict):
            for k, v in data.items():
                if k in HIGH_CARDINALITY:
                    continue
                if isinstance(v, (str, int, float, bool)) or v is None:
                    e["field_values"][k][json.dumps(v, ensure_ascii=False)] += 1
        if r.get("eventKey"):
            e["with_event_key"] += 1
        if e["sample"] is None:
            e["sample"] = {
                "_id": r["_id"],
                "_src": r["_src"],
                "timestamp": ts,
                "sceneName": r.get("sceneName"),
                "eventKey": r.get("eventKey"),
                "data": data,
            }

    event_types = {}
    for t, e in sorted(et.items(), key=lambda kv: -kv[1]["count"]):
        fv = {}
        for k, c in e["field_values"].items():
            if len(c) <= MAX_VALUES:
                fv[k] = dict(c.most_common())
            else:
                fv[k] = {"<distinct_values>": len(c), "<examples>": [v for v, _ in c.most_common(5)]}
        event_types[t] = {
            "count": e["count"],
            "scenes": dict(e["scenes"].most_common()),
            "first_ts": e["first_ts"],
            "last_ts": e["last_ts"],
            "records_with_eventKey": e["with_event_key"],
            "schema_variants": {
                " | ".join(k) if k else "<empty dict>": n
                for k, n in e["schema_variants"].most_common()
            },
            "field_values": fv,
            "sample": e["sample"],
        }

    # ---- eventKey inventory -------------------------------------------------
    ek = {}
    dlg_mismatches = []
    for r in records:
        key = r.get("eventKey")
        if not key:
            continue
        rec = ek.setdefault(
            key,
            {
                "count": 0,
                "eventTypes": Counter(),
                "scenes": Counter(),
                "first_ts": None,
                "last_ts": None,
                "examples": [],
            },
        )
        rec["count"] += 1
        rec["eventTypes"][r.get("eventType")] += 1
        rec["scenes"][r.get("sceneName")] += 1
        ts = r.get("timestamp")
        if ts:
            rec["first_ts"] = min(rec["first_ts"] or ts, ts)
            rec["last_ts"] = max(rec["last_ts"] or ts, ts)
        if len(rec["examples"]) < 3:
            rec["examples"].append({"_id": r["_id"], "_src": r["_src"], "timestamp": ts})
        kind, a, b = lib.parse_event_key(key)
        if kind == "dialogue":
            data = r.get("data") or {}
            dc, dn = data.get("conversationId"), data.get("nodeId")
            if dc is not None and dn is not None and (int(dc) != a or int(dn) != b):
                dlg_mismatches.append(
                    {"_id": r["_id"], "eventKey": key,
                     "data.conversationId": dc, "data.nodeId": dn,
                     "timestamp": ts, "sceneName": r.get("sceneName")}
                )

    event_keys = {}
    dialogue_convs = defaultdict(dict)
    quests = defaultdict(lambda: {"questActiveEvent": 0, "questFinishEvent": 0, "names": Counter()})
    for key, rec in ek.items():
        event_keys[key] = {
            "count": rec["count"],
            "eventTypes": dict(rec["eventTypes"]),
            "scenes": dict(rec["scenes"].most_common()),
            "first_ts": rec["first_ts"],
            "last_ts": rec["last_ts"],
            "examples": rec["examples"],
        }
        kind, a, b = lib.parse_event_key(key)
        if kind == "dialogue":
            dialogue_convs[a][b] = rec["count"]
        elif kind == "quest":
            quests[b][a] += rec["count"]
    # quest names from data
    for r in records:
        if r.get("eventType") == "questEvent":
            d = r.get("data") or {}
            qid = d.get("questID")
            if qid is not None:
                try:
                    quests[int(qid)]["names"][d.get("questName")] += 1
                except (ValueError, TypeError):
                    pass

    quests_out = {
        str(q): {
            "questActiveEvent": v["questActiveEvent"],
            "questFinishEvent": v["questFinishEvent"],
            "names": dict(v["names"].most_common()),
        }
        for q, v in sorted(quests.items())
    }

    # ---- anomalies ----------------------------------------------------------
    # exact duplicates among assessment-relevant records (same eventType,
    # eventKey, timestamp, and payload)
    dup_counter = Counter()
    for r in records:
        sig = (
            r.get("eventType"),
            r.get("eventKey"),
            r.get("timestamp"),
            json.dumps(r.get("data"), sort_keys=True, ensure_ascii=False),
        )
        dup_counter[sig] += 1
    duplicates = [
        {"eventType": s[0], "eventKey": s[1], "timestamp": s[2], "copies": n, "data": s[3][:160]}
        for s, n in dup_counter.most_common()
        if n > 1
    ]

    # scene timeline (compact visit list)
    timeline = []
    for r in records:
        sc = r.get("sceneName")
        if not timeline or timeline[-1]["scene"] != sc:
            timeline.append({"scene": sc, "first_ts": r.get("timestamp"), "records": 0})
        timeline[-1]["records"] += 1
        timeline[-1]["last_ts"] = r.get("timestamp")

    return {
        "meta": meta,
        "event_types": event_types,
        "event_keys": event_keys,
        "dialogue_conversations_observed": {
            str(c): dict(sorted(nodes.items())) for c, nodes in sorted(dialogue_convs.items())
        },
        "quests_observed": quests_out,
        "anomalies": {
            "dialogue_eventKey_vs_data_mismatches": dlg_mismatches,
            "exact_duplicate_records": duplicates,
        },
        "scene_timeline": timeline,
    }


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    records, meta = lib.load_logs(cfg)
    inv = build_inventory(records, meta)

    out = lib.out_path(cfg, "current-log-inventory.json")
    lib.write_json(out, inv)

    rows = []
    for key, rec in sorted(inv["event_keys"].items()):
        kind, a, b = lib.parse_event_key(key)
        rows.append(
            {
                "eventKey": key,
                "kind": kind,
                "count": rec["count"],
                "eventTypes": ";".join(rec["eventTypes"]),
                "scenes": ";".join(s or "" for s in rec["scenes"]),
                "first_ts": rec["first_ts"],
                "last_ts": rec["last_ts"],
                "example_id": rec["examples"][0]["_id"] if rec["examples"] else "",
                "example_src": rec["examples"][0]["_src"] if rec["examples"] else "",
            }
        )
    csv_out = lib.out_path(cfg, "eventkey-inventory.csv")
    lib.write_csv(csv_out, rows, ["eventKey", "kind", "count", "eventTypes", "scenes",
                                  "first_ts", "last_ts", "example_id", "example_src"])

    print(f"Wrote {out}")
    print(f"Wrote {csv_out} ({len(rows)} distinct eventKeys)")
    print(f"  files={meta['files']} records={meta['record_count']} "
          f"player_field={meta['player_field']} players={meta['players']}")
    print(f"  eventTypes={len(inv['event_types'])} "
          f"dialogue convs={len(inv['dialogue_conversations_observed'])} "
          f"quests={len(inv['quests_observed'])}")
    an = inv["anomalies"]
    print(f"  anomalies: {len(an['dialogue_eventKey_vs_data_mismatches'])} eventKey/data mismatches, "
          f"{len(an['exact_duplicate_records'])} exact-duplicate groups")
    if meta["parse_errors"]:
        print(f"  WARN parse errors: {meta['parse_errors']}")


if __name__ == "__main__":
    main()
