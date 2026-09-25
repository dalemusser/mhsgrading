"""Test for Unit 2 Point 6 — "Which Watershed? Part I".

Production rule (mhs-unit2-point6-grading.md): within the attempt window,
green iff the pass node is present AND no yellow node is present. Window
(end-first form since 2026-09-24): anchor on the latest END
(`DialogueNodeEvent:20:46`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:23:42`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the script took the latest
start and the latest end and returned yellow unless the end came after the
start.

The 2026-07-22 grading-logic fix re-anchored the window: the script previously
windowed on `DialogueNodeEvent:20:35`, which fires BEFORE the pass node
20:43 and dropped it from the window (the round-1 U2P6 miscolor). The
HIT_YELLOW_NODE reason script now uses the same 23:42 .. 20:46 window.
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 2, "point": 6, "name": "Which Watershed? Part I"}

WINDOW_START_KEY = "DialogueNodeEvent:23:42"  # opens the activity (exclusive)
WINDOW_END_KEY = "DialogueNodeEvent:20:46"    # closes the attempt (inclusive)
PASS_KEY = "DialogueNodeEvent:20:43"
KEY_44 = "DialogueNodeEvent:20:44"
KEY_45 = "DialogueNodeEvent:20:45"
YELLOW_KEYS = [KEY_44, KEY_45]


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
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_pass = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": PASS_KEY, **win_filter})
        is not None
    )
    if not has_pass:
        return "yellow"
    has_yellow = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": {"$in": YELLOW_KEYS}, **win_filter})
        is not None
    )
    return "yellow" if has_yellow else "green"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["MISSING_TRIGGER"] = (
            f"no valid window from {WINDOW_START_KEY}/{WINDOW_END_KEY} — defaults to yellow"
        )
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    has_pass = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": PASS_KEY, **win_filter})
        is not None
    )
    if not has_pass:
        out["MISSING_SUCCESS_NODE"] = (
            f"pass node {PASS_KEY} absent in window — correct criterion never selected"
        )

    # HIT_YELLOW_NODE reason quantity (same window as the grade script).
    events = coll.find(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": [KEY_44, KEY_45]}, **win_filter}
    )
    triggered = {e["eventKey"] for e in events}
    has_44 = KEY_44 in triggered
    has_45 = KEY_45 in triggered

    if has_44 and has_45:
        result = "guessing through the correct answer"
    elif has_44:
        result = "waterfall height"
    elif has_45:
        result = "salinity"
    else:
        result = None

    if result is not None:
        out["HIT_YELLOW_NODE"] = (
            f"chose an incorrect criterion for watershed size on first try: {result}"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
