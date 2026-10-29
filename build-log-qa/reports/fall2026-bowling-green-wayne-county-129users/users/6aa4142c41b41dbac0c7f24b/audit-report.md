# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f24b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f24b
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f24b.jsonl
- **Records:** 17583 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f24b
- **Time span:** 2026-09-23T16:29:00.143000+00:00 .. 2026-10-07T02:43:14.087000+00:00 (322h 14m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f24b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 17583 records, 11 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 112 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5264 | 29.94 | 1 | 4 | 0 | 2026-09-25T16:42:11.847000+00:00 | 2026-10-07T01:40:19.105000+00:00 | 272h 58m |
| InputEvent | 5084 | 28.91 | 1 | 9 | 0 | 2026-09-23T16:35:23.461000+00:00 | 2026-10-07T02:43:14.087000+00:00 | 322h 7m |
| PlayerPositionEvent | 2544 | 14.47 | 1 | 9 | 0 | 2026-09-23T16:29:10.695000+00:00 | 2026-10-07T02:43:04.293000+00:00 | 322h 13m |
| DialogueEvent | 2247 | 12.78 | 1 | 9 | 1412 | 2026-09-23T16:29:32.786000+00:00 | 2026-10-07T02:43:08.808000+00:00 | 322h 13m |
| argumentationNodeEvent | 1327 | 7.55 | 1 | 4 | 0 | 2026-09-24T16:41:56.225000+00:00 | 2026-10-07T02:29:58.934000+00:00 | 297h 48m |
| ObjectInterEvent | 424 | 2.41 | 1 | 9 | 0 | 2026-09-23T16:37:50.571000+00:00 | 2026-10-07T02:43:14.087000+00:00 | 322h 5m |
| argumentationAnswerEvent | 224 | 1.27 | 1 | 4 | 0 | 2026-09-24T16:42:55.987000+00:00 | 2026-10-07T02:30:10.125000+00:00 | 297h 47m |
| questEvent | 96 | 0.55 | 1 | 9 | 96 | 2026-09-23T16:29:32.756000+00:00 | 2026-10-07T02:38:35.299000+00:00 | 322h 9m |
| Soil Key Puzzle | 68 | 0.39 | 1 | 3 | 0 | 2026-09-25T16:51:02.538000+00:00 | 2026-10-05T16:46:29.982000+00:00 | 239h 55m |
| WaterChamberEvent | 51 | 0.29 | 1 | 1 | 0 | 2026-10-07T01:38:06.285000+00:00 | 2026-10-07T01:51:04.777000+00:00 | 12m 58s |
| gameWindowFocusEvent | 47 | 0.27 | 1 | 9 | 0 | 2026-09-23T16:29:00.143000+00:00 | 2026-10-07T02:18:36.565000+00:00 | 321h 49m |
| gameWindowUnfocusEvent | 39 | 0.22 | 1 | 8 | 0 | 2026-09-23T16:45:33.615000+00:00 | 2026-10-07T02:18:26.292000+00:00 | 321h 32m |
| soilMachine | 31 | 0.18 | 1 | 1 | 0 | 2026-10-05T17:04:14.766000+00:00 | 2026-10-06T16:28:30.256000+00:00 | 23h 24m |
| TopographicMapEvent | 29 | 0.16 | 1 | 2 | 0 | 2026-09-25T16:43:15.855000+00:00 | 2026-10-01T16:54:00.364000+00:00 | 144h 10m |
| DEBUGMenu | 26 | 0.15 | 1 | 9 | 0 | 2026-09-23T16:29:10.688000+00:00 | 2026-10-07T02:18:36.527000+00:00 | 321h 49m |
| gameStartEvent | 19 | 0.11 | 1 | 1 | 0 | 2026-09-23T16:29:00.144000+00:00 | 2026-10-07T02:18:36.565000+00:00 | 321h 49m |
| argumentationToolEvent | 16 | 0.09 | 1 | 3 | 0 | 2026-09-24T16:42:37.083000+00:00 | 2026-10-07T02:18:17.322000+00:00 | 297h 35m |
| argumentationEvent | 15 | 0.09 | 1 | 4 | 0 | 2026-09-24T16:42:42.120000+00:00 | 2026-10-07T02:30:10.130000+00:00 | 297h 47m |
| TerasGardenBox | 9 | 0.05 | 1 | 1 | 0 | 2026-10-06T16:52:59.406000+00:00 | 2026-10-06T16:53:57.610000+00:00 | 58.2s |
| DaniEvent | 7 | 0.04 | 1 | 1 | 0 | 2026-09-28T16:36:49.855000+00:00 | 2026-09-29T17:04:52.138000+00:00 | 24h 28m |
| SolarStillDesignEvent | 6 | 0.03 | 1 | 1 | 0 | 2026-10-07T02:35:26.902000+00:00 | 2026-10-07T02:35:36.870000+00:00 | 10.0s |
| EndOfUnit | 4 | 0.02 | 1 | 4 | 0 | 2026-09-25T16:37:15.214000+00:00 | 2026-10-07T02:43:14.085000+00:00 | 274h 5m |
| chatEvent | 4 | 0.02 | 1 | 2 | 0 | 2026-10-06T17:04:12.015000+00:00 | 2026-10-07T02:18:40.231000+00:00 | 9h 14m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 431596.535s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.528s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.293s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 0.63s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.984s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 16639.511s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 305.743s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 339.394s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.242s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
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
  - Observed: Cold; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 44.8x vs baseline. 
  - Observed: 224 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,B,C,1,2,I; A,B,C,1,2,II; A,B,C,1,4,II; A,B,C,2,3,II; A,B,C,3,4,II; A,B,C,4,1,II; A,B,C,4,2,II; A,B,C,4,3,II; A,B,D,2,1,I; A,B,D,3,4,II; A,C,B,1,2,II; A,C,B,2,II; A,C,B,3,4,II; A,C,D,1,2,II; A,C,D,3,4,II; A,D,B,3,4,II; A,D,C,1,2,II; A,D,C,3,4,II; B,3,I; B,4,II; B,5,I; B,5,II; B,C,A,1,2,I; B,C,A,3,4,II; B,C,D,1,2,II; B,C,D,3,4,II; B,D,A,1,2,II; B,D,A,3,4,II; B,D,C,3,4,II; C,3,II; C,4,II; C,A,2,II; C,D,3,4,II; C,D,3,II; C,D,4,II; C,D,A,3,4,II; C,D,A,4,3,II; C,D,B,3,4,II; C,D,B,4,2,II; D,A,C,3,4,II; D,C,B,3,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 9.5x vs baseline. 
  - Observed: 1327 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.2x vs baseline. 
  - Observed: 31 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 31 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[187] _id=6ab400e7485cab4c954e7220 ts=2026-09-23T16:40:07.6670000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[241] _id=6ab40249485cab4c954e78e0 ts=2026-09-23T16:46:01.3100000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[279] _id=6ab40328485cab4c954e7cd8 ts=2026-09-23T16:49:44.8140000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[5585] _id=6abbe737485cab4c9580c215 ts=2026-09-29T16:28:38.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[4] _id=6ab3fe4c485cab4c954e6159 ts=2026-09-23T16:29:00.1440000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[502] _id=6ab54b4a485cab4c9552ddab ts=2026-09-24T16:09:46.8600000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1066] _id=6ab6a153485cab4c9559be7a ts=2026-09-25T16:29:07.9910000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 47 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 47} 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[9] _id=6ab3fe4c485cab4c954e6156 ts=2026-09-23T16:29:00.1430000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[229] _id=6ab40231485cab4c954e786e ts=2026-09-23T16:45:37.4940000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[230] _id=6ab40232485cab4c954e7876 ts=2026-09-23T16:45:38.5590000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 39 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 39} 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[228] _id=6ab4022d485cab4c954e784a ts=2026-09-23T16:45:33.6150000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[237] _id=6ab40232485cab4c954e7874 ts=2026-09-23T16:45:37.5300000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[480] _id=6ab4152e485cab4c954f364a ts=2026-09-23T18:06:38.8860000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5263 | 0.0 | 0.033 | 186.716 | 1.108 | 345972.76 | 0.32 | 3144 | 10 |
| InputEvent | 5083 | 0.001 | 0.764 | 228.147 | 12.247 | 342905.445 | 0.26 | 238 | 12 |
| PlayerPositionEvent | 2530 | 9.657 | 10.0 | 322.746 | 10.029 | 256731.47 | 0.19 | 0 | 11 |
| DialogueEvent | 2246 | 0.0 | 4.114 | 516.481 | 43.919 | 342909.731 | 0.12 | 648 | 11 |
| argumentationNodeEvent | 1326 | 0.002 | 0.321 | 808.509 | 4.46 | 517952.823 | 0.07 | 295 | 4 |
| ObjectInterEvent | 423 | 0.002 | 7.405 | 2741.19 | 453.241 | 343215.5 | 0.02 | 4 | 15 |
| argumentationAnswerEvent | 223 | 0.131 | 0.63 | 4807.328 | 31.852 | 518015.52 | 0.01 | 0 | 4 |
| questEvent | 95 | 0.0 | 209.811 | 12207.816 | 84292.718 | 343099.857 | 0.0 | 21 | 20 |
| Soil Key Puzzle | 67 | 0.209 | 1.187 | 12891.454 | 655.511 | 430049.147 | 0.0 | 0 | 4 |
| WaterChamberEvent | 50 | 0.402 | 5.293 | 15.57 | 53.039 | 84.277 | 3.85 | 0 | 0 |
| gameWindowFocusEvent | 46 | 1.065 | 305.743 | 25186.444 | 86408.995 | 342864.608 | 0.0 | 0 | 20 |
| gameWindowUnfocusEvent | 38 | 0.0 | 339.394 | 30462.439 | 185105.738 | 343407.531 | 0.0 | 1 | 18 |
| soilMachine | 30 | 0.552 | 4.242 | 2808.516 | 330.747 | 83094.746 | 0.02 | 0 | 1 |
| TopographicMapEvent | 28 | 0.018 | 5.528 | 18537.304 | 87506.916 | 257013.681 | 0.0 | 2 | 6 |
| DEBUGMenu | 25 | 4.617 | 923.981 | 46342.634 | 224226.107 | 343057.722 | 0.0 | 0 | 16 |
| gameStartEvent | 18 | 141.56 | 16639.511 | 64365.357 | 271032.764 | 342864.608 | 0.0 | 0 | 14 |
| argumentationToolEvent | 15 | 0.146 | 4.984 | 71422.683 | 468567.607 | 551404.848 | 0.0 | 0 | 4 |
| argumentationEvent | 14 | 0.024 | 130.18 | 76574.858 | 462768.05 | 517953.902 | 0.0 | 1 | 5 |
| TerasGardenBox | 8 | 0.967 | 3.076 | 7.276 | 22.626 | 28.256 | 8.25 | 0 | 0 |
| DaniEvent | 6 | 0.073 | 2.072 | 14680.38 | 65150.852 | 86262.832 | 0.0 | 0 | 2 |
| SolarStillDesignEvent | 5 | 0.256 | 1.381 | 1.994 | 3.78 | 3.888 | 30.1 | 0 | 0 |
| EndOfUnit | 3 | 34774.278 | 431596.535 | 328919.624 | 511508.906 | 520388.058 | 0.0 | 0 | 3 |
| chatEvent | 3 | 1178.3 | 1612.339 | 11089.405 | 27591.053 | 30477.577 | 0.01 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 205 group(s), 282 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1497] _id=6ab6a478485cab4c955bd098 ts=2026-09-25T16:42:31.7130000Z == 6aa4142c41b41dbac0c7f24b.jsonl[1491] _id=6ab6a478485cab4c955bd0aa ts=2026-09-25T16:42:31.7130000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1496] _id=6ab6a478485cab4c955bd0de ts=2026-09-25T16:42:31.7390000Z == 6aa4142c41b41dbac0c7f24b.jsonl[1498] _id=6ab6a478485cab4c955bd0e7 ts=2026-09-25T16:42:31.7390000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1503] _id=6ab6a479485cab4c955bd135 ts=2026-09-25T16:42:32.3800000Z == 6aa4142c41b41dbac0c7f24b.jsonl[1504] _id=6ab6a479485cab4c955bd141 ts=2026-09-25T16:42:32.3800000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[17274] _id=6ac5aef6de269131f9b8a2af ts=2026-10-07T02:31:18.5960000Z == 6aa4142c41b41dbac0c7f24b.jsonl[17290] _id=6ac5aef6de269131f9b8a2b0 ts=2026-10-07T02:31:18.5960000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[17483] _id=6ac5b065de269131f9b8a427 ts=2026-10-07T02:37:25.0670000Z == 6aa4142c41b41dbac0c7f24b.jsonl[17485] _id=6ac5b065de269131f9b8a429 ts=2026-10-07T02:37:25.0670000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 36 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f24b.jsonl[138] _id=6ab4005e485cab4c954e6f1a ts=2026-09-23T16:37:50.5710000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[136] _id=6ab4005e485cab4c954e6f1c ts=2026-09-23T16:37:50.5770000Z`; `9ms: 6aa4142c41b41dbac0c7f24b.jsonl[537] _id=6ab54c43485cab4c9552e179 ts=2026-09-24T16:13:55.4410000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[542] _id=6ab54c43485cab4c9552e17b ts=2026-09-24T16:13:55.4500000Z`; `208ms: 6aa4142c41b41dbac0c7f24b.jsonl[743] _id=6ab54fe6485cab4c95530f4d ts=2026-09-24T16:29:26.0150000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[746] _id=6ab54fe6485cab4c95530f51 ts=2026-09-24T16:29:26.2230000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 677 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa4142c41b41dbac0c7f24b.jsonl[1494] _id=6ab6a478485cab4c955bd07d ts=2026-09-25T16:42:31.6910000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[1497] _id=6ab6a478485cab4c955bd098 ts=2026-09-25T16:42:31.7130000Z`; `529ms: 6aa4142c41b41dbac0c7f24b.jsonl[1500] _id=6ab6a479485cab4c955bd104 ts=2026-09-25T16:42:31.7500000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[1488] _id=6ab6a479485cab4c955bd113 ts=2026-09-25T16:42:32.2790000Z`; `17ms: 6aa4142c41b41dbac0c7f24b.jsonl[1505] _id=6ab6a479485cab4c955bd14a ts=2026-09-25T16:42:32.3800000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[1499] _id=6ab6a479485cab4c955bd15c ts=2026-09-25T16:42:32.3970000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `967ms: 6aa4142c41b41dbac0c7f24b.jsonl[14267] _id=6ac5276bde269131f9b57bf5 ts=2026-10-06T16:52:59.4060000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[14220] _id=6ac5276cde269131f9b57c21 ts=2026-10-06T16:53:00.3730000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `18ms: 6aa4142c41b41dbac0c7f24b.jsonl[3391] _id=6ab6a8b5485cab4c955d1647 ts=2026-09-25T17:00:37.4300000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[3403] _id=6ab6a8b5485cab4c955d1657 ts=2026-09-25T17:00:37.4480000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 116 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `919ms: 6aa4142c41b41dbac0c7f24b.jsonl[1232] _id=6ab6a288485cab4c955a89f7 ts=2026-09-25T16:34:17.2460000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[1233] _id=6ab6a289485cab4c955a8aa8 ts=2026-09-25T16:34:18.1650000Z`; `517ms: 6aa4142c41b41dbac0c7f24b.jsonl[7832] _id=6abd3ebd485cab4c958ec298 ts=2026-09-30T16:54:21.3120000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[7834] _id=6abd3ebd485cab4c958ec29e ts=2026-09-30T16:54:21.8290000Z`; `742ms: 6aa4142c41b41dbac0c7f24b.jsonl[7849] _id=6abd3ec7485cab4c958ec39e ts=2026-09-30T16:54:31.1220000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[7845] _id=6abd3ec7485cab4c958ec3c0 ts=2026-09-30T16:54:31.8640000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `59ms: 6aa4142c41b41dbac0c7f24b.jsonl[7866] _id=6abd3ed4485cab4c958ec51c ts=2026-09-30T16:54:44.8100000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[7867] _id=6abd3ed5485cab4c958ec526 ts=2026-09-30T16:54:44.8690000Z`; `24ms: 6aa4142c41b41dbac0c7f24b.jsonl[14152] _id=6ac52672de269131f9b55ce4 ts=2026-10-06T16:48:50.1730000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[14150] _id=6ac52672de269131f9b55cf3 ts=2026-10-06T16:48:50.1970000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 152 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `234ms: 6aa4142c41b41dbac0c7f24b.jsonl[979] _id=6ab552d5485cab4c95533a89 ts=2026-09-24T16:41:57.6860000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[980] _id=6ab552d5485cab4c95533a8f ts=2026-09-24T16:41:57.9200000Z`; `563ms: 6aa4142c41b41dbac0c7f24b.jsonl[1007] _id=6ab55305485cab4c95533f6d ts=2026-09-24T16:42:45.3410000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[1011] _id=6ab55305485cab4c95533f77 ts=2026-09-24T16:42:45.9040000Z`; `821ms: 6aa4142c41b41dbac0c7f24b.jsonl[1008] _id=6ab55305485cab4c95533f71 ts=2026-09-24T16:42:45.4770000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[1012] _id=6ab55306485cab4c95533f7f ts=2026-09-24T16:42:46.2980000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `946ms: 6aa4142c41b41dbac0c7f24b.jsonl[16813] _id=6ac5abe8de269131f9b89dfa ts=2026-10-07T02:18:16.3760000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[16818] _id=6ac5abe9de269131f9b89dfe ts=2026-10-07T02:18:17.3220000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `388ms: 6aa4142c41b41dbac0c7f24b.jsonl[685] _id=6ab54f46485cab4c95530548 ts=2026-09-24T16:26:46.8740000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[687] _id=6ab54f47485cab4c9553055f ts=2026-09-24T16:26:47.2620000Z`; `0ms: 6aa4142c41b41dbac0c7f24b.jsonl[16823] _id=6ac5abf2de269131f9b89e14 ts=2026-10-07T02:18:26.2920000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[16821] _id=6ac5abfcde269131f9b89e27 ts=2026-10-07T02:18:26.292Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f24b.jsonl[5585] _id=6abbe737485cab4c9580c215 ts=2026-09-29T16:28:38.5860000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[5592] _id=6abbe737485cab4c9580c217 ts=2026-09-29T16:28:38.5920000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `552ms: 6aa4142c41b41dbac0c7f24b.jsonl[12416] _id=6ac3d8f8de269131f9ae7758 ts=2026-10-05T17:06:00.1730000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[12418] _id=6ac3d8f8de269131f9ae776a ts=2026-10-05T17:06:00.7250000Z`; `577ms: 6aa4142c41b41dbac0c7f24b.jsonl[13190] _id=6ac5217cde269131f9b50077 ts=2026-10-06T16:27:40.4020000Z ~ 6aa4142c41b41dbac0c7f24b.jsonl[13199] _id=6ac5217cde269131f9b5007d ts=2026-10-06T16:27:40.9790000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4142c41b41dbac0c7f24b.jsonl[9963] _id=6abe9352485cab4c95ac42f6 ts=2026-10-01T17:07:30.9790000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10077] _id=6ac3cf64de269131f9ada5f9 ts=2026-10-05T16:25:08.7010000Z; 71h 46m: 6aa4142c41b41dbac0c7f24b.jsonl[1393] _id=6ab6a3a7485cab4c955b4177 ts=2026-09-25T16:39:03.8950000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3521] _id=6aba94ff485cab4c956a7e3a ts=2026-09-28T16:25:35.0420000Z; 24h 19m: 6aa4142c41b41dbac0c7f24b.jsonl[503] _id=6ab54b84485cab4c9552de2d ts=2026-09-24T16:10:45.3660000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1068] _id=6ab6a192485cab4c9559e63e ts=2026-09-25T16:30:11.3120000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 57m 
  - Evidence: 23h 57m: 6aa4142c41b41dbac0c7f24b.jsonl[5574] _id=6aba9ebb485cab4c956bfc97 ts=2026-09-28T17:07:07.7350000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[6705] _id=6abbefb2485cab4c9582b572 ts=2026-09-29T17:04:50.5670000Z; 30m 14s: 6aa4142c41b41dbac0c7f24b.jsonl[3616] _id=6aba97a4485cab4c956abb01 ts=2026-09-28T16:36:52.8240000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[5574] _id=6aba9ebb485cab4c956bfc97 ts=2026-09-28T17:07:07.7350000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 6aa4142c41b41dbac0c7f24b.jsonl[10050] _id=6abe93ff485cab4c95ac440a ts=2026-10-01T17:10:23.2890000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10100] _id=6ac3cf7cde269131f9ada67f ts=2026-10-05T16:25:33.0200000Z; 71h 19m: 6aa4142c41b41dbac0c7f24b.jsonl[3511] _id=6ab6aa1e485cab4c955d39d3 ts=2026-09-25T17:06:38.4050000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3572] _id=6aba952e485cab4c956a82ff ts=2026-09-28T16:26:22.5560000Z; 23h 42m: 6aa4142c41b41dbac0c7f24b.jsonl[1063] _id=6ab5546f485cab4c95534eff ts=2026-09-24T16:48:47.7730000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1088] _id=6ab6a1dc485cab4c955a157d ts=2026-09-25T16:31:24.9990000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 648 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[14596] _id=6ac5ae7dde269131f9b8a204 ts=2026-10-07T02:29:17.0090000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14991] _id=6ac5ae7dde269131f9b8a205 ts=2026-10-07T02:29:17.0090000Z; 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[14901] _id=6ac5a5a7de269131f9b88c78 ts=2026-10-07T01:51:35.1320000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14902] _id=6ac5a5a7de269131f9b88c79 ts=2026-10-07T01:51:35.1320000Z; 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[15076] _id=6ac5a32ede269131f9b88872 ts=2026-10-07T01:41:01.6680000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[15077] _id=6ac5a32ede269131f9b88873 ts=2026-10-07T01:41:01.6680000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 33m 
  - Evidence: 144h 33m: 6aa4142c41b41dbac0c7f24b.jsonl[1390] _id=6ab6a33a485cab4c955af946 ts=2026-09-25T16:37:15.2140000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10038] _id=6abe93ff485cab4c95ac4408 ts=2026-10-01T17:10:23.2720000Z; 119h 53m: 6aa4142c41b41dbac0c7f24b.jsonl[10038] _id=6abe93ff485cab4c95ac4408 ts=2026-10-01T17:10:23.2720000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14473] _id=6ac529ebde269131f9b60235 ts=2026-10-06T17:03:39.8070000Z; 9h 39m: 6aa4142c41b41dbac0c7f24b.jsonl[14473] _id=6ac529ebde269131f9b60235 ts=2026-10-06T17:03:39.8070000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[17580] _id=6ac5b1c2de269131f9b8a4fe ts=2026-10-07T02:43:14.0850000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 6aa4142c41b41dbac0c7f24b.jsonl[10032] _id=6abe93ef485cab4c95ac43f6 ts=2026-10-01T17:10:07.7660000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10065] _id=6ac3cf69de269131f9ada601 ts=2026-10-05T16:25:13.2110000Z; 71h 20m: 6aa4142c41b41dbac0c7f24b.jsonl[3496] _id=6ab6a9c6485cab4c955d36d9 ts=2026-09-25T17:05:10.3660000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3524] _id=6aba9505485cab4c956a7ec4 ts=2026-09-28T16:25:41.0330000Z; 23h 49m: 6aa4142c41b41dbac0c7f24b.jsonl[960] _id=6ab552ae485cab4c9553377b ts=2026-09-24T16:41:18.6630000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1074] _id=6ab6a1be485cab4c955a01fa ts=2026-09-25T16:30:55.0870000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 238 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24b.jsonl[10065] _id=6ac3cf69de269131f9ada601 ts=2026-10-05T16:25:13.2110000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10080] _id=6ac3cf69de269131f9ada604 ts=2026-10-05T16:25:13.2120000Z; 1ms: 6aa4142c41b41dbac0c7f24b.jsonl[10066] _id=6ac3cf6bde269131f9ada611 ts=2026-10-05T16:25:13.2180000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10078] _id=6ac3cf6bde269131f9ada613 ts=2026-10-05T16:25:13.2190000Z; 1ms: 6aa4142c41b41dbac0c7f24b.jsonl[10068] _id=6ac3cf6bde269131f9ada61b ts=2026-10-05T16:25:13.2280000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10090] _id=6ac3cf6bde269131f9ada61d ts=2026-10-05T16:25:13.2290000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4142c41b41dbac0c7f24b.jsonl[10034] _id=6abe93f0485cab4c95ac43fc ts=2026-10-01T17:10:08.0100000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10190] _id=6ac3d09fde269131f9adb8ef ts=2026-10-05T16:30:23.5100000Z; 72h 1m: 6aa4142c41b41dbac0c7f24b.jsonl[3195] _id=6ab6a676485cab4c955cdd52 ts=2026-09-25T16:51:02.5440000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[4051] _id=6aba9b50485cab4c956ada99 ts=2026-09-28T16:52:32.1210000Z; 23h 50m: 6aa4142c41b41dbac0c7f24b.jsonl[962] _id=6ab552b0485cab4c95533795 ts=2026-09-24T16:41:20.7110000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1089] _id=6ab6a1dc485cab4c955a1571 ts=2026-09-25T16:31:24.9760000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f24b.jsonl[13886] _id=6ac5250ade269131f9b52bad ts=2026-10-06T16:42:49.8640000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[13887] _id=6ac5250ade269131f9b52baf ts=2026-10-06T16:42:49.8660000Z; 2ms: 6aa4142c41b41dbac0c7f24b.jsonl[13971] _id=6ac52550de269131f9b5326b ts=2026-10-06T16:43:59.8210000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[13968] _id=6ac52550de269131f9b5326f ts=2026-10-06T16:43:59.8230000Z; 6ms: 6aa4142c41b41dbac0c7f24b.jsonl[138] _id=6ab4005e485cab4c954e6f1a ts=2026-09-23T16:37:50.5710000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[136] _id=6ab4005e485cab4c954e6f1c ts=2026-09-23T16:37:50.5770000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 18m 
  - Evidence: 71h 18m: 6aa4142c41b41dbac0c7f24b.jsonl[3512] _id=6ab6aa23485cab4c955d39f9 ts=2026-09-25T17:06:43.5810000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3536] _id=6aba9505485cab4c956a7ec0 ts=2026-09-28T16:25:35.0510000Z; 23h 41m: 6aa4142c41b41dbac0c7f24b.jsonl[1058] _id=6ab55471485cab4c95534f01 ts=2026-09-24T16:48:49.2810000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1069] _id=6ab6a193485cab4c9559e6de ts=2026-09-25T16:30:11.3190000Z; 23h 21m: 6aa4142c41b41dbac0c7f24b.jsonl[5573] _id=6aba9eb6485cab4c956bfaf4 ts=2026-09-28T17:07:02.6570000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[5590] _id=6abbe737485cab4c9580c203 ts=2026-09-29T16:28:37.5580000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa4142c41b41dbac0c7f24b.jsonl[8875] _id=6abe893d485cab4c95abdf5a ts=2026-10-01T16:24:30.3730000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10208] _id=6ac3d0b3de269131f9adb9dd ts=2026-10-05T16:30:43.1330000Z; 71h 52m: 6aa4142c41b41dbac0c7f24b.jsonl[3198] _id=6ab6a63b485cab4c955cd5c5 ts=2026-09-25T16:50:00.6790000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3845] _id=6aba9908485cab4c956ac580 ts=2026-09-28T16:42:47.4860000Z; 24h 26m: 6aa4142c41b41dbac0c7f24b.jsonl[6239] _id=6abbe94e485cab4c9580ec97 ts=2026-09-29T16:37:32.9940000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[8353] _id=6abd40ee485cab4c958eee7e ts=2026-09-30T17:03:41.6740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3144 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[10196] _id=6ac3d0b3de269131f9adb9e2 ts=2026-10-05T16:30:43.1330000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10197] _id=6ac3d0b3de269131f9adb9e5 ts=2026-10-05T16:30:43.1330000Z; 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[10197] _id=6ac3d0b3de269131f9adb9e5 ts=2026-10-05T16:30:43.1330000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10209] _id=6ac3d0b3de269131f9adb9eb ts=2026-10-05T16:30:43.1330000Z; 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[10207] _id=6ac3d0b3de269131f9adb9ed ts=2026-10-05T16:30:43.1330000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10210] _id=6ac3d0b3de269131f9adb9ef ts=2026-10-05T16:30:43.1330000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6aa4142c41b41dbac0c7f24b.jsonl[8327] _id=6abd40be485cab4c958eecbc ts=2026-09-30T17:02:54.3560000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10188] _id=6ac3d09fde269131f9adb8ed ts=2026-10-05T16:30:23.5030000Z; 72h 1m: 6aa4142c41b41dbac0c7f24b.jsonl[3223] _id=6ab6a679485cab4c955cddf7 ts=2026-09-25T16:51:05.5330000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[4050] _id=6aba9b50485cab4c956ada95 ts=2026-09-28T16:52:32.1180000Z; 48h 8m: 6aa4142c41b41dbac0c7f24b.jsonl[4086] _id=6aba9ba8485cab4c956ade7c ts=2026-09-28T16:54:00.3550000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[8305] _id=6abd40a7485cab4c958eeb8a ts=2026-09-30T17:02:31.6060000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 71h 23m 
  - Evidence: 71h 23m: 6aa4142c41b41dbac0c7f24b.jsonl[3498] _id=6ab6a9c4485cab4c955d36c3 ts=2026-09-25T17:05:08.1980000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3601] _id=6aba95b9485cab4c956a9259 ts=2026-09-28T16:28:41.8790000Z; 24h 20m: 6aa4142c41b41dbac0c7f24b.jsonl[6875] _id=6abd39d1485cab4c958dd028 ts=2026-09-30T16:33:21.7770000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[9682] _id=6abe9023485cab4c95ac2cff ts=2026-10-01T16:53:55.4190000Z; 24h 14m: 6aa4142c41b41dbac0c7f24b.jsonl[3612] _id=6aba97a1485cab4c956abacb ts=2026-09-28T16:36:49.8490000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[6493] _id=6abbec89485cab4c9581e9fe ts=2026-09-29T16:51:21.4180000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.018s..0.025s shown 
  - Evidence: 18ms: 6aa4142c41b41dbac0c7f24b.jsonl[3391] _id=6ab6a8b5485cab4c955d1647 ts=2026-09-25T17:00:37.4300000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3403] _id=6ab6a8b5485cab4c955d1657 ts=2026-09-25T17:00:37.4480000Z; 25ms: 6aa4142c41b41dbac0c7f24b.jsonl[3383] _id=6ab6a8b5485cab4c955d1643 ts=2026-09-25T17:00:37.4050000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3391] _id=6ab6a8b5485cab4c955d1647 ts=2026-09-25T17:00:37.4300000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 53m 
  - Evidence: 143h 53m: 6aa4142c41b41dbac0c7f24b.jsonl[7860] _id=6abd3ed4485cab4c958ec51a ts=2026-09-30T16:54:44.7920000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14102] _id=6ac52654de269131f9b557ef ts=2026-10-06T16:48:20.3120000Z; 120h 18m: 6aa4142c41b41dbac0c7f24b.jsonl[1239] _id=6ab6a28e485cab4c955a8e43 ts=2026-09-25T16:34:23.2290000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[7696] _id=6abd3e61485cab4c958eb736 ts=2026-09-30T16:52:49.4580000Z; 23h 50m: 6aa4142c41b41dbac0c7f24b.jsonl[1023] _id=6ab55310485cab4c95534021 ts=2026-09-24T16:42:55.9870000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1130] _id=6ab6a238485cab4c955a52a3 ts=2026-09-25T16:32:57.3840000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 52m 
  - Evidence: 143h 52m: 6aa4142c41b41dbac0c7f24b.jsonl[7867] _id=6abd3ed5485cab4c958ec526 ts=2026-09-30T16:54:44.8690000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14036] _id=6ac52616de269131f9b54c45 ts=2026-10-06T16:47:18.7710000Z; 120h 17m: 6aa4142c41b41dbac0c7f24b.jsonl[1240] _id=6ab6a28e485cab4c955a8e55 ts=2026-09-25T16:34:23.2610000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[7686] _id=6abd3e2b485cab4c958eb15e ts=2026-09-30T16:51:55.8520000Z; 23h 49m: 6aa4142c41b41dbac0c7f24b.jsonl[993] _id=6ab55319485cab4c955340f3 ts=2026-09-24T16:43:05.8690000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1111] _id=6ab6a22f485cab4c955a4bed ts=2026-09-25T16:32:48.2250000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.024s..0.024s shown 
  - Evidence: 24ms: 6aa4142c41b41dbac0c7f24b.jsonl[14152] _id=6ac52672de269131f9b55ce4 ts=2026-10-06T16:48:50.1730000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14150] _id=6ac52672de269131f9b55cf3 ts=2026-10-06T16:48:50.1970000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 52m 
  - Evidence: 143h 52m: 6aa4142c41b41dbac0c7f24b.jsonl[7864] _id=6abd3ed3485cab4c958ec4f4 ts=2026-09-30T16:54:43.5070000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14030] _id=6ac52614de269131f9b54c05 ts=2026-10-06T16:47:16.3300000Z; 120h 18m: 6aa4142c41b41dbac0c7f24b.jsonl[1227] _id=6ab6a287485cab4c955a88f7 ts=2026-09-25T16:34:15.6350000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[7699] _id=6abd3e66485cab4c958eb7fe ts=2026-09-30T16:52:54.1800000Z; 23h 49m: 6aa4142c41b41dbac0c7f24b.jsonl[1018] _id=6ab5530d485cab4c95533ffd ts=2026-09-24T16:42:53.4280000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1115] _id=6ab6a234485cab4c955a4f6f ts=2026-09-25T16:32:53.0560000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 295 interval(s) ≤ 0.002s..0.017s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f24b.jsonl[7728] _id=6abd3e7a485cab4c958eba89 ts=2026-09-30T16:53:14.4530000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[7734] _id=6abd3e7a485cab4c958eba8c ts=2026-09-30T16:53:14.4550000Z; 13ms: 6aa4142c41b41dbac0c7f24b.jsonl[977] _id=6ab552d4485cab4c95533a69 ts=2026-09-24T16:41:56.5950000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[978] _id=6ab552d4485cab4c95533a6d ts=2026-09-24T16:41:56.6080000Z; 17ms: 6aa4142c41b41dbac0c7f24b.jsonl[1155] _id=6ab6a269485cab4c955a7430 ts=2026-09-25T16:33:45.6100000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1157] _id=6ab6a269485cab4c955a7441 ts=2026-09-25T16:33:45.6270000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 153h 10m 
  - Evidence: 153h 10m: 6aa4142c41b41dbac0c7f24b.jsonl[7681] _id=6abd3e34485cab4c958eb222 ts=2026-09-30T16:52:04.8020000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[15968] _id=6ac5a821de269131f9b892d4 ts=2026-10-07T02:02:09.6500000Z; 120h 17m: 6aa4142c41b41dbac0c7f24b.jsonl[1235] _id=6ab6a28a485cab4c955a8b29 ts=2026-09-25T16:34:18.8700000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[7681] _id=6abd3e34485cab4c958eb222 ts=2026-09-30T16:52:04.8020000Z; 23h 51m: 6aa4142c41b41dbac0c7f24b.jsonl[1004] _id=6ab55302485cab4c95533f2d ts=2026-09-24T16:42:42.0670000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1235] _id=6ab6a28a485cab4c955a8b29 ts=2026-09-25T16:34:18.8700000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 8h 27m 
  - Evidence: 8h 27m: 6aa4142c41b41dbac0c7f24b.jsonl[14483] _id=6ac52a0cde269131f9b6088d ts=2026-10-06T17:04:12.0150000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[14601] _id=6ac5a119de269131f9b88423 ts=2026-10-07T01:32:09.5920000Z; 26m 52s: 6aa4142c41b41dbac0c7f24b.jsonl[15483] _id=6ac5a5b3de269131f9b88ccb ts=2026-10-07T01:51:47.8920000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[16545] _id=6ac5ac00de269131f9b89e34 ts=2026-10-07T02:18:40.2310000Z; 19m 38s: 6aa4142c41b41dbac0c7f24b.jsonl[14601] _id=6ac5a119de269131f9b88423 ts=2026-10-07T01:32:09.5920000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[15483] _id=6ac5a5b3de269131f9b88ccb ts=2026-10-07T01:51:47.8920000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 14m 
  - Evidence: 95h 14m: 6aa4142c41b41dbac0c7f24b.jsonl[9998] _id=6abe940b485cab4c95ac4410 ts=2026-10-01T17:10:35.1910000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10076] _id=6ac3cf5cde269131f9ada5e9 ts=2026-10-05T16:24:59.7990000Z; 71h 45m: 6aa4142c41b41dbac0c7f24b.jsonl[1392] _id=6ab6a396485cab4c955b3698 ts=2026-09-25T16:38:47.0550000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3520] _id=6aba94cb485cab4c956a7aa3 ts=2026-09-28T16:24:43.6110000Z; 24h 19m: 6aa4142c41b41dbac0c7f24b.jsonl[502] _id=6ab54b4a485cab4c9552ddab ts=2026-09-24T16:09:46.8600000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1066] _id=6ab6a153485cab4c9559be7a ts=2026-09-25T16:29:07.9910000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 14m 
  - Evidence: 95h 14m: 6aa4142c41b41dbac0c7f24b.jsonl[10051] _id=6abe940b485cab4c95ac440e ts=2026-10-01T17:10:35.1900000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10075] _id=6ac3cf5bde269131f9ada5e7 ts=2026-10-05T16:24:59.7980000Z; 71h 45m: 6aa4142c41b41dbac0c7f24b.jsonl[1391] _id=6ab6a396485cab4c955b3677 ts=2026-09-25T16:38:47.0550000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3519] _id=6aba94cb485cab4c956a7a9f ts=2026-09-28T16:24:43.6100000Z; 24h 2m: 6aa4142c41b41dbac0c7f24b.jsonl[688] _id=6ab54f4b485cab4c955305c9 ts=2026-09-24T16:26:51.8180000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1065] _id=6ab6a153485cab4c9559be6e ts=2026-09-25T16:29:07.9900000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4142c41b41dbac0c7f24b.jsonl[10052] _id=6abe940d485cab4c95ac4412 ts=2026-10-01T17:10:37.5740000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[11164] _id=6ac3d17dde269131f9adcff0 ts=2026-10-05T16:34:05.1050000Z; 71h 33m: 6aa4142c41b41dbac0c7f24b.jsonl[3513] _id=6ab6aa25485cab4c955d3a05 ts=2026-09-25T17:06:45.3310000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3761] _id=6aba986e485cab4c956ac163 ts=2026-09-28T16:40:13.9440000Z; 47h 51m: 6aa4142c41b41dbac0c7f24b.jsonl[6732] _id=6abd379e485cab4c958d8bba ts=2026-09-29T17:05:03.012Z -> 6aa4142c41b41dbac0c7f24b.jsonl[9836] _id=6abe90d6485cab4c95ac35a8 ts=2026-10-01T16:56:54.1250000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[16823] _id=6ac5abf2de269131f9b89e14 ts=2026-10-07T02:18:26.2920000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[16821] _id=6ac5abfcde269131f9b89e27 ts=2026-10-07T02:18:26.292Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4142c41b41dbac0c7f24b.jsonl[10048] _id=6abe93f6485cab4c95ac4400 ts=2026-10-01T17:10:14.2940000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[10119] _id=6ac3d032de269131f9adb1c5 ts=2026-10-05T16:28:34.1510000Z; 71h 25m: 6aa4142c41b41dbac0c7f24b.jsonl[3390] _id=6ab6a89a485cab4c955d1265 ts=2026-09-25T17:00:10.6440000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[3535] _id=6aba9508485cab4c956a7f2e ts=2026-09-28T16:25:41.1180000Z; 23h 48m: 6aa4142c41b41dbac0c7f24b.jsonl[967] _id=6ab552b1485cab4c955337a5 ts=2026-09-24T16:41:20.7510000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[1067] _id=6ab6a193485cab4c9559e6ef ts=2026-09-25T16:30:12.0640000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 21 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[15072] _id=6ac5a312de269131f9b8885f ts=2026-10-07T01:40:34.6650000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[15073] _id=6ac5a312de269131f9b88860 ts=2026-10-07T01:40:34.6650000Z; 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[15128] _id=6ac5a38bde269131f9b888de ts=2026-10-07T01:42:35.8590000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[15125] _id=6ac5a38cde269131f9b888e0 ts=2026-10-07T01:42:35.8590000Z; 0ms: 6aa4142c41b41dbac0c7f24b.jsonl[15291] _id=6ac5a48bde269131f9b88a68 ts=2026-10-07T01:46:51.6320000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[15303] _id=6ac5a48bde269131f9b88a6a ts=2026-10-07T01:46:51.6320000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 4m 
  - Evidence: 23h 4m: 6aa4142c41b41dbac0c7f24b.jsonl[12434] _id=6ac3d90ade269131f9ae780f ts=2026-10-05T17:06:18.0090000Z -> 6aa4142c41b41dbac0c7f24b.jsonl[12541] _id=6ac51da0de269131f9b4e625 ts=2026-10-06T16:11:12.7550000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[941] _id=6ab55277485cab4c9553329f ts=2026-09-24T16:40:23.1470000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[5557] _id=6aba9ea2485cab4c956bf3f6 ts=2026-09-28T17:06:42.4370000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[6139] _id=6abbe92f485cab4c9580eab9 ts=2026-09-29T16:37:03.9380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 107 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1756] _id=6ab6a512485cab4c955c313f ts=2026-09-25T16:45:05.6770000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1812] _id=6ab6a522485cab4c955c3c07 ts=2026-09-25T16:45:21.5970000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1871] _id=6ab6a527485cab4c955c3f35 ts=2026-09-25T16:45:25.1900000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 332 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1492] _id=6ab6a478485cab4c955bd0bc ts=2026-09-25T16:42:31.7130000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1495] _id=6ab6a478485cab4c955bd0cd ts=2026-09-25T16:42:31.7390000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1503] _id=6ab6a479485cab4c955bd135 ts=2026-09-25T16:42:32.3800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[7867] _id=6abd3ed5485cab4c958ec526 ts=2026-09-30T16:54:44.8690000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[14150] _id=6ac52672de269131f9b55cf3 ts=2026-10-06T16:48:50.1970000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1013] _id=6ab55306485cab4c95533f81 ts=2026-09-24T16:42:46.3280000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1020] _id=6ab5530c485cab4c95533fdb ts=2026-09-24T16:42:51.9190000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1018] _id=6ab5530d485cab4c95533ffd ts=2026-09-24T16:42:53.4280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[14483] _id=6ac52a0cde269131f9b6088d ts=2026-10-06T17:04:12.0150000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[14601] _id=6ac5a119de269131f9b88423 ts=2026-10-07T01:32:09.5920000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[15483] _id=6ac5a5b3de269131f9b88ccb ts=2026-10-07T01:51:47.8920000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[11942] _id=6ac3d5b5de269131f9ae29d5 ts=2026-10-05T16:52:05.9680000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[12576] _id=6ac51d40de269131f9b4e35f ts=2026-10-06T16:09:36.5910000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[12932] _id=6ac5205ade269131f9b4f349 ts=2026-10-06T16:22:50.2710000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[11241] _id=6ac3d31bde269131f9adee67 ts=?`; `6aa4142c41b41dbac0c7f24b.jsonl[14549] _id=6ac55037de269131f9b7b6e0 ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[6705] _id=6abbefb2485cab4c9582b572 ts=2026-09-29T17:04:50.5670000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[6709] _id=6abbefb3485cab4c9582b5bd ts=2026-09-29T17:04:51.8160000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 840 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1755] _id=6ab6a512485cab4c955c3170 ts=2026-09-25T16:45:06.0100000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1816] _id=6ab6a522485cab4c955c3c53 ts=2026-09-25T16:45:21.8240000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1801] _id=6ab6a522485cab4c955c3c5d ts=2026-09-25T16:45:21.8930000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 847 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1487] _id=6ab6a478485cab4c955bd037 ts=2026-09-25T16:42:31.6700000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1490] _id=6ab6a478485cab4c955bd052 ts=2026-09-25T16:42:31.6700000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1498] _id=6ab6a478485cab4c955bd0e7 ts=2026-09-25T16:42:31.7390000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[3391] _id=6ab6a8b5485cab4c955d1647 ts=2026-09-25T17:00:37.4300000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[3403] _id=6ab6a8b5485cab4c955d1657 ts=2026-09-25T17:00:37.4480000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[3491] _id=6ab6a9ba485cab4c955d3671 ts=2026-09-25T17:04:59.0290000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[17058] _id=6ac5ad8dde269131f9b8a0dd ts=2026-10-07T02:25:17.2890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 75 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[1163] _id=6ab6a26b485cab4c955a759d ts=2026-09-25T16:33:47.9350000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1169] _id=6ab6a26c485cab4c955a7644 ts=2026-09-25T16:33:48.7000000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[1173] _id=6ab6a26d485cab4c955a7753 ts=2026-09-25T16:33:50.1190000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[16274] _id=6ac5a8e1de269131f9b895c8 ts=2026-10-07T02:05:21.3950000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[16397] _id=6ac5a937de269131f9b8975a ts=2026-10-07T02:06:47.8160000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[16393] _id=6ac5a93ade269131f9b89760 ts=2026-10-07T02:06:50.4080000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 422 start, 413 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 160 unmatched 'BecameCameraCentered' (totals: 1123 open, 1070 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 135 unmatched 'BecameVisible' (totals: 1437 open, 1634 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 10 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 552 open, 560 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 11 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 57 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 480 of 17580 adjacent _id pairs reverse in client time; worst 85396.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f24b.jsonl[12919] _id=6ac51f6fde269131f9b4f247 ts=2026-10-06T16:18:55.5680000Z`; `6aa4142c41b41dbac0c7f24b.jsonl[12933] _id=6ac52049de269131f9b4f2e5 ts=2026-10-05T16:35:39.343Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -85614.59s, max +1.86s over 17581 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f24b\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 5264 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3161); Unit 4 Dev (1250); Unit 3 Dungeon Dev (490); Unit 5 Dev - Dungeon (363)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.11s, n=5263)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5264/5264 records)
    "BecameInvisible"  x1634
    "BecameVisible"  x1437
    "BecameCameraCentered"  x1123
    "BecameCameraUncentered"  x1070
data.pieceId  (string, 5264/5264 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5264/5264 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 5084 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (979); Unit 3 Dev (973); Unit 4 Dev - Dungeon (844); Unit 4 Dev (662); Unit 3 Dungeon Dev (521); Unit 1 Dev (400); Unit 5 Dev - Dungeon (321); Unit 5 Dev (253); Unit 4 Dev - Anderson Base (131)
- **Intervals:** median 0.76s (p5 0.06s / p95 12.25s, n=5083)
- **Fields under `data`:**

```text
data.Value  (string, 5084/5084 records)
    "pressed"  x5084
data.actionType  (string, 5084/5084 records)
    "Move"  x2441
    "Interact"  x932
    "Sprint"  x930
    "Jump"  x607
    "Hoverboard"  x101
    "Ascend"  x56
    "Descend"  x11
    "Pause"  x3
    "SkipCinematic"  x2
    "Map"  x1
data.key  (string, 5084/5084 records, 16 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5084/5084 records)
    "Player"  x4448
    "Drone"  x636
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2544 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (600); Unit 1 Dev (489); Unit 5 Dev (306); Unit 3 Dev (299); Unit 4 Dev (250); Unit 4 Dev - Dungeon (222); Unit 3 Dungeon Dev (196); Unit 5 Dev - Dungeon (126); Unit 4 Dev - Anderson Base (56)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2530)
- **Fields under `data`:**

```text
data.position  (object, 2544/2544 records)
data.position.x  (number, 2544/2544 records)
    numeric range -692.757 .. 1549.85 (807 unique)
data.position.y  (number, 2544/2544 records)
    numeric range -115.127 .. 407.641 (584 unique)
data.position.z  (number, 2544/2544 records)
    numeric range -1117.49 .. 1984.38 (805 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2247 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (496); Unit 3 Dev (369); Unit 4 Dev (302); Unit 5 Dev (296); Unit 1 Dev (290); Unit 4 Dev - Dungeon (173); Unit 3 Dungeon Dev (159); Unit 5 Dev - Dungeon (85); Unit 4 Dev - Anderson Base (77)
- **eventKey:** present on 1412 of 2247 records
- **Intervals:** median 4.11s (p5 0.00s / p95 43.92s, n=2246)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1412; [conversationId, dialogueEventType] x835
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2247/2247 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2247/2247 records)
    "DialogueNodeEvent"  x1412
    "DialogueStartEvent"  x422
    "DialogueFinishEvent"  x413
data.nodeId  (number, 1412/2247 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 1327 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 5 Dev (992); Unit 1 Dev (123); Unit 3 Dev (123); Unit 4 Dev - Anderson Base (89)
- **Intervals:** median 0.32s (p5 0.03s / p95 4.46s, n=1326)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1327/1327 records)
    "argumentationNodeHoverEnd"  x560
    "argumentationNodeHoverStart"  x552
    "argumentationNodeAdd"  x118
    "argumentationNodeRemove"  x97
data.argumentationTitle  (string, 1327/1327 records)
    "Unit 5"  x992
    "Unit 3 - Pollution Upstream"  x123
    "Unit 4 - Flooding"  x89
    "Unit 1 - Freshwater"  x81
    "Unit 1 - Argumentation Tutorial"  x42
data.nodeName  (string, 1327/1327 records)
    "B"  x207
    "A"  x205
    "C"  x159
    "D"  x149
    "3"  x112
    "4"  x105
    "1"  x101
    "2"  x96
    "I"  x91
    "II"  x91
    "5"  x11
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 424 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (169); Unit 3 Dungeon Dev (70); Unit 2 Prod (Refactor) (49); Unit 4 Dev (37); Unit 5 Dev (34); Unit 1 Dev (27); Unit 5 Dev - Dungeon (18); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 7.41s (p5 0.42s / p95 453.24s, n=423)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 424/424 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 424/424 records)
    99 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationAnswerEvent` — 224 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (203); Unit 3 Dev (11); Unit 1 Dev (5); Unit 4 Dev - Anderson Base (5)
- **Intervals:** median 0.63s (p5 0.17s / p95 31.85s, n=223)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 224/224 records)
    "submitAnswerEvent"  x224
data.answerSubmitted  (string, 224/224 records, 1 empty-string)
    45 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 224/224 records)
    "Unit 5"  x203
    "Unit 3 - Pollution Upstream"  x11
    "Unit 4 - Flooding"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `questEvent` — 96 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (21); Unit 1 Dev (20); Unit 2 Prod (Refactor) (15); Unit 3 Dev (10); Unit 4 Dev (9); Unit 5 Dev (8); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 96 of 96 records
- **Intervals:** median 209.81s (p5 0.00s / p95 84292.72s, n=95)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 96/96 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x39
data.questID  (string, 96/96 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 96/96 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/96 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 68 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 4 Dev (22); Unit 3 Dev (14)
- **Intervals:** median 1.19s (p5 0.22s / p95 655.51s, n=67)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/68 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/68 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 58/68 records)
    "RightDrag"  x32
    "LeftDrag"  x26
data.currentSoilType  (string, 58/68 records)
    "CLAY"  x12
    "CLAYSAND"  x12
    "SAND"  x10
    "CLAYROCK"  x9
    "SANDGRAVEL"  x8
    "GRAVEL"  x4
    "BEDROCK"  x3
data.isCorrectSelection  (string, 58/68 records)
    "false"  x44
    "true"  x14
data.waterLevelStatus  (string, 58/68 records)
    "Proper"  x24
    "TooHigh"  x17
    "TooLow"  x17
data.waterRetentionChange  (string, 58/68 records)
    "Increase"  x26
    "Decrease"  x18
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 51 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (51)
- **Intervals:** median 5.29s (p5 0.78s / p95 53.04s, n=50)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 51/51 records)
    "On"  x31
    "Off"  x20
data.floor  (string, 51/51 records)
    "3"  x29
    "4"  x13
    "1"  x6
    "2"  x3
data.machineNumber  (string, 51/51 records)
    "One"  x50
    "Two"  x1
data.machineType  (string, 51/51 records)
    "Condenser"  x30
    "Evaporator"  x11
    "DualChamber_Condenser"  x4
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x2
data.room  (string, 51/51 records)
    "1"  x18
    "2"  x18
    "3"  x11
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 47 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 4 Dev (11); Unit 1 Dev (8); Unit 4 Dev - Dungeon (3); Unit 2 Prod (Refactor) (2); Transition (1); Unit 3 Dev (1); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 305.74s (p5 3.39s / p95 86408.99s, n=46)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 47/47 records)
    true  x47
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 39 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (11); Unit 1 Dev (9); Unit 2 Prod (Refactor) (5); Unit 4 Dev - Dungeon (5); Unit 5 Dev (3); Transition (2); Unit 3 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 339.39s (p5 1.07s / p95 185105.74s, n=38)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 39/39 records)
    false  x39
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 31 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (31)
- **Intervals:** median 4.24s (p5 0.72s / p95 330.75s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "ChangeCanister"  x31
data.canisterType  (string, 31/31 records)
    "Gravel"  x14
    "Clay"  x9
    "Bedrock"  x5
    "Sand"  x3
data.floor  (string, 31/31 records)
    "4"  x18
    "5"  x10
    "3"  x3
data.machine  (string, 31/31 records)
    "1"  x30
    "2"  x1
data.row  (string, 31/31 records)
    "TopRow"  x25
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 29 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (5)
- **Intervals:** median 5.53s (p5 0.26s / p95 87506.92s, n=28)
- **`data` key-set variants:** [actionType, featureUsed] x17; [actionType, featureUsed, location] x12
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "MapOpenEvent"  x10
    "MapCloseEvent"  x7
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x5
data.featureUsed  (string, 29/29 records)
    "Map"  x17
    "Waypoint"  x12
data.location  (object, 12/29 records)
data.location.x  (number, 12/29 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 12/29 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 12/29 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 26 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 4 Dev - Dungeon (4); Unit 1 Dev (3); Unit 3 Dev (3); MainMenu (2); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 923.98s (p5 143.40s / p95 224226.11s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "DebugMenuStateChanged"  x26
data.isOpened  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 16639.51s (p5 151.31s / p95 271032.76s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (12); Unit 1 Dev (3); Unit 3 Dev (1)
- **Intervals:** median 4.98s (p5 0.60s / p95 468567.61s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolOpen"  x11
    "argumentationToolClose"  x5
data.argumentationTitle  (string, 16/16 records)
    "Unit 5"  x12
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x9
    "BackingInfoPanel - Evaporation Flow Diagram"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (3)
- **Intervals:** median 130.18s (p5 0.05s / p95 462768.05s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 5"  x3
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 3.08s (p5 1.13s / p95 22.63s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x4
data.boxId  (string, 9/9 records)
    "0"  x5
    "1"  x2
    "2"  x2
data.soilType  (string, 9/9 records)
    "Clay"  x7
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 7 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (7)
- **Intervals:** median 2.07s (p5 0.14s / p95 65150.85s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "Open"  x4
    "Close"  x3
data.toolName  (string, 7/7 records, 7 empty-string)
    ""  x7
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 1.38s (p5 0.42s / p95 3.78s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted Out"  x1
data.featureUsed  (string, 6/6 records)
    "RoofStyle"  x3
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records, 1 empty-string)
    ""  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 431596.53s (p5 74456.50s / p95 511508.91s, n=3)
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

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 1612.34s (p5 1221.70s / p95 27591.05s, n=3)
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
    "A user gesture is required to request Pointer Lock."  x1
    "Failed to start the audio device"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (32 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (97x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*