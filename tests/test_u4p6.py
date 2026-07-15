"""Test for Unit 4 Point 6 — "Desert Delicacies".

Production rule (mhs-unit4-point6-grading.md): score-based on the latest camera
placement per garden box, within an attempt window anchored on TWO distinct
triggers — latest `questActiveEvent:41` (start) .. latest `questFinishEvent:56`
(end, inclusive). Yellow unless both triggers exist AND end._id >= start._id
(production guard: `!latestStart || !latestEnd || latestEnd._id < latestStart._id`).

Per the production script's verbatim mapping, +1 each for:
    Box 0 latest soilType == "Clay"
    Box 1 latest soilType == "Sand"
    Box 2 latest soilType == "Gravel"
    green iff score >= 2, else yellow.
"""

from mhs_harness import GAME

META = {"unit": 4, "point": 6, "name": "Desert Delicacies", "expected": "green"}

WINDOW_START_KEY = "questActiveEvent:41"
WINDOW_END_KEY = "questFinishEvent:56"

# Verbatim from the Production Script (Attempt-Based) box -> expected soil checks.
EXPECTED_SOIL_BY_BOX = {"0": "Clay", "1": "Sand", "2": "Gravel"}


def _window(coll, pid):
    """Return (windowStartId, windowEndId) or None when the window is invalid
    (=> yellow), matching the production guard
    `!latestStart || !latestEnd || latestEnd._id < latestStart._id`."""
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_START_KEY},
        sort={"_id": -1},
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY},
        sort={"_id": -1},
    )
    if not latest_start or not latest_end or latest_end["_id"] < latest_start["_id"]:
        return None
    return latest_start["_id"], latest_end["_id"]


def _box_results(coll, pid):
    """Return (score, dict boxId -> latest soilType or None) or None if no window."""
    win = _window(coll, pid)
    if win is None:
        return None
    start, end = win
    score = 0
    latest_answer = {}
    for box_id, expected_soil in EXPECTED_SOIL_BY_BOX.items():
        latest_box = coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventType": "TerasGardenBox",
                "data.actionType": "cameraPlaced",
                "data.boxId": box_id,
                "_id": {"$gt": start, "$lte": end},
            },
            sort={"_id": -1},
        )
        actual_soil = None
        if latest_box and latest_box.get("data"):
            actual_soil = latest_box["data"].get("soilType")
        latest_answer[box_id] = actual_soil
        if actual_soil == expected_soil:
            score += 1
    return score, latest_answer


def grade(coll, pid):
    res = _box_results(coll, pid)
    if res is None:
        return "yellow"
    score, _ = res
    return "green" if score >= 2 else "yellow"


def diagnose(coll, pid):
    out = {}
    res = _box_results(coll, pid)
    if res is None:
        out["NO_TRIGGER"] = (
            f"no valid window from {WINDOW_START_KEY}/{WINDOW_END_KEY} — defaults to yellow"
        )
        return out
    score, latest_answer = res
    wrong_box_ids = [
        b for b, exp in EXPECTED_SOIL_BY_BOX.items() if latest_answer.get(b) != exp
    ]
    out["_score"] = f"score={score} wrongTime={len(wrong_box_ids)}"
    if score < 2:
        details = ", ".join(
            f"box {b}: expected {EXPECTED_SOIL_BY_BOX[b]}, got {latest_answer.get(b)}"
            for b in wrong_box_ids
        )
        out["WRONG_CHOISE_SELECTED"] = (
            f"wrongTime={len(wrong_box_ids)} (correct boxes < 2) — {details}"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
