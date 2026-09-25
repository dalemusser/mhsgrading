"""Test for Unit 3 Point 5 — "Plant the Superfruit Seeds".

Production rule (mhs-unit3-point5-grading.md): weighted score within the
attempt window.

    pos_count = windowed count of DialogueNodeEvent:73:163
    neg_count = windowed count of NEG_KEYS
    sum_score = (pos_count * 1.0) - (neg_count * 0.5)
    green iff sum_score >= 2.5 (i.e. not sum_score < 2.5). No trigger => yellow.
    (2.5 = at most one wrong planting out of four; decision A5, 2026-09-21.)

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`DialogueNodeEvent:10:194`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:73:200`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the window was (previous
`DialogueNodeEvent:10:194` exclusive .. latest `DialogueNodeEvent:10:194`
inclusive). Keys re-verified 2026-09-24 against the 2026-09-21 dialogue
database (conversation 73 unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 3, "point": 5, "name": "Plant the Superfruit Seeds"}

START_KEY = "DialogueNodeEvent:73:200"
END_KEY = "DialogueNodeEvent:10:194"
POS_KEY = "DialogueNodeEvent:73:163"
NEG_KEYS = [
    "DialogueNodeEvent:73:164",
    "DialogueNodeEvent:73:168",
    "DialogueNodeEvent:73:171",
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
    # 3) Counts inside the window
    pos_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": POS_KEY, **win_filter}
    )
    neg_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    sum_score = (pos_count * 1.0) - (neg_count * 0.5)
    return pos_count, neg_count, sum_score


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    _, _, sum_score = parts
    return "yellow" if sum_score < 2.5 else "green"


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    pos_count, neg_count, sum_score = parts
    out["_score"] = (
        f"pos_count={pos_count} neg_count={neg_count} sum_score={sum_score}"
    )
    if neg_count > 1:
        out["TOO_MANY_NEGATIVES"] = (
            f"attempts_number={neg_count} (> 1) — planted super-fruit seeds into too "
            f"many wrong spots"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
