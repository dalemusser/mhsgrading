"""Reason codes for Unit 3 Point 2 — "Pollution Solution".

mhs-unit3-point2-grading.md, "## Reason Codes":

  EXCESS_SENSOR_REMINDERS — triggered when the color formula goes yellow:
      score = 5 - pen(c27) - pen(c29 + c230) < 3, where pen caps each category
      (<=1: 0, 2-3: 1, >=4: 2). downstream_reminder_number = 11:27 count;
      redundant_reminder_number = 11:29 + 11:230 count.

Window: previous `DialogueNodeEvent:11:34` (exclusive) .. latest (inclusive).
"""

from rc_common import count_keys, gt_lte, latest_trigger_window

META = {"unit": 3, "point": 2, "name": "Pollution Solution",
        "doc": "mhs-unit3-point2-grading.md"}

TRIGGER_KEY = "DialogueNodeEvent:11:34"

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
    return latest_trigger_window(coll, pid, TRIGGER_KEY)


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
