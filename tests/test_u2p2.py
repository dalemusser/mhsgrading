"""Test for Unit 2 Point 2 — "Foraged Forging".

Production rule (mhs-unit2-point2-grading.md): windowed count of wrong-direction
prompts. Anchor on the latest END trigger (`DialogueNodeEvent:20:26`), take the
latest START (`questFinishEvent:21`) at/before it, then count TARGET keys whose
timestamp is within [startIso, endIso] AND whose _id is within
[startId, endId]. Green iff count <= 1. Missing start/end => yellow.
"""

from mhs_harness import GAME

META = {"unit": 2, "point": 2, "name": "Foraged Forging", "expected": "yellow"}

END_KEY = "DialogueNodeEvent:20:26"
START_KEY = "questFinishEvent:21"
THRESHOLD = 1

TARGET_KEYS = [
    "DialogueNodeEvent:18:99",
    "DialogueNodeEvent:28:179",
    "DialogueNodeEvent:59:179",
    "DialogueNodeEvent:18:223",
    "DialogueNodeEvent:28:182",
    "DialogueNodeEvent:59:182",
    "DialogueNodeEvent:18:224",
    "DialogueNodeEvent:28:183",
    "DialogueNodeEvent:59:183",
]


def _count_targets(coll, pid):
    """Returns (count, reason) where reason is None on success or a string when
    the window cannot be established (=> yellow)."""
    end_doc = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": END_KEY}, sort={"_id": -1}
    )
    if not end_doc or not end_doc.get("timestamp"):
        return None, f"end trigger {END_KEY} missing (or has no timestamp)"
    end_iso = end_doc["timestamp"]

    start_doc = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": START_KEY,
            "_id": {"$lte": end_doc["_id"]},
        },
        sort={"_id": -1},
    )
    if not start_doc or not start_doc.get("timestamp"):
        return None, f"start key {START_KEY} missing before end (or has no timestamp)"
    start_iso = start_doc["timestamp"]

    count = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": {"$in": TARGET_KEYS},
            "timestamp": {"$gte": start_iso, "$lte": end_iso},
            "_id": {"$gte": start_doc["_id"], "$lte": end_doc["_id"]},
        }
    )
    return count, None


def grade(coll, pid):
    count, reason = _count_targets(coll, pid)
    if reason is not None:
        return "yellow"
    return "green" if count <= THRESHOLD else "yellow"


def diagnose(coll, pid):
    out = {}
    count, reason = _count_targets(coll, pid)
    if reason is not None:
        out["MISSING_WINDOW"] = reason + " — defaults to yellow"
        return out
    if count > THRESHOLD:
        out["BAD_FEEDBACK"] = (
            f"triggering_number={count} (threshold <= {THRESHOLD}) — repeated "
            f"wrong-direction prompts while searching for Toppo"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
