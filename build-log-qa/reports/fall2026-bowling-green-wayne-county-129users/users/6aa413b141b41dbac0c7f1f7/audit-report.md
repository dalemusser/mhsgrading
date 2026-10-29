# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f7

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f7
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f7.jsonl
- **Records:** 13178 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f7
- **Time span:** 2026-09-23T13:04:12.223000+00:00 .. 2026-10-07T13:41:08.178000+00:00 (336h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f7\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 13178 records, 7 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 91 INFO, 2 NOT_TESTED, 73 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5022 | 38.11 | 1 | 3 | 0 | 2026-09-24T12:56:11.213000+00:00 | 2026-10-07T13:26:21.672000+00:00 | 312h 30m |
| InputEvent | 3840 | 29.14 | 1 | 6 | 0 | 2026-09-23T13:05:32.690000+00:00 | 2026-10-07T13:41:04.021000+00:00 | 336h 35m |
| PlayerPositionEvent | 1867 | 14.17 | 1 | 6 | 0 | 2026-09-23T13:05:13.161000+00:00 | 2026-10-07T13:41:08.178000+00:00 | 336h 35m |
| DialogueEvent | 1808 | 13.72 | 1 | 6 | 1098 | 2026-09-23T13:05:35.654000+00:00 | 2026-10-07T13:39:07.858000+00:00 | 336h 33m |
| ObjectInterEvent | 200 | 1.52 | 1 | 6 | 0 | 2026-09-23T13:10:30.919000+00:00 | 2026-10-07T13:41:04.016000+00:00 | 336h 30m |
| argumentationNodeEvent | 147 | 1.12 | 1 | 2 | 0 | 2026-09-23T13:30:12.702000+00:00 | 2026-10-01T13:26:14.791000+00:00 | 191h 56m |
| Soil Key Puzzle | 66 | 0.5 | 1 | 3 | 0 | 2026-09-24T13:07:49.468000+00:00 | 2026-10-07T13:24:36.779000+00:00 | 312h 16m |
| questEvent | 55 | 0.42 | 1 | 6 | 55 | 2026-09-23T13:05:35.629000+00:00 | 2026-10-07T13:38:15.113000+00:00 | 336h 32m |
| TopographicMapEvent | 50 | 0.38 | 1 | 2 | 0 | 2026-09-24T12:56:43.227000+00:00 | 2026-10-05T13:18:33.508000+00:00 | 264h 21m |
| gameWindowFocusEvent | 23 | 0.17 | 1 | 3 | 0 | 2026-09-23T13:04:12.223000+00:00 | 2026-10-07T13:21:11.210000+00:00 | 336h 16m |
| DEBUGMenu | 21 | 0.16 | 1 | 7 | 0 | 2026-09-23T13:05:13.154000+00:00 | 2026-10-07T13:26:35.405000+00:00 | 336h 21m |
| argumentationAnswerEvent | 20 | 0.15 | 1 | 2 | 0 | 2026-09-23T13:33:14.104000+00:00 | 2026-10-01T13:26:15.824000+00:00 | 191h 53m |
| DaniEvent | 18 | 0.14 | 1 | 2 | 0 | 2026-09-24T13:06:41.873000+00:00 | 2026-10-07T13:34:53.657000+00:00 | 312h 28m |
| gameStartEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-09-23T13:04:12.224000+00:00 | 2026-10-07T13:21:11.210000+00:00 | 336h 16m |
| gameWindowUnfocusEvent | 11 | 0.08 | 1 | 3 | 0 | 2026-09-23T13:40:28.369000+00:00 | 2026-10-05T13:19:38.720000+00:00 | 287h 39m |
| argumentationEvent | 7 | 0.05 | 1 | 2 | 0 | 2026-09-23T13:30:02.556000+00:00 | 2026-10-01T13:26:15.882000+00:00 | 191h 56m |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-23T13:36:57.472000+00:00 | 2026-10-05T13:29:17.877000+00:00 | 287h 52m |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-23T13:30:00.459000+00:00 | 2026-09-23T13:30:02.524000+00:00 | 2.1s |
| chatEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-24T13:24:57.785000+00:00 | 2026-09-24T13:25:05.393000+00:00 | 7.6s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1945.558s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 1036340.405s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.638s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.84s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 8.715s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.065s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 7.608s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 81649.535s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1051.43s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 41403.187s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 30 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,3,I; A,4,I; B,3,I; B,3,II; B,5,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D 
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
  - Observed: [21-11, 21-12, 21-92, 21-15, 18-231] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 48; 49; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 25 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[129] _id=6ab3d044485cab4c954b93a6 ts=2026-09-23T13:12:36.7600000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[196] _id=6ab3d197485cab4c954bd08e ts=2026-09-23T13:18:15.1830000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[241] _id=6ab3d24d485cab4c954bec32 ts=2026-09-23T13:21:17.7170000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[5613] _id=6aba64e3485cab4c956797c7 ts=2026-09-28T13:00:15.4930000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[5] _id=6ab3ce4c485cab4c954b8498 ts=2026-09-23T13:04:12.2240000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[575] _id=6ab3d66d485cab4c954ca439 ts=2026-09-23T13:38:53.8650000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[625] _id=6ab51caf485cab4c954fbbc9 ts=2026-09-24T12:50:54.9810000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[1] _id=6ab3ce4c485cab4c954b8496 ts=2026-09-23T13:04:12.2230000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[574] _id=6ab3d66d485cab4c954ca435 ts=2026-09-23T13:38:53.8640000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[624] _id=6ab51caf485cab4c954fbbc7 ts=2026-09-24T12:50:54.9800000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[612] _id=6ab3d6cc485cab4c954caef1 ts=2026-09-23T13:40:28.3690000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[629] _id=6ab51cd0485cab4c954fbbed ts=2026-09-24T12:51:28.9240000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[3287] _id=6ab520e4485cab4c95501d43 ts=2026-09-24T13:08:52.1070000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 8 of 50 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[775] _id=6ab51e0b485cab4c954fd0a7 ts=2026-09-24T12:56:43.2270000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[784] _id=6ab51e22485cab4c954fd478 ts=2026-09-24T12:57:06.3820000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[789] _id=6ab51e2d485cab4c954fd623 ts=2026-09-24T12:57:17.0090000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5021 | 0.0 | 0.031 | 224.061 | 1.02 | 343528.488 | 0.27 | 3043 | 7 |
| InputEvent | 3839 | 0.001 | 0.704 | 315.637 | 9.767 | 343300.826 | 0.19 | 170 | 12 |
| PlayerPositionEvent | 1858 | 9.279 | 10.0 | 559.662 | 10.029 | 343267.345 | 0.11 | 0 | 8 |
| DialogueEvent | 1807 | 0.001 | 4.188 | 670.51 | 38.385 | 343426.657 | 0.09 | 532 | 9 |
| ObjectInterEvent | 199 | 0.01 | 7.29 | 6087.604 | 470.312 | 343330.767 | 0.01 | 1 | 9 |
| argumentationNodeEvent | 146 | 0.021 | 0.368 | 4732.617 | 6.743 | 690527.462 | 0.01 | 31 | 1 |
| Soil Key Puzzle | 65 | 0.144 | 1.638 | 17295.497 | 69325.173 | 519365.261 | 0.0 | 0 | 4 |
| questEvent | 54 | 0.002 | 268.137 | 22436.287 | 115763.913 | 343895.673 | 0.0 | 5 | 17 |
| TopographicMapEvent | 49 | 0.695 | 8.84 | 19422.659 | 86501.683 | 430695.737 | 0.0 | 0 | 6 |
| gameWindowFocusEvent | 22 | 75.476 | 1051.43 | 55028.136 | 254957.895 | 345111.091 | 0.0 | 0 | 12 |
| DEBUGMenu | 20 | 8.431 | 1945.558 | 60544.113 | 263541.644 | 343903.068 | 0.0 | 0 | 13 |
| argumentationAnswerEvent | 19 | 0.556 | 8.715 | 36356.933 | 69110.467 | 690534.959 | 0.0 | 0 | 1 |
| DaniEvent | 17 | 0.002 | 1.936 | 66170.105 | 225613.133 | 1123762.602 | 0.0 | 2 | 2 |
| gameStartEvent | 15 | 75.477 | 81649.535 | 80707.932 | 285246.534 | 345769.31 | 0.0 | 0 | 11 |
| gameWindowUnfocusEvent | 10 | 12.007 | 41403.187 | 103555.035 | 395888.374 | 438073.822 | 0.0 | 0 | 8 |
| argumentationEvent | 6 | 0.036 | 88.523 | 115162.221 | 517953.86 | 690522.648 | 0.0 | 1 | 1 |
| EndOfUnit | 1 | 1036340.405 | 1036340.405 | 1036340.405 | 1036340.405 | 1036340.405 | 0.0 | 0 | 1 |
| argumentationToolEvent | 1 | 2.065 | 2.065 | 2.065 | 2.065 | 2.065 | 29.06 | 0 | 0 |
| chatEvent | 1 | 7.608 | 7.608 | 7.608 | 7.608 | 7.608 | 7.89 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 197 group(s), 260 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[857] _id=6ab51e58485cab4c954fdbcb ts=2026-09-24T12:56:26.4320000Z == 6aa413b141b41dbac0c7f1f7.jsonl[858] _id=6ab51e58485cab4c954fdbcd ts=2026-09-24T12:56:26.4320000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[769] _id=6ab51e07485cab4c954fd000 ts=2026-09-24T12:56:39.2350000Z == 6aa413b141b41dbac0c7f1f7.jsonl[759] _id=6ab51e07485cab4c954fd007 ts=2026-09-24T12:56:39.2350000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[765] _id=6ab51e07485cab4c954fd00d ts=2026-09-24T12:56:39.2570000Z == 6aa413b141b41dbac0c7f1f7.jsonl[760] _id=6ab51e07485cab4c954fd013 ts=2026-09-24T12:56:39.2570000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6aa413b141b41dbac0c7f1f7.jsonl[75] _id=6ab3cfc6485cab4c954b8a49 ts=2026-09-23T13:10:30.9190000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[87] _id=6ab3cfc6485cab4c954b8a4c ts=2026-09-23T13:10:30.9290000Z`; `551ms: 6aa413b141b41dbac0c7f1f7.jsonl[700] _id=6ab51dbe485cab4c954fc7c5 ts=2026-09-24T12:55:26.8110000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[701] _id=6ab51dbf485cab4c954fc7d5 ts=2026-09-24T12:55:27.3620000Z`; `974ms: 6aa413b141b41dbac0c7f1f7.jsonl[701] _id=6ab51dbf485cab4c954fc7d5 ts=2026-09-24T12:55:27.3620000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[707] _id=6ab51dc0485cab4c954fc7f5 ts=2026-09-24T12:55:28.3360000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 741 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `172ms: 6aa413b141b41dbac0c7f1f7.jsonl[823] _id=6ab51e57485cab4c954fdbb3 ts=2026-09-24T12:56:21.5260000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[851] _id=6ab51e57485cab4c954fdbb5 ts=2026-09-24T12:56:21.6980000Z`; `167ms: 6aa413b141b41dbac0c7f1f7.jsonl[762] _id=6ab51e08485cab4c954fd025 ts=2026-09-24T12:56:39.3440000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[763] _id=6ab51e08485cab4c954fd02b ts=2026-09-24T12:56:39.5110000Z`; `21ms: 6aa413b141b41dbac0c7f1f7.jsonl[890] _id=6ab51e5a485cab4c954fdc07 ts=2026-09-24T12:57:49.6120000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[799] _id=6ab51e5a485cab4c954fdc09 ts=2026-09-24T12:57:49.6330000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `556ms: 6aa413b141b41dbac0c7f1f7.jsonl[446] _id=6ab3d51b485cab4c954c72c5 ts=2026-09-23T13:33:15.4040000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[448] _id=6ab3d51b485cab4c954c72cf ts=2026-09-23T13:33:15.9600000Z`; `931ms: 6aa413b141b41dbac0c7f1f7.jsonl[9709] _id=6abe5eaf485cab4c95a52f4b ts=2026-10-01T13:22:55.7690000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[9711] _id=6abe5eb0485cab4c95a52fcf ts=2026-10-01T13:22:56.7000000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6aa413b141b41dbac0c7f1f7.jsonl[9825] _id=6abe5f77485cab4c95a57aa7 ts=2026-10-01T13:26:15.8460000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[9828] _id=6abe5f78485cab4c95a57abc ts=2026-10-01T13:26:15.8820000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 23 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `59ms: 6aa413b141b41dbac0c7f1f7.jsonl[393] _id=6ab3d465485cab4c954c4e7e ts=2026-09-23T13:30:13.2950000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[388] _id=6ab3d465485cab4c954c4e83 ts=2026-09-23T13:30:13.3540000Z`; `28ms: 6aa413b141b41dbac0c7f1f7.jsonl[394] _id=6ab3d467485cab4c954c4ec5 ts=2026-09-23T13:30:15.0380000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[397] _id=6ab3d467485cab4c954c4ec9 ts=2026-09-23T13:30:15.0660000Z`; `390ms: 6aa413b141b41dbac0c7f1f7.jsonl[431] _id=6ab3d510485cab4c954c70a9 ts=2026-09-23T13:33:04.7250000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[434] _id=6ab3d511485cab4c954c70c5 ts=2026-09-23T13:33:05.1150000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa413b141b41dbac0c7f1f7.jsonl[5613] _id=6aba64e3485cab4c956797c7 ts=2026-09-28T13:00:15.4930000Z ~ 6aa413b141b41dbac0c7f1f7.jsonl[5624] _id=6aba64e3485cab4c956797cd ts=2026-09-28T13:00:15.4970000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 6aa413b141b41dbac0c7f1f7.jsonl[10031] _id=6abe6061485cab4c95a5bc7b ts=2026-10-01T13:30:09.5690000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10680] _id=6ac39fc0de269131f9a843bc ts=2026-10-05T13:01:52.6370000Z; 72h 1m: 6aa413b141b41dbac0c7f1f7.jsonl[358] _id=6ab66fe9485cab4c95545381 ts=2026-09-25T12:58:17.2210000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5584] _id=6aba64d9485cab4c956796c6 ts=2026-09-28T13:00:09.3160000Z; 47h 41m: 6aa413b141b41dbac0c7f1f7.jsonl[12262] _id=6ac3a89cde269131f9a98e3f ts=2026-10-05T13:39:40.0750000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12284] _id=6ac64746de269131f9b8ccdb ts=2026-10-07T13:21:10.8010000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 312h 9m 
  - Evidence: 312h 9m: 6aa413b141b41dbac0c7f1f7.jsonl[3625] _id=6ab524c8485cab4c9550dcdd ts=2026-09-24T13:25:28.4820000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[13024] _id=6ac64a7bde269131f9b983ef ts=2026-10-07T13:34:51.0840000Z; 17m 55s: 6aa413b141b41dbac0c7f1f7.jsonl[3233] _id=6ab52074485cab4c955018a2 ts=2026-09-24T13:07:00.0080000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[3615] _id=6ab524a7485cab4c9550d66a ts=2026-09-24T13:24:55.7740000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.002s..0.010s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1f7.jsonl[3624] _id=6ab524c6485cab4c9550dcaf ts=2026-09-24T13:25:26.5440000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[3626] _id=6ab524c6485cab4c9550dcb1 ts=2026-09-24T13:25:26.5460000Z; 10ms: 6aa413b141b41dbac0c7f1f7.jsonl[3622] _id=6ab524b7485cab4c9550d94c ts=2026-09-24T13:25:11.5010000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[3623] _id=6ab524b7485cab4c9550d951 ts=2026-09-24T13:25:11.5110000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa413b141b41dbac0c7f1f7.jsonl[10575] _id=6abe6264485cab4c95a654e7 ts=2026-10-01T13:38:44.9250000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10794] _id=6ac39fe7de269131f9a845b3 ts=2026-10-05T13:02:31.5820000Z; 71h 27m: 6aa413b141b41dbac0c7f1f7.jsonl[5559] _id=6ab677e2485cab4c95551635 ts=2026-09-25T13:32:18.6320000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5619] _id=6aba64e3485cab4c956797bd ts=2026-09-28T13:00:15.4650000Z; 47h 42m: 6aa413b141b41dbac0c7f1f7.jsonl[12278] _id=6ac3a8cbde269131f9a9960b ts=2026-10-05T13:40:27.0140000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12338] _id=6ac647adde269131f9b8d82e ts=2026-10-07T13:22:53.4280000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 532 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f7.jsonl[10365] _id=6abe6144485cab4c95a6011b ts=2026-10-01T13:33:56.2660000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10366] _id=6abe6144485cab4c95a6011f ts=2026-10-01T13:33:56.2670000Z; 1ms: 6aa413b141b41dbac0c7f1f7.jsonl[10368] _id=6abe6145485cab4c95a60165 ts=2026-10-01T13:33:57.4680000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10369] _id=6abe6145485cab4c95a6016d ts=2026-10-01T13:33:57.4690000Z; 1ms: 6aa413b141b41dbac0c7f1f7.jsonl[10920] _id=6ac3a069de269131f9a84e10 ts=2026-10-05T13:04:41.0570000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10921] _id=6ac3a069de269131f9a84e14 ts=2026-10-05T13:04:41.0580000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 287h 52m 
  - Evidence: 287h 52m: 6aa413b141b41dbac0c7f1f7.jsonl[565] _id=6ab3d5f9485cab4c954c933d ts=2026-09-23T13:36:57.4720000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[11543] _id=6ac3a62dde269131f9a91e2f ts=2026-10-05T13:29:17.8770000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 6aa413b141b41dbac0c7f1f7.jsonl[10669] _id=6abe62d1485cab4c95a6770d ts=2026-10-01T13:40:33.4050000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10740] _id=6ac39fd7de269131f9a844ae ts=2026-10-05T13:02:14.2310000Z; 71h 35m: 6aa413b141b41dbac0c7f1f7.jsonl[5459] _id=6ab67617485cab4c9554d5ae ts=2026-09-25T13:24:39.2120000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5597] _id=6aba64e1485cab4c9567975d ts=2026-09-28T13:00:15.4020000Z; 47h 41m: 6aa413b141b41dbac0c7f1f7.jsonl[12258] _id=6ac3a898de269131f9a98db1 ts=2026-10-05T13:39:36.4110000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12290] _id=6ac64759de269131f9b8ce67 ts=2026-10-07T13:21:29.3070000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 170 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f7.jsonl[10004] _id=6abe6063485cab4c95a5bcf1 ts=2026-10-01T13:30:10.5300000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10005] _id=6abe6063485cab4c95a5bcf6 ts=2026-10-01T13:30:10.5310000Z; 1ms: 6aa413b141b41dbac0c7f1f7.jsonl[10025] _id=6abe6062485cab4c95a5bcdd ts=2026-10-01T13:30:10.5270000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10026] _id=6abe6062485cab4c95a5bce1 ts=2026-10-01T13:30:10.5280000Z; 1ms: 6aa413b141b41dbac0c7f1f7.jsonl[10026] _id=6abe6062485cab4c95a5bce1 ts=2026-10-01T13:30:10.5280000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10073] _id=6abe6062485cab4c95a5bce9 ts=2026-10-01T13:30:10.5290000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa413b141b41dbac0c7f1f7.jsonl[10651] _id=6abe62b9485cab4c95a672a7 ts=2026-10-01T13:40:09.7710000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10753] _id=6ac39fdcde269131f9a844fc ts=2026-10-05T13:02:20.5380000Z; 71h 44m: 6aa413b141b41dbac0c7f1f7.jsonl[5220] _id=6ab674a2485cab4c9554a8e3 ts=2026-09-25T13:18:26.8600000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5795] _id=6aba6587485cab4c95679ca9 ts=2026-09-28T13:03:03.6480000Z; 47h 44m: 6aa413b141b41dbac0c7f1f7.jsonl[12256] _id=6ac3a893de269131f9a98cdb ts=2026-10-05T13:39:31.5930000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12386] _id=6ac64804de269131f9b8e467 ts=2026-10-07T13:24:20.3180000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.010s..0.010s shown 
  - Evidence: 10ms: 6aa413b141b41dbac0c7f1f7.jsonl[75] _id=6ab3cfc6485cab4c954b8a49 ts=2026-09-23T13:10:30.9190000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[87] _id=6ab3cfc6485cab4c954b8a4c ts=2026-09-23T13:10:30.9290000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 6aa413b141b41dbac0c7f1f7.jsonl[10671] _id=6abe62dd485cab4c95a679ec ts=2026-10-01T13:40:45.3030000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10683] _id=6ac39fc4de269131f9a843da ts=2026-10-05T13:01:52.6480000Z; 71h 24m: 6aa413b141b41dbac0c7f1f7.jsonl[5579] _id=6ab678bd485cab4c95553008 ts=2026-09-25T13:35:57.5740000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5604] _id=6aba64e1485cab4c95679759 ts=2026-09-28T13:00:09.3220000Z; 23h 27m: 6aa413b141b41dbac0c7f1f7.jsonl[3774] _id=6ab52600485cab4c95511c05 ts=2026-09-24T13:30:40.3600000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[359] _id=6ab66fea485cab4c95545383 ts=2026-09-25T12:58:17.2270000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa413b141b41dbac0c7f1f7.jsonl[10469] _id=6abe61db485cab4c95a62c51 ts=2026-10-01T13:36:25.9680000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10677] _id=6ac39fc5de269131f9a843ea ts=2026-10-05T13:01:54.4560000Z; 72h 22m: 6aa413b141b41dbac0c7f1f7.jsonl[6293] _id=6aba66b7485cab4c9567a5cc ts=2026-09-28T13:08:06.7090000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10027] _id=6abe6063485cab4c95a5bd21 ts=2026-10-01T13:30:10.5410000Z; 71h 35m: 6aa413b141b41dbac0c7f1f7.jsonl[5450] _id=6ab67607485cab4c9554d336 ts=2026-09-25T13:24:21.3700000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5602] _id=6aba64e3485cab4c956797d1 ts=2026-09-28T13:00:15.8120000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3043 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f7.jsonl[10001] _id=6abe607f485cab4c95a5c4bf ts=2026-10-01T13:30:37.6550000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10002] _id=6abe607f485cab4c95a5c4c6 ts=2026-10-01T13:30:37.6550000Z; 0ms: 6aa413b141b41dbac0c7f1f7.jsonl[10009] _id=6abe6082485cab4c95a5c60e ts=2026-10-01T13:30:41.5190000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10006] _id=6abe6082485cab4c95a5c619 ts=2026-10-01T13:30:41.5190000Z; 0ms: 6aa413b141b41dbac0c7f1f7.jsonl[10010] _id=6abe6081485cab4c95a5c581 ts=2026-10-01T13:30:40.9880000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10011] _id=6abe6081485cab4c95a5c587 ts=2026-10-01T13:30:40.9880000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 16m 
  - Evidence: 144h 16m: 6aa413b141b41dbac0c7f1f7.jsonl[4157] _id=6ab67364485cab4c955487c7 ts=2026-09-25T13:13:08.9910000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9960] _id=6abe602a485cab4c95a5afbf ts=2026-10-01T13:29:14.2520000Z; 96h 6m: 6aa413b141b41dbac0c7f1f7.jsonl[9978] _id=6abe603a485cab4c95a5b41f ts=2026-10-01T13:29:30.6270000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[11651] _id=6ac3a7afde269131f9a96129 ts=2026-10-05T13:35:43.8460000Z; 47h 47m: 6aa413b141b41dbac0c7f1f7.jsonl[11577] _id=6ac3a7d7de269131f9a967c1 ts=2026-10-05T13:36:23.0240000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12384] _id=6ac64804de269131f9b8e462 ts=2026-10-07T13:24:20.3130000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6aa413b141b41dbac0c7f1f7.jsonl[8705] _id=6abd1084485cab4c9588ba28 ts=2026-09-30T13:37:08.6680000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[11289] _id=6ac3a2ecde269131f9a87eb4 ts=2026-10-05T13:15:24.4050000Z; 72h 31m: 6aa413b141b41dbac0c7f1f7.jsonl[3775] _id=6ab67215485cab4c95546e19 ts=2026-09-25T13:07:33.5720000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[6641] _id=6aba6df9485cab4c95681431 ts=2026-09-28T13:39:05.9870000Z; 24h 13m: 6aa413b141b41dbac0c7f1f7.jsonl[6847] _id=6abbbbd7485cab4c957ccc3f ts=2026-09-29T13:23:35.1820000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[8699] _id=6abd1081485cab4c9588b940 ts=2026-09-30T13:37:05.7630000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 6aa413b141b41dbac0c7f1f7.jsonl[464] _id=6ab3d525485cab4c954c745a ts=2026-09-23T13:33:25.6850000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9686] _id=6abe5e8c485cab4c95a518e3 ts=2026-10-01T13:22:20.6440000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 6aa413b141b41dbac0c7f1f7.jsonl[461] _id=6ab3d525485cab4c954c7468 ts=2026-09-23T13:33:25.7020000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9680] _id=6abe5e80485cab4c95a51338 ts=2026-10-01T13:22:08.3500000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.036s..0.036s shown 
  - Evidence: 36ms: 6aa413b141b41dbac0c7f1f7.jsonl[9825] _id=6abe5f77485cab4c95a57aa7 ts=2026-10-01T13:26:15.8460000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9828] _id=6abe5f78485cab4c95a57abc ts=2026-10-01T13:26:15.8820000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 6aa413b141b41dbac0c7f1f7.jsonl[460] _id=6ab3d524485cab4c954c73f7 ts=2026-09-23T13:33:24.5520000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9663] _id=6abe5e84485cab4c95a514cf ts=2026-10-01T13:22:12.0140000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 31 interval(s) ≤ 0.021s..0.024s shown 
  - Evidence: 21ms: 6aa413b141b41dbac0c7f1f7.jsonl[9885] _id=6abe5f52485cab4c95a56dcf ts=2026-10-01T13:25:38.2740000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9880] _id=6abe5f52485cab4c95a56ddf ts=2026-10-01T13:25:38.2950000Z; 23ms: 6aa413b141b41dbac0c7f1f7.jsonl[9789] _id=6abe5ef0485cab4c95a54aee ts=2026-10-01T13:24:00.4820000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9750] _id=6abe5ef0485cab4c95a54af9 ts=2026-10-01T13:24:00.5050000Z; 24ms: 6aa413b141b41dbac0c7f1f7.jsonl[9667] _id=6abe5e84485cab4c95a514e7 ts=2026-10-01T13:22:12.1630000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9682] _id=6abe5e84485cab4c95a514fd ts=2026-10-01T13:22:12.1870000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa413b141b41dbac0c7f1f7.jsonl[8810] _id=6abe590d485cab4c95a40b35 ts=2026-10-01T12:58:57.1610000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10682] _id=6ac39fbade269131f9a8439c ts=2026-10-05T13:01:46.4710000Z; 72h 1m: 6aa413b141b41dbac0c7f1f7.jsonl[357] _id=6ab66fe5485cab4c9554537f ts=2026-09-25T12:58:12.9110000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5583] _id=6aba64d4485cab4c956796a1 ts=2026-09-28T13:00:01.1120000Z; 47h 51m: 6aa413b141b41dbac0c7f1f7.jsonl[11544] _id=6ac3a639de269131f9a92161 ts=2026-10-05T13:29:29.1290000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12283] _id=6ac64747de269131f9b8cce2 ts=2026-10-07T13:21:11.2100000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 6aa413b141b41dbac0c7f1f7.jsonl[9396] _id=6abe5ba3485cab4c95a45a71 ts=2026-10-01T13:09:55.3790000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10681] _id=6ac39fbade269131f9a84398 ts=2026-10-05T13:01:46.4700000Z; 72h 1m: 6aa413b141b41dbac0c7f1f7.jsonl[355] _id=6ab66fe5485cab4c9554537d ts=2026-09-25T12:58:12.9100000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5585] _id=6aba64d1485cab4c9567969d ts=2026-09-28T13:00:01.1110000Z; 47h 51m: 6aa413b141b41dbac0c7f1f7.jsonl[11548] _id=6ac3a639de269131f9a9215a ts=2026-10-05T13:29:29.1270000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12282] _id=6ac64747de269131f9b8cce1 ts=2026-10-07T13:21:11.2100000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 121h 41m 
  - Evidence: 121h 41m: 6aa413b141b41dbac0c7f1f7.jsonl[3287] _id=6ab520e4485cab4c95501d43 ts=2026-09-24T13:08:52.1070000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[7383] _id=6abbd01d485cab4c957f1cad ts=2026-09-29T14:50:05.9290000Z; 95h 38m: 6aa413b141b41dbac0c7f1f7.jsonl[10672] _id=6abe62e2485cab4c95a67b2f ts=2026-10-01T13:40:50.3370000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[11417] _id=6ac3a3eade269131f9a89fe4 ts=2026-10-05T13:19:38.7200000Z; 23h 34m: 6aa413b141b41dbac0c7f1f7.jsonl[8522] _id=6abd0fbd485cab4c95886d92 ts=2026-09-30T13:33:49.3020000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[9378] _id=6abe5b2d485cab4c95a443e7 ts=2026-10-01T13:07:57.8300000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 6aa413b141b41dbac0c7f1f7.jsonl[10098] _id=6abe606c485cab4c95a5bf4f ts=2026-10-01T13:30:20.7560000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[10684] _id=6ac39fc4de269131f9a843dc ts=2026-10-05T13:01:56.4290000Z; 71h 31m: 6aa413b141b41dbac0c7f1f7.jsonl[5520] _id=6ab676fa485cab4c9554faee ts=2026-09-25T13:28:26.7910000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5613] _id=6aba64e3485cab4c956797c7 ts=2026-09-28T13:00:15.4930000Z; 47h 48m: 6aa413b141b41dbac0c7f1f7.jsonl[11578] _id=6ac3a711de269131f9a94924 ts=2026-10-05T13:33:05.0140000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[12288] _id=6ac64754de269131f9b8ce1b ts=2026-10-07T13:21:24.4900000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.002s..0.008s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1f7.jsonl[345] _id=6ab3d3d5485cab4c954c2d30 ts=2026-09-23T13:27:49.7510000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[348] _id=6ab3d3d5485cab4c954c2d32 ts=2026-09-23T13:27:49.7530000Z; 4ms: 6aa413b141b41dbac0c7f1f7.jsonl[5613] _id=6aba64e3485cab4c956797c7 ts=2026-09-28T13:00:15.4930000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[5624] _id=6aba64e3485cab4c956797cd ts=2026-09-28T13:00:15.4970000Z; 8ms: 6aa413b141b41dbac0c7f1f7.jsonl[108] _id=6ab3d01d485cab4c954b8faa ts=2026-09-23T13:11:57.0920000Z -> 6aa413b141b41dbac0c7f1f7.jsonl[109] _id=6ab3d01d485cab4c954b8fac ts=2026-09-23T13:11:57.1000000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[326] _id=6ab3d3bd485cab4c954c266c ts=2026-09-23T13:27:25.8460000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[476] _id=6ab3d545485cab4c954c7bd3 ts=2026-09-23T13:33:57.8730000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[3531] _id=6ab5241e485cab4c9550b2eb ts=2026-09-24T13:22:38.0750000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 136 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[946] _id=6ab51e5f485cab4c954fdc9f ts=2026-09-24T12:58:05.7740000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[954] _id=6ab51e5f485cab4c954fdca1 ts=2026-09-24T12:58:06.1610000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[925] _id=6ab51e63485cab4c954fdd07 ts=2026-09-24T12:58:09.3350000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 304 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[869] _id=6ab51e59485cab4c954fdbd7 ts=2026-09-24T12:56:27.7070000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[763] _id=6ab51e08485cab4c954fd02b ts=2026-09-24T12:56:39.5110000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[899] _id=6ab51e59485cab4c954fdbeb ts=2026-09-24T12:56:40.3750000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[9828] _id=6abe5f78485cab4c95a57abc ts=2026-10-01T13:26:15.8820000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[393] _id=6ab3d465485cab4c954c4e7e ts=2026-09-23T13:30:13.2950000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[388] _id=6ab3d465485cab4c954c4e83 ts=2026-09-23T13:30:13.3540000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[397] _id=6ab3d467485cab4c954c4ec9 ts=2026-09-23T13:30:15.0660000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[13073] _id=6ac64b47de269131f9b9abc3 ts=2026-10-07T13:38:15.1040000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[627] _id=6ab51cc5485cab4c954fbbd7 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 782 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[1002] _id=6ab51e6b485cab4c954fde43 ts=2026-09-24T12:58:18.6890000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[994] _id=6ab51e6b485cab4c954fde47 ts=2026-09-24T12:58:18.7620000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[1016] _id=6ab51e6e485cab4c954fde9b ts=2026-09-24T12:58:20.9000000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 952 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[841] _id=6ab51e55485cab4c954fdb59 ts=2026-09-24T12:56:21.4090000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[844] _id=6ab51e56485cab4c954fdb8d ts=2026-09-24T12:56:21.4940000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[845] _id=6ab51e56485cab4c954fdb91 ts=2026-09-24T12:56:21.4940000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 359 start, 351 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 160 unmatched 'BecameCameraCentered' (totals: 1024 open, 1000 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 122 unmatched 'BecameVisible' (totals: 1408 open, 1590 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 34 start, 21 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 413 of 13176 adjacent _id pairs reverse in client time; worst 104.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f7.jsonl[816] _id=6ab51e53485cab4c954fdb01 ts=2026-09-24T12:57:55.5860000Z`; `6aa413b141b41dbac0c7f1f7.jsonl[831] _id=6ab51e54485cab4c954fdb19 ts=2026-09-24T12:56:11.2130000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.07s, min -106.08s, max +3.71s over 13177 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f7\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 5022 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3674); Unit 4 Dev (890); Unit 3 Dungeon Dev (458)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.02s, n=5021)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5022/5022 records)
    "BecameInvisible"  x1590
    "BecameVisible"  x1408
    "BecameCameraCentered"  x1024
    "BecameCameraUncentered"  x1000
data.pieceId  (string, 5022/5022 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5022/5022 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3840 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2011); Unit 2 Prod (Refactor) (973); Unit 3 Dungeon Dev (416); Unit 4 Dev (184); Unit 4 Dev - Dungeon (163); Unit 1 Dev (93)
- **Intervals:** median 0.70s (p5 0.06s / p95 9.77s, n=3839)
- **Fields under `data`:**

```text
data.Value  (string, 3840/3840 records)
    "pressed"  x3840
data.actionType  (string, 3840/3840 records)
    "Move"  x2721
    "Interact"  x467
    "Jump"  x365
    "Ascend"  x104
    "Sprint"  x99
    "Hoverboard"  x34
    "Map"  x24
    "Descend"  x16
    "Pause"  x8
    "SkipCinematic"  x2
data.key  (string, 3840/3840 records, 7 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3840/3840 records)
    "Player"  x2071
    "Drone"  x1769
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1867 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (718); Unit 3 Dev (639); Unit 1 Dev (190); Unit 3 Dungeon Dev (136); Unit 4 Dev - Dungeon (95); Unit 4 Dev (89)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1858)
- **Fields under `data`:**

```text
data.position  (object, 1867/1867 records)
data.position.x  (number, 1867/1867 records)
    numeric range -708.806 .. 1428.76 (496 unique)
data.position.y  (number, 1867/1867 records)
    numeric range -115.115 .. 176.072 (377 unique)
data.position.z  (number, 1867/1867 records)
    numeric range -1132.33 .. 2094.14 (496 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1808 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (656); Unit 2 Prod (Refactor) (650); Unit 1 Dev (191); Unit 3 Dungeon Dev (188); Unit 4 Dev (68); Unit 4 Dev - Dungeon (55)
- **eventKey:** present on 1098 of 1808 records
- **Intervals:** median 4.19s (p5 0.00s / p95 38.38s, n=1807)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1098; [conversationId, dialogueEventType] x710
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1808/1808 records)
    numeric range 8 .. 111 (37 unique)
data.dialogueEventType  (string, 1808/1808 records)
    "DialogueNodeEvent"  x1098
    "DialogueStartEvent"  x359
    "DialogueFinishEvent"  x351
data.nodeId  (number, 1098/1808 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 200 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (75); Unit 3 Dungeon Dev (65); Unit 4 Dev - Dungeon (28); Unit 3 Dev (12); Unit 1 Dev (10); Unit 4 Dev (10)
- **Intervals:** median 7.29s (p5 1.25s / p95 470.31s, n=199)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 200/200 records)
    25 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 200/200 records)
    53 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 147 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (117); Unit 1 Dev (30)
- **Intervals:** median 0.37s (p5 0.03s / p95 6.74s, n=146)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 147/147 records)
    "argumentationNodeHoverEnd"  x69
    "argumentationNodeHoverStart"  x61
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 147/147 records)
    "Unit 3 - Pollution Upstream"  x117
    "Unit 1 - Freshwater"  x23
    "Unit 1 - Argumentation Tutorial"  x7
data.nodeName  (string, 147/147 records)
    "A"  x21
    "3"  x20
    "2"  x18
    "4"  x18
    "I"  x18
    "1"  x17
    "B"  x14
    "5"  x11
    "II"  x10
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 66 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (34); Unit 2 Prod (Refactor) (22); Unit 3 Dev (10)
- **Intervals:** median 1.64s (p5 0.18s / p95 69325.17s, n=65)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x56; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/66 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/66 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 56/66 records)
    "RightDrag"  x31
    "LeftDrag"  x25
data.currentSoilType  (string, 56/66 records)
    "CLAYSAND"  x14
    "SAND"  x12
    "CLAY"  x11
    "CLAYROCK"  x7
    "SANDGRAVEL"  x7
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 56/66 records)
    "false"  x41
    "true"  x15
data.waterLevelStatus  (string, 56/66 records)
    "TooLow"  x25
    "Proper"  x18
    "TooHigh"  x13
data.waterRetentionChange  (string, 56/66 records)
    "Increase"  x22
    "Decrease"  x19
    "NoChange"  x15
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 55 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (18); Unit 1 Dev (12); Unit 3 Dungeon Dev (3); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2)
- **eventKey:** present on 55 of 55 records
- **Intervals:** median 268.14s (p5 0.01s / p95 115763.91s, n=54)
- **`data` key-set variants:** [questEventType, questID, questName] x34; [questEventType, questID, questName, questSuccessOrFailure] x21
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 55/55 records)
    "questActiveEvent"  x34
    "questFinishEvent"  x21
data.questID  (string, 55/55 records)
    19 unique values (see csv/event_unique_values.csv)
data.questName  (string, 55/55 records)
    19 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 21/55 records)
    "Succeeded"  x21
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 50 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (39); Unit 3 Dev (11)
- **Intervals:** median 8.84s (p5 1.13s / p95 86501.68s, n=49)
- **`data` key-set variants:** [actionType, featureUsed] x32; [actionType, featureUsed, location] x10; [actionType, featureUsed, legendName] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "MapCloseEvent"  x16
    "MapOpenEvent"  x16
    "Selected"  x8
    "WaypointMoveEvent"  x6
    "WaypointSetEvent"  x4
data.featureUsed  (string, 50/50 records)
    "Map"  x32
    "Waypoint"  x10
    "Legend"  x8
data.legendName  (string, 8/50 records)
    "Water"  x4
    "0 ft"  x1
    "30 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
data.location  (object, 10/50 records)
data.location.x  (number, 10/50 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 10/50 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 10/50 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 23 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 3 Dev (6); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 1051.43s (p5 109.75s / p95 254957.90s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 21 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (5); Unit 3 Dungeon Dev (2); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2); MainMenu (1); Unit 1 Dev (1)
- **Intervals:** median 1945.56s (p5 81.69s / p95 263541.64s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "DebugMenuStateChanged"  x21
data.isOpened  (bool, 21/21 records)
    false  x21
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 20 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (16); Unit 1 Dev (4)
- **Intervals:** median 8.71s (p5 0.89s / p95 69110.47s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "submitAnswerEvent"  x20
data.answerSubmitted  (string, 20/20 records)
    "B,3,II"  x4
    "B,5,II"  x4
    "A,4,I"  x3
    "I"  x3
    "B,3,I"  x2
    "A,1,I"  x1
    "A,2,I"  x1
    "A,3,I"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 20/20 records)
    "Unit 3 - Pollution Upstream"  x16
    "Unit 1 - Freshwater"  x4
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1.94s (p5 0.01s / p95 225613.13s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 16 empty-string)
    ""  x16
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 81649.54s (p5 116.79s / p95 285246.53s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (7); Unit 2 Prod (Refactor) (3); Unit 3 Dungeon Dev (1)
- **Intervals:** median 41403.19s (p5 56.26s / p95 395888.37s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 88.52s (p5 6.55s / p95 517953.86s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 1036340.41s (p5 1036340.41s / p95 1036340.41s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 2.06s (p5 2.06s / p95 2.06s, n=1)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 7.61s (p5 7.61s / p95 7.61s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[21-11, 21-12, 21-92, 21-15, 18-231]"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TopographicMapEvent` data.actionType: "Selected" (8x); "WaypointMoveEvent" (6x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (8x); "Waypoint" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*