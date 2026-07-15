"""Test for Unit 1 Point 3 — "Defend the Expedition".

Production rule (mhs-unit1-point3-grading.md): windowed yellow-node check.
Within the latest attempt window (previous `questActiveEvent:34` exclusive ..
latest `questActiveEvent:34` inclusive), the point is yellow if any yellow node
is present, otherwise green. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 1, "point": 3, "name": "Defend the Expedition", "expected": "yellow"}

TRIGGER_KEY = "questActiveEvent:34"

YELLOW_KEYS = [
    "DialogueNodeEvent:70:25",
    "DialogueNodeEvent:70:33",
]

# Reason quantity: attempts to construct the correct argument.
ATTEMPT_KEYS = ["DialogueNodeEvent:70:25", "DialogueNodeEvent:70:33", "DialogueNodeEvent:70:7"]


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    has_yellow = (
        coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventKey": {"$in": YELLOW_KEYS},
                "_id": {"$gt": start, "$lte": end},
            }
        )
        is not None
    )
    return "yellow" if has_yellow else "green"


def diagnose(coll, pid):
    """Reason: WRONG_ARG_SELECTED — needed multiple tries to build the argument.
    Quantity `attempt_number` is the windowed count of attempt dialogue nodes."""
    out = {}
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    start, end = win
    attempt_number = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": {"$in": ATTEMPT_KEYS},
            "_id": {"$gt": start, "$lte": end},
        }
    )
    yellow_hits = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": {"$in": YELLOW_KEYS},
            "_id": {"$gt": start, "$lte": end},
        }
    )
    if yellow_hits > 0:
        out["WRONG_ARG_SELECTED"] = (
            f"attempt_number={attempt_number} (yellow nodes hit {yellow_hits}x in window) "
            f"— student needed multiple tries to build the correct argument"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
