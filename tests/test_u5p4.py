"""Test for Unit 5 Point 4 — "Water Problems Require Water Solutions".

Production rule (mhs-unit5-point4-grading.md): success key + zero-tolerance
negative count within the latest attempt window. Anchor on the latest END
(`questFinishEvent:45`); if missing => yellow. Take the latest START
(`questFinishEvent:44`) at `_id < latestEnd._id` (else ObjectId("000...")) as the
exclusive window start. Inside the window green iff the success node
`DialogueNodeEvent:106:35` is present AND the negative count == 0; otherwise
yellow.
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {
    "unit": 5,
    "point": 4,
    "name": "Water Problems Require Water Solutions",
    "expected": "green",
}

START_KEY = "questFinishEvent:44"
END_KEY = "questFinishEvent:45"
SUCCESS_KEY = "DialogueNodeEvent:106:35"

NEGATIVE_KEYS = [
    "DialogueNodeEvent:106:4",
    "DialogueNodeEvent:106:25",
    "DialogueNodeEvent:106:26",
    "DialogueNodeEvent:106:27",
    "DialogueNodeEvent:106:28",
    "DialogueNodeEvent:106:29",
    "DialogueNodeEvent:106:30",
    "DialogueNodeEvent:106:31",
    "DialogueNodeEvent:106:32",
    "DialogueNodeEvent:106:33",
    "DialogueNodeEvent:106:34",
]


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when no latest END trigger
    exists (=> yellow)."""
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": END_KEY}, sort={"_id": -1}
    )
    if not latest_end:
        return None
    prev_start = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": START_KEY,
            "_id": {"$lt": latest_end["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = prev_start["_id"] if prev_start else ObjectId(OID_MIN)
    window_end_id = latest_end["_id"]
    return window_start_id, window_end_id


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    window_start_id, window_end_id = win
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}
    has_success = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter}
        )
        is not None
    )
    if not has_success:
        return "yellow"
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEGATIVE_KEYS}, **win_filter}
    )
    return "green" if cnt == 0 else "yellow"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["NO_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    window_start_id, window_end_id = win
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}
    has_success = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter}
        )
        is not None
    )
    if not has_success:
        out["MISSING_SUCCESS_NODE"] = (
            f"success node {SUCCESS_KEY} absent in window — did not correctly "
            f"identify the water solution plan"
        )
        return out
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEGATIVE_KEYS}, **win_filter}
    )
    if cnt != 0:
        out["BAD_FEEDBACK"] = (
            f"negativeCount={cnt} (>0) — incorrect selections during the water "
            f"solution activity; threshold is zero"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
