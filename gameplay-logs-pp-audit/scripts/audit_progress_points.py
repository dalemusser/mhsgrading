"""Phases 4-6 — per-progress-point log-support audit.

Merges the dependency spec (Phase 1), the current-log inventory (Phase 2) and
the dialogue reconciliation (Phase 3) into a dependency-by-dependency support
audit, detects semantic-drift signals, and assigns each progress point an
overall log-support status.

Outputs: outputs/pp-log-support-audit.json / .csv
"""

import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

DEP_STATUSES = [
    "SUPPORTED_EXACTLY",
    "SUPPORTED_WITH_SCHEMA_CHANGE",
    "SUPPORTED_WITH_IDENTIFIER_CHANGE",
    "PARTIALLY_SUPPORTED",
    "NOT_OBSERVED_IN_PLAYTHROUGH",
    "LIKELY_MISSING_FROM_CURRENT_LOGGING",
    "AMBIGUOUS",
    "NOT_REQUIRED",
]

PP_STATUSES = [
    "READY_FOR_GRADING_TEST",
    "READY_WITH_MAPPING_UPDATE",
    "PARTIALLY_AUDITABLE",
    "BLOCKED_BY_LOGGING",
    "BLOCKED_BY_RUBRIC_AMBIGUITY",
    "BLOCKED_BY_GAME_DESIGN_CHANGE",
    "NEEDS_MANUAL_REVIEW",
]


def key_obs(inv, key):
    return inv["event_keys"].get(key)


def eval_event_key_dep(key, expectation, role, inv, recon_by_key, reach, conv_observed):
    """Evaluate one eventKey dependency; returns a dependency record."""
    obs = key_obs(inv, key)
    count = obs["count"] if obs else 0
    kind, a, b = lib.parse_event_key(key)
    recon = recon_by_key.get(key)
    notes = []
    examples = obs["examples"][:2] if obs else []

    if count > 0:
        status = "SUPPORTED_EXACTLY"
        if recon and recon["status"] == "ID_EXISTS_DIFFERENT_TEXT":
            status = "PARTIALLY_SUPPORTED"
            notes.append("dialogue text drifted for this ID (see reconciliation)")
        if obs and count > 1 and expectation == "required_anchor":
            notes.append(f"anchor fired {count}x (replay/loop) — window uses latest occurrence")
    else:
        if recon and recon["status"] == "DIALOGUE_REMOVED_OR_CHANGED":
            status = "LIKELY_MISSING_FROM_CURRENT_LOGGING"
            notes.append("dead reference: node absent from both dialogue sources — cannot fire")
            if recon.get("relocation_candidates"):
                status = "SUPPORTED_WITH_IDENTIFIER_CHANGE"
                notes.append(f"text relocated to {recon['relocation_candidates']} (candidate remap)")
        elif expectation == "counted_evidence":
            status = "NOT_OBSERVED_IN_PLAYTHROUGH"
            notes.append("counted evidence; zero occurrences is a valid grading input")
        elif kind == "dialogue":
            if conv_observed.get(a):
                status = "NOT_OBSERVED_IN_PLAYTHROUGH"
                notes.append(
                    f"conversation {a} fired {conv_observed[a]} other node(s); this node "
                    "did not trigger on this play path"
                )
            elif reach["activity_reached"]:
                status = "LIKELY_MISSING_FROM_CURRENT_LOGGING"
                notes.append(
                    f"activity reached but conversation {a} emitted no events at all"
                )
            else:
                status = "NOT_OBSERVED_IN_PLAYTHROUGH"
        elif kind == "quest":
            if reach["activity_reached"]:
                status = "LIKELY_MISSING_FROM_CURRENT_LOGGING"
                notes.append("activity reached but quest key never fired")
            else:
                status = "NOT_OBSERVED_IN_PLAYTHROUGH"
        else:
            status = "AMBIGUOUS"

    return {
        "dependency": key,
        "dep_type": "eventKey",
        "kind": kind,
        "role": role,
        "expectation": expectation,
        "status": status,
        "observed_count": count,
        "first_ts": obs["first_ts"] if obs else None,
        "last_ts": obs["last_ts"] if obs else None,
        "examples": examples,
        "reconciliation": recon["status"] if recon else ("NOT_APPLICABLE" if kind != "dialogue" else None),
        "notes": notes,
    }


def eval_event_type_dep(etype, filters, fields, inv, reach):
    et = inv["event_types"].get(etype)
    notes = []
    if not et:
        # case-variant check
        variants = [t for t in inv["event_types"] if t.lower() == etype.lower()]
        if variants:
            return {
                "dependency": etype,
                "dep_type": "eventType",
                "status": "SUPPORTED_WITH_IDENTIFIER_CHANGE",
                "observed_count": inv["event_types"][variants[0]]["count"],
                "notes": [f"eventType present under different casing: {variants}"],
                "filters": filters,
            }
        status = ("LIKELY_MISSING_FROM_CURRENT_LOGGING" if reach["activity_reached"]
                  else "NOT_OBSERVED_IN_PLAYTHROUGH")
        return {
            "dependency": etype,
            "dep_type": "eventType",
            "status": status,
            "observed_count": 0,
            "notes": ["eventType absent from this playthrough's logs"],
            "filters": filters,
        }

    # field / value checks against observed payloads
    all_fields = set()
    for variant in et["schema_variants"]:
        all_fields.update(f for f in variant.split(" | ") if f and not f.startswith("<"))
    field_status = []
    worst = "SUPPORTED_EXACTLY"
    for f in fields:
        if f in all_fields:
            continue
        case_alt = [g for g in all_fields if g.lower() == f.lower()]
        if case_alt:
            field_status.append(f"field '{f}' exists as {case_alt} (case/spelling variant)")
            worst = "SUPPORTED_WITH_SCHEMA_CHANGE"
        else:
            field_status.append(f"field '{f}' not present in any observed {etype} record")
            worst = "PARTIALLY_SUPPORTED"
    value_drift = []
    fv = et.get("field_values", {})
    for flt in filters:
        f, v = flt["field"], flt["value"]
        seen = fv.get(f)
        if seen is None or "<distinct_values>" in seen:
            continue
        seen_vals = {s.strip('"') for s in seen}
        if v not in seen_vals:
            value_drift.append(f"filter {f}={v!r} never observed (observed: {sorted(seen_vals)})")
    if field_status:
        notes.extend(field_status)
    if value_drift:
        notes.extend(value_drift)
        if worst == "SUPPORTED_EXACTLY":
            worst = "PARTIALLY_SUPPORTED"
    return {
        "dependency": etype,
        "dep_type": "eventType",
        "status": worst,
        "observed_count": et["count"],
        "first_ts": et["first_ts"],
        "last_ts": et["last_ts"],
        "scenes": et["scenes"],
        "filters": filters,
        "notes": notes,
        "sample": {k: et["sample"][k] for k in ("_id", "timestamp", "sceneName")} if et.get("sample") else None,
    }


def compute_reachability(pp, doc, inv, coverage_units):
    """Was this progress point's activity actually reached in the playthrough?"""
    basis = []
    reached = False
    end_keys = []
    if pp.get("attempt_window"):
        ek = (pp["attempt_window"].get("end") or {}).get("key")
        if ek:
            end_keys.append(("production window end", ek))
    if pp.get("trigger_end"):
        end_keys.append(("Trigger(End) header", pp["trigger_end"]))
    if doc:
        for mk in (doc.get("markers") or {}).get("end", []):
            end_keys.append(("doc end marker", mk))
    for label, k in end_keys:
        obs = key_obs(inv, k)
        if obs:
            reached = True
            basis.append(f"{label} `{k}` observed x{obs['count']} "
                         f"(first {obs['first_ts']}, e.g. _id={obs['examples'][0]['_id']})")
    if not reached:
        unit = f"Unit{pp['unit']}"
        cov = coverage_units.get(unit)
        eou = inv["event_types"].get("EndOfUnit", {}).get("field_values", {}).get("Unit", {})
        eou_units = {u.strip('"') for u in eou}
        if cov == "complete" and (str(pp["unit"]) in eou_units or f"Unit {pp['unit']}" in eou_units
                                  or any(str(pp["unit"]) in u for u in eou_units)):
            reached = True
            basis.append(
                f"no end anchor observed, but coverage manifest marks {unit} complete and an "
                f"EndOfUnit event exists for it — activity interval was traversed"
            )
    return {"activity_reached": reached, "basis": basis}


def doc_alignment(pp, doc, inv, ea_rows=()):
    """Compare doc start/end markers and dialogue tags with production anchors/keys."""
    if not doc:
        return {"available": False}
    out = {"available": True, "flags": []}
    win = pp.get("attempt_window") or {}
    prod_start = (win.get("start") or {}).get("key") or pp.get("trigger_start")
    prod_end = (win.get("end") or {}).get("key") or pp.get("trigger_end")
    doc_start = (doc.get("markers") or {}).get("start", [])
    doc_end = (doc.get("markers") or {}).get("end", [])
    out["doc_start"], out["doc_end"] = doc_start, doc_end
    out["prod_start"], out["prod_end"] = prod_start, prod_end
    if doc_start and prod_start and prod_start not in doc_start:
        out["flags"].append(
            f"start marker differs: docs say {doc_start}, production windows on `{prod_start}`"
        )
    if doc_end and prod_end and prod_end not in doc_end:
        out["flags"].append(
            f"end marker differs: docs say {doc_end}, production windows on `{prod_end}`"
        )
    # dialogue-tag set comparison per conversation (union of both source docs)
    doc_tags = {f"DialogueNodeEvent:{c}:{n}" for c, n in doc.get("color_rule_dialogue_tags") or []}
    for row in ea_rows:
        doc_tags |= {f"DialogueNodeEvent:{c}:{n}" for c, n in row.get("log_tag_dialogue_tags") or []}
    prod_keys = {k for k in pp["production"]["event_keys"] if k.startswith("DialogueNodeEvent")}
    if doc_tags:
        doc_convs = {k.split(":")[1] for k in doc_tags}
        prod_same_conv = {k for k in prod_keys if k.split(":")[1] in doc_convs}
        only_doc = sorted(doc_tags - prod_keys)
        only_prod = sorted(prod_same_conv - doc_tags)
        if only_doc or only_prod:
            out["flags"].append(
                f"rubric dialogue tags vs production keys differ — only in docs: {only_doc[:8]}"
                f"{'...' if len(only_doc) > 8 else ''}; only in production (same convs): {only_prod[:8]}"
                f"{'...' if len(only_prod) > 8 else ''}"
            )
        out["doc_only_tags"] = only_doc
        out["prod_only_keys"] = only_prod
    return out


def semantic_flags(pp, deps, inv, align):
    flags = []
    pp_keys = {d["dependency"] for d in deps if d["dep_type"] == "eventKey"}
    pp_types = {d["dependency"] for d in deps if d["dep_type"] == "eventType"}
    for dup in inv["anomalies"]["exact_duplicate_records"]:
        if dup["eventKey"] in pp_keys or dup["eventType"] in pp_types:
            flags.append(
                {
                    "type": "LOGGING_DUPLICATE_EVENT",
                    "detail": f"exact duplicate x{dup['copies']} of "
                              f"{dup['eventKey'] or dup['eventType']} at {dup['timestamp']}",
                    "impact": "can inflate counted evidence / attempt counts",
                }
            )
    for mm in inv["anomalies"]["dialogue_eventKey_vs_data_mismatches"]:
        if mm["eventKey"] in pp_keys:
            flags.append(
                {
                    "type": "KEY_DATA_MISMATCH",
                    "detail": f"{mm['eventKey']} record {mm['_id']} carries "
                              f"data.conversationId={mm['data.conversationId']}, "
                              f"data.nodeId={mm['data.nodeId']}",
                    "impact": "eventKey and payload disagree about which dialogue fired",
                }
            )
    for f in align.get("flags", []):
        flags.append(
            {
                "type": "DOC_PROD_REFERENCE_MISMATCH",
                "detail": f,
                "impact": "production may window/count different events than the rubric intends",
            }
        )
    for d in deps:
        for n in d.get("notes", []):
            if "never observed (observed:" in n:
                flags.append(
                    {
                        "type": "VALUE_DRIFT_CANDIDATE",
                        "detail": f"{d['dependency']}: {n}",
                        "impact": "filter may select nothing / wrong records",
                    }
                )
    return flags


def overall_status(deps, reach, flags):
    anchors = [d for d in deps if d.get("expectation") == "required_anchor"]
    anchors_ok = all(d["status"].startswith("SUPPORTED") for d in anchors) and anchors
    rationale = []
    core = [d for d in deps if d.get("expectation") in ("required_evidence", "activity_evidence")
            or d["dep_type"] == "eventType"]
    counted = [d for d in deps if d.get("expectation") == "counted_evidence"]

    if not anchors_ok:
        bad = [d for d in anchors if not d["status"].startswith("SUPPORTED")]
        names = [d["dependency"] for d in bad]
        if reach["activity_reached"] and any(
            d["status"] == "LIKELY_MISSING_FROM_CURRENT_LOGGING" for d in bad
        ):
            rationale.append(f"window anchor(s) {names} never fired although the activity was reached")
            return "BLOCKED_BY_LOGGING", rationale
        rationale.append(f"window anchor(s) {names} not observed; activity reach uncertain")
        return "PARTIALLY_AUDITABLE", rationale

    missing_core = [d for d in core if d["status"] == "LIKELY_MISSING_FROM_CURRENT_LOGGING"]
    if missing_core:
        rationale.append(
            f"required evidence missing though activity reached: "
            f"{[d['dependency'] for d in missing_core]}"
        )
        return "BLOCKED_BY_LOGGING", rationale

    remap = [d for d in deps if d["status"] in
             ("SUPPORTED_WITH_IDENTIFIER_CHANGE", "SUPPORTED_WITH_SCHEMA_CHANGE")]
    if remap:
        rationale.append(
            f"identifier/schema changes need a mapping update: "
            f"{[d['dependency'] for d in remap]}"
        )
        return "READY_WITH_MAPPING_UPDATE", rationale

    dead_counted = [d for d in counted if d["status"] == "LIKELY_MISSING_FROM_CURRENT_LOGGING"]
    if dead_counted:
        rationale.append(
            f"grading can run, but {len(dead_counted)} counted-evidence key(s) are dead "
            f"references that can never fire: {[d['dependency'] for d in dead_counted][:6]}"
        )
        return "PARTIALLY_AUDITABLE", rationale

    hard_flags = [f for f in flags if f["type"] in ("DOC_PROD_REFERENCE_MISMATCH",)]
    rationale.append("all window anchors and required evidence observed in current logs")
    if hard_flags:
        rationale.append(
            f"{len(hard_flags)} doc-vs-production reference mismatch(es) noted — grading is "
            "testable but its alignment with rubric intent needs review"
        )
    return "READY_FOR_GRADING_TEST", rationale


def confidence_for(status, deps, flags):
    if status == "READY_FOR_GRADING_TEST" and not flags:
        return "HIGH"
    if status in ("READY_FOR_GRADING_TEST", "READY_WITH_MAPPING_UPDATE"):
        return "MEDIUM"
    if status == "BLOCKED_BY_LOGGING":
        # blocked conclusions rest on one playthrough + a 2.5-month-old DB export
        return "MEDIUM"
    return "LOW"


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    import yaml

    deps_doc = lib.read_json(lib.out_path(cfg, "progress-point-dependencies.json"))
    intent = lib.read_json(lib.out_path(cfg, "source-doc-intent.json"))
    inv = lib.read_json(lib.out_path(cfg, "current-log-inventory.json"))
    recon = lib.read_json(lib.out_path(cfg, "dialogue-reconciliation.json"))
    recon_by_key = {r["event_key"]: r for r in recon["rows"]}

    coverage_units = {}
    cov_path = cfg.get("coverage_yaml")
    if cov_path and os.path.exists(lib.repo_path(cov_path)):
        with open(lib.repo_path(cov_path), encoding="utf-8") as f:
            coverage_units = (yaml.safe_load(f) or {}).get("tested_content", {})

    conv_observed = {int(c): sum(nodes.values())
                     for c, nodes in inv["dialogue_conversations_observed"].items()}

    results = []
    for pp in deps_doc["progress_points"]:
        pp_id = pp["pp_id"]
        doc = (intent["progress_points"].get(pp_id) or {}).get("progress_points_doc")
        ea_rows = (intent["progress_points"].get(pp_id) or {}).get("ea_working_doc") or []

        reach = compute_reachability(pp, doc, inv, coverage_units)
        align = doc_alignment(pp, doc, inv, ea_rows)

        # --- assemble dependency list ---
        role_by_key = {}
        expect_by_key = {}
        for ek in pp["event_keys"]:
            if ek["kind"] != "other":
                role_by_key.setdefault(ek["key"], ek["role"])
                expect_by_key.setdefault(ek["key"], ek["expectation"])
        anchor_keys = []
        win = pp.get("attempt_window") or {}
        for part in ("start", "end"):
            k = (win.get(part) or {}).get("key")
            if k:
                anchor_keys.append(k)
        if not anchor_keys:
            # completion-only / lifetime points anchor on the header triggers
            for k in (pp.get("trigger_start"), pp.get("trigger_end")):
                if k:
                    anchor_keys.append(k)
        for k in anchor_keys:
            expect_by_key[k] = "required_anchor"
            role_by_key.setdefault(k, "window anchor")

        all_keys = sorted(set(pp["production"]["event_keys"]) | set(anchor_keys))
        deps = []
        for k in all_keys:
            expectation = expect_by_key.get(k, "counted_evidence")
            deps.append(
                eval_event_key_dep(k, expectation, role_by_key.get(k, "production key"),
                                   inv, recon_by_key, reach, conv_observed)
            )
        for et in pp["production"]["event_types"]:
            flt = [f for f in pp["production"]["data_filters"]]
            d = eval_event_type_dep(et, flt, pp["production"]["data_fields"], inv, reach)
            d["expectation"] = "activity_evidence"
            deps.append(d)

        flags = semantic_flags(pp, deps, inv, align)
        status, rationale = overall_status(deps, reach, flags)
        conf = confidence_for(status, deps, flags)

        intent_text = None
        if doc:
            intent_text = doc.get("description")
        if ea_rows:
            act = ea_rows[0].get("student_action_scoring") or ""
            intent_text = (intent_text or "") + (" || EA scoring: " + re.sub(r"\s+", " ", act)[:300] if act else "")

        results.append(
            {
                "progress_point": pp_id,
                "progress_point_name": (doc or {}).get("name") or pp.get("activity"),
                "unit": pp["unit"],
                "grading_file": pp["grading_file"],
                "assessment_intent": intent_text,
                "activity_reached": reach["activity_reached"],
                "reachability_basis": reach["basis"],
                "doc_alignment": align,
                "dependencies": deps,
                "semantic_flags": flags,
                "log_support_status": status,
                "status_rationale": rationale,
                "confidence": conf,
            }
        )

    out_json = lib.out_path(cfg, "pp-log-support-audit.json")
    lib.write_json(out_json, {"build": cfg["build_label"], "progress_points": results})

    rows = []
    for r in results:
        dep_counts = defaultdict(int)
        for d in r["dependencies"]:
            dep_counts[d["status"]] += 1
        rows.append(
            {
                "progress_point": r["progress_point"],
                "name": r["progress_point_name"],
                "log_support_status": r["log_support_status"],
                "confidence": r["confidence"],
                "activity_reached": r["activity_reached"],
                "deps_total": len(r["dependencies"]),
                **{s: dep_counts.get(s, 0) for s in DEP_STATUSES},
                "semantic_flags": ";".join(sorted({f["type"] for f in r["semantic_flags"]})),
                "rationale": " | ".join(r["status_rationale"]),
            }
        )
    out_csv = lib.out_path(cfg, "pp-log-support-audit.csv")
    lib.write_csv(out_csv, rows, list(rows[0].keys()))

    print(f"Wrote {out_json}")
    print(f"Wrote {out_csv}")
    from collections import Counter

    counts = Counter(r["log_support_status"] for r in results)
    for s in PP_STATUSES:
        if counts.get(s):
            print(f"  {s:<28} {counts[s]}")
    print()
    for r in results:
        fl = ",".join(sorted({f['type'] for f in r['semantic_flags']})) or "-"
        print(f"  {r['progress_point']:<5} {r['log_support_status']:<26} conf={r['confidence']:<6} flags={fl}")


if __name__ == "__main__":
    main()
