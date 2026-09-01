"""Frequency / interval analysis (Step 9).

Interval statistics are computed between consecutive records of the same
event type *within one session* (and additionally within one scene for
continuous telemetry such as PlayerPositionEvent, so scene changes do not
pollute the cadence estimate).

Different event classes are interpreted differently:
  * `continuous` config -> cadence is checked against the expected interval;
  * everything else     -> intervals stay descriptive, and only extreme
    bursts / long gaps are surfaced for inspection.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .model import Finding, fmt_seconds, INFO, PASS, WARNING, MEDIUM, SEV_INFO
from .profiling import EventProfile


def _percentile(sorted_vals: List[float], q: float) -> float:
    """Linear-interpolated percentile of an ascending list (q in 0..100)."""
    if not sorted_vals:
        return float("nan")
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    pos = (len(sorted_vals) - 1) * q / 100.0
    lo = int(pos)
    hi = min(lo + 1, len(sorted_vals) - 1)
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (pos - lo)


@dataclass
class IntervalStats:
    event_type: str
    n_intervals: int = 0
    min: float = 0.0
    p5: float = 0.0
    p25: float = 0.0
    median: float = 0.0
    mean: float = 0.0
    p75: float = 0.0
    p95: float = 0.0
    max: float = 0.0
    per_minute: float = 0.0            # records per active minute
    bursts: List[tuple] = field(default_factory=list)   # (delta, ref_a, ref_b)
    long_gaps: List[tuple] = field(default_factory=list)

    def to_row(self) -> dict:
        r = {"eventType": self.event_type, "n_intervals": self.n_intervals}
        for k in ("min", "p5", "p25", "median", "mean", "p75", "p95", "max"):
            r[f"interval_{k}_s"] = round(getattr(self, k), 3) if self.n_intervals else ""
        r["records_per_active_minute"] = round(self.per_minute, 2)
        r["burst_pairs"] = len(self.bursts)
        r["long_gaps"] = len(self.long_gaps)
        return r


def compute_interval_stats(profiles: Dict[str, EventProfile],
                           thresholds: dict,
                           expectations) -> Dict[str, IntervalStats]:
    burst_s = float(thresholds.get("burst_seconds", 0.05))
    gap_s = float(thresholds.get("long_gap_seconds", 600.0))
    out: Dict[str, IntervalStats] = {}
    for et, prof in profiles.items():
        rules = expectations.for_event(et) if expectations else {}
        same_scene = bool(rules.get("continuous"))
        stats = IntervalStats(event_type=et)
        deltas: List[float] = []
        prev = None
        for rec in prof.records:                      # already chronological
            if rec.ts is None:
                continue
            if prev is not None and prev.session_id == rec.session_id \
                    and (not same_scene or prev.scene == rec.scene):
                d = (rec.ts - prev.ts).total_seconds()
                deltas.append(d)
                if d <= burst_s:
                    stats.bursts.append((d, prev.ref(), rec.ref()))
                elif d >= gap_s:
                    stats.long_gaps.append((d, prev.ref(), rec.ref()))
            prev = rec
        stats.n_intervals = len(deltas)
        if deltas:
            s = sorted(deltas)
            stats.min, stats.max = s[0], s[-1]
            stats.mean = sum(s) / len(s)
            for name, q in (("p5", 5), ("p25", 25), ("median", 50),
                            ("p75", 75), ("p95", 95)):
                setattr(stats, name, _percentile(s, q))
            active = sum(s)
            stats.per_minute = 60.0 * len(s) / active if active > 0 else 0.0
        out[et] = stats
    return out


def frequency_findings(stats: Dict[str, IntervalStats],
                       profiles: Dict[str, EventProfile],
                       expectations) -> List[Finding]:
    findings: List[Finding] = []
    for et in sorted(stats):
        st = stats[et]
        rules = expectations.for_event(et) if expectations else {}
        cont = rules.get("continuous")
        spec = rules.get("spec_source", "")

        if cont and st.n_intervals >= 3:
            expected = float(cont.get("expected_interval_seconds", 0))
            tol = float(cont.get("tolerance_seconds", max(0.5, expected * 0.1)))
            # the median interval is the cadence estimate; p5/p95 show spread
            if abs(st.median - expected) <= tol:
                findings.append(Finding(
                    status=PASS, severity=SEV_INFO, category="frequency",
                    event_type=et,
                    summary=f"continuous cadence matches expectation (~{expected:g}s)",
                    observed=f"median interval {st.median:.3f}s "
                             f"(p5 {st.p5:.2f}s, p95 {st.p95:.2f}s, n={st.n_intervals})",
                    expected=f"~{expected:g}s (±{tol:g}s)", spec_source=spec))
            else:
                findings.append(Finding(
                    status=WARNING, severity=MEDIUM, category="frequency",
                    event_type=et,
                    summary="continuous cadence differs from expectation",
                    observed=f"median interval {st.median:.3f}s "
                             f"(p5 {st.p5:.2f}s, p95 {st.p95:.2f}s, n={st.n_intervals})",
                    expected=f"~{expected:g}s (±{tol:g}s)",
                    evidence="regression candidate: cadence change or logging change",
                    spec_source=spec))
        elif cont:
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="frequency", event_type=et,
                summary="too few records to evaluate continuous cadence",
                observed=f"{st.n_intervals} interval(s)", expected="≥3 intervals",
                spec_source=spec))

        if st.bursts:
            worst = sorted(st.bursts)[:3]
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="frequency", event_type=et,
                summary="very rapid consecutive records (possible duplicates "
                        "or multi-fire)",
                observed=f"{len(st.bursts)} interval(s) ≤ "
                         f"{worst[0][0]:.3f}s..{worst[-1][0]:.3f}s shown",
                evidence="; ".join(f"{d * 1000:.0f}ms: {a} -> {b}"
                                   for d, a, b in worst),
            ))
        if st.long_gaps:
            worst = sorted(st.long_gaps, reverse=True)[:3]
            findings.append(Finding(
                status=INFO, severity=SEV_INFO, category="frequency", event_type=et,
                summary="unusually long gaps between records",
                observed=f"{len(st.long_gaps)} gap(s), longest "
                         f"{fmt_seconds(worst[0][0])}",
                evidence="; ".join(f"{fmt_seconds(d)}: {a} -> {b}"
                                   for d, a, b in worst),
            ))
    return findings
