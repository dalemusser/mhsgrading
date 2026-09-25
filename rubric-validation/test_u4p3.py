"""Test for Unit 4 Point 3 — "Alien Well Floor 3 & 4".

Production rule (mhs-unit4-point3-grading.md): score-based on soilMachine
interaction counts, within the attempt window.

    floor3 = count of soilMachine (data.machine="1", data.floor="3") in window
    floor4 = count of soilMachine (data.machine="1", data.floor="4") in window
    score  = (1 if floor3 == 1 else 0)
           + (2 if floor4 == 1 else 1 if floor4 == 2 else 0)
    green iff score > 1, else yellow. No trigger => yellow.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`questActiveEvent:50`); if missing => yellow. Take the latest START
(`questActiveEvent:48`) at `_id < latestEnd._id` (else ObjectId("000...")) as
the exclusive window start. Until 2026-09-24 the window was (previous
`questActiveEvent:50` exclusive .. latest `questActiveEvent:50` inclusive).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 4, "point": 3, "name": "Alien Well Floor 3 & 4"}

START_KEY = "questActiveEvent:48"
END_KEY = "questActiveEvent:50"
EVENT_TYPE = "soilMachine"


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
    return window_start_id, latest_end["_id"]


def _parts(coll, pid):
    """Returns (score, c_floor3, c_floor4) or None when no trigger."""
    win = _window(coll, pid)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    # 3) Count soilMachine interactions inside attempt window
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
        out["NO_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
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
