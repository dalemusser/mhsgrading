"""Per-player data-quality metrics (field_quality.py) for classroom exports."""

import unittest

from synth import load_recs, rec, ts

from mhs_log_audit.field_quality import player_metrics, transport_rows, unit_rows


def srv(seconds):
    return {"$date": ts(seconds)}


def env(event_type, seconds, seq, session="s1", data=None, late=0.0, **kw):
    """A record with the session_id/seq envelope (builds from 20261005)."""
    return rec(event_type, seconds, data, session_id=session, seq=float(seq),
               entry_id=f"{session}:{seq}", serverTimestamp=srv(seconds + late), **kw)


class TestTransport(unittest.TestCase):

    def test_seq_holes_and_resends(self):
        raw = [env("InputEvent", i, i) for i in (1, 2, 3, 7, 8)]
        raw.append(env("InputEvent", 8, 8))                # resend of seq 8
        recs, _ = load_recs(raw)
        [row] = transport_rows(recs)
        self.assertEqual(row["missing_seq"], 3)            # 4, 5, 6
        self.assertEqual(row["holes"], "4-6")
        self.assertEqual(row["resends"], 1)
        m = player_metrics(recs)
        self.assertEqual((m["seq_expected"], m["seq_missing"]), (8, 3))
        self.assertEqual(m["sessions_with_loss"], 1)
        # a resend is not counted again as an exact duplicate
        self.assertEqual(m["exact_dup_other"], 0)

    def test_session_not_starting_at_one_is_loss(self):
        recs, _ = load_recs([env("InputEvent", i, i + 2) for i in (1, 2)])
        self.assertEqual(transport_rows(recs)[0]["holes"], "1-2")


class TestStalePayloadRisk(unittest.TestCase):

    def test_only_late_legacy_records_count(self):
        raw = [rec("InputEvent", 1, serverTimestamp=srv(1.5)),       # on time
               rec("InputEvent", 2, serverTimestamp=srv(2 + 7200)),  # 2 h late, legacy
               env("InputEvent", 3, 1, late=3600)]                   # 1 h late, envelope
        m = player_metrics(load_recs(raw)[0])
        self.assertEqual(m["legacy_records"], 2)
        self.assertEqual(m["stale_risk_records"], 1)
        self.assertEqual(m["stale_risk_pct"], 33.33)    # of all the player's records
        self.assertEqual(m["delayed_over_1h"], 1)       # exactly 1 h is not "over"
        self.assertEqual(m["delayed_over_5s"], 2)

    def test_dialogue_mismatch_classification(self):
        dlg = "DialogueEvent"
        raw = [
            rec(dlg, 1, {"conversationId": 20.0, "nodeId": 33.0},
                event_key="DialogueNodeEvent:20:33", serverTimestamp=srv(1)),   # match
            rec(dlg, 2, {"conversationId": 20.0, "nodeId": 5.0},
                event_key="DialogueNodeEvent:20:0", serverTimestamp=srv(2)),    # :0 quirk
            rec(dlg, 3, {"conversationId": 9.0, "nodeId": 1.0},
                event_key="DialogueNodeEvent:20:40", serverTimestamp=srv(900)),  # late
            rec(dlg, 4, {"conversationId": 73.0, "nodeId": 212.0},
                event_key="DialogueNodeEvent:73:211", serverTimestamp=srv(4)),  # other
        ]
        m = player_metrics(load_recs(raw)[0])
        self.assertEqual(m["dialogue_keyed"], 4)
        self.assertEqual(m["dialogue_mismatch"], 3)
        self.assertEqual(m["dialogue_mismatch_late_upload"], 1)
        self.assertEqual(m["dialogue_mismatch_key_node0"], 1)
        self.assertEqual(m["dialogue_mismatch_other"], 1)


class TestProgressAndContext(unittest.TestCase):

    def test_units_quests_crash_debug(self):
        raw = [
            rec("PlayerPositionEvent", 1, scene="Unit 1 Dev"),
            rec("EndOfUnit", 2, {"Unit": "1"}, scene="Unit 1 Dev"),
            rec("questEvent", 3, {"questID": "22"}, scene="Unit 2 Prod (Refactor)",
                event_key="questFinishEvent:22"),
            rec("DEBUGMenu", 4, {"actionType": "DebugMenuStateChanged", "isOpened": False}),
            {"_id": {"$oid": "f" * 24}, "user_id": "user-1", "eventType": "crash",
             "version": "2.8.1", "data": {"type": "runtime_error"}},
        ]
        m = player_metrics(load_recs(raw)[0])
        self.assertEqual(m["units_seen"], "1,2")
        self.assertEqual(m["units_ended"], "1")
        self.assertEqual(m["quests_finished"], 1)
        self.assertEqual(m["crash_runtime_error"], 1)
        self.assertEqual(m["no_client_ts"], 1)
        self.assertEqual(m["debug_menu_opened"], 0)
        self.assertNotIn("2.8.1", m["builds"])          # crash app-version ignored

    def test_active_minutes_ignore_long_gaps(self):
        raw = [rec("InputEvent", s) for s in (0, 60, 120, 120 + 3600, 120 + 3660)]
        self.assertEqual(player_metrics(load_recs(raw)[0])["active_minutes"], 3.0)


class TestUnitRows(unittest.TestCase):

    def test_per_unit_status_staleness_and_loss(self):
        u1, u2 = "Unit 1 Dev", "Unit 2 Prod (Refactor)"
        raw = [
            rec("InputEvent", 1, scene=u1, serverTimestamp=srv(1)),
            rec("EndOfUnit", 2, {"Unit": "1"}, scene=u1, serverTimestamp=srv(2)),
            rec("InputEvent", 3, scene=u2, serverTimestamp=srv(3)),
            rec("InputEvent", 4, scene=u2, serverTimestamp=srv(4000)),   # late, legacy
            env("InputEvent", 5, 1, scene=u2),                            # build switch
            env("InputEvent", 6, 4, scene=u2),                            # seq 2-3 lost
            rec("PlayerPositionEvent", 7, scene="MainMenu", serverTimestamp=srv(7)),
        ]
        rows = {r["unit"]: r for r in unit_rows(load_recs(raw)[0])}
        self.assertEqual(sorted(rows), [1, 2])                 # MainMenu has no unit
        self.assertEqual(rows[1]["status"], "finished")
        self.assertEqual(rows[2]["status"], "played, not finished")
        self.assertEqual((rows[2]["records"], rows[2]["stale_risk_records"]), (4, 1))
        self.assertEqual(rows[2]["stale_risk_pct"], 25.0)
        self.assertEqual(rows[2]["lost_records"], 2)
        self.assertEqual(rows[2]["envelope_pct"], 50.0)


class TestCohortAggregate(unittest.TestCase):
    """The cohort roll-up must pass each user's rows through exactly once."""

    def test_rows_not_duplicated(self):
        import importlib.util
        from pathlib import Path
        path = Path(__file__).resolve().parents[1] / "scripts" / "audit_per_user.py"
        spec = importlib.util.spec_from_file_location("audit_per_user", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        raw = [env("InputEvent", i, i, scene="Unit 1 Dev") for i in (1, 2, 3)]
        raw += [env("InputEvent", 10 + i, i, session="s2", scene="Unit 2 Prod (Refactor)")
                for i in (1, 2)]
        recs, _ = load_recs(raw)
        d = {"user_id": "user-1", "metrics": player_metrics(recs),
             "by_build": {"test-build": player_metrics(recs)},
             "transport": transport_rows(recs), "units": unit_rows(recs),
             "finding_counts": {}, "findings": []}
        agg = mod.aggregate([d], set(), "baseline", {})
        self.assertEqual(len(agg["transport"]), 2)            # two sessions
        self.assertEqual(len(agg["units"]), len(mod.UNITS))   # one row per unit
        self.assertEqual(len(agg["users"]), 1)


if __name__ == "__main__":
    unittest.main()
