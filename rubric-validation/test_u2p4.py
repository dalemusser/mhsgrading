"""Test for Unit 2 Point 4 — "Investigate the Temple".

Production rule (mhs-unit2-point4-grading.md): within the attempt window,
green iff the success key is present AND no bad-feedback key is present.
Window (start-and-end form since 2026-09-24): anchor on the latest END
(`DialogueNodeEvent:23:17`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:22:18`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the window was (previous
`DialogueNodeEvent:23:17` exclusive .. latest `DialogueNodeEvent:23:17`
inclusive). Colour keys unchanged by the 2026-09-21 dialogue-database review.
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 2, "point": 4, "name": "Investigate the Temple"}

START_KEY = "DialogueNodeEvent:22:18"
END_KEY = "DialogueNodeEvent:23:17"
SUCCESS_KEY = "DialogueNodeEvent:74:21"

BAD_KEYS = [
    "DialogueNodeEvent:74:16",
    "DialogueNodeEvent:74:17",
    "DialogueNodeEvent:74:20",
    "DialogueNodeEvent:74:22",
]

# Reason-quantity key sets (attempt count for TOO_MANY_NEGATIVES)
FIVE_ATTEMPT_KEYS = [
    "DialogueNodeEvent:74:16",
    "DialogueNodeEvent:74:17",
]
SIX_ATTEMPT_KEYS = [
    "DialogueNodeEvent:74:22",
    "DialogueNodeEvent:74:20",
]


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
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    # 3) Check success/bad within this attempt window
    has_success = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter})
        is not None
    )
    has_bad = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": {"$in": BAD_KEYS}, **win_filter})
        is not None
    )
    return "green" if (has_success and not has_bad) else "yellow"


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
    if not has_success:
        out["MISSING_SUCCESS_NODE"] = (
            f"success node {SUCCESS_KEY} absent in window — did not complete "
            f"watershed-flow matching independently"
        )

    # TOO_MANY_NEGATIVES: attempts_number from bad feedback node occurrences
    relevant_keys = FIVE_ATTEMPT_KEYS + SIX_ATTEMPT_KEYS
    events = coll.find(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": relevant_keys}, **win_filter}
    )
    triggered_keys = {e["eventKey"] for e in events}
    attempt = 0
    if any(k in triggered_keys for k in SIX_ATTEMPT_KEYS):
        attempt = 6
    elif any(k in triggered_keys for k in FIVE_ATTEMPT_KEYS):
        attempt = 5
    if attempt > 5:
        out["TOO_MANY_NEGATIVES"] = (
            f"attempts_number={attempt} (> 5) — too many attempts on the "
            f"watershed-flow glyph puzzle"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
