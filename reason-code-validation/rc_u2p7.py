"""Reason codes for Unit 2 Point 7 — "Which Watershed? Part II".

mhs-unit2-point7-grading.md, "## Reason Codes":

  EXCESS_ATTEMPTS — triggered when the color rule goes yellow in the window:
      success (27:7) missing OR more than 3 incorrect submissions.
      attempt_number = incorrect submissions + 1 when success is present
      (else the incorrect count). The three sub-counts split the incorrect
      submissions by ARGUMENT STATE (the conversation-27 branch gate), not by
      wording — every feedback is a generic/specific pair chosen by
      argSpecificFeedback and both members describe the same mistake
      (reviewed against the 2026-06-10 Unity dialogue export, 2026-09-17;
      re-verified unchanged against the 2026-09-21 export, 2026-09-24):
        gate 27:31       claim I + evidence A (flow rate)   -> 27:11/12   wrong_claim_number
        gates 27:4/5/6   claim I + evidence B / C / D       -> 27:13-18   both_wrong_number
        gates 27:8/9/10  claim II + evidence B / C / D      -> 27:25-30   irrelevant_evidence_number
        any claim        several pieces of evidence at once -> 27:20      irrelevant_evidence_number

Window (start-and-end form since 2026-09-24): latest `questFinishEvent:54`
(end, inclusive), latest `DialogueNodeEvent:20:46` before it (start,
exclusive; OID_MIN when none) — the same window as the production color
script. Until 2026-09-24: previous `questFinishEvent:54` (exclusive) ..
latest (inclusive).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 2, "point": 7, "name": "Which Watershed? Part II",
        "doc": "mhs-unit2-point7-grading.md"}

START_KEY = "DialogueNodeEvent:20:46"
END_KEY = "questFinishEvent:54"
SUCCESS_KEY = "DialogueNodeEvent:27:7"  # "Well done! You have made the best argument possible."

WRONG_CLAIM_KEYS = [           # claim I with the flow-rate evidence (A): only the claim is wrong
    "DialogueNodeEvent:27:11",  # generic: evidence doesn't fit the claim (backing-info pointer)
    "DialogueNodeEvent:27:12",  # specific: try a more appropriate claim
]

BOTH_WRONG_KEYS = [            # claim I with irrelevant evidence: claim AND evidence wrong
    "DialogueNodeEvent:27:13", "DialogueNodeEvent:27:14",  # waterfall height (B)
    "DialogueNodeEvent:27:15", "DialogueNodeEvent:27:16",  # salinity (C)
    "DialogueNodeEvent:27:17", "DialogueNodeEvent:27:18",  # downstream river (D)
]

IRRELEVANT_EVIDENCE_KEYS = [   # claim II (correct) with evidence that does not indicate watershed size
    "DialogueNodeEvent:27:25", "DialogueNodeEvent:27:26",  # waterfall height (B)
    "DialogueNodeEvent:27:27", "DialogueNodeEvent:27:28",  # salinity (C)
    "DialogueNodeEvent:27:29", "DialogueNodeEvent:27:30",  # downstream river (D)
    "DialogueNodeEvent:27:20",                             # several pieces of evidence at once (any claim)
]

NEG_KEYS = WRONG_CLAIM_KEYS + BOTH_WRONG_KEYS + IRRELEVANT_EVIDENCE_KEYS


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
        return {"triggered": False, "attempt_number": 0, "wrong_claim_number": 0,
                "both_wrong_number": 0, "irrelevant_evidence_number": 0}
    f = gt_lte(win)
    # 3) Student reached the correct-argument completion
    has_success = has_keys(coll, pid, SUCCESS_KEY, f)
    # 4) Counts inside the window
    neg_count = count_keys(coll, pid, NEG_KEYS, f)
    claim_count = count_keys(coll, pid, WRONG_CLAIM_KEYS, f)
    both_count = count_keys(coll, pid, BOTH_WRONG_KEYS, f)
    evidence_count = count_keys(coll, pid, IRRELEVANT_EVIDENCE_KEYS, f)
    # 5) Mirror the color rule exactly
    triggered = not (has_success and neg_count <= 3)
    return {
        "triggered": triggered,
        "attempt_number": neg_count + 1 if has_success else neg_count,
        "wrong_claim_number": claim_count,
        "both_wrong_number": both_count,
        "irrelevant_evidence_number": evidence_count,
    }


CODES = {"EXCESS_ATTEMPTS": excess_attempts}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
