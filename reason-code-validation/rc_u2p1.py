"""Reason codes for Unit 2 Point 1 — "Escape the Ruin".

mhs-unit2-point1-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when a forced-assist node (68:28 / 68:31)
      fired in the window; attempt_number = negative-feedback nodes (one per
      wrong submission).
  EXCESS_ATTEMPTS — triggered when the student solved on their own (68:29 in
      window, no forced-assist node) but needed 4+ wrong submissions;
      attempt_number = wrong submissions + 1.

Window: previous `questFinishEvent:21` (exclusive) .. latest (inclusive).
"""

from rc_common import count_keys, gt_lte, has_keys, latest_trigger_window

META = {"unit": 2, "point": 1, "name": "Escape the Ruin",
        "doc": "mhs-unit2-point1-grading.md"}

TRIGGER_KEY = "questFinishEvent:21"
SUCCESS_KEY = "DialogueNodeEvent:68:29"  # solved-on-their-own completion

ASSIST_KEYS = [
    "DialogueNodeEvent:68:28",
    "DialogueNodeEvent:68:31",
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
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Reason code triggers if a forced-assist node fired in the window
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
