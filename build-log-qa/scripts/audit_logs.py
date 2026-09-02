#!/usr/bin/env python3
"""Weekly MHS gameplay-log audit — command-line entry point.

Typical weekly run (from the repository root):

    python build-log-qa/scripts/audit_logs.py \
        --input playthrough-logs-and-results/08-25-26 \
        --build-id 08-25-26 \
        --baseline build-log-qa/reports/08-13-26

Defaults (relative to build-log-qa/):
  --config    config/event_expectations.yaml
  --coverage  config/coverage/<build-id>.yaml   (if it exists)
  --output    reports/<build-id>
"""

from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # build-log-qa/
sys.path.insert(0, str(ROOT / "src"))

from mhs_log_audit.pipeline import run_audit        # noqa: E402


def main(argv=None) -> int:
    if hasattr(sys.stdout, "buffer"):               # Windows console safety
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace")
    ap = argparse.ArgumentParser(
        description="Audit MHS gameplay logs for a weekly build.")
    ap.add_argument("--input", required=True,
                    help="log file, or folder containing the build's log file(s)")
    ap.add_argument("--build-id", required=True,
                    help="identifier for this build/playthrough, e.g. 08-25-26")
    ap.add_argument("--baseline", default=None,
                    help="previous build to compare against: a previous report "
                         "folder, a snapshot.json, or that build's raw logs")
    ap.add_argument("--config", default=None,
                    help="event expectations YAML "
                         "(default: config/event_expectations.yaml)")
    ap.add_argument("--coverage", default=None,
                    help="coverage manifest YAML (default: "
                         "config/coverage/<build-id>.yaml when present; "
                         "otherwise coverage is inferred from scenes)")
    ap.add_argument("--output", default=None,
                    help="report output folder (default: reports/<build-id>)")
    args = ap.parse_args(argv)

    config = args.config or str(ROOT / "config" / "event_expectations.yaml")
    coverage = args.coverage
    if coverage is None:
        candidate = ROOT / "config" / "coverage" / f"{args.build_id}.yaml"
        coverage = str(candidate) if candidate.is_file() else None
    output = args.output or str(ROOT / "reports" / args.build_id)

    results = run_audit(
        input_path=args.input,
        build_id=args.build_id,
        output_dir=output,
        config_path=config,
        coverage_path=coverage,
        baseline_path=args.baseline,
    )

    print(f"Audit complete for build {results['build_id']}")
    print(f"  records:      {results['record_count']} "
          f"({results['skipped_records']} skipped)")
    print(f"  event types:  {results['event_type_count']}")
    print(f"  findings:     " + ", ".join(
        f"{k}: {v}" for k, v in results["finding_counts"].items()))
    if results["load_warnings"]:
        print(f"  loader warnings: {len(results['load_warnings'])}")
    if results["config_warnings"]:
        print("  config warnings: " + "; ".join(results["config_warnings"]))
    print(f"  report:       {Path(output) / 'audit-report.md'}")
    fails = results["finding_counts"].get("FAIL", 0)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
