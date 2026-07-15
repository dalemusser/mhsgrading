"""Test for Unit 1 Point 1 — "Getting Your Space Legs".

Production rule (mhs-unit1-point1-grading.md): completion-only. The point is
green whenever the trigger event exists; there is no yellow pathway, so the
production script returns "green" unconditionally.
"""

from mhs_harness import GAME

META = {"unit": 1, "point": 1, "name": "Getting Your Space Legs", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:31:29"


def grade(coll, pid):
    # Production Script (Attempt-Based): const color = "green";
    return "green"


def diagnose(coll, pid):
    # Completion-only points have no reason codes. We still surface whether the
    # trigger event is actually present, because an *absent* trigger is the only
    # data condition that could make "always green" wrong for this point.
    has_trigger = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": TRIGGER_KEY}) is not None
    )
    out = {}
    if not has_trigger:
        out["MISSING_TRIGGER"] = (
            f"trigger event {TRIGGER_KEY} not found for player — point is forced "
            f"green by production but the activity may not have been reached"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
