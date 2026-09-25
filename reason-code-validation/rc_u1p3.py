"""Reason codes for Unit 1 Point 3 — "Defend the Expedition".

mhs-unit1-point3-grading.md, "## Reason Codes":

  WRONG_ARG_SELECTED — "Corresponding Script" (on the settled
  `{triggered, ...}` template since 2026-09-23; before that a bare-count
  "Quantitative script"). `triggered` recomputes the production color rule
  verbatim (any YELLOW key inside the window); `attempt_number` = count of
  ATTEMPT_KEYS (70:25 wrong + 70:7 correct) inside the window, i.e. the
  attempt on which the correct argument was built.

Window (start-and-end form since 2026-09-23): latest `questActiveEvent:34`
(end, inclusive), latest `DialogueNodeEvent:30:98` before it (start,
exclusive; OID_MIN when none) — the same window as the production color
script. Until 2026-09-23: previous `questActiveEvent:34` (exclusive) ..
latest (inclusive).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 1, "point": 3, "name": "Defend the Expedition",
        "doc": "mhs-unit1-point3-grading.md"}

START_KEY = "DialogueNodeEvent:30:98"
END_KEY = "questActiveEvent:34"

YELLOW_KEYS = ["DialogueNodeEvent:70:25"]

ATTEMPT_KEYS = [
    "DialogueNodeEvent:70:25",
    "DialogueNodeEvent:70:7",
]


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def wrong_arg_selected(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "attempt_number": 0}
    f = gt_lte(win)
    # 3) Color rule, mirrored: any yellow node inside the window
    has_yellow = has_keys(coll, pid, YELLOW_KEYS, f)
    # 4) Count argument submissions inside the window
    attempts = count_keys(coll, pid, ATTEMPT_KEYS, f)
    return {"triggered": has_yellow, "attempt_number": attempts}


CODES = {"WRONG_ARG_SELECTED": wrong_arg_selected}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
