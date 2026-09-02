"""Test for Unit 2 Point 5 — "Classified Information".

Production rule (mhs-unit2-point5-grading.md): within the latest attempt window
(previous `DialogueNodeEvent:23:42` exclusive .. latest `DialogueNodeEvent:23:42`
inclusive), count POS_KEYS and NEG_KEYS, compute score = pos_count -
(neg_count / 3.0). Green iff score >= 4. No trigger => yellow.

The 2026-08-31 grading-logic update remapped the key sets:
POS +140/142/143/146/147/148 -171; NEG +137/144/145 -190.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 2, "point": 5, "name": "Classified Information"}

TRIGGER_KEY = "DialogueNodeEvent:23:42"
THRESHOLD = 4

POS_KEYS = [f"DialogueNodeEvent:26:{n}" for n in (
    140, 142, 143, 146, 147, 148, 165, 166, 167, 168, 169, 170, 172, 173,
    174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186)]

NEG_KEYS = [f"DialogueNodeEvent:26:{n}" for n in (
    137, 144, 145, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198,
    199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211)]


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
