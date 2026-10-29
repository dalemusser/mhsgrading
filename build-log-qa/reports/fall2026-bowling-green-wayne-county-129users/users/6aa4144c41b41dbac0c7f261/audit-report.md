# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f261

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f261
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f261.jsonl
- **Records:** 14886 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f261
- **Time span:** 2026-09-23T18:15:35.299000+00:00 .. 2026-10-06T18:50:54.221000+00:00 (312h 35m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f261\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 14886 records, 10 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 98 INFO, 0 NOT_TESTED, 90 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5837 | 39.21 | 1 | 4 | 0 | 2026-09-28T14:57:54.246000+00:00 | 2026-10-06T18:15:30.926000+00:00 | 195h 17m |
| InputEvent | 3555 | 23.88 | 1 | 8 | 0 | 2026-09-23T18:15:51.919000+00:00 | 2026-10-06T18:50:54.221000+00:00 | 312h 35m |
| PlayerPositionEvent | 2383 | 16.01 | 1 | 8 | 0 | 2026-09-23T18:15:46.423000+00:00 | 2026-10-06T18:50:49.637000+00:00 | 312h 35m |
| DialogueEvent | 1913 | 12.85 | 1 | 8 | 1143 | 2026-09-23T18:16:08.565000+00:00 | 2026-10-06T18:50:50.873000+00:00 | 312h 34m |
| ObjectInterEvent | 443 | 2.98 | 1 | 8 | 0 | 2026-09-23T18:22:48.481000+00:00 | 2026-10-06T18:50:54.220000+00:00 | 312h 28m |
| argumentationNodeEvent | 254 | 1.71 | 1 | 3 | 0 | 2026-09-24T18:07:37.861000+00:00 | 2026-10-06T18:39:17.767000+00:00 | 288h 31m |
| questEvent | 101 | 0.68 | 1 | 8 | 101 | 2026-09-23T18:16:08.542000+00:00 | 2026-10-06T18:47:07.669000+00:00 | 312h 30m |
| Soil Key Puzzle | 90 | 0.6 | 1 | 3 | 0 | 2026-09-28T18:19:53.130000+00:00 | 2026-10-01T14:42:52.123000+00:00 | 68h 22m |
| gameWindowFocusEvent | 48 | 0.32 | 1 | 7 | 0 | 2026-09-23T18:15:35.299000+00:00 | 2026-10-06T18:15:48.689000+00:00 | 312h 0m |
| soilMachine | 39 | 0.26 | 1 | 1 | 0 | 2026-10-05T18:20:54.808000+00:00 | 2026-10-05T18:41:35.377000+00:00 | 20m 40s |
| WaterChamberEvent | 38 | 0.26 | 1 | 1 | 0 | 2026-10-06T18:08:22.160000+00:00 | 2026-10-06T18:29:44.299000+00:00 | 21m 22s |
| DEBUGMenu | 32 | 0.21 | 1 | 7 | 0 | 2026-09-23T18:15:46.415000+00:00 | 2026-10-06T18:10:46.162000+00:00 | 311h 54m |
| gameWindowUnfocusEvent | 30 | 0.2 | 1 | 7 | 0 | 2026-09-23T18:30:33.985000+00:00 | 2026-10-06T18:15:44.750000+00:00 | 311h 45m |
| gameStartEvent | 28 | 0.19 | 1 | 1 | 0 | 2026-09-23T18:15:35.299000+00:00 | 2026-10-06T18:10:39.565000+00:00 | 311h 55m |
| DaniEvent | 24 | 0.16 | 1 | 1 | 0 | 2026-09-23T18:25:38.743000+00:00 | 2026-09-23T18:28:43.948000+00:00 | 3m 5s |
| TopographicMapEvent | 24 | 0.16 | 1 | 3 | 0 | 2026-09-23T18:27:55.998000+00:00 | 2026-09-30T18:55:04.978000+00:00 | 168h 27m |
| argumentationAnswerEvent | 15 | 0.1 | 1 | 3 | 0 | 2026-09-24T18:09:32.524000+00:00 | 2026-10-06T18:39:19.056000+00:00 | 288h 29m |
| crash | 10 | 0.07 | 1 | 1 | 0 |  |  | ? |
| argumentationEvent | 9 | 0.06 | 1 | 3 | 0 | 2026-09-24T18:08:18.404000+00:00 | 2026-10-06T18:39:19.089000+00:00 | 288h 31m |
| chatEvent | 7 | 0.05 | 1 | 3 | 0 | 2026-09-23T18:27:35.075000+00:00 | 2026-10-06T18:30:28.750000+00:00 | 312h 2m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-06T18:45:04.283000+00:00 | 2026-10-06T18:45:08.550000+00:00 | 4.3s |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-30T19:18:13.703000+00:00 | 2026-10-06T18:50:54.199000+00:00 | 143h 32m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 516760.496s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.465s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.612s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.642s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 27.338s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 5929.769s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 471.043s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 977.079s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.207s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 24 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 2; 4 
  - Expected: may simply not have been exercised — review
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
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E To Pick Up; Press E To Place Cameras; Press E To Scan; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to place canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
  - Expected: 83 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 240 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; B,1,I; B,5,I; C,2,II; C,D,2,II; C,D,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 7 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [30-41, 30-97, 30-48, 30-49, 30-50] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 10 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.7x vs baseline. 
  - Observed: 28 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 54; 56 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Power Play; Saving Cadet Anderson 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 7.8x vs baseline. 
  - Observed: 39 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 29 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[436] _id=6ab41bdb485cab4c954f5a49 ts=2026-09-23T18:35:07.1800000Z`; `6aa4144c41b41dbac0c7f261.jsonl[497] _id=6ab41ce4485cab4c954f628b ts=2026-09-23T18:39:32.0430000Z`; `6aa4144c41b41dbac0c7f261.jsonl[532] _id=6ab41df3485cab4c954f6c08 ts=2026-09-23T18:44:03.0100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[4546] _id=6abc000b485cab4c95842cb9 ts=2026-09-29T18:14:33.9230000Z`; `6aa4144c41b41dbac0c7f261.jsonl[5875] _id=6abc04e5485cab4c95848ff1 ts=2026-09-29T18:35:14.6120000Z`; `6aa4144c41b41dbac0c7f261.jsonl[6561] _id=6abd00da485cab4c958655e3 ts=2026-09-30T12:30:19.3840000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[18] _id=6ab41747485cab4c954f3688 ts=2026-09-23T18:15:35.2990000Z`; `6aa4144c41b41dbac0c7f261.jsonl[351] _id=6ab41afd485cab4c954f534e ts=2026-09-23T18:31:25.2270000Z`; `6aa4144c41b41dbac0c7f261.jsonl[569] _id=6ab5612a485cab4c95537f49 ts=2026-09-24T17:43:06.1680000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 48 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 48} 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[19] _id=6ab41747485cab4c954f3686 ts=2026-09-23T18:15:35.2990000Z`; `6aa4144c41b41dbac0c7f261.jsonl[358] _id=6ab41aca485cab4c954f523a ts=2026-09-23T18:30:33.9950000Z`; `6aa4144c41b41dbac0c7f261.jsonl[362] _id=6ab41ade485cab4c954f52c4 ts=2026-09-23T18:30:54.7670000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 30 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 30} 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[355] _id=6ab41ac9485cab4c954f5238 ts=2026-09-23T18:30:33.9850000Z`; `6aa4144c41b41dbac0c7f261.jsonl[361] _id=6ab41ade485cab4c954f52c2 ts=2026-09-23T18:30:54.7590000Z`; `6aa4144c41b41dbac0c7f261.jsonl[742] _id=6ab563bc485cab4c9553b6de ts=2026-09-24T17:54:04.4450000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 24 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[243] _id=6ab41a2b485cab4c954f4e10 ts=2026-09-23T18:27:55.9980000Z`; `6aa4144c41b41dbac0c7f261.jsonl[241] _id=6ab41a2d485cab4c954f4e1a ts=2026-09-23T18:27:57.8040000Z`; `6aa4144c41b41dbac0c7f261.jsonl[246] _id=6ab41a3f485cab4c954f4e90 ts=2026-09-23T18:28:15.6950000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5836 | 0.0 | 0.032 | 120.469 | 1.631 | 360014.458 | 0.5 | 3502 | 13 |
| InputEvent | 3554 | 0.0 | 1.465 | 316.63 | 22.863 | 355798.799 | 0.19 | 97 | 16 |
| PlayerPositionEvent | 2370 | 9.475 | 9.999 | 467.531 | 10.029 | 355787.333 | 0.13 | 0 | 13 |
| DialogueEvent | 1912 | 0.001 | 4.385 | 588.537 | 52.727 | 356053.498 | 0.1 | 563 | 15 |
| ObjectInterEvent | 442 | 0.004 | 8.162 | 2544.99 | 394.919 | 355921.697 | 0.02 | 3 | 19 |
| argumentationNodeEvent | 253 | 0.017 | 0.387 | 4105.533 | 4.286 | 519496.399 | 0.01 | 44 | 2 |
| questEvent | 100 | 0.001 | 252.852 | 11250.591 | 73788.91 | 356112.13 | 0.01 | 21 | 23 |
| Soil Key Puzzle | 89 | 0.143 | 1.612 | 2766.056 | 1344.662 | 171454.946 | 0.02 | 0 | 6 |
| gameWindowFocusEvent | 47 | 0.149 | 471.043 | 23898.157 | 87232.265 | 355768.381 | 0.0 | 0 | 23 |
| soilMachine | 38 | 0.65 | 3.207 | 32.647 | 188.921 | 222.722 | 1.84 | 0 | 0 |
| WaterChamberEvent | 37 | 0.661 | 14.633 | 34.652 | 135.384 | 234.508 | 1.73 | 0 | 0 |
| DEBUGMenu | 31 | 100.81 | 1437.564 | 36222.572 | 167024.617 | 356798.067 | 0.0 | 0 | 23 |
| gameWindowUnfocusEvent | 29 | 0.04 | 977.079 | 38700.371 | 184007.845 | 357972.402 | 0.0 | 1 | 16 |
| gameStartEvent | 27 | 108.82 | 4302.75 | 41589.047 | 198576.754 | 356787.719 | 0.0 | 0 | 21 |
| DaniEvent | 23 | 0.184 | 2.135 | 8.052 | 25.694 | 93.238 | 7.45 | 0 | 0 |
| TopographicMapEvent | 23 | 0.02 | 10.642 | 26366.477 | 138660.23 | 419400.822 | 0.0 | 2 | 5 |
| argumentationAnswerEvent | 14 | 1.665 | 27.338 | 74184.752 | 519036.089 | 519501.936 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationEvent | 8 | 0.022 | 102.281 | 129832.586 | 519217.777 | 519478.542 | 0.0 | 1 | 2 |
| chatEvent | 6 | 3.002 | 5929.769 | 187228.946 | 796735.455 | 1037880.774 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 0.762 | 1.187 | 1.422 | 2.205 | 2.318 | 42.18 | 0 | 0 |
| EndOfUnit | 1 | 516760.496 | 516760.496 | 516760.496 | 516760.496 | 516760.496 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[3141] _id=6abaad61485cab4c956f8285 ts=2026-09-28T18:09:37.0850000Z == 6aa4144c41b41dbac0c7f261.jsonl[3136] _id=6abaad61485cab4c956f828a ts=2026-09-28T18:09:37.0850000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 221 group(s), 292 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[1532] _id=6aba8076485cab4c9568f50d ts=2026-09-28T14:57:58.5910000Z == 6aa4144c41b41dbac0c7f261.jsonl[1545] _id=6aba8076485cab4c9568f50f ts=2026-09-28T14:57:58.5910000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1535] _id=6aba8077485cab4c9568f517 ts=2026-09-28T14:57:58.7860000Z == 6aa4144c41b41dbac0c7f261.jsonl[1547] _id=6aba8078485cab4c9568f519 ts=2026-09-28T14:57:58.7860000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1539] _id=6aba807a485cab4c9568f52d ts=2026-09-28T14:58:01.3980000Z == 6aa4144c41b41dbac0c7f261.jsonl[1554] _id=6aba807a485cab4c9568f52f ts=2026-09-28T14:58:01.3980000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 7 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[579] _id=6ab5615f485cab4c9553849f ts=? == 6aa4144c41b41dbac0c7f261.jsonl[1179] _id=6ab6baf6485cab4c955df505 ts=?`; `6aa4144c41b41dbac0c7f261.jsonl[1471] _id=6aba7fff485cab4c9568f46b ts=? == 6aa4144c41b41dbac0c7f261.jsonl[4544] _id=6abc000a485cab4c95842c9b ts=?`; `6aa4144c41b41dbac0c7f261.jsonl[9033] _id=6abd66ab485cab4c959d5fff ts=? == 6aa4144c41b41dbac0c7f261.jsonl[10121] _id=6abe7080485cab4c95a8f65d ts=?`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `849ms: 6aa4144c41b41dbac0c7f261.jsonl[172] _id=6ab419ae485cab4c954f49b0 ts=2026-09-23T18:25:50.6430000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[160] _id=6ab419af485cab4c954f49c6 ts=2026-09-23T18:25:51.4920000Z`; `464ms: 6aa4144c41b41dbac0c7f261.jsonl[162] _id=6ab419b1485cab4c954f49e2 ts=2026-09-23T18:25:53.6270000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[165] _id=6ab419b2485cab4c954f49ec ts=2026-09-23T18:25:54.0910000Z`; `383ms: 6aa4144c41b41dbac0c7f261.jsonl[176] _id=6ab419b1485cab4c954f49e6 ts=2026-09-23T18:25:53.8920000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[178] _id=6ab419b2485cab4c954f49f0 ts=2026-09-23T18:25:54.2750000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 50 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f261.jsonl[98] _id=6ab418f8485cab4c954f425e ts=2026-09-23T18:22:48.4810000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[100] _id=6ab418f8485cab4c954f4260 ts=2026-09-23T18:22:48.4850000Z`; `5ms: 6aa4144c41b41dbac0c7f261.jsonl[390] _id=6ab41b34485cab4c954f54d4 ts=2026-09-23T18:32:20.6540000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[389] _id=6ab41b34485cab4c954f54d6 ts=2026-09-23T18:32:20.6590000Z`; `941ms: 6aa4144c41b41dbac0c7f261.jsonl[480] _id=6ab41cce485cab4c954f61c3 ts=2026-09-23T18:39:10.3460000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[475] _id=6ab41ccf485cab4c954f61d7 ts=2026-09-23T18:39:11.2870000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 724 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `212ms: 6aa4144c41b41dbac0c7f261.jsonl[1537] _id=6aba8079485cab4c9568f523 ts=2026-09-28T14:58:00.7180000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[1551] _id=6aba8079485cab4c9568f525 ts=2026-09-28T14:58:00.9300000Z`; `101ms: 6aa4144c41b41dbac0c7f261.jsonl[1551] _id=6aba8079485cab4c9568f525 ts=2026-09-28T14:58:00.9300000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[1552] _id=6aba8079485cab4c9568f527 ts=2026-09-28T14:58:01.0310000Z`; `55ms: 6aa4144c41b41dbac0c7f261.jsonl[1614] _id=6aba80ca485cab4c9568f595 ts=2026-09-28T14:59:20.9490000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[1601] _id=6aba80ca485cab4c9568f597 ts=2026-09-28T14:59:21.0040000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa4144c41b41dbac0c7f261.jsonl[4083] _id=6abab177485cab4c956ffde3 ts=2026-09-28T18:27:02.9250000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[4086] _id=6abab177485cab4c956ffdfb ts=2026-09-28T18:27:02.9480000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa4144c41b41dbac0c7f261.jsonl[7472] _id=6abd528a485cab4c9591252f ts=2026-09-30T18:18:50.3900000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[7474] _id=6abd528a485cab4c95912539 ts=2026-09-30T18:18:50.4120000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 37 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `905ms: 6aa4144c41b41dbac0c7f261.jsonl[908] _id=6ab566ee485cab4c95541310 ts=2026-09-24T18:07:42.4540000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[912] _id=6ab566ef485cab4c95541326 ts=2026-09-24T18:07:43.3590000Z`; `809ms: 6aa4144c41b41dbac0c7f261.jsonl[960] _id=6ab567a0485cab4c95541f08 ts=2026-09-24T18:10:40.3660000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[961] _id=6ab567a1485cab4c95541f0e ts=2026-09-24T18:10:41.1750000Z`; `538ms: 6aa4144c41b41dbac0c7f261.jsonl[954] _id=6ab567a0485cab4c95541f0c ts=2026-09-24T18:10:41.1400000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[962] _id=6ab567a1485cab4c95541f12 ts=2026-09-24T18:10:41.6780000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `149ms: 6aa4144c41b41dbac0c7f261.jsonl[4535] _id=6abc045c485cab4c95848a2f ts=2026-09-29T18:33:00.3370000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[5826] _id=6abc045f485cab4c95848a4d ts=2026-09-29T18:33:00.4860000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `317ms: 6aa4144c41b41dbac0c7f261.jsonl[5828] _id=6abc045c485cab4c95848a29 ts=2026-09-29T18:33:00.1350000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[5825] _id=6abc045f485cab4c95848a4b ts=2026-09-29T18:33:00.4520000Z`; `40ms: 6aa4144c41b41dbac0c7f261.jsonl[5825] _id=6abc045f485cab4c95848a4b ts=2026-09-29T18:33:00.4520000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[5836] _id=6abc0460485cab4c95848a55 ts=2026-09-29T18:33:00.4920000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4144c41b41dbac0c7f261.jsonl[4546] _id=6abc000b485cab4c95842cb9 ts=2026-09-29T18:14:33.9230000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[4547] _id=6abc000b485cab4c95842cbe ts=2026-09-29T18:14:33.9260000Z`; `3ms: 6aa4144c41b41dbac0c7f261.jsonl[5875] _id=6abc04e5485cab4c95848ff1 ts=2026-09-29T18:35:14.6120000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[5876] _id=6abc04e5485cab4c95848ff5 ts=2026-09-29T18:35:14.6150000Z`; `2ms: 6aa4144c41b41dbac0c7f261.jsonl[6561] _id=6abd00da485cab4c958655e3 ts=2026-09-30T12:30:19.3840000Z ~ 6aa4144c41b41dbac0c7f261.jsonl[6559] _id=6abd00da485cab4c958655e5 ts=2026-09-30T12:30:19.3860000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 99h 6m 
  - Evidence: 99h 6m: 6aa4144c41b41dbac0c7f261.jsonl[11012] _id=6abe7547485cab4c95a98460 ts=2026-10-01T14:59:19.8020000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11690] _id=6ac3e705de269131f9aeb3a5 ts=2026-10-05T18:05:57.8690000Z; 68h 17m: 6aa4144c41b41dbac0c7f261.jsonl[1316] _id=6ab6bfa0485cab4c955e5a13 ts=2026-09-25T18:38:24.4830000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1470] _id=6aba7ff7485cab4c9568f469 ts=2026-09-28T14:55:51.5700000Z; 24h 30m: 6aa4144c41b41dbac0c7f261.jsonl[575] _id=6ab56159485cab4c9553840b ts=2026-09-24T17:43:54.1230000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1102] _id=6ab6b9e4485cab4c955dce87 ts=2026-09-25T18:13:56.2700000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 98h 54m 
  - Evidence: 98h 54m: 6aa4144c41b41dbac0c7f261.jsonl[11556] _id=6abe7835485cab4c95a9e494 ts=2026-10-01T15:11:49.2300000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11694] _id=6ac3e70bde269131f9aeb40e ts=2026-10-05T18:06:02.7280000Z; 68h 14m: 6aa4144c41b41dbac0c7f261.jsonl[1375] _id=6ab6c079485cab4c955e6677 ts=2026-09-25T18:42:01.5170000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1466] _id=6aba8012485cab4c9568f485 ts=2026-09-28T14:56:18.9700000Z; 24h 24m: 6aa4144c41b41dbac0c7f261.jsonl[1094] _id=6ab56881485cab4c9554254c ts=2026-09-24T18:14:25.5520000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1318] _id=6ab6bfa4485cab4c955e5a77 ts=2026-09-25T18:38:28.8040000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 563 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f261.jsonl[14492] _id=6ac54085de269131f9b6af5d ts=2026-10-06T18:40:05.5700000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14621] _id=6ac54085de269131f9b6af61 ts=2026-10-06T18:40:05.5710000Z; 1ms: 6aa4144c41b41dbac0c7f261.jsonl[14522] _id=6ac53ffdde269131f9b69ee4 ts=2026-10-06T18:37:49.1850000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14523] _id=6ac53ffdde269131f9b69eea ts=2026-10-06T18:37:49.1860000Z; 1ms: 6aa4144c41b41dbac0c7f261.jsonl[14538] _id=6ac53fd8de269131f9b69a2f ts=2026-10-06T18:37:12.3350000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14540] _id=6ac53fd8de269131f9b69a33 ts=2026-10-06T18:37:12.3360000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 32m 
  - Evidence: 143h 32m: 6aa4144c41b41dbac0c7f261.jsonl[8771] _id=6abd6075485cab4c959292b2 ts=2026-09-30T19:18:13.7030000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14884] _id=6ac5430ede269131f9b6fe7d ts=2026-10-06T18:50:54.1990000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 98h 49m 
  - Evidence: 98h 49m: 6aa4144c41b41dbac0c7f261.jsonl[11682] _id=6abe7933485cab4c95aa063e ts=2026-10-01T15:16:03.8320000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11699] _id=6ac3e70bde269131f9aeb402 ts=2026-10-05T18:06:02.6310000Z; 68h 14m: 6aa4144c41b41dbac0c7f261.jsonl[1370] _id=6ab6c053485cab4c955e657b ts=2026-09-25T18:41:23.4850000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1473] _id=6aba7fff485cab4c9568f46f ts=2026-09-28T14:55:58.8970000Z; 24h 0m: 6aa4144c41b41dbac0c7f261.jsonl[1075] _id=6ab56863485cab4c955424f0 ts=2026-09-24T18:13:55.2570000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1103] _id=6ab6b9e5485cab4c955dcea1 ts=2026-09-25T18:13:56.8000000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 97 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f261.jsonl[3141] _id=6abaad61485cab4c956f8285 ts=2026-09-28T18:09:37.0850000Z -> 6aa4144c41b41dbac0c7f261.jsonl[3136] _id=6abaad61485cab4c956f828a ts=2026-09-28T18:09:37.0850000Z; 1ms: 6aa4144c41b41dbac0c7f261.jsonl[1103] _id=6ab6b9e5485cab4c955dcea1 ts=2026-09-25T18:13:56.8000000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1100] _id=6ab6b9e5485cab4c955dcea4 ts=2026-09-25T18:13:56.8010000Z; 1ms: 6aa4144c41b41dbac0c7f261.jsonl[12266] _id=6ac3eca4de269131f9af0faf ts=2026-10-05T18:29:56.2930000Z -> 6aa4144c41b41dbac0c7f261.jsonl[12267] _id=6ac3eca4de269131f9af0fb5 ts=2026-10-05T18:29:56.2940000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 98h 52m 
  - Evidence: 98h 52m: 6aa4144c41b41dbac0c7f261.jsonl[11638] _id=6abe78e2485cab4c95a9f8d6 ts=2026-10-01T15:14:42.6740000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11715] _id=6ac3e734de269131f9aeb59f ts=2026-10-05T18:06:44.3710000Z; 68h 19m: 6aa4144c41b41dbac0c7f261.jsonl[1311] _id=6ab6bf55485cab4c955e5517 ts=2026-09-25T18:37:09.6410000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1493] _id=6aba8038485cab4c9568f4a5 ts=2026-09-28T14:56:56.8480000Z; 24h 0m: 6aa4144c41b41dbac0c7f261.jsonl[1076] _id=6ab56864485cab4c955424f8 ts=2026-09-24T18:13:56.7600000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1106] _id=6ab6b9ea485cab4c955dcf45 ts=2026-09-25T18:14:02.5240000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.004s..0.009s shown 
  - Evidence: 4ms: 6aa4144c41b41dbac0c7f261.jsonl[98] _id=6ab418f8485cab4c954f425e ts=2026-09-23T18:22:48.4810000Z -> 6aa4144c41b41dbac0c7f261.jsonl[100] _id=6ab418f8485cab4c954f4260 ts=2026-09-23T18:22:48.4850000Z; 5ms: 6aa4144c41b41dbac0c7f261.jsonl[390] _id=6ab41b34485cab4c954f54d4 ts=2026-09-23T18:32:20.6540000Z -> 6aa4144c41b41dbac0c7f261.jsonl[389] _id=6ab41b34485cab4c954f54d6 ts=2026-09-23T18:32:20.6590000Z; 9ms: 6aa4144c41b41dbac0c7f261.jsonl[609] _id=6ab56188485cab4c95538943 ts=2026-09-24T17:44:41.0500000Z -> 6aa4144c41b41dbac0c7f261.jsonl[607] _id=6ab56188485cab4c95538945 ts=2026-09-24T17:44:41.0590000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 98h 49m 
  - Evidence: 98h 49m: 6aa4144c41b41dbac0c7f261.jsonl[11683] _id=6abe793a485cab4c95aa084a ts=2026-10-01T15:16:10.5420000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11696] _id=6ac3e70ade269131f9aeb3fe ts=2026-10-05T18:05:57.8750000Z; 68h 13m: 6aa4144c41b41dbac0c7f261.jsonl[1378] _id=6ab6c075485cab4c955e6663 ts=2026-09-25T18:41:57.3130000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1472] _id=6aba7fff485cab4c9568f46d ts=2026-09-28T14:55:51.5770000Z; 23h 59m: 6aa4144c41b41dbac0c7f261.jsonl[1090] _id=6ab56887485cab4c95542556 ts=2026-09-24T18:14:32.0530000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1099] _id=6ab6b9e5485cab4c955dce9f ts=2026-09-25T18:13:56.2750000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 100h 0m 
  - Evidence: 100h 0m: 6aa4144c41b41dbac0c7f261.jsonl[10674] _id=6abe720c485cab4c95a93da8 ts=2026-10-01T14:45:30.5860000Z -> 6aa4144c41b41dbac0c7f261.jsonl[12852] _id=6ac3f059de269131f9af5be7 ts=2026-10-05T18:45:45.0440000Z; 23h 26m: 6aa4144c41b41dbac0c7f261.jsonl[4534] _id=6abab661485cab4c95706d46 ts=2026-09-28T18:48:01.0040000Z -> 6aa4144c41b41dbac0c7f261.jsonl[4553] _id=6abc000b485cab4c95842cc3 ts=2026-09-29T18:14:34.2180000Z; 20h 21m: 6aa4144c41b41dbac0c7f261.jsonl[12866] _id=6ac3f05cde269131f9af5c63 ts=2026-10-05T18:45:47.9480000Z -> 6aa4144c41b41dbac0c7f261.jsonl[12894] _id=6ac50eb1de269131f9b435cc ts=2026-10-06T15:07:27.7080000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3502 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f261.jsonl[10002] _id=6abe568f485cab4c95a3eb37 ts=2026-10-01T12:48:14.8390000Z -> 6aa4144c41b41dbac0c7f261.jsonl[9991] _id=6abe568f485cab4c95a3eb39 ts=2026-10-01T12:48:14.8390000Z; 0ms: 6aa4144c41b41dbac0c7f261.jsonl[10003] _id=6abe5690485cab4c95a3eb3d ts=2026-10-01T12:48:14.8870000Z -> 6aa4144c41b41dbac0c7f261.jsonl[10007] _id=6abe5690485cab4c95a3eb3f ts=2026-10-01T12:48:14.8870000Z; 0ms: 6aa4144c41b41dbac0c7f261.jsonl[10004] _id=6abe5690485cab4c95a3eb41 ts=2026-10-01T12:48:14.9250000Z -> 6aa4144c41b41dbac0c7f261.jsonl[10005] _id=6abe5690485cab4c95a3eb43 ts=2026-10-01T12:48:14.9250000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 47h 37m 
  - Evidence: 47h 37m: 6aa4144c41b41dbac0c7f261.jsonl[4399] _id=6abab57e485cab4c957052e5 ts=2026-09-28T18:44:14.5400000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7593] _id=6abd533d485cab4c95914217 ts=2026-09-30T18:21:49.4860000Z; 16h 57m: 6aa4144c41b41dbac0c7f261.jsonl[9096] _id=6abd6759485cab4c959f0373 ts=2026-09-30T19:47:37.5890000Z -> 6aa4144c41b41dbac0c7f261.jsonl[9598] _id=6abe55b6485cab4c95a3dddb ts=2026-10-01T12:44:40.2160000Z; 1h 56m: 6aa4144c41b41dbac0c7f261.jsonl[9611] _id=6abe55d5485cab4c95a3debd ts=2026-10-01T12:45:10.8150000Z -> 6aa4144c41b41dbac0c7f261.jsonl[10199] _id=6abe713d485cab4c95a911d2 ts=2026-10-01T14:42:05.9490000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 116h 30m 
  - Evidence: 116h 30m: 6aa4144c41b41dbac0c7f261.jsonl[247] _id=6ab41a41485cab4c954f4e94 ts=2026-09-23T18:28:17.3810000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1579] _id=6aba808a485cab4c9568f54d ts=2026-09-28T14:58:18.2030000Z; 42h 5m: 6aa4144c41b41dbac0c7f261.jsonl[4170] _id=6abab296485cab4c957012d1 ts=2026-09-28T18:31:50.0660000Z -> 6aa4144c41b41dbac0c7f261.jsonl[6650] _id=6abd0296485cab4c95865d47 ts=2026-09-30T12:37:42.9820000Z; 6h 17m: 6aa4144c41b41dbac0c7f261.jsonl[6658] _id=6abd02a1485cab4c95865d95 ts=2026-09-30T12:37:53.6240000Z -> 6aa4144c41b41dbac0c7f261.jsonl[8502] _id=6abd5b03485cab4c95922d39 ts=2026-09-30T18:54:59.6800000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.023s shown 
  - Evidence: 20ms: 6aa4144c41b41dbac0c7f261.jsonl[4081] _id=6abab176485cab4c956ffddd ts=2026-09-28T18:27:02.9050000Z -> 6aa4144c41b41dbac0c7f261.jsonl[4083] _id=6abab177485cab4c956ffde3 ts=2026-09-28T18:27:02.9250000Z; 23ms: 6aa4144c41b41dbac0c7f261.jsonl[4083] _id=6abab177485cab4c956ffde3 ts=2026-09-28T18:27:02.9250000Z -> 6aa4144c41b41dbac0c7f261.jsonl[4086] _id=6abab177485cab4c956ffdfb ts=2026-09-28T18:27:02.9480000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 18m 
  - Evidence: 144h 18m: 6aa4144c41b41dbac0c7f261.jsonl[7488] _id=6abd528a485cab4c9591252d ts=2026-09-30T18:18:50.3660000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14537] _id=6ac53fd8de269131f9b69a2a ts=2026-10-06T18:37:12.3020000Z; 144h 6m: 6aa4144c41b41dbac0c7f261.jsonl[987] _id=6ab567bf485cab4c95541fee ts=2026-09-24T18:11:11.4210000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7434] _id=6abd5240485cab4c95911a53 ts=2026-09-30T18:17:36.6700000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 17m 
  - Evidence: 144h 17m: 6aa4144c41b41dbac0c7f261.jsonl[7474] _id=6abd528a485cab4c95912539 ts=2026-09-30T18:18:50.4120000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14508] _id=6ac53fc0de269131f9b6981f ts=2026-10-06T18:36:48.9540000Z; 144h 5m: 6aa4144c41b41dbac0c7f261.jsonl[985] _id=6ab567bf485cab4c95541ff2 ts=2026-09-24T18:11:11.4600000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7362] _id=6abd520c485cab4c9591138d ts=2026-09-30T18:16:44.9580000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.022s..0.022s shown 
  - Evidence: 22ms: 6aa4144c41b41dbac0c7f261.jsonl[7472] _id=6abd528a485cab4c9591252f ts=2026-09-30T18:18:50.3900000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7474] _id=6abd528a485cab4c95912539 ts=2026-09-30T18:18:50.4120000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 18m 
  - Evidence: 144h 18m: 6aa4144c41b41dbac0c7f261.jsonl[7333] _id=6abd527b485cab4c95912329 ts=2026-09-30T18:18:35.8320000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14511] _id=6ac53fc4de269131f9b6985d ts=2026-10-06T18:36:52.2310000Z; 144h 5m: 6aa4144c41b41dbac0c7f261.jsonl[983] _id=6ab567b3485cab4c95541f9a ts=2026-09-24T18:10:59.9950000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7365] _id=6abd5215485cab4c959114ab ts=2026-09-30T18:16:53.0740000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 44 interval(s) ≤ 0.017s..0.021s shown 
  - Evidence: 17ms: 6aa4144c41b41dbac0c7f261.jsonl[7451] _id=6abd5253485cab4c95911d63 ts=2026-09-30T18:17:55.2360000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7456] _id=6abd5253485cab4c95911d67 ts=2026-09-30T18:17:55.2530000Z; 18ms: 6aa4144c41b41dbac0c7f261.jsonl[7367] _id=6abd5216485cab4c959114d9 ts=2026-09-30T18:16:54.7680000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7368] _id=6abd5216485cab4c959114db ts=2026-09-30T18:16:54.7860000Z; 21ms: 6aa4144c41b41dbac0c7f261.jsonl[7335] _id=6abd527b485cab4c95912325 ts=2026-09-30T18:18:35.8110000Z -> 6aa4144c41b41dbac0c7f261.jsonl[7333] _id=6abd527b485cab4c95912329 ts=2026-09-30T18:18:35.8320000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 288h 18m 
  - Evidence: 288h 18m: 6aa4144c41b41dbac0c7f261.jsonl[236] _id=6ab41a19485cab4c954f4d84 ts=2026-09-23T18:27:38.0770000Z -> 6aa4144c41b41dbac0c7f261.jsonl[12849] _id=6ac3f052de269131f9af5b23 ts=2026-10-05T18:45:38.8510000Z; 20h 21m: 6aa4144c41b41dbac0c7f261.jsonl[12849] _id=6ac3f052de269131f9af5b23 ts=2026-10-05T18:45:38.8510000Z -> 6aa4144c41b41dbac0c7f261.jsonl[12888] _id=6ac50ea6de269131f9b434a1 ts=2026-10-06T15:07:18.3490000Z; 2h 57m: 6aa4144c41b41dbac0c7f261.jsonl[12888] _id=6ac50ea6de269131f9b434a1 ts=2026-10-06T15:07:18.3490000Z -> 6aa4144c41b41dbac0c7f261.jsonl[13412] _id=6ac5385bde269131f9b61c05 ts=2026-10-06T18:05:15.2360000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 99h 6m 
  - Evidence: 99h 6m: 6aa4144c41b41dbac0c7f261.jsonl[11180] _id=6abe7543485cab4c95a98439 ts=2026-10-01T14:59:14.9260000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11689] _id=6ac3e6f6de269131f9aeb2b7 ts=2026-10-05T18:05:42.6450000Z; 68h 17m: 6aa4144c41b41dbac0c7f261.jsonl[1314] _id=6ab6bf83485cab4c955e57ff ts=2026-09-25T18:37:55.5750000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1458] _id=6aba7fed485cab4c9568f467 ts=2026-09-28T14:55:40.8560000Z; 24h 30m: 6aa4144c41b41dbac0c7f261.jsonl[569] _id=6ab5612a485cab4c95537f49 ts=2026-09-24T17:43:06.1680000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1098] _id=6ab6b9d7485cab4c955dcd47 ts=2026-09-25T18:13:43.0270000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 98h 49m 
  - Evidence: 98h 49m: 6aa4144c41b41dbac0c7f261.jsonl[11685] _id=6abe793e485cab4c95aa0927 ts=2026-10-01T15:16:14.2640000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11688] _id=6ac3e6f6de269131f9aeb2b3 ts=2026-10-05T18:05:42.6450000Z; 68h 17m: 6aa4144c41b41dbac0c7f261.jsonl[1315] _id=6ab6bf83485cab4c955e57fb ts=2026-09-25T18:37:55.5740000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1459] _id=6aba7fec485cab4c9568f465 ts=2026-09-28T14:55:40.8550000Z; 24h 19m: 6aa4144c41b41dbac0c7f261.jsonl[751] _id=6ab563d1485cab4c9553b888 ts=2026-09-24T17:54:25.3160000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1097] _id=6ab6b9d7485cab4c955dcd45 ts=2026-09-25T18:13:43.0260000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 99h 26m 
  - Evidence: 99h 26m: 6aa4144c41b41dbac0c7f261.jsonl[11680] _id=6abe793f485cab4c95aa0948 ts=2026-10-01T15:16:15.8050000Z -> 6aa4144c41b41dbac0c7f261.jsonl[12738] _id=6ac3ef94de269131f9af4a01 ts=2026-10-05T18:42:28.2070000Z; 68h 55m: 6aa4144c41b41dbac0c7f261.jsonl[1182] _id=6ab6bafc485cab4c955df5bd ts=2026-09-25T18:18:36.4370000Z -> 6aa4144c41b41dbac0c7f261.jsonl[3122] _id=6aba8433485cab4c95690217 ts=2026-09-28T15:13:55.8620000Z; 24h 24m: 6aa4144c41b41dbac0c7f261.jsonl[750] _id=6ab563d0485cab4c9553b880 ts=2026-09-24T17:54:24.7730000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1175] _id=6ab6baf1485cab4c955df455 ts=2026-09-25T18:18:25.2490000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.040s..0.040s shown 
  - Evidence: 40ms: 6aa4144c41b41dbac0c7f261.jsonl[5825] _id=6abc045f485cab4c95848a4b ts=2026-09-29T18:33:00.4520000Z -> 6aa4144c41b41dbac0c7f261.jsonl[5836] _id=6abc0460485cab4c95848a55 ts=2026-09-29T18:33:00.4920000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 98h 55m 
  - Evidence: 98h 55m: 6aa4144c41b41dbac0c7f261.jsonl[11529] _id=6abe77fa485cab4c95a9dd60 ts=2026-10-01T15:10:50.5190000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11700] _id=6ac3e70bde269131f9aeb409 ts=2026-10-05T18:06:02.6490000Z; 68h 15m: 6aa4144c41b41dbac0c7f261.jsonl[1354] _id=6ab6c033485cab4c955e647b ts=2026-09-25T18:40:51.7720000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1474] _id=6aba7fff485cab4c9568f471 ts=2026-09-28T14:55:58.9220000Z; 24h 26m: 6aa4144c41b41dbac0c7f261.jsonl[1077] _id=6ab56866485cab4c955424fe ts=2026-09-24T18:13:58.9060000Z -> 6aa4144c41b41dbac0c7f261.jsonl[1354] _id=6ab6c033485cab4c955e647b ts=2026-09-25T18:40:51.7720000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 21 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f261.jsonl[11804] _id=6ac3e826de269131f9aec6a9 ts=2026-10-05T18:10:46.2060000Z -> 6aa4144c41b41dbac0c7f261.jsonl[11805] _id=6ac3e826de269131f9aec6ad ts=2026-10-05T18:10:46.2070000Z; 1ms: 6aa4144c41b41dbac0c7f261.jsonl[14056] _id=6ac53adede269131f9b63bcd ts=2026-10-06T18:15:58.2580000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14047] _id=6ac53adede269131f9b63bcf ts=2026-10-06T18:15:58.2590000Z; 1ms: 6aa4144c41b41dbac0c7f261.jsonl[14657] _id=6ac540a9de269131f9b6b358 ts=2026-10-06T18:40:41.0590000Z -> 6aa4144c41b41dbac0c7f261.jsonl[14592] _id=6ac540a9de269131f9b6b361 ts=2026-10-06T18:40:41.0600000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[995] _id=6ab567e5485cab4c9554211a ts=2026-09-24T18:11:49.6210000Z`; `6aa4144c41b41dbac0c7f261.jsonl[5693] _id=6abc02f3485cab4c95846de1 ts=2026-09-29T18:26:59.3640000Z`; `6aa4144c41b41dbac0c7f261.jsonl[6427] _id=6abc070b485cab4c9584bb21 ts=2026-09-29T18:44:27.3760000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 133 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[1809] _id=6aba80ed485cab4c9568f727 ts=2026-09-28T14:59:56.5040000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1834] _id=6aba80f3485cab4c9568f739 ts=2026-09-28T15:00:01.7730000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1432] _id=6aba80f3485cab4c9568f73b ts=2026-09-28T15:00:01.8770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 341 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[1656] _id=6aba80e1485cab4c9568f611 ts=2026-09-28T14:57:57.4860000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1682] _id=6aba80e1485cab4c9568f615 ts=2026-09-28T14:57:57.4860000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1686] _id=6aba80e1485cab4c9568f623 ts=2026-09-28T14:57:57.5970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[7474] _id=6abd528a485cab4c95912539 ts=2026-09-30T18:18:50.4120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[7381] _id=6abd5220485cab4c9591163d ts=2026-09-30T18:17:04.2110000Z`; `6aa4144c41b41dbac0c7f261.jsonl[7451] _id=6abd5253485cab4c95911d63 ts=2026-09-30T18:17:55.2360000Z`; `6aa4144c41b41dbac0c7f261.jsonl[7456] _id=6abd5253485cab4c95911d67 ts=2026-09-30T18:17:55.2530000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[12849] _id=6ac3f052de269131f9af5b23 ts=2026-10-05T18:45:38.8510000Z`; `6aa4144c41b41dbac0c7f261.jsonl[12888] _id=6ac50ea6de269131f9b434a1 ts=2026-10-06T15:07:18.3490000Z`; `6aa4144c41b41dbac0c7f261.jsonl[13412] _id=6ac5385bde269131f9b61c05 ts=2026-10-06T18:05:15.2360000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[6486] _id=6abc076d485cab4c9584c0cb ts=2026-09-29T18:46:05.5400000Z`; `6aa4144c41b41dbac0c7f261.jsonl[10799] _id=6abe72d0485cab4c95a95dc0 ts=2026-10-01T14:48:48.7210000Z`; `6aa4144c41b41dbac0c7f261.jsonl[11191] _id=6abe7559485cab4c95a98560 ts=2026-10-01T14:59:37.6590000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 10 records 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[579] _id=6ab5615f485cab4c9553849f ts=?`; `6aa4144c41b41dbac0c7f261.jsonl[1179] _id=6ab6baf6485cab4c955df505 ts=?`; `6aa4144c41b41dbac0c7f261.jsonl[1471] _id=6aba7fff485cab4c9568f46b ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 892 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[1771] _id=6aba80e9485cab4c9568f6e1 ts=2026-09-28T14:59:50.0750000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1772] _id=6aba80e9485cab4c9568f6e3 ts=2026-09-28T14:59:50.0930000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1790] _id=6aba80e9485cab4c9568f6e5 ts=2026-09-28T14:59:50.0930000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1074 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[1683] _id=6aba80e1485cab4c9568f617 ts=2026-09-28T14:57:57.5290000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1688] _id=6aba80e2485cab4c9568f62b ts=2026-09-28T14:57:57.6760000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1702] _id=6aba80e2485cab4c9568f63f ts=2026-09-28T14:57:57.7580000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[4083] _id=6abab177485cab4c956ffde3 ts=2026-09-28T18:27:02.9250000Z`; `6aa4144c41b41dbac0c7f261.jsonl[4086] _id=6abab177485cab4c956ffdfb ts=2026-09-28T18:27:02.9480000Z`; `6aa4144c41b41dbac0c7f261.jsonl[4139] _id=6abab21d485cab4c95700a47 ts=2026-09-28T18:29:49.6490000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 13 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[7491] _id=6abd525c485cab4c95911eb1 ts=2026-09-30T18:18:03.9000000Z`; `6aa4144c41b41dbac0c7f261.jsonl[7331] _id=6abd527a485cab4c959122ed ts=2026-09-30T18:18:34.1920000Z`; `6aa4144c41b41dbac0c7f261.jsonl[7334] _id=6abd527b485cab4c9591231d ts=2026-09-30T18:18:35.5660000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 392 start, 378 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 176 unmatched 'BecameCameraCentered' (totals: 1272 open, 1229 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 121 unmatched 'BecameVisible' (totals: 1558 open, 1778 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 11 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 110 open, 111 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 27 unmatched 'questActiveEvent' (totals: 61 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 414 of 14875 adjacent _id pairs reverse in client time; worst 107.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f261.jsonl[1631] _id=6aba80dd485cab4c9568f5c9 ts=2026-09-28T14:59:41.7380000Z`; `6aa4144c41b41dbac0c7f261.jsonl[1627] _id=6aba80de485cab4c9568f5cb ts=2026-09-28T14:57:54.2460000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -109.51s, max +2.73s over 14876 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f261\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 10 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 5837 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3421); Unit 4 Dev (1208); Unit 5 Dev - Dungeon (878); Unit 3 Dungeon Dev (330)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.63s, n=5836)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5837/5837 records)
    "BecameInvisible"  x1778
    "BecameVisible"  x1558
    "BecameCameraCentered"  x1272
    "BecameCameraUncentered"  x1229
data.pieceId  (string, 5837/5837 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5837/5837 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3555 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1293); Unit 2 Prod (Refactor) (587); Unit 1 Dev (478); Unit 3 Dev (474); Unit 5 Dev - Dungeon (256); Unit 4 Dev (218); Unit 3 Dungeon Dev (213); Unit 5 Dev (36)
- **Intervals:** median 1.46s (p5 0.13s / p95 22.86s, n=3554)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3555/3555 records)
    "pressed"  x3555
data.actionType  (string, 3555/3555 records)
    "Move"  x2440
    "Interact"  x694
    "Jump"  x251
    "Sprint"  x101
    "Hoverboard"  x44
    "Pause"  x14
    "SkipCinematic"  x7
    "Ascend"  x3
    "Descend"  x1
data.key  (string, 3555/3555 records)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3555/3555 records)
    "Player"  x3258
    "Drone"  x297
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2383 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (548); Unit 4 Dev - Dungeon (429); Unit 1 Dev (419); Unit 3 Dev (392); Unit 5 Dev - Dungeon (198); Unit 4 Dev (172); Unit 5 Dev (121); Unit 3 Dungeon Dev (104)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2370)
- **Fields under `data`:**

```text
data.position  (object, 2383/2383 records)
data.position.x  (number, 2383/2383 records)
    numeric range -753.149 .. 1403.94 (854 unique)
data.position.y  (number, 2383/2383 records)
    numeric range -112.489 .. 222.405 (542 unique)
data.position.z  (number, 2383/2383 records)
    numeric range -1035.84 .. 2135.52 (856 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1913 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (473); Unit 3 Dev (340); Unit 1 Dev (278); Unit 5 Dev (239); Unit 4 Dev - Dungeon (230); Unit 4 Dev (125); Unit 5 Dev - Dungeon (115); Unit 3 Dungeon Dev (113)
- **eventKey:** present on 1143 of 1913 records
- **Intervals:** median 4.38s (p5 0.00s / p95 52.73s, n=1912)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1143; [conversationId, dialogueEventType] x770
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1913/1913 records)
    numeric range 10 .. 118 (45 unique)
data.dialogueEventType  (string, 1913/1913 records)
    "DialogueNodeEvent"  x1143
    "DialogueStartEvent"  x392
    "DialogueFinishEvent"  x378
data.nodeId  (number, 1143/1913 records)
    numeric range 0 .. 289 (206 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 443 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (217); Unit 2 Prod (Refactor) (74); Unit 1 Dev (63); Unit 3 Dungeon Dev (34); Unit 5 Dev - Dungeon (22); Unit 4 Dev (16); Unit 3 Dev (10); Unit 5 Dev (7)
- **Intervals:** median 8.16s (p5 0.17s / p95 394.92s, n=442)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 443/443 records)
    31 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 443/443 records)
    80 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 254 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (133); Unit 5 Dev (78); Unit 1 Dev (43)
- **Intervals:** median 0.39s (p5 0.03s / p95 4.29s, n=253)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 254/254 records)
    "argumentationNodeHoverEnd"  x111
    "argumentationNodeHoverStart"  x110
    "argumentationNodeAdd"  x22
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 254/254 records)
    "Unit 3 - Pollution Upstream"  x133
    "Unit 5"  x78
    "Unit 1 - Freshwater"  x29
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 254/254 records)
    "A"  x51
    "B"  x43
    "1"  x41
    "I"  x32
    "2"  x24
    "II"  x19
    "5"  x17
    "3"  x11
    "4"  x8
    "C"  x5
    "D"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 101 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (24); Unit 2 Prod (Refactor) (20); Unit 1 Dev (19); Unit 3 Dev (15); Unit 5 Dev - Dungeon (10); Unit 5 Dev (7); Unit 4 Dev (4); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 101 of 101 records
- **Intervals:** median 252.85s (p5 0.00s / p95 73788.91s, n=100)
- **`data` key-set variants:** [questEventType, questID, questName] x61; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 101/101 records)
    "questActiveEvent"  x61
    "questFinishEvent"  x40
data.questID  (string, 101/101 records)
    29 unique values (see csv/event_unique_values.csv)
data.questName  (string, 101/101 records)
    29 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/101 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 90 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (54); Unit 2 Prod (Refactor) (22); Unit 3 Dev (14)
- **Intervals:** median 1.61s (p5 0.19s / p95 1344.66s, n=89)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x76; [Soil Key Puzzle Status, Unit] x14
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 14/90 records)
    "Finished"  x7
    "Started"  x7
data.Unit  (string, 14/90 records)
    "Unit 4 Dev"  x8
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 76/90 records)
    "RightDrag"  x41
    "LeftDrag"  x35
data.currentSoilType  (string, 76/90 records)
    "CLAYSAND"  x21
    "CLAY"  x20
    "CLAYROCK"  x14
    "SAND"  x14
    "BEDROCK"  x3
    "SANDGRAVEL"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 76/90 records)
    "false"  x54
    "true"  x22
data.waterLevelStatus  (string, 76/90 records)
    "TooHigh"  x31
    "Proper"  x26
    "TooLow"  x19
data.waterRetentionChange  (string, 76/90 records)
    "Increase"  x37
    "NoChange"  x22
    "Decrease"  x17
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 48 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (28); Unit 1 Dev (8); Unit 4 Dev (4); Unit 4 Dev - Dungeon (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev - Dungeon (2); Transition (1)
- **Intervals:** median 471.04s (p5 9.85s / p95 87232.26s, n=47)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 48/48 records)
    true  x48
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 39 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (39)
- **Intervals:** median 3.21s (p5 1.06s / p95 188.92s, n=38)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "ChangeCanister"  x39
data.canisterType  (string, 39/39 records)
    "Clay"  x21
    "Bedrock"  x13
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 39/39 records)
    "5"  x31
    "4"  x7
    "3"  x1
data.machine  (string, 39/39 records)
    "1"  x39
data.row  (string, 39/39 records)
    "TopRow"  x23
    "BottomRow"  x16
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 38 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (38)
- **Intervals:** median 14.63s (p5 1.49s / p95 135.38s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "On"  x24
    "Off"  x14
data.floor  (string, 38/38 records)
    "4"  x19
    "3"  x10
    "1"  x6
    "2"  x3
data.machineNumber  (string, 38/38 records)
    "One"  x37
    "Two"  x1
data.machineType  (string, 38/38 records)
    "Condenser"  x20
    "Evaporator"  x15
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 38/38 records)
    "2"  x16
    "3"  x16
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 32 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (6); Unit 4 Dev - Dungeon (6); Unit 3 Dev (4); Unit 4 Dev (4); Unit 5 Dev - Dungeon (4); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1437.56s (p5 128.73s / p95 167024.62s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "DebugMenuStateChanged"  x32
data.isOpened  (bool, 32/32 records)
    false  x32
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 30 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (6); Unit 4 Dev (5); Unit 4 Dev - Dungeon (5); Unit 5 Dev - Dungeon (4); Transition (1); Unit 3 Dev (1)
- **Intervals:** median 977.08s (p5 1.19s / p95 184007.85s, n=29)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 28 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (28)
- **Intervals:** median 4302.75s (p5 116.25s / p95 198576.75s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 24 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (24)
- **Intervals:** median 2.13s (p5 0.21s / p95 25.69s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "Close"  x12
    "Open"  x12
data.toolName  (string, 24/24 records, 24 empty-string)
    ""  x24
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TopographicMapEvent` — 24 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (4); Unit 3 Dev (4)
- **Intervals:** median 10.64s (p5 0.08s / p95 138660.23s, n=23)
- **`data` key-set variants:** [actionType, featureUsed] x20; [actionType, featureUsed, location] x3; [actionType, featureUsed, legendName] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "MapOpenEvent"  x11
    "MapCloseEvent"  x9
    "WaypointSetEvent"  x2
    "Selected"  x1
    "WaypointMoveEvent"  x1
data.featureUsed  (string, 24/24 records)
    "Map"  x20
    "Waypoint"  x3
    "Legend"  x1
data.legendName  (string, 1/24 records)
    "240 ft"  x1
data.location  (object, 3/24 records)
data.location.x  (number, 3/24 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 3/24 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 3/24 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 15 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (6); Unit 3 Dev (5); Unit 1 Dev (4)
- **Intervals:** median 27.34s (p5 3.05s / p95 519036.09s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "submitAnswerEvent"  x15
data.answerSubmitted  (string, 15/15 records, 1 empty-string)
    "A,1,I"  x3
    "B,5,I"  x3
    "C,2,II"  x3
    "A,5,I"  x2
    ""  x1
    "B,1,I"  x1
    "C,D,2,II"  x1
    "C,D,3,II"  x1
data.argumentationTitle  (string, 15/15 records)
    "Unit 5"  x6
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `crash` — 10 records

- **Scenes:** <missing sceneName> (10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 10/10 records)
    true  x10
data.message  (string, 10/10 records)
    "A user gesture is required to request Pointer Lock."  x10
data.phase  (string, 10/10 records)
    "running"  x10
data.stack  (string, 10/10 records, 10 empty-string)
    ""  x10
data.type  (string, 10/10 records)
    "unhandled_rejection"  x10
data.unitId  (string, 10/10 records)
    "unit2"  x4
    "unit1"  x3
    "unit4"  x3
data.workspace  (string, 10/10 records)
    "mhs"  x10
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 102.28s (p5 15.84s / p95 519217.78s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 7 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (4); Unit 1 Dev (2); Unit 5 Dev (1)
- **Intervals:** median 5929.77s (p5 84.97s / p95 796735.45s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "Close"  x6
    "Open"  x1
data.chatID  (string, 7/7 records)
    "NA"  x6
    "[30-41, 30-97, 30-48, 30-49, 30-50]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 1.19s (p5 0.80s / p95 2.20s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted Out"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Cold"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 516760.50s (p5 516760.50s / p95 516760.50s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (1x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (13x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*