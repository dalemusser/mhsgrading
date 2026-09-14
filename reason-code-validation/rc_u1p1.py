"""Reason codes for Unit 1 Point 1 — "Getting Your Space Legs".

mhs-unit1-point1-grading.md: "No reason codes — this point is always green
when the trigger event exists." Nothing to transcribe; the module exists so
the runner shows all 26 dashboard points and will flag it if reason codes are
ever added to the markdown without a transcription here.
"""

from rc_common import GAME, latest

META = {"unit": 1, "point": 1, "name": "Getting Your Space Legs",
        "doc": "mhs-unit1-point1-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:31:29"

CODES = {}


def attempt_window(coll, pid):
    """No attempt window in the production script; report whether the trigger
    exists so the runner can show the not-reached state."""
    t = latest(coll, pid, TRIGGER_KEY)
    return (t["_id"], t["_id"]) if t else None


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
