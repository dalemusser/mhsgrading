# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae2

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae2
- **Game version string(s) in log:** 2.8.9, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae2.jsonl
- **Records:** 11441 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae2
- **Time span:** 2026-10-06T13:21:49.520000+00:00 .. 2026-10-18T23:44:43.583000+00:00 (298h 22m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae2\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 11441 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 95 INFO, 0 NOT_TESTED, 94 PASS.
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
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3136 | 27.41 | 1 | 9 | 0 | 2026-10-06T13:22:23.680000+00:00 | 2026-10-18T23:36:04.135000+00:00 | 298h 13m |
| DialogueEvent | 2512 | 21.96 | 1 | 9 | 1548 | 2026-10-06T13:22:23.852000+00:00 | 2026-10-18T23:44:18.072000+00:00 | 298h 21m |
| PuzzlePieceVisibleEvent | 2266 | 19.81 | 1 | 4 | 0 | 2026-10-07T13:27:58.126000+00:00 | 2026-10-16T13:41:50.584000+00:00 | 216h 13m |
| PlayerPositionEvent | 2149 | 18.78 | 1 | 9 | 0 | 2026-10-06T13:22:03.993000+00:00 | 2026-10-18T23:44:43.583000+00:00 | 298h 22m |
| argumentationNodeEvent | 656 | 5.73 | 1 | 5 | 0 | 2026-10-06T13:48:41.064000+00:00 | 2026-10-18T23:44:16.982000+00:00 | 297h 55m |
| ObjectInterEvent | 276 | 2.41 | 1 | 9 | 0 | 2026-10-06T13:28:05.180000+00:00 | 2026-10-18T23:35:07.079000+00:00 | 298h 7m |
| TopographicMapEvent | 87 | 0.76 | 1 | 3 | 0 | 2026-10-07T13:28:28.222000+00:00 | 2026-10-16T13:31:07.189000+00:00 | 216h 2m |
| questEvent | 81 | 0.71 | 1 | 9 | 81 | 2026-10-06T13:22:23.818000+00:00 | 2026-10-18T23:33:33.371000+00:00 | 298h 11m |
| argumentationAnswerEvent | 56 | 0.49 | 1 | 5 | 0 | 2026-10-06T13:51:43.255000+00:00 | 2026-10-18T23:44:17.996000+00:00 | 297h 52m |
| DEBUGMenu | 46 | 0.4 | 1 | 9 | 0 | 2026-10-06T13:22:03.982000+00:00 | 2026-10-18T23:33:21.061000+00:00 | 298h 11m |
| Soil Key Puzzle | 38 | 0.33 | 1 | 3 | 0 | 2026-10-08T13:31:52.917000+00:00 | 2026-10-15T13:24:53.668000+00:00 | 167h 53m |
| WaterChamberEvent | 36 | 0.31 | 1 | 1 | 0 | 2026-10-16T13:39:28.170000+00:00 | 2026-10-16T13:54:47.854000+00:00 | 15m 19s |
| gameWindowFocusEvent | 23 | 0.2 | 1 | 2 | 0 | 2026-10-06T13:21:49.520000+00:00 | 2026-10-18T23:33:21.229000+00:00 | 298h 11m |
| gameStartEvent | 22 | 0.19 | 1 | 1 | 0 | 2026-10-06T13:21:49.522000+00:00 | 2026-10-18T23:33:21.229000+00:00 | 298h 11m |
| soilMachine | 15 | 0.13 | 1 | 1 | 0 | 2026-10-15T13:41:35.139000+00:00 | 2026-10-15T13:50:12.574000+00:00 | 8m 37s |
| argumentationEvent | 14 | 0.12 | 1 | 5 | 0 | 2026-10-06T13:49:17.516000+00:00 | 2026-10-18T23:37:50.046000+00:00 | 297h 48m |
| TerasGardenBox | 8 | 0.07 | 1 | 1 | 0 | 2026-10-16T13:23:56.962000+00:00 | 2026-10-16T13:24:42.387000+00:00 | 45.4s |
| gameWindowUnfocusEvent | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T13:35:05.879000+00:00 | 2026-10-16T13:59:05.423000+00:00 | 240h 23m |
| DaniEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-08T13:54:21.481000+00:00 | 2026-10-13T13:43:03.564000+00:00 | 119h 48m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-06T13:55:24.167000+00:00 | 2026-10-16T13:33:55.227000+00:00 | 239h 38m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-16T13:34:19.878000+00:00 | 2026-10-18T23:33:30.301000+00:00 | 57h 59m |
| argumentationToolEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-06T13:51:10.046000+00:00 | 2026-10-13T13:48:50.135000+00:00 | 167h 57m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 147540.084s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.269s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 13.159s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.046s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.427s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.385s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.112s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 23.579s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 604660.089s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 10112.911s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 9825.579s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 129564.571s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.034s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.8x vs baseline. 
  - Observed: 46 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: GRAVEL 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 11.2x vs baseline. 
  - Observed: 56 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 2,II; A,2,II; A,5,II; A,B,2,II; A,B,C,1,I; A,B,C,2,II; A,B,C,3,II; A,B,D,2,II; A,C,B,2,II; A,D,2,II; B,1,II; B,2,II; B,3,II; B,4,II; B,A,C,3,I; B,C,2,II; B,C,D,2,1,II; B,C,D,2,3,II; B,C,D,2,4,II; B,C,D,2,II; B,D,1,II; B,D,A,2,II; C,2,II; C,A,2,II; C,D,2,II; C,D,A,2,II; C,D,B,2,II; D,2,II; D,B,A,2,II; D,B,C,1,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.7x vs baseline. 
  - Observed: 656 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 22 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
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
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[154] _id=6ac4f80bde269131f9b0b488 ts=2026-10-06T13:30:50.3610000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[218] _id=6ac4f946de269131f9b0de6c ts=2026-10-06T13:36:05.8060000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[225] _id=6ac4f9f0de269131f9b10109 ts=2026-10-06T13:38:55.7560000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[2] _id=6ac4f5eede269131f9b049ea ts=2026-10-06T13:21:49.5220000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[570] _id=6ac4fe21de269131f9b20716 ts=2026-10-06T13:56:48.5820000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[606] _id=6ac64844de269131f9b8f0b6 ts=2026-10-07T13:25:24.3410000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[1] _id=6ac4f5eede269131f9b049e8 ts=2026-10-06T13:21:49.5200000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[200] _id=6ac4f915de269131f9b0d755 ts=2026-10-06T13:35:17.2120000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[569] _id=6ac4fe21de269131f9b20708 ts=2026-10-06T13:56:48.5810000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 5 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 5} 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[198] _id=6ac4f90ade269131f9b0d607 ts=2026-10-06T13:35:05.8790000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[603] _id=6ac64844de269131f9b8f0ac ts=2026-10-06T13:59:29.813Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[4150] _id=6acf7fb9de269131f9d2d05b ts=2026-10-13T14:00:16.281Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3135 | 0.0 | 1.269 | 342.463 | 23.714 | 392598.325 | 0.18 | 62 | 14 |
| DialogueEvent | 2511 | 0.0 | 4.685 | 427.764 | 29.748 | 392649.177 | 0.14 | 710 | 14 |
| PuzzlePieceVisibleEvent | 2265 | 0.0 | 0.046 | 343.679 | 2.627 | 519023.054 | 0.17 | 1156 | 8 |
| PlayerPositionEvent | 2137 | 0.0 | 10.003 | 474.336 | 10.162 | 392581.082 | 0.13 | 1 | 13 |
| argumentationNodeEvent | 655 | 0.005 | 0.459 | 1637.459 | 14.19 | 604617.946 | 0.04 | 130 | 5 |
| ObjectInterEvent | 275 | 0.0 | 13.159 | 3902.625 | 869.545 | 432065.547 | 0.02 | 7 | 14 |
| TopographicMapEvent | 86 | 0.018 | 7.112 | 9043.709 | 8991.22 | 430171.748 | 0.01 | 2 | 8 |
| questEvent | 80 | 0.001 | 236.33 | 13418.369 | 83742.662 | 393143.816 | 0.0 | 11 | 19 |
| argumentationAnswerEvent | 55 | 1.402 | 23.579 | 19497.359 | 110015.794 | 604652.613 | 0.0 | 0 | 5 |
| DEBUGMenu | 45 | 7.157 | 582.157 | 23855.046 | 86208.564 | 393133.395 | 0.0 | 0 | 22 |
| Soil Key Puzzle | 37 | 0.313 | 2.427 | 16334.615 | 16963.372 | 519510.658 | 0.0 | 0 | 2 |
| WaterChamberEvent | 35 | 0.141 | 11.159 | 26.277 | 75.298 | 241.238 | 2.28 | 0 | 0 |
| gameWindowFocusEvent | 22 | 52.135 | 9825.579 | 48795.078 | 202406.428 | 393147.777 | 0.0 | 0 | 20 |
| gameStartEvent | 21 | 52.134 | 10112.911 | 51118.653 | 208499.169 | 393147.777 | 0.0 | 0 | 19 |
| soilMachine | 14 | 0.203 | 5.034 | 36.96 | 132.466 | 196.198 | 1.62 | 0 | 0 |
| argumentationEvent | 13 | 0.04 | 86.138 | 82470.195 | 367773.512 | 604607.042 | 0.0 | 1 | 5 |
| TerasGardenBox | 7 | 1.185 | 1.385 | 6.489 | 20.908 | 23.02 | 9.25 | 0 | 0 |
| gameWindowUnfocusEvent | 4 | 1463.934 | 129564.571 | 216359.886 | 543368.787 | 604846.468 | 0.0 | 0 | 4 |
| DaniEvent | 3 | 1.8 | 2.467 | 143774.028 | 388186.281 | 431317.816 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 110446.143 | 147540.084 | 287570.353 | 559006.358 | 604724.833 | 0.0 | 0 | 3 |
| chatEvent | 3 | 248.089 | 1287.175 | 69583.474 | 186622.361 | 207215.159 | 0.0 | 0 | 2 |
| argumentationToolEvent | 1 | 604660.089 | 604660.089 | 604660.089 | 604660.089 | 604660.089 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 7 group(s), 13 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[2128] _id=6ac79acade269131f9c03d16 ts=2026-10-08T13:29:43.6510000Z == 6ab9a88e9a8420a1e6b56ae2.jsonl[2129] _id=6ac79acade269131f9c03d17 ts=2026-10-08T13:29:43.6510000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[4071] _id=6ace381fde269131f9cef161 ts=2026-10-13T13:54:38.6620000Z == 6ab9a88e9a8420a1e6b56ae2.jsonl[4072] _id=6ace381fde269131f9cef162 ts=2026-10-13T13:54:38.6620000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[4073] _id=6ace381fde269131f9cef163 ts=2026-10-13T13:54:38.6630000Z == 6ab9a88e9a8420a1e6b56ae2.jsonl[4074] _id=6ace381fde269131f9cef164 ts=2026-10-13T13:54:38.6630000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 25 group(s), 40 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[686] _id=6ac648e2de269131f9b91686 ts=2026-10-07T13:28:01.4010000Z == 6ab9a88e9a8420a1e6b56ae2.jsonl[688] _id=6ac648e2de269131f9b916a9 ts=2026-10-07T13:28:01.4010000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[700] _id=6ac648e3de269131f9b9172d ts=2026-10-07T13:28:01.5810000Z == 6ab9a88e9a8420a1e6b56ae2.jsonl[689] _id=6ac648e3de269131f9b91736 ts=2026-10-07T13:28:01.5810000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[683] _id=6ac648e4de269131f9b91765 ts=2026-10-07T13:28:02.0510000Z == 6ab9a88e9a8420a1e6b56ae2.jsonl[692] _id=6ac648e4de269131f9b91775 ts=2026-10-07T13:28:02.0510000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[104] _id=6ac4f765de269131f9b08f6e ts=2026-10-06T13:28:05.1800000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[106] _id=6ac4f766de269131f9b08f90 ts=2026-10-06T13:28:05.1840000Z`; `0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[6016] _id=6acf8ae1de269131f9d3cd6f ts=2026-10-14T14:00:01.5240000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[6077] _id=6acfa73bde269131f9d515d1 ts=2026-10-14T14:00:01.524Z`; `596ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[6742] _id=6acfb254de269131f9d5db69 ts=2026-10-14T16:48:19.4840000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[6740] _id=6acfb255de269131f9d5db84 ts=2026-10-14T16:48:20.0800000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `395ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10710] _id=6ad22badde269131f9e412ac ts=2026-10-16T13:50:36.1950000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[10708] _id=6ad22badde269131f9e412ce ts=2026-10-16T13:50:36.5900000Z`; `385ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10706] _id=6ad22badde269131f9e412c2 ts=2026-10-16T13:50:36.4410000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[10711] _id=6ad22baede269131f9e412d6 ts=2026-10-16T13:50:36.8260000Z`; `377ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10708] _id=6ad22badde269131f9e412ce ts=2026-10-16T13:50:36.5900000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[10713] _id=6ad22baede269131f9e412db ts=2026-10-16T13:50:36.9670000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `40ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[5619] _id=6acf880bde269131f9d3638b ts=2026-10-14T13:47:54.8390000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[5622] _id=6acf880bde269131f9d3638e ts=2026-10-14T13:47:54.8790000Z`; `97ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[9785] _id=6ad22472de269131f9e37903 ts=2026-10-16T13:19:45.4570000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[9791] _id=6ad22472de269131f9e37909 ts=2026-10-16T13:19:45.5540000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 54 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `590ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[442] _id=6ac4fcf9de269131f9b1b573 ts=2026-10-06T13:51:52.8120000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[438] _id=6ac4fcfade269131f9b1b5aa ts=2026-10-06T13:51:53.4020000Z`; `896ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[443] _id=6ac4fcf9de269131f9b1b579 ts=2026-10-06T13:51:52.8860000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[449] _id=6ac4fcfade269131f9b1b5bf ts=2026-10-06T13:51:53.7820000Z`; `338ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[3939] _id=6ace36dfde269131f9cedfc4 ts=2026-10-13T13:49:18.8060000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[3940] _id=6ace36dfde269131f9cedfd2 ts=2026-10-13T13:49:19.1440000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `498ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[8108] _id=6ad0d88ade269131f9daf228 ts=2026-10-15T13:43:37.9120000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[8111] _id=6ad0d88ade269131f9daf244 ts=2026-10-15T13:43:38.4100000Z`; `203ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[8111] _id=6ad0d88ade269131f9daf244 ts=2026-10-15T13:43:38.4100000Z ~ 6ab9a88e9a8420a1e6b56ae2.jsonl[8115] _id=6ad0d88ade269131f9daf249 ts=2026-10-15T13:43:38.6130000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 109h 12m 
  - Evidence: 109h 12m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3041] _id=6ac82f6ede269131f9c76668 ts=2026-10-09T00:03:58.2660000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3163] _id=6ace2f1cde269131f9ce8ea4 ts=2026-10-13T13:16:11.6610000Z; 57h 54m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10140] _id=6ad227dfde269131f9e3bab1 ts=2026-10-16T13:34:20.0140000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10905] _id=6ad55647de269131f9e8ddf2 ts=2026-10-18T23:29:10.7270000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae2.jsonl[609] _id=6ac6484ede269131f9b8f2ae ts=2026-10-07T13:25:34.0790000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2124] _id=6ac79ab9de269131f9c03b46 ts=2026-10-08T13:29:28.5520000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2964] _id=6ac7a08fde269131f9c13d96 ts=2026-10-08T13:54:23.2810000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3797] _id=6ace3565de269131f9cecfb8 ts=2026-10-13T13:43:01.0970000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 109h 4m 
  - Evidence: 109h 4m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3139] _id=6ac8315fde269131f9c76c85 ts=2026-10-09T00:12:14.8870000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3162] _id=6ace2f29de269131f9ce8ed4 ts=2026-10-13T13:16:24.0640000Z; 57h 31m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10900] _id=6ad22d9bde269131f9e4466b ts=2026-10-16T13:58:49.9710000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10928] _id=6ad5567bde269131f9e8de1c ts=2026-10-18T23:30:03.4830000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2117] _id=6ac65048de269131f9ba3bc7 ts=2026-10-07T13:59:36.6240000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2130] _id=6ac79acade269131f9c03d18 ts=2026-10-08T13:29:43.6730000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 710 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[11098] _id=6ad5585bde269131f9e8e1f1 ts=2026-10-18T23:38:03.4690000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11099] _id=6ad5585bde269131f9e8e1f2 ts=2026-10-18T23:38:03.4690000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[11137] _id=6ad55871de269131f9e8e274 ts=2026-10-18T23:38:25.1570000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11138] _id=6ad55871de269131f9e8e275 ts=2026-10-18T23:38:25.1570000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[11317] _id=6ad55927de269131f9e8e5bc ts=2026-10-18T23:41:26.9230000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11318] _id=6ad55927de269131f9e8e5bd ts=2026-10-18T23:41:26.9230000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 58m 
  - Evidence: 167h 58m: 6ab9a88e9a8420a1e6b56ae2.jsonl[556] _id=6ac4fdccde269131f9b1edd6 ts=2026-10-06T13:55:24.1670000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[4061] _id=6ace3801de269131f9ceefb8 ts=2026-10-13T13:54:09.0000000Z; 40h 59m: 6ab9a88e9a8420a1e6b56ae2.jsonl[7172] _id=6acfe76fde269131f9d9686c ts=2026-10-14T20:34:55.1430000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10128] _id=6ad227c4de269131f9e3b8b1 ts=2026-10-16T13:33:55.2270000Z; 30h 40m: 6ab9a88e9a8420a1e6b56ae2.jsonl[4061] _id=6ace3801de269131f9ceefb8 ts=2026-10-13T13:54:09.0000000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[7172] _id=6acfe76fde269131f9d9686c ts=2026-10-14T20:34:55.1430000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 109h 3m 
  - Evidence: 109h 3m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3158] _id=6ac831a3de269131f9c76d38 ts=2026-10-09T00:13:22.4740000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3175] _id=6ace2f39de269131f9ce8f0b ts=2026-10-13T13:16:40.7990000Z; 57h 30m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10901] _id=6ad22da3de269131f9e446fc ts=2026-10-16T13:58:58.0440000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10911] _id=6ad55657de269131f9e8ddfd ts=2026-10-18T23:29:26.9460000Z; 23h 33m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2060] _id=6ac64f9ade269131f9ba2f8c ts=2026-10-07T13:56:41.8820000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2127] _id=6ac79acade269131f9c03d15 ts=2026-10-08T13:29:43.6480000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 62 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10144] _id=6ad227dfde269131f9e3bab5 ts=2026-10-16T13:34:21.7590000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10145] _id=6ad227dfde269131f9e3bab6 ts=2026-10-16T13:34:21.7590000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10145] _id=6ad227dfde269131f9e3bab6 ts=2026-10-16T13:34:21.7590000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10146] _id=6ad227dfde269131f9e3bab7 ts=2026-10-16T13:34:21.7590000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[11005] _id=6ad5574ede269131f9e8dfab ts=2026-10-18T23:33:33.2930000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11006] _id=6ad5574ede269131f9e8dfac ts=2026-10-18T23:33:33.2930000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2356] _id=6ac79c74de269131f9c082ee ts=2026-10-08T13:36:51.4030000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3682] _id=6ace3435de269131f9cebedc ts=2026-10-13T13:37:56.9500000Z; 57h 38m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10730] _id=6ad22be4de269131f9e41a8a ts=2026-10-16T13:51:31.6360000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10931] _id=6ad55689de269131f9e8de36 ts=2026-10-18T23:30:16.9120000Z; 23h 57m: 6ab9a88e9a8420a1e6b56ae2.jsonl[1734] _id=6ac64a62de269131f9b979a7 ts=2026-10-07T13:34:25.9120000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2167] _id=6ac79b49de269131f9c04bd8 ts=2026-10-08T13:31:52.9230000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[6016] _id=6acf8ae1de269131f9d3cd6f ts=2026-10-14T14:00:01.5240000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[6077] _id=6acfa73bde269131f9d515d1 ts=2026-10-14T14:00:01.524Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[8935] _id=6ad132f2de269131f9e11c9c ts=2026-10-15T20:09:21.1690000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[8936] _id=6ad132f2de269131f9e11c9d ts=2026-10-15T20:09:21.1690000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[9030] _id=6ad20cffde269131f9e349e4 ts=2026-10-16T11:39:43.1000000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[9031] _id=6ad20cffde269131f9e349e5 ts=2026-10-16T11:39:43.1000000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 109h 3m 
  - Evidence: 109h 3m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3156] _id=6ac831a1de269131f9c76d29 ts=2026-10-09T00:13:20.7790000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3161] _id=6ace2f29de269131f9ce8ed3 ts=2026-10-13T13:16:21.8610000Z; 57h 30m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10904] _id=6ad22da4de269131f9e44719 ts=2026-10-16T13:58:59.2860000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10910] _id=6ad55657de269131f9e8ddfc ts=2026-10-18T23:29:22.3450000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2118] _id=6ac65049de269131f9ba3bd8 ts=2026-10-07T13:59:37.7890000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2126] _id=6ac79acade269131f9c03d14 ts=2026-10-08T13:29:41.1070000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[8885] _id=6ad0fa0fde269131f9dd35b6 ts=2026-10-15T16:06:39.2640000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[8889] _id=6ad13289de269131f9e11478 ts=2026-10-15T16:06:39.264Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 144h 10m 
  - Evidence: 144h 10m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2693] _id=6ac79da0de269131f9c0b9e3 ts=2026-10-08T13:41:50.9990000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[5730] _id=6acf890fde269131f9d3851b ts=2026-10-14T13:52:14.0530000Z; 23h 59m: 6ab9a88e9a8420a1e6b56ae2.jsonl[1722] _id=6ac64a3ede269131f9b970e7 ts=2026-10-07T13:33:48.8380000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2218] _id=6ac79b8ade269131f9c05a8e ts=2026-10-08T13:32:57.7480000Z; 21h 32m: 6ab9a88e9a8420a1e6b56ae2.jsonl[8778] _id=6ad0f8e3de269131f9dd11f3 ts=2026-10-15T16:01:38.0650000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10148] _id=6ad227e4de269131f9e3bb04 ts=2026-10-16T13:34:26.2310000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1156 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[1004] _id=6ac64968de269131f9b93723 ts=2026-10-07T13:30:15.8260000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[1006] _id=6ac64968de269131f9b9372d ts=2026-10-07T13:30:15.8260000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[1005] _id=6ac64968de269131f9b93719 ts=2026-10-07T13:30:15.7710000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[1003] _id=6ac64968de269131f9b9371d ts=2026-10-07T13:30:15.7710000Z; 0ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10135] _id=6ad227e4de269131f9e3bb12 ts=2026-10-16T13:34:26.2310000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10151] _id=6ad227e4de269131f9e3bb15 ts=2026-10-16T13:34:26.2310000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 18m 
  - Evidence: 144h 18m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2174] _id=6ac79b6ade269131f9c050e6 ts=2026-10-08T13:32:25.7990000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[5706] _id=6acf88c0de269131f9d37b82 ts=2026-10-14T13:50:56.4570000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae2.jsonl[5715] _id=6acf88e4de269131f9d3800c ts=2026-10-14T13:51:32.5660000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[7258] _id=6ad0d3f9de269131f9da78a6 ts=2026-10-15T13:24:08.7680000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a88e9a8420a1e6b56ae2.jsonl[2980] _id=6ac7a0a3de269131f9c1400f ts=2026-10-08T13:54:42.8180000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3300] _id=6ace30ffde269131f9ce9dc0 ts=2026-10-13T13:24:14.5660000Z; 44h 32m: 6ab9a88e9a8420a1e6b56ae2.jsonl[7038] _id=6acfb4bbde269131f9d61b8e ts=2026-10-14T16:58:33.9700000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10078] _id=6ad2271ade269131f9e3acfa ts=2026-10-16T13:31:05.2010000Z; 23h 50m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3303] _id=6ace30ffde269131f9ce9dc6 ts=2026-10-13T13:24:15.0740000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[4202] _id=6acf8049de269131f9d2d797 ts=2026-10-14T13:14:49.5020000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.018s..0.034s shown 
  - Evidence: 18ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[1879] _id=6ac64c82de269131f9b9e01f ts=2026-10-07T13:43:30.2310000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[1883] _id=6ac64c82de269131f9b9e023 ts=2026-10-07T13:43:30.2490000Z; 34ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[1878] _id=6ac64c82de269131f9b9e01d ts=2026-10-07T13:43:30.1970000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[1879] _id=6ac64c82de269131f9b9e01f ts=2026-10-07T13:43:30.2310000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 57m 
  - Evidence: 167h 57m: 6ab9a88e9a8420a1e6b56ae2.jsonl[454] _id=6ac4fcfede269131f9b1b6f5 ts=2026-10-06T13:51:58.3110000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3942] _id=6ace36ebde269131f9cee0a6 ts=2026-10-13T13:49:30.9240000Z; 58h 18m: 6ab9a88e9a8420a1e6b56ae2.jsonl[9784] _id=6ad22472de269131f9e378fd ts=2026-10-16T13:19:45.4390000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11109] _id=6ad5585bde269131f9e8e1ef ts=2026-10-18T23:38:03.4450000Z; 45h 57m: 6ab9a88e9a8420a1e6b56ae2.jsonl[5618] _id=6acf880bde269131f9d36387 ts=2026-10-14T13:47:54.8170000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[9132] _id=6ad20e63de269131f9e34b4d ts=2026-10-16T11:45:38.7940000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 56m 
  - Evidence: 167h 56m: 6ab9a88e9a8420a1e6b56ae2.jsonl[455] _id=6ac4fcffde269131f9b1b70a ts=2026-10-06T13:51:58.3300000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3905] _id=6ace36bede269131f9ceddda ts=2026-10-13T13:48:45.3720000Z; 58h 18m: 6ab9a88e9a8420a1e6b56ae2.jsonl[9791] _id=6ad22472de269131f9e37909 ts=2026-10-16T13:19:45.5540000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11084] _id=6ad5584ede269131f9e8e193 ts=2026-10-18T23:37:50.0460000Z; 45h 57m: 6ab9a88e9a8420a1e6b56ae2.jsonl[5622] _id=6acf880bde269131f9d3638e ts=2026-10-14T13:47:54.8790000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[9101] _id=6ad20e45de269131f9e34b14 ts=2026-10-16T11:45:08.3680000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.040s..0.040s shown 
  - Evidence: 40ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[5619] _id=6acf880bde269131f9d3638b ts=2026-10-14T13:47:54.8390000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[5622] _id=6acf880bde269131f9d3638e ts=2026-10-14T13:47:54.8790000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 56m 
  - Evidence: 167h 56m: 6ab9a88e9a8420a1e6b56ae2.jsonl[451] _id=6ac4fcfbde269131f9b1b62f ts=2026-10-06T13:51:55.2940000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3909] _id=6ace36c5de269131f9cede3d ts=2026-10-13T13:48:53.2400000Z; 58h 18m: 6ab9a88e9a8420a1e6b56ae2.jsonl[9779] _id=6ad22470de269131f9e378d7 ts=2026-10-16T13:19:43.3650000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[11085] _id=6ad55852de269131f9e8e1b2 ts=2026-10-18T23:37:54.5990000Z; 45h 57m: 6ab9a88e9a8420a1e6b56ae2.jsonl[5617] _id=6acf8809de269131f9d36367 ts=2026-10-14T13:47:53.3610000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[9102] _id=6ad20e4ade269131f9e34b19 ts=2026-10-16T11:45:13.4370000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 130 interval(s) ≤ 0.005s..0.022s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[9671] _id=6ad223c8de269131f9e369ef ts=2026-10-16T13:16:55.1220000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[9669] _id=6ad223c8de269131f9e369f3 ts=2026-10-16T13:16:55.1270000Z; 22ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[3937] _id=6ace36dbde269131f9cedf74 ts=2026-10-13T13:49:14.9750000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3938] _id=6ace36dbde269131f9cedf7a ts=2026-10-13T13:49:14.9970000Z; 22ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[9352] _id=6ad20fdcde269131f9e34cf2 ts=2026-10-16T11:51:55.4100000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[9353] _id=6ad20fdcde269131f9e34cf4 ts=2026-10-16T11:51:55.4320000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 57m 
  - Evidence: 167h 57m: 6ab9a88e9a8420a1e6b56ae2.jsonl[407] _id=6ac4fccfde269131f9b1abea ts=2026-10-06T13:51:10.0460000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3907] _id=6ace36c2de269131f9cede17 ts=2026-10-13T13:48:50.1350000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 57h 33m 
  - Evidence: 57h 33m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10859] _id=6ad22ce4de269131f9e43500 ts=2026-10-16T13:55:47.0530000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10909] _id=6ad55652de269131f9e8ddf8 ts=2026-10-18T23:29:22.2120000Z; 21m 27s: 6ab9a88e9a8420a1e6b56ae2.jsonl[10139] _id=6ad227dcde269131f9e3ba94 ts=2026-10-16T13:34:19.8780000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10859] _id=6ad22ce4de269131f9e43500 ts=2026-10-16T13:55:47.0530000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 109h 12m 
  - Evidence: 109h 12m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3038] _id=6ac82f60de269131f9c76604 ts=2026-10-09T00:03:44.0330000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3160] _id=6ace2f1cde269131f9ce8ea7 ts=2026-10-13T13:16:11.8100000Z; 57h 54m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10133] _id=6ad227d5de269131f9e3ba12 ts=2026-10-16T13:34:11.8590000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10907] _id=6ad55647de269131f9e8ddf4 ts=2026-10-18T23:29:11.0280000Z; 24h 4m: 6ab9a88e9a8420a1e6b56ae2.jsonl[606] _id=6ac64844de269131f9b8f0b6 ts=2026-10-07T13:25:24.3410000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2122] _id=6ac79ab9de269131f9c03b4d ts=2026-10-08T13:29:28.7010000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 109h 12m 
  - Evidence: 109h 12m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3037] _id=6ac82f60de269131f9c76603 ts=2026-10-09T00:03:44.0330000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3159] _id=6ace2f1cde269131f9ce8ea6 ts=2026-10-13T13:16:11.8100000Z; 57h 54m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10132] _id=6ad227d5de269131f9e3ba11 ts=2026-10-16T13:34:11.8590000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10906] _id=6ad55647de269131f9e8ddf3 ts=2026-10-18T23:29:11.0280000Z; 24h 4m: 6ab9a88e9a8420a1e6b56ae2.jsonl[605] _id=6ac64844de269131f9b8f0b5 ts=2026-10-07T13:25:24.3410000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2121] _id=6ac79ab9de269131f9c03b4c ts=2026-10-08T13:29:28.7000000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 0m 
  - Evidence: 168h 0m: 6ab9a88e9a8420a1e6b56ae2.jsonl[603] _id=6ac64844de269131f9b8f0ac ts=2026-10-06T13:59:29.813Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[4150] _id=6acf7fb9de269131f9d2d05b ts=2026-10-13T14:00:16.281Z; 54h 9m: 6ab9a88e9a8420a1e6b56ae2.jsonl[4150] _id=6acf7fb9de269131f9d2d05b ts=2026-10-13T14:00:16.281Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[8986] _id=6ad20c7dde269131f9e34942 ts=2026-10-15T20:10:11.542Z; 17h 48m: 6ab9a88e9a8420a1e6b56ae2.jsonl[8986] _id=6ad20c7dde269131f9e34942 ts=2026-10-15T20:10:11.542Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10908] _id=6ad55646de269131f9e8ddf0 ts=2026-10-16T13:59:05.423Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 109h 12m 
  - Evidence: 109h 12m: 6ab9a88e9a8420a1e6b56ae2.jsonl[3045] _id=6ac82f72de269131f9c76678 ts=2026-10-09T00:04:00.3380000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[3172] _id=6ace2f29de269131f9ce8ed6 ts=2026-10-13T13:16:24.1540000Z; 57h 30m: 6ab9a88e9a8420a1e6b56ae2.jsonl[10898] _id=6ad22d8dde269131f9e44504 ts=2026-10-16T13:58:36.6210000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10912] _id=6ad55657de269131f9e8ddfe ts=2026-10-18T23:29:26.9790000Z; 23h 46m: 6ab9a88e9a8420a1e6b56ae2.jsonl[1875] _id=6ac64c54de269131f9b9db0e ts=2026-10-07T13:42:44.3440000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[2132] _id=6ac79acade269131f9c03d1a ts=2026-10-08T13:29:43.7200000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10578] _id=6ad22a74de269131f9e3ee6d ts=2026-10-16T13:45:23.4130000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10579] _id=6ad22a74de269131f9e3ee6e ts=2026-10-16T13:45:23.4140000Z; 5ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[10740] _id=6ad22bedde269131f9e41bfd ts=2026-10-16T13:51:40.4760000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[10741] _id=6ad22bedde269131f9e41c0d ts=2026-10-16T13:51:40.4810000Z; 5ms: 6ab9a88e9a8420a1e6b56ae2.jsonl[8055] _id=6ad0d84dde269131f9daeafc ts=2026-10-15T13:42:36.9040000Z -> 6ab9a88e9a8420a1e6b56ae2.jsonl[8052] _id=6ad0d84dde269131f9daeb02 ts=2026-10-15T13:42:36.9090000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[350] _id=6ac4fbd2de269131f9b162b7 ts=2026-10-06T13:46:57.6610000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[398] _id=6ac4fd23de269131f9b1bf08 ts=2026-10-06T13:52:34.4930000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[2007] _id=6ac64e9ede269131f9ba1106 ts=2026-10-07T13:52:30.1540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[5622] _id=6acf880bde269131f9d3638e ts=2026-10-14T13:47:54.8790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[10139] _id=6ad227dcde269131f9e3ba94 ts=2026-10-16T13:34:19.8780000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[10859] _id=6ad22ce4de269131f9e43500 ts=2026-10-16T13:55:47.0530000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[10909] _id=6ad55652de269131f9e8ddf8 ts=2026-10-18T23:29:22.2120000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[4155] _id=6acf7fcade269131f9d2d145 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 24 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[2335] _id=6ac79c3ede269131f9c07a6c ts=2026-10-08T13:35:55.8090000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[2347] _id=6ac79c3ede269131f9c07a7e ts=2026-10-08T13:35:56.4600000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[2408] _id=6ac79c4dde269131f9c07cd8 ts=2026-10-08T13:36:10.7030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 42 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[686] _id=6ac648e2de269131f9b91686 ts=2026-10-07T13:28:01.4010000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[688] _id=6ac648e2de269131f9b916a9 ts=2026-10-07T13:28:01.4010000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[700] _id=6ac648e3de269131f9b9172d ts=2026-10-07T13:28:01.5810000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[9628] _id=6ad223a7de269131f9e36815 ts=2026-10-16T13:16:22.5180000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 29 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[9635] _id=6ad223a9de269131f9e36836 ts=2026-10-16T13:16:24.5910000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[9627] _id=6ad223aade269131f9e3684c ts=2026-10-16T13:16:25.7970000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[9690] _id=6ad223f4de269131f9e36df2 ts=2026-10-16T13:17:39.2470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 486 start, 478 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 711 open, 699 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 266 open, 265 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'questActiveEvent' (totals: 52 start, 29 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 207 of 11439 adjacent _id pairs reverse in client time; worst 92.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae2.jsonl[767] _id=6ac6493bde269131f9b92b2a ts=2026-10-07T13:29:31.0640000Z`; `6ab9a88e9a8420a1e6b56ae2.jsonl[768] _id=6ac6493cde269131f9b92b61 ts=2026-10-07T13:27:58.1260000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.62s, min -207005.49s, max -0.12s over 11440 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae2\coverage.yaml

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
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3136 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (965); Unit 2 Prod (Refactor) (750); Unit 4 Dev - Dungeon (416); Unit 3 Dungeon Dev (343); Unit 5 Dev - Dungeon (244); Unit 4 Dev (184); Unit 1 Dev (93); Unit 5 Dev (81); Unit 4 Dev - Anderson Base (60)
- **Intervals:** median 1.27s (p5 0.16s / p95 23.71s, n=3135)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3136/3136 records)
    "pressed"  x3136
data.actionType  (string, 3136/3136 records)
    "Move"  x2233
    "Interact"  x588
    "Jump"  x122
    "Ascend"  x88
    "Hoverboard"  x63
    "Descend"  x20
    "Map"  x7
    "SkipCinematic"  x6
    "Sprint"  x6
    "ToggleDebug"  x2
    "Pause"  x1
data.key  (string, 3136/3136 records, 17 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3136/3136 records)
    "Player"  x1849
    "Drone"  x1287
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2512 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (702); Unit 3 Dev (465); Unit 4 Dev (334); Unit 4 Dev - Anderson Base (292); Unit 3 Dungeon Dev (225); Unit 1 Dev (199); Unit 5 Dev (121); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1548 of 2512 records
- **Intervals:** median 4.68s (p5 0.00s / p95 29.75s, n=2511)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1548; [conversationId, dialogueEventType] x964
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2512/2512 records)
    numeric range 8 .. 116 (52 unique)
data.dialogueEventType  (string, 2512/2512 records)
    "DialogueNodeEvent"  x1548
    "DialogueStartEvent"  x486
    "DialogueFinishEvent"  x478
data.nodeId  (number, 1548/2512 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PuzzlePieceVisibleEvent` — 2266 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1210); Unit 4 Dev (448); Unit 3 Dungeon Dev (390); Unit 5 Dev - Dungeon (218)
- **Intervals:** median 0.05s (p5 0.00s / p95 2.63s, n=2265)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2266/2266 records)
    "BecameVisible"  x711
    "BecameInvisible"  x699
    "BecameCameraCentered"  x428
    "BecameCameraUncentered"  x428
data.pieceId  (string, 2266/2266 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2266/2266 records)
    1416 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2149 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (652); Unit 3 Dev (340); Unit 4 Dev (244); Unit 1 Dev (200); Unit 4 Dev - Anderson Base (180); Unit 3 Dungeon Dev (173); Unit 4 Dev - Dungeon (130); Unit 5 Dev - Dungeon (128); Unit 5 Dev (102)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.16s, n=2137)
- **Fields under `data`:**

```text
data.position  (object, 2149/2149 records)
data.position.x  (number, 2149/2149 records)
    numeric range -676.6 .. 1556.33 (592 unique)
data.position.y  (number, 2149/2149 records)
    numeric range -112.49 .. 221.918 (411 unique)
data.position.z  (number, 2149/2149 records)
    numeric range -1038.14 .. 2000.88 (592 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 656 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (322); Unit 5 Dev (235); Unit 2 Prod (Refactor) (43); Unit 3 Dev (29); Unit 1 Dev (27)
- **Intervals:** median 0.46s (p5 0.03s / p95 14.19s, n=655)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 656/656 records)
    "argumentationNodeHoverStart"  x266
    "argumentationNodeHoverEnd"  x265
    "argumentationNodeAdd"  x74
    "argumentationNodeRemove"  x51
data.argumentationTitle  (string, 656/656 records)
    "Unit 4 - Flooding"  x322
    "Unit 5"  x235
    "Unit 2 – Watershed"  x43
    "Unit 3 - Pollution Upstream"  x29
    "Unit 1 - Freshwater"  x23
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 656/656 records)
    "B"  x123
    "C"  x114
    "A"  x112
    "D"  x81
    "II"  x56
    "3"  x47
    "I"  x34
    "1"  x32
    "2"  x28
    "4"  x26
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 276 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (76); Unit 3 Dungeon Dev (62); Unit 2 Prod (Refactor) (47); Unit 4 Dev - Anderson Base (24); Unit 4 Dev (22); Unit 5 Dev - Dungeon (14); Unit 3 Dev (11); Unit 1 Dev (10); Unit 5 Dev (10)
- **Intervals:** median 13.16s (p5 1.17s / p95 869.55s, n=275)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 276/276 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 276/276 records)
    105 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 87 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (43); Unit 3 Dev (42); Unit 4 Dev (2)
- **Intervals:** median 7.11s (p5 0.97s / p95 8991.22s, n=86)
- **`data` key-set variants:** [actionType, featureUsed] x54; [actionType, featureUsed, location] x33
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 87/87 records)
    "WaypointMoveEvent"  x30
    "MapCloseEvent"  x27
    "MapOpenEvent"  x27
    "WaypointSetEvent"  x3
data.featureUsed  (string, 87/87 records)
    "Map"  x54
    "Waypoint"  x33
data.location  (object, 33/87 records)
data.location.x  (number, 33/87 records)
    numeric range -224.237 .. 301.999 (28 unique)
data.location.y  (number, 33/87 records)
    numeric range -259.117 .. 238.574 (31 unique)
data.location.z  (number, 33/87 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev (11); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (5); Unit 5 Dev (3)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 236.33s (p5 0.01s / p95 83742.66s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x29
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x29
data.questID  (string, 81/81 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 29/81 records)
    "Succeeded"  x29
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 56 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (30); Unit 5 Dev (19); Unit 3 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 23.58s (p5 3.37s / p95 110015.79s, n=55)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 56/56 records)
    "submitAnswerEvent"  x56
data.answerSubmitted  (string, 56/56 records)
    34 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 56/56 records)
    "Unit 4 - Flooding"  x30
    "Unit 5"  x19
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 46 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (20); Unit 2 Prod (Refactor) (6); Unit 3 Dev (5); Unit 3 Dungeon Dev (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 582.16s (p5 7.86s / p95 86208.56s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "DebugMenuStateChanged"  x46
data.isOpened  (bool, 46/46 records)
    false  x46
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `Soil Key Puzzle` — 38 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (18); Unit 2 Prod (Refactor) (12); Unit 3 Dev (8)
- **Intervals:** median 2.43s (p5 0.45s / p95 16963.37s, n=37)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x32; [Soil Key Puzzle Status, Unit] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/38 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/38 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 32/38 records)
    "RightDrag"  x19
    "LeftDrag"  x13
data.currentSoilType  (string, 32/38 records)
    "CLAYSAND"  x8
    "SAND"  x8
    "CLAY"  x7
    "CLAYROCK"  x5
    "SANDGRAVEL"  x3
    "BEDROCK"  x1
data.isCorrectSelection  (string, 32/38 records)
    "false"  x22
    "true"  x10
data.waterLevelStatus  (string, 32/38 records)
    "Proper"  x14
    "TooHigh"  x13
    "TooLow"  x5
data.waterRetentionChange  (string, 32/38 records)
    "Increase"  x13
    "NoChange"  x10
    "Decrease"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 36 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (36)
- **Intervals:** median 11.16s (p5 0.21s / p95 75.30s, n=35)
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "On"  x23
    "Off"  x13
data.floor  (string, 36/36 records)
    "3"  x20
    "4"  x12
    "2"  x3
    "1"  x1
data.machineNumber  (string, 36/36 records)
    "One"  x35
    "Two"  x1
data.machineType  (string, 36/36 records)
    "Condenser"  x22
    "Evaporator"  x9
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 36/36 records)
    "2"  x11
    "4"  x10
    "3"  x9
    "1"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 23 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 1 Dev (1)
- **Intervals:** median 9825.58s (p5 277.14s / p95 202406.43s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 22 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (22)
- **Intervals:** median 10112.91s (p5 250.20s / p95 208499.17s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 15 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (15)
- **Intervals:** median 5.03s (p5 0.39s / p95 132.47s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "ChangeCanister"  x15
data.canisterType  (string, 15/15 records)
    "Gravel"  x8
    "Clay"  x4
    "Sand"  x2
    "Bedrock"  x1
data.floor  (string, 15/15 records)
    "4"  x10
    "5"  x4
    "3"  x1
data.machine  (string, 15/15 records)
    "1"  x13
    "2"  x2
data.row  (string, 15/15 records)
    "TopRow"  x14
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (1)
- **Intervals:** median 86.14s (p5 0.07s / p95 367773.51s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 14/14 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 1.39s (p5 1.19s / p95 20.91s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x3
data.boxId  (string, 8/8 records)
    "0"  x4
    "1"  x2
    "2"  x2
data.soilType  (string, 8/8 records)
    "Clay"  x3
    "Sand"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 5 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 129564.57s (p5 10864.43s / p95 543368.79s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 5/5 records)
    false  x5
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4)
- **Intervals:** median 2.47s (p5 1.87s / p95 388186.28s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 147540.08s (p5 114155.54s / p95 559006.36s, n=3)
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

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1287.17s (p5 352.00s / p95 186622.36s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 604660.09s (p5 604660.09s / p95 604660.09s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit3"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

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
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (30x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (33x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (51x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*