"""Reason codes for Unit 4 Point 6 — "Desert Delicacies".

mhs-unit4-point6-grading.md, "## Reason Codes":

  WRONG_SOIL_SELECTED — mirrors the production color rule verbatim: per-box
      latest cameraPlaced soil (Box 0 = Gravel, 1 = Sand, 2 = Clay) with the
      dialogue-feedback fallback (92:61 count after the latest 92:33 in the
      window, capped at 3), final score = max of both; triggered when < 2.
      wrong_box_summary lists the boxes whose latest placement is wrong or
      missing; wrong_box_number = their count.

Window: latest `questActiveEvent:41` (start, exclusive) .. latest
`questFinishEvent:56` (end, inclusive); guard `latestEnd._id < latestStart._id`.
"""

from rc_common import GAME, gt_lte, latest, start_end_window

META = {"unit": 4, "point": 6, "name": "Desert Delicacies",
        "doc": "mhs-unit4-point6-grading.md"}

WINDOW_START_KEY = "questActiveEvent:41"
WINDOW_END_KEY = "questFinishEvent:56"

EXPECTED_SOIL_BY_BOX = {"0": "Gravel", "1": "Sand", "2": "Clay"}
BOX_LABELS = {"0": "the first box", "1": "the second box", "2": "the third box"}

REVIEW_START_KEY = "DialogueNodeEvent:92:33"
CORRECT_FEEDBACK_KEY = "DialogueNodeEvent:92:61"


def attempt_window(coll, pid):
    # guard: !latestStart || !latestEnd || latestEnd._id < latestStart._id
    return start_end_window(coll, pid, WINDOW_START_KEY, WINDOW_END_KEY, strict=False)


def wrong_soil_selected(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_box_number": 0, "wrong_box_summary": ""}
    start_id, end_id = win
    f = gt_lte(win)

    box_score = 0
    wrong_parts = []
    for box_id, expected in EXPECTED_SOIL_BY_BOX.items():
        latest_placement = coll.find_one(
            {
                "game": GAME, "playerId": pid,
                "eventType": "TerasGardenBox",
                "data.actionType": "cameraPlaced",
                "data.boxId": box_id,
                **f,
            },
            sort={"_id": -1},
        )
        actual = (latest_placement["data"].get("soilType")
                  if latest_placement and latest_placement.get("data") else None)
        if actual == expected:
            box_score += 1
        elif actual:
            wrong_parts.append(f"{BOX_LABELS[box_id]} (chose {actual}, needs {expected})")
        else:
            wrong_parts.append(f"{BOX_LABELS[box_id]} (no camera placement recorded, needs {expected})")

    # Dialogue-feedback fallback, mirror of the color script
    latest_review = latest(coll, pid, REVIEW_START_KEY, f)
    feedback_start_id = latest_review["_id"] if latest_review else start_id
    dialogue_score = min(3, coll.count_documents({
        "game": GAME, "playerId": pid,
        "eventKey": CORRECT_FEEDBACK_KEY,
        "_id": {"$gt": feedback_start_id, "$lte": end_id},
    }))

    final_score = max(box_score, dialogue_score)

    return {
        "triggered": final_score < 2,
        "wrong_box_number": len(wrong_parts),
        "wrong_box_summary": " and ".join(wrong_parts),
    }


CODES = {"WRONG_SOIL_SELECTED": wrong_soil_selected}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
