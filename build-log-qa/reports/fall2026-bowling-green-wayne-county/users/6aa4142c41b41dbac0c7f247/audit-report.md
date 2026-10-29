# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f247

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f247
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f247.jsonl
- **Records:** 12089 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f247
- **Time span:** 2026-09-22T16:50:39.069000+00:00 .. 2026-10-07T17:05:34.468000+00:00 (360h 14m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f247\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 12089 records, 8 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 90 INFO, 2 NOT_TESTED, 71 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4025 | 33.29 | 1 | 3 | 0 | 2026-09-25T16:43:00.678000+00:00 | 2026-10-06T16:58:27.327000+00:00 | 264h 15m |
| InputEvent | 3655 | 30.23 | 1 | 6 | 0 | 2026-09-23T16:33:02.560000+00:00 | 2026-10-07T17:05:34.282000+00:00 | 336h 32m |
| PlayerPositionEvent | 1891 | 15.64 | 1 | 6 | 0 | 2026-09-23T16:33:01.547000+00:00 | 2026-10-07T17:05:29.505000+00:00 | 336h 32m |
| DialogueEvent | 1662 | 13.75 | 1 | 6 | 1034 | 2026-09-23T16:33:19.228000+00:00 | 2026-10-07T17:05:34.438000+00:00 | 336h 32m |
| ObjectInterEvent | 307 | 2.54 | 1 | 6 | 0 | 2026-09-23T16:37:30.570000+00:00 | 2026-10-07T17:02:07.969000+00:00 | 336h 24m |
| argumentationNodeEvent | 188 | 1.56 | 1 | 2 | 0 | 2026-09-25T16:32:56.159000+00:00 | 2026-10-05T16:48:44.051000+00:00 | 240h 15m |
| TopographicMapEvent | 84 | 0.69 | 1 | 2 | 0 | 2026-09-25T16:43:34.551000+00:00 | 2026-10-06T16:42:18.267000+00:00 | 263h 58m |
| questEvent | 65 | 0.54 | 1 | 6 | 65 | 2026-09-23T16:33:19.207000+00:00 | 2026-10-07T17:05:34.296000+00:00 | 336h 32m |
| gameWindowFocusEvent | 50 | 0.41 | 1 | 6 | 0 | 2026-09-22T16:50:39.069000+00:00 | 2026-10-07T17:05:34.468000+00:00 | 360h 14m |
| gameWindowUnfocusEvent | 37 | 0.31 | 1 | 5 | 0 | 2026-09-22T16:50:56.017000+00:00 | 2026-10-07T17:05:34.464000+00:00 | 360h 14m |
| Soil Key Puzzle | 34 | 0.28 | 1 | 3 | 0 | 2026-09-28T16:56:14.778000+00:00 | 2026-10-06T16:56:16.711000+00:00 | 192h 0m |
| DEBUGMenu | 22 | 0.18 | 1 | 7 | 0 | 2026-09-23T16:24:30.316000+00:00 | 2026-10-07T17:05:29.500000+00:00 | 336h 40m |
| gameStartEvent | 19 | 0.16 | 1 | 1 | 0 | 2026-09-22T16:50:39.069000+00:00 | 2026-10-07T17:05:24.322000+00:00 | 360h 14m |
| argumentationAnswerEvent | 18 | 0.15 | 1 | 2 | 0 | 2026-09-25T16:33:52.485000+00:00 | 2026-10-05T16:48:45.513000+00:00 | 240h 14m |
| soilMachine | 14 | 0.12 | 1 | 1 | 0 | 2026-10-07T16:54:58.936000+00:00 | 2026-10-07T17:01:46.025000+00:00 | 6m 47s |
| argumentationEvent | 7 | 0.06 | 1 | 2 | 0 | 2026-09-25T16:33:32.043000+00:00 | 2026-10-05T16:48:45.562000+00:00 | 240h 15m |
| argumentationToolEvent | 5 | 0.04 | 1 | 2 | 0 | 2026-09-25T16:33:32.014000+00:00 | 2026-10-05T16:43:16.877000+00:00 | 240h 9m |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-25T16:37:40.200000+00:00 | 2026-10-06T16:49:28.953000+00:00 | 264h 11m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 951108.753s median 
  - Expected: 2855.05s in 09-23-26 
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
  - Observed: 20.117s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 31.177s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.426s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43179.045s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 368.892s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 482.974s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.42s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Press E; Press E To Place Cameras; Press E To Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister 
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
  - Observed: 120 ft; 330 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,2,I; A,2,II; B,1,II; B,2,II; B,3,II; B,4,II; B,5,II; B,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit; U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
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
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 128 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[150] _id=6ab400be485cab4c954e711a ts=2026-09-23T16:39:26.7130000Z`; `6aa4142c41b41dbac0c7f247.jsonl[211] _id=6ab401df485cab4c954e76f0 ts=2026-09-23T16:44:15.5520000Z`; `6aa4142c41b41dbac0c7f247.jsonl[228] _id=6ab40217485cab4c954e77d8 ts=2026-09-23T16:45:11.3510000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'questActiveEvent:32' vs expected 'questActiveEvent:34' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1280] _id=6aba9428485cab4c956a5822 ts=2026-09-25T16:31:52.037Z`; `6aa4142c41b41dbac0c7f247.jsonl[1287] _id=6aba9429485cab4c956a5900 ts=2026-09-25T16:32:05.889Z`; `6aa4142c41b41dbac0c7f247.jsonl[1284] _id=6aba942a485cab4c956a5921 ts=2026-09-25T16:32:05.894Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1] _id=6ab2b1de485cab4c954a5572 ts=2026-09-22T16:50:39.0690000Z`; `6aa4142c41b41dbac0c7f247.jsonl[4] _id=6ab3fd30485cab4c954e60c4 ts=2026-09-23T16:24:16.5190000Z`; `6aa4142c41b41dbac0c7f247.jsonl[12] _id=6ab3fd97485cab4c954e60d4 ts=2026-09-23T16:25:59.5390000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 50 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 50} 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[0] _id=6ab2b1de485cab4c954a5570 ts=2026-09-22T16:50:39.0690000Z`; `6aa4142c41b41dbac0c7f247.jsonl[8] _id=6ab3fd30485cab4c954e60c2 ts=2026-09-23T16:24:16.5180000Z`; `6aa4142c41b41dbac0c7f247.jsonl[6] _id=6ab3fd36485cab4c954e60c8 ts=2026-09-23T16:24:22.5070000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 37 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 37} 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[2] _id=6ab2b1ef485cab4c954a5574 ts=2026-09-22T16:50:56.0170000Z`; `6aa4142c41b41dbac0c7f247.jsonl[5] _id=6ab3fd36485cab4c954e60c6 ts=2026-09-23T16:24:22.5000000Z`; `6aa4142c41b41dbac0c7f247.jsonl[9] _id=6ab3fd38485cab4c954e60ca ts=2026-09-23T16:24:24.5770000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 18 of 84 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1568] _id=6aba9466485cab4c956a6c0c ts=2026-09-25T16:43:34.551Z`; `6aa4142c41b41dbac0c7f247.jsonl[1645] _id=6aba9469485cab4c956a6c44 ts=2026-09-25T16:43:57.949Z`; `6aa4142c41b41dbac0c7f247.jsonl[3715] _id=6aba9583485cab4c956a8c10 ts=2026-09-28T16:25:34.9640000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4024 | 0.0 | 0.033 | 236.413 | 1.126 | 519538.496 | 0.25 | 2299 | 7 |
| InputEvent | 3654 | 0.0 | 0.728 | 331.569 | 14.381 | 429360.968 | 0.18 | 159 | 11 |
| PlayerPositionEvent | 1884 | 9.441 | 10.0 | 642.956 | 10.046 | 429274.481 | 0.09 | 0 | 9 |
| DialogueEvent | 1661 | 0.001 | 4.79 | 729.401 | 36.636 | 430206.151 | 0.08 | 455 | 10 |
| ObjectInterEvent | 306 | 0.006 | 5.854 | 3957.769 | 385.954 | 430958.796 | 0.02 | 2 | 11 |
| argumentationNodeEvent | 187 | 0.003 | 0.376 | 4625.39 | 9.671 | 864363.558 | 0.01 | 47 | 1 |
| TopographicMapEvent | 83 | 0.03 | 2.281 | 11449.683 | 601.534 | 518346.117 | 0.01 | 2 | 5 |
| questEvent | 64 | 0.002 | 223.45 | 18930.236 | 85417.848 | 430378.907 | 0.0 | 12 | 12 |
| gameWindowFocusEvent | 49 | 1.153 | 368.892 | 26467.253 | 86201.864 | 429795.571 | 0.0 | 0 | 20 |
| gameWindowUnfocusEvent | 36 | 0.0 | 482.974 | 36024.401 | 128752.391 | 518433.727 | 0.0 | 1 | 16 |
| Soil Key Puzzle | 33 | 0.254 | 1.173 | 20945.513 | 34627.179 | 604587.556 | 0.0 | 0 | 2 |
| DEBUGMenu | 21 | 5.585 | 880.386 | 57717.104 | 258179.049 | 431037.188 | 0.0 | 0 | 12 |
| gameStartEvent | 18 | 82.07 | 43179.045 | 72049.181 | 284096.325 | 431030.874 | 0.0 | 0 | 11 |
| argumentationAnswerEvent | 17 | 0.175 | 20.117 | 50876.06 | 173026.674 | 864376.12 | 0.0 | 0 | 1 |
| soilMachine | 13 | 0.453 | 2.42 | 31.315 | 143.428 | 156.74 | 1.92 | 0 | 0 |
| argumentationEvent | 6 | 0.029 | 31.177 | 144152.253 | 648382.403 | 864348.162 | 0.0 | 1 | 1 |
| argumentationToolEvent | 4 | 1.466 | 2.426 | 216146.216 | 734892.157 | 864578.545 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 951108.753 | 951108.753 | 951108.753 | 951108.753 | 951108.753 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[12081] _id=6ac67bdede269131f9bd9260 ts=2026-10-07T17:05:34.2820000Z == 6aa4142c41b41dbac0c7f247.jsonl[12082] _id=6ac67bdede269131f9bd9261 ts=2026-10-07T17:05:34.2820000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 364 group(s), 616 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1678] _id=6aba9475485cab4c956a6d82 ts=2026-09-25T16:43:00.755Z == 6aa4142c41b41dbac0c7f247.jsonl[1735] _id=6aba9475485cab4c956a6d88 ts=2026-09-25T16:43:00.755Z`; `6aa4142c41b41dbac0c7f247.jsonl[1743] _id=6aba9475485cab4c956a6da7 ts=2026-09-25T16:43:00.841Z == 6aa4142c41b41dbac0c7f247.jsonl[1738] _id=6aba9476485cab4c956a6dad ts=2026-09-25T16:43:00.841Z`; `6aa4142c41b41dbac0c7f247.jsonl[1508] _id=6aba945d485cab4c956a6b33 ts=2026-09-25T16:43:14.319Z == 6aa4142c41b41dbac0c7f247.jsonl[1552] _id=6aba945e485cab4c956a6b35 ts=2026-09-25T16:43:14.319Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1386] _id=6aba9440485cab4c956a6850 ts=? == 6aa4142c41b41dbac0c7f247.jsonl[7233] _id=6abd38d9485cab4c958db37c ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 41 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f247.jsonl[99] _id=6ab4004a485cab4c954e6e9a ts=2026-09-23T16:37:30.5700000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[100] _id=6ab4004a485cab4c954e6e9c ts=2026-09-23T16:37:30.5760000Z`; `569ms: 6aa4142c41b41dbac0c7f247.jsonl[824] _id=6ab54dce485cab4c9552ee06 ts=2026-09-24T16:20:30.1250000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[825] _id=6ab54dce485cab4c9552ee1f ts=2026-09-24T16:20:30.6940000Z`; `354ms: 6aa4142c41b41dbac0c7f247.jsonl[745] _id=6ab54dcf485cab4c9552ee33 ts=2026-09-24T16:20:31.6950000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[747] _id=6ab54dd0485cab4c9552ee41 ts=2026-09-24T16:20:32.0490000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1908 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6aa4142c41b41dbac0c7f247.jsonl[1675] _id=6aba9474485cab4c956a6d74 ts=2026-09-25T16:43:00.678Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1676] _id=6aba9474485cab4c956a6d7a ts=2026-09-25T16:43:00.708Z`; `28ms: 6aa4142c41b41dbac0c7f247.jsonl[1676] _id=6aba9474485cab4c956a6d7a ts=2026-09-25T16:43:00.708Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1677] _id=6aba9475485cab4c956a6d7e ts=2026-09-25T16:43:00.736Z`; `19ms: 6aa4142c41b41dbac0c7f247.jsonl[1677] _id=6aba9475485cab4c956a6d7e ts=2026-09-25T16:43:00.736Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1678] _id=6aba9475485cab4c956a6d82 ts=2026-09-25T16:43:00.755Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `599ms: 6aa4142c41b41dbac0c7f247.jsonl[1636] _id=6aba9467485cab4c956a6c12 ts=2026-09-25T16:43:42.406Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1637] _id=6aba9467485cab4c956a6c16 ts=2026-09-25T16:43:43.005Z`; `506ms: 6aa4142c41b41dbac0c7f247.jsonl[1637] _id=6aba9467485cab4c956a6c16 ts=2026-09-25T16:43:43.005Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1646] _id=6aba9467485cab4c956a6c21 ts=2026-09-25T16:43:43.511Z`; `562ms: 6aa4142c41b41dbac0c7f247.jsonl[1646] _id=6aba9467485cab4c956a6c21 ts=2026-09-25T16:43:43.511Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1639] _id=6aba9467485cab4c956a6c25 ts=2026-09-25T16:43:44.073Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `472ms: 6aa4142c41b41dbac0c7f247.jsonl[1332] _id=6aba9431485cab4c956a5e6a ts=2026-09-25T16:34:36.589Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1336] _id=6aba9431485cab4c956a5e80 ts=2026-09-25T16:34:37.061Z`; `197ms: 6aa4142c41b41dbac0c7f247.jsonl[1336] _id=6aba9431485cab4c956a5e80 ts=2026-09-25T16:34:37.061Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1337] _id=6aba9432485cab4c956a5e9c ts=2026-09-25T16:34:37.258Z`; `175ms: 6aa4142c41b41dbac0c7f247.jsonl[1337] _id=6aba9432485cab4c956a5e9c ts=2026-09-25T16:34:37.258Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1335] _id=6aba9432485cab4c956a5eb8 ts=2026-09-25T16:34:37.433Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6aa4142c41b41dbac0c7f247.jsonl[9282] _id=6ac3d4edde269131f9ae18af ts=2026-10-05T16:48:45.5330000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[9327] _id=6ac3d4edde269131f9ae18b7 ts=2026-10-05T16:48:45.5620000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa4142c41b41dbac0c7f247.jsonl[1299] _id=6aba942c485cab4c956a5a86 ts=2026-09-25T16:32:56.159Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1300] _id=6aba942c485cab4c956a5aa3 ts=2026-09-25T16:32:56.187Z`; `215ms: 6aa4142c41b41dbac0c7f247.jsonl[1301] _id=6aba942d485cab4c956a5aba ts=2026-09-25T16:32:58.45Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1304] _id=6aba942d485cab4c956a5ad4 ts=2026-09-25T16:32:58.665Z`; `549ms: 6aa4142c41b41dbac0c7f247.jsonl[1304] _id=6aba942d485cab4c956a5ad4 ts=2026-09-25T16:32:58.665Z ~ 6aa4142c41b41dbac0c7f247.jsonl[1303] _id=6aba942d485cab4c956a5aef ts=2026-09-25T16:32:59.214Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4142c41b41dbac0c7f247.jsonl[12070] _id=6ac67bc3de269131f9bd91ad ts=2026-10-07T17:05:07.7350000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[12072] _id=6ac67bd3de269131f9bd91ef ts=2026-10-07T17:05:07.735Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4142c41b41dbac0c7f247.jsonl[5742] _id=6abbe72a485cab4c9580c16d ts=2026-09-29T16:28:25.8100000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[5743] _id=6abbe72a485cab4c9580c16f ts=2026-09-29T16:28:25.8120000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `711ms: 6aa4142c41b41dbac0c7f247.jsonl[11952] _id=6ac67ab7de269131f9bd782d ts=2026-10-07T17:00:39.9130000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[11948] _id=6ac67ab8de269131f9bd7848 ts=2026-10-07T17:00:40.6240000Z`; `453ms: 6aa4142c41b41dbac0c7f247.jsonl[11948] _id=6ac67ab8de269131f9bd7848 ts=2026-10-07T17:00:40.6240000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[11954] _id=6ac67ab9de269131f9bd785c ts=2026-10-07T17:00:41.0770000Z`; `558ms: 6aa4142c41b41dbac0c7f247.jsonl[11981] _id=6ac67adfde269131f9bd7d09 ts=2026-10-07T17:01:19.3940000Z ~ 6aa4142c41b41dbac0c7f247.jsonl[11985] _id=6ac67adfde269131f9bd7d1c ts=2026-10-07T17:01:19.9520000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6aa4142c41b41dbac0c7f247.jsonl[7274] _id=6abd3a98485cab4c958df8c6 ts=2026-09-30T16:36:40.8230000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8415] _id=6ac3ce56de269131f9ada367 ts=2026-10-05T16:20:38.0110000Z; 71h 42m: 6aa4142c41b41dbac0c7f247.jsonl[1465] _id=6aba944c485cab4c956a69bf ts=2026-09-25T16:39:17.843Z -> 6aa4142c41b41dbac0c7f247.jsonl[3706] _id=6aba9578485cab4c956a8abe ts=2026-09-28T16:22:16.8920000Z; 24h 14m: 6aa4142c41b41dbac0c7f247.jsonl[770] _id=6ab54cf9485cab4c9552e52b ts=2026-09-24T16:16:59.5440000Z -> 6aa4142c41b41dbac0c7f247.jsonl[1277] _id=6aba9427485cab4c956a57f9 ts=2026-09-25T16:31:50.851Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6aa4142c41b41dbac0c7f247.jsonl[8268] _id=6abd3fb1485cab4c958ed326 ts=2026-09-30T16:58:25.0460000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8574] _id=6ac3d02fde269131f9adb14d ts=2026-10-05T16:28:31.1970000Z; 71h 18m: 6aa4142c41b41dbac0c7f247.jsonl[3712] _id=6aba9577485cab4c956a8a8e ts=2026-09-25T17:04:09.755Z -> 6aa4142c41b41dbac0c7f247.jsonl[3747] _id=6aba957a485cab4c956a8b12 ts=2026-09-28T16:22:44.3880000Z; 23h 39m: 6aa4142c41b41dbac0c7f247.jsonl[11380] _id=6ac52a65de269131f9b61173 ts=2026-10-06T17:05:41.4380000Z -> 6aa4142c41b41dbac0c7f247.jsonl[11406] _id=6ac67711de269131f9bd0fbe ts=2026-10-07T16:45:04.9930000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 455 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f247.jsonl[4940] _id=6aba9742485cab4c956ab857 ts=2026-09-28T16:35:14.1420000Z -> 6aa4142c41b41dbac0c7f247.jsonl[4939] _id=6aba9742485cab4c956ab859 ts=2026-09-28T16:35:14.1430000Z; 1ms: 6aa4142c41b41dbac0c7f247.jsonl[9055] _id=6ac3d324de269131f9adeefd ts=2026-10-05T16:41:08.3530000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9056] _id=6ac3d324de269131f9adeeff ts=2026-10-05T16:41:08.3540000Z; 1ms: 6aa4142c41b41dbac0c7f247.jsonl[9058] _id=6ac3d32cde269131f9adefb7 ts=2026-10-05T16:41:16.3960000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9059] _id=6ac3d32cde269131f9adefb9 ts=2026-10-05T16:41:16.3970000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 264h 11m 
  - Evidence: 264h 11m: 6aa4142c41b41dbac0c7f247.jsonl[1463] _id=6aba944b485cab4c956a69b7 ts=2026-09-25T16:37:40.2Z -> 6aa4142c41b41dbac0c7f247.jsonl[10680] _id=6ac52699de269131f9b56183 ts=2026-10-06T16:49:28.9530000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6aa4142c41b41dbac0c7f247.jsonl[8363] _id=6abd413d485cab4c958ef455 ts=2026-09-30T17:05:01.1960000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8419] _id=6ac3ce6ede269131f9ada36f ts=2026-10-05T16:21:02.1640000Z; 71h 18m: 6aa4142c41b41dbac0c7f247.jsonl[3686] _id=6aba9573485cab4c956a8a2a ts=2026-09-25T17:04:02.428Z -> 6aa4142c41b41dbac0c7f247.jsonl[3723] _id=6aba9578485cab4c956a8aca ts=2026-09-28T16:22:23.4700000Z; 23h 39m: 6aa4142c41b41dbac0c7f247.jsonl[11379] _id=6ac52a63de269131f9b61145 ts=2026-10-06T17:05:39.5630000Z -> 6aa4142c41b41dbac0c7f247.jsonl[11395] _id=6ac67708de269131f9bd0e4f ts=2026-10-07T16:44:56.1200000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 159 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f247.jsonl[12079] _id=6ac67bdede269131f9bd925e ts=2026-10-07T17:05:34.2810000Z -> 6aa4142c41b41dbac0c7f247.jsonl[12080] _id=6ac67bdede269131f9bd925f ts=2026-10-07T17:05:34.2810000Z; 0ms: 6aa4142c41b41dbac0c7f247.jsonl[12081] _id=6ac67bdede269131f9bd9260 ts=2026-10-07T17:05:34.2820000Z -> 6aa4142c41b41dbac0c7f247.jsonl[12082] _id=6ac67bdede269131f9bd9261 ts=2026-10-07T17:05:34.2820000Z; 0ms: 6aa4142c41b41dbac0c7f247.jsonl[12082] _id=6ac67bdede269131f9bd9261 ts=2026-10-07T17:05:34.2820000Z -> 6aa4142c41b41dbac0c7f247.jsonl[12083] _id=6ac67bdede269131f9bd9262 ts=2026-10-07T17:05:34.2820000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6aa4142c41b41dbac0c7f247.jsonl[7550] _id=6abd3d3b485cab4c958e9ef4 ts=2026-09-30T16:47:55.3190000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8622] _id=6ac3d0aade269131f9adb969 ts=2026-10-05T16:30:34.1150000Z; 71h 20m: 6aa4142c41b41dbac0c7f247.jsonl[3661] _id=6aba9575485cab4c956a8a44 ts=2026-09-25T17:04:04.98Z -> 6aa4142c41b41dbac0c7f247.jsonl[3752] _id=6aba957d485cab4c956a8b6c ts=2026-09-28T16:24:20.7620000Z; 23h 47m: 6aa4142c41b41dbac0c7f247.jsonl[1236] _id=6ab5536b485cab4c955346c1 ts=2026-09-24T16:44:27.4020000Z -> 6aa4142c41b41dbac0c7f247.jsonl[1283] _id=6aba9429485cab4c956a58ab ts=2026-09-25T16:32:05.835Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 6aa4142c41b41dbac0c7f247.jsonl[926] _id=6ab54e5a485cab4c9552f5b3 ts=2026-09-24T16:22:50.8230000Z -> 6aa4142c41b41dbac0c7f247.jsonl[925] _id=6ab54e5a485cab4c9552f5b9 ts=2026-09-24T16:22:50.8290000Z; 6ms: 6aa4142c41b41dbac0c7f247.jsonl[99] _id=6ab4004a485cab4c954e6e9a ts=2026-09-23T16:37:30.5700000Z -> 6aa4142c41b41dbac0c7f247.jsonl[100] _id=6ab4004a485cab4c954e6e9c ts=2026-09-23T16:37:30.5760000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 14m 
  - Evidence: 119h 14m: 6aa4142c41b41dbac0c7f247.jsonl[8402] _id=6abd417b485cab4c958ef83c ts=2026-09-30T17:06:03.5390000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8417] _id=6ac3ce5bde269131f9ada369 ts=2026-10-05T16:20:38.0200000Z; 71h 18m: 6aa4142c41b41dbac0c7f247.jsonl[3713] _id=6aba9577485cab4c956a8aa4 ts=2026-09-25T17:04:13.322Z -> 6aa4142c41b41dbac0c7f247.jsonl[3722] _id=6aba9578485cab4c956a8ac6 ts=2026-09-28T16:22:16.9830000Z; 23h 38m: 6aa4142c41b41dbac0c7f247.jsonl[11386] _id=6ac52aa7de269131f9b61427 ts=2026-10-06T17:06:47.0890000Z -> 6aa4142c41b41dbac0c7f247.jsonl[11394] _id=6ac67708de269131f9bd0e4e ts=2026-10-07T16:44:50.6770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 144h 18m 
  - Evidence: 144h 18m: 6aa4142c41b41dbac0c7f247.jsonl[6381] _id=6abbe8c2485cab4c9580e299 ts=2026-09-29T16:35:13.6540000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9493] _id=6ac3d635de269131f9ae3569 ts=2026-10-05T16:54:12.1500000Z; 71h 21m: 6aa4142c41b41dbac0c7f247.jsonl[3714] _id=6aba9577485cab4c956a8a9c ts=2026-09-25T17:04:09.868Z -> 6aa4142c41b41dbac0c7f247.jsonl[3850] _id=6aba9588485cab4c956a8c9c ts=2026-09-28T16:25:12.1360000Z; 23h 28m: 6aa4142c41b41dbac0c7f247.jsonl[9761] _id=6ac3d69dde269131f9ae4251 ts=2026-10-05T16:55:56.7310000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9897] _id=6ac520b0de269131f9b4f61d ts=2026-10-06T16:24:15.7740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2299 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f247.jsonl[10004] _id=6ac520cbde269131f9b4f787 ts=2026-10-06T16:24:42.2700000Z -> 6aa4142c41b41dbac0c7f247.jsonl[10005] _id=6ac520cbde269131f9b4f789 ts=2026-10-06T16:24:42.2700000Z; 0ms: 6aa4142c41b41dbac0c7f247.jsonl[10005] _id=6ac520cbde269131f9b4f789 ts=2026-10-06T16:24:42.2700000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9910] _id=6ac520cbde269131f9b4f78b ts=2026-10-06T16:24:42.2700000Z; 0ms: 6aa4142c41b41dbac0c7f247.jsonl[10017] _id=6ac520cfde269131f9b4f7ed ts=2026-10-06T16:24:46.7380000Z -> 6aa4142c41b41dbac0c7f247.jsonl[10023] _id=6ac520cfde269131f9b4f7ef ts=2026-10-06T16:24:46.7380000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 56m 
  - Evidence: 167h 56m: 6aa4142c41b41dbac0c7f247.jsonl[5423] _id=6aba9c4d485cab4c956af7e7 ts=2026-09-28T16:56:45.1550000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9459] _id=6ac3d5f8de269131f9ae2eb9 ts=2026-10-05T16:53:12.7110000Z; 24h 2m: 6aa4142c41b41dbac0c7f247.jsonl[9458] _id=6ac3d60ade269131f9ae3047 ts=2026-10-05T16:53:30.2060000Z -> 6aa4142c41b41dbac0c7f247.jsonl[10778] _id=6ac52820de269131f9b5a251 ts=2026-10-06T16:56:00.5370000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6aa4142c41b41dbac0c7f247.jsonl[7358] _id=6abd3ba5485cab4c958e4487 ts=2026-09-30T16:41:09.8630000Z -> 6aa4142c41b41dbac0c7f247.jsonl[10497] _id=6ac52470de269131f9b523ed ts=2026-10-06T16:40:15.9800000Z; 71h 41m: 6aa4142c41b41dbac0c7f247.jsonl[1645] _id=6aba9469485cab4c956a6c44 ts=2026-09-25T16:43:57.949Z -> 6aa4142c41b41dbac0c7f247.jsonl[3715] _id=6aba9583485cab4c956a8c10 ts=2026-09-28T16:25:34.9640000Z; 23h 55m: 6aa4142c41b41dbac0c7f247.jsonl[5307] _id=6aba9ad7485cab4c956ad364 ts=2026-09-28T16:50:31.4770000Z -> 6aa4142c41b41dbac0c7f247.jsonl[6593] _id=6abbeb45485cab4c95815de8 ts=2026-09-29T16:45:57.7710000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.030s..0.033s shown 
  - Evidence: 30ms: 6aa4142c41b41dbac0c7f247.jsonl[4970] _id=6aba9795485cab4c956aba45 ts=2026-09-28T16:36:37.1790000Z -> 6aa4142c41b41dbac0c7f247.jsonl[4967] _id=6aba9795485cab4c956aba47 ts=2026-09-28T16:36:37.2090000Z; 33ms: 6aa4142c41b41dbac0c7f247.jsonl[4967] _id=6aba9795485cab4c956aba47 ts=2026-09-28T16:36:37.2090000Z -> 6aa4142c41b41dbac0c7f247.jsonl[4965] _id=6aba9795485cab4c956aba53 ts=2026-09-28T16:36:37.2420000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 240h 6m 
  - Evidence: 240h 6m: 6aa4142c41b41dbac0c7f247.jsonl[1348] _id=6aba9433485cab4c956a601f ts=2026-09-25T16:34:52.221Z -> 6aa4142c41b41dbac0c7f247.jsonl[9053] _id=6ac3d324de269131f9adeef9 ts=2026-10-05T16:41:08.3410000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 240h 5m 
  - Evidence: 240h 5m: 6aa4142c41b41dbac0c7f247.jsonl[1351] _id=6aba9433485cab4c956a603a ts=2026-09-25T16:34:52.245Z -> 6aa4142c41b41dbac0c7f247.jsonl[9021] _id=6ac3d308de269131f9adecf5 ts=2026-10-05T16:40:40.4070000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.029s..0.029s shown 
  - Evidence: 29ms: 6aa4142c41b41dbac0c7f247.jsonl[9282] _id=6ac3d4edde269131f9ae18af ts=2026-10-05T16:48:45.5330000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9327] _id=6ac3d4edde269131f9ae18b7 ts=2026-10-05T16:48:45.5620000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 240h 6m 
  - Evidence: 240h 6m: 6aa4142c41b41dbac0c7f247.jsonl[1347] _id=6aba9433485cab4c956a5ff8 ts=2026-09-25T16:34:46.801Z -> 6aa4142c41b41dbac0c7f247.jsonl[9029] _id=6ac3d312de269131f9adedbd ts=2026-10-05T16:40:50.3590000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 47 interval(s) ≤ 0.003s..0.019s shown 
  - Evidence: 3ms: 6aa4142c41b41dbac0c7f247.jsonl[9043] _id=6ac3d31cde269131f9adee83 ts=2026-10-05T16:41:00.4320000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9044] _id=6ac3d31cde269131f9adee85 ts=2026-10-05T16:41:00.4350000Z; 17ms: 6aa4142c41b41dbac0c7f247.jsonl[9134] _id=6ac3d3a8de269131f9adf7ad ts=2026-10-05T16:43:20.0170000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9146] _id=6ac3d3a8de269131f9adf7b3 ts=2026-10-05T16:43:20.0340000Z; 19ms: 6aa4142c41b41dbac0c7f247.jsonl[9062] _id=6ac3d32bde269131f9adefa0 ts=2026-10-05T16:41:15.6400000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9057] _id=6ac3d32bde269131f9adefa5 ts=2026-10-05T16:41:15.6590000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 240h 9m 
  - Evidence: 240h 9m: 6aa4142c41b41dbac0c7f247.jsonl[1316] _id=6aba942f485cab4c956a5c53 ts=2026-09-25T16:33:33.48Z -> 6aa4142c41b41dbac0c7f247.jsonl[9128] _id=6ac3d3a0de269131f9adf70b ts=2026-10-05T16:43:12.0250000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6aa4142c41b41dbac0c7f247.jsonl[7277] _id=6abd3a90485cab4c958df602 ts=2026-09-30T16:36:31.8670000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8414] _id=6ac3ce47de269131f9ada365 ts=2026-10-05T16:20:22.7410000Z; 71h 42m: 6aa4142c41b41dbac0c7f247.jsonl[1464] _id=6aba944c485cab4c956a69bd ts=2026-09-25T16:39:08.372Z -> 6aa4142c41b41dbac0c7f247.jsonl[3721] _id=6aba9578485cab4c956a8ab4 ts=2026-09-28T16:21:55.0710000Z; 24h 12m: 6aa4142c41b41dbac0c7f247.jsonl[767] _id=6ab54cea485cab4c9552e4b5 ts=2026-09-24T16:16:43.1630000Z -> 6aa4142c41b41dbac0c7f247.jsonl[1274] _id=6aba9427485cab4c956a578a ts=2026-09-25T16:29:05.584Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6aa4142c41b41dbac0c7f247.jsonl[8187] _id=6abd3f63485cab4c958ecf20 ts=2026-09-30T16:57:07.1680000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8429] _id=6ac3ce46de269131f9ada363 ts=2026-10-05T16:20:22.7390000Z; 71h 19m: 6aa4142c41b41dbac0c7f247.jsonl[3310] _id=6aba954a485cab4c956a85cd ts=2026-09-25T17:02:02.011Z -> 6aa4142c41b41dbac0c7f247.jsonl[3720] _id=6aba9578485cab4c956a8aae ts=2026-09-28T16:21:54.9730000Z; 23h 57m: 6aa4142c41b41dbac0c7f247.jsonl[8523] _id=6ac3cfa6de269131f9ada78f ts=2026-10-05T16:26:14.0690000Z -> 6aa4142c41b41dbac0c7f247.jsonl[9901] _id=6ac520a2de269131f9b4f5b9 ts=2026-10-06T16:24:02.1610000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6aa4142c41b41dbac0c7f247.jsonl[8403] _id=6abd4180485cab4c958ef869 ts=2026-09-30T17:06:08.8580000Z -> 6aa4142c41b41dbac0c7f247.jsonl[11388] _id=6ac52aa2de269131f9b6140d ts=2026-10-06T17:06:42.5850000Z; 71h 50m: 6aa4142c41b41dbac0c7f247.jsonl[3323] _id=6aba954a485cab4c956a85cb ts=2026-09-25T17:02:01.866Z -> 6aa4142c41b41dbac0c7f247.jsonl[5350] _id=6aba9b68485cab4c956adbd1 ts=2026-09-28T16:52:56.5920000Z; 23h 44m: 6aa4142c41b41dbac0c7f247.jsonl[11388] _id=6ac52aa2de269131f9b6140d ts=2026-10-06T17:06:42.5850000Z -> 6aa4142c41b41dbac0c7f247.jsonl[11590] _id=6ac6786ede269131f9bd3d39 ts=2026-10-07T16:50:54.1980000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f247.jsonl[12070] _id=6ac67bc3de269131f9bd91ad ts=2026-10-07T17:05:07.7350000Z -> 6aa4142c41b41dbac0c7f247.jsonl[12072] _id=6ac67bd3de269131f9bd91ef ts=2026-10-07T17:05:07.735Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6aa4142c41b41dbac0c7f247.jsonl[7528] _id=6abd3d2f485cab4c958e9d8c ts=2026-09-30T16:47:43.6910000Z -> 6aa4142c41b41dbac0c7f247.jsonl[8430] _id=6ac3ce5bde269131f9ada36b ts=2026-10-05T16:20:42.5980000Z; 71h 41m: 6aa4142c41b41dbac0c7f247.jsonl[1485] _id=6aba9450485cab4c956a6a1e ts=2026-09-25T16:40:52.537Z -> 6aa4142c41b41dbac0c7f247.jsonl[3729] _id=6aba9579485cab4c956a8ae8 ts=2026-09-28T16:22:24.0790000Z; 23h 47m: 6aa4142c41b41dbac0c7f247.jsonl[1238] _id=6ab5536b485cab4c955346c9 ts=2026-09-24T16:44:27.4250000Z -> 6aa4142c41b41dbac0c7f247.jsonl[1280] _id=6aba9428485cab4c956a5822 ts=2026-09-25T16:31:52.037Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f247.jsonl[1215] _id=6ab5536b485cab4c955346c7 ts=2026-09-24T16:44:27.4230000Z -> 6aa4142c41b41dbac0c7f247.jsonl[1238] _id=6ab5536b485cab4c955346c9 ts=2026-09-24T16:44:27.4250000Z; 2ms: 6aa4142c41b41dbac0c7f247.jsonl[5742] _id=6abbe72a485cab4c9580c16d ts=2026-09-29T16:28:25.8100000Z -> 6aa4142c41b41dbac0c7f247.jsonl[5743] _id=6abbe72a485cab4c9580c16f ts=2026-09-29T16:28:25.8120000Z; 4ms: 6aa4142c41b41dbac0c7f247.jsonl[11371] _id=6ac52a59de269131f9b61083 ts=2026-10-06T17:05:29.7850000Z -> 6aa4142c41b41dbac0c7f247.jsonl[11369] _id=6ac52a59de269131f9b61089 ts=2026-10-06T17:05:29.7890000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[5076] _id=6aba98e9485cab4c956ac4a5 ts=2026-09-28T16:42:17.4590000Z`; `6aa4142c41b41dbac0c7f247.jsonl[6376] _id=6abbe8b4485cab4c9580e129 ts=2026-09-29T16:35:00.3520000Z`; `6aa4142c41b41dbac0c7f247.jsonl[6497] _id=6abbea3d485cab4c95810196 ts=2026-09-29T16:41:32.9660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 402 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[3923] _id=6aba958e485cab4c956a8d4a ts=2026-09-28T16:26:39.1550000Z`; `6aa4142c41b41dbac0c7f247.jsonl[3942] _id=6aba9590485cab4c956a8d7a ts=2026-09-28T16:26:47.0990000Z`; `6aa4142c41b41dbac0c7f247.jsonl[3934] _id=6aba9590485cab4c956a8d7c ts=2026-09-28T16:26:47.3990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 1943 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1675] _id=6aba9474485cab4c956a6d74 ts=2026-09-25T16:43:00.678Z`; `6aa4142c41b41dbac0c7f247.jsonl[1676] _id=6aba9474485cab4c956a6d7a ts=2026-09-25T16:43:00.708Z`; `6aa4142c41b41dbac0c7f247.jsonl[1677] _id=6aba9475485cab4c956a6d7e ts=2026-09-25T16:43:00.736Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1568] _id=6aba9466485cab4c956a6c0c ts=2026-09-25T16:43:34.551Z`; `6aa4142c41b41dbac0c7f247.jsonl[1645] _id=6aba9469485cab4c956a6c44 ts=2026-09-25T16:43:57.949Z`; `6aa4142c41b41dbac0c7f247.jsonl[3715] _id=6aba9583485cab4c956a8c10 ts=2026-09-28T16:25:34.9640000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1315] _id=6aba942e485cab4c956a5c19 ts=2026-09-25T16:33:32.043Z`; `6aa4142c41b41dbac0c7f247.jsonl[1325] _id=6aba9430485cab4c956a5d57 ts=2026-09-25T16:33:55.158Z`; `6aa4142c41b41dbac0c7f247.jsonl[1329] _id=6aba9431485cab4c956a5e2e ts=2026-09-25T16:34:34.397Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 15 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1299] _id=6aba942c485cab4c956a5a86 ts=2026-09-25T16:32:56.159Z`; `6aa4142c41b41dbac0c7f247.jsonl[1300] _id=6aba942c485cab4c956a5aa3 ts=2026-09-25T16:32:56.187Z`; `6aa4142c41b41dbac0c7f247.jsonl[1301] _id=6aba942d485cab4c956a5aba ts=2026-09-25T16:32:58.45Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1311] _id=6aba942e485cab4c956a5bda ts=2026-09-25T16:33:32.014Z`; `6aa4142c41b41dbac0c7f247.jsonl[1316] _id=6aba942f485cab4c956a5c53 ts=2026-09-25T16:33:33.48Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[137] _id=6ab4008f485cab4c954e7034 ts=2026-09-23T16:38:39.3680000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1243] _id=6ab6a3bb485cab4c955b5034 ts=?`; `6aa4142c41b41dbac0c7f247.jsonl[1386] _id=6aba9440485cab4c956a6850 ts=?`; `6aa4142c41b41dbac0c7f247.jsonl[7233] _id=6abd38d9485cab4c958db37c ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 364 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[3891] _id=6aba958a485cab4c956a8cca ts=2026-09-28T16:25:13.5400000Z`; `6aa4142c41b41dbac0c7f247.jsonl[3881] _id=6aba958a485cab4c956a8ccc ts=2026-09-28T16:25:13.5400000Z`; `6aa4142c41b41dbac0c7f247.jsonl[3892] _id=6aba958a485cab4c956a8cce ts=2026-09-28T16:25:13.5540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 256 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[3886] _id=6aba958b485cab4c956a8ce4 ts=2026-09-28T16:25:13.6870000Z`; `6aa4142c41b41dbac0c7f247.jsonl[3895] _id=6aba958b485cab4c956a8ce6 ts=2026-09-28T16:25:13.6870000Z`; `6aa4142c41b41dbac0c7f247.jsonl[3887] _id=6aba958b485cab4c956a8cea ts=2026-09-28T16:25:13.6870000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 21 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[4967] _id=6aba9795485cab4c956aba47 ts=2026-09-28T16:36:37.2090000Z`; `6aa4142c41b41dbac0c7f247.jsonl[4965] _id=6aba9795485cab4c956aba53 ts=2026-09-28T16:36:37.2420000Z`; `6aa4142c41b41dbac0c7f247.jsonl[5028] _id=6aba984b485cab4c956ac04d ts=2026-09-28T16:39:39.2940000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[9043] _id=6ac3d31cde269131f9adee83 ts=2026-10-05T16:41:00.4320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[9137] _id=6ac3d3a4de269131f9adf770 ts=2026-10-05T16:43:16.8770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 318 start, 310 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 112 unmatched 'BecameCameraCentered' (totals: 522 open, 812 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 54 unmatched 'BecameVisible' (totals: 401 open, 2290 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 22 open, 24 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 3 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 41 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 345 of 12084 adjacent _id pairs reverse in client time; worst 123.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f247.jsonl[1726] _id=6aba9474485cab4c956a6d67 ts=2026-09-25T16:45:04.122Z`; `6aa4142c41b41dbac0c7f247.jsonl[1675] _id=6aba9474485cab4c956a6d74 ts=2026-09-25T16:43:00.678Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.11s, min -344238.28s, max +2.25s over 12085 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f247\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
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

### `PuzzlePieceVisibleEvent` — 4025 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3295); Unit 3 Dungeon Dev (366); Unit 4 Dev (364)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.13s, n=4024)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4025/4025 records)
    "BecameInvisible"  x2290
    "BecameCameraUncentered"  x812
    "BecameCameraCentered"  x522
    "BecameVisible"  x401
data.pieceId  (string, 4025/4025 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4025/4025 records)
    1094 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3655 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1302); Unit 2 Prod (Refactor) (1050); Unit 1 Dev (594); Unit 4 Dev - Dungeon (423); Unit 3 Dungeon Dev (234); Unit 4 Dev (52)
- **Intervals:** median 0.73s (p5 0.06s / p95 14.38s, n=3654)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3655/3655 records)
    "pressed"  x3655
data.actionType  (string, 3655/3655 records)
    "Move"  x2535
    "Jump"  x503
    "Interact"  x443
    "Ascend"  x87
    "Map"  x24
    "Sprint"  x23
    "Descend"  x21
    "Hoverboard"  x17
    "Pause"  x1
    "SkipCinematic"  x1
data.key  (string, 3655/3655 records, 1 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3655/3655 records)
    "Player"  x2325
    "Drone"  x1330
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1891 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (680); Unit 3 Dev (437); Unit 1 Dev (398); Unit 4 Dev - Dungeon (171); Unit 3 Dungeon Dev (155); Unit 4 Dev (50)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.05s, n=1884)
- **Fields under `data`:**

```text
data.position  (object, 1891/1891 records)
data.position.x  (number, 1891/1891 records)
    numeric range -684.355 .. 1422.92 (490 unique)
data.position.y  (number, 1891/1891 records)
    numeric range -115.1 .. 177.621 (417 unique)
data.position.z  (number, 1891/1891 records)
    numeric range -1131.63 .. 1933.73 (489 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1662 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (572); Unit 3 Dev (443); Unit 1 Dev (292); Unit 3 Dungeon Dev (168); Unit 4 Dev - Dungeon (150); Unit 4 Dev (37)
- **eventKey:** present on 1034 of 1662 records
- **Intervals:** median 4.79s (p5 0.01s / p95 36.64s, n=1661)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1034; [conversationId, dialogueEventType] x628
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1662/1662 records)
    numeric range 8 .. 111 (35 unique)
data.dialogueEventType  (string, 1662/1662 records)
    "DialogueNodeEvent"  x1034
    "DialogueStartEvent"  x318
    "DialogueFinishEvent"  x310
data.nodeId  (number, 1034/1662 records)
    numeric range 0 .. 290 (217 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 307 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (105); Unit 4 Dev - Dungeon (90); Unit 1 Dev (52); Unit 3 Dungeon Dev (40); Unit 3 Dev (12); Unit 4 Dev (8)
- **Intervals:** median 5.85s (p5 0.22s / p95 385.95s, n=306)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 307/307 records)
    28 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 307/307 records)
    71 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 188 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (173); Unit 1 Dev (15)
- **Intervals:** median 0.38s (p5 0.02s / p95 9.67s, n=187)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 188/188 records)
    "argumentationNodeHoverEnd"  x91
    "argumentationNodeHoverStart"  x76
    "argumentationNodeAdd"  x12
    "argumentationNodeRemove"  x9
data.argumentationTitle  (string, 188/188 records)
    "Unit 3 - Pollution Upstream"  x173
    "Unit 1 - Freshwater"  x15
data.nodeName  (string, 188/188 records)
    "II"  x30
    "1"  x26
    "3"  x24
    "A"  x24
    "B"  x24
    "2"  x18
    "4"  x16
    "I"  x15
    "5"  x11
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 84 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (67); Unit 3 Dev (17)
- **Intervals:** median 2.28s (p5 0.55s / p95 601.53s, n=83)
- **`data` key-set variants:** [actionType, featureUsed] x46; [actionType, featureUsed, location] x20; [actionType, featureUsed, legendName] x18
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 84/84 records)
    "MapCloseEvent"  x24
    "MapOpenEvent"  x22
    "Selected"  x18
    "WaypointMoveEvent"  x16
    "WaypointSetEvent"  x4
data.featureUsed  (string, 84/84 records)
    "Map"  x46
    "Waypoint"  x20
    "Legend"  x18
data.legendName  (string, 18/84 records)
    "120 ft"  x10
    "330 ft"  x7
    "0 ft"  x1
data.location  (object, 20/84 records)
data.location.x  (number, 20/84 records)
    numeric range -245.09 .. 222.44 (18 unique)
data.location.y  (number, 20/84 records)
    numeric range -279.5 .. 147.417 (20 unique)
data.location.z  (number, 20/84 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 65 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (21); Unit 2 Prod (Refactor) (14); Unit 3 Dev (13); Unit 4 Dev - Dungeon (13); Unit 3 Dungeon Dev (3); Unit 4 Dev (1)
- **eventKey:** present on 65 of 65 records
- **Intervals:** median 223.45s (p5 0.01s / p95 85417.85s, n=64)
- **`data` key-set variants:** [questEventType, questID, questName] x41; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 65/65 records)
    "questActiveEvent"  x41
    "questFinishEvent"  x24
data.questID  (string, 65/65 records)
    22 unique values (see csv/event_unique_values.csv)
data.questName  (string, 65/65 records)
    22 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/65 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 50 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 1 Dev (13); Unit 2 Prod (Refactor) (11); Unit 4 Dev - Dungeon (4); Transition (2); Unit 3 Dev (1)
- **Intervals:** median 368.89s (p5 5.07s / p95 86201.86s, n=49)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 50/50 records)
    true  x50
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 37 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (14); Unit 2 Prod (Refactor) (12); Unit 4 Dev - Dungeon (6); Transition (3); Unit 3 Dev (2)
- **Intervals:** median 482.97s (p5 1.32s / p95 128752.39s, n=36)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 37/37 records)
    false  x37
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `Soil Key Puzzle` — 34 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 4 Dev (12); Unit 3 Dev (10)
- **Intervals:** median 1.17s (p5 0.28s / p95 34627.18s, n=33)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x28; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/34 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/34 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 28/34 records)
    "RightDrag"  x17
    "LeftDrag"  x11
data.currentSoilType  (string, 28/34 records)
    "SAND"  x7
    "CLAYSAND"  x6
    "CLAY"  x5
    "CLAYROCK"  x4
    "SANDGRAVEL"  x4
    "BEDROCK"  x1
    "GRAVEL"  x1
data.isCorrectSelection  (string, 28/34 records)
    "false"  x20
    "true"  x8
data.waterLevelStatus  (string, 28/34 records)
    "TooHigh"  x14
    "Proper"  x9
    "TooLow"  x5
data.waterRetentionChange  (string, 28/34 records)
    "Decrease"  x11
    "Increase"  x9
    "NoChange"  x8
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 22 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 1 Dev (5); Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 4 Dev - Dungeon (3); MainMenu (2); Unit 3 Dungeon Dev (2); Unit 4 Dev (1)
- **Intervals:** median 880.39s (p5 5.83s / p95 258179.05s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "DebugMenuStateChanged"  x22
data.isOpened  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 43179.04s (p5 99.88s / p95 284096.33s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (7)
- **Intervals:** median 20.12s (p5 0.19s / p95 173026.67s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    "A,1,I"  x8
    "1,"  x1
    "A,2,I"  x1
    "A,2,II"  x1
    "A,5,I"  x1
    "B,1,II"  x1
    "B,2,II"  x1
    "B,3,II"  x1
    "B,4,II"  x1
    "B,5,II"  x1
    "B,A,2,II"  x1
data.argumentationTitle  (string, 18/18 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x7
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 14 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (14)
- **Intervals:** median 2.42s (p5 0.52s / p95 143.43s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "ChangeCanister"  x14
data.canisterType  (string, 14/14 records)
    "Clay"  x7
    "Bedrock"  x5
    "Gravel"  x1
    "Sand"  x1
data.floor  (string, 14/14 records)
    "5"  x12
    "3"  x1
    "4"  x1
data.machine  (string, 14/14 records)
    "1"  x14
data.row  (string, 14/14 records)
    "TopRow"  x8
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 31.18s (p5 4.48s / p95 648382.40s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x1
data.argumentationDescription  (string, 7/7 records)
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (3); Unit 1 Dev (2)
- **Intervals:** median 2.43s (p5 1.58s / p95 734892.16s, n=4)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 5/5 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x2
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x2
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x3
    "unit4"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 951108.75s (p5 951108.75s / p95 951108.75s, n=1)
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
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TopographicMapEvent` data.actionType: "Selected" (18x); "WaypointMoveEvent" (16x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (18x); "Waypoint" (20x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (9x)
- `soilMachine` data.canisterType: "Bedrock" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*