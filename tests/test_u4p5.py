"""Test for Unit 4 Point 5 — "Saving Cadet Anderson".

Production rule (mhs-unit4-point5-grading.md): within the latest attempt window
(previous `questActiveEvent:41` exclusive .. latest `questActiveEvent:41`
inclusive), green iff a POS (success) key is present AND neg count < 3. No
trigger => yellow; missing success node => yellow; neg count >= 3 => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 4, "point": 5, "name": "Saving Cadet Anderson", "expected": "green"}

TRIGGER_KEY = "questActiveEvent:41"

POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"]

NEG_KEYS = [
    "DialogueNodeEvent:90:25", "DialogueNodeEvent:90:37", "DialogueNodeEvent:90:39",
    "DialogueNodeEvent:90:45", "DialogueNodeEvent:90:47", "DialogueNodeEvent:90:52",
    "DialogueNodeEvent:90:54", "DialogueNodeEvent:90:55", "DialogueNodeEvent:90:56",
    "DialogueNodeEvent:90:58", "DialogueNodeEvent:90:59", "DialogueNodeEvent:90:60",
    "DialogueNodeEvent:90:61",
]

THRESHOLD = 3  # cnt >= 3 ? "yellow" : "green"


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_trigger = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
        )
        is not None
    )
    if not has_trigger:
        return "yellow"
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    return "yellow" if cnt >= THRESHOLD else "green"


def diagnose(coll, pid):
    out = {}
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        out["NO_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
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
