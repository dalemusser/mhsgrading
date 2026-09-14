"""Reason codes for Unit 5 Point 1 — "If I Had a Nickel- Floors 1 & 2".

mhs-unit5-point1-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when any assist-path marker fired: 100:40
      (offer accepted), 100:41 (accepted execution), 100:43 (forced execution),
      100:46 (helped completion); attempt_number = incorrect arrangements.
  EXCESS_ATTEMPTS — triggered when no assist marker fired but a color negative
      did (100:38 / 100:39 / 100:43); attempt_number = incorrect + 1.

Window: latest `questActiveEvent:43` (start, exclusive) .. latest
`questFinishEvent:43` (end, inclusive); guard `latestEnd._id < latestStart._id`
(a started-but-unfinished attempt has no window → no code, dashboard pencil).
"""

from rc_common import count_keys, gt_lte, has_keys, start_end_window

META = {"unit": 5, "point": 1, "name": "If I Had a Nickel- Floors 1 & 2",
        "doc": "mhs-unit5-point1-grading.md"}

WINDOW_START_KEY = "questActiveEvent:43"
WINDOW_END_KEY = "questFinishEvent:43"

ASSIST_KEYS = [
    "DialogueNodeEvent:100:40",  # "Sure, I'm stuck" — offer accepted
    "DialogueNodeEvent:100:41",  # accepted-assist execution
    "DialogueNodeEvent:100:43",  # forced assist (5th attempt)
    "DialogueNodeEvent:100:46",  # DANI-helped completion
]

COLOR_NEG_KEYS = [
    "DialogueNodeEvent:100:38",  # 4th attempt, close
    "DialogueNodeEvent:100:39",  # 4th attempt, far (assist offered)
    "DialogueNodeEvent:100:43",  # 5th attempt, forced assist
]

NEGATIVE_KEYS = [
    "DialogueNodeEvent:100:33",  # 1st attempt, close
    "DialogueNodeEvent:100:34",  # 1st attempt, far
    "DialogueNodeEvent:100:35",  # 2nd attempt (evaporation-rate hint)
    "DialogueNodeEvent:100:36",  # 3rd attempt, close
    "DialogueNodeEvent:100:37",  # 3rd attempt, far (temperature hint)
    "DialogueNodeEvent:100:38",  # 4th attempt, close ("very close")
    "DialogueNodeEvent:100:39",  # 4th attempt, far (assist offered)
]


def attempt_window(coll, pid):
    return start_end_window(coll, pid, WINDOW_START_KEY, WINDOW_END_KEY, strict=False)


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 2) Any assist-path marker in the window?
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 3) Count incorrect arrangements
    attempt_number = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": assisted, "attempt_number": attempt_number}


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 2) DANI's assist did not run (otherwise SOLVED_WITH_ASSIST applies)
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 3) A color negative fired — 4th-or-later submission was wrong
    has_color_neg = has_keys(coll, pid, COLOR_NEG_KEYS, f)
    # 4) Count incorrect arrangements
    neg_count = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": (not assisted) and has_color_neg, "attempt_number": neg_count + 1}


CODES = {
    "SOLVED_WITH_ASSIST": solved_with_assist,
    "EXCESS_ATTEMPTS": excess_attempts,
}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
