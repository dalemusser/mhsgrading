"""Reason codes for Unit 2 Point 7 — "Which Watershed? Part II".

mhs-unit2-point7-grading.md, "## Reason Codes":

  EXCESS_ATTEMPTS — triggered when the color rule goes yellow in the window:
      success (27:7) missing OR more than 3 incorrect submissions.
      attempt_number = incorrect submissions + 1 when success is present
      (else the incorrect count); wrong_claim_number / irrelevant_evidence_number
      split the incorrect submissions by problem type.

Window: previous `questFinishEvent:54` (exclusive) .. latest (inclusive).
"""

from rc_common import count_keys, gt_lte, has_keys, latest_trigger_window

META = {"unit": 2, "point": 7, "name": "Which Watershed? Part II",
        "doc": "mhs-unit2-point7-grading.md"}

TRIGGER_KEY = "questFinishEvent:54"
SUCCESS_KEY = "DialogueNodeEvent:27:7"  # "Well done! You have made the best argument possible."

WRONG_CLAIM_KEYS = [           # claim wrong or doesn't fit evidence & reasoning
    "DialogueNodeEvent:27:11",  # evidence doesn't fit claim (backing-info pointer)
    "DialogueNodeEvent:27:12",  # evidence doesn't fit claim — try another claim
    "DialogueNodeEvent:27:14",  # both claim and evidence don't link to reasoning
    "DialogueNodeEvent:27:16",  # both claim and evidence don't link to reasoning
    "DialogueNodeEvent:27:18",  # both claim and evidence don't link to reasoning
]

IRRELEVANT_EVIDENCE_KEYS = [   # evidence doesn't indicate watershed size
    "DialogueNodeEvent:27:13",  # waterfall height
    "DialogueNodeEvent:27:25",  # waterfall height
    "DialogueNodeEvent:27:26",  # waterfall height (claim was correct)
    "DialogueNodeEvent:27:15",  # salinity
    "DialogueNodeEvent:27:27",  # salinity
    "DialogueNodeEvent:27:28",  # salinity
    "DialogueNodeEvent:27:17",  # downstream river
    "DialogueNodeEvent:27:29",  # downstream river
    "DialogueNodeEvent:27:30",  # downstream river
    "DialogueNodeEvent:27:20",  # multiple evidence pieces at once
]

NEG_KEYS = WRONG_CLAIM_KEYS + IRRELEVANT_EVIDENCE_KEYS


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0,
                "wrong_claim_number": 0, "irrelevant_evidence_number": 0}
    f = gt_lte(win)
    # 3) Student reached the correct-argument completion
    has_success = has_keys(coll, pid, SUCCESS_KEY, f)
    # 4) Counts inside the window
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    claim_count = count_keys(coll, pid, WRONG_CLAIM_KEYS, f)
    evidence_count = count_keys(coll, pid, IRRELEVANT_EVIDENCE_KEYS, f)
    # 5) Mirror the color rule exactly
    triggered = not (has_success and neg_count <= 3)
    return {
        "triggered": triggered,
        "attempt_number": neg_count + 1 if has_success else neg_count,
        "wrong_claim_number": claim_count,
        "irrelevant_evidence_number": evidence_count,
    }


CODES = {"EXCESS_ATTEMPTS": excess_attempts}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
