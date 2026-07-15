"""Test for Unit 2 Point 6 — "Which Watershed? Part I".

Production rule (mhs-unit2-point6-grading.md): within the latest attempt window
(previous `DialogueNodeEvent:20:35` exclusive .. latest `DialogueNodeEvent:20:35`
inclusive), green iff the pass node is present AND no yellow node is present. No
trigger => yellow.

Note: the COLOR production script windows on `DialogueNodeEvent:20:35`, while the
HIT_YELLOW_NODE reason production script windows on `DialogueNodeEvent:20:46`.
"""

from mhs_harness import GAME, latest_trigger_window

META = {"unit": 2, "point": 6, "name": "Which Watershed? Part I", "expected": "green"}

TRIGGER_KEY = "DialogueNodeEvent:20:35"
PASS_KEY = "DialogueNodeEvent:20:43"
YELLOW_KEYS = ["DialogueNodeEvent:20:44", "DialogueNodeEvent:20:45"]

# HIT_YELLOW_NODE reason script windows on a different trigger key.
REASON_TRIGGER_KEY = "DialogueNodeEvent:20:46"
KEY_44 = "DialogueNodeEvent:20:44"
KEY_45 = "DialogueNodeEvent:20:45"


def grade(coll, pid):
    win = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win is None:
        return "yellow"
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}
    has_pass = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": PASS_KEY, **win_filter})
        is not None
    )
    if not has_pass:
        return "yellow"
    has_yellow = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": {"$in": YELLOW_KEYS}, **win_filter})
        is not None
    )
    return "yellow" if has_yellow else "green"


def _analytics_color(coll, pid):
    """Lifetime (analytics-matching) color: green iff pass node exists and no
    yellow node exists, ignoring any attempt window."""
    has_pass = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": PASS_KEY}) is not None
    )
    if not has_pass:
        return "yellow"
    has_yellow = (
        coll.find_one({"game": GAME, "playerId": pid, "eventKey": {"$in": YELLOW_KEYS}})
        is not None
    )
    return "yellow" if has_yellow else "green"


def diagnose(coll, pid):
    out = {}

    # --- Window-anchor analysis (why production may disagree with expected) ---
    prod = grade(coll, pid)
    analytics = _analytics_color(coll, pid)
    pass_lifetime = coll.find_one({"game": GAME, "playerId": pid, "eventKey": PASS_KEY})
    pass_in_window = False
    win0 = latest_trigger_window(coll, pid, TRIGGER_KEY)
    if win0 is not None and pass_lifetime is not None:
        s0, e0 = win0
        pass_in_window = (
            coll.find_one(
                {"game": GAME, "playerId": pid, "eventKey": PASS_KEY,
                 "_id": {"$gt": s0, "$lte": e0}}
            )
            is not None
        )
    if prod != analytics:
        if pass_lifetime is not None and not pass_in_window:
            out["WINDOW_ANCHOR_MISMATCH"] = (
                f"production={prod} but analytics/lifetime={analytics}. The pass "
                f"node {PASS_KEY} EXISTS but falls OUTSIDE the production window "
                f"(window END anchor is {TRIGGER_KEY}, which fires before the pass "
                f"node). The documented Trigger(End) is {REASON_TRIGGER_KEY}, which "
                f"occurs after the pass node — windowing on {TRIGGER_KEY} ends the "
                f"window too early and drops the pass node. Fix: anchor the window "
                f"end on {REASON_TRIGGER_KEY}, not {TRIGGER_KEY}."
            )
        else:
            out["COLOR_MISMATCH"] = (
                f"production={prod} vs analytics/lifetime={analytics} — review window logic"
            )

    # HIT_YELLOW_NODE windows on REASON_TRIGGER_KEY (DialogueNodeEvent:20:46).
    win = latest_trigger_window(coll, pid, REASON_TRIGGER_KEY)
    if win is None:
        out["MISSING_TRIGGER"] = (
            f"no {REASON_TRIGGER_KEY} trigger found — defaults to yellow"
        )
        return out
    start, end = win
    win_filter = {"_id": {"$gt": start, "$lte": end}}

    events = coll.find(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": [KEY_44, KEY_45]}, **win_filter}
    )
    triggered = {e["eventKey"] for e in events}
    has_44 = KEY_44 in triggered
    has_45 = KEY_45 in triggered

    if has_44 and has_45:
        result = "guessing through the correct answer"
    elif has_44:
        result = "waterfall height"
    elif has_45:
        result = "salinity"
    else:
        result = None

    if result is not None:
        out["HIT_YELLOW_NODE"] = (
            f"chose an incorrect criterion for watershed size on first try: {result}"
        )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
