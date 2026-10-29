# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b73

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b73
- **Game version string(s) in log:** 2.8.9, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b73.jsonl
- **Records:** 15198 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b73
- **Time span:** 2026-10-06T18:36:59.081000+00:00 .. 2026-10-16T21:51:26.527000+00:00 (243h 14m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b73\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 15198 records, 10 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 104 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4443 | 29.23 | 1 | 9 | 0 | 2026-10-06T18:37:12.937000+00:00 | 2026-10-16T21:47:29.534000+00:00 | 243h 10m |
| PuzzlePieceVisibleEvent | 4439 | 29.21 | 1 | 4 | 0 | 2026-10-06T19:13:30.005000+00:00 | 2026-10-16T18:38:31.624000+00:00 | 239h 25m |
| PlayerPositionEvent | 2705 | 17.8 | 1 | 9 | 0 | 2026-10-06T18:37:09.445000+00:00 | 2026-10-16T21:51:26.527000+00:00 | 243h 14m |
| DialogueEvent | 2350 | 15.46 | 1 | 9 | 1461 | 2026-10-06T18:37:29.489000+00:00 | 2026-10-16T21:49:40.476000+00:00 | 243h 12m |
| argumentationNodeEvent | 447 | 2.94 | 1 | 5 | 0 | 2026-10-06T19:01:50.535000+00:00 | 2026-10-16T21:31:24.986000+00:00 | 242h 29m |
| ObjectInterEvent | 257 | 1.69 | 1 | 9 | 0 | 2026-10-06T18:43:34.362000+00:00 | 2026-10-16T21:47:20.283000+00:00 | 243h 3m |
| Soil Key Puzzle | 98 | 0.64 | 1 | 3 | 0 | 2026-10-14T12:43:26.139000+00:00 | 2026-10-15T22:50:19.077000+00:00 | 34h 6m |
| questEvent | 87 | 0.57 | 1 | 9 | 87 | 2026-10-06T18:37:29.463000+00:00 | 2026-10-16T21:49:25.591000+00:00 | 243h 11m |
| gameWindowFocusEvent | 65 | 0.43 | 1 | 8 | 0 | 2026-10-06T18:36:59.081000+00:00 | 2026-10-16T21:44:40.418000+00:00 | 243h 7m |
| gameWindowUnfocusEvent | 53 | 0.35 | 1 | 8 | 0 | 2026-10-06T19:17:39.172000+00:00 | 2026-10-16T21:22:21.550000+00:00 | 242h 4m |
| TopographicMapEvent | 47 | 0.31 | 1 | 2 | 0 | 2026-10-06T19:14:30.034000+00:00 | 2026-10-15T22:06:34.536000+00:00 | 218h 52m |
| argumentationAnswerEvent | 43 | 0.28 | 1 | 5 | 0 | 2026-10-06T19:03:15.096000+00:00 | 2026-10-16T21:31:26.084000+00:00 | 242h 28m |
| DEBUGMenu | 38 | 0.25 | 1 | 9 | 0 | 2026-10-06T18:37:09.422000+00:00 | 2026-10-16T21:44:40.086000+00:00 | 243h 7m |
| WaterChamberEvent | 35 | 0.23 | 1 | 1 | 0 | 2026-10-16T18:38:47.066000+00:00 | 2026-10-16T18:55:20.895000+00:00 | 16m 33s |
| gameStartEvent | 19 | 0.13 | 1 | 1 | 0 | 2026-10-06T18:36:59.082000+00:00 | 2026-10-16T21:44:40.418000+00:00 | 243h 7m |
| argumentationEvent | 14 | 0.09 | 1 | 5 | 0 | 2026-10-06T19:02:53.568000+00:00 | 2026-10-16T21:31:26.134000+00:00 | 242h 28m |
| SolarStillDesignEvent | 12 | 0.08 | 1 | 1 | 0 | 2026-10-16T21:37:34.752000+00:00 | 2026-10-16T21:47:04.697000+00:00 | 9m 29s |
| TerasGardenBox | 11 | 0.07 | 1 | 1 | 0 | 2026-10-16T01:00:54.562000+00:00 | 2026-10-16T01:02:07.302000+00:00 | 1m 12s |
| argumentationToolEvent | 11 | 0.07 | 1 | 3 | 0 | 2026-10-06T19:02:50.745000+00:00 | 2026-10-15T21:19:08.981000+00:00 | 218h 16m |
| soilMachine | 10 | 0.07 | 1 | 1 | 0 | 2026-10-15T23:11:41.852000+00:00 | 2026-10-15T23:33:03.076000+00:00 | 21m 21s |
| DaniEvent | 5 | 0.03 | 1 | 1 | 0 | 2026-10-08T19:17:59.095000+00:00 | 2026-10-15T12:33:07.741000+00:00 | 161h 15m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-06T19:07:43.650000+00:00 | 2026-10-16T01:12:54.911000+00:00 | 222h 5m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-16T18:32:53.282000+00:00 | 2026-10-16T21:44:49.127000+00:00 | 3h 11m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 12394.132s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.456s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 18.003s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.073s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.485s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.282s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.223s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 5.718s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 194.596s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.88s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8155.611s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 214.463s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 223.645s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 30.389s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 38 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 12 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 8.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,C,2,II; A,D,2,II; A,D,B,2,II; B,1,I; B,2,I; B,2,II; B,3,I; B,4,I; B,5,I; B,5,II; B,A,2,1,I; C,D,3,4,II; C,D,3,II; D,2,II; D,4,II; D,B,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 447 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[145] _id=6ac541e0de269131f9b6d6f5 ts=2026-10-06T18:45:51.1180000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[195] _id=6ac542cbde269131f9b6f6f9 ts=2026-10-06T18:49:45.9940000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[230] _id=6ac5432ede269131f9b7010f ts=2026-10-06T18:51:25.3940000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[6] _id=6ac53fccde269131f9b69901 ts=2026-10-06T18:36:59.0820000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[538] _id=6ac54767de269131f9b7651f ts=2026-10-06T19:09:25.8340000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[1162] _id=6ac6941ade269131f9be1fed ts=2026-10-07T18:48:57.7890000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 65 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 65} 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[5] _id=6ac53fccde269131f9b698fd ts=2026-10-06T18:36:59.0810000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[539] _id=6ac54766de269131f9b76517 ts=2026-10-06T19:09:25.8330000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[1161] _id=6ac6941ade269131f9be1fec ts=2026-10-07T18:48:57.7890000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 53 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 53} 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[1159] _id=6ac6941ade269131f9be1fe9 ts=2026-10-06T19:17:39.172Z`; `6ab9a9279a8420a1e6b56b73.jsonl[2632] _id=6ac699c6de269131f9bf0b1f ts=2026-10-07T19:13:09.8000000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[2717] _id=6ac7e648de269131f9c59f9a ts=2026-10-07T19:17:19.727Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 6 of 47 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[714] _id=6ac54897de269131f9b7804e ts=2026-10-06T19:14:30.0340000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[728] _id=6ac548bcde269131f9b7869f ts=2026-10-06T19:15:07.1090000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[1233] _id=6ac694ddde269131f9be4399 ts=2026-10-07T18:52:12.6890000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4442 | 0.0 | 1.456 | 197.077 | 16.315 | 431729.973 | 0.3 | 156 | 14 |
| PuzzlePieceVisibleEvent | 4438 | 0.0 | 0.073 | 194.209 | 1.981 | 495471.747 | 0.31 | 1874 | 13 |
| PlayerPositionEvent | 2693 | 9.704 | 10.002 | 301.89 | 10.258 | 431724.802 | 0.2 | 0 | 10 |
| DialogueEvent | 2349 | 0.0 | 4.022 | 372.725 | 39.846 | 494730.697 | 0.16 | 703 | 12 |
| argumentationNodeEvent | 446 | 0.005 | 0.504 | 1957.342 | 9.074 | 777873.555 | 0.03 | 72 | 4 |
| ObjectInterEvent | 256 | 0.0 | 18.003 | 3418.07 | 679.053 | 582144.154 | 0.02 | 3 | 15 |
| Soil Key Puzzle | 97 | 0.001 | 2.485 | 1266.113 | 29.176 | 95168.974 | 0.05 | 4 | 3 |
| questEvent | 86 | 0.0 | 227.498 | 10180.42 | 62435.86 | 433222.479 | 0.01 | 15 | 24 |
| gameWindowFocusEvent | 64 | 2.656 | 214.463 | 13675.958 | 64281.869 | 431924.345 | 0.0 | 0 | 23 |
| gameWindowUnfocusEvent | 52 | 1.248 | 223.645 | 16759.276 | 73991.273 | 495226.413 | 0.0 | 0 | 14 |
| TopographicMapEvent | 46 | 0.019 | 4.223 | 17128.794 | 69132.592 | 582087.812 | 0.0 | 2 | 7 |
| argumentationAnswerEvent | 42 | 1.32 | 5.718 | 20783.119 | 12366.53 | 777947.064 | 0.0 | 0 | 4 |
| DEBUGMenu | 37 | 7.699 | 1342.008 | 23655.423 | 85440.827 | 433203.853 | 0.0 | 0 | 22 |
| WaterChamberEvent | 34 | 2.582 | 20.311 | 29.23 | 99.546 | 134.223 | 2.05 | 0 | 0 |
| gameStartEvent | 18 | 69.507 | 8155.611 | 48625.63 | 138579.472 | 433276.866 | 0.0 | 0 | 16 |
| argumentationEvent | 13 | 0.03 | 194.596 | 67147.12 | 355508.2 | 777845.144 | 0.0 | 2 | 4 |
| SolarStillDesignEvent | 11 | 1.538 | 3.443 | 51.813 | 265.706 | 518.147 | 1.16 | 0 | 0 |
| TerasGardenBox | 10 | 1.017 | 1.282 | 7.274 | 26.171 | 28.713 | 8.25 | 0 | 0 |
| argumentationToolEvent | 10 | 0.608 | 2.88 | 78577.824 | 431378.13 | 777947.325 | 0.0 | 0 | 2 |
| soilMachine | 9 | 2.548 | 30.389 | 142.358 | 538.455 | 773.948 | 0.42 | 0 | 1 |
| DaniEvent | 4 | 3.157 | 31744.658 | 145127.161 | 448983.965 | 517016.174 | 0.0 | 0 | 2 |
| EndOfUnit | 3 | 9073.454 | 12394.132 | 266503.754 | 701478.721 | 778043.675 | 0.0 | 0 | 3 |
| chatEvent | 3 | 1352.559 | 1410.785 | 3838.615 | 8018.329 | 8752.501 | 0.02 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 19 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[3264] _id=6acf7736de269131f9d2ce4e ts=2026-10-14T12:36:04.0720000Z == 6ab9a9279a8420a1e6b56b73.jsonl[3265] _id=6acf7736de269131f9d2ce4f ts=2026-10-14T12:36:04.0720000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[3267] _id=6acf7736de269131f9d2ce51 ts=2026-10-14T12:36:04.0730000Z == 6ab9a9279a8420a1e6b56b73.jsonl[3268] _id=6acf7736de269131f9d2ce52 ts=2026-10-14T12:36:04.0730000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[3272] _id=6acf7736de269131f9d2ce56 ts=2026-10-14T12:36:04.0740000Z == 6ab9a9279a8420a1e6b56b73.jsonl[3273] _id=6acf7736de269131f9d2ce57 ts=2026-10-14T12:36:04.0740000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 113 group(s), 155 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[666] _id=6ac54868de269131f9b77af7 ts=2026-10-06T19:13:42.2670000Z == 6ab9a9279a8420a1e6b56b73.jsonl[652] _id=6ac54869de269131f9b77b0c ts=2026-10-06T19:13:42.2670000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[677] _id=6ac5486ade269131f9b77b65 ts=2026-10-06T19:13:43.0530000Z == 6ab9a9279a8420a1e6b56b73.jsonl[676] _id=6ac5486ade269131f9b77b69 ts=2026-10-06T19:13:43.0530000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[758] _id=6ac5490bde269131f9b79271 ts=2026-10-06T19:13:58.0100000Z == 6ab9a9279a8420a1e6b56b73.jsonl[762] _id=6ac5490bde269131f9b79273 ts=2026-10-06T19:13:58.0100000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[14836] _id=6ad297fbde269131f9e833bc ts=2026-10-16T21:32:42.7670000Z == 6ab9a9279a8420a1e6b56b73.jsonl[14837] _id=6ad297fbde269131f9e833bd ts=2026-10-16T21:32:42.7670000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6ab9a9279a8420a1e6b56b73.jsonl[106] _id=6ac54157de269131f9b6c783 ts=2026-10-06T18:43:34.3620000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[100] _id=6ac54157de269131f9b6c785 ts=2026-10-06T18:43:34.3700000Z`; `756ms: 6ab9a9279a8420a1e6b56b73.jsonl[603] _id=6ac54824de269131f9b77281 ts=2026-10-06T19:12:35.5760000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[595] _id=6ac54825de269131f9b7729b ts=2026-10-06T19:12:36.3320000Z`; `779ms: 6ab9a9279a8420a1e6b56b73.jsonl[605] _id=6ac54826de269131f9b772c5 ts=2026-10-06T19:12:37.5910000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[599] _id=6ac54827de269131f9b772eb ts=2026-10-06T19:12:38.3700000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 75 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `90ms: 6ab9a9279a8420a1e6b56b73.jsonl[641] _id=6ac5485bde269131f9b779d3 ts=2026-10-06T19:13:30.0050000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[646] _id=6ac5485bde269131f9b779d9 ts=2026-10-06T19:13:30.0950000Z`; `145ms: 6ab9a9279a8420a1e6b56b73.jsonl[658] _id=6ac54869de269131f9b77b17 ts=2026-10-06T19:13:42.5070000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[670] _id=6ac54869de269131f9b77b1d ts=2026-10-06T19:13:42.6520000Z`; `8ms: 6ab9a9279a8420a1e6b56b73.jsonl[674] _id=6ac5486ade269131f9b77b39 ts=2026-10-06T19:13:42.7430000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[671] _id=6ac5486ade269131f9b77b41 ts=2026-10-06T19:13:42.7510000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `40ms: 6ab9a9279a8420a1e6b56b73.jsonl[8596] _id=6ad143f2de269131f9e17a8b ts=2026-10-15T21:21:54.2290000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[8599] _id=6ad143f2de269131f9e17a8e ts=2026-10-15T21:21:54.2690000Z`; `30ms: 6ab9a9279a8420a1e6b56b73.jsonl[13177] _id=6ad175eede269131f9e25255 ts=2026-10-16T00:55:09.0780000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[13180] _id=6ad175eede269131f9e25258 ts=2026-10-16T00:55:09.1080000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `38ms: 6ab9a9279a8420a1e6b56b73.jsonl[376] _id=6ac545e8de269131f9b732f9 ts=2026-10-06T19:03:03.3170000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[377] _id=6ac545e8de269131f9b73303 ts=2026-10-06T19:03:03.3550000Z`; `41ms: 6ab9a9279a8420a1e6b56b73.jsonl[389] _id=6ac545eede269131f9b73397 ts=2026-10-06T19:03:09.4180000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[390] _id=6ac545eede269131f9b7339c ts=2026-10-06T19:03:09.4590000Z`; `75ms: 6ab9a9279a8420a1e6b56b73.jsonl[413] _id=6ac54621de269131f9b738f9 ts=2026-10-06T19:04:00.6300000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[414] _id=6ac54622de269131f9b73901 ts=2026-10-06T19:04:00.7050000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `937ms: 6ab9a9279a8420a1e6b56b73.jsonl[7418] _id=6ad124bbde269131f9dffb88 ts=2026-10-15T19:08:42.6450000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[7419] _id=6ad124bbde269131f9dffbb1 ts=2026-10-15T19:08:43.5820000Z`; `608ms: 6ab9a9279a8420a1e6b56b73.jsonl[8420] _id=6ad1434cde269131f9e175fd ts=2026-10-15T21:19:08.3730000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[8426] _id=6ad1434dde269131f9e175ff ts=2026-10-15T21:19:08.9810000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6ab9a9279a8420a1e6b56b73.jsonl[14986] _id=6ad2997bde269131f9e836cf ts=2026-10-16T21:39:06.8620000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[14979] _id=6ad2997bde269131f9e836d1 ts=2026-10-16T21:39:06.8700000Z`; `5ms: 6ab9a9279a8420a1e6b56b73.jsonl[15052] _id=6ad29ad8de269131f9e83892 ts=2026-10-16T21:44:54.5690000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[15053] _id=6ad29ad8de269131f9e83893 ts=2026-10-16T21:44:54.5740000Z`; `5ms: 6ab9a9279a8420a1e6b56b73.jsonl[15170] _id=6ad29b9ede269131f9e83962 ts=2026-10-16T21:48:14.3130000Z ~ 6ab9a9279a8420a1e6b56b73.jsonl[15171] _id=6ad29b9ede269131f9e83964 ts=2026-10-16T21:48:14.3180000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 120h 20m 
  - Evidence: 120h 20m: 6ab9a9279a8420a1e6b56b73.jsonl[2721] _id=6ac7e690de269131f9c5a819 ts=2026-10-08T18:53:04.5070000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3147] _id=6ace82c5de269131f9d19a30 ts=2026-10-13T19:13:08.3600000Z; 24h 2m: 6ab9a9279a8420a1e6b56b73.jsonl[1164] _id=6ac69424de269131f9be21f2 ts=2026-10-07T18:49:08.5910000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2714] _id=6ac7e648de269131f9c59fa2 ts=2026-10-08T18:51:51.6980000Z; 23h 39m: 6ab9a9279a8420a1e6b56b73.jsonl[542] _id=6ac54772de269131f9b76631 ts=2026-10-06T19:09:37.3820000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1160] _id=6ac6941ade269131f9be1feb ts=2026-10-07T18:48:57.6390000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 36m 
  - Evidence: 143h 36m: 6ab9a9279a8420a1e6b56b73.jsonl[3144] _id=6ac7ec67de269131f9c68881 ts=2026-10-08T19:17:59.0950000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[4865] _id=6acfcfffde269131f9d7b6bb ts=2026-10-14T18:54:55.2690000Z; 17h 37m: 6ab9a9279a8420a1e6b56b73.jsonl[4775] _id=6acfd003de269131f9d7b735 ts=2026-10-14T18:54:58.4260000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[6126] _id=6ad0c85ede269131f9da4b28 ts=2026-10-15T12:32:46.542Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 137h 25m 
  - Evidence: 137h 25m: 6ab9a9279a8420a1e6b56b73.jsonl[3138] _id=6ac7ec3cde269131f9c684a0 ts=2026-10-08T19:17:15.8650000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3396] _id=6acfcb6fde269131f9d723c7 ts=2026-10-14T12:42:46.562Z; 23h 37m: 6ab9a9279a8420a1e6b56b73.jsonl[2710] _id=6ac69ab9de269131f9bf207e ts=2026-10-07T19:17:13.4610000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2749] _id=6ac7e702de269131f9c5b5af ts=2026-10-08T18:54:58.4760000Z; 23h 33m: 6ab9a9279a8420a1e6b56b73.jsonl[944] _id=6ac5491bde269131f9b79557 ts=2026-10-06T19:16:42.0240000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1172] _id=6ac6944ade269131f9be2822 ts=2026-10-07T18:49:46.1430000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 703 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[13104] _id=6ad17595de269131f9e2505b ts=2026-10-16T00:53:41.0660000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[13105] _id=6ad17595de269131f9e2505c ts=2026-10-16T00:53:41.0660000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[13127] _id=6ad175b9de269131f9e250d5 ts=2026-10-16T00:54:16.7540000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[13128] _id=6ad175b9de269131f9e250d6 ts=2026-10-16T00:54:16.7540000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[13166] _id=6ad175e5de269131f9e25201 ts=2026-10-16T00:55:00.6660000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[13167] _id=6ad175e5de269131f9e25202 ts=2026-10-16T00:55:00.6660000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 216h 7m 
  - Evidence: 216h 7m: 6ab9a9279a8420a1e6b56b73.jsonl[536] _id=6ac54700de269131f9b75c49 ts=2026-10-06T19:07:43.6500000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[7533] _id=6ad1263bde269131f9e03454 ts=2026-10-15T19:15:07.3250000Z; 3h 26m: 6ab9a9279a8420a1e6b56b73.jsonl[7533] _id=6ad1263bde269131f9e03454 ts=2026-10-15T19:15:07.3250000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[10248] _id=6ad156a5de269131f9e1daf9 ts=2026-10-15T22:41:41.4570000Z; 2h 31m: 6ab9a9279a8420a1e6b56b73.jsonl[10248] _id=6ad156a5de269131f9e1daf9 ts=2026-10-15T22:41:41.4570000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[13526] _id=6ad17a17de269131f9e26bdc ts=2026-10-16T01:12:54.9110000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6ab9a9279a8420a1e6b56b73.jsonl[3145] _id=6ac7ec67de269131f9c68882 ts=2026-10-08T19:17:59.0970000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3153] _id=6ace82dade269131f9d19e88 ts=2026-10-13T19:13:29.0700000Z; 23h 35m: 6ab9a9279a8420a1e6b56b73.jsonl[2712] _id=6ac69abdde269131f9bf20a8 ts=2026-10-07T19:17:17.4910000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2718] _id=6ac7e69ade269131f9c5a90d ts=2026-10-08T18:53:13.8900000Z; 23h 31m: 6ab9a9279a8420a1e6b56b73.jsonl[1148] _id=6ac54950de269131f9b79c4d ts=2026-10-06T19:17:35.4860000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1166] _id=6ac69428de269131f9be227d ts=2026-10-07T18:49:11.2270000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 156 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[15046] _id=6ad29ad8de269131f9e8388c ts=2026-10-16T21:44:53.6370000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[15047] _id=6ad29ad8de269131f9e8388d ts=2026-10-16T21:44:53.6370000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[15047] _id=6ad29ad8de269131f9e8388d ts=2026-10-16T21:44:53.6370000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[15048] _id=6ad29ad8de269131f9e8388e ts=2026-10-16T21:44:53.6370000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[15048] _id=6ad29ad8de269131f9e8388e ts=2026-10-16T21:44:53.6370000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[15049] _id=6ad29ad8de269131f9e8388f ts=2026-10-16T21:44:53.6370000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 161h 42m 
  - Evidence: 161h 42m: 6ab9a9279a8420a1e6b56b73.jsonl[2409] _id=6ac696eede269131f9bebbde ts=2026-10-07T19:01:01.9860000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3429] _id=6acfcb6fde269131f9d723dc ts=2026-10-14T12:43:26.14Z; 23h 48m: 6ab9a9279a8420a1e6b56b73.jsonl[5813] _id=6acfd32dde269131f9d82018 ts=2026-10-14T19:08:28.6310000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[7053] _id=6ad12208de269131f9df9192 ts=2026-10-15T18:57:12.3490000Z; 23h 33m: 6ab9a9279a8420a1e6b56b73.jsonl[970] _id=6ac54922de269131f9b795ff ts=2026-10-06T19:16:49.0650000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1194] _id=6ac69472de269131f9be2f60 ts=2026-10-07T18:50:26.3240000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.008s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[12825] _id=6ad173f3de269131f9e249ca ts=2026-10-16T00:46:43.4020000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[12826] _id=6ad173f3de269131f9e249cb ts=2026-10-16T00:46:43.4020000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[12908] _id=6ad1745ede269131f9e24bf2 ts=2026-10-16T00:48:29.5570000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[12909] _id=6ad1745ede269131f9e24bf3 ts=2026-10-16T00:48:29.5570000Z; 8ms: 6ab9a9279a8420a1e6b56b73.jsonl[106] _id=6ac54157de269131f9b6c783 ts=2026-10-06T18:43:34.3620000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[100] _id=6ac54157de269131f9b6c785 ts=2026-10-06T18:43:34.3700000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6ab9a9279a8420a1e6b56b73.jsonl[3143] _id=6ac7ec67de269131f9c68877 ts=2026-10-08T19:17:58.9910000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3152] _id=6ace82dade269131f9d19e87 ts=2026-10-13T19:13:23.7930000Z; 23h 35m: 6ab9a9279a8420a1e6b56b73.jsonl[2711] _id=6ac69abade269131f9bf208c ts=2026-10-07T19:17:14.3900000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2719] _id=6ac7e693de269131f9c5a847 ts=2026-10-08T18:53:04.5250000Z; 23h 31m: 6ab9a9279a8420a1e6b56b73.jsonl[1131] _id=6ac5494bde269131f9b79c05 ts=2026-10-06T19:17:30.6340000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1165] _id=6ac69428de269131f9be227c ts=2026-10-07T18:49:08.6090000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 137h 37m 
  - Evidence: 137h 37m: 6ab9a9279a8420a1e6b56b73.jsonl[2980] _id=6ac7e9fade269131f9c63917 ts=2026-10-08T19:07:37.7160000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3463] _id=6acfcb6fde269131f9d7240d ts=2026-10-14T12:45:29.463Z; 24h 6m: 6ab9a9279a8420a1e6b56b73.jsonl[2401] _id=6ac696cfde269131f9beb7ed ts=2026-10-07T19:00:29.3190000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2970] _id=6ac7e9f1de269131f9c6375c ts=2026-10-08T19:07:28.2850000Z; 23h 33m: 6ab9a9279a8420a1e6b56b73.jsonl[1147] _id=6ac54952de269131f9b79c71 ts=2026-10-06T19:17:35.6220000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1248] _id=6ac6954bde269131f9be5e44 ts=2026-10-07T18:50:54.5010000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1874 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[1016] _id=6ac54934de269131f9b798ab ts=2026-10-06T19:17:07.4290000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1020] _id=6ac54935de269131f9b798af ts=2026-10-06T19:17:07.4290000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[1022] _id=6ac54939de269131f9b79969 ts=2026-10-06T19:17:11.5320000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1036] _id=6ac5493ade269131f9b79973 ts=2026-10-06T19:17:11.5320000Z; 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[10310] _id=6ad158b1de269131f9e1df59 ts=2026-10-15T22:50:23.7190000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[10311] _id=6ad158b1de269131f9e1df5a ts=2026-10-15T22:50:23.7190000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 26h 26m 
  - Evidence: 26h 26m: 6ab9a9279a8420a1e6b56b73.jsonl[5080] _id=6acfd1ecde269131f9d7f1ad ts=2026-10-14T19:03:07.6810000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[8858] _id=6ad145acde269131f9e18225 ts=2026-10-15T21:29:16.6550000Z; 6h 12m: 6ab9a9279a8420a1e6b56b73.jsonl[3447] _id=6acfcb6fde269131f9d723ee ts=2026-10-14T12:44:42.798Z -> 6ab9a9279a8420a1e6b56b73.jsonl[4967] _id=6acfd088de269131f9d7c5ac ts=2026-10-14T18:57:11.6160000Z; 1h 19m: 6ab9a9279a8420a1e6b56b73.jsonl[8897] _id=6ad145d7de269131f9e182e9 ts=2026-10-15T21:29:59.3630000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[10323] _id=6ad15887de269131f9e1dedb ts=2026-10-15T22:49:43.2610000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b73.jsonl[5064] _id=6acfd196de269131f9d7e509 ts=2026-10-14T19:01:41.7500000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[5065] _id=6acfd196de269131f9d7e50a ts=2026-10-14T19:01:41.7510000Z; 5ms: 6ab9a9279a8420a1e6b56b73.jsonl[5063] _id=6acfd196de269131f9d7e4f9 ts=2026-10-14T19:01:41.4160000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[5059] _id=6acfd196de269131f9d7e501 ts=2026-10-14T19:01:41.4210000Z; 6ms: 6ab9a9279a8420a1e6b56b73.jsonl[5057] _id=6acfd194de269131f9d7e4c4 ts=2026-10-14T19:01:39.9570000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[5054] _id=6acfd194de269131f9d7e4ce ts=2026-10-14T19:01:39.9630000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 161h 41m 
  - Evidence: 161h 41m: 6ab9a9279a8420a1e6b56b73.jsonl[2913] _id=6ac7e973de269131f9c61e56 ts=2026-10-08T19:05:23.4510000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[6433] _id=6ad11d23de269131f9def724 ts=2026-10-15T12:46:51.263Z; 23h 45m: 6ab9a9279a8420a1e6b56b73.jsonl[2640] _id=6ac699dcde269131f9bf0c7d ts=2026-10-07T19:13:32.5270000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2826] _id=6ac7e7ebde269131f9c5dcc7 ts=2026-10-08T18:58:51.5370000Z; 23h 37m: 6ab9a9279a8420a1e6b56b73.jsonl[728] _id=6ac548bcde269131f9b7869f ts=2026-10-06T19:15:07.1090000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1233] _id=6ac694ddde269131f9be4399 ts=2026-10-07T18:52:12.6890000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.047s shown 
  - Evidence: 19ms: 6ab9a9279a8420a1e6b56b73.jsonl[2588] _id=6ac69929de269131f9befe43 ts=2026-10-07T19:10:32.6630000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2589] _id=6ac69929de269131f9befe44 ts=2026-10-07T19:10:32.6820000Z; 47ms: 6ab9a9279a8420a1e6b56b73.jsonl[2589] _id=6ac69929de269131f9befe44 ts=2026-10-07T19:10:32.6820000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2593] _id=6ac69929de269131f9befe48 ts=2026-10-07T19:10:32.7290000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 216h 5m 
  - Evidence: 216h 5m: 6ab9a9279a8420a1e6b56b73.jsonl[446] _id=6ac5463dde269131f9b73d4f ts=2026-10-06T19:04:28.1460000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[7450] _id=6ad12517de269131f9e00960 ts=2026-10-15T19:10:15.2100000Z; 20h 34m: 6ab9a9279a8420a1e6b56b73.jsonl[13156] _id=6ad175edde269131f9e25253 ts=2026-10-16T00:55:09.0590000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14728] _id=6ad29753de269131f9e83177 ts=2026-10-16T21:29:54.4820000Z; 3h 30m: 6ab9a9279a8420a1e6b56b73.jsonl[8595] _id=6ad143f2de269131f9e17a89 ts=2026-10-15T21:21:54.1900000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[13010] _id=6ad17532de269131f9e24e87 ts=2026-10-16T00:52:02.1810000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 216h 4m 
  - Evidence: 216h 4m: 6ab9a9279a8420a1e6b56b73.jsonl[449] _id=6ac5463dde269131f9b73d53 ts=2026-10-06T19:04:28.1740000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[7412] _id=6ad124b1de269131f9dff9ff ts=2026-10-15T19:08:33.3180000Z; 20h 32m: 6ab9a9279a8420a1e6b56b73.jsonl[13180] _id=6ad175eede269131f9e25258 ts=2026-10-16T00:55:09.1080000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14621] _id=6ad296cbde269131f9e83036 ts=2026-10-16T21:27:39.3450000Z; 3h 29m: 6ab9a9279a8420a1e6b56b73.jsonl[8599] _id=6ad143f2de269131f9e17a8e ts=2026-10-15T21:21:54.2690000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[12953] _id=6ad174f4de269131f9e24ddf ts=2026-10-16T00:50:59.6060000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.030s..0.040s shown 
  - Evidence: 30ms: 6ab9a9279a8420a1e6b56b73.jsonl[13177] _id=6ad175eede269131f9e25255 ts=2026-10-16T00:55:09.0780000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[13180] _id=6ad175eede269131f9e25258 ts=2026-10-16T00:55:09.1080000Z; 40ms: 6ab9a9279a8420a1e6b56b73.jsonl[8596] _id=6ad143f2de269131f9e17a8b ts=2026-10-15T21:21:54.2290000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[8599] _id=6ad143f2de269131f9e17a8e ts=2026-10-15T21:21:54.2690000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 216h 4m 
  - Evidence: 216h 4m: 6ab9a9279a8420a1e6b56b73.jsonl[441] _id=6ac54637de269131f9b73c65 ts=2026-10-06T19:04:22.0620000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[7358] _id=6ad124c8de269131f9dffdbc ts=2026-10-15T19:08:55.6170000Z; 20h 32m: 6ab9a9279a8420a1e6b56b73.jsonl[13173] _id=6ad175e9de269131f9e2522c ts=2026-10-16T00:55:04.8430000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14629] _id=6ad296cfde269131f9e8303f ts=2026-10-16T21:27:43.0830000Z; 3h 29m: 6ab9a9279a8420a1e6b56b73.jsonl[8592] _id=6ad143eede269131f9e17a6d ts=2026-10-15T21:21:50.4100000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[12979] _id=6ad174f6de269131f9e24de7 ts=2026-10-16T00:51:01.9020000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 72 interval(s) ≤ 0.005s..0.017s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b73.jsonl[412] _id=6ac54621de269131f9b738ed ts=2026-10-06T19:04:00.6250000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[413] _id=6ac54621de269131f9b738f9 ts=2026-10-06T19:04:00.6300000Z; 10ms: 6ab9a9279a8420a1e6b56b73.jsonl[14637] _id=6ad296e3de269131f9e83066 ts=2026-10-16T21:28:02.6470000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14648] _id=6ad296e3de269131f9e83068 ts=2026-10-16T21:28:02.6570000Z; 17ms: 6ab9a9279a8420a1e6b56b73.jsonl[14713] _id=6ad2974fde269131f9e83169 ts=2026-10-16T21:29:51.0620000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14714] _id=6ad2974fde269131f9e8316a ts=2026-10-16T21:29:51.0790000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 216h 5m 
  - Evidence: 216h 5m: 6ab9a9279a8420a1e6b56b73.jsonl[365] _id=6ac545dede269131f9b73209 ts=2026-10-06T19:02:53.5000000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[7415] _id=6ad124b9de269131f9dffb2c ts=2026-10-15T19:08:40.8250000Z; 2h 9m: 6ab9a9279a8420a1e6b56b73.jsonl[7423] _id=6ad124d4de269131f9e00004 ts=2026-10-15T19:09:08.4170000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[8418] _id=6ad14346de269131f9e175e4 ts=2026-10-15T21:19:01.9750000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 2h 25m 
  - Evidence: 2h 25m: 6ab9a9279a8420a1e6b56b73.jsonl[14467] _id=6ad27358de269131f9e77b55 ts=2026-10-16T18:56:24.0670000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14518] _id=6ad29589de269131f9e82e1a ts=2026-10-16T21:22:16.5680000Z; 23m 30s: 6ab9a9279a8420a1e6b56b73.jsonl[13538] _id=6ad26dd5de269131f9e704d9 ts=2026-10-16T18:32:53.2820000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14467] _id=6ad27358de269131f9e77b55 ts=2026-10-16T18:56:24.0670000Z; 22m 32s: 6ab9a9279a8420a1e6b56b73.jsonl[14518] _id=6ad29589de269131f9e82e1a ts=2026-10-16T21:22:16.5680000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[15043] _id=6ad29ad1de269131f9e83888 ts=2026-10-16T21:44:49.1270000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a9279a8420a1e6b56b73.jsonl[2716] _id=6ac7e648de269131f9c59fa4 ts=2026-10-08T18:51:51.8380000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3149] _id=6ace82c5de269131f9d19a32 ts=2026-10-13T19:13:08.7040000Z; 24h 2m: 6ab9a9279a8420a1e6b56b73.jsonl[1162] _id=6ac6941ade269131f9be1fed ts=2026-10-07T18:48:57.7890000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2716] _id=6ac7e648de269131f9c59fa4 ts=2026-10-08T18:51:51.8380000Z; 23h 39m: 6ab9a9279a8420a1e6b56b73.jsonl[538] _id=6ac54767de269131f9b7651f ts=2026-10-06T19:09:25.8340000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1162] _id=6ac6941ade269131f9be1fed ts=2026-10-07T18:48:57.7890000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a9279a8420a1e6b56b73.jsonl[3110] _id=6ac7eb91de269131f9c67069 ts=2026-10-08T19:14:24.3590000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3148] _id=6ace82c5de269131f9d19a31 ts=2026-10-13T19:13:08.7040000Z; 23h 39m: 6ab9a9279a8420a1e6b56b73.jsonl[539] _id=6ac54766de269131f9b76517 ts=2026-10-06T19:09:25.8330000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1161] _id=6ac6941ade269131f9be1fec ts=2026-10-07T18:48:57.7890000Z; 23h 38m: 6ab9a9279a8420a1e6b56b73.jsonl[2635] _id=6ac699c7de269131f9bf0b36 ts=2026-10-07T19:13:11.3120000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2715] _id=6ac7e648de269131f9c59fa3 ts=2026-10-08T18:51:51.8380000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 137h 33m 
  - Evidence: 137h 33m: 6ab9a9279a8420a1e6b56b73.jsonl[3146] _id=6ace82c5de269131f9d19a17 ts=2026-10-08T19:18:06.257Z -> 6ab9a9279a8420a1e6b56b73.jsonl[4051] _id=6acfcb70de269131f9d72712 ts=2026-10-14T12:51:52.67Z; 23h 57m: 6ab9a9279a8420a1e6b56b73.jsonl[2717] _id=6ac7e648de269131f9c59f9a ts=2026-10-07T19:17:19.727Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3109] _id=6ac7eb91de269131f9c67065 ts=2026-10-08T19:14:24.3450000Z; 23h 55m: 6ab9a9279a8420a1e6b56b73.jsonl[1159] _id=6ac6941ade269131f9be1fe9 ts=2026-10-06T19:17:39.172Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2632] _id=6ac699c6de269131f9bf0b1f ts=2026-10-07T19:13:09.8000000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 120h 20m 
  - Evidence: 120h 20m: 6ab9a9279a8420a1e6b56b73.jsonl[2720] _id=6ac7e693de269131f9c5a848 ts=2026-10-08T18:53:06.6480000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[3154] _id=6ace82dade269131f9d19e89 ts=2026-10-13T19:13:29.1270000Z; 23h 42m: 6ab9a9279a8420a1e6b56b73.jsonl[2579] _id=6ac69914de269131f9befcc0 ts=2026-10-07T19:10:12.0160000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[2720] _id=6ac7e693de269131f9c5a848 ts=2026-10-08T18:53:06.6480000Z; 23h 37m: 6ab9a9279a8420a1e6b56b73.jsonl[496] _id=6ac547d2de269131f9b76ca1 ts=2026-10-06T19:11:13.8410000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[1167] _id=6ac69428de269131f9be227e ts=2026-10-07T18:49:11.2630000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b73.jsonl[14836] _id=6ad297fbde269131f9e833bc ts=2026-10-16T21:32:42.7670000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[14837] _id=6ad297fbde269131f9e833bd ts=2026-10-16T21:32:42.7670000Z; 3ms: 6ab9a9279a8420a1e6b56b73.jsonl[347] _id=6ac54581de269131f9b72afb ts=2026-10-06T19:01:19.5520000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[349] _id=6ac54581de269131f9b72afd ts=2026-10-06T19:01:19.5550000Z; 5ms: 6ab9a9279a8420a1e6b56b73.jsonl[15052] _id=6ad29ad8de269131f9e83892 ts=2026-10-16T21:44:54.5690000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[15053] _id=6ad29ad8de269131f9e83893 ts=2026-10-16T21:44:54.5740000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 12m 53s 
  - Evidence: 12m 53s: 6ab9a9279a8420a1e6b56b73.jsonl[11758] _id=6ad15e8cde269131f9e1f674 ts=2026-10-15T23:15:24.1000000Z -> 6ab9a9279a8420a1e6b56b73.jsonl[12117] _id=6ad16192de269131f9e2048e ts=2026-10-15T23:28:18.0480000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 15 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[339] _id=6ac5456ade269131f9b7291b ts=2026-10-06T19:00:58.0090000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[455] _id=6ac54653de269131f9b74021 ts=2026-10-06T19:04:50.7160000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[2904] _id=6ac7e962de269131f9c61a0c ts=2026-10-08T19:05:05.7620000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[940] _id=6ac54919de269131f9b794e7 ts=2026-10-06T19:16:22.0420000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[875] _id=6ac5491ede269131f9b795ab ts=2026-10-06T19:16:44.5230000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[974] _id=6ac54926de269131f9b7967e ts=2026-10-06T19:16:51.9740000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 41 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[641] _id=6ac5485bde269131f9b779d3 ts=2026-10-06T19:13:30.0050000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[646] _id=6ac5485bde269131f9b779d9 ts=2026-10-06T19:13:30.0950000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[658] _id=6ac54869de269131f9b77b17 ts=2026-10-06T19:13:42.5070000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[8599] _id=6ad143f2de269131f9e17a8e ts=2026-10-15T21:21:54.2690000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[13180] _id=6ad175eede269131f9e25258 ts=2026-10-16T00:55:09.1080000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[377] _id=6ac545e8de269131f9b73303 ts=2026-10-06T19:03:03.3550000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[390] _id=6ac545eede269131f9b7339c ts=2026-10-06T19:03:09.4590000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[413] _id=6ac54621de269131f9b738f9 ts=2026-10-06T19:04:00.6300000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[13538] _id=6ad26dd5de269131f9e704d9 ts=2026-10-16T18:32:53.2820000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[14467] _id=6ad27358de269131f9e77b55 ts=2026-10-16T18:56:24.0670000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[14518] _id=6ad29589de269131f9e82e1a ts=2026-10-16T21:22:16.5680000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[7540] _id=6ad1265dde269131f9e038b0 ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[4865] _id=6acfcfffde269131f9d7b6bb ts=2026-10-14T18:54:55.2690000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[6126] _id=6ad0c85ede269131f9da4b28 ts=2026-10-15T12:32:46.542Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 191 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[1010] _id=6ac54931de269131f9b79827 ts=2026-10-06T19:17:03.4270000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[1008] _id=6ac54931de269131f9b79835 ts=2026-10-06T19:17:03.7520000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[1029] _id=6ac54937de269131f9b7991f ts=2026-10-06T19:17:09.6900000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 819 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[652] _id=6ac54869de269131f9b77b0c ts=2026-10-06T19:13:42.2670000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[684] _id=6ac54876de269131f9b77c87 ts=2026-10-06T19:13:56.5580000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[691] _id=6ac54877de269131f9b77cab ts=2026-10-06T19:13:57.9190000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[7418] _id=6ad124bbde269131f9dffb88 ts=2026-10-15T19:08:42.6450000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[7419] _id=6ad124bbde269131f9dffbb1 ts=2026-10-15T19:08:43.5820000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[7423] _id=6ad124d4de269131f9e00004 ts=2026-10-15T19:09:08.4170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 3 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 449 start, 440 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameCameraCentered' (totals: 957 open, 952 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 67 unmatched 'BecameVisible' (totals: 1278 open, 1252 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 9 unmatched 'argumentationToolOpen' (totals: 10 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 52 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 391 of 15196 adjacent _id pairs reverse in client time; worst 187.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b73.jsonl[1313] _id=6ac6954ade269131f9be5e18 ts=2026-10-07T18:54:02.0780000Z`; `6ab9a9279a8420a1e6b56b73.jsonl[1248] _id=6ac6954bde269131f9be5e44 ts=2026-10-07T18:50:54.5010000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.59s, min -431702.86s, max -0.19s over 15197 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b73\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4443 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1860); Unit 3 Dev (788); Unit 4 Dev - Dungeon (680); Unit 5 Dev - Dungeon (329); Unit 3 Dungeon Dev (310); Unit 4 Dev (179); Unit 4 Dev - Anderson Base (116); Unit 5 Dev (94); Unit 1 Dev (87)
- **Intervals:** median 1.46s (p5 0.08s / p95 16.31s, n=4442)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4443/4443 records)
    "pressed"  x4443
data.actionType  (string, 4443/4443 records)
    "Move"  x3304
    "Interact"  x504
    "Jump"  x425
    "Ascend"  x68
    "Hoverboard"  x59
    "Descend"  x44
    "Sprint"  x30
    "Map"  x4
    "Pause"  x4
    "SkipCinematic"  x1
data.key  (string, 4443/4443 records, 3 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4443/4443 records)
    "Player"  x3505
    "Drone"  x938
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4439 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2879); Unit 4 Dev (888); Unit 3 Dungeon Dev (350); Unit 5 Dev - Dungeon (322)
- **Intervals:** median 0.07s (p5 0.00s / p95 1.98s, n=4438)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4439/4439 records)
    "BecameVisible"  x1278
    "BecameInvisible"  x1252
    "BecameCameraCentered"  x957
    "BecameCameraUncentered"  x952
data.pieceId  (string, 4439/4439 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4439/4439 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2705 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1106); Unit 3 Dev (362); Unit 4 Dev - Dungeon (230); Unit 4 Dev (227); Unit 1 Dev (183); Unit 5 Dev (175); Unit 3 Dungeon Dev (151); Unit 5 Dev - Dungeon (141); Unit 4 Dev - Anderson Base (130)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.26s, n=2693)
- **Fields under `data`:**

```text
data.position  (object, 2705/2705 records)
data.position.x  (number, 2705/2705 records)
    numeric range -1050.35 .. 1551.87 (1029 unique)
data.position.y  (number, 2705/2705 records)
    numeric range -112.489 .. 222.005 (725 unique)
data.position.z  (number, 2705/2705 records)
    numeric range -1216.64 .. 2211.81 (1028 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2350 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (841); Unit 3 Dev (365); Unit 5 Dev (275); Unit 4 Dev (264); Unit 1 Dev (185); Unit 3 Dungeon Dev (121); Unit 4 Dev - Anderson Base (112); Unit 4 Dev - Dungeon (110); Unit 5 Dev - Dungeon (77)
- **eventKey:** present on 1461 of 2350 records
- **Intervals:** median 4.02s (p5 0.00s / p95 39.85s, n=2349)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1461; [conversationId, dialogueEventType] x889
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2350/2350 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2350/2350 records)
    "DialogueNodeEvent"  x1461
    "DialogueStartEvent"  x449
    "DialogueFinishEvent"  x440
data.nodeId  (number, 1461/2350 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 447 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (129); Unit 5 Dev (128); Unit 3 Dev (123); Unit 1 Dev (44); Unit 2 Prod (Refactor) (23)
- **Intervals:** median 0.50s (p5 0.03s / p95 9.07s, n=446)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 447/447 records)
    "argumentationNodeHoverEnd"  x186
    "argumentationNodeHoverStart"  x182
    "argumentationNodeAdd"  x49
    "argumentationNodeRemove"  x30
data.argumentationTitle  (string, 447/447 records)
    "Unit 4 - Flooding"  x129
    "Unit 5"  x128
    "Unit 3 - Pollution Upstream"  x123
    "Unit 1 - Freshwater"  x27
    "Unit 2 – Watershed"  x23
    "Unit 1 - Argumentation Tutorial"  x17
data.nodeName  (string, 447/447 records)
    "B"  x56
    "A"  x53
    "II"  x53
    "I"  x47
    "D"  x44
    "4"  x40
    "1"  x39
    "3"  x37
    "C"  x32
    "2"  x25
    "5"  x21
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 257 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (71); Unit 2 Prod (Refactor) (63); Unit 3 Dungeon Dev (43); Unit 5 Dev - Dungeon (18); Unit 4 Dev (17); Unit 5 Dev (15); Unit 3 Dev (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 18.00s (p5 0.71s / p95 679.05s, n=256)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 257/257 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 257/257 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 98 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (86); Unit 3 Dev (6); Unit 4 Dev (6)
- **Intervals:** median 2.48s (p5 0.16s / p95 29.18s, n=97)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x90; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/98 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/98 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 90/98 records)
    "RightDrag"  x50
    "LeftDrag"  x40
data.currentSoilType  (string, 90/98 records)
    "SAND"  x18
    "CLAYSAND"  x16
    "SANDGRAVEL"  x16
    "CLAY"  x14
    "CLAYROCK"  x13
    "GRAVEL"  x8
    "BEDROCK"  x5
data.isCorrectSelection  (string, 90/98 records)
    "false"  x69
    "true"  x21
data.waterLevelStatus  (string, 90/98 records)
    "TooHigh"  x41
    "TooLow"  x39
    "Proper"  x10
data.waterRetentionChange  (string, 90/98 records)
    "Increase"  x43
    "Decrease"  x26
    "NoChange"  x21
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 87 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 5 Dev (13); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 87 of 87 records
- **Intervals:** median 227.50s (p5 0.01s / p95 62435.86s, n=86)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 87/87 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x35
data.questID  (string, 87/87 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 87/87 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/87 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 65 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 3 Dev (13); Unit 4 Dev (13); Unit 2 Prod (Refactor) (8); Unit 4 Dev - Anderson Base (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 214.46s (p5 9.14s / p95 64281.87s, n=64)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 65/65 records)
    true  x65
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 53 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (13); Unit 4 Dev (13); Unit 4 Dev - Anderson Base (7); Unit 3 Dungeon Dev (2); Unit 5 Dev (2); MainMenu (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 223.65s (p5 4.99s / p95 73991.27s, n=52)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 53/53 records)
    false  x53
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TopographicMapEvent` — 47 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (43); Unit 3 Dev (4)
- **Intervals:** median 4.22s (p5 0.53s / p95 69132.59s, n=46)
- **`data` key-set variants:** [actionType, featureUsed] x22; [actionType, featureUsed, location] x19; [actionType, featureUsed, legendName] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "WaypointMoveEvent"  x16
    "MapCloseEvent"  x11
    "MapOpenEvent"  x11
    "Selected"  x4
    "WaypointSetEvent"  x3
    "Unselected"  x2
data.featureUsed  (string, 47/47 records)
    "Map"  x22
    "Waypoint"  x19
    "Legend"  x6
data.legendName  (string, 6/47 records)
    "150 ft"  x2
    "Water"  x2
    "0 ft"  x1
    "360 ft"  x1
data.location  (object, 19/47 records)
data.location.x  (number, 19/47 records)
    numeric range -319.411 .. -143.673 (15 unique)
data.location.y  (number, 19/47 records)
    numeric range -93.3565 .. 150.002 (16 unique)
data.location.z  (number, 19/47 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 43 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (19); Unit 3 Dev (17); Unit 1 Dev (3); Unit 5 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 5.72s (p5 1.92s / p95 12366.53s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "submitAnswerEvent"  x43
data.answerSubmitted  (string, 43/43 records)
    22 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 43/43 records)
    "Unit 4 - Flooding"  x19
    "Unit 3 - Pollution Upstream"  x17
    "Unit 5"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 38 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (9); Unit 4 Dev (4); Unit 3 Dev (3); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1342.01s (p5 9.19s / p95 85440.83s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "DebugMenuStateChanged"  x38
data.isOpened  (bool, 38/38 records)
    false  x38
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 35 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (35)
- **Intervals:** median 20.31s (p5 3.15s / p95 99.55s, n=34)
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "On"  x22
    "Off"  x13
data.floor  (string, 35/35 records)
    "4"  x24
    "3"  x6
    "2"  x3
    "1"  x2
data.machineNumber  (string, 35/35 records)
    "One"  x34
    "Two"  x1
data.machineType  (string, 35/35 records)
    "Condenser"  x17
    "Evaporator"  x15
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 35/35 records)
    "3"  x18
    "2"  x10
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 8155.61s (p5 92.39s / p95 138579.47s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 194.60s (p5 0.04s / p95 355508.20s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 12 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (12)
- **Intervals:** median 3.44s (p5 1.61s / p95 265.71s, n=11)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x10; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "optionSelected"  x10
    "DesignSubmitted"  x2
data.designSelections  (object, 2/12 records)
data.designSelections.glassRoofTemperature  (string, 2/12 records)
    "Hot"  x2
data.designSelections.roofCovering  (string, 2/12 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/12 records)
    "Flat"  x1
    "Tilted Out"  x1
data.featureUsed  (string, 12/12 records)
    "RoofStyle"  x5
    "GlassRoofTemperature"  x3
    "ExtraCovering"  x2
    "Submit"  x2
data.selectedOption  (string, 10/12 records)
    "Flat"  x2
    "Hot"  x2
    "Tilted Out"  x2
    "Cold"  x1
    "Covered"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 1.28s (p5 1.08s / p95 26.17s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 8 empty-string)
    ""  x8
    "cameraPlaced"  x3
data.boxId  (string, 11/11 records)
    "0"  x6
    "1"  x3
    "2"  x2
data.soilType  (string, 11/11 records)
    "Clay"  x8
    "Sand"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 11 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 1 Dev (2)
- **Intervals:** median 2.88s (p5 0.76s / p95 431378.13s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationToolOpen"  x10
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 11/11 records)
    "BackingInfoPanel - Watershed Graph"  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 10 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (10)
- **Intervals:** median 30.39s (p5 3.75s / p95 538.45s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "ChangeCanister"  x10
data.canisterType  (string, 10/10 records)
    "Clay"  x4
    "Bedrock"  x2
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 10/10 records)
    "5"  x5
    "3"  x4
    "4"  x1
data.machine  (string, 10/10 records)
    "1"  x9
    "2"  x1
data.row  (string, 10/10 records)
    "TopRow"  x7
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 5 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (5)
- **Intervals:** median 31744.66s (p5 5.86s / p95 448983.97s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Open"  x3
    "Close"  x2
data.toolName  (string, 5/5 records, 5 empty-string)
    ""  x5
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 12394.13s (p5 9405.52s / p95 701478.72s, n=3)
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
- **Intervals:** median 1410.79s (p5 1358.38s / p95 8018.33s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Permissions check failed"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "TypeError: Permissions check failed"  x1
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
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (86 records)
- `TerasGardenBox` data.actionType: "" (8x)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "Unselected" (2x); "WaypointMoveEvent" (16x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (6x); "Waypoint" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (30x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*