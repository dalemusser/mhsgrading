"""Test for Unit 3 Point 5 — "Plant the Superfruit Seeds".

Production rule (mhs-unit3-point5-grading.md): weighted score, within the latest
attempt window (previous `DialogueNodeEvent:10:194` exclusive .. latest
`DialogueNodeEvent:10:194` inclusive).

    pos_count = windowed count of DialogueNodeEvent:73:163
    neg_count = windowed count of NEG_KEYS
    sum_score = (pos_count * 1.0) - (neg_count * 0.5)
    green iff sum_score >= 2.5 (i.e. not sum_score < 2.5). No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 3, "point": 5, "name": "Plant the Superfruit Seeds", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:10:194"
POS_KEY = "DialogueNodeEvent:73:163"
NEG_KEYS = [
    "DialogueNodeEvent:73:164",
    "DialogueNodeEvent:73:168",
    "DialogueNodeEvent:73:171",
]


def _score_parts(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    pos_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": POS_KEY, **win_filter}
    )
    neg_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": NEG_KEYS}, **win_filter}
    )
    sum_score = (pos_count * 1.0) - (neg_count * 0.5)
    return pos_count, neg_count, sum_score


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    _, _, sum_score = parts
    return "yellow" if sum_score < 2.5 else "green"


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    pos_count, neg_count, sum_score = parts
    out["_score"] = (
        f"pos_count={pos_count} neg_count={neg_count} sum_score={sum_score}"
    )
    if neg_count > 1:
        out["TOO_MANY_NEGATIVES"] = (
            f"attempts_number={neg_count} (> 1) — planted super-fruit seeds into too "
            f"many wrong spots"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
