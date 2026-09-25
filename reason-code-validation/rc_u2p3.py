"""Reason codes for Unit 2 Point 3 — "Getting the Band Back Together Part II".

mhs-unit2-point3-grading.md, "## Reason Codes":

  EXCESS_NAV_REMINDERS — triggered when 6 or more navigation reminders fired
      across the Tera and Aryn searches; triggering_number = total,
      tera_count / aryn_count = per-phase splits.

Outer window mirrors the production color script exactly: latest `22:18`
(end), latest `20:33` at/before it (start), both needing a client
`timestamp`; every count is fenced by BOTH the timestamp range and the `_id`
range of the anchors (fence added 2026-09-24, decision A7, so the pop-up
count can never differ from the color). Phase split: Tera search = start →
first `21:1` in window; Aryn search = first `18:231` in window → end.

2026-09-24: `28:195` / `59:195` added to TARGET_KEYS (Aryn search, same quest
gate as 192/193/194; never observed in a fixture).
"""

from rc_common import GAME, latest

META = {"unit": 2, "point": 3, "name": "Getting the Band Back Together Part II",
        "doc": "mhs-unit2-point3-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:22:18"
START_KEY = "DialogueNodeEvent:20:33"
TERA_FOUND_KEY = "DialogueNodeEvent:21:1"
ARYN_START_KEY = "DialogueNodeEvent:18:231"

TARGET_KEYS = [
    "DialogueNodeEvent:18:225", "DialogueNodeEvent:28:185", "DialogueNodeEvent:59:185",
    "DialogueNodeEvent:28:184", "DialogueNodeEvent:28:191", "DialogueNodeEvent:59:184", "DialogueNodeEvent:59:191",
    "DialogueNodeEvent:18:226", "DialogueNodeEvent:18:227", "DialogueNodeEvent:28:186", "DialogueNodeEvent:59:186",
    "DialogueNodeEvent:18:228", "DialogueNodeEvent:28:187", "DialogueNodeEvent:59:187",
    "DialogueNodeEvent:18:229", "DialogueNodeEvent:28:188", "DialogueNodeEvent:59:188",
    "DialogueNodeEvent:18:230", "DialogueNodeEvent:28:180", "DialogueNodeEvent:59:180",
    "DialogueNodeEvent:18:233", "DialogueNodeEvent:28:192", "DialogueNodeEvent:59:192",
    "DialogueNodeEvent:18:234", "DialogueNodeEvent:28:193", "DialogueNodeEvent:59:193",
    "DialogueNodeEvent:18:235", "DialogueNodeEvent:28:194", "DialogueNodeEvent:59:194",
    "DialogueNodeEvent:18:236", "DialogueNodeEvent:18:237", "DialogueNodeEvent:28:190", "DialogueNodeEvent:59:190",
    "DialogueNodeEvent:28:195", "DialogueNodeEvent:59:195",  # Aryn: passage doesn't go all the way through (added 2026-09-24)
]

_EMPTY = {"triggered": False, "triggering_number": 0, "tera_count": 0, "aryn_count": 0}


def _anchors(coll, pid):
    """(startDoc, endDoc) or None, mirroring the script's two guards."""
    # 1) Latest trigger (end anchor) by arrival order
    end_doc = latest(coll, pid, TRIGGER_KEY)
    if not end_doc or not end_doc.get("timestamp"):
        return None
    # 2) Latest start at/before the end (same attempt)
    start_doc = latest(coll, pid, START_KEY, {"_id": {"$lte": end_doc["_id"]}})
    if not start_doc or not start_doc.get("timestamp"):
        return None
    return start_doc, end_doc


def attempt_window(coll, pid):
    a = _anchors(coll, pid)
    return (a[0]["_id"], a[1]["_id"]) if a else None


def _count(coll, pid, keys, ts_fence, id_lo, id_hi):
    return coll.count_documents({
        "game": GAME, "playerId": pid, "eventKey": {"$in": keys} if isinstance(keys, list) else keys,
        "timestamp": ts_fence,
        "_id": {"$gte": id_lo, "$lte": id_hi},
    })


def excess_nav_reminders(coll, pid):
    a = _anchors(coll, pid)
    if a is None:
        return dict(_EMPTY)
    start_doc, end_doc = a
    # Outer fence, identical to the production color script: client timestamp AND _id
    ts_fence = {"$gte": start_doc["timestamp"], "$lte": end_doc["timestamp"]}
    fence = {"timestamp": ts_fence, "_id": {"$gte": start_doc["_id"], "$lte": end_doc["_id"]}}

    # 3) Phase boundaries: first occurrence of each marker inside the window
    tera_end = coll.find_one({"game": GAME, "playerId": pid, "eventKey": TERA_FOUND_KEY, **fence},
                             sort={"_id": 1})
    aryn_start = coll.find_one({"game": GAME, "playerId": pid, "eventKey": ARYN_START_KEY, **fence},
                               sort={"_id": 1})

    # 4) Total across the whole window — authoritative, identical to the color rule
    total = _count(coll, pid, TARGET_KEYS, ts_fence, start_doc["_id"], end_doc["_id"])

    # 5) Per-phase counts: the same fence, narrowed by _id to each search
    tera_count = _count(coll, pid, TARGET_KEYS, ts_fence, start_doc["_id"],
                        tera_end["_id"] if tera_end else end_doc["_id"])
    aryn_count = (
        _count(coll, pid, TARGET_KEYS, ts_fence, aryn_start["_id"], end_doc["_id"])
        if aryn_start else 0
    )

    return {"triggered": total >= 6, "triggering_number": total,
            "tera_count": tera_count, "aryn_count": aryn_count}


CODES = {"EXCESS_NAV_REMINDERS": excess_nav_reminders}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
