"""Synthetic log-record builders for the test suite.

Tests run on generated records only — the real gameplay logs are not needed.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

BASE_TS = datetime(2026, 8, 25, 12, 0, 0, tzinfo=timezone.utc)


def ts(seconds: float) -> str:
    t = BASE_TS + timedelta(seconds=seconds)
    return t.strftime("%Y-%m-%dT%H:%M:%S.%f0Z")


def rec(event_type: str, seconds: float, data=None, scene="Unit 1 Dev",
        oid=None, user="user-1", event_key=None, **extra) -> dict:
    r = {
        "_id": {"$oid": oid or f"{int(seconds * 1000):024x}"},
        "user_id": user,
        "game": "mhs",
        "version": "test-build",
        "sceneName": scene,
        "timestamp": ts(seconds),
        "eventType": event_type,
        "data": {} if data is None else data,
    }
    if event_key is not None:
        r["eventKey"] = event_key
    r.update(extra)
    return r


def write_log(tmpdir: Path, records, name="synthetic.logdata.json") -> Path:
    tmpdir.mkdir(parents=True, exist_ok=True)
    path = tmpdir / name
    path.write_text(json.dumps(records), encoding="utf-8")
    return path


def load_recs(records):
    """Normalize a list of raw dicts through the real loader code path."""
    from mhs_log_audit.loader import normalize_record, _sort_chronological
    warnings = []
    out = [normalize_record(r, i, "synthetic.json", warnings)
           for i, r in enumerate(records)]
    return _sort_chronological([r for r in out if r is not None]), warnings


def make_expectations(events=None, cross_event_rules=None, thresholds=None):
    from mhs_log_audit.config import Expectations, DEFAULT_THRESHOLDS
    return Expectations(events=events or {},
                        cross_event_rules=cross_event_rules or [],
                        thresholds={**DEFAULT_THRESHOLDS, **(thresholds or {})})


def make_coverage(tested=None, inferred=False):
    from mhs_log_audit.config import Coverage
    return Coverage(build="test", tested_content=tested or {}, inferred=inferred)
