# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56adf

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56adf
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56adf.jsonl
- **Records:** 9707 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56adf
- **Time span:** 2026-10-06T13:21:26.897000+00:00 .. 2026-10-16T13:46:40.925000+00:00 (240h 25m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56adf\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 9707 records, 10 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 90 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2525 | 26.01 | 1 | 4 | 0 | 2026-10-06T13:55:16.280000+00:00 | 2026-10-16T13:20:49.988000+00:00 | 239h 25m |
| InputEvent | 2435 | 25.08 | 1 | 9 | 0 | 2026-10-06T13:26:04.954000+00:00 | 2026-10-16T13:46:40.925000+00:00 | 240h 20m |
| DialogueEvent | 2118 | 21.82 | 1 | 9 | 1324 | 2026-10-06T13:21:53.669000+00:00 | 2026-10-16T13:46:37.133000+00:00 | 240h 24m |
| PlayerPositionEvent | 1570 | 16.17 | 1 | 9 | 0 | 2026-10-06T13:21:35.822000+00:00 | 2026-10-16T13:46:38.459000+00:00 | 240h 25m |
| argumentationNodeEvent | 387 | 3.99 | 1 | 5 | 0 | 2026-10-06T13:44:19.090000+00:00 | 2026-10-16T13:34:46.557000+00:00 | 239h 50m |
| ObjectInterEvent | 288 | 2.97 | 1 | 9 | 0 | 2026-10-06T13:27:16.274000+00:00 | 2026-10-16T13:46:40.925000+00:00 | 240h 19m |
| questEvent | 80 | 0.82 | 1 | 9 | 80 | 2026-10-06T13:21:53.642000+00:00 | 2026-10-16T13:43:07.832000+00:00 | 240h 21m |
| TopographicMapEvent | 57 | 0.59 | 1 | 2 | 0 | 2026-10-06T13:51:13.097000+00:00 | 2026-10-14T13:36:21.829000+00:00 | 191h 45m |
| Soil Key Puzzle | 50 | 0.52 | 1 | 3 | 0 | 2026-10-07T13:46:13.038000+00:00 | 2026-10-14T13:52:55.206000+00:00 | 168h 6m |
| WaterChamberEvent | 39 | 0.4 | 1 | 1 | 0 | 2026-10-16T13:14:32.255000+00:00 | 2026-10-16T13:27:10.126000+00:00 | 12m 37s |
| DEBUGMenu | 30 | 0.31 | 1 | 9 | 0 | 2026-10-06T13:21:35.807000+00:00 | 2026-10-16T13:10:51.809000+00:00 | 239h 49m |
| soilMachine | 24 | 0.25 | 1 | 1 | 0 | 2026-10-15T13:17:26.174000+00:00 | 2026-10-15T13:25:55.326000+00:00 | 8m 29s |
| gameWindowFocusEvent | 21 | 0.22 | 1 | 3 | 0 | 2026-10-06T13:21:26.897000+00:00 | 2026-10-16T13:10:46.621000+00:00 | 239h 49m |
| argumentationAnswerEvent | 18 | 0.19 | 1 | 5 | 0 | 2026-10-06T13:44:33.390000+00:00 | 2026-10-16T13:34:47.523000+00:00 | 239h 50m |
| argumentationEvent | 14 | 0.14 | 1 | 5 | 0 | 2026-10-06T13:44:15.775000+00:00 | 2026-10-16T13:34:47.541000+00:00 | 239h 50m |
| gameStartEvent | 13 | 0.13 | 1 | 1 | 0 | 2026-10-06T13:21:26.898000+00:00 | 2026-10-16T13:10:46.621000+00:00 | 239h 49m |
| gameWindowUnfocusEvent | 13 | 0.13 | 1 | 4 | 0 | 2026-10-06T14:00:02.756000+00:00 | 2026-10-14T14:00:03.527000+00:00 | 192h 0m |
| TerasGardenBox | 6 | 0.06 | 1 | 1 | 0 | 2026-10-15T13:46:57.358000+00:00 | 2026-10-15T13:47:42.207000+00:00 | 44.8s |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-06T13:48:59.661000+00:00 | 2026-10-16T13:46:40.910000+00:00 | 239h 57m |
| SolarStillDesignEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-16T13:40:21.025000+00:00 | 2026-10-16T13:40:33.552000+00:00 | 12.5s |
| argumentationToolEvent | 4 | 0.04 | 1 | 2 | 0 | 2026-10-06T13:44:13.041000+00:00 | 2026-10-08T13:54:16.811000+00:00 | 48h 10m |
| chatEvent | 4 | 0.04 | 1 | 2 | 0 | 2026-10-15T13:56:53.416000+00:00 | 2026-10-16T13:27:58.460000+00:00 | 23h 31m |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-13T13:38:27.623000+00:00 | 2026-10-13T13:38:33.284000+00:00 | 5.7s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87491.35s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.333s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.373s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 22.615s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 74.967s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43161.486s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1438.675s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 774.389s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.9s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; rightArrow; rightShift; upArrow 
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
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 330 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,D,1,II; B,2,II; C,2,II; C,A,2,II; C,D,3,II; C,D,4,3,II; D,2,II; D,C,4,II 
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
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 4.8x vs baseline. 
  - Observed: 24 records 
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
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[136] _id=6ac4f7b4de269131f9b0a0ff ts=2026-10-06T13:29:23.8500000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[184] _id=6ac4f896de269131f9b0c740 ts=2026-10-06T13:33:10.3640000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[226] _id=6ac4f950de269131f9b0e01e ts=2026-10-06T13:36:16.1480000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[2] _id=6ac4f5d7de269131f9b04707 ts=2026-10-06T13:21:26.8980000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[535] _id=6ac4fc99de269131f9b19ca4 ts=2026-10-06T13:50:17.7140000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[1357] _id=6ac647eede269131f9b8e018 ts=2026-10-07T13:23:56.8850000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[3] _id=6ac4f5d7de269131f9b04703 ts=2026-10-06T13:21:26.8970000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[534] _id=6ac4fc99de269131f9b19c9d ts=2026-10-06T13:50:17.7130000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[1356] _id=6ac647eede269131f9b8e017 ts=2026-10-07T13:23:56.8850000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[1354] _id=6ac647eede269131f9b8dfd1 ts=2026-10-06T14:00:02.756Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[3053] _id=6ac79a95de269131f9c0372f ts=2026-10-07T13:59:46.757Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[3514] _id=6ac79feade269131f9c11e79 ts=2026-10-08T13:51:37.8240000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 57 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[532] _id=6ac4fcd1de269131f9b1ac8f ts=2026-10-06T13:51:13.0970000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[545] _id=6ac4fcdade269131f9b1aea5 ts=2026-10-06T13:51:22.3260000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[666] _id=6ac4fdf1de269131f9b1fa13 ts=2026-10-06T13:56:01.2290000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2524 | 0.0 | 0.034 | 341.495 | 1.81 | 433309.115 | 0.18 | 1394 | 9 |
| InputEvent | 2434 | 0.0 | 1.333 | 355.479 | 21.911 | 429380.269 | 0.17 | 22 | 7 |
| DialogueEvent | 2117 | 0.0 | 3.503 | 408.825 | 24.415 | 429399.377 | 0.15 | 616 | 6 |
| PlayerPositionEvent | 1558 | 9.848 | 10.0 | 555.157 | 10.048 | 429330.295 | 0.11 | 0 | 6 |
| argumentationNodeEvent | 386 | 0.0 | 0.4 | 2236.859 | 7.662 | 431286.905 | 0.03 | 71 | 4 |
| ObjectInterEvent | 287 | 0.0 | 8.515 | 3014.511 | 356.151 | 430368.411 | 0.02 | 3 | 9 |
| questEvent | 79 | 0.0 | 175.66 | 10952.838 | 83698.456 | 429405.434 | 0.01 | 15 | 10 |
| TopographicMapEvent | 56 | 0.012 | 7.373 | 12326.942 | 84994.201 | 431066.372 | 0.0 | 2 | 4 |
| Soil Key Puzzle | 49 | 0.166 | 1.183 | 12351.065 | 24.641 | 518496.492 | 0.0 | 0 | 2 |
| WaterChamberEvent | 38 | 1.649 | 14.14 | 19.944 | 46.67 | 69.872 | 3.01 | 0 | 0 |
| DEBUGMenu | 29 | 5.098 | 450.873 | 29770.897 | 84939.653 | 431097.215 | 0.0 | 0 | 13 |
| soilMachine | 23 | 0.451 | 4.9 | 22.137 | 89.529 | 190.267 | 2.71 | 0 | 0 |
| gameWindowFocusEvent | 20 | 10.109 | 1438.675 | 43167.986 | 102593.72 | 429736.168 | 0.0 | 0 | 12 |
| argumentationAnswerEvent | 17 | 0.949 | 22.615 | 50789.067 | 224972.135 | 431380.236 | 0.0 | 0 | 4 |
| argumentationEvent | 13 | 0.029 | 86.653 | 66417.828 | 276487.261 | 431293.561 | 0.0 | 2 | 4 |
| gameStartEvent | 12 | 77.678 | 43161.486 | 71946.644 | 241575.731 | 431104.41 | 0.0 | 0 | 10 |
| gameWindowUnfocusEvent | 12 | 9.295 | 774.389 | 57600.064 | 240760.245 | 429428.001 | 0.0 | 0 | 6 |
| TerasGardenBox | 5 | 1.015 | 6.416 | 8.97 | 19.178 | 19.835 | 6.69 | 0 | 0 |
| EndOfUnit | 4 | 85829.393 | 87491.35 | 215965.312 | 525749.782 | 603049.156 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 1.777 | 2.066 | 4.176 | 8.022 | 8.684 | 14.37 | 0 | 0 |
| argumentationToolEvent | 3 | 2.681 | 74.967 | 57801.257 | 156001.006 | 173326.122 | 0.0 | 0 | 1 |
| chatEvent | 3 | 77.311 | 1026.782 | 28221.681 | 75307.534 | 83560.951 | 0.0 | 0 | 2 |
| DaniEvent | 1 | 5.661 | 5.661 | 5.661 | 5.661 | 5.661 | 10.6 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[3805] _id=6ace300ade269131f9ce962a ts=2026-10-13T13:20:09.2470000Z == 6ab9a88e9a8420a1e6b56adf.jsonl[3807] _id=6ace300ade269131f9ce962b ts=2026-10-13T13:20:09.2470000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[8391] _id=6ad2225cde269131f9e35041 ts=2026-10-16T13:10:52.4430000Z == 6ab9a88e9a8420a1e6b56adf.jsonl[8392] _id=6ad2225cde269131f9e35042 ts=2026-10-16T13:10:52.4430000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 52 group(s), 86 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[651] _id=6ac4fe34de269131f9b20c34 ts=2026-10-06T13:57:07.2290000Z == 6ab9a88e9a8420a1e6b56adf.jsonl[652] _id=6ac4fe34de269131f9b20c41 ts=2026-10-06T13:57:07.2290000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[659] _id=6ac4fe34de269131f9b20c64 ts=2026-10-06T13:57:07.2880000Z == 6ab9a88e9a8420a1e6b56adf.jsonl[663] _id=6ac4fe34de269131f9b20c76 ts=2026-10-06T13:57:07.2880000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[692] _id=6ac4fe42de269131f9b210f0 ts=2026-10-06T13:57:10.3880000Z == 6ab9a88e9a8420a1e6b56adf.jsonl[693] _id=6ac4fe42de269131f9b210f6 ts=2026-10-06T13:57:10.3880000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[9422] _id=6ad2283fde269131f9e3c0a9 ts=2026-10-16T13:35:59.1980000Z == 6ab9a88e9a8420a1e6b56adf.jsonl[9423] _id=6ad2283fde269131f9e3c0aa ts=2026-10-16T13:35:59.1980000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 25 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a88e9a8420a1e6b56adf.jsonl[96] _id=6ac4f734de269131f9b089b0 ts=2026-10-06T13:27:16.2740000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[100] _id=6ac4f734de269131f9b089b8 ts=2026-10-06T13:27:16.2770000Z`; `486ms: 6ab9a88e9a8420a1e6b56adf.jsonl[6841] _id=6ad0d268de269131f9da5a3c ts=2026-10-15T13:17:27.6090000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[6845] _id=6ad0d268de269131f9da5a47 ts=2026-10-15T13:17:28.0950000Z`; `451ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7183] _id=6ad0d427de269131f9da7c14 ts=2026-10-15T13:24:54.3430000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[7153] _id=6ad0d427de269131f9da7c1f ts=2026-10-15T13:24:54.7940000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 82 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `433ms: 6ab9a88e9a8420a1e6b56adf.jsonl[728] _id=6ac4fe44de269131f9b21188 ts=2026-10-06T13:57:16.9950000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[599] _id=6ac4fe44de269131f9b2118f ts=2026-10-06T13:57:17.4280000Z`; `114ms: 6ab9a88e9a8420a1e6b56adf.jsonl[740] _id=6ac4fe44de269131f9b211a6 ts=2026-10-06T13:57:17.4940000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[735] _id=6ac4fe44de269131f9b211b2 ts=2026-10-06T13:57:17.6080000Z`; `296ms: 6ab9a88e9a8420a1e6b56adf.jsonl[742] _id=6ac4fe45de269131f9b211ba ts=2026-10-06T13:57:17.6080000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[736] _id=6ac4fe45de269131f9b211c3 ts=2026-10-06T13:57:17.9040000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `949ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7864] _id=6ad0d835de269131f9dae65a ts=2026-10-15T13:42:12.3260000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[7866] _id=6ad0d836de269131f9dae691 ts=2026-10-15T13:42:13.2750000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6ab9a88e9a8420a1e6b56adf.jsonl[4714] _id=6ace3601de269131f9ced640 ts=2026-10-13T13:45:36.4100000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[4717] _id=6ace3601de269131f9ced643 ts=2026-10-13T13:45:36.4470000Z`; `29ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7879] _id=6ad0d84ade269131f9daeaba ts=2026-10-15T13:42:33.5560000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[7882] _id=6ad0d84ade269131f9daeabd ts=2026-10-15T13:42:33.5850000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 58 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `432ms: 6ab9a88e9a8420a1e6b56adf.jsonl[360] _id=6ac4fb33de269131f9b14329 ts=2026-10-06T13:44:19.0900000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[361] _id=6ac4fb33de269131f9b14340 ts=2026-10-06T13:44:19.5220000Z`; `37ms: 6ab9a88e9a8420a1e6b56adf.jsonl[365] _id=6ac4fb34de269131f9b14383 ts=2026-10-06T13:44:20.5350000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[359] _id=6ac4fb34de269131f9b14389 ts=2026-10-06T13:44:20.5720000Z`; `299ms: 6ab9a88e9a8420a1e6b56adf.jsonl[368] _id=6ac4fb36de269131f9b143db ts=2026-10-06T13:44:21.8560000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[370] _id=6ac4fb36de269131f9b143f3 ts=2026-10-06T13:44:22.1550000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a88e9a8420a1e6b56adf.jsonl[9605] _id=6ad229aade269131f9e3dd3a ts=2026-10-16T13:42:02.8250000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[9609] _id=6ad229abde269131f9e3dd47 ts=2026-10-16T13:42:02.8280000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `483ms: 6ab9a88e9a8420a1e6b56adf.jsonl[6840] _id=6ad0d268de269131f9da5a3a ts=2026-10-15T13:17:27.6060000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[6844] _id=6ad0d268de269131f9da5a45 ts=2026-10-15T13:17:28.0890000Z`; `451ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7182] _id=6ad0d427de269131f9da7c12 ts=2026-10-15T13:24:54.3400000Z ~ 6ab9a88e9a8420a1e6b56adf.jsonl[7179] _id=6ad0d427de269131f9da7c17 ts=2026-10-15T13:24:54.7910000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a88e9a8420a1e6b56adf.jsonl[3057] _id=6ac79a9cde269131f9c037e9 ts=2026-10-08T13:28:59.0620000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3709] _id=6ace2e95de269131f9ce8cea ts=2026-10-13T13:13:56.2770000Z; 23h 37m: 6ab9a88e9a8420a1e6b56adf.jsonl[2410] _id=6ac64e74de269131f9ba0ad7 ts=2026-10-07T13:51:47.9390000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3054] _id=6ac79a95de269131f9c03735 ts=2026-10-08T13:28:51.8780000Z; 23h 33m: 6ab9a88e9a8420a1e6b56adf.jsonl[537] _id=6ac4fc9fde269131f9b19e87 ts=2026-10-06T13:50:23.6030000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1355] _id=6ac647eede269131f9b8e016 ts=2026-10-07T13:23:56.8280000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a88e9a8420a1e6b56adf.jsonl[3706] _id=6ac7a191de269131f9c157c4 ts=2026-10-08T13:58:39.9510000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3724] _id=6ace2ee7de269131f9ce8d36 ts=2026-10-13T13:15:19.3280000Z; 23h 29m: 6ab9a88e9a8420a1e6b56adf.jsonl[3052] _id=6ac65050de269131f9ba3c38 ts=2026-10-07T13:59:43.2780000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3061] _id=6ac79aa1de269131f9c03861 ts=2026-10-08T13:29:02.3510000Z; 23h 24m: 6ab9a88e9a8420a1e6b56adf.jsonl[1352] _id=6ac4fedfde269131f9b23952 ts=2026-10-06T13:59:59.3850000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1370] _id=6ac64816de269131f9b8e796 ts=2026-10-07T13:24:37.9240000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 616 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[1957] _id=6ac64a6cde269131f9b98106 ts=2026-10-07T13:34:35.3500000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1958] _id=6ac64a6cde269131f9b98107 ts=2026-10-07T13:34:35.3500000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[3645] _id=6ac7a0d6de269131f9c145bd ts=2026-10-08T13:55:33.5540000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3646] _id=6ac7a0d6de269131f9c145be ts=2026-10-08T13:55:33.5540000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7733] _id=6ad0d7c1de269131f9dad543 ts=2026-10-15T13:40:16.4850000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7737] _id=6ad0d7c1de269131f9dad544 ts=2026-10-15T13:40:16.4850000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 30m 
  - Evidence: 167h 30m: 6ab9a88e9a8420a1e6b56adf.jsonl[522] _id=6ac4fc4bde269131f9b18448 ts=2026-10-06T13:48:59.6610000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3797] _id=6ace2ff5de269131f9ce9587 ts=2026-10-13T13:19:48.8170000Z; 24h 21m: 6ab9a88e9a8420a1e6b56adf.jsonl[3797] _id=6ace2ff5de269131f9ce9587 ts=2026-10-13T13:19:48.8170000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[6080] _id=6acf869dde269131f9d3471b ts=2026-10-14T13:41:48.8130000Z; 24h 14m: 6ab9a88e9a8420a1e6b56adf.jsonl[6080] _id=6acf869dde269131f9d3471b ts=2026-10-14T13:41:48.8130000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[8227] _id=6ad0db7cde269131f9db4f50 ts=2026-10-15T13:56:11.5170000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a88e9a8420a1e6b56adf.jsonl[3704] _id=6ac7a18ede269131f9c1577f ts=2026-10-08T13:58:37.2320000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3726] _id=6ace2ed2de269131f9ce8d09 ts=2026-10-13T13:14:57.5010000Z; 23h 31m: 6ab9a88e9a8420a1e6b56adf.jsonl[3005] _id=6ac64fc8de269131f9ba335d ts=2026-10-07T13:57:27.2730000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3060] _id=6ac79aa1de269131f9c03860 ts=2026-10-08T13:29:02.2250000Z; 23h 24m: 6ab9a88e9a8420a1e6b56adf.jsonl[1315] _id=6ac4fed6de269131f9b2383a ts=2026-10-06T13:59:50.6220000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1362] _id=6ac647f8de269131f9b8e202 ts=2026-10-07T13:24:06.9930000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[3805] _id=6ace300ade269131f9ce962a ts=2026-10-13T13:20:09.2470000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3807] _id=6ace300ade269131f9ce962b ts=2026-10-13T13:20:09.2470000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[3807] _id=6ace300ade269131f9ce962b ts=2026-10-13T13:20:09.2470000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3808] _id=6ace300ade269131f9ce962c ts=2026-10-13T13:20:09.2470000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[3808] _id=6ace300ade269131f9ce962c ts=2026-10-13T13:20:09.2470000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3809] _id=6ace300ade269131f9ce962d ts=2026-10-13T13:20:09.2470000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a88e9a8420a1e6b56adf.jsonl[3531] _id=6ac7a000de269131f9c12292 ts=2026-10-08T13:51:59.7470000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3894] _id=6ace3120de269131f9ce9ecc ts=2026-10-13T13:24:48.1580000Z; 23h 51m: 6ab9a88e9a8420a1e6b56adf.jsonl[2842] _id=6ac64f17de269131f9ba2649 ts=2026-10-07T13:54:30.9080000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3378] _id=6ac79ea9de269131f9c0e536 ts=2026-10-08T13:46:16.7310000Z; 23h 25m: 6ab9a88e9a8420a1e6b56adf.jsonl[1335] _id=6ac4fedcde269131f9b238da ts=2026-10-06T13:59:56.3560000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1388] _id=6ac64836de269131f9b8ed20 ts=2026-10-07T13:25:09.4360000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7598] _id=6ad0d68ade269131f9dab956 ts=2026-10-15T13:35:05.2420000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7599] _id=6ad0d68ade269131f9dab957 ts=2026-10-15T13:35:05.2420000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7627] _id=6ad0d6c5de269131f9dabd73 ts=2026-10-15T13:36:04.5060000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7628] _id=6ad0d6c5de269131f9dabd74 ts=2026-10-15T13:36:04.5060000Z; 3ms: 6ab9a88e9a8420a1e6b56adf.jsonl[96] _id=6ac4f734de269131f9b089b0 ts=2026-10-06T13:27:16.2740000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[100] _id=6ac4f734de269131f9b089b8 ts=2026-10-06T13:27:16.2770000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a88e9a8420a1e6b56adf.jsonl[3703] _id=6ac7a18cde269131f9c1576b ts=2026-10-08T13:58:35.4680000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3713] _id=6ace2ea2de269131f9ce8cf0 ts=2026-10-13T13:14:05.7630000Z; 23h 29m: 6ab9a88e9a8420a1e6b56adf.jsonl[3051] _id=6ac6504bde269131f9ba3bf5 ts=2026-10-07T13:59:38.9640000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3059] _id=6ac79aa1de269131f9c0385f ts=2026-10-08T13:28:59.0720000Z; 23h 24m: 6ab9a88e9a8420a1e6b56adf.jsonl[1328] _id=6ac4fedade269131f9b238ae ts=2026-10-06T13:59:53.8170000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1360] _id=6ac647f8de269131f9b8e200 ts=2026-10-07T13:24:05.3260000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a88e9a8420a1e6b56adf.jsonl[3074] _id=6ac79aabde269131f9c039a1 ts=2026-10-08T13:29:13.6110000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[4910] _id=6ace3748de269131f9cee5c6 ts=2026-10-13T13:51:02.7260000Z; 23h 32m: 6ab9a88e9a8420a1e6b56adf.jsonl[6396] _id=6acf8999de269131f9d3992a ts=2026-10-14T13:54:31.5280000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7264] _id=6ad0d49bde269131f9da893d ts=2026-10-15T13:26:50.1610000Z; 23h 32m: 6ab9a88e9a8420a1e6b56adf.jsonl[2997] _id=6ac64fb2de269131f9ba315f ts=2026-10-07T13:57:03.2540000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3058] _id=6ac79aa1de269131f9c0386b ts=2026-10-08T13:29:03.5630000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1394 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[1002] _id=6ac4fe83de269131f9b224d3 ts=2026-10-06T13:58:27.4930000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1006] _id=6ac4fe84de269131f9b224dd ts=2026-10-06T13:58:27.4930000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[1013] _id=6ac4fe99de269131f9b22a98 ts=2026-10-06T13:58:47.8420000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1149] _id=6ac4fe99de269131f9b22aa2 ts=2026-10-06T13:58:47.8420000Z; 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[1025] _id=6ac4fe87de269131f9b225de ts=2026-10-06T13:58:30.7720000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1037] _id=6ac4fe87de269131f9b225e2 ts=2026-10-06T13:58:30.7720000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 1m 
  - Evidence: 144h 1m: 6ab9a88e9a8420a1e6b56adf.jsonl[2245] _id=6ac64da4de269131f9b9f6c1 ts=2026-10-07T13:48:19.7940000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[4878] _id=6ace3704de269131f9cee245 ts=2026-10-13T13:49:56.2860000Z; 24h 2m: 6ab9a88e9a8420a1e6b56adf.jsonl[4890] _id=6ace3721de269131f9cee3e6 ts=2026-10-13T13:50:24.3900000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[6153] _id=6acf8922de269131f9d387a8 ts=2026-10-14T13:52:34.1440000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a88e9a8420a1e6b56adf.jsonl[3267] _id=6ac79d37de269131f9c0a68e ts=2026-10-08T13:40:05.9840000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3887] _id=6ace3110de269131f9ce9e5d ts=2026-10-13T13:24:32.3560000Z; 24h 2m: 6ab9a88e9a8420a1e6b56adf.jsonl[4035] _id=6ace328ade269131f9ceac9f ts=2026-10-13T13:30:50.3010000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[5903] _id=6acf84a7de269131f9d32aa5 ts=2026-10-14T13:33:26.7490000Z; 23h 58m: 6ab9a88e9a8420a1e6b56adf.jsonl[2091] _id=6ac64bf5de269131f9b9ce78 ts=2026-10-07T13:41:08.4900000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3258] _id=6ac79d1fde269131f9c0a317 ts=2026-10-08T13:39:42.4380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.012s..0.012s shown 
  - Evidence: 12ms: 6ab9a88e9a8420a1e6b56adf.jsonl[1988] _id=6ac64abdde269131f9b99187 ts=2026-10-07T13:35:57.1480000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1990] _id=6ac64abede269131f9b9918c ts=2026-10-07T13:35:57.1600000Z; 12ms: 6ab9a88e9a8420a1e6b56adf.jsonl[1990] _id=6ac64abede269131f9b9918c ts=2026-10-07T13:35:57.1600000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1994] _id=6ac64abede269131f9b99191 ts=2026-10-07T13:35:57.1720000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a88e9a8420a1e6b56adf.jsonl[3654] _id=6ac7a0edde269131f9c1483d ts=2026-10-08T13:55:56.1490000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[4713] _id=6ace3601de269131f9ced63c ts=2026-10-13T13:45:36.3850000Z; 48h 9m: 6ab9a88e9a8420a1e6b56adf.jsonl[433] _id=6ac4fb9bde269131f9b1572e ts=2026-10-06T13:46:03.4240000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3644] _id=6ac7a0d6de269131f9c145b9 ts=2026-10-08T13:55:33.5340000Z; 47h 54m: 6ab9a88e9a8420a1e6b56adf.jsonl[4713] _id=6ace3601de269131f9ced63c ts=2026-10-13T13:45:36.3850000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7732] _id=6ad0d7c1de269131f9dad53f ts=2026-10-15T13:40:16.4600000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56adf.jsonl[3658] _id=6ac7a0edde269131f9c1483f ts=2026-10-08T13:55:56.1960000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[4627] _id=6ace35aade269131f9ced29b ts=2026-10-13T13:44:09.7570000Z; 48h 8m: 6ab9a88e9a8420a1e6b56adf.jsonl[430] _id=6ac4fb9bde269131f9b15735 ts=2026-10-06T13:46:03.4450000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3573] _id=6ac7a07fde269131f9c13ba2 ts=2026-10-08T13:54:06.5060000Z; 47h 53m: 6ab9a88e9a8420a1e6b56adf.jsonl[4717] _id=6ace3601de269131f9ced643 ts=2026-10-13T13:45:36.4470000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7685] _id=6ad0d761de269131f9daca5f ts=2026-10-15T13:38:40.6770000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.029s..0.037s shown 
  - Evidence: 29ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7879] _id=6ad0d84ade269131f9daeaba ts=2026-10-15T13:42:33.5560000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7882] _id=6ad0d84ade269131f9daeabd ts=2026-10-15T13:42:33.5850000Z; 37ms: 6ab9a88e9a8420a1e6b56adf.jsonl[4714] _id=6ace3601de269131f9ced640 ts=2026-10-13T13:45:36.4100000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[4717] _id=6ace3601de269131f9ced643 ts=2026-10-13T13:45:36.4470000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56adf.jsonl[3656] _id=6ac7a0ebde269131f9c14814 ts=2026-10-08T13:55:54.6150000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[4621] _id=6ace35a2de269131f9ced238 ts=2026-10-13T13:44:01.5200000Z; 48h 8m: 6ab9a88e9a8420a1e6b56adf.jsonl[426] _id=6ac4fb98de269131f9b156d0 ts=2026-10-06T13:46:00.2550000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3567] _id=6ac7a07ade269131f9c13af8 ts=2026-10-08T13:54:01.4010000Z; 47h 53m: 6ab9a88e9a8420a1e6b56adf.jsonl[4711] _id=6ace35fede269131f9ced619 ts=2026-10-13T13:45:34.0510000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7673] _id=6ad0d75dde269131f9dac9c0 ts=2026-10-15T13:38:36.8940000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 71 interval(s) ≤ 0.000s..0.020s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7830] _id=6ad0d810de269131f9dadee6 ts=2026-10-15T13:41:35.8420000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7831] _id=6ad0d810de269131f9dadee7 ts=2026-10-15T13:41:35.8420000Z; 20ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7687] _id=6ad0d762de269131f9daca89 ts=2026-10-15T13:38:42.0590000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7688] _id=6ad0d762de269131f9daca8e ts=2026-10-15T13:38:42.0790000Z; 20ms: 6ab9a88e9a8420a1e6b56adf.jsonl[7781] _id=6ad0d7eede269131f9dad9b6 ts=2026-10-15T13:41:01.9850000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[7780] _id=6ad0d7eede269131f9dad9ba ts=2026-10-15T13:41:02.0050000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 8m 
  - Evidence: 48h 8m: 6ab9a88e9a8420a1e6b56adf.jsonl[397] _id=6ac4fb7ade269131f9b15064 ts=2026-10-06T13:45:30.6890000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3582] _id=6ac7a089de269131f9c13cdf ts=2026-10-08T13:54:16.8110000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 12m 
  - Evidence: 23h 12m: 6ab9a88e9a8420a1e6b56adf.jsonl[8232] _id=6ad0dba6de269131f9db5422 ts=2026-10-15T13:56:53.4160000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[8308] _id=6ad2220ede269131f9e34eb8 ts=2026-10-16T13:09:34.3670000Z; 17m 6s: 6ab9a88e9a8420a1e6b56adf.jsonl[8373] _id=6ad2225bde269131f9e35038 ts=2026-10-16T13:10:51.6780000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[9169] _id=6ad2265fde269131f9e39df2 ts=2026-10-16T13:27:58.4600000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a88e9a8420a1e6b56adf.jsonl[3056] _id=6ac79a95de269131f9c03737 ts=2026-10-08T13:28:51.9350000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3711] _id=6ace2e95de269131f9ce8cec ts=2026-10-13T13:13:56.3450000Z; 24h 1m: 6ab9a88e9a8420a1e6b56adf.jsonl[3803] _id=6ace3002de269131f9ce95f9 ts=2026-10-13T13:20:01.6680000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[5405] _id=6acf81edde269131f9d2ef4e ts=2026-10-14T13:21:48.4800000Z; 23h 37m: 6ab9a88e9a8420a1e6b56adf.jsonl[2218] _id=6ac64e6fde269131f9ba0a20 ts=2026-10-07T13:51:42.7630000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3056] _id=6ac79a95de269131f9c03737 ts=2026-10-08T13:28:51.9350000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a88e9a8420a1e6b56adf.jsonl[3515] _id=6ac79fedde269131f9c11f2c ts=2026-10-08T13:51:40.1770000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3710] _id=6ace2e95de269131f9ce8ceb ts=2026-10-13T13:13:56.3450000Z; 23h 42m: 6ab9a88e9a8420a1e6b56adf.jsonl[4425] _id=6ace346dde269131f9cec236 ts=2026-10-13T13:38:52.7830000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[5404] _id=6acf81edde269131f9d2ef4d ts=2026-10-14T13:21:48.4790000Z; 23h 37m: 6ab9a88e9a8420a1e6b56adf.jsonl[2216] _id=6ac64e6fde269131f9ba0a1f ts=2026-10-07T13:51:42.7630000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3055] _id=6ac79a95de269131f9c03736 ts=2026-10-08T13:28:51.9350000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a88e9a8420a1e6b56adf.jsonl[3708] _id=6ace2e94de269131f9ce8ce8 ts=2026-10-08T13:58:42.646Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3715] _id=6ace2f07de269131f9ce8ddf ts=2026-10-13T13:15:50.6470000Z; 23h 59m: 6ab9a88e9a8420a1e6b56adf.jsonl[5402] _id=6acf81edde269131f9d2ef48 ts=2026-10-13T14:00:07.809Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[6596] _id=6ad0d0d6de269131f9da4ef7 ts=2026-10-14T14:00:03.527Z; 23h 59m: 6ab9a88e9a8420a1e6b56adf.jsonl[1354] _id=6ac647eede269131f9b8dfd1 ts=2026-10-06T14:00:02.756Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3053] _id=6ac79a95de269131f9c0372f ts=2026-10-07T13:59:46.757Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a88e9a8420a1e6b56adf.jsonl[3683] _id=6ac7a144de269131f9c151a8 ts=2026-10-08T13:57:23.3850000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3714] _id=6ace2ea2de269131f9ce8cf1 ts=2026-10-13T13:14:08.8190000Z; 23h 31m: 6ab9a88e9a8420a1e6b56adf.jsonl[3007] _id=6ac64fcfde269131f9ba33a6 ts=2026-10-07T13:57:35.0810000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[3063] _id=6ac79aa1de269131f9c03863 ts=2026-10-08T13:29:02.3980000Z; 23h 30m: 6ab9a88e9a8420a1e6b56adf.jsonl[578] _id=6ac4fd44de269131f9b1c7ef ts=2026-10-06T13:53:08.4760000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[1361] _id=6ac647f8de269131f9b8e201 ts=2026-10-07T13:24:06.5970000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56adf.jsonl[9422] _id=6ad2283fde269131f9e3c0a9 ts=2026-10-16T13:35:59.1980000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[9423] _id=6ad2283fde269131f9e3c0aa ts=2026-10-16T13:35:59.1980000Z; 1ms: 6ab9a88e9a8420a1e6b56adf.jsonl[333] _id=6ac4fae6de269131f9b1307c ts=2026-10-06T13:43:02.3940000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[336] _id=6ac4fae6de269131f9b1307e ts=2026-10-06T13:43:02.3950000Z; 1ms: 6ab9a88e9a8420a1e6b56adf.jsonl[8759] _id=6ad223a5de269131f9e367fb ts=2026-10-16T13:16:21.4730000Z -> 6ab9a88e9a8420a1e6b56adf.jsonl[8760] _id=6ad223a5de269131f9e367fc ts=2026-10-16T13:16:21.4740000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[327] _id=6ac4fad0de269131f9b12d3a ts=2026-10-06T13:42:40.2780000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[443] _id=6ac4fbb0de269131f9b15b37 ts=2026-10-06T13:46:24.3740000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[2092] _id=6ac64bf3de269131f9b9ce38 ts=2026-10-07T13:41:06.8720000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[846] _id=6ac4fe64de269131f9b21bc4 ts=2026-10-06T13:57:55.0080000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[857] _id=6ac4fe64de269131f9b21bcf ts=2026-10-06T13:57:55.0080000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[880] _id=6ac4fe64de269131f9b21bd6 ts=2026-10-06T13:57:55.0590000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 57 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[685] _id=6ac4fe41de269131f9b21047 ts=2026-10-06T13:57:09.9380000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[681] _id=6ac4fe41de269131f9b21091 ts=2026-10-06T13:57:10.0210000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[670] _id=6ac4fe42de269131f9b210b6 ts=2026-10-06T13:57:10.2040000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[4717] _id=6ace3601de269131f9ced643 ts=2026-10-13T13:45:36.4470000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[7882] _id=6ad0d84ade269131f9daeabd ts=2026-10-15T13:42:33.5850000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[359] _id=6ac4fb34de269131f9b14389 ts=2026-10-06T13:44:20.5720000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[367] _id=6ac4fb38de269131f9b14489 ts=2026-10-06T13:44:24.1380000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[317] _id=6ac4fb39de269131f9b144ce ts=2026-10-06T13:44:25.4890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[8232] _id=6ad0dba6de269131f9db5422 ts=2026-10-15T13:56:53.4160000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[8308] _id=6ad2220ede269131f9e34eb8 ts=2026-10-16T13:09:34.3670000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[8373] _id=6ad2225bde269131f9e35038 ts=2026-10-16T13:10:51.6780000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 158 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[765] _id=6ac4fe49de269131f9b213a4 ts=2026-10-06T13:57:28.5170000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[776] _id=6ac4fe4bde269131f9b21410 ts=2026-10-06T13:57:29.3050000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[760] _id=6ac4fe4bde269131f9b21414 ts=2026-10-06T13:57:29.3380000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 379 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[652] _id=6ac4fe34de269131f9b20c41 ts=2026-10-06T13:57:07.2290000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[653] _id=6ac4fe34de269131f9b20c4d ts=2026-10-06T13:57:07.2290000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[704] _id=6ac4fe41de269131f9b21060 ts=2026-10-06T13:57:09.9390000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 402 start, 392 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 27 unmatched 'BecameCameraCentered' (totals: 453 open, 439 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 70 unmatched 'BecameVisible' (totals: 823 open, 810 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 47 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 171 of 9706 adjacent _id pairs reverse in client time; worst 122.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56adf.jsonl[678] _id=6ac4fe3fde269131f9b20f7d ts=2026-10-06T13:57:18.8230000Z`; `6ab9a88e9a8420a1e6b56adf.jsonl[766] _id=6ac4fe40de269131f9b20fc7 ts=2026-10-06T13:55:16.2800000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.86s, min -429314.30s, max -0.12s over 9707 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56adf\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 2525 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1569); Unit 5 Dev - Dungeon (370); Unit 4 Dev (294); Unit 3 Dungeon Dev (292)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.81s, n=2524)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2525/2525 records)
    "BecameVisible"  x823
    "BecameInvisible"  x810
    "BecameCameraCentered"  x453
    "BecameCameraUncentered"  x439
data.pieceId  (string, 2525/2525 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2525/2525 records)
    1624 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2435 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (628); Unit 4 Dev - Dungeon (460); Unit 2 Prod (Refactor) (376); Unit 3 Dungeon Dev (305); Unit 5 Dev - Dungeon (300); Unit 4 Dev (170); Unit 5 Dev (101); Unit 1 Dev (72); Unit 4 Dev - Anderson Base (23)
- **Intervals:** median 1.33s (p5 0.20s / p95 21.91s, n=2434)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2435/2435 records)
    "pressed"  x2435
data.actionType  (string, 2435/2435 records)
    "Move"  x1677
    "Interact"  x436
    "Jump"  x209
    "Ascend"  x52
    "Hoverboard"  x36
    "Descend"  x17
    "Map"  x6
    "Sprint"  x2
data.key  (string, 2435/2435 records, 3 empty-string)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2435/2435 records)
    "Player"  x1884
    "Drone"  x551
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2118 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (634); Unit 3 Dev (303); Unit 4 Dev (254); Unit 5 Dev (219); Unit 1 Dev (201); Unit 3 Dungeon Dev (187); Unit 4 Dev - Dungeon (135); Unit 4 Dev - Anderson Base (104); Unit 5 Dev - Dungeon (81)
- **eventKey:** present on 1324 of 2118 records
- **Intervals:** median 3.50s (p5 0.00s / p95 24.41s, n=2117)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1324; [conversationId, dialogueEventType] x794
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2118/2118 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2118/2118 records)
    "DialogueNodeEvent"  x1324
    "DialogueStartEvent"  x402
    "DialogueFinishEvent"  x392
data.nodeId  (number, 1324/2118 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1570 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (470); Unit 3 Dev (241); Unit 1 Dev (165); Unit 4 Dev (161); Unit 4 Dev - Dungeon (127); Unit 5 Dev - Dungeon (120); Unit 3 Dungeon Dev (114); Unit 5 Dev (111); Unit 4 Dev - Anderson Base (61)
- **Intervals:** median 10.00s (p5 9.97s / p95 10.05s, n=1558)
- **Fields under `data`:**

```text
data.position  (object, 1570/1570 records)
data.position.x  (number, 1570/1570 records)
    numeric range -674.209 .. 1559.44 (546 unique)
data.position.y  (number, 1570/1570 records)
    numeric range -115.127 .. 222.819 (401 unique)
data.position.z  (number, 1570/1570 records)
    numeric range -1075.26 .. 2104.76 (545 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 387 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (145); Unit 3 Dev (77); Unit 2 Prod (Refactor) (61); Unit 5 Dev (56); Unit 1 Dev (48)
- **Intervals:** median 0.40s (p5 0.03s / p95 7.66s, n=386)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 387/387 records)
    "argumentationNodeHoverEnd"  x176
    "argumentationNodeHoverStart"  x173
    "argumentationNodeAdd"  x28
    "argumentationNodeRemove"  x10
data.argumentationTitle  (string, 387/387 records)
    "Unit 4 - Flooding"  x145
    "Unit 3 - Pollution Upstream"  x77
    "Unit 2 – Watershed"  x61
    "Unit 5"  x56
    "Unit 1 - Freshwater"  x33
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 387/387 records)
    "D"  x52
    "C"  x48
    "II"  x47
    "B"  x46
    "1"  x39
    "A"  x39
    "4"  x38
    "I"  x25
    "2"  x23
    "3"  x23
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 288 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (96); Unit 3 Dungeon Dev (51); Unit 2 Prod (Refactor) (48); Unit 5 Dev (34); Unit 4 Dev (17); Unit 3 Dev (12); Unit 5 Dev - Dungeon (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 8.52s (p5 0.20s / p95 356.15s, n=287)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 288/288 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 288/288 records)
    103 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 80 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 4 Dev - Dungeon (12); Unit 3 Dev (9); Unit 5 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 80 of 80 records
- **Intervals:** median 175.66s (p5 0.00s / p95 83698.46s, n=79)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 80/80 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x33
data.questID  (string, 80/80 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 80/80 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/80 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 57 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (31); Unit 3 Dev (26)
- **Intervals:** median 7.37s (p5 0.87s / p95 84994.20s, n=56)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, location] x22; [actionType, featureUsed, legendName] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 57/57 records)
    "MapCloseEvent"  x17
    "MapOpenEvent"  x17
    "WaypointMoveEvent"  x17
    "WaypointSetEvent"  x5
    "Selected"  x1
data.featureUsed  (string, 57/57 records)
    "Map"  x34
    "Waypoint"  x22
    "Legend"  x1
data.legendName  (string, 1/57 records)
    "330 ft"  x1
data.location  (object, 22/57 records)
data.location.x  (number, 22/57 records)
    numeric range -319.411 .. -42.4477 (19 unique)
data.location.y  (number, 22/57 records)
    numeric range -367.372 .. 227.327 (20 unique)
data.location.z  (number, 22/57 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 50 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (38); Unit 3 Dev (6); Unit 4 Dev (6)
- **Intervals:** median 1.18s (p5 0.17s / p95 24.64s, n=49)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/50 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/50 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 44/50 records)
    "RightDrag"  x25
    "LeftDrag"  x19
data.currentSoilType  (string, 44/50 records)
    "CLAY"  x9
    "CLAYSAND"  x8
    "SAND"  x8
    "CLAYROCK"  x7
    "SANDGRAVEL"  x7
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 44/50 records)
    "false"  x33
    "true"  x11
data.waterLevelStatus  (string, 44/50 records)
    "TooHigh"  x22
    "Proper"  x13
    "TooLow"  x9
data.waterRetentionChange  (string, 44/50 records)
    "Increase"  x22
    "Decrease"  x11
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 39 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (39)
- **Intervals:** median 14.14s (p5 2.31s / p95 46.67s, n=38)
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "On"  x25
    "Off"  x14
data.floor  (string, 39/39 records)
    "4"  x22
    "3"  x8
    "1"  x6
    "2"  x3
data.machineNumber  (string, 39/39 records)
    "One"  x38
    "Two"  x1
data.machineType  (string, 39/39 records)
    "Condenser"  x18
    "Evaporator"  x16
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 39/39 records)
    "2"  x16
    "3"  x16
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (5); Unit 4 Dev (3); Unit 5 Dev - Dungeon (3); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 450.87s (p5 5.24s / p95 84939.65s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 24 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (24)
- **Intervals:** median 4.90s (p5 0.57s / p95 89.53s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "ChangeCanister"  x24
data.canisterType  (string, 24/24 records)
    "Clay"  x11
    "Bedrock"  x5
    "Gravel"  x4
    "Sand"  x4
data.floor  (string, 24/24 records)
    "5"  x17
    "3"  x4
    "4"  x3
data.machine  (string, 24/24 records)
    "1"  x23
    "2"  x1
data.row  (string, 24/24 records)
    "BottomRow"  x13
    "TopRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 21 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 3 Dev (6); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1438.67s (p5 17.21s / p95 102593.72s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (10); Unit 5 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 3 Dev (1)
- **Intervals:** median 22.61s (p5 3.30s / p95 224972.14s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    13 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x10
    "Unit 5"  x3
    "Unit 2 – Watershed"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 86.65s (p5 0.03s / p95 276487.26s, n=13)
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
- **Intervals:** median 43161.49s (p5 235.88s / p95 241575.73s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (6); Unit 2 Prod (Refactor) (5); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 774.39s (p5 14.18s / p95 240760.25s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 6.42s (p5 1.02s / p95 19.18s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 87491.35s (p5 86044.39s / p95 525749.78s, n=4)
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
- **Intervals:** median 2.07s (p5 1.81s / p95 8.02s, n=3)
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

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 74.97s (p5 9.91s / p95 156001.01s, n=3)
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

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 5 Dev (1)
- **Intervals:** median 1026.78s (p5 172.26s / p95 75307.53s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 5.66s (p5 5.66s / p95 5.66s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (38 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (17x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (10x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*