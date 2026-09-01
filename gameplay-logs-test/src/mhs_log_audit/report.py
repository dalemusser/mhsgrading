"""Machine-readable exports (Step 19) and the Markdown audit report (Step 20).

Outputs, all inside the per-build report folder:
  audit-report.md            human-readable examination report
  audit_results.json         every finding + run metadata (machine-readable)
  snapshot.json              normalized baseline for future regression runs
  event_examples.json        representative raw records per event type
  csv/*.csv                  flat tables (inventory, scenes, fields, values,
                             frequency, timeline, findings, duplicates, diff)
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd

from .model import Finding, FAIL, INFO, NOT_TESTED, PASS, WARNING
from .profiling import EventProfile, fmt_value

CSV_ENCODING = "utf-8-sig"   # Excel-friendly on Windows


def write_csv(rows: List[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding=CSV_ENCODING)


def write_json(obj, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False, default=str),
                    encoding="utf-8")


def _md_escape(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def _finding_bullet(f: Finding) -> str:
    parts = [f"- **{f.status} / {f.severity}**"]
    if f.event_type:
        parts.append(f"`{f.event_type}`")
    if f.fld:
        parts.append(f"`{f.fld}`")
    parts.append(f"— {f.summary}.")
    if f.observed:
        parts.append(f"\n  - Observed: {f.observed}")
    if f.expected:
        parts.append(f"\n  - Expected: {f.expected}")
    if f.evidence:
        parts.append(f"\n  - Evidence: {f.evidence}")
    if f.examples:
        parts.append("\n  - Examples: " + "; ".join(f"`{e}`" for e in f.examples[:3]))
    if f.spec_source:
        parts.append(f"\n  - Spec source: {f.spec_source}")
    return " ".join(parts)


def _section(findings: List[Finding], categories, include_pass=False,
             empty_note="No findings in this category.") -> List[str]:
    sel = [f for f in findings if f.category in categories
           and (include_pass or f.status != PASS)]
    sel.sort(key=lambda f: f.sort_key())
    if not sel:
        return [empty_note, ""]
    out = [_finding_bullet(f) for f in sel]
    out.append("")
    return out


def _table(rows: List[dict], columns: List[str]) -> List[str]:
    if not rows:
        return ["(empty)", ""]
    lines = ["| " + " | ".join(columns) + " |",
             "| " + " | ".join("---" for _ in columns) + " |"]
    for r in rows:
        lines.append("| " + " | ".join(_md_escape(r.get(c, "")) for c in columns) + " |")
    lines.append("")
    return lines


def render_report(ctx: dict) -> str:
    """ctx is assembled by pipeline.run_audit — see there for keys."""
    findings: List[Finding] = ctx["findings"]
    inventory = ctx["inventory_rows"]
    lines: List[str] = []
    add = lines.append

    add(f"# MHS Gameplay Log Audit Report — build {ctx['build_id']}")
    add("")
    add("## 1. Build Information")
    add("")
    add(f"- **Build ID:** {ctx['build_id']}")
    add(f"- **Game version string(s) in log:** {', '.join(ctx['versions']) or 'n/a'}")
    add(f"- **Audit date:** {ctx['audit_date']}")
    add(f"- **Log file(s):** {', '.join(ctx['files']) or 'none'}")
    add(f"- **Records:** {ctx['record_count']} "
        f"({ctx['skipped_records']} malformed skipped)")
    add(f"- **Sessions (file x user):** {ctx['session_count']}")
    add(f"- **Player id(s):** {', '.join(ctx['users']) or 'n/a'}")
    add(f"- **Time span:** {ctx['time_span']}")
    add(f"- **Coverage:** {ctx['coverage_note']}")
    add(f"- **Baseline:** {ctx['baseline_note']}")
    if ctx["load_warnings"]:
        add(f"- **Loader warnings:** {len(ctx['load_warnings'])} (first: "
            f"{ctx['load_warnings'][0]})")
    if ctx["config_warnings"]:
        add("- **Config warnings:** " + "; ".join(ctx["config_warnings"]))
    add("")

    add("## 2. Executive Summary")
    add("")
    tally = {s: 0 for s in (FAIL, WARNING, NOT_TESTED, INFO, PASS)}
    for f in findings:
        tally[f.status] = tally.get(f.status, 0) + 1
    add(f"- **{len(inventory)} event types**, {ctx['record_count']} records, "
        f"{ctx['scene_count']} scenes.")
    add(f"- Findings: **{tally[FAIL]} FAIL**, **{tally[WARNING]} WARNING**, "
        f"{tally[INFO]} INFO, {tally[NOT_TESTED]} NOT_TESTED, "
        f"{tally[PASS]} PASS.")
    top = sorted((f for f in findings if f.status in (FAIL, WARNING)),
                 key=lambda f: f.sort_key())[:10]
    if top:
        add("- Top items needing attention:")
        for f in top:
            et = f" `{f.event_type}`" if f.event_type else ""
            add(f"  - {f.status}/{f.severity}{et}: {f.summary}")
    else:
        add("- No FAIL or WARNING findings.")
    add("")

    add("## 3. Event Inventory")
    add("")
    lines.extend(_table(inventory, [
        "eventType", "record_count", "percent_of_total", "session_count",
        "scene_count", "eventKey_records", "first_timestamp", "last_timestamp",
        "active_span"]))
    add("Full details incl. observed scenes and data fields: "
        "`csv/event_type_summary.csv`.")
    add("")

    add("## 4. New / Removed / Changed Events (vs baseline)")
    add("")
    if ctx["baseline_used"]:
        lines.extend(_section(findings, {"regression"}, include_pass=True,
                              empty_note="No differences vs baseline detected."))
        add("Full diff: `csv/regression_diff.csv`.")
    else:
        add("No baseline supplied — regression analysis skipped. Pass "
            "`--baseline <previous report folder>` to enable it.")
    add("")

    add("## 5. Schema Findings")
    add("")
    lines.extend(_section(findings, {"schema"}))

    add("## 6. Frequency Findings")
    add("")
    lines.extend(_table(ctx["frequency_rows"], [
        "eventType", "n_intervals", "interval_min_s", "interval_median_s",
        "interval_mean_s", "interval_p95_s", "interval_max_s",
        "records_per_active_minute", "burst_pairs", "long_gaps"]))
    lines.extend(_section(findings, {"frequency", "duplicates"}))

    add("## 7. Sequence / Timing Findings")
    add("")
    lines.extend(_section(findings, {"sequence", "temporal", "cross-event"}))

    add("## 8. Coverage Findings")
    add("")
    add(f"Coverage source: {ctx['coverage_note']}")
    add("")
    if ctx["coverage_rows"]:
        lines.extend(_table(ctx["coverage_rows"], ["unit", "status"]))
    lines.extend(_section(findings, {"coverage"},
                          empty_note="No coverage-related findings."))

    add("## 9. Event-Type Details")
    add("")
    lines.extend(ctx["event_detail_lines"])

    add("## 10. Regression Comparison")
    add("")
    if ctx["baseline_used"]:
        add(f"Baseline: {ctx['baseline_note']}. See section 4 for the "
            "structural diff and `csv/regression_diff.csv` for every row.")
    else:
        add("No baseline supplied — skipped.")
    add("")

    add("## 11. Recommended Follow-Up")
    add("")
    dev = [f for f in findings if f.status == FAIL]
    inv = [f for f in findings if f.status == WARNING]
    spec = [f for f in findings if f.status == INFO
            and "specification review" in f.summary.lower()]
    nt = [f for f in findings if f.status == NOT_TESTED]
    if dev:
        add("**Developer investigation (FAIL):**")
        for f in dev[:15]:
            add(f"- `{f.event_type or '-'}` {f.fld or ''}: {f.summary}")
        add("")
    if inv:
        add("**Needs review (WARNING):**")
        for f in sorted(inv, key=lambda f: f.sort_key())[:15]:
            add(f"- `{f.event_type or '-'}` {f.fld or ''}: {f.summary}")
        add("")
    if spec:
        add("**Documentation / specification clarification:**")
        for f in spec[:15]:
            add(f"- `{f.event_type or '-'}` {f.fld or ''}: {f.observed}")
        add("")
    if nt:
        add("**Additional gameplay testing (content not exercised):**")
        for f in nt[:15]:
            add(f"- `{f.event_type or '-'}`: {f.summary}")
        add("")
    if not (dev or inv or spec or nt):
        add("No action required.")
    add("")
    add("---")
    add("*Generated by gameplay-logs-test / mhs_log_audit. All findings are "
        "traceable to raw records via the `file[index] _id=... ts=...` "
        "references; raw examples in `event_examples.json`.*")
    return "\n".join(lines)


def event_detail_lines(profiles: Dict[str, EventProfile], expectations,
                       interval_stats, findings: List[Finding],
                       value_rows: List[dict]) -> List[str]:
    """Section 9 body: one subsection per event type."""
    by_event_vals: Dict[str, List[dict]] = {}
    for r in value_rows:
        by_event_vals.setdefault(r["eventType"], []).append(r)
    lines: List[str] = []
    for et in sorted(profiles, key=lambda e: (-profiles[e].count, e)):
        p = profiles[et]
        rules = expectations.for_event(et) if expectations else {}
        st = interval_stats.get(et)
        rel = [f for f in findings
               if f.event_type == et and f.status in (FAIL, WARNING)]
        lines.append(f"### `{et}` — {p.count} records")
        lines.append("")
        if rules.get("purpose"):
            lines.append(f"*Purpose:* {rules['purpose']}")
            lines.append("")
        scenes = "; ".join(f"{sc} ({n})" for sc, n in
                           sorted(p.scenes.items(), key=lambda kv: (-kv[1], kv[0])))
        lines.append(f"- **Scenes:** {scenes}")
        if p.event_key_count:
            lines.append(f"- **eventKey:** present on {p.event_key_count} of "
                         f"{p.count} records")
        if st and st.n_intervals:
            lines.append(f"- **Intervals:** median {st.median:.2f}s "
                         f"(p5 {st.p5:.2f}s / p95 {st.p95:.2f}s, "
                         f"n={st.n_intervals})")
        if len(p.key_sets) > 1:
            variants = "; ".join(f"[{', '.join(ks)}] x{n}" for ks, n in
                                 p.key_sets.most_common())
            lines.append(f"- **`data` key-set variants:** {variants}")
        if rel:
            lines.append(f"- **Open findings:** {len(rel)} — see sections 5-8")
        lines.append("- **Fields under `data`:**")
        lines.append("")
        lines.append("```text")
        for path in sorted(p.fields):
            fp = p.fields[path]
            types = "/".join(t for t in sorted(fp.types) if t != "null") or "null"
            desc = f"{path}  ({types}, {fp.count}/{p.count} records"
            if fp.null_count:
                desc += f", {fp.null_count} null"
            if fp.empty_string_count:
                desc += f", {fp.empty_string_count} empty-string"
            desc += ")"
            lines.append(desc)
            vals = [v for v in by_event_vals.get(et, [])
                    if v["field_path"] == path]
            if vals and len(vals) <= 12 and not vals[0]["value_list_truncated"] \
                    and "number" not in types:
                for v in vals:
                    lines.append(f"    {v['value']}  x{v['count']}")
            elif fp.numeric_min is not None and fp.n_unique > 12:
                lines.append(f"    numeric range {fp.numeric_min:g} .. "
                             f"{fp.numeric_max:g} ({fp.n_unique} unique)")
            elif vals:
                lines.append(f"    {fp.n_unique} unique values "
                             f"(see csv/event_unique_values.csv)")
        lines.append("```")
        lines.append("")
        lines.append(f"Raw examples: `event_examples.json` -> `{et}`.")
        lines.append("")
    return lines
