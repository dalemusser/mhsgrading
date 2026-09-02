"""
Run every per-point grading test against a fixture log and compare the
production color to the fixture's expected dashboard color.

Usage (from rubric-validation/):
    python run_all.py                     # default fixture from config/fixtures.yaml
    python run_all.py --fixture 08-31-26  # a specific fixture from the manifest
    python run_all.py --quiet             # table only (no per-reason diagnostics)
    python run_all.py --log PATH.json     # ad-hoc: grade an arbitrary dump
                                          # (no expected colors — informational)
    python run_all.py --no-report         # don't write outputs/<run-id>/

Fixture logs and their expected colors live in config/fixtures.yaml. For an
ad-hoc --log run there is no expectation to compare against — to establish
expected colors for a NEW build, run the grading-readiness-audit first and
review its grading-validation output, then add a fixture entry.

Results are also written to outputs/<fixture-id>/ (or outputs/adhoc-<name>/
for --log runs): results.md (human-readable) and results.json (structured).
Exit code: 1 if any point's production color differs from the expected color.
"""

import argparse
import importlib
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from mhs_harness import SUITE_DIR, load_collection, default_player_id, resolve_fixture
from mhs_report import evaluate, format_result

# Dashboard order: points per unit.
UNIT_POINTS = {1: 4, 2: 7, 3: 5, 4: 6, 5: 4}
POINTS = [
    (u, p) for u in sorted(UNIT_POINTS) for p in range(1, UNIT_POINTS[u] + 1)
]


def run_suite(coll, pid, expected_by_pp):
    results = []
    for unit, point in POINTS:
        module = importlib.import_module(f"test_u{unit}p{point}")
        assert (module.META["unit"], module.META["point"]) == (unit, point)
        expected = (expected_by_pp or {}).get(f"U{unit}P{point}")
        results.append(evaluate(module, coll, pid, expected))
    return results


def print_table(results, compare):
    if compare:
        print(f"{'POINT':<7} {'ACTIVITY':<42} {'EXP':<7} {'GOT':<7} RESULT")
    else:
        print(f"{'POINT':<7} {'ACTIVITY':<42} {'GOT':<7}")
    print("-" * (78 if compare else 60))
    for res in results:
        pt = f"U{res['unit']}P{res['point']}"
        name = (res["name"][:40] + "..") if len(res["name"]) > 42 else res["name"]
        if compare:
            tag = "PASS" if res["passed"] else "**FAIL**"
            print(f"{pt:<7} {name:<42} {res['expected']:<7} {res['actual']:<7} {tag}")
        else:
            print(f"{pt:<7} {name:<42} {res['actual']:<7}")
    print("-" * (78 if compare else 60))


def write_report(out_dir, run_id, log_path, results, compare):
    os.makedirs(out_dir, exist_ok=True)
    passed = sum(1 for r in results if r["passed"])
    failed = [r for r in results if r["passed"] is False]

    with open(os.path.join(out_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump(
            {
                "run": run_id,
                "log": log_path.replace("\\", "/"),
                "mode": "fixture" if compare else "ad-hoc (no expected colors)",
                "summary": {
                    "points": len(results),
                    "passed": passed if compare else None,
                    "failed": len(failed) if compare else None,
                },
                "results": results,
            },
            f, indent=2, ensure_ascii=False,
        )

    lines = [
        "# Rubric validation results — " + run_id,
        "",
        f"Log: `{os.path.basename(log_path)}`",
        "",
    ]
    if compare:
        lines += [f"**{passed} / {len(results)} points match the expected dashboard color.**", ""]
    else:
        lines += ["Ad-hoc run — no expected colors for this log (informational only).", ""]
    header = ("| Point | Activity | Expected | Production | Result |"
              if compare else "| Point | Activity | Production |")
    lines += [header, ("|---|---|---|---|---|" if compare else "|---|---|---|")]
    for r in results:
        pt = f"U{r['unit']}P{r['point']}"
        if compare:
            tag = "PASS" if r["passed"] else "**FAIL**"
            lines.append(f"| {pt} | {r['name']} | {r['expected']} | {r['actual']} | {tag} |")
        else:
            lines.append(f"| {pt} | {r['name']} | {r['actual']} |")
    interesting = [r for r in results if r["diagnostics"]]
    if interesting:
        lines += ["", "## Diagnostics", ""]
        for r in interesting:
            lines += ["```", format_result(r), "```", ""]
    with open(os.path.join(out_dir, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def main():
    ap = argparse.ArgumentParser(
        description="Validate the 26 progress-point grading scripts against a fixture log.")
    ap.add_argument("--fixture", help="fixture id from config/fixtures.yaml "
                                      "(default: the manifest's default_fixture)")
    ap.add_argument("--log", help="ad-hoc log dump to grade instead of a fixture "
                                  "(no expected colors / pass-fail)")
    ap.add_argument("--quiet", action="store_true", help="table only, no diagnostics")
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
        missing = [f"U{u}P{p}" for u, p in POINTS
                   if f"U{u}P{p}" not in expected_by_pp]
        if missing:
            raise SystemExit(
                f"Fixture '{fixture_id}' is missing expected colors for: {', '.join(missing)}")

    if not os.path.isfile(log_path):
        raise SystemExit(f"Log file not found: {log_path}")
    coll = load_collection(log_path)
    pid = default_player_id(coll)
    adapted = coll.player_field_source != "playerId"
    print(f"Run: {run_id} | {len(coll.docs)} log records | player = {pid}"
          + (f" (adapted: queries use top-level {coll.player_field_source})" if adapted else ""))
    print()

    results = run_suite(coll, pid, expected_by_pp)
    print_table(results, compare)

    failed = [r for r in results if r["passed"] is False]
    if compare:
        passed = sum(1 for r in results if r["passed"])
        print(f"\nSummary: {passed}/{len(results)} points match the expected dashboard color.")
        print("\nExpected: " + ", ".join(r["expected"].capitalize() for r in results))
    print("Actual:   " + ", ".join(r["actual"].capitalize() for r in results))

    # Diagnostics: always show for yellow points (the reason) and for any FAIL.
    if not args.quiet:
        interesting = [r for r in results if r["diagnostics"]]
        if interesting:
            print("\n" + "=" * 78)
            print("DIAGNOSTICS (reasons for yellow / causes of mismatch)")
            print("=" * 78)
            for res in interesting:
                print(format_result(res))
                print()

    if failed:
        print("=" * 78)
        print(f"{len(failed)} MISMATCH(ES) — production color != expected:")
        for r in failed:
            print(f"  - U{r['unit']}P{r['point']} ({r['name']}): "
                  f"expected {r['expected']}, production gave {r['actual']}")
        print("These points' production color logic (or the log data feeding them) "
              "should be reviewed.")

    if not args.no_report:
        out_dir = os.path.join(SUITE_DIR, "outputs", run_id)
        write_report(out_dir, run_id, log_path, results, compare)
        print(f"\nReport written to {os.path.relpath(out_dir, SUITE_DIR)}"
              f"{os.sep}results.md (+ results.json)")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
