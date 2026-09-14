"""Reason codes for Unit 4 Point 1 — "Well What Have We Here?".

mhs-unit4-point1-grading.md, "## Reason Codes":

  SCORE_BELOW_THRESHOLD — mirrors the production color formula: +0.5 if 88:5
      (correct water-table answer) in window, +1.0 if the Unit 4 soil key
      puzzle took <= 30s, +0.5 if 30-90s; triggered when score < 1.
      choice_phrase / duration_phrase are the message fragments.

Window: latest `DialogueNodeEvent:88:0` (start, exclusive) .. latest Unit-4
`Soil Key Puzzle` close (`Soil Key Puzzle Status` = "Finished",
`data.Unit` =~ /^Unit 4/; end, inclusive); end must be after start. The
duration runs from the earliest Unit-4 "Started" soil-key event inside the
window to the end anchor, using serverTimestamp.
"""

from datetime import datetime

from rc_common import GAME, gt_lte, has_keys, js_round, latest

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
    latest_start = latest(coll, pid, START_KEY)
    latest_end = coll.find_one(_soilkey_query(pid, END_STATUS), sort={"_id": -1})
    if not latest_start or not latest_end or latest_end["_id"] <= latest_start["_id"]:
        return None
    return latest_start, latest_end


def attempt_window(coll, pid):
    a = _anchors(coll, pid)
    return (a[0]["_id"], a[1]["_id"]) if a else None


def score_below_threshold(coll, pid):
    a = _anchors(coll, pid)
    if a is None:
        return {"triggered": False, "choice_phrase": "", "duration_phrase": ""}
    latest_start, latest_end = a
    f = gt_lte((latest_start["_id"], latest_end["_id"]))

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
