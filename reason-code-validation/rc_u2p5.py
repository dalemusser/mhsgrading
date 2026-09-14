"""Reason codes for Unit 2 Point 5 — "Classified Information".

mhs-unit2-point5-grading.md, "## Reason Codes":

  EXCESS_MISCLASSIFICATIONS — triggered when the color formula goes yellow:
      score = posCount - negCount/3 < 4. wrong_number = total incorrect
      classifications; claim_wrong / reasoning_wrong / evidence_wrong split it
      by what the misclassified passage actually was.

Window: previous `DialogueNodeEvent:23:42` (exclusive) .. latest (inclusive).
"""

from rc_common import count_keys, gt_lte, latest_trigger_window

META = {"unit": 2, "point": 5, "name": "Classified Information",
        "doc": "mhs-unit2-point5-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:23:42"

POS_KEYS = [
    # claim correct
    "DialogueNodeEvent:26:140", "DialogueNodeEvent:26:146", "DialogueNodeEvent:26:165",
    "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:175",
    "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:184",
    # reasoning correct
    "DialogueNodeEvent:26:142", "DialogueNodeEvent:26:147", "DialogueNodeEvent:26:166",
    "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:173", "DialogueNodeEvent:26:176",
    "DialogueNodeEvent:26:179", "DialogueNodeEvent:26:182", "DialogueNodeEvent:26:185",
    # evidence correct
    "DialogueNodeEvent:26:143", "DialogueNodeEvent:26:148", "DialogueNodeEvent:26:167",
    "DialogueNodeEvent:26:170", "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:177",
    "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:186",
]

CLAIM_NEG_KEYS = [        # passage was a claim
    "DialogueNodeEvent:26:137", "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:191",
    "DialogueNodeEvent:26:194", "DialogueNodeEvent:26:197", "DialogueNodeEvent:26:200",
    "DialogueNodeEvent:26:203", "DialogueNodeEvent:26:206", "DialogueNodeEvent:26:209",
]

REASONING_NEG_KEYS = [    # passage was reasoning
    "DialogueNodeEvent:26:144", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:192",
    "DialogueNodeEvent:26:195", "DialogueNodeEvent:26:198", "DialogueNodeEvent:26:201",
    "DialogueNodeEvent:26:204", "DialogueNodeEvent:26:207", "DialogueNodeEvent:26:210",
]

EVIDENCE_NEG_KEYS = [     # passage was evidence
    "DialogueNodeEvent:26:145", "DialogueNodeEvent:26:189", "DialogueNodeEvent:26:193",
    "DialogueNodeEvent:26:196", "DialogueNodeEvent:26:199", "DialogueNodeEvent:26:202",
    "DialogueNodeEvent:26:205", "DialogueNodeEvent:26:208", "DialogueNodeEvent:26:211",
]

NEG_KEYS = CLAIM_NEG_KEYS + REASONING_NEG_KEYS + EVIDENCE_NEG_KEYS


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def excess_misclassifications(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_number": 0, "claim_wrong": 0,
                "reasoning_wrong": 0, "evidence_wrong": 0}
    f = gt_lte(win)
    # 3) Counts inside the window
    pos_count = count_keys(coll, pid, POS_KEYS, f)
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    claim_wrong = count_keys(coll, pid, CLAIM_NEG_KEYS, f)
    reasoning_wrong = count_keys(coll, pid, REASONING_NEG_KEYS, f)
    evidence_wrong = count_keys(coll, pid, EVIDENCE_NEG_KEYS, f)
    # 4) Mirror the color rule exactly
    score = pos_count - (neg_count / 3.0)
    return {
        "triggered": score < 4,
        "wrong_number": neg_count,
        "claim_wrong": claim_wrong,
        "reasoning_wrong": reasoning_wrong,
        "evidence_wrong": evidence_wrong,
    }


CODES = {"EXCESS_MISCLASSIFICATIONS": excess_misclassifications}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
