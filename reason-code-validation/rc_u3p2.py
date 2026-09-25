"""Reason codes for Unit 3 Point 2 — "Pollution Solution".

mhs-unit3-point2-grading.md, "## Reason Codes":

  EXCESS_SENSOR_REMINDERS — triggered when the color formula goes yellow:
      score = 5 - pen(c27) - pen(c29 + c230) < 3, where pen caps each category
      (<=1: 0, 2-3: 1, >=4: 2). downstream_reminder_number = 11:27 count;
      redundant_reminder_number = 11:29 + 11:230 count.

Window (start-and-end form since 2026-09-24): latest `DialogueNodeEvent:11:34`
(end, inclusive), latest `questActiveEvent:17` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. Until
2026-09-24: previous `11:34` (exclusive) .. latest (inclusive). Keys
re-verified 2026-09-24 against the 2026-09-21 dialogue database.
"""

from rc_common import OID_MIN, count_keys, gt_lte, latest

META = {"unit": 3, "point": 2, "name": "Pollution Solution",
        "doc": "mhs-unit3-point2-grading.md"}

START_KEY = "questActiveEvent:17"
END_KEY = "DialogueNodeEvent:11:34"

DOWNSTREAM_KEY = "DialogueNodeEvent:11:27"   # test further upstream
REDUNDANT_KEYS = [
    "DialogueNodeEvent:11:29",   # no need to check upstream of a clean sensor
    "DialogueNodeEvent:11:230",  # top of branch reached, proceed downstream
]


def capped_penalty(cnt):
    if cnt <= 1:
        return 0
    if cnt <= 3:
        return 1
    return 2


def attempt_window(coll, pid):
    # 1) Latest end anchor
    latest_end = latest(coll, pid, END_KEY)
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end["_id"]


def excess_sensor_reminders(coll, pid):
    win = attempt_window(coll, pid)
    if win is None:
        return {"triggered": False, "downstream_reminder_number": 0,
                "redundant_reminder_number": 0}
    f = gt_lte(win)
    # 3) Category counts inside the window
    downstream_count = count_keys(coll, pid, DOWNSTREAM_KEY, f)
    redundant_count = count_keys(coll, pid, REDUNDANT_KEYS, f)
    # 4) Mirror the color formula exactly
    score = 5 - capped_penalty(downstream_count) - capped_penalty(redundant_count)
    return {
        "triggered": score < 3,
        "downstream_reminder_number": downstream_count,
        "redundant_reminder_number": redundant_count,
    }


CODES = {"EXCESS_SENSOR_REMINDERS": excess_sensor_reminders}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
