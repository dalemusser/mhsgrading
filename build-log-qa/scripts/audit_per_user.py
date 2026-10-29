#!/usr/bin/env python3
"""Per-user build-log QA for a multi-student export (classroom field test).

Runs the weekly audit (pipeline.run_audit) once per user_id found in one
export, adds the classroom data-quality metrics of field_quality.py, and
writes a cohort roll-up that compares every user with a baseline report.

    python build-log-qa/scripts/audit_per_user.py \
        --input playthrough-logs-and-results/fall2026-bowling-green-wayne-county/stratalog_BowlingGreen_WayneCounty.jsonl \
        --build-id fall2026-bowling-green-wayne-county \
        --baseline build-log-qa/reports/09-23-26

Outputs (reports/<build-id>/):
  cohort-report.md              data-driven roll-up (verdicts, prevalence, builds)
  cohort_data.json              cached per-user results (--reuse re-renders from it)
  csv/user_summary.csv          one row per user: metrics, finding counts, verdict
  csv/finding_prevalence.csv    every WARNING/FAIL finding x users, and whether
                                the baseline playthrough had it too
  csv/build_summary.csv         per game build: users, records, delay, stale risk, loss
  csv/transport_sessions.csv    one row per session_id (builds with the envelope)
  users/<user_id>/              the standard audit output for that user, run with
                                an evidence-based coverage.yaml (EndOfUnit fired =
                                complete, unit scene seen = partial, else skipped)

The export is split into per-user JSONL files under --work-dir (default: a
folder in the system temp directory); the export itself is never modified.
Every per-user finding references `<user_id>.jsonl[i] _id=...`; the `_id` is
unique and can be searched for in the original export.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
import tempfile
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # build-log-qa/
sys.path.insert(0, str(ROOT / "src"))

import yaml                                           # noqa: E402

from mhs_log_audit.config import load_expectations   # noqa: E402
from mhs_log_audit.field_quality import (player_metrics,  # noqa: E402
                                         transport_rows, unit_rows,
                                         STALE_DELAY_S)
from mhs_log_audit.loader import load_logs            # noqa: E402
from mhs_log_audit.pipeline import run_audit          # noqa: E402
from mhs_log_audit.report import write_csv            # noqa: E402

# ---- verdict thresholds (documented in the cohort report) -------------------
MIN_ACTIVE_MINUTES = 60      # less active play than this = too little data
STALE_PCT_CAVEAT = 1.0       # % of the student's records that are late legacy-envelope
                             # uploads (stale payload) ...
STALE_PCT_PARTIAL = 10.0     # ... and the share at which payload-based
                             # measures become unreliable for the student
LOSS_PCT_PARTIAL = 5.0       # % of envelope sequence numbers missing
UNITS = (1, 2, 3, 4, 5)
# Event families the current logging design emits during ordinary play; a
# player whose log has none of them is on an older, reduced logging design.
CURRENT_DESIGN_EVENTS = ("InputEvent", "ObjectInterEvent", "gameStartEvent",
                         "argumentationAnswerEvent")


# --------------------------------------------------------------- splitting --

def _safe(uid: str) -> str:
    return re.sub(r"[^0-9A-Za-z_-]", "_", uid)[:80] or "unknown-user"


def split_export(src: Path, work: Path) -> dict:
    """Stream the export into <work>/<user_id>.jsonl; returns {user: lines}."""
    work.mkdir(parents=True, exist_ok=True)
    for old in work.glob("*.jsonl"):
        old.unlink()
    buf = defaultdict(list)
    counts: Counter = Counter()
    pending = 0

    def flush():
        for uid, lines in buf.items():
            with open(work / f"{_safe(uid)}.jsonl", "a", encoding="utf-8") as fh:
                fh.writelines(lines)
        buf.clear()

    with open(src, encoding="utf-8-sig") as fh:
        head = fh.read(1)
        fh.seek(0)
        if head == "[":                               # JSON-array export
            rows = (json.dumps(r, ensure_ascii=False) + "\n" for r in json.load(fh))
        else:
            rows = fh
        for line in rows:
            if not line.strip():
                continue
            try:
                uid = json.loads(line).get("user_id") or "unknown-user"
            except (json.JSONDecodeError, AttributeError):
                uid = "unparseable-lines"
            if not line.endswith("\n"):
                line += "\n"
            buf[uid].append(line)
            counts[uid] += 1
            pending += 1
            if pending >= 200_000:
                flush()
                pending = 0
    flush()
    return dict(counts)


# ------------------------------------------------------------ per-user run --

def _coverage_doc(uid: str, metrics: dict) -> dict:
    seen = {int(u) for u in metrics["units_seen"].split(",") if u}
    ended = {int(u) for u in metrics["units_ended"].split(",") if u}
    tested = {}
    for u in UNITS:
        tested[f"Unit{u}"] = ("complete" if u in ended else
                              "partial" if u in seen else "skipped")
    return {
        "build": uid,
        "tested_content": tested,
        "notes": [
            "Generated by audit_per_user.py from the student's own log: "
            "complete = EndOfUnit fired for the unit; partial = a scene of the "
            "unit was entered but EndOfUnit never fired; skipped = no scene of "
            "the unit appears (content not reached)."],
    }


def audit_one(task: tuple) -> dict:
    uid, path, out_dir, config, baseline, cohort_id, audit_date = task
    t0 = time.time()
    records = load_logs(path).records
    metrics = player_metrics(records)
    by_build = {}
    for v in sorted({r.version for r in records if r.event_type != "crash"}):
        by_build[v or "?"] = player_metrics(
            [r for r in records if r.version == v and r.event_type != "crash"])
    trows = transport_rows(records)
    urows = unit_rows(records)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    cov_path = out / "coverage.yaml"
    cov_path.write_text(yaml.safe_dump(_coverage_doc(uid, metrics),
                                       sort_keys=False, width=100),
                        encoding="utf-8")
    del records
    res = run_audit(input_path=path, build_id=f"{cohort_id} / {uid}",
                    output_dir=str(out), config_path=config,
                    coverage_path=str(cov_path), baseline_path=baseline,
                    audit_date=audit_date)
    keep = [{k: f[k] for k in ("status", "severity", "category", "event_type",
                               "field", "summary", "observed")}
            for f in res["findings"] if f["status"] in ("FAIL", "WARNING")]
    return {"user_id": uid, "metrics": metrics, "by_build": by_build,
            "transport": trows, "units": urows,
            "finding_counts": res["finding_counts"],
            "findings": keep, "seconds": round(time.time() - t0, 1)}


# ------------------------------------------------------------- aggregation --

def _oid_date(uid: str) -> str:
    """A Mongo ObjectId starts with its creation time — the roster upload."""
    try:
        return datetime.fromtimestamp(int(uid[:8], 16), tz=timezone.utc).strftime("%Y-%m-%d")
    except ValueError:
        return "?"


def finding_key(f: dict) -> tuple:
    return (f["status"], f["category"], f["event_type"] or "", f["field"] or "",
            f["summary"])


def baseline_keys(baseline: str) -> set:
    p = Path(baseline)
    p = p / "audit_results.json" if p.is_dir() else p.with_name("audit_results.json")
    if not p.is_file():
        return set()
    doc = json.loads(p.read_text(encoding="utf-8"))
    return {finding_key(f) for f in doc.get("findings", [])
            if f["status"] in ("FAIL", "WARNING")}


def verdict(m: dict, fails: int) -> tuple:
    """(verdict, reasons) — see the method section of the cohort report."""
    if m["active_minutes"] < MIN_ACTIVE_MINUTES:
        return "D - too little data", [
            f"{m['active_minutes']} active minutes / {m['records']} records, "
            f"unit(s) {m['units_seen'] or 'none'}"]
    loss_pct = 100 * m["seq_missing"] / max(m["seq_expected"], 1)
    partial, caveats = [], []
    stale = (f"{m['stale_risk_records']} records ({m['stale_risk_pct']}% of the "
             f"student's log) are legacy-envelope uploads >{STALE_DELAY_S:g}s late - "
             "payload stale")
    if m["stale_risk_pct"] >= STALE_PCT_PARTIAL:
        partial.append(stale)
    elif m["stale_risk_pct"] >= STALE_PCT_CAVEAT:
        caveats.append(stale)
    if m["seq_missing"]:
        (partial if loss_pct >= LOSS_PCT_PARTIAL else caveats).append(
            f"{m['seq_missing']} records lost in transport "
            f"({loss_pct:.1f}% of seq, {m['sessions_with_loss']} session(s))")
    if m["crash_runtime_error"]:
        caveats.append(f"{m['crash_runtime_error']} WASM runtime crash(es)")
    if fails:
        caveats.append(f"{fails} FAIL finding(s)")
    if partial:
        return "C - partly usable", partial + caveats
    if caveats:
        return "B - usable with handling", caveats
    return "A - ready", []


def logging_design(event_types: set) -> str:
    if any(et in event_types for et in CURRENT_DESIGN_EVENTS):
        return "current"
    return "reduced (older build)"


def aggregate(data: list, base_keys: set, baseline: str, event_units: dict) -> dict:
    users = []
    prevalence = defaultdict(lambda: {"cohorts": defaultdict(set),
                                      "unit_completed": defaultdict(set),
                                      "example": ""})
    builds = defaultdict(lambda: Counter())
    build_users = defaultdict(set)
    transport = []
    unit_table = []
    for d in data:
        m = d["metrics"]
        uid = d["user_id"]
        created = _oid_date(uid)
        cohort = ("spring-2026" if m["first_ts"][:4] == "2026"
                  and m["first_ts"][5:7] in ("03", "04", "05", "06") else "fall-2026")
        fails = d["finding_counts"].get("FAIL", 0)
        warns = d["finding_counts"].get("WARNING", 0)
        new_warn = sum(1 for f in d["findings"]
                       if f["category"] != "regression"
                       and finding_key(f) not in base_keys)
        regr = sum(1 for f in d["findings"] if f["category"] == "regression")
        v, reasons = verdict(m, fails)
        ended = {int(u) for u in m["units_ended"].split(",") if u}
        users.append({"user_id": uid, "cohort": cohort, "roster_created": created,
                      "roster_batch": uid[:8],
                      "logging_design": logging_design(set(m["event_types"].split(";"))),
                      "envelope_pct": round(100 * m["envelope_records"]
                                            / max(m["envelope_records"]
                                                  + m["legacy_records"], 1), 1),
                      **m,
                      "FAIL": fails, "WARNING": warns,
                      "warn_new_vs_baseline": new_warn,
                      "warn_regression_vs_baseline": regr,
                      "INFO": d["finding_counts"].get("INFO", 0),
                      "verdict": v, "verdict_reasons": "; ".join(reasons)})
        for f in d["findings"]:
            k = finding_key(f)
            p = prevalence[k]
            p["cohorts"][cohort].add(uid)
            if f["category"] == "coverage" and \
                    ended & set(event_units.get(f["event_type"], ())):
                p["unit_completed"][cohort].add(uid)
            if not p["example"]:
                p["example"] = f"{uid}: {f['observed'][:160]}"
        for b, bm in d["by_build"].items():
            build_users[b].add(uid)
            for k, val in bm.items():
                if isinstance(val, (int, float)) and not isinstance(val, bool) \
                        and k not in ("max_delay_h", "stale_risk_pct",
                                      "furthest_unit", "n_builds"):
                    builds[b][k] += val
            builds[b]["max_delay_h"] = max(builds[b]["max_delay_h"], bm["max_delay_h"])
        entered = {r["unit"]: r for r in d.get("units", [])}
        for u in UNITS:
            r = entered.get(u)
            unit_table.append({"user_id": uid, "roster_created": created,
                               "student_verdict": v, "unit": u,
                               **(_unit_readiness(r) if r else
                                  {"status": "not reached", "data_quality": ""})})
        transport += d["transport"]
    users.sort(key=lambda u: (u["cohort"] != "fall-2026", u["roster_created"],
                              u["roster_batch"], u["user_id"]))
    prev_rows = []
    for k, p in prevalence.items():
        prev_rows.append({
            "status": k[0], "category": k[1], "event_type": k[2], "field": k[3],
            "summary": k[4],
            "users_fall_2026": len(p["cohorts"]["fall-2026"]),
            "users_spring_2026": len(p["cohorts"]["spring-2026"]),
            "fall_users_unit_completed": (len(p["unit_completed"]["fall-2026"])
                                          if k[1] == "coverage" else ""),
            "in_baseline": ("n/a (comparison with baseline)" if k[1] == "regression"
                            else "yes" if k in base_keys else "NO - new"),
            "example": p["example"]})
    prev_rows.sort(key=lambda r: (r["in_baseline"] != "NO - new",
                                  -r["users_fall_2026"], -r["users_spring_2026"]))
    build_rows = []
    for b, c in builds.items():
        legacy = c["legacy_records"]
        build_rows.append({
            "build": b, "users": len(build_users[b]), "records": c["records"],
            "envelope_records": c["envelope_records"], "legacy_records": legacy,
            "envelope_sessions": c["envelope_sessions"],
            "delayed_over_5s": c["delayed_over_5s"],
            "delayed_over_1h": c["delayed_over_1h"],
            "delayed_over_1d": c["delayed_over_1d"],
            "max_delay_h": c["max_delay_h"],
            "client_ahead_over_5s": c["client_ahead_over_5s"],
            "stale_risk_records": c["stale_risk_records"],
            "stale_risk_pct": round(100 * c["stale_risk_records"] / max(legacy, 1), 2),
            "dialogue_keyed": c["dialogue_keyed"],
            "dialogue_mismatch": c["dialogue_mismatch"],
            "dialogue_mismatch_late_upload": c["dialogue_mismatch_late_upload"],
            "dialogue_mismatch_key_node0": c["dialogue_mismatch_key_node0"],
            "dialogue_mismatch_other": c["dialogue_mismatch_other"],
            "seq_expected": c["seq_expected"], "seq_missing": c["seq_missing"],
            "resends": c["resends"], "recovered_records": c["recovered_records"],
            "exact_dup_puzzle_piece": c["exact_dup_puzzle_piece"],
            "exact_dup_other": c["exact_dup_other"],
            "debug_menu_opened": c["debug_menu_opened"]})
    build_rows.sort(key=lambda r: r["build"])
    unit_table.sort(key=lambda r: (r["roster_created"], r["user_id"], r["unit"]))
    return {"users": users, "prevalence": prev_rows, "builds": build_rows,
            "transport": transport, "units": unit_table, "baseline": baseline}


def _unit_readiness(r: dict) -> dict:
    """Unit row + a data-quality label using the student-verdict thresholds."""
    if r["stale_risk_pct"] >= STALE_PCT_PARTIAL:
        q = f"payload unreliable (>= {STALE_PCT_PARTIAL:g}% late uploads)"
    elif r["stale_risk_pct"] >= STALE_PCT_CAVEAT:
        q = "apply late-upload rule"
    else:
        q = "ok"
    if r["lost_records"]:
        q += f"; {r['lost_records']} records lost in transport"
    return {"status": r["status"], "data_quality": q,
            **{k: v for k, v in r.items() if k not in ("unit", "status")}}


# ------------------------------------------------------------------ report --

def _md_table(rows: list, cols: list) -> list:
    out = ["| " + " | ".join(h for h, _ in cols) + " |",
           "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(fn(r) if callable(fn) else r.get(fn, ""))
                                     .replace("|", "\\|") for _, fn in cols) + " |")
    return out


def render(agg: dict, ctx: dict) -> str:
    users, prev, builds = agg["users"], agg["prevalence"], agg["builds"]
    L = [f"# Per-user build-log QA — {ctx['build_id']}", "",
         f"*Generated {ctx['date']} by `build-log-qa/scripts/audit_per_user.py`; "
         "the interpretation lives in `README.md` next to this file.*", "",
         "## 1. Scope", "",
         f"- Export: `{ctx['input']}` — {sum(u['records'] for u in users):,} records, "
         f"{len(users)} user_ids.",
         f"- Baseline: `{agg['baseline']}` (the newest internal playthrough audit).",
         "- Each user was audited with the unchanged weekly pipeline and an "
         "evidence-based coverage manifest (`users/<id>/coverage.yaml`).", ""]
    L += ["## 2. Verdicts", ""]
    vc = Counter((u["cohort"], u["roster_created"], u["verdict"]) for u in users)
    groups = sorted({(u["cohort"], u["roster_created"]) for u in users}, reverse=True)
    verdicts = sorted({u["verdict"] for u in users})
    L += _md_table(
        [{"g": f"{c} (accounts created {d})",
          "n": sum(1 for u in users if (u["cohort"], u["roster_created"]) == (c, d)),
          "design": "; ".join(f"{k}: {n}" for k, n in Counter(
              u["logging_design"] for u in users
              if (u["cohort"], u["roster_created"]) == (c, d)).items()),
          **{v: vc[(c, d, v)] for v in verdicts}} for c, d in groups],
        [("cohort / roster", "g"), ("users", "n"), ("logging design", "design")]
        + [(v, v) for v in verdicts])
    L += [""]
    L += ["## 3. Builds in the export", ""]
    L += _md_table(builds, [
        ("build", "build"), ("users", "users"), ("records", "records"),
        ("envelope recs", "envelope_records"), ("sessions", "envelope_sessions"),
        ("late >5s", "delayed_over_5s"), ("late >1d", "delayed_over_1d"),
        ("max delay h", "max_delay_h"), ("stale-risk %", "stale_risk_pct"),
        ("dlg keyed", "dialogue_keyed"), ("dlg mismatch", "dialogue_mismatch"),
        ("seq expected", "seq_expected"), ("seq missing", "seq_missing"),
        ("resends", "resends"), ("recovered", "recovered_records"),
        ("dup puzzle", "exact_dup_puzzle_piece"), ("dup other", "exact_dup_other")])
    L += ["", "## 4. WARNING/FAIL findings by prevalence", "",
          "`in baseline` = the same finding (status, category, event, field, "
          "summary) was raised for the baseline playthrough. Regression-category "
          "findings compare the user with the baseline playthrough, so they are "
          "about how the student played, not about logging defects. For "
          "absent-event (coverage) findings, `fall: unit done` counts the fall "
          "users who finished (EndOfUnit) a unit the event belongs to — only those "
          "can point at a logging gap rather than unreached content.", ""]
    L += _md_table(prev, [
        ("in baseline", "in_baseline"), ("fall users", "users_fall_2026"),
        ("fall: unit done", "fall_users_unit_completed"),
        ("spring users", "users_spring_2026"), ("status", "status"),
        ("category", "category"), ("event", "event_type"), ("field", "field"),
        ("summary", "summary")])
    L += ["", "## 5. Per-user table", "",
          "Columns: active min = minutes with no gap > 5 min between records; "
          "stale % = share of the student's records that are legacy-envelope "
          f"uploads more than {STALE_DELAY_S:g} s late; envelope % = share on "
          "builds with the session_id/seq envelope; seq miss = sequence numbers missing inside "
          "envelope sessions; FAIL/WARN = pipeline findings (WARN new = not in "
          "baseline, regression excluded).", ""]
    L += _md_table(users, [
        ("user_id", "user_id"), ("cohort", "cohort"), ("roster", "roster_created"),
        ("design", "logging_design"), ("builds", "n_builds"),
        ("envelope %", "envelope_pct"), ("records", "records"),
        ("active min", "active_minutes"), ("days", "active_days"),
        ("units seen", "units_seen"), ("units ended", "units_ended"),
        ("stale %", "stale_risk_pct"), ("seq miss", "seq_missing"),
        ("dlg mism", "dialogue_mismatch"), ("crash", lambda u: u["crash_runtime_error"]
                                            + u["crash_load_stalled"]
                                            + u["crash_unhandled_rejection"]),
        ("FAIL", "FAIL"), ("WARN", "WARNING"), ("WARN new", "warn_new_vs_baseline"),
        ("verdict", "verdict"), ("reasons", "verdict_reasons")])
    L += ["", "## 6. Per-unit readiness", "",
          "Behaviour analysis is usually per unit, and students switched builds "
          "mid-unit, so each student x unit is rated separately "
          "(`csv/user_unit_summary.csv`). Data quality uses the same thresholds "
          f"as the student verdict, applied to the unit's own records: ok = under "
          f"{STALE_PCT_CAVEAT:g}% late legacy-envelope uploads; apply late-upload "
          f"rule = {STALE_PCT_CAVEAT:g}–{STALE_PCT_PARTIAL:g}%; payload unreliable = "
          f"{STALE_PCT_PARTIAL:g}% or more. Counts are students.", ""]
    ut = agg["units"]
    qual = lambda r: r["data_quality"].split(";")[0]
    L += _md_table(
        [{"unit": u,
          "fin": sum(1 for r in ut if r["unit"] == u and r["status"] == "finished"),
          "fin_ok": sum(1 for r in ut if r["unit"] == u and r["status"] == "finished"
                        and qual(r) == "ok"),
          "fin_rule": sum(1 for r in ut if r["unit"] == u and r["status"] == "finished"
                          and qual(r) == "apply late-upload rule"),
          "fin_bad": sum(1 for r in ut if r["unit"] == u and r["status"] == "finished"
                         and qual(r).startswith("payload unreliable")),
          "part": sum(1 for r in ut if r["unit"] == u
                      and r["status"] == "played, not finished"),
          "none": sum(1 for r in ut if r["unit"] == u and r["status"] == "not reached"),
          "lost": sum(1 for r in ut if r["unit"] == u and "lost" in r["data_quality"])}
         for u in UNITS],
        [("unit", "unit"), ("finished", "fin"), ("… payload ok", "fin_ok"),
         ("… apply late-upload rule", "fin_rule"), ("… payload unreliable", "fin_bad"),
         ("played, not finished", "part"), ("not reached", "none"),
         ("with transport loss", "lost")])
    L += ["", "## 7. Method", "",
          f"- **D - too little data:** fewer than {MIN_ACTIVE_MINUTES} active minutes.",
          f"- **C - partly usable:** ≥{STALE_PCT_PARTIAL:g}% of the student's "
          "records are legacy-envelope records uploaded more than "
          f"{STALE_DELAY_S:g} s late (their `data` payload is a stale copy, so "
          "payload-based measures are unreliable for those periods; eventKey, "
          "eventType, sceneName and timestamps stay usable), or "
          f"≥{LOSS_PCT_PARTIAL:g}% of envelope sequence numbers missing.",
          f"- **B - usable with handling:** {STALE_PCT_CAVEAT:g}–"
          f"{STALE_PCT_PARTIAL:g}% stale-risk records, any smaller transport loss, a "
          "WASM runtime crash, or a FAIL finding.",
          "- **A - ready:** none of the above.",
          "- Not used for the verdict: findings that recur in the baseline "
          "playthrough (build-level quirks such as the DialogueEvent `…:0` "
          "first-node eventKey or the fixed-node eventKey/payload pairs), "
          "regression-category differences (pacing), absent events in units the "
          "student did not finish, and pointer-lock `unhandled_rejection` crash "
          "telemetry.",
          "- **Logging design:** `current` = the log contains at least one of "
          f"{', '.join(CURRENT_DESIGN_EVENTS)}; `reduced (older build)` = none of "
          "them (the April 2026 builds log 13 event types).",
          "- Late uploads are serverTimestamp minus client timestamp. On the "
          "20260914- build, 95% of student-days have a median difference within "
          "±2 s, so larger values are upload delay, not clock error.",
          "- Envelope = the `session_id`/`seq`/`entry_id`/`sent_at` fields present "
          "from build 20261005-12466; seq starts at 1 per session, so a missing "
          "number is a lost record and a repeated `entry_id` is a resend.", ""]
    return "\n".join(L)


# -------------------------------------------------------------------- main --

def main(argv=None) -> int:
    if hasattr(sys.stdout, "buffer"):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                      errors="replace")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--input", required=True, help="multi-user export (.jsonl or .json)")
    ap.add_argument("--build-id", required=True, help="report folder name")
    ap.add_argument("--baseline", required=True,
                    help="baseline report folder (e.g. build-log-qa/reports/09-23-26)")
    ap.add_argument("--config", default=str(ROOT / "config" / "event_expectations.yaml"))
    ap.add_argument("--output", default=None, help="default: reports/<build-id>")
    ap.add_argument("--work-dir", default=None,
                    help="where per-user split files go (default: system temp)")
    ap.add_argument("--jobs", type=int, default=max(1, min(16, (os.cpu_count() or 2) - 2)))
    ap.add_argument("--users", nargs="*", help="only audit these user_ids")
    ap.add_argument("--reuse", action="store_true",
                    help="skip splitting/auditing; re-render from cohort_data.json")
    args = ap.parse_args(argv)

    out = Path(args.output or ROOT / "reports" / args.build_id)
    out.mkdir(parents=True, exist_ok=True)
    cache = out / "cohort_data.json"
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if args.reuse:
        data = json.loads(cache.read_text(encoding="utf-8"))["users"]
    else:
        work = Path(args.work_dir or Path(tempfile.gettempdir())
                    / "mhs-build-log-qa-split" / args.build_id)
        t0 = time.time()
        counts = split_export(Path(args.input), work)
        print(f"split {sum(counts.values()):,} records into {len(counts)} user files "
              f"in {work} ({time.time() - t0:.0f}s)")
        uids = sorted(args.users or counts)
        tasks = [(u, str(work / f"{_safe(u)}.jsonl"), str(out / "users" / _safe(u)),
                  args.config, args.baseline, args.build_id, date) for u in uids]
        data = []
        t0 = time.time()
        with ProcessPoolExecutor(max_workers=args.jobs) as ex:
            futs = {ex.submit(audit_one, t): t[0] for t in tasks}
            for i, fut in enumerate(as_completed(futs), 1):
                data.append(fut.result())
                if i % 20 == 0 or i == len(futs):
                    print(f"  audited {i}/{len(futs)} users ({time.time() - t0:.0f}s)")
        cache.write_text(json.dumps({"generated": date, "input": args.input,
                                     "baseline": args.baseline, "users": data}),
                         encoding="utf-8")

    event_units = {et: [int(u) for u in (rules.get("units") or [])]
                   for et, rules in load_expectations(args.config).events.items()}
    agg = aggregate(data, baseline_keys(args.baseline), args.baseline, event_units)
    csv_dir = out / "csv"
    write_csv(agg["users"], csv_dir / "user_summary.csv")
    write_csv(agg["prevalence"], csv_dir / "finding_prevalence.csv")
    write_csv(agg["builds"], csv_dir / "build_summary.csv")
    write_csv(agg["transport"], csv_dir / "transport_sessions.csv")
    write_csv(agg["units"], csv_dir / "user_unit_summary.csv")
    (out / "cohort-report.md").write_text(
        render(agg, {"build_id": args.build_id, "date": date, "input": args.input}),
        encoding="utf-8")
    print("verdicts:", dict(Counter(u["verdict"] for u in agg["users"])))
    print(f"report: {out / 'cohort-report.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
