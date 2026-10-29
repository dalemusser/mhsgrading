# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b78

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b78
- **Game version string(s) in log:** 2.8.9, 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b78.jsonl
- **Records:** 13603 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b78
- **Time span:** 2026-10-06T18:39:32.286000+00:00 .. 2026-10-19T16:10:58.463000+00:00 (309h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b78\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 13603 records, 10 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 109 INFO, 0 NOT_TESTED, 93 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5633 | 41.41 | 1 | 9 | 0 | 2026-10-06T18:43:41.994000+00:00 | 2026-10-19T16:10:51.513000+00:00 | 309h 27m |
| PuzzlePieceVisibleEvent | 2514 | 18.48 | 1 | 4 | 0 | 2026-10-06T19:12:57.504000+00:00 | 2026-10-16T18:46:45.832000+00:00 | 239h 33m |
| DialogueEvent | 2260 | 16.61 | 1 | 9 | 1403 | 2026-10-06T18:40:03.139000+00:00 | 2026-10-19T16:10:51.986000+00:00 | 309h 30m |
| PlayerPositionEvent | 1944 | 14.29 | 1 | 9 | 0 | 2026-10-06T18:39:43.278000+00:00 | 2026-10-19T16:10:58.463000+00:00 | 309h 31m |
| argumentationNodeEvent | 465 | 3.42 | 1 | 4 | 0 | 2026-10-06T19:01:16.348000+00:00 | 2026-10-16T16:05:50.862000+00:00 | 237h 4m |
| ObjectInterEvent | 259 | 1.9 | 1 | 9 | 0 | 2026-10-06T18:44:36.587000+00:00 | 2026-10-19T16:10:51.987000+00:00 | 309h 26m |
| questEvent | 88 | 0.65 | 1 | 9 | 88 | 2026-10-06T18:40:03.116000+00:00 | 2026-10-19T16:09:14.843000+00:00 | 309h 29m |
| WaterChamberEvent | 75 | 0.55 | 1 | 1 | 0 | 2026-10-16T18:47:00.439000+00:00 | 2026-10-19T16:05:04.767000+00:00 | 69h 18m |
| TopographicMapEvent | 63 | 0.46 | 1 | 2 | 0 | 2026-10-06T19:13:27.460000+00:00 | 2026-10-14T21:10:16.993000+00:00 | 193h 56m |
| Soil Key Puzzle | 60 | 0.44 | 1 | 3 | 0 | 2026-10-07T19:15:44.977000+00:00 | 2026-10-15T18:38:33.031000+00:00 | 191h 22m |
| DEBUGMenu | 58 | 0.43 | 1 | 9 | 0 | 2026-10-06T18:39:43.261000+00:00 | 2026-10-19T15:55:10.264000+00:00 | 309h 15m |
| argumentationAnswerEvent | 52 | 0.38 | 1 | 4 | 0 | 2026-10-06T19:02:51.424000+00:00 | 2026-10-16T16:05:51.953000+00:00 | 237h 3m |
| gameWindowFocusEvent | 30 | 0.22 | 1 | 3 | 0 | 2026-10-06T18:39:32.286000+00:00 | 2026-10-19T15:55:02.448000+00:00 | 309h 15m |
| gameStartEvent | 25 | 0.18 | 1 | 1 | 0 | 2026-10-06T18:39:32.287000+00:00 | 2026-10-19T15:55:02.448000+00:00 | 309h 15m |
| gameWindowUnfocusEvent | 15 | 0.11 | 1 | 5 | 0 | 2026-10-06T19:17:39.722000+00:00 | 2026-10-16T18:59:29.876000+00:00 | 239h 41m |
| DaniEvent | 12 | 0.09 | 1 | 2 | 0 | 2026-10-13T18:39:48.234000+00:00 | 2026-10-14T21:10:11.040000+00:00 | 26h 30m |
| argumentationEvent | 12 | 0.09 | 1 | 4 | 0 | 2026-10-06T19:02:16.968000+00:00 | 2026-10-16T16:05:52.014000+00:00 | 237h 3m |
| soilMachine | 11 | 0.08 | 1 | 1 | 0 | 2026-10-15T18:55:29.206000+00:00 | 2026-10-15T19:00:09.143000+00:00 | 4m 39s |
| TerasGardenBox | 10 | 0.07 | 1 | 1 | 0 | 2026-10-16T16:10:33.185000+00:00 | 2026-10-16T18:33:36.060000+00:00 | 2h 23m |
| argumentationToolEvent | 7 | 0.05 | 1 | 2 | 0 | 2026-10-06T19:02:10.684000+00:00 | 2026-10-14T18:56:07.904000+00:00 | 191h 53m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-06T19:07:46.586000+00:00 | 2026-10-16T18:41:29.949000+00:00 | 239h 33m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-16T18:41:58.313000+00:00 | 2026-10-19T16:05:56.623000+00:00 | 69h 23m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 74.22s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 163531.712s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.064s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.616s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 21.265s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.242s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 7.382s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 12.467s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 65.263s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1777.604s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 5172.804s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.053s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.8x vs baseline. 
  - Observed: 58 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
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
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: GRAVEL 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 240 ft; 270 ft; 300 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 75 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.4x vs baseline. 
  - Observed: 52 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,4,II; B,1,I; B,1,II; B,2,I; B,2,II; B,3,I; B,3,II; B,4,I; B,4,II; B,5,I; C,2,II; C,4,II; C,D,2,II; C,D,A,2,II; D,1,II; D,2,II; D,4,II; D,C,1,II; D,C,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 465 records 
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
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 25 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[150] _id=6ac5420fde269131f9b6de8d ts=2026-10-06T18:46:38.3780000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[208] _id=6ac542f9de269131f9b6fc9b ts=2026-10-06T18:50:32.3520000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[333] _id=6ac543b7de269131f9b709ff ts=2026-10-06T18:53:42.0580000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[4] _id=6ac54065de269131f9b6ac81 ts=2026-10-06T18:39:32.2870000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[719] _id=6ac54756de269131f9b763f9 ts=2026-10-06T19:09:09.8910000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1521] _id=6ac69359de269131f9be0200 ts=2026-10-07T18:45:44.7440000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 30 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 30} 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[5] _id=6ac54065de269131f9b6ac7f ts=2026-10-06T18:39:32.2860000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[715] _id=6ac54756de269131f9b763f7 ts=2026-10-06T19:09:09.8900000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1520] _id=6ac69359de269131f9be01ff ts=2026-10-07T18:45:44.7430000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[1518] _id=6ac69359de269131f9be01f6 ts=2026-10-06T19:17:39.722Z`; `6ab9a9279a8420a1e6b56b78.jsonl[2707] _id=6ac93120de269131f9cae69a ts=2026-10-07T19:17:15.387Z`; `6ab9a9279a8420a1e6b56b78.jsonl[3711] _id=6ace7a14de269131f9d0fb25 ts=2026-10-13T16:11:02.781Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 9 of 63 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[842] _id=6ac54858de269131f9b77979 ts=2026-10-06T19:13:27.4600000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[849] _id=6ac54860de269131f9b77a3f ts=2026-10-06T19:13:35.5560000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[857] _id=6ac54876de269131f9b77c89 ts=2026-10-06T19:13:57.2280000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5632 | 0.0 | 0.509 | 197.804 | 7.752 | 336671.162 | 0.3 | 254 | 18 |
| PuzzlePieceVisibleEvent | 2513 | 0.0 | 0.064 | 343.187 | 1.683 | 508169.301 | 0.17 | 1160 | 10 |
| DialogueEvent | 2259 | 0.0 | 4.317 | 493.249 | 29.933 | 336678.379 | 0.12 | 668 | 15 |
| PlayerPositionEvent | 1928 | 0.0 | 10.002 | 413.979 | 10.128 | 336672.218 | 0.14 | 1 | 12 |
| argumentationNodeEvent | 464 | 0.0 | 0.51 | 1839.385 | 11.371 | 687757.812 | 0.03 | 56 | 3 |
| ObjectInterEvent | 258 | 0.0 | 11.78 | 4317.734 | 895.815 | 506621.835 | 0.01 | 5 | 15 |
| questEvent | 87 | 0.0 | 194.27 | 12806.342 | 74660.886 | 336687.412 | 0.0 | 15 | 21 |
| WaterChamberEvent | 74 | 0.524 | 7.382 | 3371.41 | 48.931 | 248392.561 | 0.02 | 0 | 1 |
| TopographicMapEvent | 62 | 0.023 | 4.242 | 11261.444 | 6366.897 | 516658.824 | 0.01 | 2 | 7 |
| Soil Key Puzzle | 59 | 0.161 | 2.616 | 11677.425 | 13458.92 | 506576.881 | 0.01 | 0 | 5 |
| DEBUGMenu | 57 | 0.36 | 74.22 | 19532.053 | 102278.86 | 336675.365 | 0.0 | 0 | 21 |
| argumentationAnswerEvent | 51 | 0.79 | 12.467 | 16732.952 | 1380.727 | 687807.068 | 0.0 | 0 | 3 |
| gameWindowFocusEvent | 29 | 13.034 | 1777.604 | 38390.695 | 218102.207 | 336686.654 | 0.0 | 0 | 19 |
| gameStartEvent | 24 | 54.309 | 4138.742 | 46388.757 | 237534.957 | 336686.655 | 0.0 | 0 | 18 |
| gameWindowUnfocusEvent | 14 | 6.785 | 5172.804 | 61636.44 | 233701.686 | 507227.394 | 0.0 | 0 | 9 |
| DaniEvent | 11 | 1.39 | 2.99 | 8674.801 | 47635.357 | 86614.222 | 0.01 | 0 | 2 |
| argumentationEvent | 11 | 0.038 | 112.558 | 77583.186 | 424904.309 | 687749.914 | 0.0 | 1 | 3 |
| soilMachine | 10 | 0.711 | 3.053 | 27.994 | 131.731 | 173.01 | 2.14 | 0 | 0 |
| TerasGardenBox | 9 | 1.296 | 21.265 | 953.653 | 5097.22 | 8478.153 | 0.06 | 0 | 1 |
| argumentationToolEvent | 6 | 1.516 | 65.263 | 115139.537 | 517974.039 | 690598.614 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 10920.226 | 163531.712 | 287474.454 | 635527.454 | 687971.425 | 0.0 | 0 | 3 |
| chatEvent | 3 | 646.536 | 878.343 | 83279.437 | 223569.922 | 248313.431 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 14 group(s), 30 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[1514] _id=6ac6936bde269131f9be042a ts=2026-10-07T18:46:01.0740000Z == 6ab9a9279a8420a1e6b56b78.jsonl[1515] _id=6ac6936bde269131f9be042b ts=2026-10-07T18:46:01.0740000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1516] _id=6ac6936bde269131f9be042c ts=2026-10-07T18:46:01.0750000Z == 6ab9a9279a8420a1e6b56b78.jsonl[1517] _id=6ac6936bde269131f9be042d ts=2026-10-07T18:46:01.0750000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[2711] _id=6ac93131de269131f9cae6b6 ts=2026-10-09T18:23:44.4240000Z == 6ab9a9279a8420a1e6b56b78.jsonl[2712] _id=6ac93131de269131f9cae6b7 ts=2026-10-09T18:23:44.4240000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 64 group(s), 100 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[909] _id=6ac548b2de269131f9b784d9 ts=2026-10-06T19:12:58.2640000Z == 6ab9a9279a8420a1e6b56b78.jsonl[905] _id=6ac548b2de269131f9b784dd ts=2026-10-06T19:12:58.2640000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[821] _id=6ac54840de269131f9b775ce ts=2026-10-06T19:13:01.2690000Z == 6ab9a9279a8420a1e6b56b78.jsonl[815] _id=6ac54840de269131f9b775df ts=2026-10-06T19:13:01.2690000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[823] _id=6ac54840de269131f9b775f1 ts=2026-10-06T19:13:01.5090000Z == 6ab9a9279a8420a1e6b56b78.jsonl[824] _id=6ac54841de269131f9b775fc ts=2026-10-06T19:13:01.5090000Z`
- **INFO / Info** `DEBUGMenu` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `360ms: 6ab9a9279a8420a1e6b56b78.jsonl[7279] _id=6ad0f808de269131f9dcfb66 ts=2026-10-15T15:57:58.1380000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[7280] _id=6ad0f808de269131f9dcfb67 ts=2026-10-15T15:57:58.4980000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b78.jsonl[101] _id=6ac54195de269131f9b6ce3f ts=2026-10-06T18:44:36.5870000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[102] _id=6ac54195de269131f9b6ce49 ts=2026-10-06T18:44:36.5920000Z`; `236ms: 6ab9a9279a8420a1e6b56b78.jsonl[8699] _id=6ad10695de269131f9de2e3c ts=2026-10-15T17:00:03.2360000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[8701] _id=6ad10695de269131f9de2e3e ts=2026-10-15T17:00:03.4720000Z`; `235ms: 6ab9a9279a8420a1e6b56b78.jsonl[8701] _id=6ad10695de269131f9de2e3e ts=2026-10-15T17:00:03.4720000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[8703] _id=6ad10695de269131f9de2e40 ts=2026-10-15T17:00:03.7070000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 126 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `99ms: 6ab9a9279a8420a1e6b56b78.jsonl[808] _id=6ac5483ede269131f9b775ac ts=2026-10-06T19:13:01.1210000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[809] _id=6ac5483fde269131f9b775b4 ts=2026-10-06T19:13:01.2200000Z`; `23ms: 6ab9a9279a8420a1e6b56b78.jsonl[810] _id=6ac54840de269131f9b775e5 ts=2026-10-06T19:13:01.2690000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[822] _id=6ac54840de269131f9b775eb ts=2026-10-06T19:13:01.2920000Z`; `217ms: 6ab9a9279a8420a1e6b56b78.jsonl[822] _id=6ac54840de269131f9b775eb ts=2026-10-06T19:13:01.2920000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[823] _id=6ac54840de269131f9b775f1 ts=2026-10-06T19:13:01.5090000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `997ms: 6ab9a9279a8420a1e6b56b78.jsonl[5806] _id=6acfcff5de269131f9d7b585 ts=2026-10-14T18:54:44.8430000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[5721] _id=6acfcff6de269131f9d7b5a2 ts=2026-10-14T18:54:45.8400000Z`; `790ms: 6ab9a9279a8420a1e6b56b78.jsonl[11261] _id=6ad249e4de269131f9e57906 ts=2026-10-16T15:59:31.1230000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[11260] _id=6ad249e4de269131f9e57920 ts=2026-10-16T15:59:31.9130000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `53ms: 6ab9a9279a8420a1e6b56b78.jsonl[5882] _id=6acfd059de269131f9d7c11d ts=2026-10-14T18:56:24.9010000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[5885] _id=6acfd059de269131f9d7c120 ts=2026-10-14T18:56:24.9540000Z`; `38ms: 6ab9a9279a8420a1e6b56b78.jsonl[11589] _id=6ad24b61de269131f9e59295 ts=2026-10-16T16:05:51.9760000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[11576] _id=6ad24b61de269131f9e5929f ts=2026-10-16T16:05:52.0140000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6ab9a9279a8420a1e6b56b78.jsonl[504] _id=6ac545d9de269131f9b7317b ts=2026-10-06T19:02:48.1450000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[505] _id=6ac545d9de269131f9b7317d ts=2026-10-06T19:02:48.1650000Z`; `518ms: 6ab9a9279a8420a1e6b56b78.jsonl[584] _id=6ac54634de269131f9b73c0f ts=2026-10-06T19:04:19.9640000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[581] _id=6ac54635de269131f9b73c21 ts=2026-10-06T19:04:20.4820000Z`; `577ms: 6ab9a9279a8420a1e6b56b78.jsonl[580] _id=6ac54635de269131f9b73c19 ts=2026-10-06T19:04:20.1200000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[585] _id=6ac54635de269131f9b73c2b ts=2026-10-06T19:04:20.6970000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `711ms: 6ab9a9279a8420a1e6b56b78.jsonl[10458] _id=6ad122b6de269131f9dfa947 ts=2026-10-15T19:00:04.1000000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[10461] _id=6ad122b6de269131f9dfa94a ts=2026-10-15T19:00:04.8110000Z`; `745ms: 6ab9a9279a8420a1e6b56b78.jsonl[10461] _id=6ad122b6de269131f9dfa94a ts=2026-10-15T19:00:04.8110000Z ~ 6ab9a9279a8420a1e6b56b78.jsonl[10464] _id=6ad122b6de269131f9dfa94d ts=2026-10-15T19:00:05.5560000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2708] _id=6ac9312bde269131f9cae6ae ts=2026-10-09T18:23:39.3050000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2762] _id=6ace544fde269131f9cf4b83 ts=2026-10-13T15:54:54.6700000Z; 69h 13m: 6ab9a9279a8420a1e6b56b78.jsonl[12167] _id=6ad26ff9de269131f9e739a1 ts=2026-10-16T18:41:58.5970000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12841] _id=6ad63d56de269131f9e987af ts=2026-10-19T15:55:02.3090000Z; 47h 37m: 6ab9a9279a8420a1e6b56b78.jsonl[1511] _id=6ac69364de269131f9be0375 ts=2026-10-07T18:45:55.9880000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2701] _id=6ac93120de269131f9cae69c ts=2026-10-09T18:23:28.1900000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 24h 3m 
  - Evidence: 24h 3m: 6ab9a9279a8420a1e6b56b78.jsonl[3945] _id=6ace7af6de269131f9d10879 ts=2026-10-13T18:39:49.6240000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5405] _id=6acfcd4cde269131f9d76a37 ts=2026-10-14T18:43:23.8460000Z; 2h 24m: 6ab9a9279a8420a1e6b56b78.jsonl[5406] _id=6acfcd4fde269131f9d76aae ts=2026-10-14T18:43:26.8360000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[7071] _id=6acfef1fde269131f9d96ccf ts=2026-10-14T21:07:43.3280000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2705] _id=6ac93139de269131f9cae6c6 ts=2026-10-09T18:23:53.4780000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2774] _id=6ace5461de269131f9cf4b90 ts=2026-10-13T15:55:11.8570000Z; 68h 55m: 6ab9a9279a8420a1e6b56b78.jsonl[12830] _id=6ad2740ede269131f9e78651 ts=2026-10-16T18:59:26.2510000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12834] _id=6ad63d68de269131f9e987d7 ts=2026-10-19T15:55:19.8080000Z; 47h 6m: 6ab9a9279a8420a1e6b56b78.jsonl[2700] _id=6ac69ab5de269131f9bf204c ts=2026-10-07T19:17:08.9590000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2717] _id=6ac93131de269131f9cae6bc ts=2026-10-09T18:23:44.4440000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 668 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[11176] _id=6ad249b5de269131f9e575d6 ts=2026-10-16T15:58:44.8610000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11177] _id=6ad249b5de269131f9e575d7 ts=2026-10-16T15:58:44.8610000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[11250] _id=6ad249ddde269131f9e5787d ts=2026-10-16T15:59:24.2420000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11251] _id=6ad249ddde269131f9e5787e ts=2026-10-16T15:59:24.2420000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[11339] _id=6ad24a2ade269131f9e57d91 ts=2026-10-16T16:00:40.6060000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11340] _id=6ad24a2ade269131f9e57d92 ts=2026-10-16T16:00:40.6060000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 6m 
  - Evidence: 191h 6m: 6ab9a9279a8420a1e6b56b78.jsonl[713] _id=6ac54703de269131f9b75ca9 ts=2026-10-06T19:07:46.5860000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5019] _id=6acfc667de269131f9d6f06c ts=2026-10-14T18:13:58.0110000Z; 45h 25m: 6ab9a9279a8420a1e6b56b78.jsonl[7266] _id=6acff10ede269131f9d9775e ts=2026-10-14T21:15:58.2370000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12160] _id=6ad26fdade269131f9e737b0 ts=2026-10-16T18:41:29.9490000Z; 3h 2m: 6ab9a9279a8420a1e6b56b78.jsonl[5019] _id=6acfc667de269131f9d6f06c ts=2026-10-14T18:13:58.0110000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[7266] _id=6acff10ede269131f9d9775e ts=2026-10-14T21:15:58.2370000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2724] _id=6ac93140de269131f9cae6d6 ts=2026-10-09T18:24:00.6750000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2773] _id=6ace5461de269131f9cf4b8f ts=2026-10-13T15:55:11.8370000Z; 68h 58m: 6ab9a9279a8420a1e6b56b78.jsonl[12795] _id=6ad27355de269131f9e77b13 ts=2026-10-16T18:56:21.1840000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12833] _id=6ad63d67de269131f9e987d5 ts=2026-10-19T15:55:19.2210000Z; 47h 6m: 6ab9a9279a8420a1e6b56b78.jsonl[2699] _id=6ac69ab6de269131f9bf2054 ts=2026-10-07T19:17:09.5770000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2710] _id=6ac93131de269131f9cae6b5 ts=2026-10-09T18:23:44.4230000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 254 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[10057] _id=6ad1219dde269131f9df81ea ts=2026-10-15T18:55:25.0630000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[10058] _id=6ad1219dde269131f9df81eb ts=2026-10-15T18:55:25.0630000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[10076] _id=6ad121a9de269131f9df83d4 ts=2026-10-15T18:55:37.1210000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[10077] _id=6ad121a9de269131f9df83d5 ts=2026-10-15T18:55:37.1210000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[10308] _id=6ad1225ade269131f9df9d99 ts=2026-10-15T18:58:34.3950000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[10309] _id=6ad1225ade269131f9df9d9a ts=2026-10-15T18:58:34.3950000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 140h 43m 
  - Evidence: 140h 43m: 6ab9a9279a8420a1e6b56b78.jsonl[2649] _id=6ac69a61de269131f9bf18e9 ts=2026-10-07T19:15:44.9820000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[3003] _id=6ace555fde269131f9cf4fd1 ts=2026-10-13T15:59:26.8170000Z; 69h 2m: 6ab9a9279a8420a1e6b56b78.jsonl[12580] _id=6ad272aede269131f9e76e5b ts=2026-10-16T18:53:34.4030000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12869] _id=6ad63d80de269131f9e9883c ts=2026-10-19T15:55:44.4520000Z; 24h 0m: 6ab9a9279a8420a1e6b56b78.jsonl[3557] _id=6ace5682de269131f9cf5520 ts=2026-10-13T16:04:17.8490000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[4624] _id=6acfa80ede269131f9d5266e ts=2026-10-14T16:04:30.0410000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[10920] _id=6ad125c0de269131f9e02313 ts=2026-10-15T19:13:03.8520000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[10921] _id=6ad125c0de269131f9e02314 ts=2026-10-15T19:13:03.8520000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[10965] _id=6ad12610de269131f9e02dfa ts=2026-10-15T19:14:23.7770000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[10966] _id=6ad12610de269131f9e02dfb ts=2026-10-15T19:14:23.7770000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[11065] _id=6ad24894de269131f9e56635 ts=2026-10-16T15:53:55.1450000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11066] _id=6ad24894de269131f9e56636 ts=2026-10-16T15:53:55.1450000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2706] _id=6ac9313ade269131f9cae6c8 ts=2026-10-09T18:23:54.8650000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2752] _id=6ace5461de269131f9cf4b8e ts=2026-10-13T15:55:07.0830000Z; 47h 6m: 6ab9a9279a8420a1e6b56b78.jsonl[2698] _id=6ac69ab4de269131f9bf2041 ts=2026-10-07T19:17:07.4180000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2709] _id=6ac93131de269131f9cae6b4 ts=2026-10-09T18:23:39.3220000Z; 23h 28m: 6ab9a9279a8420a1e6b56b78.jsonl[1506] _id=6ac5494dde269131f9b79c1c ts=2026-10-06T19:17:32.1390000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[1512] _id=6ac6936bde269131f9be0428 ts=2026-10-07T18:45:56.0000000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[8722] _id=6ad106a9de269131f9de30aa ts=2026-10-15T17:00:24.7920000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[8726] _id=6ad106b8de269131f9de31e5 ts=2026-10-15T17:00:24.792Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 141h 9m 
  - Evidence: 141h 9m: 6ab9a9279a8420a1e6b56b78.jsonl[1738] _id=6ac6949ede269131f9be3853 ts=2026-10-07T18:51:07.1530000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[3075] _id=6ace55a5de269131f9cf508c ts=2026-10-13T16:00:36.4540000Z; 23h 49m: 6ab9a9279a8420a1e6b56b78.jsonl[4406] _id=6ace8277de269131f9d18a80 ts=2026-10-13T19:11:49.7020000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[6173] _id=6acfd19cde269131f9d7e5cc ts=2026-10-14T19:01:46.7760000Z; 23h 37m: 6ab9a9279a8420a1e6b56b78.jsonl[10665] _id=6ad123d6de269131f9dfd8e6 ts=2026-10-15T19:04:51.4720000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12169] _id=6ad26ffede269131f9e739f8 ts=2026-10-16T18:42:05.0160000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1160 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[1005] _id=6ac548c9de269131f9b7889f ts=2026-10-06T19:15:19.5730000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[1006] _id=6ac548cade269131f9b788a6 ts=2026-10-06T19:15:19.5730000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[1017] _id=6ac548cbde269131f9b788d8 ts=2026-10-06T19:15:20.9100000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[1012] _id=6ac548cbde269131f9b788db ts=2026-10-06T19:15:20.9100000Z; 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[1034] _id=6ac548ddde269131f9b78bef ts=2026-10-06T19:15:38.7710000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[1098] _id=6ac548ddde269131f9b78bfb ts=2026-10-06T19:15:38.7710000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 140h 42m 
  - Evidence: 140h 42m: 6ab9a9279a8420a1e6b56b78.jsonl[2678] _id=6ac69a8ede269131f9bf1d99 ts=2026-10-07T19:16:29.9280000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[3002] _id=6ace555fde269131f9cf4fcf ts=2026-10-13T15:59:26.8090000Z; 27h 0m: 6ab9a9279a8420a1e6b56b78.jsonl[3058] _id=6ace5582de269131f9cf5029 ts=2026-10-13T16:00:01.7540000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[6133] _id=6acfd159de269131f9d7dd63 ts=2026-10-14T19:00:40.9010000Z; 21h 8m: 6ab9a9279a8420a1e6b56b78.jsonl[6150] _id=6acfd172de269131f9d7e056 ts=2026-10-14T19:01:05.9270000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[7451] _id=6ad0faadde269131f9dd479f ts=2026-10-15T16:09:16.9810000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 21m 
  - Evidence: 2h 21m: 6ab9a9279a8420a1e6b56b78.jsonl[11799] _id=6ad24c90de269131f9e5a6e6 ts=2026-10-16T16:10:55.1240000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11863] _id=6ad26dadde269131f9e70357 ts=2026-10-16T18:32:13.2770000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a9279a8420a1e6b56b78.jsonl[2456] _id=6ac698bbde269131f9bef47d ts=2026-10-07T19:08:42.3460000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[3941] _id=6ace7aeede269131f9d107e3 ts=2026-10-13T18:39:41.1700000Z; 23h 43m: 6ab9a9279a8420a1e6b56b78.jsonl[4146] _id=6ace7db4de269131f9d12ce1 ts=2026-10-13T18:51:31.3160000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5117] _id=6acfcb6dde269131f9d723a0 ts=2026-10-14T18:35:25.4470000Z; 23h 34m: 6ab9a9279a8420a1e6b56b78.jsonl[857] _id=6ac54876de269131f9b77c89 ts=2026-10-06T19:13:57.2280000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[1595] _id=6ac693f6de269131f9be18a7 ts=2026-10-07T18:48:21.6930000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.029s shown 
  - Evidence: 23ms: 6ab9a9279a8420a1e6b56b78.jsonl[2310] _id=6ac696ffde269131f9bebdde ts=2026-10-07T19:01:18.6080000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2314] _id=6ac696ffde269131f9bebde2 ts=2026-10-07T19:01:18.6310000Z; 29ms: 6ab9a9279a8420a1e6b56b78.jsonl[2308] _id=6ac696ffde269131f9bebdd6 ts=2026-10-07T19:01:18.5790000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2310] _id=6ac696ffde269131f9bebdde ts=2026-10-07T19:01:18.6080000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 68h 59m 
  - Evidence: 68h 59m: 6ab9a9279a8420a1e6b56b78.jsonl[12752] _id=6ad27328de269131f9e776fe ts=2026-10-16T18:55:36.6020000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12857] _id=6ad63d71de269131f9e987f5 ts=2026-10-19T15:55:29.1630000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 3m 
  - Evidence: 191h 3m: 6ab9a9279a8420a1e6b56b78.jsonl[595] _id=6ac5463dde269131f9b73d6d ts=2026-10-06T19:04:29.0920000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[4887] _id=6acfc4fdde269131f9d6e633 ts=2026-10-14T18:07:56.1600000Z; 45h 2m: 6ab9a9279a8420a1e6b56b78.jsonl[5881] _id=6acfd059de269131f9d7c114 ts=2026-10-14T18:56:24.8780000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11207] _id=6ad249b5de269131f9e575d4 ts=2026-10-16T15:58:44.8390000Z; 44m 23s: 6ab9a9279a8420a1e6b56b78.jsonl[4927] _id=6acfc534de269131f9d6e731 ts=2026-10-14T18:08:51.5780000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5744] _id=6acfcf9bde269131f9d7acf0 ts=2026-10-14T18:53:15.3650000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 2m 
  - Evidence: 191h 2m: 6ab9a9279a8420a1e6b56b78.jsonl[591] _id=6ac5463ede269131f9b73d75 ts=2026-10-06T19:04:29.1390000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[4822] _id=6acfc4c4de269131f9d6e4dd ts=2026-10-14T18:06:59.0530000Z; 45h 0m: 6ab9a9279a8420a1e6b56b78.jsonl[5885] _id=6acfd059de269131f9d7c120 ts=2026-10-14T18:56:24.9540000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11154] _id=6ad24964de269131f9e56eb8 ts=2026-10-16T15:57:23.6590000Z; 43m 43s: 6ab9a9279a8420a1e6b56b78.jsonl[4924] _id=6acfc534de269131f9d6e733 ts=2026-10-14T18:08:51.6110000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5707] _id=6acfcf73de269131f9d7a894 ts=2026-10-14T18:52:35.3880000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.038s..0.038s shown 
  - Evidence: 38ms: 6ab9a9279a8420a1e6b56b78.jsonl[11589] _id=6ad24b61de269131f9e59295 ts=2026-10-16T16:05:51.9760000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11576] _id=6ad24b61de269131f9e5929f ts=2026-10-16T16:05:52.0140000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 2m 
  - Evidence: 191h 2m: 6ab9a9279a8420a1e6b56b78.jsonl[590] _id=6ac54639de269131f9b73ce7 ts=2026-10-06T19:04:24.9840000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[4838] _id=6acfc4c7de269131f9d6e4f6 ts=2026-10-14T18:07:02.7960000Z; 45h 0m: 6ab9a9279a8420a1e6b56b78.jsonl[5880] _id=6acfd057de269131f9d7c0d9 ts=2026-10-14T18:56:23.4880000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11152] _id=6ad24962de269131f9e56e90 ts=2026-10-16T15:57:21.0050000Z; 43m 51s: 6ab9a9279a8420a1e6b56b78.jsonl[4918] _id=6acfc532de269131f9d6e71e ts=2026-10-14T18:08:49.4770000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5712] _id=6acfcf78de269131f9d7a93b ts=2026-10-14T18:52:40.5110000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 56 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[11210] _id=6ad249bdde269131f9e57627 ts=2026-10-16T15:58:52.4890000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11211] _id=6ad249bdde269131f9e57628 ts=2026-10-16T15:58:52.4890000Z; 4ms: 6ab9a9279a8420a1e6b56b78.jsonl[4878] _id=6acfc4f6de269131f9d6e61c ts=2026-10-14T18:07:49.4420000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[4881] _id=6acfc4f6de269131f9d6e61e ts=2026-10-14T18:07:49.4460000Z; 5ms: 6ab9a9279a8420a1e6b56b78.jsonl[11278] _id=6ad249eede269131f9e579cb ts=2026-10-16T15:59:41.8740000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[11270] _id=6ad249eede269131f9e579cd ts=2026-10-16T15:59:41.8790000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 49m 
  - Evidence: 191h 49m: 6ab9a9279a8420a1e6b56b78.jsonl[562] _id=6ac5461ede269131f9b73855 ts=2026-10-06T19:03:57.2490000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[5776] _id=6acfcfc4de269131f9d7b097 ts=2026-10-14T18:53:55.8630000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 68h 58m 
  - Evidence: 68h 58m: 6ab9a9279a8420a1e6b56b78.jsonl[12796] _id=6ad27365de269131f9e77c13 ts=2026-10-16T18:56:36.6560000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12844] _id=6ad63d5ede269131f9e987bb ts=2026-10-19T15:55:10.0870000Z; 14m 38s: 6ab9a9279a8420a1e6b56b78.jsonl[12165] _id=6ad26ff6de269131f9e7397b ts=2026-10-16T18:41:58.3130000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12796] _id=6ad27365de269131f9e77c13 ts=2026-10-16T18:56:36.6560000Z; 10m 46s: 6ab9a9279a8420a1e6b56b78.jsonl[12844] _id=6ad63d5ede269131f9e987bb ts=2026-10-19T15:55:10.0870000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12832] _id=6ad63fe4de269131f9e99c15 ts=2026-10-19T16:05:56.6230000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2703] _id=6ac93120de269131f9cae69e ts=2026-10-09T18:23:28.3500000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2755] _id=6ace544fde269131f9cf4b86 ts=2026-10-13T15:54:55.0050000Z; 69h 13m: 6ab9a9279a8420a1e6b56b78.jsonl[12164] _id=6ad26fecde269131f9e738ec ts=2026-10-16T18:41:47.8410000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12843] _id=6ad63d56de269131f9e987b1 ts=2026-10-19T15:55:02.4480000Z; 47h 37m: 6ab9a9279a8420a1e6b56b78.jsonl[1521] _id=6ac69359de269131f9be0200 ts=2026-10-07T18:45:44.7440000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2703] _id=6ac93120de269131f9cae69e ts=2026-10-09T18:23:28.3500000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2702] _id=6ac93120de269131f9cae69d ts=2026-10-09T18:23:28.3500000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2754] _id=6ace544fde269131f9cf4b85 ts=2026-10-13T15:54:55.0040000Z; 69h 13m: 6ab9a9279a8420a1e6b56b78.jsonl[12163] _id=6ad26fecde269131f9e738eb ts=2026-10-16T18:41:47.8410000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12842] _id=6ad63d56de269131f9e987b0 ts=2026-10-19T15:55:02.4480000Z; 47h 37m: 6ab9a9279a8420a1e6b56b78.jsonl[1520] _id=6ac69359de269131f9be01ff ts=2026-10-07T18:45:44.7430000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2702] _id=6ac93120de269131f9cae69d ts=2026-10-09T18:23:28.3500000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 140h 53m 
  - Evidence: 140h 53m: 6ab9a9279a8420a1e6b56b78.jsonl[2707] _id=6ac93120de269131f9cae69a ts=2026-10-07T19:17:15.387Z -> 6ab9a9279a8420a1e6b56b78.jsonl[3711] _id=6ace7a14de269131f9d0fb25 ts=2026-10-13T16:11:02.781Z; 24h 0m: 6ab9a9279a8420a1e6b56b78.jsonl[4824] _id=6acfc4adde269131f9d6e44b ts=2026-10-14T16:10:45.585Z -> 6ab9a9279a8420a1e6b56b78.jsonl[7743] _id=6ad103a4de269131f9dddb0b ts=2026-10-15T16:11:04.197Z; 23h 59m: 6ab9a9279a8420a1e6b56b78.jsonl[1518] _id=6ac69359de269131f9be01f6 ts=2026-10-06T19:17:39.722Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2707] _id=6ac93120de269131f9cae69a ts=2026-10-07T19:17:15.387Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 93h 31m 
  - Evidence: 93h 31m: 6ab9a9279a8420a1e6b56b78.jsonl[2719] _id=6ac93131de269131f9cae6be ts=2026-10-09T18:23:44.4890000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2776] _id=6ace5461de269131f9cf4b92 ts=2026-10-13T15:55:11.9010000Z; 69h 1m: 6ab9a9279a8420a1e6b56b78.jsonl[12671] _id=6ad272b3de269131f9e76ec4 ts=2026-10-16T18:53:39.0320000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[12847] _id=6ad63d61de269131f9e987c1 ts=2026-10-19T15:55:12.6630000Z; 47h 8m: 6ab9a9279a8420a1e6b56b78.jsonl[2652] _id=6ac69a59de269131f9bf1802 ts=2026-10-07T19:15:36.9460000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[2719] _id=6ac93131de269131f9cae6be ts=2026-10-09T18:23:44.4890000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b78.jsonl[13060] _id=6ad63e2dde269131f9e98cb0 ts=2026-10-19T15:58:37.1390000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[13061] _id=6ad63e2dde269131f9e98cb1 ts=2026-10-19T15:58:37.1390000Z; 2ms: 6ab9a9279a8420a1e6b56b78.jsonl[482] _id=6ac54547de269131f9b725d3 ts=2026-10-06T19:00:22.0370000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[483] _id=6ac54547de269131f9b725d9 ts=2026-10-06T19:00:22.0390000Z; 5ms: 6ab9a9279a8420a1e6b56b78.jsonl[9385] _id=6ad11ecfde269131f9df27e4 ts=2026-10-15T18:43:27.1420000Z -> 6ab9a9279a8420a1e6b56b78.jsonl[9383] _id=6ad11ecfde269131f9df27ee ts=2026-10-15T18:43:27.1470000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[457] _id=6ac54525de269131f9b722e5 ts=2026-10-06T18:59:48.5950000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[606] _id=6ac5466fde269131f9b74483 ts=2026-10-06T19:05:18.3670000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[2455] _id=6ac698b8de269131f9bef430 ts=2026-10-07T19:08:40.0410000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 29 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[1069] _id=6ac548d9de269131f9b78b11 ts=2026-10-06T19:15:33.8730000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1060] _id=6ac548d9de269131f9b78b1b ts=2026-10-06T19:15:33.9050000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1075] _id=6ac548d9de269131f9b78b25 ts=2026-10-06T19:15:33.9600000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 65 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[905] _id=6ac548b2de269131f9b784dd ts=2026-10-06T19:12:58.2640000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[810] _id=6ac54840de269131f9b775e5 ts=2026-10-06T19:13:01.2690000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[822] _id=6ac54840de269131f9b775eb ts=2026-10-06T19:13:01.2920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[5885] _id=6acfd059de269131f9d7c120 ts=2026-10-14T18:56:24.9540000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[11576] _id=6ad24b61de269131f9e5929f ts=2026-10-16T16:05:52.0140000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[505] _id=6ac545d9de269131f9b7317d ts=2026-10-06T19:02:48.1650000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[12165] _id=6ad26ff6de269131f9e7397b ts=2026-10-16T18:41:58.3130000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[12796] _id=6ad27365de269131f9e77c13 ts=2026-10-16T18:56:36.6560000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[12844] _id=6ad63d5ede269131f9e987bb ts=2026-10-19T15:55:10.0870000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[8493] _id=6ad105e7de269131f9de1c0b ts=2026-10-15T16:57:11.0300000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[9385] _id=6ad11ecfde269131f9df27e4 ts=2026-10-15T18:43:27.1420000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[13052] _id=6ad63e2dde269131f9e98ca9 ts=2026-10-19T15:58:37.0980000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[1525] _id=6ac6936bde269131f9be043d ts=?`; `6ab9a9279a8420a1e6b56b78.jsonl[5071] _id=6acfc757de269131f9d6fb38 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 233 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[1118] _id=6ac548e0de269131f9b78c5b ts=2026-10-06T19:15:42.5020000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1128] _id=6ac548e2de269131f9b78c9b ts=2026-10-06T19:15:45.7290000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[1141] _id=6ac548e6de269131f9b78d13 ts=2026-10-06T19:15:48.5670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 506 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[879] _id=6ac548b2de269131f9b784f3 ts=2026-10-06T19:12:58.2640000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[809] _id=6ac5483fde269131f9b775b4 ts=2026-10-06T19:13:01.2200000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[807] _id=6ac54841de269131f9b77605 ts=2026-10-06T19:13:01.5090000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[5839] _id=6acfd020de269131f9d7ba9e ts=2026-10-14T18:55:27.7380000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[5840] _id=6acfd021de269131f9d7bab7 ts=2026-10-14T18:55:29.2540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 DEBUGMenu record in 'Unit 3 Dev' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[5079] _id=6acfc77fde269131f9d6fc6d ts=2026-10-14T18:18:38.2890000Z`
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 DEBUGMenu record in 'Unit 4 Dev' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[7278] _id=6ad0f806de269131f9dcfb31 ts=2026-10-15T15:57:57.3480000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 434 start, 423 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 33 unmatched 'BecameCameraCentered' (totals: 554 open, 550 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 127 unmatched 'BecameVisible' (totals: 736 open, 674 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 6 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'questActiveEvent' (totals: 55 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 340 of 13600 adjacent _id pairs reverse in client time; worst 117.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b78.jsonl[890] _id=6ac548afde269131f9b78459 ts=2026-10-06T19:14:54.6670000Z`; `6ab9a9279a8420a1e6b56b78.jsonl[902] _id=6ac548b0de269131f9b7847d ts=2026-10-06T19:12:57.5040000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.72s, min -248132.80s, max -0.08s over 13601 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b78\coverage.yaml

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
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5633 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1358); Unit 2 Prod (Refactor) (1224); Unit 4 Dev (906); Unit 5 Dev - Dungeon (705); Unit 3 Dev (562); Unit 3 Dungeon Dev (420); Unit 1 Dev (269); Unit 5 Dev (104); Unit 4 Dev - Anderson Base (85)
- **Intervals:** median 0.51s (p5 0.06s / p95 7.75s, n=5632)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5633/5633 records)
    "pressed"  x5633
data.actionType  (string, 5633/5633 records)
    "Move"  x4362
    "Interact"  x754
    "Jump"  x247
    "Sprint"  x160
    "Ascend"  x44
    "Hoverboard"  x42
    "Descend"  x17
    "Pause"  x5
    "SkipCinematic"  x2
data.key  (string, 5633/5633 records, 3 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5633/5633 records)
    "Player"  x5134
    "Drone"  x499
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2514 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1420); Unit 4 Dev (764); Unit 5 Dev - Dungeon (166); Unit 3 Dungeon Dev (164)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.68s, n=2513)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2514/2514 records)
    "BecameVisible"  x736
    "BecameInvisible"  x674
    "BecameCameraCentered"  x554
    "BecameCameraUncentered"  x550
data.pieceId  (string, 2514/2514 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2514/2514 records)
    1639 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2260 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (730); Unit 3 Dev (399); Unit 4 Dev (337); Unit 4 Dev - Anderson Base (215); Unit 1 Dev (197); Unit 3 Dungeon Dev (121); Unit 4 Dev - Dungeon (110); Unit 5 Dev - Dungeon (101); Unit 5 Dev (50)
- **eventKey:** present on 1403 of 2260 records
- **Intervals:** median 4.32s (p5 0.00s / p95 29.93s, n=2259)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1403; [conversationId, dialogueEventType] x857
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2260/2260 records)
    numeric range 8 .. 116 (50 unique)
data.dialogueEventType  (string, 2260/2260 records)
    "DialogueNodeEvent"  x1403
    "DialogueStartEvent"  x434
    "DialogueFinishEvent"  x423
data.nodeId  (number, 1403/2260 records)
    numeric range 0 .. 290 (229 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1944 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (691); Unit 4 Dev (253); Unit 3 Dev (245); Unit 4 Dev - Dungeon (174); Unit 1 Dev (168); Unit 5 Dev - Dungeon (151); Unit 4 Dev - Anderson Base (126); Unit 3 Dungeon Dev (87); Unit 5 Dev (49)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=1928)
- **Fields under `data`:**

```text
data.position  (object, 1944/1944 records)
data.position.x  (number, 1944/1944 records)
    numeric range -678.692 .. 1555.33 (635 unique)
data.position.y  (number, 1944/1944 records)
    numeric range -114.326 .. 221.993 (418 unique)
data.position.z  (number, 1944/1944 records)
    numeric range -1029.81 .. 1807.62 (635 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 465 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (263); Unit 3 Dev (103); Unit 2 Prod (Refactor) (59); Unit 1 Dev (40)
- **Intervals:** median 0.51s (p5 0.04s / p95 11.37s, n=464)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 465/465 records)
    "argumentationNodeHoverEnd"  x191
    "argumentationNodeHoverStart"  x190
    "argumentationNodeAdd"  x50
    "argumentationNodeRemove"  x34
data.argumentationTitle  (string, 465/465 records)
    "Unit 4 - Flooding"  x263
    "Unit 3 - Pollution Upstream"  x103
    "Unit 2 – Watershed"  x59
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 465/465 records)
    "C"  x73
    "B"  x62
    "A"  x61
    "D"  x59
    "3"  x42
    "1"  x39
    "II"  x32
    "2"  x31
    "I"  x27
    "4"  x22
    "5"  x17
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 259 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (102); Unit 2 Prod (Refactor) (45); Unit 3 Dungeon Dev (30); Unit 4 Dev (28); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (12); Unit 3 Dev (11); Unit 1 Dev (10); Unit 5 Dev (3)
- **Intervals:** median 11.78s (p5 1.51s / p95 895.82s, n=258)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 259/259 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 259/259 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 88 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 4 Dev (13); Unit 1 Dev (12); Unit 3 Dev (12); Unit 5 Dev - Dungeon (12); Unit 4 Dev - Dungeon (10); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2); Unit 5 Dev (1)
- **eventKey:** present on 88 of 88 records
- **Intervals:** median 194.27s (p5 0.01s / p95 74660.89s, n=87)
- **`data` key-set variants:** [questEventType, questID, questName] x55; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 88/88 records)
    "questActiveEvent"  x55
    "questFinishEvent"  x33
data.questID  (string, 88/88 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 88/88 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/88 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 75 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (75)
- **Intervals:** median 7.38s (p5 1.24s / p95 48.93s, n=74)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 75/75 records)
    "On"  x46
    "Off"  x29
data.floor  (string, 75/75 records)
    "4"  x50
    "3"  x19
    "1"  x3
    "2"  x3
data.machineNumber  (string, 75/75 records)
    "One"  x73
    "Two"  x2
data.machineType  (string, 75/75 records)
    "Condenser"  x36
    "Evaporator"  x26
    "DualChamber_Evaporator"  x5
    "DualChamber_Condenser"  x4
    "VentSwitch"  x4
data.room  (string, 75/75 records)
    "3"  x43
    "2"  x21
    "1"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 63 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (33); Unit 3 Dev (30)
- **Intervals:** median 4.24s (p5 0.75s / p95 6366.90s, n=62)
- **`data` key-set variants:** [actionType, featureUsed] x30; [actionType, featureUsed, location] x24; [actionType, featureUsed, legendName] x9
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 63/63 records)
    "WaypointMoveEvent"  x19
    "MapCloseEvent"  x15
    "MapOpenEvent"  x15
    "Selected"  x7
    "WaypointSetEvent"  x5
    "Unselected"  x2
data.featureUsed  (string, 63/63 records)
    "Map"  x30
    "Waypoint"  x24
    "Legend"  x9
data.legendName  (string, 9/63 records)
    "0 ft"  x3
    "90 ft"  x3
    "240 ft"  x1
    "270 ft"  x1
    "300 ft"  x1
data.location  (object, 24/63 records)
data.location.x  (number, 24/63 records)
    numeric range -329.253 .. 649.259 (20 unique)
data.location.y  (number, 24/63 records)
    numeric range -166.327 .. 242.792 (23 unique)
data.location.z  (number, 24/63 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 60 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev (22); Unit 3 Dev (12)
- **Intervals:** median 2.62s (p5 0.33s / p95 13458.92s, n=59)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x48; [Soil Key Puzzle Status, Unit] x12
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/60 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/60 records)
    "Unit 4 Dev"  x6
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 48/60 records)
    "RightDrag"  x29
    "LeftDrag"  x19
data.currentSoilType  (string, 48/60 records)
    "SAND"  x13
    "CLAY"  x10
    "CLAYSAND"  x9
    "SANDGRAVEL"  x8
    "CLAYROCK"  x7
    "BEDROCK"  x1
data.isCorrectSelection  (string, 48/60 records)
    "false"  x32
    "true"  x16
data.waterLevelStatus  (string, 48/60 records)
    "TooHigh"  x21
    "Proper"  x14
    "TooLow"  x13
data.waterRetentionChange  (string, 48/60 records)
    "Increase"  x18
    "NoChange"  x16
    "Decrease"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 58 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (26); Unit 2 Prod (Refactor) (10); Unit 4 Dev (8); Unit 3 Dev (6); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 74.22s (p5 6.69s / p95 102278.86s, n=57)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 58/58 records)
    "DebugMenuStateChanged"  x58
data.isOpened  (bool, 58/58 records)
    false  x58
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 52 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (28); Unit 3 Dev (16); Unit 2 Prod (Refactor) (6); Unit 1 Dev (2)
- **Intervals:** median 12.47s (p5 1.06s / p95 1380.73s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "submitAnswerEvent"  x52
data.answerSubmitted  (string, 52/52 records)
    24 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 52/52 records)
    "Unit 4 - Flooding"  x28
    "Unit 3 - Pollution Upstream"  x16
    "Unit 2 – Watershed"  x6
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 30 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (25); Unit 4 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1777.60s (p5 42.64s / p95 218102.21s, n=29)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 30/30 records)
    true  x30
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 25 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (25)
- **Intervals:** median 4138.74s (p5 75.75s / p95 237534.96s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 4 Dev (5); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 5172.80s (p5 25.29s / p95 233701.69s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (10); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.99s (p5 1.50s / p95 47635.36s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 112.56s (p5 0.05s / p95 424904.31s, n=11)
- **Open findings:** 1 — see sections 5-8
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

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 3.05s (p5 0.73s / p95 131.73s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Clay"  x4
    "Sand"  x4
    "Gravel"  x2
    "Bedrock"  x1
data.floor  (string, 11/11 records)
    "5"  x11
data.machine  (string, 11/11 records)
    "2"  x6
    "1"  x5
data.row  (string, 11/11 records)
    "TopRow"  x7
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 21.27s (p5 1.89s / p95 5097.22s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records, 4 empty-string)
    "cameraPlaced"  x6
    ""  x4
data.boxId  (string, 10/10 records)
    "0"  x5
    "1"  x3
    "2"  x2
data.soilType  (string, 10/10 records)
    "Clay"  x4
    "Gravel"  x2
    "None"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4); Unit 1 Dev (3)
- **Intervals:** median 65.26s (p5 2.70s / p95 517974.04s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolOpen"  x6
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 163531.71s (p5 26181.37s / p95 635527.45s, n=3)
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

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 878.34s (p5 669.72s / p95 223569.92s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x1
    "unit3"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (26 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "Selected" (7x); "Unselected" (2x); "WaypointMoveEvent" (19x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (9x); "Waypoint" (24x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (34x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*