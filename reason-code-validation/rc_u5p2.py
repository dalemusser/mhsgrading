"""Reason codes for Unit 5 Point 2 — "If I Had a Nickel- Floors 3 & 4".

mhs-unit5-point2-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — score: floor3 <= 6 -> +2, 7-10 -> +1;
      floor4 <= 5 -> +2, 6-9 -> +1; triggered when total < 3. Counts are
      WaterChamberEvent records with machineType in VALID_TYPES, mirror-exact
      with the color script: Condenser / Evaporator plus, since 2026-09-24
      (grading-team review item approved 2026-09-21), the floor-3
      dual-chamber machine's DualChamber_Condenser / DualChamber_Evaporator.
      VentSwitch is never counted.

Window (start-and-end form since 2026-09-24): latest `DialogueNodeEvent:96:1`
(end, inclusive), latest `questFinishEvent:43` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. Until
2026-09-24: latest start and latest end, yellow when the end preceded the
start (guard `latestEnd._id < latestStart._id`).
"""

from rc_common import GAME, OID_MIN, gt_lte, latest

META = {"unit": 5, "point": 2, "name": "If I Had a Nickel- Floors 3 & 4",
        "doc": "mhs-unit5-point2-grading.md"}

WINDOW_START_KEY = "questFinishEvent:43"
WINDOW_END_KEY = "DialogueNodeEvent:96:1"
VALID_TYPES = ["Condenser", "Evaporator", "DualChamber_Condenser", "DualChamber_Evaporator"]


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, WINDOW_END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, WINDOW_START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def _floor_count(coll, pid, floor, f):
    return coll.count_documents({
        "game": GAME, "playerId": pid,
        "eventType": "WaterChamberEvent",
        "data.floor": floor,
        "data.machineType": {"$in": VALID_TYPES},
        **f,
    })


def score_below_threshold(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "floor3_attempts": 0, "floor4_attempts": 0}
    f = gt_lte(win)
    floor3 = _floor_count(coll, pid, "3", f)
    floor4 = _floor_count(coll, pid, "4", f)
    # Mirror the color formula exactly
    score = 0
    if floor3 <= 6:
        score += 2
    elif floor3 < 11:
        score += 1
    if floor4 <= 5:
        score += 2
    elif floor4 < 10:
        score += 1
    return {"triggered": score < 3, "floor3_attempts": floor3, "floor4_attempts": floor4}


CODES = {"SCORE_BELOW_THRESHOLD": score_below_threshold}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
