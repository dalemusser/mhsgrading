"""Test for Unit 1 Point 4 — "What Was That?".

Production rule (mhs-unit1-point4-grading.md): completion-only. Green whenever
the trigger event exists; no yellow pathway. Production returns "green".
"""

from mhs_harness import GAME

META = {"unit": 1, "point": 4, "name": "What Was That?", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:33:19"


def grade(coll, pid):
    return "green"


def diagnose(coll, pid):
    has_trigger = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": TRIGGER_KEY}) is not None
    )
    out = {}
    if not has_trigger:
        out["MISSING_TRIGGER"] = (
            f"trigger event {TRIGGER_KEY} not found for player — point is forced green"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
