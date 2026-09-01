"""Loader robustness and generic profiling / schema-consistency tests."""

import json
import tempfile
import unittest
from pathlib import Path

from synth import load_recs, make_expectations, rec, write_log

from mhs_log_audit.loader import load_logs
from mhs_log_audit.profiling import build_profiles, consistency_findings


class TestLoader(unittest.TestCase):

    def test_json_array_file(self):
        with tempfile.TemporaryDirectory() as td:
            path = write_log(Path(td), [rec("A", 1), rec("B", 0)])
            result = load_logs(str(path))
        self.assertEqual(len(result.records), 2)
        # sorted chronologically even though file order was reversed
        self.assertEqual([r.event_type for r in result.records], ["B", "A"])
        self.assertEqual(result.versions, ["test-build"])

    def test_directory_input(self):
        with tempfile.TemporaryDirectory() as td:
            write_log(Path(td), [rec("A", 1)], name="a.json")
            write_log(Path(td), [rec("B", 2)], name="b.json")
            result = load_logs(td)
        self.assertEqual(len(result.records), 2)
        self.assertEqual(sorted(result.files), ["a.json", "b.json"])
        self.assertEqual(len(result.sessions), 2)  # one per file

    def test_ndjson(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.jsonl"
            lines = [json.dumps(rec("A", i)) for i in range(3)]
            path.write_text("\n".join(lines), encoding="utf-8")
            result = load_logs(str(path))
        self.assertEqual(len(result.records), 3)

    def test_object_wrapper(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "log.json"
            path.write_text(json.dumps({"records": [rec("A", 0)]}),
                            encoding="utf-8")
            result = load_logs(str(path))
        self.assertEqual(len(result.records), 1)
        self.assertTrue(any("wrapper" in w for w in result.warnings))

    def test_malformed_records_skipped_not_fatal(self):
        with tempfile.TemporaryDirectory() as td:
            path = write_log(Path(td), [rec("A", 0), "not-a-record", 42])
            result = load_logs(str(path))
        self.assertEqual(len(result.records), 1)
        self.assertEqual(result.skipped_records, 2)
        self.assertEqual(len(result.warnings), 2)

    def test_bad_timestamp_warns(self):
        bad = rec("A", 0)
        bad["timestamp"] = "yesterday-ish"
        recs, warnings = load_recs([bad])
        self.assertIsNone(recs[0].ts)
        self.assertTrue(any("unparseable timestamp" in w for w in warnings))

    def test_missing_input(self):
        result = load_logs("no/such/path")
        self.assertEqual(result.records, [])
        self.assertTrue(result.warnings)


class TestProfiling(unittest.TestCase):

    def test_field_stats_and_nesting(self):
        recs, _ = load_recs([
            rec("P", 0, {"position": {"x": 1.5, "y": 2, "z": 3}}),
            rec("P", 10, {"position": {"x": -1, "y": 0, "z": 9}}),
        ])
        prof = build_profiles(recs)["P"]
        self.assertEqual(prof.count, 2)
        self.assertEqual(prof.fields["data.position.x"].count, 2)
        self.assertEqual(prof.fields["data.position.x"].types, {"number": 2})
        self.assertEqual(prof.fields["data.position.x"].numeric_min, -1)

    def test_missing_and_null_and_empty(self):
        recs, _ = load_recs([
            rec("E", 0, {"a": "x", "b": None}),
            rec("E", 1, {"a": ""}),
        ])
        prof = build_profiles(recs)["E"]
        self.assertEqual(prof.fields["data.a"].empty_string_count, 1)
        self.assertEqual(prof.fields["data.b"].null_count, 1)
        self.assertEqual(prof.fields["data.b"].count, 1)  # present in 1 record

    def test_inconsistent_types_flagged(self):
        recs, _ = load_recs([
            rec("E", 0, {"v": "1"}), rec("E", 1, {"v": 1}),
        ])
        finds = consistency_findings(build_profiles(recs), make_expectations())
        self.assertTrue(any("inconsistent value types" in f.summary
                            and f.fld == "data.v" for f in finds))

    def test_field_name_case_variants_flagged(self):
        recs, _ = load_recs([
            rec("E", 0, {"boxID": "1"}), rec("E", 1, {"boxId": "1"}),
        ])
        finds = consistency_findings(build_profiles(recs), make_expectations())
        self.assertTrue(any("field-name variants" in f.summary for f in finds))

    def test_value_case_variants_flagged(self):
        recs, _ = load_recs([
            rec("E", 0, {"s": "Started"}), rec("E", 1, {"s": "started"}),
        ])
        finds = consistency_findings(build_profiles(recs), make_expectations())
        self.assertTrue(any("values that differ only in spelling/case"
                            in f.summary for f in finds))

    def test_empty_field_name_flagged(self):
        recs, _ = load_recs([rec("E", 0, {"": True})])
        finds = consistency_findings(build_profiles(recs), make_expectations())
        self.assertTrue(any("empty string" in f.summary for f in finds))

    def test_sometimes_present_field_is_info_unless_declared(self):
        recs, _ = load_recs([
            rec("E", 0, {"a": 1, "opt": 2}), rec("E", 1, {"a": 1}),
        ])
        finds = consistency_findings(build_profiles(recs), make_expectations())
        self.assertTrue(any("only part of the records" in f.summary for f in finds))
        exp = make_expectations({"E": {"optional_data_fields": ["opt"]}})
        finds = consistency_findings(build_profiles(recs), exp)
        self.assertFalse(any("only part of the records" in f.summary for f in finds))


if __name__ == "__main__":
    unittest.main()
