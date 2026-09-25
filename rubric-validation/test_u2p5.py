"""Test for Unit 2 Point 5 — "Classified Information".

Production rule (mhs-unit2-point5-grading.md): within the attempt window count
POS_KEYS and NEG_KEYS, compute score = pos_count - (neg_count / 3.0). Green iff
score >= 4. Window (start-and-end form since 2026-09-24): anchor on the latest
END (`DialogueNodeEvent:23:42`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:23:17`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the window was (previous
`DialogueNodeEvent:23:42` exclusive .. latest `DialogueNodeEvent:23:42`
inclusive).

The 2026-08-31 grading-logic update remapped the key sets:
POS +140/142/143/146/147/148 -171; NEG +137/144/145 -190. Keys re-verified
2026-09-24 against the 2026-09-21 dialogue database (conversation 26 unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 2, "point": 5, "name": "Classified Information"}

START_KEY = "DialogueNodeEvent:23:17"
END_KEY = "DialogueNodeEvent:23:42"
THRESHOLD = 4

POS_KEYS = [f"DialogueNodeEvent:26:{n}" for n in (
    140, 142, 143, 146, 147, 148, 165, 166, 167, 168, 169, 170, 172, 173,
    174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186)]

NEG_KEYS = [f"DialogueNodeEvent:26:{n}" for n in (
    137, 144, 145, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198,
    199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211)]


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
    window_end_id = latest_end["_id"]
    return window_start_id, window_end_id


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    # 3) Count POS/NEG inside window
    pos_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
    )
    neg_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    score = pos_count - (neg_count / 3.0)
    return "green" if score >= THRESHOLD else "yellow"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    # TOO_MANY_NEGATIVES: wrong_number = count of incorrect argument selections
    wrong_number = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    pos_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
    )
    score = pos_count - (wrong_number / 3.0)
    if score < THRESHOLD:
        out["TOO_MANY_NEGATIVES"] = (
            f"wrong_number={wrong_number} (score={score:.2f} < {THRESHOLD}) — too "
            f"many incorrect attempts identifying argument parts"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
