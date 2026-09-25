"""Reason codes for Unit 2 Point 4 — "Investigate the Temple".

mhs-unit2-point4-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when an assist marker fired in the window:
      74:18 (accepted offer after the 5th wrong submission), 74:20 (forced
      assist on the 6th wrong submission) or 74:22 "SolvedHelp" (the
      DANI-completed outcome node). attempt_number = feedback nodes (one per
      wrong submission, 74:20 included since 2026-09-24, as at U2P1).
  EXCESS_ATTEMPTS — triggered when the student solved independently (74:21,
      no assist marker) but the 5th submission was wrong (74:16 / 74:17);
      attempt_number = wrong submissions + 1.

2026-09-24 review against the 2026-09-21 dialogue database: 74:25 (the former
video-link assist variant) no longer exists and was removed; both assisted
paths now run 18 -> 26 -> 22 and 20 -> 26 -> 22 (26 is an empty structural
node). The export now carries explicit gates: Attempts == 1 -> 4; == 2 -> 5
(1-2 wrong) / 6 (3-5 wrong); == 3 -> 9 / 10; == 4 -> 15; == 5 -> 16 / 17;
>= 6 -> 20.

Window (start-and-end form since 2026-09-24): latest `DialogueNodeEvent:23:17`
(end, inclusive), latest `DialogueNodeEvent:22:18` before it (start,
exclusive; OID_MIN when none) — the same window as the production color
script. Until 2026-09-24: previous `23:17` (exclusive) .. latest (inclusive).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 2, "point": 4, "name": "Investigate the Temple",
        "doc": "mhs-unit2-point4-grading.md"}

START_KEY = "DialogueNodeEvent:22:18"
END_KEY = "DialogueNodeEvent:23:17"
SUCCESS_KEY = "DialogueNodeEvent:74:21"  # solved-on-their-own completion

ASSIST_KEYS = [
    "DialogueNodeEvent:74:18",  # "Sure. I'm stuck" — accepted assist offer (5th attempt)
    "DialogueNodeEvent:74:20",  # forced assist, 6th wrong submission: DANI orders the pieces
    "DialogueNodeEvent:74:22",  # "SolvedHelp" — DANI-helped completion
]

FIFTH_ATTEMPT_KEYS = [
    "DialogueNodeEvent:74:16",  # 5th attempt, 1-2 wrong
    "DialogueNodeEvent:74:17",  # 5th attempt, 3-5 wrong (assist offered)
]

NEGATIVE_KEYS = [
    "DialogueNodeEvent:74:4",   # 1st attempt, any wrong   (gate: Attempts == 1)
    "DialogueNodeEvent:74:5",   # 2nd attempt, 1-2 wrong   (gate: Attempts == 2, IncorrectInLast 1-2)
    "DialogueNodeEvent:74:6",   # 2nd attempt, 3-5 wrong   (gate: Attempts == 2, IncorrectInLast 3-5)
    "DialogueNodeEvent:74:9",   # 3rd attempt, 1-2 wrong
    "DialogueNodeEvent:74:10",  # 3rd attempt, 3-5 wrong (video offered)
    "DialogueNodeEvent:74:15",  # 4th attempt, any wrong
    "DialogueNodeEvent:74:16",  # 5th attempt, 1-2 wrong
    "DialogueNodeEvent:74:17",  # 5th attempt, 3-5 wrong (assist offered)
    "DialogueNodeEvent:74:20",  # 6th wrong submission (gate: Attempts >= 6) — DANI takes over (added 2026-09-24)
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
