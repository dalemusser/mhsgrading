"""Frequency/cadence analysis, duplicate detection, and regression diffs."""

import unittest

from synth import load_recs, make_expectations, rec

from mhs_log_audit.duplicates import find_duplicates
from mhs_log_audit.frequency import compute_interval_stats, frequency_findings
from mhs_log_audit.model import INFO, PASS, WARNING
from mhs_log_audit.profiling import build_profiles
from mhs_log_audit.regression import build_snapshot, diff_snapshots


def _one(findings, **attrs):
    hits = [f for f in findings
            if all(getattr(f, k) == v or (isinstance(v, str) and v in str(getattr(f, k)))
                   for k, v in attrs.items())]
    assert len(hits) >= 1, f"no finding matching {attrs}:\n" + \
        "\n".join(f"{f.status} {f.event_type} {f.summary}" for f in findings)
    return hits[0]


def _stats(records, events=None):
    recs, _ = load_recs(records)
    profiles = build_profiles(recs)
    exp = make_expectations(events or {})
    stats = compute_interval_stats(profiles, exp.thresholds, exp)
    return profiles, exp, stats


class TestFrequency(unittest.TestCase):

    CONT = {"P": {"continuous": {"expected_interval_seconds": 10,
                                 "tolerance_seconds": 0.5}}}

    def test_continuous_cadence_pass(self):
        records = [rec("P", i * 10.0, {"x": i}) for i in range(8)]
        profiles, exp, stats = _stats(records, self.CONT)
        self.assertAlmostEqual(stats["P"].median, 10.0, places=3)
        _one(frequency_findings(stats, profiles, exp), status=PASS,
             summary="cadence matches")

    def test_continuous_cadence_deviation_warns(self):
        records = [rec("P", i * 0.5, {"x": i}) for i in range(8)]
        profiles, exp, stats = _stats(records, self.CONT)
        _one(frequency_findings(stats, profiles, exp), status=WARNING,
             summary="cadence differs")

    def test_continuous_intervals_ignore_scene_changes(self):
        # 10s cadence but a scene switch in the middle: the cross-scene gap
        # must not pollute the estimate
        records = [rec("P", i * 10.0, scene="A") for i in range(4)] + \
                  [rec("P", 300 + i * 10.0, scene="B") for i in range(4)]
        _, _, stats = _stats(records, self.CONT)
        self.assertEqual(stats["P"].n_intervals, 6)  # 3 per scene
        self.assertLess(stats["P"].max, 11)

    def test_long_gap_flagged(self):
        records = [rec("E", 0), rec("E", 1000)]
        profiles, exp, stats = _stats(records)
        _one(frequency_findings(stats, profiles, exp), status=INFO,
             summary="long gaps")


class TestDuplicates(unittest.TestCase):

    def test_exact_duplicates_found(self):
        a = rec("E", 5, {"k": "v"}, oid="a" * 24)
        b = rec("E", 5, {"k": "v"}, oid="b" * 24)
        recs, _ = load_recs([a, b])
        exp = make_expectations()
        finds, rows = find_duplicates(build_profiles(recs), exp.thresholds, exp)
        _one(finds, status=WARNING, summary="exact duplicate")
        self.assertEqual(len(rows), 2)

    def test_near_duplicates_found_and_high_frequency_exempt(self):
        records = [rec("E", 5.0, {"k": "v"}), rec("E", 5.4, {"k": "v"})]
        recs, _ = load_recs(records)
        exp = make_expectations()
        finds, _ = find_duplicates(build_profiles(recs), exp.thresholds, exp)
        _one(finds, status=INFO, summary="near-duplicate")
        exp = make_expectations({"E": {"high_frequency": True}})
        finds, _ = find_duplicates(build_profiles(recs), exp.thresholds, exp)
        self.assertFalse([f for f in finds if "near-duplicate" in f.summary])


class TestRegression(unittest.TestCase):

    def _snapshot(self, records, build_id="B"):
        recs, _ = load_recs(records)

        class LR:  # minimal LoadResult stand-in
            files = ["synthetic.json"]
            versions = ["test-build"]
            sessions = ["synthetic.json:user-1"]

        LR.records = recs
        profiles = build_profiles(recs)
        exp = make_expectations()
        stats = compute_interval_stats(profiles, exp.thresholds, exp)
        return build_snapshot(build_id, profiles, stats, LR, created="")

    def test_new_and_removed_event_types(self):
        base = self._snapshot([rec("Old", 0), rec("Both", 1)], "base")
        cur = self._snapshot([rec("New", 0), rec("Both", 1)], "cur")
        finds, rows = diff_snapshots(cur, base)
        _one(finds, status=INFO, event_type="New", summary="not present in baseline")
        _one(finds, status=WARNING, event_type="Old", summary="absent now")
        kinds = {r["change"] for r in rows}
        self.assertIn("new_event_type", kinds)
        self.assertIn("removed_event_type", kinds)

    def test_new_value_and_type_change(self):
        base = self._snapshot([rec("E", 0, {"a": "Open", "n": "1"})], "base")
        cur = self._snapshot([rec("E", 0, {"a": "Close", "n": 1})], "cur")
        finds, _ = diff_snapshots(cur, base)
        _one(finds, fld="data.a", summary="not seen in baseline")
        _one(finds, status=WARNING, fld="data.n", summary="type changed")

    def test_identical_snapshots_no_differences(self):
        records = [rec("E", 0, {"a": "x"})]
        finds, rows = diff_snapshots(self._snapshot(records),
                                     self._snapshot(records))
        _one(finds, summary="no structural differences")
        self.assertEqual(rows, [])


if __name__ == "__main__":
    unittest.main()
