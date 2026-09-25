"""Test for Unit 2 Point 1 — "Escape the Ruin".

Production rule (mhs-unit2-point1-grading.md): within the attempt window the
point is green iff the success node is present AND no yellow node is present.
Window (start-and-end form since 2026-09-23): anchor on the latest END
(`questFinishEvent:21`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:18:1`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-23 the window was (previous
`questFinishEvent:21` exclusive .. latest `questFinishEvent:21` inclusive).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 2, "point": 1, "name": "Escape the Ruin"}

START_KEY = "DialogueNodeEvent:18:1"
END_KEY = "questFinishEvent:21"
SUCCESS_KEY = "DialogueNodeEvent:68:29"
YELLOW_NODES = [
    "DialogueNodeEvent:68:22",
    "DialogueNodeEvent:68:23",
    "DialogueNodeEvent:68:27",
    "DialogueNodeEvent:68:28",
    "DialogueNodeEvent:68:31",
]

# Reason quantity buckets for TOO_MANY_NEGATIVES.
FIVE_ATTEMPT_KEYS = ["DialogueNodeEvent:68:22", "DialogueNodeEvent:68:23"]
SIX_ATTEMPT_KEYS = ["DialogueNodeEvent:68:27", "DialogueNodeEvent:68:31"]
NPC_HELP_KEY = "DialogueNodeEvent:68:28"


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
    # 3) Success node and yellow nodes inside the window
    has_success = (
        coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventKey": SUCCESS_KEY,
                "_id": {"$gt": start, "$lte": end},
            }
        )
        is not None
    )
    has_any_yellow = (
        coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventKey": {"$in": YELLOW_NODES},
                "_id": {"$gt": start, "$lte": end},
            }
        )
        is not None
    )
    return "green" if (has_success and not has_any_yellow) else "yellow"


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
            f"map-profile matching independently"
        )

    events = coll.find(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": {"$in": FIVE_ATTEMPT_KEYS + SIX_ATTEMPT_KEYS + [NPC_HELP_KEY]},
            **win_filter,
        }
    )
    triggered = {e["eventKey"] for e in events}
    attempts = 0
    if NPC_HELP_KEY in triggered:
        attempts = 7
    if any(k in triggered for k in SIX_ATTEMPT_KEYS):
        attempts = 6
    if any(k in triggered for k in FIVE_ATTEMPT_KEYS):
        attempts = 5
    if attempts > 4:
        out["TOO_MANY_NEGATIVES"] = (
            f"attempts_number={attempts} (>4) — too many incorrect map-terrain matches"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
