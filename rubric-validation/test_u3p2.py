"""Test for Unit 3 Point 2 — "Pollution Solution".

Production rule (mhs-unit3-point2-grading.md): score-based with capped
penalties, within the attempt window.

    c27  = windowed count of DialogueNodeEvent:11:27
    c29  = windowed count of DialogueNodeEvent:11:29
    c230 = windowed count of DialogueNodeEvent:11:230
    cSum = c29 + c230
    score = 5 - cappedPenalty(c27) - cappedPenalty(cSum)
    cappedPenalty(cnt): 0 if <=1, 1 if <=3, else 2
    green iff score >= 3 (i.e. not score < 3). No trigger => yellow.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`DialogueNodeEvent:11:34`); if missing => yellow. Take the latest START
(`questActiveEvent:17`) at `_id < latestEnd._id` (else ObjectId("000...")) as
the exclusive window start. Until 2026-09-24 the window was (previous
`DialogueNodeEvent:11:34` exclusive .. latest `DialogueNodeEvent:11:34`
inclusive). Keys re-verified 2026-09-24 against the 2026-09-21 dialogue
database.
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 3, "point": 2, "name": "Pollution Solution"}

START_KEY = "questActiveEvent:17"
END_KEY = "DialogueNodeEvent:11:34"
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
    # 3) Category counts inside the window
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
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
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
