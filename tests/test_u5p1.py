"""Test for Unit 5 Point 1 — "If I Had a Nickel- Floors 1 & 2".

Production rule (mhs-unit5-point1-grading.md): success key + negative-feedback
threshold within the latest attempt window. The window is anchored on the latest
START (`questActiveEvent:43`) and latest END (`questFinishEvent:43`) found
independently; if either is missing or the end precedes the start => yellow.
Inside the window green iff the success key `DialogueNodeEvent:100:44` is present
AND the negative-feedback count is <= 2.
"""

from mhs_harness import GAME

META = {"unit": 5, "point": 1, "name": "If I Had a Nickel- Floors 1 & 2", "expected": "green"}

WINDOW_START_KEY = "questActiveEvent:43"
WINDOW_END_KEY = "questFinishEvent:43"

POS_KEY = "DialogueNodeEvent:100:44"
NEG_KEYS = [
    "DialogueNodeEvent:100:38",
    "DialogueNodeEvent:100:39",
    "DialogueNodeEvent:100:43",
]


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when the window cannot be
    established (=> yellow)."""
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_START_KEY}, sort={"_id": -1}
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY}, sort={"_id": -1}
    )
    if not latest_start or not latest_end or latest_end["_id"] < latest_start["_id"]:
        return None
    return latest_start["_id"], latest_end["_id"]


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    window_start_id, window_end_id = win
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}
    has_trigger = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": POS_KEY, **win_filter}
        )
        is not None
    )
    if not has_trigger:
        return "yellow"
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    return "yellow" if cnt > 2 else "green"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["NO_TRIGGER"] = (
            f"no {WINDOW_END_KEY}/{WINDOW_START_KEY} attempt window found — "
            f"defaults to yellow"
        )
        return out
    window_start_id, window_end_id = win
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}
    has_trigger = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": POS_KEY, **win_filter}
        )
        is not None
    )
    if not has_trigger:
        out["MISSING_SUCCESS_NODE"] = (
            f"success node {POS_KEY} absent in window — did not solve the water "
            f"chamber puzzle on floors 1 and 2"
        )
        return out
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    if cnt > 2:
        out["BAD_FEEDBACK"] = (
            f"negative_feedback_number={cnt} (>2) — too much negative feedback "
            f"before solving the puzzle"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
