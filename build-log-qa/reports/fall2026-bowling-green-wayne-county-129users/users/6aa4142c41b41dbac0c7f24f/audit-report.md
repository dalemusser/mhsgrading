# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f24f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f24f
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f24f.jsonl
- **Records:** 14185 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f24f
- **Time span:** 2026-09-23T16:50:15.501000+00:00 .. 2026-10-06T16:56:08.107000+00:00 (312h 5m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f24f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14185 records, 10 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 103 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 6276 | 44.24 | 1 | 4 | 0 | 2026-09-24T16:34:48.735000+00:00 | 2026-10-06T16:27:00.474000+00:00 | 287h 52m |
| InputEvent | 2368 | 16.69 | 1 | 9 | 0 | 2026-09-23T16:53:56.794000+00:00 | 2026-10-06T16:56:08.107000+00:00 | 312h 2m |
| DialogueEvent | 2218 | 15.64 | 1 | 9 | 1370 | 2026-09-23T16:50:56.058000+00:00 | 2026-10-06T16:56:03.034000+00:00 | 312h 5m |
| PlayerPositionEvent | 1962 | 13.83 | 1 | 9 | 0 | 2026-09-23T16:50:34.156000+00:00 | 2026-10-06T16:56:02.507000+00:00 | 312h 5m |
| argumentationNodeEvent | 636 | 4.48 | 1 | 5 | 0 | 2026-09-24T16:26:15.276000+00:00 | 2026-10-06T16:43:55.996000+00:00 | 288h 17m |
| ObjectInterEvent | 346 | 2.44 | 1 | 9 | 0 | 2026-09-23T16:55:45.525000+00:00 | 2026-10-06T16:56:08.104000+00:00 | 312h 0m |
| questEvent | 92 | 0.65 | 1 | 9 | 92 | 2026-09-23T16:50:56.017000+00:00 | 2026-10-06T16:52:24.817000+00:00 | 312h 1m |
| Soil Key Puzzle | 53 | 0.37 | 1 | 3 | 0 | 2026-09-24T16:45:45.070000+00:00 | 2026-09-30T16:58:59.670000+00:00 | 144h 13m |
| argumentationAnswerEvent | 49 | 0.35 | 1 | 5 | 0 | 2026-09-24T16:24:59.334000+00:00 | 2026-10-06T16:43:57.021000+00:00 | 288h 18m |
| TopographicMapEvent | 38 | 0.27 | 1 | 2 | 0 | 2026-09-24T16:35:31.412000+00:00 | 2026-09-30T16:46:04.887000+00:00 | 144h 10m |
| WaterChamberEvent | 33 | 0.23 | 1 | 1 | 0 | 2026-10-05T17:02:38.156000+00:00 | 2026-10-06T16:35:06.367000+00:00 | 23h 32m |
| DEBUGMenu | 22 | 0.16 | 1 | 8 | 0 | 2026-09-23T16:50:34.148000+00:00 | 2026-10-06T16:22:18.844000+00:00 | 311h 31m |
| gameWindowFocusEvent | 19 | 0.13 | 1 | 4 | 0 | 2026-09-23T16:50:15.501000+00:00 | 2026-10-06T16:22:02.285000+00:00 | 311h 31m |
| gameStartEvent | 16 | 0.11 | 1 | 1 | 0 | 2026-09-23T16:50:15.502000+00:00 | 2026-10-06T16:22:02.287000+00:00 | 311h 31m |
| argumentationEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-09-24T16:24:23.307000+00:00 | 2026-10-06T16:43:57.058000+00:00 | 288h 19m |
| SolarStillDesignEvent | 8 | 0.06 | 1 | 1 | 0 | 2026-10-06T16:49:08.489000+00:00 | 2026-10-06T16:49:31.206000+00:00 | 22.7s |
| TerasGardenBox | 8 | 0.06 | 1 | 1 | 0 | 2026-10-05T16:45:03.063000+00:00 | 2026-10-05T16:46:15.670000+00:00 | 1m 12s |
| soilMachine | 6 | 0.04 | 1 | 1 | 0 | 2026-10-01T16:26:45.276000+00:00 | 2026-10-01T16:34:34.194000+00:00 | 7m 48s |
| DaniEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-09-23T17:04:11.582000+00:00 | 2026-09-30T16:44:15.280000+00:00 | 167h 40m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-24T16:30:18.246000+00:00 | 2026-10-06T16:56:08.084000+00:00 | 288h 25m |
| argumentationToolEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-09-24T16:26:02.092000+00:00 | 2026-10-06T16:43:03.626000+00:00 | 288h 17m |
| gameWindowUnfocusEvent | 4 | 0.03 | 1 | 3 | 0 | 2026-09-24T16:44:04.016000+00:00 | 2026-10-01T16:57:50.157000+00:00 | 168h 13m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-05T16:57:36.788000+00:00 | 2026-10-06T16:35:59.139000+00:00 | 23h 38m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 432263.029s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.523s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.location; data.location.x; data.location.y; data.location.z 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 11.297s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 9.485s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 12.221s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 42551.175s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 83858.243s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1976.986s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 173500.87s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
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
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 30 ft; 330 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 9.8x vs baseline. 
  - Observed: 49 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,B,1,I; A,B,C,2,II; A,B,D,2,II; A,C,1,II; A,C,3,II; A,C,4,II; A,C,B,2,II; A,D,2,II; A,D,B,2,II; A,D,C,2,II; B,1,I; B,2,II; B,A,1,I; B,A,2,II; B,C,1,I; B,C,2,II; C,1,I; C,2,II; C,A,2,II; C,D,3,II; D,1,I; D,1,II; D,2,II; D,B,2,II; D,C,2,II; D,C,4,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 636 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 4 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 46 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[148] _id=6ab4050c485cab4c954e8aa8 ts=2026-09-23T16:57:48.8110000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[196] _id=6ab405d4485cab4c954e901a ts=2026-09-23T17:01:07.9990000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[341] _id=6ab54b9e485cab4c9552deb1 ts=2026-09-24T16:11:10.2240000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[6419] _id=6aba93f3485cab4c956a301b ts=2026-09-28T16:21:06.1090000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[5] _id=6ab40347485cab4c954e7d74 ts=2026-09-23T16:50:15.5020000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[279] _id=6ab54ada485cab4c9552dd29 ts=2026-09-24T16:07:53.7450000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[717] _id=6ab5506a485cab4c955316d1 ts=2026-09-24T16:31:38.0730000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[4] _id=6ab40347485cab4c954e7d72 ts=2026-09-23T16:50:15.5010000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[271] _id=6ab54ada485cab4c9552dd27 ts=2026-09-24T16:07:53.7430000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[715] _id=6ab5506a485cab4c955316cf ts=2026-09-24T16:31:38.0720000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 4 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 4} 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[2466] _id=6ab55354485cab4c955344af ts=2026-09-24T16:44:04.0160000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7827] _id=6abbe8c9485cab4c9580e2c1 ts=2026-09-29T16:35:21.4780000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[11018] _id=6abe8e86485cab4c95ac1a3f ts=2026-10-01T16:47:02.3480000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 4 of 38 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[820] _id=6ab55153485cab4c95531fa9 ts=2026-09-24T16:35:31.4120000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[831] _id=6ab55162485cab4c95532021 ts=2026-09-24T16:35:46.6650000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[3037] _id=6ab6a04d485cab4c955914a8 ts=2026-09-25T16:24:46.0060000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 6275 | 0.0 | 0.03 | 165.152 | 1.288 | 346057.938 | 0.36 | 3808 | 9 |
| InputEvent | 2367 | 0.002 | 1.523 | 474.58 | 27.507 | 343550.389 | 0.13 | 29 | 11 |
| DialogueEvent | 2217 | 0.001 | 4.216 | 506.769 | 31.301 | 343468.764 | 0.12 | 643 | 9 |
| PlayerPositionEvent | 1948 | 9.866 | 10.0 | 576.643 | 10.033 | 343461.32 | 0.1 | 0 | 8 |
| argumentationNodeEvent | 635 | 0.009 | 0.34 | 1634.426 | 8.712 | 516654.558 | 0.04 | 106 | 4 |
| ObjectInterEvent | 345 | 0.0 | 7.755 | 3255.718 | 355.766 | 343604.367 | 0.02 | 5 | 13 |
| questEvent | 91 | 0.001 | 182.044 | 12343.833 | 84219.256 | 343613.72 | 0.0 | 17 | 16 |
| Soil Key Puzzle | 52 | 0.155 | 0.978 | 9984.512 | 38901.727 | 345974.507 | 0.01 | 0 | 4 |
| argumentationAnswerEvent | 48 | 0.553 | 12.221 | 21623.702 | 86458.946 | 516759.933 | 0.0 | 0 | 4 |
| TopographicMapEvent | 37 | 0.02 | 11.297 | 14027.932 | 86327.616 | 258724.676 | 0.0 | 3 | 6 |
| WaterChamberEvent | 32 | 0.538 | 9.485 | 2648.382 | 96.327 | 84006.412 | 0.02 | 0 | 1 |
| DEBUGMenu | 21 | 53.548 | 1087.477 | 53404.986 | 259124.256 | 343611.515 | 0.0 | 0 | 15 |
| gameWindowFocusEvent | 18 | 51.371 | 1976.986 | 62305.932 | 271772.249 | 343451.715 | 0.0 | 0 | 14 |
| gameStartEvent | 15 | 51.371 | 83858.243 | 74767.119 | 285113.393 | 345757.801 | 0.0 | 0 | 11 |
| argumentationEvent | 13 | 0.026 | 109.509 | 79844.135 | 415165.926 | 516657.52 | 0.0 | 2 | 5 |
| SolarStillDesignEvent | 7 | 0.973 | 2.145 | 3.245 | 6.212 | 6.808 | 18.49 | 0 | 0 |
| TerasGardenBox | 7 | 0.494 | 4.104 | 10.372 | 29.972 | 35.086 | 5.78 | 0 | 0 |
| soilMachine | 5 | 22.527 | 48.97 | 93.784 | 193.093 | 198.666 | 0.64 | 0 | 0 |
| DaniEvent | 3 | 1.335 | 1.841 | 201201.233 | 543240.654 | 603600.522 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 86331.739 | 432263.029 | 346116.613 | 511005.866 | 519755.07 | 0.0 | 0 | 3 |
| argumentationToolEvent | 3 | 0.837 | 9.521 | 345940.511 | 934031.01 | 1037811.176 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 3 | 647.809 | 173500.87 | 201875.38 | 405679.803 | 431477.462 | 0.0 | 0 | 3 |
| chatEvent | 2 | 820.38 | 42551.175 | 42551.176 | 80108.891 | 84281.971 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[11228] _id=6abe9104485cab4c95ac36ce ts=2026-10-01T16:57:40.0710000Z == 6aa4142c41b41dbac0c7f24f.jsonl[11229] _id=6abe9104485cab4c95ac36d2 ts=2026-10-01T16:57:40.0710000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 288 group(s), 392 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[805] _id=6ab5513e485cab4c95531ee5 ts=2026-09-24T16:35:09.6890000Z == 6aa4142c41b41dbac0c7f24f.jsonl[800] _id=6ab5513f485cab4c95531ee9 ts=2026-09-24T16:35:09.6890000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[802] _id=6ab5513f485cab4c95531ef1 ts=2026-09-24T16:35:09.8540000Z == 6aa4142c41b41dbac0c7f24f.jsonl[808] _id=6ab5513f485cab4c95531ef5 ts=2026-09-24T16:35:09.8540000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[862] _id=6ab55184485cab4c955320d3 ts=2026-09-24T16:36:19.7400000Z == 6aa4142c41b41dbac0c7f24f.jsonl[850] _id=6ab55184485cab4c955320d5 ts=2026-09-24T16:36:19.7400000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 18 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4142c41b41dbac0c7f24f.jsonl[108] _id=6ab40491485cab4c954e8610 ts=2026-09-23T16:55:45.5250000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[99] _id=6ab40491485cab4c954e8612 ts=2026-09-23T16:55:45.5330000Z`; `2ms: 6aa4142c41b41dbac0c7f24f.jsonl[276] _id=6ab54b2a485cab4c9552dd89 ts=2026-09-24T16:09:13.9170000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[305] _id=6ab54b2a485cab4c9552dd8b ts=2026-09-24T16:09:13.9190000Z`; `879ms: 6aa4142c41b41dbac0c7f24f.jsonl[9894] _id=6abd401a485cab4c958edc12 ts=2026-09-30T17:00:04.5960000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[9926] _id=6abd401b485cab4c958edc4f ts=2026-09-30T17:00:05.4750000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1047 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `165ms: 6aa4142c41b41dbac0c7f24f.jsonl[807] _id=6ab5513f485cab4c95531eef ts=2026-09-24T16:35:09.6890000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[802] _id=6ab5513f485cab4c95531ef1 ts=2026-09-24T16:35:09.8540000Z`; `18ms: 6aa4142c41b41dbac0c7f24f.jsonl[869] _id=6ab55185485cab4c955320e9 ts=2026-09-24T16:36:19.8300000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[853] _id=6ab55185485cab4c955320eb ts=2026-09-24T16:36:19.8480000Z`; `451ms: 6aa4142c41b41dbac0c7f24f.jsonl[857] _id=6ab55186485cab4c955320f7 ts=2026-09-24T16:36:19.9300000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[872] _id=6ab55186485cab4c955320f9 ts=2026-09-24T16:36:20.3810000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `181ms: 6aa4142c41b41dbac0c7f24f.jsonl[5316] _id=6ab6a818485cab4c955d0995 ts=2026-09-25T16:58:00.3240000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[5333] _id=6ab6a818485cab4c955d0997 ts=2026-09-25T16:58:00.5050000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `494ms: 6aa4142c41b41dbac0c7f24f.jsonl[12124] _id=6ac3d41ade269131f9ae0192 ts=2026-10-05T16:45:13.9770000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[12121] _id=6ac3d41ade269131f9ae019b ts=2026-10-05T16:45:14.4710000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6aa4142c41b41dbac0c7f24f.jsonl[5199] _id=6ab6a623485cab4c955ccf7c ts=2026-09-25T16:49:39.7210000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[5202] _id=6ab6a623485cab4c955ccf90 ts=2026-09-25T16:49:39.7470000Z`; `20ms: 6aa4142c41b41dbac0c7f24f.jsonl[5202] _id=6ab6a623485cab4c955ccf90 ts=2026-09-25T16:49:39.7470000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[5203] _id=6ab6a624485cab4c955ccfd9 ts=2026-09-25T16:49:39.7670000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `553ms: 6aa4142c41b41dbac0c7f24f.jsonl[11648] _id=6ac3d11dde269131f9adc625 ts=2026-10-05T16:32:29.6360000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[11651] _id=6ac3d11ede269131f9adc645 ts=2026-10-05T16:32:30.1890000Z`; `988ms: 6aa4142c41b41dbac0c7f24f.jsonl[11651] _id=6ac3d11ede269131f9adc645 ts=2026-10-05T16:32:30.1890000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[11653] _id=6ac3d11fde269131f9adc68b ts=2026-10-05T16:32:31.1770000Z`; `945ms: 6aa4142c41b41dbac0c7f24f.jsonl[11923] _id=6ac3d271de269131f9ade0d8 ts=2026-10-05T16:38:09.4340000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[11921] _id=6ac3d272de269131f9ade0ed ts=2026-10-05T16:38:10.3790000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `47ms: 6aa4142c41b41dbac0c7f24f.jsonl[8413] _id=6abbee34485cab4c95828ed4 ts=2026-09-29T16:58:27.9810000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[8415] _id=6abbee34485cab4c95828eda ts=2026-09-29T16:58:28.0280000Z`; `26ms: 6aa4142c41b41dbac0c7f24f.jsonl[11994] _id=6ac3d2bede269131f9ade7db ts=2026-10-05T16:39:25.9770000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[11986] _id=6ac3d2bede269131f9ade7e9 ts=2026-10-05T16:39:26.0030000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 89 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `571ms: 6aa4142c41b41dbac0c7f24f.jsonl[549] _id=6ab54f30485cab4c95530327 ts=2026-09-24T16:26:24.4460000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[557] _id=6ab54f31485cab4c9553033d ts=2026-09-24T16:26:25.0170000Z`; `277ms: 6aa4142c41b41dbac0c7f24f.jsonl[556] _id=6ab54f31485cab4c95530339 ts=2026-09-24T16:26:24.9890000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[558] _id=6ab54f31485cab4c95530346 ts=2026-09-24T16:26:25.2660000Z`; `835ms: 6aa4142c41b41dbac0c7f24f.jsonl[557] _id=6ab54f31485cab4c9553033d ts=2026-09-24T16:26:25.0170000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[550] _id=6ab54f31485cab4c95530357 ts=2026-09-24T16:26:25.8520000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4142c41b41dbac0c7f24f.jsonl[6419] _id=6aba93f3485cab4c956a301b ts=2026-09-28T16:21:06.1090000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[6417] _id=6aba93f3485cab4c956a3036 ts=2026-09-28T16:21:06.1110000Z`; `1ms: 6aa4142c41b41dbac0c7f24f.jsonl[13919] _id=6ac52590de269131f9b5399a ts=2026-10-06T16:45:04.8850000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[13921] _id=6ac52591de269131f9b5399f ts=2026-10-06T16:45:04.8860000Z`; `5ms: 6aa4142c41b41dbac0c7f24f.jsonl[14089] _id=6ac526efde269131f9b56b64 ts=2026-10-06T16:50:55.2260000Z ~ 6aa4142c41b41dbac0c7f24f.jsonl[14086] _id=6ac526efde269131f9b56b6b ts=2026-10-06T16:50:55.2310000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4142c41b41dbac0c7f24f.jsonl[11192] _id=6abe907f485cab4c95ac30a4 ts=2026-10-01T16:55:27.3530000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11285] _id=6ac3cebade269131f9ada3e1 ts=2026-10-05T16:22:18.8680000Z; 71h 58m: 6aa4142c41b41dbac0c7f24f.jsonl[2938] _id=6ab69fb6485cab4c9558b867 ts=2026-09-25T16:22:15.0350000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6415] _id=6aba93eb485cab4c956a2af6 ts=2026-09-28T16:20:59.2910000Z; 24h 7m: 6aa4142c41b41dbac0c7f24f.jsonl[6415] _id=6aba93eb485cab4c956a2af6 ts=2026-09-28T16:20:59.2910000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7748] _id=6abbe728485cab4c9580c15b ts=2026-09-29T16:28:24.5490000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 40m 
  - Evidence: 167h 40m: 6aa4142c41b41dbac0c7f24f.jsonl[243] _id=6ab4068d485cab4c954e93ea ts=2026-09-23T17:04:13.4230000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[9301] _id=6abd3c5e485cab4c958e88e8 ts=2026-09-30T16:44:13.9450000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4142c41b41dbac0c7f24f.jsonl[11273] _id=6abe9112485cab4c95ac3742 ts=2026-10-01T16:57:54.6730000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11287] _id=6ac3cebfde269131f9ada3f5 ts=2026-10-05T16:22:23.4370000Z; 71h 16m: 6aa4142c41b41dbac0c7f24f.jsonl[6407] _id=6ab6a9ba485cab4c955d366b ts=2026-09-25T17:04:58.3820000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6462] _id=6aba93ff485cab4c956a3919 ts=2026-09-28T16:21:19.1350000Z; 23h 34m: 6aa4142c41b41dbac0c7f24f.jsonl[2933] _id=6ab55440485cab4c95534eb7 ts=2026-09-24T16:48:00.8820000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[2950] _id=6ab69fdf485cab4c9558cf91 ts=2026-09-25T16:22:55.3310000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 643 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24f.jsonl[11657] _id=6ac3d122de269131f9adc740 ts=2026-10-05T16:32:34.2580000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11655] _id=6ac3d122de269131f9adc747 ts=2026-10-05T16:32:34.2590000Z; 1ms: 6aa4142c41b41dbac0c7f24f.jsonl[11940] _id=6ac3d29ede269131f9ade563 ts=2026-10-05T16:38:54.6280000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11941] _id=6ac3d29ede269131f9ade567 ts=2026-10-05T16:38:54.6290000Z; 1ms: 6aa4142c41b41dbac0c7f24f.jsonl[12037] _id=6ac3d32ede269131f9adeff0 ts=2026-10-05T16:41:18.4260000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[12038] _id=6ac3d32ede269131f9adeff3 ts=2026-10-05T16:41:18.4270000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 22m 
  - Evidence: 144h 22m: 6aa4142c41b41dbac0c7f24f.jsonl[713] _id=6ab5501a485cab4c95531315 ts=2026-09-24T16:30:18.2460000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[9465] _id=6abd3e65485cab4c958eb7e5 ts=2026-09-30T16:52:53.3160000Z; 120h 4m: 6aa4142c41b41dbac0c7f24f.jsonl[9465] _id=6abd3e65485cab4c958eb7e5 ts=2026-09-30T16:52:53.3160000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[12335] _id=6ac3d6ecde269131f9ae4a17 ts=2026-10-05T16:57:16.3450000Z; 23h 58m: 6aa4142c41b41dbac0c7f24f.jsonl[12335] _id=6ac3d6ecde269131f9ae4a17 ts=2026-10-05T16:57:16.3450000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[14184] _id=6ac52828de269131f9b5a44e ts=2026-10-06T16:56:08.0840000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4142c41b41dbac0c7f24f.jsonl[11262] _id=6abe9102485cab4c95ac36bc ts=2026-10-01T16:57:38.9260000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11297] _id=6ac3cf01de269131f9ada455 ts=2026-10-05T16:23:29.3150000Z; 71h 17m: 6aa4142c41b41dbac0c7f24f.jsonl[6382] _id=6ab6a97a485cab4c955d3371 ts=2026-09-25T17:03:54.9880000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6426] _id=6aba93f5485cab4c956a3161 ts=2026-09-28T16:21:09.1210000Z; 23h 38m: 6aa4142c41b41dbac0c7f24f.jsonl[7534] _id=6aba9c6e485cab4c956b07a3 ts=2026-09-28T16:57:18.7830000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7834] _id=6abbe8eb485cab4c9580e38f ts=2026-09-29T16:35:54.5880000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 29 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f24f.jsonl[14045] _id=6ac526bdde269131f9b565b1 ts=2026-10-06T16:50:05.2600000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[14051] _id=6ac526bdde269131f9b565b3 ts=2026-10-06T16:50:05.2620000Z; 2ms: 6aa4142c41b41dbac0c7f24f.jsonl[7350] _id=6aba9afb485cab4c956ad558 ts=2026-09-28T16:51:07.0460000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7348] _id=6aba9afb485cab4c956ad55a ts=2026-09-28T16:51:07.0480000Z; 3ms: 6aa4142c41b41dbac0c7f24f.jsonl[13553] _id=6ac522e8de269131f9b513a5 ts=2026-10-06T16:33:44.5820000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13554] _id=6ac522e8de269131f9b513a7 ts=2026-10-06T16:33:44.5850000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4142c41b41dbac0c7f24f.jsonl[11229] _id=6abe9104485cab4c95ac36d2 ts=2026-10-01T16:57:40.0710000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11311] _id=6ac3cf38de269131f9ada551 ts=2026-10-05T16:24:24.4380000Z; 71h 19m: 6aa4142c41b41dbac0c7f24f.jsonl[6339] _id=6ab6a977485cab4c955d32ed ts=2026-09-25T17:03:51.2830000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6526] _id=6aba948d485cab4c956a7072 ts=2026-09-28T16:23:41.6500000Z; 23h 44m: 6aa4142c41b41dbac0c7f24f.jsonl[7519] _id=6aba9c3f485cab4c956af1b8 ts=2026-09-28T16:56:31.5180000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7907] _id=6abbea22485cab4c9581010a ts=2026-09-29T16:41:06.3930000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24f.jsonl[11228] _id=6abe9104485cab4c95ac36ce ts=2026-10-01T16:57:40.0710000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11229] _id=6abe9104485cab4c95ac36d2 ts=2026-10-01T16:57:40.0710000Z; 2ms: 6aa4142c41b41dbac0c7f24f.jsonl[11365] _id=6ac3cf8fde269131f9ada727 ts=2026-10-05T16:25:51.0740000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11366] _id=6ac3cf8fde269131f9ada729 ts=2026-10-05T16:25:51.0760000Z; 2ms: 6aa4142c41b41dbac0c7f24f.jsonl[11411] _id=6ac3cfdede269131f9ada901 ts=2026-10-05T16:27:09.9040000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11412] _id=6ac3cfdede269131f9ada905 ts=2026-10-05T16:27:09.9060000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4142c41b41dbac0c7f24f.jsonl[11268] _id=6abe9115485cab4c95ac3752 ts=2026-10-01T16:57:57.5520000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11289] _id=6ac3cebede269131f9ada3ef ts=2026-10-05T16:22:18.8720000Z; 71h 16m: 6aa4142c41b41dbac0c7f24f.jsonl[6400] _id=6ab6a9b6485cab4c955d3643 ts=2026-09-25T17:04:54.3150000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6416] _id=6aba93f2485cab4c956a2f3a ts=2026-09-28T16:20:59.3020000Z; 23h 34m: 6aa4142c41b41dbac0c7f24f.jsonl[2935] _id=6ab5543c485cab4c95534e8f ts=2026-09-24T16:47:56.9370000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[2939] _id=6ab69fb8485cab4c9558b92c ts=2026-09-25T16:22:15.0420000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 96h 7m 
  - Evidence: 96h 7m: 6aa4142c41b41dbac0c7f24f.jsonl[11117] _id=6abe8f3d485cab4c95ac211d ts=2026-10-01T16:50:04.4650000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[12351] _id=6ac3d707de269131f9ae4cb3 ts=2026-10-05T16:57:42.4030000Z; 71h 17m: 6aa4142c41b41dbac0c7f24f.jsonl[6358] _id=6ab6a97d485cab4c955d33b7 ts=2026-09-25T17:03:55.1660000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6422] _id=6aba93f3485cab4c956a306d ts=2026-09-28T16:21:06.3980000Z; 47h 57m: 6aa4142c41b41dbac0c7f24f.jsonl[6998] _id=6aba95ea485cab4c956a99f0 ts=2026-09-28T16:29:29.8160000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[8623] _id=6abd384f485cab4c958da2bc ts=2026-09-30T16:26:54.0770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3808 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24f.jsonl[10001] _id=6abd4034485cab4c958edff7 ts=2026-09-30T17:00:35.8820000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[10002] _id=6abd4034485cab4c958edffc ts=2026-09-30T17:00:35.8820000Z; 0ms: 6aa4142c41b41dbac0c7f24f.jsonl[10004] _id=6abd4035485cab4c958ee016 ts=2026-09-30T17:00:36.2210000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[10007] _id=6abd4035485cab4c958ee01a ts=2026-09-30T17:00:36.2210000Z; 0ms: 6aa4142c41b41dbac0c7f24f.jsonl[10005] _id=6abd4035485cab4c958ee00d ts=2026-09-30T17:00:36.0280000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[9996] _id=6abd4035485cab4c958ee010 ts=2026-09-30T17:00:36.0280000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa4142c41b41dbac0c7f24f.jsonl[5368] _id=6ab6a830485cab4c955d0acf ts=2026-09-25T16:58:24.8970000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[8529] _id=6abbefa7485cab4c9582b390 ts=2026-09-29T17:04:39.4040000Z; 24h 11m: 6aa4142c41b41dbac0c7f24f.jsonl[2895] _id=6ab553bc485cab4c955349e5 ts=2026-09-24T16:45:48.0580000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[5315] _id=6ab6a7fd485cab4c955d0841 ts=2026-09-25T16:57:33.9330000Z; 23h 21m: 6aa4142c41b41dbac0c7f24f.jsonl[8529] _id=6abbefa7485cab4c9582b390 ts=2026-09-29T17:04:39.4040000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[8588] _id=6abd3811485cab4c958d9c7a ts=2026-09-30T16:25:53.6150000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 71h 52m 
  - Evidence: 71h 52m: 6aa4142c41b41dbac0c7f24f.jsonl[5206] _id=6ab6a630485cab4c955cd45d ts=2026-09-25T16:49:52.4980000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7205] _id=6aba98d5485cab4c956ac43b ts=2026-09-28T16:41:57.1740000Z; 24h 2m: 6aa4142c41b41dbac0c7f24f.jsonl[7911] _id=6abbea18485cab4c958100c8 ts=2026-09-29T16:40:56.1610000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[9285] _id=6abd3c26485cab4c958e751c ts=2026-09-30T16:43:18.3720000Z; 23h 57m: 6aa4142c41b41dbac0c7f24f.jsonl[6954] _id=6aba990a485cab4c956ac5a4 ts=2026-09-28T16:42:50.8600000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7910] _id=6abbea0c485cab4c95810045 ts=2026-09-29T16:40:44.8270000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.020s..0.026s shown 
  - Evidence: 20ms: 6aa4142c41b41dbac0c7f24f.jsonl[5196] _id=6ab6a623485cab4c955ccf45 ts=2026-09-25T16:49:39.7010000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[5199] _id=6ab6a623485cab4c955ccf7c ts=2026-09-25T16:49:39.7210000Z; 20ms: 6aa4142c41b41dbac0c7f24f.jsonl[5202] _id=6ab6a623485cab4c955ccf90 ts=2026-09-25T16:49:39.7470000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[5203] _id=6ab6a624485cab4c955ccfd9 ts=2026-09-25T16:49:39.7670000Z; 26ms: 6aa4142c41b41dbac0c7f24f.jsonl[5199] _id=6ab6a623485cab4c955ccf7c ts=2026-09-25T16:49:39.7210000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[5202] _id=6ab6a623485cab4c955ccf90 ts=2026-09-25T16:49:39.7470000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 20m 
  - Evidence: 23h 20m: 6aa4142c41b41dbac0c7f24f.jsonl[12898] _id=6ac3d8e0de269131f9ae767d ts=2026-10-05T17:05:36.5250000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13198] _id=6ac52107de269131f9b4fadf ts=2026-10-06T16:25:42.9370000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 32m 
  - Evidence: 143h 32m: 6aa4142c41b41dbac0c7f24f.jsonl[8410] _id=6abbee33485cab4c95828ecf ts=2026-09-29T16:58:27.9410000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11559] _id=6ac3d0cbde269131f9adbbe3 ts=2026-10-05T16:31:07.8740000Z; 96h 32m: 6aa4142c41b41dbac0c7f24f.jsonl[609] _id=6ab54f5e485cab4c95530725 ts=2026-09-24T16:27:10.7620000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7606] _id=6aba9d1a485cab4c956b4aad ts=2026-09-28T17:00:10.0070000Z; 24h 3m: 6aa4142c41b41dbac0c7f24f.jsonl[11993] _id=6ac3d2bede269131f9ade7d9 ts=2026-10-05T16:39:25.9590000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13788] _id=6ac52505de269131f9b52b63 ts=2026-10-06T16:42:45.2800000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6aa4142c41b41dbac0c7f24f.jsonl[8415] _id=6abbee34485cab4c95828eda ts=2026-09-29T16:58:28.0280000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11449] _id=6ac3d065de269131f9adb6ad ts=2026-10-05T16:29:25.5480000Z; 96h 31m: 6aa4142c41b41dbac0c7f24f.jsonl[605] _id=6ab54f5e485cab4c95530727 ts=2026-09-24T16:27:10.7840000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7562] _id=6aba9ccf485cab4c956b30a5 ts=2026-09-28T16:58:55.6470000Z; 24h 2m: 6aa4142c41b41dbac0c7f24f.jsonl[11986] _id=6ac3d2bede269131f9ade7e9 ts=2026-10-05T16:39:26.0030000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13743] _id=6ac524dfde269131f9b528c1 ts=2026-10-06T16:42:07.5490000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.047s shown 
  - Evidence: 26ms: 6aa4142c41b41dbac0c7f24f.jsonl[11994] _id=6ac3d2bede269131f9ade7db ts=2026-10-05T16:39:25.9770000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11986] _id=6ac3d2bede269131f9ade7e9 ts=2026-10-05T16:39:26.0030000Z; 47ms: 6aa4142c41b41dbac0c7f24f.jsonl[8413] _id=6abbee34485cab4c95828ed4 ts=2026-09-29T16:58:27.9810000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[8415] _id=6abbee34485cab4c95828eda ts=2026-09-29T16:58:28.0280000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6aa4142c41b41dbac0c7f24f.jsonl[8409] _id=6abbee32485cab4c95828ec7 ts=2026-09-29T16:58:26.7060000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11478] _id=6ac3d061de269131f9adb669 ts=2026-10-05T16:29:21.2640000Z; 96h 31m: 6aa4142c41b41dbac0c7f24f.jsonl[528] _id=6ab54f55485cab4c955306ba ts=2026-09-24T16:27:01.1570000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7559] _id=6aba9ccc485cab4c956b2f88 ts=2026-09-28T16:58:52.5780000Z; 24h 2m: 6aa4142c41b41dbac0c7f24f.jsonl[11990] _id=6ac3d2bdde269131f9ade7cf ts=2026-10-05T16:39:25.3210000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13744] _id=6ac524e2de269131f9b528ed ts=2026-10-06T16:42:10.1740000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 106 interval(s) ≤ 0.009s..0.024s shown 
  - Evidence: 9ms: 6aa4142c41b41dbac0c7f24f.jsonl[11665] _id=6ac3d145de269131f9adcb88 ts=2026-10-05T16:33:08.9350000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11680] _id=6ac3d145de269131f9adcb90 ts=2026-10-05T16:33:08.9440000Z; 23ms: 6aa4142c41b41dbac0c7f24f.jsonl[13840] _id=6ac52532de269131f9b52f65 ts=2026-10-06T16:43:30.7790000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13838] _id=6ac52532de269131f9b52f69 ts=2026-10-06T16:43:30.8020000Z; 24ms: 6aa4142c41b41dbac0c7f24f.jsonl[13774] _id=6ac524f9de269131f9b52ab1 ts=2026-10-06T16:42:33.1580000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13775] _id=6ac524f9de269131f9b52ab4 ts=2026-10-06T16:42:33.1820000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 288h 16m 
  - Evidence: 288h 16m: 6aa4142c41b41dbac0c7f24f.jsonl[552] _id=6ab54f24485cab4c955301cb ts=2026-09-24T16:26:12.4500000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13792] _id=6ac52517de269131f9b52ce3 ts=2026-10-06T16:43:03.6260000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 24m 
  - Evidence: 23h 24m: 6aa4142c41b41dbac0c7f24f.jsonl[12340] _id=6ac3d700de269131f9ae4c0a ts=2026-10-05T16:57:36.7880000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[12938] _id=6ac5203ade269131f9b4f26d ts=2026-10-06T16:22:18.7590000Z; 13m 40s: 6aa4142c41b41dbac0c7f24f.jsonl[12938] _id=6ac5203ade269131f9b4f26d ts=2026-10-06T16:22:18.7590000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13620] _id=6ac5236fde269131f9b51abf ts=2026-10-06T16:35:59.1390000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa4142c41b41dbac0c7f24f.jsonl[10386] _id=6abe880f485cab4c95abd47a ts=2026-10-01T16:19:27.0060000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11283] _id=6ac3ceacde269131f9ada3b3 ts=2026-10-05T16:22:04.8070000Z; 71h 58m: 6aa4142c41b41dbac0c7f24f.jsonl[2936] _id=6ab69fb1485cab4c9558b50f ts=2026-09-25T16:22:09.3650000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6411] _id=6aba93e4485cab4c956a25e3 ts=2026-09-28T16:20:52.2970000Z; 24h 7m: 6aa4142c41b41dbac0c7f24f.jsonl[6411] _id=6aba93e4485cab4c956a25e3 ts=2026-09-28T16:20:52.2970000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7745] _id=6abbe71f485cab4c9580c13d ts=2026-09-29T16:28:14.8590000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4142c41b41dbac0c7f24f.jsonl[11271] _id=6abe9111485cab4c95ac3738 ts=2026-10-01T16:57:53.0910000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11284] _id=6ac3ceacde269131f9ada3b1 ts=2026-10-05T16:22:04.8060000Z; 71h 58m: 6aa4142c41b41dbac0c7f24f.jsonl[2937] _id=6ab69fb1485cab4c9558b505 ts=2026-09-25T16:22:09.3630000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6412] _id=6aba93e4485cab4c956a25bc ts=2026-09-28T16:20:52.2950000Z; 24h 7m: 6aa4142c41b41dbac0c7f24f.jsonl[6412] _id=6aba93e4485cab4c956a25bc ts=2026-09-28T16:20:52.2950000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7746] _id=6abbe71e485cab4c9580c13b ts=2026-09-29T16:28:14.8580000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6aa4142c41b41dbac0c7f24f.jsonl[2466] _id=6ab55354485cab4c955344af ts=2026-09-24T16:44:04.0160000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[7827] _id=6abbe8c9485cab4c9580e2c1 ts=2026-09-29T16:35:21.4780000Z; 48h 11m: 6aa4142c41b41dbac0c7f24f.jsonl[7827] _id=6abbe8c9485cab4c9580e2c1 ts=2026-09-29T16:35:21.4780000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11018] _id=6abe8e86485cab4c95ac1a3f ts=2026-10-01T16:47:02.3480000Z; 10m 47s: 6aa4142c41b41dbac0c7f24f.jsonl[11018] _id=6abe8e86485cab4c95ac1a3f ts=2026-10-01T16:47:02.3480000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11272] _id=6abe910e485cab4c95ac372a ts=2026-10-01T16:57:50.1570000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4142c41b41dbac0c7f24f.jsonl[11145] _id=6abe9080485cab4c95ac30b4 ts=2026-10-01T16:55:28.5220000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[11286] _id=6ac3cebede269131f9ada3f1 ts=2026-10-05T16:22:22.2420000Z; 71h 16m: 6aa4142c41b41dbac0c7f24f.jsonl[6359] _id=6ab6a989485cab4c955d3443 ts=2026-09-25T17:04:09.6020000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[6419] _id=6aba93f3485cab4c956a301b ts=2026-09-28T16:21:06.1090000Z; 23h 35m: 6aa4142c41b41dbac0c7f24f.jsonl[2886] _id=6ab553e1485cab4c95534afb ts=2026-09-24T16:46:25.0210000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[2940] _id=6ab69fb8485cab4c9558b93d ts=2026-09-25T16:22:16.0650000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24f.jsonl[13919] _id=6ac52590de269131f9b5399a ts=2026-10-06T16:45:04.8850000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13921] _id=6ac52591de269131f9b5399f ts=2026-10-06T16:45:04.8860000Z; 2ms: 6aa4142c41b41dbac0c7f24f.jsonl[13357] _id=6ac52171de269131f9b4ffe1 ts=2026-10-06T16:27:29.5660000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[13355] _id=6ac52171de269131f9b4ffe3 ts=2026-10-06T16:27:29.5680000Z; 2ms: 6aa4142c41b41dbac0c7f24f.jsonl[498] _id=6ab54e6b485cab4c9552f655 ts=2026-09-24T16:23:07.2220000Z -> 6aa4142c41b41dbac0c7f24f.jsonl[505] _id=6ab54e6b485cab4c9552f657 ts=2026-09-24T16:23:07.2240000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[494] _id=6ab54e58485cab4c9552f593 ts=2026-09-24T16:22:48.2910000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[614] _id=6ab54f73485cab4c955308bb ts=2026-09-24T16:27:31.2590000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[5200] _id=6ab6a624485cab4c955ccfa3 ts=2026-09-25T16:49:39.7520000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 130 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[982] _id=6ab551ae485cab4c9553229b ts=2026-09-24T16:36:59.9720000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[1053] _id=6ab551ce485cab4c955323db ts=2026-09-24T16:37:33.4770000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[1064] _id=6ab551ce485cab4c955323e5 ts=2026-09-24T16:37:33.5620000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 467 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[841] _id=6ab55193485cab4c95532145 ts=2026-09-24T16:35:07.7910000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[809] _id=6ab5513f485cab4c95531ef3 ts=2026-09-24T16:35:09.8540000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[764] _id=6ab5513f485cab4c95531ef9 ts=2026-09-24T16:35:09.8540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[8415] _id=6abbee34485cab4c95828eda ts=2026-09-29T16:58:28.0280000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[11986] _id=6ac3d2bede269131f9ade7e9 ts=2026-10-05T16:39:26.0030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[7608] _id=6aba9d18485cab4c956b4a6b ts=2026-09-28T17:00:07.9900000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7613] _id=6aba9d19485cab4c956b4a76 ts=2026-09-28T17:00:08.0550000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7605] _id=6aba9d19485cab4c956b4a83 ts=2026-09-28T17:00:08.3160000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[12340] _id=6ac3d700de269131f9ae4c0a ts=2026-10-05T16:57:36.7880000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[12938] _id=6ac5203ade269131f9b4f26d ts=2026-10-06T16:22:18.7590000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[13620] _id=6ac5236fde269131f9b51abf ts=2026-10-06T16:35:59.1390000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[7750] _id=6abbe72a485cab4c9580c161 ts=2026-09-29T16:28:25.3340000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7774] _id=6abbe7c9485cab4c9580cc91 ts=2026-09-29T16:31:05.0270000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7797] _id=6abbe822485cab4c9580d939 ts=2026-09-29T16:32:34.3510000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[2] _id=6ab4035f485cab4c954e7dfa ts=?`; `6aa4142c41b41dbac0c7f24f.jsonl[7829] _id=6abbe8ea485cab4c9580e389 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 885 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[1140] _id=6ab551da485cab4c9553246b ts=2026-09-24T16:37:46.0180000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[1130] _id=6ab551dd485cab4c9553249f ts=2026-09-24T16:37:48.0400000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[1075] _id=6ab551de485cab4c955324a7 ts=2026-09-24T16:37:49.8030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1321 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[800] _id=6ab5513f485cab4c95531ee9 ts=2026-09-24T16:35:09.6890000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[806] _id=6ab5513f485cab4c95531eeb ts=2026-09-24T16:35:09.6890000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[801] _id=6ab5513f485cab4c95531eed ts=2026-09-24T16:35:09.6890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[8588] _id=6abd3811485cab4c958d9c7a ts=2026-09-30T16:25:53.6150000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[5202] _id=6ab6a623485cab4c955ccf90 ts=2026-09-25T16:49:39.7470000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[5203] _id=6ab6a624485cab4c955ccfd9 ts=2026-09-25T16:49:39.7670000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7205] _id=6aba98d5485cab4c956ac43b ts=2026-09-28T16:41:57.1740000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 43 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[7604] _id=6aba9d16485cab4c956b4a1b ts=2026-09-28T17:00:03.7820000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7597] _id=6aba9d17485cab4c956b4a2b ts=2026-09-28T17:00:06.4190000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[7600] _id=6aba9d17485cab4c956b4a3d ts=2026-09-28T17:00:06.6600000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[551] _id=6ab54f23485cab4c955301af ts=2026-09-24T16:26:11.6130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 PlayerPositionEvent record in 'Unit 2 Prod (Refactor)' inside a 'Unit 3 Dev' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[7838] _id=6abbe901485cab4c9580e3f5 ts=2026-09-29T16:36:17.3560000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 427 start, 421 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 202 unmatched 'BecameCameraCentered' (totals: 1184 open, 1112 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 143 unmatched 'BecameVisible' (totals: 1828 open, 2152 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 18 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationNodeHoverStart' (totals: 274 open, 274 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 52 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 470 of 14182 adjacent _id pairs reverse in client time; worst 105.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f24f.jsonl[753] _id=6ab55191485cab4c9553212d ts=2026-09-24T16:36:33.6870000Z`; `6aa4142c41b41dbac0c7f24f.jsonl[754] _id=6ab55192485cab4c95532131 ts=2026-09-24T16:34:48.7350000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.15s, min -106.03s, max +0.20s over 14183 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f24f\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 6276 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (4750); Unit 5 Dev - Dungeon (702); Unit 4 Dev (672); Unit 3 Dungeon Dev (152)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.29s, n=6275)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6276/6276 records)
    "BecameInvisible"  x2152
    "BecameVisible"  x1828
    "BecameCameraCentered"  x1184
    "BecameCameraUncentered"  x1112
data.pieceId  (string, 6276/6276 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 6276/6276 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2368 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (693); Unit 4 Dev - Dungeon (331); Unit 3 Dev (321); Unit 5 Dev - Dungeon (282); Unit 3 Dungeon Dev (245); Unit 4 Dev (153); Unit 1 Dev (149); Unit 4 Dev - Anderson Base (118); Unit 5 Dev (76)
- **Intervals:** median 1.52s (p5 0.14s / p95 27.51s, n=2367)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2368/2368 records)
    "pressed"  x2368
data.actionType  (string, 2368/2368 records)
    "Move"  x1662
    "Interact"  x506
    "Sprint"  x79
    "Jump"  x59
    "Ascend"  x33
    "Hoverboard"  x18
    "Map"  x6
    "Descend"  x4
    "Pause"  x1
data.key  (string, 2368/2368 records, 1 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2368/2368 records)
    "Player"  x1939
    "Drone"  x429
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2218 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (667); Unit 3 Dev (319); Unit 4 Dev (261); Unit 1 Dev (243); Unit 5 Dev (221); Unit 4 Dev - Anderson Base (174); Unit 4 Dev - Dungeon (118); Unit 3 Dungeon Dev (113); Unit 5 Dev - Dungeon (102)
- **eventKey:** present on 1370 of 2218 records
- **Intervals:** median 4.22s (p5 0.01s / p95 31.30s, n=2217)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1370; [conversationId, dialogueEventType] x848
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2218/2218 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2218/2218 records)
    "DialogueNodeEvent"  x1370
    "DialogueStartEvent"  x427
    "DialogueFinishEvent"  x421
data.nodeId  (number, 1370/2218 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1962 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (649); Unit 3 Dev (262); Unit 4 Dev (249); Unit 1 Dev (220); Unit 5 Dev - Dungeon (133); Unit 4 Dev - Anderson Base (124); Unit 4 Dev - Dungeon (120); Unit 5 Dev (118); Unit 3 Dungeon Dev (87)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1948)
- **Fields under `data`:**

```text
data.position  (object, 1962/1962 records)
data.position.x  (number, 1962/1962 records)
    numeric range -686.228 .. 1560.34 (630 unique)
data.position.y  (number, 1962/1962 records)
    numeric range -112.488 .. 222.405 (436 unique)
data.position.z  (number, 1962/1962 records)
    numeric range -1152.34 .. 1817.76 (629 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 636 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (343); Unit 2 Prod (Refactor) (105); Unit 5 Dev (100); Unit 1 Dev (45); Unit 3 Dev (43)
- **Intervals:** median 0.34s (p5 0.03s / p95 8.71s, n=635)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 636/636 records)
    "argumentationNodeHoverEnd"  x274
    "argumentationNodeHoverStart"  x274
    "argumentationNodeAdd"  x52
    "argumentationNodeRemove"  x36
data.argumentationTitle  (string, 636/636 records)
    "Unit 4 - Flooding"  x343
    "Unit 2 – Watershed"  x105
    "Unit 5"  x100
    "Unit 1 - Freshwater"  x45
    "Unit 3 - Pollution Upstream"  x43
data.nodeName  (string, 636/636 records)
    "C"  x100
    "B"  x94
    "A"  x88
    "I"  x85
    "D"  x76
    "II"  x55
    "1"  x42
    "2"  x33
    "4"  x33
    "3"  x27
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 346 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (141); Unit 4 Dev - Dungeon (67); Unit 3 Dungeon Dev (29); Unit 5 Dev (29); Unit 4 Dev (26); Unit 1 Dev (14); Unit 5 Dev - Dungeon (14); Unit 3 Dev (13); Unit 4 Dev - Anderson Base (13)
- **Intervals:** median 7.75s (p5 0.79s / p95 355.77s, n=345)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 346/346 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 346/346 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 92 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 1 Dev (17); Unit 4 Dev - Dungeon (12); Unit 3 Dev (11); Unit 4 Dev (8); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 92 of 92 records
- **Intervals:** median 182.04s (p5 0.00s / p95 84219.26s, n=91)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 92/92 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x40
data.questID  (string, 92/92 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 92/92 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/92 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 53 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 4 Dev (12); Unit 3 Dev (9)
- **Intervals:** median 0.98s (p5 0.17s / p95 38901.73s, n=52)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/53 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/53 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x3
    "Unit 4 Dev"  x2
data.actionType  (string, 44/53 records)
    "RightDrag"  x25
    "LeftDrag"  x19
data.currentSoilType  (string, 44/53 records)
    "SAND"  x11
    "CLAYSAND"  x10
    "CLAY"  x9
    "SANDGRAVEL"  x6
    "CLAYROCK"  x5
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 44/53 records)
    "false"  x32
    "true"  x12
data.waterLevelStatus  (string, 44/53 records)
    "Proper"  x22
    "TooHigh"  x16
    "TooLow"  x6
data.waterRetentionChange  (string, 44/53 records)
    "Increase"  x18
    "Decrease"  x14
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 49 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (30); Unit 2 Prod (Refactor) (10); Unit 1 Dev (4); Unit 5 Dev (4); Unit 3 Dev (1)
- **Intervals:** median 12.22s (p5 0.96s / p95 86458.95s, n=48)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "submitAnswerEvent"  x49
data.answerSubmitted  (string, 49/49 records, 1 empty-string)
    31 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 49/49 records)
    "Unit 4 - Flooding"  x30
    "Unit 2 – Watershed"  x10
    "Unit 5"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 38 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (16)
- **Intervals:** median 11.30s (p5 0.02s / p95 86327.62s, n=37)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, legendName] x4
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "MapOpenEvent"  x18
    "MapCloseEvent"  x16
    "Selected"  x4
data.featureUsed  (string, 38/38 records)
    "Map"  x34
    "Legend"  x4
data.legendName  (string, 4/38 records)
    "0 ft"  x1
    "30 ft"  x1
    "330 ft"  x1
    "Water"  x1
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 33 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (33)
- **Intervals:** median 9.48s (p5 0.62s / p95 96.33s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "On"  x23
    "Off"  x10
data.floor  (string, 33/33 records)
    "1"  x11
    "3"  x10
    "4"  x9
    "2"  x3
data.machineNumber  (string, 33/33 records)
    "One"  x28
    "Two"  x5
data.machineType  (string, 33/33 records)
    "Condenser"  x19
    "Evaporator"  x11
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 33/33 records)
    "2"  x17
    "3"  x6
    "4"  x6
    "1"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 22 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (3); Unit 4 Dev (3); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1087.48s (p5 89.23s / p95 259124.26s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "DebugMenuStateChanged"  x22
data.isOpened  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 19 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1976.99s (p5 84.76s / p95 271772.25s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 83858.24s (p5 78.87s / p95 285113.39s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 109.51s (p5 0.04s / p95 415165.93s, n=13)
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

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 2.15s (p5 1.19s / p95 6.21s, n=7)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x7; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "optionSelected"  x7
    "DesignSubmitted"  x1
data.designSelections  (object, 1/8 records)
data.designSelections.glassRoofTemperature  (string, 1/8 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/8 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/8 records)
    "Tilted Out"  x1
data.featureUsed  (string, 8/8 records)
    "GlassRoofTemperature"  x3
    "RoofStyle"  x3
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 7/8 records)
    "Hot"  x2
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 4.10s (p5 1.07s / p95 29.97s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x4
data.boxId  (string, 8/8 records)
    "0"  x4
    "1"  x2
    "2"  x2
data.soilType  (string, 8/8 records)
    "Gravel"  x3
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 6 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (6)
- **Intervals:** median 48.97s (p5 23.61s / p95 193.09s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "ChangeCanister"  x6
data.canisterType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 6/6 records)
    "5"  x4
    "3"  x1
    "4"  x1
data.machine  (string, 6/6 records)
    "1"  x4
    "2"  x2
data.row  (string, 6/6 records)
    "TopRow"  x5
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 1.84s (p5 1.39s / p95 543240.65s, n=3)
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

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 432263.03s (p5 120924.87s / p95 511005.87s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 5 Dev (1)
- **Intervals:** median 9.52s (p5 1.71s / p95 934031.01s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Freshwater"  x3
    "Unit 5"  x1
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 4 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 173500.87s (p5 17933.12s / p95 405679.80s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 4/4 records)
    false  x4
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 42551.18s (p5 4993.46s / p95 80108.89s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Permissions check failed"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit1"  x1
    "unit3"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (32 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "Selected" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (4x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (36x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*