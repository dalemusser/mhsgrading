"""Reason codes for Unit 4 Point 4 — "Alien Well Floor 5 + You Know the Drill".

mhs-unit4-point4-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — `triggered` mirrors the color formula verbatim:
      +1 if machine 1 has exactly one TopRow and one BottomRow change, +1 if
      machine 2 has exactly one change, +2 / +1 for the correct depth (107:5,
      the only clean-water outcome) with 0 / 1 wrong depths; yellow when
      score <= 2. Since 2026-09-24 (decision B3) 107:4 "middle" is a wrong
      depth like 2, 3 and 6, so wrong_choice_number equals the color rule's
      negative count. machine_attempt_number = all fifth-floor canister
      changes.

Window (end-first form since 2026-09-24): latest `questActiveEvent:36` (end,
inclusive; logs twice back-to-back, the latest absorbs the duplicate), latest
`questActiveEvent:50` before it (start, exclusive; OID_MIN when none) — the
same window as the production color script. Until 2026-09-24: latest start and
latest end, end must follow start.
"""

from rc_common import GAME, OID_MIN, count_keys, gt_lte, latest

META = {"unit": 4, "point": 4, "name": "Alien Well Floor 5 + You Know the Drill",
        "doc": "mhs-unit4-point4-grading.md"}

START_KEY = "questActiveEvent:50"
END_KEY = "questActiveEvent:36"

SUCCESS_KEYS = ["DialogueNodeEvent:107:5"]   # fourth floor — clean water
NEG_KEYS = [
    "DialogueNodeEvent:107:2",  # first floor — no water
    "DialogueNodeEvent:107:3",  # second floor — no water
    "DialogueNodeEvent:107:4",  # middle — contaminated water (negative since 2026-09-24)
    "DialogueNodeEvent:107:6",  # all the way down — bedrock
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

    success_total = count_keys(coll, pid, SUCCESS_KEYS, f)
    neg_total = count_keys(coll, pid, NEG_KEYS, f)

    # Mirror the color formula exactly
    score = 0
    if m1_top == 1 and m1_bottom == 1:
        score += 1
    if m2 == 1:
        score += 1
    if success_total > 0 and neg_total == 0:
        score += 2
    elif success_total > 0 and neg_total == 1:
        score += 1

    return {
        "triggered": score <= 2,
        "machine_attempt_number": m1_top + m1_bottom + m2,
        "wrong_choice_number": neg_total,
    }


CODES = {"SCORE_BELOW_THRESHOLD": score_below_threshold}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
