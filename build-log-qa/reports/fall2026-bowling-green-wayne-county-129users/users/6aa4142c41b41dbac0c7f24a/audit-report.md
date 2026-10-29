# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f24a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f24a
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f24a.jsonl
- **Records:** 13820 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f24a
- **Time span:** 2026-09-23T16:28:05.723000+00:00 .. 2026-10-06T18:45:35.702000+00:00 (314h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f24a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13820 records, 11 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 110 INFO, 0 NOT_TESTED, 97 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4596 | 33.26 | 1 | 9 | 0 | 2026-09-23T16:29:38.883000+00:00 | 2026-10-06T18:45:35.702000+00:00 | 314h 15m |
| PuzzlePieceVisibleEvent | 3212 | 23.24 | 1 | 4 | 0 | 2026-09-24T16:24:49.307000+00:00 | 2026-10-06T16:08:28.570000+00:00 | 287h 43m |
| PlayerPositionEvent | 2483 | 17.97 | 1 | 9 | 0 | 2026-09-23T16:29:33.973000+00:00 | 2026-10-06T18:45:35.015000+00:00 | 314h 16m |
| DialogueEvent | 2173 | 15.72 | 1 | 9 | 1345 | 2026-09-23T16:29:55.170000+00:00 | 2026-10-06T18:45:27.809000+00:00 | 314h 15m |
| ObjectInterEvent | 332 | 2.4 | 1 | 9 | 0 | 2026-09-23T16:43:19.079000+00:00 | 2026-10-06T18:45:35.701000+00:00 | 314h 2m |
| argumentationNodeEvent | 254 | 1.84 | 1 | 4 | 0 | 2026-09-24T16:13:46.400000+00:00 | 2026-10-06T16:56:27.256000+00:00 | 288h 42m |
| TopographicMapEvent | 138 | 1.0 | 1 | 4 | 0 | 2026-09-24T16:20:44.346000+00:00 | 2026-10-05T15:54:38.349000+00:00 | 263h 33m |
| gameWindowFocusEvent | 117 | 0.85 | 1 | 11 | 0 | 2026-09-23T16:28:05.723000+00:00 | 2026-10-06T18:35:43.208000+00:00 | 314h 7m |
| gameWindowUnfocusEvent | 100 | 0.72 | 1 | 10 | 0 | 2026-09-23T16:30:34.348000+00:00 | 2026-10-06T18:35:07.723000+00:00 | 314h 4m |
| questEvent | 100 | 0.72 | 1 | 9 | 100 | 2026-09-23T16:29:55.149000+00:00 | 2026-10-06T18:40:24.202000+00:00 | 314h 10m |
| Soil Key Puzzle | 96 | 0.69 | 1 | 3 | 0 | 2026-09-24T16:34:49.054000+00:00 | 2026-10-01T16:05:41.478000+00:00 | 167h 30m |
| WaterChamberEvent | 53 | 0.38 | 1 | 1 | 0 | 2026-10-06T16:07:06.554000+00:00 | 2026-10-06T16:39:08.751000+00:00 | 32m 2s |
| soilMachine | 29 | 0.21 | 1 | 1 | 0 | 2026-10-01T16:50:28.345000+00:00 | 2026-10-05T15:50:45.197000+00:00 | 95h 0m |
| DEBUGMenu | 28 | 0.2 | 1 | 8 | 0 | 2026-09-23T16:29:33.965000+00:00 | 2026-10-06T16:26:02.619000+00:00 | 311h 56m |
| gameStartEvent | 24 | 0.17 | 1 | 1 | 0 | 2026-09-23T16:28:05.724000+00:00 | 2026-10-06T18:32:12.151000+00:00 | 314h 4m |
| SolarStillDesignEvent | 15 | 0.11 | 1 | 1 | 0 | 2026-10-06T17:03:29.051000+00:00 | 2026-10-06T18:38:08.660000+00:00 | 1h 34m |
| TerasGardenBox | 13 | 0.09 | 1 | 1 | 0 | 2026-10-06T15:49:41.945000+00:00 | 2026-10-06T15:51:09.616000+00:00 | 1m 27s |
| argumentationEvent | 12 | 0.09 | 1 | 4 | 0 | 2026-09-24T16:13:19.003000+00:00 | 2026-10-06T16:56:29.466000+00:00 | 288h 43m |
| argumentationToolEvent | 12 | 0.09 | 1 | 2 | 0 | 2026-09-24T16:13:16.481000+00:00 | 2026-09-29T17:00:51.340000+00:00 | 120h 47m |
| DaniEvent | 8 | 0.06 | 1 | 1 | 0 | 2026-09-29T16:44:37.422000+00:00 | 2026-09-29T16:51:08.835000+00:00 | 6m 31s |
| argumentationAnswerEvent | 8 | 0.06 | 1 | 4 | 0 | 2026-09-24T16:13:57.213000+00:00 | 2026-10-06T16:56:29.435000+00:00 | 288h 42m |
| crash | 8 | 0.06 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 5 | 0.04 | 1 | 2 | 0 | 2026-10-06T15:59:25.771000+00:00 | 2026-10-06T18:32:19.590000+00:00 | 2h 32m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-24T16:18:50.394000+00:00 | 2026-10-06T18:45:35.689000+00:00 | 290h 26m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 432829.079s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 0.382s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 1.464s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 85.061s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.949s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 53.551s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.86s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 15 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 270 ft; 30 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; C,2,II; C,D,2,II; C,D,A,2,II; D,3,II 
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
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 24 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.8x vs baseline. 
  - Observed: 29 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 116 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[219] _id=6ab40231485cab4c954e7868 ts=2026-09-23T16:45:37.2180000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[315] _id=6ab4038b485cab4c954e7f82 ts=2026-09-23T16:51:23.3270000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[422] _id=6ab40500485cab4c954e8a13 ts=2026-09-23T16:57:36.6690000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:23' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[2610] _id=6aba9487485cab4c956a6f7e ts=2026-09-25T16:31:21.85Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2759] _id=6aba9495485cab4c956a71cc ts=2026-09-25T16:44:24.84Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2833] _id=6aba9499485cab4c956a7290 ts=2026-09-25T16:47:53.985Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[9] _id=6ab3fe11485cab4c954e60fa ts=2026-09-23T16:28:05.7240000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[88] _id=6ab400a7485cab4c954e709c ts=2026-09-23T16:39:03.0770000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[627] _id=6ab54b80485cab4c9552de1f ts=2026-09-24T16:10:40.6910000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 117 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 117} 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[8] _id=6ab3fe11485cab4c954e60f8 ts=2026-09-23T16:28:05.7230000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[20] _id=6ab3fea8485cab4c954e6200 ts=2026-09-23T16:30:35.9050000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[85] _id=6ab3ffa1485cab4c954e68d2 ts=2026-09-23T16:34:41.7120000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 100 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 100} 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[19] _id=6ab3fea6485cab4c954e61fe ts=2026-09-23T16:30:34.3480000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[83] _id=6ab3ffa1485cab4c954e68ce ts=2026-09-23T16:34:41.6210000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[595] _id=6ab4067a485cab4c954e939e ts=2026-09-23T17:03:54.5950000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 40 of 138 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[915] _id=6ab54ddc485cab4c9552ef3d ts=2026-09-24T16:20:44.3460000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[924] _id=6ab54ddc485cab4c9552ef43 ts=2026-09-24T16:20:44.7610000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1019] _id=6ab54ee9485cab4c9552fccd ts=2026-09-24T16:25:13.7250000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4595 | 0.0 | 0.799 | 246.215 | 14.531 | 340327.029 | 0.24 | 310 | 16 |
| PuzzlePieceVisibleEvent | 3211 | 0.0 | 0.031 | 322.585 | 1.603 | 345333.868 | 0.19 | 1907 | 6 |
| PlayerPositionEvent | 2471 | 0.437 | 10.0 | 457.76 | 10.695 | 340303.759 | 0.13 | 0 | 14 |
| DialogueEvent | 2172 | 0.001 | 4.197 | 520.871 | 45.925 | 340328.427 | 0.12 | 640 | 17 |
| ObjectInterEvent | 331 | 0.001 | 11.606 | 3415.518 | 625.298 | 340408.83 | 0.02 | 7 | 18 |
| argumentationNodeEvent | 253 | 0.001 | 0.403 | 4108.146 | 5.312 | 600188.557 | 0.01 | 50 | 3 |
| TopographicMapEvent | 137 | 0.021 | 1.828 | 6925.796 | 674.815 | 427742.436 | 0.01 | 3 | 7 |
| gameWindowFocusEvent | 116 | 0.96 | 79.405 | 9748.771 | 79447.978 | 340293.95 | 0.01 | 0 | 26 |
| gameWindowUnfocusEvent | 99 | 0.119 | 53.551 | 11420.943 | 83604.164 | 340495.598 | 0.01 | 0 | 21 |
| questEvent | 99 | 0.001 | 244.102 | 11424.536 | 82614.474 | 340332.847 | 0.01 | 19 | 24 |
| Soil Key Puzzle | 95 | 0.164 | 0.382 | 6347.92 | 15.635 | 257038.667 | 0.01 | 0 | 4 |
| WaterChamberEvent | 52 | 0.162 | 1.464 | 36.965 | 95.449 | 1107.676 | 1.62 | 0 | 1 |
| soilMachine | 28 | 0.271 | 4.86 | 12214.888 | 500.47 | 340719.252 | 0.0 | 0 | 2 |
| DEBUGMenu | 27 | 100.205 | 1010.498 | 41592.172 | 206706.203 | 342724.228 | 0.0 | 0 | 18 |
| gameStartEvent | 23 | 91.438 | 2315.956 | 49158.54 | 240882.814 | 342771.492 | 0.0 | 0 | 18 |
| SolarStillDesignEvent | 14 | 0.637 | 1.722 | 405.686 | 1982.029 | 5656.071 | 0.15 | 0 | 1 |
| TerasGardenBox | 12 | 0.437 | 4.329 | 7.306 | 20.128 | 20.735 | 8.21 | 0 | 0 |
| argumentationEvent | 11 | 0.027 | 68.222 | 94490.042 | 517418.541 | 600189.62 | 0.0 | 2 | 3 |
| argumentationToolEvent | 11 | 0.094 | 1.949 | 39532.26 | 217418.299 | 434744.803 | 0.0 | 0 | 1 |
| DaniEvent | 7 | 0.004 | 1.214 | 55.916 | 270.291 | 385.137 | 1.07 | 2 | 0 |
| argumentationAnswerEvent | 7 | 15.257 | 85.061 | 148478.889 | 550580.087 | 600224.278 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 4 | 857.246 | 1529.449 | 2293.455 | 4708.539 | 5257.674 | 0.03 | 0 | 4 |
| EndOfUnit | 3 | 9990.084 | 432829.079 | 348535.098 | 585790.427 | 602786.132 | 0.0 | 0 | 3 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[7376] _id=6abd4029485cab4c958ede97 ts=2026-09-30T17:00:24.7700000Z == 6aa4142c41b41dbac0c7f24a.jsonl[7372] _id=6abd4029485cab4c958ede9a ts=2026-09-30T17:00:24.7700000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[8960] _id=6abe89af485cab4c95abe7c6 ts=2026-10-01T16:26:23.0040000Z == 6aa4142c41b41dbac0c7f24a.jsonl[8963] _id=6abe89af485cab4c95abe7ca ts=2026-10-01T16:26:23.0040000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[12384] _id=6ac5211fde269131f9b4fb93 ts=2026-10-06T16:26:07.4540000Z == 6aa4142c41b41dbac0c7f24a.jsonl[12385] _id=6ac5211fde269131f9b4fb95 ts=2026-10-06T16:26:07.4540000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 98 group(s), 129 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[1166] _id=6ab54fb5485cab4c95530c2f ts=2026-09-24T16:28:30.7770000Z == 6aa4142c41b41dbac0c7f24a.jsonl[1167] _id=6ab54fb5485cab4c95530c31 ts=2026-09-24T16:28:30.7770000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1516] _id=6ab55012485cab4c955312a3 ts=2026-09-24T16:30:10.0110000Z == 6aa4142c41b41dbac0c7f24a.jsonl[1506] _id=6ab55013485cab4c955312a7 ts=2026-09-24T16:30:10.0110000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1464] _id=6ab55014485cab4c955312d3 ts=2026-09-24T16:30:11.9180000Z == 6aa4142c41b41dbac0c7f24a.jsonl[1465] _id=6ab55015485cab4c955312d7 ts=2026-09-24T16:30:11.9180000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[2592] _id=6ab55462485cab4c95534eef ts=? == 6aa4142c41b41dbac0c7f24a.jsonl[2595] _id=6ab6a4e8485cab4c955c1704 ts=?`; `6aa4142c41b41dbac0c7f24a.jsonl[2896] _id=6aba94a6485cab4c956a7470 ts=? == 6aa4142c41b41dbac0c7f24a.jsonl[4394] _id=6abbe774485cab4c9580c505 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 32 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4142c41b41dbac0c7f24a.jsonl[171] _id=6ab401a6485cab4c954e7610 ts=2026-09-23T16:43:19.0790000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[172] _id=6ab401a7485cab4c954e7614 ts=2026-09-23T16:43:19.0830000Z`; `661ms: 6aa4142c41b41dbac0c7f24a.jsonl[433] _id=6ab40516485cab4c954e8b04 ts=2026-09-23T16:57:58.1290000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[431] _id=6ab40516485cab4c954e8b0e ts=2026-09-23T16:57:58.7900000Z`; `233ms: 6aa4142c41b41dbac0c7f24a.jsonl[431] _id=6ab40516485cab4c954e8b0e ts=2026-09-23T16:57:58.7900000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[434] _id=6ab40516485cab4c954e8b12 ts=2026-09-23T16:57:59.0230000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 413 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `66ms: 6aa4142c41b41dbac0c7f24a.jsonl[1163] _id=6ab54fb5485cab4c95530c29 ts=2026-09-24T16:28:30.6750000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[1165] _id=6ab54fb5485cab4c95530c2b ts=2026-09-24T16:28:30.7410000Z`; `17ms: 6aa4142c41b41dbac0c7f24a.jsonl[1165] _id=6ab54fb5485cab4c95530c2b ts=2026-09-24T16:28:30.7410000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[1164] _id=6ab54fb5485cab4c95530c2d ts=2026-09-24T16:28:30.7580000Z`; `19ms: 6aa4142c41b41dbac0c7f24a.jsonl[1164] _id=6ab54fb5485cab4c95530c2d ts=2026-09-24T16:28:30.7580000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[1166] _id=6ab54fb5485cab4c95530c2f ts=2026-09-24T16:28:30.7770000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 25 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `684ms: 6aa4142c41b41dbac0c7f24a.jsonl[3124] _id=6aba94ba485cab4c956a7887 ts=2026-09-25T17:02:19.51Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[3125] _id=6aba94ba485cab4c956a788b ts=2026-09-25T17:02:20.194Z`; `550ms: 6aa4142c41b41dbac0c7f24a.jsonl[3131] _id=6aba94ba485cab4c956a7891 ts=2026-09-25T17:02:21.447Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[3132] _id=6aba94ba485cab4c956a7895 ts=2026-09-25T17:02:21.997Z`; `456ms: 6aa4142c41b41dbac0c7f24a.jsonl[3132] _id=6aba94ba485cab4c956a7895 ts=2026-09-25T17:02:21.997Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[3135] _id=6aba94ba485cab4c956a7899 ts=2026-09-25T17:02:22.453Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `437ms: 6aa4142c41b41dbac0c7f24a.jsonl[11710] _id=6ac518d9de269131f9b4c345 ts=2026-10-06T15:50:49.0990000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[11715] _id=6ac518d9de269131f9b4c347 ts=2026-10-06T15:50:49.5360000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `877ms: 6aa4142c41b41dbac0c7f24a.jsonl[1035] _id=6ab54f07485cab4c9552ff6f ts=2026-09-24T16:25:43.0560000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[1038] _id=6ab54f07485cab4c9552ff79 ts=2026-09-24T16:25:43.9330000Z`; `937ms: 6aa4142c41b41dbac0c7f24a.jsonl[1039] _id=6ab54f12485cab4c9552fffb ts=2026-09-24T16:25:54.1380000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[1040] _id=6ab54f13485cab4c95530007 ts=2026-09-24T16:25:55.0750000Z`; `751ms: 6aa4142c41b41dbac0c7f24a.jsonl[1048] _id=6ab54f12485cab4c95530005 ts=2026-09-24T16:25:54.7780000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[1049] _id=6ab54f13485cab4c95530013 ts=2026-09-24T16:25:55.5290000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `555ms: 6aa4142c41b41dbac0c7f24a.jsonl[12654] _id=6ac52301de269131f9b51445 ts=2026-10-06T16:34:09.5120000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[12639] _id=6ac52302de269131f9b51453 ts=2026-10-06T16:34:10.0670000Z`; `619ms: 6aa4142c41b41dbac0c7f24a.jsonl[12655] _id=6ac52301de269131f9b51449 ts=2026-10-06T16:34:09.7880000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[12656] _id=6ac52302de269131f9b51459 ts=2026-10-06T16:34:10.4070000Z`; `608ms: 6aa4142c41b41dbac0c7f24a.jsonl[12639] _id=6ac52302de269131f9b51453 ts=2026-10-06T16:34:10.0670000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[12658] _id=6ac52302de269131f9b51461 ts=2026-10-06T16:34:10.6750000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6aa4142c41b41dbac0c7f24a.jsonl[5217] _id=6abbeed2485cab4c958296a3 ts=2026-09-29T17:01:05.9360000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[5232] _id=6abbeed2485cab4c958296a9 ts=2026-09-29T17:01:05.9720000Z`; `27ms: 6aa4142c41b41dbac0c7f24a.jsonl[11555] _id=6ac51792de269131f9b4b093 ts=2026-10-06T15:45:23.8140000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[11556] _id=6ac51793de269131f9b4b0a1 ts=2026-10-06T15:45:23.8410000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 42 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `405ms: 6aa4142c41b41dbac0c7f24a.jsonl[697] _id=6ab54c3a485cab4c9552e155 ts=2026-09-24T16:13:46.4000000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[698] _id=6ab54c3a485cab4c9552e159 ts=2026-09-24T16:13:46.8050000Z`; `19ms: 6aa4142c41b41dbac0c7f24a.jsonl[700] _id=6ab54c3d485cab4c9552e163 ts=2026-09-24T16:13:49.3420000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[701] _id=6ab54c3d485cab4c9552e165 ts=2026-09-24T16:13:49.3610000Z`; `867ms: 6aa4142c41b41dbac0c7f24a.jsonl[758] _id=6ab54c86485cab4c9552e2a7 ts=2026-09-24T16:15:02.8150000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[736] _id=6ab54c87485cab4c9552e2ad ts=2026-09-24T16:15:03.6820000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `300ms: 6aa4142c41b41dbac0c7f24a.jsonl[727] _id=6ab54c7c485cab4c9552e261 ts=2026-09-24T16:14:52.7030000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[728] _id=6ab54c7c485cab4c9552e265 ts=2026-09-24T16:14:53.0030000Z`; `949ms: 6aa4142c41b41dbac0c7f24a.jsonl[742] _id=6ab54c7c485cab4c9552e263 ts=2026-09-24T16:14:52.9090000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[743] _id=6ab54c7d485cab4c9552e26b ts=2026-09-24T16:14:53.8580000Z`; `410ms: 6aa4142c41b41dbac0c7f24a.jsonl[5202] _id=6abbeeb7485cab4c9582964b ts=2026-09-29T17:00:39.9360000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[5203] _id=6abbeeb8485cab4c9582964d ts=2026-09-29T17:00:40.3460000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `960ms: 6aa4142c41b41dbac0c7f24a.jsonl[13314] _id=6ac5292ede269131f9b5de23 ts=2026-10-06T17:00:30.6610000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[13316] _id=6ac5292fde269131f9b5de4b ts=2026-10-06T17:00:31.6210000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `119ms: 6aa4142c41b41dbac0c7f24a.jsonl[10757] _id=6ac3d233de269131f9addb8d ts=2026-10-05T16:37:07.1990000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[10754] _id=6ac3d233de269131f9addb93 ts=2026-10-05T16:37:07.3180000Z`; `921ms: 6aa4142c41b41dbac0c7f24a.jsonl[13308] _id=6ac52928de269131f9b5dd25 ts=2026-10-06T17:00:24.7160000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[13313] _id=6ac52929de269131f9b5dd51 ts=2026-10-06T17:00:25.6370000Z`; `474ms: 6aa4142c41b41dbac0c7f24a.jsonl[13400] _id=6ac52a11de269131f9b609bd ts=2026-10-06T17:04:17.7150000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[13410] _id=6ac52a13de269131f9b60a25 ts=2026-10-06T17:04:18.1890000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4142c41b41dbac0c7f24a.jsonl[13251] _id=6ac52885de269131f9b5bc0f ts=2026-10-06T16:57:41.2040000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[13252] _id=6ac52885de269131f9b5bc16 ts=2026-10-06T16:57:41.2060000Z`; `2ms: 6aa4142c41b41dbac0c7f24a.jsonl[13416] _id=6ac52a34de269131f9b60e2f ts=2026-10-06T17:04:51.1510000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[13417] _id=6ac52a34de269131f9b60e35 ts=2026-10-06T17:04:51.1530000Z`; `6ms: 6aa4142c41b41dbac0c7f24a.jsonl[13488] _id=6ac52ab0de269131f9b61437 ts=2026-10-06T17:06:56.3980000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[13489] _id=6ac52ab0de269131f9b61439 ts=2026-10-06T17:06:56.4040000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `460ms: 6aa4142c41b41dbac0c7f24a.jsonl[9459] _id=6abe91ea485cab4c95ac3b94 ts=2026-10-01T17:01:30.1180000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[9460] _id=6abe91ea485cab4c95ac3b9a ts=2026-10-01T17:01:30.5780000Z`; `355ms: 6aa4142c41b41dbac0c7f24a.jsonl[9460] _id=6abe91ea485cab4c95ac3b9a ts=2026-10-01T17:01:30.5780000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[9473] _id=6abe91ea485cab4c95ac3ba0 ts=2026-10-01T17:01:30.9330000Z`; `550ms: 6aa4142c41b41dbac0c7f24a.jsonl[9473] _id=6abe91ea485cab4c95ac3ba0 ts=2026-10-01T17:01:30.9330000Z ~ 6aa4142c41b41dbac0c7f24a.jsonl[9475] _id=6abe91eb485cab4c95ac3ba8 ts=2026-10-01T17:01:31.4830000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 12m 
  - Evidence: 95h 12m: 6aa4142c41b41dbac0c7f24a.jsonl[8940] _id=6abe89a1485cab4c95abe620 ts=2026-10-01T16:26:09.4770000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9560] _id=6ac3c465de269131f9ad518d ts=2026-10-05T15:38:13.7050000Z; 71h 39m: 6aa4142c41b41dbac0c7f24a.jsonl[2768] _id=6aba9495485cab4c956a71c2 ts=2026-09-25T16:44:16.555Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3183] _id=6aba94be485cab4c956a797d ts=2026-09-28T16:24:00.3160000Z; 24h 10m: 6aa4142c41b41dbac0c7f24a.jsonl[896] _id=6ab54dc3485cab4c9552ed4f ts=2026-09-24T16:20:19.1070000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2621] _id=6aba9486485cab4c956a6f54 ts=2026-09-25T16:31:17.676Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.006s shown 
  - Evidence: 4ms: 6aa4142c41b41dbac0c7f24a.jsonl[4708] _id=6abbeaf8485cab4c95813c0d ts=2026-09-29T16:44:40.6420000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[4709] _id=6abbeaf8485cab4c95813c18 ts=2026-09-29T16:44:40.6460000Z; 6ms: 6aa4142c41b41dbac0c7f24a.jsonl[4707] _id=6abbeaf7485cab4c95813b85 ts=2026-09-29T16:44:39.4220000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[4705] _id=6abbeaf7485cab4c95813b8f ts=2026-09-29T16:44:39.4280000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 94h 32m 
  - Evidence: 94h 32m: 6aa4142c41b41dbac0c7f24a.jsonl[9542] _id=6abe9302485cab4c95ac423c ts=2026-10-01T17:06:10.9420000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9588] _id=6ac3c46dde269131f9ad5251 ts=2026-10-05T15:38:19.3690000Z; 71h 19m: 6aa4142c41b41dbac0c7f24a.jsonl[3188] _id=6aba94be485cab4c956a795f ts=2026-09-25T17:04:08.638Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3027] _id=6aba94bf485cab4c956a79ad ts=2026-09-28T16:24:06.7230000Z; 23h 46m: 6aa4142c41b41dbac0c7f24a.jsonl[2526] _id=6ab553e8485cab4c95534b45 ts=2026-09-24T16:46:31.9860000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2671] _id=6aba948e485cab4c956a70ac ts=2026-09-25T16:32:33.57Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 640 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[11524] _id=6ac51771de269131f9b4ac63 ts=2026-10-06T15:44:50.2320000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11520] _id=6ac51771de269131f9b4ac67 ts=2026-10-06T15:44:50.2330000Z; 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[11538] _id=6ac51783de269131f9b4ae6b ts=2026-10-06T15:45:08.5580000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11539] _id=6ac51783de269131f9b4ae6d ts=2026-10-06T15:45:08.5590000Z; 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[13193] _id=6ac52828de269131f9b5a487 ts=2026-10-06T16:56:08.7920000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13190] _id=6ac52828de269131f9b5a48c ts=2026-10-06T16:56:08.7930000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 26m 
  - Evidence: 167h 26m: 6aa4142c41b41dbac0c7f24a.jsonl[886] _id=6ab54d6a485cab4c9552e8d9 ts=2026-09-24T16:18:50.3940000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[7677] _id=6abe800a485cab4c95ab5734 ts=2026-10-01T15:45:16.5260000Z; 120h 13m: 6aa4142c41b41dbac0c7f24a.jsonl[7677] _id=6abe800a485cab4c95ab5734 ts=2026-10-01T15:45:16.5260000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11875] _id=6ac51ac9de269131f9b4d2ad ts=2026-10-06T15:59:05.6050000Z; 2h 46m: 6aa4142c41b41dbac0c7f24a.jsonl[11875] _id=6ac51ac9de269131f9b4d2ad ts=2026-10-06T15:59:05.6050000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13813] _id=6ac541cfde269131f9b6d4c5 ts=2026-10-06T18:45:35.6890000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 94h 32m 
  - Evidence: 94h 32m: 6aa4142c41b41dbac0c7f24a.jsonl[9544] _id=6abe9304485cab4c95ac4244 ts=2026-10-01T17:06:12.1370000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9570] _id=6ac3c46bde269131f9ad5207 ts=2026-10-05T15:38:19.1660000Z; 71h 20m: 6aa4142c41b41dbac0c7f24a.jsonl[3158] _id=6aba94bd485cab4c956a793b ts=2026-09-25T17:03:32.387Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3193] _id=6aba94be485cab4c956a7986 ts=2026-09-28T16:24:06.6100000Z; 23h 42m: 6aa4142c41b41dbac0c7f24a.jsonl[2579] _id=6ab55457485cab4c95534ee3 ts=2026-09-24T16:48:23.2310000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2614] _id=6aba9486485cab4c956a6f5a ts=2026-09-25T16:31:21.711Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 310 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24a.jsonl[12384] _id=6ac5211fde269131f9b4fb93 ts=2026-10-06T16:26:07.4540000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[12385] _id=6ac5211fde269131f9b4fb95 ts=2026-10-06T16:26:07.4540000Z; 0ms: 6aa4142c41b41dbac0c7f24a.jsonl[7376] _id=6abd4029485cab4c958ede97 ts=2026-09-30T17:00:24.7700000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[7372] _id=6abd4029485cab4c958ede9a ts=2026-09-30T17:00:24.7700000Z; 0ms: 6aa4142c41b41dbac0c7f24a.jsonl[8960] _id=6abe89af485cab4c95abe7c6 ts=2026-10-01T16:26:23.0040000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[8963] _id=6abe89af485cab4c95abe7ca ts=2026-10-01T16:26:23.0040000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 94h 33m 
  - Evidence: 94h 33m: 6aa4142c41b41dbac0c7f24a.jsonl[9505] _id=6abe92da485cab4c95ac4198 ts=2026-10-01T17:05:30.7250000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9605] _id=6ac3c493de269131f9ad54d7 ts=2026-10-05T15:38:59.5550000Z; 71h 25m: 6aa4142c41b41dbac0c7f24a.jsonl[3123] _id=6aba94ba485cab4c956a7883 ts=2026-09-25T17:02:15.507Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3296] _id=6aba956c485cab4c956a89a0 ts=2026-09-28T16:27:25.6870000Z; 24h 27m: 6aa4142c41b41dbac0c7f24a.jsonl[2383] _id=6ab55129485cab4c95531e89 ts=2026-09-24T16:34:49.0600000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3123] _id=6aba94ba485cab4c956a7883 ts=2026-09-25T17:02:15.507Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[10642] _id=6ac3ca14de269131f9ad8b17 ts=2026-10-05T16:02:28.3330000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10647] _id=6ac3ca14de269131f9ad8b19 ts=2026-10-05T16:02:28.3340000Z; 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[10929] _id=6ac3d632de269131f9ae3509 ts=2026-10-05T16:54:10.8190000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10926] _id=6ac3d633de269131f9ae350b ts=2026-10-05T16:54:10.8200000Z; 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[11360] _id=6ac51667de269131f9b49461 ts=2026-10-06T15:40:25.8800000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11358] _id=6ac51667de269131f9b49468 ts=2026-10-06T15:40:25.8810000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 31m 
  - Evidence: 94h 31m: 6aa4142c41b41dbac0c7f24a.jsonl[9545] _id=6abe9315485cab4c95ac427a ts=2026-10-01T17:06:29.9530000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9569] _id=6ac3c46bde269131f9ad5205 ts=2026-10-05T15:38:13.7120000Z; 71h 19m: 6aa4142c41b41dbac0c7f24a.jsonl[3023] _id=6aba94be485cab4c956a796b ts=2026-09-25T17:04:25.327Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3192] _id=6aba94be485cab4c956a7983 ts=2026-09-28T16:24:00.3340000Z; 23h 42m: 6aa4142c41b41dbac0c7f24a.jsonl[2594] _id=6ab5546a485cab4c95534ef9 ts=2026-09-24T16:48:42.3140000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2622] _id=6aba9486485cab4c956a6f58 ts=2026-09-25T16:31:17.682Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 6aa4142c41b41dbac0c7f24a.jsonl[2333] _id=6ab550c8485cab4c95531cb5 ts=2026-09-24T16:33:10.4560000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3344] _id=6aba95bb485cab4c956a9299 ts=2026-09-28T16:28:44.3240000Z; 95h 42m: 6aa4142c41b41dbac0c7f24a.jsonl[8679] _id=6abe8592485cab4c95abc2b0 ts=2026-10-01T16:08:49.3150000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10148] _id=6ac3c78bde269131f9ad7d39 ts=2026-10-05T15:51:37.8620000Z; 47h 27m: 6aa4142c41b41dbac0c7f24a.jsonl[3966] _id=6aba96e2485cab4c956ab3ea ts=2026-09-28T16:33:35.3140000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5627] _id=6abd3259485cab4c958d31f2 ts=2026-09-30T16:01:28.5760000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1907 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24a.jsonl[10096] _id=6ac3c78bde269131f9ad7d3d ts=2026-10-05T15:51:38.5340000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10150] _id=6ac3c78bde269131f9ad7d3f ts=2026-10-05T15:51:38.5340000Z; 0ms: 6aa4142c41b41dbac0c7f24a.jsonl[10148] _id=6ac3c78bde269131f9ad7d39 ts=2026-10-05T15:51:37.8620000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10149] _id=6ac3c78bde269131f9ad7d3b ts=2026-10-05T15:51:37.8620000Z; 0ms: 6aa4142c41b41dbac0c7f24a.jsonl[10154] _id=6ac3c795de269131f9ad7d91 ts=2026-10-05T15:51:47.8330000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10155] _id=6ac3c795de269131f9ad7d93 ts=2026-10-05T15:51:47.8330000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 23m 
  - Evidence: 71h 23m: 6aa4142c41b41dbac0c7f24a.jsonl[3156] _id=6aba94bd485cab4c956a792d ts=2026-09-25T17:03:27.017Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3295] _id=6aba956c485cab4c956a899c ts=2026-09-28T16:27:25.6840000Z; 47h 32m: 6aa4142c41b41dbac0c7f24a.jsonl[3325] _id=6aba9593485cab4c956a8db0 ts=2026-09-28T16:28:04.3780000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5587] _id=6abd3221485cab4c958d2d52 ts=2026-09-30T16:00:33.9560000Z; 24h 27m: 6aa4142c41b41dbac0c7f24a.jsonl[2385] _id=6ab5512c485cab4c95531e9b ts=2026-09-24T16:34:52.0350000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3122] _id=6aba94ba485cab4c956a787b ts=2026-09-25T17:02:15.474Z
- **INFO / Info** `SolarStillDesignEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 34m 
  - Evidence: 1h 34m: 6aa4142c41b41dbac0c7f24a.jsonl[13356] _id=6ac529ebde269131f9b60213 ts=2026-10-06T17:03:38.8560000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13627] _id=6ac54002de269131f9b69f8d ts=2026-10-06T18:37:54.9270000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 118h 49m 
  - Evidence: 118h 49m: 6aa4142c41b41dbac0c7f24a.jsonl[7513] _id=6abd415e485cab4c958ef664 ts=2026-09-30T17:05:34.6880000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[10362] _id=6ac3c83dde269131f9ad8147 ts=2026-10-05T15:54:37.1240000Z; 72h 3m: 6aa4142c41b41dbac0c7f24a.jsonl[2984] _id=6aba94af485cab4c956a763e ts=2026-09-25T16:56:28.136Z -> 6aa4142c41b41dbac0c7f24a.jsonl[4313] _id=6aba9cf3485cab4c956b3e2b ts=2026-09-28T16:59:31.8930000Z; 23h 55m: 6aa4142c41b41dbac0c7f24a.jsonl[2460] _id=6ab55248485cab4c95532d47 ts=2026-09-24T16:39:36.5330000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2709] _id=6aba9491485cab4c956a7135 ts=2026-09-25T16:34:42.443Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.021s..0.047s shown 
  - Evidence: 21ms: 6aa4142c41b41dbac0c7f24a.jsonl[2840] _id=6aba949a485cab4c956a72b8 ts=2026-09-25T16:48:19.483Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2845] _id=6aba949a485cab4c956a72ba ts=2026-09-25T16:48:19.504Z; 22ms: 6aa4142c41b41dbac0c7f24a.jsonl[2723] _id=6aba9492485cab4c956a713e ts=2026-09-25T16:34:55.598Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2724] _id=6aba9492485cab4c956a7142 ts=2026-09-25T16:34:55.62Z; 47ms: 6aa4142c41b41dbac0c7f24a.jsonl[2845] _id=6aba949a485cab4c956a72ba ts=2026-09-25T16:48:19.504Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2846] _id=6aba949b485cab4c956a72c6 ts=2026-09-25T16:48:19.551Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 18m 27s 
  - Evidence: 18m 27s: 6aa4142c41b41dbac0c7f24a.jsonl[12311] _id=6ac51cdcde269131f9b4e03b ts=2026-10-06T16:07:55.9030000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[12422] _id=6ac5212dde269131f9b4fc57 ts=2026-10-06T16:26:23.5790000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 166h 43m 
  - Evidence: 166h 43m: 6aa4142c41b41dbac0c7f24a.jsonl[5230] _id=6abbeed1485cab4c958296a1 ts=2026-09-29T17:01:05.9160000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11519] _id=6ac51771de269131f9b4ac5d ts=2026-10-06T15:44:50.1940000Z; 120h 45m: 6aa4142c41b41dbac0c7f24a.jsonl[771] _id=6ab54c9a485cab4c9552e309 ts=2026-09-24T16:15:22.2740000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5230] _id=6abbeed1485cab4c958296a1 ts=2026-09-29T17:01:05.9160000Z; 1h 10m: 6aa4142c41b41dbac0c7f24a.jsonl[11554] _id=6ac51792de269131f9b4b091 ts=2026-10-06T15:45:23.7940000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13188] _id=6ac52828de269131f9b5a481 ts=2026-10-06T16:56:08.7490000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 166h 43m 
  - Evidence: 166h 43m: 6aa4142c41b41dbac0c7f24a.jsonl[5232] _id=6abbeed2485cab4c958296a9 ts=2026-09-29T17:01:05.9720000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11480] _id=6ac5174dde269131f9b4aa2f ts=2026-10-06T15:44:15.5920000Z; 120h 44m: 6aa4142c41b41dbac0c7f24a.jsonl[768] _id=6ab54c9a485cab4c9552e30d ts=2026-09-24T16:15:22.2980000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5132] _id=6abbee71485cab4c9582952d ts=2026-09-29T16:59:29.7590000Z; 1h 9m: 6aa4142c41b41dbac0c7f24a.jsonl[11556] _id=6ac51793de269131f9b4b0a1 ts=2026-10-06T15:45:23.8410000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13114] _id=6ac527f0de269131f9b5981d ts=2026-10-06T16:55:12.2640000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.036s shown 
  - Evidence: 27ms: 6aa4142c41b41dbac0c7f24a.jsonl[11555] _id=6ac51792de269131f9b4b093 ts=2026-10-06T15:45:23.8140000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11556] _id=6ac51793de269131f9b4b0a1 ts=2026-10-06T15:45:23.8410000Z; 36ms: 6aa4142c41b41dbac0c7f24a.jsonl[5217] _id=6abbeed2485cab4c958296a3 ts=2026-09-29T17:01:05.9360000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5232] _id=6abbeed2485cab4c958296a9 ts=2026-09-29T17:01:05.9720000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 166h 43m 
  - Evidence: 166h 43m: 6aa4142c41b41dbac0c7f24a.jsonl[5216] _id=6abbeed0485cab4c95829699 ts=2026-09-29T17:01:04.2600000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11476] _id=6ac5174bde269131f9b4a9e5 ts=2026-10-06T15:44:12.8170000Z; 120h 44m: 6aa4142c41b41dbac0c7f24a.jsonl[767] _id=6ab54c96485cab4c9552e304 ts=2026-09-24T16:15:18.8800000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5122] _id=6abbee83485cab4c9582956b ts=2026-09-29T16:59:47.4290000Z; 1h 9m: 6aa4142c41b41dbac0c7f24a.jsonl[11559] _id=6ac51791de269131f9b4b05b ts=2026-10-06T15:45:22.2150000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13119] _id=6ac527f1de269131f9b5984b ts=2026-10-06T16:55:13.0620000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 50 interval(s) ≤ 0.001s..0.018s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[5164] _id=6abbeeb5485cab4c9582963f ts=2026-09-29T17:00:37.1460000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5200] _id=6abbeeb5485cab4c95829641 ts=2026-09-29T17:00:37.1470000Z; 2ms: 6aa4142c41b41dbac0c7f24a.jsonl[13157] _id=6ac52818de269131f9b59ff7 ts=2026-10-06T16:55:52.2920000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13155] _id=6ac52818de269131f9b59ffc ts=2026-10-06T16:55:52.2940000Z; 18ms: 6aa4142c41b41dbac0c7f24a.jsonl[11486] _id=6ac51751de269131f9b4aa93 ts=2026-10-06T15:44:19.5550000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[11492] _id=6ac51751de269131f9b4aa95 ts=2026-10-06T15:44:19.5730000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 120h 45m 
  - Evidence: 120h 45m: 6aa4142c41b41dbac0c7f24a.jsonl[743] _id=6ab54c7d485cab4c9552e26b ts=2026-09-24T16:14:53.8580000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[5165] _id=6abbeeb6485cab4c95829647 ts=2026-09-29T17:00:38.6610000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 1h 27m 
  - Evidence: 1h 27m: 6aa4142c41b41dbac0c7f24a.jsonl[13414] _id=6ac52a29de269131f9b60cd3 ts=2026-10-06T17:04:41.9160000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13524] _id=6ac53eb3de269131f9b679a1 ts=2026-10-06T18:32:19.5900000Z; 26m 36s: 6aa4142c41b41dbac0c7f24a.jsonl[11893] _id=6ac51addde269131f9b4d30d ts=2026-10-06T15:59:25.7710000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[12390] _id=6ac52117de269131f9b4fb4d ts=2026-10-06T16:26:02.5450000Z; 24m 22s: 6aa4142c41b41dbac0c7f24a.jsonl[12882] _id=6ac52473de269131f9b52435 ts=2026-10-06T16:40:19.7910000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13414] _id=6ac52a29de269131f9b60cd3 ts=2026-10-06T17:04:41.9160000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 12m 
  - Evidence: 95h 12m: 6aa4142c41b41dbac0c7f24a.jsonl[8930] _id=6abe896c485cab4c95abe272 ts=2026-10-01T16:25:16.2260000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9559] _id=6ac3c460de269131f9ad513f ts=2026-10-05T15:38:07.7180000Z; 71h 39m: 6aa4142c41b41dbac0c7f24a.jsonl[2767] _id=6aba9495485cab4c956a71c0 ts=2026-09-25T16:43:58.394Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3191] _id=6aba94be485cab4c956a7979 ts=2026-09-28T16:23:34.2100000Z; 24h 10m: 6aa4142c41b41dbac0c7f24a.jsonl[894] _id=6ab54dbd485cab4c9552ece9 ts=2026-09-24T16:20:13.0730000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2620] _id=6aba9486485cab4c956a6f50 ts=2026-09-25T16:30:58.869Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 94h 31m 
  - Evidence: 94h 31m: 6aa4142c41b41dbac0c7f24a.jsonl[9509] _id=6abe9319485cab4c95ac4280 ts=2026-10-01T17:06:33.7680000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9558] _id=6ac3c45fde269131f9ad513d ts=2026-10-05T15:38:07.7180000Z; 71h 39m: 6aa4142c41b41dbac0c7f24a.jsonl[2730] _id=6aba9495485cab4c956a71bc ts=2026-09-25T16:43:58.383Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3190] _id=6aba94be485cab4c956a7973 ts=2026-09-28T16:23:34.1750000Z; 23h 42m: 6aa4142c41b41dbac0c7f24a.jsonl[2593] _id=6ab55464485cab4c95534ef3 ts=2026-09-24T16:48:36.1170000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2613] _id=6aba9485485cab4c956a6f4c ts=2026-09-25T16:30:58.867Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 94h 34m 
  - Evidence: 94h 34m: 6aa4142c41b41dbac0c7f24a.jsonl[9546] _id=6abe9319485cab4c95ac427e ts=2026-10-01T17:06:33.7570000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9706] _id=6ac3c529de269131f9ad5d4e ts=2026-10-05T15:41:29.3550000Z; 71h 24m: 6aa4142c41b41dbac0c7f24a.jsonl[3189] _id=6aba94be485cab4c956a7967 ts=2026-09-25T17:04:25.208Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3361] _id=6aba95cc485cab4c956a958b ts=2026-09-28T16:29:01.3640000Z; 23h 54m: 6aa4142c41b41dbac0c7f24a.jsonl[2587] _id=6ab55468485cab4c95534ef7 ts=2026-09-24T16:48:40.5000000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2758] _id=6aba9494485cab4c956a71b6 ts=2026-09-25T16:43:21.928Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 94h 32m 
  - Evidence: 94h 32m: 6aa4142c41b41dbac0c7f24a.jsonl[9537] _id=6abe92fe485cab4c95ac422a ts=2026-10-01T17:06:06.3850000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9587] _id=6ac3c46dde269131f9ad524f ts=2026-10-05T15:38:19.2320000Z; 71h 22m: 6aa4142c41b41dbac0c7f24a.jsonl[3095] _id=6aba94b9485cab4c956a7839 ts=2026-09-25T17:01:53.72Z -> 6aa4142c41b41dbac0c7f24a.jsonl[3186] _id=6aba94bf485cab4c956a79b3 ts=2026-09-28T16:24:06.7690000Z; 23h 44m: 6aa4142c41b41dbac0c7f24a.jsonl[2524] _id=6ab553e3485cab4c95534b13 ts=2026-09-24T16:46:27.2530000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[2610] _id=6aba9487485cab4c956a6f7e ts=2026-09-25T16:31:21.85Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24a.jsonl[12469] _id=6ac5217dde269131f9b50091 ts=2026-10-06T16:27:44.4270000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[12471] _id=6ac5217dde269131f9b50095 ts=2026-10-06T16:27:44.4280000Z; 2ms: 6aa4142c41b41dbac0c7f24a.jsonl[12368] _id=6ac51d07de269131f9b4e1ab ts=2026-10-06T16:08:39.1850000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[12369] _id=6ac51d07de269131f9b4e1ad ts=2026-10-06T16:08:39.1870000Z; 2ms: 6aa4142c41b41dbac0c7f24a.jsonl[13251] _id=6ac52885de269131f9b5bc0f ts=2026-10-06T16:57:41.2040000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[13252] _id=6ac52885de269131f9b5bc16 ts=2026-10-06T16:57:41.2060000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 38m 
  - Evidence: 94h 38m: 6aa4142c41b41dbac0c7f24a.jsonl[9477] _id=6abe91ed485cab4c95ac3bb2 ts=2026-10-01T17:01:33.5280000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9654] _id=6ac3c4dcde269131f9ad5a21 ts=2026-10-05T15:40:12.7800000Z; 10m 53s: 6aa4142c41b41dbac0c7f24a.jsonl[9256] _id=6abe8f5c485cab4c95ac222b ts=2026-10-01T16:50:36.9080000Z -> 6aa4142c41b41dbac0c7f24a.jsonl[9459] _id=6abe91ea485cab4c95ac3b94 ts=2026-10-01T17:01:30.1180000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[780] _id=6ab54cb5485cab4c9552e387 ts=2026-09-24T16:15:49.0100000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2688] _id=6aba948f485cab4c956a70c6 ts=2026-09-25T16:32:57.798Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2696] _id=6aba948f485cab4c956a70d2 ts=2026-09-25T16:33:01.627Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 78 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[1206] _id=6ab54fc6485cab4c95530d3d ts=2026-09-24T16:28:53.5150000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1272] _id=6ab54fd4485cab4c95530e31 ts=2026-09-24T16:29:07.3610000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1532] _id=6ab5501c485cab4c9553132f ts=2026-09-24T16:30:19.4220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 165 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[1093] _id=6ab54fb2485cab4c95530bd1 ts=2026-09-24T16:25:05.8820000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1130] _id=6ab54fb2485cab4c95530bdc ts=2026-09-24T16:25:06.0260000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1137] _id=6ab54fb3485cab4c95530bed ts=2026-09-24T16:28:20.4180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Finished' preceded by 'Started' per Unit 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[3122] _id=6aba94ba485cab4c956a787b ts=2026-09-25T17:02:15.474Z`; `6aa4142c41b41dbac0c7f24a.jsonl[3156] _id=6aba94bd485cab4c956a792d ts=2026-09-25T17:03:27.017Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[2709] _id=6aba9491485cab4c956a7135 ts=2026-09-25T16:34:42.443Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2724] _id=6aba9492485cab4c956a7142 ts=2026-09-25T16:34:55.62Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2732] _id=6aba9492485cab4c956a714e ts=2026-09-25T16:34:55.681Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[5232] _id=6abbeed2485cab4c958296a9 ts=2026-09-29T17:01:05.9720000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[11556] _id=6ac51793de269131f9b4b0a1 ts=2026-10-06T15:45:23.8410000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[701] _id=6ab54c3d485cab4c9552e165 ts=2026-09-24T16:13:49.3610000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[5169] _id=6abbee96485cab4c958295cb ts=2026-09-29T17:00:06.6630000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[5197] _id=6abbeeb2485cab4c95829631 ts=2026-09-29T17:00:34.8330000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[11893] _id=6ac51addde269131f9b4d30d ts=2026-10-06T15:59:25.7710000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[12390] _id=6ac52117de269131f9b4fb4d ts=2026-10-06T16:26:02.5450000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[12882] _id=6ac52473de269131f9b52435 ts=2026-10-06T16:40:19.7910000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[2806] _id=6aba9499485cab4c956a7280 ts=2026-09-25T16:47:29.424Z`; `6aa4142c41b41dbac0c7f24a.jsonl[5622] _id=6abd3255485cab4c958d31a0 ts=2026-09-30T16:01:25.4100000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[12470] _id=6ac5217dde269131f9b5008c ts=2026-10-06T16:27:44.4160000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 8 records 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[2592] _id=6ab55462485cab4c95534eef ts=?`; `6aa4142c41b41dbac0c7f24a.jsonl[2595] _id=6ab6a4e8485cab4c955c1704 ts=?`; `6aa4142c41b41dbac0c7f24a.jsonl[2896] _id=6aba94a6485cab4c956a7470 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 402 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[1302] _id=6ab54fd8485cab4c95530e89 ts=2026-09-24T16:29:11.7260000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1303] _id=6ab54fd8485cab4c95530e8d ts=2026-09-24T16:29:11.7290000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1388] _id=6ab54ff6485cab4c955310f9 ts=2026-09-24T16:29:42.0210000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 612 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[1139] _id=6ab54fb3485cab4c95530bf5 ts=2026-09-24T16:28:20.4690000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1156] _id=6ab54fb4485cab4c95530c0b ts=2026-09-24T16:28:24.5420000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[1145] _id=6ab54fb4485cab4c95530c15 ts=2026-09-24T16:28:25.6840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[5180] _id=6abbee96485cab4c958295c3 ts=2026-09-29T17:00:02.7420000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[5173] _id=6abbee9c485cab4c958295dd ts=2026-09-29T17:00:11.9790000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[5175] _id=6abbee9c485cab4c958295e3 ts=2026-09-29T17:00:12.3480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[727] _id=6ab54c7c485cab4c9552e261 ts=2026-09-24T16:14:52.7030000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[728] _id=6ab54c7c485cab4c9552e265 ts=2026-09-24T16:14:53.0030000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[5202] _id=6abbeeb7485cab4c9582964b ts=2026-09-29T17:00:39.9360000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'DialogueStartEvent' (totals: 420 start, 408 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 124 unmatched 'BecameCameraCentered' (totals: 672 open, 626 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 93 unmatched 'BecameVisible' (totals: 921 open, 993 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 112 open, 118 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 9 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 27 unmatched 'questActiveEvent' (totals: 62 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 276 of 13811 adjacent _id pairs reverse in client time; worst 87239.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f24a.jsonl[2594] _id=6ab5546a485cab4c95534ef9 ts=2026-09-24T16:48:42.3140000Z`; `6aa4142c41b41dbac0c7f24a.jsonl[2606] _id=6aba9484485cab4c956a6f1c ts=2026-09-23T16:34:43.119Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -431329.62s, max +3.97s over 13812 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f24a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 8 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4596 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (827); Unit 3 Dungeon Dev (768); Unit 3 Dev (655); Unit 2 Prod (Refactor) (604); Unit 4 Dev - Anderson Base (582); Unit 5 Dev - Dungeon (373); Unit 1 Dev (343); Unit 4 Dev (236); Unit 5 Dev (208)
- **Intervals:** median 0.80s (p5 0.02s / p95 14.53s, n=4595)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4596/4596 records)
    "pressed"  x4596
data.actionType  (string, 4596/4596 records)
    "Move"  x3471
    "Interact"  x467
    "Jump"  x420
    "Sprint"  x79
    "Ascend"  x69
    "Hoverboard"  x57
    "Map"  x19
    "Pause"  x5
    "SkipCinematic"  x4
    "Descend"  x3
    "ToggleDebug"  x2
data.key  (string, 4596/4596 records, 9 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4596/4596 records)
    "Player"  x3813
    "Drone"  x783
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3212 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1610); Unit 4 Dev (848); Unit 3 Dungeon Dev (406); Unit 5 Dev - Dungeon (348)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.60s, n=3211)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3212/3212 records)
    "BecameInvisible"  x993
    "BecameVisible"  x921
    "BecameCameraCentered"  x672
    "BecameCameraUncentered"  x626
data.pieceId  (string, 3212/3212 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3212/3212 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2483 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (587); Unit 3 Dungeon Dev (298); Unit 4 Dev - Dungeon (293); Unit 4 Dev - Anderson Base (271); Unit 3 Dev (262); Unit 5 Dev (239); Unit 1 Dev (234); Unit 4 Dev (176); Unit 5 Dev - Dungeon (123)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.69s, n=2471)
- **Fields under `data`:**

```text
data.position  (object, 2483/2483 records)
data.position.x  (number, 2483/2483 records)
    numeric range -707.451 .. 1550.08 (666 unique)
data.position.y  (number, 2483/2483 records)
    numeric range -115.127 .. 222.214 (455 unique)
data.position.z  (number, 2483/2483 records)
    numeric range -1286.16 .. 1576.32 (665 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2173 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (464); Unit 3 Dev (327); Unit 5 Dev (308); Unit 4 Dev (259); Unit 3 Dungeon Dev (218); Unit 1 Dev (208); Unit 4 Dev - Dungeon (165); Unit 4 Dev - Anderson Base (152); Unit 5 Dev - Dungeon (72)
- **eventKey:** present on 1345 of 2173 records
- **Intervals:** median 4.20s (p5 0.00s / p95 45.92s, n=2172)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1345; [conversationId, dialogueEventType] x828
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2173/2173 records)
    numeric range 8 .. 118 (53 unique)
data.dialogueEventType  (string, 2173/2173 records)
    "DialogueNodeEvent"  x1345
    "DialogueStartEvent"  x420
    "DialogueFinishEvent"  x408
data.nodeId  (number, 1345/2173 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 332 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (118); Unit 3 Dungeon Dev (62); Unit 2 Prod (Refactor) (37); Unit 4 Dev - Anderson Base (26); Unit 4 Dev (25); Unit 5 Dev (25); Unit 1 Dev (15); Unit 5 Dev - Dungeon (13); Unit 3 Dev (11)
- **Intervals:** median 11.61s (p5 0.25s / p95 625.30s, n=331)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 332/332 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 332/332 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 254 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (73); Unit 5 Dev (70); Unit 4 Dev - Anderson Base (65); Unit 1 Dev (46)
- **Intervals:** median 0.40s (p5 0.03s / p95 5.31s, n=253)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 254/254 records)
    "argumentationNodeHoverEnd"  x118
    "argumentationNodeHoverStart"  x112
    "argumentationNodeAdd"  x20
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 254/254 records)
    "Unit 3 - Pollution Upstream"  x73
    "Unit 5"  x70
    "Unit 4 - Flooding"  x65
    "Unit 1 - Freshwater"  x35
    "Unit 1 - Argumentation Tutorial"  x11
data.nodeName  (string, 254/254 records)
    "A"  x47
    "B"  x32
    "I"  x31
    "C"  x24
    "II"  x21
    "1"  x20
    "3"  x19
    "2"  x18
    "4"  x18
    "5"  x14
    "D"  x10
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 138 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (93); Unit 3 Dev (41); Unit 3 Dungeon Dev (2); Unit 4 Dev (2)
- **Intervals:** median 1.83s (p5 0.29s / p95 674.82s, n=137)
- **`data` key-set variants:** [actionType, featureUsed, location] x50; [actionType, featureUsed] x48; [actionType, featureUsed, legendName] x40
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 138/138 records)
    "WaypointMoveEvent"  x42
    "MapCloseEvent"  x31
    "Selected"  x28
    "MapOpenEvent"  x17
    "Unselected"  x12
    "WaypointSetEvent"  x7
    "WaypointResetEvent"  x1
data.featureUsed  (string, 138/138 records)
    "Waypoint"  x50
    "Map"  x48
    "Legend"  x40
data.legendName  (string, 40/138 records)
    "360 ft"  x10
    "0 ft"  x5
    "180 ft"  x4
    "120 ft"  x3
    "30 ft"  x3
    "60 ft"  x3
    "90 ft"  x3
    "150 ft"  x2
    "210 ft"  x2
    "330 ft"  x2
    "Water"  x2
    "270 ft"  x1
data.location  (object, 50/138 records)
data.location.x  (number, 50/138 records)
    numeric range -352.09 .. 311.135 (46 unique)
data.location.y  (number, 50/138 records)
    numeric range -368.5 .. 353.5 (43 unique)
data.location.z  (number, 50/138 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 117 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (29); MainMenu (24); Unit 5 Dev (24); Unit 4 Dev - Anderson Base (10); Unit 4 Dev - Dungeon (8); Unit 4 Dev (7); Unit 1 Dev (5); Unit 3 Dev (4); Unit 5 Dev - Dungeon (4); Transition (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 79.41s (p5 1.70s / p95 79447.98s, n=116)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 117/117 records)
    true  x117
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 100 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (33); Unit 5 Dev (25); Unit 4 Dev - Anderson Base (11); Unit 4 Dev - Dungeon (8); Unit 4 Dev (7); Unit 1 Dev (5); Unit 3 Dev (4); Unit 5 Dev - Dungeon (4); Unit 3 Dungeon Dev (2); Transition (1)
- **Intervals:** median 53.55s (p5 1.51s / p95 83604.16s, n=99)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 100/100 records)
    false  x100
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `questEvent` — 100 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 4 Dev - Dungeon (16); Unit 1 Dev (15); Unit 5 Dev (14); Unit 3 Dev (12); Unit 5 Dev - Dungeon (9); Unit 4 Dev (8); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 100 of 100 records
- **Intervals:** median 244.10s (p5 0.00s / p95 82614.47s, n=99)
- **`data` key-set variants:** [questEventType, questID, questName] x62; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 100/100 records)
    "questActiveEvent"  x62
    "questFinishEvent"  x38
data.questID  (string, 100/100 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 100/100 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/100 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 96 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (66); Unit 3 Dev (18); Unit 4 Dev (12)
- **Intervals:** median 0.38s (p5 0.18s / p95 15.64s, n=95)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x86; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/96 records)
    "Finished"  x6
    "Started"  x4
data.Unit  (string, 10/96 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 86/96 records)
    "RightDrag"  x64
    "LeftDrag"  x22
data.currentSoilType  (string, 86/96 records)
    "SAND"  x46
    "CLAY"  x10
    "CLAYSAND"  x10
    "SANDGRAVEL"  x9
    "CLAYROCK"  x6
    "GRAVEL"  x4
    "BEDROCK"  x1
data.isCorrectSelection  (string, 86/96 records)
    "true"  x48
    "false"  x38
data.waterLevelStatus  (string, 86/96 records)
    "Proper"  x61
    "TooHigh"  x23
    "TooLow"  x2
data.waterRetentionChange  (string, 86/96 records)
    "NoChange"  x48
    "Decrease"  x22
    "Increase"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 53 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (53)
- **Intervals:** median 1.46s (p5 0.17s / p95 95.45s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "On"  x33
    "Off"  x20
data.floor  (string, 53/53 records)
    "4"  x37
    "3"  x11
    "2"  x3
    "1"  x2
data.machineNumber  (string, 53/53 records)
    "One"  x52
    "Two"  x1
data.machineType  (string, 53/53 records)
    "Condenser"  x35
    "Evaporator"  x10
    "DualChamber_Condenser"  x4
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 53/53 records)
    "3"  x24
    "2"  x23
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 29 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (29)
- **Intervals:** median 4.86s (p5 0.39s / p95 500.47s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "ChangeCanister"  x29
data.canisterType  (string, 29/29 records)
    "Clay"  x10
    "Gravel"  x8
    "Bedrock"  x6
    "Sand"  x5
data.floor  (string, 29/29 records)
    "5"  x14
    "4"  x7
    "3"  x6
    "2"  x2
data.machine  (string, 29/29 records)
    "1"  x27
    "2"  x2
data.row  (string, 29/29 records)
    "TopRow"  x21
    "BottomRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (3); Unit 4 Dev (3); Unit 4 Dev - Dungeon (3); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 1010.50s (p5 129.18s / p95 206706.20s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 24 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (24)
- **Intervals:** median 2315.96s (p5 130.97s / p95 240882.81s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 15 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (15)
- **Intervals:** median 1.72s (p5 0.66s / p95 1982.03s, n=14)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x13; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "optionSelected"  x13
    "DesignSubmitted"  x2
data.designSelections  (object, 2/15 records)
data.designSelections.glassRoofTemperature  (string, 2/15 records)
    "Cold"  x2
data.designSelections.roofCovering  (string, 2/15 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/15 records)
    "Tilted In"  x1
    "Tilted Out"  x1
data.featureUsed  (string, 15/15 records)
    "RoofStyle"  x6
    "ExtraCovering"  x4
    "GlassRoofTemperature"  x3
    "Submit"  x2
data.selectedOption  (string, 13/15 records)
    "Tilted In"  x3
    "Cold"  x2
    "Covered"  x2
    "Tilted Out"  x2
    "Uncovered"  x2
    "Flat"  x1
    "Hot"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 13 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (13)
- **Intervals:** median 4.33s (p5 0.78s / p95 20.13s, n=12)
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x6
data.boxId  (string, 13/13 records)
    "0"  x8
    "2"  x3
    "1"  x2
data.soilType  (string, 13/13 records)
    "Gravel"  x6
    "Clay"  x4
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 68.22s (p5 0.03s / p95 517418.54s, n=11)
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
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (5)
- **Intervals:** median 1.95s (p5 0.15s / p95 217418.30s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (8)
- **Intervals:** median 1.21s (p5 0.00s / p95 270.29s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 6 empty-string)
    ""  x6
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationAnswerEvent` — 8 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 5 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 85.06s (p5 16.18s / p95 550580.09s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "submitAnswerEvent"  x8
data.answerSubmitted  (string, 8/8 records)
    "1,"  x1
    "A,1,I"  x1
    "A,5,I"  x1
    "C,2,II"  x1
    "C,D,2,II"  x1
    "C,D,A,2,II"  x1
    "D,3,II"  x1
    "D,C,3,II"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 4 - Flooding"  x3
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `crash` — 8 records

- **Scenes:** <missing sceneName> (8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 8/8 records)
    true  x8
data.message  (string, 8/8 records)
    "A user gesture is required to request Pointer Lock."  x5
    "Permissions check failed"  x3
data.phase  (string, 8/8 records)
    "running"  x8
data.stack  (string, 8/8 records, 5 empty-string)
    ""  x5
    "TypeError: Permissions check failed"  x3
data.type  (string, 8/8 records)
    "unhandled_rejection"  x8
data.unitId  (string, 8/8 records)
    "unit2"  x4
    "unit4"  x2
    "unit3"  x1
    "unit5"  x1
data.workspace  (string, 8/8 records)
    "mhs"  x8
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 1529.45s (p5 947.98s / p95 4708.54s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x5
data.chatID  (string, 5/5 records)
    "NA"  x5
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 432829.08s (p5 52273.98s / p95 585790.43s, n=3)
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

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (66 records)
- `TerasGardenBox` data.actionType: "" (7x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (28x); "Unselected" (12x); "WaypointMoveEvent" (42x); "WaypointResetEvent" (1x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (40x); "Waypoint" (50x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*