"""Reason codes for Unit 4 Point 3 — "Alien Well Floor 3 & 4".

mhs-unit4-point3-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — score: floor3 == 1 -> +1; floor4 == 1 -> +2,
      floor4 == 2 -> +1; triggered when score <= 1. Counts are soilMachine
      interactions on machine "1" per floor (data.floor / data.machine are
      strings; floor 5's machine "2" is excluded).

Window (start-and-end form since 2026-09-24): latest `questActiveEvent:50`
(end, inclusive), latest `questActiveEvent:48` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. Until
2026-09-24: previous `questActiveEvent:50` (exclusive) .. latest (inclusive).
"""

from rc_common import GAME, OID_MIN, gt_lte, latest

META = {"unit": 4, "point": 3, "name": "Alien Well Floor 3 & 4",
        "doc": "mhs-unit4-point3-grading.md"}

START_KEY = "questActiveEvent:48"
END_KEY = "questActiveEvent:50"


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def _floor_count(coll, pid, floor, f):
    return coll.count_documents({
        "game": GAME, "playerId": pid,
        "eventType": "soilMachine",
        "data.machine": "1",
        "data.floor": floor,
        **f,
    })


def score_below_threshold(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "floor3_attempts": 0, "floor4_attempts": 0}
    f = gt_lte(win)
    # 3) Per-floor interaction counts inside the window
    floor3 = _floor_count(coll, pid, "3", f)
    floor4 = _floor_count(coll, pid, "4", f)
    # 4) Mirror the color formula exactly
    score = 0
    if floor3 == 1:
        score += 1
    if floor4 == 1:
        score += 2
    elif floor4 == 2:
        score += 1
    return {"triggered": score <= 1, "floor3_attempts": floor3, "floor4_attempts": floor4}


CODES = {"SCORE_BELOW_THRESHOLD": score_below_threshold}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
