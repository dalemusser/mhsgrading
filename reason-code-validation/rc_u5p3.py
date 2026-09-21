"""Reason codes for Unit 5 Point 3 — "What Happened Here?".

mhs-unit5-point3-grading.md, "## Reason Codes":

  EXCESS_ATTEMPTS — triggered when the color rule goes yellow: 4+ flagged
      submissions (count-only; no success-node requirement).
      wrong_argument_number = total flagged submissions; the component counts
      split it. The softer twins 108:63-66/68/69 were added to the colour rule and
      the buckets on 2026-09-17 and are counted.

Window: latest `DialogueNodeEvent:96:1` (start, exclusive) .. latest
`questFinishEvent:44` (end, inclusive); guard `latestEnd._id < latestStart._id`.
"""

from rc_common import count_keys, gt_lte, start_end_window

META = {"unit": 5, "point": 3, "name": "What Happened Here?",
        "doc": "mhs-unit5-point3-grading.md"}

WINDOW_START_KEY = "DialogueNodeEvent:96:1"
WINDOW_END_KEY = "questFinishEvent:44"

CLAIM_NEG_KEYS = [            # restating Aryn's claim
    "DialogueNodeEvent:108:32", "DialogueNodeEvent:108:33", "DialogueNodeEvent:108:37",
    "DialogueNodeEvent:108:41", "DialogueNodeEvent:108:70", "DialogueNodeEvent:108:72",
    "DialogueNodeEvent:108:73", "DialogueNodeEvent:108:74", "DialogueNodeEvent:108:75",
    "DialogueNodeEvent:108:76", "DialogueNodeEvent:108:78", "DialogueNodeEvent:108:79",
]

REASONING_NEG_KEYS = [
    "DialogueNodeEvent:108:39", "DialogueNodeEvent:108:53",  # too many reasoning statements
    "DialogueNodeEvent:108:54", "DialogueNodeEvent:108:55",  # redundant reasoning
    "DialogueNodeEvent:108:90", "DialogueNodeEvent:108:91",  # too many reasoning statements
    "DialogueNodeEvent:108:59", "DialogueNodeEvent:108:84",  # "water being filtered" misconception
    "DialogueNodeEvent:108:85",
    "DialogueNodeEvent:108:61", "DialogueNodeEvent:108:86",  # "transformed into salt" misconception
    "DialogueNodeEvent:108:60", "DialogueNodeEvent:108:62",  # reasoning doesn't match the argument
    "DialogueNodeEvent:108:87",
    "DialogueNodeEvent:108:88", "DialogueNodeEvent:108:89",  # reasoning doesn't connect all evidence (C and D)
    "DialogueNodeEvent:108:65", "DialogueNodeEvent:108:66",  # reasoning doesn't connect all evidence (C or D alone)
]

EVIDENCE_NEG_KEYS = [
    "DialogueNodeEvent:108:25", "DialogueNodeEvent:108:80",  # salt amount doesn't explain the water
    "DialogueNodeEvent:108:82", "DialogueNodeEvent:108:83",  # evidence doesn't support the claim (A alone)
    "DialogueNodeEvent:108:68", "DialogueNodeEvent:108:69",  # evidence doesn't support the claim (pair other than C+D)
    "DialogueNodeEvent:108:63", "DialogueNodeEvent:108:64",  # one piece of evidence missing (C or D alone, reasoning 3)
    "DialogueNodeEvent:108:47",                              # incomplete argument
]

NEG_KEYS = CLAIM_NEG_KEYS + REASONING_NEG_KEYS + EVIDENCE_NEG_KEYS


def attempt_window(coll, pid):
    return start_end_window(coll, pid, WINDOW_START_KEY, WINDOW_END_KEY, strict=False)


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_argument_number": 0, "claim_wrong_number": 0,
                "reasoning_wrong_number": 0, "evidence_wrong_number": 0}
    f = gt_lte(win)
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    return {
        "triggered": neg_count >= 4,
        "wrong_argument_number": neg_count,
        "claim_wrong_number": count_keys(coll, pid, CLAIM_NEG_KEYS, f),
        "reasoning_wrong_number": count_keys(coll, pid, REASONING_NEG_KEYS, f),
        "evidence_wrong_number": count_keys(coll, pid, EVIDENCE_NEG_KEYS, f),
    }


CODES = {"EXCESS_ATTEMPTS": excess_attempts}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
