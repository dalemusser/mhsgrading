"""Reason codes for Unit 2 Point 3 — "Getting the Band Back Together Part II".

mhs-unit2-point3-grading.md, "## Reason Codes":

  EXCESS_NAV_REMINDERS — triggered when 6 or more navigation reminders fired
      across the Tera and Aryn searches; triggering_number = total,
      tera_count / aryn_count = per-phase splits.

Outer window mirrors the production color script: latest `22:18` (end),
latest `20:33` at/before it (start); counts use `$gte start, $lte end`.
Phase split: Tera search = start → first `21:1` in window; Aryn search =
first `18:231` in window → end.
"""

from rc_common import count_keys, earliest, latest

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
]

_EMPTY = {"triggered": False, "triggering_number": 0, "tera_count": 0, "aryn_count": 0}


def attempt_window(coll, pid):
    # 1) Latest trigger (end anchor)
    end_doc = latest(coll, pid, TRIGGER_KEY)
    if not end_doc:
        return None
    # 2) Latest start at/before the end (same attempt)
    start_doc = latest(coll, pid, START_KEY, {"_id": {"$lte": end_doc["_id"]}})
    if not start_doc:
        return None
    return start_doc["_id"], end_doc["_id"]


def excess_nav_reminders(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return dict(_EMPTY)
    start_id, end_id = win
    inside = {"_id": {"$gte": start_id, "$lte": end_id}}

    # 3) Phase boundaries: first occurrence of each marker inside the window
    tera_end = earliest(coll, pid, TERA_FOUND_KEY, inside)
    aryn_start = earliest(coll, pid, ARYN_START_KEY, inside)

    # 4) Total across the whole window — authoritative, matches the color rule
    total = count_keys(coll, pid, TARGET_KEYS, inside)

    # 5) Per-phase counts by time window
    tera_count = count_keys(coll, pid, TARGET_KEYS, {
        "_id": {"$gte": start_id, "$lte": (tera_end["_id"] if tera_end else end_id)}
    })
    aryn_count = (
        count_keys(coll, pid, TARGET_KEYS, {"_id": {"$gte": aryn_start["_id"], "$lte": end_id}})
        if aryn_start else 0
    )

    return {"triggered": total >= 6, "triggering_number": total,
            "tera_count": tera_count, "aryn_count": aryn_count}


CODES = {"EXCESS_NAV_REMINDERS": excess_nav_reminders}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
