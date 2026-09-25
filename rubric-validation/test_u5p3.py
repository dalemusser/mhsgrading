"""Test for Unit 5 Point 3 — "What Happened Here?".

Production rule (mhs-unit5-point3-grading.md): attempt-based negative-dialogue
count within the latest attempt window; green iff the count is < 4 (yellow iff
cnt >= 4). No success node is required.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`questFinishEvent:44`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:96:1`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the script took the latest
start and the latest end independently and returned yellow when the end
preceded the start (guard `!latestStart || !latestEnd || latestEnd._id < latestStart._id`).

NEGATIVE_KEYS = all 39 conversation-108 wrong-answer feedback nodes (extended
2026-09-17 with 63/64, 65/66, 68/69; re-verified 2026-09-24 against the
2026-09-21 dialogue database — conversation 108 unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 5, "point": 3, "name": "What Happened Here?"}

WINDOW_START_KEY = "DialogueNodeEvent:96:1"
WINDOW_END_KEY = "questFinishEvent:44"

NEGATIVE_KEYS = [
    "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
    "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
    "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
    "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
    "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:63",
    "DialogueNodeEvent:108:64", "DialogueNodeEvent:108:65", "DialogueNodeEvent:108:66",
    "DialogueNodeEvent:108:68", "DialogueNodeEvent:108:69", "DialogueNodeEvent:108:70",
    "DialogueNodeEvent:108:72", "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74",
    "DialogueNodeEvent:108:75", "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78",
    "DialogueNodeEvent:108:79", "DialogueNodeEvent:108:80", "DialogueNodeEvent:108:82",
    "DialogueNodeEvent:108:83", "DialogueNodeEvent:108:84", "DialogueNodeEvent:108:85",
    "DialogueNodeEvent:108:86", "DialogueNodeEvent:108:87", "DialogueNodeEvent:108:88",
    "DialogueNodeEvent:108:89", "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91",
]


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when no latest END trigger
    exists (=> yellow)."""
    # 1) Latest end anchor
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY}, sort={"_id": -1}
    )
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": WINDOW_START_KEY,
            "_id": {"$lt": latest_end["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = latest_start["_id"] if latest_start else ObjectId(OID_MIN)
    return window_start_id, latest_end["_id"]


def _count(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return None
    window_start_id, window_end_id = win
    # 3) Count flagged submissions inside the window
    return coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": {"$in": NEGATIVE_KEYS},
            "_id": {"$gt": window_start_id, "$lte": window_end_id},
        }
    )


def grade(coll, pid):
    cnt = _count(coll, pid)
    if cnt is None:
        return "yellow"
    return "yellow" if cnt >= 4 else "green"


def diagnose(coll, pid):
    out = {}
    cnt = _count(coll, pid)
    if cnt is None:
        out["NO_TRIGGER"] = f"no {WINDOW_END_KEY} trigger found — defaults to yellow"
        return out
    if cnt >= 4:
        out["WRONG_ARG_SELECTED"] = (
            f"negativeCount={cnt} (>=4) — too many wrong arguments before "
            f"submitting the correct one"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
