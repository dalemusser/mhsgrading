"""Test for Unit 2 Point 5 — "Classified Information".

Production rule (mhs-unit2-point5-grading.md): within the latest attempt window
(previous `DialogueNodeEvent:23:42` exclusive .. latest `DialogueNodeEvent:23:42`
inclusive), count POS_KEYS and NEG_KEYS, compute score = pos_count -
(neg_count / 3.0). Green iff score >= 4. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 2, "point": 5, "name": "Classified Information", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:23:42"
THRESHOLD = 4

POS_KEYS = [
    "DialogueNodeEvent:26:165", "DialogueNodeEvent:26:166", "DialogueNodeEvent:26:167",
    "DialogueNodeEvent:26:168", "DialogueNodeEvent:26:169", "DialogueNodeEvent:26:170",
    "DialogueNodeEvent:26:171", "DialogueNodeEvent:26:172", "DialogueNodeEvent:26:173",
    "DialogueNodeEvent:26:174", "DialogueNodeEvent:26:175", "DialogueNodeEvent:26:176",
    "DialogueNodeEvent:26:177", "DialogueNodeEvent:26:178", "DialogueNodeEvent:26:179",
    "DialogueNodeEvent:26:180", "DialogueNodeEvent:26:181", "DialogueNodeEvent:26:182",
    "DialogueNodeEvent:26:183", "DialogueNodeEvent:26:184", "DialogueNodeEvent:26:185",
    "DialogueNodeEvent:26:186",
]

NEG_KEYS = [
    "DialogueNodeEvent:26:187", "DialogueNodeEvent:26:188", "DialogueNodeEvent:26:189",
    "DialogueNodeEvent:26:190", "DialogueNodeEvent:26:191", "DialogueNodeEvent:26:192",
    "DialogueNodeEvent:26:193", "DialogueNodeEvent:26:194", "DialogueNodeEvent:26:195",
    "DialogueNodeEvent:26:196", "DialogueNodeEvent:26:197", "DialogueNodeEvent:26:198",
    "DialogueNodeEvent:26:199", "DialogueNodeEvent:26:200", "DialogueNodeEvent:26:201",
    "DialogueNodeEvent:26:202", "DialogueNodeEvent:26:203", "DialogueNodeEvent:26:204",
    "DialogueNodeEvent:26:205", "DialogueNodeEvent:26:206", "DialogueNodeEvent:26:207",
    "DialogueNodeEvent:26:208", "DialogueNodeEvent:26:209", "DialogueNodeEvent:26:210",
    "DialogueNodeEvent:26:211",
]


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    pos_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
    )
    neg_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    score = pos_count - (neg_count / 3.0)
    return "green" if score >= THRESHOLD else "yellow"


def diagnose(coll, pid):
    out = {}
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    # TOO_MANY_NEGATIVES: wrong_number = count of incorrect argument selections
    wrong_number = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    pos_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": POS_KEYS}, **win_filter}
    )
    score = pos_count - (wrong_number / 3.0)
    if score < THRESHOLD:
        out["TOO_MANY_NEGATIVES"] = (
            f"wrong_number={wrong_number} (score={score:.2f} < {THRESHOLD}) — too "
            f"many incorrect attempts identifying argument parts"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
