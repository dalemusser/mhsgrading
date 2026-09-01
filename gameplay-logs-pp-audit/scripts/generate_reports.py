"""Phase 8/9 — human-readable reports.

Builds reports/audit-summary.md and one detailed report per progress point
under reports/progress-points/, entirely from the machine-readable outputs of
the earlier phases (no new analysis happens here).
"""

import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib


def short(s, n=110):
    if not s:
        return ""
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def recommended_action(sup, val):
    status = sup["log_support_status"]
    test = (val or {}).get("grading_test_status")
    if test == "MISMATCH_NEEDS_REVIEW":
        if sup["progress_point"] == "U4P2":
            return ("Dev team + replay: confirm whether the post-glyph success dialogue "
                    "(88:11) still fires in the current build; rerun a clean playthrough "
                    "without the debug menu. If the flow changed, remap the success marker.")
        return ("Manual review of the window/evidence mismatch (see this point's §10–11 "
                "for the traced divergence).")
    if status == "PARTIALLY_AUDITABLE":
        if any("not observed" in r for r in sup.get("status_rationale", [])):
            return ("Grading code + docs: a cited window anchor never fired on this play "
                    "path (see §9) — if the anchor is an optional/branch dialogue node, "
                    "re-anchor the window on a guaranteed-on-path event, then replay.")
        return ("Grading code: replace/confirm the dead dialogue references (they can never "
                "fire per the current dialogue DB); ask the dev team whether the dialogue "
                "was redesigned.")
    if test == "EXECUTED_NO_INDEPENDENT_CHECK":
        return ("More playtesting: production executed cleanly, but this playthrough gave "
                "no independent way to confirm the color; a targeted replay exercising "
                "failure paths would close the loop.")
    if test == "PASS":
        return "None — supported and validated on this playthrough; keep monitoring weekly."
    return "Manual investigation."


def pp_report(sup, spec, val, recon_rows, doc):
    pp = sup["progress_point"]
    lines = []
    a = lines.append
    a(f"# {pp} — {sup['progress_point_name']}")
    a("")
    a(f"| | |\n|---|---|")
    a(f"| Unit | {sup['unit']} |")
    a(f"| Grading file | `{sup['grading_file']}` |")
    a(f"| Log support status | **{sup['log_support_status']}** (confidence {sup['confidence']}) |")
    if val:
        a(f"| Grading test | **{val['grading_test_status']}** — production `{val['production_color']}`"
          + (f", expected `{val['expected_color']}`" if val.get("expected_color") else "") + " |")
    a("")

    a("## 1–2. Assessment intent")
    a("")
    if doc:
        a(f"**{doc.get('name', '')}** — {doc.get('description', '(no description)')}")
        if doc.get("color_determination"):
            a("")
            a(f"*Color determination (Progress-Points.docx):* {short(doc['color_determination'], 400)}")
    if sup.get("assessment_intent") and "EA scoring" in (sup["assessment_intent"] or ""):
        a("")
        a(f"*{short(sup['assessment_intent'].split('|| EA scoring:')[-1], 400)}*")
    a("")

    a("## 3. Current production logic")
    a("")
    a(f"{spec.get('grading_rule_prose') or '(see grading file)'}")
    a("")
    win = spec.get("attempt_window")
    if win:
        a(f"- Attempt window: {win['start'].get('raw', '?')} → {win['end'].get('raw', '?')}")
    for row in spec.get("outcome_table", []):
        a(f"- **{row['outcome']}**: {row['condition']}")
    a("")

    a("## 4–6. Required log evidence and dependency audit")
    a("")
    a("| Dependency | Role/Class | Status | Observed | Notes |")
    a("|---|---|---|---|---|")
    for d in sup["dependencies"]:
        role = d.get("role") or d.get("dep_type")
        cls = d.get("expectation", "")
        obs = d.get("observed_count", 0)
        ex = d.get("examples") or []
        obs_s = f"x{obs}"
        if ex:
            obs_s += f" (first `{ex[0]['_id']}` @ {short(ex[0].get('timestamp'), 30)})"
        elif d.get("sample"):
            obs_s += f" (e.g. `{d['sample']['_id']}`)"
        a(f"| `{short(d['dependency'], 45)}` | {role}/{cls} | {d['status']} | {obs_s} | "
          f"{short('; '.join(d.get('notes', [])), 160)} |")
    a("")
    if sup.get("reachability_basis"):
        a(f"**Activity reached:** {sup['activity_reached']} — " +
          "; ".join(short(b, 160) for b in sup["reachability_basis"]))
        a("")

    my_recon = [r for r in recon_rows if pp in r["referenced_by"].split(";")]
    non_exact = [r for r in my_recon if r["status"] != "EXACT_MATCH"]
    a("## 7. Dialogue reconciliation")
    a("")
    if not my_recon:
        a("No dialogue-based references.")
    elif not non_exact:
        a(f"All {len(my_recon)} dialogue references resolve exactly in the current "
          "dialogue DB and fired in this playthrough.")
    else:
        exact_n = len(my_recon) - len(non_exact)
        a(f"{exact_n}/{len(my_recon)} references EXACT_MATCH. Non-exact:")
        a("")
        a("| Key | Status | Detail |")
        a("|---|---|---|")
        for r in non_exact:
            a(f"| `{r['event_key']}` | {r['status']} | {short(r['note'], 140)} |")
    a("")

    a("## 8. Semantic drift / cross-reference flags")
    a("")
    if sup["semantic_flags"]:
        for f in sup["semantic_flags"]:
            a(f"- **{f['type']}** — {short(f['detail'], 300)}")
            a(f"  - impact: {f['impact']}")
    else:
        a("None detected for this point.")
    a("")

    a("## 9. Overall log support status")
    a("")
    a(f"**{sup['log_support_status']}** (confidence {sup['confidence']})")
    for r in sup["status_rationale"]:
        a(f"- {r}")
    a("")

    a("## 10. Grading validation (Stage 2)")
    a("")
    if not val:
        a("Not executed.")
    else:
        a(f"- Executor: {val['executor']}")
        if val.get("transcription_note"):
            a(f"- Transcription note: {val['transcription_note']}")
        a(f"- Adaptation: {val['adaptations']}")
        aw = val.get("attempt_window") or {}
        if aw.get("start_id"):
            a(f"- Attempt window ({aw.get('anchors')}): `({aw['start_id']}, {aw['end_id']}]`, "
              f"{aw.get('records_in_window')} records inside")
        else:
            a(f"- Attempt window: not reconstructed ({aw.get('anchors')})")
        a(f"- **Production color: `{val['production_color']}`**")
        dw = val.get("doc_window")
        if dw and dw.get("color"):
            a(f"- Doc-derived activity window `({dw['start_id']}, {dw['end_id']}]` "
              f"({dw['records_in_window']} records) → color `{dw['color']}`")
        if val.get("expected_color"):
            a(f"- Expected color: `{val['expected_color']}` (confidence "
              f"{val['expected_confidence']}) — {short(val['expected_basis'], 500)}")
        else:
            a(f"- Expected color: not independently derivable — {short(val['expected_basis'], 300)}")
        if val.get("diagnostics"):
            a("- Diagnostics (from the 1:1 transcription):")
            for k, v in val["diagnostics"].items():
                a(f"  - `{k}`: {short(v, 300)}")
        trace = val.get("query_trace") or []
        if trace:
            a(f"- Query trace ({len(trace)} queries):")
            for t in trace[:10]:
                a(f"  - {t['query']} → {t['matches']} match(es)")
            if len(trace) > 10:
                a(f"  - … {len(trace) - 10} more (see grading-validation.json)")
    a("")

    a("## 11. Root cause")
    a("")
    roots = (val or {}).get("root_causes") or []
    if roots:
        for r in roots:
            a(f"- {r}")
    elif sup["log_support_status"] == "PARTIALLY_AUDITABLE":
        a("- OUTDATED_RUBRIC_TECHNICAL_REFERENCE / DIALOGUE_ID_CHANGED: dead dialogue "
          "references (see §7) can never fire, so part of the rubric signal is unreachable.")
    else:
        a("No failure to attribute on this playthrough.")
    a("")

    a("## 12. Recommended action")
    a("")
    a(recommended_action(sup, val))
    a("")
    return "\n".join(lines)


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    deps = {p["pp_id"]: p for p in
            lib.read_json(lib.out_path(cfg, "progress-point-dependencies.json"))["progress_points"]}
    intent = lib.read_json(lib.out_path(cfg, "source-doc-intent.json"))["progress_points"]
    support = lib.read_json(lib.out_path(cfg, "pp-log-support-audit.json"))["progress_points"]
    val_doc = lib.read_json(lib.out_path(cfg, "grading-validation.json"))
    vals = {v["progress_point"]: v for v in val_doc["results"]}
    recon_rows = lib.read_json(lib.out_path(cfg, "dialogue-reconciliation.json"))["rows"]
    inv = lib.read_json(lib.out_path(cfg, "current-log-inventory.json"))

    # ---- per-PP reports -----------------------------------------------------
    for sup in support:
        pp = sup["progress_point"]
        doc = (intent.get(pp) or {}).get("progress_points_doc")
        text = pp_report(sup, deps[pp], vals.get(pp), recon_rows, doc)
        path = lib.report_path(cfg, "progress-points", f"{pp.lower()}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    # ---- summary ------------------------------------------------------------
    s_counts = Counter(r["log_support_status"] for r in support)
    t_counts = Counter(v["grading_test_status"] for v in vals.values())
    dead = [r for r in recon_rows if r["status"] == "DIALOGUE_REMOVED_OR_CHANGED"]
    mismatch = [v for v in vals.values() if v["grading_test_status"] == "MISMATCH_NEEDS_REVIEW"]
    window_flags = [(r["progress_point"],
                     [f["detail"] for f in r["semantic_flags"]
                      if "marker differs" in f.get("detail", "")])
                    for r in support]
    window_flags = [(p, fl) for p, fl in window_flags if fl]

    L = []
    a = L.append
    a(f"# Gameplay-Log → Progress-Point Grading Audit — build {cfg['build_label']}")
    a("")
    meta = val_doc["adaptation"]
    a(f"- Logs: `{cfg['log_dir']}` — single full playthrough, all 5 units complete "
      f"(player `{meta['player_id_used']}`).")
    a("- Stage 1 = can the current logs still feed each grading rule; "
      "Stage 2 = does the production logic then produce a defensible color.")
    a("- Detailed evidence: `outputs/*.json|csv`; per-point reports: `reports/progress-points/`.")
    a("")
    a("## Headline numbers")
    a("")
    a(f"| Stage | Result |")
    a(f"|---|---|")
    a(f"| Progress points examined | {len(support)} |")
    for k, v in s_counts.most_common():
        a(f"| Stage 1 — {k} | {v} |")
    for k, v in t_counts.most_common():
        a(f"| Stage 2 — {k} | {v} |")
    a("")

    a("## Cross-cutting findings (affect many/all points)")
    a("")
    detected_field = (inv["meta"].get("player_field") or "user_id")
    n = 1
    if detected_field != "playerId":
        a(f"{n}. **Top-level player field: `{detected_field}` (production scripts filter on "
          f"`playerId`).** The 05-01-26 export carried `playerId`; every export since 08-13 "
          f"carries only `{detected_field}`. Unadapted production scripts would match nothing "
          f"against this export. Stage 2 ran with a declared translation "
          f"({meta['player_field_translation']}). Whether the live grading DB changed too "
          f"cannot be verified from this repo — **confirm with the dev team**; if it did, "
          f"all 26 scripts need the field rename.")
        n += 1
    if dead:
        a(f"{n}. **{len(dead)} dead dialogue reference(s)** (absent from both dialogue "
          f"sources, so they can never fire): " +
          "; ".join(f"`{r['event_key']}` ({r['referenced_by']})" for r in dead) + ".")
    else:
        a(f"{n}. **No dead dialogue references** among grading keys — every referenced "
          "dialogue node exists in at least one dialogue source.")
    n += 1
    stale_tests = sorted(
        (v["progress_point"], v.get("transcription_note") or "")
        for v in vals.values() if "override" in (v.get("executor") or "")
    )
    if stale_tests:
        a(f"{n}. **{len(stale_tests)} stale test transcription(s)**: the `tests/` modules for "
          + ", ".join(p for p, _ in stale_tests) +
          " still implement earlier production scripts; the audit executed audit-local "
          "overrides transcribing the CURRENT markdown (notes in grading-validation.json). "
          "The test modules should be re-synced with the markdown.")
        n += 1
    if window_flags:
        both = [(p, vals.get(p)) for p, _ in window_flags]
        computable = [(p, v) for p, v in both
                      if v and (v.get("doc_window") or {}).get("color")]
        disagree = [p for p, v in computable
                    if v["doc_window"]["color"] != v.get("production_color")]
        if disagree:
            agreement = ("Doc-derived windows DISAGREED with production colors for: "
                         + ", ".join(disagree) + " — active miscolor risk")
        elif computable:
            agreement = ("On this playthrough the doc-derived windows agreed with "
                         "production colors wherever both were computable, but the "
                         "divergent anchors remain fragile on replays")
        else:
            agreement = "No doc-derived window was computable this run to cross-check"
        a(f"{n}. **Doc-vs-production window anchors differ** for: " +
          ", ".join(p for p, _ in window_flags) +
          " — same bug class that produced the round-1 U2P6/U3P3 miscolors. " +
          agreement + ".")
        n += 1
    build_versions = ", ".join(inv["meta"].get("versions") or ["?"])
    a(f"{n}. **Dialogue DB export is 2026-06-10** vs game build {build_versions}: "
      "text-level conclusions carry that staleness caveat (MEDIUM confidence ceiling).")
    n += 1
    kv_mm = inv.get("anomalies", {}).get("dialogue_eventKey_vs_data_mismatches", [])
    if kv_mm:
        hit = sorted({s["progress_point"] for s in support
                      for f in s["semantic_flags"] if f["type"] == "KEY_DATA_MISMATCH"})
        a(f"{n}. **eventKey↔payload mismatches** exist in {len(kv_mm)} DialogueEvent "
          f"record(s) in this dump; " +
          (f"they hit grading keys of: {', '.join(hit)}." if hit
           else "none hit grading keys in this dump, but keyed grading is exposed to them."))
        n += 1
    # markdown-internal window divergence: block documents a start anchor the
    # script never queries (the script uses previous-occurrence-of-END instead)
    internal = []
    for pp_id, spec in deps.items():
        win = spec.get("attempt_window")
        if not win:
            continue
        script_keys = set(spec["production"]["event_keys"])
        for part in ("start", "end"):
            k = (win.get(part) or {}).get("key")
            if k and k not in script_keys:
                internal.append(f"{pp_id} (`{k}`)")
    if internal:
        a(f"{n}. **Documented window ≠ implemented window** inside {len(internal)} grading "
          f"files: the 'Attempt Window (Production)' block cites an anchor the production "
          f"script never queries — the script bounds the window with the previous "
          f"occurrence of its END trigger instead: " + ", ".join(internal) + ". This is "
          "the same anchor-divergence class that produced the round-1 U2P6/U3P3 "
          "miscolors; harmless on a first playthrough, fragile on replays.")
        n += 1
    a("")

    a("## Master table")
    a("")
    a("| PP | Rubric requirement | Required log evidence | Current evidence | "
      "Log support | Grading test | Root cause | Recommended action |")
    a("|---|---|---|---|---|---|---|---|")
    for sup in support:
        pp = sup["progress_point"]
        v = vals.get(pp) or {}
        spec = deps[pp]
        n_keys = len([d for d in sup["dependencies"] if d.get("dep_type") == "eventKey"])
        n_types = len([d for d in sup["dependencies"] if d.get("dep_type") == "eventType"])
        req = f"{n_keys} event keys" + (f" + {n_types} event type(s)" if n_types else "")
        n_obs = len([d for d in sup["dependencies"] if d.get("observed_count", 0) > 0])
        cur = f"{n_obs}/{n_keys + n_types} observed"
        root = short("; ".join(v.get("root_causes") or []), 80) or "—"
        a(f"| {pp} | {short(spec.get('grading_rule_prose'), 70)} | {req} | {cur} | "
          f"{sup['log_support_status']} | "
          f"{v.get('grading_test_status', '—')} ({v.get('production_color', '?')}"
          + (f"→exp {v['expected_color']}" if v.get("expected_color") and
             v.get("expected_color") != v.get("production_color") else "") + ") | "
          f"{root} | {short(recommended_action(sup, v), 90)} |")
    a("")

    # ---- data-driven lists reused by the answers and priorities ------------
    def pps_with_status(st):
        return sorted(r["progress_point"] for r in support if r["log_support_status"] == st)

    def vals_with_test(st):
        return sorted(v["progress_point"] for v in vals.values()
                      if v["grading_test_status"] == st)

    blocked = pps_with_status("BLOCKED_BY_LOGGING")
    mapping_updates = pps_with_status("READY_WITH_MAPPING_UPDATE")
    partial = pps_with_status("PARTIALLY_AUDITABLE")
    unexercised = vals_with_test("EXECUTED_NO_INDEPENDENT_CHECK")
    mismatched = vals_with_test("MISMATCH_NEEDS_REVIEW") + vals_with_test("MISMATCH")
    drift_pps = sorted({v["progress_point"] for v in vals.values()
                        if any("SEMANTIC_DRIFT" in rt for rt in (v.get("root_causes") or []))})
    grading_bug_pps = sorted({v["progress_point"] for v in vals.values()
                              if any("GRADING" in rt for rt in (v.get("root_causes") or []))})
    dead_by_pp = {}
    for r in dead:
        for p in r["referenced_by"].split(";"):
            dead_by_pp.setdefault(p, []).append(r["event_key"])

    def lst(xs):
        return ", ".join(xs) if xs else "none"

    a("## Answers to the standing audit questions")
    a("")
    ready = s_counts.get("READY_FOR_GRADING_TEST", 0)
    a(f"1. **Examined:** {len(support)} progress points (all).")
    a(f"2. **READY_FOR_GRADING_TEST:** {ready}.")
    a(f"3. **Needing identifier/schema mapping updates:** {lst(mapping_updates)}"
      + (" — plus the global `playerId` field question (finding 1) if the live DB changed."
         if detected_field != "playerId" else "."))
    a(f"4. **Blocked by missing logging:** {lst(blocked)}"
      + ("." if blocked else " — every window anchor and required evidence family fired "
         "in this playthrough."))
    a(f"5. **Not fully evaluable due to unexercised behavior:** {len(unexercised)} point(s) "
      f"executed but had no independent expectation ({lst(unexercised)}).")
    a(f"6. **Affected by game-design/dialogue-flow change (drift candidates):** "
      f"{lst(drift_pps)} (see per-point §11 root causes).")
    a(f"7. **Grading-logic problems:** {lst(sorted(set(grading_bug_pps)))}"
      + (f"; dead rubric keys remain in: "
         + "; ".join(f"{p} ({', '.join('`' + k + '`' for k in ks)})"
                     for p, ks in sorted(dead_by_pp.items()))
         if dead_by_pp else "; no dead rubric keys remain")
      + (f"; divergent window anchors: {lst([p for p, _ in window_flags])}."
         if window_flags else "."))
    a("8. **Problematic identifiers across multiple points:** see per-point §8 "
      "DOC_PROD_REFERENCE_MISMATCH flags (rubric dialogue tags vs production keys) and "
      "the reconciliation table for cross-conversation relocations.")
    a(f"9. **Prioritize for additional playtesting:** {lst(sorted(set(mismatched + unexercised)))} "
      f"— mismatches need targeted replays; unexercised failure paths need a "
      f"deliberately-imperfect run.")
    a("10. **Dev team vs dashboard:** dev team — player-field rename confirmation, "
      "dialogue-flow drift candidates (Q6), dialogue-DB export refresh; dashboard — "
      "grading-logic problems (Q7), dead-key cleanup, re-sync of stale `tests/` modules "
      "with the current markdown scripts.")
    a("")

    a("## Priorities")
    a("")
    a("### Priority A — logging blocks grading entirely")
    if blocked:
        for p in blocked:
            r = next(r for r in support if r["progress_point"] == p)
            a(f"- **{p}**: {short(' | '.join(r['status_rationale']), 160)}")
    else:
        a("- None on this build/playthrough."
          + (" (Watch the `playerId` field question: if the live collection changed, "
             "this becomes an A for all 26 points.)" if detected_field != "playerId" else ""))
    a("")
    a("### Priority B — evidence exists but grading mapping/code must change")
    prio_b = False
    for p in sorted(set(mismatched)):
        v = vals[p]
        a(f"- **{p}**: {short('; '.join(v.get('root_causes') or ['window/evidence mismatch']), 160)}")
        prio_b = True
    for p, ks in sorted(dead_by_pp.items()):
        a(f"- **{p}**: remove/replace dead dialogue key(s) {', '.join('`' + k + '`' for k in ks)} "
          "(cannot fire).")
        prio_b = True
    if stale_tests:
        a("- **tests/**: re-sync " +
          ", ".join(f"`test_{p.lower()}.py`" for p, _ in stale_tests) +
          " with the current markdown scripts.")
        prio_b = True
    if not prio_b:
        a("- None on this build/playthrough.")
    a("")
    a("### Priority C — additional targeted playthrough required")
    if drift_pps:
        for p in drift_pps:
            a(f"- **{p}**: targeted replay to confirm/refute the drift candidate "
              "(see its report §10).")
    if unexercised:
        a(f"- Yellow/failure paths for {lst(unexercised)} were never exercised; a "
          "deliberately-imperfect run would validate their counting logic.")
    if not drift_pps and not unexercised:
        a("- None on this build/playthrough.")
    a("")
    a("### Priority D — specification clarification required")
    if window_flags:
        a("- Doc-vs-production window anchors: confirm which interval definition is "
          "authoritative per point, then align docs or scripts "
          f"({lst([p for p, _ in window_flags])}).")
    if internal:
        a("- Markdown-internal divergence (documented window ≠ implemented window): "
          + ", ".join(internal) + ".")
    a("- Refresh `Dialogue-ID-Texts.xlsx` / dialogue export to the current build.")
    a("")

    path = lib.report_path(cfg, "audit-summary.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Wrote {path}")
    print(f"Wrote {len(support)} per-point reports under "
          f"{cfg.get('reports_dir', 'reports')}/progress-points/")


if __name__ == "__main__":
    main()
