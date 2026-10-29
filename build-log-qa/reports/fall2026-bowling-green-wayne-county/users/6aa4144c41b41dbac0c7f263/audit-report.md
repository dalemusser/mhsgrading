# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f263

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f263
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f263.jsonl
- **Records:** 9167 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f263
- **Time span:** 2026-09-23T18:15:47.847000+00:00 .. 2026-10-07T18:47:19.033000+00:00 (336h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f263\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **17 event types**, 9167 records, 8 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 78 INFO, 2 NOT_TESTED, 64 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3070 | 33.49 | 1 | 3 | 0 | 2026-09-24T17:58:01.959000+00:00 | 2026-10-05T18:43:21.902000+00:00 | 264h 45m |
| InputEvent | 2305 | 25.14 | 1 | 6 | 0 | 2026-09-23T18:16:03.700000+00:00 | 2026-10-07T18:47:15.998000+00:00 | 336h 31m |
| DialogueEvent | 1485 | 16.2 | 1 | 6 | 937 | 2026-09-23T18:16:20.542000+00:00 | 2026-10-07T18:47:17.490000+00:00 | 336h 30m |
| PlayerPositionEvent | 1450 | 15.82 | 1 | 6 | 0 | 2026-09-23T18:15:58.551000+00:00 | 2026-10-07T18:47:19.033000+00:00 | 336h 31m |
| ObjectInterEvent | 235 | 2.56 | 1 | 6 | 0 | 2026-09-23T18:24:47.594000+00:00 | 2026-10-07T18:47:17.498000+00:00 | 336h 22m |
| argumentationNodeEvent | 214 | 2.33 | 1 | 2 | 0 | 2026-09-23T18:44:03.542000+00:00 | 2026-09-30T18:30:16.907000+00:00 | 167h 46m |
| TopographicMapEvent | 151 | 1.65 | 1 | 3 | 0 | 2026-09-24T17:59:10.315000+00:00 | 2026-10-05T18:47:40.434000+00:00 | 264h 48m |
| Soil Key Puzzle | 108 | 1.18 | 1 | 3 | 0 | 2026-09-24T18:04:42.431000+00:00 | 2026-10-05T18:41:29.811000+00:00 | 264h 36m |
| questEvent | 57 | 0.62 | 1 | 6 | 57 | 2026-09-23T18:16:20.518000+00:00 | 2026-10-07T18:47:08.687000+00:00 | 336h 30m |
| gameWindowFocusEvent | 20 | 0.22 | 1 | 6 | 0 | 2026-09-23T18:15:47.847000+00:00 | 2026-10-07T18:34:22.614000+00:00 | 336h 18m |
| DEBUGMenu | 16 | 0.17 | 1 | 7 | 0 | 2026-09-23T18:15:58.544000+00:00 | 2026-10-07T18:34:29.015000+00:00 | 336h 18m |
| DaniEvent | 12 | 0.13 | 1 | 3 | 0 | 2026-09-28T18:42:28.216000+00:00 | 2026-10-05T18:47:44.411000+00:00 | 168h 5m |
| gameStartEvent | 12 | 0.13 | 1 | 1 | 0 | 2026-09-23T18:15:47.848000+00:00 | 2026-10-07T18:34:22.614000+00:00 | 336h 18m |
| argumentationAnswerEvent | 11 | 0.12 | 1 | 2 | 0 | 2026-09-24T17:46:23.030000+00:00 | 2026-09-30T18:30:18.616000+00:00 | 144h 43m |
| gameWindowUnfocusEvent | 10 | 0.11 | 1 | 6 | 0 | 2026-09-23T18:46:11.409000+00:00 | 2026-10-05T18:47:14.973000+00:00 | 288h 1m |
| argumentationEvent | 9 | 0.1 | 1 | 2 | 0 | 2026-09-23T18:45:14.501000+00:00 | 2026-09-30T18:30:18.683000+00:00 | 167h 45m |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-24T17:52:05.555000+00:00 | 2026-10-05T18:35:24.532000+00:00 | 264h 43m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1686.84s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 952998.977s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.306s median 
  - Expected: 0.583s in 09-23-26 
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
  - Observed: 17.172s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84296.635s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1769.43s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 82480.933s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Pick Up; Press E To Place Cameras; Press E To Scan; Press E to Pickup Canister; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 240 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,4,I; A,I; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 10 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 21 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[205] _id=6ab41a03485cab4c954f4ce4 ts=2026-09-23T18:27:15.9000000Z`; `6aa4144c41b41dbac0c7f263.jsonl[274] _id=6ab41b39485cab4c954f5508 ts=2026-09-23T18:32:25.9180000Z`; `6aa4144c41b41dbac0c7f263.jsonl[335] _id=6ab41bd0485cab4c954f59fb ts=2026-09-23T18:34:56.6800000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[4093] _id=6abaac96485cab4c956f6f49 ts=2026-09-28T18:06:12.6430000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[17] _id=6ab41753485cab4c954f36bc ts=2026-09-23T18:15:47.8480000Z`; `6aa4144c41b41dbac0c7f263.jsonl[635] _id=6ab5609c485cab4c95537567 ts=2026-09-24T17:40:44.4830000Z`; `6aa4144c41b41dbac0c7f263.jsonl[647] _id=6ab560d7485cab4c95537a8d ts=2026-09-24T17:41:43.7040000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[15] _id=6ab41753485cab4c954f36ba ts=2026-09-23T18:15:47.8470000Z`; `6aa4144c41b41dbac0c7f263.jsonl[633] _id=6ab41e73485cab4c954f70f3 ts=2026-09-23T18:46:11.4220000Z`; `6aa4144c41b41dbac0c7f263.jsonl[634] _id=6ab5609c485cab4c95537565 ts=2026-09-24T17:40:44.4820000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[632] _id=6ab41e73485cab4c954f70f1 ts=2026-09-23T18:46:11.4090000Z`; `6aa4144c41b41dbac0c7f263.jsonl[638] _id=6ab560a4485cab4c95537673 ts=2026-09-24T17:40:52.3420000Z`; `6aa4144c41b41dbac0c7f263.jsonl[650] _id=6ab560cb485cab4c95537a21 ts=2026-09-24T17:41:31.1280000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 50 of 151 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1136] _id=6ab564ee485cab4c9553cf20 ts=2026-09-24T17:59:10.3150000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1139] _id=6ab564f6485cab4c9553cff0 ts=2026-09-24T17:59:18.3570000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1142] _id=6ab564f7485cab4c9553d008 ts=2026-09-24T17:59:19.4660000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3069 | 0.0 | 0.03 | 310.564 | 1.195 | 356691.739 | 0.19 | 1947 | 7 |
| InputEvent | 2304 | 0.0 | 1.306 | 525.813 | 17.473 | 355900.061 | 0.11 | 47 | 8 |
| DialogueEvent | 1484 | 0.001 | 3.931 | 816.346 | 37.93 | 355930.874 | 0.07 | 414 | 7 |
| PlayerPositionEvent | 1443 | 8.086 | 10.0 | 839.432 | 10.034 | 355887.46 | 0.07 | 0 | 7 |
| ObjectInterEvent | 234 | 0.005 | 6.886 | 5175.0 | 360.414 | 356078.876 | 0.01 | 1 | 10 |
| argumentationNodeEvent | 213 | 0.002 | 0.414 | 2835.556 | 9.859 | 520749.469 | 0.02 | 42 | 2 |
| TopographicMapEvent | 150 | 0.023 | 1.977 | 6355.401 | 386.773 | 431790.474 | 0.01 | 2 | 6 |
| Soil Key Puzzle | 107 | 0.133 | 0.831 | 8902.873 | 13.284 | 432375.862 | 0.01 | 0 | 3 |
| questEvent | 56 | 0.003 | 223.87 | 21633.003 | 171996.931 | 356765.196 | 0.0 | 9 | 11 |
| gameWindowFocusEvent | 19 | 9.177 | 1769.43 | 63721.83 | 268540.726 | 355884.438 | 0.0 | 0 | 13 |
| DEBUGMenu | 15 | 7.171 | 1686.84 | 80714.031 | 288349.982 | 356766.617 | 0.0 | 0 | 11 |
| DaniEvent | 11 | 0.007 | 2.54 | 55010.563 | 301736.708 | 432121.745 | 0.0 | 2 | 3 |
| gameStartEvent | 11 | 59.221 | 84296.635 | 110064.979 | 307914.281 | 356767.002 | 0.0 | 0 | 9 |
| argumentationAnswerEvent | 10 | 2.998 | 17.172 | 52103.559 | 286487.693 | 520801.269 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 9 | 38.786 | 82480.933 | 115207.063 | 318589.119 | 358406.992 | 0.0 | 0 | 8 |
| argumentationEvent | 8 | 0.049 | 73.71 | 75488.023 | 367448.596 | 520732.095 | 0.0 | 1 | 2 |
| EndOfUnit | 1 | 952998.977 | 952998.977 | 952998.977 | 952998.977 | 952998.977 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 11 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[7512] _id=6ac3e9c0de269131f9aed9a7 ts=2026-10-05T18:17:36.0240000Z == 6aa4144c41b41dbac0c7f263.jsonl[7513] _id=6ac3e9c0de269131f9aed9ad ts=2026-10-05T18:17:36.0240000Z`; `6aa4144c41b41dbac0c7f263.jsonl[8672] _id=6ac690bade269131f9bdc49d ts=2026-10-07T18:34:34.5810000Z == 6aa4144c41b41dbac0c7f263.jsonl[8673] _id=6ac690bade269131f9bdc49e ts=2026-10-07T18:34:34.5810000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 137 group(s), 176 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1111] _id=6ab564d3485cab4c9553cd5c ts=2026-09-24T17:58:42.0730000Z == 6aa4144c41b41dbac0c7f263.jsonl[1112] _id=6ab564d3485cab4c9553cd64 ts=2026-09-24T17:58:42.0730000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1095] _id=6ab564d3485cab4c9553cd6a ts=2026-09-24T17:58:42.1190000Z == 6aa4144c41b41dbac0c7f263.jsonl[1113] _id=6ab564d3485cab4c9553cd6c ts=2026-09-24T17:58:42.1190000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1124] _id=6ab564d4485cab4c9553cd94 ts=2026-09-24T17:58:43.1250000Z == 6aa4144c41b41dbac0c7f263.jsonl[1125] _id=6ab564d4485cab4c9553cd96 ts=2026-09-24T17:58:43.1250000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 40 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4144c41b41dbac0c7f263.jsonl[156] _id=6ab4196f485cab4c954f4732 ts=2026-09-23T18:24:47.5940000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[154] _id=6ab4196f485cab4c954f4734 ts=2026-09-23T18:24:47.5990000Z`; `689ms: 6aa4144c41b41dbac0c7f263.jsonl[446] _id=6ab41d84485cab4c954f674d ts=2026-09-23T18:42:12.1230000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[441] _id=6ab41d84485cab4c954f6757 ts=2026-09-23T18:42:12.8120000Z`; `285ms: 6aa4144c41b41dbac0c7f263.jsonl[441] _id=6ab41d84485cab4c954f6757 ts=2026-09-23T18:42:12.8120000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[442] _id=6ab41d85485cab4c954f675b ts=2026-09-23T18:42:13.0970000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 388 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `40ms: 6aa4144c41b41dbac0c7f263.jsonl[1119] _id=6ab564d4485cab4c9553cd86 ts=2026-09-24T17:58:42.4310000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[1120] _id=6ab564d4485cab4c9553cd88 ts=2026-09-24T17:58:42.4710000Z`; `654ms: 6aa4144c41b41dbac0c7f263.jsonl[1120] _id=6ab564d4485cab4c9553cd88 ts=2026-09-24T17:58:42.4710000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[1121] _id=6ab564d4485cab4c9553cd8e ts=2026-09-24T17:58:43.1250000Z`; `6ms: 6aa4144c41b41dbac0c7f263.jsonl[1105] _id=6ab564d5485cab4c9553cda9 ts=2026-09-24T17:58:43.1330000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[1106] _id=6ab564d5485cab4c9553cdac ts=2026-09-24T17:58:43.1390000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `913ms: 6aa4144c41b41dbac0c7f263.jsonl[1155] _id=6ab56511485cab4c9553d358 ts=2026-09-24T17:59:45.3770000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[1160] _id=6ab56512485cab4c9553d387 ts=2026-09-24T17:59:46.2900000Z`; `766ms: 6aa4144c41b41dbac0c7f263.jsonl[1892] _id=6ab566fd485cab4c95541414 ts=2026-09-24T18:07:57.0670000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[1902] _id=6ab566fd485cab4c95541424 ts=2026-09-24T18:07:57.8330000Z`; `468ms: 6aa4144c41b41dbac0c7f263.jsonl[1901] _id=6ab566fd485cab4c95541416 ts=2026-09-24T18:07:57.5530000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[1903] _id=6ab566fd485cab4c9554142c ts=2026-09-24T18:07:58.0210000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `49ms: 6aa4144c41b41dbac0c7f263.jsonl[6059] _id=6abd553a485cab4c959196cd ts=2026-09-30T18:30:18.6340000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[6057] _id=6abd553a485cab4c959196db ts=2026-09-30T18:30:18.6830000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `413ms: 6aa4144c41b41dbac0c7f263.jsonl[547] _id=6ab41df5485cab4c954f6c29 ts=2026-09-23T18:44:05.2890000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[551] _id=6ab41df5485cab4c954f6c31 ts=2026-09-23T18:44:05.7020000Z`; `787ms: 6aa4144c41b41dbac0c7f263.jsonl[533] _id=6ab41df6485cab4c954f6c37 ts=2026-09-23T18:44:06.7700000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[555] _id=6ab41df7485cab4c954f6c45 ts=2026-09-23T18:44:07.5570000Z`; `23ms: 6aa4144c41b41dbac0c7f263.jsonl[555] _id=6ab41df7485cab4c954f6c45 ts=2026-09-23T18:44:07.5570000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[556] _id=6ab41df7485cab4c954f6c49 ts=2026-09-23T18:44:07.5800000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4144c41b41dbac0c7f263.jsonl[4093] _id=6abaac96485cab4c956f6f49 ts=2026-09-28T18:06:12.6430000Z ~ 6aa4144c41b41dbac0c7f263.jsonl[4095] _id=6abaac96485cab4c956f6f4b ts=2026-09-28T18:06:12.6480000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 99h 6m 
  - Evidence: 99h 6m: 6aa4144c41b41dbac0c7f263.jsonl[6375] _id=6abe753f485cab4c95a9841c ts=2026-10-01T14:59:11.9090000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7029] _id=6ac3e6d4de269131f9aeb13f ts=2026-10-05T18:05:18.5260000Z; 71h 57m: 6aa4144c41b41dbac0c7f263.jsonl[1996] _id=6ab6b8b9485cab4c955dad89 ts=2026-09-25T18:08:57.1500000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4085] _id=6abaac8d485cab4c956f6ebb ts=2026-09-28T18:06:05.7170000Z; 47h 57m: 6aa4144c41b41dbac0c7f263.jsonl[4085] _id=6abaac8d485cab4c956f6ebb ts=2026-09-28T18:06:05.7170000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5297] _id=6abd4eeb485cab4c9590d3b5 ts=2026-09-30T18:03:22.8560000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 2m 
  - Evidence: 120h 2m: 6aa4144c41b41dbac0c7f263.jsonl[5498] _id=6abd5274485cab4c95912255 ts=2026-09-30T18:18:28.1960000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7588] _id=6ac3ea6dde269131f9aee5a7 ts=2026-10-05T18:20:29.9410000Z; 47h 35m: 6aa4144c41b41dbac0c7f263.jsonl[5175] _id=6abab51a485cab4c95704cb7 ts=2026-09-28T18:42:34.2940000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5495] _id=6abd5271485cab4c95912209 ts=2026-09-30T18:18:25.9650000Z; 27m 7s: 6aa4144c41b41dbac0c7f263.jsonl[7587] _id=6ac3ea70de269131f9aee5d9 ts=2026-10-05T18:20:32.5760000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8634] _id=6ac3f0ccde269131f9af60fd ts=2026-10-05T18:47:40.4420000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.007s..0.009s shown 
  - Evidence: 7ms: 6aa4144c41b41dbac0c7f263.jsonl[5179] _id=6abab518485cab4c95704ca1 ts=2026-09-28T18:42:32.8370000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5180] _id=6abab518485cab4c95704ca3 ts=2026-09-28T18:42:32.8440000Z; 9ms: 6aa4144c41b41dbac0c7f263.jsonl[5173] _id=6abab516485cab4c95704c73 ts=2026-09-28T18:42:30.7560000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5174] _id=6abab516485cab4c95704c77 ts=2026-09-28T18:42:30.7650000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 98h 52m 
  - Evidence: 98h 52m: 6aa4144c41b41dbac0c7f263.jsonl[6990] _id=6abe78a2485cab4c95a9f11e ts=2026-10-01T15:13:38.8650000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7077] _id=6ac3e6f3de269131f9aeb2a5 ts=2026-10-05T18:05:49.7390000Z; 71h 18m: 6aa4144c41b41dbac0c7f263.jsonl[4059] _id=6ab6c1d6485cab4c955e6b39 ts=2026-09-25T18:47:50.4540000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4086] _id=6abaac96485cab4c956f6f43 ts=2026-09-28T18:06:12.5880000Z; 47h 46m: 6aa4144c41b41dbac0c7f263.jsonl[8532] _id=6ac3f10fde269131f9af6325 ts=2026-10-05T18:48:47.0360000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8695] _id=6ac690cdde269131f9bdc5a7 ts=2026-10-07T18:34:53.7910000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 414 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f263.jsonl[2104] _id=6ab6b978485cab4c955dc143 ts=2026-09-25T18:12:08.6090000Z -> 6aa4144c41b41dbac0c7f263.jsonl[2102] _id=6ab6b978485cab4c955dc145 ts=2026-09-25T18:12:08.6100000Z; 1ms: 6aa4144c41b41dbac0c7f263.jsonl[2107] _id=6ab6b97c485cab4c955dc1ab ts=2026-09-25T18:12:12.4430000Z -> 6aa4144c41b41dbac0c7f263.jsonl[2108] _id=6ab6b97c485cab4c955dc1af ts=2026-09-25T18:12:12.4440000Z; 1ms: 6aa4144c41b41dbac0c7f263.jsonl[3992] _id=6ab6c0d6485cab4c955e6859 ts=2026-09-25T18:43:34.5710000Z -> 6aa4144c41b41dbac0c7f263.jsonl[3987] _id=6ab6c0d6485cab4c955e685b ts=2026-09-25T18:43:34.5720000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 264h 43m 
  - Evidence: 264h 43m: 6aa4144c41b41dbac0c7f263.jsonl[932] _id=6ab56345485cab4c9553ad0a ts=2026-09-24T17:52:05.5550000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7871] _id=6ac3edecde269131f9af2501 ts=2026-10-05T18:35:24.5320000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 98h 51m 
  - Evidence: 98h 51m: 6aa4144c41b41dbac0c7f263.jsonl[6996] _id=6abe78a7485cab4c95a9f1aa ts=2026-10-01T15:13:43.3750000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7031] _id=6ac3e6d9de269131f9aeb157 ts=2026-10-05T18:05:23.4360000Z; 71h 22m: 6aa4144c41b41dbac0c7f263.jsonl[3972] _id=6ab6c0cb485cab4c955e6821 ts=2026-09-25T18:43:23.9160000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4082] _id=6abaac96485cab4c956f6f37 ts=2026-09-28T18:06:12.5590000Z; 47h 45m: 6aa4144c41b41dbac0c7f263.jsonl[8511] _id=6ac3f10dde269131f9af6315 ts=2026-10-05T18:48:45.2220000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8670] _id=6ac690bade269131f9bdc49b ts=2026-10-07T18:34:34.5790000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 47 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f263.jsonl[7512] _id=6ac3e9c0de269131f9aed9a7 ts=2026-10-05T18:17:36.0240000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7513] _id=6ac3e9c0de269131f9aed9ad ts=2026-10-05T18:17:36.0240000Z; 0ms: 6aa4144c41b41dbac0c7f263.jsonl[8672] _id=6ac690bade269131f9bdc49d ts=2026-10-07T18:34:34.5810000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8673] _id=6ac690bade269131f9bdc49e ts=2026-10-07T18:34:34.5810000Z; 0ms: 6aa4144c41b41dbac0c7f263.jsonl[8673] _id=6ac690bade269131f9bdc49e ts=2026-10-07T18:34:34.5810000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8674] _id=6ac690bade269131f9bdc49f ts=2026-10-07T18:34:34.5810000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 98h 54m 
  - Evidence: 98h 54m: 6aa4144c41b41dbac0c7f263.jsonl[6930] _id=6abe7802485cab4c95a9de67 ts=2026-10-01T15:10:58.3950000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7033] _id=6ac3e6e7de269131f9aeb249 ts=2026-10-05T18:05:37.2710000Z; 71h 28m: 6aa4144c41b41dbac0c7f263.jsonl[3818] _id=6ab6c01e485cab4c955e6365 ts=2026-09-25T18:40:30.3110000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4364] _id=6abaad2b485cab4c956f7aad ts=2026-09-28T18:08:42.7480000Z; 47h 46m: 6aa4144c41b41dbac0c7f263.jsonl[8533] _id=6ac3f10fde269131f9af6327 ts=2026-10-05T18:48:47.0420000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8697] _id=6ac690cdde269131f9bdc5aa ts=2026-10-07T18:34:53.8300000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6aa4144c41b41dbac0c7f263.jsonl[156] _id=6ab4196f485cab4c954f4732 ts=2026-09-23T18:24:47.5940000Z -> 6aa4144c41b41dbac0c7f263.jsonl[154] _id=6ab4196f485cab4c954f4734 ts=2026-09-23T18:24:47.5990000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 98h 51m 
  - Evidence: 98h 51m: 6aa4144c41b41dbac0c7f263.jsonl[6999] _id=6abe78af485cab4c95a9f272 ts=2026-10-01T15:13:51.0760000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7041] _id=6ac3e6d7de269131f9aeb141 ts=2026-10-05T18:05:18.5360000Z; 71h 18m: 6aa4144c41b41dbac0c7f263.jsonl[4062] _id=6ab6c1d1485cab4c955e6b33 ts=2026-09-25T18:47:45.7740000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4079] _id=6abaac96485cab4c956f6f2b ts=2026-09-28T18:06:05.7280000Z; 47h 45m: 6aa4144c41b41dbac0c7f263.jsonl[8531] _id=6ac3f10ede269131f9af631f ts=2026-10-05T18:48:46.2420000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8669] _id=6ac690bade269131f9bdc49a ts=2026-10-07T18:34:29.0220000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 99h 4m 
  - Evidence: 99h 4m: 6aa4144c41b41dbac0c7f263.jsonl[6552] _id=6abe758f485cab4c95a98840 ts=2026-10-01T15:00:30.1270000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7030] _id=6ac3e6d9de269131f9aeb159 ts=2026-10-05T18:05:21.8660000Z; 71h 23m: 6aa4144c41b41dbac0c7f263.jsonl[3948] _id=6ab6c0bc485cab4c955e67c3 ts=2026-09-25T18:43:06.0470000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4094] _id=6abaac97485cab4c956f6f4d ts=2026-09-28T18:06:13.1340000Z; 47h 52m: 6aa4144c41b41dbac0c7f263.jsonl[5198] _id=6abab53b485cab4c95704ed7 ts=2026-09-28T18:43:06.7450000Z -> 6aa4144c41b41dbac0c7f263.jsonl[6190] _id=6abd5678485cab4c9591c12d ts=2026-09-30T18:35:35.6160000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1947 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f263.jsonl[1092] _id=6ab564d3485cab4c9553cd5a ts=2026-09-24T17:58:42.0730000Z -> 6aa4144c41b41dbac0c7f263.jsonl[1111] _id=6ab564d3485cab4c9553cd5c ts=2026-09-24T17:58:42.0730000Z; 0ms: 6aa4144c41b41dbac0c7f263.jsonl[1093] _id=6ab564d3485cab4c9553cd60 ts=2026-09-24T17:58:42.0730000Z -> 6aa4144c41b41dbac0c7f263.jsonl[1112] _id=6ab564d3485cab4c9553cd64 ts=2026-09-24T17:58:42.0730000Z; 0ms: 6aa4144c41b41dbac0c7f263.jsonl[1094] _id=6ab564d3485cab4c9553cd68 ts=2026-09-24T17:58:42.1190000Z -> 6aa4144c41b41dbac0c7f263.jsonl[1095] _id=6ab564d3485cab4c9553cd6a ts=2026-09-24T17:58:42.1190000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 6m 
  - Evidence: 120h 6m: 6aa4144c41b41dbac0c7f263.jsonl[6167] _id=6abd564e485cab4c9591bbed ts=2026-09-30T18:34:54.2440000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7970] _id=6ac3ef46de269131f9af43f5 ts=2026-10-05T18:41:10.1060000Z; 119h 59m: 6aa4144c41b41dbac0c7f263.jsonl[2615] _id=6ab6beb6485cab4c955e4d1b ts=2026-09-25T18:34:30.4730000Z -> 6aa4144c41b41dbac0c7f263.jsonl[6144] _id=6abd5604485cab4c9591b02d ts=2026-09-30T18:33:40.2420000Z; 24h 27m: 6aa4144c41b41dbac0c7f263.jsonl[1827] _id=6ab5663d485cab4c95540282 ts=2026-09-24T18:04:45.3960000Z -> 6aa4144c41b41dbac0c7f263.jsonl[2524] _id=6ab6be29485cab4c955e4899 ts=2026-09-25T18:32:09.8660000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6aa4144c41b41dbac0c7f263.jsonl[5625] _id=6abd535a485cab4c959145e1 ts=2026-09-30T18:22:18.6200000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7559] _id=6ac3ea08de269131f9aedded ts=2026-10-05T18:18:49.0940000Z; 71h 55m: 6aa4144c41b41dbac0c7f263.jsonl[2440] _id=6ab6bd79485cab4c955e4255 ts=2026-09-25T18:29:14.0410000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4920] _id=6abab0f2485cab4c956ff537 ts=2026-09-28T18:24:50.3000000Z; 47h 25m: 6aa4144c41b41dbac0c7f263.jsonl[5228] _id=6abab5be485cab4c95705787 ts=2026-09-28T18:45:18.7700000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5375] _id=6abd50a6485cab4c9590ec4f ts=2026-09-30T18:10:45.9130000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.027s shown 
  - Evidence: 23ms: 6aa4144c41b41dbac0c7f263.jsonl[2145] _id=6ab6ba1f485cab4c955dd4b1 ts=2026-09-25T18:14:55.3270000Z -> 6aa4144c41b41dbac0c7f263.jsonl[2141] _id=6ab6ba1f485cab4c955dd4c3 ts=2026-09-25T18:14:55.3500000Z; 27ms: 6aa4144c41b41dbac0c7f263.jsonl[2143] _id=6ab6ba1f485cab4c955dd4ad ts=2026-09-25T18:14:55.3000000Z -> 6aa4144c41b41dbac0c7f263.jsonl[2145] _id=6ab6ba1f485cab4c955dd4b1 ts=2026-09-25T18:14:55.3270000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 40m 
  - Evidence: 144h 40m: 6aa4144c41b41dbac0c7f263.jsonl[813] _id=6ab56292485cab4c95539d68 ts=2026-09-24T17:49:06.9140000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5994] _id=6abd54f4485cab4c95918aeb ts=2026-09-30T18:29:08.1830000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 38m 
  - Evidence: 144h 38m: 6aa4144c41b41dbac0c7f263.jsonl[812] _id=6ab56292485cab4c95539d6c ts=2026-09-24T17:49:06.9330000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5923] _id=6abd54af485cab4c95917f09 ts=2026-09-30T18:27:59.0280000Z; 22h 59m: 6aa4144c41b41dbac0c7f263.jsonl[630] _id=6ab41e6e485cab4c954f70c3 ts=2026-09-23T18:46:06.0420000Z -> 6aa4144c41b41dbac0c7f263.jsonl[726] _id=6ab561c9485cab4c95538e87 ts=2026-09-24T17:45:45.2840000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.049s..0.049s shown 
  - Evidence: 49ms: 6aa4144c41b41dbac0c7f263.jsonl[6059] _id=6abd553a485cab4c959196cd ts=2026-09-30T18:30:18.6340000Z -> 6aa4144c41b41dbac0c7f263.jsonl[6057] _id=6abd553a485cab4c959196db ts=2026-09-30T18:30:18.6830000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 39m 
  - Evidence: 144h 39m: 6aa4144c41b41dbac0c7f263.jsonl[804] _id=6ab56286485cab4c95539c8a ts=2026-09-24T17:48:54.3030000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5905] _id=6abd54b3485cab4c95918004 ts=2026-09-30T18:28:03.7720000Z; 22h 58m: 6aa4144c41b41dbac0c7f263.jsonl[628] _id=6ab41e67485cab4c954f7085 ts=2026-09-23T18:45:59.8140000Z -> 6aa4144c41b41dbac0c7f263.jsonl[636] _id=6ab56162485cab4c95538532 ts=2026-09-24T17:44:02.3830000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 42 interval(s) ≤ 0.002s..0.018s shown 
  - Evidence: 2ms: 6aa4144c41b41dbac0c7f263.jsonl[775] _id=6ab5624d485cab4c95539834 ts=2026-09-24T17:47:57.2020000Z -> 6aa4144c41b41dbac0c7f263.jsonl[771] _id=6ab5624d485cab4c9553983a ts=2026-09-24T17:47:57.2040000Z; 15ms: 6aa4144c41b41dbac0c7f263.jsonl[741] _id=6ab561e5485cab4c955390ea ts=2026-09-24T17:46:13.4460000Z -> 6aa4144c41b41dbac0c7f263.jsonl[742] _id=6ab561e5485cab4c955390ed ts=2026-09-24T17:46:13.4610000Z; 18ms: 6aa4144c41b41dbac0c7f263.jsonl[619] _id=6ab41e58485cab4c954f7003 ts=2026-09-23T18:45:44.8430000Z -> 6aa4144c41b41dbac0c7f263.jsonl[616] _id=6ab41e58485cab4c954f7005 ts=2026-09-23T18:45:44.8610000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 99h 6m 
  - Evidence: 99h 6m: 6aa4144c41b41dbac0c7f263.jsonl[6372] _id=6abe7539485cab4c95a983ee ts=2026-10-01T14:59:05.4290000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7004] _id=6ac3e6cede269131f9aeb137 ts=2026-10-05T18:05:12.4310000Z; 71h 57m: 6aa4144c41b41dbac0c7f263.jsonl[1993] _id=6ab6b88d485cab4c955daa13 ts=2026-09-25T18:08:11.9910000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4084] _id=6abaac81485cab4c956f6e75 ts=2026-09-28T18:05:53.5510000Z; 47h 58m: 6aa4144c41b41dbac0c7f263.jsonl[7873] _id=6ac3edf7de269131f9af2561 ts=2026-10-05T18:35:35.0760000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8662] _id=6ac690aede269131f9bdc432 ts=2026-10-07T18:34:22.6140000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 98h 51m 
  - Evidence: 98h 51m: 6aa4144c41b41dbac0c7f263.jsonl[7001] _id=6abe78ac485cab4c95a9f22d ts=2026-10-01T15:13:47.9920000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7003] _id=6ac3e6cede269131f9aeb135 ts=2026-10-05T18:05:12.4300000Z; 71h 53m: 6aa4144c41b41dbac0c7f263.jsonl[2096] _id=6ab6b96d485cab4c955dc02f ts=2026-09-25T18:11:57.6810000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4083] _id=6abaac81485cab4c956f6e6f ts=2026-09-28T18:05:53.5500000Z; 47h 57m: 6aa4144c41b41dbac0c7f263.jsonl[4081] _id=6abaac96485cab4c956f6f35 ts=2026-09-28T18:06:12.5530000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5296] _id=6abd4ee4485cab4c9590d3a5 ts=2026-09-30T18:03:15.5910000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 99h 33m 
  - Evidence: 99h 33m: 6aa4144c41b41dbac0c7f263.jsonl[7000] _id=6abe78ac485cab4c95a9f228 ts=2026-10-01T15:13:47.9810000Z -> 6aa4144c41b41dbac0c7f263.jsonl[8617] _id=6ac3f0b3de269131f9af605b ts=2026-10-05T18:47:14.9730000Z; 71h 54m: 6aa4144c41b41dbac0c7f263.jsonl[2092] _id=6ab6b966485cab4c955dbf6d ts=2026-09-25T18:11:50.2370000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4080] _id=6abaac96485cab4c956f6f2f ts=2026-09-28T18:06:12.5470000Z; 47h 19m: 6aa4144c41b41dbac0c7f263.jsonl[5287] _id=6abab65e485cab4c95706cc9 ts=2026-09-28T18:47:58.8170000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5338] _id=6abd4ffe485cab4c9590e21d ts=2026-09-30T18:07:57.9720000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 99h 6m 
  - Evidence: 99h 6m: 6aa4144c41b41dbac0c7f263.jsonl[6374] _id=6abe7544485cab4c95a98444 ts=2026-10-01T14:59:16.0230000Z -> 6aa4144c41b41dbac0c7f263.jsonl[7042] _id=6ac3e6d7de269131f9aeb143 ts=2026-10-05T18:05:21.2190000Z; 71h 19m: 6aa4144c41b41dbac0c7f263.jsonl[4010] _id=6ab6c198485cab4c955e6adf ts=2026-09-25T18:46:48.5420000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4093] _id=6abaac96485cab4c956f6f49 ts=2026-09-28T18:06:12.6430000Z; 47h 47m: 6aa4144c41b41dbac0c7f263.jsonl[4772] _id=6abaaec6485cab4c956fad6f ts=2026-09-28T18:15:34.9490000Z -> 6aa4144c41b41dbac0c7f263.jsonl[5298] _id=6abd4eec485cab4c9590d3b9 ts=2026-09-30T18:03:23.6650000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6aa4144c41b41dbac0c7f263.jsonl[671] _id=6ab56107485cab4c95537d2b ts=2026-09-24T17:42:31.3380000Z -> 6aa4144c41b41dbac0c7f263.jsonl[672] _id=6ab56107485cab4c95537d2d ts=2026-09-24T17:42:31.3410000Z; 4ms: 6aa4144c41b41dbac0c7f263.jsonl[540] _id=6ab41dc7485cab4c954f6a59 ts=2026-09-23T18:43:19.1910000Z -> 6aa4144c41b41dbac0c7f263.jsonl[501] _id=6ab41dc7485cab4c954f6a5b ts=2026-09-23T18:43:19.1950000Z; 5ms: 6aa4144c41b41dbac0c7f263.jsonl[4093] _id=6abaac96485cab4c956f6f49 ts=2026-09-28T18:06:12.6430000Z -> 6aa4144c41b41dbac0c7f263.jsonl[4095] _id=6abaac96485cab4c956f6f4b ts=2026-09-28T18:06:12.6480000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[445] _id=6ab41d7f485cab4c954f672f ts=2026-09-23T18:42:07.2600000Z`; `6aa4144c41b41dbac0c7f263.jsonl[821] _id=6ab562a5485cab4c95539ee2 ts=2026-09-24T17:49:25.6600000Z`; `6aa4144c41b41dbac0c7f263.jsonl[2242] _id=6ab6bb85485cab4c955e1019 ts=2026-09-25T18:20:53.6330000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 46 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1517] _id=6ab56591485cab4c9553e7f0 ts=2026-09-24T18:01:52.9360000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1636] _id=6ab565b4485cab4c9553ecce ts=2026-09-24T18:02:27.2540000Z`; `6aa4144c41b41dbac0c7f263.jsonl[2694] _id=6ab6bf19485cab4c955e51f5 ts=2026-09-25T18:36:08.0830000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 188 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1108] _id=6ab564d5485cab4c9553cdb4 ts=2026-09-24T17:58:43.2010000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1109] _id=6ab564d5485cab4c9553cdba ts=2026-09-24T17:58:43.2010000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1101] _id=6ab564d5485cab4c9553cdbe ts=2026-09-24T17:58:43.2010000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[6057] _id=6abd553a485cab4c959196db ts=2026-09-30T18:30:18.6830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 16 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[555] _id=6ab41df7485cab4c954f6c45 ts=2026-09-23T18:44:07.5570000Z`; `6aa4144c41b41dbac0c7f263.jsonl[556] _id=6ab41df7485cab4c954f6c49 ts=2026-09-23T18:44:07.5800000Z`; `6aa4144c41b41dbac0c7f263.jsonl[592] _id=6ab41e56485cab4c954f6fe9 ts=2026-09-23T18:45:42.0510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[4710] _id=6abaae03485cab4c956f9acb ts=2026-09-28T18:12:19.4530000Z`; `6aa4144c41b41dbac0c7f263.jsonl[7608] _id=6ac3eaa3de269131f9aeea2d ts=2026-10-05T18:21:23.2760000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 501 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1441] _id=6ab56584485cab4c9553e650 ts=2026-09-24T18:01:33.4330000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1442] _id=6ab56584485cab4c9553e654 ts=2026-09-24T18:01:33.4970000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1443] _id=6ab56584485cab4c9553e656 ts=2026-09-24T18:01:33.4970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 524 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1112] _id=6ab564d3485cab4c9553cd64 ts=2026-09-24T17:58:42.0730000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1095] _id=6ab564d3485cab4c9553cd6a ts=2026-09-24T17:58:42.1190000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1113] _id=6ab564d3485cab4c9553cd6c ts=2026-09-24T17:58:42.1190000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 20 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[2145] _id=6ab6ba1f485cab4c955dd4b1 ts=2026-09-25T18:14:55.3270000Z`; `6aa4144c41b41dbac0c7f263.jsonl[2141] _id=6ab6ba1f485cab4c955dd4c3 ts=2026-09-25T18:14:55.3500000Z`; `6aa4144c41b41dbac0c7f263.jsonl[2201] _id=6ab6bade485cab4c955df143 ts=2026-09-25T18:18:07.0120000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[789] _id=6ab5625a485cab4c95539996 ts=2026-09-24T17:48:10.4970000Z`; `6aa4144c41b41dbac0c7f263.jsonl[800] _id=6ab56268485cab4c95539aac ts=2026-09-24T17:48:24.4120000Z`; `6aa4144c41b41dbac0c7f263.jsonl[716] _id=6ab56280485cab4c95539c26 ts=2026-09-24T17:48:48.9290000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 277 start, 271 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 109 unmatched 'BecameCameraCentered' (totals: 708 open, 645 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 61 unmatched 'BecameVisible' (totals: 795 open, 922 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 22 open, 20 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 93 open, 108 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 34 start, 23 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 212 of 9166 adjacent _id pairs reverse in client time; worst 205.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f263.jsonl[1301] _id=6ab56577485cab4c9553e42a ts=2026-09-24T18:01:27.7780000Z`; `6aa4144c41b41dbac0c7f263.jsonl[1309] _id=6ab56578485cab4c9553e43c ts=2026-09-24T17:58:01.9590000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -206.85s, max +9.93s over 9167 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f263\coverage.yaml

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
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3070 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2264); Unit 4 Dev (430); Unit 3 Dungeon Dev (376)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.19s, n=3069)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3070/3070 records)
    "BecameInvisible"  x922
    "BecameVisible"  x795
    "BecameCameraCentered"  x708
    "BecameCameraUncentered"  x645
data.pieceId  (string, 3070/3070 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3070/3070 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2305 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (688); Unit 3 Dungeon Dev (471); Unit 3 Dev (425); Unit 4 Dev - Dungeon (401); Unit 1 Dev (245); Unit 4 Dev (75)
- **Intervals:** median 1.31s (p5 0.16s / p95 17.47s, n=2304)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2305/2305 records)
    "pressed"  x2305
data.actionType  (string, 2305/2305 records)
    "Move"  x1409
    "Interact"  x437
    "Jump"  x361
    "Ascend"  x48
    "Hoverboard"  x30
    "Sprint"  x13
    "Map"  x5
    "Pause"  x1
    "ToggleDebug"  x1
data.key  (string, 2305/2305 records, 13 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2305/2305 records)
    "Player"  x1984
    "Drone"  x321
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1485 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (557); Unit 3 Dev (341); Unit 3 Dungeon Dev (227); Unit 1 Dev (225); Unit 4 Dev - Dungeon (102); Unit 4 Dev (33)
- **eventKey:** present on 937 of 1485 records
- **Intervals:** median 3.93s (p5 0.00s / p95 37.93s, n=1484)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x937; [conversationId, dialogueEventType] x548
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1485/1485 records)
    numeric range 8 .. 111 (37 unique)
data.dialogueEventType  (string, 1485/1485 records)
    "DialogueNodeEvent"  x937
    "DialogueStartEvent"  x277
    "DialogueFinishEvent"  x271
data.nodeId  (number, 937/1485 records)
    numeric range 0 .. 290 (216 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1450 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (606); Unit 3 Dev (269); Unit 1 Dev (246); Unit 3 Dungeon Dev (174); Unit 4 Dev - Dungeon (107); Unit 4 Dev (48)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1443)
- **Fields under `data`:**

```text
data.position  (object, 1450/1450 records)
data.position.x  (number, 1450/1450 records)
    numeric range -680.133 .. 1732.86 (503 unique)
data.position.y  (number, 1450/1450 records)
    numeric range -115.127 .. 158.376 (398 unique)
data.position.z  (number, 1450/1450 records)
    numeric range -1042.9 .. 2563.92 (503 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 235 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (69); Unit 4 Dev - Dungeon (60); Unit 1 Dev (52); Unit 2 Prod (Refactor) (40); Unit 3 Dev (11); Unit 4 Dev (3)
- **Intervals:** median 6.89s (p5 0.19s / p95 360.41s, n=234)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 235/235 records)
    26 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 235/235 records)
    59 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 214 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (119); Unit 3 Dev (95)
- **Intervals:** median 0.41s (p5 0.03s / p95 9.86s, n=213)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 214/214 records)
    "argumentationNodeHoverEnd"  x108
    "argumentationNodeHoverStart"  x93
    "argumentationNodeAdd"  x9
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 214/214 records)
    "Unit 3 - Pollution Upstream"  x95
    "Unit 1 - Argumentation Tutorial"  x94
    "Unit 1 - Freshwater"  x25
data.nodeName  (string, 214/214 records)
    "1"  x56
    "A"  x52
    "I"  x51
    "4"  x16
    "II"  x14
    "2"  x8
    "5"  x7
    "B"  x6
    "3"  x4
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 151 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (128); Unit 3 Dev (21); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1.98s (p5 0.38s / p95 386.77s, n=150)
- **`data` key-set variants:** [actionType, featureUsed, location] x59; [actionType, featureUsed, legendName] x50; [actionType, featureUsed] x42
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 151/151 records)
    "WaypointMoveEvent"  x52
    "Selected"  x37
    "MapOpenEvent"  x22
    "MapCloseEvent"  x20
    "Unselected"  x13
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x2
data.featureUsed  (string, 151/151 records)
    "Waypoint"  x59
    "Legend"  x50
    "Map"  x42
data.legendName  (string, 50/151 records)
    13 unique values (see csv/event_unique_values.csv)
data.location  (object, 59/151 records)
data.location.x  (number, 59/151 records)
    numeric range -349.043 .. 187.91 (53 unique)
data.location.y  (number, 59/151 records)
    numeric range -278.927 .. 314.5 (50 unique)
data.location.z  (number, 59/151 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 108 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (70); Unit 3 Dev (26); Unit 4 Dev (12)
- **Intervals:** median 0.83s (p5 0.19s / p95 13.28s, n=107)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x100; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/108 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/108 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 100/108 records)
    "RightDrag"  x53
    "LeftDrag"  x47
data.currentSoilType  (string, 100/108 records)
    "SAND"  x20
    "CLAY"  x17
    "CLAYSAND"  x17
    "SANDGRAVEL"  x17
    "CLAYROCK"  x16
    "BEDROCK"  x7
    "GRAVEL"  x6
data.isCorrectSelection  (string, 100/108 records)
    "false"  x78
    "true"  x22
data.waterLevelStatus  (string, 100/108 records)
    "TooHigh"  x53
    "Proper"  x30
    "TooLow"  x17
data.waterRetentionChange  (string, 100/108 records)
    "Increase"  x46
    "Decrease"  x32
    "NoChange"  x22
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 57 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (16); Unit 2 Prod (Refactor) (16); Unit 3 Dev (10); Unit 4 Dev - Dungeon (10); Unit 3 Dungeon Dev (4); Unit 4 Dev (1)
- **eventKey:** present on 57 of 57 records
- **Intervals:** median 223.87s (p5 0.01s / p95 171996.93s, n=56)
- **`data` key-set variants:** [questEventType, questID, questName] x34; [questEventType, questID, questName, questSuccessOrFailure] x23
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 57/57 records)
    "questActiveEvent"  x34
    "questFinishEvent"  x23
data.questID  (string, 57/57 records)
    21 unique values (see csv/event_unique_values.csv)
data.questName  (string, 57/57 records)
    21 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 23/57 records)
    "Succeeded"  x23
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (12); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 3 Dungeon Dev (2); Unit 3 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1769.43s (p5 18.02s / p95 268540.73s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 16 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 1 Dev (3); Unit 3 Dungeon Dev (3); Unit 3 Dev (2); Unit 4 Dev - Dungeon (2); MainMenu (1); Unit 4 Dev (1)
- **Intervals:** median 1686.84s (p5 44.60s / p95 288349.98s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "DebugMenuStateChanged"  x16
data.isOpened  (bool, 16/16 records)
    false  x16
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (4); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.54s (p5 0.01s / p95 301736.71s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 10 empty-string)
    ""  x10
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 12 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (12)
- **Intervals:** median 84296.63s (p5 152.44s / p95 307914.28s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    true  x12
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 11 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (5)
- **Intervals:** median 17.17s (p5 5.62s / p95 286487.69s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "submitAnswerEvent"  x11
data.answerSubmitted  (string, 11/11 records)
    "A,1,I"  x5
    "A,I"  x2
    "A,1,"  x1
    "A,4,I"  x1
    "A,5,I"  x1
    "I"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 10 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Transition (1); Unit 3 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 82480.93s (p5 731.04s / p95 318589.12s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    false  x10
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (3)
- **Intervals:** median 73.71s (p5 18.07s / p95 367448.60s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 952998.98s (p5 952998.98s / p95 952998.98s, n=1)
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now
- `chatEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (70 records)
- `TopographicMapEvent` data.actionType: "Selected" (37x); "Unselected" (13x); "WaypointMoveEvent" (52x); "WaypointResetEvent" (2x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (50x); "Waypoint" (59x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*