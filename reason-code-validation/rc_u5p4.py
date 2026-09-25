"""Reason codes for Unit 5 Point 4 — "Water Problems Require Water Solutions".

mhs-unit5-point4-grading.md, "## Reason Codes":

  WRONG_SETTINGS_SELECTED — mirrors the color rule (zero tolerance): triggered
      unless 106:35 fired AND no failure outcome fired in the window.
      failure_phrase names the observed failure mode(s) (sunlight blocked /
      glass too hot / roof angle, with run counts when > 1); wrong_run_number
      = failed runs.

Window (start-and-end form since 2026-09-01): latest `questFinishEvent:45`
(end, inclusive), latest `questFinishEvent:44` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script.

Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 106: same twelve outcome nodes; the empty continuation node
106:37 is new and ungraded).
"""

from rc_common import OID_MIN, count_keys, gt_lte, has_keys, latest

META = {"unit": 5, "point": 4, "name": "Water Problems Require Water Solutions",
        "doc": "mhs-unit5-point4-grading.md"}

START_KEY = "questFinishEvent:44"
END_KEY = "questFinishEvent:45"
SUCCESS_KEY = "DialogueNodeEvent:106:35"

SUNLIGHT_KEYS = [   # no water: sunlight blocked, no evaporation
    "DialogueNodeEvent:106:4", "DialogueNodeEvent:106:25", "DialogueNodeEvent:106:26",
    "DialogueNodeEvent:106:27", "DialogueNodeEvent:106:28", "DialogueNodeEvent:106:29",
]
GLASS_KEYS = [      # no water: glass too hot, no condensation
    "DialogueNodeEvent:106:30", "DialogueNodeEvent:106:31", "DialogueNodeEvent:106:32",
]
ROOF_KEYS = [       # small amount: roof angle didn't collect the water
    "DialogueNodeEvent:106:33", "DialogueNodeEvent:106:34",
]

NEGATIVE_KEYS = SUNLIGHT_KEYS + GLASS_KEYS + ROOF_KEYS


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def _runs_suffix(n):
    return f" ({n} runs)" if n > 1 else ""


def wrong_settings_selected(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "wrong_run_number": 0, "failure_phrase": ""}
    f = gt_lte(win)

    has_success = has_keys(coll, pid, SUCCESS_KEY, f)

    sunlight_count = count_keys(coll, pid, SUNLIGHT_KEYS, f)
    glass_count = count_keys(coll, pid, GLASS_KEYS, f)
    roof_count = count_keys(coll, pid, ROOF_KEYS, f)
    neg_count = sunlight_count + glass_count + roof_count

    parts = []
    if sunlight_count > 0:
        parts.append("the settings blocked sunlight, so the salt water could not heat up and evaporate"
                     + _runs_suffix(sunlight_count))
    if glass_count > 0:
        parts.append("the glass surface was too hot for condensation to form"
                     + _runs_suffix(glass_count))
    if roof_count > 0:
        parts.append("the roof angle let most of the condensed water escape, collecting only a small amount"
                     + _runs_suffix(roof_count))

    failure_phrase = "; and ".join(parts) if parts else "no successful desalinator run was recorded"

    # Mirror the color rule exactly: green requires success AND zero failures
    return {
        "triggered": (not has_success) or neg_count > 0,
        "wrong_run_number": neg_count,
        "failure_phrase": failure_phrase,
    }


CODES = {"WRONG_SETTINGS_SELECTED": wrong_settings_selected}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
