# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b25

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b25
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b25.jsonl
- **Records:** 13148 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b25
- **Time span:** 2026-10-05T16:32:18.407000+00:00 .. 2026-10-19T14:44:06.181000+00:00 (334h 11m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b25\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13148 records, 11 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 108 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4018 | 30.56 | 1 | 4 | 0 | 2026-10-06T16:55:49.420000+00:00 | 2026-10-16T16:50:21.411000+00:00 | 239h 54m |
| InputEvent | 3032 | 23.06 | 1 | 9 | 0 | 2026-10-05T16:32:49.661000+00:00 | 2026-10-19T14:44:06.181000+00:00 | 334h 11m |
| DialogueEvent | 2435 | 18.52 | 1 | 9 | 1499 | 2026-10-05T16:32:49.702000+00:00 | 2026-10-19T14:43:58.639000+00:00 | 334h 11m |
| PlayerPositionEvent | 2072 | 15.76 | 1 | 9 | 0 | 2026-10-05T16:32:29.579000+00:00 | 2026-10-19T14:44:05.041000+00:00 | 334h 11m |
| argumentationNodeEvent | 735 | 5.59 | 1 | 5 | 0 | 2026-10-05T16:55:04.535000+00:00 | 2026-10-19T14:10:25.191000+00:00 | 333h 15m |
| ObjectInterEvent | 318 | 2.42 | 1 | 9 | 0 | 2026-10-05T16:38:05.995000+00:00 | 2026-10-19T14:44:06.181000+00:00 | 334h 6m |
| questEvent | 84 | 0.64 | 1 | 9 | 84 | 2026-10-05T16:32:49.683000+00:00 | 2026-10-19T14:40:26.893000+00:00 | 334h 7m |
| Soil Key Puzzle | 82 | 0.62 | 1 | 3 | 0 | 2026-10-07T16:41:56.034000+00:00 | 2026-10-15T16:27:29.543000+00:00 | 191h 45m |
| argumentationAnswerEvent | 65 | 0.49 | 1 | 5 | 0 | 2026-10-05T16:56:15.593000+00:00 | 2026-10-19T14:10:26.227000+00:00 | 333h 14m |
| TopographicMapEvent | 47 | 0.36 | 1 | 2 | 0 | 2026-10-06T16:56:32.665000+00:00 | 2026-10-14T16:59:43.966000+00:00 | 192h 3m |
| DEBUGMenu | 42 | 0.32 | 1 | 9 | 0 | 2026-10-05T16:32:29.563000+00:00 | 2026-10-19T14:33:05.332000+00:00 | 334h 0m |
| gameWindowFocusEvent | 41 | 0.31 | 1 | 7 | 0 | 2026-10-05T16:32:18.407000+00:00 | 2026-10-19T14:36:08.949000+00:00 | 334h 3m |
| argumentationToolEvent | 33 | 0.25 | 1 | 4 | 0 | 2026-10-05T16:55:48.159000+00:00 | 2026-10-19T14:09:30.696000+00:00 | 333h 13m |
| gameWindowUnfocusEvent | 28 | 0.21 | 1 | 7 | 0 | 2026-10-05T17:04:40.012000+00:00 | 2026-10-19T14:36:07.184000+00:00 | 333h 31m |
| WaterChamberEvent | 25 | 0.19 | 1 | 1 | 0 | 2026-10-16T16:49:04.428000+00:00 | 2026-10-16T16:58:57.541000+00:00 | 9m 53s |
| gameStartEvent | 20 | 0.15 | 1 | 1 | 0 | 2026-10-05T16:32:18.408000+00:00 | 2026-10-19T14:33:05.476000+00:00 | 334h 0m |
| SolarStillDesignEvent | 18 | 0.14 | 1 | 1 | 0 | 2026-10-19T14:18:15.369000+00:00 | 2026-10-19T14:38:18.653000+00:00 | 20m 3s |
| argumentationEvent | 16 | 0.12 | 1 | 5 | 0 | 2026-10-05T16:55:51.911000+00:00 | 2026-10-19T14:10:26.269000+00:00 | 333h 14m |
| EndOfUnit | 11 | 0.08 | 1 | 5 | 0 | 2026-10-05T17:02:07.277000+00:00 | 2026-10-19T14:44:06.164000+00:00 | 333h 41m |
| TerasGardenBox | 10 | 0.08 | 1 | 1 | 0 | 2026-10-16T16:34:32.862000+00:00 | 2026-10-16T16:35:30.929000+00:00 | 58.1s |
| DaniEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-10-07T17:02:04.862000+00:00 | 2026-10-14T16:38:44.002000+00:00 | 167h 36m |
| soilMachine | 5 | 0.04 | 1 | 1 | 0 | 2026-10-15T16:37:56.274000+00:00 | 2026-10-15T16:46:23.867000+00:00 | 8m 27s |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-16T16:44:14.677000+00:00 | 2026-10-19T14:33:20.247000+00:00 | 69h 49m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 441.608s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.264s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.064s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.327s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.415s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.045s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 194.739s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.236s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8932.973s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 627.302s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 482.936s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 142.922s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.5x vs baseline. 
  - Observed: 42 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 18 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 180 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 13.0x vs baseline. 
  - Observed: 65 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; 1,II; A,2,I; A,2,II; A,3,I; A,4,I; A,4,II; B,1,II; B,2,II; B,3,II; B,4,II; C,2,II; C,3,II; C,B,2,II; C,D,2,II; C,D,A,2,II; D,1,I; D,1,II; D,2,II; D,3,I; D,3,II; D,4,I; D,C,1,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.2x vs baseline. 
  - Observed: 735 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 33 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[155] _id=6ac3d2fdde269131f9adec55 ts=2026-10-05T16:40:29.2400000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[208] _id=6ac3d406de269131f9adffe5 ts=2026-10-05T16:44:53.4280000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[247] _id=6ac3d49ade269131f9ae1256 ts=2026-10-05T16:47:21.6600000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[13] _id=6ac3d113de269131f9adc4a1 ts=2026-10-05T16:32:18.4080000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[570] _id=6ac3d868de269131f9ae6eaf ts=2026-10-05T17:03:35.3340000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[584] _id=6ac526b1de269131f9b563ff ts=2026-10-06T16:49:51.8530000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 41 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 41} 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[12] _id=6ac3d112de269131f9adc49f ts=2026-10-05T16:32:18.4070000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[569] _id=6ac3d867de269131f9ae6ead ts=2026-10-05T17:03:35.3330000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[582] _id=6ac526b1de269131f9b563f9 ts=2026-10-06T16:49:51.8510000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[583] _id=6ac526b0de269131f9b563e9 ts=2026-10-05T17:04:40.012Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[2239] _id=6ac6741cde269131f9bc8c12 ts=2026-10-06T17:04:17.741Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[5840] _id=6ace5fffde269131f9cfb1a7 ts=2026-10-13T16:44:47.5630000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 47 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[801] _id=6ac52841de269131f9b5aab7 ts=2026-10-06T16:56:32.6650000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[803] _id=6ac52843de269131f9b5ab23 ts=2026-10-06T16:56:34.6110000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[806] _id=6ac52848de269131f9b5ac7f ts=2026-10-06T16:56:39.4280000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4017 | 0.0 | 0.064 | 215.004 | 1.551 | 518012.416 | 0.28 | 1803 | 7 |
| InputEvent | 3031 | 0.0 | 1.264 | 396.924 | 22.601 | 429331.561 | 0.15 | 57 | 14 |
| DialogueEvent | 2434 | 0.0 | 4.345 | 494.276 | 29.221 | 429347.275 | 0.12 | 724 | 12 |
| PlayerPositionEvent | 2058 | 0.0 | 10.001 | 583.951 | 10.117 | 429333.335 | 0.1 | 1 | 11 |
| argumentationNodeEvent | 734 | 0.021 | 0.577 | 1634.497 | 12.275 | 690160.957 | 0.04 | 83 | 6 |
| ObjectInterEvent | 317 | 0.0 | 10.869 | 3794.196 | 638.464 | 430986.24 | 0.02 | 9 | 17 |
| questEvent | 83 | 0.0 | 201.283 | 14492.256 | 85027.849 | 429958.593 | 0.0 | 15 | 18 |
| Soil Key Puzzle | 81 | 0.148 | 2.327 | 8522.636 | 174.27 | 518272.853 | 0.01 | 0 | 4 |
| argumentationAnswerEvent | 64 | 0.168 | 20.045 | 18744.541 | 84079.171 | 690145.721 | 0.0 | 0 | 6 |
| TopographicMapEvent | 46 | 0.023 | 4.415 | 15030.246 | 84988.898 | 431863.103 | 0.0 | 2 | 6 |
| DEBUGMenu | 41 | 9.966 | 571.144 | 29327.702 | 86167.152 | 431368.49 | 0.0 | 0 | 20 |
| gameWindowFocusEvent | 40 | 0.579 | 627.302 | 30065.764 | 94304.134 | 431383.562 | 0.0 | 0 | 20 |
| argumentationToolEvent | 32 | 0.021 | 1.236 | 37488.204 | 237707.671 | 690283.474 | 0.0 | 2 | 3 |
| gameWindowUnfocusEvent | 27 | 0.0 | 482.936 | 44469.895 | 200775.143 | 603629.822 | 0.0 | 1 | 13 |
| WaterChamberEvent | 24 | 0.846 | 16.72 | 24.713 | 56.675 | 96.301 | 2.43 | 0 | 0 |
| gameStartEvent | 19 | 181.482 | 8932.973 | 63286.688 | 267826.182 | 431383.562 | 0.0 | 0 | 17 |
| SolarStillDesignEvent | 17 | 0.641 | 1.045 | 70.781 | 238.739 | 1182.481 | 0.85 | 0 | 1 |
| argumentationEvent | 15 | 0.038 | 194.739 | 79978.291 | 382531.207 | 690137.659 | 0.0 | 2 | 6 |
| EndOfUnit | 10 | 0.153 | 441.608 | 120131.889 | 492798.122 | 690507.037 | 0.0 | 0 | 5 |
| TerasGardenBox | 9 | 0.932 | 3.227 | 6.452 | 15.813 | 17.705 | 9.3 | 0 | 0 |
| DaniEvent | 5 | 2.907 | 5.163 | 120679.828 | 431777.826 | 518500.431 | 0.0 | 0 | 2 |
| soilMachine | 4 | 6.876 | 142.922 | 126.898 | 205.113 | 214.873 | 0.47 | 0 | 0 |
| chatEvent | 3 | 950.034 | 1693.262 | 83781.857 | 224001.373 | 248702.274 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 11 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[3677] _id=6ac7c4d1de269131f9c428bd ts=2026-10-08T16:29:03.3630000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[3678] _id=6ac7c4d1de269131f9c428be ts=2026-10-08T16:29:03.3630000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[6874] _id=6acfb03cde269131f9d5a830 ts=2026-10-14T16:39:23.2930000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[6875] _id=6acfb03cde269131f9d5a831 ts=2026-10-14T16:39:23.2930000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[7932] _id=6ad0dd29de269131f9db7464 ts=2026-10-15T14:03:21.0260000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[7933] _id=6ad0dd29de269131f9db7465 ts=2026-10-15T14:03:21.0260000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 92 group(s), 151 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[762] _id=6ac52816de269131f9b59fab ts=2026-10-06T16:55:49.4200000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[758] _id=6ac52817de269131f9b59fb1 ts=2026-10-06T16:55:49.4200000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[783] _id=6ac5282fde269131f9b5a5ed ts=2026-10-06T16:56:13.3570000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[780] _id=6ac5282fde269131f9b5a5f6 ts=2026-10-06T16:56:13.3570000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[768] _id=6ac52830de269131f9b5a64d ts=2026-10-06T16:56:14.6920000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[785] _id=6ac52830de269131f9b5a653 ts=2026-10-06T16:56:14.6920000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[12598] _id=6ad62521de269131f9e9745d ts=2026-10-19T14:11:44.4210000Z == 6ab9a8e69a8420a1e6b56b25.jsonl[12599] _id=6ad62521de269131f9e9745e ts=2026-10-19T14:11:44.4210000Z`
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `153ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12897] _id=6ad62a22de269131f9e97919 ts=2026-10-19T14:29:22.418Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[12900] _id=6ad62a22de269131f9e9791c ts=2026-10-19T14:29:22.571Z`; `154ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12903] _id=6ad62a22de269131f9e9791f ts=2026-10-19T14:29:26.71Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[12906] _id=6ad62a22de269131f9e97922 ts=2026-10-19T14:29:26.864Z`; `222ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12906] _id=6ad62a22de269131f9e97922 ts=2026-10-19T14:29:26.864Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[12909] _id=6ad62a22de269131f9e97925 ts=2026-10-19T14:29:27.086Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 41 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b25.jsonl[112] _id=6ac3d26ede269131f9ade09f ts=2026-10-05T16:38:05.9950000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[111] _id=6ac3d26ede269131f9ade0a1 ts=2026-10-05T16:38:05.9990000Z`; `885ms: 6ab9a8e69a8420a1e6b56b25.jsonl[646] _id=6ac527d7de269131f9b59285 ts=2026-10-06T16:54:46.1920000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[653] _id=6ac527d8de269131f9b592c4 ts=2026-10-06T16:54:47.0770000Z`; `575ms: 6ab9a8e69a8420a1e6b56b25.jsonl[653] _id=6ac527d8de269131f9b592c4 ts=2026-10-06T16:54:47.0770000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[661] _id=6ac527d8de269131f9b59301 ts=2026-10-06T16:54:47.6520000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 211 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `598ms: 6ab9a8e69a8420a1e6b56b25.jsonl[767] _id=6ac52830de269131f9b5a646 ts=2026-10-06T16:56:14.0940000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[768] _id=6ac52830de269131f9b5a64d ts=2026-10-06T16:56:14.6920000Z`; `10ms: 6ab9a8e69a8420a1e6b56b25.jsonl[828] _id=6ac52876de269131f9b5b78d ts=2026-10-06T16:57:24.3250000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[826] _id=6ac52877de269131f9b5b7c1 ts=2026-10-06T16:57:24.3350000Z`; `258ms: 6ab9a8e69a8420a1e6b56b25.jsonl[832] _id=6ac52877de269131f9b5b7ea ts=2026-10-06T16:57:24.4950000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[829] _id=6ac52877de269131f9b5b7f1 ts=2026-10-06T16:57:24.7530000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `362ms: 6ab9a8e69a8420a1e6b56b25.jsonl[814] _id=6ac52854de269131f9b5afc7 ts=2026-10-06T16:56:51.1390000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[816] _id=6ac52854de269131f9b5afd9 ts=2026-10-06T16:56:51.5010000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `765ms: 6ab9a8e69a8420a1e6b56b25.jsonl[437] _id=6ac3d72ade269131f9ae4fbd ts=2026-10-05T16:58:18.0690000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[444] _id=6ac3d72bde269131f9ae4fc9 ts=2026-10-05T16:58:18.8340000Z`; `180ms: 6ab9a8e69a8420a1e6b56b25.jsonl[444] _id=6ac3d72bde269131f9ae4fc9 ts=2026-10-05T16:58:18.8340000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[445] _id=6ac3d72bde269131f9ae4fcb ts=2026-10-05T16:58:19.0140000Z`; `875ms: 6ab9a8e69a8420a1e6b56b25.jsonl[445] _id=6ac3d72bde269131f9ae4fcb ts=2026-10-05T16:58:19.0140000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[447] _id=6ac3d72cde269131f9ae4fe5 ts=2026-10-05T16:58:19.8890000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `47ms: 6ab9a8e69a8420a1e6b56b25.jsonl[6718] _id=6acfaf06de269131f9d58d6d ts=2026-10-14T16:34:13.5250000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[6721] _id=6acfaf06de269131f9d58d70 ts=2026-10-14T16:34:13.5720000Z`; `38ms: 6ab9a8e69a8420a1e6b56b25.jsonl[11236] _id=6ad2510dde269131f9e5e0b6 ts=2026-10-16T16:30:04.5520000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[11244] _id=6ad2510dde269131f9e5e0bc ts=2026-10-16T16:30:04.5900000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 44 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6ab9a8e69a8420a1e6b56b25.jsonl[375] _id=6ac3d6a3de269131f9ae42bc ts=2026-10-05T16:56:02.3610000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[382] _id=6ac3d6a3de269131f9ae42c3 ts=2026-10-05T16:56:02.3960000Z`; `441ms: 6ab9a8e69a8420a1e6b56b25.jsonl[5744] _id=6ace5f58de269131f9cfa684 ts=2026-10-13T16:42:00.3330000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[5747] _id=6ace5f59de269131f9cfa699 ts=2026-10-13T16:42:00.7740000Z`; `949ms: 6ab9a8e69a8420a1e6b56b25.jsonl[5768] _id=6ace5f82de269131f9cfa982 ts=2026-10-13T16:42:42.1320000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[5769] _id=6ace5f83de269131f9cfa9b4 ts=2026-10-13T16:42:43.0810000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `780ms: 6ab9a8e69a8420a1e6b56b25.jsonl[415] _id=6ac3d705de269131f9ae4c81 ts=2026-10-05T16:57:41.2020000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[417] _id=6ac3d706de269131f9ae4c9d ts=2026-10-05T16:57:41.9820000Z`; `759ms: 6ab9a8e69a8420a1e6b56b25.jsonl[411] _id=6ac3d705de269131f9ae4c87 ts=2026-10-05T16:57:41.2800000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[412] _id=6ac3d706de269131f9ae4ca3 ts=2026-10-05T16:57:42.0390000Z`; `766ms: 6ab9a8e69a8420a1e6b56b25.jsonl[417] _id=6ac3d706de269131f9ae4c9d ts=2026-10-05T16:57:41.9820000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[418] _id=6ac3d707de269131f9ae4cad ts=2026-10-05T16:57:42.7480000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `599ms: 6ab9a8e69a8420a1e6b56b25.jsonl[7999] _id=6ad0f7f8de269131f9dcf9d5 ts=2026-10-15T15:57:44.1470000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[8014] _id=6ad0f7f9de269131f9dcf9e6 ts=2026-10-15T15:57:44.7460000Z`; `651ms: 6ab9a8e69a8420a1e6b56b25.jsonl[8014] _id=6ad0f7f9de269131f9dcf9e6 ts=2026-10-15T15:57:44.7460000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[8015] _id=6ad0f7fade269131f9dcfa00 ts=2026-10-15T15:57:45.3970000Z`; `579ms: 6ab9a8e69a8420a1e6b56b25.jsonl[8015] _id=6ad0f7fade269131f9dcfa00 ts=2026-10-15T15:57:45.3970000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[8013] _id=6ad0f7fade269131f9dcfa0f ts=2026-10-15T15:57:45.9760000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[6864] _id=6acfb017de269131f9d5a389 ts=2026-10-14T16:38:47.0170000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[6868] _id=6acfb026de269131f9d5a552 ts=2026-10-14T16:38:47.017Z`; `702ms: 6ab9a8e69a8420a1e6b56b25.jsonl[8016] _id=6ad0f7f8de269131f9dcf9c5 ts=2026-10-15T15:57:43.6720000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[8017] _id=6ad0f7f9de269131f9dcf9dc ts=2026-10-15T15:57:44.3740000Z`; `566ms: 6ab9a8e69a8420a1e6b56b25.jsonl[8017] _id=6ad0f7f9de269131f9dcf9dc ts=2026-10-15T15:57:44.3740000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[8008] _id=6ad0f7f9de269131f9dcf9f6 ts=2026-10-15T15:57:44.9400000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12747] _id=6ad62701de269131f9e976ca ts=2026-10-19T14:19:44.1200000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[12748] _id=6ad62701de269131f9e976cc ts=2026-10-19T14:19:44.1240000Z`; `6ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12806] _id=6ad62a34de269131f9e97933 ts=2026-10-19T14:33:23.6200000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[12807] _id=6ad62a34de269131f9e97934 ts=2026-10-19T14:33:23.6260000Z`; `4ms: 6ab9a8e69a8420a1e6b56b25.jsonl[13043] _id=6ad62ba0de269131f9e97b19 ts=2026-10-19T14:39:27.1180000Z ~ 6ab9a8e69a8420a1e6b56b25.jsonl[13044] _id=6ad62ba0de269131f9e97b1b ts=2026-10-19T14:39:27.1220000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8e69a8420a1e6b56b25.jsonl[3672] _id=6ac7c4cdde269131f9c42875 ts=2026-10-08T16:28:59.9330000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5187] _id=6ace59d4de269131f9cf58e7 ts=2026-10-13T16:18:28.4230000Z; 69h 20m: 6ab9a8e69a8420a1e6b56b25.jsonl[11602] _id=6ad25462de269131f9e60e06 ts=2026-10-16T16:44:14.8690000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12285] _id=6ad6238ade269131f9e97181 ts=2026-10-19T14:04:57.7170000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b25.jsonl[2244] _id=6ac67427de269131f9bc8cee ts=2026-10-07T16:32:37.8770000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3669] _id=6ac7c4bede269131f9c42707 ts=2026-10-08T16:28:45.0290000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 1m 
  - Evidence: 144h 1m: 6ab9a8e69a8420a1e6b56b25.jsonl[3628] _id=6ac67b10de269131f9bd82d2 ts=2026-10-07T17:02:07.7690000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6169] _id=6ace6474de269131f9d00d8b ts=2026-10-13T17:03:48.2000000Z; 23h 34m: 6ab9a8e69a8420a1e6b56b25.jsonl[6171] _id=6ace6477de269131f9d00ddb ts=2026-10-13T17:03:51.4330000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6862] _id=6acfb00fde269131f9d5a257 ts=2026-10-14T16:38:38.8390000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b25.jsonl[5180] _id=6ac7cccfde269131f9c4dc73 ts=2026-10-08T17:03:10.5190000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5197] _id=6ace59f1de269131f9cf592b ts=2026-10-13T16:18:57.7940000Z; 69h 0m: 6ab9a8e69a8420a1e6b56b25.jsonl[12183] _id=6ad25927de269131f9e660f9 ts=2026-10-16T17:04:38.4850000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12311] _id=6ad623afde269131f9e971b3 ts=2026-10-19T14:05:34.7160000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b25.jsonl[576] _id=6ac3d881de269131f9ae70bf ts=2026-10-05T17:04:00.6240000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[587] _id=6ac526c0de269131f9b56603 ts=2026-10-06T16:50:07.9880000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 724 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10180] _id=6ad1070cde269131f9de3958 ts=2026-10-15T17:02:04.1670000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10181] _id=6ad1070cde269131f9de3959 ts=2026-10-15T17:02:04.1670000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10277] _id=6ad1078cde269131f9de45ae ts=2026-10-15T17:04:12.1610000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10278] _id=6ad1078cde269131f9de45af ts=2026-10-15T17:04:12.1610000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10706] _id=6ad22d36de269131f9e43c42 ts=2026-10-16T13:57:09.1320000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10707] _id=6ad22d36de269131f9e43c43 ts=2026-10-16T13:57:09.1320000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 6ab9a8e69a8420a1e6b56b25.jsonl[568] _id=6ac3d80fde269131f9ae67f9 ts=2026-10-05T17:02:07.2770000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5927] _id=6ace615ade269131f9cfcade ts=2026-10-13T16:50:34.3140000Z; 69h 45m: 6ab9a8e69a8420a1e6b56b25.jsonl[11591] _id=6ad25430de269131f9e60b8f ts=2026-10-16T16:43:27.0960000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12893] _id=6ad62a22de269131f9e97915 ts=2026-10-19T14:29:20.988Z; 45h 16m: 6ab9a8e69a8420a1e6b56b25.jsonl[5927] _id=6ace615ade269131f9cfcade ts=2026-10-13T16:50:34.3140000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[7988] _id=6ad0ddf8de269131f9db80d1 ts=2026-10-15T14:06:48.2530000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b25.jsonl[5182] _id=6ac7ccd4de269131f9c4dcad ts=2026-10-08T17:03:14.9430000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5189] _id=6ace59e8de269131f9cf5902 ts=2026-10-13T16:18:46.5040000Z; 69h 0m: 6ab9a8e69a8420a1e6b56b25.jsonl[12267] _id=6ad2590cde269131f9e65fe4 ts=2026-10-16T17:04:11.5280000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12299] _id=6ad62397de269131f9e9718b ts=2026-10-19T14:05:09.9070000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b25.jsonl[574] _id=6ac3d879de269131f9ae7031 ts=2026-10-05T17:03:52.2710000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[593] _id=6ac526cfde269131f9b56783 ts=2026-10-06T16:50:22.5020000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 57 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12142] _id=6ad257b2de269131f9e64ba8 ts=2026-10-16T16:58:25.0300000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12143] _id=6ad257b2de269131f9e64ba9 ts=2026-10-16T16:58:25.0300000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[3038] _id=6ac675c0de269131f9bcd67b ts=2026-10-07T16:39:26.9050000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3039] _id=6ac675c0de269131f9bcd67c ts=2026-10-07T16:39:26.9050000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[3677] _id=6ac7c4d1de269131f9c428bd ts=2026-10-08T16:29:03.3630000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3678] _id=6ac7c4d1de269131f9c428be ts=2026-10-08T16:29:03.3630000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8e69a8420a1e6b56b25.jsonl[4826] _id=6ac7c8b7de269131f9c49980 ts=2026-10-08T16:45:42.0810000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5354] _id=6ace5c40de269131f9cf70d1 ts=2026-10-13T16:28:48.3210000Z; 69h 1m: 6ab9a8e69a8420a1e6b56b25.jsonl[12270] _id=6ad2590ede269131f9e6600f ts=2026-10-16T17:04:13.0880000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12315] _id=6ad623b6de269131f9e971c2 ts=2026-10-19T14:05:41.4760000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b25.jsonl[3260] _id=6ac67655de269131f9bcef8d ts=2026-10-07T16:41:56.0390000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3901] _id=6ac7c6e6de269131f9c46858 ts=2026-10-08T16:37:57.4570000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10017] _id=6ad10602de269131f9de1e5c ts=2026-10-15T16:57:38.4170000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10018] _id=6ad10602de269131f9de1e5d ts=2026-10-15T16:57:38.4170000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10091] _id=6ad10661de269131f9de2862 ts=2026-10-15T16:59:12.9730000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10092] _id=6ad10661de269131f9de2863 ts=2026-10-15T16:59:12.9730000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10489] _id=6ad22b8ede269131f9e40e87 ts=2026-10-16T13:50:04.9470000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10490] _id=6ad22b8ede269131f9e40e88 ts=2026-10-16T13:50:04.9470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b25.jsonl[5179] _id=6ac7cccdde269131f9c4dc43 ts=2026-10-08T17:03:08.0910000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5188] _id=6ace59e8de269131f9cf5901 ts=2026-10-13T16:18:41.4260000Z; 69h 0m: 6ab9a8e69a8420a1e6b56b25.jsonl[12182] _id=6ad25925de269131f9e660e9 ts=2026-10-16T17:04:36.6760000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12297] _id=6ad62397de269131f9e97189 ts=2026-10-19T14:05:07.1130000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b25.jsonl[580] _id=6ac3d8a1de269131f9ae7313 ts=2026-10-05T17:04:32.4620000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[586] _id=6ac526bfde269131f9b565e3 ts=2026-10-06T16:50:02.6110000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[2232] _id=6ac52a12de269131f9b609dd ts=2026-10-06T17:04:17.4410000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[2238] _id=6ac6741cde269131f9bc8c11 ts=2026-10-06T17:04:17.441Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 53m 
  - Evidence: 143h 53m: 6ab9a8e69a8420a1e6b56b25.jsonl[4952] _id=6ac7c977de269131f9c4a989 ts=2026-10-08T16:48:52.8000000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6963] _id=6acfb0f3de269131f9d5b516 ts=2026-10-14T16:42:25.2160000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b25.jsonl[3225] _id=6ac675f9de269131f9bce1ab ts=2026-10-07T16:40:22.7760000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3960] _id=6ac7c766de269131f9c4773f ts=2026-10-08T16:40:04.2600000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b25.jsonl[9844] _id=6ad10463de269131f9ddf01d ts=2026-10-15T16:50:41.7210000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[11594] _id=6ad25467de269131f9e60e40 ts=2026-10-16T16:44:21.3150000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1803 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[1012] _id=6ac5289dde269131f9b5c22b ts=2026-10-06T16:58:02.4840000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[1008] _id=6ac5289ede269131f9b5c23b ts=2026-10-06T16:58:02.4840000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[1061] _id=6ac528b1de269131f9b5c631 ts=2026-10-06T16:58:22.7050000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[1077] _id=6ac528b1de269131f9b5c635 ts=2026-10-06T16:58:22.7050000Z; 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[1079] _id=6ac528cfde269131f9b5cd48 ts=2026-10-06T16:58:52.5540000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[1197] _id=6ac528cfde269131f9b5cd55 ts=2026-10-06T16:58:52.5540000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 6ab9a8e69a8420a1e6b56b25.jsonl[3954] _id=6ac7c75dde269131f9c47647 ts=2026-10-08T16:39:56.6620000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6850] _id=6acfafddde269131f9d59e53 ts=2026-10-14T16:37:49.5150000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b25.jsonl[3261] _id=6ac67658de269131f9bcefe7 ts=2026-10-07T16:41:58.9950000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3898] _id=6ac7c6e6de269131f9c46850 ts=2026-10-08T16:37:57.4510000Z; 23h 23m: 6ab9a8e69a8420a1e6b56b25.jsonl[6945] _id=6acfb0c9de269131f9d5b2d4 ts=2026-10-14T16:41:45.0240000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[8127] _id=6ad0f9d0de269131f9dd2e57 ts=2026-10-15T16:05:36.0270000Z
- **INFO / Info** `SolarStillDesignEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 19m 42s 
  - Evidence: 19m 42s: 6ab9a8e69a8420a1e6b56b25.jsonl[12700] _id=6ad626b6de269131f9e9760c ts=2026-10-19T14:18:29.8050000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12980] _id=6ad62b55de269131f9e97a1d ts=2026-10-19T14:38:12.2860000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 57m 
  - Evidence: 119h 57m: 6ab9a8e69a8420a1e6b56b25.jsonl[5176] _id=6ac7ccbbde269131f9c4db36 ts=2026-10-08T17:02:50.5470000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6079] _id=6ace63b1de269131f9cff538 ts=2026-10-13T17:00:33.6500000Z; 23h 58m: 6ab9a8e69a8420a1e6b56b25.jsonl[6070] _id=6ace63bdde269131f9cff673 ts=2026-10-13T17:00:45.7520000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[7801] _id=6acfb4fcde269131f9d62439 ts=2026-10-14T16:59:39.7260000Z; 23h 38m: 6ab9a8e69a8420a1e6b56b25.jsonl[818] _id=6ac52855de269131f9b5b07f ts=2026-10-06T16:56:52.8710000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[2354] _id=6ac674e4de269131f9bca3fd ts=2026-10-07T16:35:47.6860000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.047s shown 
  - Evidence: 23ms: 6ab9a8e69a8420a1e6b56b25.jsonl[3432] _id=6ac6786cde269131f9bd3cf0 ts=2026-10-07T16:50:50.7990000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3436] _id=6ac6786cde269131f9bd3cf4 ts=2026-10-07T16:50:50.8220000Z; 47ms: 6ab9a8e69a8420a1e6b56b25.jsonl[3437] _id=6ac6786bde269131f9bd3cee ts=2026-10-07T16:50:50.7520000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3432] _id=6ac6786cde269131f9bd3cf0 ts=2026-10-07T16:50:50.7990000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 6ab9a8e69a8420a1e6b56b25.jsonl[465] _id=6ac3d74ade269131f9ae52c1 ts=2026-10-05T16:58:50.0480000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5619] _id=6ace5f2bde269131f9cfa2c0 ts=2026-10-13T16:41:15.7690000Z; 69h 38m: 6ab9a8e69a8420a1e6b56b25.jsonl[11243] _id=6ad2510dde269131f9e5e0b2 ts=2026-10-16T16:30:04.5290000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12444] _id=6ad6247bde269131f9e972d7 ts=2026-10-19T14:08:58.0200000Z; 24h 27m: 6ab9a8e69a8420a1e6b56b25.jsonl[6710] _id=6acfaf05de269131f9d58d69 ts=2026-10-14T16:34:13.5110000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10178] _id=6ad1070cde269131f9de3956 ts=2026-10-15T17:02:04.1520000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 6ab9a8e69a8420a1e6b56b25.jsonl[466] _id=6ac3d74ade269131f9ae52c3 ts=2026-10-05T16:58:50.0680000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5714] _id=6ace5f23de269131f9cfa233 ts=2026-10-13T16:41:07.7270000Z; 69h 38m: 6ab9a8e69a8420a1e6b56b25.jsonl[11244] _id=6ad2510dde269131f9e5e0bc ts=2026-10-16T16:30:04.5900000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12404] _id=6ad62459de269131f9e9726c ts=2026-10-19T14:08:24.4610000Z; 24h 27m: 6ab9a8e69a8420a1e6b56b25.jsonl[6721] _id=6acfaf06de269131f9d58d70 ts=2026-10-14T16:34:13.5720000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10161] _id=6ad106f9de269131f9de3739 ts=2026-10-15T17:01:45.0200000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.038s..0.047s shown 
  - Evidence: 38ms: 6ab9a8e69a8420a1e6b56b25.jsonl[11236] _id=6ad2510dde269131f9e5e0b6 ts=2026-10-16T16:30:04.5520000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[11244] _id=6ad2510dde269131f9e5e0bc ts=2026-10-16T16:30:04.5900000Z; 47ms: 6ab9a8e69a8420a1e6b56b25.jsonl[6718] _id=6acfaf06de269131f9d58d6d ts=2026-10-14T16:34:13.5250000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6721] _id=6acfaf06de269131f9d58d70 ts=2026-10-14T16:34:13.5720000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 6ab9a8e69a8420a1e6b56b25.jsonl[443] _id=6ac3d742de269131f9ae51df ts=2026-10-05T16:58:42.2600000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5712] _id=6ace5f33de269131f9cfa33c ts=2026-10-13T16:41:23.2170000Z; 69h 38m: 6ab9a8e69a8420a1e6b56b25.jsonl[11240] _id=6ad2510cde269131f9e5e09b ts=2026-10-16T16:30:03.0130000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12327] _id=6ad6245bde269131f9e97271 ts=2026-10-19T14:08:26.2900000Z; 24h 27m: 6ab9a8e69a8420a1e6b56b25.jsonl[6715] _id=6acfaf04de269131f9d58d4f ts=2026-10-14T16:34:11.8760000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10164] _id=6ad106fcde269131f9de377d ts=2026-10-15T17:01:47.5140000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 83 interval(s) ≤ 0.021s..0.022s shown 
  - Evidence: 21ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10660] _id=6ad22cf4de269131f9e43687 ts=2026-10-16T13:56:03.2110000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[10657] _id=6ad22cf4de269131f9e4368b ts=2026-10-16T13:56:03.2320000Z; 22ms: 6ab9a8e69a8420a1e6b56b25.jsonl[10999] _id=6ad24fb5de269131f9e5cb0e ts=2026-10-16T16:24:20.3130000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[11000] _id=6ad24fb6de269131f9e5cb1c ts=2026-10-16T16:24:20.3350000Z; 22ms: 6ab9a8e69a8420a1e6b56b25.jsonl[11030] _id=6ad24fe6de269131f9e5cdbc ts=2026-10-16T16:25:09.1480000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[11017] _id=6ad24fe6de269131f9e5cdbe ts=2026-10-16T16:25:09.1700000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 44m 
  - Evidence: 191h 44m: 6ab9a8e69a8420a1e6b56b25.jsonl[418] _id=6ac3d707de269131f9ae4cad ts=2026-10-05T16:57:42.7480000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5760] _id=6ace5f72de269131f9cfa846 ts=2026-10-13T16:42:26.2220000Z; 117h 35m: 6ab9a8e69a8420a1e6b56b25.jsonl[6706] _id=6acfaeefde269131f9d58bb7 ts=2026-10-14T16:33:50.6170000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12465] _id=6ad62498de269131f9e97326 ts=2026-10-19T14:09:27.1250000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b25.jsonl[5763] _id=6ace5f76de269131f9cfa884 ts=2026-10-13T16:42:30.5610000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6664] _id=6acfaebcde269131f9d587d8 ts=2026-10-14T16:33:00.0930000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.050s shown 
  - Evidence: 21ms: 6ab9a8e69a8420a1e6b56b25.jsonl[408] _id=6ac3d701de269131f9ae4c1f ts=2026-10-05T16:57:37.0720000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[404] _id=6ac3d701de269131f9ae4c23 ts=2026-10-05T16:57:37.0930000Z; 50ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12481] _id=6ad6249bde269131f9e97330 ts=2026-10-19T14:09:30.1030000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12482] _id=6ad6249bde269131f9e97332 ts=2026-10-19T14:09:30.1530000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 69h 5m 
  - Evidence: 69h 5m: 6ab9a8e69a8420a1e6b56b25.jsonl[12185] _id=6ad25815de269131f9e65232 ts=2026-10-16T17:00:04.7110000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12288] _id=6ad62394de269131f9e97187 ts=2026-10-19T14:05:06.9850000Z; 28m 13s: 6ab9a8e69a8420a1e6b56b25.jsonl[12288] _id=6ad62394de269131f9e97187 ts=2026-10-19T14:05:06.9850000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12915] _id=6ad62a31de269131f9e97930 ts=2026-10-19T14:33:20.2470000Z; 15m 50s: 6ab9a8e69a8420a1e6b56b25.jsonl[11593] _id=6ad2545fde269131f9e60dde ts=2026-10-16T16:44:14.6770000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12185] _id=6ad25815de269131f9e65232 ts=2026-10-16T17:00:04.7110000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8e69a8420a1e6b56b25.jsonl[3671] _id=6ac7c4bede269131f9c4270a ts=2026-10-08T16:28:45.1860000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5185] _id=6ace59d4de269131f9cf58ea ts=2026-10-13T16:18:28.7480000Z; 69h 20m: 6ab9a8e69a8420a1e6b56b25.jsonl[11413] _id=6ad25455de269131f9e60d59 ts=2026-10-16T16:44:04.7180000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12287] _id=6ad6238ade269131f9e97183 ts=2026-10-19T14:04:57.8580000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b25.jsonl[2242] _id=6ac6741cde269131f9bc8c19 ts=2026-10-07T16:32:27.1250000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3671] _id=6ac7c4bede269131f9c4270a ts=2026-10-08T16:28:45.1860000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8e69a8420a1e6b56b25.jsonl[3670] _id=6ac7c4bede269131f9c42709 ts=2026-10-08T16:28:45.1860000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5184] _id=6ace59d4de269131f9cf58e9 ts=2026-10-13T16:18:28.7480000Z; 69h 4m: 6ab9a8e69a8420a1e6b56b25.jsonl[12181] _id=6ad2580fde269131f9e651ee ts=2026-10-16T16:59:58.3350000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12286] _id=6ad6238ade269131f9e97182 ts=2026-10-19T14:04:57.8580000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b25.jsonl[2241] _id=6ac6741cde269131f9bc8c18 ts=2026-10-07T16:32:27.1250000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[3670] _id=6ac7c4bede269131f9c42709 ts=2026-10-08T16:28:45.1860000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 167h 40m 
  - Evidence: 167h 40m: 6ab9a8e69a8420a1e6b56b25.jsonl[2239] _id=6ac6741cde269131f9bc8c12 ts=2026-10-06T17:04:17.741Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5840] _id=6ace5fffde269131f9cfb1a7 ts=2026-10-13T16:44:47.5630000Z; 69h 23m: 6ab9a8e69a8420a1e6b56b25.jsonl[12284] _id=6ad6238ade269131f9e9717f ts=2026-10-16T17:04:41.642Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12870] _id=6ad62a22de269131f9e978fd ts=2026-10-19T14:28:04.248Z; 23h 59m: 6ab9a8e69a8420a1e6b56b25.jsonl[583] _id=6ac526b0de269131f9b563e9 ts=2026-10-05T17:04:40.012Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[2239] _id=6ac6741cde269131f9bc8c12 ts=2026-10-06T17:04:17.741Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[6864] _id=6acfb017de269131f9d5a389 ts=2026-10-14T16:38:47.0170000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[6868] _id=6acfb026de269131f9d5a552 ts=2026-10-14T16:38:47.017Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a8e69a8420a1e6b56b25.jsonl[5027] _id=6ac7ca61de269131f9c4b2eb ts=2026-10-08T16:52:47.9600000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[5190] _id=6ace59e8de269131f9cf5903 ts=2026-10-13T16:18:46.5530000Z; 69h 2m: 6ab9a8e69a8420a1e6b56b25.jsonl[12226] _id=6ad258a6de269131f9e659e3 ts=2026-10-16T17:02:29.6690000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12298] _id=6ad62397de269131f9e9718a ts=2026-10-19T14:05:09.6890000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b25.jsonl[548] _id=6ac3d7e6de269131f9ae634f ts=2026-10-05T17:01:26.3680000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[609] _id=6ac52711de269131f9b570a1 ts=2026-10-06T16:51:28.3380000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12598] _id=6ad62521de269131f9e9745d ts=2026-10-19T14:11:44.4210000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12599] _id=6ad62521de269131f9e9745e ts=2026-10-19T14:11:44.4210000Z; 2ms: 6ab9a8e69a8420a1e6b56b25.jsonl[349] _id=6ac3d63fde269131f9ae372d ts=2026-10-05T16:54:22.3820000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[345] _id=6ac3d63fde269131f9ae3737 ts=2026-10-05T16:54:22.3840000Z; 4ms: 6ab9a8e69a8420a1e6b56b25.jsonl[12747] _id=6ad62701de269131f9e976ca ts=2026-10-19T14:19:44.1200000Z -> 6ab9a8e69a8420a1e6b56b25.jsonl[12748] _id=6ad62701de269131f9e976cc ts=2026-10-19T14:19:44.1240000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[341] _id=6ac3d637de269131f9ae35ad ts=2026-10-05T16:54:14.9990000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[473] _id=6ac3d764de269131f9ae55a5 ts=2026-10-05T16:59:15.5870000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[3560] _id=6ac67a6cde269131f9bd6f62 ts=2026-10-07T16:59:23.7320000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 20 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[1044] _id=6ac528a7de269131f9b5c3e5 ts=2026-10-06T16:58:12.5080000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[1042] _id=6ac528a7de269131f9b5c3ec ts=2026-10-06T16:58:12.6850000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[1043] _id=6ac528a7de269131f9b5c3f1 ts=2026-10-06T16:58:12.8890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 97 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[759] _id=6ac52817de269131f9b59fbc ts=2026-10-06T16:55:49.6740000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[786] _id=6ac52830de269131f9b5a65d ts=2026-10-06T16:56:14.6920000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[789] _id=6ac52830de269131f9b5a663 ts=2026-10-06T16:56:14.6920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[6721] _id=6acfaf06de269131f9d58d70 ts=2026-10-14T16:34:13.5720000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[382] _id=6ac3d6a3de269131f9ae42c3 ts=2026-10-05T16:56:02.3960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[11593] _id=6ad2545fde269131f9e60dde ts=2026-10-16T16:44:14.6770000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[12185] _id=6ad25815de269131f9e65232 ts=2026-10-16T17:00:04.7110000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[12288] _id=6ad62394de269131f9e97187 ts=2026-10-19T14:05:06.9850000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[9188] _id=6ad10000de269131f9dd9886 ts=2026-10-15T16:31:59.6940000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[592] _id=6ac526cade269131f9b56725 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 249 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[1035] _id=6ac528afde269131f9b5c5c9 ts=2026-10-06T16:58:21.7780000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[1145] _id=6ac528bede269131f9b5c9dd ts=2026-10-06T16:58:36.9880000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[1150] _id=6ac528c0de269131f9b5ca71 ts=2026-10-06T16:58:38.9270000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 710 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[758] _id=6ac52817de269131f9b59fb1 ts=2026-10-06T16:55:49.4200000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[769] _id=6ac52825de269131f9b5a394 ts=2026-10-06T16:56:03.6310000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[870] _id=6ac52886de269131f9b5bc54 ts=2026-10-06T16:56:03.8930000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[10580] _id=6ad22c5ade269131f9e42538 ts=2026-10-16T13:53:29.8530000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[10875] _id=6ad24f19de269131f9e5c03c ts=2026-10-16T16:21:43.9500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[407] _id=6ac3d6ffde269131f9ae4bed ts=2026-10-05T16:57:35.0840000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[404] _id=6ac3d701de269131f9ae4c23 ts=2026-10-05T16:57:37.0930000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[410] _id=6ac3d703de269131f9ae4c47 ts=2026-10-05T16:57:38.6350000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'DialogueStartEvent' (totals: 474 start, 462 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 36 unmatched 'BecameCameraCentered' (totals: 723 open, 707 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 93 unmatched 'BecameVisible' (totals: 1292 open, 1296 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 8 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 15 unmatched 'argumentationToolOpen' (totals: 24 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 50 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 390 of 13146 adjacent _id pairs reverse in client time; worst 95.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b25.jsonl[871] _id=6ac52883de269131f9b5bbc2 ts=2026-10-06T16:57:38.9480000Z`; `6ab9a8e69a8420a1e6b56b25.jsonl[873] _id=6ac52884de269131f9b5bbf1 ts=2026-10-06T16:56:03.8080000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.14s, min -248417.14s, max -0.11s over 13147 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b25\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4018 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2728); Unit 4 Dev (804); Unit 3 Dungeon Dev (292); Unit 5 Dev - Dungeon (194)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.55s, n=4017)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4018/4018 records)
    "BecameInvisible"  x1296
    "BecameVisible"  x1292
    "BecameCameraCentered"  x723
    "BecameCameraUncentered"  x707
data.pieceId  (string, 4018/4018 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4018/4018 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3032 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1003); Unit 3 Dev (497); Unit 4 Dev - Dungeon (338); Unit 4 Dev (278); Unit 3 Dungeon Dev (267); Unit 4 Dev - Anderson Base (235); Unit 5 Dev - Dungeon (172); Unit 5 Dev (156); Unit 1 Dev (86)
- **Intervals:** median 1.26s (p5 0.15s / p95 22.60s, n=3031)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3032/3032 records)
    "pressed"  x3032
data.actionType  (string, 3032/3032 records)
    "Move"  x2027
    "Interact"  x535
    "Jump"  x287
    "Ascend"  x89
    "Sprint"  x53
    "Hoverboard"  x34
    "Descend"  x3
    "Pause"  x3
    "SkipCinematic"  x1
data.key  (string, 3032/3032 records)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3032/3032 records)
    "Player"  x2335
    "Drone"  x697
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2435 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (635); Unit 5 Dev (359); Unit 4 Dev - Anderson Base (338); Unit 3 Dev (331); Unit 4 Dev (283); Unit 1 Dev (207); Unit 3 Dungeon Dev (116); Unit 4 Dev - Dungeon (91); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1499 of 2435 records
- **Intervals:** median 4.35s (p5 0.00s / p95 29.22s, n=2434)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1499; [conversationId, dialogueEventType] x936
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2435/2435 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2435/2435 records)
    "DialogueNodeEvent"  x1499
    "DialogueStartEvent"  x474
    "DialogueFinishEvent"  x462
data.nodeId  (number, 1499/2435 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2072 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (673); Unit 3 Dev (258); Unit 5 Dev (236); Unit 4 Dev - Anderson Base (220); Unit 4 Dev (208); Unit 1 Dev (178); Unit 4 Dev - Dungeon (111); Unit 3 Dungeon Dev (95); Unit 5 Dev - Dungeon (93)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=2058)
- **Fields under `data`:**

```text
data.position  (object, 2072/2072 records)
data.position.x  (number, 2072/2072 records)
    numeric range -694.321 .. 1558.89 (619 unique)
data.position.y  (number, 2072/2072 records)
    numeric range -856.417 .. 222.011 (467 unique)
data.position.z  (number, 2072/2072 records)
    numeric range -1034.66 .. 2195.77 (619 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 735 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (403); Unit 5 Dev (132); Unit 2 Prod (Refactor) (83); Unit 3 Dev (81); Unit 1 Dev (36)
- **Intervals:** median 0.58s (p5 0.04s / p95 12.28s, n=734)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 735/735 records)
    "argumentationNodeHoverEnd"  x309
    "argumentationNodeHoverStart"  x308
    "argumentationNodeAdd"  x72
    "argumentationNodeRemove"  x46
data.argumentationTitle  (string, 735/735 records)
    "Unit 4 - Flooding"  x403
    "Unit 5"  x132
    "Unit 2 – Watershed"  x83
    "Unit 3 - Pollution Upstream"  x81
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x11
data.nodeName  (string, 735/735 records)
    "B"  x99
    "A"  x87
    "C"  x83
    "2"  x79
    "1"  x75
    "3"  x75
    "D"  x74
    "I"  x63
    "II"  x55
    "4"  x38
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 318 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (105); Unit 4 Dev - Dungeon (63); Unit 4 Dev - Anderson Base (36); Unit 3 Dungeon Dev (32); Unit 4 Dev (25); Unit 5 Dev (19); Unit 5 Dev - Dungeon (16); Unit 3 Dev (12); Unit 1 Dev (10)
- **Intervals:** median 10.87s (p5 0.18s / p95 638.46s, n=317)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 318/318 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 318/318 records)
    105 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (13); Unit 5 Dev (13); Unit 1 Dev (12); Unit 4 Dev (9); Unit 4 Dev - Dungeon (8); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 201.28s (p5 0.00s / p95 85027.85s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x34
data.questID  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/84 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 82 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (46); Unit 4 Dev (22); Unit 3 Dev (14)
- **Intervals:** median 2.33s (p5 0.16s / p95 174.27s, n=81)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x70; [Soil Key Puzzle Status, Unit] x12
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/82 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/82 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x4
    "Unit 4 Dev"  x4
data.actionType  (string, 70/82 records)
    "RightDrag"  x39
    "LeftDrag"  x31
data.currentSoilType  (string, 70/82 records)
    "CLAYSAND"  x17
    "CLAY"  x14
    "SAND"  x14
    "SANDGRAVEL"  x11
    "CLAYROCK"  x7
    "GRAVEL"  x6
    "BEDROCK"  x1
data.isCorrectSelection  (string, 70/82 records)
    "false"  x49
    "true"  x21
data.waterLevelStatus  (string, 70/82 records)
    "Proper"  x26
    "TooLow"  x24
    "TooHigh"  x20
data.waterRetentionChange  (string, 70/82 records)
    "Increase"  x25
    "Decrease"  x24
    "NoChange"  x21
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 65 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (41); Unit 1 Dev (9); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 5 Dev (5)
- **Intervals:** median 20.05s (p5 0.28s / p95 84079.17s, n=64)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 65/65 records)
    "submitAnswerEvent"  x65
data.answerSubmitted  (string, 65/65 records)
    28 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 65/65 records)
    "Unit 4 - Flooding"  x41
    "Unit 1 - Freshwater"  x8
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 47 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (41); Unit 3 Dev (6)
- **Intervals:** median 4.41s (p5 0.43s / p95 84988.90s, n=46)
- **`data` key-set variants:** [actionType, featureUsed, location] x23; [actionType, featureUsed] x22; [actionType, featureUsed, legendName] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "WaypointMoveEvent"  x20
    "MapCloseEvent"  x11
    "MapOpenEvent"  x11
    "WaypointSetEvent"  x3
    "Selected"  x2
data.featureUsed  (string, 47/47 records)
    "Waypoint"  x23
    "Map"  x22
    "Legend"  x2
data.legendName  (string, 2/47 records)
    "120 ft"  x1
    "180 ft"  x1
data.location  (object, 23/47 records)
data.location.x  (number, 23/47 records)
    numeric range -323.629 .. 122.043 (19 unique)
data.location.y  (number, 23/47 records)
    numeric range -16.0316 .. 378.382 (20 unique)
data.location.z  (number, 23/47 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 42 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 4 Dev (6); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev - Anderson Base (4); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 571.14s (p5 10.31s / p95 86167.15s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "DebugMenuStateChanged"  x42
data.isOpened  (bool, 42/42 records)
    false  x42
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 41 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21); Unit 4 Dev (8); Transition (5); Unit 3 Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 627.30s (p5 0.65s / p95 94304.13s, n=40)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 41/41 records)
    true  x41
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationToolEvent` — 33 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (15); Unit 3 Dev (9); Unit 5 Dev (6); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 1.24s (p5 0.05s / p95 237707.67s, n=32)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "argumentationToolOpen"  x24
    "argumentationToolClose"  x9
data.argumentationTitle  (string, 33/33 records)
    "Unit 1 - Freshwater"  x13
    "Unit 3 - Pollution Upstream"  x9
    "Unit 5"  x6
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 33/33 records)
    "BackingInfoPanel - "  x13
    "BackingInfoPanel - Pollution Site Data"  x6
    "BackingInfoPanel - Heat Added/Released Chart"  x5
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 28 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (8); Unit 3 Dev (6); Transition (5); Unit 2 Prod (Refactor) (3); Unit 5 Dev (3); Unit 4 Dev - Dungeon (2); MainMenu (1)
- **Intervals:** median 482.94s (p5 0.52s / p95 200775.14s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `WaterChamberEvent` — 25 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (25)
- **Intervals:** median 16.72s (p5 3.05s / p95 56.68s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "On"  x18
    "Off"  x7
data.floor  (string, 25/25 records)
    "4"  x9
    "3"  x8
    "1"  x5
    "2"  x3
data.machineNumber  (string, 25/25 records)
    "One"  x24
    "Two"  x1
data.machineType  (string, 25/25 records)
    "Condenser"  x14
    "Evaporator"  x8
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 25/25 records)
    "2"  x10
    "3"  x9
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 8932.97s (p5 228.08s / p95 267826.18s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 18 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (18)
- **Intervals:** median 1.04s (p5 0.68s / p95 238.74s, n=17)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x16; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "optionSelected"  x16
    "DesignSubmitted"  x2
data.designSelections  (object, 2/18 records)
data.designSelections.glassRoofTemperature  (string, 2/18 records)
    "Cold"  x1
    "Hot"  x1
data.designSelections.roofCovering  (string, 2/18 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/18 records)
    "Flat"  x1
    "Tilted In"  x1
data.featureUsed  (string, 18/18 records)
    "RoofStyle"  x7
    "GlassRoofTemperature"  x5
    "ExtraCovering"  x4
    "Submit"  x2
data.selectedOption  (string, 16/18 records, 2 empty-string)
    "Cold"  x3
    ""  x2
    "Covered"  x2
    "Flat"  x2
    "Tilted In"  x2
    "Tilted Out"  x2
    "Uncovered"  x2
    "Hot"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (5); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 194.74s (p5 0.04s / p95 382531.21s, n=15)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 16/16 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x5
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 4 - Flooding"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 11 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 5 Dev (7); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 441.61s (p5 0.15s / p95 492798.12s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 11/11 records)
    "5"  x7
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 3.23s (p5 1.00s / p95 15.81s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x5
data.boxId  (string, 10/10 records)
    "0"  x5
    "2"  x3
    "1"  x2
data.soilType  (string, 10/10 records)
    "Sand"  x4
    "Gravel"  x3
    "Clay"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 5.16s (p5 2.97s / p95 431777.83s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `soilMachine` — 5 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (5)
- **Intervals:** median 142.92s (p5 26.25s / p95 205.11s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "ChangeCanister"  x5
data.canisterType  (string, 5/5 records)
    "Gravel"  x3
    "Clay"  x1
    "Sand"  x1
data.floor  (string, 5/5 records)
    "4"  x2
    "5"  x2
    "3"  x1
data.machine  (string, 5/5 records)
    "1"  x4
    "2"  x1
data.row  (string, 5/5 records)
    "TopRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1693.26s (p5 1024.36s / p95 224001.37s, n=3)
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
    "unit2"  x1
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
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (46 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (20x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (23x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (46x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*