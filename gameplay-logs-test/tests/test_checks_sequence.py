"""Expectation-driven checks, coverage gating, sequence and cross-event rules."""

import unittest

from synth import load_recs, make_coverage, make_expectations, rec

from mhs_log_audit.checks import cross_event_findings, expectation_findings
from mhs_log_audit.model import FAIL, INFO, NOT_TESTED, PASS, WARNING
from mhs_log_audit.profiling import build_profiles
from mhs_log_audit.temporal import sequence_findings


def _one(findings, **attrs):
    hits = [f for f in findings
            if all(getattr(f, k) == v or (isinstance(v, str) and v in str(getattr(f, k)))
                   for k, v in attrs.items())]
    assert len(hits) >= 1, f"no finding matching {attrs}:\n" + \
        "\n".join(f"{f.status} {f.event_type} {f.summary}" for f in findings)
    return hits[0]


class TestExpectationChecks(unittest.TestCase):

    def _run(self, records, events, tested=None):
        recs, _ = load_recs(records)
        profiles = build_profiles(recs)
        return expectation_findings(
            profiles, make_expectations(events),
            make_coverage(tested or {"Unit1": "complete"}))

    def test_required_field_missing_is_fail(self):
        finds = self._run(
            [rec("E", 0, {"actionType": "Open"}), rec("E", 1, {})],
            {"E": {"required_data_fields": ["actionType"]}})
        f = _one(finds, status=FAIL, event_type="E")
        self.assertIn("1 of 2", f.observed)
        self.assertTrue(f.examples)

    def test_required_field_all_present_is_pass(self):
        finds = self._run([rec("E", 0, {"actionType": "Open"})],
                          {"E": {"required_data_fields": ["actionType"]}})
        _one(finds, status=PASS, event_type="E")

    def test_new_action_value_is_spec_review_info_not_fail(self):
        finds = self._run(
            [rec("E", 0, {"actionType": "LegendClick"})],
            {"E": {"allowed_values": {"actionType": ["Open", "Close"]}}})
        f = _one(finds, status=INFO, summary="specification review")
        self.assertIn("LegendClick", f.observed)
        self.assertFalse([x for x in finds if x.status == FAIL])

    def test_unknown_event_type_gets_descriptive_info(self):
        finds = self._run([rec("Mystery", 0, {"a": 1})], {})
        _one(finds, status=INFO, event_type="Mystery",
             summary="no expectation rules")

    def test_absent_event_with_skipped_unit_is_not_tested(self):
        finds = self._run([rec("Other", 0)],
                          {"U4Event": {"units": [4]}},
                          tested={"Unit1": "complete", "Unit4": "skipped"})
        _one(finds, status=NOT_TESTED, event_type="U4Event")

    def test_absent_event_with_played_unit_is_warning(self):
        finds = self._run([rec("Other", 0)],
                          {"U1Event": {"units": [1]}},
                          tested={"Unit1": "complete"})
        f = _one(finds, status=WARNING, event_type="U1Event")
        self.assertIn("possible logging failure", f.summary)

    def test_conditional_field(self):
        events = {"Q": {"conditional_fields": {
            "outcome": {"when": {"kind": "finish"}, "required": True,
                        "forbidden_otherwise": True}}}}
        finds = self._run(
            [rec("Q", 0, {"kind": "finish"}),                      # missing
             rec("Q", 1, {"kind": "start", "outcome": "early"})],  # stray
            events)
        _one(finds, status=FAIL, fld="data.outcome")
        _one(finds, status=WARNING, summary="condition")

    def test_expected_scene_and_unexpected_scene(self):
        events = {"E": {"expected_scenes": ["Unit 1 Dev"]}}
        finds = self._run(
            [rec("E", 0, scene="Unit 1 Dev"), rec("E", 1, scene="Unit 9 Lab")],
            events)
        f = _one(finds, status=INFO, category="scenes",
                 summary="specification review")
        self.assertIn("Unit 9 Lab", f.observed)

    def test_event_key_format_mismatch(self):
        events = {"Q": {"event_key": {
            "required": True, "format": "{data.kind}:{data.qid}"}}}
        finds = self._run(
            [rec("Q", 0, {"kind": "start", "qid": "7"}, event_key="start:7"),
             rec("Q", 1, {"kind": "start", "qid": "8"}, event_key="start:9"),
             rec("Q", 2, {"kind": "start", "qid": "9"})],   # missing key
            events)
        _one(finds, status=WARNING, fld="eventKey", summary="format")
        _one(finds, status=FAIL, fld="eventKey", summary="missing")

    def test_semantics_sufficiency(self):
        events = {"E": {"semantics": [
            {"question": "what was chosen?", "satisfied_by": ["choice"]},
            {"question": "did it succeed?", "satisfied_by": ["outcome"]}]}}
        finds = self._run([rec("E", 0, {"choice": "A"})], events)
        _one(finds, status=PASS, category="semantics", summary="what was chosen")
        _one(finds, status=WARNING, category="semantics", summary="did it succeed")


class TestSequence(unittest.TestCase):

    def _run(self, records, events):
        recs, _ = load_recs(records)
        return sequence_findings(build_profiles(recs), make_expectations(events))

    PAIR = {"E": {"pairing": [{"label": "door", "field": "actionType",
                               "open_value": "Open", "close_value": "Close"}]}}

    def test_balanced_pairing_passes(self):
        finds = self._run([rec("E", 0, {"actionType": "Open"}),
                           rec("E", 1, {"actionType": "Close"})], self.PAIR)
        _one(finds, status=PASS, summary="pair correctly")

    def test_close_without_open(self):
        finds = self._run([rec("E", 0, {"actionType": "Close"})], self.PAIR)
        _one(finds, status=WARNING, summary="close without preceding open")

    def test_open_never_closed_is_info(self):
        finds = self._run([rec("E", 0, {"actionType": "Open"})], self.PAIR)
        _one(finds, status=INFO, summary="never close")

    def test_start_finish_grouped(self):
        events = {"Q": {"start_finish": [{
            "label": "quest", "field": "kind", "start_value": "start",
            "finish_value": "finish", "group_by": "qid"}]}}
        finds = self._run(
            [rec("Q", 0, {"kind": "start", "qid": "1"}),
             rec("Q", 1, {"kind": "finish", "qid": "1"}),
             rec("Q", 2, {"kind": "finish", "qid": "2"})],  # finish w/o start
            events)
        _one(finds, status=WARNING, summary="finish without preceding start")


class TestCrossEvent(unittest.TestCase):

    def test_missing_corroboration_warns(self):
        rules = [{"label": "submit implies open",
                  "if": {"event_type": "Answer", "where": {"a": "submit"}},
                  "expect": {"event_type": "Session", "where": {"a": "open"}}}]
        recs, _ = load_recs([rec("Answer", 0, {"a": "submit"})])
        finds = cross_event_findings(build_profiles(recs),
                                     make_expectations(cross_event_rules=rules))
        _one(finds, status=WARNING, summary="submit implies open")
        # satisfied case
        recs, _ = load_recs([rec("Answer", 0, {"a": "submit"}),
                             rec("Session", 1, {"a": "open"})])
        finds = cross_event_findings(build_profiles(recs),
                                     make_expectations(cross_event_rules=rules))
        _one(finds, status=PASS, summary="submit implies open")


if __name__ == "__main__":
    unittest.main()
