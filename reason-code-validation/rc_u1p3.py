"""Reason codes for Unit 1 Point 3 — "Defend the Expedition".

mhs-unit1-point3-grading.md, "## Reason Codes":

  WRONG_ARG_SELECTED — "Quantitative script": the one script in the set that
  predates the settled `{triggered, ...}` template. It returns only
  `attempt_number` (count of ATTEMPT_KEYS in the window); the pop-up shows the
  code whenever the cell is yellow, so `triggered` here mirrors the production
  color rule verbatim (any YELLOW key inside the window).

Window: previous `questActiveEvent:34` (exclusive) .. latest (inclusive), the
same trigger-to-trigger window as the production color script.
"""

from rc_common import count_keys, gt_lte, has_keys, latest_trigger_window

META = {"unit": 1, "point": 3, "name": "Defend the Expedition",
        "doc": "mhs-unit1-point3-grading.md"}

TRIGGER_KEY = "questActiveEvent:34"

YELLOW_KEYS = ["DialogueNodeEvent:70:25"]

ATTEMPT_KEYS = [
    "DialogueNodeEvent:70:25",
    "DialogueNodeEvent:70:7",
]


def attempt_window(coll, pid):
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


def wrong_arg_selected(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # Production color rule (mirrored so the pop-up follows the cell).
    has_yellow = has_keys(coll, pid, YELLOW_KEYS, f)
    # 3) Count attempt dialogue triggers only inside the window
    attempts = count_keys(coll, pid, ATTEMPT_KEYS, f)
    return {"triggered": has_yellow, "attempt_number": attempts}


CODES = {"WRONG_ARG_SELECTED": wrong_arg_selected}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
