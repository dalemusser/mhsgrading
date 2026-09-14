"""Reason codes for Unit 3 Point 4 — "Forsaken Facility".

mhs-unit3-point4-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when DANI's assist executed (78:23) or the
      completion gate (78:24) is absent from a valid window;
      attempt_number = attempt-indexed feedback nodes fired.
  EXCESS_ATTEMPTS — triggered when the student completed the puzzle (gate
      present, no assist) but the color count (all 8 target keys) reached 3+;
      attempt_number = color count + 1.

Window: latest `questActiveEvent:18` (start, exclusive) .. latest
`DialogueNodeEvent:73:200` (end, inclusive); end must be after start.
"""

from rc_common import count_keys, gt_lte, has_keys, start_end_window

META = {"unit": 3, "point": 4, "name": "Forsaken Facility",
        "doc": "mhs-unit3-point4-grading.md"}

START_KEY = "questActiveEvent:18"
END_KEY = "DialogueNodeEvent:73:200"
GATE_KEY = "DialogueNodeEvent:78:24"    # completion marker (empty text)
ASSIST_KEY = "DialogueNodeEvent:78:23"  # DANI orders the pieces

NEGATIVE_KEYS = [
    "DialogueNodeEvent:78:4",   # 1st attempt, 1-2 wrong
    "DialogueNodeEvent:78:3",   # 1st attempt, 3-4 wrong
    "DialogueNodeEvent:78:7",   # 2nd attempt, any wrong (microscope hint)
    "DialogueNodeEvent:78:9",   # 3rd attempt, 1-2 wrong
    "DialogueNodeEvent:78:10",  # 3rd attempt, 3-4 wrong
    "DialogueNodeEvent:78:12",  # 4th attempt, 1-2 wrong
    "DialogueNodeEvent:78:18",  # 4th attempt, 3-4 wrong (assist offered)
]

COLOR_TARGET_KEYS = [
    "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
    "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
    "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23",
]


def attempt_window(coll, pid):
    # guard: !latestStart || !latestEnd || latestEnd._id <= latestStart._id
    return start_end_window(coll, pid, START_KEY, END_KEY, strict=True)


def solved_with_assist(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    assisted = has_keys(coll, pid, ASSIST_KEY, f)
    has_gate = has_keys(coll, pid, GATE_KEY, f)
    attempt_number = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": assisted or not has_gate, "attempt_number": attempt_number}


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    assisted = has_keys(coll, pid, ASSIST_KEY, f)
    has_gate = has_keys(coll, pid, GATE_KEY, f)
    color_count = count_keys(coll, pid, COLOR_TARGET_KEYS, f)
    return {"triggered": has_gate and not assisted and color_count >= 3,
            "attempt_number": color_count + 1}


CODES = {
    "SOLVED_WITH_ASSIST": solved_with_assist,
    "EXCESS_ATTEMPTS": excess_attempts,
}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
