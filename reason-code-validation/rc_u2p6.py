"""Reason codes for Unit 2 Point 6 — "Which Watershed? Part I".

mhs-unit2-point6-grading.md, "## Reason Codes":

  WRONG_EVIDENCE_SELECTED — triggered when a wrong-option node (20:44
      waterfall height, 20:45 salinity) fired in the attempt window;
      wrong_choice names the option(s) chosen.

Window (end-first form since 2026-09-24): latest `DialogueNodeEvent:20:46`
(end, inclusive), latest `DialogueNodeEvent:23:42` before it (start,
exclusive; OID_MIN when none) — the same window as the production color
script. Until 2026-09-24: latest start and latest end, end must follow start.
Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 20 unchanged; 20:42 -> 43 | 44 | 45 -> 46, single-select).
"""

from rc_common import OID_MIN, gt_lte, has_keys, latest

META = {"unit": 2, "point": 6, "name": "Which Watershed? Part I",
        "doc": "mhs-unit2-point6-grading.md"}

START_KEY = "DialogueNodeEvent:23:42"   # opens the activity (exclusive)
END_KEY = "DialogueNodeEvent:20:46"     # closes the attempt (inclusive)
HEIGHT_KEY = "DialogueNodeEvent:20:44"    # chose waterfall height
SALINITY_KEY = "DialogueNodeEvent:20:45"  # chose salinity


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def wrong_evidence_selected(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_choice": None}
    f = gt_lte(win)
    has_height = has_keys(coll, pid, HEIGHT_KEY, f)
    has_salinity = has_keys(coll, pid, SALINITY_KEY, f)

    wrong_choice = None
    if has_height and has_salinity:
        wrong_choice = "waterfall height and salinity"
    elif has_height:
        wrong_choice = "waterfall height"
    elif has_salinity:
        wrong_choice = "salinity"

    return {"triggered": wrong_choice is not None, "wrong_choice": wrong_choice}


CODES = {"WRONG_EVIDENCE_SELECTED": wrong_evidence_selected}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
