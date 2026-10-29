# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7e
- **Game version string(s) in log:** 2.8.9, 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b7e.jsonl
- **Records:** 8677 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b7e
- **Time span:** 2026-10-06T18:31:37.362000+00:00 .. 2026-10-19T04:45:57.281000+00:00 (298h 14m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 8677 records, 7 scenes.
- Findings: **0 FAIL**, **29 WARNING**, 92 INFO, 2 NOT_TESTED, 73 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3058 | 35.24 | 1 | 5 | 0 | 2026-10-06T18:32:12.272000+00:00 | 2026-10-19T04:43:31.738000+00:00 | 298h 11m |
| PuzzlePieceVisibleEvent | 1792 | 20.65 | 1 | 2 | 0 | 2026-10-07T18:49:39.572000+00:00 | 2026-10-15T18:58:59.008000+00:00 | 192h 9m |
| DialogueEvent | 1564 | 18.02 | 1 | 5 | 994 | 2026-10-06T18:32:11.201000+00:00 | 2026-10-19T04:43:32.046000+00:00 | 298h 11m |
| PlayerPositionEvent | 1486 | 17.13 | 1 | 5 | 0 | 2026-10-06T18:31:51.364000+00:00 | 2026-10-19T04:45:57.281000+00:00 | 298h 14m |
| argumentationNodeEvent | 218 | 2.51 | 1 | 3 | 0 | 2026-10-06T19:00:44.365000+00:00 | 2026-10-15T18:50:03.457000+00:00 | 215h 49m |
| ObjectInterEvent | 147 | 1.69 | 1 | 4 | 0 | 2026-10-06T18:36:52.994000+00:00 | 2026-10-19T04:42:30.537000+00:00 | 298h 5m |
| Soil Key Puzzle | 126 | 1.45 | 1 | 2 | 0 | 2026-10-07T18:54:32.429000+00:00 | 2026-10-15T18:54:07.140000+00:00 | 191h 59m |
| TopographicMapEvent | 67 | 0.77 | 1 | 3 | 0 | 2026-10-06T18:57:29.566000+00:00 | 2026-10-15T19:13:47.305000+00:00 | 216h 16m |
| questEvent | 50 | 0.58 | 1 | 4 | 50 | 2026-10-06T18:32:11.174000+00:00 | 2026-10-19T04:42:37.848000+00:00 | 298h 10m |
| gameWindowFocusEvent | 35 | 0.4 | 1 | 6 | 0 | 2026-10-06T18:31:37.362000+00:00 | 2026-10-19T04:43:00.547000+00:00 | 298h 11m |
| DEBUGMenu | 30 | 0.35 | 1 | 6 | 0 | 2026-10-06T18:31:51.350000+00:00 | 2026-10-19T04:43:15.144000+00:00 | 298h 11m |
| gameWindowUnfocusEvent | 27 | 0.31 | 1 | 4 | 0 | 2026-10-06T18:43:27.350000+00:00 | 2026-10-15T19:17:14.124000+00:00 | 216h 33m |
| argumentationToolEvent | 25 | 0.29 | 1 | 3 | 0 | 2026-10-06T19:01:11.619000+00:00 | 2026-10-15T18:48:41.516000+00:00 | 215h 47m |
| argumentationAnswerEvent | 18 | 0.21 | 1 | 3 | 0 | 2026-10-06T19:01:26.865000+00:00 | 2026-10-15T18:50:07.246000+00:00 | 215h 48m |
| gameStartEvent | 15 | 0.17 | 1 | 1 | 0 | 2026-10-06T18:31:37.364000+00:00 | 2026-10-19T04:43:00.548000+00:00 | 298h 11m |
| argumentationEvent | 9 | 0.1 | 1 | 3 | 0 | 2026-10-06T19:01:12.214000+00:00 | 2026-10-15T18:50:07.302000+00:00 | 215h 48m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-06T19:12:48.288000+00:00 | 2026-10-19T04:42:46.638000+00:00 | 297h 29m |
| crash | 3 | 0.03 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T18:58:20.885000+00:00 | 2026-10-06T18:58:22.761000+00:00 | 1.9s |
| chatEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T18:58:23.040000+00:00 | 2026-10-06T18:58:26.784000+00:00 | 3.7s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 535499.175s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.057s median 
  - Expected: 0.018s in 09-23-26 
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
  - Observed: 27.837s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 153.115s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.45s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3.744s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8010.203s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 603.497s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 381.034s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.3x vs baseline. 
  - Observed: 126 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Anderson's Room; Commons; Jasper's Room; PodBay; Teleporter Room; Tera's Room; Toppo's Room 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,3,I; A,4,I; A,I; B,2,I; C,1,I; C,A,1,I; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [32-88, 32-91, 32-95, 32-96, 30-98] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 10 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[173] _id=6ac54066de269131f9b6acb7 ts=2026-10-06T18:39:34.3570000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[287] _id=6ac541c8de269131f9b6d3fd ts=2026-10-06T18:45:28.4920000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[332] _id=6ac5426bde269131f9b6ea87 ts=2026-10-06T18:48:10.6040000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[6] _id=6ac53e89de269131f9b676ab ts=2026-10-06T18:31:37.3640000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1012] _id=6ac5488ade269131f9b77f0f ts=2026-10-06T19:14:18.3790000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1091] _id=6ac693b1de269131f9be0d50 ts=2026-10-07T18:47:11.6060000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 35 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 35} 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[7] _id=6ac53e89de269131f9b676a9 ts=2026-10-06T18:31:37.3620000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[216] _id=6ac54150de269131f9b6c6db ts=2026-10-06T18:43:28.0950000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[871] _id=6ac546ddde269131f9b7574a ts=2026-10-06T19:07:09.5400000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[215] _id=6ac5414fde269131f9b6c6c9 ts=2026-10-06T18:43:27.3500000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[872] _id=6ac546ddde269131f9b75735 ts=2026-10-06T19:07:08.6960000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1009] _id=6ac5482fde269131f9b773dd ts=2026-10-06T19:12:46.7540000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 19 of 67 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[602] _id=6ac5449ade269131f9b71951 ts=2026-10-06T18:57:29.5660000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[610] _id=6ac544afde269131f9b71a9d ts=2026-10-06T18:57:51.1360000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[619] _id=6ac544bdde269131f9b71bef ts=2026-10-06T18:58:04.7060000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3057 | 0.0 | 0.668 | 351.155 | 11.74 | 429960.65 | 0.17 | 213 | 9 |
| PuzzlePieceVisibleEvent | 1791 | 0.0 | 0.057 | 386.242 | 1.497 | 429968.372 | 0.16 | 848 | 5 |
| DialogueEvent | 1563 | 0.0 | 3.947 | 686.808 | 34.388 | 429559.941 | 0.09 | 447 | 9 |
| PlayerPositionEvent | 1478 | 0.0 | 10.002 | 669.495 | 10.127 | 429557.077 | 0.09 | 2 | 8 |
| argumentationNodeEvent | 217 | 0.023 | 0.689 | 3580.457 | 14.027 | 690322.313 | 0.02 | 22 | 2 |
| ObjectInterEvent | 146 | 0.005 | 9.361 | 7350.257 | 547.536 | 510512.74 | 0.01 | 1 | 7 |
| Soil Key Puzzle | 125 | 0.155 | 1.413 | 5529.398 | 18.615 | 518170.703 | 0.01 | 0 | 3 |
| TopographicMapEvent | 66 | 0.021 | 2.766 | 11796.632 | 65569.509 | 511154.111 | 0.01 | 2 | 6 |
| questEvent | 49 | 0.002 | 234.388 | 21906.667 | 84797.707 | 429739.295 | 0.0 | 3 | 15 |
| gameWindowFocusEvent | 34 | 5.226 | 603.497 | 31573.035 | 157682.71 | 431323.735 | 0.0 | 0 | 17 |
| DEBUGMenu | 29 | 10.44 | 567.248 | 37016.683 | 209688.499 | 431313.123 | 0.0 | 0 | 14 |
| gameWindowUnfocusEvent | 26 | 8.045 | 381.034 | 29985.645 | 86376.694 | 430467.168 | 0.0 | 0 | 11 |
| argumentationToolEvent | 24 | 0.008 | 7.45 | 32368.746 | 73247.548 | 690321.14 | 0.0 | 1 | 2 |
| argumentationAnswerEvent | 17 | 1.973 | 27.837 | 45701.199 | 207003.749 | 690389.413 | 0.0 | 0 | 2 |
| gameStartEvent | 14 | 185.815 | 8010.203 | 76677.37 | 342791.818 | 431323.735 | 0.0 | 0 | 12 |
| argumentationEvent | 8 | 0.031 | 153.115 | 97116.886 | 478825.98 | 690318.848 | 0.0 | 1 | 2 |
| EndOfUnit | 2 | 380724.464 | 535499.175 | 535499.175 | 674796.415 | 690273.886 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 1 | 1.876 | 1.876 | 1.876 | 1.876 | 1.876 | 31.98 | 0 | 0 |
| chatEvent | 1 | 3.744 | 3.744 | 3.744 | 3.744 | 3.744 | 16.03 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 18 group(s), 29 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[1114] _id=6ac693e5de269131f9be15f3 ts=2026-10-07T18:48:04.3060000Z == 6ab9a9279a8420a1e6b56b7e.jsonl[1115] _id=6ac693e5de269131f9be15f4 ts=2026-10-07T18:48:04.3060000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[2506] _id=6ac69a0fde269131f9bf11b3 ts=2026-10-07T19:14:20.9730000Z == 6ab9a9279a8420a1e6b56b7e.jsonl[2507] _id=6ac69a0fde269131f9bf11b4 ts=2026-10-07T19:14:20.9730000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[2510] _id=6ac69a0fde269131f9bf11b7 ts=2026-10-07T19:14:20.9740000Z == 6ab9a9279a8420a1e6b56b7e.jsonl[2511] _id=6ac69a0fde269131f9bf11b8 ts=2026-10-07T19:14:20.9740000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 53 group(s), 87 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[1210] _id=6ac69446de269131f9be277d ts=2026-10-07T18:49:39.7370000Z == 6ab9a9279a8420a1e6b56b7e.jsonl[1211] _id=6ac69446de269131f9be277e ts=2026-10-07T18:49:39.7370000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1220] _id=6ac69446de269131f9be2787 ts=2026-10-07T18:49:40.3180000Z == 6ab9a9279a8420a1e6b56b7e.jsonl[1221] _id=6ac69446de269131f9be2788 ts=2026-10-07T18:49:40.3180000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1247] _id=6ac69452de269131f9be296b ts=2026-10-07T18:49:52.6760000Z == 6ab9a9279a8420a1e6b56b7e.jsonl[1244] _id=6ac69452de269131f9be2971 ts=2026-10-07T18:49:52.6760000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[3986] _id=6ace7a74de269131f9d0fd91 ts=? == 6ab9a9279a8420a1e6b56b7e.jsonl[4383] _id=6ace9dccde269131f9d26bcd ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 27 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b7e.jsonl[89] _id=6ac53fc5de269131f9b6986d ts=2026-10-06T18:36:52.9940000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[90] _id=6ac53fc5de269131f9b6986f ts=2026-10-06T18:36:52.9990000Z`; `275ms: 6ab9a9279a8420a1e6b56b7e.jsonl[488] _id=6ac543e7de269131f9b70e39 ts=2026-10-06T18:54:30.7320000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[484] _id=6ac543e7de269131f9b70e41 ts=2026-10-06T18:54:31.0070000Z`; `172ms: 6ab9a9279a8420a1e6b56b7e.jsonl[484] _id=6ac543e7de269131f9b70e41 ts=2026-10-06T18:54:31.0070000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[491] _id=6ac543e7de269131f9b70e49 ts=2026-10-06T18:54:31.1790000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `926ms: 6ab9a9279a8420a1e6b56b7e.jsonl[2195] _id=6ac69771de269131f9beca30 ts=2026-10-07T19:03:12.2030000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[2256] _id=6ac69772de269131f9beca46 ts=2026-10-07T19:03:13.1290000Z`; `129ms: 6ab9a9279a8420a1e6b56b7e.jsonl[2448] _id=6ac69950de269131f9bf013d ts=2026-10-07T19:11:11.8330000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[2447] _id=6ac69950de269131f9bf0141 ts=2026-10-07T19:11:11.9620000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `31ms: 6ab9a9279a8420a1e6b56b7e.jsonl[6712] _id=6ad12060de269131f9df5dd2 ts=2026-10-15T18:50:07.2710000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[6715] _id=6ad12060de269131f9df5dd5 ts=2026-10-15T18:50:07.3020000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 24 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `472ms: 6ab9a9279a8420a1e6b56b7e.jsonl[686] _id=6ac5457bde269131f9b72a7c ts=2026-10-06T19:01:15.4870000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[681] _id=6ac5457cde269131f9b72a87 ts=2026-10-06T19:01:15.9590000Z`; `53ms: 6ab9a9279a8420a1e6b56b7e.jsonl[701] _id=6ac5457dde269131f9b72a9d ts=2026-10-06T19:01:16.8430000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[682] _id=6ac5457dde269131f9b72aa1 ts=2026-10-06T19:01:16.8960000Z`; `23ms: 6ab9a9279a8420a1e6b56b7e.jsonl[698] _id=6ac54582de269131f9b72b1d ts=2026-10-06T19:01:22.1480000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[712] _id=6ac54582de269131f9b72b21 ts=2026-10-06T19:01:22.1710000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `82ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5402] _id=6acfcf0ade269131f9d79f92 ts=2026-10-14T18:50:49.7940000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[5403] _id=6acfcf0ade269131f9d79f96 ts=2026-10-14T18:50:49.8760000Z`; `61ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5418] _id=6acfcf19de269131f9d7a116 ts=2026-10-14T18:51:04.5400000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[5419] _id=6acfcf19de269131f9d7a118 ts=2026-10-14T18:51:04.6010000Z`; `77ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5425] _id=6acfcf22de269131f9d7a1de ts=2026-10-14T18:51:14.0190000Z ~ 6ab9a9279a8420a1e6b56b7e.jsonl[5422] _id=6acfcf22de269131f9d7a1e5 ts=2026-10-14T18:51:14.0960000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b7e.jsonl[2561] _id=6ac7e587de269131f9c589c4 ts=2026-10-08T18:48:39.3210000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[3982] _id=6ace7a59de269131f9d0fc63 ts=2026-10-13T18:37:12.4440000Z; 81h 21m: 6ab9a9279a8420a1e6b56b7e.jsonl[8086] _id=6ad12558de269131f9e0145c ts=2026-10-15T19:11:19.7500000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8310] _id=6ad59d89de269131f9e952c8 ts=2026-10-19T04:33:11.9250000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7e.jsonl[2502] _id=6ac69a08de269131f9bf112a ts=2026-10-07T19:14:15.8970000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2557] _id=6ac7e57dde269131f9c58900 ts=2026-10-08T18:48:28.8810000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b7e.jsonl[3978] _id=6ac7ec7bde269131f9c6897f ts=2026-10-08T19:18:18.9410000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4026] _id=6ace7a74de269131f9d0fdba ts=2026-10-13T18:37:38.8820000Z; 81h 17m: 6ab9a9279a8420a1e6b56b7e.jsonl[8298] _id=6ad126b2de269131f9e04398 ts=2026-10-15T19:17:05.6920000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8389] _id=6ad59de9de269131f9e9536c ts=2026-10-19T04:34:48.4050000Z; 23h 32m: 6ab9a9279a8420a1e6b56b7e.jsonl[2549] _id=6ac69a9ede269131f9bf1ee7 ts=2026-10-07T19:16:45.6680000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2575] _id=6ac7e5aede269131f9c58c01 ts=2026-10-08T18:49:17.7020000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 447 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5475] _id=6acfcf4ede269131f9d7a516 ts=2026-10-14T18:51:58.0950000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5476] _id=6acfcf4ede269131f9d7a517 ts=2026-10-14T18:51:58.0950000Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5492] _id=6acfcf65de269131f9d7a730 ts=2026-10-14T18:52:20.2740000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5493] _id=6acfcf65de269131f9d7a731 ts=2026-10-14T18:52:20.2740000Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5499] _id=6acfcf6dde269131f9d7a803 ts=2026-10-14T18:52:28.3470000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5500] _id=6acfcf6dde269131f9d7a804 ts=2026-10-14T18:52:28.3470000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 44m 
  - Evidence: 191h 44m: 6ab9a9279a8420a1e6b56b7e.jsonl[1010] _id=6ac54830de269131f9b7740b ts=2026-10-06T19:12:48.2880000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5627] _id=6acfd093de269131f9d7c6eb ts=2026-10-14T18:57:22.1740000Z; 105h 45m: 6ab9a9279a8420a1e6b56b7e.jsonl[5627] _id=6acfd093de269131f9d7c6eb ts=2026-10-14T18:57:22.1740000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8652] _id=6ad59fc7de269131f9e955d2 ts=2026-10-19T04:42:46.6380000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b7e.jsonl[3852] _id=6ac7eae5de269131f9c65d4e ts=2026-10-08T19:11:32.9700000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[3988] _id=6ace7a74de269131f9d0fd94 ts=2026-10-13T18:37:33.6200000Z; 81h 16m: 6ab9a9279a8420a1e6b56b7e.jsonl[8302] _id=6ad126b8de269131f9e04490 ts=2026-10-15T19:17:11.8880000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8306] _id=6ad59da0de269131f9e952d3 ts=2026-10-19T04:33:34.9680000Z; 23h 31m: 6ab9a9279a8420a1e6b56b7e.jsonl[2556] _id=6ac69abade269131f9bf2088 ts=2026-10-07T19:17:13.4130000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2564] _id=6ac7e58dde269131f9c589f6 ts=2026-10-08T18:48:45.1510000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 213 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[1114] _id=6ac693e5de269131f9be15f3 ts=2026-10-07T18:48:04.3060000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[1115] _id=6ac693e5de269131f9be15f4 ts=2026-10-07T18:48:04.3060000Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[1749] _id=6ac69500de269131f9be4a53 ts=2026-10-07T18:52:47.5750000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[1750] _id=6ac69500de269131f9be4a54 ts=2026-10-07T18:52:47.5750000Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[2463] _id=6ac69964de269131f9bf03a3 ts=2026-10-07T19:11:31.1880000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2466] _id=6ac69964de269131f9bf03a4 ts=2026-10-07T19:11:31.1880000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 141h 48m 
  - Evidence: 141h 48m: 6ab9a9279a8420a1e6b56b7e.jsonl[3735] _id=6ac7ea4cde269131f9c64b24 ts=2026-10-08T19:08:59.4870000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4891] _id=6acfb47dde269131f9d615a5 ts=2026-10-14T16:57:32.2270000Z; 81h 17m: 6ab9a9279a8420a1e6b56b7e.jsonl[8291] _id=6ad126a8de269131f9e041f9 ts=2026-10-15T19:16:55.5570000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8400] _id=6ad59de9de269131f9e9536a ts=2026-10-19T04:34:48.3830000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7e.jsonl[2079] _id=6ac69569de269131f9be6643 ts=2026-10-07T18:54:32.4350000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2759] _id=6ac7e798de269131f9c5cec4 ts=2026-10-08T18:57:28.1750000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b7e.jsonl[89] _id=6ac53fc5de269131f9b6986d ts=2026-10-06T18:36:52.9940000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[90] _id=6ac53fc5de269131f9b6986f ts=2026-10-06T18:36:52.9990000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b7e.jsonl[3977] _id=6ac7ec79de269131f9c6895f ts=2026-10-08T19:18:16.4780000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[3987] _id=6ace7a74de269131f9d0fd93 ts=2026-10-13T18:37:33.5550000Z; 81h 16m: 6ab9a9279a8420a1e6b56b7e.jsonl[8300] _id=6ad126b7de269131f9e04469 ts=2026-10-15T19:17:10.7890000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8305] _id=6ad59da0de269131f9e952d2 ts=2026-10-19T04:33:33.1590000Z; 23h 31m: 6ab9a9279a8420a1e6b56b7e.jsonl[2554] _id=6ac69ab9de269131f9bf207c ts=2026-10-07T19:17:12.7190000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2562] _id=6ac7e58cde269131f9c589e5 ts=2026-10-08T18:48:39.3430000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[4378] _id=6ace9d59de269131f9d26afe ts=2026-10-13T21:06:32.1590000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4379] _id=6ace9da9de269131f9d26b91 ts=2026-10-13T21:06:32.159Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[5979] _id=6acfd4e5de269131f9d86bc5 ts=2026-10-14T19:15:48.4110000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5980] _id=6acfd538de269131f9d880c4 ts=2026-10-14T19:15:48.411Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b7e.jsonl[3866] _id=6ac7eae5de269131f9c65d40 ts=2026-10-08T19:11:30.9070000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4030] _id=6ace7a75de269131f9d0fdca ts=2026-10-13T18:37:39.2790000Z; 26h 18m: 6ab9a9279a8420a1e6b56b7e.jsonl[4558] _id=6acfaf84de269131f9d59797 ts=2026-10-14T16:36:19.1450000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[7051] _id=6ad1217ade269131f9df7e2a ts=2026-10-15T18:54:48.6670000Z; 24h 10m: 6ab9a9279a8420a1e6b56b7e.jsonl[2046] _id=6ac69531de269131f9be5833 ts=2026-10-07T18:53:35.0940000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2913] _id=6ac7e93fde269131f9c612b5 ts=2026-10-08T19:04:30.7850000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 848 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[1119] _id=6ac69445de269131f9be2751 ts=2026-10-07T18:49:39.5720000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[1213] _id=6ac69445de269131f9be2758 ts=2026-10-07T18:49:39.5720000Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[1210] _id=6ac69446de269131f9be277d ts=2026-10-07T18:49:39.7370000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[1211] _id=6ac69446de269131f9be277e ts=2026-10-07T18:49:39.7370000Z; 0ms: 6ab9a9279a8420a1e6b56b7e.jsonl[1213] _id=6ac69445de269131f9be2758 ts=2026-10-07T18:49:39.5720000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[1214] _id=6ac69446de269131f9be2773 ts=2026-10-07T18:49:39.5720000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 6ab9a9279a8420a1e6b56b7e.jsonl[2891] _id=6ac7e914de269131f9c6094c ts=2026-10-08T19:03:48.2870000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5648] _id=6acfd12fde269131f9d7d957 ts=2026-10-14T18:59:58.9900000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7e.jsonl[2081] _id=6ac6956cde269131f9be66e8 ts=2026-10-07T18:54:35.4620000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2758] _id=6ac7e798de269131f9c5cec0 ts=2026-10-08T18:57:28.1700000Z; 23h 53m: 6ab9a9279a8420a1e6b56b7e.jsonl[5651] _id=6acfd131de269131f9d7d96c ts=2026-10-14T18:59:59.9510000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6997] _id=6ad1211dde269131f9df72b1 ts=2026-10-15T18:53:16.9760000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 141h 59m 
  - Evidence: 141h 59m: 6ab9a9279a8420a1e6b56b7e.jsonl[2599] _id=6ac7e615de269131f9c597e2 ts=2026-10-08T18:51:01.1170000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4758] _id=6acfb2c8de269131f9d5ee28 ts=2026-10-14T16:50:15.2280000Z; 24h 6m: 6ab9a9279a8420a1e6b56b7e.jsonl[5795] _id=6acfd2f5de269131f9d81724 ts=2026-10-14T19:07:32.6210000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8145] _id=6ad125e7de269131f9e028c2 ts=2026-10-15T19:13:43.1520000Z; 23h 51m: 6ab9a9279a8420a1e6b56b7e.jsonl[646] _id=6ac544fbde269131f9b71ff8 ts=2026-10-06T18:59:07.3210000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[1287] _id=6ac69464de269131f9be2cb0 ts=2026-10-07T18:50:11.7390000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.037s shown 
  - Evidence: 21ms: 6ab9a9279a8420a1e6b56b7e.jsonl[2184] _id=6ac69769de269131f9bec918 ts=2026-10-07T19:03:04.0110000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2188] _id=6ac69769de269131f9bec91c ts=2026-10-07T19:03:04.0320000Z; 37ms: 6ab9a9279a8420a1e6b56b7e.jsonl[2190] _id=6ac69769de269131f9bec915 ts=2026-10-07T19:03:03.9740000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2184] _id=6ac69769de269131f9bec918 ts=2026-10-07T19:03:04.0110000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 46m 
  - Evidence: 191h 46m: 6ab9a9279a8420a1e6b56b7e.jsonl[805] _id=6ac54679de269131f9b74607 ts=2026-10-06T19:05:28.6600000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5479] _id=6acfcf4ede269131f9d7a514 ts=2026-10-14T18:51:58.0730000Z; 23h 55m: 6ab9a9279a8420a1e6b56b7e.jsonl[5481] _id=6acfcf8dde269131f9d7ab79 ts=2026-10-14T18:53:01.0550000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6650] _id=6ad1201bde269131f9df5725 ts=2026-10-15T18:48:58.3880000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 45m 
  - Evidence: 191h 45m: 6ab9a9279a8420a1e6b56b7e.jsonl[797] _id=6ac54679de269131f9b7460d ts=2026-10-06T19:05:28.6840000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5399] _id=6acfcf08de269131f9d79f6b ts=2026-10-14T18:50:47.5320000Z; 23h 54m: 6ab9a9279a8420a1e6b56b7e.jsonl[5530] _id=6acfcf8dde269131f9d7ab7b ts=2026-10-14T18:53:01.0760000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6576] _id=6ad11fb3de269131f9df4a49 ts=2026-10-15T18:47:14.5860000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.031s..0.031s shown 
  - Evidence: 31ms: 6ab9a9279a8420a1e6b56b7e.jsonl[6712] _id=6ad12060de269131f9df5dd2 ts=2026-10-15T18:50:07.2710000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6715] _id=6ad12060de269131f9df5dd5 ts=2026-10-15T18:50:07.3020000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 45m 
  - Evidence: 191h 45m: 6ab9a9279a8420a1e6b56b7e.jsonl[800] _id=6ac54669de269131f9b7437b ts=2026-10-06T19:05:13.2580000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5390] _id=6acfcefcde269131f9d79e33 ts=2026-10-14T18:50:35.5710000Z; 23h 54m: 6ab9a9279a8420a1e6b56b7e.jsonl[5529] _id=6acfcf8bde269131f9d7ab3e ts=2026-10-14T18:52:59.0550000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6571] _id=6ad11fb1de269131f9df4a1f ts=2026-10-15T18:47:12.5050000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.023s..0.023s shown 
  - Evidence: 23ms: 6ab9a9279a8420a1e6b56b7e.jsonl[6681] _id=6ad1202ede269131f9df59a1 ts=2026-10-15T18:49:17.8440000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6680] _id=6ad1202ede269131f9df59a5 ts=2026-10-15T18:49:17.8670000Z; 23ms: 6ab9a9279a8420a1e6b56b7e.jsonl[698] _id=6ac54582de269131f9b72b1d ts=2026-10-06T19:01:22.1480000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[712] _id=6ac54582de269131f9b72b21 ts=2026-10-06T19:01:22.1710000Z; 23ms: 6ab9a9279a8420a1e6b56b7e.jsonl[755] _id=6ac54667de269131f9b74307 ts=2026-10-06T19:05:10.6700000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[794] _id=6ac54667de269131f9b7430b ts=2026-10-06T19:05:10.6930000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 45m 
  - Evidence: 191h 45m: 6ab9a9279a8420a1e6b56b7e.jsonl[808] _id=6ac54679de269131f9b745ff ts=2026-10-06T19:05:28.6540000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[5402] _id=6acfcf0ade269131f9d79f92 ts=2026-10-14T18:50:49.7940000Z; 23h 56m: 6ab9a9279a8420a1e6b56b7e.jsonl[5506] _id=6acfcf72de269131f9d7a86b ts=2026-10-14T18:52:33.4010000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[6636] _id=6ad12002de269131f9df544a ts=2026-10-15T18:48:33.4310000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.008s..0.008s shown 
  - Evidence: 8ms: 6ab9a9279a8420a1e6b56b7e.jsonl[784] _id=6ac5465cde269131f9b740d3 ts=2026-10-06T19:04:59.5990000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[786] _id=6ac5465cde269131f9b740dd ts=2026-10-06T19:04:59.6070000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b7e.jsonl[2559] _id=6ac7e57dde269131f9c58902 ts=2026-10-08T18:48:29.0230000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[3984] _id=6ace7a59de269131f9d0fc65 ts=2026-10-13T18:37:12.7580000Z; 81h 58m: 6ab9a9279a8420a1e6b56b7e.jsonl[6004] _id=6ad11cb8de269131f9deeff4 ts=2026-10-15T18:34:31.2830000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8312] _id=6ad59d89de269131f9e952ca ts=2026-10-19T04:33:12.0690000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7e.jsonl[2497] _id=6ac699fede269131f9bf103d ts=2026-10-07T19:14:05.7720000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2559] _id=6ac7e57dde269131f9c58902 ts=2026-10-08T18:48:29.0230000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b7e.jsonl[2558] _id=6ac7e57dde269131f9c58901 ts=2026-10-08T18:48:29.0230000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[3983] _id=6ace7a59de269131f9d0fc64 ts=2026-10-13T18:37:12.7580000Z; 81h 21m: 6ab9a9279a8420a1e6b56b7e.jsonl[8084] _id=6ad12552de269131f9e0138c ts=2026-10-15T19:11:13.2220000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8311] _id=6ad59d89de269131f9e952c9 ts=2026-10-19T04:33:12.0690000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7e.jsonl[2496] _id=6ac699fede269131f9bf103c ts=2026-10-07T19:14:05.7720000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2558] _id=6ac7e57dde269131f9c58901 ts=2026-10-08T18:48:29.0230000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 34m 
  - Evidence: 119h 34m: 6ab9a9279a8420a1e6b56b7e.jsonl[3981] _id=6ace7a59de269131f9d0fc5b ts=2026-10-08T19:18:24.958Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4251] _id=6ace7e04de269131f9d12f3f ts=2026-10-13T18:52:52.1260000Z; 24h 1m: 6ab9a9279a8420a1e6b56b7e.jsonl[2560] _id=6ac7e57dde269131f9c588fe ts=2026-10-07T19:17:21.796Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[3981] _id=6ace7a59de269131f9d0fc5b ts=2026-10-08T19:18:24.958Z; 23h 55m: 6ab9a9279a8420a1e6b56b7e.jsonl[1088] _id=6ac693b1de269131f9be0d44 ts=2026-10-06T19:17:43.331Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2495] _id=6ac699bede269131f9bf0aa8 ts=2026-10-07T19:13:00.6210000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9279a8420a1e6b56b7e.jsonl[3930] _id=6ac7ebc8de269131f9c67672 ts=2026-10-08T19:15:19.6350000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[4028] _id=6ace7a74de269131f9d0fdbc ts=2026-10-13T18:37:38.9300000Z; 81h 20m: 6ab9a9279a8420a1e6b56b7e.jsonl[8140] _id=6ad125dede269131f9e02719 ts=2026-10-15T19:13:33.1780000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[8327] _id=6ad59da0de269131f9e952d7 ts=2026-10-19T04:33:35.1460000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7e.jsonl[2516] _id=6ac69a0fde269131f9bf11bd ts=2026-10-07T19:14:21.0140000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[2563] _id=6ac7e58cde269131f9c589e6 ts=2026-10-08T18:48:42.9970000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.008s shown 
  - Evidence: 2ms: 6ab9a9279a8420a1e6b56b7e.jsonl[663] _id=6ac54511de269131f9b72134 ts=2026-10-06T18:59:28.2910000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[659] _id=6ac54511de269131f9b72139 ts=2026-10-06T18:59:28.2930000Z; 8ms: 6ab9a9279a8420a1e6b56b7e.jsonl[111] _id=6ac5400ede269131f9b6a091 ts=2026-10-06T18:38:05.9970000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[108] _id=6ac5400ede269131f9b6a098 ts=2026-10-06T18:38:06.0050000Z; 8ms: 6ab9a9279a8420a1e6b56b7e.jsonl[220] _id=6ac5415dde269131f9b6c7f1 ts=2026-10-06T18:43:40.6350000Z -> 6ab9a9279a8420a1e6b56b7e.jsonl[219] _id=6ac5415dde269131f9b6c7f3 ts=2026-10-06T18:43:40.6430000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[567] _id=6ac5447ade269131f9b71793 ts=2026-10-06T18:56:58.2530000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[775] _id=6ac54652de269131f9b74009 ts=2026-10-06T19:04:50.1940000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[2549] _id=6ac69a9ede269131f9bf1ee7 ts=2026-10-07T19:16:45.6680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[6715] _id=6ad12060de269131f9df5dd5 ts=2026-10-15T18:50:07.3020000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[682] _id=6ac5457dde269131f9b72aa1 ts=2026-10-06T19:01:16.8960000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[712] _id=6ac54582de269131f9b72b21 ts=2026-10-06T19:01:22.1710000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[794] _id=6ac54667de269131f9b7430b ts=2026-10-06T19:05:10.6930000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[3986] _id=6ace7a74de269131f9d0fd91 ts=?`; `6ab9a9279a8420a1e6b56b7e.jsonl[4383] _id=6ace9dccde269131f9d26bcd ts=?`; `6ab9a9279a8420a1e6b56b7e.jsonl[7071] _id=6ad121c1de269131f9df8706 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 57 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[3049] _id=6ac7e9d7de269131f9c63170 ts=2026-10-08T19:07:01.4420000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[3051] _id=6ac7e9d7de269131f9c63175 ts=2026-10-08T19:07:01.6060000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[3107] _id=6ac7e9dfde269131f9c63306 ts=2026-10-08T19:07:08.4410000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 97 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[1211] _id=6ac69446de269131f9be277e ts=2026-10-07T18:49:39.7370000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1217] _id=6ac69446de269131f9be277f ts=2026-10-07T18:49:39.9240000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1218] _id=6ac69446de269131f9be2780 ts=2026-10-07T18:49:40.0400000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 13 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[744] _id=6ac545fcde269131f9b73529 ts=2026-10-06T19:03:24.6010000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[754] _id=6ac5460bde269131f9b73613 ts=2026-10-06T19:03:39.5000000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[785] _id=6ac5465ade269131f9b7408d ts=2026-10-06T19:04:57.6570000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 288 start, 282 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 545 open, 533 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 13 unmatched 'argumentationToolOpen' (totals: 19 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 30 start, 20 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 227 of 8673 adjacent _id pairs reverse in client time; worst 102.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b7e.jsonl[1385] _id=6ac694adde269131f9be3a46 ts=2026-10-07T18:51:24.3460000Z`; `6ab9a9279a8420a1e6b56b7e.jsonl[1364] _id=6ac694adde269131f9be3a48 ts=2026-10-07T18:49:41.9370000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.84s, min -429528.05s, max -0.37s over 8674 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7e\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
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
  - Observed: 3 records 
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

### `InputEvent` — 3058 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1077); Unit 3 Dev (1062); Unit 3 Dungeon Dev (498); Unit 1 Dev (415); Unit 4 Dev (6)
- **Intervals:** median 0.67s (p5 0.02s / p95 11.74s, n=3057)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3058/3058 records)
    "pressed"  x3058
data.actionType  (string, 3058/3058 records)
    "Move"  x2081
    "Interact"  x350
    "Sprint"  x308
    "Jump"  x170
    "Ascend"  x58
    "Descend"  x40
    "Hoverboard"  x35
    "Map"  x14
    "SkipCinematic"  x2
data.key  (string, 3058/3058 records, 1 empty-string)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3058/3058 records)
    "Player"  x2515
    "Drone"  x543
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 1792 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1518); Unit 3 Dungeon Dev (274)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.50s, n=1791)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1792/1792 records)
    "BecameVisible"  x545
    "BecameInvisible"  x533
    "BecameCameraCentered"  x357
    "BecameCameraUncentered"  x357
data.pieceId  (string, 1792/1792 records)
    24 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1792/1792 records)
    1243 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1564 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (845); Unit 3 Dev (379); Unit 1 Dev (218); Unit 3 Dungeon Dev (119); Unit 4 Dev (3)
- **eventKey:** present on 994 of 1564 records
- **Intervals:** median 3.95s (p5 0.00s / p95 34.39s, n=1563)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x994; [conversationId, dialogueEventType] x570
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1564/1564 records)
    numeric range 8 .. 104 (37 unique)
data.dialogueEventType  (string, 1564/1564 records)
    "DialogueNodeEvent"  x994
    "DialogueStartEvent"  x288
    "DialogueFinishEvent"  x282
data.nodeId  (number, 994/1564 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1486 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (817); Unit 3 Dev (314); Unit 1 Dev (239); Unit 3 Dungeon Dev (99); Unit 4 Dev (17)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=1478)
- **Fields under `data`:**

```text
data.position  (object, 1486/1486 records)
data.position.x  (number, 1486/1486 records)
    numeric range -742.236 .. 1789.35 (402 unique)
data.position.y  (number, 1486/1486 records)
    numeric range -115.127 .. 157.866 (334 unique)
data.position.z  (number, 1486/1486 records)
    numeric range -1124.84 .. 1875.28 (402 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 218 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (97); Unit 2 Prod (Refactor) (85); Unit 1 Dev (36)
- **Intervals:** median 0.69s (p5 0.04s / p95 14.03s, n=217)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 218/218 records)
    "argumentationNodeHoverEnd"  x98
    "argumentationNodeHoverStart"  x95
    "argumentationNodeAdd"  x17
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 218/218 records)
    "Unit 3 - Pollution Upstream"  x97
    "Unit 2 – Watershed"  x85
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x17
data.nodeName  (string, 218/218 records)
    "A"  x38
    "1"  x35
    "I"  x31
    "B"  x28
    "2"  x20
    "C"  x18
    "II"  x13
    "5"  x11
    "3"  x8
    "4"  x8
    "D"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 147 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (63); Unit 3 Dungeon Dev (44); Unit 1 Dev (27); Unit 3 Dev (13)
- **Intervals:** median 9.36s (p5 0.17s / p95 547.54s, n=146)
- **Fields under `data`:**

```text
data.actionType  (string, 147/147 records)
    19 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 147/147 records)
    54 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 126 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (96); Unit 3 Dev (30)
- **Intervals:** median 1.41s (p5 0.17s / p95 18.61s, n=125)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x120; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/126 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/126 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 120/126 records)
    "RightDrag"  x64
    "LeftDrag"  x56
data.currentSoilType  (string, 120/126 records)
    "SAND"  x26
    "SANDGRAVEL"  x23
    "CLAYSAND"  x21
    "CLAY"  x18
    "CLAYROCK"  x16
    "GRAVEL"  x10
    "BEDROCK"  x6
data.isCorrectSelection  (string, 120/126 records)
    "false"  x91
    "true"  x29
data.waterLevelStatus  (string, 120/126 records)
    "TooHigh"  x49
    "Proper"  x41
    "TooLow"  x30
data.waterRetentionChange  (string, 120/126 records)
    "Increase"  x48
    "Decrease"  x43
    "NoChange"  x29
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 67 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (31); Unit 1 Dev (24); Unit 3 Dev (12)
- **Intervals:** median 2.77s (p5 0.31s / p95 65569.51s, n=66)
- **`data` key-set variants:** [actionType, featureUsed] x36; [actionType, featureUsed, legendName] x19; [actionType, featureUsed, location] x12
- **Fields under `data`:**

```text
data.actionType  (string, 67/67 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
    "Selected"  x14
    "WaypointMoveEvent"  x9
    "Unselected"  x5
    "WaypointSetEvent"  x3
data.featureUsed  (string, 67/67 records)
    "Map"  x36
    "Legend"  x19
    "Waypoint"  x12
data.legendName  (string, 19/67 records)
    "Teleporter Room"  x7
    "90 ft"  x3
    "Jasper's Room"  x2
    "Tera's Room"  x2
    "Toppo's Room"  x2
    "Anderson's Room"  x1
    "Commons"  x1
    "PodBay"  x1
data.location  (object, 12/67 records)
data.location.x  (number, 12/67 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 12/67 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 12/67 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 50 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 1 Dev (12); Unit 3 Dev (11); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 50 of 50 records
- **Intervals:** median 234.39s (p5 1.42s / p95 84797.71s, n=49)
- **`data` key-set variants:** [questEventType, questID, questName] x30; [questEventType, questID, questName, questSuccessOrFailure] x20
- **Fields under `data`:**

```text
data.questEventType  (string, 50/50 records)
    "questActiveEvent"  x30
    "questFinishEvent"  x20
data.questID  (string, 50/50 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 50/50 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 20/50 records)
    "Succeeded"  x20
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 35 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (9); Unit 3 Dev (6); Unit 1 Dev (3); Transition (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 603.50s (p5 39.54s / p95 157682.71s, n=34)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 35/35 records)
    true  x35
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (10); Unit 3 Dev (4); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 567.25s (p5 10.51s / p95 209688.50s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 27 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (7); Unit 1 Dev (3); Unit 3 Dungeon Dev (2)
- **Intervals:** median 381.03s (p5 16.96s / p95 86376.69s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 25 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (13); Unit 2 Prod (Refactor) (9); Unit 3 Dev (3)
- **Intervals:** median 7.45s (p5 0.06s / p95 73247.55s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "argumentationToolOpen"  x19
    "argumentationToolClose"  x6
data.argumentationTitle  (string, 25/25 records)
    "Unit 1 - Freshwater"  x11
    "Unit 2 – Watershed"  x9
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 25/25 records)
    "BackingInfoPanel - "  x11
    "BackingInfoPanel - Watershed Graph"  x7
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (6); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 27.84s (p5 2.33s / p95 207003.75s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    "I"  x4
    "A,I"  x3
    "A,1,I"  x2
    "A,5,I"  x2
    "A,1,II"  x1
    "A,2,I"  x1
    "A,3,I"  x1
    "A,4,I"  x1
    "B,2,I"  x1
    "C,1,I"  x1
    "C,A,1,I"  x1
data.argumentationTitle  (string, 18/18 records)
    "Unit 1 - Freshwater"  x8
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 8010.20s (p5 447.55s / p95 342791.82s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 153.11s (p5 6.41s / p95 478825.98s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 535499.18s (p5 396201.94s / p95 674796.41s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x3
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 3 empty-string)
    ""  x3
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x2
    "unit3"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 1.88s (p5 1.88s / p95 1.88s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 3.74s (p5 3.74s / p95 3.74s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[32-88, 32-91, 32-95, 32-96, 30-98]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (96 records)
- `TopographicMapEvent` data.actionType: "Selected" (14x); "Unselected" (5x); "WaypointMoveEvent" (9x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (19x); "Waypoint" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*