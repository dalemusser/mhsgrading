"""Test for Unit 5 Point 1 — "If I Had a Nickel- Floors 1 & 2".

Production rule (mhs-unit5-point1-grading.md): success key + negative-feedback
threshold within the latest attempt window. Inside the window green iff the
success key `DialogueNodeEvent:100:44` is present AND the negative-feedback
count (100:38 / 100:39 / 100:43) is 0.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`questFinishEvent:43`); if missing => yellow. Take the latest START
(`questActiveEvent:43`) at `_id < latestEnd._id` (else ObjectId("000...")) as
the exclusive window start. Until 2026-09-24 the script took the latest start
and the latest end independently and returned yellow when the end preceded
the start (guard `!latestStart || !latestEnd || latestEnd._id < latestStart._id`).

Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 100 unchanged: 18 nodes, same gates). Note: 100:44
("OnPlayerSolve") also fires on the DANI-assisted path because the assist does
not move the tablets on the current build; the colour stays yellow there
because 100:39 (offer) or 100:43 (forced) is itself a negative key.
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 5, "point": 1, "name": "If I Had a Nickel- Floors 1 & 2"}

WINDOW_START_KEY = "questActiveEvent:43"
WINDOW_END_KEY = "questFinishEvent:43"

POS_KEY = "DialogueNodeEvent:100:44"
NEG_KEYS = [
    "DialogueNodeEvent:100:38",
    "DialogueNodeEvent:100:39",
    "DialogueNodeEvent:100:43",
]


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when no latest END trigger
    exists (=> yellow)."""
    # 1) Latest end anchor
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY}, sort={"_id": -1}
    )
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": WINDOW_START_KEY,
            "_id": {"$lt": latest_end["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = latest_start["_id"] if latest_start else ObjectId(OID_MIN)
    return window_start_id, latest_end["_id"]


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    window_start_id, window_end_id = win
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}
    # 3) Check success inside window
    has_trigger = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": POS_KEY, **win_filter}
        )
        is not None
    )
    if not has_trigger:
        return "yellow"
    # 4) Count negative feedback inside window
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    return "yellow" if cnt > 0 else "green"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["NO_TRIGGER"] = f"no {WINDOW_END_KEY} trigger found — defaults to yellow"
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
            f"success node {POS_KEY} absent in window — did not solve the "
            f"evaporation glyph puzzle on floors 1 and 2"
        )
        return out
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    if cnt > 0:
        out["BAD_FEEDBACK"] = (
            f"negative_feedback_number={cnt} (>0) — received negative feedback "
            f"before solving the puzzle"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
