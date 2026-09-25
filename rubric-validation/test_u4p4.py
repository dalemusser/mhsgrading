"""Test for Unit 4 Point 4 — "Alien Well Floor 5 + You Know the Drill".

Production rule (mhs-unit4-point4-grading.md): score-based, within the attempt
window.

    +1 if soilMachine floor 5 machine 1 TopRow count == 1 AND BottomRow count == 1
    +1 if soilMachine floor 5 machine 2 count == 1
    +2 if success_total > 0 and neg_total == 0
    +1 elif success_total > 0 and neg_total == 1
    green iff score > 2, else yellow.

Window (end-first form since 2026-09-24): anchor on the latest END
(`questActiveEvent:36`, which logs twice back-to-back — the latest absorbs the
duplicate); if missing => yellow. Take the latest START (`questActiveEvent:50`)
at `_id < latestEnd._id` (else ObjectId("000...")) as the exclusive window
start. Until 2026-09-24 the script took the latest start and the latest end and
returned yellow unless the end came after the start.

Keys (decision B3, applied 2026-09-24): SUCCESS_KEYS = 107:5 only (fourth floor,
clean water); NEG_KEYS = 107:2 / 107:3 / 107:4 / 107:6 (107:4 "middle" yields
contaminated water and the task continues). Conversation 107 re-verified
against the 2026-09-21 dialogue database (unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {
    "unit": 4,
    "point": 4,
    "name": "Alien Well Floor 5 + You Know the Drill",
}

START_KEY = "questActiveEvent:50"
END_KEY = "questActiveEvent:36"

SUCCESS_KEYS = ["DialogueNodeEvent:107:5"]
NEG_KEYS = [
    "DialogueNodeEvent:107:2",
    "DialogueNodeEvent:107:3",
    "DialogueNodeEvent:107:4",
    "DialogueNodeEvent:107:6",
]


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


def _score_parts(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    c_m1_top = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "soilMachine",
            "data.floor": "5",
            "data.machine": "1",
            "data.row": "TopRow",
            **win_filter,
        }
    )
    c_m1_bottom = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "soilMachine",
            "data.floor": "5",
            "data.machine": "1",
            "data.row": "BottomRow",
            **win_filter,
        }
    )
    c_m2_floor5 = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "soilMachine",
            "data.floor": "5",
            "data.machine": "2",
            **win_filter,
        }
    )
    success_total = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": SUCCESS_KEYS}, **win_filter}
    )
    neg_total = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )

    score = 0
    if c_m1_top == 1 and c_m1_bottom == 1:
        score += 1
    if c_m2_floor5 == 1:
        score += 1
    if success_total > 0 and neg_total == 0:
        score += 2
    elif success_total > 0 and neg_total == 1:
        score += 1

    attempt_time = c_m1_top + c_m1_bottom + c_m2_floor5
    return score, attempt_time, neg_total


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    score, _, _ = parts
    return "green" if score > 2 else "yellow"


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["NO_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    score, attempt_time, neg_total = parts
    out["_score"] = f"score={score} attempt_time={attempt_time} negative_feedback_number={neg_total}"
    if score <= 2:
        out["SCORE_BELOW_THRESHOLD"] = (
            f"score={score} (<= 2) — combined soil-machine and dialogue score too low"
        )
    if attempt_time > 3:
        out["TOO_MANY_ATTEMPTS"] = (
            f"attempt_time={attempt_time} (> 3) — too many fifth-floor soil machine interactions"
        )
    if neg_total > 0:
        out["BAD_FEEDBACK"] = (
            f"negative_feedback_number={neg_total} (> 0) — wrong drilling depths "
            f"before the clean-water depth"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
