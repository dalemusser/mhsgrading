"""Reason codes for Unit 4 Point 5 — "Saving Cadet Anderson".

mhs-unit4-point5-grading.md, "## Reason Codes":

  EXCESS_ATTEMPTS — `triggered` mirrors the color rule verbatim: no success
      node (90:50 first-try / 90:57 after revisions) OR 3+ negative
      submissions. attempt_number = incorrect submissions + 1 when success is
      present; the three component counts split the incorrect submissions by
      the conversation-90 gate that fired (re-verified against the 2026-09-21
      Unity export on 2026-09-24, unchanged since 2026-06-10):
        gate 90:4          claim I (any evidence)       -> 90:37/55   claim_wrong_number
        gates 90:8/51/53   claim II, reasoning 1/3/4    -> 25,56/52,60/54,61  reasoning_wrong_number
        gate 90:38         claim II, reasoning 2 (ok)   -> 39/58 missing, 45/59 unsupportive  evidence_wrong_number
        (no gate)          any part empty               -> 90:47      evidence_wrong_number

Window (start-and-end form since 2026-09-24): latest `questActiveEvent:41`
(end, inclusive), latest `questActiveEvent:36` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script.
`questActiveEvent:36` logs twice per playthrough; the later one is taken and
every conversation-90 submission follows it. Until 2026-09-24: previous
`questActiveEvent:41` (exclusive) .. latest (inclusive).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 4, "point": 5, "name": "Saving Cadet Anderson",
        "doc": "mhs-unit4-point5-grading.md"}

START_KEY = "questActiveEvent:36"
END_KEY = "questActiveEvent:41"

POS_KEYS = ["DialogueNodeEvent:90:50", "DialogueNodeEvent:90:57"]

CLAIM_NEG_KEYS = [
    "DialogueNodeEvent:90:37", "DialogueNodeEvent:90:55",
]
REASONING_NEG_KEYS = [
    "DialogueNodeEvent:90:25", "DialogueNodeEvent:90:56",
    "DialogueNodeEvent:90:52", "DialogueNodeEvent:90:60",  # bedrock misconception
    "DialogueNodeEvent:90:54", "DialogueNodeEvent:90:61",  # infiltrate-upward misconception
]
EVIDENCE_NEG_KEYS = [
    "DialogueNodeEvent:90:39", "DialogueNodeEvent:90:58",  # missing evidence
    "DialogueNodeEvent:90:45", "DialogueNodeEvent:90:59",  # unsupportive evidence
    "DialogueNodeEvent:90:47",                             # incomplete argument
]

NEG_KEYS = CLAIM_NEG_KEYS + REASONING_NEG_KEYS + EVIDENCE_NEG_KEYS


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0, "claim_wrong_number": 0,
                "reasoning_wrong_number": 0, "evidence_wrong_number": 0}
    f = gt_lte(win)
    has_success = has_keys(coll, pid, POS_KEYS, f)
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    return {
        "triggered": (not has_success) or neg_count >= 3,
        "attempt_number": neg_count + (1 if has_success else 0),
        "claim_wrong_number": count_keys(coll, pid, CLAIM_NEG_KEYS, f),
        "reasoning_wrong_number": count_keys(coll, pid, REASONING_NEG_KEYS, f),
        "evidence_wrong_number": count_keys(coll, pid, EVIDENCE_NEG_KEYS, f),
    }


CODES = {"EXCESS_ATTEMPTS": excess_attempts}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
