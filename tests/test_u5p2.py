"""Test for Unit 5 Point 2 — "If I Had a Nickel- Floors 3 & 4".

Production rule (mhs-unit5-point2-grading.md): score-based on WaterChamberEvent
machine interactions within the latest attempt window. The window is anchored on
the latest START (`questFinishEvent:43`) and latest END (`DialogueNodeEvent:96:1`)
found independently; if either is missing or the end precedes the start =>
yellow. Inside the window:

    floor3_attempts = WaterChamberEvent, data.floor "3", data.machineType in
                      VALID_TYPES (Condenser/Evaporator)
    floor4_attempts = same but data.floor "4"
    score = 0
    floor3: +2 if <=6,  +1 if <11
    floor4: +2 if <=5,  +1 if <10
    green iff score >= 3.
"""

from mhs_harness import GAME

META = {"unit": 5, "point": 2, "name": "If I Had a Nickel- Floors 3 & 4", "expected": "green"}

WINDOW_START_KEY = "questFinishEvent:43"
WINDOW_END_KEY = "DialogueNodeEvent:96:1"
VALID_TYPES = ["Condenser", "Evaporator"]


def _window(coll, pid):
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_START_KEY}, sort={"_id": -1}
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": WINDOW_END_KEY}, sort={"_id": -1}
    )
    if not latest_start or not latest_end or latest_end["_id"] < latest_start["_id"]:
        return None
    return latest_start["_id"], latest_end["_id"]


def _score_parts(coll, pid):
    win = _window(coll, pid)
    if win is None:
        return None
    window_start_id, window_end_id = win
    win_filter = {"_id": {"$gt": window_start_id, "$lte": window_end_id}}

    floor3_attempts = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "WaterChamberEvent",
            "data.floor": "3",
            "data.machineType": {"$in": VALID_TYPES},
            **win_filter,
        }
    )
    floor4_attempts = coll.count_documents(
        {
            "game": GAME,
            "playerId": pid,
            "eventType": "WaterChamberEvent",
            "data.floor": "4",
            "data.machineType": {"$in": VALID_TYPES},
            **win_filter,
        }
    )

    score = 0
    if floor3_attempts <= 6:
        score += 2
    elif floor3_attempts < 11:
        score += 1

    if floor4_attempts <= 5:
        score += 2
    elif floor4_attempts < 10:
        score += 1

    return floor3_attempts, floor4_attempts, score


def grade(coll, pid):
    parts = _score_parts(coll, pid)
    if parts is None:
        return "yellow"
    _, _, score = parts
    return "yellow" if score < 3 else "green"


def diagnose(coll, pid):
    out = {}
    parts = _score_parts(coll, pid)
    if parts is None:
        out["NO_TRIGGER"] = (
            f"no {WINDOW_END_KEY}/{WINDOW_START_KEY} attempt window found — "
            f"defaults to yellow"
        )
        return out
    floor3_attempts, floor4_attempts, score = parts
    out["_score"] = (
        f"floor3_attempts={floor3_attempts} floor4_attempts={floor4_attempts} "
        f"score={score}"
    )
    if score < 3:
        if floor3_attempts > 6:
            out["TOO_MANY_ATTEMPTS_3"] = (
                f"floor3_attempts={floor3_attempts} (>6) — too many condenser/"
                f"evaporator interactions on the 3rd floor"
            )
        if floor4_attempts > 5:
            out["TOO_MANY_ATTEMPTS_4"] = (
                f"floor4_attempts={floor4_attempts} (>5) — too many condenser/"
                f"evaporator interactions on the 4th floor"
            )
    return out


if __name__ == "__main__":
    from mhs_report import run_standalone

    run_standalone("__main__")
