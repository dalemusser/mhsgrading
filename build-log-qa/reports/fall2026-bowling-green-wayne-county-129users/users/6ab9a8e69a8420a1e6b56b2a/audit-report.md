# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b2a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b2a
- **Game version string(s) in log:** 2.8.4, 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b2a.jsonl
- **Records:** 12024 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b2a
- **Time span:** 2026-10-05T16:25:35.918000+00:00 .. 2026-10-18T17:42:56.656000+00:00 (313h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b2a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 12024 records, 10 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 107 INFO, 0 NOT_TESTED, 102 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3894 | 32.39 | 1 | 9 | 0 | 2026-10-05T16:32:34.632000+00:00 | 2026-10-18T17:42:56.656000+00:00 | 313h 10m |
| PlayerPositionEvent | 2618 | 21.77 | 1 | 9 | 0 | 2026-10-05T16:32:31.177000+00:00 | 2026-10-18T17:42:50.699000+00:00 | 313h 10m |
| DialogueEvent | 2351 | 19.55 | 1 | 9 | 1512 | 2026-10-05T16:32:51.163000+00:00 | 2026-10-18T17:42:45.174000+00:00 | 313h 9m |
| PuzzlePieceVisibleEvent | 2122 | 17.65 | 1 | 4 | 0 | 2026-10-07T16:38:12.821000+00:00 | 2026-10-16T17:00:43.833000+00:00 | 216h 22m |
| ObjectInterEvent | 264 | 2.2 | 1 | 9 | 0 | 2026-10-05T16:42:37.328000+00:00 | 2026-10-18T17:42:56.656000+00:00 | 313h 0m |
| argumentationNodeEvent | 249 | 2.07 | 1 | 5 | 0 | 2026-10-06T16:56:04.131000+00:00 | 2026-10-18T17:29:28.662000+00:00 | 288h 33m |
| Soil Key Puzzle | 138 | 1.15 | 1 | 3 | 0 | 2026-10-07T16:37:50.785000+00:00 | 2026-10-15T16:27:35.719000+00:00 | 191h 49m |
| questEvent | 91 | 0.76 | 1 | 9 | 91 | 2026-10-05T16:32:51.140000+00:00 | 2026-10-18T17:39:14.833000+00:00 | 313h 6m |
| TopographicMapEvent | 73 | 0.61 | 1 | 2 | 0 | 2026-10-07T16:38:59.345000+00:00 | 2026-10-15T01:38:41.115000+00:00 | 176h 59m |
| DEBUGMenu | 37 | 0.31 | 1 | 9 | 0 | 2026-10-05T16:32:31.158000+00:00 | 2026-10-18T17:21:16.932000+00:00 | 312h 48m |
| WaterChamberEvent | 34 | 0.28 | 1 | 1 | 0 | 2026-10-16T16:53:16.132000+00:00 | 2026-10-16T18:11:53.517000+00:00 | 1h 18m |
| soilMachine | 23 | 0.19 | 1 | 1 | 0 | 2026-10-15T16:48:17.166000+00:00 | 2026-10-15T17:02:02.135000+00:00 | 13m 44s |
| gameWindowFocusEvent | 22 | 0.18 | 1 | 4 | 0 | 2026-10-05T16:25:35.918000+00:00 | 2026-10-18T17:21:17.080000+00:00 | 312h 55m |
| argumentationAnswerEvent | 21 | 0.17 | 1 | 5 | 0 | 2026-10-06T16:56:41.927000+00:00 | 2026-10-18T17:29:30.769000+00:00 | 288h 32m |
| gameStartEvent | 18 | 0.15 | 1 | 1 | 0 | 2026-10-05T16:25:35.919000+00:00 | 2026-10-18T17:21:17.080000+00:00 | 312h 55m |
| argumentationEvent | 14 | 0.12 | 1 | 5 | 0 | 2026-10-06T16:56:30.968000+00:00 | 2026-10-18T17:29:30.806000+00:00 | 288h 32m |
| argumentationToolEvent | 14 | 0.12 | 1 | 4 | 0 | 2026-10-06T16:56:27.649000+00:00 | 2026-10-18T17:28:24.240000+00:00 | 288h 31m |
| gameWindowUnfocusEvent | 10 | 0.08 | 1 | 5 | 0 | 2026-10-05T17:04:31.346000+00:00 | 2026-10-16T17:09:43.347000+00:00 | 264h 5m |
| TerasGardenBox | 9 | 0.07 | 1 | 1 | 0 | 2026-10-16T16:38:34.199000+00:00 | 2026-10-16T16:39:45.628000+00:00 | 1m 11s |
| chatEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-10-16T16:47:29.262000+00:00 | 2026-10-18T17:21:27.105000+00:00 | 48h 33m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T17:01:40.639000+00:00 | 2026-10-18T17:42:56.639000+00:00 | 288h 41m |
| SolarStillDesignEvent | 5 | 0.04 | 1 | 1 | 0 | 2026-10-18T17:35:33.768000+00:00 | 2026-10-18T17:35:48.111000+00:00 | 14.3s |
| DaniEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-13T16:55:36.023000+00:00 | 2026-10-15T00:48:28.140000+00:00 | 31h 52m |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 158006.126s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.257s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 17.457s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.082s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 3.812s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.814s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 13.014s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 135.267s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 20514.049s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 4483.289s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86392.914s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 8.491s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.1x vs baseline. 
  - Observed: 37 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.6x vs baseline. 
  - Observed: 138 records 
  - Expected: 38 in 09-23-26 
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 300 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,4,I; A,4,II; A,5,II; C,2,II; C,D,2,II; C,D,A,2,II; D,3,II; D,4,II 
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
  - Observed: Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel -  
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
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
- **INFO / Info** `soilMachine` — record volume changed 4.6x vs baseline. 
  - Observed: 23 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 10 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[255] _id=6ac3d404de269131f9adffc7 ts=2026-10-05T16:44:51.3810000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[316] _id=6ac3d506de269131f9ae1a2d ts=2026-10-05T16:49:09.2110000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[335] _id=6ac3d5e9de269131f9ae2d93 ts=2026-10-05T16:52:56.7650000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[5] _id=6ac3cf81de269131f9ada6a5 ts=2026-10-05T16:25:35.9190000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[538] _id=6ac52760de269131f9b57a3c ts=2026-10-06T16:52:47.0810000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[702] _id=6ac529d0de269131f9b5fdcb ts=2026-10-06T17:03:11.0590000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[6] _id=6ac3cf80de269131f9ada6a1 ts=2026-10-05T16:25:35.9180000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[539] _id=6ac52760de269131f9b57a33 ts=2026-10-06T16:52:47.0800000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[703] _id=6ac529cfde269131f9b5fdc1 ts=2026-10-06T17:03:11.0580000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[540] _id=6ac5275fde269131f9b57a15 ts=2026-10-05T17:04:31.346Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[779] _id=6ac67400de269131f9bc8a58 ts=2026-10-06T17:04:24.26Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[2281] _id=6ac7c4b7de269131f9c42688 ts=2026-10-07T17:04:23.508Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 73 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[918] _id=6ac675a3de269131f9bccf52 ts=2026-10-07T16:38:59.3450000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[922] _id=6ac675a6de269131f9bccfdf ts=2026-10-07T16:39:01.7000000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[925] _id=6ac675afde269131f9bcd253 ts=2026-10-07T16:39:10.9200000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3893 | 0.0 | 1.257 | 289.602 | 20.285 | 429506.456 | 0.21 | 160 | 14 |
| PlayerPositionEvent | 2604 | 0.0 | 10.003 | 431.544 | 10.098 | 429505.516 | 0.14 | 1 | 10 |
| DialogueEvent | 2350 | 0.0 | 4.694 | 479.742 | 40.455 | 429511.791 | 0.13 | 628 | 13 |
| PuzzlePieceVisibleEvent | 2121 | 0.0 | 0.082 | 367.256 | 2.749 | 429508.106 | 0.16 | 809 | 8 |
| ObjectInterEvent | 263 | 0.0 | 17.457 | 4284.484 | 1003.579 | 432111.896 | 0.01 | 3 | 16 |
| argumentationNodeEvent | 248 | 0.02 | 0.802 | 4188.728 | 12.531 | 689981.176 | 0.01 | 27 | 4 |
| Soil Key Puzzle | 137 | 0.005 | 1.212 | 5040.766 | 204.166 | 526465.47 | 0.01 | 5 | 6 |
| questEvent | 90 | 0.0 | 227.107 | 12524.263 | 84561.559 | 429706.051 | 0.0 | 18 | 22 |
| TopographicMapEvent | 72 | 0.019 | 10.814 | 8849.747 | 13409.997 | 431836.486 | 0.01 | 2 | 7 |
| DEBUGMenu | 36 | 8.408 | 786.173 | 31281.271 | 108055.151 | 431619.991 | 0.0 | 0 | 21 |
| WaterChamberEvent | 33 | 1.07 | 25.171 | 142.951 | 99.2 | 3704.199 | 0.42 | 0 | 1 |
| soilMachine | 22 | 0.13 | 8.491 | 37.499 | 163.962 | 255.774 | 1.6 | 0 | 0 |
| gameWindowFocusEvent | 21 | 1.634 | 4483.289 | 53644.817 | 169266.7 | 431631.232 | 0.0 | 0 | 18 |
| argumentationAnswerEvent | 20 | 0.361 | 13.014 | 51938.442 | 201789.814 | 690081.519 | 0.0 | 0 | 4 |
| gameStartEvent | 17 | 623.978 | 20514.049 | 66267.127 | 221739.606 | 431631.232 | 0.0 | 0 | 17 |
| argumentationEvent | 13 | 0.028 | 135.267 | 79906.141 | 381568.005 | 689965.955 | 0.0 | 2 | 4 |
| argumentationToolEvent | 13 | 0.642 | 17.098 | 79901.276 | 467071.598 | 690147.14 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 9 | 1.004 | 86392.914 | 105634.667 | 361366.94 | 431122.432 | 0.0 | 0 | 8 |
| TerasGardenBox | 8 | 0.976 | 2.322 | 8.929 | 21.33 | 21.417 | 6.72 | 0 | 0 |
| chatEvent | 5 | 431.118 | 1069.637 | 34967.569 | 136129.524 | 169257.72 | 0.0 | 0 | 3 |
| EndOfUnit | 4 | 33076.364 | 158006.126 | 259819.0 | 613082.965 | 690187.384 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 4 | 2.244 | 3.812 | 3.586 | 4.416 | 4.474 | 16.73 | 0 | 0 |
| DaniEvent | 3 | 5.127 | 13.306 | 38257.372 | 103279.646 | 114753.684 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 15 group(s), 35 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[2690] _id=6ac7c8fade269131f9c49eee ts=2026-10-08T16:46:48.9910000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[2691] _id=6ac7c8fade269131f9c49eef ts=2026-10-08T16:46:48.9910000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[4708] _id=6acfa6e8de269131f9d50eda ts=2026-10-14T15:59:34.1240000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[4709] _id=6acfa6e8de269131f9d50edb ts=2026-10-14T15:59:34.1240000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[5567] _id=6acfb19bde269131f9d5c61c ts=2026-10-14T16:45:14.2380000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[5568] _id=6acfb19bde269131f9d5c61d ts=2026-10-14T16:45:14.2380000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 18 group(s), 29 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[970] _id=6ac675ffde269131f9bce2ba ts=2026-10-07T16:40:29.0370000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[971] _id=6ac675ffde269131f9bce2bb ts=2026-10-07T16:40:29.0370000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[988] _id=6ac67601de269131f9bce325 ts=2026-10-07T16:40:30.4020000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[989] _id=6ac67601de269131f9bce326 ts=2026-10-07T16:40:30.4020000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[996] _id=6ac67601de269131f9bce32d ts=2026-10-07T16:40:30.4150000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[997] _id=6ac67601de269131f9bce32e ts=2026-10-07T16:40:30.4150000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[11758] _id=6ad50240de269131f9e8b860 ts=2026-10-18T17:30:39.2400000Z == 6ab9a8e69a8420a1e6b56b2a.jsonl[11759] _id=6ad50240de269131f9e8b861 ts=2026-10-18T17:30:39.2400000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[217] _id=6ac3d37ede269131f9adf4ed ts=2026-10-05T16:42:37.3280000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[219] _id=6ac3d37ede269131f9adf4f4 ts=2026-10-05T16:42:37.3320000Z`; `258ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[864] _id=6ac67538de269131f9bcb5c6 ts=2026-10-07T16:37:11.9870000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[865] _id=6ac67538de269131f9bcb5d9 ts=2026-10-07T16:37:12.2450000Z`; `219ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[7315] _id=6ad0282dde269131f9d9f051 ts=2026-10-15T01:11:08.7260000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[7316] _id=6ad0282dde269131f9d9f055 ts=2026-10-15T01:11:08.9450000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `976ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10415] _id=6ad25322de269131f9e5fdb2 ts=2026-10-16T16:38:58.1800000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[10416] _id=6ad25323de269131f9e5fdbe ts=2026-10-16T16:38:59.1560000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `901ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[8127] _id=6ad02e54de269131f9da1525 ts=2026-10-15T01:37:23.9190000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[8124] _id=6ad02e55de269131f9da1530 ts=2026-10-15T01:37:24.8200000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `971ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10202] _id=6ad251a9de269131f9e5e8f1 ts=2026-10-16T16:32:40.7030000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[10216] _id=6ad251aade269131f9e5e8f9 ts=2026-10-16T16:32:41.6740000Z`; `361ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10218] _id=6ad251abde269131f9e5e90a ts=2026-10-16T16:32:43.3640000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[10224] _id=6ad251acde269131f9e5e912 ts=2026-10-16T16:32:43.7250000Z`; `364ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10224] _id=6ad251acde269131f9e5e912 ts=2026-10-16T16:32:43.7250000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[10225] _id=6ad251acde269131f9e5e91c ts=2026-10-16T16:32:44.0890000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[7005] _id=6ad0262ede269131f9d9e932 ts=2026-10-15T01:02:37.6480000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[7008] _id=6ad0262ede269131f9d9e935 ts=2026-10-15T01:02:37.6760000Z`; `40ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10290] _id=6ad25212de269131f9e5ee3c ts=2026-10-16T16:34:26.1270000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[10288] _id=6ad25212de269131f9e5ee44 ts=2026-10-16T16:34:26.1670000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `565ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[590] _id=6ac52826de269131f9b5a407 ts=2026-10-06T16:56:05.9910000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[592] _id=6ac52827de269131f9b5a42d ts=2026-10-06T16:56:06.5560000Z`; `153ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[6943] _id=6ad025e2de269131f9d9e847 ts=2026-10-15T01:01:21.4560000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[6945] _id=6ad025e2de269131f9d9e84b ts=2026-10-15T01:01:21.6090000Z`; `360ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[6989] _id=6ad02613de269131f9d9e8d7 ts=2026-10-15T01:02:10.9790000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[6983] _id=6ad02614de269131f9d9e8db ts=2026-10-15T01:02:11.3390000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `642ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[6938] _id=6ad025d1de269131f9d9e817 ts=2026-10-15T01:01:04.2750000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[6940] _id=6ad025d1de269131f9d9e819 ts=2026-10-15T01:01:04.9170000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11923] _id=6ad503d8de269131f9e8b984 ts=2026-10-18T17:37:27.0640000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[11918] _id=6ad503d8de269131f9e8b986 ts=2026-10-18T17:37:27.0710000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `801ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[9347] _id=6ad105e2de269131f9de1b65 ts=2026-10-15T16:57:06.0200000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[9345] _id=6ad105e3de269131f9de1b88 ts=2026-10-15T16:57:06.8210000Z`; `199ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[9355] _id=6ad105e5de269131f9de1bb5 ts=2026-10-15T16:57:08.5980000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[9354] _id=6ad105e5de269131f9de1bba ts=2026-10-15T16:57:08.7970000Z`; `133ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[9354] _id=6ad105e5de269131f9de1bba ts=2026-10-15T16:57:08.7970000Z ~ 6ab9a8e69a8420a1e6b56b2a.jsonl[9346] _id=6ad105e5de269131f9de1bc4 ts=2026-10-15T16:57:08.9300000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2282] _id=6ac7c4c2de269131f9c42777 ts=2026-10-08T16:28:49.3600000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3595] _id=6ace5ac6de269131f9cf5fa6 ts=2026-10-13T16:22:29.3510000Z; 47h 1m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11508] _id=6ad26adade269131f9e6ff4a ts=2026-10-16T18:20:10.0550000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11537] _id=6ad5000ede269131f9e8b59e ts=2026-10-18T17:21:16.9320000Z; 24h 20m: 6ab9a8e69a8420a1e6b56b2a.jsonl[9] _id=6ac3d120de269131f9adc6b7 ts=2026-10-05T16:32:31.1580000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[542] _id=6ac52783de269131f9b57fd5 ts=2026-10-06T16:53:22.4000000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 31h 52m 
  - Evidence: 31h 52m: 6ab9a8e69a8420a1e6b56b2a.jsonl[4305] _id=6ace6296de269131f9cfe1bb ts=2026-10-13T16:55:49.3290000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[6693] _id=6ad022d7de269131f9d9dd18 ts=2026-10-15T00:48:23.0130000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3572] _id=6ac7cd0fde269131f9c4df4e ts=2026-10-08T17:04:14.9190000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3605] _id=6ace5ad8de269131f9cf6059 ts=2026-10-13T16:22:46.7100000Z; 47h 3m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11502] _id=6ad26a82de269131f9e6fe5c ts=2026-10-16T18:18:41.7520000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11558] _id=6ad50031de269131f9e8b5dc ts=2026-10-18T17:21:52.6460000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b2a.jsonl[533] _id=6ac3d874de269131f9ae6fb9 ts=2026-10-05T17:03:47.4630000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[565] _id=6ac527bbde269131f9b58bf9 ts=2026-10-06T16:54:18.1930000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 628 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10184] _id=6ad25184de269131f9e5e6ff ts=2026-10-16T16:32:03.7940000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10185] _id=6ad25184de269131f9e5e700 ts=2026-10-16T16:32:03.7940000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[6993] _id=6ad0261ade269131f9d9e8f1 ts=2026-10-15T01:02:17.5560000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[6994] _id=6ad0261ade269131f9d9e8f2 ts=2026-10-15T01:02:17.5560000Z; 1ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10126] _id=6ad25247de269131f9e5f196 ts=2026-10-16T16:35:19.3550000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10127] _id=6ad25247de269131f9e5f197 ts=2026-10-16T16:35:19.3560000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 43m 
  - Evidence: 191h 43m: 6ab9a8e69a8420a1e6b56b2a.jsonl[762] _id=6ac52975de269131f9b5ed34 ts=2026-10-06T17:01:40.6390000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5557] _id=6acfb180de269131f9d5c347 ts=2026-10-14T16:44:48.0230000Z; 48h 55m: 6ab9a8e69a8420a1e6b56b2a.jsonl[10599] _id=6ad25503de269131f9e6161f ts=2026-10-16T16:46:58.7150000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[12023] _id=6ad50521de269131f9e8ba4d ts=2026-10-18T17:42:56.6390000Z; 38h 50m: 6ab9a8e69a8420a1e6b56b2a.jsonl[8338] _id=6ad032b5de269131f9da2401 ts=2026-10-15T01:56:04.3870000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10599] _id=6ad25503de269131f9e6161f ts=2026-10-16T16:46:58.7150000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3582] _id=6ac7cd15de269131f9c4df9a ts=2026-10-08T17:04:20.2330000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3604] _id=6ace5ad8de269131f9cf6058 ts=2026-10-13T16:22:46.6890000Z; 47h 0m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11526] _id=6ad26afdde269131f9e6ff99 ts=2026-10-16T18:20:44.9680000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11539] _id=6ad5001bde269131f9e8b5b2 ts=2026-10-18T17:21:29.5650000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b2a.jsonl[474] _id=6ac3d842de269131f9ae6bd3 ts=2026-10-05T17:02:57.1240000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[544] _id=6ac52785de269131f9b58033 ts=2026-10-06T16:53:24.0040000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 160 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11223] _id=6ad26776de269131f9e6f4bc ts=2026-10-16T18:05:40.3290000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11224] _id=6ad26776de269131f9e6f4bd ts=2026-10-16T18:05:40.3290000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11224] _id=6ad26776de269131f9e6f4bd ts=2026-10-16T18:05:40.3290000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11225] _id=6ad26776de269131f9e6f4be ts=2026-10-16T18:05:40.3290000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11406] _id=6ad26923de269131f9e6fa11 ts=2026-10-16T18:12:50.1440000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11407] _id=6ad26923de269131f9e6fa12 ts=2026-10-16T18:12:50.1440000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3506] _id=6ac7cc3ade269131f9c4d308 ts=2026-10-08T17:00:41.8200000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[4648] _id=6ace642ade269131f9d00440 ts=2026-10-13T17:02:33.7160000Z; 47h 3m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11503] _id=6ad26a82de269131f9e6fe5d ts=2026-10-16T18:18:41.7530000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11568] _id=6ad5003bde269131f9e8b5fa ts=2026-10-18T17:22:02.6010000Z; 24h 5m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2070] _id=6ac6780fde269131f9bd3426 ts=2026-10-07T16:49:18.9150000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3110] _id=6ac7cabcde269131f9c4b849 ts=2026-10-08T16:54:19.1540000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10080] _id=6ad250a9de269131f9e5d9ed ts=2026-10-16T16:28:25.2260000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10081] _id=6ad250a9de269131f9e5d9ee ts=2026-10-16T16:28:25.2260000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[9986] _id=6ad25023de269131f9e5d1d6 ts=2026-10-16T16:26:11.4270000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[9987] _id=6ad25023de269131f9e5d1d7 ts=2026-10-16T16:26:11.4270000Z; 4ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[217] _id=6ac3d37ede269131f9adf4ed ts=2026-10-05T16:42:37.3280000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[219] _id=6ac3d37ede269131f9adf4f4 ts=2026-10-05T16:42:37.3320000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3573] _id=6ac7cd11de269131f9c4df60 ts=2026-10-08T17:04:16.2540000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3603] _id=6ace5ad8de269131f9cf6057 ts=2026-10-13T16:22:41.7700000Z; 47h 0m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11527] _id=6ad26b07de269131f9e6ffa1 ts=2026-10-16T18:20:54.8480000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11538] _id=6ad5001bde269131f9e8b5b1 ts=2026-10-18T17:21:27.2700000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b2a.jsonl[531] _id=6ac3d89ade269131f9ae72bb ts=2026-10-05T17:04:26.0420000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[543] _id=6ac52785de269131f9b5802d ts=2026-10-06T16:53:22.4230000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[5854] _id=6acfb632de269131f9d644b2 ts=2026-10-14T17:04:49.1010000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5858] _id=6acfd12ade269131f9d7d8cc ts=2026-10-14T17:04:49.101Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3578] _id=6ac7cd15de269131f9c4dfa9 ts=2026-10-08T17:04:19.4200000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3608] _id=6ace5ad8de269131f9cf605d ts=2026-10-13T16:22:47.5260000Z; 32h 16m: 6ab9a8e69a8420a1e6b56b2a.jsonl[4296] _id=6ace626cde269131f9cfdfbf ts=2026-10-13T16:55:06.5140000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[7342] _id=6ad0285ede269131f9d9f12c ts=2026-10-15T01:11:56.3360000Z; 24h 9m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2019] _id=6ac67780de269131f9bd2383 ts=2026-10-07T16:46:54.4090000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3168] _id=6ac7cb28de269131f9c4bf6d ts=2026-10-08T16:56:07.5360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 809 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[1000] _id=6ac67604de269131f9bce378 ts=2026-10-07T16:40:34.9790000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[1001] _id=6ac67604de269131f9bce37e ts=2026-10-07T16:40:34.9790000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[1001] _id=6ac67604de269131f9bce37e ts=2026-10-07T16:40:34.9790000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[982] _id=6ac67605de269131f9bce38c ts=2026-10-07T16:40:34.9790000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[1003] _id=6ac67605de269131f9bce38e ts=2026-10-07T16:40:35.0440000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[1002] _id=6ac67605de269131f9bce396 ts=2026-10-07T16:40:35.0440000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 146h 14m 
  - Evidence: 146h 14m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3135] _id=6ac7caf5de269131f9c4bb4a ts=2026-10-08T16:55:16.8810000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[6085] _id=6acfd377de269131f9d82be0 ts=2026-10-14T19:09:42.3510000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2231] _id=6ac67af1de269131f9bd7f32 ts=2026-10-07T17:01:37.3970000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[2380] _id=6ac7c5ddde269131f9c44242 ts=2026-10-08T16:33:32.9790000Z; 15h 15m: 6ab9a8e69a8420a1e6b56b2a.jsonl[7311] _id=6ad02827de269131f9d9f02b ts=2026-10-15T01:11:02.7560000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[8400] _id=6ad0fed2de269131f9dd7f32 ts=2026-10-15T16:26:57.6460000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[3085] _id=6ac7cadade269131f9c4b9dd ts=2026-10-08T16:54:49.6770000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3096] _id=6ac7cadade269131f9c4b9e1 ts=2026-10-08T16:54:49.6820000Z; 6ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[3097] _id=6ac7cadade269131f9c4b9e5 ts=2026-10-08T16:54:50.0460000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3098] _id=6ac7cadbde269131f9c4b9e7 ts=2026-10-08T16:54:50.0520000Z; 7ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[2110] _id=6ac678a3de269131f9bd44f5 ts=2026-10-07T16:51:47.0360000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[2111] _id=6ac678a3de269131f9bd44ff ts=2026-10-07T16:51:47.0430000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 57m 
  - Evidence: 119h 57m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2536] _id=6ac7c796de269131f9c47c9d ts=2026-10-08T16:40:53.6650000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3889] _id=6ace5e72de269131f9cf9400 ts=2026-10-13T16:38:10.1510000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b2a.jsonl[934] _id=6ac675c6de269131f9bcd7c1 ts=2026-10-07T16:39:33.3950000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[2347] _id=6ac7c57cde269131f9c4361a ts=2026-10-08T16:31:55.7300000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b2a.jsonl[4431] _id=6ace6362de269131f9cfecfe ts=2026-10-13T16:59:14.3670000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5634] _id=6acfb2f6de269131f9d5f451 ts=2026-10-14T16:51:01.0200000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.021s shown 
  - Evidence: 19ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[2351] _id=6ac7c58fde269131f9c437e5 ts=2026-10-08T16:32:14.7490000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[2355] _id=6ac7c58fde269131f9c437e9 ts=2026-10-08T16:32:14.7680000Z; 21ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[2350] _id=6ac7c58fde269131f9c437dd ts=2026-10-08T16:32:14.7280000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[2351] _id=6ac7c58fde269131f9c437e5 ts=2026-10-08T16:32:14.7490000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 1m 
  - Evidence: 1h 1m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11184] _id=6ad25912de269131f9e66030 ts=2026-10-16T17:04:17.5530000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11235] _id=6ad2678ade269131f9e6f4f5 ts=2026-10-16T18:06:01.7520000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 41m 
  - Evidence: 191h 41m: 6ab9a8e69a8420a1e6b56b2a.jsonl[665] _id=6ac528cade269131f9b5cc77 ts=2026-10-06T16:58:49.3430000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5469] _id=6acfb06bde269131f9d5ad57 ts=2026-10-14T16:40:10.8620000Z; 48h 54m: 6ab9a8e69a8420a1e6b56b2a.jsonl[10285] _id=6ad25212de269131f9e5ee3a ts=2026-10-16T16:34:26.0970000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11719] _id=6ad501edde269131f9e8b7f9 ts=2026-10-18T17:29:16.3480000Z; 39h 29m: 6ab9a8e69a8420a1e6b56b2a.jsonl[7004] _id=6ad0262ede269131f9d9e930 ts=2026-10-15T01:02:37.6290000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10187] _id=6ad25184de269131f9e5e6fd ts=2026-10-16T16:32:03.7680000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 39m 
  - Evidence: 191h 39m: 6ab9a8e69a8420a1e6b56b2a.jsonl[667] _id=6ac528cade269131f9b5cc7d ts=2026-10-06T16:58:49.3630000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5429] _id=6acfaff8de269131f9d5a037 ts=2026-10-14T16:38:15.3180000Z; 48h 52m: 6ab9a8e69a8420a1e6b56b2a.jsonl[10288] _id=6ad25212de269131f9e5ee44 ts=2026-10-16T16:34:26.1670000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11672] _id=6ad50174de269131f9e8b77f ts=2026-10-18T17:27:15.5390000Z; 39h 29m: 6ab9a8e69a8420a1e6b56b2a.jsonl[7008] _id=6ad0262ede269131f9d9e935 ts=2026-10-15T01:02:37.6760000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10164] _id=6ad2516ade269131f9e5e57c ts=2026-10-16T16:31:38.0670000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.028s..0.040s shown 
  - Evidence: 28ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[7005] _id=6ad0262ede269131f9d9e932 ts=2026-10-15T01:02:37.6480000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[7008] _id=6ad0262ede269131f9d9e935 ts=2026-10-15T01:02:37.6760000Z; 40ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10290] _id=6ad25212de269131f9e5ee3c ts=2026-10-16T16:34:26.1270000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10288] _id=6ad25212de269131f9e5ee44 ts=2026-10-16T16:34:26.1670000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 39m 
  - Evidence: 191h 39m: 6ab9a8e69a8420a1e6b56b2a.jsonl[663] _id=6ac528c1de269131f9b5ca9f ts=2026-10-06T16:58:39.8870000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5430] _id=6acfaffdde269131f9d5a0c8 ts=2026-10-14T16:38:21.0630000Z; 48h 53m: 6ab9a8e69a8420a1e6b56b2a.jsonl[10287] _id=6ad25210de269131f9e5ee10 ts=2026-10-16T16:34:23.7320000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11681] _id=6ad5017dde269131f9e8b788 ts=2026-10-18T17:27:24.4300000Z; 39h 28m: 6ab9a8e69a8420a1e6b56b2a.jsonl[7003] _id=6ad0262cde269131f9d9e92c ts=2026-10-15T01:02:35.9380000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10163] _id=6ad25166de269131f9e5e545 ts=2026-10-16T16:31:34.3750000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 27 interval(s) ≤ 0.020s..0.023s shown 
  - Evidence: 20ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11696] _id=6ad501c8de269131f9e8b7cb ts=2026-10-18T17:28:39.0820000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11697] _id=6ad501c8de269131f9e8b7cc ts=2026-10-18T17:28:39.1020000Z; 23ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10244] _id=6ad251cbde269131f9e5ea51 ts=2026-10-16T16:33:15.3190000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10245] _id=6ad251ccde269131f9e5ea57 ts=2026-10-16T16:33:15.3420000Z; 23ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[6952] _id=6ad025e8de269131f9d9e870 ts=2026-10-15T01:01:27.9830000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[6953] _id=6ad025e8de269131f9d9e872 ts=2026-10-15T01:01:28.0060000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 6ab9a8e69a8420a1e6b56b2a.jsonl[602] _id=6ac5283fde269131f9b5aa33 ts=2026-10-06T16:56:30.8120000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[5438] _id=6acfb022de269131f9d5a4c8 ts=2026-10-14T16:38:57.9520000Z; 88h 25m: 6ab9a8e69a8420a1e6b56b2a.jsonl[6960] _id=6ad025f2de269131f9d9e897 ts=2026-10-15T01:01:37.8470000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11685] _id=6ad50185de269131f9e8b798 ts=2026-10-18T17:27:32.4170000Z; 8h 21m: 6ab9a8e69a8420a1e6b56b2a.jsonl[5445] _id=6acfb04ade269131f9d5a9f5 ts=2026-10-14T16:39:38.0920000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[6929] _id=6ad025cdde269131f9d9e811 ts=2026-10-15T01:01:01.1280000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 0m 
  - Evidence: 47h 0m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11507] _id=6ad26aeede269131f9e6ff67 ts=2026-10-16T18:20:29.3850000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11548] _id=6ad50018de269131f9e8b5ad ts=2026-10-18T17:21:27.1050000Z; 1h 0m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11140] _id=6ad2594fde269131f9e661dc ts=2026-10-16T17:05:18.8990000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11215] _id=6ad26770de269131f9e6f4af ts=2026-10-16T18:05:35.6370000Z; 17m 49s: 6ab9a8e69a8420a1e6b56b2a.jsonl[10604] _id=6ad25521de269131f9e61832 ts=2026-10-16T16:47:29.2620000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11140] _id=6ad2594fde269131f9e661dc ts=2026-10-16T17:05:18.8990000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2280] _id=6ac7c4b7de269131f9c4268e ts=2026-10-08T16:28:38.4250000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3597] _id=6ace5ac6de269131f9cf5fa8 ts=2026-10-13T16:22:29.6570000Z; 47h 1m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11511] _id=6ad26adbde269131f9e6ff4d ts=2026-10-16T18:20:10.3800000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11547] _id=6ad5000ede269131f9e8b5a1 ts=2026-10-18T17:21:17.0800000Z; 24h 27m: 6ab9a8e69a8420a1e6b56b2a.jsonl[5] _id=6ac3cf81de269131f9ada6a5 ts=2026-10-05T16:25:35.9190000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[538] _id=6ac52760de269131f9b57a3c ts=2026-10-06T16:52:47.0810000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2279] _id=6ac7c4b7de269131f9c4268d ts=2026-10-08T16:28:38.4250000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3596] _id=6ace5ac6de269131f9cf5fa7 ts=2026-10-13T16:22:29.6570000Z; 47h 1m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11510] _id=6ad26adbde269131f9e6ff4c ts=2026-10-16T18:20:10.3800000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11546] _id=6ad5000ede269131f9e8b5a0 ts=2026-10-18T17:21:17.0800000Z; 24h 27m: 6ab9a8e69a8420a1e6b56b2a.jsonl[6] _id=6ac3cf80de269131f9ada6a1 ts=2026-10-05T16:25:35.9180000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[539] _id=6ac52760de269131f9b57a33 ts=2026-10-06T16:52:47.0800000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3594] _id=6ace5ac5de269131f9cf5fa1 ts=2026-10-08T17:04:24.836Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[4027] _id=6ace612cde269131f9cfc721 ts=2026-10-13T16:49:47.2680000Z; 71h 18m: 6ab9a8e69a8420a1e6b56b2a.jsonl[4700] _id=6acfa6d6de269131f9d50dd0 ts=2026-10-13T17:05:02.811Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[9899] _id=6ad24f9cde269131f9e5c90f ts=2026-10-16T16:23:56.5130000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b2a.jsonl[2281] _id=6ac7c4b7de269131f9c42688 ts=2026-10-07T17:04:23.508Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3594] _id=6ace5ac5de269131f9cf5fa1 ts=2026-10-08T17:04:24.836Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a8e69a8420a1e6b56b2a.jsonl[3527] _id=6ac7cc4dde269131f9c4d4a0 ts=2026-10-08T17:01:00.7070000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[3607] _id=6ace5ad8de269131f9cf605b ts=2026-10-13T16:22:46.7580000Z; 47h 0m: 6ab9a8e69a8420a1e6b56b2a.jsonl[11523] _id=6ad26af2de269131f9e6ff7d ts=2026-10-16T18:20:33.8170000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11543] _id=6ad5001bde269131f9e8b5b6 ts=2026-10-18T17:21:29.9310000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b2a.jsonl[475] _id=6ac3d845de269131f9ae6c29 ts=2026-10-05T17:03:00.1920000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[548] _id=6ac52785de269131f9b5804f ts=2026-10-06T16:53:24.1630000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11323] _id=6ad26851de269131f9e6f7a0 ts=2026-10-16T18:09:20.5400000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11325] _id=6ad26851de269131f9e6f7a1 ts=2026-10-16T18:09:20.5400000Z; 0ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[11758] _id=6ad50240de269131f9e8b860 ts=2026-10-18T17:30:39.2400000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[11759] _id=6ad50240de269131f9e8b861 ts=2026-10-18T17:30:39.2400000Z; 1ms: 6ab9a8e69a8420a1e6b56b2a.jsonl[10911] _id=6ad2571cde269131f9e64011 ts=2026-10-16T16:55:55.9860000Z -> 6ab9a8e69a8420a1e6b56b2a.jsonl[10912] _id=6ad2571cde269131f9e64012 ts=2026-10-16T16:55:55.9870000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[461] _id=6ac3d82bde269131f9ae6a01 ts=2026-10-05T17:02:34.5300000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[3572] _id=6ac7cd0fde269131f9c4df4e ts=2026-10-08T17:04:14.9190000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[3790] _id=6ace5cbcde269131f9cf763c ts=2026-10-13T16:30:52.2900000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[7008] _id=6ad0262ede269131f9d9e935 ts=2026-10-15T01:02:37.6760000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[10288] _id=6ad25212de269131f9e5ee44 ts=2026-10-16T16:34:26.1670000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[10604] _id=6ad25521de269131f9e61832 ts=2026-10-16T16:47:29.2620000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[11140] _id=6ad2594fde269131f9e661dc ts=2026-10-16T17:05:18.8990000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[11215] _id=6ad26770de269131f9e6f4af ts=2026-10-16T18:05:35.6370000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[8946] _id=6ad101e7de269131f9ddb5c2 ts=2026-10-15T16:40:06.4850000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[11321] _id=6ad26851de269131f9e6f797 ts=2026-10-16T18:09:20.4920000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[11322] _id=6ad26851de269131f9e6f79f ts=2026-10-16T18:09:20.5090000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[792] _id=6ac67429de269131f9bc8d45 ts=?`; `6ab9a8e69a8420a1e6b56b2a.jsonl[9687] _id=6ad24dd2de269131f9e5a9a4 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 17 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[3313] _id=6ac7cbf8de269131f9c4cd7d ts=2026-10-08T16:59:35.1000000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[3310] _id=6ac7cbf9de269131f9c4cda1 ts=2026-10-08T16:59:35.2600000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[3323] _id=6ac7cbfbde269131f9c4cdd7 ts=2026-10-08T16:59:38.1780000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 49 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[970] _id=6ac675ffde269131f9bce2ba ts=2026-10-07T16:40:29.0370000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[971] _id=6ac675ffde269131f9bce2bb ts=2026-10-07T16:40:29.0370000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[972] _id=6ac675ffde269131f9bce2bc ts=2026-10-07T16:40:29.0370000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[5440] _id=6acfb037de269131f9d5a785 ts=2026-10-14T16:39:18.3100000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[5445] _id=6acfb04ade269131f9d5a9f5 ts=2026-10-14T16:39:38.0920000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[6937] _id=6ad025d0de269131f9d9e815 ts=2026-10-15T01:01:03.5900000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 424 start, 415 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 728 open, 716 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'argumentationToolOpen' (totals: 13 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 53 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 163 of 12021 adjacent _id pairs reverse in client time; worst 152.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b2a.jsonl[1023] _id=6ac6760dde269131f9bce4ba ts=2026-10-07T16:40:45.3500000Z`; `6ab9a8e69a8420a1e6b56b2a.jsonl[1022] _id=6ac6760ede269131f9bce4d4 ts=2026-10-07T16:38:12.8210000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.88s, min -429485.10s, max -0.41s over 12022 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b2a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3894 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1658); Unit 3 Dev (904); Unit 4 Dev - Dungeon (312); Unit 1 Dev (216); Unit 5 Dev - Dungeon (209); Unit 3 Dungeon Dev (188); Unit 4 Dev (149); Unit 4 Dev - Anderson Base (129); Unit 5 Dev (129)
- **Intervals:** median 1.26s (p5 0.08s / p95 20.29s, n=3893)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3894/3894 records)
    "pressed"  x3894
data.actionType  (string, 3894/3894 records)
    "Move"  x2808
    "Interact"  x516
    "Jump"  x359
    "Ascend"  x130
    "Hoverboard"  x43
    "Map"  x17
    "Sprint"  x14
    "SkipCinematic"  x3
    "ToggleDebug"  x3
    "Pause"  x1
data.key  (string, 3894/3894 records, 11 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3894/3894 records)
    "Player"  x2422
    "Drone"  x1472
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2618 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (916); Unit 3 Dev (531); Unit 1 Dev (242); Unit 4 Dev (217); Unit 5 Dev (194); Unit 4 Dev - Dungeon (188); Unit 5 Dev - Dungeon (148); Unit 3 Dungeon Dev (117); Unit 4 Dev - Anderson Base (65)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.10s, n=2604)
- **Fields under `data`:**

```text
data.position  (object, 2618/2618 records)
data.position.x  (number, 2618/2618 records)
    numeric range -673.027 .. 1556.26 (763 unique)
data.position.y  (number, 2618/2618 records)
    numeric range -114.326 .. 264.76 (574 unique)
data.position.z  (number, 2618/2618 records)
    numeric range -1283.05 .. 1816.24 (763 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2351 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (692); Unit 3 Dev (475); Unit 4 Dev (274); Unit 5 Dev (262); Unit 1 Dev (223); Unit 3 Dungeon Dev (129); Unit 5 Dev - Dungeon (116); Unit 4 Dev - Anderson Base (98); Unit 4 Dev - Dungeon (82)
- **eventKey:** present on 1512 of 2351 records
- **Intervals:** median 4.69s (p5 0.01s / p95 40.45s, n=2350)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1512; [conversationId, dialogueEventType] x839
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2351/2351 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2351/2351 records)
    "DialogueNodeEvent"  x1512
    "DialogueStartEvent"  x424
    "DialogueFinishEvent"  x415
data.nodeId  (number, 1512/2351 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PuzzlePieceVisibleEvent` — 2122 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1290); Unit 4 Dev (446); Unit 5 Dev - Dungeon (214); Unit 3 Dungeon Dev (172)
- **Intervals:** median 0.08s (p5 0.00s / p95 2.75s, n=2121)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2122/2122 records)
    "BecameVisible"  x728
    "BecameInvisible"  x716
    "BecameCameraCentered"  x339
    "BecameCameraUncentered"  x339
data.pieceId  (string, 2122/2122 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2122/2122 records)
    1592 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `ObjectInterEvent` — 264 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (84); Unit 2 Prod (Refactor) (50); Unit 3 Dungeon Dev (42); Unit 5 Dev (20); Unit 4 Dev (19); Unit 3 Dev (18); Unit 1 Dev (11); Unit 5 Dev - Dungeon (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 17.46s (p5 0.18s / p95 1003.58s, n=263)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 264/264 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 264/264 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 249 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (83); Unit 3 Dev (75); Unit 1 Dev (38); Unit 5 Dev (32); Unit 2 Prod (Refactor) (21)
- **Intervals:** median 0.80s (p5 0.03s / p95 12.53s, n=248)
- **Fields under `data`:**

```text
data.actionType  (string, 249/249 records)
    "argumentationNodeHoverEnd"  x106
    "argumentationNodeHoverStart"  x106
    "argumentationNodeAdd"  x29
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 249/249 records)
    "Unit 4 - Flooding"  x83
    "Unit 3 - Pollution Upstream"  x75
    "Unit 5"  x32
    "Unit 1 - Freshwater"  x21
    "Unit 2 – Watershed"  x21
    "Unit 1 - Argumentation Tutorial"  x17
data.nodeName  (string, 249/249 records)
    "II"  x41
    "A"  x37
    "I"  x33
    "4"  x24
    "D"  x22
    "3"  x21
    "C"  x20
    "B"  x16
    "5"  x15
    "1"  x13
    "2"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 138 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (90); Unit 3 Dev (34); Unit 4 Dev (14)
- **Intervals:** median 1.21s (p5 0.15s / p95 204.17s, n=137)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x130; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/138 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/138 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 130/138 records)
    "RightDrag"  x66
    "LeftDrag"  x64
data.currentSoilType  (string, 130/138 records)
    "CLAY"  x27
    "CLAYSAND"  x27
    "SAND"  x25
    "CLAYROCK"  x22
    "SANDGRAVEL"  x15
    "BEDROCK"  x10
    "GRAVEL"  x4
data.isCorrectSelection  (string, 130/138 records)
    "false"  x100
    "true"  x30
data.waterLevelStatus  (string, 130/138 records)
    "TooHigh"  x55
    "Proper"  x46
    "TooLow"  x29
data.waterRetentionChange  (string, 130/138 records)
    "Increase"  x56
    "Decrease"  x44
    "NoChange"  x30
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 91 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (15); Unit 3 Dev (14); Unit 4 Dev (13); Unit 5 Dev - Dungeon (12); Unit 5 Dev (9); Unit 4 Dev - Dungeon (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 91 of 91 records
- **Intervals:** median 227.11s (p5 0.00s / p95 84561.56s, n=90)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 91/91 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x38
data.questID  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/91 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 73 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (48); Unit 2 Prod (Refactor) (25)
- **Intervals:** median 10.81s (p5 1.24s / p95 13410.00s, n=72)
- **`data` key-set variants:** [actionType, featureUsed] x50; [actionType, featureUsed, location] x22; [actionType, featureUsed, legendName] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 73/73 records)
    "MapCloseEvent"  x25
    "MapOpenEvent"  x25
    "WaypointMoveEvent"  x18
    "WaypointSetEvent"  x4
    "Selected"  x1
data.featureUsed  (string, 73/73 records)
    "Map"  x50
    "Waypoint"  x22
    "Legend"  x1
data.legendName  (string, 1/73 records)
    "300 ft"  x1
data.location  (object, 22/73 records)
data.location.x  (number, 22/73 records)
    numeric range -323.629 .. 88.3016 (20 unique)
data.location.y  (number, 22/73 records)
    numeric range -150.862 .. 277.94 (18 unique)
data.location.z  (number, 22/73 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 37 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (6); Unit 4 Dev (5); Unit 3 Dev (4); Unit 1 Dev (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 786.17s (p5 10.43s / p95 108055.15s, n=36)
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "DebugMenuStateChanged"  x37
data.isOpened  (bool, 37/37 records)
    false  x37
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 34 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (34)
- **Intervals:** median 25.17s (p5 3.27s / p95 99.20s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "On"  x26
    "Off"  x8
data.floor  (string, 34/34 records)
    "4"  x16
    "3"  x12
    "1"  x3
    "2"  x3
data.machineNumber  (string, 34/34 records)
    "One"  x32
    "Two"  x2
data.machineType  (string, 34/34 records)
    "Condenser"  x20
    "Evaporator"  x8
    "VentSwitch"  x4
    "DualChamber_Condenser"  x2
data.room  (string, 34/34 records)
    "2"  x13
    "3"  x10
    "1"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 23 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (23)
- **Intervals:** median 8.49s (p5 0.14s / p95 163.96s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "ChangeCanister"  x23
data.canisterType  (string, 23/23 records)
    "Clay"  x15
    "Bedrock"  x4
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 23/23 records)
    "5"  x21
    "3"  x1
    "4"  x1
data.machine  (string, 23/23 records)
    "1"  x21
    "2"  x2
data.row  (string, 23/23 records)
    "TopRow"  x16
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 22 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 4 Dev (2); Unit 2 Prod (Refactor) (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 4483.29s (p5 249.03s / p95 169266.70s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 21 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (11); Unit 3 Dev (5); Unit 1 Dev (2); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 13.01s (p5 0.36s / p95 201789.81s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "submitAnswerEvent"  x21
data.answerSubmitted  (string, 21/21 records)
    "D,3,II"  x8
    "A,1,I"  x2
    "A,4,I"  x2
    "A,1,II"  x1
    "A,4,II"  x1
    "A,5,I"  x1
    "A,5,II"  x1
    "C,2,II"  x1
    "C,D,2,II"  x1
    "C,D,A,2,II"  x1
    "D,4,II"  x1
    "D,C,3,II"  x1
data.argumentationTitle  (string, 21/21 records)
    "Unit 4 - Flooding"  x11
    "Unit 3 - Pollution Upstream"  x5
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 20514.05s (p5 839.96s / p95 221739.61s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 135.27s (p5 0.04s / p95 381568.01s, n=13)
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

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (6); Unit 2 Prod (Refactor) (4); Unit 1 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 17.10s (p5 0.67s / p95 467071.60s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x2
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 10 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 4 Dev (2); Unit 1 Dev (1); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 86392.91s (p5 366.82s / p95 361366.94s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    false  x10
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 2.32s (p5 1.10s / p95 21.33s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x4
data.boxId  (string, 9/9 records)
    "0"  x4
    "1"  x3
    "2"  x2
data.soilType  (string, 9/9 records)
    "Sand"  x5
    "Clay"  x2
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (4); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 1069.64s (p5 437.42s / p95 136129.52s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x6
data.chatID  (string, 6/6 records)
    "NA"  x6
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 158006.13s (p5 49093.06s / p95 613082.97s, n=4)
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

### `SolarStillDesignEvent` — 5 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (5)
- **Intervals:** median 3.81s (p5 2.44s / p95 4.42s, n=4)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x4; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "optionSelected"  x4
    "DesignSubmitted"  x1
data.designSelections  (object, 1/5 records)
data.designSelections.glassRoofTemperature  (string, 1/5 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/5 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/5 records)
    "Tilted Out"  x1
data.featureUsed  (string, 5/5 records)
    "RoofStyle"  x2
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 4/5 records)
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 13.31s (p5 5.94s / p95 103279.65s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

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
    "unit4"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
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
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (90 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (18x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*