"""
Run every progress point's reason-code scripts against a fixture log and
validate the triggered codes, their message variables, and the rendered
instructor messages.

Usage (from reason-code-validation/):
    python run_all.py                        # default fixture from config/expectations.yaml
    python run_all.py --fixture 09-03-26-3   # a specific fixture from the manifest
    python run_all.py --all-codes            # also list codes that did NOT trigger
    python run_all.py --quiet                # table only (no messages)
    python run_all.py --log PATH.json        # ad-hoc: any dump; no expected codes,
                                             # structural checks still apply
    python run_all.py --no-report            # don't write outputs/<run-id>/

Per point the runner checks (see rc_common.evaluate_point):
    code-set             module transcribes exactly the markdown's ### codes
    placeholders:<CODE>  every {variable} in the Instructor Message is returned
    color-consistency    yellow cell <=> at least one code triggered (when a
                         window exists; no window => no code, not-reached state)
    expected-codes       triggered set == fixture expectation (fixture mode)
    expected-variables   returned variables == fixture expectation (fixture mode)

Exit code: 1 if any check fails.
"""

import argparse
import json
import os
import sys

from rc_common import (POINTS, SUITE_DIR, default_player_id, evaluate_point,
                       format_point, load_collection, load_modules, resolve_fixture)


def run_suite(coll, pid, expected_by_pp):
    results = []
    for unit, point in POINTS:
        rc, color_mod = load_modules(unit, point)
        assert (rc.META["unit"], rc.META["point"]) == (unit, point)
        expectation = (expected_by_pp or {}).get(f"U{unit}P{point}")
        results.append(evaluate_point(rc, color_mod, coll, pid, expectation))
    return results


def _codes_cell(codes, width):
    s = ", ".join(codes) if codes else "-"
    return (s[:width - 2] + "..") if len(s) > width else s


def print_table(results, compare):
    w_trig, w_exp = 34, 34
    head = f"{'POINT':<6} {'COLOR':<7} {'WIN':<4} {'TRIGGERED CODE(S)':<{w_trig}} "
    head += f"{'EXPECTED':<{w_exp}} " if compare else ""
    head += "RESULT"
    print(head)
    print("-" * len(head))
    for r in results:
        line = (f"{r['pp']:<6} {r['color']:<7} {('yes' if r['has_window'] else 'no'):<4} "
                f"{_codes_cell(r['triggered'], w_trig):<{w_trig}} ")
        if compare:
            line += f"{_codes_cell(r['expected_codes'] or [], w_exp):<{w_exp}} "
        line += "PASS" if r["passed"] else "**FAIL**"
        print(line)
    print("-" * len(head))


def write_report(out_dir, run_id, log_path, results, compare):
    os.makedirs(out_dir, exist_ok=True)
    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if not r["passed"]]

    with open(os.path.join(out_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(
            {
                "run": run_id,
                "log": log_path.replace("\\", "/"),
                "mode": "fixture" if compare else "ad-hoc (no expected codes)",
                "summary": {"points": len(results), "passed": passed, "failed": len(failed),
                            "triggered_codes": sum(len(r["triggered"]) for r in results)},
                "results": results,
            },
            f, indent=2, ensure_ascii=False,
        )

    lines = ["# Reason-code validation results — " + run_id, "",
             f"Log: `{os.path.basename(log_path)}`", ""]
    if compare:
        lines.append(f"**{passed} / {len(results)} points pass every check "
                     f"(expected codes + variables, pop-up/cell consistency, message placeholders).**")
    else:
        lines.append(f"Ad-hoc run — no expected codes for this log; **{passed} / {len(results)} "
                     f"points pass the structural checks** (pop-up/cell consistency, message placeholders).")
    lines.append("")
    header = "| Point | Activity | Color | Window | Triggered code(s) |"
    sep = "|---|---|---|---|---|"
    if compare:
        header += " Expected |"
        sep += "---|"
    header += " Result |"
    sep += "---|"
    lines += [header, sep]
    for r in results:
        row = (f"| {r['pp']} | {r['name']} | {r['color']} | {'yes' if r['has_window'] else 'no'} "
               f"| {', '.join(r['triggered']) or '-'} |")
        if compare:
            row += f" {', '.join(r['expected_codes'] or []) or '-'} |"
        row += f" {'PASS' if r['passed'] else '**FAIL**'} |"
        lines.append(row)

    if failed:
        lines += ["", "## Check failures", ""]
        for r in failed:
            lines.append(f"### {r['pp']} — {r['name']}")
            lines.append("")
            for chk in r["checks"]:
                if not chk["ok"]:
                    lines.append(f"- **{chk['name']}**: {chk['detail']}")
            lines.append("")

    lines += ["", "## Instructor messages (triggered codes)", ""]
    any_msg = False
    for r in results:
        trig = [(c, cr) for c, cr in r["codes"].items() if cr.get("triggered")]
        if not trig:
            continue
        any_msg = True
        lines.append(f"### {r['pp']} — {r['name']} ({r['color']})")
        lines.append("")
        for code, cr in trig:
            vars_str = ", ".join(f"`{k}={v!r}`" for k, v in cr["variables"].items()) or "-"
            lines.append(f"**{code}** — {vars_str}")
            lines.append("")
            lines.append(f"> {cr['message']}")
            lines.append("")
    if not any_msg:
        lines.append("_No reason code triggered on this log._")
        lines.append("")

    lines += ["## All code evaluations", "",
              "| Point | Code | Triggered | Variables |", "|---|---|---|---|"]
    for r in results:
        if not r["codes"]:
            lines.append(f"| {r['pp']} | _(no reason codes)_ | - | - |")
            continue
        for code, cr in r["codes"].items():
            if cr.get("error"):
                lines.append(f"| {r['pp']} | {code} | ERROR | {cr['error']} |")
                continue
            vars_str = ", ".join(f"{k}={v!r}" for k, v in cr["variables"].items()) or "-"
            lines.append(f"| {r['pp']} | {code} | {'yes' if cr['triggered'] else 'no'} | {vars_str} |")

    with open(os.path.join(out_dir, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def main():
    ap = argparse.ArgumentParser(
        description="Validate the reason-code scripts of all 26 progress points against a fixture log.")
    ap.add_argument("--fixture", help="fixture id from config/expectations.yaml "
                                      "(default: the manifest's default_fixture)")
    ap.add_argument("--log", help="ad-hoc log dump instead of a fixture (no expected codes)")
    ap.add_argument("--all-codes", action="store_true",
                    help="in the per-point detail, also list codes that did not trigger")
    ap.add_argument("--quiet", action="store_true", help="table only, no per-point detail")
    ap.add_argument("--no-report", action="store_true",
                    help="don't write outputs/<run-id>/results.{md,json}")
    args = ap.parse_args()

    if args.log and args.fixture:
        ap.error("--log and --fixture are mutually exclusive")

    if args.log:
        run_id = "adhoc-" + os.path.splitext(os.path.basename(args.log))[0]
        log_path, expected_by_pp, compare = args.log, None, False
    else:
        fixture_id, log_path, entry = resolve_fixture(args.fixture)
        run_id, expected_by_pp, compare = fixture_id, entry.get("expected") or {}, True
        missing = [f"U{u}P{p}" for u, p in POINTS if f"U{u}P{p}" not in expected_by_pp]
        if missing:
            raise SystemExit(
                f"Fixture '{fixture_id}' is missing expectations for: {', '.join(missing)}")

    if not os.path.isfile(log_path):
        raise SystemExit(f"Log file not found: {log_path}")
    coll = load_collection(log_path)
    pid = default_player_id(coll)
    adapted = coll.player_field_source != "playerId"
    print(f"Run: {run_id} | {len(coll.docs)} log records | player = {pid}"
          + (f" (adapted: queries use top-level {coll.player_field_source})" if adapted else ""))
    if not compare:
        print("Ad-hoc mode: no expected codes — structural checks only "
              "(pop-up/cell consistency, message placeholders).")
    print()

    results = run_suite(coll, pid, expected_by_pp)
    print_table(results, compare)

    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if not r["passed"]]
    n_trig = sum(len(r["triggered"]) for r in results)
    print(f"\nSummary: {passed}/{len(results)} points pass; {n_trig} reason code(s) triggered "
          f"across {sum(1 for r in results if r['triggered'])} point(s).")

    if not args.quiet:
        print("\n" + "=" * 78)
        print("REASON CODES AND INSTRUCTOR MESSAGES")
        print("=" * 78)
        for r in results:
            if r["triggered"] or not r["passed"] or args.all_codes:
                print(format_point(r, show_all_codes=args.all_codes))
                print()

    if failed:
        print("=" * 78)
        print(f"{len(failed)} POINT(S) FAILED:")
        for r in failed:
            for chk in r["checks"]:
                if not chk["ok"]:
                    print(f"  - {r['pp']} {chk['name']}: {chk['detail']}")
        print("Review the reason-code script (grading-logic markdown), its transcription "
              "(rc_uXpY.py), or the fixture expectation.")

    if not args.no_report:
        out_dir = os.path.join(SUITE_DIR, "outputs", run_id)
        write_report(out_dir, run_id, log_path, results, compare)
        print(f"\nReport written to {os.path.relpath(out_dir, SUITE_DIR)}"
              f"{os.sep}results.md (+ results.json)")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
