"""Test for Unit 4 Point 2 — "Infiltration Glyph + Alien Well Floors 1 & 2".

Production rule (mhs-unit4-point2-grading.md): within the attempt window
(latest Unit-4 soil-key close before the trigger, exclusive — OID_MIN when
none — .. latest `questActiveEvent:48`, inclusive), green iff the success node
`DialogueNodeEvent:88:11` is present AND no negative feedback node is present.
No trigger => yellow.

The 2026-09-01 grading-logic update re-based the window start: previously the
window ran from the previous `questActiveEvent:48` (and the prose referenced
the optional node 88:10, which never fires on a clean solve). The start is now
the latest close of the Unit 4 soil key puzzle before the trigger — the
`Soil Key Puzzle` event with `Soil Key Puzzle Status` = "Finished" and
`data.Unit` matching /^Unit 4/ (an eventType + data match, not an eventKey).
"""

from mhs_harness import GAME, OID_MIN

META = {
    "unit": 4,
    "point": 2,
    "name": "Infiltration Glyph + Alien Well Floors 1 & 2",
}

END_TRIGGER = "questActiveEvent:48"
SUCCESS_KEY = "DialogueNodeEvent:88:11"

EVENT_TYPE = "Soil Key Puzzle"
END_STATUS = "Finished"
UNIT_4_REGEX = "^Unit 4"

NEGATIVE_KEYS = [
    "DialogueNodeEvent:102:9",
    "DialogueNodeEvent:102:10",
    "DialogueNodeEvent:102:12",
    "DialogueNodeEvent:102:18",
    "DialogueNodeEvent:102:23",
]

WINDOW_DESC = "latest Unit-4 soil-key close .. latest questActiveEvent:48"


def attempt_window(coll, pid):
    """(windowStartId, windowEndId) or None when the trigger is missing.
    Start falls back to OID_MIN when no Unit-4 soil-key close precedes the
    trigger."""
    latest_trigger = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": END_TRIGGER}, sort={"_id": -1}
    )
    if not latest_trigger:
        return None
    latest_close = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": EVENT_TYPE,
            "data.Soil Key Puzzle Status": END_STATUS,
            "data.Unit": {"$regex": UNIT_4_REGEX},
            "_id": {"$lt": latest_trigger["_id"]},
        },
        sort={"_id": -1},
    )
    start_id = latest_close["_id"] if latest_close else OID_MIN
    return start_id, latest_trigger["_id"]


def _parts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_8811 = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter})
        is not None
    )
    has_any_102 = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": NEGATIVE_KEYS}, **win_filter}
        )
        is not None
    )
    return has_8811, has_any_102


def grade(coll, pid):
    parts = _parts(coll, pid)
    if parts is None:
        return "yellow"
    has_8811, has_any_102 = parts
    if not has_8811:
        return "yellow"
    return "yellow" if has_any_102 else "green"


def diagnose(coll, pid):
    out = {}
    parts = _parts(coll, pid)
    if parts is None:
        out["NO_TRIGGER"] = f"no {END_TRIGGER} trigger found — defaults to yellow"
        return out
    has_8811, has_any_102 = parts
    if not has_8811:
        out["MISSING_SUCCESS_NODE"] = (
            f"success node {SUCCESS_KEY} absent in window — did not complete the "
            f"infiltration glyph puzzle independently"
        )
    if has_any_102:
        out["TOO_MANY_NEGATIVES"] = (
            "negative feedback node present in window — needed more than 2 attempts "
            "to figure out the correct matches"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
