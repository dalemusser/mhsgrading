"""Reason codes for Unit 4 Point 3 — "Alien Well Floor 3 & 4".

mhs-unit4-point3-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — score: floor3 == 1 -> +1; floor4 == 1 -> +2,
      floor4 == 2 -> +1; triggered when score <= 1. Counts are soilMachine
      interactions on machine "1" per floor (data.floor / data.machine are
      strings; floor 5's machine "2" is excluded).

Window: previous `questActiveEvent:50` (exclusive) .. latest (inclusive).
"""

from rc_common import GAME, gt_lte, latest_trigger_window

META = {"unit": 4, "point": 3, "name": "Alien Well Floor 3 & 4",
        "doc": "mhs-unit4-point3-grading.md"}

TRIGGER_KEY = "questActiveEvent:50"


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


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
