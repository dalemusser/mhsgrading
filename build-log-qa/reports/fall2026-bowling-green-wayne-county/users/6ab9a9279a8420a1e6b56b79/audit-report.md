# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b79

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b79
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b79.jsonl
- **Records:** 12010 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b79
- **Time span:** 2026-10-06T18:44:42.148000+00:00 .. 2026-10-19T00:06:29.646000+00:00 (293h 21m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b79\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 12010 records, 10 scenes.
- Findings: **0 FAIL**, **29 WARNING**, 96 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3046 | 25.36 | 1 | 4 | 0 | 2026-10-14T21:06:29.867000+00:00 | 2026-10-16T18:40:32.994000+00:00 | 45h 34m |
| InputEvent | 3023 | 25.17 | 1 | 9 | 0 | 2026-10-06T18:45:29.242000+00:00 | 2026-10-19T00:06:29.646000+00:00 | 293h 21m |
| DialogueEvent | 2343 | 19.51 | 1 | 9 | 1459 | 2026-10-06T18:45:45.815000+00:00 | 2026-10-19T00:06:18.580000+00:00 | 293h 20m |
| PlayerPositionEvent | 2199 | 18.31 | 1 | 9 | 0 | 2026-10-06T18:45:25.828000+00:00 | 2026-10-19T00:06:22.376000+00:00 | 293h 20m |
| argumentationNodeEvent | 469 | 3.91 | 1 | 5 | 0 | 2026-10-14T19:14:46.079000+00:00 | 2026-10-18T23:52:53.035000+00:00 | 100h 38m |
| ObjectInterEvent | 308 | 2.56 | 1 | 9 | 0 | 2026-10-06T18:53:38.766000+00:00 | 2026-10-19T00:06:29.646000+00:00 | 293h 12m |
| TopographicMapEvent | 189 | 1.57 | 1 | 2 | 0 | 2026-10-14T21:06:57.907000+00:00 | 2026-10-16T00:41:30.964000+00:00 | 27h 34m |
| Soil Key Puzzle | 99 | 0.82 | 1 | 3 | 0 | 2026-10-14T21:05:57.130000+00:00 | 2026-10-16T00:54:18.969000+00:00 | 27h 48m |
| questEvent | 81 | 0.67 | 1 | 9 | 81 | 2026-10-06T18:45:45.787000+00:00 | 2026-10-19T00:02:06.698000+00:00 | 293h 16m |
| argumentationAnswerEvent | 45 | 0.37 | 1 | 5 | 0 | 2026-10-14T19:15:08.593000+00:00 | 2026-10-18T23:53:06.169000+00:00 | 100h 37m |
| soilMachine | 35 | 0.29 | 1 | 1 | 0 | 2026-10-16T01:17:24.521000+00:00 | 2026-10-16T01:30:46.313000+00:00 | 13m 21s |
| WaterChamberEvent | 26 | 0.22 | 1 | 1 | 0 | 2026-10-16T18:38:33.138000+00:00 | 2026-10-16T18:53:20.159000+00:00 | 14m 47s |
| DEBUGMenu | 24 | 0.2 | 1 | 9 | 0 | 2026-10-06T18:45:25.810000+00:00 | 2026-10-18T23:45:54.098000+00:00 | 293h 0m |
| DaniEvent | 24 | 0.2 | 1 | 3 | 0 | 2026-10-06T19:10:21.815000+00:00 | 2026-10-16T00:35:36.470000+00:00 | 221h 25m |
| TerasGardenBox | 19 | 0.16 | 1 | 1 | 0 | 2026-10-16T01:52:44.880000+00:00 | 2026-10-16T01:54:33.463000+00:00 | 1m 48s |
| argumentationEvent | 19 | 0.16 | 1 | 5 | 0 | 2026-10-06T19:17:15.078000+00:00 | 2026-10-18T23:53:06.209000+00:00 | 292h 35m |
| gameWindowFocusEvent | 16 | 0.13 | 1 | 4 | 0 | 2026-10-06T18:44:42.148000+00:00 | 2026-10-18T23:45:54.258000+00:00 | 293h 1m |
| SolarStillDesignEvent | 13 | 0.11 | 1 | 1 | 0 | 2026-10-18T23:59:01.607000+00:00 | 2026-10-18T23:59:29.313000+00:00 | 27.7s |
| gameStartEvent | 10 | 0.08 | 1 | 1 | 0 | 2026-10-06T18:44:42.149000+00:00 | 2026-10-18T23:45:54.258000+00:00 | 293h 1m |
| argumentationToolEvent | 7 | 0.06 | 1 | 1 | 0 | 2026-10-06T19:17:11.535000+00:00 | 2026-10-14T20:54:14.391000+00:00 | 193h 37m |
| gameWindowUnfocusEvent | 7 | 0.06 | 1 | 3 | 0 | 2026-10-06T18:55:44.081000+00:00 | 2026-10-16T01:20:49.936000+00:00 | 222h 25m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-14T20:57:50.999000+00:00 | 2026-10-19T00:06:29.635000+00:00 | 99h 8m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-16T18:33:09.719000+00:00 | 2026-10-18T23:46:03.878000+00:00 | 53h 12m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 50091.217s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.666s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.064s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.042s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.377s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 14.071s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 149.697s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 41.329s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 95787.08s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 14518.165s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2409.9s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1793.718s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.452s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 24 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 9.0x vs baseline. 
  - Observed: 45 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,B,5,I; B,1,II; B,A,1,II; C,2,II; C,3,II; C,4,II; C,A,2,II; C,D,3,II; D,1,I; D,1,II; D,2,II; D,3,4,II; D,3,II; D,4,II; D,A,1,II; D,C,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.4x vs baseline. 
  - Observed: 469 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 7 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 7.0x vs baseline. 
  - Observed: 35 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[198] _id=6ac54447de269131f9b7153d ts=2026-10-06T18:56:07.1880000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[259] _id=6ac5456fde269131f9b7297c ts=2026-10-06T19:01:03.1300000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[312] _id=6ac5462cde269131f9b73acd ts=2026-10-06T19:04:12.3040000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[4] _id=6ac5419ade269131f9b6cedd ts=2026-10-06T18:44:42.1490000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[504] _id=6acfd423de269131f9d84999 ts=2026-10-14T19:12:34.2440000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[663] _id=6acfeb2cde269131f9d96928 ts=2026-10-14T20:50:52.0330000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[3] _id=6ac5419ade269131f9b6ced7 ts=2026-10-06T18:44:42.1480000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[195] _id=6ac5443dde269131f9b71481 ts=2026-10-06T18:55:56.6840000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[414] _id=6ac54808de269131f9b7706b ts=2026-10-06T19:12:07.8100000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[189] _id=6ac54430de269131f9b713cd ts=2026-10-06T18:55:44.0810000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[413] _id=6ac54803de269131f9b7702b ts=2026-10-06T19:12:03.4060000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[860] _id=6acfecaade269131f9d96b1c ts=2026-10-14T20:57:14.3850000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 33 of 189 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[1045] _id=6acfeef2de269131f9d96c6c ts=2026-10-14T21:06:57.9070000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[1049] _id=6acfef04de269131f9d96c7f ts=2026-10-14T21:07:15.7590000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[1529] _id=6acfefecde269131f9d97148 ts=2026-10-14T21:11:07.4870000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3045 | 0.0 | 0.064 | 53.873 | 2.435 | 78206.41 | 1.11 | 1405 | 6 |
| InputEvent | 3022 | 0.0 | 1.666 | 349.457 | 23.773 | 691017.109 | 0.17 | 38 | 8 |
| DialogueEvent | 2342 | 0.0 | 4.419 | 450.911 | 34.593 | 690956.668 | 0.13 | 672 | 6 |
| PlayerPositionEvent | 2187 | 9.73 | 10.001 | 455.569 | 10.177 | 690917.812 | 0.13 | 0 | 5 |
| argumentationNodeEvent | 468 | 0.01 | 0.68 | 774.117 | 10.881 | 252136.071 | 0.08 | 51 | 5 |
| ObjectInterEvent | 307 | 0.0 | 11.369 | 3438.342 | 400.851 | 691051.892 | 0.02 | 3 | 8 |
| TopographicMapEvent | 188 | 0.019 | 7.377 | 528.048 | 142.84 | 75344.056 | 0.11 | 2 | 6 |
| Soil Key Puzzle | 98 | 0.15 | 2.042 | 1021.447 | 42.902 | 77799.919 | 0.06 | 0 | 4 |
| questEvent | 80 | 0.0 | 200.995 | 13197.261 | 14930.119 | 691015.239 | 0.0 | 15 | 13 |
| argumentationAnswerEvent | 44 | 0.682 | 14.071 | 8233.581 | 6015.142 | 252173.345 | 0.01 | 0 | 5 |
| soilMachine | 34 | 0.099 | 2.452 | 23.582 | 154.128 | 229.893 | 2.54 | 0 | 0 |
| WaterChamberEvent | 25 | 5.174 | 25.957 | 35.481 | 98.503 | 121.792 | 1.69 | 0 | 0 |
| DEBUGMenu | 23 | 8.586 | 751.058 | 45862.099 | 180207.732 | 692828.083 | 0.0 | 0 | 13 |
| DaniEvent | 23 | 0.94 | 6.688 | 34657.159 | 87189.094 | 698449.661 | 0.0 | 0 | 3 |
| TerasGardenBox | 18 | 0.231 | 3.072 | 6.032 | 18.774 | 22.769 | 9.95 | 0 | 0 |
| argumentationEvent | 18 | 0.03 | 149.697 | 58519.507 | 317976.032 | 691047.029 | 0.0 | 2 | 6 |
| gameWindowFocusEvent | 15 | 121.498 | 2409.9 | 70324.807 | 341472.875 | 691226.434 | 0.0 | 0 | 12 |
| SolarStillDesignEvent | 12 | 0.575 | 2.174 | 2.309 | 4.241 | 5.2 | 25.99 | 0 | 0 |
| gameStartEvent | 9 | 504.309 | 14518.165 | 117208.012 | 492354.654 | 692872.095 | 0.0 | 0 | 8 |
| argumentationToolEvent | 6 | 1.256 | 41.329 | 116170.476 | 519756.245 | 691044.346 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 6 | 445.34 | 1793.718 | 133450.976 | 547773.583 | 697510.979 | 0.0 | 0 | 5 |
| EndOfUnit | 4 | 4498.201 | 50091.217 | 89229.659 | 228653.098 | 252238.001 | 0.0 | 0 | 4 |
| chatEvent | 2 | 1280.038 | 95787.08 | 95787.08 | 180843.417 | 190294.121 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 33 group(s), 61 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[889] _id=6acfeedcde269131f9d96c3e ts=2026-10-14T21:06:35.5280000Z == 6ab9a9279a8420a1e6b56b79.jsonl[890] _id=6acfeedcde269131f9d96c40 ts=2026-10-14T21:06:35.5280000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[1019] _id=6acfeeddde269131f9d96c45 ts=2026-10-14T21:06:36.1900000Z == 6ab9a9279a8420a1e6b56b79.jsonl[1020] _id=6acfeeddde269131f9d96c47 ts=2026-10-14T21:06:36.1900000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[1024] _id=6acfeee8de269131f9d96c54 ts=2026-10-14T21:06:47.0250000Z == 6ab9a9279a8420a1e6b56b79.jsonl[1025] _id=6acfeee8de269131f9d96c56 ts=2026-10-14T21:06:47.0250000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[11765] _id=6ad55c27de269131f9e8ec26 ts=2026-10-18T23:54:14.9780000Z == 6ab9a9279a8420a1e6b56b79.jsonl[11766] _id=6ad55c27de269131f9e8ec27 ts=2026-10-18T23:54:14.9780000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a9279a8420a1e6b56b79.jsonl[150] _id=6ac543b3de269131f9b709b4 ts=2026-10-06T18:53:38.7660000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[151] _id=6ac543b3de269131f9b709b9 ts=2026-10-06T18:53:38.7720000Z`; `417ms: 6ab9a9279a8420a1e6b56b79.jsonl[985] _id=6acfee92de269131f9d96bef ts=2026-10-14T21:05:22.0520000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[986] _id=6acfee92de269131f9d96bf3 ts=2026-10-14T21:05:22.4690000Z`; `845ms: 6ab9a9279a8420a1e6b56b79.jsonl[969] _id=6acfee94de269131f9d96bf7 ts=2026-10-14T21:05:24.1030000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[970] _id=6acfee95de269131f9d96bfb ts=2026-10-14T21:05:24.9480000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `755ms: 6ab9a9279a8420a1e6b56b79.jsonl[10425] _id=6ad18388de269131f9e297d6 ts=2026-10-16T01:53:12.3090000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[10429] _id=6ad18389de269131f9e297d8 ts=2026-10-16T01:53:13.0640000Z`; `231ms: 6ab9a9279a8420a1e6b56b79.jsonl[10460] _id=6ad183b3de269131f9e29882 ts=2026-10-16T01:53:54.7260000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[10461] _id=6ad183b3de269131f9e29884 ts=2026-10-16T01:53:54.9570000Z`; `900ms: 6ab9a9279a8420a1e6b56b79.jsonl[10469] _id=6ad183cdde269131f9e298eb ts=2026-10-16T01:54:21.3680000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[10470] _id=6ad183cede269131f9e298ef ts=2026-10-16T01:54:22.2680000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `682ms: 6ab9a9279a8420a1e6b56b79.jsonl[11712] _id=6ad55bd7de269131f9e8eb86 ts=2026-10-18T23:52:55.2980000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[11713] _id=6ad55bd8de269131f9e8eb88 ts=2026-10-18T23:52:55.9800000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6ab9a9279a8420a1e6b56b79.jsonl[6615] _id=6ad16a33de269131f9e22172 ts=2026-10-16T00:05:06.5620000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[6618] _id=6ad16a33de269131f9e22175 ts=2026-10-16T00:05:06.6010000Z`; `30ms: 6ab9a9279a8420a1e6b56b79.jsonl[10293] _id=6ad18258de269131f9e29357 ts=2026-10-16T01:48:08.1850000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[10296] _id=6ad18258de269131f9e2935a ts=2026-10-16T01:48:08.2150000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `222ms: 6ab9a9279a8420a1e6b56b79.jsonl[731] _id=6acfebacde269131f9d969c6 ts=2026-10-14T20:53:00.2010000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[738] _id=6acfebacde269131f9d969ca ts=2026-10-14T20:53:00.4230000Z`; `146ms: 6ab9a9279a8420a1e6b56b79.jsonl[737] _id=6acfebacde269131f9d969c8 ts=2026-10-14T20:53:00.3920000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[732] _id=6acfebadde269131f9d969cc ts=2026-10-14T20:53:00.5380000Z`; `726ms: 6ab9a9279a8420a1e6b56b79.jsonl[738] _id=6acfebacde269131f9d969ca ts=2026-10-14T20:53:00.4230000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[733] _id=6acfebadde269131f9d969ce ts=2026-10-14T20:53:01.1490000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9279a8420a1e6b56b79.jsonl[11912] _id=6ad55db8de269131f9e8eec9 ts=2026-10-19T00:00:55.6490000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[11913] _id=6ad55db8de269131f9e8eecb ts=2026-10-19T00:00:55.6530000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `750ms: 6ab9a9279a8420a1e6b56b79.jsonl[9535] _id=6ad17d8cde269131f9e27e17 ts=2026-10-16T01:27:40.0190000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[9538] _id=6ad17d8dde269131f9e27e22 ts=2026-10-16T01:27:40.7690000Z`; `296ms: 6ab9a9279a8420a1e6b56b79.jsonl[9542] _id=6ad17d8fde269131f9e27e29 ts=2026-10-16T01:27:42.5980000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[9539] _id=6ad17d8fde269131f9e27e30 ts=2026-10-16T01:27:42.8940000Z`; `618ms: 6ab9a9279a8420a1e6b56b79.jsonl[9580] _id=6ad17dc7de269131f9e27f7e ts=2026-10-16T01:28:38.9080000Z ~ 6ab9a9279a8420a1e6b56b79.jsonl[9583] _id=6ad17dc8de269131f9e27f87 ts=2026-10-16T01:28:39.5260000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 192h 27m 
  - Evidence: 192h 27m: 6ab9a9279a8420a1e6b56b79.jsonl[8] _id=6ac541c6de269131f9b6d395 ts=2026-10-06T18:45:25.8100000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[505] _id=6acfd422de269131f9d84987 ts=2026-10-14T19:12:33.8930000Z; 53h 12m: 6ab9a9279a8420a1e6b56b79.jsonl[10636] _id=6ad26de9de269131f9e705da ts=2026-10-16T18:33:09.9510000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11456] _id=6ad55a32de269131f9e8e854 ts=2026-10-18T23:45:54.0980000Z; 21h 39m: 6ab9a9279a8420a1e6b56b79.jsonl[906] _id=6acfed2dde269131f9d96b47 ts=2026-10-14T20:59:24.7780000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3056] _id=6ad11dddde269131f9df0a60 ts=2026-10-15T18:39:24.7770000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 194h 0m 
  - Evidence: 194h 0m: 6ab9a9279a8420a1e6b56b79.jsonl[385] _id=6ac547a3de269131f9b7696b ts=2026-10-06T19:10:27.0280000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[1530] _id=6acfeff5de269131f9d97150 ts=2026-10-14T21:11:16.6890000Z; 26h 52m: 6ab9a9279a8420a1e6b56b79.jsonl[2954] _id=6acff75bde269131f9d98215 ts=2026-10-14T21:42:51.2160000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[7559] _id=6ad17156de269131f9e23fb3 ts=2026-10-16T00:35:33.8320000Z; 17m 7s: 6ab9a9279a8420a1e6b56b79.jsonl[2019] _id=6acff0c7de269131f9d9754d ts=2026-10-14T21:14:46.6610000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[2731] _id=6acff4cade269131f9d97bad ts=2026-10-14T21:31:54.0610000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 55m 
  - Evidence: 191h 55m: 6ab9a9279a8420a1e6b56b79.jsonl[499] _id=6ac5494ade269131f9b79bcd ts=2026-10-06T19:17:29.7190000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[521] _id=6acfd457de269131f9d8515e ts=2026-10-14T19:13:26.3870000Z; 52h 48m: 6ab9a9279a8420a1e6b56b79.jsonl[11442] _id=6ad273ebde269131f9e78563 ts=2026-10-16T18:58:51.0020000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11462] _id=6ad55a6cde269131f9e8e8cb ts=2026-10-18T23:46:52.2120000Z; 20h 52m: 6ab9a9279a8420a1e6b56b79.jsonl[3051] _id=6acff88ade269131f9d9852e ts=2026-10-14T21:47:53.9550000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3075] _id=6ad11e1cde269131f9df10aa ts=2026-10-15T18:40:27.9470000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 672 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[10185] _id=6ad181d7de269131f9e2910a ts=2026-10-16T01:45:58.9300000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10186] _id=6ad181d7de269131f9e2910b ts=2026-10-16T01:45:58.9300000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[10281] _id=6ad1824ade269131f9e2932a ts=2026-10-16T01:47:54.1530000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10282] _id=6ad1824ade269131f9e2932b ts=2026-10-16T01:47:54.1530000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[11595] _id=6ad55b66de269131f9e8ea47 ts=2026-10-18T23:51:01.5430000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11596] _id=6ad55b66de269131f9e8ea48 ts=2026-10-18T23:51:01.5430000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 70h 3m 
  - Evidence: 70h 3m: 6ab9a9279a8420a1e6b56b79.jsonl[10618] _id=6ad185b8de269131f9e2a27f ts=2026-10-16T02:02:31.6340000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[12009] _id=6ad55f06de269131f9e8f0a2 ts=2026-10-19T00:06:29.6350000Z; 26h 23m: 6ab9a9279a8420a1e6b56b79.jsonl[904] _id=6acfeccfde269131f9d96b40 ts=2026-10-14T20:57:50.9990000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[5080] _id=6ad15fecde269131f9e1fc0e ts=2026-10-15T23:21:16.3100000Z; 1h 26m: 6ab9a9279a8420a1e6b56b79.jsonl[5080] _id=6ad15fecde269131f9e1fc0e ts=2026-10-15T23:21:16.3100000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[7796] _id=6ad17425de269131f9e24a88 ts=2026-10-16T00:47:33.4330000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 191h 56m 
  - Evidence: 191h 56m: 6ab9a9279a8420a1e6b56b79.jsonl[475] _id=6ac548e8de269131f9b78d79 ts=2026-10-06T19:15:52.4200000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[508] _id=6acfd433de269131f9d84bfb ts=2026-10-14T19:12:49.5290000Z; 52h 47m: 6ab9a9279a8420a1e6b56b79.jsonl[11441] _id=6ad273e6de269131f9e78530 ts=2026-10-16T18:58:45.9070000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11458] _id=6ad55a3fde269131f9e8e866 ts=2026-10-18T23:46:06.5760000Z; 20h 52m: 6ab9a9279a8420a1e6b56b79.jsonl[3038] _id=6acff86bde269131f9d984f5 ts=2026-10-14T21:47:22.9210000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3060] _id=6ad11debde269131f9df0be3 ts=2026-10-15T18:39:38.1950000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[509] _id=6acfd433de269131f9d84bfc ts=2026-10-14T19:12:49.5300000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[510] _id=6acfd433de269131f9d84bfd ts=2026-10-14T19:12:49.5300000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[6430] _id=6ad1683ede269131f9e21bd6 ts=2026-10-15T23:56:45.5900000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[6442] _id=6ad1683ede269131f9e21bd7 ts=2026-10-15T23:56:45.5900000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[671] _id=6acfeb37de269131f9d96936 ts=2026-10-14T20:51:02.8860000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[672] _id=6acfeb37de269131f9d96937 ts=2026-10-14T20:51:02.8860000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 191h 57m 
  - Evidence: 191h 57m: 6ab9a9279a8420a1e6b56b79.jsonl[472] _id=6ac548eade269131f9b78db5 ts=2026-10-06T19:15:54.4750000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[519] _id=6acfd457de269131f9d85156 ts=2026-10-14T19:13:26.3670000Z; 52h 56m: 6ab9a9279a8420a1e6b56b79.jsonl[11281] _id=6ad271e5de269131f9e75e70 ts=2026-10-16T18:50:13.7960000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11498] _id=6ad55a81de269131f9e8e8f0 ts=2026-10-18T23:47:13.2790000Z; 21h 38m: 6ab9a9279a8420a1e6b56b79.jsonl[2522] _id=6acff190de269131f9d97921 ts=2026-10-14T21:18:07.7380000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3337] _id=6ad121e2de269131f9df8bc5 ts=2026-10-15T18:56:33.5850000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.006s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[10067] _id=6ad180fbde269131f9e28d8d ts=2026-10-16T01:42:19.4280000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10068] _id=6ad180fbde269131f9e28d8e ts=2026-10-16T01:42:19.4280000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[10121] _id=6ad1813ede269131f9e28ea7 ts=2026-10-16T01:43:25.8250000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10122] _id=6ad1813ede269131f9e28ea8 ts=2026-10-16T01:43:25.8250000Z; 6ms: 6ab9a9279a8420a1e6b56b79.jsonl[150] _id=6ac543b3de269131f9b709b4 ts=2026-10-06T18:53:38.7660000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[151] _id=6ac543b3de269131f9b709b9 ts=2026-10-06T18:53:38.7720000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 55m 
  - Evidence: 191h 55m: 6ab9a9279a8420a1e6b56b79.jsonl[498] _id=6ac54948de269131f9b79b90 ts=2026-10-06T19:17:28.1420000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[507] _id=6acfd433de269131f9d84bfa ts=2026-10-14T19:12:45.9540000Z; 52h 46m: 6ab9a9279a8420a1e6b56b79.jsonl[11447] _id=6ad2740ade269131f9e78647 ts=2026-10-16T18:59:22.5280000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11457] _id=6ad55a3fde269131f9e8e865 ts=2026-10-18T23:46:04.1750000Z; 20h 51m: 6ab9a9279a8420a1e6b56b79.jsonl[3054] _id=6acff8a1de269131f9d98560 ts=2026-10-14T21:48:17.1380000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3059] _id=6ad11debde269131f9df0be2 ts=2026-10-15T18:39:35.2910000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 21h 43m 
  - Evidence: 21h 43m: 6ab9a9279a8420a1e6b56b79.jsonl[2501] _id=6acff151de269131f9d978fc ts=2026-10-14T21:17:03.6430000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3411] _id=6ad122cede269131f9dfac7b ts=2026-10-15T19:00:30.0530000Z; 16h 58m: 6ab9a9279a8420a1e6b56b79.jsonl[9849] _id=6ad17f31de269131f9e2865d ts=2026-10-16T01:34:39.4450000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10633] _id=6ad26deede269131f9e7062e ts=2026-10-16T18:33:16.9840000Z; 3h 33m: 6ab9a9279a8420a1e6b56b79.jsonl[4002] _id=6ad12489de269131f9dff3e3 ts=2026-10-15T19:07:52.4960000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[4191] _id=6ad156a1de269131f9e1dada ts=2026-10-15T22:41:36.8790000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1405 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[1011] _id=6acfef47de269131f9d96d6c ts=2026-10-14T21:08:22.2010000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[1012] _id=6acfef48de269131f9d96d70 ts=2026-10-14T21:08:22.2010000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[1013] _id=6acfef48de269131f9d96d72 ts=2026-10-14T21:08:22.7420000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[1112] _id=6acfef48de269131f9d96d74 ts=2026-10-14T21:08:22.7420000Z; 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[1019] _id=6acfeeddde269131f9d96c45 ts=2026-10-14T21:06:36.1900000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[1020] _id=6acfeeddde269131f9d96c47 ts=2026-10-14T21:06:36.1900000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 21h 36m 
  - Evidence: 21h 36m: 6ab9a9279a8420a1e6b56b79.jsonl[2544] _id=6acff1fade269131f9d9795b ts=2026-10-14T21:19:53.6610000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3336] _id=6ad121e1de269131f9df8bb9 ts=2026-10-15T18:56:33.5800000Z; 5h 7m: 6ab9a9279a8420a1e6b56b79.jsonl[3485] _id=6ad1231cde269131f9dfb75a ts=2026-10-15T19:01:47.7360000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[6717] _id=6ad16b36de269131f9e22664 ts=2026-10-16T00:09:26.4530000Z; 42m 56s: 6ab9a9279a8420a1e6b56b79.jsonl[6744] _id=6ad16b8fde269131f9e22722 ts=2026-10-16T00:10:54.7480000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[7872] _id=6ad175a0de269131f9e2507f ts=2026-10-16T00:53:51.6920000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 20h 55m 
  - Evidence: 20h 55m: 6ab9a9279a8420a1e6b56b79.jsonl[2935] _id=6acff81ade269131f9d98402 ts=2026-10-14T21:46:02.2740000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3098] _id=6ad11e6ade269131f9df1923 ts=2026-10-15T18:41:46.3300000Z; 4h 0m: 6ab9a9279a8420a1e6b56b79.jsonl[3293] _id=6ad12145de269131f9df76bb ts=2026-10-15T18:53:57.5470000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[4435] _id=6ad159bfde269131f9e1e7ed ts=2026-10-15T22:54:55.4190000Z; 39m 44s: 6ab9a9279a8420a1e6b56b79.jsonl[6342] _id=6ad167e1de269131f9e21abc ts=2026-10-15T23:55:13.5200000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[7549] _id=6ad17132de269131f9e23ef6 ts=2026-10-16T00:34:58.1880000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.020s shown 
  - Evidence: 19ms: 6ab9a9279a8420a1e6b56b79.jsonl[2702] _id=6acff454de269131f9d97a8d ts=2026-10-14T21:29:55.8320000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[2693] _id=6acff454de269131f9d97a8f ts=2026-10-14T21:29:55.8510000Z; 20ms: 6ab9a9279a8420a1e6b56b79.jsonl[2693] _id=6acff454de269131f9d97a8f ts=2026-10-14T21:29:55.8510000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[2697] _id=6acff454de269131f9d97a93 ts=2026-10-14T21:29:55.8710000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 70h 2m 
  - Evidence: 70h 2m: 6ab9a9279a8420a1e6b56b79.jsonl[10291] _id=6ad18258de269131f9e29355 ts=2026-10-16T01:48:08.1680000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11594] _id=6ad55b66de269131f9e8ea43 ts=2026-10-18T23:51:01.5130000Z; 26h 19m: 6ab9a9279a8420a1e6b56b79.jsonl[793] _id=6acfec10de269131f9d96a6f ts=2026-10-14T20:54:40.2950000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[4853] _id=6ad15e2bde269131f9e1f498 ts=2026-10-15T23:13:47.2700000Z; 1h 40m: 6ab9a9279a8420a1e6b56b79.jsonl[6614] _id=6ad16a32de269131f9e22170 ts=2026-10-16T00:05:06.5430000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10184] _id=6ad181d7de269131f9e29108 ts=2026-10-16T01:45:58.9080000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 57m 
  - Evidence: 191h 57m: 6ab9a9279a8420a1e6b56b79.jsonl[494] _id=6ac5493bde269131f9b799c7 ts=2026-10-06T19:17:15.0780000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[540] _id=6acfd4a3de269131f9d85fad ts=2026-10-14T19:14:42.1070000Z; 70h 2m: 6ab9a9279a8420a1e6b56b79.jsonl[10296] _id=6ad18258de269131f9e2935a ts=2026-10-16T01:48:08.2150000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11570] _id=6ad55b44de269131f9e8e9e9 ts=2026-10-18T23:50:28.1890000Z; 26h 18m: 6ab9a9279a8420a1e6b56b79.jsonl[794] _id=6acfec10de269131f9d96a71 ts=2026-10-14T20:54:40.3210000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[4793] _id=6ad15df0de269131f9e1f370 ts=2026-10-15T23:12:48.1020000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.030s..0.039s shown 
  - Evidence: 30ms: 6ab9a9279a8420a1e6b56b79.jsonl[10293] _id=6ad18258de269131f9e29357 ts=2026-10-16T01:48:08.1850000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10296] _id=6ad18258de269131f9e2935a ts=2026-10-16T01:48:08.2150000Z; 39ms: 6ab9a9279a8420a1e6b56b79.jsonl[6615] _id=6ad16a33de269131f9e22172 ts=2026-10-16T00:05:06.5620000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[6618] _id=6ad16a33de269131f9e22175 ts=2026-10-16T00:05:06.6010000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 70h 2m 
  - Evidence: 70h 2m: 6ab9a9279a8420a1e6b56b79.jsonl[10288] _id=6ad18253de269131f9e2934d ts=2026-10-16T01:48:03.3380000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11538] _id=6ad55b3bde269131f9e8e9d9 ts=2026-10-18T23:50:19.4090000Z; 26h 18m: 6ab9a9279a8420a1e6b56b79.jsonl[791] _id=6acfec0bde269131f9d96a67 ts=2026-10-14T20:54:35.3570000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[4792] _id=6ad15de7de269131f9e1f356 ts=2026-10-15T23:12:38.9200000Z; 1h 40m: 6ab9a9279a8420a1e6b56b79.jsonl[6610] _id=6ad16a31de269131f9e2216c ts=2026-10-16T00:05:05.0730000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[10165] _id=6ad181bade269131f9e290a5 ts=2026-10-16T01:45:29.9390000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 51 interval(s) ≤ 0.010s..0.022s shown 
  - Evidence: 10ms: 6ab9a9279a8420a1e6b56b79.jsonl[710] _id=6acfeb8bde269131f9d96996 ts=2026-10-14T20:52:27.3900000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[716] _id=6acfeb8cde269131f9d96998 ts=2026-10-14T20:52:27.4000000Z; 12ms: 6ab9a9279a8420a1e6b56b79.jsonl[730] _id=6acfebacde269131f9d969c4 ts=2026-10-14T20:53:00.1890000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[731] _id=6acfebacde269131f9d969c6 ts=2026-10-14T20:53:00.2010000Z; 22ms: 6ab9a9279a8420a1e6b56b79.jsonl[11635] _id=6ad55b81de269131f9e8ea83 ts=2026-10-18T23:51:28.7970000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11636] _id=6ad55b81de269131f9e8ea84 ts=2026-10-18T23:51:28.8190000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 57m 
  - Evidence: 191h 57m: 6ab9a9279a8420a1e6b56b79.jsonl[495] _id=6ac5493bde269131f9b799b5 ts=2026-10-06T19:17:15.0320000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[526] _id=6acfd4a0de269131f9d85f25 ts=2026-10-14T19:14:39.3780000Z; 1h 38m: 6ab9a9279a8420a1e6b56b79.jsonl[502] _id=6acfd4a3de269131f9d85f97 ts=2026-10-14T19:14:42.0340000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[719] _id=6acfeba6de269131f9d969af ts=2026-10-14T20:52:53.9740000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 52h 51m 
  - Evidence: 52h 51m: 6ab9a9279a8420a1e6b56b79.jsonl[11380] _id=6ad272e6de269131f9e77209 ts=2026-10-16T18:54:29.7570000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11455] _id=6ad55a3cde269131f9e8e863 ts=2026-10-18T23:46:03.8780000Z; 21m 20s: 6ab9a9279a8420a1e6b56b79.jsonl[10634] _id=6ad26de5de269131f9e705a8 ts=2026-10-16T18:33:09.7190000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11380] _id=6ad272e6de269131f9e77209 ts=2026-10-16T18:54:29.7570000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 192h 27m 
  - Evidence: 192h 27m: 6ab9a9279a8420a1e6b56b79.jsonl[4] _id=6ac5419ade269131f9b6cedd ts=2026-10-06T18:44:42.1490000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[504] _id=6acfd423de269131f9d84999 ts=2026-10-14T19:12:34.2440000Z; 53h 12m: 6ab9a9279a8420a1e6b56b79.jsonl[10628] _id=6ad26dd8de269131f9e70507 ts=2026-10-16T18:32:55.7650000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11461] _id=6ad55a32de269131f9e8e857 ts=2026-10-18T23:45:54.2580000Z; 21h 40m: 6ab9a9279a8420a1e6b56b79.jsonl[883] _id=6acfed24de269131f9d96b45 ts=2026-10-14T20:59:16.3420000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3057] _id=6ad11dddde269131f9df0a67 ts=2026-10-15T18:39:24.9460000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 192h 0m 
  - Evidence: 192h 0m: 6ab9a9279a8420a1e6b56b79.jsonl[414] _id=6ac54808de269131f9b7706b ts=2026-10-06T19:12:07.8100000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[503] _id=6acfd423de269131f9d84998 ts=2026-10-14T19:12:34.2440000Z; 53h 12m: 6ab9a9279a8420a1e6b56b79.jsonl[10627] _id=6ad26dd8de269131f9e70506 ts=2026-10-16T18:32:55.7650000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11460] _id=6ad55a32de269131f9e8e856 ts=2026-10-18T23:45:54.2580000Z; 21h 34m: 6ab9a9279a8420a1e6b56b79.jsonl[958] _id=6acfee6ade269131f9d96bc9 ts=2026-10-14T21:04:41.9320000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3055] _id=6ad11dddde269131f9df0a66 ts=2026-10-15T18:39:24.9460000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 193h 45m 
  - Evidence: 193h 45m: 6ab9a9279a8420a1e6b56b79.jsonl[413] _id=6ac54803de269131f9b7702b ts=2026-10-06T19:12:03.4060000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[860] _id=6acfecaade269131f9d96b1c ts=2026-10-14T20:57:14.3850000Z; 27h 22m: 6ab9a9279a8420a1e6b56b79.jsonl[3053] _id=6acff898de269131f9d9854c ts=2026-10-14T21:48:07.8350000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[8957] _id=6ad17999de269131f9e26938 ts=2026-10-16T01:10:49.2290000Z; 43m 28s: 6ab9a9279a8420a1e6b56b79.jsonl[945] _id=6acfee68de269131f9d96bc7 ts=2026-10-14T21:04:39.7250000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3053] _id=6acff898de269131f9d9854c ts=2026-10-14T21:48:07.8350000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 191h 56m 
  - Evidence: 191h 56m: 6ab9a9279a8420a1e6b56b79.jsonl[468] _id=6ac548ebde269131f9b78dd5 ts=2026-10-06T19:15:54.5020000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[512] _id=6acfd433de269131f9d84bff ts=2026-10-14T19:12:49.7410000Z; 52h 48m: 6ab9a9279a8420a1e6b56b79.jsonl[11414] _id=6ad2739ade269131f9e77f49 ts=2026-10-16T18:57:30.5170000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11459] _id=6ad55a3fde269131f9e8e867 ts=2026-10-18T23:46:06.9660000Z; 21h 10m: 6ab9a9279a8420a1e6b56b79.jsonl[2685] _id=6acff434de269131f9d97a7c ts=2026-10-14T21:29:24.0140000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[3061] _id=6ad11debde269131f9df0be4 ts=2026-10-15T18:39:38.2400000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b79.jsonl[11765] _id=6ad55c27de269131f9e8ec26 ts=2026-10-18T23:54:14.9780000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[11766] _id=6ad55c27de269131f9e8ec27 ts=2026-10-18T23:54:14.9780000Z; 1ms: 6ab9a9279a8420a1e6b56b79.jsonl[523] _id=6acfd457de269131f9d85160 ts=2026-10-14T19:13:26.4060000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[524] _id=6acfd457de269131f9d85161 ts=2026-10-14T19:13:26.4070000Z; 1ms: 6ab9a9279a8420a1e6b56b79.jsonl[696] _id=6acfeb5ade269131f9d96960 ts=2026-10-14T20:51:38.0870000Z -> 6ab9a9279a8420a1e6b56b79.jsonl[697] _id=6acfeb5ade269131f9d96961 ts=2026-10-14T20:51:38.0880000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[460] _id=6ac548c8de269131f9b78879 ts=2026-10-06T19:15:20.3190000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[806] _id=6acfec28de269131f9d96a94 ts=2026-10-14T20:55:03.2580000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[2779] _id=6acff691de269131f9d97f29 ts=2026-10-14T21:39:28.9120000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[6618] _id=6ad16a33de269131f9e22175 ts=2026-10-16T00:05:06.6010000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[10296] _id=6ad18258de269131f9e2935a ts=2026-10-16T01:48:08.2150000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[10634] _id=6ad26de5de269131f9e705a8 ts=2026-10-16T18:33:09.7190000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[11380] _id=6ad272e6de269131f9e77209 ts=2026-10-16T18:54:29.7570000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[11455] _id=6ad55a3cde269131f9e8e863 ts=2026-10-18T23:46:03.8780000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 39 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[3608] _id=6ad12382de269131f9dfc70f ts=2026-10-15T19:03:25.4840000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[3609] _id=6ad12383de269131f9dfc718 ts=2026-10-15T19:03:25.4840000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[3610] _id=6ad12383de269131f9dfc71f ts=2026-10-15T19:03:25.4840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 57 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[1018] _id=6acfeedcde269131f9d96c3c ts=2026-10-14T21:06:35.4530000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[889] _id=6acfeedcde269131f9d96c3e ts=2026-10-14T21:06:35.5280000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[890] _id=6acfeedcde269131f9d96c40 ts=2026-10-14T21:06:35.5280000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[540] _id=6acfd4a3de269131f9d85fad ts=2026-10-14T19:14:42.1070000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[726] _id=6acfeba7de269131f9d969b6 ts=2026-10-14T20:52:55.2960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 446 start, 438 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'BecameCameraCentered' (totals: 662 open, 660 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 868 open, 856 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 9 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 46 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 244 of 12009 adjacent _id pairs reverse in client time; worst 90.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b79.jsonl[1079] _id=6acfef31de269131f9d96d0a ts=2026-10-14T21:08:00.7360000Z`; `6ab9a9279a8420a1e6b56b79.jsonl[1080] _id=6acfef32de269131f9d96d0c ts=2026-10-14T21:06:29.8670000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.48s, min -92.73s, max -0.15s over 12010 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b79\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

No coverage-related findings.

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3046 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1726); Unit 4 Dev (788); Unit 5 Dev - Dungeon (290); Unit 3 Dungeon Dev (242)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.43s, n=3045)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3046/3046 records)
    "BecameVisible"  x868
    "BecameInvisible"  x856
    "BecameCameraCentered"  x662
    "BecameCameraUncentered"  x660
data.pieceId  (string, 3046/3046 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3046/3046 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3023 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (987); Unit 2 Prod (Refactor) (599); Unit 4 Dev - Dungeon (507); Unit 5 Dev - Dungeon (205); Unit 3 Dungeon Dev (183); Unit 4 Dev (179); Unit 1 Dev (161); Unit 4 Dev - Anderson Base (105); Unit 5 Dev (97)
- **Intervals:** median 1.67s (p5 0.18s / p95 23.77s, n=3022)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3023/3023 records)
    "pressed"  x3023
data.actionType  (string, 3023/3023 records)
    "Move"  x2207
    "Interact"  x504
    "Ascend"  x105
    "Jump"  x74
    "Map"  x55
    "Sprint"  x39
    "Hoverboard"  x36
    "ToggleDebug"  x2
    "Pause"  x1
data.key  (string, 3023/3023 records, 25 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3023/3023 records)
    "Player"  x1994
    "Drone"  x1029
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2343 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (700); Unit 3 Dev (425); Unit 1 Dev (293); Unit 4 Dev (260); Unit 5 Dev (236); Unit 3 Dungeon Dev (135); Unit 4 Dev - Dungeon (120); Unit 4 Dev - Anderson Base (95); Unit 5 Dev - Dungeon (79)
- **eventKey:** present on 1459 of 2343 records
- **Intervals:** median 4.42s (p5 0.00s / p95 34.59s, n=2342)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1459; [conversationId, dialogueEventType] x884
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2343/2343 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2343/2343 records)
    "DialogueNodeEvent"  x1459
    "DialogueStartEvent"  x446
    "DialogueFinishEvent"  x438
data.nodeId  (number, 1459/2343 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2199 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (720); Unit 3 Dev (370); Unit 1 Dev (266); Unit 4 Dev (199); Unit 4 Dev - Dungeon (184); Unit 5 Dev (148); Unit 5 Dev - Dungeon (127); Unit 3 Dungeon Dev (125); Unit 4 Dev - Anderson Base (60)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.18s, n=2187)
- **Fields under `data`:**

```text
data.position  (object, 2199/2199 records)
data.position.x  (number, 2199/2199 records)
    numeric range -675.822 .. 1553.94 (749 unique)
data.position.y  (number, 2199/2199 records)
    numeric range -114.326 .. 222.252 (541 unique)
data.position.z  (number, 2199/2199 records)
    numeric range -1136.35 .. 2095.62 (749 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 469 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (139); Unit 5 Dev (104); Unit 3 Dev (79); Unit 1 Dev (74); Unit 4 Dev - Anderson Base (73)
- **Intervals:** median 0.68s (p5 0.03s / p95 10.88s, n=468)
- **Fields under `data`:**

```text
data.actionType  (string, 469/469 records)
    "argumentationNodeHoverEnd"  x200
    "argumentationNodeHoverStart"  x200
    "argumentationNodeAdd"  x48
    "argumentationNodeRemove"  x21
data.argumentationTitle  (string, 469/469 records)
    "Unit 2 – Watershed"  x139
    "Unit 5"  x104
    "Unit 3 - Pollution Upstream"  x79
    "Unit 4 - Flooding"  x73
    "Unit 1 - Argumentation Tutorial"  x40
    "Unit 1 - Freshwater"  x34
data.nodeName  (string, 469/469 records)
    "B"  x66
    "A"  x65
    "II"  x55
    "1"  x53
    "D"  x50
    "I"  x47
    "C"  x44
    "4"  x32
    "2"  x29
    "3"  x23
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 308 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (115); Unit 2 Prod (Refactor) (69); Unit 3 Dungeon Dev (43); Unit 4 Dev (27); Unit 1 Dev (14); Unit 5 Dev - Dungeon (13); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (7)
- **Intervals:** median 11.37s (p5 0.42s / p95 400.85s, n=307)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 308/308 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 308/308 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 189 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (114); Unit 3 Dev (75)
- **Intervals:** median 7.38s (p5 1.26s / p95 142.84s, n=188)
- **`data` key-set variants:** [actionType, featureUsed] x142; [actionType, featureUsed, legendName] x33; [actionType, featureUsed, location] x14
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 189/189 records)
    "MapCloseEvent"  x71
    "MapOpenEvent"  x71
    "Selected"  x28
    "WaypointMoveEvent"  x10
    "Unselected"  x5
    "WaypointSetEvent"  x4
data.featureUsed  (string, 189/189 records)
    "Map"  x142
    "Legend"  x33
    "Waypoint"  x14
data.legendName  (string, 33/189 records)
    14 unique values (see csv/event_unique_values.csv)
data.location  (object, 14/189 records)
data.location.x  (number, 14/189 records)
    numeric range -379.865 .. 95.3311 (13 unique)
data.location.y  (number, 14/189 records)
    numeric range -280.205 .. 297.622 (14 unique)
data.location.z  (number, 14/189 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 99 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (75); Unit 3 Dev (20); Unit 4 Dev (4)
- **Intervals:** median 2.04s (p5 0.32s / p95 42.90s, n=98)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x91; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/99 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/99 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 91/99 records)
    "RightDrag"  x47
    "LeftDrag"  x44
data.currentSoilType  (string, 91/99 records)
    "CLAY"  x19
    "CLAYSAND"  x17
    "SAND"  x16
    "SANDGRAVEL"  x15
    "CLAYROCK"  x13
    "GRAVEL"  x7
    "BEDROCK"  x4
data.isCorrectSelection  (string, 91/99 records)
    "false"  x70
    "true"  x21
data.waterLevelStatus  (string, 91/99 records)
    "TooHigh"  x38
    "TooLow"  x29
    "Proper"  x24
data.waterRetentionChange  (string, 91/99 records)
    "Increase"  x39
    "Decrease"  x31
    "NoChange"  x21
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (20); Unit 2 Prod (Refactor) (16); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 201.00s (p5 0.00s / p95 14930.12s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x46; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x46
    "questFinishEvent"  x35
data.questID  (string, 81/81 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/81 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 45 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (15); Unit 2 Prod (Refactor) (10); Unit 5 Dev (10); Unit 1 Dev (7); Unit 3 Dev (3)
- **Intervals:** median 14.07s (p5 2.03s / p95 6015.14s, n=44)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "submitAnswerEvent"  x45
data.answerSubmitted  (string, 45/45 records)
    21 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 45/45 records)
    "Unit 4 - Flooding"  x15
    "Unit 2 – Watershed"  x10
    "Unit 5"  x10
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 35 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (35)
- **Intervals:** median 2.45s (p5 0.13s / p95 154.13s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "ChangeCanister"  x35
data.canisterType  (string, 35/35 records)
    "Clay"  x26
    "Bedrock"  x6
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 35/35 records)
    "5"  x32
    "4"  x2
    "3"  x1
data.machine  (string, 35/35 records)
    "1"  x34
    "2"  x1
data.row  (string, 35/35 records)
    "BottomRow"  x24
    "TopRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 26 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (26)
- **Intervals:** median 25.96s (p5 5.89s / p95 98.50s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "On"  x18
    "Off"  x8
data.floor  (string, 26/26 records)
    "3"  x13
    "4"  x7
    "1"  x3
    "2"  x3
data.machineNumber  (string, 26/26 records)
    "One"  x24
    "Two"  x2
data.machineType  (string, 26/26 records)
    "Condenser"  x15
    "Evaporator"  x6
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 26/26 records)
    "2"  x8
    "3"  x7
    "1"  x6
    "4"  x5
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 24 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (9); Unit 1 Dev (3); Unit 2 Prod (Refactor) (3); Unit 4 Dev (3); Unit 3 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 751.06s (p5 9.55s / p95 180207.73s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "DebugMenuStateChanged"  x24
data.isOpened  (bool, 24/24 records)
    false  x24
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 24 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 6.69s (p5 1.77s / p95 87189.09s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "Close"  x12
    "Open"  x12
data.toolName  (string, 24/24 records, 24 empty-string)
    ""  x24
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 19 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (19)
- **Intervals:** median 3.07s (p5 0.68s / p95 18.77s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records, 11 empty-string)
    ""  x11
    "cameraPlaced"  x8
data.boxId  (string, 19/19 records)
    "0"  x10
    "1"  x5
    "2"  x4
data.soilType  (string, 19/19 records)
    "Sand"  x8
    "Clay"  x4
    "None"  x4
    "Gravel"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 19 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 149.70s (p5 0.04s / p95 317976.03s, n=18)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x9
data.argumentationDescription  (string, 19/19 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x5
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 19/19 records)
    "Unit 1 - Argumentation Tutorial"  x5
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowFocusEvent` — 16 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (10); Unit 1 Dev (3); Unit 4 Dev - Dungeon (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 2409.90s (p5 264.36s / p95 341472.88s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `SolarStillDesignEvent` — 13 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (13)
- **Intervals:** median 2.17s (p5 0.70s / p95 4.24s, n=12)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x12; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "optionSelected"  x12
    "DesignSubmitted"  x1
data.designSelections  (object, 1/13 records)
data.designSelections.glassRoofTemperature  (string, 1/13 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/13 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/13 records)
    "Tilted Out"  x1
data.featureUsed  (string, 13/13 records)
    "RoofStyle"  x5
    "GlassRoofTemperature"  x4
    "ExtraCovering"  x3
    "Submit"  x1
data.selectedOption  (string, 12/13 records, 1 empty-string)
    "Cold"  x2
    "Covered"  x2
    "Hot"  x2
    "Tilted In"  x2
    ""  x1
    "Flat"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 10 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (10)
- **Intervals:** median 14518.17s (p5 1266.55s / p95 492354.65s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    true  x10
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 41.33s (p5 1.61s / p95 519756.24s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Argumentation Tutorial"  x6
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - Argumentation"  x6
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 7 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1793.72s (p5 484.18s / p95 547773.58s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    false  x7
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 50091.22s (p5 4600.04s / p95 228653.10s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 95787.08s (p5 10730.74s / p95 180843.42s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (75 records)
- `TerasGardenBox` data.actionType: "" (11x)
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "Selected" (28x); "Unselected" (5x); "WaypointMoveEvent" (10x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (33x); "Waypoint" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (21x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*