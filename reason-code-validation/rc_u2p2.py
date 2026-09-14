"""Reason codes for Unit 2 Point 2 — "Foraged Forging".

mhs-unit2-point2-grading.md, "## Reason Codes":

  EXCESS_NAV_REMINDERS — triggered when more than 1 adaptive navigation
      reminder fired during the search for Toppo; triggering_number = count.

Window mirrors the production color script: latest end trigger
`DialogueNodeEvent:20:26`, then the latest start `questFinishEvent:21` at or
before it, both needing a `timestamp`; reminders are counted inside the window
fenced by BOTH timestamp and _id (inclusive on both ends).
"""

from rc_common import GAME, latest

META = {"unit": 2, "point": 2, "name": "Foraged Forging",
        "doc": "mhs-unit2-point2-grading.md"}

END_KEY = "DialogueNodeEvent:20:26"     # trigger
START_KEY = "questFinishEvent:21"

BAD_FEEDBACK_KEYS = [
    "DialogueNodeEvent:28:179",  # clue reminder: near original location, rock formations
    "DialogueNodeEvent:59:179",
    "DialogueNodeEvent:28:182",  # map-usage reminder: open the map with M
    "DialogueNodeEvent:59:182",
    "DialogueNodeEvent:28:183",  # clue reminder: hill at ~90 feet elevation
    "DialogueNodeEvent:59:183",
]


def _anchors(coll, pid):
    """(startDoc, endDoc) or None, mirroring the script's two guards."""
    # 1) Latest end trigger by arrival order
    end_doc = latest(coll, pid, END_KEY)
    if not end_doc or not end_doc.get("timestamp"):
        return None
    # 2) Latest start at or before this end (same attempt)
    start_doc = latest(coll, pid, START_KEY, {"_id": {"$lte": end_doc["_id"]}})
    if not start_doc or not start_doc.get("timestamp"):
        return None
    return start_doc, end_doc


def attempt_window(coll, pid):
    a = _anchors(coll, pid)
    return (a[0]["_id"], a[1]["_id"]) if a else None


def excess_nav_reminders(coll, pid):
    a = _anchors(coll, pid)
    if a is None:
        return {"triggered": False, "triggering_number": 0}
    start_doc, end_doc = a
    # 3) Count reminders within the window, fenced by timestamp and _id
    count = coll.count_documents({
        "game": GAME,
        "playerId": pid,
        "eventKey": {"$in": BAD_FEEDBACK_KEYS},
        "timestamp": {"$gte": start_doc["timestamp"], "$lte": end_doc["timestamp"]},
        "_id": {"$gte": start_doc["_id"], "$lte": end_doc["_id"]},
    })
    # 4) Green allows at most 1 reminder; more than 1 triggers the reason code
    return {"triggered": count > 1, "triggering_number": count}


CODES = {"EXCESS_NAV_REMINDERS": excess_nav_reminders}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
