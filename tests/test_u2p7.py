"""Test for Unit 2 Point 7 — "Which Watershed? Part II".

Production rule (mhs-unit2-point7-grading.md): within the latest attempt window
(previous `questFinishEvent:54` exclusive .. latest `questFinishEvent:54`
inclusive), green iff the success key is present AND neg_count <= 3. No trigger
=> yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 2, "point": 7, "name": "Which Watershed? Part II", "expected": "yellow"}

TRIGGER_KEY = "questFinishEvent:54"
SUCCESS_KEY = "DialogueNodeEvent:27:7"
THRESHOLD = 3

NEG_KEYS = [f"DialogueNodeEvent:27:{n}" for n in range(11, 31)]  # 27:11 .. 27:30


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
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
