"""Core data structures shared by every audit module.

`Rec` is the normalized view of one raw log record; the raw dict is kept
alongside so every finding can be traced back to the original JSON.
`Finding` is the single unit of audit output.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional

# Statuses (observation vs expectation vs coverage — see README)
PASS = "PASS"
WARNING = "WARNING"
FAIL = "FAIL"
NOT_TESTED = "NOT_TESTED"
INFO = "INFO"

# Severities
CRITICAL = "Critical"
HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"
SEV_INFO = "Info"
SEV_NOT_TESTED = "NotTested"

_SEV_ORDER = {CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3, SEV_INFO: 4, SEV_NOT_TESTED: 5}

_TS_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})(?:\.(\d+))?(?:Z|[+-]\d{2}:?\d{2})?$")


def parse_timestamp(value: Any) -> Optional[datetime]:
    """Parse the game's ISO timestamps (7 fractional digits, trailing Z).

    Returns a timezone-aware UTC datetime, or None when unparseable.
    """
    if not isinstance(value, str):
        return None
    m = _TS_RE.match(value.strip())
    if not m:
        return None
    frac = (m.group(3) or "0")[:6].ljust(6, "0")
    try:
        return datetime.strptime(
            f"{m.group(1)}T{m.group(2)}.{frac}", "%Y-%m-%dT%H:%M:%S.%f"
        ).replace(tzinfo=timezone.utc)
    except ValueError:
        return None


@dataclass
class Rec:
    """One normalized log record. `raw` preserves the original JSON dict."""

    index: int                      # position within the source file (as exported)
    source_file: str                # basename of the file the record came from
    oid: Optional[str] = None       # _id.$oid hex string when present
    user_id: Optional[str] = None
    session_id: str = ""            # source_file + user_id
    event_type: Optional[str] = None
    event_key: Optional[str] = None
    scene: Optional[str] = None
    version: Optional[str] = None   # game build version string
    ts: Optional[datetime] = None   # client timestamp
    server_ts: Optional[datetime] = None
    data: Any = None                # raw `data` payload (usually a dict)
    raw: dict = field(default_factory=dict)

    def ref(self) -> str:
        """Stable human-checkable pointer back to the raw record."""
        oid = self.oid or "?"
        ts = self.raw.get("timestamp", "?")
        return f"{self.source_file}[{self.index}] _id={oid} ts={ts}"


@dataclass
class Finding:
    """One audit result item, always with evidence."""

    status: str                     # PASS / WARNING / FAIL / NOT_TESTED / INFO
    severity: str                   # Critical / High / Medium / Low / Info / NotTested
    category: str                   # schema, values, scenes, frequency, sequence, ...
    summary: str
    event_type: Optional[str] = None
    fld: Optional[str] = None       # dotted data path when field-specific
    observed: str = ""
    expected: str = ""
    evidence: str = ""              # counts / scenes / sessions supporting the claim
    examples: list = field(default_factory=list)  # Rec.ref() strings
    spec_source: str = ""           # where the expectation came from

    def sort_key(self):
        return (_SEV_ORDER.get(self.severity, 9), self.category,
                self.event_type or "", self.fld or "", self.summary)

    def to_row(self) -> dict:
        return {
            "status": self.status,
            "severity": self.severity,
            "category": self.category,
            "event_type": self.event_type or "",
            "field": self.fld or "",
            "summary": self.summary,
            "observed": self.observed,
            "expected": self.expected,
            "evidence": self.evidence,
            "examples": " | ".join(self.examples[:5]),
            "spec_source": self.spec_source,
        }


def fmt_seconds(s: Optional[float]) -> str:
    """Human-readable duration."""
    if s is None:
        return "?"
    if s < 60:
        return f"{s:.1f}s"
    if s < 3600:
        return f"{int(s // 60)}m {int(s % 60)}s"
    return f"{int(s // 3600)}h {int((s % 3600) // 60)}m"
