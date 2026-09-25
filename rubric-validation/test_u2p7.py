"""Test for Unit 2 Point 7 — "Which Watershed? Part II".

Production rule (mhs-unit2-point7-grading.md): within the attempt window,
green iff the success key is present AND neg_count <= 3. Window (start-and-end
form since 2026-09-24): anchor on the latest END (`questFinishEvent:54`); if
missing => yellow. Take the latest START (`DialogueNodeEvent:20:46`) at
`_id < latestEnd._id` (else ObjectId("000...")) as the exclusive window start.
Until 2026-09-24 the window was (previous `questFinishEvent:54` exclusive ..
latest `questFinishEvent:54` inclusive).

The 2026-08-31 grading-logic update removed the dead keys 27:19 and
27:21-27:24 from NEG_KEYS (15 keys remain). Keys re-verified 2026-09-24
against the 2026-09-21 dialogue database (conversation 27 unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 2, "point": 7, "name": "Which Watershed? Part II"}

START_KEY = "DialogueNodeEvent:20:46"
END_KEY = "questFinishEvent:54"
SUCCESS_KEY = "DialogueNodeEvent:27:7"
THRESHOLD = 3

NEG_KEYS = [f"DialogueNodeEvent:27:{n}" for n in
            (11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28, 29, 30)]


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
    return window_start_id, latest_end["_id"]


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    # 3) Success node and negative count inside the window
    has_success = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter})
        is not None
    )
    neg_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    return "green" if (has_success and neg_count <= THRESHOLD) else "yellow"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_success = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter})
        is not None
    )
    neg_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    if not has_success:
        out["MISSING_SUCCESS_NODE"] = (
            f"success key {SUCCESS_KEY} absent in window — did not build the watershed argument"
        )
    # attempt_number = neg_count + 1 (per the reason quantity script)
    if neg_count > THRESHOLD:
        out["WRONG_ARG_SELECTED"] = (
            f"attempt_number={neg_count + 1} (neg_count={neg_count} > {THRESHOLD}) — "
            f"too many attempts to select evidence to support the claim"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
