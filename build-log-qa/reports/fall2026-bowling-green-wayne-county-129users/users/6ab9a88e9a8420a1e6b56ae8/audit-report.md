# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae8

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae8
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae8.jsonl
- **Records:** 16353 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae8
- **Time span:** 2026-10-06T13:23:36.783000+00:00 .. 2026-10-19T02:55:00.584000+00:00 (301h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae8\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 16353 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 101 INFO, 0 NOT_TESTED, 92 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4614 | 28.22 | 1 | 8 | 0 | 2026-10-06T13:23:49.031000+00:00 | 2026-10-19T02:23:09.205000+00:00 | 300h 59m |
| PuzzlePieceVisibleEvent | 4528 | 27.69 | 1 | 4 | 0 | 2026-10-07T13:31:27.948000+00:00 | 2026-10-19T02:14:17.028000+00:00 | 276h 42m |
| PlayerPositionEvent | 3427 | 20.96 | 1 | 8 | 0 | 2026-10-06T13:23:45.515000+00:00 | 2026-10-19T02:55:00.584000+00:00 | 301h 31m |
| DialogueEvent | 2315 | 14.16 | 1 | 8 | 1421 | 2026-10-06T13:24:05.510000+00:00 | 2026-10-19T02:23:55.058000+00:00 | 300h 59m |
| argumentationNodeEvent | 677 | 4.14 | 1 | 4 | 0 | 2026-10-06T13:51:50.890000+00:00 | 2026-10-19T01:00:04.710000+00:00 | 299h 8m |
| ObjectInterEvent | 281 | 1.72 | 1 | 8 | 0 | 2026-10-06T13:31:01.229000+00:00 | 2026-10-19T02:22:51.991000+00:00 | 300h 51m |
| Soil Key Puzzle | 153 | 0.94 | 1 | 3 | 0 | 2026-10-07T13:44:29.215000+00:00 | 2026-10-18T21:26:42.922000+00:00 | 271h 42m |
| questEvent | 83 | 0.51 | 1 | 8 | 83 | 2026-10-06T13:24:05.483000+00:00 | 2026-10-19T02:20:21.868000+00:00 | 300h 56m |
| argumentationAnswerEvent | 68 | 0.42 | 1 | 4 | 0 | 2026-10-06T13:52:04.219000+00:00 | 2026-10-19T01:00:10.987000+00:00 | 299h 8m |
| TopographicMapEvent | 47 | 0.29 | 1 | 3 | 0 | 2026-10-07T13:31:51.194000+00:00 | 2026-10-16T13:53:14.670000+00:00 | 216h 21m |
| DEBUGMenu | 41 | 0.25 | 1 | 9 | 0 | 2026-10-06T13:23:45.495000+00:00 | 2026-10-19T02:02:18.577000+00:00 | 300h 38m |
| gameWindowFocusEvent | 22 | 0.13 | 1 | 4 | 0 | 2026-10-06T13:23:36.783000+00:00 | 2026-10-19T02:02:12.139000+00:00 | 300h 38m |
| gameStartEvent | 19 | 0.12 | 1 | 1 | 0 | 2026-10-06T13:23:36.784000+00:00 | 2026-10-19T02:02:12.139000+00:00 | 300h 38m |
| TerasGardenBox | 15 | 0.09 | 1 | 1 | 0 | 2026-10-19T01:27:29.851000+00:00 | 2026-10-19T01:46:12.221000+00:00 | 18m 42s |
| WaterChamberEvent | 13 | 0.08 | 1 | 1 | 0 | 2026-10-19T02:09:47.437000+00:00 | 2026-10-19T02:22:40.419000+00:00 | 12m 52s |
| soilMachine | 13 | 0.08 | 1 | 1 | 0 | 2026-10-18T21:45:28.850000+00:00 | 2026-10-18T22:02:27.168000+00:00 | 16m 58s |
| argumentationEvent | 12 | 0.07 | 1 | 4 | 0 | 2026-10-06T13:51:44.222000+00:00 | 2026-10-19T01:00:11.058000+00:00 | 299h 8m |
| gameWindowUnfocusEvent | 10 | 0.06 | 1 | 5 | 0 | 2026-10-06T13:59:33.218000+00:00 | 2026-10-19T01:38:03.014000+00:00 | 299h 38m |
| DaniEvent | 6 | 0.04 | 1 | 2 | 0 | 2026-10-07T13:36:41.644000+00:00 | 2026-10-15T13:24:01.204000+00:00 | 191h 47m |
| EndOfUnit | 4 | 0.02 | 1 | 4 | 0 | 2026-10-06T13:57:05.112000+00:00 | 2026-10-19T02:01:50.600000+00:00 | 300h 4m |
| argumentationToolEvent | 4 | 0.02 | 1 | 2 | 0 | 2026-10-06T13:51:39.335000+00:00 | 2026-10-15T02:23:16.489000+00:00 | 204h 31m |
| chatEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-10-19T02:02:18.416000+00:00 | 2026-10-19T02:02:18.416000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 326005.701s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.263s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 17.574s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.07s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.88s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 11.12s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 43.81s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 6.416s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 408.581s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 113.222s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 25066.934s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 4117.473s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 84776.62s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.22s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.4x vs baseline. 
  - Observed: 41 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 4.0x vs baseline. 
  - Observed: 153 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — baseline categorical value(s) not seen this build. 
  - Observed: Two 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Condenser; DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.room` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 13.6x vs baseline. 
  - Observed: 68 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,I; A,2,II; A,3,II; A,4,II; B,2,II; B,C,1,I; C,1,I; C,2,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 677 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 10 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 53; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[154] _id=6ac4f8aade269131f9b0c9d2 ts=2026-10-06T13:33:29.9050000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[220] _id=6ac4fa3fde269131f9b1126d ts=2026-10-06T13:40:15.0000000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[275] _id=6ac4fad7de269131f9b12e1a ts=2026-10-06T13:42:47.3850000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[1] _id=6ac4f659de269131f9b063a4 ts=2026-10-06T13:23:36.7840000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[568] _id=6ac4fea5de269131f9b22d77 ts=2026-10-06T13:59:01.0970000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[584] _id=6ac64887de269131f9b8ff5b ts=2026-10-07T13:26:29.8790000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[2] _id=6ac4f659de269131f9b063a0 ts=2026-10-06T13:23:36.7830000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[569] _id=6ac4fea5de269131f9b22d6a ts=2026-10-06T13:59:01.0960000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[583] _id=6ac64887de269131f9b8ff5a ts=2026-10-07T13:26:29.8790000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[578] _id=6ac64887de269131f9b8ff40 ts=2026-10-06T13:59:33.218Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[2941] _id=6ace56bcde269131f9cf55bf ts=2026-10-07T13:59:45.87Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[2417] _id=6ac79b7bde269131f9c0594e ts=2026-10-08T13:32:42.4900000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4613 | 0.0 | 1.263 | 234.893 | 18.217 | 439719.141 | 0.26 | 91 | 17 |
| PuzzlePieceVisibleEvent | 4527 | 0.0 | 0.07 | 220.051 | 2.657 | 516602.141 | 0.27 | 1964 | 10 |
| PlayerPositionEvent | 3416 | 0.0 | 10.001 | 317.648 | 10.079 | 439641.006 | 0.19 | 1 | 14 |
| DialogueEvent | 2314 | 0.0 | 4.829 | 468.276 | 52.089 | 439696.486 | 0.13 | 667 | 15 |
| argumentationNodeEvent | 676 | 0.004 | 0.621 | 1593.038 | 13.895 | 736050.961 | 0.04 | 94 | 3 |
| ObjectInterEvent | 280 | 0.0 | 17.574 | 3868.253 | 836.186 | 516800.403 | 0.02 | 4 | 17 |
| Soil Key Puzzle | 152 | 0.175 | 1.88 | 6435.09 | 113.055 | 516604.224 | 0.01 | 0 | 6 |
| questEvent | 82 | 0.0 | 248.088 | 13211.907 | 74539.066 | 439983.076 | 0.0 | 10 | 28 |
| argumentationAnswerEvent | 67 | 0.179 | 6.416 | 16072.937 | 369.938 | 736061.735 | 0.0 | 0 | 3 |
| TopographicMapEvent | 46 | 0.017 | 11.12 | 16932.249 | 42717.556 | 562290.968 | 0.0 | 4 | 9 |
| DEBUGMenu | 40 | 6.591 | 1168.55 | 27057.827 | 92254.517 | 441190.984 | 0.0 | 0 | 23 |
| gameWindowFocusEvent | 21 | 54.223 | 4117.473 | 51538.826 | 199011.433 | 441147.872 | 0.0 | 0 | 18 |
| gameStartEvent | 18 | 168.322 | 25066.934 | 60128.631 | 235340.031 | 441202.095 | 0.0 | 0 | 17 |
| TerasGardenBox | 14 | 1.184 | 2.083 | 80.169 | 384.002 | 1005.685 | 0.75 | 0 | 1 |
| WaterChamberEvent | 12 | 3.057 | 43.81 | 64.415 | 205.465 | 321.132 | 0.93 | 0 | 0 |
| soilMachine | 12 | 1.626 | 7.22 | 84.86 | 376.499 | 406.571 | 0.71 | 0 | 0 |
| argumentationEvent | 11 | 0.047 | 408.581 | 97900.621 | 496621.264 | 736035.919 | 0.0 | 1 | 5 |
| gameWindowUnfocusEvent | 9 | 27.316 | 84776.62 | 119856.644 | 393245.436 | 520041.54 | 0.0 | 0 | 7 |
| DaniEvent | 5 | 1.117 | 3.014 | 138087.912 | 529249.943 | 651938.688 | 0.0 | 0 | 2 |
| EndOfUnit | 3 | 17450.195 | 326005.701 | 360095.163 | 695747.203 | 736829.592 | 0.0 | 0 | 3 |
| argumentationToolEvent | 3 | 4.814 | 113.222 | 245432.385 | 662572.528 | 736179.118 | 0.0 | 0 | 1 |
| chatEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 8 group(s), 25 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[2409] _id=6ac79b60de269131f9c04f4d ts=2026-10-08T13:32:14.3970000Z == 6ab9a88e9a8420a1e6b56ae8.jsonl[2410] _id=6ac79b60de269131f9c04f4e ts=2026-10-08T13:32:14.3970000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[2945] _id=6ace56cdde269131f9cf55eb ts=2026-10-13T16:05:32.3350000Z == 6ab9a88e9a8420a1e6b56ae8.jsonl[2946] _id=6ace56cdde269131f9cf55ec ts=2026-10-13T16:05:32.3350000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[2949] _id=6ace56cdde269131f9cf55ef ts=2026-10-13T16:05:32.3360000Z == 6ab9a88e9a8420a1e6b56ae8.jsonl[2950] _id=6ace56cdde269131f9cf55f0 ts=2026-10-13T16:05:32.3360000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 94 group(s), 131 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[719] _id=6ac649fade269131f9b95e3a ts=2026-10-07T13:32:40.4390000Z == 6ab9a88e9a8420a1e6b56ae8.jsonl[720] _id=6ac649fade269131f9b95e45 ts=2026-10-07T13:32:40.4390000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[750] _id=6ac64a00de269131f9b96081 ts=2026-10-07T13:32:45.4270000Z == 6ab9a88e9a8420a1e6b56ae8.jsonl[751] _id=6ac64a00de269131f9b96086 ts=2026-10-07T13:32:45.4270000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[739] _id=6ac64a00de269131f9b96089 ts=2026-10-07T13:32:45.5090000Z == 6ab9a88e9a8420a1e6b56ae8.jsonl[741] _id=6ac64a01de269131f9b96093 ts=2026-10-07T13:32:45.5090000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[113] _id=6ac4f815de269131f9b0b635 ts=2026-10-06T13:31:01.2290000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[110] _id=6ac4f815de269131f9b0b637 ts=2026-10-06T13:31:01.2350000Z`; `616ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[10728] _id=6ad229b9de269131f9e3dede ts=2026-10-16T13:42:16.4460000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[10730] _id=6ad229b9de269131f9e3dee6 ts=2026-10-16T13:42:17.0620000Z`; `264ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[10730] _id=6ad229b9de269131f9e3dee6 ts=2026-10-16T13:42:17.0620000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[10721] _id=6ad229bade269131f9e3def7 ts=2026-10-16T13:42:17.3260000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `179ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[6093] _id=6ad038c3de269131f9da3cba ts=2026-10-15T02:21:54.7090000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[6092] _id=6ad038c3de269131f9da3cbe ts=2026-10-15T02:21:54.8880000Z`; `198ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[6092] _id=6ad038c3de269131f9da3cbe ts=2026-10-15T02:21:54.8880000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[6094] _id=6ad038c4de269131f9da3cc0 ts=2026-10-15T02:21:55.0860000Z`; `220ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[6094] _id=6ad038c4de269131f9da3cc0 ts=2026-10-15T02:21:55.0860000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[6095] _id=6ad038c4de269131f9da3cc2 ts=2026-10-15T02:21:55.3060000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `47ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[9207] _id=6ad179f8de269131f9e26b39 ts=2026-10-16T01:12:23.2540000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[9211] _id=6ad179f8de269131f9e26b3d ts=2026-10-16T01:12:23.3010000Z`; `52ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14853] _id=6ad56b9cde269131f9e9068e ts=2026-10-19T01:00:11.0060000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[14904] _id=6ad56b9cde269131f9e90692 ts=2026-10-19T01:00:11.0580000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 36 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[407] _id=6ac4fcf7de269131f9b1b511 ts=2026-10-06T13:51:51.4010000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[409] _id=6ac4fcf7de269131f9b1b515 ts=2026-10-06T13:51:51.4210000Z`; `54ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[418] _id=6ac4fcfdde269131f9b1b67d ts=2026-10-06T13:51:56.9680000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[419] _id=6ac4fcfdde269131f9b1b687 ts=2026-10-06T13:51:57.0220000Z`; `686ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[6009] _id=6ad03896de269131f9da3c02 ts=2026-10-15T02:21:09.1060000Z ~ 6ab9a88e9a8420a1e6b56ae8.jsonl[6011] _id=6ad03896de269131f9da3c08 ts=2026-10-15T02:21:09.7920000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 122h 33m 
  - Evidence: 122h 33m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2405] _id=6ac79b56de269131f9c04dc1 ts=2026-10-08T13:32:05.3720000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2938] _id=6ace56bcde269131f9cf55c1 ts=2026-10-13T16:05:16.3560000Z; 54h 53m: 6ab9a88e9a8420a1e6b56ae8.jsonl[10992] _id=6ad22be4de269131f9e41a92 ts=2026-10-16T13:51:32.3540000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11200] _id=6ad52fcede269131f9e8ba52 ts=2026-10-18T20:45:01.3870000Z; 24h 5m: 6ab9a88e9a8420a1e6b56ae8.jsonl[585] _id=6ac64895de269131f9b902d4 ts=2026-10-07T13:26:44.5680000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2404] _id=6ac79b4bde269131f9c04c04 ts=2026-10-08T13:31:54.1110000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 181h 5m 
  - Evidence: 181h 5m: 6ab9a88e9a8420a1e6b56ae8.jsonl[1252] _id=6ac64aedde269131f9b99a55 ts=2026-10-07T13:36:44.6580000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6479] _id=6ad03d90de269131f9da468a ts=2026-10-15T02:42:23.3460000Z; 10h 41m: 6ab9a88e9a8420a1e6b56ae8.jsonl[6478] _id=6ad03d92de269131f9da468c ts=2026-10-15T02:42:25.1240000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6755] _id=6ad0d3f0de269131f9da77e3 ts=2026-10-15T13:24:00.0870000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 122h 8m 
  - Evidence: 122h 8m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2931] _id=6ac7a13cde269131f9c150d1 ts=2026-10-08T13:57:15.8700000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2957] _id=6ace56cdde269131f9cf55f7 ts=2026-10-13T16:05:32.3560000Z; 54h 47m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11183] _id=6ad22daede269131f9e447d8 ts=2026-10-16T13:59:09.9460000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11247] _id=6ad5304bde269131f9e8ba9a ts=2026-10-18T20:47:06.4410000Z; 23h 35m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2395] _id=6ac65017de269131f9ba38da ts=2026-10-07T13:58:46.5580000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2430] _id=6ac79bc1de269131f9c0621a ts=2026-10-08T13:33:52.9180000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 667 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14522] _id=6ad569bede269131f9e900ed ts=2026-10-19T00:52:12.9330000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14523] _id=6ad569bede269131f9e900ee ts=2026-10-19T00:52:12.9330000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14657] _id=6ad56a89de269131f9e902d0 ts=2026-10-19T00:55:35.7480000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14658] _id=6ad56a89de269131f9e902d1 ts=2026-10-19T00:55:35.7480000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14691] _id=6ad56ab6de269131f9e90368 ts=2026-10-19T00:56:21.2330000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14692] _id=6ad56ab6de269131f9e90369 ts=2026-10-19T00:56:21.2330000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 204h 40m 
  - Evidence: 204h 40m: 6ab9a88e9a8420a1e6b56ae8.jsonl[474] _id=6ac4fe31de269131f9b20b5b ts=2026-10-06T13:57:05.1120000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6436] _id=6ad03c6fde269131f9da44d6 ts=2026-10-15T02:37:34.7040000Z; 90h 33m: 6ab9a88e9a8420a1e6b56ae8.jsonl[6436] _id=6ad03c6fde269131f9da44d6 ts=2026-10-15T02:37:34.7040000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11494] _id=6ad535e5de269131f9e8bc7f ts=2026-10-18T21:11:00.4050000Z; 4h 50m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11494] _id=6ad535e5de269131f9e8bc7f ts=2026-10-18T21:11:00.4050000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[15473] _id=6ad57a0fde269131f9e929e4 ts=2026-10-19T02:01:50.6000000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 122h 8m 
  - Evidence: 122h 8m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2897] _id=6ac7a126de269131f9c14eab ts=2026-10-08T13:56:53.1930000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2944] _id=6ace56cdde269131f9cf55ea ts=2026-10-13T16:05:32.3340000Z; 54h 46m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11176] _id=6ad22d98de269131f9e4462b ts=2026-10-16T13:58:47.9240000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11193] _id=6ad52fe5de269131f9e8ba5a ts=2026-10-18T20:45:24.0040000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2373] _id=6ac64fc1de269131f9ba32a9 ts=2026-10-07T13:57:20.2050000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2407] _id=6ac79b60de269131f9c04f4b ts=2026-10-08T13:32:14.3930000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 91 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[11195] _id=6ad52fe5de269131f9e8ba5c ts=2026-10-18T20:45:24.0060000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11196] _id=6ad52fe5de269131f9e8ba5d ts=2026-10-18T20:45:24.0060000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[11196] _id=6ad52fe5de269131f9e8ba5d ts=2026-10-18T20:45:24.0060000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11197] _id=6ad52fe5de269131f9e8ba5e ts=2026-10-18T20:45:24.0060000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[11197] _id=6ad52fe5de269131f9e8ba5e ts=2026-10-18T20:45:24.0060000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11198] _id=6ad52fe5de269131f9e8ba5f ts=2026-10-18T20:45:24.0060000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 143h 33m 
  - Evidence: 143h 33m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2800] _id=6ac7a02ade269131f9c12afb ts=2026-10-08T13:52:41.3360000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[3180] _id=6acf82eade269131f9d30a1e ts=2026-10-14T13:26:01.7390000Z; 54h 48m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11178] _id=6ad22d9ede269131f9e446a2 ts=2026-10-16T13:58:53.6510000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11248] _id=6ad5304bde269131f9e8ba98 ts=2026-10-18T20:47:06.4200000Z; 24h 8m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2166] _id=6ac64cbede269131f9b9e49e ts=2026-10-07T13:44:29.2200000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2800] _id=6ac7a02ade269131f9c12afb ts=2026-10-08T13:52:41.3360000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14018] _id=6ad546a0de269131f9e8da24 ts=2026-10-18T22:22:23.5690000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14019] _id=6ad546a0de269131f9e8da25 ts=2026-10-18T22:22:23.5690000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14203] _id=6ad56592de269131f9e8f96b ts=2026-10-19T00:34:25.6790000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14204] _id=6ad56592de269131f9e8f96c ts=2026-10-19T00:34:25.6790000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14256] _id=6ad565eede269131f9e8fa16 ts=2026-10-19T00:35:56.7910000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14257] _id=6ad565eede269131f9e8fa17 ts=2026-10-19T00:35:56.7910000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 122h 7m 
  - Evidence: 122h 7m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2936] _id=6ac7a170de269131f9c15568 ts=2026-10-08T13:58:07.9450000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2943] _id=6ace56cdde269131f9cf55e9 ts=2026-10-13T16:05:28.9510000Z; 54h 45m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11188] _id=6ad22dc5de269131f9e44936 ts=2026-10-16T13:59:33.0580000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11192] _id=6ad52fe5de269131f9e8ba59 ts=2026-10-18T20:45:22.1260000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2401] _id=6ac6504bde269131f9ba3beb ts=2026-10-07T13:59:38.2510000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2406] _id=6ac79b60de269131f9c04f4a ts=2026-10-08T13:32:05.3880000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[8811] _id=6ad0dc51de269131f9db6892 ts=2026-10-15T13:59:44.7670000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[8814] _id=6ad1762fde269131f9e25424 ts=2026-10-15T13:59:44.767Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2919] _id=6ac7a129de269131f9c14efe ts=2026-10-08T13:56:52.6190000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[3199] _id=6acf8320de269131f9d30e13 ts=2026-10-14T13:26:54.7600000Z; 55h 47m: 6ab9a88e9a8420a1e6b56ae8.jsonl[10340] _id=6ad226dcde269131f9e3a84e ts=2026-10-16T13:30:02.5860000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11569] _id=6ad53762de269131f9e8bd2c ts=2026-10-18T21:17:20.8880000Z; 24h 13m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2130] _id=6ac64c63de269131f9b9dd1c ts=2026-10-07T13:42:56.0710000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2909] _id=6ac7a124de269131f9c14e6c ts=2026-10-08T13:56:50.9010000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1964 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[10002] _id=6ad17f71de269131f9e28762 ts=2026-10-16T01:35:42.3770000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[10008] _id=6ad17f71de269131f9e28764 ts=2026-10-16T01:35:42.3770000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[10003] _id=6ad17f71de269131f9e28766 ts=2026-10-16T01:35:42.4500000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[10004] _id=6ad17f71de269131f9e28767 ts=2026-10-16T01:35:42.4500000Z; 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[10007] _id=6ad17f71de269131f9e2875f ts=2026-10-16T01:35:42.3050000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[10001] _id=6ad17f71de269131f9e28761 ts=2026-10-16T01:35:42.3050000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2888] _id=6ac7a0eede269131f9c14863 ts=2026-10-08T13:55:57.5080000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[3179] _id=6acf82eade269131f9d30a1a ts=2026-10-14T13:26:01.7320000Z; 67h 58m: 6ab9a88e9a8420a1e6b56ae8.jsonl[9338] _id=6ad17b45de269131f9e270b9 ts=2026-10-16T01:17:56.2950000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11497] _id=6ad5373dde269131f9e8bd04 ts=2026-10-18T21:16:44.0760000Z; 24h 8m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2170] _id=6ac64cc1de269131f9b9e4da ts=2026-10-07T13:44:32.1740000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2799] _id=6ac7a02ade269131f9c12aed ts=2026-10-08T13:52:41.3280000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16m 45s 
  - Evidence: 16m 45s: 6ab9a88e9a8420a1e6b56ae8.jsonl[15155] _id=6ad57214de269131f9e915e6 ts=2026-10-19T01:27:46.8280000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[15222] _id=6ad57601de269131f9e92193 ts=2026-10-19T01:44:32.5130000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 156h 11m 
  - Evidence: 156h 11m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2557] _id=6ac79d71de269131f9c0b1d0 ts=2026-10-08T13:41:04.8730000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[5382] _id=6ad031e4de269131f9da21c1 ts=2026-10-15T01:52:35.8410000Z; 23h 40m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2340] _id=6ac64f40de269131f9ba2a78 ts=2026-10-07T13:55:11.0020000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2469] _id=6ac79c3bde269131f9c079e3 ts=2026-10-08T13:35:54.7880000Z; 12h 2m: 6ab9a88e9a8420a1e6b56ae8.jsonl[10137] _id=6ad182d1de269131f9e2948d ts=2026-10-16T01:50:08.3550000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11033] _id=6ad22c40de269131f9e42396 ts=2026-10-16T13:53:04.3500000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.017s..0.032s shown 
  - Evidence: 17ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[2331] _id=6ac64f1cde269131f9ba26e5 ts=2026-10-07T13:54:35.1730000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2335] _id=6ac64f1cde269131f9ba26e9 ts=2026-10-07T13:54:35.1900000Z; 18ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[2330] _id=6ac64f1cde269131f9ba26e0 ts=2026-10-07T13:54:35.1550000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2331] _id=6ac64f1cde269131f9ba26e5 ts=2026-10-07T13:54:35.1730000Z; 32ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[2471] _id=6ac79c41de269131f9c07b2b ts=2026-10-08T13:36:00.0750000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2475] _id=6ac79c41de269131f9c07b2f ts=2026-10-08T13:36:00.1070000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 204h 27m 
  - Evidence: 204h 27m: 6ab9a88e9a8420a1e6b56ae8.jsonl[439] _id=6ac4fd65de269131f9b1d07c ts=2026-10-06T13:53:41.6720000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6068] _id=6ad038a4de269131f9da3c44 ts=2026-10-15T02:21:23.4070000Z; 71h 38m: 6ab9a88e9a8420a1e6b56ae8.jsonl[9214] _id=6ad179f8de269131f9e26b37 ts=2026-10-16T01:12:23.2360000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14481] _id=6ad5698cde269131f9e9005c ts=2026-10-19T00:51:22.9320000Z; 22h 34m: 6ab9a88e9a8420a1e6b56ae8.jsonl[6328] _id=6ad03afdde269131f9da4112 ts=2026-10-15T02:31:24.4520000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[9044] _id=6ad17886de269131f9e2630a ts=2026-10-16T01:06:13.3950000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 204h 27m 
  - Evidence: 204h 27m: 6ab9a88e9a8420a1e6b56ae8.jsonl[451] _id=6ac4fd66de269131f9b1d08f ts=2026-10-06T13:53:41.6950000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6052] _id=6ad0388ade269131f9da3bd6 ts=2026-10-15T02:20:57.6140000Z; 71h 26m: 6ab9a88e9a8420a1e6b56ae8.jsonl[9211] _id=6ad179f8de269131f9e26b3d ts=2026-10-16T01:12:23.3010000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14310] _id=6ad566afde269131f9e8fb1d ts=2026-10-19T00:39:09.9110000Z; 22h 34m: 6ab9a88e9a8420a1e6b56ae8.jsonl[6329] _id=6ad03afdde269131f9da4114 ts=2026-10-15T02:31:24.5000000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[9023] _id=6ad1785fde269131f9e26245 ts=2026-10-16T01:05:34.6730000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.047s..0.047s shown 
  - Evidence: 47ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[9207] _id=6ad179f8de269131f9e26b39 ts=2026-10-16T01:12:23.2540000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[9211] _id=6ad179f8de269131f9e26b3d ts=2026-10-16T01:12:23.3010000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 204h 27m 
  - Evidence: 204h 27m: 6ab9a88e9a8420a1e6b56ae8.jsonl[424] _id=6ac4fd5fde269131f9b1cf04 ts=2026-10-06T13:53:34.9890000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6056] _id=6ad03892de269131f9da3bf4 ts=2026-10-15T02:21:05.9500000Z; 71h 27m: 6ab9a88e9a8420a1e6b56ae8.jsonl[9201] _id=6ad179e8de269131f9e26ae9 ts=2026-10-16T01:12:07.5490000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14319] _id=6ad566b2de269131f9e8fb24 ts=2026-10-19T00:39:13.0800000Z; 22h 34m: 6ab9a88e9a8420a1e6b56ae8.jsonl[6327] _id=6ad03afade269131f9da410e ts=2026-10-15T02:31:21.9810000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[9026] _id=6ad17868de269131f9e26273 ts=2026-10-16T01:05:43.7880000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 94 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14718] _id=6ad56acbde269131f9e903bc ts=2026-10-19T00:56:42.5870000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14719] _id=6ad56acbde269131f9e903be ts=2026-10-19T00:56:42.5910000Z; 5ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[14748] _id=6ad56aefde269131f9e90435 ts=2026-10-19T00:57:17.8290000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14759] _id=6ad56aefde269131f9e90437 ts=2026-10-19T00:57:17.8340000Z; 5ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[6244] _id=6ad039d3de269131f9da3ef8 ts=2026-10-15T02:26:26.2620000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6248] _id=6ad039d3de269131f9da3efa ts=2026-10-15T02:26:26.2670000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 204h 29m 
  - Evidence: 204h 29m: 6ab9a88e9a8420a1e6b56ae8.jsonl[437] _id=6ac4fd61de269131f9b1cfa2 ts=2026-10-06T13:53:37.3710000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[6134] _id=6ad03915de269131f9da3d9c ts=2026-10-15T02:23:16.4890000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 122h 33m 
  - Evidence: 122h 33m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2403] _id=6ac79b4bde269131f9c04c10 ts=2026-10-08T13:31:54.3970000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2940] _id=6ace56bcde269131f9cf55c3 ts=2026-10-13T16:05:16.4920000Z; 55h 16m: 6ab9a88e9a8420a1e6b56ae8.jsonl[10145] _id=6ad2266bde269131f9e39ee5 ts=2026-10-16T13:28:10.1100000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11191] _id=6ad52fcede269131f9e8ba55 ts=2026-10-18T20:45:01.5420000Z; 24h 5m: 6ab9a88e9a8420a1e6b56ae8.jsonl[584] _id=6ac64887de269131f9b8ff5b ts=2026-10-07T13:26:29.8790000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2403] _id=6ac79b4bde269131f9c04c10 ts=2026-10-08T13:31:54.3970000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 122h 32m 
  - Evidence: 122h 32m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2419] _id=6ac79b81de269131f9c059bd ts=2026-10-08T13:32:48.6200000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2939] _id=6ace56bcde269131f9cf55c2 ts=2026-10-13T16:05:16.4920000Z; 55h 16m: 6ab9a88e9a8420a1e6b56ae8.jsonl[10144] _id=6ad2266bde269131f9e39ee4 ts=2026-10-16T13:28:10.1090000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11190] _id=6ad52fcede269131f9e8ba54 ts=2026-10-18T20:45:01.5420000Z; 24h 5m: 6ab9a88e9a8420a1e6b56ae8.jsonl[583] _id=6ac64887de269131f9b8ff5a ts=2026-10-07T13:26:29.8790000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2402] _id=6ac79b4bde269131f9c04c0f ts=2026-10-08T13:31:54.3970000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 144h 27m 
  - Evidence: 144h 27m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2417] _id=6ac79b7bde269131f9c0594e ts=2026-10-08T13:32:42.4900000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[5038] _id=6ad02cacde269131f9da0bcb ts=2026-10-14T14:00:04.03Z; 56h 24m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11189] _id=6ad22dccde269131f9e4497f ts=2026-10-16T13:59:39.1660000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[14086] _id=6ad546f7de269131f9e8da87 ts=2026-10-18T22:23:50.4470000Z; 35h 4m: 6ab9a88e9a8420a1e6b56ae8.jsonl[6672] _id=6ad04074de269131f9da48b4 ts=2026-10-15T02:54:43.0870000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11189] _id=6ad22dccde269131f9e4497f ts=2026-10-16T13:59:39.1660000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 28 gap(s), longest 122h 13m 
  - Evidence: 122h 13m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2790] _id=6ac7a01ede269131f9c12849 ts=2026-10-08T13:52:29.3480000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2959] _id=6ace56cdde269131f9cf55f9 ts=2026-10-13T16:05:32.4240000Z; 54h 52m: 6ab9a88e9a8420a1e6b56ae8.jsonl[11003] _id=6ad22c35de269131f9e422d1 ts=2026-10-16T13:52:53.2940000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[11234] _id=6ad52fe5de269131f9e8ba62 ts=2026-10-18T20:45:24.3870000Z; 23h 38m: 6ab9a88e9a8420a1e6b56ae8.jsonl[2319] _id=6ac64f01de269131f9ba21e2 ts=2026-10-07T13:54:08.4680000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[2411] _id=6ac79b60de269131f9c04f4f ts=2026-10-08T13:32:14.4400000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[16032] _id=6ad57d26de269131f9e931e0 ts=2026-10-19T02:15:00.8200000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[16033] _id=6ad57d26de269131f9e931e1 ts=2026-10-19T02:15:00.8200000Z; 1ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[380] _id=6ac4fc8bde269131f9b19764 ts=2026-10-06T13:50:00.6720000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[383] _id=6ac4fc8bde269131f9b1976e ts=2026-10-06T13:50:00.6730000Z; 5ms: 6ab9a88e9a8420a1e6b56ae8.jsonl[13057] _id=6ad53cd4de269131f9e8cb13 ts=2026-10-18T21:40:35.1010000Z -> 6ab9a88e9a8420a1e6b56ae8.jsonl[12919] _id=6ad53cd4de269131f9e8cb17 ts=2026-10-18T21:40:35.1060000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[355] _id=6ac4fc43de269131f9b180ae ts=2026-10-06T13:48:50.7480000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[477] _id=6ac4fd7cde269131f9b1d618 ts=2026-10-06T13:54:04.0630000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[2556] _id=6ac79d70de269131f9c0b187 ts=2026-10-08T13:41:03.4110000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[9211] _id=6ad179f8de269131f9e26b3d ts=2026-10-16T01:12:23.3010000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[14904] _id=6ad56b9cde269131f9e90692 ts=2026-10-19T01:00:11.0580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[409] _id=6ac4fcf7de269131f9b1b515 ts=2026-10-06T13:51:51.4210000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[419] _id=6ac4fcfdde269131f9b1b687 ts=2026-10-06T13:51:57.0220000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[15484] _id=6ad57a2bde269131f9e92a17 ts=2026-10-19T02:02:18.4160000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 105 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[3410] _id=6acf840ade269131f9d31db4 ts=2026-10-14T13:30:47.4940000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[3407] _id=6acf840ade269131f9d31db8 ts=2026-10-14T13:30:47.5860000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[3341] _id=6acf840bde269131f9d31dd3 ts=2026-10-14T13:30:47.6770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 176 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[720] _id=6ac649fade269131f9b95e45 ts=2026-10-07T13:32:40.4390000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[723] _id=6ac649fade269131f9b95e58 ts=2026-10-07T13:32:40.4390000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[724] _id=6ac649fbde269131f9b95e60 ts=2026-10-07T13:32:40.4390000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[11033] _id=6ad22c40de269131f9e42396 ts=2026-10-16T13:53:04.3500000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 451 start, 443 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 1291 open, 1279 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 17 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 50 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 335 of 16352 adjacent _id pairs reverse in client time; worst 86302.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae8.jsonl[2936] _id=6ac7a170de269131f9c15568 ts=2026-10-08T13:58:07.9450000Z`; `6ab9a88e9a8420a1e6b56ae8.jsonl[2941] _id=6ace56bcde269131f9cf55bf ts=2026-10-07T13:59:45.87Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.11s, min -525930.66s, max -0.13s over 16353 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae8\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)

## 9. Event-Type Details

### `InputEvent` — 4614 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1984); Unit 2 Prod (Refactor) (1012); Unit 3 Dungeon Dev (612); Unit 4 Dev - Dungeon (418); Unit 4 Dev (223); Unit 4 Dev - Anderson Base (159); Unit 1 Dev (107); Unit 5 Dev - Dungeon (99)
- **Intervals:** median 1.26s (p5 0.16s / p95 18.22s, n=4613)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4614/4614 records)
    "pressed"  x4614
data.actionType  (string, 4614/4614 records)
    "Move"  x3733
    "Interact"  x576
    "Jump"  x130
    "Ascend"  x68
    "Descend"  x43
    "Hoverboard"  x39
    "Sprint"  x18
    "Map"  x4
    "Pause"  x2
    "ToggleDebug"  x1
data.key  (string, 4614/4614 records, 7 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4614/4614 records)
    "Player"  x2452
    "Drone"  x2162
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4528 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2624); Unit 4 Dev (1078); Unit 3 Dungeon Dev (460); Unit 5 Dev - Dungeon (366)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.66s, n=4527)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4528/4528 records)
    "BecameVisible"  x1291
    "BecameInvisible"  x1279
    "BecameCameraCentered"  x979
    "BecameCameraUncentered"  x979
data.pieceId  (string, 4528/4528 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4528/4528 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 3427 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (983); Unit 3 Dev (656); Unit 4 Dev (500); Unit 3 Dungeon Dev (328); Unit 5 Dev - Dungeon (317); Unit 4 Dev - Anderson Base (245); Unit 1 Dev (200); Unit 4 Dev - Dungeon (198)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.08s, n=3416)
- **Fields under `data`:**

```text
data.position  (object, 3427/3427 records)
data.position.x  (number, 3427/3427 records)
    numeric range -821.683 .. 1668.18 (907 unique)
data.position.y  (number, 3427/3427 records)
    numeric range -115.029 .. 178.051 (623 unique)
data.position.z  (number, 3427/3427 records)
    numeric range -1305.86 .. 2062.17 (907 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2315 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (777); Unit 3 Dev (525); Unit 4 Dev (286); Unit 1 Dev (195); Unit 3 Dungeon Dev (180); Unit 4 Dev - Anderson Base (176); Unit 4 Dev - Dungeon (112); Unit 5 Dev - Dungeon (64)
- **eventKey:** present on 1421 of 2315 records
- **Intervals:** median 4.83s (p5 0.01s / p95 52.09s, n=2314)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1421; [conversationId, dialogueEventType] x894
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2315/2315 records)
    numeric range 8 .. 114 (48 unique)
data.dialogueEventType  (string, 2315/2315 records)
    "DialogueNodeEvent"  x1421
    "DialogueStartEvent"  x451
    "DialogueFinishEvent"  x443
data.nodeId  (number, 1421/2315 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 677 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (361); Unit 2 Prod (Refactor) (159); Unit 3 Dev (127); Unit 1 Dev (30)
- **Intervals:** median 0.62s (p5 0.03s / p95 13.89s, n=676)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 677/677 records)
    "argumentationNodeHoverEnd"  x296
    "argumentationNodeHoverStart"  x294
    "argumentationNodeAdd"  x51
    "argumentationNodeRemove"  x36
data.argumentationTitle  (string, 677/677 records)
    "Unit 4 - Flooding"  x361
    "Unit 2 – Watershed"  x159
    "Unit 3 - Pollution Upstream"  x127
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x11
data.nodeName  (string, 677/677 records)
    "1"  x109
    "A"  x99
    "B"  x98
    "I"  x65
    "2"  x63
    "3"  x58
    "C"  x57
    "II"  x54
    "D"  x39
    "4"  x28
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 281 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (79); Unit 2 Prod (Refactor) (67); Unit 3 Dungeon Dev (58); Unit 4 Dev (25); Unit 3 Dev (17); Unit 4 Dev - Anderson Base (15); Unit 1 Dev (10); Unit 5 Dev - Dungeon (10)
- **Intervals:** median 17.57s (p5 2.26s / p95 836.19s, n=280)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 281/281 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 281/281 records)
    102 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 153 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (128); Unit 4 Dev (17); Unit 3 Dev (8)
- **Intervals:** median 1.88s (p5 0.28s / p95 113.06s, n=152)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x142; [Soil Key Puzzle Status, Unit] x11
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/153 records)
    "Started"  x6
    "Finished"  x5
data.Unit  (string, 11/153 records)
    "Unit 2 Prod (Refactor)"  x7
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 142/153 records)
    "RightDrag"  x75
    "LeftDrag"  x67
data.currentSoilType  (string, 142/153 records)
    "SAND"  x32
    "CLAYSAND"  x31
    "CLAY"  x26
    "CLAYROCK"  x20
    "SANDGRAVEL"  x19
    "BEDROCK"  x7
    "GRAVEL"  x7
data.isCorrectSelection  (string, 142/153 records)
    "false"  x106
    "true"  x36
data.waterLevelStatus  (string, 142/153 records)
    "TooHigh"  x59
    "Proper"  x53
    "TooLow"  x30
data.waterRetentionChange  (string, 142/153 records)
    "Increase"  x75
    "NoChange"  x36
    "Decrease"  x31
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 83 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 3 Dev (19); Unit 1 Dev (12); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (5); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 83 of 83 records
- **Intervals:** median 248.09s (p5 0.01s / p95 74539.07s, n=82)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Fields under `data`:**

```text
data.questEventType  (string, 83/83 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x33
data.questID  (string, 83/83 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 83/83 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/83 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 68 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (33); Unit 4 Dev - Anderson Base (25); Unit 3 Dev (8); Unit 1 Dev (2)
- **Intervals:** median 6.42s (p5 0.23s / p95 369.94s, n=67)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "submitAnswerEvent"  x68
data.answerSubmitted  (string, 68/68 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 68/68 records)
    "Unit 2 – Watershed"  x33
    "Unit 4 - Flooding"  x25
    "Unit 3 - Pollution Upstream"  x8
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 47 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (22); Unit 3 Dungeon Dev (1)
- **Intervals:** median 11.12s (p5 0.03s / p95 42717.56s, n=46)
- **`data` key-set variants:** [actionType, featureUsed] x33; [actionType, featureUsed, location] x14
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "MapOpenEvent"  x17
    "MapCloseEvent"  x16
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x7
data.featureUsed  (string, 47/47 records)
    "Map"  x33
    "Waypoint"  x14
data.location  (object, 14/47 records)
data.location.x  (number, 14/47 records)
    numeric range -289.887 .. 219.051 (14 unique)
data.location.y  (number, 14/47 records)
    numeric range -250.681 .. 249.822 (14 unique)
data.location.z  (number, 14/47 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 41 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (7); Unit 3 Dev (6); Unit 4 Dev (4); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1168.55s (p5 8.04s / p95 92254.52s, n=40)
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "DebugMenuStateChanged"  x41
data.isOpened  (bool, 41/41 records)
    false  x41
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 22 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 4117.47s (p5 168.32s / p95 199011.43s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 25066.93s (p5 728.14s / p95 235340.03s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 2.08s (p5 1.38s / p95 384.00s, n=14)
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records, 12 empty-string)
    ""  x12
    "cameraPlaced"  x3
data.boxId  (string, 15/15 records)
    "0"  x11
    "1"  x2
    "2"  x2
data.soilType  (string, 15/15 records)
    "Sand"  x7
    "Clay"  x4
    "Gravel"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `WaterChamberEvent` — 13 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (13)
- **Intervals:** median 43.81s (p5 3.52s / p95 205.47s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "On"  x9
    "Off"  x4
data.floor  (string, 13/13 records)
    "3"  x6
    "2"  x5
    "1"  x2
data.machineNumber  (string, 13/13 records)
    "One"  x13
data.machineType  (string, 13/13 records)
    "Condenser"  x7
    "Evaporator"  x5
    "VentSwitch"  x1
data.room  (string, 13/13 records)
    "1"  x7
    "2"  x3
    "3"  x3
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 13 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (13)
- **Intervals:** median 7.22s (p5 2.23s / p95 376.50s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "ChangeCanister"  x13
data.canisterType  (string, 13/13 records)
    "Gravel"  x7
    "Clay"  x3
    "Bedrock"  x2
    "Sand"  x1
data.floor  (string, 13/13 records)
    "4"  x9
    "5"  x3
    "3"  x1
data.machine  (string, 13/13 records)
    "1"  x12
    "2"  x1
data.row  (string, 13/13 records)
    "TopRow"  x12
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 408.58s (p5 0.05s / p95 496621.26s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 10 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2); Transition (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 84776.62s (p5 187.70s / p95 393245.44s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    false  x10
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 3.01s (p5 1.25s / p95 529249.94s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 326005.70s (p5 48305.75s / p95 695747.20s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 113.22s (p5 15.65s / p95 662572.53s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 1 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "Close"  x1
data.chatID  (string, 1/1 records)
    "NA"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (128 records)
- `TerasGardenBox` data.actionType: "" (12x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (36x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*