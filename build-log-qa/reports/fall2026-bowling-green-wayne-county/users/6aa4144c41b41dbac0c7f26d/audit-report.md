# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26d
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f26d.jsonl
- **Records:** 15763 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f26d
- **Time span:** 2026-09-23T18:15:36.122000+00:00 .. 2026-10-06T20:03:52.576000+00:00 (313h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 15763 records, 11 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 115 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4991 | 31.66 | 1 | 4 | 0 | 2026-09-28T18:15:07.566000+00:00 | 2026-10-06T15:44:12.929000+00:00 | 189h 29m |
| InputEvent | 4433 | 28.12 | 1 | 9 | 0 | 2026-09-23T18:15:49.905000+00:00 | 2026-10-06T20:03:52.576000+00:00 | 313h 48m |
| DialogueEvent | 2496 | 15.83 | 1 | 9 | 1569 | 2026-09-23T18:16:31.412000+00:00 | 2026-10-06T20:03:36.344000+00:00 | 313h 47m |
| PlayerPositionEvent | 2234 | 14.17 | 1 | 9 | 0 | 2026-09-23T18:15:44.980000+00:00 | 2026-10-06T20:03:44.951000+00:00 | 313h 47m |
| argumentationNodeEvent | 615 | 3.9 | 1 | 4 | 0 | 2026-09-25T18:36:25.913000+00:00 | 2026-10-06T16:07:49.928000+00:00 | 261h 31m |
| ObjectInterEvent | 311 | 1.97 | 1 | 9 | 0 | 2026-09-23T18:21:06.921000+00:00 | 2026-10-06T20:03:52.575000+00:00 | 313h 42m |
| questEvent | 108 | 0.69 | 1 | 9 | 108 | 2026-09-23T18:16:31.398000+00:00 | 2026-10-06T19:57:48.959000+00:00 | 313h 41m |
| TopographicMapEvent | 91 | 0.58 | 1 | 4 | 0 | 2026-09-23T18:15:49.914000+00:00 | 2026-10-01T16:10:33.994000+00:00 | 189h 54m |
| gameWindowFocusEvent | 80 | 0.51 | 1 | 10 | 0 | 2026-09-23T18:15:36.122000+00:00 | 2026-10-06T19:50:36.475000+00:00 | 313h 35m |
| WaterChamberEvent | 62 | 0.39 | 1 | 1 | 0 | 2026-10-06T15:43:15.148000+00:00 | 2026-10-06T15:58:09.249000+00:00 | 14m 54s |
| gameWindowUnfocusEvent | 59 | 0.37 | 1 | 9 | 0 | 2026-09-23T18:18:20.447000+00:00 | 2026-10-06T16:17:01.363000+00:00 | 309h 58m |
| Soil Key Puzzle | 58 | 0.37 | 1 | 3 | 0 | 2026-09-28T18:21:39.887000+00:00 | 2026-10-01T15:57:16.189000+00:00 | 69h 35m |
| DEBUGMenu | 35 | 0.22 | 1 | 9 | 0 | 2026-09-23T18:15:44.973000+00:00 | 2026-10-06T19:50:35.868000+00:00 | 313h 34m |
| argumentationAnswerEvent | 34 | 0.22 | 1 | 4 | 0 | 2026-09-25T18:39:35.841000+00:00 | 2026-10-06T16:07:51.207000+00:00 | 261h 28m |
| gameStartEvent | 29 | 0.18 | 1 | 1 | 0 | 2026-09-23T18:15:36.123000+00:00 | 2026-10-06T19:50:36.475000+00:00 | 313h 35m |
| DaniEvent | 26 | 0.16 | 1 | 3 | 0 | 2026-09-23T18:16:12.479000+00:00 | 2026-10-01T15:49:46.719000+00:00 | 189h 33m |
| soilMachine | 25 | 0.16 | 1 | 1 | 0 | 2026-10-05T15:49:15.981000+00:00 | 2026-10-05T15:57:31.279000+00:00 | 8m 15s |
| argumentationEvent | 17 | 0.11 | 1 | 4 | 0 | 2026-09-25T18:37:20.077000+00:00 | 2026-10-06T16:07:51.230000+00:00 | 261h 30m |
| SolarStillDesignEvent | 16 | 0.1 | 1 | 1 | 0 | 2026-10-06T16:11:39.061000+00:00 | 2026-10-06T19:55:32.975000+00:00 | 3h 43m |
| TerasGardenBox | 11 | 0.07 | 1 | 1 | 0 | 2026-10-05T18:23:38.766000+00:00 | 2026-10-05T18:24:34.241000+00:00 | 55.5s |
| argumentationToolEvent | 11 | 0.07 | 1 | 2 | 0 | 2026-09-25T18:40:05.636000+00:00 | 2026-09-30T16:06:20.298000+00:00 | 117h 26m |
| crash | 11 | 0.07 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 6 | 0.04 | 1 | 3 | 0 | 2026-09-23T18:16:15.683000+00:00 | 2026-10-06T19:50:48.122000+00:00 | 313h 34m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-28T18:10:25.421000+00:00 | 2026-10-06T20:03:52.525000+00:00 | 193h 53m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 250776.848s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.451s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 24.752s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.997s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 13904.595s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 5338.704s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 229.938s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 315.494s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.813s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 26 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E To Place Cameras; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 16 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.boxId` — baseline categorical value(s) not seen this build. 
  - Observed: 0; 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 62 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.8x vs baseline. 
  - Observed: 34 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; A,4,I; B,1,I; B,1,II; B,4,II; B,A,4,II; C,3,I; C,3,II; C,D,3,II; D,3,I; D,3,II; D,4,II; D,C,1,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.4x vs baseline. 
  - Observed: 615 records 
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
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 11 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 29 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Desert Delicacies 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.0x vs baseline. 
  - Observed: 25 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 322 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[246] _id=6ab41952485cab4c954f4634 ts=2026-09-23T18:24:18.5720000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[316] _id=6ab41aa6485cab4c954f50dc ts=2026-09-23T18:29:58.6390000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[456] _id=6ab41dea485cab4c954f6bb1 ts=2026-09-23T18:43:54.2590000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 12 mismatch(es); e.g. 'questActiveEvent:29' vs expected 'questActiveEvent:31' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[691] _id=6abaac14485cab4c956f67ab ts=2026-09-25T18:16:01.067Z`; `6aa4144c41b41dbac0c7f26d.jsonl[802] _id=6abaac2a485cab4c956f68c3 ts=2026-09-25T18:20:32.985Z`; `6aa4144c41b41dbac0c7f26d.jsonl[712] _id=6abaac2e485cab4c956f6921 ts=2026-09-25T18:22:15.179Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 29 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 29} 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[45] _id=6ab41747485cab4c954f3690 ts=2026-09-23T18:15:36.1230000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[321] _id=6ab41c9a485cab4c954f6079 ts=2026-09-23T18:38:18.3270000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[486] _id=6ab56168485cab4c955385f9 ts=2026-09-24T17:44:07.5050000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 80 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 80} 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[44] _id=6ab41747485cab4c954f368e ts=2026-09-23T18:15:36.1220000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[91] _id=6ab417ec485cab4c954f39e0 ts=2026-09-23T18:18:20.5800000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[268] _id=6ab419cb485cab4c954f4ab4 ts=2026-09-23T18:26:19.9920000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 59 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 59} 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[96] _id=6ab417ec485cab4c954f39de ts=2026-09-23T18:18:20.4470000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[263] _id=6ab419a6485cab4c954f495a ts=2026-09-23T18:25:42.0780000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[319] _id=6ab41ab1485cab4c954f5118 ts=2026-09-23T18:30:09.8570000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 4 of 91 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[52] _id=6ab41756485cab4c954f36d2 ts=2026-09-23T18:15:49.9140000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[48] _id=6ab41759485cab4c954f36fa ts=2026-09-23T18:15:54.1350000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[56] _id=6ab4175b485cab4c954f3700 ts=2026-09-23T18:15:56.3060000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4990 | 0.0 | 0.027 | 136.702 | 1.11 | 345452.878 | 0.44 | 3116 | 10 |
| InputEvent | 4432 | 0.0 | 0.75 | 254.892 | 13.671 | 329881.24 | 0.24 | 257 | 17 |
| DialogueEvent | 2495 | 0.001 | 4.401 | 452.755 | 36.269 | 329881.845 | 0.13 | 727 | 16 |
| PlayerPositionEvent | 2220 | 9.186 | 9.999 | 353.732 | 10.317 | 256901.026 | 0.17 | 0 | 14 |
| argumentationNodeEvent | 614 | 0.015 | 0.361 | 1533.362 | 9.658 | 432280.785 | 0.04 | 137 | 5 |
| ObjectInterEvent | 310 | 0.001 | 10.756 | 3643.115 | 866.365 | 343476.322 | 0.02 | 10 | 21 |
| questEvent | 107 | 0.001 | 192.599 | 10553.996 | 72562.736 | 343795.389 | 0.01 | 22 | 21 |
| TopographicMapEvent | 90 | 0.008 | 2.985 | 7596.49 | 10302.547 | 431953.193 | 0.01 | 3 | 10 |
| gameWindowFocusEvent | 79 | 1.465 | 229.938 | 14289.878 | 76109.329 | 329939.157 | 0.0 | 0 | 28 |
| WaterChamberEvent | 61 | 0.214 | 4.451 | 14.657 | 62.538 | 118.78 | 4.09 | 0 | 0 |
| gameWindowUnfocusEvent | 58 | 1.692 | 315.494 | 19240.016 | 84670.667 | 344241.683 | 0.0 | 0 | 22 |
| Soil Key Puzzle | 57 | 0.178 | 0.809 | 4395.374 | 251.293 | 163758.684 | 0.01 | 0 | 3 |
| DEBUGMenu | 34 | 73.863 | 1262.57 | 33202.673 | 147021.04 | 330211.473 | 0.0 | 0 | 23 |
| argumentationAnswerEvent | 33 | 0.509 | 24.752 | 28524.102 | 202110.686 | 432308.228 | 0.0 | 0 | 5 |
| gameStartEvent | 28 | 66.811 | 5338.704 | 40317.87 | 198349.318 | 330270.978 | 0.0 | 0 | 19 |
| DaniEvent | 25 | 0.004 | 2.431 | 27296.57 | 73573.304 | 519957.732 | 0.0 | 2 | 5 |
| soilMachine | 24 | 0.293 | 1.813 | 20.637 | 92.952 | 235.3 | 2.91 | 0 | 0 |
| argumentationEvent | 16 | 0.037 | 76.993 | 58839.447 | 300910.528 | 432277.24 | 0.0 | 1 | 5 |
| SolarStillDesignEvent | 15 | 0.516 | 1.349 | 895.594 | 4026.009 | 13403.333 | 0.07 | 0 | 1 |
| TerasGardenBox | 10 | 1.119 | 2.933 | 5.548 | 15.126 | 17.785 | 10.82 | 0 | 0 |
| argumentationToolEvent | 10 | 0.528 | 3.997 | 42277.466 | 215910.197 | 257156.579 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 5 | 2.211 | 13904.595 | 225774.488 | 845633.26 | 1038124.563 | 0.0 | 0 | 4 |
| EndOfUnit | 3 | 91557.075 | 250776.848 | 232669.035 | 345183.548 | 355673.181 | 0.0 | 0 | 3 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[5804] _id=6abc07fa485cab4c9584c947 ts=2026-09-29T18:48:26.2420000Z == 6aa4144c41b41dbac0c7f26d.jsonl[5799] _id=6abc07fa485cab4c9584c949 ts=2026-09-29T18:48:26.2420000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[6177] _id=6abd2e9f485cab4c958cf05c ts=2026-09-30T15:45:37.1540000Z == 6aa4144c41b41dbac0c7f26d.jsonl[6179] _id=6abd2e9f485cab4c958cf064 ts=2026-09-30T15:45:37.1540000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[12294] _id=6ac3e6e0de269131f9aeb1b9 ts=2026-10-05T18:05:19.8090000Z == 6aa4144c41b41dbac0c7f26d.jsonl[12300] _id=6ac3e6e0de269131f9aeb1bb ts=2026-10-05T18:05:19.8090000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 222 group(s), 297 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1560] _id=6abaaeb7485cab4c956fac87 ts=2026-09-28T18:15:19.0820000Z == 6aa4144c41b41dbac0c7f26d.jsonl[1577] _id=6abaaeb8485cab4c956fac89 ts=2026-09-28T18:15:19.0820000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1578] _id=6abaaeb8485cab4c956fac8b ts=2026-09-28T18:15:19.0980000Z == 6aa4144c41b41dbac0c7f26d.jsonl[1563] _id=6abaaeb8485cab4c956fac90 ts=2026-09-28T18:15:19.0980000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1570] _id=6abaaeb8485cab4c956fac93 ts=2026-09-28T18:15:19.1630000Z == 6aa4144c41b41dbac0c7f26d.jsonl[1571] _id=6abaaeb8485cab4c956fac95 ts=2026-09-28T18:15:19.1630000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[5812] _id=6abcfdc5485cab4c95864f1d ts=? == 6aa4144c41b41dbac0c7f26d.jsonl[5923] _id=6abd0042485cab4c958651d7 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 38 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4144c41b41dbac0c7f26d.jsonl[155] _id=6ab41892485cab4c954f3e70 ts=2026-09-23T18:21:06.9210000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[152] _id=6ab41892485cab4c954f3e72 ts=2026-09-23T18:21:06.9290000Z`; `552ms: 6aa4144c41b41dbac0c7f26d.jsonl[200] _id=6ab41920485cab4c954f440e ts=2026-09-23T18:23:28.7460000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[206] _id=6ab41921485cab4c954f441c ts=2026-09-23T18:23:29.2980000Z`; `250ms: 6aa4144c41b41dbac0c7f26d.jsonl[206] _id=6ab41921485cab4c954f441c ts=2026-09-23T18:23:29.2980000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[201] _id=6ab41921485cab4c954f4422 ts=2026-09-23T18:23:29.5480000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 464 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `77ms: 6aa4144c41b41dbac0c7f26d.jsonl[1686] _id=6abaaf0a485cab4c956fb619 ts=2026-09-28T18:16:42.2540000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1688] _id=6abaaf0a485cab4c956fb61d ts=2026-09-28T18:16:42.3310000Z`; `29ms: 6aa4144c41b41dbac0c7f26d.jsonl[1802] _id=6abaaf2b485cab4c956fbb3b ts=2026-09-28T18:17:14.7140000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1813] _id=6abaaf2b485cab4c956fbb3d ts=2026-09-28T18:17:14.7430000Z`; `9ms: 6aa4144c41b41dbac0c7f26d.jsonl[1870] _id=6abaaf37485cab4c956fbd0f ts=2026-09-28T18:17:24.7160000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1821] _id=6abaaf37485cab4c956fbd13 ts=2026-09-28T18:17:24.7250000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `582ms: 6aa4144c41b41dbac0c7f26d.jsonl[9547] _id=6abe82d0485cab4c95ab9dd2 ts=2026-10-01T15:57:04.7160000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[9553] _id=6abe82d1485cab4c95ab9dde ts=2026-10-01T15:57:05.2980000Z`; `995ms: 6aa4144c41b41dbac0c7f26d.jsonl[9548] _id=6abe82d0485cab4c95ab9dd6 ts=2026-10-01T15:57:04.9450000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[9549] _id=6abe82d1485cab4c95ab9dea ts=2026-10-01T15:57:05.9400000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 6aa4144c41b41dbac0c7f26d.jsonl[3012] _id=6abab1cd485cab4c95700473 ts=2026-09-28T18:28:29.1530000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[3003] _id=6abab1cd485cab4c9570047d ts=2026-09-28T18:28:29.1650000Z`; `800ms: 6aa4144c41b41dbac0c7f26d.jsonl[5791] _id=6abc07f8485cab4c9584c918 ts=2026-09-29T18:48:24.7370000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[5794] _id=6abc07f9485cab4c9584c92f ts=2026-09-29T18:48:25.5370000Z`; `483ms: 6aa4144c41b41dbac0c7f26d.jsonl[6066] _id=6abd2dcb485cab4c958cd8ad ts=2026-09-30T15:42:06.6890000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[6074] _id=6abd2dcc485cab4c958cd8c4 ts=2026-09-30T15:42:07.1720000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `843ms: 6aa4144c41b41dbac0c7f26d.jsonl[14679] _id=6ac51900de269131f9b4c4cb ts=2026-10-06T15:51:28.0530000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[14688] _id=6ac51901de269131f9b4c4d9 ts=2026-10-06T15:51:28.8960000Z`; `523ms: 6aa4144c41b41dbac0c7f26d.jsonl[14685] _id=6ac51900de269131f9b4c4d1 ts=2026-10-06T15:51:28.6120000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[14697] _id=6ac51901de269131f9b4c4df ts=2026-10-06T15:51:29.1350000Z`; `453ms: 6aa4144c41b41dbac0c7f26d.jsonl[14688] _id=6ac51901de269131f9b4c4d9 ts=2026-10-06T15:51:28.8960000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[14698] _id=6ac51901de269131f9b4c4e3 ts=2026-10-06T15:51:29.3490000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `509ms: 6aa4144c41b41dbac0c7f26d.jsonl[1108] _id=6abaac46485cab4c956f6b71 ts=2026-09-25T18:39:35.841Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1113] _id=6abaac46485cab4c956f6b73 ts=2026-09-25T18:39:36.35Z`; `528ms: 6aa4144c41b41dbac0c7f26d.jsonl[12176] _id=6ac3ccb7de269131f9ad9ea1 ts=2026-10-05T16:13:43.0760000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[12185] _id=6ac3ccb7de269131f9ad9eb1 ts=2026-10-05T16:13:43.6040000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6aa4144c41b41dbac0c7f26d.jsonl[7339] _id=6abd33f6485cab4c958d4a7a ts=2026-09-30T16:08:22.2940000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[7342] _id=6abd33f6485cab4c958d4a82 ts=2026-09-30T16:08:22.3310000Z`; `72ms: 6aa4144c41b41dbac0c7f26d.jsonl[12796] _id=6ac3eeb3de269131f9af34d9 ts=2026-10-05T18:18:22.389Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[12793] _id=6ac3eeb3de269131f9af34e5 ts=2026-10-05T18:18:22.461Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 219 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `52ms: 6aa4144c41b41dbac0c7f26d.jsonl[1067] _id=6abaac43485cab4c956f6aff ts=2026-09-25T18:36:25.913Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1054] _id=6abaac43485cab4c956f6b01 ts=2026-09-25T18:36:25.965Z`; `289ms: 6aa4144c41b41dbac0c7f26d.jsonl[1054] _id=6abaac43485cab4c956f6b01 ts=2026-09-25T18:36:25.965Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1068] _id=6abaac43485cab4c956f6b03 ts=2026-09-25T18:36:26.254Z`; `44ms: 6aa4144c41b41dbac0c7f26d.jsonl[1068] _id=6abaac43485cab4c956f6b03 ts=2026-09-25T18:36:26.254Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1069] _id=6abaac43485cab4c956f6b05 ts=2026-09-25T18:36:26.298Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `967ms: 6aa4144c41b41dbac0c7f26d.jsonl[1329] _id=6abaace9485cab4c956f74e1 ts=2026-09-28T18:07:38.0010000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[1330] _id=6abaacea485cab4c956f74ed ts=2026-09-28T18:07:38.9680000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f26d.jsonl[3522] _id=6abbff6f485cab4c9584216b ts=2026-09-29T18:11:59.8490000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[3530] _id=6abbff6f485cab4c9584216d ts=2026-09-29T18:11:59.8530000Z`; `1ms: 6aa4144c41b41dbac0c7f26d.jsonl[15226] _id=6ac51d1dde269131f9b4e237 ts=2026-10-06T16:09:01.3170000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[15270] _id=6ac51d1dde269131f9b4e239 ts=2026-10-06T16:09:01.3180000Z`; `3ms: 6aa4144c41b41dbac0c7f26d.jsonl[15401] _id=6ac51e1bde269131f9b4ead7 ts=2026-10-06T16:13:15.3210000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[15396] _id=6ac51e1bde269131f9b4eadb ts=2026-10-06T16:13:15.3240000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `910ms: 6aa4144c41b41dbac0c7f26d.jsonl[11224] _id=6ac3c6fcde269131f9ad79d9 ts=2026-10-05T15:49:15.9810000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[11226] _id=6ac3c6fdde269131f9ad79e5 ts=2026-10-05T15:49:16.8910000Z`; `305ms: 6aa4144c41b41dbac0c7f26d.jsonl[11226] _id=6ac3c6fdde269131f9ad79e5 ts=2026-10-05T15:49:16.8910000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[11235] _id=6ac3c6fdde269131f9ad79ed ts=2026-10-05T15:49:17.1960000Z`; `293ms: 6aa4144c41b41dbac0c7f26d.jsonl[11235] _id=6ac3c6fdde269131f9ad79ed ts=2026-10-05T15:49:17.1960000Z ~ 6aa4144c41b41dbac0c7f26d.jsonl[11219] _id=6ac3c6fdde269131f9ad79f3 ts=2026-10-05T15:49:17.4890000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 91h 43m 
  - Evidence: 91h 43m: 6aa4144c41b41dbac0c7f26d.jsonl[10671] _id=6abe85ef485cab4c95abc4c8 ts=2026-10-01T16:10:26.1120000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10881] _id=6ac38fc9de269131f9a83c60 ts=2026-10-05T11:53:57.5850000Z; 71h 43m: 6aa4144c41b41dbac0c7f26d.jsonl[808] _id=6abaac2a485cab4c956f68bd ts=2026-09-25T18:20:32.259Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1214] _id=6abaac4e485cab4c956f6c4f ts=2026-09-28T18:04:13.7240000Z; 24h 12m: 6aa4144c41b41dbac0c7f26d.jsonl[552] _id=6ab565f8485cab4c9553f8f2 ts=2026-09-24T18:03:36.2590000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[741] _id=6abaac14485cab4c956f6799 ts=2026-09-25T18:16:00.147Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 25m 
  - Evidence: 144h 25m: 6aa4144c41b41dbac0c7f26d.jsonl[63] _id=6ab41774485cab4c954f37a2 ts=2026-09-23T18:16:20.3320000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[5492] _id=6abc068a485cab4c9584b09d ts=2026-09-29T18:42:18.0640000Z; 21h 0m: 6aa4144c41b41dbac0c7f26d.jsonl[5491] _id=6abc068d485cab4c9584b0d7 ts=2026-09-29T18:42:21.0300000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[6086] _id=6abd2de1485cab4c958cdb0e ts=2026-09-30T15:42:29.1100000Z; 18h 10m: 6aa4144c41b41dbac0c7f26d.jsonl[8881] _id=6abd5668485cab4c9591bf3b ts=2026-09-30T18:35:20.6190000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[9014] _id=6abe55ff485cab4c95a3e069 ts=2026-10-01T12:45:54.8200000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6aa4144c41b41dbac0c7f26d.jsonl[8878] _id=6abd5665485cab4c9591bed3 ts=2026-09-30T18:35:17.9170000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[8879] _id=6abd5666485cab4c9591bed5 ts=2026-09-30T18:35:17.9210000Z; 5ms: 6aa4144c41b41dbac0c7f26d.jsonl[8880] _id=6abd5667485cab4c9591bf0b ts=2026-09-30T18:35:19.3350000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[8874] _id=6abd5667485cab4c9591bf0f ts=2026-09-30T18:35:19.3400000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 91h 38m 
  - Evidence: 91h 38m: 6aa4144c41b41dbac0c7f26d.jsonl[10870] _id=6abe8743485cab4c95abd064 ts=2026-10-01T16:16:03.4960000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10885] _id=6ac38fd1de269131f9a83c6e ts=2026-10-05T11:54:05.3410000Z; 71h 22m: 6aa4144c41b41dbac0c7f26d.jsonl[1207] _id=6abaac4d485cab4c956f6c39 ts=2026-09-25T18:42:10.404Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1196] _id=6abaac4f485cab4c956f6c81 ts=2026-09-28T18:04:41.4640000Z; 24h 4m: 6aa4144c41b41dbac0c7f26d.jsonl[685] _id=6ab567d7485cab4c955420ba ts=2026-09-24T18:11:35.0270000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[718] _id=6abaac15485cab4c956f67b3 ts=2026-09-25T18:16:06.478Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 727 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[12153] _id=6ac3cccbde269131f9ad9f39 ts=2026-10-05T16:14:03.8740000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12154] _id=6ac3ccccde269131f9ad9f3b ts=2026-10-05T16:14:03.8750000Z; 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[12177] _id=6ac3ccb7de269131f9ad9ea4 ts=2026-10-05T16:13:43.0880000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12178] _id=6ac3ccb7de269131f9ad9ea7 ts=2026-10-05T16:13:43.0890000Z; 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[1292] _id=6abaad13485cab4c956f7767 ts=2026-09-28T18:08:19.2510000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1293] _id=6abaad13485cab4c956f7769 ts=2026-09-28T18:08:19.2520000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 98h 47m 
  - Evidence: 98h 47m: 6aa4144c41b41dbac0c7f26d.jsonl[9271] _id=6abe812a485cab4c95ab7da4 ts=2026-10-01T15:50:02.2690000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[13186] _id=6ac3eed4de269131f9af3baf ts=2026-10-05T18:37:55.45Z; 69h 39m: 6aa4144c41b41dbac0c7f26d.jsonl[1442] _id=6abaad91485cab4c956f8949 ts=2026-09-28T18:10:25.4210000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[9271] _id=6abe812a485cab4c95ab7da4 ts=2026-10-01T15:50:02.2690000Z; 25h 25m: 6aa4144c41b41dbac0c7f26d.jsonl[13186] _id=6ac3eed4de269131f9af3baf ts=2026-10-05T18:37:55.45Z -> 6aa4144c41b41dbac0c7f26d.jsonl[15760] _id=6ac55429de269131f9b81cb4 ts=2026-10-06T20:03:52.5250000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 91h 38m 
  - Evidence: 91h 38m: 6aa4144c41b41dbac0c7f26d.jsonl[10825] _id=6abe8742485cab4c95abd056 ts=2026-10-01T16:16:02.7660000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10883] _id=6ac38fd0de269131f9a83c66 ts=2026-10-05T11:54:04.0060000Z; 71h 22m: 6aa4144c41b41dbac0c7f26d.jsonl[1211] _id=6abaac4d485cab4c956f6c41 ts=2026-09-25T18:42:16.336Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1190] _id=6abaac4e485cab4c956f6c53 ts=2026-09-28T18:04:19.3600000Z; 24h 9m: 6aa4144c41b41dbac0c7f26d.jsonl[628] _id=6ab5669e485cab4c9554094a ts=2026-09-24T18:06:22.0210000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[689] _id=6abaac14485cab4c956f67a4 ts=2026-09-25T18:16:00.793Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 257 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26d.jsonl[12294] _id=6ac3e6e0de269131f9aeb1b9 ts=2026-10-05T18:05:19.8090000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12300] _id=6ac3e6e0de269131f9aeb1bb ts=2026-10-05T18:05:19.8090000Z; 0ms: 6aa4144c41b41dbac0c7f26d.jsonl[12302] _id=6ac3e6e0de269131f9aeb1c5 ts=2026-10-05T18:05:19.8140000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12298] _id=6ac3e6e0de269131f9aeb1c7 ts=2026-10-05T18:05:19.8140000Z; 0ms: 6aa4144c41b41dbac0c7f26d.jsonl[5804] _id=6abc07fa485cab4c9584c947 ts=2026-09-29T18:48:26.2420000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[5799] _id=6abc07fa485cab4c9584c949 ts=2026-09-29T18:48:26.2420000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4144c41b41dbac0c7f26d.jsonl[10875] _id=6abe8743485cab4c95abd066 ts=2026-10-01T16:16:03.4990000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10910] _id=6ac3c4f7de269131f9ad5b5d ts=2026-10-05T15:40:39.8210000Z; 71h 28m: 6aa4144c41b41dbac0c7f26d.jsonl[975] _id=6abaac42485cab4c956f6ae5 ts=2026-09-25T18:35:55.242Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1224] _id=6abaac4f485cab4c956f6c7f ts=2026-09-28T18:04:41.4410000Z; 24h 10m: 6aa4144c41b41dbac0c7f26d.jsonl[629] _id=6ab5669f485cab4c95540956 ts=2026-09-24T18:06:23.0140000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[693] _id=6abaac1c485cab4c956f67f9 ts=2026-09-25T18:16:52.171Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[11959] _id=6ac3cb95de269131f9ad9421 ts=2026-10-05T16:08:53.1720000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[11963] _id=6ac3cb95de269131f9ad9423 ts=2026-10-05T16:08:53.1730000Z; 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[12048] _id=6ac3cbf0de269131f9ad98f1 ts=2026-10-05T16:10:24.3960000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12051] _id=6ac3cbf0de269131f9ad98f5 ts=2026-10-05T16:10:24.3970000Z; 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[12494] _id=6ac3e795de269131f9aebbab ts=2026-10-05T18:08:21.3100000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12493] _id=6ac3e795de269131f9aebbb1 ts=2026-10-05T18:08:21.3110000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa4144c41b41dbac0c7f26d.jsonl[1213] _id=6abaac4e485cab4c956f6c45 ts=2026-09-25T18:42:32.728Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1218] _id=6abaac4e485cab4c956f6c51 ts=2026-09-28T18:04:13.7540000Z; 24h 4m: 6aa4144c41b41dbac0c7f26d.jsonl[688] _id=6ab567ea485cab4c95542174 ts=2026-09-24T18:11:54.7810000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[699] _id=6abaac14485cab4c956f679f ts=2026-09-25T18:16:00.152Z; 23h 24m: 6aa4144c41b41dbac0c7f26d.jsonl[3471] _id=6abab657485cab4c95706ae4 ts=2026-09-28T18:47:51.4390000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[3520] _id=6abbff6e485cab4c9584215b ts=2026-09-29T18:11:59.0480000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4144c41b41dbac0c7f26d.jsonl[10617] _id=6abe83dd485cab4c95abaf8a ts=2026-10-01T16:01:30.4880000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[11603] _id=6ac3c948de269131f9ad8637 ts=2026-10-05T15:59:03.3660000Z; 23h 25m: 6aa4144c41b41dbac0c7f26d.jsonl[3461] _id=6abab5fb485cab4c95705d29 ts=2026-09-28T18:46:18.3830000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[3524] _id=6abbff6f485cab4c95842171 ts=2026-09-29T18:12:00.1300000Z; 21h 33m: 6aa4144c41b41dbac0c7f26d.jsonl[8526] _id=6abd53ad485cab4c9591553d ts=2026-09-30T18:23:39.3990000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[9571] _id=6abe82e0485cab4c95ab9e7a ts=2026-10-01T15:57:20.0830000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3116 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26d.jsonl[10000] _id=6abe8356485cab4c95aba728 ts=2026-10-01T15:59:17.2950000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10115] _id=6abe8356485cab4c95aba72a ts=2026-10-01T15:59:17.2950000Z; 0ms: 6aa4144c41b41dbac0c7f26d.jsonl[10004] _id=6abe8343485cab4c95aba5ac ts=2026-10-01T15:58:57.4820000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[9997] _id=6abe8343485cab4c95aba5b0 ts=2026-10-01T15:58:57.4820000Z; 0ms: 6aa4144c41b41dbac0c7f26d.jsonl[10008] _id=6abe8345485cab4c95aba5c8 ts=2026-10-01T15:59:00.8180000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[9945] _id=6abe8345485cab4c95aba5cb ts=2026-10-01T15:59:00.8180000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 45h 29m 
  - Evidence: 45h 29m: 6aa4144c41b41dbac0c7f26d.jsonl[3301] _id=6abab514485cab4c95704c45 ts=2026-09-28T18:42:28.4200000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7518] _id=6abd34c3485cab4c958d5aab ts=2026-09-30T16:11:47.1040000Z; 23h 44m: 6aa4144c41b41dbac0c7f26d.jsonl[7161] _id=6abd34da485cab4c958d5bea ts=2026-09-30T16:12:10.7720000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[9517] _id=6abe82c0485cab4c95ab9d12 ts=2026-10-01T15:56:48.5220000Z; 20m 8s: 6aa4144c41b41dbac0c7f26d.jsonl[2839] _id=6abab036485cab4c956fe17b ts=2026-09-28T18:21:42.8880000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[3283] _id=6abab4ef485cab4c957048d7 ts=2026-09-28T18:41:51.3340000Z
- **INFO / Info** `SolarStillDesignEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 3h 43m 
  - Evidence: 3h 43m: 6aa4144c41b41dbac0c7f26d.jsonl[15327] _id=6ac51dd4de269131f9b4e755 ts=2026-10-06T16:12:04.3270000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[15582] _id=6ac55230de269131f9b7d1d8 ts=2026-10-06T19:55:27.6600000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6aa4144c41b41dbac0c7f26d.jsonl[64] _id=6ab41777485cab4c954f37c8 ts=2026-09-23T18:16:23.7220000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1585] _id=6abaaec8485cab4c956fada3 ts=2026-09-28T18:15:36.9150000Z; 23h 54m: 6aa4144c41b41dbac0c7f26d.jsonl[3139] _id=6abab3ab485cab4c957025db ts=2026-09-28T18:36:27.9020000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[5273] _id=6abc03e4485cab4c958482dd ts=2026-09-29T18:31:00.6210000Z; 20h 53m: 6aa4144c41b41dbac0c7f26d.jsonl[5810] _id=6abc080a485cab4c9584ca39 ts=2026-09-29T18:48:42.2040000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[6066] _id=6abd2dcb485cab4c958cd8ad ts=2026-09-30T15:42:06.6890000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.008s..0.012s shown 
  - Evidence: 8ms: 6aa4144c41b41dbac0c7f26d.jsonl[10688] _id=6abe85f8485cab4c95abc532 ts=2026-10-01T16:10:33.9860000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10689] _id=6abe85fa485cab4c95abc53a ts=2026-10-01T16:10:33.9940000Z; 10ms: 6aa4144c41b41dbac0c7f26d.jsonl[3015] _id=6abab1cd485cab4c95700471 ts=2026-09-28T18:28:29.1430000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[3012] _id=6abab1cd485cab4c95700473 ts=2026-09-28T18:28:29.1530000Z; 12ms: 6aa4144c41b41dbac0c7f26d.jsonl[3012] _id=6abab1cd485cab4c95700473 ts=2026-09-28T18:28:29.1530000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[3003] _id=6abab1cd485cab4c9570047d ts=2026-09-28T18:28:29.1650000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 5m 
  - Evidence: 120h 5m: 6aa4144c41b41dbac0c7f26d.jsonl[7334] _id=6abd33f6485cab4c958d4a78 ts=2026-09-30T16:08:22.2620000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12105] _id=6ac3ccaade269131f9ad9e39 ts=2026-10-05T16:13:30.4900000Z; 71h 25m: 6aa4144c41b41dbac0c7f26d.jsonl[1170] _id=6abaac4a485cab4c956f6be1 ts=2026-09-25T18:40:45.38Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1287] _id=6abaac96485cab4c956f6f39 ts=2026-09-28T18:06:14.5460000Z; 45h 57m: 6aa4144c41b41dbac0c7f26d.jsonl[1334] _id=6abaaceb485cab4c956f74f7 ts=2026-09-28T18:07:39.6020000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7080] _id=6abd3323485cab4c958d3f04 ts=2026-09-30T16:04:51.3020000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 4m 
  - Evidence: 120h 4m: 6aa4144c41b41dbac0c7f26d.jsonl[7342] _id=6abd33f6485cab4c958d4a82 ts=2026-09-30T16:08:22.3310000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12118] _id=6ac3cc8bde269131f9ad9d51 ts=2026-10-05T16:12:59.5710000Z; 71h 25m: 6aa4144c41b41dbac0c7f26d.jsonl[1138] _id=6abaac4a485cab4c956f6be3 ts=2026-09-25T18:40:45.415Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1267] _id=6abaac8f485cab4c956f6ec9 ts=2026-09-28T18:06:07.0390000Z; 45h 56m: 6aa4144c41b41dbac0c7f26d.jsonl[1335] _id=6abaaceb485cab4c956f74fb ts=2026-09-28T18:07:39.6150000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7000] _id=6abd32f5485cab4c958d3c74 ts=2026-09-30T16:04:05.0360000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.037s..0.037s shown 
  - Evidence: 37ms: 6aa4144c41b41dbac0c7f26d.jsonl[7339] _id=6abd33f6485cab4c958d4a7a ts=2026-09-30T16:08:22.2940000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7342] _id=6abd33f6485cab4c958d4a82 ts=2026-09-30T16:08:22.3310000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 4m 
  - Evidence: 120h 4m: 6aa4144c41b41dbac0c7f26d.jsonl[7318] _id=6abd33f4485cab4c958d4a6a ts=2026-09-30T16:08:20.5240000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[12127] _id=6ac3cc8dde269131f9ad9d67 ts=2026-10-05T16:13:01.3090000Z; 71h 24m: 6aa4144c41b41dbac0c7f26d.jsonl[1136] _id=6abaac4a485cab4c956f6bdd ts=2026-09-25T18:40:38.106Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1242] _id=6abaac5a485cab4c956f6ccf ts=2026-09-28T18:05:14.5030000Z; 45h 56m: 6aa4144c41b41dbac0c7f26d.jsonl[1328] _id=6abaace7485cab4c956f74b3 ts=2026-09-28T18:07:34.9900000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7008] _id=6abd32f8485cab4c958d3c8a ts=2026-09-30T16:04:08.2290000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 137 interval(s) ≤ 0.015s..0.017s shown 
  - Evidence: 15ms: 6aa4144c41b41dbac0c7f26d.jsonl[1283] _id=6abaac94485cab4c956f6f1b ts=2026-09-28T18:06:12.9360000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1276] _id=6abaac95485cab4c956f6f1d ts=2026-09-28T18:06:12.9510000Z; 16ms: 6aa4144c41b41dbac0c7f26d.jsonl[1280] _id=6abaac93485cab4c956f6f03 ts=2026-09-28T18:06:11.2950000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1281] _id=6abaac93485cab4c956f6f05 ts=2026-09-28T18:06:11.3110000Z; 17ms: 6aa4144c41b41dbac0c7f26d.jsonl[7061] _id=6abd3314485cab4c958d3e16 ts=2026-09-30T16:04:36.3150000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7070] _id=6abd3314485cab4c958d3e18 ts=2026-09-30T16:04:36.3320000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 71h 25m 
  - Evidence: 71h 25m: 6aa4144c41b41dbac0c7f26d.jsonl[1120] _id=6abaac48485cab4c956f6b9f ts=2026-09-25T18:40:05.636Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1263] _id=6abaac8a485cab4c956f6ea3 ts=2026-09-28T18:06:02.2150000Z; 45h 58m: 6aa4144c41b41dbac0c7f26d.jsonl[1332] _id=6abaaceb485cab4c956f74f4 ts=2026-09-28T18:07:39.4960000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[7148] _id=6abd3365485cab4c958d4288 ts=2026-09-30T16:05:57.4480000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 288h 22m 
  - Evidence: 288h 22m: 6aa4144c41b41dbac0c7f26d.jsonl[59] _id=6ab41771485cab4c954f378a ts=2026-09-23T18:16:17.8940000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[13196] _id=6ac3eed4de269131f9af3bc5 ts=2026-10-05T18:38:22.4570000Z; 21h 1m: 6aa4144c41b41dbac0c7f26d.jsonl[13196] _id=6ac3eed4de269131f9af3bc5 ts=2026-10-05T18:38:22.4570000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[13995] _id=6ac51632de269131f9b48ef1 ts=2026-10-06T15:39:30.5040000Z; 3h 51m: 6aa4144c41b41dbac0c7f26d.jsonl[15017] _id=6ac51ac7de269131f9b4d2a3 ts=2026-10-06T15:59:03.5270000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[15480] _id=6ac55118de269131f9b7beb8 ts=2026-10-06T19:50:48.1220000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 91h 44m 
  - Evidence: 91h 44m: 6aa4144c41b41dbac0c7f26d.jsonl[10669] _id=6abe85ad485cab4c95abc32c ts=2026-10-01T16:09:19.8380000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10879] _id=6ac38fc2de269131f9a83c5e ts=2026-10-05T11:53:50.8160000Z; 71h 43m: 6aa4144c41b41dbac0c7f26d.jsonl[807] _id=6abaac29485cab4c956f68bb ts=2026-09-25T18:20:18.013Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1217] _id=6abaac4e485cab4c956f6c4b ts=2026-09-28T18:04:03.5470000Z; 24h 12m: 6aa4144c41b41dbac0c7f26d.jsonl[549] _id=6ab565e5485cab4c9553f5e8 ts=2026-09-24T18:03:16.8160000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[740] _id=6abaac14485cab4c956f6797 ts=2026-09-25T18:15:47.446Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 28 gap(s), longest 91h 38m 
  - Evidence: 91h 38m: 6aa4144c41b41dbac0c7f26d.jsonl[10815] _id=6abe86fa485cab4c95abccbe ts=2026-10-01T16:14:51.6580000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10878] _id=6ac38fc2de269131f9a83c5c ts=2026-10-05T11:53:50.8150000Z; 71h 43m: 6aa4144c41b41dbac0c7f26d.jsonl[800] _id=6abaac29485cab4c956f68b9 ts=2026-09-25T18:20:18.002Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1216] _id=6abaac4e485cab4c956f6c49 ts=2026-09-28T18:04:03.5190000Z; 24h 12m: 6aa4144c41b41dbac0c7f26d.jsonl[548] _id=6ab565e5485cab4c9553f5db ts=2026-09-24T18:03:16.8160000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[739] _id=6abaac14485cab4c956f6793 ts=2026-09-25T18:15:47.445Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa4144c41b41dbac0c7f26d.jsonl[10877] _id=6abe8749485cab4c95abd106 ts=2026-10-01T16:16:09.8780000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[11387] _id=6ac3c7fbde269131f9ad7fc7 ts=2026-10-05T15:53:31.5610000Z; 71h 45m: 6aa4144c41b41dbac0c7f26d.jsonl[716] _id=6abaac29485cab4c956f68b5 ts=2026-09-25T18:20:05.086Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1254] _id=6abaac6e485cab4c956f6db7 ts=2026-09-28T18:05:34.5790000Z; 24h 8m: 6aa4144c41b41dbac0c7f26d.jsonl[687] _id=6ab567ec485cab4c9554217a ts=2026-09-24T18:11:56.4320000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[716] _id=6abaac29485cab4c956f68b5 ts=2026-09-25T18:20:05.086Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa4144c41b41dbac0c7f26d.jsonl[10691] _id=6abe85fa485cab4c95abc544 ts=2026-10-01T16:10:34.0290000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[10895] _id=6ac3c4edde269131f9ad5af1 ts=2026-10-05T15:40:29.4180000Z; 71h 22m: 6aa4144c41b41dbac0c7f26d.jsonl[1183] _id=6abaac4b485cab4c956f6c0b ts=2026-09-25T18:41:26.621Z -> 6aa4144c41b41dbac0c7f26d.jsonl[1220] _id=6abaac4f485cab4c956f6c63 ts=2026-09-28T18:04:19.6860000Z; 24h 10m: 6aa4144c41b41dbac0c7f26d.jsonl[607] _id=6ab5666f485cab4c95540652 ts=2026-09-24T18:05:34.9770000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[691] _id=6abaac14485cab4c956f67ab ts=2026-09-25T18:16:01.067Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26d.jsonl[15226] _id=6ac51d1dde269131f9b4e237 ts=2026-10-06T16:09:01.3170000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[15270] _id=6ac51d1dde269131f9b4e239 ts=2026-10-06T16:09:01.3180000Z; 3ms: 6aa4144c41b41dbac0c7f26d.jsonl[14469] _id=6ac5177bde269131f9b4ad63 ts=2026-10-06T15:44:58.6040000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[14470] _id=6ac5177bde269131f9b4ad67 ts=2026-10-06T15:44:58.6070000Z; 3ms: 6aa4144c41b41dbac0c7f26d.jsonl[14715] _id=6ac5191cde269131f9b4c579 ts=2026-10-06T15:51:55.9270000Z -> 6aa4144c41b41dbac0c7f26d.jsonl[14720] _id=6ac5191cde269131f9b4c57b ts=2026-10-06T15:51:55.9300000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[3133] _id=6abab393485cab4c95702451 ts=2026-09-28T18:36:03.6760000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[4994] _id=6abc0155485cab4c958451f1 ts=2026-09-29T18:20:05.3780000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[5215] _id=6abc0319485cab4c9584700b ts=2026-09-29T18:27:37.1540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 125 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1797] _id=6abaaf2c485cab4c956fbb59 ts=2026-09-28T18:17:15.3680000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1874] _id=6abaaf37485cab4c956fbd1f ts=2026-09-28T18:17:25.1640000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1857] _id=6abaaf38485cab4c956fbd45 ts=2026-09-28T18:17:28.2170000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 229 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1576] _id=6abaaeb8485cab4c956faca9 ts=2026-09-28T18:15:19.6240000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1688] _id=6abaaf0a485cab4c956fb61d ts=2026-09-28T18:16:42.3310000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1695] _id=6abaaf0c485cab4c956fb63b ts=2026-09-28T18:16:43.0810000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1081] _id=6abaac44485cab4c956f6b23 ts=2026-09-25T18:37:20.077Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1089] _id=6abaac45485cab4c956f6b4d ts=2026-09-25T18:38:11.429Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1104] _id=6abaac46485cab4c956f6b65 ts=2026-09-25T18:39:20.298Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 215 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1067] _id=6abaac43485cab4c956f6aff ts=2026-09-25T18:36:25.913Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1054] _id=6abaac43485cab4c956f6b01 ts=2026-09-25T18:36:25.965Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1068] _id=6abaac43485cab4c956f6b03 ts=2026-09-25T18:36:26.254Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[13196] _id=6ac3eed4de269131f9af3bc5 ts=2026-10-05T18:38:22.4570000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[13995] _id=6ac51632de269131f9b48ef1 ts=2026-10-06T15:39:30.5040000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[15017] _id=6ac51ac7de269131f9b4d2a3 ts=2026-10-06T15:59:03.5270000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[712] _id=6abaac2e485cab4c956f6921 ts=2026-09-25T18:22:15.179Z`; `6aa4144c41b41dbac0c7f26d.jsonl[831] _id=6abaac35485cab4c956f69c7 ts=2026-09-25T18:28:19.433Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1049] _id=6abaac42485cab4c956f6aeb ts=2026-09-25T18:35:55.311Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 11 records 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[329] _id=6ab41caf485cab4c954f60f5 ts=?`; `6aa4144c41b41dbac0c7f26d.jsonl[490] _id=6ab56179485cab4c955387b1 ts=?`; `6aa4144c41b41dbac0c7f26d.jsonl[5812] _id=6abcfdc5485cab4c95864f1d ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 733 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1905] _id=6abaaf3d485cab4c956fbde3 ts=2026-09-28T18:17:33.0370000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[2047] _id=6abaaf5a485cab4c956fc3ba ts=2026-09-28T18:18:01.0370000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[2116] _id=6abaaf64485cab4c956fc609 ts=2026-09-28T18:18:10.6590000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 861 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1560] _id=6abaaeb7485cab4c956fac87 ts=2026-09-28T18:15:19.0820000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1577] _id=6abaaeb8485cab4c956fac89 ts=2026-09-28T18:15:19.0820000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1578] _id=6abaaeb8485cab4c956fac8b ts=2026-09-28T18:15:19.0980000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 28 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[3012] _id=6abab1cd485cab4c95700473 ts=2026-09-28T18:28:29.1530000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[3003] _id=6abab1cd485cab4c9570047d ts=2026-09-28T18:28:29.1650000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[3045] _id=6abab2a2485cab4c95701445 ts=2026-09-28T18:32:02.3580000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 20 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[7182] _id=6abd337e485cab4c958d4416 ts=2026-09-30T16:06:22.1140000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[7213] _id=6abd339a485cab4c958d4566 ts=2026-09-30T16:06:50.4910000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[7231] _id=6abd33a1485cab4c958d45d0 ts=2026-09-30T16:06:57.3510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[1329] _id=6abaace9485cab4c956f74e1 ts=2026-09-28T18:07:38.0010000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[1330] _id=6abaacea485cab4c956f74ed ts=2026-09-28T18:07:38.9680000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[7149] _id=6abd3366485cab4c958d42b0 ts=2026-09-30T16:05:58.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 472 start, 455 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 155 unmatched 'BecameCameraCentered' (totals: 1140 open, 1110 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 122 unmatched 'BecameVisible' (totals: 1317 open, 1424 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 32 open, 30 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 179 open, 392 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 9 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 34 unmatched 'questActiveEvent' (totals: 69 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 434 of 15751 adjacent _id pairs reverse in client time; worst 85305.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f26d.jsonl[687] _id=6ab567ec485cab4c9554217a ts=2026-09-24T18:11:56.4320000Z`; `6aa4144c41b41dbac0c7f26d.jsonl[738] _id=6abaac13485cab4c956f6783 ts=2026-09-23T18:30:11.395Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.11s, min -430431.71s, max +12.29s over 15752 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26d\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 11 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4991 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2597); Unit 4 Dev (1054); Unit 5 Dev - Dungeon (956); Unit 3 Dungeon Dev (384)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.11s, n=4990)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4991/4991 records)
    "BecameInvisible"  x1424
    "BecameVisible"  x1317
    "BecameCameraCentered"  x1140
    "BecameCameraUncentered"  x1110
data.pieceId  (string, 4991/4991 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4991/4991 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4433 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1068); Unit 2 Prod (Refactor) (794); Unit 4 Dev - Dungeon (517); Unit 5 Dev - Dungeon (473); Unit 3 Dungeon Dev (387); Unit 1 Dev (385); Unit 4 Dev (335); Unit 4 Dev - Anderson Base (316); Unit 5 Dev (158)
- **Intervals:** median 0.75s (p5 0.04s / p95 13.67s, n=4432)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4433/4433 records)
    "pressed"  x4433
data.actionType  (string, 4433/4433 records)
    "Move"  x2391
    "Interact"  x701
    "Jump"  x598
    "Sprint"  x459
    "Ascend"  x112
    "Hoverboard"  x76
    "Pause"  x27
    "Map"  x24
    "SkipCinematic"  x21
    "Descend"  x20
    "ToggleDebug"  x4
data.key  (string, 4433/4433 records, 15 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4433/4433 records)
    "Player"  x3409
    "Drone"  x1024
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2496 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (483); Unit 1 Dev (429); Unit 3 Dev (409); Unit 5 Dev (327); Unit 4 Dev (277); Unit 4 Dev - Anderson Base (175); Unit 3 Dungeon Dev (157); Unit 4 Dev - Dungeon (126); Unit 5 Dev - Dungeon (113)
- **eventKey:** present on 1569 of 2496 records
- **Intervals:** median 4.40s (p5 0.00s / p95 36.27s, n=2495)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1569; [conversationId, dialogueEventType] x927
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2496/2496 records)
    numeric range 8 .. 118 (49 unique)
data.dialogueEventType  (string, 2496/2496 records)
    "DialogueNodeEvent"  x1569
    "DialogueStartEvent"  x472
    "DialogueFinishEvent"  x455
data.nodeId  (number, 1569/2496 records)
    numeric range 0 .. 290 (213 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2234 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (494); Unit 1 Dev (388); Unit 3 Dev (295); Unit 4 Dev (228); Unit 3 Dungeon Dev (189); Unit 5 Dev (181); Unit 5 Dev - Dungeon (162); Unit 4 Dev - Dungeon (156); Unit 4 Dev - Anderson Base (141)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.32s, n=2220)
- **Fields under `data`:**

```text
data.position  (object, 2234/2234 records)
data.position.x  (number, 2234/2234 records)
    numeric range -681.506 .. 1444.72 (595 unique)
data.position.y  (number, 2234/2234 records)
    numeric range -114.326 .. 223.583 (435 unique)
data.position.z  (number, 2234/2234 records)
    numeric range -1040.57 .. 1753.12 (594 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 615 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (259); Unit 3 Dev (217); Unit 1 Dev (99); Unit 5 Dev (40)
- **Intervals:** median 0.36s (p5 0.02s / p95 9.66s, n=614)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 615/615 records)
    "argumentationNodeHoverEnd"  x392
    "argumentationNodeHoverStart"  x179
    "argumentationNodeAdd"  x29
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 615/615 records)
    "Unit 4 - Flooding"  x259
    "Unit 3 - Pollution Upstream"  x217
    "Unit 1 - Freshwater"  x74
    "Unit 5"  x40
    "Unit 1 - Argumentation Tutorial"  x25
data.nodeName  (string, 615/615 records)
    "2"  x163
    "I"  x120
    "1"  x63
    "II"  x61
    "A"  x53
    "4"  x45
    "3"  x43
    "B"  x36
    "C"  x16
    "D"  x10
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 311 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (88); Unit 3 Dungeon Dev (56); Unit 2 Prod (Refactor) (38); Unit 1 Dev (34); Unit 4 Dev (23); Unit 3 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 5 Dev (18); Unit 5 Dev - Dungeon (18)
- **Intervals:** median 10.76s (p5 0.24s / p95 866.37s, n=310)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 311/311 records)
    36 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 311/311 records)
    91 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 108 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (32); Unit 2 Prod (Refactor) (19); Unit 3 Dev (12); Unit 5 Dev (12); Unit 4 Dev - Dungeon (11); Unit 4 Dev (8); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 108 of 108 records
- **Intervals:** median 192.60s (p5 0.00s / p95 72562.74s, n=107)
- **`data` key-set variants:** [questEventType, questID, questName] x69; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 108/108 records)
    "questActiveEvent"  x69
    "questFinishEvent"  x39
data.questID  (string, 108/108 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 108/108 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/108 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 91 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (42); Unit 3 Dev (42); Unit 1 Dev (5); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.98s (p5 0.17s / p95 10302.55s, n=90)
- **`data` key-set variants:** [actionType, featureUsed] x62; [actionType, featureUsed, location] x25; [actionType, featureUsed, legendName] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 91/91 records)
    "MapOpenEvent"  x32
    "MapCloseEvent"  x30
    "WaypointMoveEvent"  x19
    "WaypointSetEvent"  x6
    "Selected"  x3
    "Unselected"  x1
data.featureUsed  (string, 91/91 records)
    "Map"  x62
    "Waypoint"  x25
    "Legend"  x4
data.legendName  (string, 4/91 records)
    "0 ft"  x2
    "360 ft"  x1
    "90 ft"  x1
data.location  (object, 25/91 records)
data.location.x  (number, 25/91 records)
    numeric range -270.426 .. 268.91 (24 unique)
data.location.y  (number, 25/91 records)
    numeric range -192.5 .. 280.461 (23 unique)
data.location.z  (number, 25/91 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 80 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (29); Unit 2 Prod (Refactor) (15); Unit 1 Dev (9); Unit 3 Dev (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (4); Unit 4 Dev - Dungeon (4); Unit 5 Dev - Dungeon (2); Transition (1); Unit 4 Dev (1)
- **Intervals:** median 229.94s (p5 9.12s / p95 76109.33s, n=79)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 80/80 records)
    true  x80
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 62 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (62)
- **Intervals:** median 4.45s (p5 0.42s / p95 62.54s, n=61)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "On"  x36
    "Off"  x26
data.floor  (string, 62/62 records)
    "3"  x30
    "4"  x27
    "2"  x3
    "1"  x2
data.machineNumber  (string, 62/62 records)
    "One"  x51
    "Two"  x11
data.machineType  (string, 62/62 records)
    "Condenser"  x34
    "Evaporator"  x14
    "DualChamber_Condenser"  x6
    "DualChamber_Evaporator"  x6
    "VentSwitch"  x2
data.room  (string, 62/62 records)
    "2"  x25
    "3"  x14
    "4"  x14
    "1"  x9
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 59 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (11); Unit 3 Dev (9); Unit 5 Dev (7); Unit 4 Dev - Dungeon (6); Unit 4 Dev - Anderson Base (4); Unit 5 Dev - Dungeon (2); Transition (1); Unit 4 Dev (1)
- **Intervals:** median 315.49s (p5 4.86s / p95 84670.67s, n=58)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 59/59 records)
    false  x59
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (36); Unit 2 Prod (Refactor) (14); Unit 3 Dev (8)
- **Intervals:** median 0.81s (p5 0.20s / p95 251.29s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x50; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/58 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/58 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 50/58 records)
    "RightDrag"  x28
    "LeftDrag"  x22
data.currentSoilType  (string, 50/58 records)
    "CLAY"  x11
    "CLAYSAND"  x10
    "CLAYROCK"  x8
    "SAND"  x8
    "SANDGRAVEL"  x7
    "BEDROCK"  x3
    "GRAVEL"  x3
data.isCorrectSelection  (string, 50/58 records)
    "false"  x38
    "true"  x12
data.waterLevelStatus  (string, 50/58 records)
    "Proper"  x27
    "TooHigh"  x13
    "TooLow"  x10
data.waterRetentionChange  (string, 50/58 records)
    "Increase"  x21
    "Decrease"  x17
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 35 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 1 Dev (7); Unit 3 Dev (4); Unit 4 Dev (3); Unit 4 Dev - Dungeon (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (2); MainMenu (1)
- **Intervals:** median 1262.57s (p5 133.01s / p95 147021.04s, n=34)
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "DebugMenuStateChanged"  x35
data.isOpened  (bool, 35/35 records)
    false  x35
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 34 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (16); Unit 3 Dev (9); Unit 1 Dev (7); Unit 5 Dev (2)
- **Intervals:** median 24.75s (p5 1.30s / p95 202110.69s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "submitAnswerEvent"  x34
data.answerSubmitted  (string, 34/34 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 34/34 records)
    "Unit 4 - Flooding"  x16
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Freshwater"  x6
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 29 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (29)
- **Intervals:** median 5338.70s (p5 124.40s / p95 198349.32s, n=28)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 29/29 records)
    true  x29
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 26 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (20); Unit 1 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.43s (p5 0.19s / p95 73573.30s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "Close"  x13
    "Open"  x13
data.toolName  (string, 26/26 records, 24 empty-string)
    ""  x24
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `soilMachine` — 25 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (25)
- **Intervals:** median 1.81s (p5 0.31s / p95 92.95s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "ChangeCanister"  x25
data.canisterType  (string, 25/25 records)
    "Clay"  x8
    "Sand"  x8
    "Bedrock"  x5
    "Gravel"  x4
data.floor  (string, 25/25 records)
    "3"  x15
    "5"  x9
    "4"  x1
data.machine  (string, 25/25 records)
    "1"  x24
    "2"  x1
data.row  (string, 25/25 records)
    "TopRow"  x24
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 76.99s (p5 0.06s / p95 300910.53s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x12
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 17/17 records)
    "Unit 1 - Does the planet WAT-247 have freshwater"  x6
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 1 - Freshwater"  x6
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 16 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (16)
- **Intervals:** median 1.35s (p5 0.66s / p95 4026.01s, n=15)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x14; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "optionSelected"  x14
    "DesignSubmitted"  x2
data.designSelections  (object, 2/16 records)
data.designSelections.glassRoofTemperature  (string, 2/16 records)
    "Cold"  x1
    "Hot"  x1
data.designSelections.roofCovering  (string, 2/16 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/16 records)
    "Tilted Out"  x2
data.featureUsed  (string, 16/16 records)
    "RoofStyle"  x7
    "GlassRoofTemperature"  x5
    "ExtraCovering"  x2
    "Submit"  x2
data.selectedOption  (string, 14/16 records, 2 empty-string)
    "Tilted In"  x3
    ""  x2
    "Cold"  x2
    "Hot"  x2
    "Tilted Out"  x2
    "Covered"  x1
    "Flat"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 2.93s (p5 1.45s / p95 15.13s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x4
data.boxId  (string, 11/11 records)
    "2"  x11
data.soilType  (string, 11/11 records)
    "Clay"  x11
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 11 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (5)
- **Intervals:** median 4.00s (p5 0.73s / p95 215910.20s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 11/11 records)
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x4
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 11/11 records)
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 11 records

- **Scenes:** <missing sceneName> (11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 11/11 records)
    true  x11
data.message  (string, 11/11 records)
    "Permissions check failed"  x7
    "A user gesture is required to request Pointer Lock."  x4
data.phase  (string, 11/11 records)
    "running"  x11
data.stack  (string, 11/11 records, 4 empty-string)
    "TypeError: Permissions check failed"  x7
    ""  x4
data.type  (string, 11/11 records)
    "unhandled_rejection"  x11
data.unitId  (string, 11/11 records)
    "unit2"  x5
    "unit1"  x2
    "unit3"  x2
    "unit4"  x2
data.workspace  (string, 11/11 records)
    "mhs"  x11
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 13904.59s (p5 236.37s / p95 845633.26s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x5
    "Open"  x1
data.chatID  (string, 6/6 records)
    "NA"  x5
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 250776.85s (p5 107479.05s / p95 345183.55s, n=3)
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
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (14 records)
- `TerasGardenBox` data.actionType: "" (7x)
- `TopographicMapEvent` data.actionType: "Selected" (3x); "Unselected" (1x); "WaypointMoveEvent" (19x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (4x); "Waypoint" (25x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*