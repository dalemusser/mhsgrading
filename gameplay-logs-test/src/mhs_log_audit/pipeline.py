"""End-to-end audit orchestration: load -> profile -> audit -> export.

`run_audit` is the single entry point used by both the CLI and the tests.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

from . import checks, duplicates, examples, frequency, inventory, profiling, \
    regression, report, temporal
from .config import (Coverage, infer_coverage, load_coverage,
                     load_expectations, scene_to_units)
from .loader import load_logs
from .model import Finding, fmt_seconds


def run_audit(input_path: str,
              build_id: str,
              output_dir: str,
              config_path: Optional[str] = None,
              coverage_path: Optional[str] = None,
              baseline_path: Optional[str] = None,
              audit_date: Optional[str] = None) -> dict:
    """Run the full audit; returns a summary dict (also written to disk)."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    audit_date = audit_date or datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # ---- load ------------------------------------------------------------
    load_result = load_logs(input_path)
    records = load_result.records
    expectations = load_expectations(config_path)

    # ---- observe ---------------------------------------------------------
    profiles = profiling.build_profiles(records)
    interval_stats = frequency.compute_interval_stats(
        profiles, expectations.thresholds, expectations)
    runs = temporal.scene_timeline(records)

    # ---- coverage --------------------------------------------------------
    coverage = load_coverage(coverage_path)
    if coverage is None:
        scene_units = {sc: scene_to_units(sc)
                       for p in profiles.values() for sc in p.scenes}
        coverage = infer_coverage(scene_units, build_id)
    cov_note = (f"manifest {coverage.path}" if not coverage.inferred
                else "INFERRED from observed scenes (no manifest) — "
                     "a unit seen in the log is assumed at most 'partial'")

    # ---- audit -----------------------------------------------------------
    findings: List[Finding] = []
    findings += profiling.consistency_findings(profiles, expectations)
    findings += checks.expectation_findings(profiles, expectations, coverage)
    findings += checks.cross_event_findings(profiles, expectations)
    findings += frequency.frequency_findings(interval_stats, profiles, expectations)
    dup_findings, dup_rows = duplicates.find_duplicates(
        profiles, expectations.thresholds, expectations)
    findings += dup_findings
    findings += temporal.sequence_findings(profiles, expectations)
    findings += temporal.timeline_findings(runs)
    findings += temporal.ordering_findings(records)

    # ---- regression ------------------------------------------------------
    snapshot = regression.build_snapshot(
        build_id, profiles, interval_stats, load_result, created=audit_date)
    baseline_used = False
    baseline_note = "none supplied"
    diff_rows: List[dict] = []
    if baseline_path:
        base_snap, note = regression.load_baseline(baseline_path)
        baseline_note = note
        if base_snap is None:
            findings.append(Finding(
                status="WARNING", severity="Medium", category="regression",
                summary=f"baseline could not be loaded ({note}) — regression "
                        "analysis skipped"))
        else:
            baseline_used = True
            reg_findings, diff_rows = regression.diff_snapshots(snapshot, base_snap)
            findings += reg_findings

    findings.sort(key=lambda f: f.sort_key())

    # ---- export ----------------------------------------------------------
    total = len(records)
    inv_rows = inventory.event_type_rows(profiles, total)
    scene_rows = inventory.event_scene_rows(profiles)
    fld_rows = inventory.field_rows(profiles)
    val_rows = inventory.unique_value_rows(profiles)
    freq_rows = [interval_stats[et].to_row()
                 for et in sorted(interval_stats,
                                  key=lambda e: (-profiles[e].count, e))]
    timeline_rows = [r.to_row() for r in runs]
    finding_rows = [f.to_row() for f in findings]

    csv_dir = out / "csv"
    report.write_csv(inv_rows, csv_dir / "event_type_summary.csv")
    report.write_csv(scene_rows, csv_dir / "event_scene_summary.csv")
    report.write_csv(fld_rows, csv_dir / "event_field_summary.csv")
    report.write_csv(val_rows, csv_dir / "event_unique_values.csv")
    report.write_csv(freq_rows, csv_dir / "event_frequency_summary.csv")
    report.write_csv(timeline_rows, csv_dir / "scene_timeline.csv")
    report.write_csv(finding_rows, csv_dir / "findings.csv")
    report.write_csv(dup_rows, csv_dir / "duplicate_events.csv")
    if baseline_used:
        report.write_csv(diff_rows, csv_dir / "regression_diff.csv")

    report.write_json(examples.build_examples(profiles), out / "event_examples.json")
    report.write_json(snapshot, out / "snapshot.json")

    first_ts = min((r.ts for r in records if r.ts), default=None)
    last_ts = max((r.ts for r in records if r.ts), default=None)
    span = (f"{first_ts.isoformat()} .. {last_ts.isoformat()} "
            f"({fmt_seconds((last_ts - first_ts).total_seconds())})"
            if first_ts and last_ts else "n/a")

    cov_rows = [{"unit": u, "status": s}
                for u, s in sorted(coverage.tested_content.items())]
    if coverage.notes:
        cov_rows.append({"unit": "notes", "status": "; ".join(coverage.notes)})

    ctx = {
        "build_id": build_id,
        "audit_date": audit_date,
        "files": load_result.files,
        "versions": load_result.versions,
        "users": load_result.users,
        "record_count": total,
        "skipped_records": load_result.skipped_records,
        "session_count": len(load_result.sessions),
        "scene_count": len({r.scene for r in records if r.scene}),
        "time_span": span,
        "coverage_note": cov_note,
        "coverage_rows": cov_rows,
        "baseline_used": baseline_used,
        "baseline_note": baseline_note,
        "load_warnings": load_result.warnings,
        "config_warnings": expectations.warnings + coverage.warnings,
        "findings": findings,
        "inventory_rows": inv_rows,
        "frequency_rows": freq_rows,
        "event_detail_lines": report.event_detail_lines(
            profiles, expectations, interval_stats, findings, val_rows),
    }
    (out / "audit-report.md").write_text(report.render_report(ctx),
                                         encoding="utf-8")

    results = {
        "build_id": build_id,
        "audit_date": audit_date,
        "input": str(input_path),
        "config": expectations.path,
        "coverage": {"inferred": coverage.inferred,
                     "tested_content": coverage.tested_content,
                     "notes": coverage.notes},
        "baseline": baseline_note,
        "record_count": total,
        "skipped_records": load_result.skipped_records,
        "event_type_count": len(profiles),
        "finding_counts": _tally(findings),
        "findings": finding_rows,
        "load_warnings": load_result.warnings,
        "config_warnings": expectations.warnings + coverage.warnings,
    }
    report.write_json(results, out / "audit_results.json")
    return results


def _tally(findings: List[Finding]) -> dict:
    t: dict = {}
    for f in findings:
        t[f.status] = t.get(f.status, 0) + 1
    return dict(sorted(t.items()))
