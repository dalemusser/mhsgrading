"""Test for Unit 4 Point 6 — "Desert Delicacies".

Production rule (mhs-unit4-point6-grading.md): score-based on the latest camera
placement per garden box, within the attempt window.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`questFinishEvent:56`); if missing => yellow. Take the latest START
(`questActiveEvent:41`) at `_id < latestEnd._id` (else ObjectId("000...")) as
the exclusive window start. Until 2026-09-24 the script took the latest start
and the latest end and returned yellow when the end preceded the start
(guard `!latestStart || !latestEnd || latestEnd._id < latestStart._id`).

Box score: +1 each for
    Box 0 latest soilType == "Gravel"
    Box 1 latest soilType == "Sand"
    Box 2 latest soilType == "Clay"
(the 2026-08-31 update fixed the previously inverted box0/box2 mapping).

Dialogue-feedback fallback (2026-09-01 update, OR logic): box ids have shifted
between builds, so the score is additionally secured by Dani's review
feedback — dialogueScore = count of correct-soil feedback `DialogueNodeEvent:92:61`
after the latest review-start `DialogueNodeEvent:92:33` in the window (whole
window if 92:33 missing — the case when the player asks for the results through
the second-round node 92:36 instead), capped at 3.

    final score = max(box score, dialogueScore); green iff final score >= 2.

Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 92: review and feedback nodes unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 4, "point": 6, "name": "Desert Delicacies"}

WINDOW_START_KEY = "questActiveEvent:41"
WINDOW_END_KEY = "questFinishEvent:56"

# Verbatim from the Production Script (Attempt-Based) box -> expected soil checks.
EXPECTED_SOIL_BY_BOX = {"0": "Gravel", "1": "Sand", "2": "Clay"}

REVIEW_START_KEY = "DialogueNodeEvent:92:33"
CORRECT_FEEDBACK_KEY = "DialogueNodeEvent:92:61"


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when no latest END trigger
    exists (=> yellow)."""
    # 1) Latest end anchor
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY},
        sort={"_id": -1},
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


def _box_results(coll, pid):
    """Return (box_score, dialogue_score, dict boxId -> latest soilType or None)
    or None if no window."""
    win = _window(coll, pid)
    if win is None:
        return None
    start, end = win
    score = 0
    latest_answer = {}
    for box_id, expected_soil in EXPECTED_SOIL_BY_BOX.items():
        latest_box = coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventType": "TerasGardenBox",
                "data.actionType": "cameraPlaced",
                "data.boxId": box_id,
                "_id": {"$gt": start, "$lte": end},
            },
            sort={"_id": -1},
        )
        actual_soil = None
        if latest_box and latest_box.get("data"):
            actual_soil = latest_box["data"].get("soilType")
        latest_answer[box_id] = actual_soil
        if actual_soil == expected_soil:
            score += 1

    # Dialogue-feedback fallback: count 92:61 in the latest review round
    # (after the latest 92:33 in the window; whole window if 92:33 missing).
    latest_review = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": REVIEW_START_KEY,
         "_id": {"$gt": start, "$lte": end}},
        sort={"_id": -1},
    )
    fb_start = latest_review["_id"] if latest_review else start
    dialogue_score = min(3, coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": CORRECT_FEEDBACK_KEY,
         "_id": {"$gt": fb_start, "$lte": end}}
    ))
    return score, dialogue_score, latest_answer


def grade(coll, pid):
    res = _box_results(coll, pid)
    if res is None:
        return "yellow"
    box_score, dialogue_score, _ = res
    return "green" if max(box_score, dialogue_score) >= 2 else "yellow"


def diagnose(coll, pid):
    out = {}
    res = _box_results(coll, pid)
    if res is None:
        out["NO_TRIGGER"] = f"no {WINDOW_END_KEY} trigger found — defaults to yellow"
        return out
    box_score, dialogue_score, latest_answer = res
    wrong_box_ids = [
        b for b, exp in EXPECTED_SOIL_BY_BOX.items() if latest_answer.get(b) != exp
    ]
    out["_score"] = (
        f"box_score={box_score} dialogue_score={dialogue_score} "
        f"final={max(box_score, dialogue_score)} wrongTime={len(wrong_box_ids)}"
    )
    if max(box_score, dialogue_score) < 2:
        details = ", ".join(
            f"box {b}: expected {EXPECTED_SOIL_BY_BOX[b]}, got {latest_answer.get(b)}"
            for b in wrong_box_ids
        )
        out["WRONG_CHOISE_SELECTED"] = (
            f"wrongTime={len(wrong_box_ids)} (correct boxes < 2, correct-soil "
            f"feedback dialogues = {dialogue_score}) — {details}"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
