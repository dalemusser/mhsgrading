"""Reason codes for Unit 5 Point 1 — "If I Had a Nickel- Floors 1 & 2".

mhs-unit5-point1-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when any assist-path marker fired: 100:40
      (offer accepted), 100:41 (accepted execution), 100:43 (forced execution),
      100:46 (helped completion); attempt_number = incorrect arrangements, one
      attempt-indexed node each (100:33-39 and the forced node 100:43 — the
      5th wrong order that forces the assist is counted since 2026-09-24, as
      at U2P1/U2P4 and the aligned U3P4/U4P2).
  EXCESS_ATTEMPTS — triggered when no assist marker fired but a color negative
      did (100:38 / 100:39 / 100:43); attempt_number = incorrect + 1.

Assistance is detected from the assist nodes, never from 100:44's absence:
on the current build the projector does not move the tablets, so 100:44
("OnPlayerSolve") also fires after 100:46 ("OnAutoSolve") on the assisted
path (09-03-26-3 and 09-14-26-3). The colour is yellow on every assisted path
regardless, because 100:39 or 100:43 is itself a colour negative.

Window (start-and-end form since 2026-09-24): latest `questFinishEvent:43`
(end, inclusive), latest `questActiveEvent:43` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. A
started-but-unfinished attempt has no end → no code (dashboard pencil). Until
2026-09-24: latest start and latest end, yellow when the end preceded the
start (guard `latestEnd._id < latestStart._id`).

Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 100 unchanged: 18 nodes, same gates).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 5, "point": 1, "name": "If I Had a Nickel- Floors 1 & 2",
        "doc": "mhs-unit5-point1-grading.md"}

WINDOW_START_KEY = "questActiveEvent:43"
WINDOW_END_KEY = "questFinishEvent:43"

ASSIST_KEYS = [
    "DialogueNodeEvent:100:40",  # "Sure, I'm stuck" — offer accepted
    "DialogueNodeEvent:100:41",  # accepted-assist execution
    "DialogueNodeEvent:100:43",  # forced assist (5th attempt)
    "DialogueNodeEvent:100:46",  # DANI-helped completion ("OnAutoSolve")
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
    "DialogueNodeEvent:100:43",  # 5th attempt, any wrong — forces the assist (counted since 2026-09-24)
]


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, WINDOW_END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, WINDOW_START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Any assist-path marker in the window?
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 4) Count incorrect arrangements
    attempt_number = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": assisted, "attempt_number": attempt_number}


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) DANI's assist did not run (otherwise SOLVED_WITH_ASSIST applies)
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    # 4) A color negative fired — 4th-or-later submission was wrong
    has_color_neg = has_keys(coll, pid, COLOR_NEG_KEYS, f)
    # 5) Count incorrect arrangements
    neg_count = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": (not assisted) and has_color_neg, "attempt_number": neg_count + 1}


CODES = {
    "SOLVED_WITH_ASSIST": solved_with_assist,
    "EXCESS_ATTEMPTS": excess_attempts,
}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
