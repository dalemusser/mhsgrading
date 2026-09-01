"""Automated consistency checks over the audit's own outputs.

Run last. Exits 1 on hard failures; prints WARN lines for soft issues
(these are audit findings in their own right, not pipeline bugs).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit_lib as lib

PP_STATUSES = {
    "READY_FOR_GRADING_TEST", "READY_WITH_MAPPING_UPDATE", "PARTIALLY_AUDITABLE",
    "BLOCKED_BY_LOGGING", "BLOCKED_BY_RUBRIC_AMBIGUITY",
    "BLOCKED_BY_GAME_DESIGN_CHANGE", "NEEDS_MANUAL_REVIEW",
}
DEP_STATUSES = {
    "SUPPORTED_EXACTLY", "SUPPORTED_WITH_SCHEMA_CHANGE",
    "SUPPORTED_WITH_IDENTIFIER_CHANGE", "PARTIALLY_SUPPORTED",
    "NOT_OBSERVED_IN_PLAYTHROUGH", "LIKELY_MISSING_FROM_CURRENT_LOGGING",
    "AMBIGUOUS", "NOT_REQUIRED",
}
RECON_STATUSES = {
    "EXACT_MATCH", "TEXT_MATCH_DIFFERENT_ID", "ID_EXISTS_DIFFERENT_TEXT",
    "EXPECTED_DIALOGUE_NOT_OBSERVED", "DIALOGUE_REMOVED_OR_CHANGED",
    "AMBIGUOUS", "NOT_APPLICABLE",
}
TEST_STATUSES = {
    "PASS", "MISMATCH", "MISMATCH_NEEDS_REVIEW",
    "EXECUTED_NO_INDEPENDENT_CHECK", "NOT_TESTABLE", "ERROR",
}


def main():
    lib.utf8_stdout()
    cfg = lib.load_config()
    fails, warns = [], []

    def check(cond, msg):
        if not cond:
            fails.append(msg)

    deps = lib.read_json(lib.out_path(cfg, "progress-point-dependencies.json"))["progress_points"]
    intent = lib.read_json(lib.out_path(cfg, "source-doc-intent.json"))["progress_points"]
    inv = lib.read_json(lib.out_path(cfg, "current-log-inventory.json"))
    recon = lib.read_json(lib.out_path(cfg, "dialogue-reconciliation.json"))["rows"]
    support = lib.read_json(lib.out_path(cfg, "pp-log-support-audit.json"))["progress_points"]
    vals = lib.read_json(lib.out_path(cfg, "grading-validation.json"))["results"]

    # structural expectations
    check(len(deps) == 26, f"expected 26 grading specs, got {len(deps)}")
    check(len(support) == 26, f"expected 26 support-audit records, got {len(support)}")
    check(len(vals) == 26, f"expected 26 validation records, got {len(vals)}")
    ids = {p["pp_id"] for p in deps}
    check(ids == {r["progress_point"] for r in support}, "spec/support PP id sets differ")
    check(ids == {r["progress_point"] for r in vals}, "spec/validation PP id sets differ")
    check(all(p["production"]["has_script"] for p in deps),
          "some grading files lack a Production Script fence")
    for p in deps:
        if not (intent.get(p["pp_id"]) or {}).get("progress_points_doc"):
            warns.append(f"{p['pp_id']}: no Progress-Points.docx row matched")

    # enum conformance
    for r in support:
        check(r["log_support_status"] in PP_STATUSES,
              f"{r['progress_point']}: bad status {r['log_support_status']}")
        for d in r["dependencies"]:
            check(d["status"] in DEP_STATUSES,
                  f"{r['progress_point']}: bad dep status {d['status']}")
    for r in recon:
        check(r["status"] in RECON_STATUSES, f"recon {r['event_key']}: bad status {r['status']}")
    for v in vals:
        check(v["grading_test_status"] in TEST_STATUSES,
              f"{v['progress_point']}: bad test status {v['grading_test_status']}")
        check(v["executes"], f"{v['progress_point']}: production logic failed to execute")
        if v["executes"]:
            check(v["production_color"] in ("green", "yellow"),
                  f"{v['progress_point']}: unexpected color {v['production_color']}")

    # log parseability / inventory sanity
    check(inv["meta"]["record_count"] > 0, "no log records loaded")
    check(not inv["meta"]["parse_errors"], f"log parse errors: {inv['meta']['parse_errors']}")
    check(len(inv["meta"]["players"]) == 1,
          f"expected single-player dump, players={inv['meta']['players']}")

    # every referenced dialogue key made it into the reconciliation
    recon_keys = {r["event_key"] for r in recon}
    for p in deps:
        for k in p["all_referenced_event_keys"]:
            if k.startswith("DialogueNodeEvent") and k not in recon_keys:
                fails.append(f"{p['pp_id']}: dialogue key {k} missing from reconciliation")

    # anchors occur in a usable order where both were observed
    for r in support:
        anchors = [d for d in r["dependencies"] if d.get("expectation") == "required_anchor"]
        obs = [d for d in anchors if d.get("observed_count", 0) > 0]
        if len(obs) >= 2:
            first = min(d["first_ts"] for d in obs if d.get("first_ts"))
            last = max(d["last_ts"] for d in obs if d.get("last_ts"))
            if first == last:
                warns.append(f"{r['progress_point']}: all anchors share one timestamp")

    # duplicated eventKeys among grading anchors (degenerate-window risk)
    for r in support:
        for d in r["dependencies"]:
            if d.get("expectation") == "required_anchor" and d.get("observed_count", 0) > 1:
                warns.append(
                    f"{r['progress_point']}: anchor {d['dependency']} fired "
                    f"{d['observed_count']}x — 'previous trigger' windows shrink on replays"
                )

    # internal markdown consistency: attempt-window block keys should appear in
    # the production script (U3P3-style divergence is a real audit finding)
    for p in deps:
        win = p.get("attempt_window")
        if not win:
            continue
        script_keys = set(p["production"]["event_keys"])
        for part in ("start", "end"):
            k = (win.get(part) or {}).get("key")
            if k and k not in script_keys:
                warns.append(
                    f"{p['pp_id']}: Attempt Window block cites `{k}` but the production "
                    f"script never queries it — markdown block and script disagree"
                )

    print(f"Checks complete: {len(fails)} failure(s), {len(warns)} warning(s)\n")
    for w in warns:
        print(f"  WARN {w}")
    for f in fails:
        print(f"  FAIL {f}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
