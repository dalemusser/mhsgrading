"""Reason codes for Unit 3 Point 4 — "Forsaken Facility".

mhs-unit3-point4-grading.md, "## Reason Codes":

  SOLVED_WITH_ASSIST — triggered when an assist marker fired in the window
      (78:20 accepted offer, 78:21 "Activating holid projector", 78:23 forced
      assist on the 5th attempt) or the completion gate 78:24 is absent;
      attempt_number = attempt-indexed feedback nodes fired, one per wrong
      submission, 78:23 included (the 5th wrong order that forces the assist
      is counted since 2026-09-24, as at U2P1/U2P4). The accepted nodes
      were added 2026-09-24 (gates verified in the 2026-09-21 export; path not
      yet observed). On build 20260914- the projector does not move the pieces
      (log 09-14-26-3: two placements between 78:23 and 78:24), so 78:24 also
      fires after an assisted solve and can never signal independence.
  EXCESS_ATTEMPTS — triggered when the student completed the puzzle (gate
      present, no assist marker) but the color count (all 8 target keys)
      reached 3+; attempt_number = color count + 1.

Window (end-first form since 2026-09-24): latest `DialogueNodeEvent:73:200`
(end, inclusive), latest `questActiveEvent:18` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. Until
2026-09-24: latest start and latest end, end must follow start.
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 3, "point": 4, "name": "Forsaken Facility",
        "doc": "mhs-unit3-point4-grading.md"}

START_KEY = "questActiveEvent:18"
END_KEY = "DialogueNodeEvent:73:200"
GATE_KEY = "DialogueNodeEvent:78:24"    # "OnSolve" completion marker

ASSIST_KEYS = [
    "DialogueNodeEvent:78:20",  # accepted offer after the 4th attempt ("Sure. I'm stuck")
    "DialogueNodeEvent:78:21",  # DANI: "I have calculated the correct order... Activating holid projector."
    "DialogueNodeEvent:78:23",  # forced assist, 5th attempt
]

NEGATIVE_KEYS = [
    "DialogueNodeEvent:78:4",   # 1st attempt, 1-2 wrong
    "DialogueNodeEvent:78:3",   # 1st attempt, 3 wrong
    "DialogueNodeEvent:78:7",   # 2nd attempt, any wrong (microscope hint)
    "DialogueNodeEvent:78:9",   # 3rd attempt, 1-2 wrong
    "DialogueNodeEvent:78:10",  # 3rd attempt, 3 wrong
    "DialogueNodeEvent:78:12",  # 4th attempt, 1-2 wrong
    "DialogueNodeEvent:78:18",  # 4th attempt, 3 wrong (assist offered)
    "DialogueNodeEvent:78:23",  # 5th attempt, any wrong — forces the assist (counted since 2026-09-24)
]

COLOR_TARGET_KEYS = [
    "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
    "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
    "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23",
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
    # 3) Any assist marker (accepted or forced) inside the window
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
    has_gate = has_keys(coll, pid, GATE_KEY, f)
    attempt_number = count_keys(coll, pid, NEGATIVE_KEYS, f)
    return {"triggered": assisted or not has_gate, "attempt_number": attempt_number}


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Any assist marker (accepted or forced) inside the window
    assisted = has_keys(coll, pid, ASSIST_KEYS, f)
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
