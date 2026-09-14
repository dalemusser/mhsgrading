"""Reason codes for Unit 4 Point 2 — "Infiltration Glyph + Alien Well Floors 1 & 2".

mhs-unit4-point2-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when DANI's assist executed (102:23) in the
      window (never inferred from 88:11's absence — it fires on the assisted
      path too); attempt_number = incorrect arrangements.
  EXCESS_ATTEMPTS — triggered when no assist executed but a yellow key fired
      (3rd-or-later submission wrong); attempt_number = incorrect + 1.

Window: latest Unit-4 soil-key-puzzle close before the trigger (start,
exclusive; OID_MIN when none) .. latest `questActiveEvent:48` (end, inclusive).
"""

from rc_common import GAME, OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 4, "point": 2, "name": "Infiltration Glyph + Alien Well Floors 1 & 2",
        "doc": "mhs-unit4-point2-grading.md"}

TRIGGER_KEY = "questActiveEvent:48"
ASSIST_KEY = "DialogueNodeEvent:102:23"  # DANI orders the pieces

SOIL_KEY_EVENT_TYPE = "Soil Key Puzzle"
SOIL_KEY_END_STATUS = "Finished"
UNIT_4 = "^Unit 4"  # data.Unit is the scene name (currently "Unit 4 Dev")

YELLOW_KEYS = [
    "DialogueNodeEvent:102:9",   # 3rd attempt, 1-2 wrong
    "DialogueNodeEvent:102:10",  # 3rd attempt, 3-4 wrong
    "DialogueNodeEvent:102:12",  # 4th attempt, 1-2 wrong
    "DialogueNodeEvent:102:18",  # 4th attempt, 3-4 wrong (assist offered)
]

NEGATIVE_KEYS = [
    "DialogueNodeEvent:102:4",   # 1st attempt, 1-2 wrong
    "DialogueNodeEvent:102:3",   # 1st attempt, 3-4 wrong
    "DialogueNodeEvent:102:7",   # 2nd attempt, any wrong (particle-size hint)
    "DialogueNodeEvent:102:9",   # 3rd attempt, 1-2 wrong
    "DialogueNodeEvent:102:10",  # 3rd attempt, 3-4 wrong (rate-graph hint)
    "DialogueNodeEvent:102:12",  # 4th attempt, 1-2 wrong
    "DialogueNodeEvent:102:18",  # 4th attempt, 3-4 wrong (assist offered)
]


def attempt_window(coll, pid):
    # 1) Latest trigger (end anchor)
    latest_trigger = latest(coll, pid, TRIGGER_KEY)
    if not latest_trigger:
        return None
    # 2) Window start: latest Unit 4 soil key puzzle close before the trigger
    soil_key_close = coll.find_one(
        {
            "game": GAME, "playerId": pid,
            "eventType": SOIL_KEY_EVENT_TYPE,
            "data.Soil Key Puzzle Status": SOIL_KEY_END_STATUS,
            "data.Unit": {"$regex": UNIT_4},
            "_id": {"$lt": latest_trigger["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = soil_key_close["_id"] if soil_key_close else OID_MIN
    return window_start_id, latest_trigger["_id"]


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Assist executed?
    assisted = has_keys(coll, pid, ASSIST_KEY, f)
    # 4) Count incorrect arrangements
    attempt_number = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": assisted, "attempt_number": attempt_number}


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) DANI's assist did not execute (otherwise SOLVED_WITH_ASSIST applies)
    assisted = has_keys(coll, pid, ASSIST_KEY, f)
    # 4) A yellow key fired — 3rd-or-later submission was wrong
    has_yellow = has_keys(coll, pid, YELLOW_KEYS, f)
    # 5) Count incorrect arrangements
    neg_count = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": (not assisted) and has_yellow, "attempt_number": neg_count + 1}


CODES = {
    "SOLVED_WITH_ASSIST": solved_with_assist,
    "EXCESS_ATTEMPTS": excess_attempts,
}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
