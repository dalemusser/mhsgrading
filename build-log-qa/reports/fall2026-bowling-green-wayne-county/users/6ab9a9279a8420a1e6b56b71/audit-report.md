# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b71

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b71
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b71.jsonl
- **Records:** 14091 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b71
- **Time span:** 2026-10-05T19:11:08.454000+00:00 .. 2026-10-16T21:43:55.560000+00:00 (266h 32m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b71\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 14091 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 106 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5050 | 35.84 | 1 | 9 | 0 | 2026-10-05T19:11:20.823000+00:00 | 2026-10-16T21:43:55.560000+00:00 | 266h 32m |
| PuzzlePieceVisibleEvent | 3062 | 21.73 | 1 | 4 | 0 | 2026-10-06T19:03:39.389000+00:00 | 2026-10-16T21:14:38.766000+00:00 | 242h 10m |
| DialogueEvent | 2540 | 18.03 | 1 | 9 | 1573 | 2026-10-05T19:11:37.340000+00:00 | 2026-10-16T21:43:45.734000+00:00 | 266h 32m |
| PlayerPositionEvent | 1991 | 14.13 | 1 | 9 | 0 | 2026-10-05T19:11:17.313000+00:00 | 2026-10-16T21:43:46.587000+00:00 | 266h 32m |
| argumentationNodeEvent | 500 | 3.55 | 1 | 5 | 0 | 2026-10-06T18:51:11.728000+00:00 | 2026-10-16T21:31:17.765000+00:00 | 242h 40m |
| ObjectInterEvent | 339 | 2.41 | 1 | 9 | 0 | 2026-10-05T19:17:02.018000+00:00 | 2026-10-16T21:43:55.560000+00:00 | 266h 26m |
| TopographicMapEvent | 108 | 0.77 | 1 | 3 | 0 | 2026-10-06T18:34:24.491000+00:00 | 2026-10-14T19:11:10.323000+00:00 | 192h 36m |
| questEvent | 96 | 0.68 | 1 | 9 | 96 | 2026-10-05T19:11:37.311000+00:00 | 2026-10-16T21:40:15.145000+00:00 | 266h 28m |
| DaniEvent | 84 | 0.6 | 1 | 4 | 0 | 2026-10-05T19:16:14.750000+00:00 | 2026-10-15T19:04:42.965000+00:00 | 239h 48m |
| Soil Key Puzzle | 72 | 0.51 | 1 | 3 | 0 | 2026-10-06T19:10:07.874000+00:00 | 2026-10-15T18:43:37.399000+00:00 | 215h 33m |
| soilMachine | 44 | 0.31 | 1 | 1 | 0 | 2026-10-15T18:59:52.593000+00:00 | 2026-10-15T19:16:09.125000+00:00 | 16m 16s |
| DEBUGMenu | 41 | 0.29 | 1 | 9 | 0 | 2026-10-05T19:11:17.295000+00:00 | 2026-10-16T21:10:29.511000+00:00 | 265h 59m |
| argumentationAnswerEvent | 40 | 0.28 | 1 | 5 | 0 | 2026-10-06T18:53:22.566000+00:00 | 2026-10-16T21:31:39.910000+00:00 | 242h 38m |
| WaterChamberEvent | 25 | 0.18 | 1 | 1 | 0 | 2026-10-16T21:13:34.753000+00:00 | 2026-10-16T21:22:34.628000+00:00 | 8m 59s |
| gameWindowFocusEvent | 24 | 0.17 | 1 | 3 | 0 | 2026-10-05T19:11:08.454000+00:00 | 2026-10-16T21:35:21.364000+00:00 | 266h 24m |
| gameStartEvent | 19 | 0.13 | 1 | 1 | 0 | 2026-10-05T19:11:08.456000+00:00 | 2026-10-16T21:10:13.372000+00:00 | 265h 59m |
| argumentationEvent | 15 | 0.11 | 1 | 5 | 0 | 2026-10-06T18:52:42.269000+00:00 | 2026-10-16T21:31:39.943000+00:00 | 242h 38m |
| chatEvent | 11 | 0.08 | 1 | 5 | 0 | 2026-10-06T18:34:15.547000+00:00 | 2026-10-16T21:23:28.584000+00:00 | 242h 49m |
| gameWindowUnfocusEvent | 9 | 0.06 | 1 | 4 | 0 | 2026-10-06T19:17:57.182000+00:00 | 2026-10-16T21:35:20.098000+00:00 | 242h 17m |
| TerasGardenBox | 8 | 0.06 | 1 | 1 | 0 | 2026-10-16T18:45:10.923000+00:00 | 2026-10-16T18:46:08.245000+00:00 | 57.3s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T18:58:05.764000+00:00 | 2026-10-16T21:43:55.543000+00:00 | 242h 45m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-16T21:37:44.047000+00:00 | 2026-10-16T21:37:53.283000+00:00 | 9.2s |
| argumentationToolEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-06T18:52:42.174000+00:00 | 2026-10-14T18:49:19.307000+00:00 | 191h 56m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172300.091s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.05s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.701s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.146s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.489s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 139.435s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 391.023s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6621.796s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1854.328s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 50409.355s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.531s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.4x vs baseline. 
  - Observed: 41 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 84 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 8.0x vs baseline. 
  - Observed: 40 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,2,I; A,2,II; A,3,I; A,4,I; A,B,2,II; A,D,B,2,II; A,D,C,2,II; B,1,I; B,2,I; B,2,II; B,C,D,2,II; B,D,2,II; C,2,II; C,3,II; C,D,2,II; C,D,3,4,II; C,D,3,II; C,D,B,2,II; D,1,I; D,2,I; D,2,II; D,A,2,II; D,B,2,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 500 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.5x vs baseline. 
  - Observed: 11 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [16-3]; [30-48, 30-49, 30-50, 30-56, 30-57]; [91-88, 91-90, 91-92, 91-98, 91-99] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 9 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 8.8x vs baseline. 
  - Observed: 44 records 
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
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[217] _id=6ac53f48de269131f9b68a7f ts=2026-10-06T18:34:46.7750000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[296] _id=6ac54062de269131f9b6ac1a ts=2026-10-06T18:39:28.6520000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[356] _id=6ac5418dde269131f9b6cd4d ts=2026-10-06T18:44:28.3270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[5] _id=6ac3f64dde269131f9af6a7f ts=2026-10-05T19:11:08.4560000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[133] _id=6ac53e83de269131f9b67623 ts=2026-10-06T18:31:30.3020000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[712] _id=6ac54513de269131f9b7216f ts=2026-10-06T18:59:30.1390000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[7] _id=6ac3f64dde269131f9af6a7d ts=2026-10-05T19:11:08.4540000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[134] _id=6ac53e83de269131f9b67621 ts=2026-10-06T18:31:30.3010000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[711] _id=6ac54513de269131f9b7216b ts=2026-10-06T18:59:30.1380000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 9 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 9} 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[2065] _id=6ac69283de269131f9bde969 ts=2026-10-06T19:17:57.182Z`; `6ab9a9279a8420a1e6b56b71.jsonl[4016] _id=6ac69ad5de269131f9bf20d7 ts=2026-10-07T19:17:40.6110000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[5579] _id=6ace8317de269131f9d1a7e8 ts=2026-10-13T18:54:55.499Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 23 of 108 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[208] _id=6ac53f32de269131f9b687d1 ts=2026-10-06T18:34:24.4910000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[210] _id=6ac53f32de269131f9b687e3 ts=2026-10-06T18:34:25.6120000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[928] _id=6ac54629de269131f9b73a57 ts=2026-10-06T19:04:08.4450000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5049 | 0.0 | 0.859 | 190.048 | 10.032 | 346608.465 | 0.32 | 110 | 13 |
| PuzzlePieceVisibleEvent | 3061 | 0.0 | 0.05 | 284.828 | 1.384 | 434076.393 | 0.21 | 1534 | 9 |
| DialogueEvent | 2539 | 0.0 | 3.679 | 377.916 | 25.798 | 346423.526 | 0.16 | 731 | 11 |
| PlayerPositionEvent | 1979 | 0.0 | 10.002 | 309.7 | 10.203 | 84748.983 | 0.19 | 2 | 10 |
| argumentationNodeEvent | 499 | 0.004 | 0.663 | 1750.714 | 10.494 | 433895.353 | 0.03 | 54 | 6 |
| ObjectInterEvent | 338 | 0.0 | 6.986 | 2837.91 | 371.005 | 430075.6 | 0.02 | 6 | 12 |
| TopographicMapEvent | 107 | 0.386 | 4.146 | 6480.428 | 1260.356 | 430338.541 | 0.01 | 0 | 7 |
| questEvent | 95 | 0.001 | 167.991 | 10098.082 | 83767.503 | 346584.752 | 0.01 | 15 | 17 |
| DaniEvent | 83 | 0.005 | 3.738 | 10401.304 | 84146.018 | 430347.074 | 0.01 | 6 | 11 |
| Soil Key Puzzle | 71 | 0.002 | 1.701 | 10929.712 | 22.729 | 604479.591 | 0.01 | 1 | 3 |
| soilMachine | 43 | 0.618 | 3.531 | 22.71 | 110.911 | 272.333 | 2.64 | 0 | 0 |
| DEBUGMenu | 40 | 8.274 | 542.658 | 23938.805 | 85419.191 | 346900.182 | 0.0 | 0 | 19 |
| argumentationAnswerEvent | 39 | 0.152 | 15.489 | 22397.368 | 172112.026 | 433972.067 | 0.0 | 0 | 5 |
| WaterChamberEvent | 24 | 0.934 | 11.989 | 22.495 | 60.344 | 86.071 | 2.67 | 0 | 0 |
| gameWindowFocusEvent | 23 | 2.292 | 1854.328 | 41697.953 | 86650.334 | 346912.391 | 0.0 | 0 | 17 |
| gameStartEvent | 18 | 223.553 | 6621.796 | 53196.94 | 125763.597 | 346912.391 | 0.0 | 0 | 16 |
| argumentationEvent | 14 | 0.037 | 139.435 | 62395.548 | 265043.518 | 433895.18 | 0.0 | 2 | 5 |
| chatEvent | 10 | 0.229 | 391.023 | 87415.304 | 466441.71 | 777844.8 | 0.0 | 0 | 5 |
| gameWindowUnfocusEvent | 8 | 1.131 | 50409.355 | 109030.364 | 394469.45 | 517034.888 | 0.0 | 0 | 6 |
| TerasGardenBox | 7 | 1.242 | 5.648 | 8.189 | 17.422 | 18.294 | 7.33 | 0 | 0 |
| EndOfUnit | 4 | 10160.756 | 172300.091 | 218487.445 | 479878.705 | 519188.84 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 1.949 | 3.059 | 3.079 | 4.111 | 4.228 | 19.49 | 0 | 0 |
| argumentationToolEvent | 3 | 2.9 | 17.303 | 230332.378 | 621880.967 | 690976.93 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 7 group(s), 11 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[2075] _id=6ac69293de269131f9bdead3 ts=2026-10-07T18:42:25.5050000Z == 6ab9a9279a8420a1e6b56b71.jsonl[2076] _id=6ac69293de269131f9bdead4 ts=2026-10-07T18:42:25.5050000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[4037] _id=6ac7e5e2de269131f9c590f4 ts=2026-10-08T18:50:08.5100000Z == 6ab9a9279a8420a1e6b56b71.jsonl[4038] _id=6ac7e5e2de269131f9c590f5 ts=2026-10-08T18:50:08.5100000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[4731] _id=6ac92f2bde269131f9cadcae ts=2026-10-09T18:15:05.6200000Z == 6ab9a9279a8420a1e6b56b71.jsonl[4732] _id=6ac92f2bde269131f9cadcaf ts=2026-10-09T18:15:05.6200000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 112 group(s), 176 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[895] _id=6ac54611de269131f9b7369d ts=2026-10-06T19:03:42.9730000Z == 6ab9a9279a8420a1e6b56b71.jsonl[879] _id=6ac54611de269131f9b736a1 ts=2026-10-06T19:03:42.9730000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[880] _id=6ac54612de269131f9b736b5 ts=2026-10-06T19:03:43.6800000Z == 6ab9a9279a8420a1e6b56b71.jsonl[897] _id=6ac54612de269131f9b736bf ts=2026-10-06T19:03:43.6800000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[900] _id=6ac54614de269131f9b736fc ts=2026-10-06T19:03:46.4630000Z == 6ab9a9279a8420a1e6b56b71.jsonl[901] _id=6ac54614de269131f9b736ff ts=2026-10-06T19:03:46.4630000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a9279a8420a1e6b56b71.jsonl[107] _id=6ac3f7afde269131f9af6e9f ts=2026-10-05T19:17:02.0180000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[78] _id=6ac3f7afde269131f9af6ea1 ts=2026-10-05T19:17:02.0240000Z`; `6ms: 6ab9a9279a8420a1e6b56b71.jsonl[166] _id=6ac53ec6de269131f9b67b59 ts=2026-10-06T18:32:37.2720000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[167] _id=6ac53ec6de269131f9b67b5b ts=2026-10-06T18:32:37.2780000Z`; `739ms: 6ab9a9279a8420a1e6b56b71.jsonl[430] _id=6ac54250de269131f9b6e747 ts=2026-10-06T18:47:43.2470000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[432] _id=6ac54251de269131f9b6e765 ts=2026-10-06T18:47:43.9860000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 102 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `491ms: 6ab9a9279a8420a1e6b56b71.jsonl[879] _id=6ac54611de269131f9b736a1 ts=2026-10-06T19:03:42.9730000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[896] _id=6ac54612de269131f9b736af ts=2026-10-06T19:03:43.4640000Z`; `216ms: 6ab9a9279a8420a1e6b56b71.jsonl[896] _id=6ac54612de269131f9b736af ts=2026-10-06T19:03:43.4640000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[880] _id=6ac54612de269131f9b736b5 ts=2026-10-06T19:03:43.6800000Z`; `431ms: 6ab9a9279a8420a1e6b56b71.jsonl[910] _id=6ac54620de269131f9b738cd ts=2026-10-06T19:03:57.8040000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[919] _id=6ac54620de269131f9b738d2 ts=2026-10-06T19:03:58.2350000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `510ms: 6ab9a9279a8420a1e6b56b71.jsonl[1967] _id=6ac548dbde269131f9b78ba1 ts=2026-10-06T19:15:38.1610000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[1968] _id=6ac548dbde269131f9b78baf ts=2026-10-06T19:15:38.6710000Z`; `445ms: 6ab9a9279a8420a1e6b56b71.jsonl[5447] _id=6ace7c81de269131f9d1207a ts=2026-10-13T18:46:24.3030000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[5448] _id=6ace7c81de269131f9d1207e ts=2026-10-13T18:46:24.7480000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `262ms: 6ab9a9279a8420a1e6b56b71.jsonl[12125] _id=6ad26f60de269131f9e72d06 ts=2026-10-16T18:39:27.8920000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[12126] _id=6ad26f60de269131f9e72d0c ts=2026-10-16T18:39:28.1540000Z`; `152ms: 6ab9a9279a8420a1e6b56b71.jsonl[12126] _id=6ad26f60de269131f9e72d0c ts=2026-10-16T18:39:28.1540000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[12124] _id=6ad26f60de269131f9e72d12 ts=2026-10-16T18:39:28.3060000Z`; `205ms: 6ab9a9279a8420a1e6b56b71.jsonl[12124] _id=6ad26f60de269131f9e72d12 ts=2026-10-16T18:39:28.3060000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[12127] _id=6ad26f61de269131f9e72d16 ts=2026-10-16T18:39:28.5110000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `38ms: 6ab9a9279a8420a1e6b56b71.jsonl[7750] _id=6acfced8de269131f9d79a82 ts=2026-10-14T18:50:00.0680000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[7753] _id=6acfced8de269131f9d79a85 ts=2026-10-14T18:50:00.1060000Z`; `37ms: 6ab9a9279a8420a1e6b56b71.jsonl[12193] _id=6ad26fbcde269131f9e7357d ts=2026-10-16T18:40:59.8890000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[12198] _id=6ad26fbcde269131f9e73580 ts=2026-10-16T18:40:59.9260000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6ab9a9279a8420a1e6b56b71.jsonl[525] _id=6ac54391de269131f9b70752 ts=2026-10-06T18:53:03.6800000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[539] _id=6ac54391de269131f9b70755 ts=2026-10-06T18:53:03.7070000Z`; `464ms: 6ab9a9279a8420a1e6b56b71.jsonl[550] _id=6ac54393de269131f9b7077d ts=2026-10-06T18:53:06.2850000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[551] _id=6ac54393de269131f9b70783 ts=2026-10-06T18:53:06.7490000Z`; `24ms: 6ab9a9279a8420a1e6b56b71.jsonl[563] _id=6ac5439bde269131f9b707f9 ts=2026-10-06T18:53:14.1510000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[560] _id=6ac5439bde269131f9b707fb ts=2026-10-06T18:53:14.1750000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6ab9a9279a8420a1e6b56b71.jsonl[13844] _id=6ad29806de269131f9e833d9 ts=2026-10-16T21:32:53.0240000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[13845] _id=6ad29806de269131f9e833da ts=2026-10-16T21:32:53.0250000Z`; `5ms: 6ab9a9279a8420a1e6b56b71.jsonl[13918] _id=6ad29984de269131f9e836e0 ts=2026-10-16T21:39:15.1230000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[13919] _id=6ad29984de269131f9e836e2 ts=2026-10-16T21:39:15.1280000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `743ms: 6ab9a9279a8420a1e6b56b71.jsonl[10257] _id=6ad122abde269131f9dfa80f ts=2026-10-15T18:59:55.0150000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[10258] _id=6ad122acde269131f9dfa828 ts=2026-10-15T18:59:55.7580000Z`; `790ms: 6ab9a9279a8420a1e6b56b71.jsonl[10258] _id=6ad122acde269131f9dfa828 ts=2026-10-15T18:59:55.7580000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[10268] _id=6ad122acde269131f9dfa858 ts=2026-10-15T18:59:56.5480000Z`; `737ms: 6ab9a9279a8420a1e6b56b71.jsonl[10910] _id=6ad12570de269131f9e0175d ts=2026-10-15T19:11:44.2280000Z ~ 6ab9a9279a8420a1e6b56b71.jsonl[10914] _id=6ad12571de269131f9e0177e ts=2026-10-15T19:11:44.9650000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 96h 21m 
  - Evidence: 96h 21m: 6ab9a9279a8420a1e6b56b71.jsonl[4728] _id=6ac92f24de269131f9cadc46 ts=2026-10-09T18:15:00.4390000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5177] _id=6ace7a39de269131f9d0fb75 ts=2026-10-13T18:36:40.6210000Z; 24h 5m: 6ab9a9279a8420a1e6b56b71.jsonl[2071] _id=6ac6928ede269131f9bdea75 ts=2026-10-07T18:42:22.2270000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4019] _id=6ac7e555de269131f9c586f7 ts=2026-10-08T18:47:48.0080000Z; 23h 42m: 6ab9a9279a8420a1e6b56b71.jsonl[715] _id=6ac5451dde269131f9b72245 ts=2026-10-06T18:59:40.2460000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2066] _id=6ac69283de269131f9bde96f ts=2026-10-07T18:42:10.6690000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a9279a8420a1e6b56b71.jsonl[4474] _id=6ac7ea0fde269131f9c63df0 ts=2026-10-08T19:07:58.1590000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5252] _id=6ace7b1ade269131f9d10a4d ts=2026-10-13T18:40:25.2330000Z; 24h 5m: 6ab9a9279a8420a1e6b56b71.jsonl[2576] _id=6ac69734de269131f9bec3ba ts=2026-10-07T19:02:12.2240000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4469] _id=6ac7ea04de269131f9c63b69 ts=2026-10-08T19:07:47.3080000Z; 23h 53m: 6ab9a9279a8420a1e6b56b71.jsonl[8826] _id=6acfd3c7de269131f9d83953 ts=2026-10-14T19:11:02.9980000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[10557] _id=6ad123aade269131f9dfceaf ts=2026-10-15T19:04:10.1730000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.005s..0.008s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b71.jsonl[10571] _id=6ad123c9de269131f9dfd5a5 ts=2026-10-15T19:04:41.0390000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[10570] _id=6ad123c9de269131f9dfd5b1 ts=2026-10-15T19:04:41.0440000Z; 6ms: 6ab9a9279a8420a1e6b56b71.jsonl[10568] _id=6ad123bade269131f9dfd266 ts=2026-10-15T19:04:26.3560000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[10567] _id=6ad123bade269131f9dfd270 ts=2026-10-15T19:04:26.3620000Z; 8ms: 6ab9a9279a8420a1e6b56b71.jsonl[10559] _id=6ad123aede269131f9dfcfa9 ts=2026-10-15T19:04:13.9110000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[10560] _id=6ad123aede269131f9dfcfb7 ts=2026-10-15T19:04:13.9190000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 13m 
  - Evidence: 96h 13m: 6ab9a9279a8420a1e6b56b71.jsonl[5144] _id=6ac9311fde269131f9cae692 ts=2026-10-09T18:23:27.0610000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5183] _id=6ace7a57de269131f9d0fc50 ts=2026-10-13T18:37:10.5870000Z; 23h 32m: 6ab9a9279a8420a1e6b56b71.jsonl[4022] _id=6ac7e554de269131f9c586f5 ts=2026-10-07T19:17:39.586Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4040] _id=6ac7e5e2de269131f9c590f7 ts=2026-10-08T18:50:08.5300000Z; 23h 25m: 6ab9a9279a8420a1e6b56b71.jsonl[2058] _id=6ac54960de269131f9b79cb1 ts=2026-10-06T19:17:50.9420000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2112] _id=6ac692d3de269131f9bdf15d ts=2026-10-07T18:43:31.2490000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 731 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11871] _id=6ad26e46de269131f9e71014 ts=2026-10-16T18:34:46.0710000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11872] _id=6ad26e46de269131f9e71015 ts=2026-10-16T18:34:46.0710000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11936] _id=6ad26e91de269131f9e714d3 ts=2026-10-16T18:36:00.4350000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11937] _id=6ad26e91de269131f9e714d4 ts=2026-10-16T18:36:00.4350000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11980] _id=6ad26eb6de269131f9e71994 ts=2026-10-16T18:36:37.9380000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11981] _id=6ad26eb6de269131f9e71995 ts=2026-10-16T18:36:37.9380000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 13m 
  - Evidence: 144h 13m: 6ab9a9279a8420a1e6b56b71.jsonl[5175] _id=6ac9311fde269131f9cae690 ts=2026-10-09T18:23:27.0380000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[9064] _id=6ad11d34de269131f9def94d ts=2026-10-15T18:36:35.8780000Z; 71h 25m: 6ab9a9279a8420a1e6b56b71.jsonl[706] _id=6ac544bede269131f9b71c11 ts=2026-10-06T18:58:05.7640000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5175] _id=6ac9311fde269131f9cae690 ts=2026-10-09T18:23:27.0380000Z; 24h 17m: 6ab9a9279a8420a1e6b56b71.jsonl[9064] _id=6ad11d34de269131f9def94d ts=2026-10-15T18:36:35.8780000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[12571] _id=6ad272ebde269131f9e77261 ts=2026-10-16T18:54:34.7870000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6ab9a9279a8420a1e6b56b71.jsonl[5163] _id=6ac9310dde269131f9cae669 ts=2026-10-09T18:23:08.9020000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5228] _id=6ace7afede269131f9d108c0 ts=2026-10-13T18:39:57.3670000Z; 23h 40m: 6ab9a9279a8420a1e6b56b71.jsonl[3872] _id=6ac698f8de269131f9befa83 ts=2026-10-07T19:09:44.0380000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4036] _id=6ac7e5e2de269131f9c590f3 ts=2026-10-08T18:50:08.5090000Z; 23h 25m: 6ab9a9279a8420a1e6b56b71.jsonl[2035] _id=6ac54921de269131f9b795f3 ts=2026-10-06T19:16:47.9130000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2074] _id=6ac69293de269131f9bdead2 ts=2026-10-07T18:42:25.5020000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 110 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[10215] _id=6ad12268de269131f9df9f70 ts=2026-10-15T18:58:47.9100000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[10216] _id=6ad12268de269131f9df9f71 ts=2026-10-15T18:58:47.9100000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11556] _id=6ad25709de269131f9e63ef2 ts=2026-10-16T16:55:36.1900000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11557] _id=6ad25709de269131f9e63ef3 ts=2026-10-16T16:55:36.1900000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11557] _id=6ad25709de269131f9e63ef3 ts=2026-10-16T16:55:36.1900000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11558] _id=6ad25709de269131f9e63ef4 ts=2026-10-16T16:55:36.1900000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a9279a8420a1e6b56b71.jsonl[4641] _id=6ac7eba5de269131f9c67309 ts=2026-10-08T19:14:44.8800000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5312] _id=6ace7ba1de269131f9d110ce ts=2026-10-13T18:42:40.4800000Z; 24h 1m: 6ab9a9279a8420a1e6b56b71.jsonl[3692] _id=6ac69841de269131f9beeb23 ts=2026-10-07T19:06:41.2990000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4494] _id=6ac7ea30de269131f9c64598 ts=2026-10-08T19:08:31.5520000Z; 23h 48m: 6ab9a9279a8420a1e6b56b71.jsonl[1867] _id=6ac54791de269131f9b7685d ts=2026-10-06T19:10:07.8780000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2473] _id=6ac69675de269131f9bea6d0 ts=2026-10-07T18:59:01.3610000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11631] _id=6ad257afde269131f9e64b8a ts=2026-10-16T16:58:22.9160000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11632] _id=6ad257afde269131f9e64b8b ts=2026-10-16T16:58:22.9160000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11660] _id=6ad257f2de269131f9e64f79 ts=2026-10-16T16:59:29.0100000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11661] _id=6ad257f2de269131f9e64f7a ts=2026-10-16T16:59:29.0100000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[11773] _id=6ad26d6fde269131f9e7027c ts=2026-10-16T18:31:11.0720000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11774] _id=6ad26d6fde269131f9e7027d ts=2026-10-16T18:31:11.0720000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 23h 32m 
  - Evidence: 23h 32m: 6ab9a9279a8420a1e6b56b71.jsonl[4006] _id=6ac69acfde269131f9bf20c6 ts=2026-10-07T19:17:35.5190000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4035] _id=6ac7e5e2de269131f9c590f2 ts=2026-10-08T18:50:04.5020000Z; 23h 24m: 6ab9a9279a8420a1e6b56b71.jsonl[2057] _id=6ac5495dde269131f9b79cad ts=2026-10-06T19:17:48.4850000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2073] _id=6ac69293de269131f9bdead1 ts=2026-10-07T18:42:22.2410000Z; 23h 14m: 6ab9a9279a8420a1e6b56b71.jsonl[8995] _id=6acfd59bde269131f9d888f0 ts=2026-10-14T19:18:51.0330000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[9002] _id=6ad11c89de269131f9deed9f ts=2026-10-15T18:33:42.4230000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[5574] _id=6ace7e80de269131f9d13195 ts=2026-10-13T18:54:54.9450000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5578] _id=6ace8317de269131f9d1a7e7 ts=2026-10-13T18:54:54.945Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[6866] _id=6acfc92fde269131f9d70aef ts=2026-10-14T18:25:51.3190000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[6868] _id=6acfca50de269131f9d71291 ts=2026-10-14T18:25:51.319Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 34m 
  - Evidence: 120h 34m: 6ab9a9279a8420a1e6b56b71.jsonl[5100] _id=6ac930cade269131f9cae4fe ts=2026-10-09T18:22:00.7350000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[8047] _id=6acfd066de269131f9d7c29b ts=2026-10-14T18:56:37.1280000Z; 23h 51m: 6ab9a9279a8420a1e6b56b71.jsonl[1838] _id=6ac54771de269131f9b76621 ts=2026-10-06T19:09:35.2960000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2516] _id=6ac696dede269131f9beb9e3 ts=2026-10-07T19:00:44.6890000Z; 23h 45m: 6ab9a9279a8420a1e6b56b71.jsonl[8231] _id=6acfd0c2de269131f9d7cccf ts=2026-10-14T18:58:07.1240000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[9232] _id=6ad11edfde269131f9df2b22 ts=2026-10-15T18:43:42.9930000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1534 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[1007] _id=6ac5466ade269131f9b743b7 ts=2026-10-06T19:05:11.9770000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[1013] _id=6ac5466ade269131f9b743bb ts=2026-10-06T19:05:11.9770000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[1009] _id=6ac54669de269131f9b74391 ts=2026-10-06T19:05:11.7790000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[999] _id=6ac5466ade269131f9b7439d ts=2026-10-06T19:05:11.7790000Z; 0ms: 6ab9a9279a8420a1e6b56b71.jsonl[1010] _id=6ac5466ade269131f9b743aa ts=2026-10-06T19:05:11.8120000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[1011] _id=6ac5466ade269131f9b743af ts=2026-10-06T19:05:11.8120000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 54m 
  - Evidence: 167h 54m: 6ab9a9279a8420a1e6b56b71.jsonl[2494] _id=6ac696a6de269131f9beb065 ts=2026-10-07T18:59:49.7120000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[8004] _id=6acfcfe5de269131f9d7b3bb ts=2026-10-14T18:54:29.3030000Z; 23h 48m: 6ab9a9279a8420a1e6b56b71.jsonl[1862] _id=6ac54794de269131f9b76881 ts=2026-10-06T19:10:10.8590000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2472] _id=6ac69675de269131f9bea6c9 ts=2026-10-07T18:59:01.3550000Z; 23h 46m: 6ab9a9279a8420a1e6b56b71.jsonl[8033] _id=6acfd03cde269131f9d7bdbc ts=2026-10-14T18:55:56.4200000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[9190] _id=6ad11e99de269131f9df1f55 ts=2026-10-15T18:42:33.0910000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 6ab9a9279a8420a1e6b56b71.jsonl[2470] _id=6ac69698de269131f9beade1 ts=2026-10-07T18:59:35.6990000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2471] _id=6ac69698de269131f9beade2 ts=2026-10-07T18:59:35.7010000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a9279a8420a1e6b56b71.jsonl[4480] _id=6ac7ea19de269131f9c63fbe ts=2026-10-08T19:08:08.4250000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5255] _id=6ace7b1cde269131f9d10a66 ts=2026-10-13T18:40:26.9660000Z; 24h 6m: 6ab9a9279a8420a1e6b56b71.jsonl[2341] _id=6ac69568de269131f9be65f6 ts=2026-10-07T18:54:32.1840000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4354] _id=6ac7e880de269131f9c5f0dd ts=2026-10-08T19:01:19.4280000Z; 23h 30m: 6ab9a9279a8420a1e6b56b71.jsonl[1971] _id=6ac548ddde269131f9b78bee ts=2026-10-06T19:15:40.0490000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2169] _id=6ac6935ade269131f9be021a ts=2026-10-07T18:45:46.0740000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 32m 
  - Evidence: 120h 32m: 6ab9a9279a8420a1e6b56b71.jsonl[4755] _id=6ac92f50de269131f9cadd52 ts=2026-10-09T18:15:44.2600000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[7760] _id=6acfce84de269131f9d79255 ts=2026-10-14T18:48:36.3270000Z; 48h 22m: 6ab9a9279a8420a1e6b56b71.jsonl[620] _id=6ac54427de269131f9b71345 ts=2026-10-06T18:55:34.0520000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4719] _id=6ac7ec69de269131f9c68893 ts=2026-10-08T19:18:00.3460000Z; 47h 44m: 6ab9a9279a8420a1e6b56b71.jsonl[7749] _id=6acfced8de269131f9d79a7b ts=2026-10-14T18:50:00.0440000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11870] _id=6ad26e46de269131f9e7100f ts=2026-10-16T18:34:46.0400000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 31m 
  - Evidence: 120h 31m: 6ab9a9279a8420a1e6b56b71.jsonl[4763] _id=6ac92f50de269131f9cadd54 ts=2026-10-09T18:15:44.2900000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[7682] _id=6acfce37de269131f9d78afb ts=2026-10-14T18:47:19.4700000Z; 48h 22m: 6ab9a9279a8420a1e6b56b71.jsonl[588] _id=6ac54427de269131f9b71347 ts=2026-10-06T18:55:34.0680000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4700] _id=6ac7ec52de269131f9c686c1 ts=2026-10-08T19:17:37.4600000Z; 47h 44m: 6ab9a9279a8420a1e6b56b71.jsonl[7753] _id=6acfced8de269131f9d79a85 ts=2026-10-14T18:50:00.1060000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11845] _id=6ad26e2cde269131f9e70c79 ts=2026-10-16T18:34:20.3070000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.037s..0.038s shown 
  - Evidence: 37ms: 6ab9a9279a8420a1e6b56b71.jsonl[12193] _id=6ad26fbcde269131f9e7357d ts=2026-10-16T18:40:59.8890000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[12198] _id=6ad26fbcde269131f9e73580 ts=2026-10-16T18:40:59.9260000Z; 38ms: 6ab9a9279a8420a1e6b56b71.jsonl[7750] _id=6acfced8de269131f9d79a82 ts=2026-10-14T18:50:00.0680000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[7753] _id=6acfced8de269131f9d79a85 ts=2026-10-14T18:50:00.1060000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 31m 
  - Evidence: 120h 31m: 6ab9a9279a8420a1e6b56b71.jsonl[4762] _id=6ac92f4ede269131f9cadd4e ts=2026-10-09T18:15:42.4270000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[7677] _id=6acfce36de269131f9d78a93 ts=2026-10-14T18:47:17.7800000Z; 47h 44m: 6ab9a9279a8420a1e6b56b71.jsonl[7843] _id=6acfced7de269131f9d79a5e ts=2026-10-14T18:49:58.6970000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11849] _id=6ad26e2fde269131f9e70cd5 ts=2026-10-16T18:34:22.6970000Z; 24h 15m: 6ab9a9279a8420a1e6b56b71.jsonl[2574] _id=6ac69730de269131f9bec36e ts=2026-10-07T19:02:08.2110000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4701] _id=6ac7ec57de269131f9c68726 ts=2026-10-08T19:17:42.5840000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 54 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b71.jsonl[7720] _id=6acfce64de269131f9d78f7d ts=2026-10-14T18:48:04.3080000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[7716] _id=6acfce64de269131f9d78f80 ts=2026-10-14T18:48:04.3120000Z; 6ms: 6ab9a9279a8420a1e6b56b71.jsonl[11887] _id=6ad26e61de269131f9e711bf ts=2026-10-16T18:35:12.8040000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11886] _id=6ad26e61de269131f9e711c5 ts=2026-10-16T18:35:12.8100000Z; 7ms: 6ab9a9279a8420a1e6b56b71.jsonl[558] _id=6ac5439bde269131f9b707ed ts=2026-10-06T18:53:13.8340000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[562] _id=6ac5439bde269131f9b707f5 ts=2026-10-06T18:53:13.8410000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 56m 
  - Evidence: 191h 56m: 6ab9a9279a8420a1e6b56b71.jsonl[545] _id=6ac5438cde269131f9b70709 ts=2026-10-06T18:52:59.4770000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[7796] _id=6acfceacde269131f9d79631 ts=2026-10-14T18:49:16.4070000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 216h 4m 
  - Evidence: 216h 4m: 6ab9a9279a8420a1e6b56b71.jsonl[742] _id=6ac5453fde269131f9b7250d ts=2026-10-06T19:00:14.2820000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[10563] _id=6ad123b3de269131f9dfd0f8 ts=2026-10-15T19:04:19.0820000Z; 23h 50m: 6ab9a9279a8420a1e6b56b71.jsonl[10565] _id=6ad123b5de269131f9dfd156 ts=2026-10-15T19:04:20.8960000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[12576] _id=6ad27303de269131f9e7742e ts=2026-10-16T18:54:58.8300000Z; 2h 15m: 6ab9a9279a8420a1e6b56b71.jsonl[12576] _id=6ad27303de269131f9e7742e ts=2026-10-16T18:54:58.8300000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[12926] _id=6ad292c6de269131f9e8279c ts=2026-10-16T21:10:29.3320000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 96h 21m 
  - Evidence: 96h 21m: 6ab9a9279a8420a1e6b56b71.jsonl[4725] _id=6ac92f18de269131f9cadb9f ts=2026-10-09T18:14:48.5580000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5179] _id=6ace7a39de269131f9d0fb78 ts=2026-10-13T18:36:40.9490000Z; 24h 5m: 6ab9a9279a8420a1e6b56b71.jsonl[2068] _id=6ac69283de269131f9bde971 ts=2026-10-07T18:42:10.8100000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4021] _id=6ac7e555de269131f9c586f9 ts=2026-10-08T18:47:48.1490000Z; 23h 58m: 6ab9a9279a8420a1e6b56b71.jsonl[6990] _id=6acfcb41de269131f9d71edf ts=2026-10-14T18:34:41.2430000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[8999] _id=6ad11c63de269131f9deec0e ts=2026-10-15T18:33:06.6540000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 96h 21m 
  - Evidence: 96h 21m: 6ab9a9279a8420a1e6b56b71.jsonl[4724] _id=6ac92f18de269131f9cadb9e ts=2026-10-09T18:14:48.5580000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5178] _id=6ace7a39de269131f9d0fb77 ts=2026-10-13T18:36:40.9490000Z; 24h 5m: 6ab9a9279a8420a1e6b56b71.jsonl[2067] _id=6ac69283de269131f9bde970 ts=2026-10-07T18:42:10.8100000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4020] _id=6ac7e555de269131f9c586f8 ts=2026-10-08T18:47:48.1480000Z; 23h 51m: 6ab9a9279a8420a1e6b56b71.jsonl[7468] _id=6acfccf7de269131f9d75d98 ts=2026-10-14T18:41:59.3530000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[8998] _id=6ad11c63de269131f9deec0d ts=2026-10-15T18:33:06.6540000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a9279a8420a1e6b56b71.jsonl[4016] _id=6ac69ad5de269131f9bf20d7 ts=2026-10-07T19:17:40.6110000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5579] _id=6ace8317de269131f9d1a7e8 ts=2026-10-13T18:54:55.499Z; 46h 20m: 6ab9a9279a8420a1e6b56b71.jsonl[7460] _id=6acfccf6de269131f9d75d2f ts=2026-10-14T18:41:57.8990000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[11721] _id=6ad258b7de269131f9e65ae7 ts=2026-10-16T17:02:45.8220000Z; 23h 59m: 6ab9a9279a8420a1e6b56b71.jsonl[2065] _id=6ac69283de269131f9bde969 ts=2026-10-06T19:17:57.182Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4016] _id=6ac69ad5de269131f9bf20d7 ts=2026-10-07T19:17:40.6110000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6ab9a9279a8420a1e6b56b71.jsonl[5165] _id=6ac93119de269131f9cae682 ts=2026-10-09T18:23:21.0760000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[5224] _id=6ace7af2de269131f9d10841 ts=2026-10-13T18:39:45.8280000Z; 23h 37m: 6ab9a9279a8420a1e6b56b71.jsonl[3936] _id=6ac699c4de269131f9bf0b0c ts=2026-10-07T19:13:08.0800000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[4042] _id=6ac7e5e2de269131f9c590f9 ts=2026-10-08T18:50:08.5740000Z; 23h 24m: 6ab9a9279a8420a1e6b56b71.jsonl[2061] _id=6ac54960de269131f9b79caf ts=2026-10-06T19:17:50.9300000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[2077] _id=6ac69293de269131f9bdead5 ts=2026-10-07T18:42:25.5570000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b71.jsonl[13844] _id=6ad29806de269131f9e833d9 ts=2026-10-16T21:32:53.0240000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[13845] _id=6ad29806de269131f9e833da ts=2026-10-16T21:32:53.0250000Z; 5ms: 6ab9a9279a8420a1e6b56b71.jsonl[13435] _id=6ad29517de269131f9e82d89 ts=2026-10-16T21:20:21.8040000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[13429] _id=6ad29517de269131f9e82d8b ts=2026-10-16T21:20:21.8090000Z; 5ms: 6ab9a9279a8420a1e6b56b71.jsonl[13918] _id=6ad29984de269131f9e836e0 ts=2026-10-16T21:39:15.1230000Z -> 6ab9a9279a8420a1e6b56b71.jsonl[13919] _id=6ad29984de269131f9e836e2 ts=2026-10-16T21:39:15.1280000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[632] _id=6ac54439de269131f9b71451 ts=2026-10-06T18:55:52.2250000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[2340] _id=6ac69567de269131f9be65b1 ts=2026-10-07T18:54:31.1880000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[3777] _id=6ac698dade269131f9bef76b ts=2026-10-07T19:09:13.9660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 23 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[1053] _id=6ac54675de269131f9b74597 ts=2026-10-06T19:05:23.7900000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[905] _id=6ac54679de269131f9b74624 ts=2026-10-06T19:05:27.0840000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[1048] _id=6ac54679de269131f9b7462d ts=2026-10-06T19:05:28.0720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 88 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[882] _id=6ac54611de269131f9b73699 ts=2026-10-06T19:03:42.7790000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[879] _id=6ac54611de269131f9b736a1 ts=2026-10-06T19:03:42.9730000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[896] _id=6ac54612de269131f9b736af ts=2026-10-06T19:03:43.4640000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[7753] _id=6acfced8de269131f9d79a85 ts=2026-10-14T18:50:00.1060000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[12198] _id=6ad26fbcde269131f9e73580 ts=2026-10-16T18:40:59.9260000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[539] _id=6ac54391de269131f9b70755 ts=2026-10-06T18:53:03.7070000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[560] _id=6ac5439bde269131f9b707fb ts=2026-10-06T18:53:14.1750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[12576] _id=6ad27303de269131f9e7742e ts=2026-10-16T18:54:58.8300000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[12926] _id=6ad292c6de269131f9e8279c ts=2026-10-16T21:10:29.3320000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[13538] _id=6ad295d2de269131f9e82e9f ts=2026-10-16T21:23:28.5840000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[10739] _id=6ad12498de269131f9dff688 ts=2026-10-15T19:08:08.6170000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 147 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[1002] _id=6ac54674de269131f9b74571 ts=2026-10-06T19:05:21.5090000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[1041] _id=6ac54674de269131f9b74575 ts=2026-10-06T19:05:21.5380000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[1066] _id=6ac5467bde269131f9b74671 ts=2026-10-06T19:05:28.6890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 371 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[980] _id=6ac54664de269131f9b7424a ts=2026-10-06T19:03:46.1860000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[901] _id=6ac54614de269131f9b736ff ts=2026-10-06T19:03:46.4630000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[770] _id=6ac54614de269131f9b73703 ts=2026-10-06T19:03:46.4630000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[4746] _id=6ac92f36de269131f9cadd09 ts=2026-10-09T18:15:18.7070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 29 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[561] _id=6ac5439cde269131f9b70801 ts=2026-10-06T18:53:14.4670000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[601] _id=6ac5440bde269131f9b7113d ts=2026-10-06T18:55:06.7060000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[600] _id=6ac5440cde269131f9b71149 ts=2026-10-06T18:55:07.3430000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 489 start, 478 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 30 unmatched 'BecameCameraCentered' (totals: 658 open, 651 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 35 unmatched 'BecameVisible' (totals: 850 open, 903 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 211 open, 212 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 57 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 411 of 14090 adjacent _id pairs reverse in client time; worst 85.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b71.jsonl[864] _id=6ac54662de269131f9b741d8 ts=2026-10-06T19:05:05.0710000Z`; `6ab9a9279a8420a1e6b56b71.jsonl[966] _id=6ac54663de269131f9b741fa ts=2026-10-06T19:03:39.6220000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.72s, min -84609.37s, max -0.24s over 14091 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b71\coverage.yaml

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

### `InputEvent` — 5050 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1777); Unit 2 Prod (Refactor) (1038); Unit 4 Dev - Dungeon (1002); Unit 3 Dungeon Dev (349); Unit 4 Dev (289); Unit 5 Dev - Dungeon (275); Unit 1 Dev (143); Unit 5 Dev (100); Unit 4 Dev - Anderson Base (77)
- **Intervals:** median 0.86s (p5 0.12s / p95 10.03s, n=5049)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5050/5050 records)
    "pressed"  x5050
data.actionType  (string, 5050/5050 records)
    "Move"  x2875
    "Interact"  x693
    "Sprint"  x626
    "Jump"  x603
    "Ascend"  x109
    "Hoverboard"  x79
    "Descend"  x46
    "Pause"  x16
    "SkipCinematic"  x3
data.key  (string, 5050/5050 records, 22 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5050/5050 records)
    "Player"  x3682
    "Drone"  x1368
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3062 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2028); Unit 5 Dev - Dungeon (444); Unit 4 Dev (442); Unit 3 Dungeon Dev (148)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.38s, n=3061)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3062/3062 records)
    "BecameInvisible"  x903
    "BecameVisible"  x850
    "BecameCameraCentered"  x658
    "BecameCameraUncentered"  x651
data.pieceId  (string, 3062/3062 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3062/3062 records)
    1894 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2540 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (659); Unit 3 Dev (603); Unit 4 Dev (265); Unit 1 Dev (239); Unit 5 Dev (219); Unit 4 Dev - Anderson Base (206); Unit 4 Dev - Dungeon (152); Unit 3 Dungeon Dev (118); Unit 5 Dev - Dungeon (79)
- **eventKey:** present on 1573 of 2540 records
- **Intervals:** median 3.68s (p5 0.00s / p95 25.80s, n=2539)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1573; [conversationId, dialogueEventType] x967
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2540/2540 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2540/2540 records)
    "DialogueNodeEvent"  x1573
    "DialogueStartEvent"  x489
    "DialogueFinishEvent"  x478
data.nodeId  (number, 1573/2540 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1991 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (532); Unit 3 Dev (465); Unit 1 Dev (198); Unit 4 Dev (197); Unit 4 Dev - Dungeon (179); Unit 4 Dev - Anderson Base (121); Unit 5 Dev (121); Unit 5 Dev - Dungeon (104); Unit 3 Dungeon Dev (74)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.20s, n=1979)
- **Fields under `data`:**

```text
data.position  (object, 1991/1991 records)
data.position.x  (number, 1991/1991 records)
    numeric range -694.72 .. 1557.6 (671 unique)
data.position.y  (number, 1991/1991 records)
    numeric range -112.615 .. 221.745 (492 unique)
data.position.z  (number, 1991/1991 records)
    numeric range -1161.51 .. 1771.71 (671 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 500 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (199); Unit 3 Dev (109); Unit 5 Dev (78); Unit 1 Dev (64); Unit 2 Prod (Refactor) (50)
- **Intervals:** median 0.66s (p5 0.03s / p95 10.49s, n=499)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 500/500 records)
    "argumentationNodeHoverEnd"  x212
    "argumentationNodeHoverStart"  x211
    "argumentationNodeAdd"  x49
    "argumentationNodeRemove"  x28
data.argumentationTitle  (string, 500/500 records)
    "Unit 4 - Flooding"  x199
    "Unit 3 - Pollution Upstream"  x109
    "Unit 5"  x78
    "Unit 2 – Watershed"  x50
    "Unit 1 - Argumentation Tutorial"  x41
    "Unit 1 - Freshwater"  x23
data.nodeName  (string, 500/500 records)
    "B"  x85
    "A"  x84
    "I"  x63
    "C"  x54
    "1"  x52
    "D"  x44
    "2"  x33
    "II"  x27
    "4"  x24
    "3"  x23
    "5"  x11
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 339 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (167); Unit 2 Prod (Refactor) (39); Unit 3 Dungeon Dev (31); Unit 5 Dev - Dungeon (24); Unit 4 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 1 Dev (16); Unit 5 Dev (14); Unit 3 Dev (12)
- **Intervals:** median 6.99s (p5 0.82s / p95 371.01s, n=338)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 339/339 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 339/339 records)
    111 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 108 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (72); Unit 2 Prod (Refactor) (34); Unit 1 Dev (2)
- **Intervals:** median 4.15s (p5 0.76s / p95 1260.36s, n=107)
- **`data` key-set variants:** [actionType, featureUsed] x66; [actionType, featureUsed, legendName] x23; [actionType, featureUsed, location] x19
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 108/108 records)
    "MapCloseEvent"  x33
    "MapOpenEvent"  x33
    "Selected"  x17
    "WaypointMoveEvent"  x15
    "Unselected"  x6
    "WaypointSetEvent"  x4
data.featureUsed  (string, 108/108 records)
    "Map"  x66
    "Legend"  x23
    "Waypoint"  x19
data.legendName  (string, 23/108 records)
    "360 ft"  x7
    "Water"  x4
    "330 ft"  x3
    "60 ft"  x3
    "90 ft"  x2
    "0 ft"  x1
    "150 ft"  x1
    "30 ft"  x1
    "300 ft"  x1
data.location  (object, 19/108 records)
data.location.x  (number, 19/108 records)
    numeric range -353.153 .. 126.261 (15 unique)
data.location.y  (number, 19/108 records)
    numeric range -277.394 .. 128.298 (17 unique)
data.location.z  (number, 19/108 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 96 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (20); Unit 2 Prod (Refactor) (18); Unit 4 Dev - Dungeon (15); Unit 1 Dev (13); Unit 4 Dev (9); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 96 of 96 records
- **Intervals:** median 167.99s (p5 0.01s / p95 83767.50s, n=95)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 96/96 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x39
data.questID  (string, 96/96 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 96/96 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/96 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DaniEvent` — 84 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (44); Unit 2 Prod (Refactor) (20); Unit 4 Dev - Dungeon (12); Unit 1 Dev (8)
- **Intervals:** median 3.74s (p5 0.01s / p95 84146.02s, n=83)
- **Fields under `data`:**

```text
data.actionType  (string, 84/84 records)
    "Close"  x42
    "Open"  x42
data.toolName  (string, 84/84 records, 78 empty-string)
    ""  x78
    "Settings"  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `Soil Key Puzzle` — 72 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 4 Dev (24); Unit 3 Dev (18)
- **Intervals:** median 1.70s (p5 0.16s / p95 22.73s, n=71)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x64; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/72 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/72 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 64/72 records)
    "RightDrag"  x35
    "LeftDrag"  x29
data.currentSoilType  (string, 64/72 records)
    "CLAYSAND"  x13
    "SAND"  x13
    "CLAY"  x11
    "SANDGRAVEL"  x11
    "CLAYROCK"  x8
    "GRAVEL"  x5
    "BEDROCK"  x3
data.isCorrectSelection  (string, 64/72 records)
    "false"  x48
    "true"  x16
data.waterLevelStatus  (string, 64/72 records)
    "TooHigh"  x27
    "TooLow"  x21
    "Proper"  x16
data.waterRetentionChange  (string, 64/72 records)
    "Decrease"  x26
    "Increase"  x22
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `soilMachine` — 44 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (44)
- **Intervals:** median 3.53s (p5 0.71s / p95 110.91s, n=43)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "ChangeCanister"  x44
data.canisterType  (string, 44/44 records)
    "Clay"  x20
    "Bedrock"  x14
    "Gravel"  x8
    "Sand"  x2
data.floor  (string, 44/44 records)
    "5"  x34
    "4"  x9
    "3"  x1
data.machine  (string, 44/44 records)
    "1"  x43
    "2"  x1
data.row  (string, 44/44 records)
    "BottomRow"  x24
    "TopRow"  x20
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 41 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (16); Unit 3 Dev (7); Unit 2 Prod (Refactor) (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 542.66s (p5 8.68s / p95 85419.19s, n=40)
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "DebugMenuStateChanged"  x41
data.isOpened  (bool, 41/41 records)
    false  x41
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 40 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (24); Unit 3 Dev (8); Unit 5 Dev (4); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 15.49s (p5 0.26s / p95 172112.03s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "submitAnswerEvent"  x40
data.answerSubmitted  (string, 40/40 records)
    28 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 40/40 records)
    "Unit 4 - Flooding"  x24
    "Unit 3 - Pollution Upstream"  x8
    "Unit 5"  x4
    "Unit 2 – Watershed"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 25 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (25)
- **Intervals:** median 11.99s (p5 1.13s / p95 60.34s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "On"  x19
    "Off"  x6
data.floor  (string, 25/25 records)
    "3"  x8
    "4"  x8
    "1"  x6
    "2"  x3
data.machineNumber  (string, 25/25 records)
    "One"  x24
    "Two"  x1
data.machineType  (string, 25/25 records)
    "Evaporator"  x11
    "Condenser"  x9
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 25/25 records)
    "2"  x12
    "3"  x7
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 24 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 1854.33s (p5 33.88s / p95 86650.33s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 6621.80s (p5 238.69s / p95 125763.60s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 139.44s (p5 0.04s / p95 265043.52s, n=14)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 11 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 391.02s (p5 0.86s / p95 466441.71s, n=10)
- **`data` key-set variants:** [actionType, chatID] x10; [actionKey, chatID] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 1/11 records)
    "ScrollStop"  x1
data.actionType  (string, 10/11 records)
    "Close"  x6
    "Open"  x3
    "ScrollStart"  x1
data.chatID  (string, 11/11 records)
    "NA"  x7
    "[30-48, 30-49, 30-50, 30-56, 30-57]"  x2
    "[16-3]"  x1
    "[91-88, 91-90, 91-92, 91-98, 91-99]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `gameWindowUnfocusEvent` — 9 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 50409.35s (p5 158.62s / p95 394469.45s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 9/9 records)
    false  x9
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 5.65s (p5 1.28s / p95 17.42s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x4
data.boxId  (string, 8/8 records)
    "0"  x3
    "1"  x3
    "2"  x2
data.soilType  (string, 8/8 records)
    "Gravel"  x3
    "Clay"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 172300.09s (p5 21758.48s / p95 479878.71s, n=4)
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

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 3.06s (p5 2.06s / p95 4.11s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted Out"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Covered"  x1
    "Hot"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 17.30s (p5 4.34s / p95 621880.97s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (30 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (17x); "Unselected" (6x); "WaypointMoveEvent" (15x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (23x); "Waypoint" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (28x)
- `soilMachine` data.canisterType: "Bedrock" (14x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*