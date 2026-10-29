# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b6d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b6d
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b6d.jsonl
- **Records:** 15272 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b6d
- **Time span:** 2026-10-06T18:36:02.382000+00:00 .. 2026-10-19T01:49:07.776000+00:00 (295h 13m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b6d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 15272 records, 10 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 93 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5026 | 32.91 | 1 | 9 | 0 | 2026-10-06T18:36:19.776000+00:00 | 2026-10-19T01:49:07.776000+00:00 | 295h 12m |
| PuzzlePieceVisibleEvent | 3906 | 25.58 | 1 | 4 | 0 | 2026-10-07T18:50:59.283000+00:00 | 2026-10-16T18:53:30.056000+00:00 | 216h 2m |
| PlayerPositionEvent | 2619 | 17.15 | 1 | 9 | 0 | 2026-10-06T18:36:16.299000+00:00 | 2026-10-19T01:49:02.774000+00:00 | 295h 12m |
| DialogueEvent | 2435 | 15.94 | 1 | 9 | 1488 | 2026-10-06T18:36:36.321000+00:00 | 2026-10-19T01:48:52.008000+00:00 | 295h 12m |
| ObjectInterEvent | 378 | 2.48 | 1 | 9 | 0 | 2026-10-06T18:44:03.524000+00:00 | 2026-10-19T01:49:07.776000+00:00 | 295h 5m |
| argumentationNodeEvent | 328 | 2.15 | 1 | 5 | 0 | 2026-10-06T19:09:17.541000+00:00 | 2026-10-19T01:35:47.478000+00:00 | 294h 26m |
| TopographicMapEvent | 219 | 1.43 | 1 | 2 | 0 | 2026-10-07T18:51:34.031000+00:00 | 2026-10-15T19:00:46.207000+00:00 | 192h 9m |
| questEvent | 94 | 0.62 | 1 | 9 | 94 | 2026-10-06T18:36:36.293000+00:00 | 2026-10-19T01:45:10.701000+00:00 | 295h 8m |
| DEBUGMenu | 43 | 0.28 | 1 | 9 | 0 | 2026-10-06T18:36:16.288000+00:00 | 2026-10-19T01:08:15.630000+00:00 | 294h 31m |
| Soil Key Puzzle | 41 | 0.27 | 1 | 3 | 0 | 2026-10-07T19:02:18.144000+00:00 | 2026-10-16T17:02:34.617000+00:00 | 214h 0m |
| WaterChamberEvent | 35 | 0.23 | 1 | 1 | 0 | 2026-10-16T18:52:31.712000+00:00 | 2026-10-19T01:25:45.571000+00:00 | 54h 33m |
| argumentationAnswerEvent | 28 | 0.18 | 1 | 5 | 0 | 2026-10-06T19:09:30.358000+00:00 | 2026-10-19T01:35:49.051000+00:00 | 294h 26m |
| gameWindowFocusEvent | 21 | 0.14 | 1 | 3 | 0 | 2026-10-06T18:36:02.382000+00:00 | 2026-10-19T01:08:06.258000+00:00 | 294h 32m |
| gameStartEvent | 19 | 0.12 | 1 | 1 | 0 | 2026-10-06T18:36:02.383000+00:00 | 2026-10-19T01:08:06.258000+00:00 | 294h 32m |
| argumentationEvent | 15 | 0.1 | 1 | 5 | 0 | 2026-10-06T19:08:53.398000+00:00 | 2026-10-19T01:35:49.079000+00:00 | 294h 26m |
| TerasGardenBox | 12 | 0.08 | 1 | 1 | 0 | 2026-10-16T17:01:55.656000+00:00 | 2026-10-16T18:36:33.706000+00:00 | 1h 34m |
| DaniEvent | 11 | 0.07 | 1 | 2 | 0 | 2026-10-08T19:11:22.457000+00:00 | 2026-10-15T18:55:03.742000+00:00 | 167h 43m |
| SolarStillDesignEvent | 11 | 0.07 | 1 | 1 | 0 | 2026-10-19T01:41:32.772000+00:00 | 2026-10-19T01:42:03.215000+00:00 | 30.4s |
| soilMachine | 10 | 0.07 | 1 | 1 | 0 | 2026-10-16T02:20:24.130000+00:00 | 2026-10-16T13:57:54.307000+00:00 | 11h 37m |
| gameWindowUnfocusEvent | 7 | 0.05 | 1 | 5 | 0 | 2026-10-07T19:17:16.121000+00:00 | 2026-10-16T17:04:01.863000+00:00 | 213h 46m |
| argumentationToolEvent | 6 | 0.04 | 1 | 2 | 0 | 2026-10-06T19:11:35.410000+00:00 | 2026-10-14T02:40:19.359000+00:00 | 175h 28m |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T19:15:28.449000+00:00 | 2026-10-19T01:49:07.761000+00:00 | 294h 33m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-16T18:48:05.827000+00:00 | 2026-10-19T01:26:45.858000+00:00 | 54h 38m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 171589.981s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 15.613s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.092s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 18.832s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 21.194s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.116s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 98360.015s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 25707.2s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 17092.222s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 82405.895s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 202.744s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 11 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.6x vs baseline. 
  - Observed: 28 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 1,; 1,I; 1,II; A,2,II; A,3,I; B,5,I; C,2,II; C,3,4,II; C,3,II; C,4,II; C,A,B,2,II; C,D,3,II; D,2,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 7 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[214] _id=6ac54227de269131f9b6e182 ts=2026-10-06T18:47:02.9100000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[284] _id=6ac54327de269131f9b70073 ts=2026-10-06T18:51:18.2390000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[433] _id=6ac544abde269131f9b71a4b ts=2026-10-06T18:57:47.0000000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[0] _id=6ac53f93de269131f9b692d6 ts=2026-10-06T18:36:02.3830000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[980] _id=6ac6931bde269131f9bdf96c ts=2026-10-07T18:44:42.0430000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[2509] _id=6ac697bbde269131f9bed4bc ts=2026-10-07T19:04:26.9160000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[7] _id=6ac53f93de269131f9b692d1 ts=2026-10-06T18:36:02.3820000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[979] _id=6ac6931bde269131f9bdf96b ts=2026-10-07T18:44:42.0430000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[2507] _id=6ac697bbde269131f9bed4bb ts=2026-10-07T19:04:26.9160000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[3401] _id=6ac7e592de269131f9c58a3f ts=2026-10-07T19:17:16.121Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[5032] _id=6ac864c7de269131f9c7dc1b ts=2026-10-08T19:17:47.445Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[5544] _id=6ace7d56de269131f9d12a19 ts=2026-10-13T18:49:57.5810000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 36 of 219 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[1297] _id=6ac694b6de269131f9be3c3f ts=2026-10-07T18:51:34.0310000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[1302] _id=6ac694bdde269131f9be3da6 ts=2026-10-07T18:51:40.7520000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[1303] _id=6ac694bede269131f9be3de3 ts=2026-10-07T18:51:41.5330000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5025 | 0.0 | 1.064 | 211.496 | 17.844 | 397703.775 | 0.28 | 169 | 16 |
| PuzzlePieceVisibleEvent | 3905 | 0.0 | 0.092 | 199.168 | 2.973 | 432534.362 | 0.3 | 1468 | 9 |
| PlayerPositionEvent | 2607 | 0.0 | 10.001 | 353.373 | 10.126 | 397700.023 | 0.17 | 3 | 13 |
| DialogueEvent | 2434 | 0.0 | 3.824 | 436.621 | 44.062 | 397942.781 | 0.14 | 701 | 16 |
| ObjectInterEvent | 377 | 0.0 | 15.613 | 2817.783 | 413.92 | 432245.797 | 0.02 | 6 | 14 |
| argumentationNodeEvent | 327 | 0.001 | 0.728 | 3241.559 | 10.052 | 631629.348 | 0.02 | 41 | 5 |
| TopographicMapEvent | 218 | 0.022 | 3.481 | 3173.175 | 693.414 | 397774.615 | 0.02 | 3 | 13 |
| questEvent | 93 | 0.0 | 259.544 | 11424.886 | 64019.982 | 398488.461 | 0.01 | 16 | 25 |
| DEBUGMenu | 42 | 6.024 | 668.471 | 25245.699 | 86832.644 | 398717.011 | 0.0 | 0 | 22 |
| Soil Key Puzzle | 40 | 0.131 | 1.189 | 19260.412 | 90627.163 | 431537.821 | 0.0 | 0 | 6 |
| WaterChamberEvent | 34 | 0.814 | 17.885 | 5776.29 | 211.248 | 195079.948 | 0.01 | 0 | 1 |
| argumentationAnswerEvent | 27 | 1.002 | 21.194 | 39258.47 | 191276.546 | 631651.074 | 0.0 | 0 | 5 |
| gameWindowFocusEvent | 20 | 878.024 | 17092.222 | 53016.194 | 205762.818 | 398728.132 | 0.0 | 0 | 20 |
| gameStartEvent | 18 | 878.024 | 25707.2 | 58906.882 | 226074.956 | 398728.132 | 0.0 | 0 | 18 |
| argumentationEvent | 14 | 0.05 | 128.752 | 75715.406 | 353542.233 | 631618.697 | 0.0 | 1 | 5 |
| TerasGardenBox | 11 | 1.548 | 18.832 | 516.186 | 2785.133 | 5537.186 | 0.12 | 0 | 1 |
| DaniEvent | 10 | 1.462 | 54.579 | 60382.129 | 258737.269 | 398983.37 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 10 | 1.034 | 2.769 | 3.044 | 5.452 | 5.911 | 19.71 | 0 | 0 |
| soilMachine | 9 | 1.445 | 202.744 | 4650.02 | 24428.347 | 40403.813 | 0.01 | 0 | 1 |
| gameWindowUnfocusEvent | 6 | 11174.257 | 82405.895 | 128267.624 | 344605.901 | 430330.136 | 0.0 | 0 | 6 |
| argumentationToolEvent | 5 | 0.921 | 3.116 | 126344.79 | 505351.069 | 631678.952 | 0.0 | 0 | 1 |
| EndOfUnit | 4 | 85406.027 | 171589.981 | 265104.828 | 566773.29 | 631833.322 | 0.0 | 0 | 4 |
| chatEvent | 2 | 1110.381 | 98360.015 | 98360.015 | 185884.687 | 195609.65 | 0.0 | 0 | 2 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 20 group(s), 69 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[977] _id=6ac6932cde269131f9bdfb77 ts=2026-10-07T18:44:58.7430000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[978] _id=6ac6932cde269131f9bdfb78 ts=2026-10-07T18:44:58.7430000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[986] _id=6ac6932cde269131f9bdfb7c ts=2026-10-07T18:44:58.7440000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[987] _id=6ac6932cde269131f9bdfb7d ts=2026-10-07T18:44:58.7440000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[994] _id=6ac6932cde269131f9bdfb84 ts=2026-10-07T18:44:58.7470000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[995] _id=6ac6932cde269131f9bdfb85 ts=2026-10-07T18:44:58.7470000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 49 group(s), 73 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[1343] _id=6ac69516de269131f9be4fcc ts=2026-10-07T18:53:08.1720000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[1340] _id=6ac69516de269131f9be4fd5 ts=2026-10-07T18:53:08.1720000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[1348] _id=6ac69516de269131f9be4ff1 ts=2026-10-07T18:53:08.3310000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[1349] _id=6ac69516de269131f9be4ff8 ts=2026-10-07T18:53:08.3310000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[2664] _id=6ac698a1de269131f9bef1ff ts=2026-10-07T19:08:15.3470000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[2663] _id=6ac698a1de269131f9bef20a ts=2026-10-07T19:08:15.3470000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[15021] _id=6ad5743ade269131f9e91c4d ts=2026-10-19T01:36:57.7300000Z == 6ab9a9279a8420a1e6b56b6d.jsonl[15022] _id=6ad5743ade269131f9e91c4e ts=2026-10-19T01:36:57.7300000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 69 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b6d.jsonl[129] _id=6ac54174de269131f9b6ca6d ts=2026-10-06T18:44:03.5240000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[130] _id=6ac54174de269131f9b6ca71 ts=2026-10-06T18:44:03.5290000Z`; `212ms: 6ab9a9279a8420a1e6b56b6d.jsonl[1090] _id=6ac69409de269131f9be1c25 ts=2026-10-07T18:48:40.3520000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[1091] _id=6ac69409de269131f9be1c3e ts=2026-10-07T18:48:40.5640000Z`; `346ms: 6ab9a9279a8420a1e6b56b6d.jsonl[1100] _id=6ac6940ede269131f9be1d66 ts=2026-10-07T18:48:45.4970000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[1103] _id=6ac6940ede269131f9be1d75 ts=2026-10-07T18:48:45.8430000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `148ms: 6ab9a9279a8420a1e6b56b6d.jsonl[5379] _id=6ace7aa5de269131f9d10273 ts=2026-10-13T18:38:29.0890000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[5380] _id=6ace7aa6de269131f9d10277 ts=2026-10-13T18:38:29.2370000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `50ms: 6ab9a9279a8420a1e6b56b6d.jsonl[9054] _id=6acfd3d9de269131f9d83cf0 ts=2026-10-14T19:11:21.4300000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[9057] _id=6acfd3d9de269131f9d83cf3 ts=2026-10-14T19:11:21.4800000Z`; `89ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13560] _id=6ad25747de269131f9e64314 ts=2026-10-16T16:56:38.7660000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[13558] _id=6ad25747de269131f9e64319 ts=2026-10-16T16:56:38.8550000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `25ms: 6ab9a9279a8420a1e6b56b6d.jsonl[816] _id=6ac547e5de269131f9b76dfb ts=2026-10-06T19:11:32.5610000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[817] _id=6ac547e5de269131f9b76e01 ts=2026-10-06T19:11:32.5860000Z`; `840ms: 6ab9a9279a8420a1e6b56b6d.jsonl[7505] _id=6aceeb8ade269131f9d2abf7 ts=2026-10-14T02:40:09.5490000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[7573] _id=6aceeb8bde269131f9d2abfd ts=2026-10-14T02:40:10.3890000Z`; `705ms: 6ab9a9279a8420a1e6b56b6d.jsonl[7586] _id=6aceebb1de269131f9d2ac3a ts=2026-10-14T02:40:48.3430000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[7608] _id=6aceebb2de269131f9d2ac3d ts=2026-10-14T02:40:49.0480000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9279a8420a1e6b56b6d.jsonl[15167] _id=6ad575bfde269131f9e920fe ts=2026-10-19T01:43:26.1410000Z ~ 6ab9a9279a8420a1e6b56b6d.jsonl[15165] _id=6ad575bfde269131f9e92102 ts=2026-10-19T01:43:26.1450000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 110h 45m 
  - Evidence: 110h 45m: 6ab9a9279a8420a1e6b56b6d.jsonl[5041] _id=6ac864d1de269131f9c7dc28 ts=2026-10-09T03:51:44.3030000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5324] _id=6ace7a4ede269131f9d0fc06 ts=2026-10-13T18:37:01.3140000Z; 54h 20m: 6ab9a9279a8420a1e6b56b6d.jsonl[14095] _id=6ad27169de269131f9e755b6 ts=2026-10-16T18:48:06.0560000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14413] _id=6ad56d77de269131f9e90a58 ts=2026-10-19T01:08:06.1250000Z; 24h 8m: 6ab9a9279a8420a1e6b56b6d.jsonl[6] _id=6ac53fa1de269131f9b6948a ts=2026-10-06T18:36:16.2880000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[981] _id=6ac6931bde269131f9bdf95e ts=2026-10-07T18:44:41.8920000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 110h 49m 
  - Evidence: 110h 49m: 6ab9a9279a8420a1e6b56b6d.jsonl[5322] _id=6ac868d5de269131f9c7e244 ts=2026-10-09T04:08:52.7460000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5550] _id=6ace7f5dde269131f9d136e5 ts=2026-10-13T18:58:36.1160000Z; 24h 15m: 6ab9a9279a8420a1e6b56b6d.jsonl[5547] _id=6ace7f5fde269131f9d136f9 ts=2026-10-13T18:58:38.7470000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[9131] _id=6acfd47cde269131f9d85877 ts=2026-10-14T19:14:04.1150000Z; 23h 40m: 6ab9a9279a8420a1e6b56b6d.jsonl[9135] _id=6acfd47fde269131f9d85949 ts=2026-10-14T19:14:07.2510000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[10429] _id=6ad12186de269131f9df7f84 ts=2026-10-15T18:55:01.6480000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 110h 32m 
  - Evidence: 110h 32m: 6ab9a9279a8420a1e6b56b6d.jsonl[5294] _id=6ac86868de269131f9c7e161 ts=2026-10-09T04:07:03.6040000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5403] _id=6ace7adfde269131f9d106fa ts=2026-10-13T18:39:26.3850000Z; 54h 11m: 6ab9a9279a8420a1e6b56b6d.jsonl[14379] _id=6ad2737cde269131f9e77d92 ts=2026-10-16T18:56:59.3730000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14422] _id=6ad56d8ade269131f9e90a8e ts=2026-10-19T01:08:25.4980000Z; 23h 32m: 6ab9a9279a8420a1e6b56b6d.jsonl[3399] _id=6ac69abbde269131f9bf2092 ts=2026-10-07T19:17:14.6910000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3400] _id=6ac7e5d9de269131f9c58fe9 ts=2026-10-08T18:50:01.4700000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 701 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13157] _id=6ad24c50de269131f9e5a29a ts=2026-10-16T16:09:52.4500000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13158] _id=6ad24c50de269131f9e5a29b ts=2026-10-16T16:09:52.4500000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13172] _id=6ad24c61de269131f9e5a3cf ts=2026-10-16T16:10:08.8590000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13173] _id=6ad24c61de269131f9e5a3d0 ts=2026-10-16T16:10:08.8590000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[8982] _id=6acfd36ede269131f9d82aa6 ts=2026-10-14T19:09:34.5350000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[8983] _id=6acfd36ede269131f9d82aa7 ts=2026-10-14T19:09:34.5350000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 175h 30m 
  - Evidence: 175h 30m: 6ab9a9279a8420a1e6b56b6d.jsonl[967] _id=6ac548d1de269131f9b789b7 ts=2026-10-06T19:15:28.4490000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[7708] _id=6aceeceade269131f9d2ae48 ts=2026-10-14T02:46:01.7710000Z; 55h 1m: 6ab9a9279a8420a1e6b56b6d.jsonl[14076] _id=6ad27140de269131f9e751f8 ts=2026-10-16T18:47:27.9870000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[15268] _id=6ad57714de269131f9e92438 ts=2026-10-19T01:49:07.7610000Z; 40h 18m: 6ab9a9279a8420a1e6b56b6d.jsonl[7708] _id=6aceeceade269131f9d2ae48 ts=2026-10-14T02:46:01.7710000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[10622] _id=6ad123a2de269131f9dfccfc ts=2026-10-15T19:04:01.9600000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 110h 28m 
  - Evidence: 110h 28m: 6ab9a9279a8420a1e6b56b6d.jsonl[5323] _id=6ac868d6de269131f9c7e246 ts=2026-10-09T04:08:52.7530000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5329] _id=6ace7a5ede269131f9d0fc8c ts=2026-10-13T18:37:16.5280000Z; 54h 11m: 6ab9a9279a8420a1e6b56b6d.jsonl[14397] _id=6ad2739ade269131f9e77f33 ts=2026-10-16T18:57:29.4040000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14428] _id=6ad56d95de269131f9e90ab7 ts=2026-10-19T01:08:37.0330000Z; 23h 35m: 6ab9a9279a8420a1e6b56b6d.jsonl[3345] _id=6ac699eade269131f9bf0e0e ts=2026-10-07T19:13:45.1350000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3407] _id=6ac7e5a8de269131f9c58ba2 ts=2026-10-08T18:49:11.3910000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 169 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[1058] _id=6ac693fcde269131f9be19c0 ts=2026-10-07T18:48:27.9040000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[1059] _id=6ac693fcde269131f9be19c1 ts=2026-10-07T18:48:27.9040000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[1114] _id=6ac69411de269131f9be1e0d ts=2026-10-07T18:48:48.3950000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[1115] _id=6ac69411de269131f9be1e0e ts=2026-10-07T18:48:48.3950000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[11230] _id=6ad125fcde269131f9e02b4c ts=2026-10-15T19:14:03.7170000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[11231] _id=6ad125fcde269131f9e02b4d ts=2026-10-15T19:14:03.7170000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 120h 4m 
  - Evidence: 120h 4m: 6ab9a9279a8420a1e6b56b6d.jsonl[4456] _id=6ac7e7e5de269131f9c5dbfe ts=2026-10-08T18:58:45.2500000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5614] _id=6ace805cde269131f9d14677 ts=2026-10-13T19:02:51.0470000Z; 54h 13m: 6ab9a9279a8420a1e6b56b6d.jsonl[14390] _id=6ad27386de269131f9e77e32 ts=2026-10-16T18:57:09.7970000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14478] _id=6ad56e00de269131f9e90c45 ts=2026-10-19T01:10:23.4210000Z; 23h 37m: 6ab9a9279a8420a1e6b56b6d.jsonl[3311] _id=6ac699c1de269131f9bf0ae1 ts=2026-10-07T19:13:04.4400000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3456] _id=6ac7e608de269131f9c5963c ts=2026-10-08T18:50:48.1130000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[12977] _id=6ad24b3dde269131f9e5904a ts=2026-10-16T16:05:17.4600000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[12978] _id=6ad24b3dde269131f9e5904b ts=2026-10-16T16:05:17.4600000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13075] _id=6ad24ba4de269131f9e596b7 ts=2026-10-16T16:07:00.4820000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13076] _id=6ad24ba4de269131f9e596b8 ts=2026-10-16T16:07:00.4820000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13337] _id=6ad255a2de269131f9e621cf ts=2026-10-16T16:49:38.0370000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13338] _id=6ad255a2de269131f9e621d0 ts=2026-10-16T16:49:38.0370000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 110h 28m 
  - Evidence: 110h 28m: 6ab9a9279a8420a1e6b56b6d.jsonl[5321] _id=6ac868d5de269131f9c7e242 ts=2026-10-09T04:08:51.8330000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5328] _id=6ace7a5ede269131f9d0fc8b ts=2026-10-13T18:37:11.8560000Z; 54h 9m: 6ab9a9279a8420a1e6b56b6d.jsonl[14412] _id=6ad56d77de269131f9e90a56 ts=2026-10-16T18:58:58.183Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14420] _id=6ad56d83de269131f9e90a7b ts=2026-10-19T01:08:15.6400000Z; 23h 32m: 6ab9a9279a8420a1e6b56b6d.jsonl[3398] _id=6ac69ab5de269131f9bf2050 ts=2026-10-07T19:17:09.0350000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3406] _id=6ac7e5a8de269131f9c58ba1 ts=2026-10-08T18:49:09.1550000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[12070] _id=6ad18b58de269131f9e2b9aa ts=2026-10-16T02:26:32.1800000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[12077] _id=6ad22825de269131f9e3bee6 ts=2026-10-16T02:26:32.18Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[12618] _id=6ad22dccde269131f9e4498d ts=2026-10-16T13:59:39.9810000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[12625] _id=6ad248c9de269131f9e567d8 ts=2026-10-16T13:59:39.981Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[14407] _id=6ad273f3de269131f9e785b7 ts=2026-10-16T18:58:58.1830000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14412] _id=6ad56d77de269131f9e90a56 ts=2026-10-16T18:58:58.183Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 8m 
  - Evidence: 120h 8m: 6ab9a9279a8420a1e6b56b6d.jsonl[4446] _id=6ac7e7c7de269131f9c5d6a2 ts=2026-10-08T18:58:13.2590000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5685] _id=6ace815cde269131f9d15fe8 ts=2026-10-13T19:07:07.6210000Z; 37h 57m: 6ab9a9279a8420a1e6b56b6d.jsonl[6736] _id=6acee2e7de269131f9d29a29 ts=2026-10-14T02:03:18.0880000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[9328] _id=6ad0f89fde269131f9dd088e ts=2026-10-15T16:00:30.7060000Z; 23h 39m: 6ab9a9279a8420a1e6b56b6d.jsonl[3289] _id=6ac69991de269131f9bf075d ts=2026-10-07T19:12:15.3030000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3548] _id=6ac7e680de269131f9c5a66b ts=2026-10-08T18:51:29.1020000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1468 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[10704] _id=6ad12528de269131f9e00caf ts=2026-10-15T19:10:28.8060000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[10762] _id=6ad12528de269131f9e00cbd ts=2026-10-15T19:10:28.8060000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[10706] _id=6ad12525de269131f9e00c2e ts=2026-10-15T19:10:27.4530000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[10707] _id=6ad12525de269131f9e00c32 ts=2026-10-15T19:10:27.4530000Z; 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[10713] _id=6ad1250dde269131f9e0078d ts=2026-10-15T19:10:03.6280000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[10715] _id=6ad1250dde269131f9e00791 ts=2026-10-15T19:10:03.6280000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a9279a8420a1e6b56b6d.jsonl[4736] _id=6ac7eaa9de269131f9c6573b ts=2026-10-08T19:10:33.2180000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5615] _id=6ace805bde269131f9d1466d ts=2026-10-13T19:02:51.0390000Z; 44h 53m: 6ab9a9279a8420a1e6b56b6d.jsonl[5653] _id=6ace8111de269131f9d1554a ts=2026-10-13T19:05:52.4430000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[9271] _id=6ad0f853de269131f9dd01e6 ts=2026-10-15T15:59:15.4120000Z; 24h 8m: 6ab9a9279a8420a1e6b56b6d.jsonl[2473] _id=6ac6973dde269131f9bec4d6 ts=2026-10-07T19:02:20.9810000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[4730] _id=6ac7eaa8de269131f9c65727 ts=2026-10-08T19:10:32.5750000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 32m 
  - Evidence: 1h 32m: 6ab9a9279a8420a1e6b56b6d.jsonl[13732] _id=6ad258c0de269131f9e65b42 ts=2026-10-16T17:02:56.2480000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13797] _id=6ad26e62de269131f9e711d6 ts=2026-10-16T18:35:13.4340000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 110h 29m 
  - Evidence: 110h 29m: 6ab9a9279a8420a1e6b56b6d.jsonl[5291] _id=6ac868bfde269131f9c7e214 ts=2026-10-09T04:08:30.2570000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5369] _id=6ace7a8dde269131f9d10092 ts=2026-10-13T18:38:04.8720000Z; 23h 44m: 6ab9a9279a8420a1e6b56b6d.jsonl[2639] _id=6ac69880de269131f9beef87 ts=2026-10-07T19:07:43.3990000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3489] _id=6ac7e64dde269131f9c5a042 ts=2026-10-08T18:51:57.3720000Z; 23h 40m: 6ab9a9279a8420a1e6b56b6d.jsonl[9096] _id=6acfd450de269131f9d85054 ts=2026-10-14T19:13:19.7980000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[10389] _id=6ad12130de269131f9df74c1 ts=2026-10-15T18:53:35.2350000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.022s..0.047s shown 
  - Evidence: 22ms: 6ab9a9279a8420a1e6b56b6d.jsonl[5119] _id=6ac865f5de269131f9c7dd5f ts=2026-10-09T03:56:35.9410000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5123] _id=6ac865f5de269131f9c7dd63 ts=2026-10-09T03:56:35.9630000Z; 23ms: 6ab9a9279a8420a1e6b56b6d.jsonl[4631] _id=6ac7ea1cde269131f9c64012 ts=2026-10-08T19:08:11.5750000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[4635] _id=6ac7ea1cde269131f9c64016 ts=2026-10-08T19:08:11.5980000Z; 47ms: 6ab9a9279a8420a1e6b56b6d.jsonl[5124] _id=6ac865f5de269131f9c7dd5d ts=2026-10-09T03:56:35.8940000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5119] _id=6ac865f5de269131f9c7dd5f ts=2026-10-09T03:56:35.9410000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 54h 11m 
  - Evidence: 54h 11m: 6ab9a9279a8420a1e6b56b6d.jsonl[14394] _id=6ad27393de269131f9e77ed0 ts=2026-10-16T18:57:22.8120000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14430] _id=6ad56d9bde269131f9e90aca ts=2026-10-19T01:08:42.7600000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 175h 27m 
  - Evidence: 175h 27m: 6ab9a9279a8420a1e6b56b6d.jsonl[834] _id=6ac547ffde269131f9b76fe1 ts=2026-10-06T19:11:59.0300000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[7555] _id=6aceeb63de269131f9d2abc7 ts=2026-10-14T02:39:30.1040000Z; 56h 37m: 6ab9a9279a8420a1e6b56b6d.jsonl[13557] _id=6ad25746de269131f9e64311 ts=2026-10-16T16:56:38.7500000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14911] _id=6ad5739dde269131f9e91a7b ts=2026-10-19T01:34:20.5200000Z; 44h 58m: 6ab9a9279a8420a1e6b56b6d.jsonl[9053] _id=6acfd3d9de269131f9d83ce7 ts=2026-10-14T19:11:21.4050000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13152] _id=6ad24c50de269131f9e5a298 ts=2026-10-16T16:09:52.4270000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 175h 26m 
  - Evidence: 175h 26m: 6ab9a9279a8420a1e6b56b6d.jsonl[837] _id=6ac547ffde269131f9b76fe3 ts=2026-10-06T19:11:59.0500000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[7531] _id=6aceeb42de269131f9d2ab9a ts=2026-10-14T02:38:57.7470000Z; 56h 36m: 6ab9a9279a8420a1e6b56b6d.jsonl[13558] _id=6ad25747de269131f9e64319 ts=2026-10-16T16:56:38.8550000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14864] _id=6ad57368de269131f9e91941 ts=2026-10-19T01:33:27.6080000Z; 44h 57m: 6ab9a9279a8420a1e6b56b6d.jsonl[9057] _id=6acfd3d9de269131f9d83cf3 ts=2026-10-14T19:11:21.4800000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13129] _id=6ad24c29de269131f9e59f82 ts=2026-10-16T16:09:13.1450000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.050s..0.050s shown 
  - Evidence: 50ms: 6ab9a9279a8420a1e6b56b6d.jsonl[9054] _id=6acfd3d9de269131f9d83cf0 ts=2026-10-14T19:11:21.4300000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[9057] _id=6acfd3d9de269131f9d83cf3 ts=2026-10-14T19:11:21.4800000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 175h 27m 
  - Evidence: 175h 27m: 6ab9a9279a8420a1e6b56b6d.jsonl[833] _id=6ac547fcde269131f9b76faf ts=2026-10-06T19:11:56.2480000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[7542] _id=6aceeb4ade269131f9d2aba5 ts=2026-10-14T02:39:05.5960000Z; 56h 36m: 6ab9a9279a8420a1e6b56b6d.jsonl[13513] _id=6ad25745de269131f9e642f0 ts=2026-10-16T16:56:37.5360000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14869] _id=6ad5736ade269131f9e91946 ts=2026-10-19T01:33:30.0290000Z; 44h 58m: 6ab9a9279a8420a1e6b56b6d.jsonl[9047] _id=6acfd3cbde269131f9d839fa ts=2026-10-14T19:11:06.7850000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13133] _id=6ad24c2cde269131f9e59fb7 ts=2026-10-16T16:09:16.4580000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 41 interval(s) ≤ 0.001s..0.021s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b6d.jsonl[8968] _id=6acfd354de269131f9d82605 ts=2026-10-14T19:09:08.5000000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[8969] _id=6acfd354de269131f9d82606 ts=2026-10-14T19:09:08.5010000Z; 6ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13536] _id=6ad25733de269131f9e641a7 ts=2026-10-16T16:56:18.9730000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13533] _id=6ad25733de269131f9e641aa ts=2026-10-16T16:56:18.9790000Z; 21ms: 6ab9a9279a8420a1e6b56b6d.jsonl[13505] _id=6ad25704de269131f9e63ea6 ts=2026-10-16T16:55:32.0940000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[13492] _id=6ad25704de269131f9e63ea8 ts=2026-10-16T16:55:32.1150000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 175h 27m 
  - Evidence: 175h 27m: 6ab9a9279a8420a1e6b56b6d.jsonl[821] _id=6ac547eade269131f9b76e61 ts=2026-10-06T19:11:37.7540000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[7556] _id=6aceeb69de269131f9d2abcf ts=2026-10-14T02:39:36.7060000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 54h 20m 
  - Evidence: 54h 20m: 6ab9a9279a8420a1e6b56b6d.jsonl[14096] _id=6ad27166de269131f9e7556f ts=2026-10-16T18:48:05.8270000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14415] _id=6ad56d80de269131f9e90a70 ts=2026-10-19T01:08:15.4770000Z; 18m 30s: 6ab9a9279a8420a1e6b56b6d.jsonl[14415] _id=6ad56d80de269131f9e90a70 ts=2026-10-19T01:08:15.4770000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14726] _id=6ad571d6de269131f9e9150d ts=2026-10-19T01:26:45.8580000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 110h 45m 
  - Evidence: 110h 45m: 6ab9a9279a8420a1e6b56b6d.jsonl[5040] _id=6ac864c7de269131f9c7dc1f ts=2026-10-09T03:51:33.5120000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5326] _id=6ace7a4ede269131f9d0fc0b ts=2026-10-13T18:37:01.6440000Z; 54h 20m: 6ab9a9279a8420a1e6b56b6d.jsonl[14084] _id=6ad27160de269131f9e754de ts=2026-10-16T18:47:59.5090000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14416] _id=6ad56d77de269131f9e90a5a ts=2026-10-19T01:08:06.2580000Z; 24h 8m: 6ab9a9279a8420a1e6b56b6d.jsonl[0] _id=6ac53f93de269131f9b692d6 ts=2026-10-06T18:36:02.3830000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[980] _id=6ac6931bde269131f9bdf96c ts=2026-10-07T18:44:42.0430000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 110h 45m 
  - Evidence: 110h 45m: 6ab9a9279a8420a1e6b56b6d.jsonl[5039] _id=6ac864c7de269131f9c7dc1e ts=2026-10-09T03:51:33.5120000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5325] _id=6ace7a4ede269131f9d0fc0a ts=2026-10-13T18:37:01.6440000Z; 54h 20m: 6ab9a9279a8420a1e6b56b6d.jsonl[14083] _id=6ad27160de269131f9e754dd ts=2026-10-16T18:47:59.5090000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14414] _id=6ad56d77de269131f9e90a59 ts=2026-10-19T01:08:06.2580000Z; 24h 8m: 6ab9a9279a8420a1e6b56b6d.jsonl[7] _id=6ac53f93de269131f9b692d1 ts=2026-10-06T18:36:02.3820000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[979] _id=6ac6931bde269131f9bdf96b ts=2026-10-07T18:44:42.0430000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a9279a8420a1e6b56b6d.jsonl[5032] _id=6ac864c7de269131f9c7dc1b ts=2026-10-08T19:17:47.445Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5544] _id=6ace7d56de269131f9d12a19 ts=2026-10-13T18:49:57.5810000Z; 24h 17m: 6ab9a9279a8420a1e6b56b6d.jsonl[5544] _id=6ace7d56de269131f9d12a19 ts=2026-10-13T18:49:57.5810000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[8932] _id=6acfd2dfde269131f9d8130f ts=2026-10-14T19:07:10.7770000Z; 24h 0m: 6ab9a9279a8420a1e6b56b6d.jsonl[3401] _id=6ac7e592de269131f9c58a3f ts=2026-10-07T19:17:16.121Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5032] _id=6ac864c7de269131f9c7dc1b ts=2026-10-08T19:17:47.445Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 110h 41m 
  - Evidence: 110h 41m: 6ab9a9279a8420a1e6b56b6d.jsonl[5107] _id=6ac865c5de269131f9c7dd01 ts=2026-10-09T03:55:48.1130000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[5349] _id=6ace7a5ede269131f9d0fca0 ts=2026-10-13T18:37:16.5740000Z; 54h 10m: 6ab9a9279a8420a1e6b56b6d.jsonl[14398] _id=6ad2739ede269131f9e77f8f ts=2026-10-16T18:57:33.0530000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14421] _id=6ad56d83de269131f9e90a7c ts=2026-10-19T01:08:18.1970000Z; 23h 35m: 6ab9a9279a8420a1e6b56b6d.jsonl[3349] _id=6ac699f0de269131f9bf0ee3 ts=2026-10-07T19:13:52.0610000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[3421] _id=6ac7e5a8de269131f9c58bb0 ts=2026-10-08T18:49:11.4230000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6d.jsonl[15021] _id=6ad5743ade269131f9e91c4d ts=2026-10-19T01:36:57.7300000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[15022] _id=6ad5743ade269131f9e91c4e ts=2026-10-19T01:36:57.7300000Z; 1ms: 6ab9a9279a8420a1e6b56b6d.jsonl[14350] _id=6ad2731ade269131f9e775cc ts=2026-10-16T18:55:21.6360000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14351] _id=6ad2731ade269131f9e775cd ts=2026-10-16T18:55:21.6370000Z; 1ms: 6ab9a9279a8420a1e6b56b6d.jsonl[14542] _id=6ad56e8cde269131f9e90dab ts=2026-10-19T01:12:42.8110000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[14543] _id=6ad56e8cde269131f9e90dac ts=2026-10-19T01:12:42.8120000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 11h 13m 
  - Evidence: 11h 13m: 6ab9a9279a8420a1e6b56b6d.jsonl[12055] _id=6ad18b07de269131f9e2b898 ts=2026-10-16T02:25:10.6600000Z -> 6ab9a9279a8420a1e6b56b6d.jsonl[12144] _id=6ad228dbde269131f9e3cd28 ts=2026-10-16T13:38:34.4730000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[680] _id=6ac546a9de269131f9b74da3 ts=2026-10-06T19:06:16.0840000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[844] _id=6ac54826de269131f9b772ce ts=2026-10-06T19:12:37.8580000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[5425] _id=6ace7b4bde269131f9d10cc7 ts=2026-10-13T18:41:15.0790000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[9057] _id=6acfd3d9de269131f9d83cf3 ts=2026-10-14T19:11:21.4800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[817] _id=6ac547e5de269131f9b76e01 ts=2026-10-06T19:11:32.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[14096] _id=6ad27166de269131f9e7556f ts=2026-10-16T18:48:05.8270000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[14415] _id=6ad56d80de269131f9e90a70 ts=2026-10-19T01:08:15.4770000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[14726] _id=6ad571d6de269131f9e9150d ts=2026-10-19T01:26:45.8580000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[9319] _id=6ad0f899de269131f9dd0809 ts=2026-10-15T16:00:25.3450000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[11802] _id=6ad188b1de269131f9e2acff ts=2026-10-16T02:15:12.9520000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[12083] _id=6ad22842de269131f9e3c0ed ts=2026-10-16T13:36:01.3590000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[5550] _id=6ace7f5dde269131f9d136e5 ts=2026-10-13T18:58:36.1160000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[9131] _id=6acfd47cde269131f9d85877 ts=2026-10-14T19:14:04.1150000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[10429] _id=6ad12186de269131f9df7f84 ts=2026-10-15T18:55:01.6480000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 56 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[5712] _id=6ace8160de269131f9d1605c ts=2026-10-13T19:07:09.3190000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[5699] _id=6ace8160de269131f9d16062 ts=2026-10-13T19:07:09.3190000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[5682] _id=6ace8160de269131f9d1606f ts=2026-10-13T19:07:09.3940000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 578 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[1343] _id=6ac69516de269131f9be4fcc ts=2026-10-07T18:53:08.1720000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[1340] _id=6ac69516de269131f9be4fd5 ts=2026-10-07T18:53:08.1720000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[2672] _id=6ac698aede269131f9bef308 ts=2026-10-07T19:06:51.6800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[13488] _id=6ad256f4de269131f9e63dbb ts=2026-10-16T16:55:15.7600000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[812] _id=6ac547e9de269131f9b76e55 ts=2026-10-06T19:11:36.8330000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[7574] _id=6aceeb94de269131f9d2ac03 ts=2026-10-14T02:40:19.3590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 478 start, 469 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 40 unmatched 'BecameVisible' (totals: 1219 open, 1179 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 5 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 53 start, 41 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 313 of 15271 adjacent _id pairs reverse in client time; worst 170.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b6d.jsonl[1402] _id=6ac6953ede269131f9be5ae9 ts=2026-10-07T18:53:49.8080000Z`; `6ab9a9279a8420a1e6b56b6d.jsonl[1408] _id=6ac6953ede269131f9be5af5 ts=2026-10-07T18:50:59.2830000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.91s, min -194948.92s, max -0.12s over 15272 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b6d\coverage.yaml

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

### `InputEvent` — 5026 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1788); Unit 3 Dev (951); Unit 4 Dev - Dungeon (695); Unit 1 Dev (458); Unit 4 Dev - Anderson Base (317); Unit 3 Dungeon Dev (311); Unit 4 Dev (255); Unit 5 Dev - Dungeon (167); Unit 5 Dev (84)
- **Intervals:** median 1.06s (p5 0.09s / p95 17.84s, n=5025)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5026/5026 records)
    "pressed"  x5026
data.actionType  (string, 5026/5026 records)
    "Move"  x3866
    "Interact"  x546
    "Jump"  x215
    "Ascend"  x163
    "Sprint"  x142
    "Hoverboard"  x64
    "Map"  x20
    "Descend"  x5
    "Pause"  x2
    "SkipCinematic"  x2
    "ToggleDebug"  x1
data.key  (string, 5026/5026 records, 21 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5026/5026 records)
    "Player"  x3664
    "Drone"  x1362
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3906 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2886); Unit 4 Dev (552); Unit 3 Dungeon Dev (306); Unit 5 Dev - Dungeon (162)
- **Intervals:** median 0.09s (p5 0.00s / p95 2.97s, n=3905)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3906/3906 records)
    "BecameVisible"  x1219
    "BecameInvisible"  x1179
    "BecameCameraCentered"  x754
    "BecameCameraUncentered"  x754
data.pieceId  (string, 3906/3906 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3906/3906 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2619 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (857); Unit 3 Dev (353); Unit 4 Dev - Dungeon (339); Unit 4 Dev (238); Unit 1 Dev (235); Unit 5 Dev - Dungeon (178); Unit 3 Dungeon Dev (174); Unit 5 Dev (130); Unit 4 Dev - Anderson Base (115)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=2607)
- **Fields under `data`:**

```text
data.position  (object, 2619/2619 records)
data.position.x  (number, 2619/2619 records)
    numeric range -683.663 .. 1556.62 (1032 unique)
data.position.y  (number, 2619/2619 records)
    numeric range -112.491 .. 222.003 (629 unique)
data.position.z  (number, 2619/2619 records)
    numeric range -1266.14 .. 1999.22 (1033 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2435 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (761); Unit 3 Dev (384); Unit 4 Dev (299); Unit 5 Dev (224); Unit 1 Dev (204); Unit 3 Dungeon Dev (197); Unit 4 Dev - Dungeon (145); Unit 4 Dev - Anderson Base (141); Unit 5 Dev - Dungeon (80)
- **eventKey:** present on 1488 of 2435 records
- **Intervals:** median 3.82s (p5 0.00s / p95 44.06s, n=2434)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1488; [conversationId, dialogueEventType] x947
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2435/2435 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2435/2435 records)
    "DialogueNodeEvent"  x1488
    "DialogueStartEvent"  x478
    "DialogueFinishEvent"  x469
data.nodeId  (number, 1488/2435 records)
    numeric range 0 .. 290 (229 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 378 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (151); Unit 4 Dev - Dungeon (91); Unit 3 Dungeon Dev (51); Unit 4 Dev (30); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (11); Unit 1 Dev (10); Unit 5 Dev (8); Unit 5 Dev - Dungeon (8)
- **Intervals:** median 15.61s (p5 0.17s / p95 413.92s, n=377)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 378/378 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 378/378 records)
    104 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 328 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (100); Unit 5 Dev (74); Unit 3 Dev (67); Unit 2 Prod (Refactor) (55); Unit 1 Dev (32)
- **Intervals:** median 0.73s (p5 0.03s / p95 10.05s, n=327)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 328/328 records)
    "argumentationNodeHoverEnd"  x143
    "argumentationNodeHoverStart"  x142
    "argumentationNodeAdd"  x33
    "argumentationNodeRemove"  x10
data.argumentationTitle  (string, 328/328 records)
    "Unit 4 - Flooding"  x100
    "Unit 5"  x74
    "Unit 3 - Pollution Upstream"  x67
    "Unit 2 – Watershed"  x55
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x7
data.nodeName  (string, 328/328 records)
    "A"  x52
    "1"  x41
    "4"  x40
    "I"  x36
    "2"  x32
    "II"  x32
    "C"  x25
    "B"  x24
    "D"  x24
    "3"  x17
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 219 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (159); Unit 3 Dev (60)
- **Intervals:** median 3.48s (p5 0.75s / p95 693.41s, n=218)
- **`data` key-set variants:** [actionType, featureUsed, location] x93; [actionType, featureUsed] x90; [actionType, featureUsed, legendName] x36
- **Fields under `data`:**

```text
data.actionType  (string, 219/219 records)
    "WaypointMoveEvent"  x80
    "MapCloseEvent"  x45
    "MapOpenEvent"  x45
    "Selected"  x27
    "Unselected"  x9
    "WaypointSetEvent"  x9
    "WaypointResetEvent"  x4
data.featureUsed  (string, 219/219 records)
    "Waypoint"  x93
    "Map"  x90
    "Legend"  x36
data.legendName  (string, 36/219 records)
    13 unique values (see csv/event_unique_values.csv)
data.location  (object, 93/219 records)
data.location.x  (number, 93/219 records)
    numeric range -368.618 .. 176.874 (71 unique)
data.location.y  (number, 93/219 records)
    numeric range -194.445 .. 217.486 (77 unique)
data.location.z  (number, 93/219 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 94 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 4 Dev - Dungeon (16); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev (10); Unit 5 Dev - Dungeon (10); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 94 of 94 records
- **Intervals:** median 259.54s (p5 0.00s / p95 64019.98s, n=93)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x41
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 94/94 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x41
data.questID  (string, 94/94 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 94/94 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 41/94 records)
    "Succeeded"  x41
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 43 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (6); Unit 4 Dev (5); Unit 4 Dev - Dungeon (4); Unit 3 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1)
- **Intervals:** median 668.47s (p5 6.91s / p95 86832.64s, n=42)
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "DebugMenuStateChanged"  x43
data.isOpened  (bool, 43/43 records)
    false  x43
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `Soil Key Puzzle` — 41 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 4 Dev (17); Unit 3 Dev (6)
- **Intervals:** median 1.19s (p5 0.22s / p95 90627.16s, n=40)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x33; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/41 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/41 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 33/41 records)
    "RightDrag"  x17
    "LeftDrag"  x16
data.currentSoilType  (string, 33/41 records)
    "CLAY"  x9
    "CLAYROCK"  x7
    "CLAYSAND"  x5
    "SAND"  x4
    "BEDROCK"  x3
    "SANDGRAVEL"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 33/41 records)
    "false"  x26
    "true"  x7
data.waterLevelStatus  (string, 33/41 records)
    "Proper"  x12
    "TooLow"  x12
    "TooHigh"  x9
data.waterRetentionChange  (string, 33/41 records)
    "Increase"  x18
    "Decrease"  x8
    "NoChange"  x7
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 35 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (35)
- **Intervals:** median 17.88s (p5 1.14s / p95 211.25s, n=34)
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "On"  x23
    "Off"  x12
data.floor  (string, 35/35 records)
    "4"  x23
    "3"  x7
    "2"  x3
    "1"  x2
data.machineNumber  (string, 35/35 records)
    "One"  x34
    "Two"  x1
data.machineType  (string, 35/35 records)
    "Condenser"  x18
    "Evaporator"  x14
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 35/35 records)
    "3"  x20
    "2"  x8
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 28 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (9); Unit 1 Dev (6); Unit 3 Dev (5); Unit 5 Dev (5); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 21.19s (p5 1.53s / p95 191276.55s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "submitAnswerEvent"  x28
data.answerSubmitted  (string, 28/28 records, 1 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 28/28 records)
    "Unit 4 - Flooding"  x9
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 5"  x5
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 21 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 17092.22s (p5 1066.19s / p95 205762.82s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 25707.20s (p5 1046.38s / p95 226074.96s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 128.75s (p5 0.08s / p95 353542.23s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 12 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (12)
- **Intervals:** median 18.83s (p5 1.62s / p95 2785.13s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records, 5 empty-string)
    "cameraPlaced"  x7
    ""  x5
data.boxId  (string, 12/12 records)
    "0"  x6
    "1"  x3
    "2"  x3
data.soilType  (string, 12/12 records)
    "Sand"  x5
    "None"  x3
    "Clay"  x2
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 11 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (4)
- **Intervals:** median 54.58s (p5 1.74s / p95 258737.27s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "Open"  x6
    "Close"  x5
data.toolName  (string, 11/11 records, 11 empty-string)
    ""  x11
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 2.77s (p5 1.14s / p95 5.45s, n=10)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x10; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "optionSelected"  x10
    "DesignSubmitted"  x1
data.designSelections  (object, 1/11 records)
data.designSelections.glassRoofTemperature  (string, 1/11 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/11 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/11 records)
    "Tilted Out"  x1
data.featureUsed  (string, 11/11 records)
    "RoofStyle"  x7
    "GlassRoofTemperature"  x2
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 10/11 records)
    "Tilted Out"  x4
    "Flat"  x2
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `soilMachine` — 10 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (10)
- **Intervals:** median 202.74s (p5 1.58s / p95 24428.35s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "ChangeCanister"  x10
data.canisterType  (string, 10/10 records)
    "Gravel"  x5
    "Sand"  x3
    "Clay"  x2
data.floor  (string, 10/10 records)
    "4"  x6
    "3"  x2
    "5"  x2
data.machine  (string, 10/10 records)
    "1"  x9
    "2"  x1
data.row  (string, 10/10 records)
    "TopRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 7 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 82405.90s (p5 27344.78s / p95 344605.90s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    false  x7
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 3.12s (p5 1.02s / p95 505351.07s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Freshwater"  x3
    "Unit 2 – Watershed"  x3
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 171589.98s (p5 94357.15s / p95 566773.29s, n=4)
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

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 98360.02s (p5 10835.34s / p95 185884.69s, n=2)
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
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (27x); "Unselected" (9x); "WaypointMoveEvent" (80x); "WaypointResetEvent" (4x); "WaypointSetEvent" (9x)
- `TopographicMapEvent` data.featureUsed: "Legend" (36x); "Waypoint" (93x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (10x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*