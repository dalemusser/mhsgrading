"""Reason codes for Unit 4 Point 4 — "Alien Well Floor 5 + You Know the Drill".

mhs-unit4-point4-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — `triggered` mirrors the CURRENT color formula
      verbatim (including 107:4 in SUCCESS_KEYS, flagged for review in the
      markdown): +1 if machine 1 has exactly one TopRow and one BottomRow
      change, +1 if machine 2 has exactly one change, +2/+1 for a success
      choice with 0/1 color-negative choices; yellow when score <= 2.
      machine_attempt_number = all fifth-floor canister changes;
      wrong_choice_number = honest count of wrong drill depths (107:2/3/4/6).

Window: latest `questActiveEvent:50` (start, exclusive) .. latest
`questActiveEvent:36` (end, inclusive); end must be after start.
"""

from rc_common import GAME, count_keys, gt_lte, start_end_window

META = {"unit": 4, "point": 4, "name": "Alien Well Floor 5 + You Know the Drill",
        "doc": "mhs-unit4-point4-grading.md"}

WINDOW_START_KEY = "questActiveEvent:50"
WINDOW_END_KEY = "questActiveEvent:36"

COLOR_SUCCESS_KEYS = ["DialogueNodeEvent:107:4", "DialogueNodeEvent:107:5"]
COLOR_NEG_KEYS = ["DialogueNodeEvent:107:2", "DialogueNodeEvent:107:3", "DialogueNodeEvent:107:6"]
WRONG_DEPTH_KEYS = [
    "DialogueNodeEvent:107:2",  # first floor — no water
    "DialogueNodeEvent:107:3",  # second floor — no water
    "DialogueNodeEvent:107:4",  # middle — contaminated water
    "DialogueNodeEvent:107:6",  # all the way down — bedrock
]


def attempt_window(coll, pid):
    # guard: !latestStart || !latestEnd || latestEnd._id <= latestStart._id
    return start_end_window(coll, pid, WINDOW_START_KEY, WINDOW_END_KEY, strict=True)


def _machine_count(coll, pid, row, machine, f):
    q = {
        "game": GAME, "playerId": pid, "eventType": "soilMachine",
        "data.floor": "5", "data.machine": machine,
        **f,
    }
    if row:
        q["data.row"] = row
    return coll.count_documents(q)


def score_below_threshold(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "machine_attempt_number": 0, "wrong_choice_number": 0}
    f = gt_lte(win)

    m1_top = _machine_count(coll, pid, "TopRow", "1", f)
    m1_bottom = _machine_count(coll, pid, "BottomRow", "1", f)
    m2 = _machine_count(coll, pid, None, "2", f)

    success_total = count_keys(coll, pid, COLOR_SUCCESS_KEYS, f)
    color_neg_total = count_keys(coll, pid, COLOR_NEG_KEYS, f)
    wrong_depths = count_keys(coll, pid, WRONG_DEPTH_KEYS, f)

    # Mirror the color formula exactly
    score = 0
    if m1_top == 1 and m1_bottom == 1:
        score += 1
    if m2 == 1:
        score += 1
    if success_total > 0 and color_neg_total == 0:
        score += 2
    elif success_total > 0 and color_neg_total == 1:
        score += 1

    return {
        "triggered": score <= 2,
        "machine_attempt_number": m1_top + m1_bottom + m2,
        "wrong_choice_number": wrong_depths,
    }


CODES = {"SCORE_BELOW_THRESHOLD": score_below_threshold}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
