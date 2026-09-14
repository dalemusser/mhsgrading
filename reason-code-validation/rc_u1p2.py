"""Reason codes for Unit 1 Point 2 — "Info and Intros".

mhs-unit1-point2-grading.md: "No reason codes — this point is always green
when the trigger event exists." See rc_u1p1.py.
"""

from rc_common import latest

META = {"unit": 1, "point": 2, "name": "Info and Intros",
        "doc": "mhs-unit1-point2-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:30:98"

CODES = {}


def attempt_window(coll, pid):
    t = latest(coll, pid, TRIGGER_KEY)
    return (t["_id"], t["_id"]) if t else None


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
