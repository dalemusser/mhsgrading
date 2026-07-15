"""Test for Unit 3 Point 2 — "Pollution Solution".

Production rule (mhs-unit3-point2-grading.md): score-based with capped
penalties, within the latest attempt window (previous `DialogueNodeEvent:11:34`
exclusive .. latest `DialogueNodeEvent:11:34` inclusive).

    c27  = windowed count of DialogueNodeEvent:11:27
    c29  = windowed count of DialogueNodeEvent:11:29
    c230 = windowed count of DialogueNodeEvent:11:230
    cSum = c29 + c230
    score = 5 - cappedPenalty(c27) - cappedPenalty(cSum)
    cappedPenalty(cnt): 0 if <=1, 1 if <=3, else 2
    green iff score >= 3 (i.e. not score < 3). No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 3, "point": 2, "name": "Pollution Solution", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:11:34"
C27_KEY = "DialogueNodeEvent:11:27"
C29_KEY = "DialogueNodeEvent:11:29"
C230_KEY = "DialogueNodeEvent:11:230"

REMINDING_KEYS = [
    "DialogueNodeEvent:11:27",
    "DialogueNodeEvent:11:29",
    "DialogueNodeEvent:11:230",
]


def _capped_penalty(cnt):
    if cnt <= 1:
        return 0
    if cnt <= 3:
        return 1
    return 2


def _score_parts(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    c27 = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": C27_KEY, **win_filter}
    )
    c29 = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": C29_KEY, **win_filter}
    )
    c230 = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": C230_KEY, **win_filter}
    )
    c_sum = c29 + c230
    score = 5
    score -= _capped_penalty(c27)
    score -= _capped_penalty(c_sum)
    return c27, c29, c230, c_sum, score


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    *_, score = parts
    return "yellow" if score < 3 else "green"


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    c27, c29, c230, c_sum, score = parts
    reminding_count = c27 + c29 + c230
    out["_score"] = (
        f"c27={c27} c29={c29} c230={c230} cSum={c_sum} score={score} "
        f"reminding_count={reminding_count}"
    )
    if reminding_count > 6:
        out["BAD_FEEDBACK"] = (
            f"attempt_number={reminding_count} (> 6) — repeated reminding dialogues "
            f"regarding redundant sensor usage"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
