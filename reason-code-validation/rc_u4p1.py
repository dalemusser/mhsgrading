"""Reason codes for Unit 4 Point 1 — "Well What Have We Here?".

mhs-unit4-point1-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — mirrors the production color formula: +0.5 if 88:5
      (correct water-table answer) in window, +1.0 if the Unit 4 soil key
      puzzle took <= 30s, +0.5 if 30-90s; triggered when score < 1.
      choice_phrase / duration_phrase are the message fragments.

Window (end-first form since 2026-09-24): latest Unit-4 `Soil Key Puzzle`
close (`Soil Key Puzzle Status` = "Finished", `data.Unit` =~ /^Unit 4/; end,
inclusive), latest `DialogueNodeEvent:88:0` before it (start, exclusive;
OID_MIN when none) — the same window as the production color script. Until
2026-09-24: latest start and latest end, end must follow start. The duration
runs from the earliest Unit-4 "Started" soil-key event inside the window to
the end anchor, using serverTimestamp. Keys re-verified 2026-09-24 against
the 2026-09-21 dialogue database (conversation 88 unchanged).
"""

from datetime import datetime

from rc_common import GAME, OID_MIN, gt_lte, has_keys, js_round, latest

META = {"unit": 4, "point": 1, "name": "Well What Have We Here?",
        "doc": "mhs-unit4-point1-grading.md"}

START_KEY = "DialogueNodeEvent:88:0"
CORRECT_KEY = "DialogueNodeEvent:88:5"
WRONG_KEY = "DialogueNodeEvent:88:7"   # "any water found underground" (informational)

EVENT_TYPE = "Soil Key Puzzle"
START_STATUS = "Started"
END_STATUS = "Finished"
UNIT_4 = "^Unit 4"  # data.Unit is the scene name; puzzle also fires in U2/U3


def _soilkey_query(pid, status):
    return {
        "game": GAME, "playerId": pid, "eventType": EVENT_TYPE,
        "data.Soil Key Puzzle Status": status, "data.Unit": {"$regex": UNIT_4},
    }


def _server_iso(doc):
    """serverTimestamp is exported as {"$date": "..."} (or a raw string)."""
    if not doc:
        return None
    v = doc.get("serverTimestamp")
    if isinstance(v, dict):
        return v.get("$date")
    return v


def _to_ms(iso):
    """`new Date(iso).getTime()`; None when unparseable (JS NaN)."""
    if not iso:
        return None
    try:
        return datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000.0
    except ValueError:
        return None


def _anchors(coll, pid):
    """(windowStartId, latestEndDoc) or None when no Unit-4 soil-key close."""
    # 1) Latest end anchor: latest Unit 4 soil key puzzle close
    latest_end = coll.find_one(_soilkey_query(pid, END_STATUS), sort={"_id": -1})
    if not latest_end:
        return None
    # 2) Latest start anchor before the latest end
    latest_start = latest(coll, pid, START_KEY, {"_id": {"$lt": latest_end["_id"]}})
    window_start_id = latest_start["_id"] if latest_start else OID_MIN
    return window_start_id, latest_end


def attempt_window(coll, pid):
    a = _anchors(coll, pid)
    return (a[0], a[1]["_id"]) if a else None


def score_below_threshold(coll, pid):
    a = _anchors(coll, pid)
    if a is None:
        return {"triggered": False, "choice_phrase": "", "duration_phrase": ""}
    window_start_id, latest_end = a
    f = gt_lte((window_start_id, latest_end["_id"]))

    has_correct = has_keys(coll, pid, CORRECT_KEY, f)

    # Earliest Unit 4 puzzle start inside the window; the end anchor is the close.
    start_doc = coll.find_one({**_soilkey_query(pid, START_STATUS), **f}, sort={"_id": 1})

    duration_seconds = None
    if start_doc and _server_iso(start_doc) and _server_iso(latest_end):
        start_ms = _to_ms(_server_iso(start_doc))
        end_ms = _to_ms(_server_iso(latest_end))
        if start_ms is not None and end_ms is not None:
            duration_seconds = (end_ms - start_ms) / 1000.0

    score = 0.0
    if has_correct:
        score += 0.5
    if duration_seconds is not None:
        if 0 < duration_seconds <= 30:
            score += 1.0
        elif 30 < duration_seconds <= 90:
            score += 0.5

    choice_phrase = (
        "answered correctly" if has_correct
        else "chose 'it's any water found underground' instead of the correct answer on"
    )
    duration_phrase = (
        "took " + str(js_round(duration_seconds)) + " seconds to solve"
        if duration_seconds is not None
        else "has no measured completion time for"
    )

    return {"triggered": score < 1, "choice_phrase": choice_phrase,
            "duration_phrase": duration_phrase}


CODES = {"SCORE_BELOW_THRESHOLD": score_below_threshold}


if __name__ == "__main__":
    from rc_common import run_standalone

    run_standalone("__main__")
