"""Reason codes for Unit 3 Point 5 — "Plant the Superfruit Seeds".

mhs-unit3-point5-grading.md, "## Reason Codes":

  EXCESS_WRONG_PLANTINGS — triggered when the color formula goes yellow:
      sum_score = posCount*1.0 - negCount*0.5 < 2.5 (2+ wrong plantings;
      threshold 2.5 confirmed as decision A5, 2026-09-21).
      wrong_planting_number = wrong-spot feedback count (73:164 first wrong,
      73:168 second and third, 73:171 when a third or later wrong planting is
      the last seed).

Window (start-and-end form since 2026-09-24): latest `DialogueNodeEvent:10:194`
(end, inclusive), latest `DialogueNodeEvent:73:200` before it (start,
exclusive; OID_MIN when none) — the same window as the production color
script. Until 2026-09-24: previous `10:194` (exclusive) .. latest (inclusive).
Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database.
"""

from rc_common import OID_MIN, count_keys, gt_lte, latest

META = {"unit": 3, "point": 5, "name": "Plant the Superfruit Seeds",
        "doc": "mhs-unit3-point5-grading.md"}

START_KEY = "DialogueNodeEvent:73:200"
END_KEY = "DialogueNodeEvent:10:194"
POS_KEY = "DialogueNodeEvent:73:163"

NEG_KEYS = [
    "DialogueNodeEvent:73:164",  # 1st wrong spot
    "DialogueNodeEvent:73:168",  # 2nd and 3rd wrong spot
    "DialogueNodeEvent:73:171",  # 3rd+ wrong spot on the last seed, activity terminates
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


def excess_wrong_plantings(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_planting_number": 0}
    f = gt_lte(win)
    # 3) Counts inside the window
    pos_count = count_keys(coll, pid, POS_KEY, f)
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    sum_score = (pos_count * 1.0) - (neg_count * 0.5)
    return {"triggered": sum_score < 2.5, "wrong_planting_number": neg_count}


CODES = {"EXCESS_WRONG_PLANTINGS": excess_wrong_plantings}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
