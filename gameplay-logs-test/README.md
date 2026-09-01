# MHS Gameplay-Log Audit Pipeline (`gameplay-logs-test/`)

A reusable, configuration-driven QA/audit system for the weekly Mission
HydroSci gameplay-log investigation. One command turns a new build's log dump
into a Markdown examination report plus machine-readable evidence, and
compares the build against a previous one.

```text
gameplay-logs-test/
├── config/
│   ├── event_expectations.yaml   # EXPECTED logging behavior per eventType (edit weekly as needed)
│   └── coverage/<build-id>.yaml  # what content each playthrough exercised (edit weekly)
├── src/mhs_log_audit/            # the pipeline modules (rarely need edits)
│   ├── loader.py      # robust load + normalize (JSON array / object / NDJSON, dirs)
│   ├── profiling.py   # generic recursive field/value profiling + schema consistency
│   ├── inventory.py   # event inventory tables
│   ├── frequency.py   # interval stats, cadence checks, bursts, gaps
│   ├── temporal.py    # scene timeline, ordering diagnostics, pairing/sequence rules
│   ├── duplicates.py  # exact + near-duplicate detection
│   ├── checks.py      # all config-driven expectation/coverage/cross-event checks
│   ├── regression.py  # snapshot + build-vs-build diff
│   ├── examples.py    # representative raw records
│   ├── report.py      # CSV/JSON exports + audit-report.md
│   └── pipeline.py    # run_audit() orchestration
├── scripts/audit_logs.py         # CLI entry point
├── tests/                        # synthetic-data unit tests (no real logs needed)
└── reports/<build-id>/           # generated outputs, one folder per build
```

**Requirements:** Python 3.10+ with `pandas` and `pyyaml`
(`pip install pandas pyyaml`). Raw logs are read-only — the pipeline never
modifies anything under `playthrough-logs-and-results/`.

---

## Weekly workflow (the short version)

When a new build's log arrives (example: the 08-25-26 build):

1. **Drop the log** in a dated folder:
   `playthrough-logs-and-results/08-25-26/wenyi082526-1.stratalog.logdata.json`
   (one or more `.json`/`.jsonl` files; the folder is passed to `--input`).
2. **Write the coverage manifest** `config/coverage/08-25-26.yaml` — which
   units you actually played (`complete` / `partial` / `skipped`) plus notes
   ("stuck at Soil Key Puzzle", "jumped to Unit 4 via debug menu"). If you
   skip this, coverage is *inferred* from scene names and clearly labeled as
   inferred — but the manifest makes NOT_TESTED vs FAIL decisions much better.
3. **Run one command** (from the repository root):

   ```bash
   python gameplay-logs-test/scripts/audit_logs.py \
       --input playthrough-logs-and-results/08-25-26 \
       --build-id 08-25-26 \
       --baseline gameplay-logs-test/reports/08-13-26
   ```

   `--baseline` points at **last week's report folder** (its `snapshot.json`
   is used). Omit it for the first build ever; regression is skipped
   gracefully. `--config`/`--coverage`/`--output` have sensible defaults
   (see `--help`).
4. **Read `reports/08-25-26/audit-report.md`** — start with section 2
   (Executive Summary) and section 11 (Recommended Follow-Up), then section 4
   (what changed vs last week).
5. When done, the new `reports/08-25-26/` folder automatically becomes the
   baseline candidate for next week's run.

The CLI exits with code 1 if any FAIL finding exists (handy for scripting).

---

## What gets generated

| File | What it is / when to open it |
| ---- | ---------------------------- |
| `audit-report.md` | The human report (11 sections). Read this first. |
| `audit_results.json` | Every finding with status/severity/evidence — machine-readable. |
| `snapshot.json` | Normalized build fingerprint; used as `--baseline` next week. |
| `event_examples.json` | Raw example records per event type (first/last/typical/rare variant/per action value) — for validating any claim against real JSON. |
| `csv/event_type_summary.csv` | Inventory: counts, %, sessions, time span, scenes, fields. |
| `csv/event_scene_summary.csv` | Per event x scene counts and time spans. |
| `csv/event_field_summary.csv` | Per field: presence, types, nulls, empty strings, cardinality. |
| `csv/event_unique_values.csv` | Observed unique values per categorical field. |
| `csv/event_frequency_summary.csv` | Interval percentiles, bursts, long gaps. |
| `csv/scene_timeline.csv` | Chronological scene runs with durations ("how long in Unit 2?"). |
| `csv/findings.csv` | All findings as a flat table. |
| `csv/duplicate_events.csv` | The actual suspicious duplicate records. |
| `csv/regression_diff.csv` | Every build-vs-baseline difference (when a baseline was given). |

Every finding carries references like
`wenyi082526-1.stratalog.logdata.json[5986] _id=6a8dc8bd... ts=2026-08-25T16:54:21.899Z`
— file, position in the file, Mongo `_id`, and client timestamp — so any
claim can be traced back to the raw record.

---

## How to read the statuses

| Status | Meaning |
| ------ | ------- |
| `PASS` | Observation matches the configured expectation. |
| `FAIL` | Observation violates the expectation (e.g. a required field is missing). Developer-facing. |
| `WARNING` | Suspicious and worth review, but plausibly explainable (duplicates, close-without-open, cadence drift, absent event in *played* content). |
| `NOT_TESTED` | No conclusion possible — the relevant content was not exercised this playthrough (driven by the coverage manifest). |
| `INFO` | Descriptive: new values ("specification review required"), long gaps, unmatched opens at session end, ordering diagnostics, known issues being tracked. |

Severity (`Critical/High/Medium/Low/Info/NotTested`) ranks findings within a
status. Two principles baked in everywhere:

* **Absence ≠ failure.** An expected event that never fired is only a WARNING
  if the coverage manifest says its content was actually played; otherwise
  NOT_TESTED.
* **Unexpected values are surfaced, never hidden or auto-merged.** A new
  `actionType` is an INFO "specification review required" item, not a FAIL —
  it is usually exactly the design change you're looking for. Naming variants
  (`boxID`/`boxId`, `Started`/`started`) are reported, not normalized.

---

## Updating expectations when the game changes

All expectations live in `config/event_expectations.yaml` — one entry per
`eventType`, using a small rule vocabulary (documented at the top of
`src/mhs_log_audit/config.py`): `expected_scenes`, `required_data_fields`,
`conditional_fields`, `allowed_values`, `field_types`, `continuous`
(cadence), `pairing` / `start_finish` (sequences), `event_key` (format
checks), `units` (for coverage gating), `semantics`, `known_issues`.

**Example — the TopographicMapEvent redesign.** The 08-25-26 audit reports
new values `Waypoint` / `WaypointMoveEvent` / `WaypointSetEvent` /
`WaypointResetEvent` as spec-review items, because the config still encodes
the documented 08-13 design (`waypoint` / `dragEnd`). Once the developers
confirm the new design is intentional, update the entry:

```yaml
  TopographicMapEvent:
    allowed_values:
      featureUsed: [Map, Waypoint]
      actionType: [MapOpenEvent, MapCloseEvent,
                   WaypointMoveEvent, WaypointSetEvent, WaypointResetEvent]
```

and the items become PASS next week — while a *reversion* to the old values
would then be flagged.

**Adding a brand-new event type** (e.g. `SolarStillDesignEvent` appeared in
08-25-26): unknown events are always profiled automatically and marked
"no expectation rules configured". To promote one to a checked event, add an
entry with whatever rules the documentation supports; start minimal:

```yaml
  SomeNewEvent:
    purpose: one line on what it logs
    spec_source: where the expectation comes from
    units: [3]
    required_data_fields: [actionType]
```

`cross_event_rules` (top level) express "if X happened, Y must appear in the
same session" consistency checks. `thresholds` tunes near-duplicate/burst/gap
sensitivity.

---

## Coverage manifests

`config/coverage/<build-id>.yaml`:

```yaml
build: "08-25-26"
tested_content:
  Unit1: complete
  Unit2: partial
  Unit4: skipped
notes:
  - "Unable to progress beyond the Soil Key Puzzle in Unit 2."
```

The audit uses `tested_content` to gate absent-event decisions (an event's
`units:` list in the expectations file says which units it belongs to). The
`notes` are echoed in the report for the development team.

---

## Comparing builds

* Weekly: `--baseline gameplay-logs-test/reports/<last-week>`.
* Against a known-good build instead: point `--baseline` at that build's
  report folder (or directly at its `snapshot.json`).
* Against raw logs that were never audited: `--baseline path/to/old/logs`
  also works — a snapshot is computed on the fly.

The diff covers: new/removed event types, new/removed scenes, added/removed
fields, type changes, new/removed categorical values, >3x volume changes and
>2x cadence changes — all as review candidates, never auto-judged as defects.

---

## Tests

```bash
cd gameplay-logs-test/tests
python -m unittest discover
```

41 tests, all on synthetic records (missing fields, type drift, unknown
events, duplicates, start-without-finish, new values, skipped coverage,
cadence, no-baseline runs, end-to-end pipeline). Real logs are not required.

---

## Design notes

* **Chronology** uses the client `timestamp` (tie-broken by `_id`): the raw
  export is ordered newest-first and `_id` (arrival) order disagrees with
  client time for ~2.6% of adjacent pairs (batched uploads). The audit
  reports this disagreement as an INFO diagnostic each run.
* **Session** = one log file x one `user_id`. Multi-file and multi-user
  inputs are supported; sequence/frequency logic never crosses sessions.
* The loader tolerates JSON arrays, wrapped objects, single records, and
  NDJSON; malformed entries become loader warnings, never crashes.
* Everything event-specific lives in YAML. The Python is generic and should
  only need edits for genuinely new *kinds* of checks.
