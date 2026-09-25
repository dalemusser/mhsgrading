"""Test for Unit 1 Point 3 — "Defend the Expedition".

Production rule (mhs-unit1-point3-grading.md): windowed yellow-node check.
Window (start-and-end form since 2026-09-23): anchor on the latest END
(`questActiveEvent:34`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:30:98`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Inside the window the point is yellow if any
yellow node is present, otherwise green.

History: until 2026-09-23 the window was (previous `questActiveEvent:34`
exclusive .. latest `questActiveEvent:34` inclusive). The 2026-08-31
grading-logic update removed the dead key `DialogueNodeEvent:70:33` from
YELLOW_KEYS/ATTEMPT_KEYS (70:25 only now).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 1, "point": 3, "name": "Defend the Expedition"}

START_KEY = "DialogueNodeEvent:30:98"
END_KEY = "questActiveEvent:34"

YELLOW_KEYS = [
    "DialogueNodeEvent:70:25",
]

# Reason quantity: attempts to construct the correct argument.
ATTEMPT_KEYS = ["DialogueNodeEvent:70:25", "DialogueNodeEvent:70:7"]


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when no latest END trigger
    exists (=> yellow)."""
    # 1) Latest end anchor
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": END_KEY}, sort={"_id": -1}
    )
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": START_KEY,
            "_id": {"$lt": latest_end["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = latest_start["_id"] if latest_start else ObjectId(OID_MIN)
    window_end_id = latest_end["_id"]
    return window_start_id, window_end_id


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    start, end = win
    # 3) Any yellow node inside the window?
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
    win = _window(coll, pid)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
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
