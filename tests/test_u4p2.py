"""Test for Unit 4 Point 2 — "Infiltration Glyph + Alien Well Floors 1 & 2".

Production rule (mhs-unit4-point2-grading.md): within the latest attempt window
(previous `questActiveEvent:48` exclusive .. latest `questActiveEvent:48`
inclusive), green iff the success node `DialogueNodeEvent:88:11` is present AND
no negative feedback node is present. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {
    "unit": 4,
    "point": 2,
    "name": "Infiltration Glyph + Alien Well Floors 1 & 2",
    "expected": "green",
}

TRIGGER_KEY = "questActiveEvent:48"
SUCCESS_KEY = "DialogueNodeEvent:88:11"

NEGATIVE_KEYS = [
    "DialogueNodeEvent:102:9",
    "DialogueNodeEvent:102:10",
    "DialogueNodeEvent:102:12",
    "DialogueNodeEvent:102:18",
    "DialogueNodeEvent:102:23",
]


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_8811 = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": SUCCESS_KEY, **win_filter})
        is not None
    )
    if not has_8811:
        return "yellow"
    has_any_102 = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": NEGATIVE_KEYS}, **win_filter}
        )
        is not None
    )
    return "yellow" if has_any_102 else "green"


def diagnose(coll, pid):
    out = {}
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        out["NO_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
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
