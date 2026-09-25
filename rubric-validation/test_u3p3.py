"""Test for Unit 3 Point 3 — "Pollution Argument".

Production rule (mhs-unit3-point3-grading.md): score-based with a bonus,
within the attempt window.

    sum_count   = windowed count of TARGET_KEYS (incorrect argument selections,
                  plus the success node 84:36 and the inert gate 84:38 by design)
    base_score  = 3 if <=3, 2 if ==4, 1 if ==5, else 0
    bonus       = 1 if BackingInfoPanel tool event present in window, else 0
    total_score = base_score + bonus
    green iff total_score >= 3. No trigger => yellow.

Window (start-and-end form since 2026-09-24): anchor on the latest END
(`questFinishEvent:18`); if missing => yellow. Take the latest START
(`DialogueNodeEvent:11:34`) at `_id < latestEnd._id` (else ObjectId("000..."))
as the exclusive window start. Until 2026-09-24 the window was (previous
`questFinishEvent:18` exclusive .. latest `questFinishEvent:18` inclusive).
Keys re-verified 2026-09-24 against the 2026-09-21 dialogue database
(conversation 84 unchanged).

The 2026-07-22 grading-logic fix re-anchored the window on
`questFinishEvent:18`: the script previously windowed on `questActiveEvent:18`,
which fires AFTER the argumentation activity and captured none of it (the
round-1 U3P3 miscolor).
"""

from mhs_harness import GAME, OID_MIN, ObjectId

META = {"unit": 3, "point": 3, "name": "Pollution Argument"}

START_KEY = "DialogueNodeEvent:11:34"
END_KEY = "questFinishEvent:18"
BONUS_TOOL = "BackingInfoPanel - Pollution Site Data"

TARGET_KEYS = [f"DialogueNodeEvent:84:{n}" for n in (20, 25)] + [
    f"DialogueNodeEvent:84:{n}" for n in range(32, 48)
]


def _base_score(sum_count):
    if sum_count <= 3:
        return 3
    if sum_count == 4:
        return 2
    if sum_count == 5:
        return 1
    return 0


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


def _score_parts(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    # 3) Target count and bonus inside the window
    sum_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": TARGET_KEYS}, **win_filter}
    )
    has_bonus = (
        coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventType": "argumentationToolEvent",
                "data.toolName": BONUS_TOOL,
                **win_filter,
            }
        )
        is not None
    )
    base = _base_score(sum_count)
    total = base + (1 if has_bonus else 0)
    return sum_count, base, has_bonus, total


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    _, _, _, total = parts
    return "green" if total >= 3 else "yellow"


def _lifetime_score(coll, pid):
    """Analytics-matching (lifetime) score, ignoring the attempt window."""
    sum_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": TARGET_KEYS}}
    )
    has_bonus = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventType": "argumentationToolEvent",
             "data.toolName": BONUS_TOOL}
        )
        is not None
    )
    base = _base_score(sum_count)
    total = base + (1 if has_bonus else 0)
    return sum_count, base, has_bonus, total


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["MISSING_TRIGGER"] = f"no {END_KEY} trigger found — defaults to yellow"
        return out
    sum_count, base, has_bonus, total = parts
    out["_score"] = (
        f"sum_count={sum_count} base_score={base} bonus={int(has_bonus)} total_score={total}"
    )

    # Cross-check the windowed result against the lifetime (analytics) score —
    # a disagreement means the attempt window excludes relevant activity.
    life_sum, life_base, life_bonus, life_total = _lifetime_score(coll, pid)
    prod_color = "green" if total >= 3 else "yellow"
    life_color = "green" if life_total >= 3 else "yellow"
    if prod_color != life_color:
        out["WINDOW_ANCHOR_MISMATCH"] = (
            f"production={prod_color} (windowed on {START_KEY}..{END_KEY}: sum_count={sum_count}, "
            f"total={total}) but analytics/lifetime={life_color} (sum_count={life_sum}, "
            f"total={life_total}) — the attempt window excludes part of the "
            f"argumentation activity; review the window anchors."
        )
    if not has_bonus:
        out["MISSING_SUCCESS_NODE"] = (
            "BackingInfoPanel tool event absent in window — did not check backing "
            "information for key knowledge"
        )
    if sum_count > 4:
        out["WRONG_ARG_SELECTED"] = (
            f"attempts_number={sum_count} (>4) — too many attempts to select correct reasoning"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
