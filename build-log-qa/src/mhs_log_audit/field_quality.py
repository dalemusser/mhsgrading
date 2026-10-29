"""Per-player data-quality metrics for classroom / field-test exports.

The weekly audit (`pipeline.run_audit`) answers "is this build's logging
implemented as specified?" for one internal playthrough. A classroom export
raises questions an internal playthrough never does, and they have to be
answered per student:

* offline buffering on school devices — records uploaded long after they
  happened. In builds that use the legacy record envelope (no `session_id`)
  the `data` payload of a late upload can be stale (serialised at upload time),
  so only `eventKey`, `eventType`, `sceneName` and the timestamps are reliable;
* transport loss and resends — from build 20261005 every record carries a
  `session_id` / `seq` envelope (seq starts at 1 per session), so missing
  sequence numbers measure loss directly and repeated `entry_id`s are resends;
* the DialogueEvent eventKey-vs-payload agreement the dashboard depends on;
* crashes, debug-menu use and how far the student actually got (context for
  every absence finding).

`player_metrics` returns one flat dict per player; `transport_rows` returns one
row per `session_id`. Both work on the normalized `Rec` list from the loader.
"""

from __future__ import annotations

import json
from collections import Counter
from typing import Dict, List, Optional

from .config import scene_to_units
from .model import Rec

STALE_DELAY_S = 5.0      # server-minus-client delay beyond which a legacy-envelope
                         # payload may be stale (observed: <=5 s 97% eventKey/payload
                         # agreement, 5-30 s 56%, >30 s <10%)
ACTIVE_GAP_S = 300.0     # gaps longer than this are not counted as active play
HOUR, DAY = 3600.0, 86400.0


def _int(v) -> Optional[int]:
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _has_envelope(rec: Rec) -> bool:
    return "session_id" in rec.raw


def _dialogue_key_payload(rec: Rec):
    """(key_conv, key_node, data_conv, data_node) for a keyed dialogue node."""
    parts = (rec.event_key or "").split(":")
    if len(parts) != 3 or parts[0] != "DialogueNodeEvent":
        return None
    data = rec.data if isinstance(rec.data, dict) else {}
    return (_int(parts[1]), _int(parts[2]),
            _int(data.get("conversationId")), _int(data.get("nodeId")))


def _seq_holes(seqs: Counter) -> List[tuple]:
    present = sorted(seqs)
    holes = []
    for a, b in zip(present, present[1:]):
        if b > a + 1:
            holes.append((a + 1, b - 1))
    if present and present[0] > 1:          # seq starts at 1 in every session
        holes.insert(0, (1, present[0] - 1))
    return holes


def transport_rows(records: List[Rec]) -> List[dict]:
    """One row per envelope session: span, loss, resends, recovered records."""
    sessions: Dict[str, dict] = {}
    for r in records:
        sid = r.raw.get("session_id")
        if not isinstance(sid, str):
            continue
        s = sessions.setdefault(sid, {"seqs": Counter(), "versions": Counter(),
                                      "first": None, "last": None,
                                      "recovered": 0, "scenes": Counter()})
        seq = _int(r.raw.get("seq"))
        if seq is not None:
            s["seqs"][seq] += 1
        s["versions"][r.version] += 1
        s["scenes"][r.scene] += 1
        if r.raw.get("recovered") is True:
            s["recovered"] += 1
        if r.ts:
            s["first"] = r.ts if s["first"] is None or r.ts < s["first"] else s["first"]
            s["last"] = r.ts if s["last"] is None or r.ts > s["last"] else s["last"]
    rows = []
    for sid, s in sessions.items():
        seqs = s["seqs"]
        holes = _seq_holes(seqs)
        top = max(seqs) if seqs else 0
        rows.append({
            "session_id": sid,
            "user_id": records[0].user_id if records else "",
            "version": "/".join(v for v, _ in s["versions"].most_common()),
            "first_ts": s["first"].isoformat() if s["first"] else "",
            "last_ts": s["last"].isoformat() if s["last"] else "",
            "minutes": round((s["last"] - s["first"]).total_seconds() / 60, 1)
            if s["first"] and s["last"] else "",
            "records": sum(seqs.values()),
            "max_seq": top,
            "missing_seq": sum(b - a + 1 for a, b in holes),
            "holes": "; ".join(f"{a}-{b}" if a != b else str(a) for a, b in holes),
            "resends": sum(c - 1 for c in seqs.values() if c > 1),
            "recovered": s["recovered"],
            "main_scene": s["scenes"].most_common(1)[0][0] if s["scenes"] else "",
        })
    rows.sort(key=lambda x: x["first_ts"])
    return rows


def player_metrics(records: List[Rec]) -> dict:
    """Flat per-player data-quality facts (see module docstring)."""
    game = [r for r in records if r.event_type != "crash"]
    crash = [r for r in records if r.event_type == "crash"]
    m: dict = {"records": len(records)}

    builds = Counter(r.version or "?" for r in game)
    m["builds"] = "; ".join(f"{v}: {c}" for v, c in builds.most_common())
    m["primary_build"] = builds.most_common(1)[0][0] if builds else ""
    m["n_builds"] = len(builds)
    m["event_types"] = ";".join(sorted({r.event_type or "?" for r in records}))
    envelope = [r for r in game if _has_envelope(r)]
    m["envelope_records"] = len(envelope)
    m["legacy_records"] = len(game) - len(envelope)

    # ---- when / how much -------------------------------------------------
    ts = sorted(r.ts for r in game if r.ts)
    m["first_ts"] = ts[0].isoformat() if ts else ""
    m["last_ts"] = ts[-1].isoformat() if ts else ""
    m["active_days"] = len({t.date() for t in ts})
    m["active_minutes"] = round(sum(
        g for g in ((b - a).total_seconds() for a, b in zip(ts, ts[1:]))
        if g <= ACTIVE_GAP_S) / 60, 1)
    m["launches"] = sum(1 for r in game if r.event_type == "gameStartEvent")
    m["envelope_sessions"] = len({r.raw["session_id"] for r in envelope})

    # ---- progress (context for absence findings) ---------------------------
    units_seen = sorted({u for r in game for u in scene_to_units(r.scene or "")})
    units_ended = sorted({u for u in (_int((r.data or {}).get("Unit"))
                                      for r in game if r.event_type == "EndOfUnit"
                                      and isinstance(r.data, dict)) if u is not None})
    m["units_seen"] = ",".join(map(str, units_seen))
    m["units_ended"] = ",".join(map(str, units_ended))
    m["furthest_unit"] = max(units_seen) if units_seen else 0
    m["quests_finished"] = len({r.event_key for r in game
                                if r.event_type == "questEvent"
                                and (r.event_key or "").startswith("questFinishEvent")})

    # ---- timestamps / upload delay ---------------------------------------
    delays = [(r, (r.server_ts - r.ts).total_seconds())
              for r in game if r.ts and r.server_ts]
    m["no_client_ts"] = sum(1 for r in records if r.ts is None)
    m["delayed_over_5s"] = sum(1 for _, d in delays if d > STALE_DELAY_S)
    m["delayed_over_1h"] = sum(1 for _, d in delays if d > HOUR)
    m["delayed_over_1d"] = sum(1 for _, d in delays if d > DAY)
    m["max_delay_h"] = round(max((d for _, d in delays), default=0) / HOUR, 2)
    m["client_ahead_over_5s"] = sum(1 for _, d in delays if d < -STALE_DELAY_S)
    stale = [r for r, d in delays if d > STALE_DELAY_S and not _has_envelope(r)]
    m["stale_risk_records"] = len(stale)
    m["stale_risk_pct"] = round(100 * len(stale) / max(len(game), 1), 2)  # of ALL records

    # ---- DialogueEvent eventKey vs payload -------------------------------
    delay_of = {id(r): d for r, d in delays}
    keyed = mism = mism_late = mism_key0 = 0
    for r in game:
        if r.event_type != "DialogueEvent" or not r.event_key:
            continue
        kp = _dialogue_key_payload(r)
        if kp is None:
            continue
        keyed += 1
        if kp[:2] == kp[2:]:
            continue
        mism += 1
        if delay_of.get(id(r), 0) > STALE_DELAY_S:
            mism_late += 1
        elif kp[1] == 0 and kp[0] == kp[2]:
            mism_key0 += 1
    m["dialogue_keyed"] = keyed
    m["dialogue_mismatch"] = mism
    m["dialogue_mismatch_late_upload"] = mism_late
    m["dialogue_mismatch_key_node0"] = mism_key0
    m["dialogue_mismatch_other"] = mism - mism_late - mism_key0

    # ---- transport envelope ------------------------------------------------
    trows = transport_rows(records)
    m["seq_expected"] = sum(t["max_seq"] for t in trows)
    m["seq_missing"] = sum(t["missing_seq"] for t in trows)
    m["sessions_with_loss"] = sum(1 for t in trows if t["missing_seq"])
    m["resends"] = sum(t["resends"] for t in trows)
    m["recovered_records"] = sum(1 for r in game if r.raw.get("recovered") is True)

    # ---- exact duplicates not explained by an envelope resend --------------
    groups: Counter = Counter()
    seen_entries: set = set()
    for r in game:
        entry = r.raw.get("entry_id")
        if entry is not None:
            if entry in seen_entries:        # resend — counted in `resends`
                continue
            seen_entries.add(entry)
        try:
            dk = json.dumps(r.data, sort_keys=True, ensure_ascii=False)
        except TypeError:
            dk = repr(r.data)
        groups[(r.event_type, r.scene, r.raw.get("timestamp"), dk)] += 1
    m["exact_dup_puzzle_piece"] = sum(c - 1 for k, c in groups.items()
                                      if c > 1 and k[0] == "PuzzlePieceVisibleEvent")
    m["exact_dup_other"] = sum(c - 1 for k, c in groups.items()
                               if c > 1 and k[0] != "PuzzlePieceVisibleEvent")

    # ---- crashes / debug ---------------------------------------------------
    ctypes = Counter((r.data or {}).get("type", "?") for r in crash
                     if isinstance(r.data, dict))
    m["crash_runtime_error"] = ctypes.get("runtime_error", 0)
    m["crash_load_stalled"] = ctypes.get("load_stalled", 0)
    m["crash_unhandled_rejection"] = ctypes.get("unhandled_rejection", 0)
    m["debug_menu_opened"] = sum(1 for r in game if r.event_type == "DEBUGMenu"
                                 and isinstance(r.data, dict)
                                 and r.data.get("isOpened") is True)
    return m


def unit_rows(records: List[Rec]) -> List[dict]:
    """One row per game unit the player entered: volume, time, builds, whether
    EndOfUnit fired, the late-upload (stale-payload) share, and envelope
    records lost inside the unit (a seq hole is attributed to the unit of the
    record just before it). Behaviour analysis is usually done per unit, and
    players switch builds mid-unit, so data quality is reported per unit too."""
    game = [r for r in records if r.event_type != "crash"]
    ended = {u for u in (_int((r.data or {}).get("Unit")) for r in game
                         if r.event_type == "EndOfUnit" and isinstance(r.data, dict))
             if u is not None}
    by_unit: Dict[int, List[Rec]] = {}
    for r in game:
        units = scene_to_units(r.scene or "")
        if len(units) == 1:
            by_unit.setdefault(units[0], []).append(r)

    lost: Counter = Counter()
    sessions: Dict[str, Dict[int, Rec]] = {}
    for r in game:
        sid, seq = r.raw.get("session_id"), _int(r.raw.get("seq"))
        if isinstance(sid, str) and seq is not None:
            sessions.setdefault(sid, {})[seq] = r
    for seqmap in sessions.values():
        for a, b in _seq_holes(Counter(seqmap)):
            before = seqmap.get(a - 1)
            units = scene_to_units(before.scene or "") if before else []
            lost[units[0] if len(units) == 1 else 0] += b - a + 1

    rows = []
    for u in sorted(by_unit):
        rs = by_unit[u]
        ts = sorted(r.ts for r in rs if r.ts)
        stale = sum(1 for r in rs if not _has_envelope(r) and r.ts and r.server_ts
                    and (r.server_ts - r.ts).total_seconds() > STALE_DELAY_S)
        builds = Counter(r.version or "?" for r in rs)
        rows.append({
            "unit": u,
            "status": "finished" if u in ended else "played, not finished",
            "records": len(rs),
            "first_ts": ts[0].isoformat() if ts else "",
            "last_ts": ts[-1].isoformat() if ts else "",
            "active_days": len({t.date() for t in ts}),
            "active_minutes": round(sum(
                g for g in ((b - a).total_seconds() for a, b in zip(ts, ts[1:]))
                if g <= ACTIVE_GAP_S) / 60, 1),
            "builds": "; ".join(f"{v}: {c}" for v, c in builds.most_common()),
            "envelope_pct": round(100 * sum(1 for r in rs if _has_envelope(r)) / len(rs), 1),
            "quests_finished": len({r.event_key for r in rs if r.event_type == "questEvent"
                                    and (r.event_key or "").startswith("questFinishEvent")}),
            "stale_risk_records": stale,
            "stale_risk_pct": round(100 * stale / len(rs), 2),
            "lost_records": lost.get(u, 0),
        })
    return rows
