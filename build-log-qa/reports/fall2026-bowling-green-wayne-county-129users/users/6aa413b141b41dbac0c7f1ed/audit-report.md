# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1ed

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1ed
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1ed.jsonl
- **Records:** 20942 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1ed
- **Time span:** 2026-09-23T13:04:37.488000+00:00 .. 2026-10-06T12:58:08.281000+00:00 (311h 53m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1ed\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 20942 records, 10 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 111 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 11214 | 53.55 | 1 | 9 | 0 | 2026-09-23T13:05:14.877000+00:00 | 2026-10-06T12:58:06.480000+00:00 | 311h 52m |
| PuzzlePieceVisibleEvent | 4422 | 21.12 | 1 | 4 | 0 | 2026-09-23T13:39:04.228000+00:00 | 2026-10-05T13:10:31.881000+00:00 | 287h 31m |
| DialogueEvent | 2063 | 9.85 | 1 | 9 | 1234 | 2026-09-23T13:08:14.475000+00:00 | 2026-10-05T13:41:12.165000+00:00 | 288h 32m |
| PlayerPositionEvent | 1924 | 9.19 | 1 | 9 | 0 | 2026-09-23T13:05:09.480000+00:00 | 2026-10-06T12:58:08.166000+00:00 | 311h 52m |
| argumentationNodeEvent | 551 | 2.63 | 1 | 4 | 0 | 2026-09-23T13:27:36.492000+00:00 | 2026-10-05T13:31:50.190000+00:00 | 288h 4m |
| ObjectInterEvent | 260 | 1.24 | 1 | 9 | 0 | 2026-09-23T13:13:02.380000+00:00 | 2026-10-06T12:54:52.533000+00:00 | 311h 41m |
| TopographicMapEvent | 94 | 0.45 | 1 | 2 | 0 | 2026-09-23T13:35:59.064000+00:00 | 2026-09-30T13:21:57.838000+00:00 | 167h 45m |
| questEvent | 81 | 0.39 | 1 | 9 | 81 | 2026-09-23T13:08:14.453000+00:00 | 2026-10-06T12:53:57.892000+00:00 | 311h 45m |
| WaterChamberEvent | 65 | 0.31 | 1 | 1 | 0 | 2026-10-05T13:06:17.154000+00:00 | 2026-10-05T13:18:52.703000+00:00 | 12m 35s |
| Soil Key Puzzle | 64 | 0.31 | 1 | 3 | 0 | 2026-09-24T13:26:06.856000+00:00 | 2026-10-01T12:58:09.867000+00:00 | 167h 32m |
| SolarStillDesignEvent | 52 | 0.25 | 1 | 1 | 0 | 2026-10-05T13:38:46.080000+00:00 | 2026-10-05T13:40:03.715000+00:00 | 1m 17s |
| argumentationAnswerEvent | 26 | 0.12 | 1 | 4 | 0 | 2026-09-23T13:28:48.777000+00:00 | 2026-10-05T13:31:51.375000+00:00 | 288h 3m |
| DEBUGMenu | 22 | 0.11 | 1 | 8 | 0 | 2026-09-23T13:05:09.469000+00:00 | 2026-10-05T13:02:05.117000+00:00 | 287h 56m |
| gameWindowFocusEvent | 22 | 0.11 | 1 | 5 | 0 | 2026-09-23T13:04:37.488000+00:00 | 2026-10-06T12:58:08.281000+00:00 | 311h 53m |
| gameStartEvent | 16 | 0.08 | 1 | 1 | 0 | 2026-09-23T13:04:37.490000+00:00 | 2026-10-06T12:53:28.646000+00:00 | 311h 48m |
| argumentationEvent | 15 | 0.07 | 1 | 4 | 0 | 2026-09-23T13:28:20.071000+00:00 | 2026-10-05T13:31:51.407000+00:00 | 288h 3m |
| DaniEvent | 9 | 0.04 | 1 | 1 | 0 | 2026-09-23T13:35:41.505000+00:00 | 2026-09-24T13:16:06.133000+00:00 | 23h 40m |
| TerasGardenBox | 9 | 0.04 | 1 | 1 | 0 | 2026-10-01T13:36:40.406000+00:00 | 2026-10-01T13:37:31.614000+00:00 | 51.2s |
| argumentationToolEvent | 9 | 0.04 | 1 | 1 | 0 | 2026-09-23T13:28:16.752000+00:00 | 2026-09-23T13:30:34.586000+00:00 | 2m 17s |
| soilMachine | 9 | 0.04 | 1 | 1 | 0 | 2026-10-01T13:09:17.020000+00:00 | 2026-10-01T13:15:29.049000+00:00 | 6m 12s |
| gameWindowUnfocusEvent | 7 | 0.03 | 1 | 4 | 0 | 2026-09-23T13:40:46.406000+00:00 | 2026-10-06T12:58:08.274000+00:00 | 311h 17m |
| chatEvent | 3 | 0.01 | 1 | 2 | 0 | 2026-10-05T13:02:05.063000+00:00 | 2026-10-06T12:53:49.548000+00:00 | 23h 51m |
| crash | 3 | 0.01 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-23T13:33:36.686000+00:00 | 2026-09-30T13:28:36.159000+00:00 | 167h 54m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 604499.473s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 0.253s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.433s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 2.308s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 21.119s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.503s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 42952.243s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 83698.843s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1631.452s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85654.504s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 30.064s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 9 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 4.7x vs baseline. 
  - Observed: 11214 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 13.0x vs baseline. 
  - Observed: 52 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 240 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 65 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,3,I; A,4,I; B,1,II; B,3,I; B,5,I; C,1,II; C,2,II; C,3,II; C,D,2,II; C,D,3,II; C,D,A,2,II; D,2,I; D,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.9x vs baseline. 
  - Observed: 551 records 
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
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 7 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 40 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[163] _id=6ab3d0c9485cab4c954ba64c ts=2026-09-23T13:14:49.3050000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[233] _id=6ab3d1a5485cab4c954bd356 ts=2026-09-23T13:18:29.0640000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[395] _id=6ab3d239485cab4c954be9c4 ts=2026-09-23T13:20:57.4540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[5452] _id=6ab67043485cab4c955453ed ts=2026-09-25T12:59:46.7880000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[18548] _id=6ac39ec7de269131f9a83d86 ts=2026-10-05T12:57:39.4210000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[4] _id=6ab3ce65485cab4c954b84ba ts=2026-09-23T13:04:37.4900000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[17] _id=6ab3cf24485cab4c954b86cc ts=2026-09-23T13:07:48.6550000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[926] _id=6ab3d584485cab4c954c84bd ts=2026-09-23T13:35:00.1060000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[3] _id=6ab3ce65485cab4c954b84b8 ts=2026-09-23T13:04:37.4880000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[18] _id=6ab3cf24485cab4c954b86ca ts=2026-09-23T13:07:48.6530000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[978] _id=6ab3d584485cab4c954c84b3 ts=2026-09-23T13:35:00.1050000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[1490] _id=6ab3d6de485cab4c954cb079 ts=2026-09-23T13:40:46.4060000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[4860] _id=6ab5256a485cab4c9551038f ts=2026-09-24T13:28:10.5050000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[10438] _id=6abbb927485cab4c957c4264 ts=2026-09-29T13:12:07.4700000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 94 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[1083] _id=6ab3d5bf485cab4c954c8bb3 ts=2026-09-23T13:35:59.0640000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1091] _id=6ab3d5c1485cab4c954c8c03 ts=2026-09-23T13:36:01.4770000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1453] _id=6ab3d694485cab4c954ca925 ts=2026-09-23T13:39:32.6360000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 11213 | 0.0 | 0.253 | 100.131 | 2.056 | 343005.706 | 0.6 | 1312 | 9 |
| PuzzlePieceVisibleEvent | 4421 | 0.0 | 0.019 | 234.13 | 0.712 | 431616.769 | 0.26 | 3049 | 8 |
| DialogueEvent | 2062 | 0.001 | 4.443 | 503.772 | 30.23 | 343038.766 | 0.12 | 629 | 7 |
| PlayerPositionEvent | 1910 | 9.752 | 9.999 | 543.839 | 10.018 | 342991.384 | 0.11 | 0 | 7 |
| argumentationNodeEvent | 550 | 0.004 | 0.294 | 1885.552 | 4.53 | 432444.561 | 0.03 | 136 | 4 |
| ObjectInterEvent | 259 | 0.002 | 6.275 | 4332.472 | 472.161 | 343210.473 | 0.01 | 3 | 13 |
| TopographicMapEvent | 93 | 0.015 | 2.963 | 6494.18 | 417.444 | 258163.677 | 0.01 | 2 | 4 |
| questEvent | 80 | 0.002 | 212.072 | 14029.293 | 84197.954 | 343089.219 | 0.0 | 16 | 12 |
| WaterChamberEvent | 64 | 0.237 | 2.308 | 11.805 | 64.265 | 104.499 | 5.08 | 0 | 0 |
| Soil Key Puzzle | 63 | 0.129 | 0.862 | 9573.381 | 76.669 | 516800.336 | 0.01 | 0 | 3 |
| SolarStillDesignEvent | 51 | 0.398 | 1.279 | 1.522 | 3.405 | 7.098 | 39.42 | 0 | 0 |
| argumentationAnswerEvent | 25 | 2.723 | 21.119 | 41479.304 | 310957.426 | 432472.328 | 0.0 | 0 | 4 |
| DEBUGMenu | 21 | 97.582 | 797.738 | 49362.65 | 259035.45 | 343471.45 | 0.0 | 0 | 13 |
| gameWindowFocusEvent | 21 | 27.797 | 1631.452 | 53467.181 | 259041.894 | 345744.412 | 0.0 | 0 | 11 |
| gameStartEvent | 15 | 96.182 | 83698.843 | 74835.41 | 285052.65 | 345744.411 | 0.0 | 0 | 11 |
| argumentationEvent | 14 | 0.023 | 98.798 | 74072.238 | 375903.483 | 432441.515 | 0.0 | 3 | 4 |
| DaniEvent | 8 | 0.005 | 2.715 | 10653.078 | 55302.797 | 84928.561 | 0.01 | 1 | 1 |
| TerasGardenBox | 8 | 0.333 | 1.433 | 6.401 | 23.231 | 26.362 | 9.37 | 0 | 0 |
| argumentationToolEvent | 8 | 0.098 | 0.503 | 17.229 | 87.028 | 132.117 | 3.48 | 0 | 0 |
| soilMachine | 8 | 3.024 | 30.064 | 46.504 | 130.891 | 165.321 | 1.29 | 0 | 0 |
| gameWindowUnfocusEvent | 6 | 203.909 | 85654.504 | 186773.645 | 496153.343 | 517858.802 | 0.0 | 0 | 4 |
| chatEvent | 2 | 1057.637 | 42952.243 | 42952.243 | 80657.387 | 84846.848 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 604499.473 | 604499.473 | 604499.473 | 604499.473 | 604499.473 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[308] _id=6ab3d220485cab4c954be5c3 ts=2026-09-23T13:20:31.7330000Z == 6aa413b141b41dbac0c7f1ed.jsonl[298] _id=6ab3d220485cab4c954be5ca ts=2026-09-23T13:20:31.7330000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[303] _id=6ab3d220485cab4c954be5d8 ts=2026-09-23T13:20:31.7360000Z == 6aa413b141b41dbac0c7f1ed.jsonl[309] _id=6ab3d220485cab4c954be5de ts=2026-09-23T13:20:31.7360000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[18578] _id=6ac39ee0de269131f9a83dfe ts=2026-10-05T12:58:08.3670000Z == 6aa413b141b41dbac0c7f1ed.jsonl[18567] _id=6ac39ee0de269131f9a83e00 ts=2026-10-05T12:58:08.3670000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 323 group(s), 484 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[1429] _id=6ab3d67e485cab4c954ca68d ts=2026-09-23T13:39:08.2670000Z == 6aa413b141b41dbac0c7f1ed.jsonl[1423] _id=6ab3d67e485cab4c954ca697 ts=2026-09-23T13:39:08.2670000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1405] _id=6ab3d67e485cab4c954ca699 ts=2026-09-23T13:39:08.3020000Z == 6aa413b141b41dbac0c7f1ed.jsonl[1433] _id=6ab3d67e485cab4c954ca69b ts=2026-09-23T13:39:08.3020000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1329] _id=6ab3d68d485cab4c954ca885 ts=2026-09-23T13:39:24.1240000Z == 6aa413b141b41dbac0c7f1ed.jsonl[1459] _id=6ab3d68e485cab4c954ca887 ts=2026-09-23T13:39:24.1240000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 18 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa413b141b41dbac0c7f1ed.jsonl[111] _id=6ab3d05e485cab4c954b9662 ts=2026-09-23T13:13:02.3800000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[109] _id=6ab3d05e485cab4c954b966b ts=2026-09-23T13:13:02.3850000Z`; `809ms: 6aa413b141b41dbac0c7f1ed.jsonl[2161] _id=6ab51d94485cab4c954fc277 ts=2026-09-24T12:54:44.4710000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[2070] _id=6ab51d95485cab4c954fc283 ts=2026-09-24T12:54:45.2800000Z`; `785ms: 6aa413b141b41dbac0c7f1ed.jsonl[2070] _id=6ab51d95485cab4c954fc283 ts=2026-09-24T12:54:45.2800000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[2164] _id=6ab51d96485cab4c954fc291 ts=2026-09-24T12:54:46.0650000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 979 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa413b141b41dbac0c7f1ed.jsonl[1401] _id=6ab3d67b485cab4c954ca5eb ts=2026-09-23T13:39:07.5590000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[1397] _id=6ab3d67b485cab4c954ca5ef ts=2026-09-23T13:39:07.5670000Z`; `26ms: 6aa413b141b41dbac0c7f1ed.jsonl[1415] _id=6ab3d67d485cab4c954ca66f ts=2026-09-23T13:39:08.1740000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[1416] _id=6ab3d67d485cab4c954ca675 ts=2026-09-23T13:39:08.2000000Z`; `10ms: 6aa413b141b41dbac0c7f1ed.jsonl[1427] _id=6ab3d67e485cab4c954ca683 ts=2026-09-23T13:39:08.2290000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[1421] _id=6ab3d67e485cab4c954ca689 ts=2026-09-23T13:39:08.2390000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `766ms: 6aa413b141b41dbac0c7f1ed.jsonl[4713] _id=6ab524f8485cab4c9550e701 ts=2026-09-24T13:26:16.7670000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[4715] _id=6ab524f9485cab4c9550e723 ts=2026-09-24T13:26:17.5330000Z`; `551ms: 6aa413b141b41dbac0c7f1ed.jsonl[4718] _id=6ab524f9485cab4c9550e711 ts=2026-09-24T13:26:17.2050000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[4716] _id=6ab524f9485cab4c9550e729 ts=2026-09-24T13:26:17.7560000Z`; `644ms: 6aa413b141b41dbac0c7f1ed.jsonl[4726] _id=6ab524fb485cab4c9550e7c3 ts=2026-09-24T13:26:19.7250000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[4724] _id=6ab524fc485cab4c9550e7d7 ts=2026-09-24T13:26:20.3690000Z`
- **INFO / Info** `SolarStillDesignEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `970ms: 6aa413b141b41dbac0c7f1ed.jsonl[20588] _id=6ac3a86cde269131f9a9867f ts=2026-10-05T13:38:52.5450000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[20593] _id=6ac3a86dde269131f9a986a6 ts=2026-10-05T13:38:53.5150000Z`; `910ms: 6aa413b141b41dbac0c7f1ed.jsonl[20597] _id=6ac3a873de269131f9a9877f ts=2026-10-05T13:38:59.0760000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[20583] _id=6ac3a874de269131f9a987a3 ts=2026-10-05T13:38:59.9860000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6aa413b141b41dbac0c7f1ed.jsonl[3467] _id=6ab5208d485cab4c955019b1 ts=2026-09-24T13:07:25.3230000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[3475] _id=6ab5208d485cab4c955019bd ts=2026-09-24T13:07:25.3420000Z`; `279ms: 6aa413b141b41dbac0c7f1ed.jsonl[3463] _id=6ab52090485cab4c955019e9 ts=2026-09-24T13:07:28.8770000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[3464] _id=6ab52091485cab4c955019ef ts=2026-09-24T13:07:29.1560000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `688ms: 6aa413b141b41dbac0c7f1ed.jsonl[19883] _id=6ac3a36dde269131f9a88dfe ts=2026-10-05T13:17:33.7530000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[19795] _id=6ac3a36ede269131f9a88e1c ts=2026-10-05T13:17:34.4410000Z`; `490ms: 6aa413b141b41dbac0c7f1ed.jsonl[19885] _id=6ac3a36ede269131f9a88e0e ts=2026-10-05T13:17:34.2040000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[19874] _id=6ac3a36ede269131f9a88e28 ts=2026-10-05T13:17:34.6940000Z`; `781ms: 6aa413b141b41dbac0c7f1ed.jsonl[19795] _id=6ac3a36ede269131f9a88e1c ts=2026-10-05T13:17:34.4410000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[19876] _id=6ac3a36fde269131f9a88e3c ts=2026-10-05T13:17:35.2220000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa413b141b41dbac0c7f1ed.jsonl[9768] _id=6aba6e8d485cab4c956819b3 ts=2026-09-28T13:41:33.7010000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[9765] _id=6aba6e8e485cab4c956819bb ts=2026-09-28T13:41:33.7240000Z`; `24ms: 6aa413b141b41dbac0c7f1ed.jsonl[11442] _id=6abbbd35485cab4c957d179c ts=2026-09-29T13:29:25.4200000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[11441] _id=6abbbd35485cab4c957d17ad ts=2026-09-29T13:29:25.4440000Z`; `28ms: 6aa413b141b41dbac0c7f1ed.jsonl[18253] _id=6abe60e0485cab4c95a5e500 ts=2026-10-01T13:32:16.4510000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[18254] _id=6abe60e0485cab4c95a5e518 ts=2026-10-01T13:32:16.4790000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 136 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `323ms: 6aa413b141b41dbac0c7f1ed.jsonl[665] _id=6ab3d3c9485cab4c954c2a36 ts=2026-09-23T13:27:37.9670000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[658] _id=6ab3d3ca485cab4c954c2a50 ts=2026-09-23T13:27:38.2900000Z`; `765ms: 6aa413b141b41dbac0c7f1ed.jsonl[661] _id=6ab3d3c9485cab4c954c2a3b ts=2026-09-23T13:27:37.9970000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[662] _id=6ab3d3ca485cab4c954c2a76 ts=2026-09-23T13:27:38.7620000Z`; `26ms: 6aa413b141b41dbac0c7f1ed.jsonl[692] _id=6ab3d3f9485cab4c954c35a1 ts=2026-09-23T13:28:25.9850000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[690] _id=6ab3d3fa485cab4c954c35a5 ts=2026-09-23T13:28:26.0110000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `819ms: 6aa413b141b41dbac0c7f1ed.jsonl[747] _id=6ab3d478485cab4c954c5359 ts=2026-09-23T13:30:32.1600000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[749] _id=6ab3d478485cab4c954c538b ts=2026-09-23T13:30:32.9790000Z`; `620ms: 6aa413b141b41dbac0c7f1ed.jsonl[749] _id=6ab3d478485cab4c954c538b ts=2026-09-23T13:30:32.9790000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[753] _id=6ab3d479485cab4c954c53af ts=2026-09-23T13:30:33.5990000Z`; `588ms: 6aa413b141b41dbac0c7f1ed.jsonl[748] _id=6ab3d479485cab4c954c53ab ts=2026-09-23T13:30:33.4980000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[750] _id=6ab3d47a485cab4c954c53cd ts=2026-09-23T13:30:34.0860000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa413b141b41dbac0c7f1ed.jsonl[5452] _id=6ab67043485cab4c955453ed ts=2026-09-25T12:59:46.7880000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[5439] _id=6ab67043485cab4c955453ef ts=2026-09-25T12:59:46.7920000Z`; `6ms: 6aa413b141b41dbac0c7f1ed.jsonl[18548] _id=6ac39ec7de269131f9a83d86 ts=2026-10-05T12:57:39.4210000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[18556] _id=6ac39ec7de269131f9a83d8a ts=2026-10-05T12:57:39.4270000Z`; `2ms: 6aa413b141b41dbac0c7f1ed.jsonl[20470] _id=6ac3a71ade269131f9a94a55 ts=2026-10-05T13:33:14.5580000Z ~ 6aa413b141b41dbac0c7f1ed.jsonl[20469] _id=6ac3a71ade269131f9a94a57 ts=2026-10-05T13:33:14.5600000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa413b141b41dbac0c7f1ed.jsonl[18275] _id=6abe610f485cab4c95a5f2f8 ts=2026-10-01T13:33:03.1220000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18536] _id=6ac39ebede269131f9a83d48 ts=2026-10-05T12:57:34.5720000Z; 71h 57m: 6aa413b141b41dbac0c7f1ed.jsonl[5450] _id=6ab67041485cab4c955453e5 ts=2026-09-25T12:59:45.7700000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7448] _id=6aba641d485cab4c956795b1 ts=2026-09-28T12:57:01.2200000Z; 24h 9m: 6aa413b141b41dbac0c7f1ed.jsonl[1538] _id=6ab51c7c485cab4c954fbb53 ts=2026-09-24T12:50:04.9100000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[5450] _id=6ab67041485cab4c955453e5 ts=2026-09-25T12:59:45.7700000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 35m 
  - Evidence: 23h 35m: 6aa413b141b41dbac0c7f1ed.jsonl[1489] _id=6ab3d6d4485cab4c954caf99 ts=2026-09-23T13:40:36.4730000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[4020] _id=6ab52295485cab4c95506049 ts=2026-09-24T13:16:05.0340000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6aa413b141b41dbac0c7f1ed.jsonl[1484] _id=6ab3d6d4485cab4c954caf97 ts=2026-09-23T13:40:36.4680000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[1489] _id=6ab3d6d4485cab4c954caf99 ts=2026-09-23T13:40:36.4730000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa413b141b41dbac0c7f1ed.jsonl[18511] _id=6abe62e6485cab4c95a67c05 ts=2026-10-01T13:40:54.2060000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18571] _id=6ac39ee4de269131f9a83e10 ts=2026-10-05T12:58:12.9720000Z; 71h 22m: 6aa413b141b41dbac0c7f1ed.jsonl[7426] _id=6ab67851485cab4c9555251f ts=2026-09-25T13:34:10.0010000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7450] _id=6aba6423485cab4c956795bd ts=2026-09-28T12:57:06.7180000Z; 23h 29m: 6aa413b141b41dbac0c7f1ed.jsonl[11587] _id=6abbbd8b485cab4c957d2995 ts=2026-09-29T13:30:51.0220000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12109] _id=6abd07f4485cab4c95867aaf ts=2026-09-30T13:00:36.7410000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 629 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1ed.jsonl[11335] _id=6abbbd0b485cab4c957d0dc0 ts=2026-09-29T13:28:43.4140000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[11336] _id=6abbbd0b485cab4c957d0dc9 ts=2026-09-29T13:28:43.4150000Z; 1ms: 6aa413b141b41dbac0c7f1ed.jsonl[11379] _id=6abbbcf0485cab4c957d07dd ts=2026-09-29T13:28:16.6380000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[11374] _id=6abbbcf0485cab4c957d07e5 ts=2026-09-29T13:28:16.6390000Z; 1ms: 6aa413b141b41dbac0c7f1ed.jsonl[11397] _id=6abbbcfa485cab4c957d0a14 ts=2026-09-29T13:28:26.6340000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[11394] _id=6abbbcfa485cab4c957d0a16 ts=2026-09-29T13:28:26.6350000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 54m 
  - Evidence: 167h 54m: 6aa413b141b41dbac0c7f1ed.jsonl[970] _id=6ab3d530485cab4c954c76eb ts=2026-09-23T13:33:36.6860000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[14054] _id=6abd0e84485cab4c9587e238 ts=2026-09-30T13:28:36.1590000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa413b141b41dbac0c7f1ed.jsonl[18512] _id=6abe62e5485cab4c95a67be4 ts=2026-10-01T13:40:53.4890000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18525] _id=6ac39ec5de269131f9a83d5a ts=2026-10-05T12:57:39.1950000Z; 71h 25m: 6aa413b141b41dbac0c7f1ed.jsonl[7427] _id=6ab67850485cab4c955524de ts=2026-09-25T13:34:08.5130000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7460] _id=6aba64c9485cab4c95679637 ts=2026-09-28T12:59:53.9600000Z; 23h 30m: 6aa413b141b41dbac0c7f1ed.jsonl[9443] _id=6aba6c76485cab4c956804cf ts=2026-09-28T13:32:38.7810000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9811] _id=6abbb708485cab4c957c1a62 ts=2026-09-29T13:03:04.4610000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1312 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ed.jsonl[12466] _id=6abd0863485cab4c95868485 ts=2026-09-30T13:02:26.7030000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12461] _id=6abd0863485cab4c95868487 ts=2026-09-30T13:02:26.7030000Z; 0ms: 6aa413b141b41dbac0c7f1ed.jsonl[18578] _id=6ac39ee0de269131f9a83dfe ts=2026-10-05T12:58:08.3670000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18567] _id=6ac39ee0de269131f9a83e00 ts=2026-10-05T12:58:08.3670000Z; 0ms: 6aa413b141b41dbac0c7f1ed.jsonl[303] _id=6ab3d220485cab4c954be5d8 ts=2026-09-23T13:20:31.7360000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[309] _id=6ab3d220485cab4c954be5de ts=2026-09-23T13:20:31.7360000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa413b141b41dbac0c7f1ed.jsonl[18444] _id=6abe623a485cab4c95a64892 ts=2026-10-01T13:38:02.5140000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18573] _id=6ac39ee5de269131f9a83e14 ts=2026-10-05T12:58:12.9870000Z; 71h 37m: 6aa413b141b41dbac0c7f1ed.jsonl[7423] _id=6ab67851485cab4c95552514 ts=2026-09-25T13:34:09.9800000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7815] _id=6aba6782485cab4c9567b3d9 ts=2026-09-28T13:11:30.4970000Z; 24h 1m: 6aa413b141b41dbac0c7f1ed.jsonl[5365] _id=6ab525ff485cab4c95511bcf ts=2026-09-24T13:30:37.6370000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7384] _id=6ab677e2485cab4c9555163e ts=2026-09-25T13:32:18.9850000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1ed.jsonl[17957] _id=6abe5fa5485cab4c95a58829 ts=2026-10-01T13:27:01.4540000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[17952] _id=6abe5fa5485cab4c95a58831 ts=2026-10-01T13:27:01.4560000Z; 2ms: 6aa413b141b41dbac0c7f1ed.jsonl[18024] _id=6abe5fe7485cab4c95a59a7f ts=2026-10-01T13:28:07.2990000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18025] _id=6abe5fe7485cab4c95a59a84 ts=2026-10-01T13:28:07.3010000Z; 5ms: 6aa413b141b41dbac0c7f1ed.jsonl[111] _id=6ab3d05e485cab4c954b9662 ts=2026-09-23T13:13:02.3800000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[109] _id=6ab3d05e485cab4c954b966b ts=2026-09-23T13:13:02.3850000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa413b141b41dbac0c7f1ed.jsonl[18499] _id=6abe62ef485cab4c95a67e3d ts=2026-10-01T13:41:03.1940000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18538] _id=6ac39ec5de269131f9a83d58 ts=2026-10-05T12:57:34.5780000Z; 71h 22m: 6aa413b141b41dbac0c7f1ed.jsonl[7431] _id=6ab6786e485cab4c95552844 ts=2026-09-25T13:34:38.5490000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7439] _id=6aba6423485cab4c956795b7 ts=2026-09-28T12:57:01.2270000Z; 23h 29m: 6aa413b141b41dbac0c7f1ed.jsonl[5413] _id=6ab52604485cab4c95511c9b ts=2026-09-24T13:30:43.0270000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[5437] _id=6ab67043485cab4c955453e7 ts=2026-09-25T12:59:45.7770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6aa413b141b41dbac0c7f1ed.jsonl[6574] _id=6ab6725f485cab4c955472b5 ts=2026-09-25T13:08:45.7100000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12470] _id=6abd0863485cab4c9586848f ts=2026-09-30T13:02:22.4790000Z; 95h 42m: 6aa413b141b41dbac0c7f1ed.jsonl[17516] _id=6abe5df5485cab4c95a4cbe6 ts=2026-10-01T13:19:46.6490000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18639] _id=6ac39fd3de269131f9a8442a ts=2026-10-05T13:02:10.4430000Z; 23h 29m: 6aa413b141b41dbac0c7f1ed.jsonl[5377] _id=6ab52606485cab4c95511cd1 ts=2026-09-24T13:30:46.2060000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[5453] _id=6ab67043485cab4c955453f1 ts=2026-09-25T12:59:46.6990000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3049 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ed.jsonl[12410] _id=6abd0867485cab4c9586850a ts=2026-09-30T13:02:28.1640000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12447] _id=6abd0867485cab4c9586850f ts=2026-09-30T13:02:28.1640000Z; 0ms: 6aa413b141b41dbac0c7f1ed.jsonl[12423] _id=6abd0865485cab4c958684c9 ts=2026-09-30T13:02:26.7200000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12491] _id=6abd0865485cab4c958684cb ts=2026-09-30T13:02:26.7200000Z; 0ms: 6aa413b141b41dbac0c7f1ed.jsonl[12457] _id=6abd0864485cab4c958684a7 ts=2026-09-30T13:02:23.3000000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12458] _id=6abd0864485cab4c958684ab ts=2026-09-30T13:02:23.3000000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 33m 
  - Evidence: 143h 33m: 6aa413b141b41dbac0c7f1ed.jsonl[4849] _id=6ab5255d485cab4c95510123 ts=2026-09-24T13:27:57.7280000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[12393] _id=6abd081e485cab4c95867dc1 ts=2026-09-30T13:01:18.0640000Z; 23h 23m: 6aa413b141b41dbac0c7f1ed.jsonl[14531] _id=6abd0fee485cab4c95888306 ts=2026-09-30T13:34:38.1000000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[15458] _id=6abe58c6485cab4c95a40549 ts=2026-10-01T12:57:42.3200000Z; 32m 37s: 6aa413b141b41dbac0c7f1ed.jsonl[12409] _id=6abd0838485cab4c95868106 ts=2026-09-30T13:01:44.0330000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[14432] _id=6abd0fdd485cab4c95887be1 ts=2026-09-30T13:34:21.4360000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 42m 
  - Evidence: 71h 42m: 6aa413b141b41dbac0c7f1ed.jsonl[7087] _id=6ab6765f485cab4c9554e256 ts=2026-09-25T13:25:51.4590000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7636] _id=6aba66d3485cab4c9567a725 ts=2026-09-28T13:08:35.1360000Z; 48h 6m: 6aa413b141b41dbac0c7f1ed.jsonl[7813] _id=6aba677d485cab4c9567b387 ts=2026-09-28T13:11:25.7660000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[13700] _id=6abd0c06485cab4c9586d591 ts=2026-09-30T13:17:58.2770000Z; 24h 4m: 6aa413b141b41dbac0c7f1ed.jsonl[4227] _id=6ab5230d485cab4c955073db ts=2026-09-24T13:18:05.6600000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[6847] _id=6ab67586485cab4c9554c06c ts=2026-09-25T13:22:14.7880000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.015s..0.019s shown 
  - Evidence: 15ms: 6aa413b141b41dbac0c7f1ed.jsonl[3472] _id=6ab5208d485cab4c955019af ts=2026-09-24T13:07:25.3080000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[3467] _id=6ab5208d485cab4c955019b1 ts=2026-09-24T13:07:25.3230000Z; 19ms: 6aa413b141b41dbac0c7f1ed.jsonl[3467] _id=6ab5208d485cab4c955019b1 ts=2026-09-24T13:07:25.3230000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[3475] _id=6ab5208d485cab4c955019bd ts=2026-09-24T13:07:25.3420000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 7m 
  - Evidence: 120h 7m: 6aa413b141b41dbac0c7f1ed.jsonl[772] _id=6ab3d48e485cab4c954c58a3 ts=2026-09-23T13:30:54.1620000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9567] _id=6aba6de6485cab4c9568135b ts=2026-09-28T13:38:46.4900000Z; 95h 57m: 6aa413b141b41dbac0c7f1ed.jsonl[18256] _id=6abe60e0485cab4c95a5e4f8 ts=2026-10-01T13:32:16.4420000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20332] _id=6ac3a664de269131f9a92abd ts=2026-10-05T13:30:12.2450000Z; 48h 1m: 6aa413b141b41dbac0c7f1ed.jsonl[11440] _id=6abbbd35485cab4c957d179a ts=2026-09-29T13:29:25.4070000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18095] _id=6abe6089485cab4c95a5c891 ts=2026-10-01T13:30:49.3230000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 7m 
  - Evidence: 120h 7m: 6aa413b141b41dbac0c7f1ed.jsonl[775] _id=6ab3d48e485cab4c954c58ab ts=2026-09-23T13:30:54.1840000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9530] _id=6aba6dc7485cab4c95681189 ts=2026-09-28T13:38:15.6990000Z; 95h 57m: 6aa413b141b41dbac0c7f1ed.jsonl[18254] _id=6abe60e0485cab4c95a5e518 ts=2026-10-01T13:32:16.4790000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20297] _id=6ac3a654de269131f9a9276c ts=2026-10-05T13:29:56.4070000Z; 48h 0m: 6aa413b141b41dbac0c7f1ed.jsonl[11441] _id=6abbbd35485cab4c957d17ad ts=2026-09-29T13:29:25.4440000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18099] _id=6abe605f485cab4c95a5bbe6 ts=2026-10-01T13:30:07.1410000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.023s..0.028s shown 
  - Evidence: 23ms: 6aa413b141b41dbac0c7f1ed.jsonl[9768] _id=6aba6e8d485cab4c956819b3 ts=2026-09-28T13:41:33.7010000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9765] _id=6aba6e8e485cab4c956819bb ts=2026-09-28T13:41:33.7240000Z; 24ms: 6aa413b141b41dbac0c7f1ed.jsonl[11442] _id=6abbbd35485cab4c957d179c ts=2026-09-29T13:29:25.4200000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[11441] _id=6abbbd35485cab4c957d17ad ts=2026-09-29T13:29:25.4440000Z; 28ms: 6aa413b141b41dbac0c7f1ed.jsonl[18253] _id=6abe60e0485cab4c95a5e500 ts=2026-10-01T13:32:16.4510000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18254] _id=6abe60e0485cab4c95a5e518 ts=2026-10-01T13:32:16.4790000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 7m 
  - Evidence: 120h 7m: 6aa413b141b41dbac0c7f1ed.jsonl[768] _id=6ab3d489485cab4c954c5768 ts=2026-09-23T13:30:49.1970000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9505] _id=6aba6dc5485cab4c9568116f ts=2026-09-28T13:38:13.7580000Z; 95h 57m: 6aa413b141b41dbac0c7f1ed.jsonl[18257] _id=6abe60df485cab4c95a5e48e ts=2026-10-01T13:32:15.4650000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20300] _id=6ac3a656de269131f9a927cb ts=2026-10-05T13:29:57.9780000Z; 48h 0m: 6aa413b141b41dbac0c7f1ed.jsonl[11439] _id=6abbbd31485cab4c957d16b2 ts=2026-09-29T13:29:21.8000000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18088] _id=6abe605e485cab4c95a5bb71 ts=2026-10-01T13:30:05.8130000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 136 interval(s) ≤ 0.004s..0.016s shown 
  - Evidence: 4ms: 6aa413b141b41dbac0c7f1ed.jsonl[9625] _id=6aba6e03485cab4c956814a9 ts=2026-09-28T13:39:15.1940000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9626] _id=6aba6e03485cab4c956814ad ts=2026-09-28T13:39:15.1980000Z; 16ms: 6aa413b141b41dbac0c7f1ed.jsonl[18048] _id=6abe605f485cab4c95a5bbce ts=2026-10-01T13:30:06.4440000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18053] _id=6abe605f485cab4c95a5bbd7 ts=2026-10-01T13:30:06.4600000Z; 16ms: 6aa413b141b41dbac0c7f1ed.jsonl[18088] _id=6abe605e485cab4c95a5bb71 ts=2026-10-01T13:30:05.8130000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18093] _id=6abe605e485cab4c95a5bb8e ts=2026-10-01T13:30:05.8290000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 34m 
  - Evidence: 23h 34m: 6aa413b141b41dbac0c7f1ed.jsonl[20062] _id=6ac3a3eede269131f9a8a0ce ts=2026-10-05T13:19:42.7000000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20719] _id=6ac4ef5dde269131f9affad9 ts=2026-10-06T12:53:49.5480000Z; 17m 37s: 6aa413b141b41dbac0c7f1ed.jsonl[18635] _id=6ac39fcdde269131f9a84404 ts=2026-10-05T13:02:05.0630000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20062] _id=6ac3a3eede269131f9a8a0ce ts=2026-10-05T13:19:42.7000000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa413b141b41dbac0c7f1ed.jsonl[15278] _id=6abe5826485cab4c95a3fea5 ts=2026-10-01T12:55:02.0120000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18535] _id=6ac39eb6de269131f9a83d38 ts=2026-10-05T12:57:26.4230000Z; 71h 57m: 6aa413b141b41dbac0c7f1ed.jsonl[5436] _id=6ab67022485cab4c955453d1 ts=2026-09-25T12:59:14.1500000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7438] _id=6aba6404485cab4c956795a7 ts=2026-09-28T12:56:36.0450000Z; 24h 9m: 6aa413b141b41dbac0c7f1ed.jsonl[1509] _id=6ab51c77485cab4c954fbb51 ts=2026-09-24T12:49:58.9490000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[5436] _id=6ab67022485cab4c955453d1 ts=2026-09-25T12:59:14.1500000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa413b141b41dbac0c7f1ed.jsonl[15283] _id=6abe5826485cab4c95a3fe9f ts=2026-10-01T12:55:02.0100000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18537] _id=6ac39eb6de269131f9a83d36 ts=2026-10-05T12:57:26.4220000Z; 71h 57m: 6aa413b141b41dbac0c7f1ed.jsonl[1491] _id=6ab67022485cab4c955453cf ts=2026-09-25T12:59:14.1490000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7447] _id=6aba6404485cab4c956795a5 ts=2026-09-28T12:56:36.0430000Z; 23h 58m: 6aa413b141b41dbac0c7f1ed.jsonl[7522] _id=6aba65dd485cab4c9567a095 ts=2026-09-28T13:04:29.0660000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[9798] _id=6abbb6f2485cab4c957c19d8 ts=2026-09-29T13:02:42.5870000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 50m 
  - Evidence: 143h 50m: 6aa413b141b41dbac0c7f1ed.jsonl[10877] _id=6abbb9f3485cab4c957c5e30 ts=2026-09-29T13:15:31.3790000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[19253] _id=6ac3a0d6de269131f9a85618 ts=2026-10-05T13:06:30.1810000Z; 119h 43m: 6aa413b141b41dbac0c7f1ed.jsonl[4860] _id=6ab5256a485cab4c9551038f ts=2026-09-24T13:28:10.5050000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[10438] _id=6abbb927485cab4c957c4264 ts=2026-09-29T13:12:07.4700000Z; 23h 47m: 6aa413b141b41dbac0c7f1ed.jsonl[19253] _id=6ac3a0d6de269131f9a85618 ts=2026-10-05T13:06:30.1810000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20745] _id=6ac4ef77de269131f9affb35 ts=2026-10-06T12:54:15.0900000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1ed.jsonl[18484] _id=6abe6292485cab4c95a66638 ts=2026-10-01T13:39:30.2020000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[18548] _id=6ac39ec7de269131f9a83d86 ts=2026-10-05T12:57:39.4210000Z; 71h 43m: 6aa413b141b41dbac0c7f1ed.jsonl[6730] _id=6ab6737b485cab4c95548963 ts=2026-09-25T13:13:31.2920000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[7440] _id=6aba6423485cab4c956795bb ts=2026-09-28T12:57:06.7100000Z; 23h 33m: 6aa413b141b41dbac0c7f1ed.jsonl[4674] _id=6ab524e6485cab4c9550e2a5 ts=2026-09-24T13:25:58.3030000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[5452] _id=6ab67043485cab4c955453ed ts=2026-09-25T12:59:46.7880000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1ed.jsonl[19388] _id=6ac3a17dde269131f9a85e1e ts=2026-10-05T13:09:17.5210000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[19400] _id=6ac3a17dde269131f9a85e20 ts=2026-10-05T13:09:17.5230000Z; 2ms: 6aa413b141b41dbac0c7f1ed.jsonl[19530] _id=6ac3a220de269131f9a868ac ts=2026-10-05T13:12:00.4790000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[19527] _id=6ac3a220de269131f9a868ae ts=2026-10-05T13:12:00.4810000Z; 2ms: 6aa413b141b41dbac0c7f1ed.jsonl[20470] _id=6ac3a71ade269131f9a94a55 ts=2026-10-05T13:33:14.5580000Z -> 6aa413b141b41dbac0c7f1ed.jsonl[20469] _id=6ac3a71ade269131f9a94a57 ts=2026-10-05T13:33:14.5600000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[609] _id=6ab3d386485cab4c954c16c2 ts=2026-09-23T13:26:30.2850000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[779] _id=6ab3d4a1485cab4c954c5ddd ts=2026-09-23T13:31:13.3000000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[4038] _id=6ab5229d485cab4c95506181 ts=2026-09-24T13:16:13.5880000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 217 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[2183] _id=6ab51d99485cab4c954fc2c7 ts=2026-09-24T12:54:48.6540000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[2261] _id=6ab51dae485cab4c954fc53b ts=2026-09-24T12:55:09.8300000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[2250] _id=6ab51daf485cab4c954fc54b ts=2026-09-24T12:55:09.8940000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 520 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[1423] _id=6ab3d67e485cab4c954ca697 ts=2026-09-23T13:39:08.2670000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1405] _id=6ab3d67e485cab4c954ca699 ts=2026-09-23T13:39:08.3020000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1433] _id=6ab3d67e485cab4c954ca69b ts=2026-09-23T13:39:08.3020000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[9765] _id=6aba6e8e485cab4c956819bb ts=2026-09-28T13:41:33.7240000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[11441] _id=6abbbd35485cab4c957d17ad ts=2026-09-29T13:29:25.4440000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[18254] _id=6abe60e0485cab4c95a5e518 ts=2026-10-01T13:32:16.4790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 23 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[690] _id=6ab3d3fa485cab4c954c35a5 ts=2026-09-23T13:28:26.0110000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[699] _id=6ab3d401485cab4c954c37a7 ts=2026-09-23T13:28:33.5000000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[702] _id=6ab3d406485cab4c954c38c8 ts=2026-09-23T13:28:38.1520000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[18635] _id=6ac39fcdde269131f9a84404 ts=2026-10-05T13:02:05.0630000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[20062] _id=6ac3a3eede269131f9a8a0ce ts=2026-10-05T13:19:42.7000000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[20719] _id=6ac4ef5dde269131f9affad9 ts=2026-10-06T12:53:49.5480000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[12445] _id=6abd085a485cab4c9586840d ts=2026-09-30T13:02:18.6090000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[16042] _id=6abe59bf485cab4c95a41afb ts=2026-10-01T13:01:51.3870000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[8] _id=6ab3ce8a485cab4c954b84e6 ts=?`; `6aa413b141b41dbac0c7f1ed.jsonl[7449] _id=6aba6423485cab4c956795b9 ts=?`; `6aa413b141b41dbac0c7f1ed.jsonl[20700] _id=6ac4ef66de269131f9affadd ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 730 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[2103] _id=6ab51d94485cab4c954fc271 ts=2026-09-24T12:54:43.0690000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[2197] _id=6ab51da7485cab4c954fc409 ts=2026-09-24T12:55:02.3200000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[2198] _id=6ab51da7485cab4c954fc40d ts=2026-09-24T12:55:02.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 779 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[1401] _id=6ab3d67b485cab4c954ca5eb ts=2026-09-23T13:39:07.5590000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1397] _id=6ab3d67b485cab4c954ca5ef ts=2026-09-23T13:39:07.5670000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1389] _id=6ab3d67d485cab4c954ca631 ts=2026-09-23T13:39:07.8660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 25 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[3467] _id=6ab5208d485cab4c955019b1 ts=2026-09-24T13:07:25.3230000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[3475] _id=6ab5208d485cab4c955019bd ts=2026-09-24T13:07:25.3420000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[3596] _id=6ab5215f485cab4c955024eb ts=2026-09-24T13:10:55.7650000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 37 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[11358] _id=6abbbcea485cab4c957d061f ts=2026-09-29T13:28:10.0880000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[18104] _id=6abe6063485cab4c95a5bd2f ts=2026-10-01T13:30:11.7320000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[18126] _id=6abe606d485cab4c95a5bf77 ts=2026-10-01T13:30:21.0050000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[749] _id=6ab3d478485cab4c954c538b ts=2026-09-23T13:30:32.9790000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[753] _id=6ab3d479485cab4c954c53af ts=2026-09-23T13:30:33.5990000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[751] _id=6ab3d47a485cab4c954c53d3 ts=2026-09-23T13:30:34.1840000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 418 start, 411 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 296 unmatched 'BecameCameraCentered' (totals: 931 open, 852 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 163 unmatched 'BecameVisible' (totals: 1141 open, 1498 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 29 open, 27 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationNodeHoverStart' (totals: 234 open, 252 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 49 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 732 of 20938 adjacent _id pairs reverse in client time; worst 109.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1ed.jsonl[1891] _id=6ab51d7b485cab4c954fbfc9 ts=2026-09-24T12:54:19.0730000Z`; `6aa413b141b41dbac0c7f1ed.jsonl[1892] _id=6ab51d7c485cab4c954fbfcd ts=2026-09-24T12:52:29.5680000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -113.57s, max +0.40s over 20939 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1ed\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 11214 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (3844); Unit 2 Prod (Refactor) (2828); Unit 4 Dev - Dungeon (1185); Unit 4 Dev (951); Unit 3 Dungeon Dev (734); Unit 5 Dev - Dungeon (658); Unit 1 Dev (513); Unit 5 Dev (382); Unit 4 Dev - Anderson Base (119)
- **Intervals:** median 0.25s (p5 0.02s / p95 2.06s, n=11213)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 11214/11214 records)
    "pressed"  x11214
data.actionType  (string, 11214/11214 records)
    "Move"  x9465
    "Jump"  x854
    "Interact"  x748
    "Ascend"  x68
    "Hoverboard"  x50
    "Map"  x18
    "Pause"  x4
    "Sprint"  x4
    "SkipCinematic"  x2
    "ToggleDebug"  x1
data.key  (string, 11214/11214 records, 4 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 11214/11214 records)
    "Player"  x9373
    "Drone"  x1841
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4422 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2514); Unit 4 Dev (1174); Unit 5 Dev - Dungeon (496); Unit 3 Dungeon Dev (238)
- **Intervals:** median 0.02s (p5 0.00s / p95 0.71s, n=4421)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4422/4422 records)
    "BecameInvisible"  x1498
    "BecameVisible"  x1141
    "BecameCameraCentered"  x931
    "BecameCameraUncentered"  x852
data.pieceId  (string, 4422/4422 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4422/4422 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2063 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (559); Unit 2 Prod (Refactor) (487); Unit 4 Dev (267); Unit 1 Dev (198); Unit 5 Dev (179); Unit 3 Dungeon Dev (117); Unit 4 Dev - Dungeon (91); Unit 4 Dev - Anderson Base (87); Unit 5 Dev - Dungeon (78)
- **eventKey:** present on 1234 of 2063 records
- **Intervals:** median 4.44s (p5 0.00s / p95 30.23s, n=2062)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1234; [conversationId, dialogueEventType] x829
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2063/2063 records)
    numeric range 8 .. 118 (53 unique)
data.dialogueEventType  (string, 2063/2063 records)
    "DialogueNodeEvent"  x1234
    "DialogueStartEvent"  x418
    "DialogueFinishEvent"  x411
data.nodeId  (number, 1234/2063 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1924 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (548); Unit 2 Prod (Refactor) (523); Unit 4 Dev (208); Unit 1 Dev (156); Unit 5 Dev (146); Unit 5 Dev - Dungeon (106); Unit 4 Dev - Dungeon (100); Unit 3 Dungeon Dev (85); Unit 4 Dev - Anderson Base (52)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.02s, n=1910)
- **Fields under `data`:**

```text
data.position  (object, 1924/1924 records)
data.position.x  (number, 1924/1924 records)
    numeric range -682.408 .. 1557.3 (628 unique)
data.position.y  (number, 1924/1924 records)
    numeric range -115.071 .. 222.005 (484 unique)
data.position.z  (number, 1924/1924 records)
    numeric range -1190.35 .. 1783.81 (628 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 551 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (270); Unit 4 Dev - Anderson Base (145); Unit 5 Dev (84); Unit 1 Dev (52)
- **Intervals:** median 0.29s (p5 0.02s / p95 4.53s, n=550)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 551/551 records)
    "argumentationNodeHoverEnd"  x252
    "argumentationNodeHoverStart"  x234
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x24
data.argumentationTitle  (string, 551/551 records)
    "Unit 3 - Pollution Upstream"  x270
    "Unit 4 - Flooding"  x145
    "Unit 5"  x84
    "Unit 1 - Argumentation Tutorial"  x33
    "Unit 1 - Freshwater"  x19
data.nodeName  (string, 551/551 records)
    "1"  x72
    "I"  x67
    "A"  x55
    "II"  x54
    "B"  x53
    "3"  x52
    "D"  x51
    "2"  x41
    "C"  x41
    "5"  x34
    "4"  x31
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 260 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (82); Unit 3 Dungeon Dev (43); Unit 2 Prod (Refactor) (42); Unit 4 Dev (26); Unit 5 Dev - Dungeon (19); Unit 3 Dev (15); Unit 1 Dev (12); Unit 5 Dev (12); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 6.28s (p5 0.57s / p95 472.16s, n=259)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 260/260 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 260/260 records)
    95 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 94 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (62); Unit 3 Dev (32)
- **Intervals:** median 2.96s (p5 0.33s / p95 417.44s, n=93)
- **`data` key-set variants:** [actionType, featureUsed] x56; [actionType, featureUsed, location] x37; [actionType, featureUsed, legendName] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 94/94 records)
    "WaypointMoveEvent"  x35
    "MapOpenEvent"  x29
    "MapCloseEvent"  x27
    "WaypointSetEvent"  x2
    "Selected"  x1
data.featureUsed  (string, 94/94 records)
    "Map"  x56
    "Waypoint"  x37
    "Legend"  x1
data.legendName  (string, 1/94 records)
    "240 ft"  x1
data.location  (object, 37/94 records)
data.location.x  (number, 37/94 records)
    numeric range -572.09 .. 67.9101 (31 unique)
data.location.y  (number, 37/94 records)
    numeric range -214.5 .. 147.5 (31 unique)
data.location.z  (number, 37/94 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (18); Unit 2 Prod (Refactor) (14); Unit 1 Dev (12); Unit 4 Dev (10); Unit 4 Dev - Dungeon (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 212.07s (p5 0.00s / p95 84197.95s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x32
data.questID  (string, 81/81 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/81 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 65 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (65)
- **Intervals:** median 2.31s (p5 0.35s / p95 64.26s, n=64)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 65/65 records)
    "On"  x35
    "Off"  x30
data.floor  (string, 65/65 records)
    "4"  x43
    "3"  x12
    "2"  x7
    "1"  x3
data.machineNumber  (string, 65/65 records)
    "One"  x62
    "Two"  x3
data.machineType  (string, 65/65 records)
    "Condenser"  x38
    "Evaporator"  x23
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
    "DualChamber_Evaporator"  x1
data.room  (string, 65/65 records)
    "3"  x36
    "2"  x18
    "4"  x6
    "1"  x5
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Soil Key Puzzle` — 64 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 3 Dev (16); Unit 4 Dev (16)
- **Intervals:** median 0.86s (p5 0.17s / p95 76.67s, n=63)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x56; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/64 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/64 records)
    "Unit 4 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
data.actionType  (string, 56/64 records)
    "RightDrag"  x29
    "LeftDrag"  x27
data.currentSoilType  (string, 56/64 records)
    "SAND"  x14
    "CLAYSAND"  x13
    "CLAY"  x11
    "SANDGRAVEL"  x8
    "CLAYROCK"  x7
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 56/64 records)
    "false"  x40
    "true"  x16
data.waterLevelStatus  (string, 56/64 records)
    "Proper"  x24
    "TooHigh"  x24
    "TooLow"  x8
data.waterRetentionChange  (string, 56/64 records)
    "Increase"  x22
    "Decrease"  x18
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `SolarStillDesignEvent` — 52 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (52)
- **Intervals:** median 1.28s (p5 0.45s / p95 3.41s, n=51)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x51; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "optionSelected"  x51
    "DesignSubmitted"  x1
data.designSelections  (object, 1/52 records)
data.designSelections.glassRoofTemperature  (string, 1/52 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/52 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/52 records)
    "Tilted Out"  x1
data.featureUsed  (string, 52/52 records)
    "GlassRoofTemperature"  x32
    "RoofStyle"  x12
    "ExtraCovering"  x7
    "Submit"  x1
data.selectedOption  (string, 51/52 records, 18 empty-string)
    ""  x18
    "Cold"  x10
    "Hot"  x8
    "Tilted Out"  x5
    "Covered"  x4
    "Flat"  x3
    "Tilted In"  x2
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationAnswerEvent` — 26 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (14); Unit 5 Dev (5); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (3)
- **Intervals:** median 21.12s (p5 4.23s / p95 310957.43s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "submitAnswerEvent"  x26
data.answerSubmitted  (string, 26/26 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 26/26 records)
    "Unit 3 - Pollution Upstream"  x14
    "Unit 5"  x5
    "Unit 4 - Flooding"  x4
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 22 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev (5); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 797.74s (p5 168.30s / p95 259035.45s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "DebugMenuStateChanged"  x22
data.isOpened  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 22 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 3 Dev (2); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1631.45s (p5 48.82s / p95 259041.89s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 83698.84s (p5 162.67s / p95 285052.65s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 98.80s (p5 0.02s / p95 375903.48s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 15/15 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 9 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (9)
- **Intervals:** median 2.71s (p5 0.39s / p95 55302.80s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "Open"  x5
    "Close"  x4
data.toolName  (string, 9/9 records, 8 empty-string)
    ""  x8
    "Settings"  x1
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 1.43s (p5 0.50s / p95 23.23s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 6 empty-string)
    ""  x6
    "cameraPlaced"  x3
data.boxId  (string, 9/9 records)
    "0"  x5
    "1"  x2
    "2"  x2
data.soilType  (string, 9/9 records)
    "Gravel"  x4
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9)
- **Intervals:** median 0.50s (p5 0.10s / p95 87.03s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 9 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (9)
- **Intervals:** median 30.06s (p5 3.16s / p95 130.89s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "ChangeCanister"  x9
data.canisterType  (string, 9/9 records)
    "Clay"  x4
    "Bedrock"  x2
    "Sand"  x2
    "Gravel"  x1
data.floor  (string, 9/9 records)
    "5"  x8
    "4"  x1
data.machine  (string, 9/9 records)
    "1"  x7
    "2"  x2
data.row  (string, 9/9 records)
    "TopRow"  x6
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 7 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 85654.50s (p5 211.23s / p95 496153.34s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    false  x7
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 42952.24s (p5 5247.10s / p95 80657.39s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Permissions check failed"  x2
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 1 empty-string)
    "TypeError: Permissions check failed"  x2
    ""  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit1"  x1
    "unit2"  x1
    "unit5"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 604499.47s (p5 604499.47s / p95 604499.47s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
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

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (32 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (35x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (37x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (24x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*