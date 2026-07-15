"""Test for Unit 3 Point 1 — "Good Morning Cadet + Establishing a Foothold".

Production rule (mhs-unit3-point1-grading.md): count-based, within the latest
attempt window (previous `DialogueNodeEvent:11:22` exclusive .. latest
`DialogueNodeEvent:11:22` inclusive).

    cnt = windowed count of TARGET_KEY (DialogueNodeEvent:10:30)
    green iff cnt > 1. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {
    "unit": 3,
    "point": 1,
    "name": "Good Morning Cadet + Establishing a Foothold",
    "expected": "green",
}

TRIGGER_KEY = "DialogueNodeEvent:11:22"
TARGET_KEY = "DialogueNodeEvent:10:30"


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": TARGET_KEY, **win_filter}
    )
    return "green" if cnt > 1 else "yellow"


def diagnose(coll, pid):
    out = {}
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": TARGET_KEY, **win_filter}
    )
    # wrongCount = max(0, 3 - cnt) per the windowed reason script.
    wrong_count = max(0, 3 - cnt)
    out["_score"] = f"cnt={cnt} wrong_count={wrong_count}"
    if wrong_count >= 2:
        out["TOO_MANY_NEGATIVES"] = (
            f"attempt_number={wrong_count} (>= 2) — selected the wrong river too many "
            f"times while identifying the direction of water flow"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
