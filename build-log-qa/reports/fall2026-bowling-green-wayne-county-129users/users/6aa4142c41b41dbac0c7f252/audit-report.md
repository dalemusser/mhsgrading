# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f252

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f252
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f252.jsonl
- **Records:** 17129 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f252
- **Time span:** 2026-09-23T16:27:36.544000+00:00 .. 2026-10-06T17:06:52.950000+00:00 (312h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f252\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 17129 records, 7 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 108 INFO, 2 NOT_TESTED, 81 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8966 | 52.34 | 1 | 6 | 0 | 2026-09-23T16:27:52.410000+00:00 | 2026-10-06T17:06:27.392000+00:00 | 312h 38m |
| PuzzlePieceVisibleEvent | 3587 | 20.94 | 1 | 3 | 0 | 2026-09-24T16:23:18.013000+00:00 | 2026-10-06T16:55:03.576000+00:00 | 288h 31m |
| PlayerPositionEvent | 1865 | 10.89 | 1 | 6 | 0 | 2026-09-23T16:27:46.786000+00:00 | 2026-10-06T17:06:52.950000+00:00 | 312h 39m |
| DialogueEvent | 1748 | 10.2 | 1 | 6 | 1055 | 2026-09-23T16:28:09.248000+00:00 | 2026-10-06T17:06:37.355000+00:00 | 312h 38m |
| argumentationNodeEvent | 233 | 1.36 | 1 | 2 | 0 | 2026-09-23T17:02:18.572000+00:00 | 2026-10-05T16:46:33.794000+00:00 | 287h 44m |
| ObjectInterEvent | 212 | 1.24 | 1 | 6 | 0 | 2026-09-23T16:34:33.667000+00:00 | 2026-10-06T17:06:28.296000+00:00 | 312h 31m |
| Soil Key Puzzle | 162 | 0.95 | 1 | 3 | 0 | 2026-09-24T16:28:37.831000+00:00 | 2026-10-06T16:53:07.521000+00:00 | 288h 24m |
| TopographicMapEvent | 125 | 0.73 | 1 | 3 | 0 | 2026-09-24T16:23:38.293000+00:00 | 2026-10-06T16:44:16.248000+00:00 | 288h 20m |
| questEvent | 70 | 0.41 | 1 | 6 | 70 | 2026-09-23T16:28:09.192000+00:00 | 2026-10-06T17:06:17.536000+00:00 | 312h 38m |
| argumentationAnswerEvent | 32 | 0.19 | 1 | 2 | 0 | 2026-09-24T16:15:39.525000+00:00 | 2026-10-05T16:46:35.038000+00:00 | 264h 30m |
| gameWindowFocusEvent | 28 | 0.16 | 1 | 4 | 0 | 2026-09-23T16:27:36.544000+00:00 | 2026-10-06T16:47:27.758000+00:00 | 312h 19m |
| DEBUGMenu | 23 | 0.13 | 1 | 6 | 0 | 2026-09-23T16:27:46.776000+00:00 | 2026-10-06T16:55:17.342000+00:00 | 312h 27m |
| gameStartEvent | 19 | 0.11 | 1 | 1 | 0 | 2026-09-23T16:27:36.545000+00:00 | 2026-10-06T16:47:27.839000+00:00 | 312h 19m |
| gameWindowUnfocusEvent | 18 | 0.11 | 1 | 4 | 0 | 2026-09-23T17:03:58.052000+00:00 | 2026-10-05T17:06:31.562000+00:00 | 288h 2m |
| argumentationToolEvent | 13 | 0.08 | 1 | 2 | 0 | 2026-09-23T17:03:01.823000+00:00 | 2026-10-05T16:45:38.379000+00:00 | 287h 42m |
| argumentationEvent | 10 | 0.06 | 1 | 2 | 0 | 2026-09-24T16:14:14.205000+00:00 | 2026-10-05T16:46:35.078000+00:00 | 264h 32m |
| chatEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-09-30T16:41:04.511000+00:00 | 2026-09-30T16:41:19.070000+00:00 | 14.6s |
| crash | 5 | 0.03 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 4 | 0.02 | 1 | 1 | 0 | 2026-09-30T16:41:02.371000+00:00 | 2026-09-30T17:03:31.254000+00:00 | 22m 28s |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-24T16:18:55.707000+00:00 | 2026-10-06T16:47:16.390000+00:00 | 288h 28m |
| soilMachine | 1 | 0.01 | 1 | 1 | 0 | 2026-10-06T17:05:21.113000+00:00 | 2026-10-06T17:05:21.113000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 1038500.683s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 0.308s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 9.159s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.058s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3.385s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 574.705s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1610.272s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 8966 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to Pickup Canister; Press E to Plant Seed; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 4.3x vs baseline. 
  - Observed: 162 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 240 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.4x vs baseline. 
  - Observed: 32 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,I; A,3,I; A,4,I; B,1,I; B,1,II; B,3,I; B,3,II 
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
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-0, 10-199, 10-200, 10-202, 10-204]; [10-200, 10-202, 10-204, 10-38, 10-39, 10-211]; [10-211, 10-217, 10-218, 11-27, 11-29] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 36; 40; 41; 43; 44; 45; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 152 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[323] _id=6ab40042485cab4c954e6e50 ts=2026-09-23T16:37:22.4240000Z`; `6aa4142c41b41dbac0c7f252.jsonl[443] _id=6ab40175485cab4c954e7536 ts=2026-09-23T16:42:29.0560000Z`; `6aa4142c41b41dbac0c7f252.jsonl[527] _id=6ab403b5485cab4c954e809e ts=2026-09-23T16:52:05.4820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[6169] _id=6abbe770485cab4c9580c49f ts=2026-09-29T16:29:34.7750000Z`; `6aa4142c41b41dbac0c7f252.jsonl[15183] _id=6ac52667de269131f9b55b2c ts=2026-10-06T16:35:48.225Z`; `6aa4142c41b41dbac0c7f252.jsonl[15459] _id=6ac5267cde269131f9b55e95 ts=2026-10-06T16:40:51.683Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[9] _id=6ab3fdf8485cab4c954e60e0 ts=2026-09-23T16:27:36.5450000Z`; `6aa4142c41b41dbac0c7f252.jsonl[803] _id=6ab54bdb485cab4c9552df8f ts=2026-09-24T16:12:11.2970000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1081] _id=6ab54dc2485cab4c9552ed47 ts=2026-09-24T16:20:18.8160000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[2] _id=6ab3fdf8485cab4c954e60de ts=2026-09-23T16:27:36.5440000Z`; `6aa4142c41b41dbac0c7f252.jsonl[802] _id=6ab54bdb485cab4c9552df8d ts=2026-09-24T16:12:11.2960000Z`; `6aa4142c41b41dbac0c7f252.jsonl[809] _id=6ab54bef485cab4c9552dfcb ts=2026-09-24T16:12:30.3080000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[785] _id=6ab4067e485cab4c954e93b2 ts=2026-09-23T17:03:58.0520000Z`; `6aa4142c41b41dbac0c7f252.jsonl[804] _id=6ab54bef485cab4c9552dfc9 ts=2026-09-24T16:12:30.3040000Z`; `6aa4142c41b41dbac0c7f252.jsonl[3563] _id=6ab5544f485cab4c95534edb ts=2026-09-24T16:48:15.1640000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 14 of 125 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1218] _id=6ab54e8a485cab4c9552f743 ts=2026-09-24T16:23:38.2930000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1215] _id=6ab54e8b485cab4c9552f749 ts=2026-09-24T16:23:39.3170000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1210] _id=6ab54e8c485cab4c9552f74f ts=2026-09-24T16:23:40.1680000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8965 | 0.0 | 0.382 | 125.545 | 3.156 | 343575.313 | 0.48 | 710 | 11 |
| PuzzlePieceVisibleEvent | 3586 | 0.0 | 0.025 | 289.656 | 0.804 | 345292.284 | 0.21 | 2312 | 7 |
| PlayerPositionEvent | 1856 | 0.0 | 9.999 | 421.509 | 10.859 | 343486.325 | 0.14 | 1 | 7 |
| DialogueEvent | 1747 | 0.0 | 4.354 | 644.252 | 37.124 | 343502.075 | 0.09 | 485 | 10 |
| argumentationNodeEvent | 232 | 0.001 | 0.28 | 4464.893 | 7.518 | 606052.742 | 0.01 | 63 | 4 |
| ObjectInterEvent | 211 | 0.003 | 6.463 | 5332.297 | 539.301 | 343956.81 | 0.01 | 1 | 10 |
| Soil Key Puzzle | 161 | 0.049 | 0.308 | 6448.88 | 7.192 | 518273.629 | 0.01 | 1 | 4 |
| TopographicMapEvent | 124 | 0.017 | 3.235 | 8371.274 | 4837.187 | 345251.613 | 0.01 | 2 | 9 |
| questEvent | 69 | 0.002 | 212.052 | 16311.425 | 84441.999 | 343802.477 | 0.0 | 8 | 13 |
| argumentationAnswerEvent | 31 | 0.183 | 9.159 | 30717.92 | 172973.918 | 606078.169 | 0.0 | 0 | 3 |
| gameWindowFocusEvent | 27 | 17.183 | 574.705 | 41644.119 | 267474.344 | 345531.02 | 0.0 | 0 | 13 |
| DEBUGMenu | 22 | 48.113 | 1252.223 | 51129.571 | 330775.865 | 345478.255 | 0.0 | 0 | 14 |
| gameStartEvent | 18 | 47.784 | 1398.065 | 62466.183 | 345543.162 | 345611.958 | 0.0 | 0 | 11 |
| gameWindowUnfocusEvent | 17 | 0.198 | 1610.272 | 60997.265 | 345023.653 | 345969.342 | 0.0 | 0 | 11 |
| argumentationToolEvent | 12 | 0.491 | 2.058 | 86313.046 | 462728.703 | 606171.314 | 0.0 | 0 | 4 |
| argumentationEvent | 9 | 0.022 | 47.456 | 105815.653 | 501722.996 | 606050.787 | 0.0 | 2 | 3 |
| chatEvent | 5 | 0.48 | 3.385 | 2.912 | 4.678 | 4.89 | 20.61 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 3 | 1.998 | 2.983 | 449.628 | 1209.81 | 1343.902 | 0.13 | 0 | 1 |
| EndOfUnit | 1 | 1038500.683 | 1038500.683 | 1038500.683 | 1038500.683 | 1038500.683 | 0.0 | 0 | 1 |
| soilMachine | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 6 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[72] _id=6ab3ff3a485cab4c954e64ea ts=2026-09-23T16:32:59.0070000Z == 6aa4142c41b41dbac0c7f252.jsonl[95] _id=6ab3ff3b485cab4c954e64ec ts=2026-09-23T16:32:59.0070000Z`; `6aa4142c41b41dbac0c7f252.jsonl[6173] _id=6abbe770485cab4c9580c48f ts=2026-09-29T16:29:34.7290000Z == 6aa4142c41b41dbac0c7f252.jsonl[6174] _id=6abbe770485cab4c9580c491 ts=2026-09-29T16:29:34.7290000Z`; `6aa4142c41b41dbac0c7f252.jsonl[11896] _id=6ac3cfe6de269131f9ada97d ts=2026-10-05T16:27:18.6810000Z == 6aa4142c41b41dbac0c7f252.jsonl[11897] _id=6ac3cfe6de269131f9ada97f ts=2026-10-05T16:27:18.6810000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 239 group(s), 350 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1315] _id=6ab54ecb485cab4c9552f9f9 ts=2026-09-24T16:23:34.0880000Z == 6aa4142c41b41dbac0c7f252.jsonl[1316] _id=6ab54ecb485cab4c9552f9fb ts=2026-09-24T16:23:34.0880000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1308] _id=6ab54ecc485cab4c9552fa0f ts=2026-09-24T16:23:34.1470000Z == 6aa4142c41b41dbac0c7f252.jsonl[1320] _id=6ab54ecc485cab4c9552fa13 ts=2026-09-24T16:23:34.1470000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1385] _id=6ab54ed2485cab4c9552fac3 ts=2026-09-24T16:24:45.9280000Z == 6aa4142c41b41dbac0c7f252.jsonl[1386] _id=6ab54ed2485cab4c9552fac7 ts=2026-09-24T16:24:45.9280000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[10132] _id=6abe8895485cab4c95abd708 ts=? == 6aa4142c41b41dbac0c7f252.jsonl[11724] _id=6ac3ceaede269131f9ada3b5 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `583ms: 6aa4142c41b41dbac0c7f252.jsonl[222] _id=6ab3ff9c485cab4c954e6890 ts=2026-09-23T16:34:36.7620000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[178] _id=6ab3ff9d485cab4c954e6896 ts=2026-09-23T16:34:37.3450000Z`; `850ms: 6aa4142c41b41dbac0c7f252.jsonl[226] _id=6ab3ff9e485cab4c954e68ae ts=2026-09-23T16:34:38.9340000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[216] _id=6ab3ff9f485cab4c954e68b8 ts=2026-09-23T16:34:39.7840000Z`; `582ms: 6aa4142c41b41dbac0c7f252.jsonl[216] _id=6ab3ff9f485cab4c954e68b8 ts=2026-09-23T16:34:39.7840000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[227] _id=6ab3ffa0485cab4c954e68bc ts=2026-09-23T16:34:40.3660000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 785 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6aa4142c41b41dbac0c7f252.jsonl[1316] _id=6ab54ecb485cab4c9552f9fb ts=2026-09-24T16:23:34.0880000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[1317] _id=6ab54ecb485cab4c9552fa01 ts=2026-09-24T16:23:34.1150000Z`; `9ms: 6aa4142c41b41dbac0c7f252.jsonl[1317] _id=6ab54ecb485cab4c9552fa01 ts=2026-09-24T16:23:34.1150000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[1306] _id=6ab54ecc485cab4c9552fa07 ts=2026-09-24T16:23:34.1240000Z`; `9ms: 6aa4142c41b41dbac0c7f252.jsonl[1306] _id=6ab54ecc485cab4c9552fa07 ts=2026-09-24T16:23:34.1240000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[1318] _id=6ab54ecc485cab4c9552fa09 ts=2026-09-24T16:23:34.1330000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `360ms: 6aa4142c41b41dbac0c7f252.jsonl[5071] _id=6ab6a791485cab4c955d0113 ts=2026-09-25T16:55:46.1130000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[5076] _id=6ab6a792485cab4c955d0127 ts=2026-09-25T16:55:46.4730000Z`; `264ms: 6aa4142c41b41dbac0c7f252.jsonl[5075] _id=6ab6a792485cab4c955d011f ts=2026-09-25T16:55:46.3200000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[5049] _id=6ab6a792485cab4c955d012b ts=2026-09-25T16:55:46.5840000Z`; `266ms: 6aa4142c41b41dbac0c7f252.jsonl[5076] _id=6ab6a792485cab4c955d0127 ts=2026-09-25T16:55:46.4730000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[5050] _id=6ab6a792485cab4c955d0133 ts=2026-09-25T16:55:46.7390000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6aa4142c41b41dbac0c7f252.jsonl[3036] _id=6ab551f6485cab4c955325e5 ts=2026-09-24T16:38:14.1270000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[3038] _id=6ab551f6485cab4c955325ef ts=2026-09-24T16:38:14.1460000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `805ms: 6aa4142c41b41dbac0c7f252.jsonl[908] _id=6ab54cae485cab4c9552e351 ts=2026-09-24T16:15:42.3760000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[900] _id=6ab54caf485cab4c9552e353 ts=2026-09-24T16:15:43.1810000Z`; `549ms: 6aa4142c41b41dbac0c7f252.jsonl[924] _id=6ab54cb8485cab4c9552e3a7 ts=2026-09-24T16:15:52.3400000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[932] _id=6ab54cb8485cab4c9552e3ad ts=2026-09-24T16:15:52.8890000Z`; `649ms: 6aa4142c41b41dbac0c7f252.jsonl[932] _id=6ab54cb8485cab4c9552e3ad ts=2026-09-24T16:15:52.8890000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[933] _id=6ab54cb9485cab4c9552e3b3 ts=2026-09-24T16:15:53.5380000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa4142c41b41dbac0c7f252.jsonl[10961] _id=6abe8f60485cab4c95ac224b ts=2026-10-01T16:50:40.6430000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[10963] _id=6abe8f60485cab4c95ac2257 ts=2026-10-01T16:50:40.6650000Z`; `22ms: 6aa4142c41b41dbac0c7f252.jsonl[12678] _id=6ac3d46bde269131f9ae0bf5 ts=2026-10-05T16:46:35.0560000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[12612] _id=6ac3d46bde269131f9ae0bff ts=2026-10-05T16:46:35.0780000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 43 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `166ms: 6aa4142c41b41dbac0c7f252.jsonl[895] _id=6ab54cb2485cab4c9552e36f ts=2026-09-24T16:15:46.7060000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[896] _id=6ab54cb2485cab4c9552e373 ts=2026-09-24T16:15:46.8720000Z`; `521ms: 6aa4142c41b41dbac0c7f252.jsonl[916] _id=6ab54cb2485cab4c9552e371 ts=2026-09-24T16:15:46.7580000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[918] _id=6ab54cb3485cab4c9552e37b ts=2026-09-24T16:15:47.2790000Z`; `417ms: 6aa4142c41b41dbac0c7f252.jsonl[10813] _id=6abe8c1c485cab4c95ac1460 ts=2026-10-01T16:36:44.0400000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[10817] _id=6abe8c1c485cab4c95ac1464 ts=2026-10-01T16:36:44.4570000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `908ms: 6aa4142c41b41dbac0c7f252.jsonl[12604] _id=6ac3d42ede269131f9ae0410 ts=2026-10-05T16:45:34.6970000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[12605] _id=6ac3d42fde269131f9ae0439 ts=2026-10-05T16:45:35.6050000Z`; `491ms: 6aa4142c41b41dbac0c7f252.jsonl[12605] _id=6ac3d42fde269131f9ae0439 ts=2026-10-05T16:45:35.6050000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[12603] _id=6ac3d430de269131f9ae0449 ts=2026-10-05T16:45:36.0960000Z`; `621ms: 6aa4142c41b41dbac0c7f252.jsonl[12603] _id=6ac3d430de269131f9ae0449 ts=2026-10-05T16:45:36.0960000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[12599] _id=6ac3d430de269131f9ae0460 ts=2026-10-05T16:45:36.7170000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `198ms: 6aa4142c41b41dbac0c7f252.jsonl[9399] _id=6abd3ca5485cab4c958e91aa ts=2026-09-30T16:45:25.4910000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[9403] _id=6abd3ca5485cab4c958e91ae ts=2026-09-30T16:45:25.6890000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4142c41b41dbac0c7f252.jsonl[6169] _id=6abbe770485cab4c9580c49f ts=2026-09-29T16:29:34.7750000Z ~ 6aa4142c41b41dbac0c7f252.jsonl[6164] _id=6abbe770485cab4c9580c4a1 ts=2026-09-29T16:29:34.7780000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4142c41b41dbac0c7f252.jsonl[3598] _id=6ab6a1e1485cab4c955a18b1 ts=2026-09-25T16:31:29.7460000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6163] _id=6abbe767485cab4c9580c3de ts=2026-09-29T16:29:28.0010000Z; 95h 26m: 6aa4142c41b41dbac0c7f252.jsonl[11311] _id=6abe9076485cab4c95ac3062 ts=2026-10-01T16:55:18.3290000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11716] _id=6ac3cea9de269131f9ada3a9 ts=2026-10-05T16:22:01.0870000Z; 24h 11m: 6aa4142c41b41dbac0c7f252.jsonl[1082] _id=6ab54dc8485cab4c9552eda3 ts=2026-09-24T16:20:24.8380000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3598] _id=6ab6a1e1485cab4c955a18b1 ts=2026-09-25T16:31:29.7460000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22m 23s 
  - Evidence: 22m 23s: 6aa4142c41b41dbac0c7f252.jsonl[9114] _id=6abd3ba0485cab4c958e42cf ts=2026-09-30T16:41:04.3690000Z -> 6aa4142c41b41dbac0c7f252.jsonl[9992] _id=6abd40e0485cab4c958eee18 ts=2026-09-30T17:03:28.2710000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4142c41b41dbac0c7f252.jsonl[6155] _id=6ab6a9a0485cab4c955d3577 ts=2026-09-25T17:04:32.6710000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6167] _id=6abbe770485cab4c9580c497 ts=2026-09-29T16:29:34.7460000Z; 95h 17m: 6aa4142c41b41dbac0c7f252.jsonl[11691] _id=6abe9299485cab4c95ac40e2 ts=2026-10-01T17:04:25.0900000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11718] _id=6ac3ceb6de269131f9ada3d3 ts=2026-10-05T16:22:14.0650000Z; 23h 45m: 6aa4142c41b41dbac0c7f252.jsonl[3436] _id=6ab553f3485cab4c95534baf ts=2026-09-24T16:46:43.9390000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3687] _id=6ab6a21b485cab4c955a3e3b ts=2026-09-25T16:32:28.1580000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 485 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f252.jsonl[12644] _id=6ac3d455de269131f9ae090e ts=2026-10-05T16:46:12.9500000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12647] _id=6ac3d455de269131f9ae0911 ts=2026-10-05T16:46:12.9500000Z; 1ms: 6aa4142c41b41dbac0c7f252.jsonl[1056] _id=6ab54d48485cab4c9552e803 ts=2026-09-24T16:18:16.3950000Z -> 6aa4142c41b41dbac0c7f252.jsonl[1060] _id=6ab54d48485cab4c9552e805 ts=2026-09-24T16:18:16.3960000Z; 1ms: 6aa4142c41b41dbac0c7f252.jsonl[1065] _id=6ab54d4f485cab4c9552e83b ts=2026-09-24T16:18:23.5910000Z -> 6aa4142c41b41dbac0c7f252.jsonl[1062] _id=6ab54d4f485cab4c9552e83e ts=2026-09-24T16:18:23.5920000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 288h 28m 
  - Evidence: 288h 28m: 6aa4142c41b41dbac0c7f252.jsonl[1078] _id=6ab54d6f485cab4c9552e8f1 ts=2026-09-24T16:18:55.7070000Z -> 6aa4142c41b41dbac0c7f252.jsonl[15564] _id=6ac52684de269131f9b55ff3 ts=2026-10-06T16:47:16.39Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4142c41b41dbac0c7f252.jsonl[6114] _id=6ab6a957485cab4c955d2e0f ts=2026-09-25T17:03:19.4140000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6166] _id=6abbe770485cab4c9580c48b ts=2026-09-29T16:29:34.7270000Z; 95h 17m: 6aa4142c41b41dbac0c7f252.jsonl[11692] _id=6abe9299485cab4c95ac40e6 ts=2026-10-01T17:04:25.5980000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11726] _id=6ac3ceaede269131f9ada3b9 ts=2026-10-05T16:22:06.0360000Z; 23h 43m: 6aa4142c41b41dbac0c7f252.jsonl[3555] _id=6ab55442485cab4c95534ec7 ts=2026-09-24T16:48:02.4360000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3599] _id=6ab6a1e7485cab4c955a1ca1 ts=2026-09-25T16:31:35.6340000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 710 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f252.jsonl[11896] _id=6ac3cfe6de269131f9ada97d ts=2026-10-05T16:27:18.6810000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11897] _id=6ac3cfe6de269131f9ada97f ts=2026-10-05T16:27:18.6810000Z; 0ms: 6aa4142c41b41dbac0c7f252.jsonl[11901] _id=6ac3cfe6de269131f9ada981 ts=2026-10-05T16:27:18.6820000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11902] _id=6ac3cfe6de269131f9ada983 ts=2026-10-05T16:27:18.6820000Z; 0ms: 6aa4142c41b41dbac0c7f252.jsonl[13152] _id=6ac3d629de269131f9ae33b5 ts=2026-10-05T16:54:01.0360000Z -> 6aa4142c41b41dbac0c7f252.jsonl[13176] _id=6ac3d629de269131f9ae33bb ts=2026-10-05T16:54:01.0360000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 32m 
  - Evidence: 95h 32m: 6aa4142c41b41dbac0c7f252.jsonl[11581] _id=6abe90c9485cab4c95ac34ba ts=2026-10-01T16:56:41.4350000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11975] _id=6ac3d05ede269131f9adb623 ts=2026-10-05T16:29:18.2450000Z; 95h 28m: 6aa4142c41b41dbac0c7f252.jsonl[6011] _id=6ab6a94f485cab4c955d2cc1 ts=2026-09-25T17:03:11.3090000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6545] _id=6abbe7f1485cab4c9580d1f2 ts=2026-09-29T16:31:45.1200000Z; 24h 25m: 6aa4142c41b41dbac0c7f252.jsonl[2788] _id=6ab54fb5485cab4c95530c45 ts=2026-09-24T16:28:37.8350000Z -> 6aa4142c41b41dbac0c7f252.jsonl[5001] _id=6ab6a73b485cab4c955cf807 ts=2026-09-25T16:54:19.2660000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 6aa4142c41b41dbac0c7f252.jsonl[253] _id=6ab3ffd2485cab4c954e6ab2 ts=2026-09-23T16:35:30.8210000Z -> 6aa4142c41b41dbac0c7f252.jsonl[279] _id=6ab3ffd2485cab4c954e6ab6 ts=2026-09-23T16:35:30.8240000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4142c41b41dbac0c7f252.jsonl[6157] _id=6ab6a9a9485cab4c955d35c1 ts=2026-09-25T17:04:41.6820000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6172] _id=6abbe76f485cab4c9580c487 ts=2026-09-29T16:29:28.0070000Z; 23h 43m: 6aa4142c41b41dbac0c7f252.jsonl[3562] _id=6ab5544d485cab4c95534ed9 ts=2026-09-24T16:48:13.3120000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3600] _id=6ab6a1e7485cab4c955a1c85 ts=2026-09-25T16:31:29.7570000Z; 23h 16m: 6aa4142c41b41dbac0c7f252.jsonl[14411] _id=6ac3d911de269131f9ae7833 ts=2026-10-05T17:06:25.6280000Z -> 6aa4142c41b41dbac0c7f252.jsonl[14413] _id=6ac5206dde269131f9b4f3b4 ts=2026-10-06T16:23:04.4470000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f252.jsonl[7239] _id=6abbeced485cab4c958216b1 ts=2026-09-29T16:53:01.4670000Z -> 6aa4142c41b41dbac0c7f252.jsonl[7240] _id=6abbed00485cab4c95821ee1 ts=2026-09-29T16:53:01.467Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 54m 
  - Evidence: 95h 54m: 6aa4142c41b41dbac0c7f252.jsonl[11654] _id=6abe9156485cab4c95ac38aa ts=2026-10-01T16:58:59.7240000Z -> 6aa4142c41b41dbac0c7f252.jsonl[13166] _id=6ac3d621de269131f9ae3289 ts=2026-10-05T16:53:52.0080000Z; 95h 26m: 6aa4142c41b41dbac0c7f252.jsonl[6120] _id=6ab6a959485cab4c955d2e75 ts=2026-09-25T17:03:19.6840000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6175] _id=6abbe770485cab4c9580c4a5 ts=2026-09-29T16:29:35.1910000Z; 48h 17m: 6aa4142c41b41dbac0c7f252.jsonl[6824] _id=6abbe941485cab4c9580eb3b ts=2026-09-29T16:37:20.0630000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11316] _id=6abe907a485cab4c95ac3074 ts=2026-10-01T16:55:18.5610000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2312 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f252.jsonl[10896] _id=6abe907e485cab4c95ac3092 ts=2026-10-01T16:55:22.6380000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10897] _id=6abe907e485cab4c95ac3094 ts=2026-10-01T16:55:22.6380000Z; 0ms: 6aa4142c41b41dbac0c7f252.jsonl[10898] _id=6abe907e485cab4c95ac3098 ts=2026-10-01T16:55:25.9740000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10899] _id=6abe907f485cab4c95ac309a ts=2026-10-01T16:55:25.9740000Z; 0ms: 6aa4142c41b41dbac0c7f252.jsonl[10900] _id=6abe907f485cab4c95ac309e ts=2026-10-01T16:55:25.9760000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10776] _id=6abe907f485cab4c95ac30a2 ts=2026-10-01T16:55:25.9760000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 6aa4142c41b41dbac0c7f252.jsonl[5125] _id=6ab6a7be485cab4c955d03db ts=2026-09-25T16:56:30.2440000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11276] _id=6abe903f485cab4c95ac2e57 ts=2026-10-01T16:54:23.8730000Z; 95h 58m: 6aa4142c41b41dbac0c7f252.jsonl[11294] _id=6abe9052485cab4c95ac2f49 ts=2026-10-01T16:54:42.3270000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12978] _id=6ac3d5e7de269131f9ae2d59 ts=2026-10-05T16:52:55.0220000Z; 24h 25m: 6aa4142c41b41dbac0c7f252.jsonl[2789] _id=6ab54fb8485cab4c95530c77 ts=2026-09-24T16:28:40.8210000Z -> 6aa4142c41b41dbac0c7f252.jsonl[4993] _id=6ab6a73b485cab4c955cf7ff ts=2026-09-25T16:54:19.2610000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.049s..0.049s shown 
  - Evidence: 49ms: 6aa4142c41b41dbac0c7f252.jsonl[5118] _id=6ab6a7b7485cab4c955d0367 ts=2026-09-25T16:56:23.8170000Z -> 6aa4142c41b41dbac0c7f252.jsonl[5116] _id=6ab6a7b7485cab4c955d0369 ts=2026-09-25T16:56:23.8660000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 54m 
  - Evidence: 95h 54m: 6aa4142c41b41dbac0c7f252.jsonl[4952] _id=6ab6a710485cab4c955cf273 ts=2026-09-25T16:53:37.0930000Z -> 6aa4142c41b41dbac0c7f252.jsonl[7049] _id=6abbebb4485cab4c95818e7c ts=2026-09-29T16:47:48.7060000Z; 95h 33m: 6aa4142c41b41dbac0c7f252.jsonl[11310] _id=6abe9079485cab4c95ac3072 ts=2026-10-01T16:55:21.3530000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11967] _id=6ac3d04dde269131f9adb48f ts=2026-10-05T16:29:01.5590000Z; 23h 45m: 6aa4142c41b41dbac0c7f252.jsonl[3511] _id=6ab5541a485cab4c95534d3f ts=2026-09-24T16:47:22.5480000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3694] _id=6ab6a22c485cab4c955a4a21 ts=2026-09-25T16:32:45.1570000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.017s..0.019s shown 
  - Evidence: 17ms: 6aa4142c41b41dbac0c7f252.jsonl[3040] _id=6ab551f6485cab4c955325e3 ts=2026-09-24T16:38:14.1100000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3036] _id=6ab551f6485cab4c955325e5 ts=2026-09-24T16:38:14.1270000Z; 19ms: 6aa4142c41b41dbac0c7f252.jsonl[3036] _id=6ab551f6485cab4c955325e5 ts=2026-09-24T16:38:14.1270000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3038] _id=6ab551f6485cab4c955325ef ts=2026-09-24T16:38:14.1460000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 21m 
  - Evidence: 168h 21m: 6aa4142c41b41dbac0c7f252.jsonl[926] _id=6ab54cbe485cab4c9552e3d3 ts=2026-09-24T16:15:58.0540000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10857] _id=6abe8c3c485cab4c95ac151a ts=2026-10-01T16:37:16.2230000Z; 95h 54m: 6aa4142c41b41dbac0c7f252.jsonl[11051] _id=6abe8f60485cab4c95ac2249 ts=2026-10-01T16:50:40.5930000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12558] _id=6ac3d404de269131f9adffd1 ts=2026-10-05T16:44:52.8350000Z; 11m 35s: 6aa4142c41b41dbac0c7f252.jsonl[10863] _id=6abe8c3d485cab4c95ac1526 ts=2026-10-01T16:37:17.2400000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10911] _id=6abe8ef4485cab4c95ac1b73 ts=2026-10-01T16:48:52.8330000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 20m 
  - Evidence: 168h 20m: 6aa4142c41b41dbac0c7f252.jsonl[937] _id=6ab54cbe485cab4c9552e3d5 ts=2026-09-24T16:15:58.0720000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10815] _id=6abe8c20485cab4c95ac1476 ts=2026-10-01T16:36:48.8590000Z; 95h 53m: 6aa4142c41b41dbac0c7f252.jsonl[10963] _id=6abe8f60485cab4c95ac2257 ts=2026-10-01T16:50:40.6650000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12531] _id=6ac3d3f0de269131f9adfdfd ts=2026-10-05T16:44:31.9750000Z; 13m 51s: 6aa4142c41b41dbac0c7f252.jsonl[10815] _id=6abe8c20485cab4c95ac1476 ts=2026-10-01T16:36:48.8590000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10961] _id=6abe8f60485cab4c95ac224b ts=2026-10-01T16:50:40.6430000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.022s shown 
  - Evidence: 22ms: 6aa4142c41b41dbac0c7f252.jsonl[10961] _id=6abe8f60485cab4c95ac224b ts=2026-10-01T16:50:40.6430000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10963] _id=6abe8f60485cab4c95ac2257 ts=2026-10-01T16:50:40.6650000Z; 22ms: 6aa4142c41b41dbac0c7f252.jsonl[12678] _id=6ac3d46bde269131f9ae0bf5 ts=2026-10-05T16:46:35.0560000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12612] _id=6ac3d46bde269131f9ae0bff ts=2026-10-05T16:46:35.0780000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 20m 
  - Evidence: 168h 20m: 6aa4142c41b41dbac0c7f252.jsonl[922] _id=6ab54cb7485cab4c9552e399 ts=2026-09-24T16:15:51.2980000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10813] _id=6abe8c1c485cab4c95ac1460 ts=2026-10-01T16:36:44.0400000Z; 95h 53m: 6aa4142c41b41dbac0c7f252.jsonl[11050] _id=6abe8f5e485cab4c95ac223d ts=2026-10-01T16:50:38.5390000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12529] _id=6ac3d3ebde269131f9adfd8d ts=2026-10-05T16:44:27.7390000Z; 23h 13m: 6aa4142c41b41dbac0c7f252.jsonl[774] _id=6ab4061e485cab4c954e920a ts=2026-09-23T17:02:22.5130000Z -> 6aa4142c41b41dbac0c7f252.jsonl[909] _id=6ab54cb1485cab4c9552e361 ts=2026-09-24T16:15:45.2240000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 63 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f252.jsonl[12634] _id=6ac3d451de269131f9ae0894 ts=2026-10-05T16:46:09.4970000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12630] _id=6ac3d451de269131f9ae089b ts=2026-10-05T16:46:09.4980000Z; 1ms: 6aa4142c41b41dbac0c7f252.jsonl[12666] _id=6ac3d463de269131f9ae0ae5 ts=2026-10-05T16:46:27.3900000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12667] _id=6ac3d463de269131f9ae0ae9 ts=2026-10-05T16:46:27.3910000Z; 4ms: 6aa4142c41b41dbac0c7f252.jsonl[10944] _id=6abe8f0f485cab4c95ac1d53 ts=2026-10-01T16:49:19.4990000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10945] _id=6abe8f0f485cab4c95ac1d57 ts=2026-10-01T16:49:19.5030000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 22m 
  - Evidence: 168h 22m: 6aa4142c41b41dbac0c7f252.jsonl[884] _id=6ab54c5d485cab4c9552e1eb ts=2026-09-24T16:14:21.7390000Z -> 6aa4142c41b41dbac0c7f252.jsonl[10860] _id=6abe8c39485cab4c95ac1504 ts=2026-10-01T16:37:13.0530000Z; 95h 56m: 6aa4142c41b41dbac0c7f252.jsonl[10952] _id=6abe8f18485cab4c95ac1e8b ts=2026-10-01T16:49:28.1300000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12604] _id=6ac3d42ede269131f9ae0410 ts=2026-10-05T16:45:34.6970000Z; 23h 11m: 6aa4142c41b41dbac0c7f252.jsonl[788] _id=6ab40645485cab4c954e92d4 ts=2026-09-23T17:03:01.8230000Z -> 6aa4142c41b41dbac0c7f252.jsonl[880] _id=6ab54c56485cab4c9552e1d1 ts=2026-09-24T16:14:14.1680000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 6aa4142c41b41dbac0c7f252.jsonl[10119] _id=6abe8886485cab4c95abd6ea ts=2026-10-01T16:21:26.6860000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11715] _id=6ac3ce92de269131f9ada393 ts=2026-10-05T16:21:38.6440000Z; 95h 58m: 6aa4142c41b41dbac0c7f252.jsonl[3597] _id=6ab6a1a6485cab4c9559f2fa ts=2026-09-25T16:30:30.9100000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6162] _id=6abbe761485cab4c9580c385 ts=2026-09-29T16:29:21.9310000Z; 24h 10m: 6aa4142c41b41dbac0c7f252.jsonl[1081] _id=6ab54dc2485cab4c9552ed47 ts=2026-09-24T16:20:18.8160000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3597] _id=6ab6a1a6485cab4c9559f2fa ts=2026-09-25T16:30:30.9100000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 58m 
  - Evidence: 95h 58m: 6aa4142c41b41dbac0c7f252.jsonl[3596] _id=6ab6a1a6485cab4c9559f2db ts=2026-09-25T16:30:30.9100000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6161] _id=6abbe761485cab4c9580c383 ts=2026-09-29T16:29:21.9300000Z; 95h 46m: 6aa4142c41b41dbac0c7f252.jsonl[10780] _id=6abe8ba3485cab4c95ac11c2 ts=2026-10-01T16:34:43.3370000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11714] _id=6ac3ce92de269131f9ada391 ts=2026-10-05T16:21:38.6440000Z; 24h 10m: 6aa4142c41b41dbac0c7f252.jsonl[1080] _id=6ab54dc2485cab4c9552ed45 ts=2026-09-24T16:20:18.8140000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3596] _id=6ab6a1a6485cab4c9559f2db ts=2026-09-25T16:30:30.9100000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa4142c41b41dbac0c7f252.jsonl[10773] _id=6abe8b5b485cab4c95ac0f22 ts=2026-10-01T16:33:31.9480000Z -> 6aa4142c41b41dbac0c7f252.jsonl[12473] _id=6ac3d2cdde269131f9ade8e7 ts=2026-10-05T16:39:41.2900000Z; 95h 46m: 6aa4142c41b41dbac0c7f252.jsonl[6151] _id=6ab6a9a7485cab4c955d35b9 ts=2026-09-25T17:04:40.1130000Z -> 6aa4142c41b41dbac0c7f252.jsonl[7217] _id=6abbec7b485cab4c9581e3b3 ts=2026-09-29T16:51:07.3440000Z; 24h 16m: 6aa4142c41b41dbac0c7f252.jsonl[3563] _id=6ab5544f485cab4c95534edb ts=2026-09-24T16:48:15.1640000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6151] _id=6ab6a9a7485cab4c955d35b9 ts=2026-09-25T17:04:40.1130000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 30m 
  - Evidence: 95h 30m: 6aa4142c41b41dbac0c7f252.jsonl[11086] _id=6abe907f485cab4c95ac30ac ts=2026-10-01T16:55:27.9280000Z -> 6aa4142c41b41dbac0c7f252.jsonl[11766] _id=6ac3cf7ade269131f9ada675 ts=2026-10-05T16:25:30.4050000Z; 95h 25m: 6aa4142c41b41dbac0c7f252.jsonl[6139] _id=6ab6a973485cab4c955d325e ts=2026-09-25T17:03:47.6980000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6169] _id=6abbe770485cab4c9580c49f ts=2026-09-29T16:29:34.7750000Z; 23h 54m: 6aa4142c41b41dbac0c7f252.jsonl[3020] _id=6ab551bc485cab4c9553231e ts=2026-09-24T16:37:16.3260000Z -> 6aa4142c41b41dbac0c7f252.jsonl[3601] _id=6ab6a1e8485cab4c955a1cb2 ts=2026-09-25T16:31:35.6660000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f252.jsonl[848] _id=6ab54c0b485cab4c9552e09d ts=2026-09-24T16:12:59.5250000Z -> 6aa4142c41b41dbac0c7f252.jsonl[861] _id=6ab54c0b485cab4c9552e09f ts=2026-09-24T16:12:59.5270000Z; 3ms: 6aa4142c41b41dbac0c7f252.jsonl[16791] _id=6ac52990de269131f9b5f1f3 ts=2026-10-06T17:02:08.5410000Z -> 6aa4142c41b41dbac0c7f252.jsonl[16788] _id=6ac52990de269131f9b5f1f9 ts=2026-10-06T17:02:08.5440000Z; 3ms: 6aa4142c41b41dbac0c7f252.jsonl[6169] _id=6abbe770485cab4c9580c49f ts=2026-09-29T16:29:34.7750000Z -> 6aa4142c41b41dbac0c7f252.jsonl[6164] _id=6abbe770485cab4c9580c4a1 ts=2026-09-29T16:29:34.7780000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[721] _id=6ab405cb485cab4c954e8fce ts=2026-09-23T17:00:59.6200000Z`; `6aa4142c41b41dbac0c7f252.jsonl[3945] _id=6ab6a332485cab4c955af467 ts=2026-09-25T16:37:06.8960000Z`; `6aa4142c41b41dbac0c7f252.jsonl[6811] _id=6abbe8f5485cab4c9580e3bb ts=2026-09-29T16:36:05.2100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 215 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1392] _id=6ab54ed3485cab4c9552fae5 ts=2026-09-24T16:24:45.9780000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1394] _id=6ab54ed3485cab4c9552faef ts=2026-09-24T16:24:47.8050000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1395] _id=6ab54ed4485cab4c9552faf1 ts=2026-09-24T16:24:47.8180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 356 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1275] _id=6ab54ec7485cab4c9552f98b ts=2026-09-24T16:23:20.4740000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1280] _id=6ab54ec8485cab4c9552f99d ts=2026-09-24T16:23:20.5410000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1298] _id=6ab54eca485cab4c9552f9cc ts=2026-09-24T16:23:33.6870000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[15263] _id=6ac5266cde269131f9b55c05 ts=2026-10-06T16:37:00.674Z`; `6aa4142c41b41dbac0c7f252.jsonl[15258] _id=6ac5266dde269131f9b55c0d ts=2026-10-06T16:37:04.398Z`; `6aa4142c41b41dbac0c7f252.jsonl[15359] _id=6ac52674de269131f9b55d39 ts=2026-10-06T16:38:32.857Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[10963] _id=6abe8f60485cab4c95ac2257 ts=2026-10-01T16:50:40.6650000Z`; `6aa4142c41b41dbac0c7f252.jsonl[12612] _id=6ac3d46bde269131f9ae0bff ts=2026-10-05T16:46:35.0780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[10945] _id=6abe8f0f485cab4c95ac1d57 ts=2026-10-01T16:49:19.5030000Z`; `6aa4142c41b41dbac0c7f252.jsonl[10941] _id=6abe8f0f485cab4c95ac1d5b ts=2026-10-01T16:49:19.5500000Z`; `6aa4142c41b41dbac0c7f252.jsonl[12570] _id=6ac3d40dde269131f9ae00a0 ts=2026-10-05T16:45:00.9890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[807] _id=6ab54bee485cab4c9552dfc5 ts=?`; `6aa4142c41b41dbac0c7f252.jsonl[6170] _id=6abbe76e485cab4c9580c471 ts=?`; `6aa4142c41b41dbac0c7f252.jsonl[9409] _id=6abd3e32485cab4c958eb1f0 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 597 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1549] _id=6ab54ee7485cab4c9552fc95 ts=2026-09-24T16:25:09.0340000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1617] _id=6ab54ee9485cab4c9552fcd3 ts=2026-09-24T16:25:13.1180000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1618] _id=6ab54ee9485cab4c9552fcd7 ts=2026-09-24T16:25:13.3310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 650 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1281] _id=6ab54ec7485cab4c9552f98d ts=2026-09-24T16:23:20.4740000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1291] _id=6ab54ec8485cab4c9552f9a9 ts=2026-09-24T16:23:20.5640000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1295] _id=6ab54ec9485cab4c9552f9b7 ts=2026-09-24T16:23:21.0860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 33 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[3036] _id=6ab551f6485cab4c955325e5 ts=2026-09-24T16:38:14.1270000Z`; `6aa4142c41b41dbac0c7f252.jsonl[3038] _id=6ab551f6485cab4c955325ef ts=2026-09-24T16:38:14.1460000Z`; `6aa4142c41b41dbac0c7f252.jsonl[3275] _id=6ab5536c485cab4c955346d1 ts=2026-09-24T16:44:28.1300000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[12639] _id=6ac3d451de269131f9ae08a3 ts=2026-10-05T16:46:09.6900000Z`; `6aa4142c41b41dbac0c7f252.jsonl[12649] _id=6ac3d45ade269131f9ae09a3 ts=2026-10-05T16:46:18.1090000Z`; `6aa4142c41b41dbac0c7f252.jsonl[12671] _id=6ac3d462de269131f9ae0aab ts=2026-10-05T16:46:25.9880000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 10 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[880] _id=6ab54c56485cab4c9552e1d1 ts=2026-09-24T16:14:14.1680000Z`; `6aa4142c41b41dbac0c7f252.jsonl[10861] _id=6abe8c3b485cab4c95ac1512 ts=2026-10-01T16:37:15.6350000Z`; `6aa4142c41b41dbac0c7f252.jsonl[10951] _id=6abe8f16485cab4c95ac1e45 ts=2026-10-01T16:49:26.5960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 349 start, 344 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 197 unmatched 'BecameCameraCentered' (totals: 792 open, 810 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 143 unmatched 'BecameVisible' (totals: 886 open, 1099 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 96 open, 102 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'argumentationToolOpen' (totals: 12 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 45 start, 25 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 492 of 17123 adjacent _id pairs reverse in client time; worst 80.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f252.jsonl[1271] _id=6ab54ec6485cab4c9552f963 ts=2026-09-24T16:24:38.1300000Z`; `6aa4142c41b41dbac0c7f252.jsonl[1269] _id=6ab54ec7485cab4c9552f96f ts=2026-09-24T16:23:18.0130000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -1433.42s, max +0.89s over 17124 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f252\coverage.yaml

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
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
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

### `InputEvent` — 8966 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (3915); Unit 2 Prod (Refactor) (2475); Unit 3 Dungeon Dev (1355); Unit 4 Dev - Dungeon (553); Unit 1 Dev (523); Unit 4 Dev (145)
- **Intervals:** median 0.38s (p5 0.03s / p95 3.16s, n=8965)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 8966/8966 records)
    "pressed"  x8966
data.actionType  (string, 8966/8966 records)
    "Move"  x6566
    "Jump"  x1265
    "Interact"  x536
    "Sprint"  x269
    "Ascend"  x126
    "Descend"  x91
    "Map"  x44
    "Hoverboard"  x41
    "Pause"  x13
    "ToggleDebug"  x11
    "SkipCinematic"  x4
data.key  (string, 8966/8966 records, 29 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 8966/8966 records)
    "Player"  x7008
    "Drone"  x1958
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3587 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2481); Unit 3 Dungeon Dev (560); Unit 4 Dev (546)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.80s, n=3586)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3587/3587 records)
    "BecameInvisible"  x1099
    "BecameVisible"  x886
    "BecameCameraUncentered"  x810
    "BecameCameraCentered"  x792
data.pieceId  (string, 3587/3587 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3587/3587 records)
    1911 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1865 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (702); Unit 2 Prod (Refactor) (601); Unit 1 Dev (249); Unit 3 Dungeon Dev (197); Unit 4 Dev - Dungeon (70); Unit 4 Dev (46)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.86s, n=1856)
- **Fields under `data`:**

```text
data.position  (object, 1865/1865 records)
data.position.x  (number, 1865/1865 records)
    numeric range -666.751 .. 3515.03 (549 unique)
data.position.y  (number, 1865/1865 records)
    numeric range -57942 .. 435.648 (482 unique)
data.position.z  (number, 1865/1865 records)
    numeric range -1261.21 .. 2179.77 (549 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1748 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (714); Unit 2 Prod (Refactor) (499); Unit 1 Dev (210); Unit 3 Dungeon Dev (203); Unit 4 Dev - Dungeon (81); Unit 4 Dev (41)
- **eventKey:** present on 1055 of 1748 records
- **Intervals:** median 4.35s (p5 0.00s / p95 37.12s, n=1747)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1055; [conversationId, dialogueEventType] x693
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1748/1748 records)
    numeric range 8 .. 111 (36 unique)
data.dialogueEventType  (string, 1748/1748 records)
    "DialogueNodeEvent"  x1055
    "DialogueStartEvent"  x349
    "DialogueFinishEvent"  x344
data.nodeId  (number, 1055/1748 records)
    numeric range 0 .. 290 (191 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 233 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (210); Unit 1 Dev (23)
- **Intervals:** median 0.28s (p5 0.02s / p95 7.52s, n=232)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 233/233 records)
    "argumentationNodeHoverEnd"  x102
    "argumentationNodeHoverStart"  x96
    "argumentationNodeAdd"  x21
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 233/233 records)
    "Unit 3 - Pollution Upstream"  x210
    "Unit 1 - Freshwater"  x15
    "Unit 1 - Argumentation Tutorial"  x8
data.nodeName  (string, 233/233 records)
    "3"  x44
    "4"  x32
    "1"  x31
    "B"  x30
    "2"  x26
    "II"  x26
    "A"  x19
    "I"  x17
    "5"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 212 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (73); Unit 2 Prod (Refactor) (49); Unit 4 Dev - Dungeon (44); Unit 1 Dev (23); Unit 3 Dev (17); Unit 4 Dev (6)
- **Intervals:** median 6.46s (p5 1.15s / p95 539.30s, n=211)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 212/212 records)
    26 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 212/212 records)
    54 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 162 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (116); Unit 3 Dev (28); Unit 4 Dev (18)
- **Intervals:** median 0.31s (p5 0.11s / p95 7.19s, n=161)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x152; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/162 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/162 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 152/162 records)
    "RightDrag"  x80
    "LeftDrag"  x72
data.currentSoilType  (string, 152/162 records)
    "CLAYSAND"  x34
    "CLAY"  x31
    "SAND"  x28
    "SANDGRAVEL"  x24
    "CLAYROCK"  x18
    "GRAVEL"  x12
    "BEDROCK"  x5
data.isCorrectSelection  (string, 152/162 records)
    "false"  x121
    "true"  x31
data.waterLevelStatus  (string, 152/162 records)
    "Proper"  x70
    "TooHigh"  x64
    "TooLow"  x18
data.waterRetentionChange  (string, 152/162 records)
    "Increase"  x72
    "Decrease"  x49
    "NoChange"  x31
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 125 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (62); Unit 3 Dev (61); Unit 3 Dungeon Dev (2)
- **Intervals:** median 3.23s (p5 0.79s / p95 4837.19s, n=124)
- **`data` key-set variants:** [actionType, featureUsed] x82; [actionType, featureUsed, location] x29; [actionType, featureUsed, legendName] x14
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 125/125 records)
    "MapCloseEvent"  x47
    "MapOpenEvent"  x35
    "WaypointMoveEvent"  x21
    "Selected"  x13
    "WaypointSetEvent"  x8
    "Unselected"  x1
data.featureUsed  (string, 125/125 records)
    "Map"  x82
    "Waypoint"  x29
    "Legend"  x14
data.legendName  (string, 14/125 records)
    "0 ft"  x3
    "120 ft"  x2
    "240 ft"  x2
    "330 ft"  x2
    "90 ft"  x2
    "Water"  x2
    "360 ft"  x1
data.location  (object, 29/125 records)
data.location.x  (number, 29/125 records)
    numeric range -649.09 .. 133.91 (28 unique)
data.location.y  (number, 29/125 records)
    numeric range -288.5 .. 369.5 (28 unique)
data.location.z  (number, 29/125 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (19); Unit 1 Dev (15); Unit 4 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 4 Dev (1)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 212.05s (p5 0.00s / p95 84442.00s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x45; [questEventType, questID, questName, questSuccessOrFailure] x25
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x45
    "questFinishEvent"  x25
data.questID  (string, 70/70 records)
    20 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    20 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 25/70 records)
    "Succeeded"  x25
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 32 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (22); Unit 1 Dev (10)
- **Intervals:** median 9.16s (p5 0.18s / p95 172973.92s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "submitAnswerEvent"  x32
data.answerSubmitted  (string, 32/32 records, 3 empty-string)
    "A,1,I"  x11
    "A,3,I"  x4
    "A,4,I"  x4
    "B,3,II"  x4
    ""  x3
    "A,5,I"  x2
    "A,2,I"  x1
    "B,1,I"  x1
    "B,1,II"  x1
    "B,3,I"  x1
data.argumentationTitle  (string, 32/32 records)
    "Unit 3 - Pollution Upstream"  x22
    "Unit 1 - Freshwater"  x10
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 3 Dev (6); Unit 2 Prod (Refactor) (2); Unit 1 Dev (1)
- **Intervals:** median 574.71s (p5 17.79s / p95 267474.34s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (7); Unit 3 Dungeon Dev (3); Unit 1 Dev (2); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1252.22s (p5 85.34s / p95 330775.87s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 1398.07s (p5 78.63s / p95 345543.16s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 18 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (9); Unit 2 Prod (Refactor) (6); Unit 1 Dev (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1610.27s (p5 86.86s / p95 345023.65s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    false  x18
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (10); Unit 1 Dev (3)
- **Intervals:** median 2.06s (p5 0.56s / p95 462728.70s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x12
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 13/13 records)
    "Unit 3 - Pollution Upstream"  x10
    "Unit 1 - Argumentation Tutorial"  x3
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - Pollution Site Data"  x10
    "BackingInfoPanel - Argumentation"  x3
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (4)
- **Intervals:** median 47.46s (p5 0.02s / p95 501723.00s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (6)
- **Intervals:** median 3.38s (p5 0.78s / p95 4.68s, n=5)
- **`data` key-set variants:** [actionType, chatID] x4; [actionKey, chatID] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/6 records)
    "ScrollStop"  x2
data.actionType  (string, 4/6 records)
    "ScrollStart"  x2
    "Close"  x1
    "Open"  x1
data.chatID  (string, 6/6 records)
    "NA"  x3
    "[10-0, 10-199, 10-200, 10-202, 10-204]"  x1
    "[10-200, 10-202, 10-204, 10-38, 10-39, 10-211]"  x1
    "[10-211, 10-217, 10-218, 11-27, 11-29]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x1
    "Pointer is already locked."  x1
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 4 empty-string)
    ""  x4
    "TypeError: Permissions check failed"  x1
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit3"  x3
    "unit1"  x1
    "unit2"  x1
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 2.98s (p5 2.10s / p95 1209.81s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 1038500.68s (p5 1038500.68s / p95 1038500.68s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `soilMachine` — 1 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "ChangeCanister"  x1
data.canisterType  (string, 1/1 records)
    "Gravel"  x1
data.floor  (string, 1/1 records)
    "3"  x1
data.machine  (string, 1/1 records)
    "1"  x1
data.row  (string, 1/1 records)
    "TopRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (116 records)
- `TopographicMapEvent` data.actionType: "Selected" (13x); "Unselected" (1x); "WaypointMoveEvent" (21x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Legend" (14x); "Waypoint" (29x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*