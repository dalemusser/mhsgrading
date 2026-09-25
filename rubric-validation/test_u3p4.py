"""Test for Unit 3 Point 4 — "Forsaken Facility".

Production rule (mhs-unit3-point4-grading.md): gate + score-based, within the
attempt window.

    gate  = a DialogueNodeEvent:78:24 event present in window
    total = windowed count of TARGET_KEYS
    score = 2 if total == 0, 1 if total <= 2, else 0
    green iff gate present AND score != 0 (i.e. total <= 2).
    Missing end anchor, gate missing, or score == 0 => yellow.

Window (end-first form since 2026-09-24): anchor on the latest END
(`DialogueNodeEvent:73:200`); if missing => yellow. Take the latest START
(`questActiveEvent:18`) at `_id < latestEnd._id` (else ObjectId("000...")) as
the exclusive window start. Until 2026-09-24 the script took the latest start
and the latest end and returned yellow unless the end came after the start.
Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversations 73 and 78 unchanged).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 3, "point": 4, "name": "Forsaken Facility"}

START_KEY = "questActiveEvent:18"
END_KEY = "DialogueNodeEvent:73:200"
GATE_KEY = "DialogueNodeEvent:78:24"

TARGET_KEYS = [
    "DialogueNodeEvent:78:3", "DialogueNodeEvent:78:4", "DialogueNodeEvent:78:7",
    "DialogueNodeEvent:78:9", "DialogueNodeEvent:78:10", "DialogueNodeEvent:78:12",
    "DialogueNodeEvent:78:18", "DialogueNodeEvent:78:23",
]


def _window(coll, pid):
    """Returns (windowStartId, windowEndId) or None when no latest END trigger
    exists (=> yellow)."""
    # 1) Latest end anchor
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": END_KEY}, sort={"_id": -1}
    )
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventKey": START_KEY,
            "_id": {"$lt": latest_end["_id"]},
        },
        sort={"_id": -1},
    )
    window_start_id = latest_start["_id"] if latest_start else ObjectId(OID_MIN)
    return window_start_id, latest_end["_id"]


def _parts(coll, pid):
    """Returns (has_gate, total_count, score, reason). reason is None on a valid
    window, else a string explaining the no-window => yellow case."""
    win = _window(coll, pid)
    if win is None:
        return None, None, None, f"missing {END_KEY} anchor"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    # 3) Gate: must have 78:24 within (start, end]
    has_gate = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": GATE_KEY, **win_filter}
        )
        is not None
    )
    # 4) Count target events within the window
    total_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": TARGET_KEYS}, **win_filter}
    )
    if total_count == 0:
        score = 2
    elif total_count <= 2:
        score = 1
    else:
        score = 0
    return has_gate, total_count, score, None


def grade(coll, pid):
    has_gate, _, score, reason = _parts(coll, pid)
    if reason is not None:
        return "yellow"
    if not has_gate:
        return "yellow"
    return "yellow" if score == 0 else "green"


def diagnose(coll, pid):
    out = {}
    has_gate, total_count, score, reason = _parts(coll, pid)
    if reason is not None:
        out["MISSING_TRIGGER"] = reason + " — defaults to yellow"
        return out
    out["_score"] = (
        f"has_gate={int(has_gate)} total_count={total_count} score={score}"
    )
    if not has_gate:
        out["MISSING_SUCCESS_NODE"] = (
            f"gate key {GATE_KEY} absent in window — did not solve the matching "
            f"puzzle independently"
        )
    if total_count >= 3:
        out["TOO_MANY_NEGATIVES"] = (
            f"attempts_number={total_count} (>= 3) — too many attempts to make the "
            f"correct matches"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
