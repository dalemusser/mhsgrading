# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f230

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f230
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f230.jsonl
- **Records:** 8432 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f230
- **Time span:** 2026-09-23T13:55:15.678000+00:00 .. 2026-10-06T16:17:06.088000+00:00 (314h 21m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f230\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 8432 records, 5 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 103 INFO, 5 NOT_TESTED, 71 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2908 | 34.49 | 1 | 1 | 0 | 2026-09-25T14:11:31.855000+00:00 | 2026-10-05T13:57:59.420000+00:00 | 239h 46m |
| InputEvent | 2166 | 25.69 | 1 | 3 | 0 | 2026-09-23T13:58:28.560000+00:00 | 2026-10-06T16:15:32.200000+00:00 | 314h 17m |
| PlayerPositionEvent | 1443 | 17.11 | 1 | 3 | 0 | 2026-09-23T13:55:26.072000+00:00 | 2026-10-06T16:17:03.251000+00:00 | 314h 21m |
| DialogueEvent | 1136 | 13.47 | 1 | 3 | 760 | 2026-09-23T13:55:47.728000+00:00 | 2026-10-06T16:16:59.146000+00:00 | 314h 21m |
| argumentationNodeEvent | 258 | 3.06 | 1 | 2 | 0 | 2026-09-24T14:01:52.676000+00:00 | 2026-10-06T16:09:07.596000+00:00 | 290h 7m |
| ObjectInterEvent | 140 | 1.66 | 1 | 3 | 0 | 2026-09-23T14:17:15.447000+00:00 | 2026-10-06T15:53:50.111000+00:00 | 313h 36m |
| DaniEvent | 95 | 1.13 | 1 | 3 | 0 | 2026-09-23T14:00:14.076000+00:00 | 2026-10-06T16:12:41.246000+00:00 | 314h 12m |
| gameWindowFocusEvent | 60 | 0.71 | 1 | 4 | 0 | 2026-09-23T13:55:15.678000+00:00 | 2026-10-06T16:13:15.770000+00:00 | 314h 18m |
| gameWindowUnfocusEvent | 58 | 0.69 | 1 | 4 | 0 | 2026-09-23T14:00:06.740000+00:00 | 2026-10-06T16:17:06.088000+00:00 | 314h 16m |
| questEvent | 48 | 0.57 | 1 | 3 | 48 | 2026-09-23T13:55:47.707000+00:00 | 2026-10-06T16:10:47.781000+00:00 | 314h 15m |
| TopographicMapEvent | 39 | 0.46 | 1 | 3 | 0 | 2026-09-24T14:01:58.321000+00:00 | 2026-10-06T16:09:52.676000+00:00 | 290h 7m |
| Soil Key Puzzle | 18 | 0.21 | 1 | 1 | 0 | 2026-09-25T14:19:36.057000+00:00 | 2026-09-28T14:08:26.070000+00:00 | 71h 48m |
| DEBUGMenu | 13 | 0.15 | 1 | 3 | 0 | 2026-09-23T13:55:26.065000+00:00 | 2026-10-06T15:50:41.092000+00:00 | 313h 55m |
| gameStartEvent | 13 | 0.15 | 1 | 1 | 0 | 2026-09-23T13:55:15.679000+00:00 | 2026-10-06T15:50:30.887000+00:00 | 313h 55m |
| argumentationToolEvent | 10 | 0.12 | 1 | 2 | 0 | 2026-09-25T14:00:32.747000+00:00 | 2026-10-06T16:07:45.802000+00:00 | 266h 7m |
| argumentationAnswerEvent | 8 | 0.09 | 1 | 2 | 0 | 2026-09-25T13:59:39.342000+00:00 | 2026-10-06T16:09:10.146000+00:00 | 266h 9m |
| argumentationEvent | 7 | 0.08 | 1 | 2 | 0 | 2026-09-25T13:59:12.899000+00:00 | 2026-10-06T16:09:10.200000+00:00 | 266h 9m |
| crash | 7 | 0.08 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 4 | 0.05 | 1 | 1 | 0 | 2026-09-24T14:02:04.816000+00:00 | 2026-09-24T14:02:10.528000+00:00 | 5.7s |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-25T14:04:56.885000+00:00 | 2026-09-25T14:04:56.885000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 45894.531s median 
  - Expected: 795.292s in 09-23-26 
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
  - Observed: 34.589s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 1.062s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 45886.9s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 95 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; backquote; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.waterLevelStatus` — baseline categorical value(s) not seen this build. 
  - Observed: TooLow 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointMoveEvent; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 240 ft; 30 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,3,I; B,2,I; B,2,II 
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
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [30-33, 30-37, 30-38, 30-40, 30-42]; [31-35, 31-38, 31-39, 31-41, 31-45] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 18 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[395] _id=6ab3e069485cab4c954d1a3f ts=2026-09-23T14:21:29.1810000Z`; `6aa4140b41b41dbac0c7f230.jsonl[496] _id=6ab3e1df485cab4c954d2a05 ts=2026-09-23T14:27:43.5030000Z`; `6aa4140b41b41dbac0c7f230.jsonl[509] _id=6ab3e248485cab4c954d2dcc ts=2026-09-23T14:29:28.2530000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[4865] _id=6abbc394485cab4c957e134d ts=2026-09-29T13:56:33.0580000Z`; `6aa4140b41b41dbac0c7f230.jsonl[5917] _id=6ac3ab7fde269131f9a9fcde ts=2026-10-05T13:51:58.2330000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[26] _id=6ab3da44485cab4c954ce349 ts=2026-09-23T13:55:15.6790000Z`; `6aa4140b41b41dbac0c7f230.jsonl[202] _id=6ab3dcb3485cab4c954cf55f ts=2026-09-23T14:05:39.3440000Z`; `6aa4140b41b41dbac0c7f230.jsonl[544] _id=6ab527b8485cab4c95513945 ts=2026-09-24T13:38:00.4690000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 60 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 60} 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[27] _id=6ab3da44485cab4c954ce347 ts=2026-09-23T13:55:15.6780000Z`; `6aa4140b41b41dbac0c7f230.jsonl[150] _id=6ab3db67485cab4c954cea9e ts=2026-09-23T14:00:06.7490000Z`; `6aa4140b41b41dbac0c7f230.jsonl[201] _id=6ab3dcb3485cab4c954cf55d ts=2026-09-23T14:05:39.3430000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 58 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 58} 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[120] _id=6ab3db67485cab4c954cea97 ts=2026-09-23T14:00:06.7400000Z`; `6aa4140b41b41dbac0c7f230.jsonl[177] _id=6ab3dba6485cab4c954cec9b ts=2026-09-23T14:01:10.3630000Z`; `6aa4140b41b41dbac0c7f230.jsonl[383] _id=6ab3e056485cab4c954d18ed ts=2026-09-23T14:21:10.2130000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 10 of 39 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[987] _id=6ab52d56485cab4c9551c61b ts=2026-09-24T14:01:58.3210000Z`; `6aa4140b41b41dbac0c7f230.jsonl[991] _id=6ab52d58485cab4c9551c645 ts=2026-09-24T14:02:00.9200000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1589] _id=6ab6812f485cab4c9555dae1 ts=2026-09-25T14:11:59.3330000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2907 | 0.0 | 0.03 | 296.934 | 1.04 | 517573.102 | 0.2 | 1822 | 4 |
| InputEvent | 2165 | 0.001 | 0.541 | 522.598 | 17.644 | 517084.893 | 0.11 | 120 | 8 |
| PlayerPositionEvent | 1440 | 9.938 | 9.999 | 785.765 | 10.298 | 516030.584 | 0.08 | 0 | 7 |
| DialogueEvent | 1135 | 0.0 | 3.781 | 997.067 | 47.676 | 516033.013 | 0.06 | 309 | 8 |
| argumentationNodeEvent | 257 | 0.019 | 0.333 | 4063.949 | 11.148 | 957806.762 | 0.01 | 60 | 2 |
| ObjectInterEvent | 139 | 0.004 | 5.173 | 8122.264 | 662.809 | 517700.54 | 0.01 | 2 | 7 |
| DaniEvent | 94 | 0.002 | 1.871 | 12033.481 | 978.05 | 604996.238 | 0.0 | 24 | 7 |
| gameWindowFocusEvent | 59 | 0.014 | 107.567 | 19177.629 | 84702.042 | 518106.057 | 0.0 | 1 | 12 |
| gameWindowUnfocusEvent | 57 | 0.0 | 90.009 | 19849.462 | 84586.419 | 516190.411 | 0.0 | 2 | 13 |
| questEvent | 47 | 0.001 | 233.381 | 24070.214 | 85582.995 | 517084.349 | 0.0 | 8 | 14 |
| TopographicMapEvent | 38 | 0.008 | 3.496 | 27486.167 | 117507.576 | 604858.434 | 0.0 | 3 | 4 |
| Soil Key Puzzle | 17 | 0.297 | 1.402 | 15207.648 | 51706.375 | 258485.137 | 0.0 | 0 | 1 |
| DEBUGMenu | 12 | 36.623 | 45894.531 | 94176.252 | 375094.153 | 518125.075 | 0.0 | 0 | 10 |
| gameStartEvent | 12 | 35.181 | 45886.9 | 94176.267 | 375110.301 | 518139.293 | 0.0 | 0 | 10 |
| argumentationToolEvent | 9 | 1.031 | 10.699 | 106448.117 | 574785.832 | 957961.052 | 0.0 | 0 | 1 |
| argumentationAnswerEvent | 7 | 5.505 | 34.589 | 136881.543 | 670565.521 | 957902.258 | 0.0 | 0 | 1 |
| argumentationEvent | 6 | 0.032 | 45.383 | 159699.55 | 718417.901 | 957799.387 | 0.0 | 1 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 3 | 0.978 | 1.062 | 1.904 | 3.411 | 3.672 | 31.51 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 143 group(s), 199 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1559] _id=6ab68116485cab4c9555d920 ts=2026-09-25T14:11:32.5790000Z == 6aa4140b41b41dbac0c7f230.jsonl[1569] _id=6ab68116485cab4c9555d922 ts=2026-09-25T14:11:32.5790000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1565] _id=6ab68116485cab4c9555d928 ts=2026-09-25T14:11:32.6630000Z == 6aa4140b41b41dbac0c7f230.jsonl[1560] _id=6ab68116485cab4c9555d92c ts=2026-09-25T14:11:32.6630000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1523] _id=6ab68117485cab4c9555d948 ts=2026-09-25T14:11:33.4400000Z == 6aa4140b41b41dbac0c7f230.jsonl[1534] _id=6ab68117485cab4c9555d94a ts=2026-09-25T14:11:33.4400000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[29] _id=6ab3da53485cab4c954ce37f ts=? == 6aa4140b41b41dbac0c7f230.jsonl[1039] _id=6ab52e81485cab4c9551d1af ts=?`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `100ms: 6aa4140b41b41dbac0c7f230.jsonl[978] _id=6ab52d3f485cab4c9551c4e7 ts=2026-09-24T14:01:35.7190000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[980] _id=6ab52d40485cab4c9551c4f1 ts=2026-09-24T14:01:35.8190000Z`; `4ms: 6aa4140b41b41dbac0c7f230.jsonl[6534] _id=6ac3ad83de269131f9aa6693 ts=2026-10-05T14:00:35.5170000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[6529] _id=6ac3ad83de269131f9aa66a4 ts=2026-10-05T14:00:35.5210000Z`; `407ms: 6aa4140b41b41dbac0c7f230.jsonl[6548] _id=6ac3ad86de269131f9aa6724 ts=2026-10-05T14:00:38.6380000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[6552] _id=6ac3ad87de269131f9aa6739 ts=2026-10-05T14:00:39.0450000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 54 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4140b41b41dbac0c7f230.jsonl[326] _id=6ab3df6b485cab4c954d0d1b ts=2026-09-23T14:17:15.4470000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[327] _id=6ab3df6b485cab4c954d0d1f ts=2026-09-23T14:17:15.4510000Z`; `6ms: 6aa4140b41b41dbac0c7f230.jsonl[584] _id=6ab527fd485cab4c95513d53 ts=2026-09-24T13:39:09.2240000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[580] _id=6ab527fd485cab4c95513d59 ts=2026-09-24T13:39:09.2300000Z`; `156ms: 6aa4140b41b41dbac0c7f230.jsonl[891] _id=6ab52cfc485cab4c9551c027 ts=2026-09-24T14:00:28.0210000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[906] _id=6ab52cfc485cab4c9551c02d ts=2026-09-24T14:00:28.1770000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 516 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa4140b41b41dbac0c7f230.jsonl[1556] _id=6ab68115485cab4c9555d914 ts=2026-09-25T14:11:32.0630000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1551] _id=6ab68115485cab4c9555d916 ts=2026-09-25T14:11:32.0800000Z`; `69ms: 6aa4140b41b41dbac0c7f230.jsonl[1569] _id=6ab68116485cab4c9555d922 ts=2026-09-25T14:11:32.5790000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1570] _id=6ab68116485cab4c9555d924 ts=2026-09-25T14:11:32.6480000Z`; `15ms: 6aa4140b41b41dbac0c7f230.jsonl[1570] _id=6ab68116485cab4c9555d924 ts=2026-09-25T14:11:32.6480000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1565] _id=6ab68116485cab4c9555d928 ts=2026-09-25T14:11:32.6630000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `43ms: 6aa4140b41b41dbac0c7f230.jsonl[3366] _id=6aba72bd485cab4c9568616d ts=2026-09-28T13:59:25.2890000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[3369] _id=6aba72bd485cab4c95686175 ts=2026-09-28T13:59:25.3320000Z`; `8ms: 6aa4140b41b41dbac0c7f230.jsonl[3369] _id=6aba72bd485cab4c95686175 ts=2026-09-28T13:59:25.3320000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[3355] _id=6aba72bd485cab4c95686179 ts=2026-09-28T13:59:25.3400000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: 6aa4140b41b41dbac0c7f230.jsonl[8178] _id=6ac51d26de269131f9b4e273 ts=2026-10-06T16:09:10.1680000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[8185] _id=6ac51d26de269131f9b4e27b ts=2026-10-06T16:09:10.2000000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 49 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `672ms: 6aa4140b41b41dbac0c7f230.jsonl[1177] _id=6ab67dae485cab4c9555a99a ts=2026-09-25T13:57:02.2360000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1165] _id=6ab67dae485cab4c9555a9a4 ts=2026-09-25T13:57:02.9080000Z`; `877ms: 6aa4140b41b41dbac0c7f230.jsonl[1176] _id=6ab67dae485cab4c9555a9a0 ts=2026-09-25T13:57:02.5750000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1166] _id=6ab67daf485cab4c9555a9a8 ts=2026-09-25T13:57:03.4520000Z`; `644ms: 6aa4140b41b41dbac0c7f230.jsonl[1190] _id=6ab67df2485cab4c9555b176 ts=2026-09-25T13:58:10.3980000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1193] _id=6ab67df2485cab4c9555b192 ts=2026-09-25T13:58:11.0420000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `135ms: 6aa4140b41b41dbac0c7f230.jsonl[390] _id=6ab3e069485cab4c954d1a37 ts=2026-09-23T14:21:29.1640000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[397] _id=6ab3e069485cab4c954d1a47 ts=2026-09-23T14:21:29.2990000Z`; `14ms: 6aa4140b41b41dbac0c7f230.jsonl[4897] _id=6abbc394485cab4c957e135f ts=2026-09-29T13:56:33.1500000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[4905] _id=6abbc394485cab4c957e136b ts=2026-09-29T13:56:33.1640000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `717ms: 6aa4140b41b41dbac0c7f230.jsonl[1279] _id=6ab67e6d485cab4c9555b7df ts=2026-09-25T14:00:13.4270000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[1283] _id=6ab67e6e485cab4c9555b7ec ts=2026-09-25T14:00:14.1440000Z`; `15ms: 6aa4140b41b41dbac0c7f230.jsonl[4896] _id=6abbc394485cab4c957e1353 ts=2026-09-29T13:56:33.1420000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[4867] _id=6abbc394485cab4c957e1363 ts=2026-09-29T13:56:33.1570000Z`; `856ms: 6aa4140b41b41dbac0c7f230.jsonl[6888] _id=6ac3b281de269131f9ab7c43 ts=2026-10-05T14:21:53.0120000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[6887] _id=6ac3b281de269131f9ab7c8e ts=2026-10-05T14:21:53.8680000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa4140b41b41dbac0c7f230.jsonl[4865] _id=6abbc394485cab4c957e134d ts=2026-09-29T13:56:33.0580000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[4866] _id=6abbc394485cab4c957e1351 ts=2026-09-29T13:56:33.0650000Z`; `2ms: 6aa4140b41b41dbac0c7f230.jsonl[5917] _id=6ac3ab7fde269131f9a9fcde ts=2026-10-05T13:51:58.2330000Z ~ 6aa4140b41b41dbac0c7f230.jsonl[5913] _id=6ac3ab7fde269131f9a9fce3 ts=2026-10-05T13:51:58.2350000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 55m 
  - Evidence: 143h 55m: 6aa4140b41b41dbac0c7f230.jsonl[4888] _id=6abbc38a485cab4c957e124b ts=2026-09-29T13:56:26.7640000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5908] _id=6ac3ab77de269131f9a9fa92 ts=2026-10-05T13:51:51.8390000Z; 71h 41m: 6aa4140b41b41dbac0c7f230.jsonl[1429] _id=6ab68028485cab4c9555cdf8 ts=2026-09-25T14:07:36.7440000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3060] _id=6aba703d485cab4c95681d43 ts=2026-09-28T13:48:45.5970000Z; 24h 7m: 6aa4140b41b41dbac0c7f230.jsonl[3060] _id=6aba703d485cab4c95681d43 ts=2026-09-28T13:48:45.5970000Z -> 6aa4140b41b41dbac0c7f230.jsonl[4888] _id=6abbc38a485cab4c957e124b ts=2026-09-29T13:56:26.7640000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 168h 3m 
  - Evidence: 168h 3m: 6aa4140b41b41dbac0c7f230.jsonl[3336] _id=6aba723f485cab4c95685a75 ts=2026-09-28T13:57:19.2790000Z -> 6aa4140b41b41dbac0c7f230.jsonl[6534] _id=6ac3ad83de269131f9aa6693 ts=2026-10-05T14:00:35.5170000Z; 95h 41m: 6aa4140b41b41dbac0c7f230.jsonl[1055] _id=6ab52ead485cab4c9551d475 ts=2026-09-24T14:07:41.5740000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3107] _id=6aba7073485cab4c956820d9 ts=2026-09-28T13:49:39.1170000Z; 25h 20m: 6aa4140b41b41dbac0c7f230.jsonl[7119] _id=6ac3b475de269131f9abe3fc ts=2026-10-05T14:30:13.2170000Z -> 6aa4140b41b41dbac0c7f230.jsonl[7391] _id=6ac518eede269131f9b4c403 ts=2026-10-06T15:51:05.0160000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 24 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f230.jsonl[3114] _id=6aba7077485cab4c95682125 ts=2026-09-28T13:49:43.5030000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3115] _id=6aba7077485cab4c95682127 ts=2026-09-28T13:49:43.5050000Z; 2ms: 6aa4140b41b41dbac0c7f230.jsonl[6824] _id=6ac3b18ade269131f9ab3751 ts=2026-10-05T14:17:46.8860000Z -> 6aa4140b41b41dbac0c7f230.jsonl[6817] _id=6ac3b18ade269131f9ab3759 ts=2026-10-05T14:17:46.8880000Z; 2ms: 6aa4140b41b41dbac0c7f230.jsonl[708] _id=6ab52b3b485cab4c95519f0f ts=2026-09-24T13:52:59.6460000Z -> 6aa4140b41b41dbac0c7f230.jsonl[696] _id=6ab52b3b485cab4c95519f11 ts=2026-09-24T13:52:59.6480000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 20m 
  - Evidence: 143h 20m: 6aa4140b41b41dbac0c7f230.jsonl[5899] _id=6abbcbbd485cab4c957ee34f ts=2026-09-29T14:31:25.1970000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5910] _id=6ac3ab7fde269131f9a9fccc ts=2026-10-05T13:51:58.2100000Z; 71h 28m: 6aa4140b41b41dbac0c7f230.jsonl[2885] _id=6ab683d7485cab4c95563452 ts=2026-09-25T14:23:19.8880000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3198] _id=6aba70fe485cab4c95682dff ts=2026-09-28T13:51:59.0080000Z; 23h 55m: 6aa4140b41b41dbac0c7f230.jsonl[899] _id=6ab52cf9485cab4c9551bfe3 ts=2026-09-24T14:00:25.2260000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1159] _id=6ab67d7a485cab4c9555a5e6 ts=2026-09-25T13:56:10.9380000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 309 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f230.jsonl[8161] _id=6ac51d03de269131f9b4e185 ts=2026-10-06T16:08:35.5750000Z -> 6aa4140b41b41dbac0c7f230.jsonl[8156] _id=6ac51d03de269131f9b4e189 ts=2026-10-06T16:08:35.5750000Z; 1ms: 6aa4140b41b41dbac0c7f230.jsonl[1376] _id=6ab67f0f485cab4c9555bfc8 ts=2026-09-25T14:02:55.8690000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1377] _id=6ab67f0f485cab4c9555bfca ts=2026-09-25T14:02:55.8700000Z; 1ms: 6aa4140b41b41dbac0c7f230.jsonl[1471] _id=6ab680a9485cab4c9555d386 ts=2026-09-25T14:09:46.0640000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1472] _id=6ab680aa485cab4c9555d388 ts=2026-09-25T14:09:46.0650000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 38m 
  - Evidence: 143h 38m: 6aa4140b41b41dbac0c7f230.jsonl[5817] _id=6abbc7a1485cab4c957e6fa5 ts=2026-09-29T14:13:53.3040000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5912] _id=6ac3ab7fde269131f9a9fcc0 ts=2026-10-05T13:51:58.1970000Z; 71h 19m: 6aa4140b41b41dbac0c7f230.jsonl[3049] _id=6ab68539485cab4c955648c2 ts=2026-09-25T14:29:13.9380000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3078] _id=6aba7044485cab4c95681d8f ts=2026-09-28T13:48:51.8480000Z; 23h 47m: 6aa4140b41b41dbac0c7f230.jsonl[1054] _id=6ab52ead485cab4c9551d473 ts=2026-09-24T14:07:41.5690000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1090] _id=6ab67d35485cab4c9555a27c ts=2026-09-25T13:55:00.5930000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 120 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f230.jsonl[1059] _id=6ab67d36485cab4c9555a284 ts=2026-09-25T13:55:00.5940000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1060] _id=6ab67d36485cab4c9555a28c ts=2026-09-25T13:55:00.5950000Z; 1ms: 6aa4140b41b41dbac0c7f230.jsonl[1060] _id=6ab67d36485cab4c9555a28c ts=2026-09-25T13:55:00.5950000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1061] _id=6ab67d36485cab4c9555a28e ts=2026-09-25T13:55:00.5960000Z; 1ms: 6aa4140b41b41dbac0c7f230.jsonl[1061] _id=6ab67d36485cab4c9555a28e ts=2026-09-25T13:55:00.5960000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1062] _id=6ab67d36485cab4c9555a292 ts=2026-09-25T13:55:00.5970000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 48m 
  - Evidence: 143h 48m: 6aa4140b41b41dbac0c7f230.jsonl[5718] _id=6abbc5b4485cab4c957e4f37 ts=2026-09-29T14:05:40.6360000Z -> 6aa4140b41b41dbac0c7f230.jsonl[6100] _id=6ac3abfbde269131f9aa1843 ts=2026-10-05T13:54:01.1760000Z; 71h 48m: 6aa4140b41b41dbac0c7f230.jsonl[2816] _id=6ab682f8485cab4c9556255e ts=2026-09-25T14:19:36.0600000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3587] _id=6aba74b0485cab4c95687f21 ts=2026-09-28T14:07:44.1940000Z; 25h 24m: 6aa4140b41b41dbac0c7f230.jsonl[7106] _id=6ac3b441de269131f9abdc4f ts=2026-10-05T14:29:21.5580000Z -> 6aa4140b41b41dbac0c7f230.jsonl[7464] _id=6ac51993de269131f9b4c82f ts=2026-10-06T15:53:50.1110000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.006s shown 
  - Evidence: 4ms: 6aa4140b41b41dbac0c7f230.jsonl[326] _id=6ab3df6b485cab4c954d0d1b ts=2026-09-23T14:17:15.4470000Z -> 6aa4140b41b41dbac0c7f230.jsonl[327] _id=6ab3df6b485cab4c954d0d1f ts=2026-09-23T14:17:15.4510000Z; 6ms: 6aa4140b41b41dbac0c7f230.jsonl[584] _id=6ab527fd485cab4c95513d53 ts=2026-09-24T13:39:09.2240000Z -> 6aa4140b41b41dbac0c7f230.jsonl[580] _id=6ab527fd485cab4c95513d59 ts=2026-09-24T13:39:09.2300000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 20m 
  - Evidence: 143h 20m: 6aa4140b41b41dbac0c7f230.jsonl[5898] _id=6abbcbb9485cab4c957ee2bb ts=2026-09-29T14:31:21.2610000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5909] _id=6ac3ab7fde269131f9a9fcb6 ts=2026-10-05T13:51:51.8450000Z; 71h 19m: 6aa4140b41b41dbac0c7f230.jsonl[3055] _id=6ab68551485cab4c955649ac ts=2026-09-25T14:29:37.6460000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3077] _id=6aba7044485cab4c95681d8d ts=2026-09-28T13:48:45.6050000Z; 23h 47m: 6aa4140b41b41dbac0c7f230.jsonl[1053] _id=6ab52ea8485cab4c9551d43f ts=2026-09-24T14:07:36.9380000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1094] _id=6ab67d35485cab4c9555a278 ts=2026-09-25T13:54:55.4490000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 46m 
  - Evidence: 143h 46m: 6aa4140b41b41dbac0c7f230.jsonl[5770] _id=6abbc5bb485cab4c957e5097 ts=2026-09-29T14:05:45.4320000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5911] _id=6ac3ab80de269131f9a9fced ts=2026-10-05T13:51:58.5340000Z; 71h 39m: 6aa4140b41b41dbac0c7f230.jsonl[2779] _id=6ab68282485cab4c95561856 ts=2026-09-25T14:17:37.2720000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3327] _id=6aba7224485cab4c956858cd ts=2026-09-28T13:56:51.2960000Z; 23h 34m: 6aa4140b41b41dbac0c7f230.jsonl[4677] _id=6aba77f5485cab4c9568cb8b ts=2026-09-28T14:21:38.8520000Z -> 6aa4140b41b41dbac0c7f230.jsonl[4869] _id=6abbc394485cab4c957e1373 ts=2026-09-29T13:56:33.4280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1822 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f230.jsonl[1519] _id=6ab68117485cab4c9555d93e ts=2026-09-25T14:11:33.3770000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1520] _id=6ab68117485cab4c9555d940 ts=2026-09-25T14:11:33.3770000Z; 0ms: 6aa4140b41b41dbac0c7f230.jsonl[1523] _id=6ab68117485cab4c9555d948 ts=2026-09-25T14:11:33.4400000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1534] _id=6ab68117485cab4c9555d94a ts=2026-09-25T14:11:33.4400000Z; 0ms: 6aa4140b41b41dbac0c7f230.jsonl[1524] _id=6ab68117485cab4c9555d94e ts=2026-09-25T14:11:33.4400000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1525] _id=6ab68117485cab4c9555d950 ts=2026-09-25T14:11:33.4400000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 71h 48m 
  - Evidence: 71h 48m: 6aa4140b41b41dbac0c7f230.jsonl[2820] _id=6ab682fa485cab4c95562570 ts=2026-09-25T14:19:39.0510000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3586] _id=6aba74b0485cab4c95687f1d ts=2026-09-28T14:07:44.1880000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 0m 
  - Evidence: 168h 0m: 6aa4140b41b41dbac0c7f230.jsonl[3371] _id=6aba72c9485cab4c956861d1 ts=2026-09-28T13:59:37.0890000Z -> 6aa4140b41b41dbac0c7f230.jsonl[6538] _id=6ac3ad83de269131f9aa66ac ts=2026-10-05T14:00:35.5230000Z; 71h 40m: 6aa4140b41b41dbac0c7f230.jsonl[1610] _id=6ab68161485cab4c9555e087 ts=2026-09-25T14:12:49.1760000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3231] _id=6aba714e485cab4c95683851 ts=2026-09-28T13:53:18.5600000Z; 25h 45m: 6aa4140b41b41dbac0c7f230.jsonl[6962] _id=6ac3b32ade269131f9aba266 ts=2026-10-05T14:24:42.6660000Z -> 6aa4140b41b41dbac0c7f230.jsonl[8213] _id=6ac51d50de269131f9b4e3ff ts=2026-10-06T16:09:52.2760000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.008s..0.043s shown 
  - Evidence: 8ms: 6aa4140b41b41dbac0c7f230.jsonl[3369] _id=6aba72bd485cab4c95686175 ts=2026-09-28T13:59:25.3320000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3355] _id=6aba72bd485cab4c95686179 ts=2026-09-28T13:59:25.3400000Z; 15ms: 6aa4140b41b41dbac0c7f230.jsonl[3365] _id=6aba72bd485cab4c9568616b ts=2026-09-28T13:59:25.2740000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3366] _id=6aba72bd485cab4c9568616d ts=2026-09-28T13:59:25.2890000Z; 43ms: 6aa4140b41b41dbac0c7f230.jsonl[3366] _id=6aba72bd485cab4c9568616d ts=2026-09-28T13:59:25.2890000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3369] _id=6aba72bd485cab4c95686175 ts=2026-09-28T13:59:25.3320000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 266h 5m 
  - Evidence: 266h 5m: 6aa4140b41b41dbac0c7f230.jsonl[1336] _id=6ab67ead485cab4c9555bbee ts=2026-09-25T14:01:17.3170000Z -> 6aa4140b41b41dbac0c7f230.jsonl[8012] _id=6ac51c7bde269131f9b4dc31 ts=2026-10-06T16:06:19.5750000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 266h 3m 
  - Evidence: 266h 3m: 6aa4140b41b41dbac0c7f230.jsonl[1340] _id=6ab67ead485cab4c9555bbf0 ts=2026-09-25T14:01:17.3380000Z -> 6aa4140b41b41dbac0c7f230.jsonl[7948] _id=6ac51c14de269131f9b4d879 ts=2026-10-06T16:04:36.7250000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.032s..0.032s shown 
  - Evidence: 32ms: 6aa4140b41b41dbac0c7f230.jsonl[8178] _id=6ac51d26de269131f9b4e273 ts=2026-10-06T16:09:10.1680000Z -> 6aa4140b41b41dbac0c7f230.jsonl[8185] _id=6ac51d26de269131f9b4e27b ts=2026-10-06T16:09:10.2000000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 266h 3m 
  - Evidence: 266h 3m: 6aa4140b41b41dbac0c7f230.jsonl[1326] _id=6ab67ea9485cab4c9555bbb0 ts=2026-09-25T14:01:13.6600000Z -> 6aa4140b41b41dbac0c7f230.jsonl[7949] _id=6ac51c18de269131f9b4d88d ts=2026-10-06T16:04:40.4220000Z; 23h 55m: 6aa4140b41b41dbac0c7f230.jsonl[988] _id=6ab52d50485cab4c9551c597 ts=2026-09-24T14:01:52.7050000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1174] _id=6ab67dac485cab4c9555a97a ts=2026-09-25T13:57:00.9840000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 60 interval(s) ≤ 0.019s..0.022s shown 
  - Evidence: 19ms: 6aa4140b41b41dbac0c7f230.jsonl[1276] _id=6ab67e7e485cab4c9555b8be ts=2026-09-25T14:00:30.4980000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1298] _id=6ab67e7e485cab4c9555b8c0 ts=2026-09-25T14:00:30.5170000Z; 21ms: 6aa4140b41b41dbac0c7f230.jsonl[1203] _id=6ab67df6485cab4c9555b222 ts=2026-09-25T13:58:15.1080000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1202] _id=6ab67df7485cab4c9555b227 ts=2026-09-25T13:58:15.1290000Z; 22ms: 6aa4140b41b41dbac0c7f230.jsonl[1199] _id=6ab67df6485cab4c9555b1fe ts=2026-09-25T13:58:14.5840000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1200] _id=6ab67df6485cab4c9555b204 ts=2026-09-25T13:58:14.6060000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 266h 6m 
  - Evidence: 266h 6m: 6aa4140b41b41dbac0c7f230.jsonl[1308] _id=6ab67e99485cab4c9555ba2a ts=2026-09-25T14:00:57.1420000Z -> 6aa4140b41b41dbac0c7f230.jsonl[8056] _id=6ac51ca2de269131f9b4ddad ts=2026-10-06T16:06:58.1940000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 55m 
  - Evidence: 143h 55m: 6aa4140b41b41dbac0c7f230.jsonl[4863] _id=6abbc372485cab4c957e1021 ts=2026-09-29T13:56:01.3880000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5906] _id=6ac3ab6cde269131f9a9f832 ts=2026-10-05T13:51:40.6810000Z; 71h 41m: 6aa4140b41b41dbac0c7f230.jsonl[1424] _id=6ab68006485cab4c9555cc6c ts=2026-09-25T14:07:02.6720000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3058] _id=6aba702d485cab4c95681cc1 ts=2026-09-28T13:48:29.2530000Z; 24h 7m: 6aa4140b41b41dbac0c7f230.jsonl[3058] _id=6aba702d485cab4c95681cc1 ts=2026-09-28T13:48:29.2530000Z -> 6aa4140b41b41dbac0c7f230.jsonl[4863] _id=6abbc372485cab4c957e1021 ts=2026-09-29T13:56:01.3880000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 55m 
  - Evidence: 143h 55m: 6aa4140b41b41dbac0c7f230.jsonl[4868] _id=6abbc394485cab4c957e1371 ts=2026-09-29T13:56:34.6230000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5907] _id=6ac3ab6cde269131f9a9f826 ts=2026-10-05T13:51:40.6800000Z; 71h 37m: 6aa4140b41b41dbac0c7f230.jsonl[1542] _id=6ab6810d485cab4c9555d87c ts=2026-09-25T14:11:26.0510000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3057] _id=6aba702d485cab4c95681cbf ts=2026-09-28T13:48:29.2520000Z; 23h 46m: 6aa4140b41b41dbac0c7f230.jsonl[1057] _id=6ab52eb8485cab4c9551d4c5 ts=2026-09-24T14:07:52.5740000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1086] _id=6ab67d14485cab4c9555a15c ts=2026-09-25T13:54:28.9360000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.014s..0.014s shown 
  - Evidence: 14ms: 6aa4140b41b41dbac0c7f230.jsonl[4897] _id=6abbc394485cab4c957e135f ts=2026-09-29T13:56:33.1500000Z -> 6aa4140b41b41dbac0c7f230.jsonl[4905] _id=6abbc394485cab4c957e136b ts=2026-09-29T13:56:33.1640000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 143h 23m 
  - Evidence: 143h 23m: 6aa4140b41b41dbac0c7f230.jsonl[5900] _id=6abbcbbe485cab4c957ee377 ts=2026-09-29T14:31:26.1250000Z -> 6aa4140b41b41dbac0c7f230.jsonl[6348] _id=6ac3ac1cde269131f9aa20f0 ts=2026-10-05T13:54:36.5360000Z; 71h 52m: 6aa4140b41b41dbac0c7f230.jsonl[3056] _id=6ab68553485cab4c955649b6 ts=2026-09-25T14:29:39.2290000Z -> 6aa4140b41b41dbac0c7f230.jsonl[4691] _id=6aba7826485cab4c9568cdd3 ts=2026-09-28T14:22:30.7340000Z; 23h 52m: 6aa4140b41b41dbac0c7f230.jsonl[1058] _id=6ab52ebb485cab4c9551d4db ts=2026-09-24T14:07:55.6450000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1277] _id=6ab67e6a485cab4c9555b7c6 ts=2026-09-25T14:00:10.7780000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.015s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f230.jsonl[7371] _id=6ac518bbde269131f9b4c287 ts=2026-10-06T15:50:14.4290000Z -> 6aa4140b41b41dbac0c7f230.jsonl[7372] _id=6ac518cbde269131f9b4c2e5 ts=2026-10-06T15:50:14.429Z; 15ms: 6aa4140b41b41dbac0c7f230.jsonl[4896] _id=6abbc394485cab4c957e1353 ts=2026-09-29T13:56:33.1420000Z -> 6aa4140b41b41dbac0c7f230.jsonl[4867] _id=6abbc394485cab4c957e1363 ts=2026-09-29T13:56:33.1570000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 143h 38m 
  - Evidence: 143h 38m: 6aa4140b41b41dbac0c7f230.jsonl[5818] _id=6abbc7a1485cab4c957e6fb9 ts=2026-09-29T14:13:53.8840000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5917] _id=6ac3ab7fde269131f9a9fcde ts=2026-10-05T13:51:58.2330000Z; 71h 25m: 6aa4140b41b41dbac0c7f230.jsonl[2882] _id=6ab683d4485cab4c9556343a ts=2026-09-25T14:23:16.2610000Z -> 6aa4140b41b41dbac0c7f230.jsonl[3065] _id=6aba7045485cab4c95681dbf ts=2026-09-28T13:48:51.9050000Z; 23h 48m: 6aa4140b41b41dbac0c7f230.jsonl[1043] _id=6ab52e81485cab4c9551d1bb ts=2026-09-24T14:06:56.7620000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1101] _id=6ab67d37485cab4c9555a29e ts=2026-09-25T13:55:01.6590000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f230.jsonl[846] _id=6ab52c9a485cab4c9551ba73 ts=2026-09-24T13:58:50.4180000Z -> 6aa4140b41b41dbac0c7f230.jsonl[847] _id=6ab52c9a485cab4c9551ba77 ts=2026-09-24T13:58:50.4190000Z; 2ms: 6aa4140b41b41dbac0c7f230.jsonl[1161] _id=6ab67d7b485cab4c9555a5f0 ts=2026-09-25T13:56:10.9530000Z -> 6aa4140b41b41dbac0c7f230.jsonl[1096] _id=6ab67d7b485cab4c9555a5f2 ts=2026-09-25T13:56:10.9550000Z; 2ms: 6aa4140b41b41dbac0c7f230.jsonl[5917] _id=6ac3ab7fde269131f9a9fcde ts=2026-10-05T13:51:58.2330000Z -> 6aa4140b41b41dbac0c7f230.jsonl[5913] _id=6ac3ab7fde269131f9a9fce3 ts=2026-10-05T13:51:58.2350000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[978] _id=6ab52d3f485cab4c9551c4e7 ts=2026-09-24T14:01:35.7190000Z`; `6aa4140b41b41dbac0c7f230.jsonl[980] _id=6ab52d40485cab4c9551c4f1 ts=2026-09-24T14:01:35.8190000Z`; `6aa4140b41b41dbac0c7f230.jsonl[6529] _id=6ac3ad83de269131f9aa66a4 ts=2026-10-05T14:00:35.5210000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1348] _id=6ab67edc485cab4c9555be36 ts=2026-09-25T14:02:04.7980000Z`; `6aa4140b41b41dbac0c7f230.jsonl[3367] _id=6aba72bd485cab4c95686171 ts=2026-09-28T13:59:25.3170000Z`; `6aa4140b41b41dbac0c7f230.jsonl[4639] _id=6aba77ed485cab4c9568cab3 ts=2026-09-28T14:21:33.0020000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 44 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1846] _id=6ab681bb485cab4c9555f0dc ts=2026-09-25T14:14:19.1600000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1844] _id=6ab681bb485cab4c9555f0de ts=2026-09-25T14:14:19.1890000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1849] _id=6ab681bc485cab4c9555f11a ts=2026-09-25T14:14:19.3800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 249 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1554] _id=6ab68115485cab4c9555d910 ts=2026-09-25T14:11:32.0350000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1552] _id=6ab68115485cab4c9555d91c ts=2026-09-25T14:11:32.5790000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1569] _id=6ab68116485cab4c9555d922 ts=2026-09-25T14:11:32.5790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[8185] _id=6ac51d26de269131f9b4e27b ts=2026-10-06T16:09:10.2000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1197] _id=6ab67df7485cab4c9555b22f ts=2026-09-25T13:58:15.1680000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1276] _id=6ab67e7e485cab4c9555b8be ts=2026-09-25T14:00:30.4980000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1298] _id=6ab67e7e485cab4c9555b8c0 ts=2026-09-25T14:00:30.5170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[6492] _id=6ac3ad08de269131f9aa52dc ts=2026-10-05T13:58:32.8620000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 7 records 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[29] _id=6ab3da53485cab4c954ce37f ts=?`; `6aa4140b41b41dbac0c7f230.jsonl[568] _id=6ab527d8485cab4c95513b15 ts=?`; `6aa4140b41b41dbac0c7f230.jsonl[1039] _id=6ab52e81485cab4c9551d1af ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[3107] _id=6aba7073485cab4c956820d9 ts=2026-09-28T13:49:39.1170000Z`; `6aa4140b41b41dbac0c7f230.jsonl[3115] _id=6aba7077485cab4c95682127 ts=2026-09-28T13:49:43.5050000Z`; `6aa4140b41b41dbac0c7f230.jsonl[3333] _id=6aba723f485cab4c95685a6f ts=2026-09-28T13:57:19.0060000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 427 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1809] _id=6ab681b3485cab4c9555ef82 ts=2026-09-25T14:14:10.8760000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1872] _id=6ab681be485cab4c9555f190 ts=2026-09-25T14:14:21.7330000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1874] _id=6ab681bf485cab4c9555f19a ts=2026-09-25T14:14:22.1460000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 675 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1562] _id=6ab68115485cab4c9555d8fe ts=2026-09-25T14:11:31.9250000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1563] _id=6ab68115485cab4c9555d900 ts=2026-09-25T14:11:31.9250000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1564] _id=6ab68115485cab4c9555d902 ts=2026-09-25T14:11:31.9440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[3369] _id=6aba72bd485cab4c95686175 ts=2026-09-28T13:59:25.3320000Z`; `6aa4140b41b41dbac0c7f230.jsonl[3355] _id=6aba72bd485cab4c95686179 ts=2026-09-28T13:59:25.3400000Z`; `6aa4140b41b41dbac0c7f230.jsonl[6538] _id=6ac3ad83de269131f9aa66ac ts=2026-10-05T14:00:35.5230000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 42 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1192] _id=6ab67df6485cab4c9555b21a ts=2026-09-25T13:58:14.8670000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1184] _id=6ab67df9485cab4c9555b2b1 ts=2026-09-25T13:58:18.0970000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1182] _id=6ab67dfa485cab4c9555b2c8 ts=2026-09-25T13:58:18.6120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1307] _id=6ab67e97485cab4c9555ba08 ts=2026-09-25T14:00:55.7490000Z`; `6aa4140b41b41dbac0c7f230.jsonl[8064] _id=6ac51cacde269131f9b4de63 ts=2026-10-06T16:07:08.8930000Z`; `6aa4140b41b41dbac0c7f230.jsonl[8060] _id=6ac51cb3de269131f9b4de89 ts=2026-10-06T16:07:15.0180000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'DialogueStartEvent' (totals: 191 start, 185 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 110 unmatched 'BecameCameraCentered' (totals: 515 open, 449 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 103 unmatched 'BecameVisible' (totals: 899 open, 1045 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 15 open, 13 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationNodeHoverStart' (totals: 119 open, 120 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 9 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 30 start, 18 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 184 of 8424 adjacent _id pairs reverse in client time; worst 140.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f230.jsonl[1648] _id=6ab681a1485cab4c9555ebce ts=2026-09-25T14:13:53.8840000Z`; `6aa4140b41b41dbac0c7f230.jsonl[1650] _id=6ab681a2485cab4c9555ebf4 ts=2026-09-25T14:11:33.7370000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.09s, min -141.40s, max +0.13s over 8425 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f230\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 7 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `TerasGardenBox` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **NOT_TESTED / NotTested** `soilMachine` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 2908 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2908)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.04s, n=2907)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2908/2908 records)
    "BecameInvisible"  x1045
    "BecameVisible"  x899
    "BecameCameraCentered"  x515
    "BecameCameraUncentered"  x449
data.pieceId  (string, 2908/2908 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2908/2908 records)
    1862 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2166 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1157); Unit 3 Dev (576); Unit 1 Dev (433)
- **Intervals:** median 0.54s (p5 0.03s / p95 17.64s, n=2165)
- **Fields under `data`:**

```text
data.Value  (string, 2166/2166 records)
    "pressed"  x2166
data.actionType  (string, 2166/2166 records)
    "Move"  x1271
    "Jump"  x419
    "Interact"  x226
    "Hoverboard"  x114
    "Ascend"  x59
    "Pause"  x33
    "Sprint"  x31
    "SkipCinematic"  x8
    "Map"  x4
    "ToggleDebug"  x1
data.key  (string, 2166/2166 records, 18 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2166/2166 records)
    "Player"  x1662
    "Drone"  x504
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1443 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (805); Unit 1 Dev (419); Unit 3 Dev (219)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.30s, n=1440)
- **Fields under `data`:**

```text
data.position  (object, 1443/1443 records)
data.position.x  (number, 1443/1443 records)
    numeric range -641.33 .. 1680.82 (320 unique)
data.position.y  (number, 1443/1443 records)
    numeric range -115.127 .. 180.046 (259 unique)
data.position.z  (number, 1443/1443 records)
    numeric range -1238.27 .. 2265.87 (322 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1136 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (638); Unit 1 Dev (277); Unit 3 Dev (221)
- **eventKey:** present on 760 of 1136 records
- **Intervals:** median 3.78s (p5 0.00s / p95 47.68s, n=1135)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x760; [conversationId, dialogueEventType] x376
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1136/1136 records)
    numeric range 8 .. 101 (29 unique)
data.dialogueEventType  (string, 1136/1136 records)
    "DialogueNodeEvent"  x760
    "DialogueStartEvent"  x191
    "DialogueFinishEvent"  x185
data.nodeId  (number, 760/1136 records)
    numeric range 0 .. 290 (192 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 258 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (169); Unit 1 Dev (89)
- **Intervals:** median 0.33s (p5 0.03s / p95 11.15s, n=257)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 258/258 records)
    "argumentationNodeHoverEnd"  x120
    "argumentationNodeHoverStart"  x119
    "argumentationNodeAdd"  x12
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 258/258 records)
    "Unit 3 - Pollution Upstream"  x169
    "Unit 1 - Argumentation Tutorial"  x52
    "Unit 1 - Freshwater"  x37
data.nodeName  (string, 258/258 records)
    "1"  x60
    "A"  x52
    "3"  x39
    "I"  x37
    "2"  x21
    "II"  x20
    "B"  x16
    "5"  x7
    "4"  x6
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 140 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (73); Unit 1 Dev (66); Unit 3 Dev (1)
- **Intervals:** median 5.17s (p5 0.13s / p95 662.81s, n=139)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 140/140 records)
    13 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 140/140 records)
    40 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `DaniEvent` — 95 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (39); Unit 2 Prod (Refactor) (36); Unit 3 Dev (20)
- **Intervals:** median 1.87s (p5 0.00s / p95 978.05s, n=94)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 95/95 records)
    "Close"  x49
    "Open"  x46
data.toolName  (string, 95/95 records, 73 empty-string)
    ""  x73
    "Settings"  x22
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowFocusEvent` — 60 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 1 Dev (19); MainMenu (13); Unit 3 Dev (6)
- **Intervals:** median 107.57s (p5 1.32s / p95 84702.04s, n=59)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 60/60 records)
    true  x60
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 58 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 1 Dev (22); Unit 3 Dev (9); Transition (1)
- **Intervals:** median 90.01s (p5 0.83s / p95 84586.42s, n=57)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 58/58 records)
    false  x58
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `questEvent` — 48 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (22); Unit 2 Prod (Refactor) (19); Unit 3 Dev (7)
- **eventKey:** present on 48 of 48 records
- **Intervals:** median 233.38s (p5 0.00s / p95 85582.99s, n=47)
- **`data` key-set variants:** [questEventType, questID, questName] x30; [questEventType, questID, questName, questSuccessOrFailure] x18
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 48/48 records)
    "questActiveEvent"  x30
    "questFinishEvent"  x18
data.questID  (string, 48/48 records)
    14 unique values (see csv/event_unique_values.csv)
data.questName  (string, 48/48 records)
    14 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 18/48 records)
    "Succeeded"  x18
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 39 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (35); Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 3.50s (p5 0.04s / p95 117507.58s, n=38)
- **`data` key-set variants:** [actionType, featureUsed] x28; [actionType, featureUsed, legendName] x10; [actionType, featureUsed, location] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "MapOpenEvent"  x15
    "MapCloseEvent"  x13
    "Selected"  x8
    "Unselected"  x2
    "WaypointSetEvent"  x1
data.featureUsed  (string, 39/39 records)
    "Map"  x28
    "Legend"  x10
    "Waypoint"  x1
data.legendName  (string, 10/39 records)
    "360 ft"  x3
    "150 ft"  x2
    "30 ft"  x2
    "0 ft"  x1
    "240 ft"  x1
    "Water"  x1
data.location  (object, 1/39 records)
data.location.x  (number, 1/39 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 1/39 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 1/39 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 18 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (18)
- **Intervals:** median 1.40s (p5 0.45s / p95 51706.37s, n=17)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x14; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/18 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/18 records)
    "Unit 2 Prod (Refactor)"  x4
data.actionType  (string, 14/18 records)
    "RightDrag"  x9
    "LeftDrag"  x5
data.currentSoilType  (string, 14/18 records)
    "SAND"  x5
    "CLAYSAND"  x3
    "SANDGRAVEL"  x3
    "CLAY"  x1
    "CLAYROCK"  x1
    "GRAVEL"  x1
data.isCorrectSelection  (string, 14/18 records)
    "false"  x9
    "true"  x5
data.waterLevelStatus  (string, 14/18 records)
    "Proper"  x7
    "TooHigh"  x7
data.waterRetentionChange  (string, 14/18 records)
    "Increase"  x5
    "NoChange"  x5
    "Decrease"  x4
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 13 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 1 Dev (5); Unit 2 Prod (Refactor) (5); Unit 3 Dev (3)
- **Intervals:** median 45894.53s (p5 199.48s / p95 375094.15s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "DebugMenuStateChanged"  x13
data.isOpened  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 45886.90s (p5 196.31s / p95 375110.30s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (7); Unit 1 Dev (3)
- **Intervals:** median 10.70s (p5 1.18s / p95 574785.83s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x3
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationAnswerEvent` — 8 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (2)
- **Intervals:** median 34.59s (p5 5.63s / p95 670565.52s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "submitAnswerEvent"  x8
data.answerSubmitted  (string, 8/8 records, 1 empty-string)
    "B,2,I"  x2
    "B,2,II"  x2
    ""  x1
    "A,1,I"  x1
    "A,3,I"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 45.38s (p5 8.44s / p95 718417.90s, n=6)
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

### `crash` — 7 records

- **Scenes:** <missing sceneName> (7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 7/7 records)
    true  x7
data.message  (string, 7/7 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x3
data.phase  (string, 7/7 records)
    "running"  x7
data.stack  (string, 7/7 records, 4 empty-string)
    ""  x4
    "TypeError: Permissions check failed"  x3
data.type  (string, 7/7 records)
    "unhandled_rejection"  x7
data.unitId  (string, 7/7 records)
    "unit1"  x4
    "unit2"  x2
    "unit3"  x1
data.workspace  (string, 7/7 records)
    "mhs"  x7
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 1.06s (p5 0.99s / p95 3.41s, n=3)
- **`data` key-set variants:** [actionType, chatID] x3; [actionKey, chatID] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 1/4 records)
    "ScrollStop"  x1
data.actionType  (string, 3/4 records)
    "Close"  x1
    "Open"  x1
    "ScrollStart"  x1
data.chatID  (string, 4/4 records)
    "NA"  x2
    "[30-33, 30-37, 30-38, 30-40, 30-42]"  x1
    "[31-35, 31-38, 31-39, 31-41, 31-45]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "1"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `soilMachine` : event type present in baseline 09-23-26 but absent now
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DaniEvent` actionType: tool open/close: close without preceding open
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TopographicMapEvent` data.actionType: "Selected" (8x); "Unselected" (2x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Legend" (10x); "Waypoint" (1x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*