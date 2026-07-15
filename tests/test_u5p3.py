"""Test for Unit 5 Point 3 — "What Happened Here?".

Production rule (mhs-unit5-point3-grading.md): attempt-based negative-dialogue
count within the latest attempt window. The window is anchored on the latest
START (`DialogueNodeEvent:96:1`) and latest END (`questFinishEvent:44`) found
independently; if either is missing or the end precedes the start => yellow.
Inside the window green iff the negative count is < 4 (yellow iff cnt >= 4).
"""

from mhs_harness import GAME

META = {"unit": 5, "point": 3, "name": "What Happened Here?", "expected": "green"}

WINDOW_START_KEY = "DialogueNodeEvent:96:1"
WINDOW_END_KEY = "questFinishEvent:44"

NEGATIVE_KEYS = [
    "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33",
    "DialogueNodeEvent:108:37", "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:41",
    "DialogueNodeEvent:108:47", "DialogueNodeEvent:108:53", "DialogueNodeEvent:108:54",
    "DialogueNodeEvent:108:55", "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:60",
    "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:62", "DialogueNodeEvent:108:70",
    "DialogueNodeEvent:108:72", "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74",
    "DialogueNodeEvent:108:75", "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78",
    "DialogueNodeEvent:108:79", "DialogueNodeEvent:108:80", "DialogueNodeEvent:108:82",
    "DialogueNodeEvent:108:83", "DialogueNodeEvent:108:84", "DialogueNodeEvent:108:85",
    "DialogueNodeEvent:108:86", "DialogueNodeEvent:108:87", "DialogueNodeEvent:108:88",
    "DialogueNodeEvent:108:89", "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91",
]


def _window(coll, pid):
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_START_KEY}, sort={"_id": -1}
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY}, sort={"_id": -1}
    )
    if not latest_start or not latest_end or latest_end["_id"] < latest_start["_id"]:
        return None
    return latest_start["_id"], latest_end["_id"]


def _count(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return None
    window_start_id, window_end_id = win
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
        out["NO_TRIGGER"] = (
            f"no {WINDOW_END_KEY}/{WINDOW_START_KEY} attempt window found — "
            f"defaults to yellow"
        )
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
