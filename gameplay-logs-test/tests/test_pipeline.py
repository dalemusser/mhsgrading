"""End-to-end pipeline test on a synthetic build (no real logs required)."""

import json
import tempfile
import unittest
from pathlib import Path

from synth import rec, write_log

from mhs_log_audit.pipeline import run_audit

CONFIG_YAML = """
events:
  DoorEvent:
    units: [1]
    required_data_fields: [actionType]
    allowed_values:
      actionType: [Open, Close]
    pairing:
      - {label: door, field: actionType, open_value: Open, close_value: Close}
  GhostEvent:
    units: [4]
"""

COVERAGE_YAML = """
build: synthetic
tested_content:
  Unit1: complete
  Unit4: skipped
"""


class TestPipeline(unittest.TestCase):

    def _make_build(self, root: Path, name: str, records):
        d = root / name
        write_log(d, records)
        return d

    def test_full_run_and_regression(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            cfg = root / "expectations.yaml"
            cfg.write_text(CONFIG_YAML, encoding="utf-8")
            cov = root / "coverage.yaml"
            cov.write_text(COVERAGE_YAML, encoding="utf-8")

            base_logs = self._make_build(root, "base", [
                rec("DoorEvent", 0, {"actionType": "Open"}),
                rec("DoorEvent", 5, {"actionType": "Close"}),
            ])
            cur_logs = self._make_build(root, "cur", [
                rec("DoorEvent", 0, {"actionType": "Open"}),
                rec("DoorEvent", 5, {"actionType": "Slam"}),   # new value
                rec("NewEvent", 6, {"x": 1}),                  # new event type
            ])

            base_out = root / "reports" / "base"
            results = run_audit(str(base_logs), "base", str(base_out),
                                config_path=str(cfg), coverage_path=str(cov))
            self.assertEqual(results["record_count"], 2)
            self.assertTrue((base_out / "snapshot.json").is_file())

            cur_out = root / "reports" / "cur"
            results = run_audit(str(cur_logs), "cur", str(cur_out),
                                config_path=str(cfg), coverage_path=str(cov),
                                baseline_path=str(base_out))

            report = (cur_out / "audit-report.md").read_text(encoding="utf-8")
            data = json.loads((cur_out / "audit_results.json")
                              .read_text(encoding="utf-8"))
            summaries = [f["summary"] for f in data["findings"]]

            # expectation checks
            self.assertTrue(any("specification review" in s for s in summaries))
            # coverage gating: GhostEvent absent + Unit4 skipped -> NOT_TESTED
            nt = [f for f in data["findings"]
                  if f["event_type"] == "GhostEvent"]
            self.assertEqual(nt[0]["status"], "NOT_TESTED")
            # regression picked up the new event type
            self.assertTrue(any("not present in baseline" in s for s in summaries))
            # outputs exist
            for out_file in ("audit-report.md", "audit_results.json",
                             "snapshot.json", "event_examples.json"):
                self.assertTrue((cur_out / out_file).is_file(), out_file)
            for csv_name in ("event_type_summary.csv", "findings.csv",
                             "scene_timeline.csv", "regression_diff.csv"):
                self.assertTrue((cur_out / "csv" / csv_name).is_file(), csv_name)
            self.assertIn("NewEvent", report)

    def test_run_without_baseline_or_coverage(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            logs = self._make_build(root, "solo", [rec("DoorEvent", 0,
                                                       {"actionType": "Open"})])
            out = root / "reports" / "solo"
            results = run_audit(str(logs), "solo", str(out))
            self.assertEqual(results["record_count"], 1)
            self.assertTrue(results["coverage"]["inferred"])
            report = (out / "audit-report.md").read_text(encoding="utf-8")
            self.assertIn("No baseline supplied", report)

    def test_broken_baseline_is_nonfatal(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            logs = self._make_build(root, "solo", [rec("E", 0)])
            out = root / "reports" / "solo"
            results = run_audit(str(logs), "solo", str(out),
                                baseline_path=str(root / "missing"))
            self.assertTrue(any("baseline could not be loaded" in f["summary"]
                                for f in results["findings"]))


if __name__ == "__main__":
    unittest.main()
