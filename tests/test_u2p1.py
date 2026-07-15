"""Test for Unit 2 Point 1 — "Escape the Ruin".

Production rule (mhs-unit2-point1-grading.md): within the latest attempt window
(previous `questFinishEvent:21` exclusive .. latest `questFinishEvent:21`
inclusive) the point is green iff the success node is present AND no yellow node
is present. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 2, "point": 1, "name": "Escape the Ruin", "expected": "green"}

TRIGGER_KEY = "questFinishEvent:21"
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


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
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
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
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
