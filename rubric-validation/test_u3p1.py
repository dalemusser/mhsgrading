"""Test for Unit 3 Point 1 — "Good Morning Cadet + Establishing a Foothold".

Production rule (mhs-unit3-point1-grading.md): count-based within the attempt
window.

    cnt = windowed count of TARGET_KEY (DialogueNodeEvent:10:30)
    green iff cnt > 1. No trigger => yellow.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`DialogueNodeEvent:11:22`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:10:1`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the window was (previous
`DialogueNodeEvent:11:22` exclusive .. latest `DialogueNodeEvent:11:22`
inclusive). Keys re-verified 2026-09-24 against the 2026-09-21 dialogue
database.
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {
    "unit": 3,
    "point": 1,
    "name": "Good Morning Cadet + Establishing a Foothold",
}

START_KEY = "DialogueNodeEvent:10:1"
END_KEY = "DialogueNodeEvent:11:22"
TARGET_KEY = "DialogueNodeEvent:10:30"


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


def grade(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    # 3) Count target occurrences within attempt window
    cnt = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": TARGET_KEY, **win_filter}
    )
    return "green" if cnt > 1 else "yellow"


def diagnose(coll, pid):
    out = {}
    win = _window(coll, pid)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
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
