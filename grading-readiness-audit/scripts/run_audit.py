"""Orchestrator — runs the full audit pipeline in phase order.

Usage (from the repository root):

    python grading-readiness-audit/scripts/run_audit.py
    python grading-readiness-audit/scripts/run_audit.py --log-dir playthrough-logs-and-results/09-01-26 --build-label 09-01-26

--log-dir / --build-label / --coverage-yaml override config/audit-config.yaml
for one run (handy for pointing at a new weekly build without editing the
config). Exits non-zero if any phase fails or the final consistency checks
report failures.
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

PHASES = [
    ("Phase 1a  parse grading specs", "parse_grading_specs.py"),
    ("Phase 1b  parse source docs", "parse_source_docs.py"),
    ("Phase 2   inventory gameplay logs", "inventory_gameplay_logs.py"),
    ("Phase 3   reconcile dialogues", "reconcile_dialogues.py"),
    ("Phase 4-6 audit progress points", "audit_progress_points.py"),
    ("Phase 7   run grading validation", "run_grading_validation.py"),
    ("Phase 8   generate reports", "generate_reports.py"),
    ("Checks    validate outputs", "validate_outputs.py"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log-dir")
    ap.add_argument("--build-label")
    ap.add_argument("--coverage-yaml")
    ap.add_argument("--outputs-dir", help="run-specific outputs dir relative to grading-readiness-audit/, e.g. outputs/08-31-26")
    ap.add_argument("--reports-dir", help="run-specific reports dir relative to grading-readiness-audit/, e.g. reports/08-31-26")
    args = ap.parse_args()

    # Apply one-run overrides via a temp config the phases pick up through env.
    env = dict(os.environ)
    if any((args.log_dir, args.build_label, args.coverage_yaml, args.outputs_dir, args.reports_dir)):
        import yaml

        cfg_path = os.path.join(HERE, "..", "config", "audit-config.yaml")
        with open(cfg_path, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        if args.log_dir:
            cfg["log_dir"] = args.log_dir
        if args.build_label:
            cfg["build_label"] = args.build_label
        if args.coverage_yaml:
            cfg["coverage_yaml"] = args.coverage_yaml
        if args.outputs_dir:
            cfg["outputs_dir"] = args.outputs_dir
        if args.reports_dir:
            cfg["reports_dir"] = args.reports_dir
        tmp_cfg = os.path.join(HERE, "..", "config", "audit-config.override.yaml")
        with open(tmp_cfg, "w", encoding="utf-8") as f:
            yaml.safe_dump(cfg, f)
        env["PPAUDIT_CONFIG"] = os.path.abspath(tmp_cfg)
        print(f"Using override config: {tmp_cfg}")

    for label, script in PHASES:
        print(f"\n=== {label} ===", flush=True)
        r = subprocess.run([sys.executable, os.path.join(HERE, script)], env=env)
        if r.returncode != 0:
            print(f"\nABORT: {script} exited {r.returncode}")
            return r.returncode
    print("\nAudit pipeline complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
