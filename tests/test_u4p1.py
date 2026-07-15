"""Test for Unit 4 Point 1 — "Well What Have We Here?: Water Table Basics".

Production rule (mhs-unit4-point1-grading.md): score-based, within the latest
attempt window anchored on the latest START (`DialogueNodeEvent:88:0`) and the
latest END (`DialogueNodeEvent:88:10`). Both anchors required and END must be
after START (else yellow).

    +0.5  if CORRECT_KEY (`DialogueNodeEvent:88:5`) present inside window
    +1.0  if 0 < soil-key-puzzle duration <= 30s
    +0.5  if 30s < duration <= 90s
    green iff score >= 1, else yellow.

The soil key puzzle duration is the gap between the earliest "Soil Key Puzzle"
event with status "Started" inside the window and the earliest "Finished" event
strictly after that Started doc (still inside the window), using serverTimestamp.
"""

from datetime import datetime

from mhs_harness import GAME

META = {
    "unit": 4,
    "point": 1,
    "name": "Well What Have We Here?: Water Table Basics",
    "expected": "green",
}

START_KEY = "DialogueNodeEvent:88:0"
END_KEY = "DialogueNodeEvent:88:10"
CORRECT_KEY = "DialogueNodeEvent:88:5"

EVENT_TYPE = "Soil Key Puzzle"
START_STATUS = "Started"
END_STATUS = "Finished"


def _server_iso(doc):
    """Extract the serverTimestamp ISO string ({"$date": "..."} or raw)."""
    if not doc:
        return None
    v = doc.get("serverTimestamp")
    if isinstance(v, dict):
        return v.get("$date")
    return v


def _to_ms(iso):
    """Parse an ISO-8601 timestamp to epoch milliseconds (None on failure)."""
    if not iso:
        return None
    s = iso.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(s).timestamp() * 1000.0
    except ValueError:
        return None


def _parts(coll, pid):
    """Returns (score, has_correct, duration_seconds, reason).
    reason is None on success or a string when the window cannot be
    established (=> yellow)."""
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": START_KEY}, sort={"_id": -1}
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": END_KEY}, sort={"_id": -1}
    )

    if not latest_start or not latest_end:
        return None, None, None, "missing start or end anchor"
    if latest_end["_id"] <= latest_start["_id"]:
        return None, None, None, "end anchor not after start anchor"

    window_start_id = latest_start["_id"]
    window_end_id = latest_end["_id"]
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}

    score = 0.0

    has8805 = (
        coll.find_one(
            {"game": GAME, "playerId": pid, "eventKey": CORRECT_KEY, **win_filter}
        )
        is not None
    )
    if has8805:
        score += 0.5

    start_doc = coll.find_one(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": EVENT_TYPE,
            "data.Soil Key Puzzle Status": START_STATUS,
            **win_filter,
        },
        sort={"_id": 1},
    )

    duration_seconds = None
    if start_doc and _server_iso(start_doc):
        end_doc = coll.find_one(
            {
                "game": GAME,
                "playerId": pid,
                "eventType": EVENT_TYPE,
                "data.Soil Key Puzzle Status": END_STATUS,
                "_id": {"$gt": start_doc["_id"], "$lte": window_end_id},
            },
            sort={"_id": 1},
        )
        if end_doc and _server_iso(end_doc):
            start_ms = _to_ms(_server_iso(start_doc))
            end_ms = _to_ms(_server_iso(end_doc))
            if start_ms is not None and end_ms is not None:
                duration_seconds = (end_ms - start_ms) / 1000.0

    if duration_seconds is not None:
        if 0 < duration_seconds <= 30:
            score += 1.0
        elif 30 < duration_seconds <= 90:
            score += 0.5

    return score, has8805, duration_seconds, None


def grade(coll, pid):
    score, _, _, reason = _parts(coll, pid)
    if reason is not None:
        return "yellow"
    return "green" if score >= 1 else "yellow"


def diagnose(coll, pid):
    out = {}
    score, has_correct, duration_seconds, reason = _parts(coll, pid)
    if reason is not None:
        out["NO_TRIGGER"] = (
            f"{reason} — trigger event {END_KEY} window not established, defaults to yellow"
        )
        return out
    out["_score"] = (
        f"score={score} has_correct={int(bool(has_correct))} "
        f"duration_seconds={duration_seconds}"
    )
    if score < 1:
        if not has_correct:
            out["WRONG_CHOISE_SELECTED"] = (
                f"correct choice {CORRECT_KEY} absent in window — did not select "
                f"the water-table boundary answer on first attempt"
            )
        if duration_seconds is None or duration_seconds > 30:
            out["TOO_LONG_TO_SOLVE_PROBLEM"] = (
                f"soil key puzzle duration={duration_seconds}s (> 30s or unmeasured) — "
                f"spent too long solving the soil key puzzle"
            )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
