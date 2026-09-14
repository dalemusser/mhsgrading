"""Reason codes for Unit 3 Point 5 — "Plant the Superfruit Seeds".

mhs-unit3-point5-grading.md, "## Reason Codes":

  EXCESS_WRONG_PLANTINGS — triggered when the PRODUCTION color formula goes
      yellow: sum_score = posCount*1.0 - negCount*0.5 < 2.5 (2+ wrong
      plantings; the rule table's ">= 3" is flagged for reconciliation in the
      markdown). wrong_planting_number = wrong-spot feedback count.

Window: previous `DialogueNodeEvent:10:194` (exclusive) .. latest (inclusive).
"""

from rc_common import count_keys, gt_lte, latest_trigger_window

META = {"unit": 3, "point": 5, "name": "Plant the Superfruit Seeds",
        "doc": "mhs-unit3-point5-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:10:194"
POS_KEY = "DialogueNodeEvent:73:163"

NEG_KEYS = [
    "DialogueNodeEvent:73:164",  # 1st wrong spot
    "DialogueNodeEvent:73:168",  # intermediate wrong spot (repeats)
    "DialogueNodeEvent:73:171",  # 4th wrong spot, activity terminates
]


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def excess_wrong_plantings(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_planting_number": 0}
    f = gt_lte(win)
    pos_count = count_keys(coll, pid, POS_KEY, f)
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    sum_score = (pos_count * 1.0) - (neg_count * 0.5)
    return {"triggered": sum_score < 2.5, "wrong_planting_number": neg_count}


CODES = {"EXCESS_WRONG_PLANTINGS": excess_wrong_plantings}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
