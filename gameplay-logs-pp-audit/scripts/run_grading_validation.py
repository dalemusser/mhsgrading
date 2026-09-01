"""Phase 7 (Stage 2) — execute the current production grading logic against
the audited gameplay logs and trace what it computes.

Executor: the 1:1 Python transcriptions under tests/ (mhs_harness + the 26
test modules), reused as-is EXCEPT:

  * ADAPTATION (recorded, never silent): the 08-25-26 export identifies the
    player via top-level `user_id`, while every production script filters on
    `playerId`. Queries are translated playerId -> <detected field>. Without
    this the scripts match zero records and everything degrades to "yellow".
  * OVERRIDES: tests/test_u2p6.py and tests/test_u3p3.py transcribe the
    pre-2026-07-22 production scripts; the markdown files have since been
    fixed (U2P6: latest-23:42 -> latest-20:46 window; U3P3: window anchored
    on questFinishEvent:18). Audit-local overrides below transcribe the
    CURRENT markdown production scripts. The stale test modules are reported,
    not modified.

Independent cross-check: for every module whose grade() windows via
`latest_trigger_window`, the same logic is re-run over a *doc-derived
activity window* (last start-marker occurrence before the last end-marker
occurrence, markers from Progress-Points.docx). Production color vs
doc-window color disagreement reproduces the round-1 "window anchored on the
wrong key" bug class.

Outputs: outputs/grading-validation.json / .csv
"""

import importlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

cfg = lib.load_config()
TESTS_DIR = lib.repo_path(cfg["tests_dir"])
sys.path.insert(0, TESTS_DIR)

import mhs_harness  # noqa: E402  (from tests/)
from mhs_harness import GAME, OID_MIN, Collection  # noqa: E402


# ---------------------------------------------------------------------------
# Instrumented, field-adapted collection
# ---------------------------------------------------------------------------


class AdaptedCollection(Collection):
    """Translates `playerId` filters to the detected player field and records
    every query for the trace output."""

    def __init__(self, docs, player_field):
        super().__init__(docs)
        self.player_field = player_field
        self.trace = []

    def _adapt(self, query):
        if self.player_field != "playerId" and "playerId" in query:
            query = dict(query)
            query[self.player_field] = query.pop("playerId")
        return query

    def _filtered(self, query):
        res = super()._filtered(self._adapt(query))
        self.trace.append(
            {
                "query": {k: v for k, v in query.items() if k not in ("game",)},
                "matches": len(res),
            }
        )
        return res


def _fmt_query(q):
    out = {}
    for k, v in q.items():
        if isinstance(v, dict) and "$in" in v and len(v["$in"]) > 6:
            out[k] = {"$in": f"<{len(v['$in'])} keys>"}
        else:
            out[k] = v
    return out


# ---------------------------------------------------------------------------
# Audit-local overrides for stale test transcriptions
# ---------------------------------------------------------------------------


def grade_u2p6_current(coll, pid):
    """Current mhs-unit2-point6-grading.md production script:
    window = latest 23:42 (exclusive) .. latest 20:46 (inclusive)."""
    start_t = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:23:42"},
        sort={"_id": -1},
    )
    end_t = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:20:46"},
        sort={"_id": -1},
    )
    if not start_t or not end_t or end_t["_id"] <= start_t["_id"]:
        return "yellow"
    wf = {"_id": {"$gt": start_t["_id"], "$lte": end_t["_id"]}}
    has_pass = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:20:43", **wf}
    ) is not None
    if not has_pass:
        return "yellow"
    has_yellow = coll.find_one(
        {"game": GAME, "playerId": pid,
         "eventKey": {"$in": ["DialogueNodeEvent:20:44", "DialogueNodeEvent:20:45"]}, **wf}
    ) is not None
    return "yellow" if has_yellow else "green"


def grade_u3p3_current(coll, pid):
    """Current mhs-unit3-point3-grading.md production script: window =
    previous questFinishEvent:18 (exclusive) .. latest questFinishEvent:18
    (inclusive); score = base(sum of 18 wrong-arg keys) + BackingInfoPanel
    bonus; green iff score >= 3."""
    trigger = "questFinishEvent:18"
    win = mhs_harness.latest_trigger_window(coll, pid, trigger)
    if win is None:
        return "yellow"
    start, end = win
    wf = {"_id": {"$gt": start, "$lte": end}}
    target_keys = [f"DialogueNodeEvent:84:{n}" for n in (20, 25)] + [
        f"DialogueNodeEvent:84:{n}" for n in range(32, 48)
    ]
    sum_count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": target_keys}, **wf}
    )
    base = 3 if sum_count <= 3 else 2 if sum_count == 4 else 1 if sum_count == 5 else 0
    has_bonus = coll.find_one(
        {"game": GAME, "playerId": pid, "eventType": "argumentationToolEvent",
         "data.toolName": "BackingInfoPanel - Pollution Site Data", **wf}
    ) is not None
    return "green" if base + (1 if has_bonus else 0) >= 3 else "yellow"


def grade_u1p3_current(coll, pid):
    """Current mhs-unit1-point3-grading.md production script: window =
    previous/latest questActiveEvent:34 (unchanged); YELLOW_KEYS reduced to
    70:25 only (dead key 70:33 removed in the 2026-08-31 update)."""
    win = mhs_harness.latest_trigger_window(coll, pid, "questActiveEvent:34")
    if win is None:
        return "yellow"
    start, end = win
    has_yellow = coll.find_one(
        {"game": GAME, "playerId": pid,
         "eventKey": {"$in": ["DialogueNodeEvent:70:25"]},
         "_id": {"$gt": start, "$lte": end}}
    ) is not None
    return "yellow" if has_yellow else "green"


U2P2_TARGET_KEYS = [
    "DialogueNodeEvent:28:179", "DialogueNodeEvent:59:179",
    "DialogueNodeEvent:28:182", "DialogueNodeEvent:59:182",
    "DialogueNodeEvent:28:183", "DialogueNodeEvent:59:183",
]


def grade_u2p2_current(coll, pid):
    """Current mhs-unit2-point2-grading.md production script: same window
    (latest 20:26 end, latest questFinishEvent:21 start before it, iso+_id
    fence); TARGET_KEYS reduced — the three conv-18 keys (18:99/223/224)
    removed in the 2026-08-31 update. Green iff count <= 1."""
    end_doc = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:20:26"},
        sort={"_id": -1},
    )
    if not end_doc or not end_doc.get("timestamp"):
        return "yellow"
    start_doc = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questFinishEvent:21",
         "_id": {"$lte": end_doc["_id"]}},
        sort={"_id": -1},
    )
    if not start_doc or not start_doc.get("timestamp"):
        return "yellow"
    count = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": U2P2_TARGET_KEYS},
         "timestamp": {"$gte": start_doc["timestamp"], "$lte": end_doc["timestamp"]},
         "_id": {"$gte": start_doc["_id"], "$lte": end_doc["_id"]}}
    )
    return "green" if count <= 1 else "yellow"


U2P5_POS_KEYS = [f"DialogueNodeEvent:26:{n}" for n in (
    140, 142, 143, 146, 147, 148, 165, 166, 167, 168, 169, 170, 172, 173,
    174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186)]
U2P5_NEG_KEYS = [f"DialogueNodeEvent:26:{n}" for n in (
    137, 144, 145, 187, 188, 189, 191, 192, 193, 194, 195, 196, 197, 198,
    199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211)]


def grade_u2p5_current(coll, pid):
    """Current mhs-unit2-point5-grading.md production script: same window
    (prev/latest 23:42); POS/NEG key sets remapped in the 2026-08-31 update
    (POS +140/142/143/146/147/148 −171; NEG +137/144/145 −190).
    Green iff pos - neg/3 >= 4."""
    win = mhs_harness.latest_trigger_window(coll, pid, "DialogueNodeEvent:23:42")
    if win is None:
        return "yellow"
    start, end = win
    wf = {"_id": {"$gt": start, "$lte": end}}
    pos = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": U2P5_POS_KEYS}, **wf})
    neg = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": U2P5_NEG_KEYS}, **wf})
    return "green" if pos - neg / 3.0 >= 4 else "yellow"


U2P7_NEG_KEYS = [f"DialogueNodeEvent:27:{n}" for n in (
    11, 12, 13, 14, 15, 16, 17, 18, 20, 25, 26, 27, 28, 29, 30)]


def grade_u2p7_current(coll, pid):
    """Current mhs-unit2-point7-grading.md production script: same window
    (prev/latest questFinishEvent:54); NEG_KEYS reduced — dead keys
    27:19/21/22/23/24 removed in the 2026-08-31 update. Green iff success
    27:7 present AND neg_count <= 3."""
    win = mhs_harness.latest_trigger_window(coll, pid, "questFinishEvent:54")
    if win is None:
        return "yellow"
    start, end = win
    wf = {"_id": {"$gt": start, "$lte": end}}
    has_success = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:27:7", **wf}
    ) is not None
    neg = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": U2P7_NEG_KEYS}, **wf})
    return "green" if (has_success and neg <= 3) else "yellow"


U4P6_EXPECTED_SOIL_BY_BOX = {"0": "Gravel", "1": "Sand", "2": "Clay"}


def grade_u4p6_current(coll, pid):
    """Current mhs-unit4-point6-grading.md production script: window = latest
    questActiveEvent:41 .. latest questFinishEvent:56; box→soil mapping fixed
    in the 2026-08-31 update (box0=Gravel, box1=Sand, box2=Clay). 2026-09-01
    update adds a box-id-independent OR fallback: dialogueScore = count of
    correct-soil feedback 92:61 after the latest review-start 92:33 in the
    window (whole window if 92:33 missing), capped at 3; final score =
    max(box score, dialogueScore). Green iff final score >= 2."""
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questActiveEvent:41"},
        sort={"_id": -1},
    )
    latest_end = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questFinishEvent:56"},
        sort={"_id": -1},
    )
    if not latest_start or not latest_end or latest_end["_id"] < latest_start["_id"]:
        return "yellow"
    wf = {"_id": {"$gt": latest_start["_id"], "$lte": latest_end["_id"]}}
    score = 0
    for box_id, expected in U4P6_EXPECTED_SOIL_BY_BOX.items():
        latest_box = coll.find_one(
            {"game": GAME, "playerId": pid, "eventType": "TerasGardenBox",
             "data.actionType": "cameraPlaced", "data.boxId": box_id, **wf},
            sort={"_id": -1},
        )
        if latest_box and latest_box.get("data") and latest_box["data"].get("soilType") == expected:
            score += 1
    latest_review = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:92:33", **wf},
        sort={"_id": -1},
    )
    fb_start = latest_review["_id"] if latest_review else latest_start["_id"]
    dialogue_score = min(3, coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:92:61",
         "_id": {"$gt": fb_start, "$lte": latest_end["_id"]}}
    ))
    return "green" if max(score, dialogue_score) >= 2 else "yellow"


# --- U4P1 / U4P2: re-anchored off optional node 88:10 (2026-09-01 update) ----
# The 08-31-26 audit found 88:10 vs 88:11 are alternate branches (88:10 never
# fires on a clean solve), so both points now anchor on the CLOSE of the Unit 4
# soil key puzzle: eventType "Soil Key Puzzle", data["Soil Key Puzzle Status"]
# = "Finished", data.Unit matching /^Unit 4/ (the puzzle also fires in Units 2
# and 3; data.Unit holds the build-flavored scene name, hence prefix match).
# The tests/ harness has no $regex, so the Unit filter is applied in Python.


def _server_iso(doc):
    if not doc:
        return None
    v = doc.get("serverTimestamp")
    if isinstance(v, dict):
        return v.get("$date")
    return v


def _to_ms(iso):
    from datetime import datetime
    if not iso:
        return None
    try:
        return datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000.0
    except ValueError:
        return None


def _is_unit4(doc):
    return str(((doc or {}).get("data") or {}).get("Unit") or "").startswith("Unit 4")


def _u4_soilkey_docs(coll, pid, status, id_filter=None, sort_dir=-1):
    """Unit-4 'Soil Key Puzzle' status records, harness query + Python Unit filter."""
    q = {"game": GAME, "playerId": pid, "eventType": "Soil Key Puzzle",
         "data.Soil Key Puzzle Status": status}
    if id_filter:
        q["_id"] = id_filter
    return [d for d in coll.find(q, sort={"_id": sort_dir}) if _is_unit4(d)]


def grade_u4p1_current(coll, pid):
    """Current mhs-unit4-point1-grading.md production script: window = latest
    DialogueNodeEvent:88:0 (exclusive) .. latest Unit-4 soil-key close
    (inclusive); +0.5 for 88:5 in window, +1.0/+0.5 for puzzle duration
    <=30s / <=90s (Started in window -> the end anchor itself);
    green iff score >= 1."""
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:0"},
        sort={"_id": -1},
    )
    closes = _u4_soilkey_docs(coll, pid, "Finished")
    latest_end = closes[0] if closes else None
    if not latest_start or not latest_end or latest_end["_id"] <= latest_start["_id"]:
        return "yellow"
    wf = {"_id": {"$gt": latest_start["_id"], "$lte": latest_end["_id"]}}
    score = 0.0
    if coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:5", **wf}
    ) is not None:
        score += 0.5
    started = _u4_soilkey_docs(coll, pid, "Started", id_filter=wf["_id"], sort_dir=1)
    duration = None
    if started:
        s_ms, e_ms = _to_ms(_server_iso(started[0])), _to_ms(_server_iso(latest_end))
        if s_ms is not None and e_ms is not None:
            duration = (e_ms - s_ms) / 1000.0
    if duration is not None:
        if 0 < duration <= 30:
            score += 1.0
        elif 30 < duration <= 90:
            score += 0.5
    return "green" if score >= 1 else "yellow"


U4P2_NEGATIVE_KEYS = [f"DialogueNodeEvent:102:{n}" for n in (9, 10, 12, 18, 23)]


def grade_u4p2_current(coll, pid):
    """Current mhs-unit4-point2-grading.md production script: window = latest
    Unit-4 soil-key close before the trigger (exclusive; OID_MIN fallback) ..
    latest questActiveEvent:48 (inclusive). Green iff 88:11 in window and no
    conv-102 negative feedback in window."""
    latest_trigger = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questActiveEvent:48"},
        sort={"_id": -1},
    )
    if not latest_trigger:
        return "yellow"
    closes = _u4_soilkey_docs(coll, pid, "Finished",
                              id_filter={"$lt": latest_trigger["_id"]})
    start_id = closes[0]["_id"] if closes else OID_MIN
    wf = {"_id": {"$gt": start_id, "$lte": latest_trigger["_id"]}}
    has_8811 = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:11", **wf}
    ) is not None
    if not has_8811:
        return "yellow"
    has_neg = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": U4P2_NEGATIVE_KEYS}, **wf}
    ) is not None
    return "yellow" if has_neg else "green"


def _u4p1_window(coll, pid):
    latest_start = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:0"},
        sort={"_id": -1},
    )
    closes = _u4_soilkey_docs(coll, pid, "Finished")
    if not latest_start or not closes or closes[0]["_id"] <= latest_start["_id"]:
        return None
    return latest_start["_id"], closes[0]["_id"]


def _u4p2_window(coll, pid):
    latest_trigger = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questActiveEvent:48"},
        sort={"_id": -1},
    )
    if not latest_trigger:
        return None
    closes = _u4_soilkey_docs(coll, pid, "Finished",
                              id_filter={"$lt": latest_trigger["_id"]})
    return (closes[0]["_id"] if closes else OID_MIN), latest_trigger["_id"]


OVERRIDES = {
    "U1P3": {
        "grade": grade_u1p3_current,
        "trigger_key": "questActiveEvent:34",
        "note": "tests/test_u1p3.py transcribes the pre-2026-08-31 script "
                "(YELLOW_KEYS still include dead key 70:33); override matches "
                "the current markdown (70:25 only)",
    },
    "U2P2": {
        "grade": grade_u2p2_current,
        "trigger_key": None,  # custom start/end window; doc-window check n/a
        "note": "tests/test_u2p2.py transcribes the pre-2026-08-31 script "
                "(TARGET_KEYS still include 18:99/18:223/18:224); override "
                "matches the current markdown (six conv-28/59 keys only)",
    },
    "U2P5": {
        "grade": grade_u2p5_current,
        "trigger_key": "DialogueNodeEvent:23:42",
        "note": "tests/test_u2p5.py transcribes the pre-2026-08-31 key sets "
                "(POS 165-186 incl. dead 26:171, NEG 187-211); override matches "
                "the current markdown remapped POS/NEG sets",
    },
    "U2P6": {
        "grade": grade_u2p6_current,
        "trigger_key": None,  # custom two-key window; doc-window check n/a
        "note": "tests/test_u2p6.py transcribes the pre-2026-07-22 script "
                "(windows on 20:35); override implements the current markdown "
                "window latest-23:42 .. latest-20:46",
    },
    "U2P7": {
        "grade": grade_u2p7_current,
        "trigger_key": "questFinishEvent:54",
        "note": "tests/test_u2p7.py transcribes the pre-2026-08-31 script "
                "(NEG_KEYS still include dead 27:19/21/22/23/24); override "
                "matches the current markdown (15 keys)",
    },
    "U3P3": {
        "grade": grade_u3p3_current,
        "trigger_key": "questFinishEvent:18",
        "note": "tests/test_u3p3.py transcribes the pre-2026-07-22 script "
                "(windows on questActiveEvent:18); override windows on "
                "questFinishEvent:18 per the current markdown",
    },
    "U4P6": {
        "grade": grade_u4p6_current,
        "trigger_key": None,  # two-anchor window; doc-window check n/a
        "note": "tests/test_u4p6.py transcribes the pre-2026-08-31 script "
                "(inverted box0=Clay/box2=Gravel map); override matches the "
                "current markdown: fixed map box0=Gravel/box1=Sand/box2=Clay "
                "plus the 2026-09-01 dialogue-feedback OR fallback (92:61 count)",
    },
    "U4P1": {
        "grade": grade_u4p1_current,
        "trigger_key": None,  # custom two-anchor window; doc-window check n/a
        "window_fn": _u4p1_window,
        "window_desc": "latest DialogueNodeEvent:88:0 .. latest Unit-4 soil-key close",
        "note": "tests/test_u4p1.py transcribes the pre-2026-09-01 script "
                "(END_KEY = optional node 88:10, never fires on a clean solve); "
                "override matches the current markdown: end anchor = Unit-4 "
                "Soil Key Puzzle Finished (data.Unit ^Unit 4), duration ends "
                "at the anchor itself",
    },
    "U4P2": {
        "grade": grade_u4p2_current,
        "trigger_key": None,  # custom window start; doc-window check n/a
        "window_fn": _u4p2_window,
        "window_desc": "latest Unit-4 soil-key close .. latest questActiveEvent:48",
        "note": "tests/test_u4p2.py transcribes the pre-2026-09-01 script "
                "(window start = previous questActiveEvent:48; prose said the "
                "unfired 88:10); override matches the current markdown: window "
                "start = latest Unit-4 soil-key close before the trigger",
    },
}

COMPLETION_ONLY = {"U1P1", "U1P2", "U1P4"}


# ---------------------------------------------------------------------------
# Special-case independent checks (documented evidence-based expectations)
# ---------------------------------------------------------------------------


def special_u4p6(coll, pid, rec):
    """Expected color from the grading file's rule PROSE mapping (box0=Gravel,
    box1=Sand, box2=Clay — also the analytics-script and Go-grader mapping),
    applied to the observed latest cameraPlaced placement per box (unwindowed —
    deliberately independent of the production window). The 2026-08-31 update
    aligned the production script with this mapping; before that it inverted
    box0/box2."""
    prose_map = {"0": "Gravel", "1": "Sand", "2": "Clay"}
    correct = 0
    placements = {}
    for box, soil in prose_map.items():
        latest = coll.find_one(
            {"game": GAME, "playerId": pid, "eventType": "TerasGardenBox",
             "data.actionType": "cameraPlaced", "data.boxId": box},
            sort={"_id": -1},
        )
        got = (latest or {}).get("data", {}).get("soilType")
        placements[f"box{box}"] = got
        if got == soil:
            correct += 1
    expected = "green" if correct >= 2 else "yellow"
    basis = (
        f"rule prose mapping box0=Gravel/box1=Sand/box2=Clay applied to observed "
        f"latest placements {placements} -> {correct}/3 correct. Production script "
        f"uses the same mapping since the 2026-08-31 fix (previously inverted "
        f"box0/box2 — the 08-25-26 audit's U4P6 finding)."
    )
    root = []
    if expected != rec.get("production_color"):
        root = [
            "GRADING_WINDOW_OR_MAPPING_BUG candidate: production color disagrees with "
            "the rule-prose mapping applied to the observed latest placements — since "
            "the box->soil maps now agree, the divergence is in window selection or "
            "payload interpretation",
        ]
        return expected, basis, "MEDIUM", "MISMATCH_NEEDS_REVIEW", root
    return expected, basis, "MEDIUM", "PASS", root


def special_u4p1(coll, pid, rec):
    """Independent expectation for U4P1 (the 08-31-26 finding: yellow despite
    a completed puzzle, caused by the unfired optional end anchor 88:10).
    Applies the rubric formula to the observed evidence UNWINDOWED and
    box-anchor-free: +0.5 if 88:5 fired at all, duration = earliest Unit-4
    soil-key Started -> earliest Unit-4 Finished after it. Stands down when
    the Unit-4 soil key puzzle was never closed (activity not exercised)."""
    closes = _u4_soilkey_docs(coll, pid, "Finished", sort_dir=1)
    if not closes:
        return None
    score = 0.0
    has_correct = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:5"}
    ) is not None
    if has_correct:
        score += 0.5
    started = _u4_soilkey_docs(coll, pid, "Started", sort_dir=1)
    duration = None
    if started:
        end_after = [c for c in closes if c["_id"] > started[0]["_id"]]
        if end_after:
            s_ms, e_ms = _to_ms(_server_iso(started[0])), _to_ms(_server_iso(end_after[0]))
            if s_ms is not None and e_ms is not None:
                duration = (e_ms - s_ms) / 1000.0
    if duration is not None:
        if 0 < duration <= 30:
            score += 1.0
        elif 30 < duration <= 90:
            score += 0.5
    expected = "green" if score >= 1 else "yellow"
    basis = (
        f"rubric formula on unwindowed evidence: correct choice 88:5 "
        f"{'observed' if has_correct else 'absent'} (+0.5), Unit-4 soil-key "
        f"duration {duration}s -> score {score}. Independent of the production "
        f"window anchors (the 08-31-26 bug was a window-anchor failure)."
    )
    if expected != rec.get("production_color"):
        return expected, basis, "MEDIUM", "MISMATCH_NEEDS_REVIEW", [
            "GRADING_WINDOW_BUG candidate: production color disagrees with the rubric "
            "formula applied to the observed puzzle evidence"
        ]
    return expected, basis, "MEDIUM", "PASS", []


def special_u4p2(coll, pid, rec):
    """Evidence-based check for the 08-25-26 U4P2 finding: production yellow
    although the infiltration-glyph quest (47) was completed cleanly (zero
    conv-102 hint/wrong-answer nodes) and the success node 88:11 never fired —
    evidence of a changed dialogue flow rather than player failure. All
    quantities are recomputed from THIS run's logs; when the success node DID
    fire, the check instead compares production against the rubric applied to
    the unwindowed evidence (single-attempt playthrough assumption)."""
    n8811_total = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:11"}
    )
    if n8811_total > 0:
        n_neg = coll.count_documents(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": U4P2_NEGATIVE_KEYS}}
        )
        expected = "green" if n_neg == 0 else "yellow"
        basis = (
            f"success node 88:11 observed x{n8811_total}; conv-102 negative feedback "
            f"nodes observed: {n_neg}. Rubric on unwindowed evidence (valid for a "
            f"single-attempt playthrough) -> {expected}."
        )
        if expected != rec.get("production_color"):
            return expected, basis, "MEDIUM", "MISMATCH_NEEDS_REVIEW", [
                "GRADING_WINDOW_BUG candidate: production window excludes the observed "
                "success/negative evidence"
            ]
        return expected, basis, "MEDIUM", "PASS", []
    q47_done = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questFinishEvent:47"},
        sort={"_id": -1},
    )
    if not q47_done or rec.get("production_color") != "yellow":
        return None
    n102 = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventType": "DialogueEvent",
         "data.conversationId": 102}
    )
    n8811 = coll.count_documents(
        {"game": GAME, "playerId": pid, "eventKey": "DialogueNodeEvent:88:11"}
    )
    if n8811 > 0 or n102 > 0:
        # success node fired (window problem, not drift) or hint/wrong-answer
        # feedback occurred (yellow may be defensible) — let the generic
        # doc-window / no-check paths judge this instead.
        return None
    q47_active = coll.find_one(
        {"game": GAME, "playerId": pid, "eventKey": "questActiveEvent:47",
         "_id": {"$lte": q47_done["_id"]}},
        sort={"_id": -1},
    )
    debug_inside = 0
    if q47_active:
        debug_inside = coll.count_documents(
            {"game": GAME, "playerId": pid, "eventType": "DEBUGMenu",
             "_id": {"$gt": q47_active["_id"], "$lte": q47_done["_id"]}}
        )
    span = (
        f"{(q47_active or {}).get('timestamp', '?')} .. {q47_done.get('timestamp', '?')}"
    )
    basis = (
        f"glyph-puzzle quest 47 ran {span} (finish _id={q47_done['_id']}); conv-102 "
        f"hint/wrong-answer nodes observed: {n102}; success node 88:11 observed: "
        f"{n8811}. A no-error completion should have produced the success dialogue — "
        f"its absence points to a changed dialogue flow."
        + (f" Confound: {debug_inside} DEBUGMenu event(s) inside the quest interval."
           if debug_inside else " No DEBUGMenu use inside the quest interval this run.")
    )
    root = [
        "SEMANTIC_DRIFT: success dialogue 88:11 did not fire although the puzzle was "
        "completed with no logged wrong attempts",
    ]
    if debug_inside:
        root.append(
            "INSUFFICIENT_PLAYTHROUGH_COVERAGE: debug-menu use inside the interval "
            "taints this playthrough as evidence; needs a clean replay"
        )
    return "green", basis, ("LOW" if debug_inside else "MEDIUM"), "MISMATCH_NEEDS_REVIEW", root


SPECIAL_CHECKS = {"U4P6": special_u4p6, "U4P2": special_u4p2, "U4P1": special_u4p1}


# ---------------------------------------------------------------------------
# Doc-derived activity window
# ---------------------------------------------------------------------------


def doc_window(coll, pid, doc_markers):
    """(start_id, end_id] derived from the source-doc start/end markers:
    end = last end-marker record; start = last start-marker record before it
    (OID_MIN when none). Returns None when no end marker was observed."""
    starts = doc_markers.get("start") or []
    ends = doc_markers.get("end") or []
    if not ends:
        return None
    end_docs = coll.find(
        {"game": GAME, "playerId": pid, "eventKey": {"$in": ends}}, sort={"_id": 1}
    )
    if not end_docs:
        return None
    end_id = end_docs[-1]["_id"]
    start_id = OID_MIN
    if starts:
        sdocs = coll.find(
            {"game": GAME, "playerId": pid, "eventKey": {"$in": starts},
             "_id": {"$lt": end_id}},
            sort={"_id": 1},
        )
        if sdocs:
            start_id = sdocs[-1]["_id"]
    return start_id, end_id


def run_with_doc_window(module, grade_fn, coll, pid, win):
    """Re-run a latest_trigger_window-based grader with the window pinned to
    the doc-derived interval. Patches the module attribute, restores after."""
    fixed = lambda c, p, k: win  # noqa: E731
    patched = []
    for holder in (module,):
        if holder is not None and hasattr(holder, "latest_trigger_window"):
            patched.append((holder, holder.latest_trigger_window))
            holder.latest_trigger_window = fixed
    # overrides call mhs_harness.latest_trigger_window directly
    patched.append((mhs_harness, mhs_harness.latest_trigger_window))
    mhs_harness.latest_trigger_window = fixed
    try:
        return grade_fn(coll, pid)
    finally:
        for holder, orig in patched:
            holder.latest_trigger_window = orig


# ---------------------------------------------------------------------------


def main():
    lib.utf8_stdout()
    records, meta = lib.load_logs(cfg)
    # mirror harness semantics: docs as loaded (order irrelevant to queries)
    coll = AdaptedCollection(records, meta["player_field"])
    pid = meta["players"][0] if meta["players"] else None

    intent = lib.read_json(lib.out_path(cfg, "source-doc-intent.json"))
    support = {
        r["progress_point"]: r
        for r in lib.read_json(lib.out_path(cfg, "pp-log-support-audit.json"))["progress_points"]
    }

    adaptation = {
        "player_field_translation": f"playerId -> {meta['player_field']}",
        "reason": f"{cfg['build_label']} export records identify the player via "
                  f"'{meta['player_field']}'; production scripts filter on playerId. "
                  "Translation applied openly; whether the LIVE grading DB also "
                  "changed cannot be verified from this repository.",
        "player_id_used": pid,
    }

    results = []
    for unit, point in [(u, p) for u in range(1, 6) for p in range(1, 8)]:
        mod_name = f"test_u{unit}p{point}"
        try:
            module = importlib.import_module(mod_name)
        except ModuleNotFoundError:
            continue
        pp_id = f"U{unit}P{point}"
        override = OVERRIDES.get(pp_id)
        grade_fn = override["grade"] if override else module.grade
        executor = f"tests/{mod_name}.py" + (" + audit override (current markdown script)" if override else "")

        rec = {
            "progress_point": pp_id,
            "name": module.META.get("name"),
            "executor": executor,
            "transcription_note": override["note"] if override else None,
            "adaptations": adaptation["player_field_translation"],
        }

        # --- production run -------------------------------------------------
        coll.trace = []
        try:
            color = grade_fn(coll, pid)
            rec["executes"] = True
            rec["production_color"] = color
        except Exception as e:  # noqa: BLE001 — report, don't crash the audit
            rec["executes"] = False
            rec["production_color"] = None
            rec["error"] = f"{type(e).__name__}: {e}"
        rec["query_trace"] = [
            {"query": _fmt_query(t["query"]), "matches": t["matches"]}
            for t in coll.trace
        ]

        # window reconstruction: latest_trigger_window-style graders, plus
        # custom two-anchor graders (WINDOW_START_KEY/WINDOW_END_KEY or
        # START_KEY/END_KEY: latest start exclusive .. latest end inclusive)
        trigger_key = override["trigger_key"] if override else getattr(module, "TRIGGER_KEY", None)
        win = None
        win_desc = trigger_key
        if override and override.get("window_fn"):
            win = override["window_fn"](coll, pid)
            win_desc = override.get("window_desc", "override-defined window")
        elif trigger_key:
            win = mhs_harness.latest_trigger_window(coll, pid, trigger_key)
        else:
            for s_attr, e_attr in (("WINDOW_START_KEY", "WINDOW_END_KEY"), ("START_KEY", "END_KEY")):
                s_key, e_key = getattr(module, s_attr, None), getattr(module, e_attr, None)
                if s_key and e_key:
                    s_doc = coll.find_one(
                        {"game": GAME, "playerId": pid, "eventKey": s_key}, sort={"_id": -1})
                    e_doc = coll.find_one(
                        {"game": GAME, "playerId": pid, "eventKey": e_key}, sort={"_id": -1})
                    win_desc = f"latest {s_key} .. latest {e_key}"
                    if s_doc and e_doc and s_doc["_id"] < e_doc["_id"]:
                        win = (s_doc["_id"], e_doc["_id"])
                    break
        if win:
            in_win = coll.count_documents(
                {"game": GAME, "playerId": pid, "_id": {"$gt": win[0], "$lte": win[1]}}
            )
            rec["attempt_window"] = {
                "anchors": win_desc,
                "start_id": win[0],
                "end_id": win[1],
                "records_in_window": in_win,
            }
        else:
            rec["attempt_window"] = {"anchors": win_desc, "constructed": False}

        # --- diagnostics from the module (verbatim) -------------------------
        try:
            coll.trace = []
            diag = module.diagnose(coll, pid) if hasattr(module, "diagnose") and not override else {}
            rec["diagnostics"] = {k: str(v)[:400] for k, v in diag.items()}
        except Exception as e:  # noqa: BLE001
            rec["diagnostics"] = {"_diagnose_error": f"{type(e).__name__}: {e}"}

        # --- doc-window cross-check -----------------------------------------
        doc = (intent["progress_points"].get(pp_id) or {}).get("progress_points_doc") or {}
        markers = doc.get("markers") or {}
        rec["doc_window"] = None
        if pp_id in COMPLETION_ONLY:
            pass
        elif trigger_key and markers.get("end"):
            dwin = doc_window(coll, pid, markers)
            if dwin:
                try:
                    dcolor = run_with_doc_window(module, grade_fn, coll, pid, dwin)
                    in_dwin = coll.count_documents(
                        {"game": GAME, "playerId": pid, "_id": {"$gt": dwin[0], "$lte": dwin[1]}}
                    )
                    rec["doc_window"] = {
                        "start_id": dwin[0], "end_id": dwin[1],
                        "markers": markers, "records_in_window": in_dwin,
                        "color": dcolor,
                    }
                except Exception as e:  # noqa: BLE001
                    rec["doc_window"] = {"error": f"{type(e).__name__}: {e}", "markers": markers}
            else:
                rec["doc_window"] = {"constructed": False, "markers": markers,
                                     "note": "doc end marker never observed in this playthrough"}

        # --- expected color & test status ------------------------------------
        sup = support.get(pp_id, {})
        root_causes = []
        special = SPECIAL_CHECKS.get(pp_id)
        special_out = special(coll, pid, rec) if (special and rec["executes"]) else None
        if not rec["executes"]:
            status, expected, basis, conf = "ERROR", None, "grader raised", "LOW"
        elif special_out:
            expected, basis, conf, status, root_causes = special_out
        elif pp_id in COMPLETION_ONLY:
            reached = sup.get("activity_reached")
            expected = "green" if reached else "yellow"
            basis = ("completion-only rubric; end evidence " +
                     ("observed" if reached else "not observed") + " in logs")
            conf = "HIGH"
            status = "PASS" if rec["production_color"] == expected else "MISMATCH"
        elif rec.get("doc_window") and rec["doc_window"].get("color"):
            dcolor = rec["doc_window"]["color"]
            if dcolor == rec["production_color"]:
                expected, conf = dcolor, "MEDIUM"
                basis = ("production window and doc-derived activity window yield the same "
                         "color; rubric formula applied to observed behavior")
                status = "PASS"
            else:
                expected, conf = dcolor, "LOW"
                basis = ("doc-derived activity window disagrees with production window — "
                         "one of the two intervals excludes relevant evidence")
                status = "MISMATCH_NEEDS_REVIEW"
                root_causes = [
                    "GRADING_SEQUENCE_BUG candidate: production attempt window and the "
                    "doc-derived activity interval select different evidence"
                ]
        else:
            expected, conf = None, "LOW"
            basis = ("no independent expectation derivable (custom window or no doc "
                     "end-marker observed); production executed and traced only")
            status = "EXECUTED_NO_INDEPENDENT_CHECK"
        rec["expected_color"] = expected
        rec["expected_basis"] = basis
        rec["expected_confidence"] = conf
        rec["grading_test_status"] = status
        rec["root_causes"] = root_causes
        results.append(rec)

    out_json = lib.out_path(cfg, "grading-validation.json")
    lib.write_json(out_json, {"build": cfg["build_label"], "adaptation": adaptation,
                              "results": results})
    rows = [
        {
            "progress_point": r["progress_point"],
            "name": r["name"],
            "production_color": r["production_color"],
            "expected_color": r["expected_color"],
            "grading_test_status": r["grading_test_status"],
            "expected_confidence": r["expected_confidence"],
            "doc_window_color": (r.get("doc_window") or {}).get("color"),
            "records_in_window": (r.get("attempt_window") or {}).get("records_in_window"),
            "executor": r["executor"],
        }
        for r in results
    ]
    out_csv = lib.out_path(cfg, "grading-validation.csv")
    lib.write_csv(out_csv, rows, list(rows[0].keys()))

    print(f"Wrote {out_json}")
    print(f"Wrote {out_csv}")
    print(f"\n{'PP':<6} {'prod':<7} {'docwin':<7} {'expected':<9} status")
    for r in rows:
        print(f"{r['progress_point']:<6} {str(r['production_color']):<7} "
              f"{str(r['doc_window_color']):<7} {str(r['expected_color']):<9} "
              f"{r['grading_test_status']}")


if __name__ == "__main__":
    main()
