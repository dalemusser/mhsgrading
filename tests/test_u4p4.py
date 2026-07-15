"""Test for Unit 4 Point 4 — "Alien Well Floor 5 + You Know the Drill".

Production rule (mhs-unit4-point4-grading.md): score-based, within an attempt
window anchored on TWO distinct triggers — latest `questActiveEvent:50` (start,
exclusive) .. latest `questActiveEvent:36` (end, inclusive). Yellow unless both
triggers exist AND end._id > start._id.

    +1 if soilMachine floor 5 machine 1 TopRow count == 1 AND BottomRow count == 1
    +1 if soilMachine floor 5 machine 2 count == 1
    +2 if success_total > 0 and neg_total == 0
    +1 elif success_total > 0 and neg_total == 1
    green iff score > 2, else yellow.
"""

from mhs_harness import GAME

META = {
    "unit": 4,
    "point": 4,
    "name": "Alien Well Floor 5 + You Know the Drill",
    "expected": "green",
}

WINDOW_START_KEY = "questActiveEvent:50"
WINDOW_END_KEY = "questActiveEvent:36"

SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"]
NEG_KEYS = [
    "DialogueNodeEvent:107:2",
    "DialogueNodeEvent:107:3",
    "DialogueNodeEvent:107:6",
]


def _window(coll, pid):
    """Return (windowStartId, windowEndId) or None when the window is invalid
    (=> yellow), matching the production guard
    `!latestStart || !latestEnd || latestEnd._id <= latestStart._id`."""
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_START_KEY},
        sort={"_id": -1},
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY},
        sort={"_id": -1},
    )
    if not latest_start or not latest_end or latest_end["_id"] <= latest_start["_id"]:
        return None
    return latest_start["_id"], latest_end["_id"]


def _score_parts(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    c_m1_top = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "soilMachine",
            "data.floor": "5",
            "data.machine": "1",
            "data.row": "TopRow",
            **win_filter,
        }
    )
    c_m1_bottom = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "soilMachine",
            "data.floor": "5",
            "data.machine": "1",
            "data.row": "BottomRow",
            **win_filter,
        }
    )
    c_m2_floor5 = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "soilMachine",
            "data.floor": "5",
            "data.machine": "2",
            **win_filter,
        }
    )
    success_total = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": SUCCESS_KEYS}, **win_filter}
    )
    neg_total = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )

    score = 0
    if c_m1_top == 1 and c_m1_bottom == 1:
        score += 1
    if c_m2_floor5 == 1:
        score += 1
    if success_total > 0 and neg_total == 0:
        score += 2
    elif success_total > 0 and neg_total == 1:
        score += 1

    attempt_time = c_m1_top + c_m1_bottom + c_m2_floor5
    return score, attempt_time, neg_total


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    score, _, _ = parts
    return "green" if score > 2 else "yellow"


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["NO_TRIGGER"] = (
            f"no valid window from {WINDOW_START_KEY}/{WINDOW_END_KEY} — defaults to yellow"
        )
        return out
    score, attempt_time, neg_total = parts
    out["_score"] = f"score={score} attempt_time={attempt_time} negative_feedback_number={neg_total}"
    if score <= 2:
        out["SCORE_BELOW_THRESHOLD"] = (
            f"score={score} (<= 2) — combined soil-machine and dialogue score too low"
        )
    if attempt_time > 3:
        out["TOO_MANY_ATTEMPTS"] = (
            f"attempt_time={attempt_time} (> 3) — too many fifth-floor soil machine interactions"
        )
    if neg_total > 0:
        out["BAD_FEEDBACK"] = (
            f"negative_feedback_number={neg_total} (> 0) — wrong water-table choices "
            f"before the correct layer"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
