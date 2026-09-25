"""Reason codes for Unit 3 Point 1 — "Establishing a Foothold" (Supply Run).

mhs-unit3-point1-grading.md, "## Reason Codes":

  EXCESS_WRONG_RIVERS — triggered when the color rule goes yellow: fewer than
      2 correct-river confirmations (10:30) in the window; wrong_river_number
      counts the wrong-river feedback nodes (10:31 mid-task, 10:32 last crate).

Window (start-and-end form since 2026-09-24): latest `DialogueNodeEvent:11:22`
(end, inclusive), latest `DialogueNodeEvent:10:1` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. Until
2026-09-24: previous `11:22` (exclusive) .. latest (inclusive). Keys
re-verified 2026-09-24 against the 2026-09-21 dialogue database.
"""

from rc_common import OID_MIN, count_keys, gt_lte, latest

META = {"unit": 3, "point": 1, "name": "Establishing a Foothold",
        "doc": "mhs-unit3-point1-grading.md"}

START_KEY = "DialogueNodeEvent:10:1"
END_KEY = "DialogueNodeEvent:11:22"
CORRECT_KEY = "DialogueNodeEvent:10:30"   # "you picked the right river"

WRONG_RIVER_KEYS = [
    "DialogueNodeEvent:10:31",  # wrong river, crate lost (crates 1-2)
    "DialogueNodeEvent:10:32",  # wrong river, last crate
]


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def excess_wrong_rivers(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_river_number": 0}
    f = gt_lte(win)
    # 3) Correct-river confirmations (the color rule's target)
    correct_count = count_keys(coll, pid, CORRECT_KEY, f)
    # 4) Wrong-river selections, counted directly
    wrong_count = count_keys(coll, pid, WRONG_RIVER_KEYS, f)
    # 5) Mirror the color rule exactly (green requires correctCount > 1)
    return {"triggered": correct_count <= 1, "wrong_river_number": wrong_count}


CODES = {"EXCESS_WRONG_RIVERS": excess_wrong_rivers}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
