"""Reason codes for Unit 2 Point 1 — "Escape the Ruin".

mhs-unit2-point1-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when DANI completed the puzzle in the window,
      forced (68:28 / 68:31) or accepted (offer answered "Sure. I'm stuck"
      68:24 / 68:32, then DANI places the pieces 68:26 / 68:34 — verified in
      log 09-14-26-3, where 68:29 never fires on that path) or by the
      "SolvedHelp" outcome node 68:30 (added 2026-09-23; the game's own
      DANI-completed counterpart of 68:29); attempt_number =
      negative-feedback nodes (one per wrong submission).
  EXCESS_ATTEMPTS — triggered when the student solved on their own (68:29 in
      window, no assist node of either kind) but needed 4+ wrong submissions;
      attempt_number = wrong submissions + 1. The >= 4 threshold mirrors the
      color rule (yellow nodes = 4th-attempt feedback and later); re-verified
      2026-09-23 against builds 20260902-12353 and 20260914-.

Window (start-and-end form since 2026-09-23): latest `questFinishEvent:21`
(end, inclusive), latest `DialogueNodeEvent:18:1` before it (start,
exclusive; OID_MIN when none) — the same window as the production color
script. Until 2026-09-23: previous `questFinishEvent:21` (exclusive) ..
latest (inclusive).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 2, "point": 1, "name": "Escape the Ruin",
        "doc": "mhs-unit2-point1-grading.md"}

START_KEY = "DialogueNodeEvent:18:1"
END_KEY = "questFinishEvent:21"
SUCCESS_KEY = "DialogueNodeEvent:68:29"  # solved-on-their-own completion

ASSIST_KEYS = [
    "DialogueNodeEvent:68:24",  # accepted offer after 4th attempt ("Sure. I'm stuck")
    "DialogueNodeEvent:68:26",  # DANI places the pieces (accepted after 4th attempt)
    "DialogueNodeEvent:68:28",  # forced assist, 5th attempt, >3 wrong
    "DialogueNodeEvent:68:31",  # forced assist, 6th attempt, any wrong
    "DialogueNodeEvent:68:32",  # accepted offer after 5th attempt ("Sure. I'm stuck")
    "DialogueNodeEvent:68:34",  # DANI places the pieces (accepted after 5th attempt)
    "DialogueNodeEvent:68:30",  # "SolvedHelp" outcome node: DANI completed the puzzle on any
                                # assisted path (added 2026-09-23; fires instead of 68:29 on
                                # build 20260914-)
]

NEGATIVE_KEYS = [
    "DialogueNodeEvent:68:4",   # 1st attempt, 2-3 wrong
    "DialogueNodeEvent:68:5",   # 1st attempt, >3 wrong
    "DialogueNodeEvent:68:6",   # 2nd attempt, 2-3 wrong
    "DialogueNodeEvent:68:7",   # 2nd attempt, >3 wrong
    "DialogueNodeEvent:68:17",  # 3rd attempt, 2-3 wrong
    "DialogueNodeEvent:68:18",  # 3rd attempt, >3 wrong
    "DialogueNodeEvent:68:22",  # 4th attempt, 2-3 wrong
    "DialogueNodeEvent:68:23",  # 4th attempt, >3 wrong (assist offered)
    "DialogueNodeEvent:68:27",  # 5th attempt, 2-3 wrong (assist offered)
    "DialogueNodeEvent:68:28",  # 5th attempt, >3 wrong (DANI assists)
    "DialogueNodeEvent:68:31",  # 6th attempt, any wrong (DANI assists)
]


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Reason code triggers if any assist node (forced or accepted) fired in the window
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 4) attempt_number: count negative-feedback nodes in the window
    attempt_number = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": assisted, "attempt_number": attempt_number}


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Student reached the solved-on-their-own completion
    solved_self = has_keys(coll, pid, SUCCESS_KEY, f)
    # 4) DANI did not take over (otherwise SOLVED_WITH_ASSIST applies instead)
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 5) Count incorrect submissions (one negative-feedback node each)
    negative_count = count_keys(coll, pid, NEGATIVE_KEYS, f)
    # 6) 4+ wrong submissions means success came on attempt 5 or later
    triggered = solved_self and not assisted and negative_count >= 4
    return {"triggered": triggered, "attempt_number": negative_count + 1}


CODES = {
    "SOLVED_WITH_ASSIST": solved_with_assist,
    "EXCESS_ATTEMPTS": excess_attempts,
}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
