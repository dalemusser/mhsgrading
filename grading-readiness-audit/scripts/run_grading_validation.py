"""Phase 7 (Stage 2) — execute the current production grading logic against
the audited gameplay logs and trace what it computes.

Executor: the 1:1 Python transcriptions under rubric-validation/
(mhs_harness + the 26 test modules, config `tests_dir`), reused as-is EXCEPT
one ADAPTATION (recorded, never silent): exports since 08-13-26 identify the
player via top-level `user_id`, while every production script filters on
`playerId`. Queries are translated playerId -> <detected field>. Without
this the scripts match zero records and everything degrades to "yellow".

(Earlier audits carried audit-local overrides here for test modules that
transcribed outdated production scripts; the modules were re-synced with the
current grading markdown on 2026-09-02 and the overrides retired. If a module
goes stale again, prefer re-syncing it over reintroducing an override.)

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

import mhs_harness  # noqa: E402  (from rubric-validation/)
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
# Helpers for the special evidence-based checks below (U4P1/U4P2/U4P6):
# Unit-4 'Soil Key Puzzle' status records — the puzzle also fires in Units 2
# and 3, and data.Unit holds the build-flavored scene name, hence the
# prefix match applied in Python.

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


U4P2_NEGATIVE_KEYS = [f"DialogueNodeEvent:102:{n}" for n in (9, 10, 12, 18, 23)]


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
    # some graders reach latest_trigger_window via the mhs_harness module
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
        grade_fn = module.grade
        executor = f"{cfg['tests_dir']}/{mod_name}.py"

        rec = {
            "progress_point": pp_id,
            "name": module.META.get("name"),
            "executor": executor,
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

        # window reconstruction: latest_trigger_window-style graders, custom
        # windows exported by the module (attempt_window/WINDOW_DESC, e.g. the
        # U4P1/U4P2 soil-key anchors), and generic two-anchor graders
        # (WINDOW_START_KEY/WINDOW_END_KEY or START_KEY/END_KEY: latest start
        # exclusive .. latest end inclusive)
        trigger_key = getattr(module, "TRIGGER_KEY", None)
        win = None
        win_desc = trigger_key
        if hasattr(module, "attempt_window"):
            win = module.attempt_window(coll, pid)
            win_desc = getattr(module, "WINDOW_DESC", "module-defined window")
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
            diag = module.diagnose(coll, pid) if hasattr(module, "diagnose") else {}
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
