"""Reason codes for Unit 3 Point 3 — "Pollution Argument".

mhs-unit3-point3-grading.md, "## Reason Codes":

  EXCESS_ATTEMPTS — `triggered` mirrors the color formula verbatim: base score
      from the color script's TARGET_KEYS count (which still includes success
      node 84:36 and empty 84:38 — flagged for review in the markdown), plus 1
      bonus for opening the Pollution Site Data panel; yellow when total < 3.
      The quantities report honest counts: wrong_argument_number excludes
      84:36/38 and the component counts split it by ARGUMENT STATE (the
      conversation-84 branch gate): claim II + evidence A -> 39/45; claim II +
      evidence B -> 25/46 (reasoning 1/2/3/5) and 40 (reasoning 4), all claim;
      claim I + evidence A with wrong reasoning -> 32-35/41-44, reasoning;
      claim I + evidence B -> 37, multiple evidence -> 20, incomplete -> 47,
      evidence/structure (reviewed against the Unity export 2026-09-17);
      backing_info_phrase = "opened" / "did not open".

Window: previous `questFinishEvent:18` (exclusive) .. latest (inclusive).
"""

from rc_common import GAME, count_keys, gt_lte, latest_trigger_window

META = {"unit": 3, "point": 3, "name": "Pollution Argument",
        "doc": "mhs-unit3-point3-grading.md"}

TRIGGER_KEY = "questFinishEvent:18"

CLAIM_NEG_KEYS = [
    "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:45",  # claim II + evidence A: only the claim is wrong
    "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:46",  # claim II + evidence B, reasoning 1/2/3/5
    "DialogueNodeEvent:84:40",                             # claim II + evidence B, reasoning 4: same gate
]
REASONING_NEG_KEYS = [                                     # claim I + evidence A: only the reasoning is wrong
    "DialogueNodeEvent:84:32", "DialogueNodeEvent:84:41",  # reasoning 1
    "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:42",  # reasoning 2
    "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:43",  # reasoning 3
    "DialogueNodeEvent:84:35", "DialogueNodeEvent:84:44",  # reasoning 4
]
EVIDENCE_STRUCT_NEG_KEYS = [
    "DialogueNodeEvent:84:37",  # evidence doesn't match the argument
    "DialogueNodeEvent:84:20",  # multiple evidence pieces used
    "DialogueNodeEvent:84:47",  # incomplete argument
]

WRONG_KEYS = CLAIM_NEG_KEYS + REASONING_NEG_KEYS + EVIDENCE_STRUCT_NEG_KEYS

# Color-rule key list, kept verbatim so triggered matches the cell (incl. 36/38)
COLOR_TARGET_KEYS = WRONG_KEYS + ["DialogueNodeEvent:84:36", "DialogueNodeEvent:84:38"]

BACKING_INFO_TOOL = "BackingInfoPanel - Pollution Site Data"


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def excess_attempts(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_argument_number": 0, "claim_wrong_number": 0,
                "reasoning_wrong_number": 0, "evidence_wrong_number": 0,
                "backing_info_phrase": "did not open"}
    f = gt_lte(win)

    sum_count = count_keys(coll, pid, COLOR_TARGET_KEYS, f)   # mirrors the color script
    wrong_count = count_keys(coll, pid, WRONG_KEYS, f)        # honest wrong-submission count
    claim_count = count_keys(coll, pid, CLAIM_NEG_KEYS, f)
    reasoning_count = count_keys(coll, pid, REASONING_NEG_KEYS, f)
    evidence_count = count_keys(coll, pid, EVIDENCE_STRUCT_NEG_KEYS, f)

    if sum_count <= 3:
        base_score = 3
    elif sum_count == 4:
        base_score = 2
    elif sum_count == 5:
        base_score = 1
    else:
        base_score = 0

    has_bonus = coll.find_one({
        "game": GAME, "playerId": pid,
        "eventType": "argumentationToolEvent",
        "data.toolName": BACKING_INFO_TOOL,
        **f,
    }) is not None

    return {
        "triggered": (base_score + (1 if has_bonus else 0)) < 3,
        "wrong_argument_number": wrong_count,
        "claim_wrong_number": claim_count,
        "reasoning_wrong_number": reasoning_count,
        "evidence_wrong_number": evidence_count,
        "backing_info_phrase": "opened" if has_bonus else "did not open",
    }


CODES = {"EXCESS_ATTEMPTS": excess_attempts}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
