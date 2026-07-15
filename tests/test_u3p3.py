"""Test for Unit 3 Point 3 — "Pollution Argument".

Production rule (mhs-unit3-point3-grading.md): score-based with a bonus, within
the latest attempt window (previous `questActiveEvent:18` exclusive .. latest
`questActiveEvent:18` inclusive).

    sum_count   = windowed count of TARGET_KEYS (incorrect argument selections)
    base_score  = 3 if <=3, 2 if ==4, 1 if ==5, else 0
    bonus       = 1 if BackingInfoPanel tool event present in window, else 0
    total_score = base_score + bonus
    green iff total_score >= 3. No trigger => yellow.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 3, "point": 3, "name": "Pollution Argument", "expected": "yellow"}

TRIGGER_KEY = "questActiveEvent:18"
BONUS_TOOL = "BackingInfoPanel - Pollution Site Data"

TARGET_KEYS = [
    "DialogueNodeEvent:84:20", "DialogueNodeEvent:84:25", "DialogueNodeEvent:84:32",
    "DialogueNodeEvent:84:33", "DialogueNodeEvent:84:34", "DialogueNodeEvent:84:35",
    "DialogueNodeEvent:84:36", "DialogueNodeEvent:84:37", "DialogueNodeEvent:84:38",
    "DialogueNodeEvent:84:39", "DialogueNodeEvent:84:40", "DialogueNodeEvent:84:41",
    "DialogueNodeEvent:84:42", "DialogueNodeEvent:84:43", "DialogueNodeEvent:84:44",
    "DialogueNodeEvent:84:45", "DialogueNodeEvent:84:46", "DialogueNodeEvent:84:47",
]


def _base_score(sum_count):
    if sum_count <= 3:
        return 3
    if sum_count == 4:
        return 2
    if sum_count == 5:
        return 1
    return 0


def _score_parts(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return None
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
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


# The file documents the attempt window as Start=`DialogueNodeEvent:11:34`,
# End=`questFinishEvent:18`, but the production *script* windows on
# `questActiveEvent:18` (both ends). These differ, which is the bug below.
DOC_START_KEY = "DialogueNodeEvent:11:34"
DOC_END_KEY = "questFinishEvent:18"


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
        out["MISSING_TRIGGER"] = f"no {TRIGGER_KEY} trigger found — defaults to yellow"
        return out
    sum_count, base, has_bonus, total = parts
    out["_score"] = (
        f"sum_count={sum_count} base_score={base} bonus={int(has_bonus)} total_score={total}"
    )

    # --- Window-anchor analysis (why production may disagree with expected) ---
    life_sum, life_base, life_bonus, life_total = _lifetime_score(coll, pid)
    prod_color = "green" if total >= 3 else "yellow"
    life_color = "green" if life_total >= 3 else "yellow"
    if prod_color != life_color:
        out["WINDOW_ANCHOR_MISMATCH"] = (
            f"production={prod_color} (windowed on {TRIGGER_KEY}: sum_count={sum_count}, "
            f"total={total}) but analytics/lifetime={life_color} (sum_count={life_sum}, "
            f"total={life_total}). The {len(TARGET_KEYS)}-key wrong-argument activity and "
            f"the BackingInfoPanel use all occur BEFORE {TRIGGER_KEY} fires, so the "
            f"production window captures none of them. The file's documented window is "
            f"Start={DOC_START_KEY} .. End={DOC_END_KEY}; that window DOES contain the "
            f"activity and yields {life_color}. Fix: anchor the window on "
            f"{DOC_START_KEY}/{DOC_END_KEY}, not {TRIGGER_KEY}."
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
