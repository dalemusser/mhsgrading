# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f24c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f24c
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f24c.jsonl
- **Records:** 9411 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f24c
- **Time span:** 2026-09-23T16:30:12.379000+00:00 .. 2026-10-07T17:07:42.822000+00:00 (336h 37m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f24c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 9411 records, 11 scenes.
- Findings: **0 FAIL**, **29 WARNING**, 102 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2608 | 27.71 | 1 | 9 | 0 | 2026-09-23T16:31:42.513000+00:00 | 2026-10-07T17:07:33.270000+00:00 | 336h 35m |
| PuzzlePieceVisibleEvent | 1974 | 20.98 | 1 | 4 | 0 | 2026-09-24T16:17:19.733000+00:00 | 2026-10-07T16:39:18.458000+00:00 | 312h 21m |
| DialogueEvent | 1714 | 18.21 | 1 | 9 | 1045 | 2026-09-23T16:31:59.449000+00:00 | 2026-10-07T17:07:28.068000+00:00 | 336h 35m |
| PlayerPositionEvent | 1670 | 17.75 | 1 | 9 | 0 | 2026-09-23T16:31:37.264000+00:00 | 2026-10-07T17:07:36.894000+00:00 | 336h 35m |
| argumentationNodeEvent | 484 | 5.14 | 1 | 4 | 0 | 2026-09-23T16:55:18.007000+00:00 | 2026-10-07T16:56:34.850000+00:00 | 336h 1m |
| ObjectInterEvent | 302 | 3.21 | 1 | 9 | 0 | 2026-09-23T16:38:06.269000+00:00 | 2026-10-07T17:04:26.639000+00:00 | 336h 26m |
| TopographicMapEvent | 236 | 2.51 | 1 | 2 | 0 | 2026-09-24T16:12:58.227000+00:00 | 2026-10-01T16:30:24.650000+00:00 | 168h 17m |
| questEvent | 75 | 0.8 | 1 | 9 | 75 | 2026-09-23T16:31:59.429000+00:00 | 2026-10-07T17:07:22.181000+00:00 | 336h 35m |
| soilMachine | 65 | 0.69 | 1 | 1 | 0 | 2026-10-01T17:04:09.534000+00:00 | 2026-10-05T16:48:14.338000+00:00 | 95h 44m |
| Soil Key Puzzle | 58 | 0.62 | 1 | 3 | 0 | 2026-09-24T16:23:45.343000+00:00 | 2026-10-01T16:51:59.969000+00:00 | 168h 28m |
| WaterChamberEvent | 47 | 0.5 | 1 | 1 | 0 | 2026-10-06T16:55:04.325000+00:00 | 2026-10-07T16:46:08.920000+00:00 | 23h 51m |
| gameWindowFocusEvent | 30 | 0.32 | 1 | 8 | 0 | 2026-09-23T16:30:12.379000+00:00 | 2026-10-07T17:07:42.780000+00:00 | 336h 37m |
| DaniEvent | 24 | 0.26 | 1 | 2 | 0 | 2026-09-24T16:13:02.277000+00:00 | 2026-09-30T17:05:32.238000+00:00 | 144h 52m |
| DEBUGMenu | 22 | 0.23 | 1 | 9 | 0 | 2026-09-23T16:31:37.257000+00:00 | 2026-10-07T16:37:53.210000+00:00 | 336h 6m |
| argumentationAnswerEvent | 22 | 0.23 | 1 | 4 | 0 | 2026-09-23T16:56:47.034000+00:00 | 2026-10-07T16:56:36.027000+00:00 | 335h 59m |
| gameWindowUnfocusEvent | 20 | 0.21 | 1 | 8 | 0 | 2026-09-23T16:31:35.291000+00:00 | 2026-10-07T17:07:42.822000+00:00 | 336h 36m |
| gameStartEvent | 16 | 0.17 | 1 | 1 | 0 | 2026-09-23T16:30:12.380000+00:00 | 2026-10-07T16:37:47.429000+00:00 | 336h 7m |
| argumentationEvent | 13 | 0.14 | 1 | 4 | 0 | 2026-09-23T16:56:06.046000+00:00 | 2026-10-07T16:56:36.065000+00:00 | 336h 0m |
| SolarStillDesignEvent | 11 | 0.12 | 1 | 1 | 0 | 2026-10-07T17:03:37.271000+00:00 | 2026-10-07T17:04:00.411000+00:00 | 23.1s |
| TerasGardenBox | 8 | 0.09 | 1 | 1 | 0 | 2026-10-06T16:37:24.548000+00:00 | 2026-10-06T16:38:31.075000+00:00 | 1m 6s |
| chatEvent | 5 | 0.05 | 1 | 3 | 0 | 2026-09-28T16:38:56.118000+00:00 | 2026-10-07T16:47:02.325000+00:00 | 216h 8m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-09-23T17:01:05.728000+00:00 | 2026-10-06T16:49:55.099000+00:00 | 311h 48m |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-23T16:56:00.556000+00:00 | 2026-09-23T16:56:06.016000+00:00 | 5.5s |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 561264.686s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.783s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.524s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 21.451s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 138.638s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 5.46s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 43097.054s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1478.611s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.804s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 24 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Insert; Press E to place 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
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
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.4x vs baseline. 
  - Observed: 22 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,II; A,D,C,2,II; B,2,II; C,2,II; D,2,II; D,3,II; D,4,3,II; D,4,II; D,A,2,II; D,A,3,II; D,A,B,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 484 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [22-48, 22-27, 18-232, 18-287, 18-289] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 24; 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Investigate the Temple; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 13.0x vs baseline. 
  - Observed: 65 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 26 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[255] _id=6ab401a6485cab4c954e760c ts=2026-09-23T16:43:18.8970000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[299] _id=6ab40279485cab4c954e79a0 ts=2026-09-23T16:46:49.4080000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[332] _id=6ab402f4485cab4c954e7b7c ts=2026-09-23T16:48:52.4950000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[12] _id=6ab3fe94485cab4c954e61d0 ts=2026-09-23T16:30:12.3800000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[655] _id=6ab40628485cab4c954e9248 ts=2026-09-23T17:02:32.3370000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[710] _id=6ab54be9485cab4c9552dfbd ts=2026-09-24T16:12:25.2600000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 30 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 30} 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[9] _id=6ab3fe94485cab4c954e61ce ts=2026-09-23T16:30:12.3790000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[16] _id=6ab3fee7485cab4c954e631c ts=2026-09-23T16:31:35.4800000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[30] _id=6ab3ff09485cab4c954e63d8 ts=2026-09-23T16:32:09.4440000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[13] _id=6ab3fee7485cab4c954e631a ts=2026-09-23T16:31:35.2910000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[22] _id=6ab3ff05485cab4c954e63bc ts=2026-09-23T16:32:05.2070000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[673] _id=6ab4067d485cab4c954e93ad ts=2026-09-23T17:03:57.2690000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 7 of 236 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[733] _id=6ab54c0a485cab4c9552e08d ts=2026-09-24T16:12:58.2270000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[722] _id=6ab54c0b485cab4c9552e097 ts=2026-09-24T16:12:59.3380000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[726] _id=6ab54c17485cab4c9552e0c9 ts=2026-09-24T16:13:11.4420000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2607 | 0.001 | 1.783 | 464.807 | 19.792 | 344368.306 | 0.13 | 49 | 8 |
| PuzzlePieceVisibleEvent | 1973 | 0.0 | 0.035 | 569.954 | 1.803 | 519374.243 | 0.11 | 1129 | 5 |
| DialogueEvent | 1713 | 0.0 | 3.928 | 707.372 | 35.579 | 344440.41 | 0.08 | 508 | 7 |
| PlayerPositionEvent | 1657 | 9.93 | 10.001 | 731.091 | 10.8 | 344209.322 | 0.08 | 0 | 9 |
| argumentationNodeEvent | 483 | 0.001 | 0.376 | 2504.507 | 9.369 | 603586.976 | 0.02 | 69 | 4 |
| ObjectInterEvent | 301 | 0.002 | 8.11 | 4023.855 | 372.726 | 347411.098 | 0.01 | 5 | 11 |
| TopographicMapEvent | 235 | 0.02 | 3.268 | 2578.07 | 153.275 | 344380.028 | 0.02 | 2 | 7 |
| questEvent | 74 | 0.0 | 205.623 | 16374.632 | 84682.367 | 345171.954 | 0.0 | 15 | 12 |
| soilMachine | 64 | 0.163 | 1.804 | 5385.075 | 119.272 | 343735.167 | 0.01 | 0 | 1 |
| Soil Key Puzzle | 57 | 0.068 | 1.013 | 10640.257 | 8.307 | 519668.199 | 0.01 | 0 | 2 |
| WaterChamberEvent | 46 | 1.093 | 6.524 | 1866.622 | 54.971 | 85186.37 | 0.03 | 0 | 1 |
| gameWindowFocusEvent | 29 | 1.576 | 191.32 | 41787.945 | 272607.593 | 346221.917 | 0.0 | 0 | 14 |
| DaniEvent | 23 | 1.321 | 3.696 | 22676.085 | 156883.005 | 345309.816 | 0.0 | 0 | 3 |
| DEBUGMenu | 21 | 6.28 | 1009.577 | 57617.903 | 344265.946 | 346338.26 | 0.0 | 0 | 16 |
| argumentationAnswerEvent | 21 | 2.871 | 21.451 | 57599.476 | 433663.933 | 603730.581 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 19 | 1.795 | 1478.611 | 63777.238 | 341162.24 | 344201.707 | 0.0 | 0 | 11 |
| gameStartEvent | 15 | 36.515 | 1939.957 | 80670.337 | 345238.54 | 346221.917 | 0.0 | 0 | 11 |
| argumentationEvent | 12 | 0.046 | 138.638 | 100802.502 | 510087.833 | 603595.347 | 0.0 | 1 | 4 |
| SolarStillDesignEvent | 10 | 0.933 | 1.993 | 2.314 | 4.108 | 4.301 | 25.93 | 0 | 0 |
| TerasGardenBox | 7 | 1.41 | 2.562 | 9.504 | 30.82 | 35.327 | 6.31 | 0 | 0 |
| chatEvent | 4 | 2.041 | 43097.054 | 194521.552 | 600953.289 | 691890.058 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 432270.265 | 561264.686 | 561264.686 | 677359.664 | 690259.106 | 0.0 | 0 | 2 |
| argumentationToolEvent | 1 | 5.46 | 5.46 | 5.46 | 5.46 | 5.46 | 10.99 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 81 group(s), 112 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[838] _id=6ab54d14485cab4c9552e5d9 ts=2026-09-24T16:17:24.6330000Z == 6aa4142c41b41dbac0c7f24c.jsonl[842] _id=6ab54d14485cab4c9552e5dd ts=2026-09-24T16:17:24.6330000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[847] _id=6ab54d16485cab4c9552e5e7 ts=2026-09-24T16:17:24.8420000Z == 6aa4142c41b41dbac0c7f24c.jsonl[827] _id=6ab54d16485cab4c9552e5e9 ts=2026-09-24T16:17:24.8420000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[853] _id=6ab54d17485cab4c9552e60d ts=2026-09-24T16:17:25.6090000Z == 6aa4142c41b41dbac0c7f24c.jsonl[861] _id=6ab54d17485cab4c9552e60f ts=2026-09-24T16:17:25.6090000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f24c.jsonl[216] _id=6ab4012e485cab4c954e73a0 ts=2026-09-23T16:41:18.7100000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[213] _id=6ab4012e485cab4c954e73a4 ts=2026-09-23T16:41:18.7160000Z`; `966ms: 6aa4142c41b41dbac0c7f24c.jsonl[4316] _id=6abd3f20485cab4c958ecba2 ts=2026-09-30T16:55:59.9800000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[4320] _id=6abd3f20485cab4c958ecbac ts=2026-09-30T16:56:00.9460000Z`; `833ms: 6aa4142c41b41dbac0c7f24c.jsonl[6302] _id=6ac3d348de269131f9adf1cf ts=2026-10-05T16:41:44.2460000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[6269] _id=6ac3d349de269131f9adf1ed ts=2026-10-05T16:41:45.0790000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 261 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6aa4142c41b41dbac0c7f24c.jsonl[851] _id=6ab54d17485cab4c9552e5ff ts=2026-09-24T16:17:25.2790000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[834] _id=6ab54d17485cab4c9552e603 ts=2026-09-24T16:17:25.2890000Z`; `218ms: 6aa4142c41b41dbac0c7f24c.jsonl[834] _id=6ab54d17485cab4c9552e603 ts=2026-09-24T16:17:25.2890000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[852] _id=6ab54d17485cab4c9552e607 ts=2026-09-24T16:17:25.5070000Z`; `67ms: 6aa4142c41b41dbac0c7f24c.jsonl[852] _id=6ab54d17485cab4c9552e607 ts=2026-09-24T16:17:25.5070000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[835] _id=6ab54d17485cab4c9552e609 ts=2026-09-24T16:17:25.5740000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa4142c41b41dbac0c7f24c.jsonl[1956] _id=6ab550a1485cab4c955319e7 ts=2026-09-24T16:32:33.8900000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[1961] _id=6ab550a2485cab4c955319ef ts=2026-09-24T16:32:33.9100000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `46ms: 6aa4142c41b41dbac0c7f24c.jsonl[3684] _id=6abd3b66485cab4c958e2f15 ts=2026-09-30T16:40:06.3850000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[3687] _id=6abd3b66485cab4c958e2f31 ts=2026-09-30T16:40:06.4310000Z`; `55ms: 6aa4142c41b41dbac0c7f24c.jsonl[7701] _id=6ac522abde269131f9b51097 ts=2026-10-06T16:32:43.1030000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[7703] _id=6ac522abde269131f9b5109d ts=2026-10-06T16:32:43.1580000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 75 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `908ms: 6aa4142c41b41dbac0c7f24c.jsonl[435] _id=6ab4047b485cab4c954e85a8 ts=2026-09-23T16:55:23.5790000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[437] _id=6ab4047c485cab4c954e85b0 ts=2026-09-23T16:55:24.4870000Z`; `877ms: 6aa4142c41b41dbac0c7f24c.jsonl[440] _id=6ab4047b485cab4c954e85aa ts=2026-09-23T16:55:23.6320000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[445] _id=6ab4047c485cab4c954e85b2 ts=2026-09-23T16:55:24.5090000Z`; `53ms: 6aa4142c41b41dbac0c7f24c.jsonl[386] _id=6ab404b1485cab4c954e8740 ts=2026-09-23T16:56:17.8140000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[399] _id=6ab404b1485cab4c954e8742 ts=2026-09-23T16:56:17.8670000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6aa4142c41b41dbac0c7f24c.jsonl[9220] _id=6ac67a15de269131f9bd658a ts=2026-10-07T16:57:57.3350000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[9221] _id=6ac67a15de269131f9bd658b ts=2026-10-07T16:57:57.3360000Z`; `3ms: 6aa4142c41b41dbac0c7f24c.jsonl[9376] _id=6ac67bdade269131f9bd9231 ts=2026-10-07T17:05:30.4890000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[9377] _id=6ac67bdade269131f9bd9235 ts=2026-10-07T17:05:30.4920000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `835ms: 6aa4142c41b41dbac0c7f24c.jsonl[6301] _id=6ac3d348de269131f9adf1cb ts=2026-10-05T16:41:44.2370000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[6294] _id=6ac3d349de269131f9adf1e5 ts=2026-10-05T16:41:45.0720000Z`; `604ms: 6aa4142c41b41dbac0c7f24c.jsonl[6347] _id=6ac3d386de269131f9adf579 ts=2026-10-05T16:42:46.7680000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[6332] _id=6ac3d387de269131f9adf58d ts=2026-10-05T16:42:47.3720000Z`; `333ms: 6aa4142c41b41dbac0c7f24c.jsonl[6332] _id=6ac3d387de269131f9adf58d ts=2026-10-05T16:42:47.3720000Z ~ 6aa4142c41b41dbac0c7f24c.jsonl[6355] _id=6ac3d387de269131f9adf593 ts=2026-10-05T16:42:47.7050000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 6aa4142c41b41dbac0c7f24c.jsonl[711] _id=6ab54bef485cab4c9552dfcf ts=2026-09-24T16:12:31.8040000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2305] _id=6aba94d2485cab4c956a7b2a ts=2026-09-28T16:24:50.0640000Z; 95h 37m: 6aa4142c41b41dbac0c7f24c.jsonl[5491] _id=6abe9061485cab4c95ac2fb0 ts=2026-10-01T16:54:56.9010000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5949] _id=6ac3d12ade269131f9adc8b9 ts=2026-10-05T16:32:42.8470000Z; 47h 36m: 6aa4142c41b41dbac0c7f24c.jsonl[2768] _id=6aba9a52485cab4c956acef7 ts=2026-09-28T16:48:18.1700000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3205] _id=6abd37c0485cab4c958d8d8e ts=2026-09-30T16:24:32.4090000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 6aa4142c41b41dbac0c7f24c.jsonl[2191] _id=6ab552fe485cab4c95533eb3 ts=2026-09-24T16:42:38.1440000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2576] _id=6aba97dc485cab4c956abd6b ts=2026-09-28T16:37:47.9600000Z; 48h 23m: 6aa4142c41b41dbac0c7f24c.jsonl[2610] _id=6aba9825485cab4c956abf46 ts=2026-09-28T16:39:01.8720000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[4541] _id=6abd40a8485cab4c958eeb9e ts=2026-09-30T17:02:32.4470000Z; 15m 34s: 6aa4142c41b41dbac0c7f24c.jsonl[725] _id=6ab54c17485cab4c9552e0c7 ts=2026-09-24T16:13:11.4380000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[1879] _id=6ab54fbe485cab4c95530cc5 ts=2026-09-24T16:28:46.3130000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 6aa4142c41b41dbac0c7f24c.jsonl[2294] _id=6ab55440485cab4c95534eb0 ts=2026-09-24T16:48:00.1730000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2388] _id=6aba95b8485cab4c956a9209 ts=2026-09-28T16:28:40.5830000Z; 95h 23m: 6aa4142c41b41dbac0c7f24c.jsonl[5924] _id=6abe93a2485cab4c95ac43c8 ts=2026-10-01T17:08:49.9120000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5950] _id=6ac3d130de269131f9adc961 ts=2026-10-05T16:32:48.2620000Z; 47h 21m: 6aa4142c41b41dbac0c7f24c.jsonl[3161] _id=6aba9ded485cab4c956bb005 ts=2026-09-28T17:03:41.1810000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3219] _id=6abd37f0485cab4c958d96de ts=2026-09-30T16:25:20.6880000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 508 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24c.jsonl[9115] _id=6ac67986de269131f9bd57ae ts=2026-10-07T16:55:34.0220000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[9116] _id=6ac67986de269131f9bd57af ts=2026-10-07T16:55:34.0220000Z; 0ms: 6aa4142c41b41dbac0c7f24c.jsonl[9158] _id=6ac679b6de269131f9bd5ba4 ts=2026-10-07T16:56:22.6670000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[9159] _id=6ac679b6de269131f9bd5ba5 ts=2026-10-07T16:56:22.6670000Z; 1ms: 6aa4142c41b41dbac0c7f24c.jsonl[1932] _id=6ab5504d485cab4c955315c3 ts=2026-09-24T16:31:09.7970000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[1933] _id=6ab5504d485cab4c955315c5 ts=2026-09-24T16:31:09.7980000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 44m 
  - Evidence: 191h 44m: 6aa4142c41b41dbac0c7f24c.jsonl[616] _id=6ab405d1485cab4c954e8fff ts=2026-09-23T17:01:05.7280000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[4824] _id=6abe8e24485cab4c95ac19ab ts=2026-10-01T16:45:24.8340000Z; 120h 4m: 6aa4142c41b41dbac0c7f24c.jsonl[4824] _id=6abe8e24485cab4c95ac19ab ts=2026-10-01T16:45:24.8340000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[8055] _id=6ac526b3de269131f9b56445 ts=2026-10-06T16:49:55.0990000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 39m 
  - Evidence: 95h 39m: 6aa4142c41b41dbac0c7f24c.jsonl[2269] _id=6ab553ba485cab4c955349db ts=2026-09-24T16:45:46.7350000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2310] _id=6aba94eb485cab4c956a7ce7 ts=2026-09-28T16:25:15.0410000Z; 95h 24m: 6aa4142c41b41dbac0c7f24c.jsonl[5923] _id=6abe93a0485cab4c95ac43c4 ts=2026-10-01T17:08:48.0560000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5962] _id=6ac3d149de269131f9adcc27 ts=2026-10-05T16:33:13.7140000Z; 47h 20m: 6aa4142c41b41dbac0c7f24c.jsonl[3199] _id=6aba9e1c485cab4c956bc479 ts=2026-09-28T17:04:28.3450000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3210] _id=6abd37da485cab4c958d91f4 ts=2026-09-30T16:24:58.7490000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 49 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24c.jsonl[5966] _id=6ac3d14ede269131f9adccdd ts=2026-10-05T16:33:18.8700000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5967] _id=6ac3d14ede269131f9adcce1 ts=2026-10-05T16:33:18.8710000Z; 2ms: 6aa4142c41b41dbac0c7f24c.jsonl[6603] _id=6ac3d51bde269131f9ae1b2d ts=2026-10-05T16:49:30.9780000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[6604] _id=6ac3d51bde269131f9ae1b2f ts=2026-10-05T16:49:30.9800000Z; 2ms: 6aa4142c41b41dbac0c7f24c.jsonl[6604] _id=6ac3d51bde269131f9ae1b2f ts=2026-10-05T16:49:30.9800000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[6599] _id=6ac3d51bde269131f9ae1b31 ts=2026-10-05T16:49:30.9820000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 30m 
  - Evidence: 96h 30m: 6aa4142c41b41dbac0c7f24c.jsonl[1795] _id=6ab54e91485cab4c9552f783 ts=2026-09-24T16:23:45.3490000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2865] _id=6aba9ba4485cab4c956ade4c ts=2026-09-28T16:53:56.4470000Z; 95h 25m: 6aa4142c41b41dbac0c7f24c.jsonl[5884] _id=6abe937f485cab4c95ac4382 ts=2026-10-01T17:08:15.3160000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5971] _id=6ac3d152de269131f9adcd3d ts=2026-10-05T16:33:22.3800000Z; 47h 25m: 6aa4142c41b41dbac0c7f24c.jsonl[3090] _id=6aba9d8d485cab4c956b8079 ts=2026-09-28T17:02:05.8310000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3257] _id=6abd387f485cab4c958da8bc ts=2026-09-30T16:27:43.0510000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f24c.jsonl[7068] _id=6ac3d816de269131f9ae6887 ts=2026-10-05T17:02:14.5680000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[7073] _id=6ac3d816de269131f9ae688d ts=2026-10-05T17:02:14.5700000Z; 3ms: 6aa4142c41b41dbac0c7f24c.jsonl[7112] _id=6ac3d878de269131f9ae7017 ts=2026-10-05T17:03:52.7240000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[7110] _id=6ac3d879de269131f9ae701d ts=2026-10-05T17:03:52.7270000Z; 3ms: 6aa4142c41b41dbac0c7f24c.jsonl[7413] _id=6ac52137de269131f9b4fc9d ts=2026-10-06T16:26:31.3040000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[7417] _id=6ac52137de269131f9b4fc9f ts=2026-10-06T16:26:31.3070000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 6aa4142c41b41dbac0c7f24c.jsonl[2293] _id=6ab55440485cab4c95534eb3 ts=2026-09-24T16:48:00.7490000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2308] _id=6aba94d8485cab4c956a7b99 ts=2026-09-28T16:24:50.0710000Z; 94h 29m: 6aa4142c41b41dbac0c7f24c.jsonl[5945] _id=6ac3d124de269131f9adc7cf ts=2026-10-01T18:03:36.808Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5952] _id=6ac3d130de269131f9adc95b ts=2026-10-05T16:32:42.8550000Z; 47h 20m: 6aa4142c41b41dbac0c7f24c.jsonl[3200] _id=6aba9e1f485cab4c956bc61c ts=2026-09-28T17:04:31.8620000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3206] _id=6abd37c1485cab4c958d8da6 ts=2026-09-30T16:24:32.4150000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 16m 
  - Evidence: 144h 16m: 6aa4142c41b41dbac0c7f24c.jsonl[1909] _id=6ab55021485cab4c955313b0 ts=2026-09-24T16:30:24.3770000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3872] _id=6abd3cef485cab4c958e978a ts=2026-09-30T16:46:38.6200000Z; 95h 55m: 6aa4142c41b41dbac0c7f24c.jsonl[5475] _id=6abe904b485cab4c95ac2f17 ts=2026-10-01T16:54:32.9560000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[6615] _id=6ac3d525de269131f9ae1bf9 ts=2026-10-05T16:49:40.4050000Z; 24h 3m: 6aa4142c41b41dbac0c7f24c.jsonl[4087] _id=6abd3d52485cab4c958ea10e ts=2026-09-30T16:48:16.7580000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[4872] _id=6abe8fb6485cab4c95ac2511 ts=2026-10-01T16:52:05.9420000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1129 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24c.jsonl[1012] _id=6ab54d80485cab4c9552e9dd ts=2026-09-24T16:18:52.2310000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[1013] _id=6ab54d80485cab4c9552e9df ts=2026-09-24T16:18:52.2310000Z; 0ms: 6aa4142c41b41dbac0c7f24c.jsonl[1016] _id=6ab54d81485cab4c9552e9ef ts=2026-09-24T16:19:01.9530000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[962] _id=6ab54d81485cab4c9552e9f1 ts=2026-09-24T16:19:01.9530000Z; 0ms: 6aa4142c41b41dbac0c7f24c.jsonl[1018] _id=6ab54d83485cab4c9552ea2d ts=2026-09-24T16:19:13.6710000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[1037] _id=6ab54d83485cab4c9552ea2f ts=2026-09-24T16:19:13.6710000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 21m 
  - Evidence: 144h 21m: 6aa4142c41b41dbac0c7f24c.jsonl[1796] _id=6ab54e94485cab4c9552f795 ts=2026-09-24T16:23:48.3330000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3814] _id=6abd3c88485cab4c958e8f52 ts=2026-09-30T16:44:56.5320000Z; 24h 5m: 6aa4142c41b41dbac0c7f24c.jsonl[3847] _id=6abd3cc7485cab4c958e944a ts=2026-09-30T16:45:59.1560000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[4904] _id=6abe8f88485cab4c95ac237b ts=2026-10-01T16:51:20.1450000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 39m 
  - Evidence: 95h 39m: 6aa4142c41b41dbac0c7f24c.jsonl[2266] _id=6ab553ba485cab4c955349d9 ts=2026-09-24T16:45:46.7100000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2314] _id=6aba94f6485cab4c956a7db6 ts=2026-09-28T16:25:26.7380000Z; 47h 25m: 6aa4142c41b41dbac0c7f24c.jsonl[3188] _id=6aba9e0a485cab4c956bbbdf ts=2026-09-28T17:04:10.2740000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3358] _id=6abd390f485cab4c958dbb1f ts=2026-09-30T16:30:07.8180000Z; 23h 22m: 6aa4142c41b41dbac0c7f24c.jsonl[4601] _id=6abd417e485cab4c958ef85c ts=2026-09-30T17:06:06.5600000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[4611] _id=6abe8a1a485cab4c95abf0fd ts=2026-10-01T16:28:10.5410000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.028s shown 
  - Evidence: 20ms: 6aa4142c41b41dbac0c7f24c.jsonl[1956] _id=6ab550a1485cab4c955319e7 ts=2026-09-24T16:32:33.8900000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[1961] _id=6ab550a2485cab4c955319ef ts=2026-09-24T16:32:33.9100000Z; 28ms: 6aa4142c41b41dbac0c7f24c.jsonl[1955] _id=6ab550a1485cab4c955319e5 ts=2026-09-24T16:32:33.8620000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[1956] _id=6ab550a1485cab4c955319e7 ts=2026-09-24T16:32:33.8900000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 39m 
  - Evidence: 23h 39m: 6aa4142c41b41dbac0c7f24c.jsonl[8564] _id=6ac528acde269131f9b5c520 ts=2026-10-06T16:58:19.9920000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[8613] _id=6ac6756ede269131f9bcc24d ts=2026-10-07T16:38:06.3620000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 42m 
  - Evidence: 167h 42m: 6aa4142c41b41dbac0c7f24c.jsonl[546] _id=6ab40513485cab4c954e8ae4 ts=2026-09-23T16:57:55.7610000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3682] _id=6abd3b66485cab4c958e2f0d ts=2026-09-30T16:40:06.3420000Z; 120h 27m: 6aa4142c41b41dbac0c7f24c.jsonl[3682] _id=6abd3b66485cab4c958e2f0d ts=2026-09-30T16:40:06.3420000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[7212] _id=6ac3d966de269131f9ae79e1 ts=2026-10-05T17:07:50.2750000Z; 24h 22m: 6aa4142c41b41dbac0c7f24c.jsonl[7700] _id=6ac522abde269131f9b51095 ts=2026-10-06T16:32:43.0690000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[9093] _id=6ac67966de269131f9bd553f ts=2026-10-07T16:55:02.7010000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 39m 
  - Evidence: 167h 39m: 6aa4142c41b41dbac0c7f24c.jsonl[542] _id=6ab40513485cab4c954e8ae6 ts=2026-09-23T16:57:55.7840000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3596] _id=6abd3adf485cab4c958e0c0a ts=2026-09-30T16:37:51.1310000Z; 120h 26m: 6aa4142c41b41dbac0c7f24c.jsonl[3687] _id=6abd3b66485cab4c958e2f31 ts=2026-09-30T16:40:06.4310000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[7168] _id=6ac3d914de269131f9ae784f ts=2026-10-05T17:06:28.1160000Z; 24h 21m: 6aa4142c41b41dbac0c7f24c.jsonl[7703] _id=6ac522abde269131f9b5109d ts=2026-10-06T16:32:43.1580000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[9063] _id=6ac67936de269131f9bd50a8 ts=2026-10-07T16:54:14.0420000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.046s..0.046s shown 
  - Evidence: 46ms: 6aa4142c41b41dbac0c7f24c.jsonl[3684] _id=6abd3b66485cab4c958e2f15 ts=2026-09-30T16:40:06.3850000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3687] _id=6abd3b66485cab4c958e2f31 ts=2026-09-30T16:40:06.4310000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 39m 
  - Evidence: 167h 39m: 6aa4142c41b41dbac0c7f24c.jsonl[544] _id=6ab40511485cab4c954e8ad6 ts=2026-09-23T16:57:53.1840000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3581] _id=6abd3ad4485cab4c958e08f5 ts=2026-09-30T16:37:40.1600000Z; 120h 26m: 6aa4142c41b41dbac0c7f24c.jsonl[3678] _id=6abd3b63485cab4c958e2e39 ts=2026-09-30T16:40:03.7830000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[7166] _id=6ac3d911de269131f9ae7835 ts=2026-10-05T17:06:25.8210000Z; 24h 21m: 6aa4142c41b41dbac0c7f24c.jsonl[7695] _id=6ac522a9de269131f9b51087 ts=2026-10-06T16:32:41.0910000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[9061] _id=6ac67937de269131f9bd50d2 ts=2026-10-07T16:54:15.9190000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 69 interval(s) ≤ 0.001s..0.011s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24c.jsonl[398] _id=6ab404b1485cab4c954e873e ts=2026-09-23T16:56:17.8130000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[386] _id=6ab404b1485cab4c954e8740 ts=2026-09-23T16:56:17.8140000Z; 8ms: 6aa4142c41b41dbac0c7f24c.jsonl[468] _id=6ab404b5485cab4c954e875a ts=2026-09-23T16:56:21.2170000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[390] _id=6ab404b5485cab4c954e875c ts=2026-09-23T16:56:21.2250000Z; 11ms: 6aa4142c41b41dbac0c7f24c.jsonl[3586] _id=6abd3ad5485cab4c958e096e ts=2026-09-30T16:37:41.6080000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3583] _id=6abd3ad5485cab4c958e097a ts=2026-09-30T16:37:41.6190000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 11m 
  - Evidence: 192h 11m: 6aa4142c41b41dbac0c7f24c.jsonl[2609] _id=6aba9822485cab4c956abf3c ts=2026-09-28T16:38:58.1590000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[8061] _id=6ac526d4de269131f9b567e7 ts=2026-10-06T16:50:28.2170000Z; 23h 47m: 6aa4142c41b41dbac0c7f24c.jsonl[8061] _id=6ac526d4de269131f9b567e7 ts=2026-10-06T16:50:28.2170000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[8605] _id=6ac67561de269131f9bcbf79 ts=2026-10-07T16:37:53.1470000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 10m 
  - Evidence: 96h 10m: 6aa4142c41b41dbac0c7f24c.jsonl[710] _id=6ab54be9485cab4c9552dfbd ts=2026-09-24T16:12:25.2600000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2301] _id=6aba9457485cab4c956a6aa6 ts=2026-09-28T16:22:47.1770000Z; 95h 46m: 6aa4142c41b41dbac0c7f24c.jsonl[4831] _id=6abe8e33485cab4c95ac19df ts=2026-10-01T16:45:39.6440000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5938] _id=6ac3d125de269131f9adc7f2 ts=2026-10-05T16:32:36.7360000Z; 47h 36m: 6aa4142c41b41dbac0c7f24c.jsonl[2766] _id=6aba9a4b485cab4c956aceb1 ts=2026-09-28T16:48:11.1980000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3204] _id=6abd37ac485cab4c958d8c3e ts=2026-09-30T16:24:12.0680000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 96h 10m 
  - Evidence: 96h 10m: 6aa4142c41b41dbac0c7f24c.jsonl[708] _id=6ab54be9485cab4c9552dfbb ts=2026-09-24T16:12:25.2590000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2300] _id=6aba9457485cab4c956a6aa0 ts=2026-09-28T16:22:47.1760000Z; 94h 28m: 6aa4142c41b41dbac0c7f24c.jsonl[5946] _id=6ac3d124de269131f9adc7df ts=2026-10-01T18:03:41.27Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5947] _id=6ac3d125de269131f9adc7e9 ts=2026-10-05T16:32:36.7340000Z; 47h 35m: 6aa4142c41b41dbac0c7f24c.jsonl[2783] _id=6aba9a78485cab4c956ad05e ts=2026-09-28T16:48:56.2810000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3203] _id=6abd37ac485cab4c958d8c38 ts=2026-09-30T16:24:12.0670000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 6aa4142c41b41dbac0c7f24c.jsonl[2297] _id=6ab55447485cab4c95534ecf ts=2026-09-24T16:48:07.2370000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2303] _id=6aba94d1485cab4c956a7b15 ts=2026-09-28T16:24:48.9440000Z; 94h 40m: 6aa4142c41b41dbac0c7f24c.jsonl[5944] _id=6ac3d124de269131f9adc7db ts=2026-10-01T18:03:39.472Z -> 6aa4142c41b41dbac0c7f24c.jsonl[6403] _id=6ac3d3d4de269131f9adfbbd ts=2026-10-05T16:44:03.9930000Z; 48h 17m: 6aa4142c41b41dbac0c7f24c.jsonl[2782] _id=6aba9a66485cab4c956acfda ts=2026-09-28T16:48:37.5750000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[4594] _id=6abd4185485cab4c958ef886 ts=2026-09-30T17:06:13.1820000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa4142c41b41dbac0c7f24c.jsonl[1949] _id=6ab55084485cab4c9553182d ts=2026-09-24T16:32:04.5420000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[2306] _id=6aba94d9485cab4c956a7ba3 ts=2026-09-28T16:24:56.4960000Z; 95h 26m: 6aa4142c41b41dbac0c7f24c.jsonl[5845] _id=6abe9305485cab4c95ac4248 ts=2026-10-01T17:06:13.2570000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[5953] _id=6ac3d130de269131f9adc95d ts=2026-10-05T16:32:48.1280000Z; 47h 23m: 6aa4142c41b41dbac0c7f24c.jsonl[3028] _id=6aba9d50485cab4c956b6227 ts=2026-09-28T17:01:04.7980000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[3208] _id=6abd37c1485cab4c958d8da8 ts=2026-09-30T16:24:33.1500000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24c.jsonl[8508] _id=6ac5284dde269131f9b5ade4 ts=2026-10-06T16:56:45.2830000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[8529] _id=6ac5284ede269131f9b5ae13 ts=2026-10-06T16:56:45.2830000Z; 1ms: 6aa4142c41b41dbac0c7f24c.jsonl[423] _id=6ab4045c485cab4c954e84e2 ts=2026-09-23T16:54:52.4920000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[419] _id=6ab4045c485cab4c954e84e8 ts=2026-09-23T16:54:52.4930000Z; 1ms: 6aa4142c41b41dbac0c7f24c.jsonl[8676] _id=6ac675e2de269131f9bcdd9e ts=2026-10-07T16:40:02.2270000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[8677] _id=6ac675e2de269131f9bcdd9f ts=2026-10-07T16:40:02.2280000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4142c41b41dbac0c7f24c.jsonl[5872] _id=6abe9333485cab4c95ac42b2 ts=2026-10-01T17:06:59.5960000Z -> 6aa4142c41b41dbac0c7f24c.jsonl[6043] _id=6ac3d1eade269131f9add5f3 ts=2026-10-05T16:35:54.7630000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[417] _id=6ab40446485cab4c954e843a ts=2026-09-23T16:54:30.4040000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[551] _id=6ab40525485cab4c954e8bc4 ts=2026-09-23T16:58:13.5050000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[2412] _id=6aba9610485cab4c956a9dec ts=2026-09-28T16:30:08.4310000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 83 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[1081] _id=6ab54d8f485cab4c9552eabf ts=2026-09-24T16:19:26.0500000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[1093] _id=6ab54d8f485cab4c9552eac1 ts=2026-09-24T16:19:26.0630000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[1219] _id=6ab54db5485cab4c9552ec59 ts=2026-09-24T16:20:03.7250000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 147 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[830] _id=6ab54d16485cab4c9552e5f3 ts=2026-09-24T16:17:24.9590000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[864] _id=6ab54d18485cab4c9552e61f ts=2026-09-24T16:17:26.2720000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[865] _id=6ab54d18485cab4c9552e623 ts=2026-09-24T16:17:26.3370000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[3687] _id=6abd3b66485cab4c958e2f31 ts=2026-09-30T16:40:06.4310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[399] _id=6ab404b1485cab4c954e8742 ts=2026-09-23T16:56:17.8670000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[388] _id=6ab404b3485cab4c954e8750 ts=2026-09-23T16:56:19.4800000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[390] _id=6ab404b5485cab4c954e875c ts=2026-09-23T16:56:21.2250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[8061] _id=6ac526d4de269131f9b567e7 ts=2026-10-06T16:50:28.2170000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[8605] _id=6ac67561de269131f9bcbf79 ts=2026-10-07T16:37:53.1470000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[8916] _id=6ac67786de269131f9bd2497 ts=2026-10-07T16:47:02.3250000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[5955] _id=6ac3d13fde269131f9adcae5 ts=2026-10-05T16:33:03.8490000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[8634] _id=6ac675e2de269131f9bcdd88 ts=2026-10-07T16:40:02.2060000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[17] _id=6ab3feee485cab4c954e633a ts=?`; `6aa4142c41b41dbac0c7f24c.jsonl[2307] _id=6aba94d8485cab4c956a7b95 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 216 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[1085] _id=6ab54d8e485cab4c9552eaa3 ts=2026-09-24T16:19:25.5680000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[1090] _id=6ab54d8e485cab4c9552eab3 ts=2026-09-24T16:19:25.9550000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[1137] _id=6ab54d9c485cab4c9552eb47 ts=2026-09-24T16:19:38.6670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 371 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[842] _id=6ab54d14485cab4c9552e5dd ts=2026-09-24T16:17:24.6330000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[839] _id=6ab54d15485cab4c9552e5e1 ts=2026-09-24T16:17:24.7650000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[847] _id=6ab54d16485cab4c9552e5e7 ts=2026-09-24T16:17:24.8420000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 53 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[1956] _id=6ab550a1485cab4c955319e7 ts=2026-09-24T16:32:33.8900000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[1961] _id=6ab550a2485cab4c955319ef ts=2026-09-24T16:32:33.9100000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[1980] _id=6ab550bb485cab4c95531bc1 ts=2026-09-24T16:32:59.8020000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[7473] _id=6ac521cade269131f9b5032d ts=2026-10-06T16:28:58.1200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 338 start, 331 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 77 unmatched 'BecameCameraCentered' (totals: 370 open, 376 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 109 unmatched 'BecameVisible' (totals: 595 open, 633 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 58 open, 56 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 44 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 124 of 9408 adjacent _id pairs reverse in client time; worst 105.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f24c.jsonl[929] _id=6ab54d79485cab4c9552e913 ts=2026-09-24T16:19:04.9450000Z`; `6aa4142c41b41dbac0c7f24c.jsonl[918] _id=6ab54d79485cab4c9552e917 ts=2026-09-24T16:17:19.7330000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -340149.20s, max +0.50s over 9409 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f24c\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 2608 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (551); Unit 4 Dev - Dungeon (546); Unit 2 Prod (Refactor) (466); Unit 4 Dev - Anderson Base (239); Unit 5 Dev - Dungeon (206); Unit 3 Dungeon Dev (200); Unit 4 Dev (183); Unit 1 Dev (149); Unit 5 Dev (68)
- **Intervals:** median 1.78s (p5 0.18s / p95 19.79s, n=2607)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2608/2608 records)
    "pressed"  x2608
data.actionType  (string, 2608/2608 records)
    "Move"  x1816
    "Interact"  x445
    "Jump"  x111
    "Ascend"  x83
    "Hoverboard"  x59
    "Map"  x37
    "Sprint"  x36
    "Pause"  x11
    "SkipCinematic"  x5
    "ToggleDebug"  x4
    "Descend"  x1
data.key  (string, 2608/2608 records, 24 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2608/2608 records)
    "Player"  x2022
    "Drone"  x586
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 1974 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (828); Unit 4 Dev (604); Unit 5 Dev - Dungeon (358); Unit 3 Dungeon Dev (184)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.80s, n=1973)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1974/1974 records)
    "BecameInvisible"  x633
    "BecameVisible"  x595
    "BecameCameraUncentered"  x376
    "BecameCameraCentered"  x370
data.pieceId  (string, 1974/1974 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1974/1974 records)
    1221 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1714 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (312); Unit 2 Prod (Refactor) (274); Unit 4 Dev (255); Unit 1 Dev (198); Unit 5 Dev (190); Unit 4 Dev - Anderson Base (163); Unit 4 Dev - Dungeon (124); Unit 3 Dungeon Dev (115); Unit 5 Dev - Dungeon (83)
- **eventKey:** present on 1045 of 1714 records
- **Intervals:** median 3.93s (p5 0.00s / p95 35.58s, n=1713)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1045; [conversationId, dialogueEventType] x669
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1714/1714 records)
    numeric range 10 .. 118 (49 unique)
data.dialogueEventType  (string, 1714/1714 records)
    "DialogueNodeEvent"  x1045
    "DialogueStartEvent"  x338
    "DialogueFinishEvent"  x331
data.nodeId  (number, 1045/1714 records)
    numeric range 0 .. 289 (206 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1670 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (330); Unit 2 Prod (Refactor) (304); Unit 4 Dev (212); Unit 4 Dev - Dungeon (186); Unit 1 Dev (179); Unit 5 Dev - Dungeon (135); Unit 5 Dev (121); Unit 4 Dev - Anderson Base (118); Unit 3 Dungeon Dev (85)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.80s, n=1657)
- **Fields under `data`:**

```text
data.position  (object, 1670/1670 records)
data.position.x  (number, 1670/1670 records)
    numeric range -831.295 .. 1555.33 (642 unique)
data.position.y  (number, 1670/1670 records)
    numeric range -114.326 .. 221.322 (487 unique)
data.position.z  (number, 1670/1670 records)
    numeric range -1303.26 .. 1990.11 (642 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 484 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (244); Unit 3 Dev (83); Unit 1 Dev (81); Unit 5 Dev (76)
- **Intervals:** median 0.38s (p5 0.03s / p95 9.37s, n=483)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 484/484 records)
    "argumentationNodeHoverEnd"  x225
    "argumentationNodeHoverStart"  x212
    "argumentationNodeAdd"  x33
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 484/484 records)
    "Unit 4 - Flooding"  x244
    "Unit 3 - Pollution Upstream"  x83
    "Unit 5"  x76
    "Unit 1 - Argumentation Tutorial"  x54
    "Unit 1 - Freshwater"  x27
data.nodeName  (string, 484/484 records)
    "A"  x75
    "B"  x63
    "I"  x59
    "C"  x55
    "1"  x49
    "3"  x43
    "II"  x43
    "D"  x42
    "2"  x26
    "4"  x22
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 302 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (156); Unit 3 Dungeon Dev (31); Unit 2 Prod (Refactor) (27); Unit 4 Dev - Anderson Base (18); Unit 1 Dev (17); Unit 3 Dev (16); Unit 4 Dev (15); Unit 5 Dev (11); Unit 5 Dev - Dungeon (11)
- **Intervals:** median 8.11s (p5 0.96s / p95 372.73s, n=301)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 302/302 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 302/302 records)
    92 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 236 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (153); Unit 3 Dev (83)
- **Intervals:** median 3.27s (p5 0.78s / p95 153.27s, n=235)
- **`data` key-set variants:** [actionType, featureUsed, location] x115; [actionType, featureUsed] x114; [actionType, featureUsed, legendName] x7
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 236/236 records)
    "WaypointMoveEvent"  x105
    "MapOpenEvent"  x58
    "MapCloseEvent"  x56
    "WaypointSetEvent"  x8
    "Selected"  x4
    "Unselected"  x3
    "WaypointResetEvent"  x2
data.featureUsed  (string, 236/236 records)
    "Waypoint"  x115
    "Map"  x114
    "Legend"  x7
data.legendName  (string, 7/236 records)
    "0 ft"  x4
    "90 ft"  x3
data.location  (object, 115/236 records)
data.location.x  (number, 115/236 records)
    numeric range -325.09 .. 562.91 (93 unique)
data.location.y  (number, 115/236 records)
    numeric range -363.5 .. 281.5 (98 unique)
data.location.z  (number, 115/236 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 75 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (13); Unit 4 Dev - Dungeon (13); Unit 1 Dev (12); Unit 5 Dev - Dungeon (9); Unit 2 Prod (Refactor) (8); Unit 4 Dev (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 75 of 75 records
- **Intervals:** median 205.62s (p5 0.00s / p95 84682.37s, n=74)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 75/75 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x31
data.questID  (string, 75/75 records)
    31 unique values (see csv/event_unique_values.csv)
data.questName  (string, 75/75 records)
    31 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/75 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 65 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (65)
- **Intervals:** median 1.80s (p5 0.27s / p95 119.27s, n=64)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 65/65 records)
    "ChangeCanister"  x65
data.canisterType  (string, 65/65 records)
    "Clay"  x29
    "Sand"  x13
    "Gravel"  x12
    "Bedrock"  x11
data.floor  (string, 65/65 records)
    "5"  x42
    "3"  x20
    "4"  x3
data.machine  (string, 65/65 records)
    "1"  x59
    "2"  x6
data.row  (string, 65/65 records)
    "TopRow"  x44
    "BottomRow"  x21
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (30); Unit 3 Dev (26); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.01s (p5 0.28s / p95 8.31s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/58 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/58 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/58 records)
    "RightDrag"  x27
    "LeftDrag"  x25
data.currentSoilType  (string, 52/58 records)
    "CLAYSAND"  x14
    "CLAY"  x11
    "SAND"  x11
    "CLAYROCK"  x8
    "SANDGRAVEL"  x4
    "BEDROCK"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 52/58 records)
    "false"  x38
    "true"  x14
data.waterLevelStatus  (string, 52/58 records)
    "Proper"  x23
    "TooLow"  x17
    "TooHigh"  x12
data.waterRetentionChange  (string, 52/58 records)
    "Decrease"  x22
    "Increase"  x16
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 47 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (47)
- **Intervals:** median 6.52s (p5 1.18s / p95 54.97s, n=46)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "On"  x29
    "Off"  x18
data.floor  (string, 47/47 records)
    "3"  x21
    "4"  x18
    "2"  x6
    "1"  x2
data.machineNumber  (string, 47/47 records)
    "One"  x42
    "Two"  x5
data.machineType  (string, 47/47 records)
    "Condenser"  x24
    "Evaporator"  x12
    "DualChamber_Condenser"  x5
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x2
data.room  (string, 47/47 records)
    "2"  x22
    "3"  x12
    "4"  x8
    "1"  x5
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 30 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 4 Dev - Dungeon (4); Transition (2); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 191.32s (p5 2.96s / p95 272607.59s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 30/30 records)
    true  x30
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 24 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (4)
- **Intervals:** median 3.70s (p5 1.74s / p95 156883.00s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "Close"  x12
    "Open"  x12
data.toolName  (string, 24/24 records, 24 empty-string)
    ""  x24
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `DEBUGMenu` — 22 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 4 Dev (3); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); MainMenu (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1009.58s (p5 55.75s / p95 344265.95s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "DebugMenuStateChanged"  x22
data.isOpened  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 22 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (14); Unit 5 Dev (5); Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 21.45s (p5 3.51s / p95 433663.93s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "submitAnswerEvent"  x22
data.answerSubmitted  (string, 22/22 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 22/22 records)
    "Unit 4 - Flooding"  x14
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 20 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (4); Unit 3 Dev (3); Unit 5 Dev - Dungeon (3); Transition (2); Unit 5 Dev (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1478.61s (p5 3.05s / p95 341162.24s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    false  x20
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 1939.96s (p5 51.79s / p95 345238.54s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 138.64s (p5 0.05s / p95 510087.83s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 1.99s (p5 0.97s / p95 4.11s, n=10)
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
    "GlassRoofTemperature"  x5
    "RoofStyle"  x4
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 10/11 records, 1 empty-string)
    "Cold"  x3
    "Hot"  x2
    "Tilted In"  x2
    ""  x1
    "Covered"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 2.56s (p5 1.56s / p95 30.82s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x3
data.boxId  (string, 8/8 records)
    "0"  x4
    "1"  x2
    "2"  x2
data.soilType  (string, 8/8 records)
    "Clay"  x3
    "Sand"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 43097.05s (p5 84.11s / p95 600953.29s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x4
    "Open"  x1
data.chatID  (string, 5/5 records)
    "NA"  x4
    "[22-48, 22-27, 18-232, 18-287, 18-289]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 561264.69s (p5 445169.71s / p95 677359.66s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 5.46s (p5 5.46s / p95 5.46s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Permissions check failed"  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records)
    "TypeError: Permissions check failed"  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit1"  x1
    "unit2"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "Unselected" (3x); "WaypointMoveEvent" (105x); "WaypointResetEvent" (2x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Legend" (7x); "Waypoint" (115x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (11x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*