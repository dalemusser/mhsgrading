"""Test for Unit 4 Point 5 — "Saving Cadet Anderson".

Production rule (mhs-unit4-point5-grading.md): within the attempt window,
green iff a POS (success) key is present AND neg count < 3. No trigger =>
yellow; missing success node => yellow; neg count >= 3 => yellow.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`questActiveEvent:41`); if missing => yellow. Take the latest START
(`questActiveEvent:36`, which logs twice per playthrough — the later one is
taken and every conversation-90 submission follows it) at
`_id < latestEnd._id` (else ObjectId("000...")) as the exclusive window start.
Until 2026-09-24 the window was (previous `questActiveEvent:41` exclusive ..
latest `questActiveEvent:41` inclusive).

Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 90 unchanged: 23 nodes, same gates and texts).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 4, "point": 5, "name": "Saving Cadet Anderson"}

START_KEY = "questActiveEvent:36"
END_KEY = "questActiveEvent:41"

POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"]

NEG_KEYS = [
    "DialogueNodeEvent:90:25", "DialogueNodeEvent:90:37", "DialogueNodeEvent:90:39",
    "DialogueNodeEvent:90:45", "DialogueNodeEvent:90:47", "DialogueNodeEvent:90:52",
    "DialogueNodeEvent:90:54", "DialogueNodeEvent:90:55", "DialogueNodeEvent:90:56",
    "DialogueNodeEvent:90:58", "DialogueNodeEvent:90:59", "DialogueNodeEvent:90:60",
    "DialogueNodeEvent:90:61",
]

THRESHOLD = 3  # cnt >= 3 ? "yellow" : "green"


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
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
        )
        is not None
    )
    if not has_success:
        return "yellow"
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    return "yellow" if cnt >= THRESHOLD else "green"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["NO_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_success = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
        )
        is not None
    )
    negative_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    out["_score"] = f"has_success={int(has_success)} negativeCount={negative_count}"
    if not has_success:
        out["MISSING_SUCCESS_NODE"] = (
            f"neither {POS_KEYS[0]} nor {POS_KEYS[1]} present in window — did not "
            f"construct the correct argument"
        )
    if negative_count >= THRESHOLD:
        out["WRONG_ARG_SELECTED"] = (
            f"negativeCount={negative_count} (>= {THRESHOLD}) — too many negative "
            f"feedback events before submitting the correct argument"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
