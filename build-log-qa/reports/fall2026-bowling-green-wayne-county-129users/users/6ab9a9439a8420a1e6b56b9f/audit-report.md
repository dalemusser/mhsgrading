# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56b9f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56b9f
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56b9f.jsonl
- **Records:** 16081 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56b9f
- **Time span:** 2026-10-05T19:58:03.443000+00:00 .. 2026-10-15T21:44:16.823000+00:00 (241h 46m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56b9f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 16081 records, 10 scenes.
- Findings: **0 FAIL**, **27 WARNING**, 95 INFO, 0 NOT_TESTED, 102 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6688 | 41.59 | 1 | 9 | 0 | 2026-10-05T19:58:15.364000+00:00 | 2026-10-15T21:44:16.823000+00:00 | 241h 46m |
| PuzzlePieceVisibleEvent | 3589 | 22.32 | 1 | 4 | 0 | 2026-10-06T19:54:13.444000+00:00 | 2026-10-15T21:10:48.657000+00:00 | 217h 16m |
| DialogueEvent | 2357 | 14.66 | 1 | 9 | 1509 | 2026-10-05T19:58:31.952000+00:00 | 2026-10-15T21:44:03.476000+00:00 | 241h 45m |
| PlayerPositionEvent | 1840 | 11.44 | 1 | 9 | 0 | 2026-10-05T19:58:11.861000+00:00 | 2026-10-15T21:44:10.796000+00:00 | 241h 45m |
| argumentationNodeEvent | 544 | 3.38 | 1 | 5 | 0 | 2026-10-06T19:44:00.258000+00:00 | 2026-10-15T21:32:10.784000+00:00 | 217h 48m |
| ObjectInterEvent | 381 | 2.37 | 1 | 9 | 0 | 2026-10-05T20:02:43.701000+00:00 | 2026-10-15T21:44:16.823000+00:00 | 241h 41m |
| TopographicMapEvent | 152 | 0.95 | 1 | 2 | 0 | 2026-10-06T19:54:42.444000+00:00 | 2026-10-14T20:11:15.809000+00:00 | 192h 16m |
| Soil Key Puzzle | 130 | 0.81 | 1 | 3 | 0 | 2026-10-06T19:53:53.393000+00:00 | 2026-10-15T20:34:40.767000+00:00 | 216h 40m |
| questEvent | 93 | 0.58 | 1 | 9 | 93 | 2026-10-05T19:58:31.926000+00:00 | 2026-10-15T21:40:35.045000+00:00 | 241h 42m |
| argumentationAnswerEvent | 77 | 0.48 | 1 | 5 | 0 | 2026-10-06T19:44:13.611000+00:00 | 2026-10-15T21:32:21.862000+00:00 | 217h 48m |
| WaterChamberEvent | 76 | 0.47 | 1 | 1 | 0 | 2026-10-15T21:09:17.952000+00:00 | 2026-10-15T21:21:19.841000+00:00 | 12m 1s |
| DEBUGMenu | 31 | 0.19 | 1 | 9 | 0 | 2026-10-05T19:58:11.845000+00:00 | 2026-10-15T21:03:57.446000+00:00 | 241h 5m |
| gameWindowFocusEvent | 23 | 0.14 | 1 | 5 | 0 | 2026-10-05T19:58:03.443000+00:00 | 2026-10-15T21:02:41.136000+00:00 | 241h 4m |
| gameWindowUnfocusEvent | 17 | 0.11 | 1 | 6 | 0 | 2026-10-05T20:11:27.857000+00:00 | 2026-10-15T20:36:10.471000+00:00 | 240h 24m |
| soilMachine | 17 | 0.11 | 1 | 1 | 0 | 2026-10-15T20:02:08.551000+00:00 | 2026-10-15T20:08:41.615000+00:00 | 6m 33s |
| argumentationEvent | 14 | 0.09 | 1 | 5 | 0 | 2026-10-06T19:43:45.966000+00:00 | 2026-10-15T21:32:21.899000+00:00 | 217h 48m |
| gameStartEvent | 13 | 0.08 | 1 | 1 | 0 | 2026-10-05T19:58:03.444000+00:00 | 2026-10-15T21:02:41.136000+00:00 | 241h 4m |
| DaniEvent | 10 | 0.06 | 1 | 3 | 0 | 2026-10-06T19:51:23.965000+00:00 | 2026-10-14T19:59:39.415000+00:00 | 192h 8m |
| TerasGardenBox | 8 | 0.05 | 1 | 1 | 0 | 2026-10-15T20:53:05.213000+00:00 | 2026-10-15T20:53:55.761000+00:00 | 50.5s |
| argumentationToolEvent | 8 | 0.05 | 1 | 3 | 0 | 2026-10-06T19:45:25.398000+00:00 | 2026-10-14T19:35:14.160000+00:00 | 191h 49m |
| SolarStillDesignEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-15T21:37:58.560000+00:00 | 2026-10-15T21:38:10.045000+00:00 | 11.5s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T19:49:10.689000+00:00 | 2026-10-15T21:44:16.808000+00:00 | 217h 55m |
| chatEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-10-15T21:03:57.217000+00:00 | 2026-10-15T21:22:03.463000+00:00 | 18m 6s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 88349.73s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.06s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 0.841s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 1.19s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.311s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43180.069s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1183.697s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1456.627s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.556s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 10 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.4x vs baseline. 
  - Observed: 130 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: ; Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 240 ft; 30 ft; 360 ft; 60 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 76 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 15.4x vs baseline. 
  - Observed: 77 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,I; A,3,I; A,4,I; B,1,I; B,2,II; B,C,1,I; C,1,I; C,D,2,II; C,D,3,4,II; C,D,3,II; C,D,4,II; C,D,A,2,II; D,1,I; D,1,II; D,2,II; D,3,II; D,4,II; D,B,2,I; D,C,2,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.9x vs baseline. 
  - Observed: 544 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.4x vs baseline. 
  - Observed: 17 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[162] _id=6ac402e2de269131f9af8e89 ts=2026-10-05T20:04:49.1960000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[216] _id=6ac403d4de269131f9af936f ts=2026-10-05T20:08:51.4570000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[6] _id=6ac4014cde269131f9af8827 ts=2026-10-05T19:58:03.4440000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[263] _id=6ac54b44de269131f9b79dbc ts=2026-10-06T19:25:56.5080000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[910] _id=6ac5511dde269131f9b7bef7 ts=2026-10-06T19:50:52.8960000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[5] _id=6ac4014cde269131f9af8825 ts=2026-10-05T19:58:03.4430000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[262] _id=6ac54b44de269131f9b79dbb ts=2026-10-06T19:25:56.5080000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[909] _id=6ac5511dde269131f9b7bef6 ts=2026-10-06T19:50:52.8960000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[260] _id=6ac54b44de269131f9b79db8 ts=2026-10-05T20:11:27.857Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[2798] _id=6ac69c55de269131f9bf20fd ts=2026-10-06T20:11:10.511Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[2803] _id=6ac69c5cde269131f9bf2103 ts=2026-10-07T19:24:11.8070000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 24 of 152 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[1060] _id=6ac55202de269131f9b7ce0f ts=2026-10-06T19:54:42.4440000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1058] _id=6ac55205de269131f9b7ce3e ts=2026-10-06T19:54:44.9290000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1061] _id=6ac55206de269131f9b7ce4a ts=2026-10-06T19:54:45.8510000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6687 | 0.0 | 0.495 | 130.157 | 5.583 | 429802.881 | 0.46 | 384 | 8 |
| PuzzlePieceVisibleEvent | 3588 | 0.0 | 0.06 | 218.003 | 1.27 | 517045.497 | 0.28 | 1674 | 8 |
| DialogueEvent | 2356 | 0.0 | 3.912 | 369.411 | 25.832 | 429789.569 | 0.16 | 640 | 7 |
| PlayerPositionEvent | 1828 | 9.752 | 10.003 | 429.894 | 10.148 | 429790.617 | 0.14 | 0 | 6 |
| argumentationNodeEvent | 543 | 0.001 | 0.435 | 1443.997 | 6.295 | 604968.211 | 0.04 | 67 | 4 |
| ObjectInterEvent | 380 | 0.0 | 6.766 | 2289.719 | 308.364 | 430242.346 | 0.03 | 4 | 12 |
| TopographicMapEvent | 151 | 0.004 | 2.373 | 4584.062 | 499.595 | 431080.206 | 0.01 | 5 | 8 |
| Soil Key Puzzle | 129 | 0.005 | 0.767 | 6046.879 | 137.052 | 603485.007 | 0.01 | 3 | 4 |
| questEvent | 92 | 0.0 | 168.697 | 9457.86 | 83758.224 | 430917.897 | 0.01 | 18 | 13 |
| argumentationAnswerEvent | 76 | 0.055 | 1.19 | 10316.951 | 691.327 | 604993.281 | 0.01 | 0 | 4 |
| WaterChamberEvent | 75 | 0.088 | 0.841 | 9.625 | 44.296 | 131.167 | 6.23 | 0 | 0 |
| DEBUGMenu | 30 | 5.724 | 667.578 | 28931.52 | 85713.831 | 431063.828 | 0.0 | 0 | 16 |
| gameWindowFocusEvent | 22 | 0.5 | 1183.697 | 39448.986 | 86515.602 | 430055.359 | 0.0 | 0 | 15 |
| gameWindowUnfocusEvent | 16 | 0.0 | 1456.627 | 54092.663 | 172363.578 | 430306.351 | 0.0 | 1 | 10 |
| soilMachine | 16 | 1.147 | 7.556 | 24.567 | 108.787 | 147.044 | 2.44 | 0 | 0 |
| argumentationEvent | 13 | 0.042 | 96.605 | 60316.61 | 296318.357 | 604947.384 | 0.0 | 1 | 4 |
| gameStartEvent | 12 | 539.888 | 43180.069 | 72323.141 | 241965.118 | 431074.008 | 0.0 | 0 | 11 |
| DaniEvent | 9 | 0.36 | 2.541 | 76855.05 | 414870.877 | 690999.443 | 0.0 | 0 | 2 |
| TerasGardenBox | 7 | 1.445 | 2.779 | 7.221 | 21.247 | 23.499 | 8.31 | 0 | 0 |
| argumentationToolEvent | 7 | 0.163 | 1.311 | 98655.537 | 449162.241 | 604969.834 | 0.0 | 0 | 2 |
| SolarStillDesignEvent | 5 | 0.479 | 2.203 | 2.297 | 4.907 | 5.476 | 26.12 | 0 | 0 |
| EndOfUnit | 4 | 2548.658 | 88349.73 | 196126.53 | 527877.96 | 605258.001 | 0.0 | 0 | 4 |
| chatEvent | 1 | 1086.246 | 1086.246 | 1086.246 | 1086.246 | 1086.246 | 0.06 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 18 group(s), 47 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[266] _id=6ac54b4ede269131f9b79dd7 ts=2026-10-06T19:26:06.0410000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[267] _id=6ac54b4ede269131f9b79dd8 ts=2026-10-06T19:26:06.0410000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[269] _id=6ac54b4ede269131f9b79dda ts=2026-10-06T19:26:06.0420000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[270] _id=6ac54b4ede269131f9b79ddb ts=2026-10-06T19:26:06.0420000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[427] _id=6ac54d5ade269131f9b7a5bd ts=2026-10-06T19:34:50.7020000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[428] _id=6ac54d5ade269131f9b7a5be ts=2026-10-06T19:34:50.7020000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 64 group(s), 96 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[1000] _id=6ac551f0de269131f9b7ccaa ts=2026-10-06T19:54:22.8550000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[1001] _id=6ac551f0de269131f9b7ccab ts=2026-10-06T19:54:22.8550000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1002] _id=6ac551f0de269131f9b7ccb1 ts=2026-10-06T19:54:23.0920000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[1003] _id=6ac551f0de269131f9b7ccb2 ts=2026-10-06T19:54:23.0920000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1047] _id=6ac551f3de269131f9b7cd08 ts=2026-10-06T19:54:25.9380000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[1048] _id=6ac551f3de269131f9b7cd0c ts=2026-10-06T19:54:25.9380000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[15749] _id=6ad146adde269131f9e1899a ts=2026-10-15T21:33:32.1170000Z == 6ab9a9439a8420a1e6b56b9f.jsonl[15750] _id=6ad146adde269131f9e1899b ts=2026-10-15T21:33:32.1170000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 69 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56b9f.jsonl[105] _id=6ac40264de269131f9af8c79 ts=2026-10-05T20:02:43.7010000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[108] _id=6ac40264de269131f9af8c7b ts=2026-10-05T20:02:43.7060000Z`; `11ms: 6ab9a9439a8420a1e6b56b9f.jsonl[286] _id=6ac54b7dde269131f9b79e99 ts=2026-10-06T19:26:53.5620000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[287] _id=6ac54b7ede269131f9b79e9b ts=2026-10-06T19:26:53.5730000Z`; `712ms: 6ab9a9439a8420a1e6b56b9f.jsonl[1586] _id=6ac552adde269131f9b7e005 ts=2026-10-06T19:57:33.0300000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[1588] _id=6ac552adde269131f9b7e008 ts=2026-10-06T19:57:33.7420000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `703ms: 6ab9a9439a8420a1e6b56b9f.jsonl[1069] _id=6ac5520fde269131f9b7cefc ts=2026-10-06T19:54:55.6830000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[1071] _id=6ac55210de269131f9b7cf09 ts=2026-10-06T19:54:56.3860000Z`; `834ms: 6ab9a9439a8420a1e6b56b9f.jsonl[1090] _id=6ac55221de269131f9b7d0a8 ts=2026-10-06T19:55:13.5400000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[1088] _id=6ac55222de269131f9b7d0c1 ts=2026-10-06T19:55:14.3740000Z`; `688ms: 6ab9a9439a8420a1e6b56b9f.jsonl[1087] _id=6ac55222de269131f9b7d0b9 ts=2026-10-06T19:55:14.0900000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[1089] _id=6ac55222de269131f9b7d0cd ts=2026-10-06T19:55:14.7780000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 27 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `382ms: 6ab9a9439a8420a1e6b56b9f.jsonl[14921] _id=6ad14216de269131f9e16ee9 ts=2026-10-15T21:13:58.0470000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[14922] _id=6ad14217de269131f9e16ef0 ts=2026-10-15T21:13:58.4290000Z`; `237ms: 6ab9a9439a8420a1e6b56b9f.jsonl[14913] _id=6ad14217de269131f9e16eed ts=2026-10-15T21:13:58.2930000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[14915] _id=6ad14217de269131f9e16ef3 ts=2026-10-15T21:13:58.5300000Z`; `942ms: 6ab9a9439a8420a1e6b56b9f.jsonl[14922] _id=6ad14217de269131f9e16ef0 ts=2026-10-15T21:13:58.4290000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[14917] _id=6ad14218de269131f9e16ef6 ts=2026-10-15T21:13:59.3710000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 35 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `582ms: 6ab9a9439a8420a1e6b56b9f.jsonl[658] _id=6ac54fd7de269131f9b7b407 ts=2026-10-06T19:45:27.0230000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[659] _id=6ac54fd7de269131f9b7b409 ts=2026-10-06T19:45:27.6050000Z`; `721ms: 6ab9a9439a8420a1e6b56b9f.jsonl[660] _id=6ac54fd8de269131f9b7b40d ts=2026-10-06T19:45:28.6530000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[700] _id=6ac54fd9de269131f9b7b413 ts=2026-10-06T19:45:29.3740000Z`; `519ms: 6ab9a9439a8420a1e6b56b9f.jsonl[701] _id=6ac54fdade269131f9b7b419 ts=2026-10-06T19:45:30.5220000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[702] _id=6ac54fdbde269131f9b7b41f ts=2026-10-06T19:45:31.0410000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `42ms: 6ab9a9439a8420a1e6b56b9f.jsonl[7757] _id=6acfd999de269131f9d8e2d7 ts=2026-10-14T19:35:53.0110000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[7760] _id=6acfd99ade269131f9d8e2e0 ts=2026-10-14T19:35:53.0530000Z`; `52ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13931] _id=6ad13c50de269131f9e13984 ts=2026-10-15T20:49:19.7690000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[13934] _id=6ad13c50de269131f9e13988 ts=2026-10-15T20:49:19.8210000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 72 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `442ms: 6ab9a9439a8420a1e6b56b9f.jsonl[638] _id=6ac54f82de269131f9b7b1dc ts=2026-10-06T19:44:02.1390000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[629] _id=6ac54f82de269131f9b7b1e1 ts=2026-10-06T19:44:02.5810000Z`; `356ms: 6ab9a9439a8420a1e6b56b9f.jsonl[628] _id=6ac54f82de269131f9b7b1df ts=2026-10-06T19:44:02.5170000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[631] _id=6ac54f83de269131f9b7b1ec ts=2026-10-06T19:44:02.8730000Z`; `312ms: 6ab9a9439a8420a1e6b56b9f.jsonl[666] _id=6ac54fc4de269131f9b7b367 ts=2026-10-06T19:45:08.3460000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[675] _id=6ac54fc4de269131f9b7b36b ts=2026-10-06T19:45:08.6580000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `163ms: 6ab9a9439a8420a1e6b56b9f.jsonl[697] _id=6ac54fd5de269131f9b7b3ed ts=2026-10-06T19:45:25.3980000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[698] _id=6ac54fd5de269131f9b7b3ef ts=2026-10-06T19:45:25.5610000Z`; `278ms: 6ab9a9439a8420a1e6b56b9f.jsonl[6415] _id=6ace8b01de269131f9d22293 ts=2026-10-13T19:48:16.7060000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[6416] _id=6ace8b01de269131f9d22295 ts=2026-10-13T19:48:16.9840000Z`; `674ms: 6ab9a9439a8420a1e6b56b9f.jsonl[6416] _id=6ace8b01de269131f9d22295 ts=2026-10-13T19:48:16.9840000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[6418] _id=6ace8b02de269131f9d222af ts=2026-10-13T19:48:17.6580000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `500ms: 6ab9a9439a8420a1e6b56b9f.jsonl[6379] _id=6ace8a94de269131f9d21b72 ts=2026-10-13T19:46:28.0330000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[6380] _id=6ace8a95de269131f9d21b76 ts=2026-10-13T19:46:28.5330000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[5981] _id=6ac7f8b1de269131f9c745cb ts=2026-10-08T20:10:24.1690000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[5983] _id=6ace871ade269131f9d1f6a1 ts=2026-10-08T20:10:24.169Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a9439a8420a1e6b56b9f.jsonl[15972] _id=6ad1480dde269131f9e18fce ts=2026-10-15T21:39:25.1660000Z ~ 6ab9a9439a8420a1e6b56b9f.jsonl[15973] _id=6ad1480ede269131f9e18fd0 ts=2026-10-15T21:39:25.1720000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a9439a8420a1e6b56b9f.jsonl[5409] _id=6ac7f342de269131f9c6d33f ts=2026-10-08T19:47:13.9760000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5984] _id=6ace871ade269131f9d1f6a5 ts=2026-10-13T19:31:37.8040000Z; 24h 1m: 6ab9a9439a8420a1e6b56b9f.jsonl[2820] _id=6ac69f51de269131f9bf223b ts=2026-10-07T19:36:48.3500000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4836] _id=6ac7f11dde269131f9c6aa68 ts=2026-10-08T19:38:04.0920000Z; 23h 33m: 6ab9a9439a8420a1e6b56b9f.jsonl[911] _id=6ac55126de269131f9b7bf5f ts=2026-10-06T19:51:01.8180000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2799] _id=6ac69c55de269131f9bf20ff ts=2026-10-07T19:24:04.4240000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 56m 
  - Evidence: 191h 56m: 6ab9a9439a8420a1e6b56b9f.jsonl[925] _id=6ac5513dde269131f9b7c14e ts=2026-10-06T19:51:25.0640000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[8558] _id=6acfdc75de269131f9d91420 ts=2026-10-14T19:48:04.5070000Z; 11m 18s: 6ab9a9439a8420a1e6b56b9f.jsonl[8578] _id=6acfdc85de269131f9d914e5 ts=2026-10-14T19:48:21.0280000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[9322] _id=6acfdf2cde269131f9d940fc ts=2026-10-14T19:59:39.0550000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a9439a8420a1e6b56b9f.jsonl[5982] _id=6ac7f8afde269131f9c745b3 ts=2026-10-08T20:10:22.7910000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5988] _id=6ace878ede269131f9d1fb14 ts=2026-10-13T19:33:32.3600000Z; 23h 28m: 6ab9a9439a8420a1e6b56b9f.jsonl[4802] _id=6ac6a712de269131f9bf8adb ts=2026-10-07T20:09:53.5500000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4862] _id=6ac7f146de269131f9c6ac6c ts=2026-10-08T19:38:43.7970000Z; 23h 28m: 6ab9a9439a8420a1e6b56b9f.jsonl[2788] _id=6ac555d9de269131f9b853c3 ts=2026-10-06T20:11:05.7830000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2868] _id=6ac6a00cde269131f9bf2522 ts=2026-10-07T19:39:55.9850000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 640 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13763] _id=6ad13b9ede269131f9e13514 ts=2026-10-15T20:46:22.0370000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13764] _id=6ad13b9ede269131f9e13515 ts=2026-10-15T20:46:22.0370000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13835] _id=6ad13be4de269131f9e13722 ts=2026-10-15T20:47:31.2390000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13836] _id=6ad13be4de269131f9e13723 ts=2026-10-15T20:47:31.2390000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13867] _id=6ad13c03de269131f9e1380b ts=2026-10-15T20:48:02.2800000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13870] _id=6ad13c03de269131f9e1380c ts=2026-10-15T20:48:02.2800000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 7m 
  - Evidence: 168h 7m: 6ab9a9439a8420a1e6b56b9f.jsonl[902] _id=6ac550b6de269131f9b7ba96 ts=2026-10-06T19:49:10.6890000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6752] _id=6ace8d01de269131f9d239bb ts=2026-10-13T19:56:48.6900000Z; 24h 49m: 6ab9a9439a8420a1e6b56b9f.jsonl[9844] _id=6acfe20ede269131f9d96766 ts=2026-10-14T20:11:57.0900000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[14341] _id=6ad13f3cde269131f9e14e97 ts=2026-10-15T21:01:48.1500000Z; 24h 15m: 6ab9a9439a8420a1e6b56b9f.jsonl[6752] _id=6ace8d01de269131f9d239bb ts=2026-10-13T19:56:48.6900000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[9844] _id=6acfe20ede269131f9d96766 ts=2026-10-14T20:11:57.0900000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a9439a8420a1e6b56b9f.jsonl[5972] _id=6ac7f8acde269131f9c74587 ts=2026-10-08T20:10:19.2930000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6001] _id=6ace8796de269131f9d1fbae ts=2026-10-13T19:33:42.1740000Z; 23h 30m: 6ab9a9439a8420a1e6b56b9f.jsonl[4747] _id=6ac6a69cde269131f9bf8778 ts=2026-10-07T20:07:56.2120000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4832] _id=6ac7f146de269131f9c6ac55 ts=2026-10-08T19:38:43.7420000Z; 23h 25m: 6ab9a9439a8420a1e6b56b9f.jsonl[2784] _id=6ac555d0de269131f9b85324 ts=2026-10-06T20:10:56.1270000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2808] _id=6ac69f54de269131f9bf2245 ts=2026-10-07T19:36:50.7040000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 384 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[10359] _id=6ad12b7ede269131f9e094af ts=2026-10-15T19:37:32.9090000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[10360] _id=6ad12b7ede269131f9e094b0 ts=2026-10-15T19:37:32.9090000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[11177] _id=6ad12ca2de269131f9e0af58 ts=2026-10-15T19:42:25.3210000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[11178] _id=6ad12ca2de269131f9e0af59 ts=2026-10-15T19:42:25.3210000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[11375] _id=6ad12d25de269131f9e0b73e ts=2026-10-15T19:44:36.2960000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[11376] _id=6ad12d25de269131f9e0b73f ts=2026-10-15T19:44:36.2960000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a9439a8420a1e6b56b9f.jsonl[5942] _id=6ac7f848de269131f9c73ff0 ts=2026-10-08T20:08:39.1220000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6130] _id=6ace88e9de269131f9d20a92 ts=2026-10-13T19:39:21.4680000Z; 24h 0m: 6ab9a9439a8420a1e6b56b9f.jsonl[2507] _id=6ac553afde269131f9b80a74 ts=2026-10-06T20:01:51.2010000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[3719] _id=6ac6a539de269131f9bf6cbf ts=2026-10-07T20:02:00.5350000Z; 23h 33m: 6ab9a9439a8420a1e6b56b9f.jsonl[4752] _id=6ac6a69bde269131f9bf8761 ts=2026-10-07T20:07:55.2960000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5017] _id=6ac7f1e7de269131f9c6b902 ts=2026-10-08T19:41:26.3980000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13568] _id=6ad13a89de269131f9e1301d ts=2026-10-15T20:41:44.7630000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13569] _id=6ad13a89de269131f9e1301e ts=2026-10-15T20:41:44.7630000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13620] _id=6ad13ad3de269131f9e130dd ts=2026-10-15T20:42:59.2020000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13621] _id=6ad13ad3de269131f9e130de ts=2026-10-15T20:42:59.2020000Z; 5ms: 6ab9a9439a8420a1e6b56b9f.jsonl[105] _id=6ac40264de269131f9af8c79 ts=2026-10-05T20:02:43.7010000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[108] _id=6ac40264de269131f9af8c7b ts=2026-10-05T20:02:43.7060000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a9439a8420a1e6b56b9f.jsonl[5978] _id=6ac7f8a9de269131f9c7456e ts=2026-10-08T20:10:16.9310000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5987] _id=6ace878ede269131f9d1fb13 ts=2026-10-13T19:33:27.5480000Z; 23h 28m: 6ab9a9439a8420a1e6b56b9f.jsonl[4803] _id=6ac6a724de269131f9bf8b06 ts=2026-10-07T20:10:12.3660000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4831] _id=6ac7f146de269131f9c6ac54 ts=2026-10-08T19:38:41.1180000Z; 23h 25m: 6ab9a9439a8420a1e6b56b9f.jsonl[2732] _id=6ac555dbde269131f9b853db ts=2026-10-06T20:11:07.7450000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2807] _id=6ac69f54de269131f9bf2244 ts=2026-10-07T19:36:48.3630000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a9439a8420a1e6b56b9f.jsonl[5772] _id=6ac7f73ade269131f9c7298e ts=2026-10-08T20:04:09.6350000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[8143] _id=6acfdaf1de269131f9d8ff98 ts=2026-10-14T19:41:35.1320000Z; 24h 2m: 6ab9a9439a8420a1e6b56b9f.jsonl[2448] _id=6ac55362de269131f9b80162 ts=2026-10-06T20:00:31.4430000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[3764] _id=6ac6a566de269131f9bf6ff7 ts=2026-10-07T20:02:44.7630000Z; 23h 53m: 6ab9a9439a8420a1e6b56b9f.jsonl[8348] _id=6acfdb54de269131f9d90724 ts=2026-10-14T19:43:13.3820000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[9991] _id=6ad12b4cde269131f9e08d67 ts=2026-10-15T19:36:42.8200000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1674 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[10008] _id=6ad12b4ede269131f9e08daf ts=2026-10-15T19:36:45.3900000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[10009] _id=6ad12b4fde269131f9e08db3 ts=2026-10-15T19:36:45.3900000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[10009] _id=6ad12b4fde269131f9e08db3 ts=2026-10-15T19:36:45.3900000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[10010] _id=6ad12b4fde269131f9e08db5 ts=2026-10-15T19:36:45.3900000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[1000] _id=6ac551f0de269131f9b7ccaa ts=2026-10-06T19:54:22.8550000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[1001] _id=6ac551f0de269131f9b7ccab ts=2026-10-06T19:54:22.8550000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 38m 
  - Evidence: 167h 38m: 6ab9a9439a8420a1e6b56b9f.jsonl[3726] _id=6ac6a54ade269131f9bf6e55 ts=2026-10-07T20:02:17.4270000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[8097] _id=6acfdaa7de269131f9d8fb68 ts=2026-10-14T19:40:22.4340000Z; 23h 53m: 6ab9a9439a8420a1e6b56b9f.jsonl[2683] _id=6ac55546de269131f9b84532 ts=2026-10-06T20:08:38.6780000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[3710] _id=6ac6a539de269131f9bf6cb7 ts=2026-10-07T20:02:00.5310000Z; 23h 52m: 6ab9a9439a8420a1e6b56b9f.jsonl[8111] _id=6acfdab9de269131f9d8fcc9 ts=2026-10-14T19:40:40.7350000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[9871] _id=6ad12a80de269131f9e07d4d ts=2026-10-15T19:33:19.1550000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.005s..0.048s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56b9f.jsonl[2543] _id=6ac553dcde269131f9b811f2 ts=2026-10-06T20:02:36.0520000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2545] _id=6ac553dcde269131f9b81208 ts=2026-10-06T20:02:36.0570000Z; 5ms: 6ab9a9439a8420a1e6b56b9f.jsonl[2547] _id=6ac553dede269131f9b81269 ts=2026-10-06T20:02:38.6230000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2550] _id=6ac553dede269131f9b8126e ts=2026-10-06T20:02:38.6280000Z; 48ms: 6ab9a9439a8420a1e6b56b9f.jsonl[2562] _id=6ac553e8de269131f9b813d3 ts=2026-10-06T20:02:48.3920000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2561] _id=6ac553e8de269131f9b813df ts=2026-10-06T20:02:48.4400000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a9439a8420a1e6b56b9f.jsonl[5635] _id=6ac7f57cde269131f9c6fa6e ts=2026-10-08T19:56:43.4620000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6200] _id=6ace8964de269131f9d2114e ts=2026-10-13T19:41:23.6680000Z; 23h 38m: 6ab9a9439a8420a1e6b56b9f.jsonl[3569] _id=6ac6a4bcde269131f9bf62de ts=2026-10-07T19:59:55.4480000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4849] _id=6ac7f146de269131f9c6ac5f ts=2026-10-08T19:38:43.7500000Z; 23h 34m: 6ab9a9439a8420a1e6b56b9f.jsonl[2640] _id=6ac554dede269131f9b83755 ts=2026-10-06T20:06:54.3660000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2904] _id=6ac6a07dde269131f9bf2847 ts=2026-10-07T19:41:48.4040000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.004s..0.010s shown 
  - Evidence: 4ms: 6ab9a9439a8420a1e6b56b9f.jsonl[4853] _id=6ac7f146de269131f9c6ac63 ts=2026-10-08T19:38:43.7690000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4855] _id=6ac7f146de269131f9c6ac65 ts=2026-10-08T19:38:43.7730000Z; 9ms: 6ab9a9439a8420a1e6b56b9f.jsonl[4851] _id=6ac7f146de269131f9c6ac61 ts=2026-10-08T19:38:43.7600000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4853] _id=6ac7f146de269131f9c6ac63 ts=2026-10-08T19:38:43.7690000Z; 10ms: 6ab9a9439a8420a1e6b56b9f.jsonl[4849] _id=6ac7f146de269131f9c6ac5f ts=2026-10-08T19:38:43.7500000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4851] _id=6ac7f146de269131f9c6ac61 ts=2026-10-08T19:38:43.7600000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 3m 
  - Evidence: 168h 3m: 6ab9a9439a8420a1e6b56b9f.jsonl[725] _id=6ac54fe3de269131f9b7b484 ts=2026-10-06T19:45:39.0690000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6461] _id=6ace8b24de269131f9d22574 ts=2026-10-13T19:48:52.3500000Z; 25h 10m: 6ab9a9439a8420a1e6b56b9f.jsonl[7744] _id=6acfd999de269131f9d8e2d1 ts=2026-10-14T19:35:52.9890000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13723] _id=6ad13b84de269131f9e13464 ts=2026-10-15T20:45:56.0160000Z; 23h 42m: 6ab9a9439a8420a1e6b56b9f.jsonl[6651] _id=6ace8be8de269131f9d22ef8 ts=2026-10-13T19:52:07.8090000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[7676] _id=6acfd953de269131f9d8dbfe ts=2026-10-14T19:34:43.0380000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 2m 
  - Evidence: 168h 2m: 6ab9a9439a8420a1e6b56b9f.jsonl[722] _id=6ac54fe3de269131f9b7b486 ts=2026-10-06T19:45:39.0900000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6409] _id=6ace8af7de269131f9d221e7 ts=2026-10-13T19:48:06.4740000Z; 25h 9m: 6ab9a9439a8420a1e6b56b9f.jsonl[7760] _id=6acfd99ade269131f9d8e2e0 ts=2026-10-14T19:35:53.0530000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13692] _id=6ad13b5fde269131f9e13363 ts=2026-10-15T20:45:18.7250000Z; 23h 42m: 6ab9a9439a8420a1e6b56b9f.jsonl[6635] _id=6ace8be8de269131f9d22efa ts=2026-10-13T19:52:07.8280000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[7637] _id=6acfd939de269131f9d8d970 ts=2026-10-14T19:34:16.4060000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.042s..0.042s shown 
  - Evidence: 42ms: 6ab9a9439a8420a1e6b56b9f.jsonl[7757] _id=6acfd999de269131f9d8e2d7 ts=2026-10-14T19:35:53.0110000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[7760] _id=6acfd99ade269131f9d8e2e0 ts=2026-10-14T19:35:53.0530000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 2m 
  - Evidence: 168h 2m: 6ab9a9439a8420a1e6b56b9f.jsonl[668] _id=6ac54fd4de269131f9b7b3e3 ts=2026-10-06T19:45:23.9260000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6411] _id=6ace8afcde269131f9d22237 ts=2026-10-13T19:48:12.1370000Z; 25h 9m: 6ab9a9439a8420a1e6b56b9f.jsonl[7743] _id=6acfd999de269131f9d8e2b2 ts=2026-10-14T19:35:51.6170000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13678] _id=6ad13b59de269131f9e13321 ts=2026-10-15T20:45:12.8960000Z; 23h 42m: 6ab9a9439a8420a1e6b56b9f.jsonl[6647] _id=6ace8be3de269131f9d22ec5 ts=2026-10-13T19:52:02.5720000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[7626] _id=6acfd933de269131f9d8d8d1 ts=2026-10-14T19:34:10.6500000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 67 interval(s) ≤ 0.001s..0.010s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56b9f.jsonl[13882] _id=6ad13c1fde269131f9e13896 ts=2026-10-15T20:48:30.5870000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[13888] _id=6ad13c1fde269131f9e13897 ts=2026-10-15T20:48:30.5880000Z; 6ms: 6ab9a9439a8420a1e6b56b9f.jsonl[7627] _id=6acfd933de269131f9d8d8d8 ts=2026-10-14T19:34:10.7560000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[7630] _id=6acfd933de269131f9d8d8dd ts=2026-10-14T19:34:10.7620000Z; 10ms: 6ab9a9439a8420a1e6b56b9f.jsonl[15684] _id=6ad1463cde269131f9e185ab ts=2026-10-15T21:31:40.1340000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[15685] _id=6ad1463cde269131f9e185ad ts=2026-10-15T21:31:40.1440000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 2m 
  - Evidence: 168h 2m: 6ab9a9439a8420a1e6b56b9f.jsonl[699] _id=6ac54fd7de269131f9b7b405 ts=2026-10-06T19:45:26.8720000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6415] _id=6ace8b01de269131f9d22293 ts=2026-10-13T19:48:16.7060000Z; 23h 46m: 6ab9a9439a8420a1e6b56b9f.jsonl[6418] _id=6ace8b02de269131f9d222af ts=2026-10-13T19:48:17.6580000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[7702] _id=6acfd96dde269131f9d8de70 ts=2026-10-14T19:35:08.8470000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 18m 6s 
  - Evidence: 18m 6s: 6ab9a9439a8420a1e6b56b9f.jsonl[14348] _id=6ad13fbdde269131f9e15233 ts=2026-10-15T21:03:57.2170000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[15406] _id=6ad143fcde269131f9e17af1 ts=2026-10-15T21:22:03.4630000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a9439a8420a1e6b56b9f.jsonl[5261] _id=6ac7f339de269131f9c6d24f ts=2026-10-08T19:47:04.1170000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5986] _id=6ace871ade269131f9d1f6a7 ts=2026-10-13T19:31:38.1250000Z; 24h 13m: 6ab9a9439a8420a1e6b56b9f.jsonl[2801] _id=6ac69c55de269131f9bf2101 ts=2026-10-07T19:24:04.5670000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4838] _id=6ac7f11dde269131f9c6aa6a ts=2026-10-08T19:38:04.2290000Z; 24h 6m: 6ab9a9439a8420a1e6b56b9f.jsonl[7194] _id=6acfd6fcde269131f9d8a1ad ts=2026-10-14T19:24:43.9800000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[9849] _id=6ad129f6de269131f9e07234 ts=2026-10-15T19:31:00.8100000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a9439a8420a1e6b56b9f.jsonl[5766] _id=6ac7f734de269131f9c72925 ts=2026-10-08T20:04:02.7660000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5985] _id=6ace871ade269131f9d1f6a6 ts=2026-10-13T19:31:38.1250000Z; 24h 3m: 6ab9a9439a8420a1e6b56b9f.jsonl[2802] _id=6ac69ecede269131f9bf210c ts=2026-10-07T19:34:37.8940000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4837] _id=6ac7f11dde269131f9c6aa69 ts=2026-10-08T19:38:04.2290000Z; 23h 33m: 6ab9a9439a8420a1e6b56b9f.jsonl[909] _id=6ac5511dde269131f9b7bef6 ts=2026-10-06T19:50:52.8960000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2800] _id=6ac69c55de269131f9bf2100 ts=2026-10-07T19:24:04.5670000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a9439a8420a1e6b56b9f.jsonl[5983] _id=6ace871ade269131f9d1f6a1 ts=2026-10-08T20:10:24.169Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[6224] _id=6ace8993de269131f9d212fb ts=2026-10-13T19:42:10.5200000Z; 23h 59m: 6ab9a9439a8420a1e6b56b9f.jsonl[260] _id=6ac54b44de269131f9b79db8 ts=2026-10-05T20:11:27.857Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2798] _id=6ac69c55de269131f9bf20fd ts=2026-10-06T20:11:10.511Z; 23h 54m: 6ab9a9439a8420a1e6b56b9f.jsonl[7195] _id=6acfd6fcde269131f9d8a1a5 ts=2026-10-13T20:11:34.846Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[9707] _id=6acfe0c8de269131f9d957da ts=2026-10-14T20:06:31.4780000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[5981] _id=6ac7f8b1de269131f9c745cb ts=2026-10-08T20:10:24.1690000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5983] _id=6ace871ade269131f9d1f6a1 ts=2026-10-08T20:10:24.169Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 41m 
  - Evidence: 119h 41m: 6ab9a9439a8420a1e6b56b9f.jsonl[5538] _id=6ac7f447de269131f9c6e697 ts=2026-10-08T19:51:34.5080000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[5990] _id=6ace878ede269131f9d1fb16 ts=2026-10-13T19:33:32.4050000Z; 23h 30m: 6ab9a9439a8420a1e6b56b9f.jsonl[4780] _id=6ac6a6c3de269131f9bf88dc ts=2026-10-07T20:08:34.6290000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[4864] _id=6ac7f146de269131f9c6ac6e ts=2026-10-08T19:38:43.8330000Z; 23h 27m: 6ab9a9439a8420a1e6b56b9f.jsonl[2693] _id=6ac55573de269131f9b84a79 ts=2026-10-06T20:09:23.1110000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[2818] _id=6ac69f54de269131f9bf224f ts=2026-10-07T19:36:50.7530000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[14894] _id=6ad141d9de269131f9e16e3e ts=2026-10-15T21:12:56.7690000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[14895] _id=6ad141d9de269131f9e16e3f ts=2026-10-15T21:12:56.7690000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[15749] _id=6ad146adde269131f9e1899a ts=2026-10-15T21:33:32.1170000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[15750] _id=6ad146adde269131f9e1899b ts=2026-10-15T21:33:32.1170000Z; 0ms: 6ab9a9439a8420a1e6b56b9f.jsonl[610] _id=6ac54f22de269131f9b7af86 ts=2026-10-06T19:42:26.2830000Z -> 6ab9a9439a8420a1e6b56b9f.jsonl[611] _id=6ac54f22de269131f9b7af87 ts=2026-10-06T19:42:26.2830000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[588] _id=6ac54f0fde269131f9b7aec0 ts=2026-10-06T19:42:07.3470000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[737] _id=6ac54ff9de269131f9b7b521 ts=2026-10-06T19:46:01.4250000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[3142] _id=6ac6a24dde269131f9bf46df ts=2026-10-07T19:49:32.7630000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[7760] _id=6acfd99ade269131f9d8e2e0 ts=2026-10-14T19:35:53.0530000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[13934] _id=6ad13c50de269131f9e13988 ts=2026-10-15T20:49:19.8210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[14348] _id=6ad13fbdde269131f9e15233 ts=2026-10-15T21:03:57.2170000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[15406] _id=6ad143fcde269131f9e17af1 ts=2026-10-15T21:22:03.4630000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[9486] _id=6acfdfb1de269131f9d948cf ts=2026-10-14T20:01:52.3700000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[12291] _id=6ad13045de269131f9e0ef9d ts=2026-10-15T19:57:56.5970000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 89 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[3891] _id=6ac6a60cde269131f9bf7877 ts=2026-10-07T20:05:28.0840000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[3890] _id=6ac6a60cde269131f9bf7879 ts=2026-10-07T20:05:28.0840000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[3892] _id=6ac6a60cde269131f9bf787b ts=2026-10-07T20:05:28.0840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 224 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[1001] _id=6ac551f0de269131f9b7ccab ts=2026-10-06T19:54:22.8550000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1002] _id=6ac551f0de269131f9b7ccb1 ts=2026-10-06T19:54:23.0920000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1003] _id=6ac551f0de269131f9b7ccb2 ts=2026-10-06T19:54:23.0920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[698] _id=6ac54fd5de269131f9b7b3ef ts=2026-10-06T19:45:25.5610000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[6416] _id=6ace8b01de269131f9d22295 ts=2026-10-13T19:48:16.9840000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[6418] _id=6ace8b02de269131f9d222af ts=2026-10-13T19:48:17.6580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 428 start, 420 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 23 unmatched 'BecameVisible' (totals: 1048 open, 1025 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 7 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 52 start, 41 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 578 of 16080 adjacent _id pairs reverse in client time; worst 138.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56b9f.jsonl[1211] _id=6ac5526fde269131f9b7d82d ts=2026-10-06T19:56:31.4070000Z`; `6ab9a9439a8420a1e6b56b9f.jsonl[1204] _id=6ac55270de269131f9b7d837 ts=2026-10-06T19:54:13.4440000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.94s, min -429674.20s, max -0.17s over 16081 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56b9f\coverage.yaml

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

### `InputEvent` — 6688 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1792); Unit 4 Dev - Dungeon (1408); Unit 3 Dev (1165); Unit 3 Dungeon Dev (630); Unit 4 Dev (561); Unit 5 Dev - Dungeon (514); Unit 1 Dev (315); Unit 5 Dev (205); Unit 4 Dev - Anderson Base (98)
- **Intervals:** median 0.49s (p5 0.04s / p95 5.58s, n=6687)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6688/6688 records)
    "pressed"  x6688
data.actionType  (string, 6688/6688 records)
    "Move"  x5179
    "Interact"  x686
    "Jump"  x544
    "Hoverboard"  x125
    "Ascend"  x59
    "Map"  x41
    "Descend"  x36
    "Sprint"  x7
    "Pause"  x6
    "ToggleDebug"  x5
data.key  (string, 6688/6688 records, 19 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6688/6688 records)
    "Player"  x5977
    "Drone"  x711
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3589 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2201); Unit 4 Dev (1002); Unit 5 Dev - Dungeon (242); Unit 3 Dungeon Dev (144)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.27s, n=3588)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3589/3589 records)
    "BecameVisible"  x1048
    "BecameInvisible"  x1025
    "BecameCameraCentered"  x758
    "BecameCameraUncentered"  x758
data.pieceId  (string, 3589/3589 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3589/3589 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2357 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (738); Unit 3 Dev (356); Unit 4 Dev (290); Unit 1 Dev (254); Unit 5 Dev (228); Unit 4 Dev - Dungeon (154); Unit 3 Dungeon Dev (138); Unit 4 Dev - Anderson Base (111); Unit 5 Dev - Dungeon (88)
- **eventKey:** present on 1509 of 2357 records
- **Intervals:** median 3.91s (p5 0.00s / p95 25.83s, n=2356)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1509; [conversationId, dialogueEventType] x848
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2357/2357 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2357/2357 records)
    "DialogueNodeEvent"  x1509
    "DialogueStartEvent"  x428
    "DialogueFinishEvent"  x420
data.nodeId  (number, 1509/2357 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1840 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (621); Unit 3 Dev (241); Unit 1 Dev (219); Unit 4 Dev (187); Unit 4 Dev - Dungeon (170); Unit 5 Dev (132); Unit 5 Dev - Dungeon (108); Unit 3 Dungeon Dev (98); Unit 4 Dev - Anderson Base (64)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.15s, n=1828)
- **Fields under `data`:**

```text
data.position  (object, 1840/1840 records)
data.position.x  (number, 1840/1840 records)
    numeric range -704.578 .. 1549.85 (666 unique)
data.position.y  (number, 1840/1840 records)
    numeric range -113.43 .. 224.057 (501 unique)
data.position.z  (number, 1840/1840 records)
    numeric range -1110.09 .. 1807.97 (666 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 544 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (181); Unit 4 Dev - Anderson Base (165); Unit 3 Dev (85); Unit 5 Dev (74); Unit 1 Dev (39)
- **Intervals:** median 0.43s (p5 0.03s / p95 6.30s, n=543)
- **Fields under `data`:**

```text
data.actionType  (string, 544/544 records)
    "argumentationNodeHoverEnd"  x237
    "argumentationNodeHoverStart"  x237
    "argumentationNodeAdd"  x45
    "argumentationNodeRemove"  x25
data.argumentationTitle  (string, 544/544 records)
    "Unit 2 – Watershed"  x181
    "Unit 4 - Flooding"  x165
    "Unit 3 - Pollution Upstream"  x85
    "Unit 5"  x74
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 544/544 records)
    "I"  x88
    "1"  x69
    "B"  x58
    "C"  x58
    "II"  x53
    "D"  x50
    "A"  x49
    "2"  x45
    "3"  x37
    "4"  x34
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 381 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (124); Unit 3 Dungeon Dev (98); Unit 2 Prod (Refactor) (62); Unit 4 Dev (23); Unit 5 Dev (18); Unit 1 Dev (17); Unit 5 Dev - Dungeon (16); Unit 3 Dev (14); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 6.77s (p5 0.16s / p95 308.36s, n=380)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 381/381 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 381/381 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 152 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (86); Unit 3 Dev (66)
- **Intervals:** median 2.37s (p5 0.21s / p95 499.60s, n=151)
- **`data` key-set variants:** [actionType, featureUsed] x66; [actionType, featureUsed, location] x62; [actionType, featureUsed, legendName] x24
- **Fields under `data`:**

```text
data.actionType  (string, 152/152 records)
    "WaypointMoveEvent"  x51
    "MapCloseEvent"  x33
    "MapOpenEvent"  x33
    "Selected"  x14
    "Unselected"  x10
    "WaypointSetEvent"  x7
    "WaypointResetEvent"  x4
data.featureUsed  (string, 152/152 records)
    "Map"  x66
    "Waypoint"  x62
    "Legend"  x24
data.legendName  (string, 24/152 records)
    "360 ft"  x9
    "60 ft"  x6
    "120 ft"  x4
    "240 ft"  x2
    "0 ft"  x1
    "150 ft"  x1
    "30 ft"  x1
data.location  (object, 62/152 records)
data.location.x  (number, 62/152 records)
    numeric range -516.51 .. 580.813 (38 unique)
data.location.y  (number, 62/152 records)
    numeric range -307.841 .. 246.258 (42 unique)
data.location.z  (number, 62/152 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 130 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (93); Unit 4 Dev (23); Unit 3 Dev (14)
- **Intervals:** median 0.77s (p5 0.14s / p95 137.05s, n=129)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x122; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/130 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/130 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 122/130 records)
    "RightDrag"  x64
    "LeftDrag"  x58
data.currentSoilType  (string, 122/130 records)
    "SAND"  x23
    "CLAYSAND"  x22
    "SANDGRAVEL"  x22
    "CLAY"  x19
    "CLAYROCK"  x16
    "GRAVEL"  x12
    "BEDROCK"  x8
data.isCorrectSelection  (string, 122/130 records)
    "false"  x100
    "true"  x22
data.waterLevelStatus  (string, 122/130 records)
    "TooHigh"  x52
    "Proper"  x45
    "TooLow"  x25
data.waterRetentionChange  (string, 122/130 records)
    "Decrease"  x57
    "Increase"  x43
    "NoChange"  x22
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 93 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (17); Unit 4 Dev - Dungeon (15); Unit 3 Dev (13); Unit 4 Dev (11); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 93 of 93 records
- **Intervals:** median 168.70s (p5 0.01s / p95 83758.22s, n=92)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x41
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 93/93 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x41
data.questID  (string, 93/93 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 93/93 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 41/93 records)
    "Succeeded"  x41
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 77 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (29); Unit 4 Dev - Anderson Base (27); Unit 5 Dev (9); Unit 2 Prod (Refactor) (7); Unit 3 Dev (5)
- **Intervals:** median 1.19s (p5 0.12s / p95 691.33s, n=76)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 77/77 records)
    "submitAnswerEvent"  x77
data.answerSubmitted  (string, 77/77 records)
    23 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 77/77 records)
    "Unit 1 - Freshwater"  x28
    "Unit 4 - Flooding"  x27
    "Unit 5"  x9
    "Unit 2 – Watershed"  x7
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 76 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (76)
- **Intervals:** median 0.84s (p5 0.10s / p95 44.30s, n=75)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "On"  x42
    "Off"  x34
data.floor  (string, 76/76 records)
    "4"  x47
    "3"  x18
    "2"  x6
    "1"  x5
data.machineNumber  (string, 76/76 records)
    "One"  x75
    "Two"  x1
data.machineType  (string, 76/76 records)
    "Condenser"  x36
    "Evaporator"  x32
    "DualChamber_Condenser"  x5
    "VentSwitch"  x2
    "DualChamber_Evaporator"  x1
data.room  (string, 76/76 records)
    "3"  x37
    "2"  x26
    "1"  x11
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 31 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (12); Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 3 Dev (3); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 667.58s (p5 8.47s / p95 85713.83s, n=30)
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "DebugMenuStateChanged"  x31
data.isOpened  (bool, 31/31 records)
    false  x31
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 23 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 2 Prod (Refactor) (5); Unit 4 Dev - Dungeon (2); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 1183.70s (p5 67.94s / p95 86515.60s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 17 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (2); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2); MainMenu (1); Unit 1 Dev (1)
- **Intervals:** median 1456.63s (p5 0.91s / p95 172363.58s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    false  x17
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 17 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (17)
- **Intervals:** median 7.56s (p5 1.58s / p95 108.79s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "ChangeCanister"  x17
data.canisterType  (string, 17/17 records)
    "Clay"  x7
    "Sand"  x4
    "Bedrock"  x3
    "Gravel"  x3
data.floor  (string, 17/17 records)
    "5"  x11
    "4"  x6
data.machine  (string, 17/17 records)
    "1"  x15
    "2"  x2
data.row  (string, 17/17 records)
    "TopRow"  x11
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 96.61s (p5 0.05s / p95 296318.36s, n=13)
- **Open findings:** 1 — see sections 5-8
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

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 43180.07s (p5 1065.96s / p95 241965.12s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 10 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dungeon Dev (6); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 2.54s (p5 0.66s / p95 414870.88s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "Close"  x5
    "Open"  x5
data.toolName  (string, 10/10 records, 10 empty-string)
    ""  x10
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 2.78s (p5 1.53s / p95 21.25s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x3
data.boxId  (string, 8/8 records)
    "0"  x3
    "2"  x3
    "1"  x2
data.soilType  (string, 8/8 records)
    "Sand"  x5
    "Gravel"  x2
    "Clay"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2)
- **Intervals:** median 1.31s (p5 0.20s / p95 449162.24s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x7
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x3
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Graph"  x3
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 2.20s (p5 0.52s / p95 4.91s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted Out"  x1
data.featureUsed  (string, 6/6 records)
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records, 1 empty-string)
    "Covered"  x2
    ""  x1
    "Cold"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 88349.73s (p5 15262.62s / p95 527877.96s, n=4)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1086.25s (p5 1086.25s / p95 1086.25s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
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
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `argumentationEvent` actionType: argumentation session: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (93 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "Selected" (14x); "Unselected" (10x); "WaypointMoveEvent" (51x); "WaypointResetEvent" (4x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (24x); "Waypoint" (62x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (25x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*