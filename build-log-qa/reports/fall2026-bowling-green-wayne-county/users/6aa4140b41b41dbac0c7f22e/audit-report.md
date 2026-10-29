# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22e
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f22e.jsonl
- **Records:** 15769 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f22e
- **Time span:** 2026-09-23T13:54:22.429000+00:00 .. 2026-10-07T16:17:08.851000+00:00 (338h 22m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 15769 records, 8 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 105 INFO, 2 NOT_TESTED, 84 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8704 | 55.2 | 1 | 7 | 0 | 2026-09-23T13:55:30.372000+00:00 | 2026-10-07T16:15:08.693000+00:00 | 338h 19m |
| PuzzlePieceVisibleEvent | 2646 | 16.78 | 1 | 3 | 0 | 2026-09-24T13:41:02.330000+00:00 | 2026-10-06T14:25:01.231000+00:00 | 288h 43m |
| DialogueEvent | 1782 | 11.3 | 1 | 7 | 1063 | 2026-09-23T13:55:47.053000+00:00 | 2026-10-07T16:17:06.932000+00:00 | 338h 21m |
| PlayerPositionEvent | 1713 | 10.86 | 1 | 7 | 0 | 2026-09-23T13:55:25.532000+00:00 | 2026-10-07T16:17:08.851000+00:00 | 338h 21m |
| ObjectInterEvent | 247 | 1.57 | 1 | 7 | 0 | 2026-09-23T14:03:35.037000+00:00 | 2026-10-07T16:14:46.236000+00:00 | 338h 11m |
| argumentationNodeEvent | 177 | 1.12 | 1 | 4 | 0 | 2026-09-23T14:20:23.820000+00:00 | 2026-10-07T14:23:11.720000+00:00 | 336h 2m |
| argumentationAnswerEvent | 102 | 0.65 | 1 | 3 | 0 | 2026-09-23T14:23:40.374000+00:00 | 2026-10-07T14:23:18.181000+00:00 | 335h 59m |
| TopographicMapEvent | 89 | 0.56 | 1 | 2 | 0 | 2026-09-24T13:42:47.863000+00:00 | 2026-10-05T14:04:44.370000+00:00 | 264h 21m |
| questEvent | 64 | 0.41 | 1 | 7 | 64 | 2026-09-23T13:55:47.031000+00:00 | 2026-10-07T16:09:10.838000+00:00 | 338h 13m |
| Soil Key Puzzle | 58 | 0.37 | 1 | 3 | 0 | 2026-09-24T13:48:54.166000+00:00 | 2026-10-06T13:53:40.638000+00:00 | 288h 4m |
| DaniEvent | 56 | 0.36 | 1 | 5 | 0 | 2026-09-23T14:01:51.230000+00:00 | 2026-10-07T16:10:01.519000+00:00 | 338h 8m |
| gameWindowFocusEvent | 28 | 0.18 | 1 | 5 | 0 | 2026-09-23T13:54:22.429000+00:00 | 2026-10-07T16:08:41.919000+00:00 | 338h 14m |
| DEBUGMenu | 25 | 0.16 | 1 | 8 | 0 | 2026-09-23T13:55:25.523000+00:00 | 2026-10-07T16:09:05.749000+00:00 | 338h 13m |
| gameStartEvent | 16 | 0.1 | 1 | 1 | 0 | 2026-09-23T13:54:22.430000+00:00 | 2026-10-07T16:08:41.919000+00:00 | 338h 14m |
| gameWindowUnfocusEvent | 15 | 0.1 | 1 | 4 | 0 | 2026-09-23T13:55:50.524000+00:00 | 2026-10-06T14:16:52.179000+00:00 | 312h 21m |
| TerasGardenBox | 11 | 0.07 | 1 | 1 | 0 | 2026-10-07T14:29:00.311000+00:00 | 2026-10-07T16:13:50.431000+00:00 | 1h 44m |
| soilMachine | 11 | 0.07 | 1 | 1 | 0 | 2026-10-06T14:10:18.133000+00:00 | 2026-10-06T14:15:08.842000+00:00 | 4m 50s |
| argumentationEvent | 10 | 0.06 | 1 | 3 | 0 | 2026-09-23T14:22:13.900000+00:00 | 2026-10-07T14:23:18.232000+00:00 | 336h 1m |
| argumentationToolEvent | 9 | 0.06 | 1 | 2 | 0 | 2026-09-23T14:22:09.799000+00:00 | 2026-09-29T14:07:51.806000+00:00 | 143h 45m |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-23T14:28:22.597000+00:00 | 2026-10-05T14:23:04.376000+00:00 | 287h 54m |
| chatEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-09-24T13:52:38.172000+00:00 | 2026-09-24T13:52:39.952000+00:00 | 1.8s |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 1036481.779s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 0.284s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 0.192s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.107s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 1.78s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 7058.155s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.458s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 56 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 8704 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 20.4x vs baseline. 
  - Observed: 102 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,I; A,3,I; A,4,I; A,B,1,I; B,1,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-210, 18-75, 18-76, 18-77, 18-79] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 24 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[318] _id=6ab3dca5485cab4c954cf51f ts=2026-09-23T14:05:25.1990000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[406] _id=6ab3dd95485cab4c954cfdbf ts=2026-09-23T14:09:25.6280000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[434] _id=6ab3de34485cab4c954d0171 ts=2026-09-23T14:12:04.8320000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[26] _id=6ab3da0e485cab4c954ce2b5 ts=2026-09-23T13:54:22.4300000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1128] _id=6ab3e256485cab4c954d2e1e ts=2026-09-23T14:29:41.9940000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1197] _id=6ab5277a485cab4c9551348f ts=2026-09-24T13:36:58.3400000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[25] _id=6ab3da0e485cab4c954ce2b3 ts=2026-09-23T13:54:22.4290000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[46] _id=6ab3da68485cab4c954ce3bb ts=2026-09-23T13:55:52.4070000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[47] _id=6ab3da6b485cab4c954ce3c3 ts=2026-09-23T13:55:55.6050000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[41] _id=6ab3da66485cab4c954ce3b1 ts=2026-09-23T13:55:50.5240000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[49] _id=6ab3da6a485cab4c954ce3bf ts=2026-09-23T13:55:54.1260000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[48] _id=6ab3da6b485cab4c954ce3c5 ts=2026-09-23T13:55:55.6490000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8703 | 0.0 | 0.284 | 139.949 | 3.381 | 516037.202 | 0.43 | 806 | 9 |
| PuzzlePieceVisibleEvent | 2645 | 0.0 | 0.024 | 392.983 | 1.025 | 516721.266 | 0.15 | 1671 | 5 |
| DialogueEvent | 1781 | 0.0 | 4.319 | 683.93 | 41.753 | 515983.257 | 0.09 | 547 | 8 |
| PlayerPositionEvent | 1701 | 9.954 | 10.0 | 412.606 | 10.083 | 256654.573 | 0.15 | 0 | 7 |
| ObjectInterEvent | 246 | 0.0 | 7.365 | 4949.07 | 643.922 | 516155.157 | 0.01 | 3 | 13 |
| argumentationNodeEvent | 176 | 0.016 | 0.303 | 6873.681 | 9.093 | 691853.961 | 0.01 | 43 | 3 |
| argumentationAnswerEvent | 101 | 0.081 | 0.192 | 11976.018 | 18.699 | 691857.282 | 0.01 | 0 | 2 |
| TopographicMapEvent | 88 | 0.007 | 1.671 | 10814.96 | 606.042 | 603861.668 | 0.01 | 3 | 5 |
| questEvent | 63 | 0.003 | 267.405 | 19327.045 | 85137.602 | 516048.483 | 0.0 | 8 | 12 |
| Soil Key Puzzle | 57 | 0.137 | 0.775 | 18194.5 | 17440.987 | 603449.025 | 0.0 | 0 | 3 |
| DaniEvent | 55 | 0.002 | 2.071 | 22132.551 | 88842.728 | 689387.268 | 0.0 | 6 | 7 |
| gameWindowFocusEvent | 27 | 3.198 | 191.457 | 45098.5 | 207159.103 | 518138.794 | 0.0 | 0 | 12 |
| DEBUGMenu | 24 | 7.639 | 1236.207 | 50734.176 | 232808.48 | 515969.762 | 0.0 | 0 | 17 |
| gameStartEvent | 15 | 127.789 | 7058.155 | 81177.299 | 336353.579 | 518138.795 | 0.0 | 0 | 11 |
| gameWindowUnfocusEvent | 14 | 1.523 | 153.022 | 80318.69 | 380386.457 | 606446.513 | 0.0 | 0 | 6 |
| TerasGardenBox | 10 | 1.712 | 8.011 | 629.012 | 3426.524 | 6214.085 | 0.1 | 0 | 1 |
| soilMachine | 10 | 0.31 | 1.458 | 29.071 | 144.488 | 189.686 | 2.06 | 0 | 0 |
| argumentationEvent | 9 | 0.028 | 109.419 | 134407.148 | 622039.794 | 691851.377 | 0.0 | 1 | 2 |
| argumentationToolEvent | 8 | 0.108 | 3.107 | 64692.751 | 336363.979 | 517429.264 | 0.0 | 0 | 1 |
| EndOfUnit | 1 | 1036481.779 | 1036481.779 | 1036481.779 | 1036481.779 | 1036481.779 | 0.0 | 0 | 1 |
| chatEvent | 1 | 1.78 | 1.78 | 1.78 | 1.78 | 1.78 | 33.71 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 12 group(s), 15 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[452] _id=6ab3de16485cab4c954d006d ts=2026-09-23T14:11:33.7520000Z == 6aa4140b41b41dbac0c7f22e.jsonl[453] _id=6ab3de16485cab4c954d006f ts=2026-09-23T14:11:33.7520000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[455] _id=6ab3de16485cab4c954d0075 ts=2026-09-23T14:11:33.7540000Z == 6aa4140b41b41dbac0c7f22e.jsonl[477] _id=6ab3de16485cab4c954d0077 ts=2026-09-23T14:11:33.7540000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[562] _id=6ab3de7b485cab4c954d0357 ts=2026-09-23T14:13:15.5950000Z == 6aa4140b41b41dbac0c7f22e.jsonl[567] _id=6ab3de7b485cab4c954d0359 ts=2026-09-23T14:13:15.5950000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 168 group(s), 255 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[1363] _id=6ab52873485cab4c955149f1 ts=2026-09-24T13:41:06.8430000Z == 6aa4140b41b41dbac0c7f22e.jsonl[1368] _id=6ab52873485cab4c955149f3 ts=2026-09-24T13:41:06.8430000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1407] _id=6ab5287c485cab4c95514b28 ts=2026-09-24T13:41:14.4960000Z == 6aa4140b41b41dbac0c7f22e.jsonl[1415] _id=6ab5287c485cab4c95514b2f ts=2026-09-24T13:41:14.4960000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1416] _id=6ab5287c485cab4c95514b37 ts=2026-09-24T13:41:14.5170000Z == 6aa4140b41b41dbac0c7f22e.jsonl[1409] _id=6ab5287c485cab4c95514b3f ts=2026-09-24T13:41:14.5170000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `189ms: 6aa4140b41b41dbac0c7f22e.jsonl[3291] _id=6ab52b1d485cab4c95519dff ts=2026-09-24T13:52:29.2150000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[3293] _id=6ab52b1d485cab4c95519e03 ts=2026-09-24T13:52:29.4040000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6aa4140b41b41dbac0c7f22e.jsonl[300] _id=6ab3dc36485cab4c954cf23f ts=2026-09-23T14:03:35.0370000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[295] _id=6ab3dc37485cab4c954cf241 ts=2026-09-23T14:03:35.0460000Z`; `212ms: 6aa4140b41b41dbac0c7f22e.jsonl[697] _id=6ab3dfde485cab4c954d12bd ts=2026-09-23T14:19:10.2360000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[701] _id=6ab3dfde485cab4c954d12c1 ts=2026-09-23T14:19:10.4480000Z`; `689ms: 6aa4140b41b41dbac0c7f22e.jsonl[1979] _id=6ab52926485cab4c955163e3 ts=2026-09-24T13:44:06.3700000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[1983] _id=6ab52927485cab4c955163fb ts=2026-09-24T13:44:07.0590000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 550 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `84ms: 6aa4140b41b41dbac0c7f22e.jsonl[1383] _id=6ab5287a485cab4c95514ac7 ts=2026-09-24T13:41:13.2660000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[1390] _id=6ab5287a485cab4c95514acb ts=2026-09-24T13:41:13.3500000Z`; `192ms: 6aa4140b41b41dbac0c7f22e.jsonl[1390] _id=6ab5287a485cab4c95514acb ts=2026-09-24T13:41:13.3500000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[1385] _id=6ab5287a485cab4c95514ad1 ts=2026-09-24T13:41:13.5420000Z`; `24ms: 6aa4140b41b41dbac0c7f22e.jsonl[1398] _id=6ab5287c485cab4c95514b22 ts=2026-09-24T13:41:14.4720000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[1407] _id=6ab5287c485cab4c95514b28 ts=2026-09-24T13:41:14.4960000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `50ms: 6aa4140b41b41dbac0c7f22e.jsonl[3641] _id=6ab52dce485cab4c9551cb55 ts=2026-09-24T14:03:58.7080000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[3642] _id=6ab52dcf485cab4c9551cb5b ts=2026-09-24T14:03:58.7580000Z`; `7ms: 6aa4140b41b41dbac0c7f22e.jsonl[3642] _id=6ab52dcf485cab4c9551cb5b ts=2026-09-24T14:03:58.7580000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[3652] _id=6ab52dcf485cab4c9551cb5f ts=2026-09-24T14:03:58.7650000Z`; `231ms: 6aa4140b41b41dbac0c7f22e.jsonl[3657] _id=6ab52ddd485cab4c9551cbe3 ts=2026-09-24T14:04:13.1410000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[3674] _id=6ab52ddd485cab4c9551cbe6 ts=2026-09-24T14:04:13.3720000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 77 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `860ms: 6aa4140b41b41dbac0c7f22e.jsonl[845] _id=6ab3e0ef485cab4c954d20b7 ts=2026-09-23T14:23:43.1440000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[838] _id=6ab3e0ef485cab4c954d20bb ts=2026-09-23T14:23:44.0040000Z`; `183ms: 6aa4140b41b41dbac0c7f22e.jsonl[838] _id=6ab3e0ef485cab4c954d20bb ts=2026-09-23T14:23:44.0040000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[839] _id=6ab3e0f0485cab4c954d20bf ts=2026-09-23T14:23:44.1870000Z`; `189ms: 6aa4140b41b41dbac0c7f22e.jsonl[839] _id=6ab3e0f0485cab4c954d20bf ts=2026-09-23T14:23:44.1870000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[840] _id=6ab3e0f0485cab4c954d20c7 ts=2026-09-23T14:23:44.3760000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `58ms: 6aa4140b41b41dbac0c7f22e.jsonl[9230] _id=6abbc6b5485cab4c957e623d ts=2026-09-29T14:09:57.5460000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[9234] _id=6abbc6b5485cab4c957e6247 ts=2026-09-29T14:09:57.6040000Z`; `28ms: 6aa4140b41b41dbac0c7f22e.jsonl[15146] _id=6ac655d6de269131f9bac50f ts=2026-10-07T14:23:18.2040000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[15149] _id=6ac655d6de269131f9bac512 ts=2026-10-07T14:23:18.2320000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 18 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `788ms: 6aa4140b41b41dbac0c7f22e.jsonl[944] _id=6ab3e14d485cab4c954d242b ts=2026-09-23T14:25:17.5730000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[946] _id=6ab3e14e485cab4c954d243f ts=2026-09-23T14:25:18.3610000Z`; `903ms: 6aa4140b41b41dbac0c7f22e.jsonl[945] _id=6ab3e14d485cab4c954d2430 ts=2026-09-23T14:25:17.6300000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[947] _id=6ab3e14e485cab4c954d2445 ts=2026-09-23T14:25:18.5330000Z`; `585ms: 6aa4140b41b41dbac0c7f22e.jsonl[3231] _id=6ab52b22485cab4c95519e2d ts=2026-09-24T13:52:34.5660000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[3298] _id=6ab52b23485cab4c95519e3d ts=2026-09-24T13:52:35.1510000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `819ms: 6aa4140b41b41dbac0c7f22e.jsonl[863] _id=6ab3e0fb485cab4c954d2117 ts=2026-09-23T14:23:55.5080000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[864] _id=6ab3e0fc485cab4c954d211f ts=2026-09-23T14:23:56.3270000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `473ms: 6aa4140b41b41dbac0c7f22e.jsonl[13913] _id=6ac5014bde269131f9b261fe ts=2026-10-06T14:10:19.4880000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[14003] _id=6ac5014bde269131f9b2621a ts=2026-10-06T14:10:19.9610000Z`; `353ms: 6aa4140b41b41dbac0c7f22e.jsonl[14010] _id=6ac5014dde269131f9b2624c ts=2026-10-06T14:10:21.5220000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[14015] _id=6ac5014dde269131f9b2625c ts=2026-10-06T14:10:21.8750000Z`; `310ms: 6aa4140b41b41dbac0c7f22e.jsonl[14015] _id=6ac5014dde269131f9b2625c ts=2026-10-06T14:10:21.8750000Z ~ 6aa4140b41b41dbac0c7f22e.jsonl[14017] _id=6ac5014ede269131f9b2626c ts=2026-10-06T14:10:22.1850000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 143h 19m 
  - Evidence: 143h 19m: 6aa4140b41b41dbac0c7f22e.jsonl[10801] _id=6abbcbcc485cab4c957ee513 ts=2026-09-29T14:31:40.0130000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10822] _id=6ac3ab4dde269131f9a9f010 ts=2026-10-05T13:51:09.7750000Z; 71h 47m: 6aa4140b41b41dbac0c7f22e.jsonl[4350] _id=6ab67e45485cab4c9555b684 ts=2026-09-25T13:59:33.8240000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6263] _id=6aba6fd6485cab4c95681b41 ts=2026-09-28T13:47:02.1010000Z; 24h 18m: 6aa4140b41b41dbac0c7f22e.jsonl[1201] _id=6ab52788485cab4c95513549 ts=2026-09-24T13:37:12.6420000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4315] _id=6ab67d64485cab4c9555a4f4 ts=2026-09-25T13:55:48.9390000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 191h 29m 
  - Evidence: 191h 29m: 6aa4140b41b41dbac0c7f22e.jsonl[7924] _id=6aba7927485cab4c9568dca1 ts=2026-09-28T14:26:47.7830000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[13086] _id=6ac4fe13de269131f9b202fa ts=2026-10-06T13:56:35.0510000Z; 71h 46m: 6aa4140b41b41dbac0c7f22e.jsonl[5767] _id=6ab681e9485cab4c9555fad0 ts=2026-09-25T14:15:05.5230000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6560] _id=6aba7338485cab4c95686a41 ts=2026-09-28T14:01:28.6210000Z; 26h 13m: 6aa4140b41b41dbac0c7f22e.jsonl[13089] _id=6ac4fe14de269131f9b20380 ts=2026-10-06T13:56:36.8440000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15403] _id=6ac66ec4de269131f9bc4bfe ts=2026-10-07T16:09:39.9240000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f22e.jsonl[90] _id=6ab3dbdd485cab4c954cee83 ts=2026-09-23T14:02:05.3910000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[91] _id=6ab3dbdd485cab4c954cee85 ts=2026-09-23T14:02:05.3930000Z; 3ms: 6aa4140b41b41dbac0c7f22e.jsonl[137] _id=6ab3dbd4485cab4c954cee39 ts=2026-09-23T14:01:56.4810000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[138] _id=6ab3dbd4485cab4c954cee3b ts=2026-09-23T14:01:56.4840000Z; 3ms: 6aa4140b41b41dbac0c7f22e.jsonl[15418] _id=6ac66ed7de269131f9bc4c24 ts=2026-10-07T16:09:59.8230000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15410] _id=6ac66ed7de269131f9bc4c26 ts=2026-10-07T16:09:59.8260000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 19m 
  - Evidence: 143h 19m: 6aa4140b41b41dbac0c7f22e.jsonl[10814] _id=6abbcbe0485cab4c957ee70d ts=2026-09-29T14:32:00.2550000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10928] _id=6ac3ab6fde269131f9a9f8be ts=2026-10-05T13:51:43.5120000Z; 71h 17m: 6aa4140b41b41dbac0c7f22e.jsonl[6251] _id=6ab6853f485cab4c95564900 ts=2026-09-25T14:29:19.1830000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6266] _id=6aba6fde485cab4c95681b51 ts=2026-09-28T13:47:10.2270000Z; 23h 40m: 6aa4140b41b41dbac0c7f22e.jsonl[4306] _id=6ab53072485cab4c9551edb5 ts=2026-09-24T14:15:14.9510000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4322] _id=6ab67d6b485cab4c9555a572 ts=2026-09-25T13:55:55.2270000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 547 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[15064] _id=6ac65546de269131f9bab510 ts=2026-10-07T14:20:54.8300000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15065] _id=6ac65546de269131f9bab511 ts=2026-10-07T14:20:54.8300000Z; 1ms: 6aa4140b41b41dbac0c7f22e.jsonl[1000] _id=6ab3e19c485cab4c954d2739 ts=2026-09-23T14:26:36.2610000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[1001] _id=6ab3e19c485cab4c954d273f ts=2026-09-23T14:26:36.2620000Z; 1ms: 6aa4140b41b41dbac0c7f22e.jsonl[10773] _id=6abbcb7b485cab4c957edb2d ts=2026-09-29T14:30:19.4390000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10769] _id=6abbcb7b485cab4c957edb2f ts=2026-09-29T14:30:19.4400000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 287h 54m 
  - Evidence: 287h 54m: 6aa4140b41b41dbac0c7f22e.jsonl[1125] _id=6ab3e206485cab4c954d2b69 ts=2026-09-23T14:28:22.5970000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[12065] _id=6ac3b2c8de269131f9ab8c7c ts=2026-10-05T14:23:04.3760000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 20m 
  - Evidence: 143h 20m: 6aa4140b41b41dbac0c7f22e.jsonl[10785] _id=6abbcb8a485cab4c957edd01 ts=2026-09-29T14:30:34.6350000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10831] _id=6ac3ab51de269131f9a9f0dc ts=2026-10-05T13:51:11.8370000Z; 71h 29m: 6aa4140b41b41dbac0c7f22e.jsonl[6227] _id=6ab684f7485cab4c955644c8 ts=2026-09-25T14:28:07.5150000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6371] _id=6aba723a485cab4c95685a2d ts=2026-09-28T13:57:14.4330000Z; 23h 43m: 6aa4140b41b41dbac0c7f22e.jsonl[4269] _id=6ab52fc8485cab4c9551e28d ts=2026-09-24T14:12:24.0490000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4316] _id=6ab67d6b485cab4c9555a564 ts=2026-09-25T13:55:55.1960000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 806 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[10038] _id=6abbc8e1485cab4c957e92f1 ts=2026-09-29T14:19:13.1720000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10035] _id=6abbc8e1485cab4c957e92f5 ts=2026-09-29T14:19:13.1720000Z; 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[12228] _id=6ac4fc78de269131f9b19193 ts=2026-10-06T13:49:43.7250000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[12233] _id=6ac4fc78de269131f9b1919b ts=2026-10-06T13:49:43.7250000Z; 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[12231] _id=6ac4fc78de269131f9b191b9 ts=2026-10-06T13:49:43.7290000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[12235] _id=6ac4fc78de269131f9b191bd ts=2026-10-06T13:49:43.7290000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 6aa4140b41b41dbac0c7f22e.jsonl[10690] _id=6abbcb26485cab4c957ed2d3 ts=2026-09-29T14:28:54.6810000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10870] _id=6ac3ab61de269131f9a9f520 ts=2026-10-05T13:51:29.8380000Z; 71h 53m: 6aa4140b41b41dbac0c7f22e.jsonl[5438] _id=6ab6800c485cab4c9555ccf8 ts=2026-09-25T14:07:08.5200000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6459] _id=6aba7302485cab4c956864e5 ts=2026-09-28T14:00:34.1740000Z; 24h 12m: 6aa4140b41b41dbac0c7f22e.jsonl[3128] _id=6ab52a46485cab4c95519265 ts=2026-09-24T13:48:54.1710000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4617] _id=6ab67ebb485cab4c9555bd4a ts=2026-09-25T14:01:31.4460000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.009s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[14881] _id=6ac6537ede269131f9ba75a0 ts=2026-10-07T14:13:18.2200000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[14882] _id=6ac6537ede269131f9ba75a1 ts=2026-10-07T14:13:18.2200000Z; 1ms: 6aa4140b41b41dbac0c7f22e.jsonl[14979] _id=6ac653dade269131f9ba825f ts=2026-10-07T14:14:50.2490000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[14980] _id=6ac653dade269131f9ba8260 ts=2026-10-07T14:14:50.2500000Z; 9ms: 6aa4140b41b41dbac0c7f22e.jsonl[300] _id=6ab3dc36485cab4c954cf23f ts=2026-09-23T14:03:35.0370000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[295] _id=6ab3dc37485cab4c954cf241 ts=2026-09-23T14:03:35.0460000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 17m 
  - Evidence: 71h 17m: 6aa4140b41b41dbac0c7f22e.jsonl[6247] _id=6ab68547485cab4c95564968 ts=2026-09-25T14:29:27.5350000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6264] _id=6aba6fde485cab4c95681b4b ts=2026-09-28T13:47:02.1080000Z; 23h 40m: 6aa4140b41b41dbac0c7f22e.jsonl[4307] _id=6ab53073485cab4c9551edbb ts=2026-09-24T14:15:15.1940000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4314] _id=6ab67d6b485cab4c9555a562 ts=2026-09-25T13:55:48.9450000Z; 23h 39m: 6aa4140b41b41dbac0c7f22e.jsonl[14816] _id=6ac50654de269131f9b342be ts=2026-10-06T14:31:48.5640000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[14824] _id=6ac65303de269131f9ba6af2 ts=2026-10-07T14:11:10.9480000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 32m 
  - Evidence: 143h 32m: 6aa4140b41b41dbac0c7f22e.jsonl[10040] _id=6abbc8e1485cab4c957e92e3 ts=2026-09-29T14:19:10.5830000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10832] _id=6ac3ab52de269131f9a9f108 ts=2026-10-05T13:51:11.8490000Z; 96h 5m: 6aa4140b41b41dbac0c7f22e.jsonl[5589] _id=6ab68108485cab4c9555d84c ts=2026-09-25T14:11:18.7370000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[9711] _id=6abbc850485cab4c957e7f51 ts=2026-09-29T14:16:47.1750000Z; 24h 16m: 6aa4140b41b41dbac0c7f22e.jsonl[2932] _id=6ab529c2485cab4c95517eb5 ts=2026-09-24T13:46:40.7480000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4600] _id=6ab67f24485cab4c9555c0e2 ts=2026-09-25T14:03:15.3690000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1671 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[10016] _id=6abbc8dd485cab4c957e9241 ts=2026-09-29T14:19:08.7840000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10018] _id=6abbc8dd485cab4c957e9251 ts=2026-09-29T14:19:08.7840000Z; 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[10019] _id=6abbc8dd485cab4c957e9253 ts=2026-09-29T14:19:09.1390000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10017] _id=6abbc8dd485cab4c957e9255 ts=2026-09-29T14:19:09.1390000Z; 0ms: 6aa4140b41b41dbac0c7f22e.jsonl[10024] _id=6abbc8df485cab4c957e928b ts=2026-09-29T14:19:09.5270000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10025] _id=6abbc8df485cab4c957e928d ts=2026-09-29T14:19:09.5270000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 37m 
  - Evidence: 167h 37m: 6aa4140b41b41dbac0c7f22e.jsonl[9670] _id=6abbc81e485cab4c957e7a89 ts=2026-09-29T14:15:58.4420000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[12478] _id=6ac4fd57de269131f9b1cd2a ts=2026-10-06T13:53:27.4670000Z; 96h 12m: 6aa4140b41b41dbac0c7f22e.jsonl[4639] _id=6ab67efb485cab4c9555bf28 ts=2026-09-25T14:02:35.3690000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[9654] _id=6abbc7fe485cab4c957e7711 ts=2026-09-29T14:15:26.2960000Z; 24h 12m: 6aa4140b41b41dbac0c7f22e.jsonl[3136] _id=6ab52a49485cab4c955192bb ts=2026-09-24T13:48:57.1530000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4610] _id=6ab67ebb485cab4c9555bd48 ts=2026-09-25T14:01:31.4440000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 43m 
  - Evidence: 1h 43m: 6aa4140b41b41dbac0c7f22e.jsonl[15324] _id=6ac6574cde269131f9bade22 ts=2026-10-07T14:29:31.9930000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15664] _id=6ac66f92de269131f9bc505b ts=2026-10-07T16:13:06.0780000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 44m 
  - Evidence: 167h 44m: 6aa4140b41b41dbac0c7f22e.jsonl[7612] _id=6aba77a1485cab4c9568c78d ts=2026-09-28T14:20:17.4860000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[11560] _id=6ac3ae77de269131f9aa865e ts=2026-10-05T14:04:39.1540000Z; 71h 33m: 6aa4140b41b41dbac0c7f22e.jsonl[5949] _id=6ab6848d485cab4c95563d70 ts=2026-09-25T14:26:21.7810000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6457] _id=6aba72ea485cab4c9568631a ts=2026-09-28T14:00:10.3270000Z; 24h 2m: 6aa4140b41b41dbac0c7f22e.jsonl[4218] _id=6ab52fa1485cab4c9551e05b ts=2026-09-24T14:11:45.1240000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[5727] _id=6ab681c9485cab4c9555f3ad ts=2026-09-25T14:14:34.0650000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.007s..0.050s shown 
  - Evidence: 7ms: 6aa4140b41b41dbac0c7f22e.jsonl[3642] _id=6ab52dcf485cab4c9551cb5b ts=2026-09-24T14:03:58.7580000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[3652] _id=6ab52dcf485cab4c9551cb5f ts=2026-09-24T14:03:58.7650000Z; 17ms: 6aa4140b41b41dbac0c7f22e.jsonl[3649] _id=6ab52dce485cab4c9551cb53 ts=2026-09-24T14:03:58.6910000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[3641] _id=6ab52dce485cab4c9551cb55 ts=2026-09-24T14:03:58.7080000Z; 50ms: 6aa4140b41b41dbac0c7f22e.jsonl[3641] _id=6ab52dce485cab4c9551cb55 ts=2026-09-24T14:03:58.7080000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[3642] _id=6ab52dcf485cab4c9551cb5b ts=2026-09-24T14:03:58.7580000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 10m 
  - Evidence: 192h 10m: 6aa4140b41b41dbac0c7f22e.jsonl[9241] _id=6abbc6b5485cab4c957e623b ts=2026-09-29T14:09:57.5260000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15068] _id=6ac65546de269131f9bab50c ts=2026-10-07T14:20:54.8080000Z; 143h 42m: 6aa4140b41b41dbac0c7f22e.jsonl[962] _id=6ab3e157485cab4c954d24a9 ts=2026-09-23T14:25:27.1470000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[9152] _id=6abbc655485cab4c957e5e6b ts=2026-09-29T14:08:21.8680000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 10m 
  - Evidence: 192h 10m: 6aa4140b41b41dbac0c7f22e.jsonl[9234] _id=6abbc6b5485cab4c957e6247 ts=2026-09-29T14:09:57.6040000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15057] _id=6ac65541de269131f9bab442 ts=2026-10-07T14:20:48.9810000Z; 143h 42m: 6aa4140b41b41dbac0c7f22e.jsonl[956] _id=6ab3e157485cab4c954d24af ts=2026-09-23T14:25:27.1830000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[9074] _id=6abbc621485cab4c957e598b ts=2026-09-29T14:07:29.6030000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.028s..0.028s shown 
  - Evidence: 28ms: 6aa4140b41b41dbac0c7f22e.jsonl[15146] _id=6ac655d6de269131f9bac50f ts=2026-10-07T14:23:18.2040000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15149] _id=6ac655d6de269131f9bac512 ts=2026-10-07T14:23:18.2320000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 192h 10m 
  - Evidence: 192h 10m: 6aa4140b41b41dbac0c7f22e.jsonl[9229] _id=6abbc6b4485cab4c957e6233 ts=2026-09-29T14:09:56.1640000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15061] _id=6ac65542de269131f9bab466 ts=2026-10-07T14:20:50.1250000Z; 120h 15m: 6aa4140b41b41dbac0c7f22e.jsonl[3299] _id=6ab52b23485cab4c95519e43 ts=2026-09-24T13:52:35.2570000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[9090] _id=6abbc627485cab4c957e59d9 ts=2026-09-29T14:07:35.4800000Z; 23h 27m: 6aa4140b41b41dbac0c7f22e.jsonl[952] _id=6ab3e14f485cab4c954d245b ts=2026-09-23T14:25:19.4530000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[3231] _id=6ab52b22485cab4c95519e2d ts=2026-09-24T13:52:34.5660000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 43 interval(s) ≤ 0.016s..0.023s shown 
  - Evidence: 16ms: 6aa4140b41b41dbac0c7f22e.jsonl[15141] _id=6ac655cfde269131f9bac447 ts=2026-10-07T14:23:11.7040000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15138] _id=6ac655cfde269131f9bac449 ts=2026-10-07T14:23:11.7200000Z; 17ms: 6aa4140b41b41dbac0c7f22e.jsonl[15100] _id=6ac655afde269131f9bac057 ts=2026-10-07T14:22:39.0620000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15101] _id=6ac655afde269131f9bac058 ts=2026-10-07T14:22:39.0790000Z; 23ms: 6aa4140b41b41dbac0c7f22e.jsonl[15121] _id=6ac655bcde269131f9bac203 ts=2026-10-07T14:22:52.1260000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[15122] _id=6ac655bcde269131f9bac207 ts=2026-10-07T14:22:52.1490000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 43m 
  - Evidence: 143h 43m: 6aa4140b41b41dbac0c7f22e.jsonl[846] _id=6ab3e0fe485cab4c954d2131 ts=2026-09-23T14:23:58.6940000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[9107] _id=6abbc633485cab4c957e5a86 ts=2026-09-29T14:07:47.9580000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 143h 55m 
  - Evidence: 143h 55m: 6aa4140b41b41dbac0c7f22e.jsonl[8484] _id=6abbc34a485cab4c957e0c6f ts=2026-09-29T13:55:22.3330000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10815] _id=6ac3ab45de269131f9a9ee31 ts=2026-10-05T13:51:01.1280000Z; 71h 47m: 6aa4140b41b41dbac0c7f22e.jsonl[4349] _id=6ab67e3f485cab4c9555b65c ts=2026-09-25T13:59:27.5700000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6255] _id=6aba6fcd485cab4c95681b29 ts=2026-09-28T13:46:53.1990000Z; 24h 22m: 6aa4140b41b41dbac0c7f22e.jsonl[12194] _id=6ac4fc43de269131f9b180a9 ts=2026-10-06T13:48:50.8180000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[14822] _id=6ac652f7de269131f9ba6a1a ts=2026-10-07T14:11:03.7640000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 55m 
  - Evidence: 143h 55m: 6aa4140b41b41dbac0c7f22e.jsonl[8483] _id=6abbc34a485cab4c957e0c6b ts=2026-09-29T13:55:22.3320000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10839] _id=6ac3ab45de269131f9a9ee2c ts=2026-10-05T13:51:01.1260000Z; 71h 47m: 6aa4140b41b41dbac0c7f22e.jsonl[4348] _id=6ab67e3f485cab4c9555b658 ts=2026-09-25T13:59:27.5680000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6252] _id=6aba6fcd485cab4c95681b27 ts=2026-09-28T13:46:53.1980000Z; 24h 18m: 6aa4140b41b41dbac0c7f22e.jsonl[1212] _id=6ab5279c485cab4c955136eb ts=2026-09-24T13:37:32.2020000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4308] _id=6ab67d5e485cab4c9555a440 ts=2026-09-25T13:55:42.7420000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 168h 27m 
  - Evidence: 168h 27m: 6aa4140b41b41dbac0c7f22e.jsonl[6311] _id=6aba7100485cab4c95682e2b ts=2026-09-28T13:52:00.3320000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[11991] _id=6ac3b1eede269131f9ab52e0 ts=2026-10-05T14:19:26.8450000Z; 71h 51m: 6aa4140b41b41dbac0c7f22e.jsonl[4328] _id=6ab67d83485cab4c9555a68a ts=2026-09-25T13:56:19.6240000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6261] _id=6aba6fe9485cab4c95681b63 ts=2026-09-28T13:47:21.4360000Z; 24h 18m: 6aa4140b41b41dbac0c7f22e.jsonl[1200] _id=6ab52797485cab4c95513633 ts=2026-09-24T13:37:27.1770000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4326] _id=6ab67d7e485cab4c9555a622 ts=2026-09-25T13:56:14.2980000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 20m 
  - Evidence: 143h 20m: 6aa4140b41b41dbac0c7f22e.jsonl[10774] _id=6abbcb80485cab4c957edbd3 ts=2026-09-29T14:30:24.8080000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[10825] _id=6ac3ab51de269131f9a9f0e8 ts=2026-10-05T13:51:13.2910000Z; 71h 28m: 6aa4140b41b41dbac0c7f22e.jsonl[5801] _id=6ab682ab485cab4c95561f4c ts=2026-09-25T14:18:19.8680000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[6265] _id=6aba6fde485cab4c95681b4f ts=2026-09-28T13:47:10.2180000Z; 23h 57m: 6aa4140b41b41dbac0c7f22e.jsonl[3453] _id=6ab52c94485cab4c9551ba47 ts=2026-09-24T13:58:44.6900000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[4324] _id=6ab67d6c485cab4c9555a578 ts=2026-09-25T13:55:55.2700000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6aa4140b41b41dbac0c7f22e.jsonl[782] _id=6ab3e008485cab4c954d157f ts=2026-09-23T14:19:51.9350000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[767] _id=6ab3e008485cab4c954d1581 ts=2026-09-23T14:19:51.9380000Z; 4ms: 6aa4140b41b41dbac0c7f22e.jsonl[13679] _id=6ac4fffade269131f9b24cc6 ts=2026-10-06T14:04:42.4320000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[13680] _id=6ac4fffade269131f9b24cc8 ts=2026-10-06T14:04:42.4360000Z; 5ms: 6aa4140b41b41dbac0c7f22e.jsonl[13210] _id=6ac4fe94de269131f9b2293b ts=2026-10-06T13:58:44.3330000Z -> 6aa4140b41b41dbac0c7f22e.jsonl[13211] _id=6ac4fe94de269131f9b22940 ts=2026-10-06T13:58:44.3380000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[3291] _id=6ab52b1d485cab4c95519dff ts=2026-09-24T13:52:29.2150000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[3293] _id=6ab52b1d485cab4c95519e03 ts=2026-09-24T13:52:29.4040000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[699] _id=6ab3dfde485cab4c954d12b9 ts=2026-09-23T14:19:10.1660000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[969] _id=6ab3e16b485cab4c954d2595 ts=2026-09-23T14:25:47.0860000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[5513] _id=6ab680f5485cab4c9555d73c ts=2026-09-25T14:11:01.2260000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 102 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[1945] _id=6ab52928485cab4c95516451 ts=2026-09-24T13:44:08.3290000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1988] _id=6ab52929485cab4c95516458 ts=2026-09-24T13:44:08.4170000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1996] _id=6ab52929485cab4c9551645b ts=2026-09-24T13:44:08.4220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 320 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[1779] _id=6ab5290e485cab4c95515ed4 ts=2026-09-24T13:41:02.3300000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1773] _id=6ab5290e485cab4c95515ed9 ts=2026-09-24T13:41:02.3300000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1784] _id=6ab5290e485cab4c95515edf ts=2026-09-24T13:41:02.3310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[9234] _id=6abbc6b5485cab4c957e6247 ts=2026-09-29T14:09:57.6040000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[15149] _id=6ac655d6de269131f9bac512 ts=2026-10-07T14:23:18.2320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[3299] _id=6ab52b23485cab4c95519e43 ts=2026-09-24T13:52:35.2570000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[13210] _id=6ac4fe94de269131f9b2293b ts=2026-10-06T13:58:44.3330000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[19] _id=6ab3da52485cab4c954ce365 ts=?`; `6aa4140b41b41dbac0c7f22e.jsonl[8487] _id=6abbc35a485cab4c957e0daf ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 353 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[1875] _id=6ab52916485cab4c9551608d ts=2026-09-24T13:43:35.5080000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1876] _id=6ab52917485cab4c95516093 ts=2026-09-24T13:43:35.5080000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1882] _id=6ab52917485cab4c95516099 ts=2026-09-24T13:43:35.5080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 486 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[1786] _id=6ab5290e485cab4c95515ee3 ts=2026-09-24T13:41:02.3800000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1803] _id=6ab52910485cab4c95515f1d ts=2026-09-24T13:41:02.7710000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1804] _id=6ab52910485cab4c95515f2d ts=2026-09-24T13:41:02.8180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[3642] _id=6ab52dcf485cab4c9551cb5b ts=2026-09-24T14:03:58.7580000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[3652] _id=6ab52dcf485cab4c9551cb5f ts=2026-09-24T14:03:58.7650000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[3682] _id=6ab52df8485cab4c9551ccfd ts=2026-09-24T14:04:40.7070000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[15121] _id=6ac655bcde269131f9bac203 ts=2026-10-07T14:22:52.1260000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[15129] _id=6ac655c4de269131f9bac310 ts=2026-10-07T14:23:00.9220000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[15136] _id=6ac655cade269131f9bac39e ts=2026-10-07T14:23:06.0610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[863] _id=6ab3e0fb485cab4c954d2117 ts=2026-09-23T14:23:55.5080000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[864] _id=6ab3e0fc485cab4c954d211f ts=2026-09-23T14:23:56.3270000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 365 start, 354 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 160 unmatched 'BecameCameraCentered' (totals: 527 open, 469 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 130 unmatched 'BecameVisible' (totals: 730 open, 920 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 22 open, 20 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 72 open, 72 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 6 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 40 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 366 of 15766 adjacent _id pairs reverse in client time; worst 158.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f22e.jsonl[1771] _id=6ab5290d485cab4c95515ead ts=2026-09-24T13:43:41.0420000Z`; `6aa4140b41b41dbac0c7f22e.jsonl[1772] _id=6ab5290e485cab4c95515ec1 ts=2026-09-24T13:41:02.3300000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -163.58s, max +0.27s over 15767 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22e\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `InputEvent` — 8704 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2766); Unit 2 Prod (Refactor) (2234); Unit 3 Dungeon Dev (1076); Unit 4 Dev - Dungeon (1058); Unit 4 Dev (878); Unit 1 Dev (576); Unit 4 Dev - Anderson Base (116)
- **Intervals:** median 0.28s (p5 0.03s / p95 3.38s, n=8703)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 8704/8704 records)
    "pressed"  x8704
data.actionType  (string, 8704/8704 records)
    "Move"  x7058
    "Interact"  x627
    "Jump"  x418
    "Hoverboard"  x256
    "Sprint"  x148
    "Ascend"  x119
    "Descend"  x39
    "Pause"  x32
    "Map"  x5
    "SkipCinematic"  x2
data.key  (string, 8704/8704 records, 20 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 8704/8704 records)
    "Player"  x7166
    "Drone"  x1538
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2646 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1838); Unit 4 Dev (502); Unit 3 Dungeon Dev (306)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.03s, n=2645)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2646/2646 records)
    "BecameInvisible"  x920
    "BecameVisible"  x730
    "BecameCameraCentered"  x527
    "BecameCameraUncentered"  x469
data.pieceId  (string, 2646/2646 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2646/2646 records)
    1439 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1782 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (471); Unit 2 Prod (Refactor) (470); Unit 4 Dev (262); Unit 3 Dungeon Dev (226); Unit 1 Dev (191); Unit 4 Dev - Dungeon (82); Unit 4 Dev - Anderson Base (80)
- **eventKey:** present on 1063 of 1782 records
- **Intervals:** median 4.32s (p5 0.00s / p95 41.75s, n=1781)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1063; [conversationId, dialogueEventType] x719
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1782/1782 records)
    numeric range 8 .. 114 (42 unique)
data.dialogueEventType  (string, 1782/1782 records)
    "DialogueNodeEvent"  x1063
    "DialogueStartEvent"  x365
    "DialogueFinishEvent"  x354
data.nodeId  (number, 1063/1782 records)
    numeric range 0 .. 290 (220 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1713 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (470); Unit 2 Prod (Refactor) (432); Unit 4 Dev (256); Unit 1 Dev (196); Unit 3 Dungeon Dev (157); Unit 4 Dev - Dungeon (120); Unit 4 Dev - Anderson Base (82)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.08s, n=1701)
- **Fields under `data`:**

```text
data.position  (object, 1713/1713 records)
data.position.x  (number, 1713/1713 records)
    numeric range -707.908 .. 1555.76 (562 unique)
data.position.y  (number, 1713/1713 records)
    numeric range -113.435 .. 158.925 (462 unique)
data.position.z  (number, 1713/1713 records)
    numeric range -1201.75 .. 1911.64 (561 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 247 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (79); Unit 3 Dungeon Dev (61); Unit 2 Prod (Refactor) (45); Unit 4 Dev (29); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 7.37s (p5 0.56s / p95 643.92s, n=246)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 247/247 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 247/247 records)
    85 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 177 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (97); Unit 4 Dev - Anderson Base (59); Unit 1 Dev (15); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 0.30s (p5 0.03s / p95 9.09s, n=176)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 177/177 records)
    "argumentationNodeHoverEnd"  x72
    "argumentationNodeHoverStart"  x72
    "argumentationNodeAdd"  x22
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 177/177 records)
    "Unit 3 - Pollution Upstream"  x97
    "Unit 4 - Flooding"  x59
    "Unit 1 - Freshwater"  x13
    "Unit 2 – Watershed"  x6
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 177/177 records)
    "A"  x37
    "1"  x32
    "B"  x20
    "I"  x20
    "2"  x19
    "3"  x14
    "4"  x10
    "II"  x9
    "C"  x8
    "D"  x5
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationAnswerEvent` — 102 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (90); Unit 3 Dev (7); Unit 4 Dev - Anderson Base (5)
- **Intervals:** median 0.19s (p5 0.10s / p95 18.70s, n=101)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 102/102 records)
    "submitAnswerEvent"  x102
data.answerSubmitted  (string, 102/102 records, 84 empty-string)
    ""  x84
    "A,1,I"  x10
    "A,C,D,2,II"  x2
    "A,2,I"  x1
    "A,3,I"  x1
    "A,4,I"  x1
    "A,5,I"  x1
    "A,B,1,I"  x1
    "B,1,I"  x1
data.argumentationTitle  (string, 102/102 records)
    "Unit 1 - Freshwater"  x90
    "Unit 3 - Pollution Upstream"  x7
    "Unit 4 - Flooding"  x5
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 89 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (72); Unit 3 Dev (17)
- **Intervals:** median 1.67s (p5 0.25s / p95 606.04s, n=88)
- **`data` key-set variants:** [actionType, featureUsed, location] x47; [actionType, featureUsed] x42
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 89/89 records)
    "WaypointMoveEvent"  x43
    "MapOpenEvent"  x22
    "MapCloseEvent"  x20
    "WaypointSetEvent"  x4
data.featureUsed  (string, 89/89 records)
    "Waypoint"  x47
    "Map"  x42
data.location  (object, 47/89 records)
data.location.x  (number, 47/89 records)
    numeric range -293.09 .. 454.91 (40 unique)
data.location.y  (number, 47/89 records)
    numeric range -294.5 .. 231.5 (43 unique)
data.location.z  (number, 47/89 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 64 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (15); Unit 2 Prod (Refactor) (14); Unit 1 Dev (12); Unit 4 Dev (8); Unit 4 Dev - Dungeon (8); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 64 of 64 records
- **Intervals:** median 267.40s (p5 0.01s / p95 85137.60s, n=63)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 64/64 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x24
data.questID  (string, 64/64 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 64/64 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/64 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (20); Unit 4 Dev (14)
- **Intervals:** median 0.78s (p5 0.14s / p95 17440.99s, n=57)
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
    "CLAYSAND"  x11
    "SAND"  x11
    "CLAY"  x10
    "CLAYROCK"  x8
    "SANDGRAVEL"  x6
    "BEDROCK"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 50/58 records)
    "false"  x36
    "true"  x14
data.waterLevelStatus  (string, 50/58 records)
    "Proper"  x21
    "TooHigh"  x18
    "TooLow"  x11
data.waterRetentionChange  (string, 50/58 records)
    "Increase"  x20
    "Decrease"  x16
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DaniEvent` — 56 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 1 Dev (10); Unit 3 Dev (6); Unit 4 Dev (6); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.07s (p5 0.00s / p95 88842.73s, n=55)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 56/56 records)
    "Close"  x29
    "Open"  x27
data.toolName  (string, 56/56 records, 50 empty-string)
    ""  x50
    "Settings"  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 1 Dev (5); Unit 2 Prod (Refactor) (5); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 191.46s (p5 4.91s / p95 207159.10s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 25 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (5); Unit 4 Dev (5); MainMenu (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1236.21s (p5 39.32s / p95 232808.48s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "DebugMenuStateChanged"  x25
data.isOpened  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 7058.15s (p5 134.85s / p95 336353.58s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (5); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 153.02s (p5 2.17s / p95 380386.46s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 8.01s (p5 1.76s / p95 3426.52s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 5 empty-string)
    "cameraPlaced"  x6
    ""  x5
data.boxId  (string, 11/11 records)
    "0"  x5
    "1"  x3
    "2"  x3
data.soilType  (string, 11/11 records)
    "Clay"  x3
    "None"  x3
    "Sand"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 1.46s (p5 0.31s / p95 144.49s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Clay"  x8
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 11/11 records)
    "4"  x9
    "5"  x2
data.machine  (string, 11/11 records)
    "1"  x10
    "2"  x1
data.row  (string, 11/11 records)
    "TopRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 109.42s (p5 0.04s / p95 622039.79s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (2)
- **Intervals:** median 3.11s (p5 0.32s / p95 336363.98s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x6
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 1036481.78s (p5 1036481.78s / p95 1036481.78s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.78s (p5 1.78s / p95 1.78s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[18-210, 18-75, 18-76, 18-77, 18-79]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

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
    "unit3"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DaniEvent` actionType: tool open/close: close without preceding open
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (43x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (47x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*