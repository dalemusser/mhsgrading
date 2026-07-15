"""Test for Unit 2 Point 3 — "Getting the Band Back Together Part II".

Production rule (mhs-unit2-point3-grading.md): same windowed-count shape as
U2P2. Anchor on latest trigger `DialogueNodeEvent:22:18`, take latest start
`DialogueNodeEvent:20:33` at/before it, count TARGET keys within both the
timestamp window and the _id window. Green iff count <= 6. Missing start/end
=> yellow.
"""

from mhs_harness import GAME

META = {"unit": 2, "point": 3, "name": "Getting the Band Back Together Part II", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:22:18"
START_KEY = "DialogueNodeEvent:20:33"
THRESHOLD = 6

TARGET_KEYS = [
    "DialogueNodeEvent:18:225", "DialogueNodeEvent:28:185", "DialogueNodeEvent:59:185",
    "DialogueNodeEvent:28:184", "DialogueNodeEvent:28:191", "DialogueNodeEvent:59:184", "DialogueNodeEvent:59:191",
    "DialogueNodeEvent:18:226", "DialogueNodeEvent:18:227", "DialogueNodeEvent:28:186", "DialogueNodeEvent:59:186",
    "DialogueNodeEvent:18:228", "DialogueNodeEvent:28:187", "DialogueNodeEvent:59:187",
    "DialogueNodeEvent:18:229", "DialogueNodeEvent:28:188", "DialogueNodeEvent:59:188",
    "DialogueNodeEvent:18:230", "DialogueNodeEvent:28:180", "DialogueNodeEvent:59:180",
    "DialogueNodeEvent:18:233", "DialogueNodeEvent:28:192", "DialogueNodeEvent:59:192",
    "DialogueNodeEvent:18:234", "DialogueNodeEvent:28:193", "DialogueNodeEvent:59:193",
    "DialogueNodeEvent:18:235", "DialogueNodeEvent:28:194", "DialogueNodeEvent:59:194",
    "DialogueNodeEvent:18:236", "DialogueNodeEvent:18:237", "DialogueNodeEvent:28:190", "DialogueNodeEvent:59:190",
]


def _count_targets(coll, pid):
    end_doc = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": TRIGGER_KEY}, sort={"_id": -1}
    )
    if not end_doc or not end_doc.get("timestamp"):
        return None, f"trigger {TRIGGER_KEY} missing (or has no timestamp)"
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
        return None, f"start key {START_KEY} missing before trigger (or has no timestamp)"
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
            f"wrong-direction prompts while searching for Tera/Aryn"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
