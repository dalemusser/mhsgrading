"""Test for Unit 4 Point 3 — "Alien Well Floor 3 & 4".

Production rule (mhs-unit4-point3-grading.md): score-based on soilMachine
interaction counts, within the latest attempt window (previous
`questActiveEvent:50` exclusive .. latest `questActiveEvent:50` inclusive).

    floor3 = count of soilMachine (data.machine="1", data.floor="3") in window
    floor4 = count of soilMachine (data.machine="1", data.floor="4") in window
    score  = (1 if floor3 == 1 else 0)
           + (2 if floor4 == 1 else 1 if floor4 == 2 else 0)
    green iff score > 1, else yellow. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 4, "point": 3, "name": "Alien Well Floor 3 & 4", "expected": "green"}

TRIGGER_KEY = "questActiveEvent:50"
EVENT_TYPE = "soilMachine"


def _parts(coll, pid):
    """Returns (score, c_floor3, c_floor4) or None when no trigger."""
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    c_floor3 = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": EVENT_TYPE,
            "data.machine": "1",
            "data.floor": "3",
            **win_filter,
        }
    )
    c_floor4 = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": EVENT_TYPE,
            "data.machine": "1",
            "data.floor": "4",
            **win_filter,
        }
    )

    score = 0
    if c_floor3 == 1:
        score += 1
    if c_floor4 == 1:
        score += 2
    elif c_floor4 == 2:
        score += 1

    return score, c_floor3, c_floor4


def grade(coll, pid):
    parts = _parts(coll, pid)
    if parts is None:
        return "yellow"
    score, _, _ = parts
    return "green" if score > 1 else "yellow"


def diagnose(coll, pid):
    out = {}
    parts = _parts(coll, pid)
    if parts is None:
        out["NO_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    score, c_floor3, c_floor4 = parts
    out["_score"] = (
        f"score={score} floor3_attempts={c_floor3} floor4_attempts={c_floor4}"
    )
    if score <= 1:
        if c_floor3 > 1:
            out["TOO_MANY_ATTEMPTS_3"] = (
                f"floor3_attempts={c_floor3} (> 1) — interacted with the third-floor "
                f"soil machine more than the optimal one attempt"
            )
        if c_floor4 > 1:
            out["TOO_MANY_ATTEMPTS_4"] = (
                f"floor4_attempts={c_floor4} (> 1) — interacted with the fourth-floor "
                f"soil machine more than the optimal one attempt"
            )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
