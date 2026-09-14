"""Reason codes for Unit 2 Point 4 — "Investigate the Temple".

mhs-unit2-point4-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when an assist marker (74:18 accepted offer,
      74:20 / 74:25 DANI orders the pieces, 74:22 helped completion) fired in
      the window; attempt_number = feedback nodes (one per wrong submission).
  EXCESS_ATTEMPTS — triggered when the student solved independently (74:21,
      no assist marker) but the 5th submission was wrong (74:16 / 74:17);
      attempt_number = wrong submissions + 1.

Window: previous `DialogueNodeEvent:23:17` (exclusive) .. latest (inclusive).
"""

from rc_common import count_keys, gt_lte, has_keys, latest_trigger_window

META = {"unit": 2, "point": 4, "name": "Investigate the Temple",
        "doc": "mhs-unit2-point4-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:23:17"
SUCCESS_KEY = "DialogueNodeEvent:74:21"  # solved-on-their-own completion

ASSIST_KEYS = [
    "DialogueNodeEvent:74:18",  # "Sure. I'm stuck" — accepted assist offer
    "DialogueNodeEvent:74:20",  # DANI orders the pieces
    "DialogueNodeEvent:74:22",  # DANI-helped completion
    "DialogueNodeEvent:74:25",  # DANI orders the pieces (video-link variant)
]

FIFTH_ATTEMPT_KEYS = [
    "DialogueNodeEvent:74:16",  # 5th attempt, 2-3 wrong
    "DialogueNodeEvent:74:17",  # 5th attempt, >3 wrong (assist offered)
]

NEGATIVE_KEYS = [
    "DialogueNodeEvent:74:4",   # 1st attempt, any wrong
    "DialogueNodeEvent:74:5",   # 2nd attempt, 2-3 wrong
    "DialogueNodeEvent:74:6",   # 2nd attempt, >3 wrong
    "DialogueNodeEvent:74:9",   # 3rd attempt, 2-3 wrong
    "DialogueNodeEvent:74:10",  # 3rd attempt, >3 wrong (video offered)
    "DialogueNodeEvent:74:15",  # 4th attempt, any wrong
    "DialogueNodeEvent:74:16",  # 5th attempt, 2-3 wrong
    "DialogueNodeEvent:74:17",  # 5th attempt, >3 wrong (assist offered)
]


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Reason code triggers if any assist marker fired in the window
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
    # 4) DANI did not step in (otherwise SOLVED_WITH_ASSIST applies instead)
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 5) The 5th submission was wrong — success required 6+ attempts
    fifth_wrong = has_keys(coll, pid, FIFTH_ATTEMPT_KEYS, f)
    # 6) Count incorrect submissions (one feedback node each)
    negative_count = count_keys(coll, pid, NEGATIVE_KEYS, f)
    triggered = solved_self and not assisted and fifth_wrong
    return {"triggered": triggered, "attempt_number": negative_count + 1}


CODES = {
    "SOLVED_WITH_ASSIST": solved_with_assist,
    "EXCESS_ATTEMPTS": excess_attempts,
}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
