"""Robust gameplay-log loading and normalization.

Handles the formats seen in this repository plus realistic variations:
  * a JSON array of records (the current MongoDB export format);
  * a JSON object wrapping a record list (keys like "records"/"logdata");
  * a single JSON object record;
  * JSON Lines / NDJSON (one record per line);
  * one file or a directory of files (each file = one export).

Raw records are never modified; normalization builds `Rec` views on top.
Malformed entries are collected as load warnings instead of crashing.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List, Optional

from .model import Rec, parse_timestamp

_LIST_WRAPPER_KEYS = ("records", "logdata", "logs", "data", "items", "documents")


@dataclass
class LoadResult:
    records: List[Rec] = field(default_factory=list)
    files: List[str] = field(default_factory=list)         # basenames, load order
    warnings: List[str] = field(default_factory=list)
    skipped_records: int = 0

    @property
    def sessions(self) -> List[str]:
        return sorted({r.session_id for r in self.records})

    @property
    def users(self) -> List[str]:
        return sorted({r.user_id for r in self.records if r.user_id})

    @property
    def versions(self) -> List[str]:
        return sorted({r.version for r in self.records if r.version})


def _extract_oid(rec: dict) -> Optional[str]:
    v = rec.get("_id")
    if isinstance(v, dict):
        v = v.get("$oid")
    return v if isinstance(v, str) else None


def _extract_server_ts(rec: dict):
    v = rec.get("serverTimestamp")
    if isinstance(v, dict):
        v = v.get("$date")
    return parse_timestamp(v)


def normalize_record(raw: Any, index: int, source_file: str,
                     warnings: List[str]) -> Optional[Rec]:
    """Build a Rec from one raw JSON value; None (plus a warning) if unusable."""
    if not isinstance(raw, dict):
        warnings.append(
            f"{source_file}[{index}]: record is {type(raw).__name__}, not an object — skipped")
        return None
    ts = parse_timestamp(raw.get("timestamp"))
    if raw.get("timestamp") is not None and ts is None:
        warnings.append(
            f"{source_file}[{index}]: unparseable timestamp {raw.get('timestamp')!r}")
    user = raw.get("user_id") if isinstance(raw.get("user_id"), str) else None
    return Rec(
        index=index,
        source_file=source_file,
        oid=_extract_oid(raw),
        user_id=user,
        session_id=f"{source_file}:{user or '?'}",
        event_type=raw.get("eventType") if isinstance(raw.get("eventType"), str) else None,
        event_key=raw.get("eventKey") if isinstance(raw.get("eventKey"), str) else None,
        scene=raw.get("sceneName") if isinstance(raw.get("sceneName"), str) else None,
        version=raw.get("version") if isinstance(raw.get("version"), str) else None,
        ts=ts,
        server_ts=_extract_server_ts(raw),
        data=raw.get("data"),
        raw=raw,
    )


def _parse_file(path: Path, warnings: List[str]) -> List[Any]:
    """Return the list of raw record values found in one file."""
    text = path.read_text(encoding="utf-8-sig")
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        # fall back to JSON Lines
        rows: List[Any] = []
        n_bad = 0
        for i, line in enumerate(text.splitlines()):
            line = line.strip().rstrip(",")
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                n_bad += 1
        if rows:
            if n_bad:
                warnings.append(f"{path.name}: {n_bad} unparseable JSONL line(s) skipped")
            return rows
        warnings.append(f"{path.name}: not valid JSON or JSON Lines — file skipped")
        return []
    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict):
        for key in _LIST_WRAPPER_KEYS:
            if isinstance(parsed.get(key), list):
                warnings.append(f"{path.name}: records taken from wrapper key {key!r}")
                return parsed[key]
        if "eventType" in parsed or "_id" in parsed:
            return [parsed]  # single-record file
        warnings.append(f"{path.name}: JSON object with no recognizable record list — skipped")
        return []
    warnings.append(f"{path.name}: unexpected top-level {type(parsed).__name__} — skipped")
    return []


def _sort_chronological(records: List[Rec]) -> List[Rec]:
    """Chronological order = client timestamp, tie-broken by _id then file order.

    The raw exports are ordered newest-first and `_id` order does not fully
    agree with client timestamps (batched uploads), so the client timestamp is
    the primary key for gameplay chronology.
    """
    def key(r: Rec):
        ts = r.ts.timestamp() if r.ts else float("inf")
        return (ts, r.oid or "", r.source_file, r.index)
    return sorted(records, key=key)


def load_logs(input_path: str) -> LoadResult:
    """Load one log file or every *.json/*.jsonl/*.ndjson file in a directory."""
    result = LoadResult()
    root = Path(input_path)
    if root.is_dir():
        paths = sorted(p for p in root.iterdir()
                       if p.suffix.lower() in (".json", ".jsonl", ".ndjson"))
        if not paths:
            result.warnings.append(f"no .json/.jsonl/.ndjson files found in {root}")
    elif root.is_file():
        paths = [root]
    else:
        result.warnings.append(f"input path not found: {root}")
        paths = []

    for path in paths:
        raw_rows = _parse_file(path, result.warnings)
        result.files.append(path.name)
        for i, raw in enumerate(raw_rows):
            rec = normalize_record(raw, i, path.name, result.warnings)
            if rec is None:
                result.skipped_records += 1
            else:
                result.records.append(rec)

    result.records = _sort_chronological(result.records)
    return result
