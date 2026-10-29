# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b0b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b0b
- **Game version string(s) in log:** 2.8.9, 2.9.0, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b0b.jsonl
- **Records:** 12217 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b0b
- **Time span:** 2026-10-05T15:15:58.839000+00:00 .. 2026-10-16T15:48:13.312000+00:00 (264h 32m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b0b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 12217 records, 6 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 93 INFO, 2 NOT_TESTED, 72 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6572 | 53.79 | 1 | 4 | 0 | 2026-10-05T15:16:28.015000+00:00 | 2026-10-16T15:44:36.514000+00:00 | 264h 28m |
| PuzzlePieceVisibleEvent | 1720 | 14.08 | 1 | 2 | 0 | 2026-10-07T15:46:47.931000+00:00 | 2026-10-16T15:25:49.457000+00:00 | 215h 39m |
| DialogueEvent | 1530 | 12.52 | 1 | 5 | 990 | 2026-10-05T15:16:28.994000+00:00 | 2026-10-16T15:45:48.034000+00:00 | 264h 29m |
| PlayerPositionEvent | 1375 | 11.25 | 1 | 5 | 0 | 2026-10-05T15:16:08.958000+00:00 | 2026-10-16T15:48:13.312000+00:00 | 264h 32m |
| ObjectInterEvent | 435 | 3.56 | 1 | 4 | 0 | 2026-10-05T15:20:57.137000+00:00 | 2026-10-16T15:44:39.478000+00:00 | 264h 23m |
| argumentationNodeEvent | 203 | 1.66 | 1 | 3 | 0 | 2026-10-05T15:44:28.253000+00:00 | 2026-10-16T15:15:03.876000+00:00 | 263h 30m |
| TopographicMapEvent | 92 | 0.75 | 1 | 4 | 0 | 2026-10-07T15:25:09.787000+00:00 | 2026-10-16T15:38:45.628000+00:00 | 216h 13m |
| Soil Key Puzzle | 64 | 0.52 | 1 | 2 | 0 | 2026-10-08T15:34:44.271000+00:00 | 2026-10-16T15:22:45.918000+00:00 | 191h 48m |
| questEvent | 54 | 0.44 | 1 | 4 | 54 | 2026-10-05T15:16:28.969000+00:00 | 2026-10-16T15:44:44.252000+00:00 | 264h 28m |
| DaniEvent | 48 | 0.39 | 1 | 2 | 0 | 2026-10-07T15:25:05.617000+00:00 | 2026-10-07T15:44:19.606000+00:00 | 19m 13s |
| DEBUGMenu | 30 | 0.25 | 1 | 6 | 0 | 2026-10-05T15:16:08.935000+00:00 | 2026-10-16T15:45:31.295000+00:00 | 264h 29m |
| gameWindowFocusEvent | 26 | 0.21 | 1 | 6 | 0 | 2026-10-05T15:15:58.839000+00:00 | 2026-10-16T15:46:00.850000+00:00 | 264h 30m |
| gameWindowUnfocusEvent | 17 | 0.14 | 1 | 5 | 0 | 2026-10-05T15:48:00.468000+00:00 | 2026-10-16T15:46:00.826000+00:00 | 263h 58m |
| gameStartEvent | 15 | 0.12 | 1 | 1 | 0 | 2026-10-05T15:15:58.840000+00:00 | 2026-10-16T15:45:20.455000+00:00 | 264h 29m |
| argumentationEvent | 13 | 0.11 | 1 | 3 | 0 | 2026-10-05T15:45:31.211000+00:00 | 2026-10-16T15:15:05.402000+00:00 | 263h 29m |
| argumentationAnswerEvent | 9 | 0.07 | 1 | 3 | 0 | 2026-10-05T15:45:43.201000+00:00 | 2026-10-16T15:15:05.349000+00:00 | 263h 29m |
| chatEvent | 6 | 0.05 | 1 | 1 | 0 | 2026-10-07T15:25:20.287000+00:00 | 2026-10-07T15:30:37.801000+00:00 | 5m 17s |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-10-15T15:30:47.301000+00:00 | 2026-10-16T15:44:54.099000+00:00 | 24h 14m |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-05T15:46:42.948000+00:00 | 2026-10-06T15:42:26.686000+00:00 | 23h 55m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 104.966s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87246.798s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 0.26s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.068s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.266s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 87.119s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 86143.738s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 4.167s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43629.407s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 680.685s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 530.007s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 48 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 1720 records 
  - Expected: 5172 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Toppo's Room 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,I; D,1,II 
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
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
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
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[163] _id=6ac3c0cfde269131f9ad139d ts=2026-10-05T15:22:54.7030000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[958] _id=6ac3c3afde269131f9ad44dd ts=2026-10-05T15:35:10.2160000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1036] _id=6ac3c3e3de269131f9ad47e7 ts=2026-10-05T15:36:02.8510000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[1] _id=6ac3bf30de269131f9ace73a ts=2026-10-05T15:15:58.8400000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1384] _id=6ac515b5de269131f9b48578 ts=2026-10-06T15:37:23.8780000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1807] _id=6ac66379de269131f9bb9f82 ts=2026-10-07T15:21:28.4560000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[0] _id=6ac3bf2fde269131f9ace735 ts=2026-10-05T15:15:58.8390000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1382] _id=6ac515b5de269131f9b48576 ts=2026-10-06T15:37:23.8770000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1806] _id=6ac66379de269131f9bb9f81 ts=2026-10-07T15:21:28.4560000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[1383] _id=6ac515b4de269131f9b48566 ts=2026-10-05T15:48:00.468Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1804] _id=6ac66378de269131f9bb9f7c ts=2026-10-06T15:47:33.881Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[2158] _id=6ac663e6de269131f9bbabcf ts=2026-10-07T15:23:05.589Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 3 of 92 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[2321] _id=6ac66456de269131f9bbb6a8 ts=2026-10-07T15:25:09.7870000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[2319] _id=6ac66458de269131f9bbb6d0 ts=2026-10-07T15:25:11.9270000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[2325] _id=6ac6645fde269131f9bbb765 ts=2026-10-07T15:25:18.5150000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6571 | 0.0 | 0.333 | 144.892 | 4.186 | 430650.127 | 0.41 | 655 | 8 |
| PuzzlePieceVisibleEvent | 1719 | 0.0 | 0.068 | 451.624 | 1.425 | 516959.518 | 0.13 | 729 | 4 |
| DialogueEvent | 1529 | 0.0 | 3.812 | 622.733 | 25.482 | 430748.283 | 0.1 | 430 | 7 |
| PlayerPositionEvent | 1369 | 9.756 | 10.003 | 695.506 | 10.261 | 430648.04 | 0.09 | 0 | 7 |
| ObjectInterEvent | 434 | 0.012 | 0.26 | 2193.139 | 147.694 | 516773.967 | 0.03 | 3 | 10 |
| argumentationNodeEvent | 202 | 0.006 | 0.899 | 4696.216 | 14.644 | 690809.512 | 0.01 | 22 | 4 |
| TopographicMapEvent | 91 | 0.0 | 6.266 | 8554.02 | 42829.231 | 430847.366 | 0.01 | 5 | 9 |
| Soil Key Puzzle | 63 | 0.063 | 1.527 | 10960.026 | 31.501 | 516918.783 | 0.01 | 0 | 2 |
| questEvent | 53 | 0.002 | 150.818 | 17964.062 | 85633.272 | 430705.174 | 0.0 | 8 | 11 |
| DaniEvent | 47 | 0.005 | 2.138 | 24.553 | 60.374 | 716.891 | 2.44 | 4 | 1 |
| DEBUGMenu | 29 | 7.696 | 104.966 | 32833.185 | 87086.625 | 431340.037 | 0.0 | 0 | 12 |
| gameWindowFocusEvent | 25 | 2.004 | 680.685 | 38088.08 | 87236.946 | 431384.96 | 0.0 | 0 | 14 |
| gameWindowUnfocusEvent | 16 | 3.908 | 530.007 | 59392.522 | 194521.95 | 518727.28 | 0.0 | 0 | 8 |
| gameStartEvent | 14 | 109.69 | 43629.407 | 68011.544 | 207980.011 | 431384.96 | 0.0 | 0 | 11 |
| argumentationEvent | 12 | 0.036 | 46.455 | 79047.849 | 396741.758 | 776509.141 | 0.0 | 1 | 3 |
| argumentationAnswerEvent | 8 | 14.914 | 87.119 | 118570.268 | 534876.797 | 776557.833 | 0.0 | 0 | 3 |
| chatEvent | 5 | 1.88 | 4.167 | 63.503 | 233.502 | 286.605 | 0.94 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 87246.798 | 87246.798 | 87246.798 | 87246.798 | 87246.798 | 0.0 | 0 | 1 |
| argumentationToolEvent | 1 | 86143.738 | 86143.738 | 86143.738 | 86143.738 | 86143.738 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 27 group(s), 74 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[1819] _id=6ac66384de269131f9bba074 ts=2026-10-07T15:21:38.4450000Z == 6ab9a8bc9a8420a1e6b56b0b.jsonl[1820] _id=6ac66384de269131f9bba075 ts=2026-10-07T15:21:38.4450000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1825] _id=6ac66384de269131f9bba07a ts=2026-10-07T15:21:39.2440000Z == 6ab9a8bc9a8420a1e6b56b0b.jsonl[1826] _id=6ac66384de269131f9bba07b ts=2026-10-07T15:21:39.2440000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[2180] _id=6ac663f0de269131f9bbacde ts=2026-10-07T15:23:27.2600000Z == 6ab9a8bc9a8420a1e6b56b0b.jsonl[2182] _id=6ac663f0de269131f9bbace0 ts=2026-10-07T15:23:27.2600000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 21 group(s), 22 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[3847] _id=6ac66969de269131f9bc2c69 ts=2026-10-07T15:46:47.9310000Z == 6ab9a8bc9a8420a1e6b56b0b.jsonl[3849] _id=6ac66969de269131f9bc2c71 ts=2026-10-07T15:46:47.9310000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[3852] _id=6ac66969de269131f9bc2c76 ts=2026-10-07T15:46:48.0970000Z == 6ab9a8bc9a8420a1e6b56b0b.jsonl[3853] _id=6ac66969de269131f9bc2c7a ts=2026-10-07T15:46:48.0970000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[3858] _id=6ac6696ade269131f9bc2c96 ts=2026-10-07T15:46:49.6180000Z == 6ab9a8bc9a8420a1e6b56b0b.jsonl[3857] _id=6ac6696bde269131f9bc2c9a ts=2026-10-07T15:46:49.6180000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `521ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2692] _id=6ac66560de269131f9bbd7d4 ts=2026-10-07T15:29:35.9920000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[2687] _id=6ac66561de269131f9bbd7dc ts=2026-10-07T15:29:36.5130000Z`; `375ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2685] _id=6ac66561de269131f9bbd7da ts=2026-10-07T15:29:36.3240000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[2689] _id=6ac66561de269131f9bbd7de ts=2026-10-07T15:29:36.6990000Z`; `480ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2687] _id=6ac66561de269131f9bbd7dc ts=2026-10-07T15:29:36.5130000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[2676] _id=6ac66561de269131f9bbd7e8 ts=2026-10-07T15:29:36.9930000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 281 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[72] _id=6ac3c05ade269131f9ad06c7 ts=2026-10-05T15:20:57.1370000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[73] _id=6ac3c05ade269131f9ad06cb ts=2026-10-05T15:20:57.1490000Z`; `199ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1869] _id=6ac6639ade269131f9bba2a1 ts=2026-10-07T15:22:02.0530000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[1875] _id=6ac6639ade269131f9bba2ae ts=2026-10-07T15:22:02.2520000Z`; `573ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1875] _id=6ac6639ade269131f9bba2ae ts=2026-10-07T15:22:02.2520000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[1880] _id=6ac6639bde269131f9bba2bd ts=2026-10-07T15:22:02.8250000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `329ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[7393] _id=6acf9bacde269131f9d46d9a ts=2026-10-14T15:11:39.5370000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[7395] _id=6acf9bacde269131f9d46dac ts=2026-10-14T15:11:39.8660000Z`; `479ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[7394] _id=6acf9bacde269131f9d46da1 ts=2026-10-14T15:11:39.7170000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[7396] _id=6acf9badde269131f9d46db6 ts=2026-10-14T15:11:40.1960000Z`; `490ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[7395] _id=6acf9bacde269131f9d46dac ts=2026-10-14T15:11:39.8660000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[7397] _id=6acf9badde269131f9d46dbc ts=2026-10-14T15:11:40.3560000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `195ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2436] _id=6ac664c5de269131f9bbc7e1 ts=2026-10-07T15:27:01.2630000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[2433] _id=6ac664c6de269131f9bbc7e8 ts=2026-10-07T15:27:01.4580000Z`; `198ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2433] _id=6ac664c6de269131f9bbc7e8 ts=2026-10-07T15:27:01.4580000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[2437] _id=6ac664c6de269131f9bbc7f1 ts=2026-10-07T15:27:01.6560000Z`; `348ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2437] _id=6ac664c6de269131f9bbc7f1 ts=2026-10-07T15:27:01.6560000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[2434] _id=6ac664c6de269131f9bbc7fc ts=2026-10-07T15:27:02.0040000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10816] _id=6ad23f79de269131f9e5106e ts=2026-10-16T15:15:05.3660000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[10819] _id=6ad23f79de269131f9e51071 ts=2026-10-16T15:15:05.4020000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1309] _id=6ac3c61fde269131f9ad6bad ts=2026-10-05T15:45:34.2060000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[1312] _id=6ac3c61fde269131f9ad6bb5 ts=2026-10-05T15:45:34.2330000Z`; `23ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1320] _id=6ac3c625de269131f9ad6c35 ts=2026-10-05T15:45:40.5630000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[1323] _id=6ac3c625de269131f9ad6c3b ts=2026-10-05T15:45:40.5860000Z`; `158ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1357] _id=6ac3c67bde269131f9ad7445 ts=2026-10-05T15:47:06.4340000Z ~ 6ab9a8bc9a8420a1e6b56b0b.jsonl[1359] _id=6ac3c67bde269131f9ad744f ts=2026-10-05T15:47:06.5920000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5403] _id=6ac7b79ede269131f9c3e919 ts=2026-10-08T15:32:45.9210000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6209] _id=6ace4c8ade269131f9cf1306 ts=2026-10-13T15:21:45.9580000Z; 24h 21m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6] _id=6ac3bf39de269131f9ace777 ts=2026-10-05T15:16:08.9350000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1385] _id=6ac515bcde269131f9b4866d ts=2026-10-06T15:37:31.9270000Z; 23h 56m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[7247] _id=6acf9af2de269131f9d45d0e ts=2026-10-14T15:08:33.1560000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[8612] _id=6ad0eba2de269131f9dc2562 ts=2026-10-15T15:05:05.2300000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 11m 56s 
  - Evidence: 11m 56s: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2931] _id=6ac66605de269131f9bbeb55 ts=2026-10-07T15:32:20.6060000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[3694] _id=6ac668d2de269131f9bc2085 ts=2026-10-07T15:44:17.4970000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.005s..0.008s shown 
  - Evidence: 5ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2741] _id=6ac66586de269131f9bbdb93 ts=2026-10-07T15:30:13.3880000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[2740] _id=6ac66586de269131f9bbdb95 ts=2026-10-07T15:30:13.3930000Z; 7ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2340] _id=6ac6647cde269131f9bbba1a ts=2026-10-07T15:25:48.2200000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[2343] _id=6ac6647cde269131f9bbba1f ts=2026-10-07T15:25:48.2270000Z; 8ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2344] _id=6ac66480de269131f9bbba88 ts=2026-10-07T15:25:51.9580000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[2345] _id=6ac66480de269131f9bbba8a ts=2026-10-07T15:25:51.9660000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 39m 
  - Evidence: 119h 39m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6188] _id=6ac7ba83de269131f9c41e28 ts=2026-10-08T15:45:06.8350000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6222] _id=6ace4d1fde269131f9cf1864 ts=2026-10-13T15:24:15.1180000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1782] _id=6ac51814de269131f9b4be5f ts=2026-10-06T15:47:31.0750000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[3545] _id=6ac6680bde269131f9bc12da ts=2026-10-07T15:40:58.4370000Z; 23h 51m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1376] _id=6ac3c6acde269131f9ad7848 ts=2026-10-05T15:47:55.5190000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1451] _id=6ac51613de269131f9b48cce ts=2026-10-06T15:38:58.7220000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 430 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10788] _id=6ad23f5ede269131f9e50efa ts=2026-10-16T15:14:37.9330000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10789] _id=6ad23f5ede269131f9e50efb ts=2026-10-16T15:14:37.9330000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[9286] _id=6ad0f05cde269131f9dc869c ts=2026-10-15T15:25:15.8800000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[9287] _id=6ad0f05cde269131f9dc869d ts=2026-10-15T15:25:15.8800000Z; 1ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10769] _id=6ad23f4fde269131f9e50e18 ts=2026-10-16T15:14:23.0270000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10770] _id=6ad23f4fde269131f9e50e19 ts=2026-10-16T15:14:23.0280000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 24h 14m 
  - Evidence: 24h 14m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[9409] _id=6ad0f1a8de269131f9dc9e9c ts=2026-10-15T15:30:47.3010000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[12188] _id=6ad24676de269131f9e55ebf ts=2026-10-16T15:44:54.0990000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 37m 
  - Evidence: 119h 37m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6207] _id=6ac7ba9fde269131f9c41ef7 ts=2026-10-08T15:45:34.7920000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6223] _id=6ace4cd9de269131f9cf155d ts=2026-10-13T15:23:04.9190000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1252] _id=6ac3c5bcde269131f9ad6705 ts=2026-10-05T15:43:55.7500000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1387] _id=6ac515bfde269131f9b486a8 ts=2026-10-06T15:37:32.1340000Z; 23h 36m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[3886] _id=6ac6698bde269131f9bc2fd5 ts=2026-10-07T15:47:22.4360000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[3927] _id=6ac7b578de269131f9c39a8b ts=2026-10-08T15:23:34.3260000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 655 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10126] _id=6ad23c4ede269131f9e4c70e ts=2026-10-16T15:01:32.8010000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10127] _id=6ad23c4ede269131f9e4c70f ts=2026-10-16T15:01:32.8010000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10128] _id=6ad23c4ede269131f9e4c710 ts=2026-10-16T15:01:32.8020000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10129] _id=6ad23c4ede269131f9e4c711 ts=2026-10-16T15:01:32.8020000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10129] _id=6ad23c4ede269131f9e4c711 ts=2026-10-16T15:01:32.8020000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10130] _id=6ad23c4ede269131f9e4c712 ts=2026-10-16T15:01:32.8020000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 32m 
  - Evidence: 143h 32m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5966] _id=6ac7b8a5de269131f9c40140 ts=2026-10-08T15:37:09.5430000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[7368] _id=6acf9b4cde269131f9d465fa ts=2026-10-14T15:10:03.5100000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1259] _id=6ac3c5bdde269131f9ad6711 ts=2026-10-05T15:43:56.6500000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1425] _id=6ac51607de269131f9b48c36 ts=2026-10-06T15:38:46.7860000Z; 23h 39m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[3796] _id=6ac66905de269131f9bc244f ts=2026-10-07T15:45:08.6180000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[4000] _id=6ac7b5b8de269131f9c3a221 ts=2026-10-08T15:24:40.5880000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.012s..0.031s shown 
  - Evidence: 12ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[72] _id=6ac3c05ade269131f9ad06c7 ts=2026-10-05T15:20:57.1370000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[73] _id=6ac3c05ade269131f9ad06cb ts=2026-10-05T15:20:57.1490000Z; 24ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[3015] _id=6ac6663bde269131f9bbefbf ts=2026-10-07T15:33:14.4100000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[3017] _id=6ac6663bde269131f9bbefc2 ts=2026-10-07T15:33:14.4340000Z; 31ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2498] _id=6ac664dede269131f9bbcaef ts=2026-10-07T15:27:26.2360000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[2503] _id=6ac664dede269131f9bbcaf4 ts=2026-10-07T15:27:26.2670000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 37m 
  - Evidence: 119h 37m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6202] _id=6ac7ba98de269131f9c41ecd ts=2026-10-08T15:45:27.8230000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6212] _id=6ace4cd5de269131f9cf1551 ts=2026-10-13T15:22:55.8630000Z; 23h 49m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1377] _id=6ac3c6adde269131f9ad784d ts=2026-10-05T15:47:56.0410000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1386] _id=6ac515bfde269131f9b486a6 ts=2026-10-06T15:37:31.9470000Z; 23h 36m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[3915] _id=6ac66988de269131f9bc2f86 ts=2026-10-07T15:47:19.5430000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[3926] _id=6ac7b578de269131f9c39a8a ts=2026-10-08T15:23:31.9740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 35m 
  - Evidence: 143h 35m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5983] _id=6ac7b8a7de269131f9c40172 ts=2026-10-08T15:37:09.6250000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[7465] _id=6acf9c06de269131f9d475f5 ts=2026-10-14T15:13:09.1430000Z; 24h 10m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[8859] _id=6ad0ed6ede269131f9dc59ac ts=2026-10-15T15:12:44.8900000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[11010] _id=6ad2416fde269131f9e52882 ts=2026-10-16T15:23:26.3010000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[7972] _id=6acf9d70de269131f9d4938e ts=2026-10-14T15:19:09.6530000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[8836] _id=6ad0ed5ede269131f9dc5842 ts=2026-10-15T15:12:27.7700000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 729 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[11056] _id=6ad24181de269131f9e5297e ts=2026-10-16T15:23:43.6400000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[11057] _id=6ad24181de269131f9e52982 ts=2026-10-16T15:23:43.6400000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[11057] _id=6ad24181de269131f9e52982 ts=2026-10-16T15:23:43.6400000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[11059] _id=6ad24181de269131f9e52984 ts=2026-10-16T15:23:43.6400000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[11059] _id=6ad24181de269131f9e52984 ts=2026-10-16T15:23:43.6400000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[11063] _id=6ad24181de269131f9e5298a ts=2026-10-16T15:23:43.6400000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 35m 
  - Evidence: 143h 35m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5480] _id=6ac7b814de269131f9c3f315 ts=2026-10-08T15:34:44.7230000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[7369] _id=6acf9b4cde269131f9d465f3 ts=2026-10-14T15:10:03.5060000Z; 47h 59m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[8084] _id=6acf9e4ede269131f9d4a08b ts=2026-10-14T15:22:53.0180000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10968] _id=6ad24117de269131f9e523e3 ts=2026-10-16T15:21:59.4700000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 40m 
  - Evidence: 119h 40m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6187] _id=6ac7ba83de269131f9c41e27 ts=2026-10-08T15:45:06.8300000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6339] _id=6ace4d82de269131f9cf1af9 ts=2026-10-13T15:25:54.1960000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[3383] _id=6ac6672fde269131f9bc05de ts=2026-10-07T15:37:19.0530000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[4060] _id=6ac7b5f2de269131f9c3a928 ts=2026-10-08T15:25:38.1480000Z; 23h 46m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[8297] _id=6acfa0bbde269131f9d4be51 ts=2026-10-14T15:33:14.9230000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[9112] _id=6ad0ef06de269131f9dc73ec ts=2026-10-15T15:19:33.9140000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.020s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6614] _id=6ace4f83de269131f9cf2c04 ts=2026-10-13T15:34:27.4980000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6616] _id=6ace4f98de269131f9cf2cb6 ts=2026-10-13T15:34:27.498Z; 6ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6419] _id=6ace4e4cde269131f9cf1fea ts=2026-10-13T15:29:16.4440000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6421] _id=6ace4e4cde269131f9cf1fec ts=2026-10-13T15:29:16.4500000Z; 20ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6175] _id=6ac7ba76de269131f9c41d8e ts=2026-10-08T15:44:54.2230000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6179] _id=6ac7ba76de269131f9c41d92 ts=2026-10-08T15:44:54.2430000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 42m 
  - Evidence: 215h 42m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1537] _id=6ac516efde269131f9b4a1e3 ts=2026-10-06T15:42:38.0250000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[9289] _id=6ad0f05cde269131f9dc8698 ts=2026-10-15T15:25:15.8580000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1368] _id=6ac3c689de269131f9ad7613 ts=2026-10-05T15:47:20.0600000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1501] _id=6ac516a1de269131f9b49b8a ts=2026-10-06T15:41:20.6460000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[9302] _id=6ad0f075de269131f9dc88a0 ts=2026-10-15T15:25:40.2330000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10768] _id=6ad23f4fde269131f9e50e16 ts=2026-10-16T15:14:23.0050000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 41m 
  - Evidence: 215h 41m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1538] _id=6ac516efde269131f9b4a1ed ts=2026-10-06T15:42:38.0430000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[9253] _id=6ad0f02cde269131f9dc846f ts=2026-10-15T15:24:27.1840000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1369] _id=6ac3c689de269131f9ad761b ts=2026-10-05T15:47:20.0990000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1486] _id=6ac51690de269131f9b49a42 ts=2026-10-06T15:41:03.0900000Z; 23h 47m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[9303] _id=6ad0f075de269131f9dc88a4 ts=2026-10-15T15:25:40.2530000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10722] _id=6ad23effde269131f9e509f8 ts=2026-10-16T15:13:03.5250000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.036s..0.036s shown 
  - Evidence: 36ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10816] _id=6ad23f79de269131f9e5106e ts=2026-10-16T15:15:05.3660000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10819] _id=6ad23f79de269131f9e51071 ts=2026-10-16T15:15:05.4020000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 53m 
  - Evidence: 191h 53m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[2765] _id=6ac665b6de269131f9bbe045 ts=2026-10-07T15:31:02.1380000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[9259] _id=6ad0f030de269131f9dc84a8 ts=2026-10-15T15:24:31.6500000Z; 23h 52m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1366] _id=6ac3c687de269131f9ad75c7 ts=2026-10-05T15:47:18.3190000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1464] _id=6ac51646de269131f9b49104 ts=2026-10-06T15:39:49.6330000Z; 23h 47m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[9297] _id=6ad0f071de269131f9dc8842 ts=2026-10-15T15:25:36.4420000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10716] _id=6ad23efcde269131f9e509be ts=2026-10-16T15:13:00.2540000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.006s..0.024s shown 
  - Evidence: 6ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10752] _id=6ad23f37de269131f9e50cd6 ts=2026-10-16T15:13:59.5790000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10754] _id=6ad23f37de269131f9e50cd8 ts=2026-10-16T15:13:59.5850000Z; 23ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1320] _id=6ac3c625de269131f9ad6c35 ts=2026-10-05T15:45:40.5630000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1323] _id=6ac3c625de269131f9ad6c3b ts=2026-10-05T15:45:40.5860000Z; 24ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[10730] _id=6ad23f0fde269131f9e50ac0 ts=2026-10-16T15:13:18.7230000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[10732] _id=6ad23f0fde269131f9e50ac2 ts=2026-10-16T15:13:18.7470000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 55m 
  - Evidence: 23h 55m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1344] _id=6ac3c664de269131f9ad717f ts=2026-10-05T15:46:42.9480000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1525] _id=6ac516e3de269131f9b4a0a4 ts=2026-10-06T15:42:26.6860000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5402] _id=6ac7b771de269131f9c3e407 ts=2026-10-08T15:32:01.3330000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6211] _id=6ace4c8ade269131f9cf130f ts=2026-10-13T15:21:46.2930000Z; 24h 21m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1] _id=6ac3bf30de269131f9ace73a ts=2026-10-05T15:15:58.8400000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1384] _id=6ac515b5de269131f9b48578 ts=2026-10-06T15:37:23.8780000Z; 23h 56m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[7118] _id=6acf9aeade269131f9d45c78 ts=2026-10-14T15:08:24.9400000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[8614] _id=6ad0eba2de269131f9dc256e ts=2026-10-15T15:05:05.3800000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5401] _id=6ac7b771de269131f9c3e406 ts=2026-10-08T15:32:01.3330000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6210] _id=6ace4c8ade269131f9cf130e ts=2026-10-13T15:21:46.2930000Z; 24h 21m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[0] _id=6ac3bf2fde269131f9ace735 ts=2026-10-05T15:15:58.8390000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1382] _id=6ac515b5de269131f9b48576 ts=2026-10-06T15:37:23.8770000Z; 23h 44m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1382] _id=6ac515b5de269131f9b48576 ts=2026-10-06T15:37:23.8770000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1806] _id=6ac66379de269131f9bb9f81 ts=2026-10-07T15:21:28.4560000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 144h 5m 
  - Evidence: 144h 5m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[5399] _id=6ac7b753de269131f9c3e0ec ts=2026-10-08T15:31:30.9910000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[8363] _id=6acfa19bde269131f9d4cd07 ts=2026-10-14T15:36:58.2710000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[8578] _id=6acfa2fdde269131f9d4e621 ts=2026-10-14T15:42:52.9220000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[9992] _id=6ad0f4b3de269131f9dcd1ed ts=2026-10-15T15:43:46.4290000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1383] _id=6ac515b4de269131f9b48566 ts=2026-10-05T15:48:00.468Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1804] _id=6ac66378de269131f9bb9f7c ts=2026-10-06T15:47:33.881Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6165] _id=6ac7ba63de269131f9c41cde ts=2026-10-08T15:44:35.0590000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6213] _id=6ace4cd5de269131f9cf1552 ts=2026-10-13T15:23:00.2330000Z; 23h 56m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1790] _id=6ac517ffde269131f9b4bce1 ts=2026-10-06T15:47:09.9970000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[3639] _id=6ac66896de269131f9bc1c9b ts=2026-10-07T15:43:18.1870000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1261] _id=6ac3c5bede269131f9ad6723 ts=2026-10-05T15:43:56.6800000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1395] _id=6ac515c0de269131f9b486d0 ts=2026-10-06T15:37:33.9340000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[6629] _id=6ace4fbcde269131f9cf2dbe ts=2026-10-13T15:35:22.6140000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[6630] _id=6ace4fbcde269131f9cf2dbf ts=2026-10-13T15:35:22.6160000Z; 3ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1271] _id=6ac3c5bede269131f9ad6721 ts=2026-10-05T15:43:56.6770000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1261] _id=6ac3c5bede269131f9ad6723 ts=2026-10-05T15:43:56.6800000Z; 3ms: 6ab9a8bc9a8420a1e6b56b0b.jsonl[1443] _id=6ac51614de269131f9b48cd3 ts=2026-10-06T15:38:58.7440000Z -> 6ab9a8bc9a8420a1e6b56b0b.jsonl[1454] _id=6ac51614de269131f9b48cd6 ts=2026-10-06T15:38:58.7470000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[1245] _id=6ac3c5b3de269131f9ad6675 ts=2026-10-05T15:43:45.9630000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1566] _id=6ac51770de269131f9b4ac51 ts=2026-10-06T15:44:47.5320000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[6487] _id=6ace4eecde269131f9cf254c ts=2026-10-13T15:31:56.0290000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[6616] _id=6ace4f98de269131f9cf2cb6 ts=2026-10-13T15:34:27.498Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[10819] _id=6ad23f79de269131f9e51071 ts=2026-10-16T15:15:05.4020000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[1312] _id=6ac3c61fde269131f9ad6bb5 ts=2026-10-05T15:45:34.2330000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[1323] _id=6ac3c625de269131f9ad6c3b ts=2026-10-05T15:45:40.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[2703] _id=6ac66564de269131f9bbd849 ts=?`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[6215] _id=6ace4cd5de269131f9cf154f ts=?`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[8577] _id=6acfa2fede269131f9d4e623 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 23 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[7526] _id=6acf9c96de269131f9d48038 ts=2026-10-14T15:15:29.2780000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[7574] _id=6acf9c97de269131f9d48046 ts=2026-10-14T15:15:29.8010000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[7639] _id=6acf9cb5de269131f9d481ef ts=2026-10-14T15:16:02.7130000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 164 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[3849] _id=6ac66969de269131f9bc2c71 ts=2026-10-07T15:46:47.9310000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[3852] _id=6ac66969de269131f9bc2c76 ts=2026-10-07T15:46:48.0970000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[3853] _id=6ac66969de269131f9bc2c7a ts=2026-10-07T15:46:48.0970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[1525] _id=6ac516e3de269131f9b4a0a4 ts=2026-10-06T15:42:26.6860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 273 start, 267 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 24 unmatched 'BecameVisible' (totals: 544 open, 520 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 35 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 349 of 12212 adjacent _id pairs reverse in client time; worst 80.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b0b.jsonl[4123] _id=6ac7b62ede269131f9c3b19a ts=2026-10-08T15:26:38.1290000Z`; `6ab9a8bc9a8420a1e6b56b0b.jsonl[4124] _id=6ac7b62fde269131f9c3b1ba ts=2026-10-08T15:25:17.6110000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.93s, min -85764.36s, max -0.18s over 12213 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b0b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
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

### `InputEvent` — 6572 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2610); Unit 1 Dev (2410); Unit 3 Dev (1045); Unit 3 Dungeon Dev (507)
- **Intervals:** median 0.33s (p5 0.00s / p95 4.19s, n=6571)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6572/6572 records)
    "pressed"  x6572
data.actionType  (string, 6572/6572 records)
    "Move"  x4911
    "Interact"  x769
    "Jump"  x372
    "Sprint"  x290
    "Hoverboard"  x73
    "Descend"  x60
    "Ascend"  x55
    "Map"  x20
    "Pause"  x18
    "SkipCinematic"  x4
data.key  (string, 6572/6572 records, 11 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6572/6572 records)
    "Player"  x5462
    "Drone"  x1110
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 1720 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1536); Unit 3 Dungeon Dev (184)
- **Intervals:** median 0.07s (p5 0.00s / p95 1.43s, n=1719)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1720/1720 records)
    "BecameVisible"  x544
    "BecameInvisible"  x520
    "BecameCameraCentered"  x328
    "BecameCameraUncentered"  x328
data.pieceId  (string, 1720/1720 records)
    24 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1720/1720 records)
    1315 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1530 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (802); Unit 3 Dev (381); Unit 1 Dev (216); Unit 3 Dungeon Dev (128); Unit 4 Dev (3)
- **eventKey:** present on 990 of 1530 records
- **Intervals:** median 3.81s (p5 0.01s / p95 25.48s, n=1529)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x990; [conversationId, dialogueEventType] x540
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1530/1530 records)
    numeric range 8 .. 104 (36 unique)
data.dialogueEventType  (string, 1530/1530 records)
    "DialogueNodeEvent"  x990
    "DialogueStartEvent"  x273
    "DialogueFinishEvent"  x267
data.nodeId  (number, 990/1530 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1375 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (659); Unit 1 Dev (346); Unit 3 Dev (274); Unit 3 Dungeon Dev (79); Unit 4 Dev (17)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.26s, n=1369)
- **Fields under `data`:**

```text
data.position  (object, 1375/1375 records)
data.position.x  (number, 1375/1375 records)
    numeric range -677.6 .. 2267.3 (460 unique)
data.position.y  (number, 1375/1375 records)
    numeric range -114.326 .. 159.548 (349 unique)
data.position.z  (number, 1375/1375 records)
    numeric range -1097.87 .. 3720.64 (459 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 435 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (323); Unit 2 Prod (Refactor) (69); Unit 3 Dungeon Dev (32); Unit 3 Dev (11)
- **Intervals:** median 0.26s (p5 0.13s / p95 147.69s, n=434)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 435/435 records)
    20 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 435/435 records)
    53 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 203 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (99); Unit 3 Dev (69); Unit 2 Prod (Refactor) (35)
- **Intervals:** median 0.90s (p5 0.03s / p95 14.64s, n=202)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 203/203 records)
    "argumentationNodeHoverEnd"  x90
    "argumentationNodeHoverStart"  x88
    "argumentationNodeAdd"  x20
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 203/203 records)
    "Unit 3 - Pollution Upstream"  x69
    "Unit 1 - Freshwater"  x56
    "Unit 1 - Argumentation Tutorial"  x43
    "Unit 2 – Watershed"  x35
data.nodeName  (string, 203/203 records)
    "I"  x60
    "A"  x44
    "1"  x43
    "II"  x11
    "2"  x10
    "4"  x10
    "5"  x7
    "3"  x6
    "D"  x6
    "C"  x4
    "B"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 92 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (39); Unit 1 Dev (33); Unit 3 Dev (18); Unit 3 Dungeon Dev (2)
- **Intervals:** median 6.27s (p5 0.04s / p95 42829.23s, n=91)
- **`data` key-set variants:** [actionType, featureUsed] x73; [actionType, featureUsed, location] x16; [actionType, featureUsed, legendName] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 92/92 records)
    "MapCloseEvent"  x37
    "MapOpenEvent"  x36
    "WaypointMoveEvent"  x9
    "WaypointSetEvent"  x6
    "Selected"  x2
    "Unselected"  x1
    "WaypointResetEvent"  x1
data.featureUsed  (string, 92/92 records)
    "Map"  x73
    "Waypoint"  x16
    "Legend"  x3
data.legendName  (string, 3/92 records)
    "Toppo's Room"  x3
data.location  (object, 16/92 records)
data.location.x  (number, 16/92 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 16/92 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 16/92 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 64 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (50); Unit 3 Dev (14)
- **Intervals:** median 1.53s (p5 0.18s / p95 31.50s, n=63)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x60; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/64 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/64 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
data.actionType  (string, 60/64 records)
    "LeftDrag"  x32
    "RightDrag"  x28
data.currentSoilType  (string, 60/64 records)
    "CLAY"  x10
    "CLAYSAND"  x10
    "SANDGRAVEL"  x10
    "CLAYROCK"  x9
    "SAND"  x9
    "GRAVEL"  x7
    "BEDROCK"  x5
data.isCorrectSelection  (string, 60/64 records)
    "false"  x49
    "true"  x11
data.waterLevelStatus  (string, 60/64 records)
    "TooLow"  x21
    "TooHigh"  x20
    "Proper"  x19
data.waterRetentionChange  (string, 60/64 records)
    "Increase"  x26
    "Decrease"  x23
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 54 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 1 Dev (15); Unit 3 Dev (12); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 54 of 54 records
- **Intervals:** median 150.82s (p5 0.00s / p95 85633.27s, n=53)
- **`data` key-set variants:** [questEventType, questID, questName] x35; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 54/54 records)
    "questActiveEvent"  x35
    "questFinishEvent"  x19
data.questID  (string, 54/54 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 54/54 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/54 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DaniEvent` — 48 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (46); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.14s (p5 0.01s / p95 60.37s, n=47)
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "Close"  x24
    "Open"  x24
data.toolName  (string, 48/48 records, 44 empty-string)
    ""  x44
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (8); Unit 1 Dev (4); Unit 3 Dev (3); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 104.97s (p5 8.37s / p95 87086.62s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 26 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (5); Unit 1 Dev (3); Unit 3 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 680.68s (p5 4.26s / p95 87236.95s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 17 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 530.01s (p5 4.15s / p95 194521.95s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    false  x17
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 43629.41s (p5 133.44s / p95 207980.01s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 46.45s (p5 8.80s / p95 396741.76s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationAnswerEvent` — 9 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 87.12s (p5 18.23s / p95 534876.80s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "submitAnswerEvent"  x9
data.answerSubmitted  (string, 9/9 records)
    "A,1,I"  x4
    "A,1,"  x1
    "A,1,II"  x1
    "A,2,I"  x1
    "A,5,I"  x1
    "D,1,II"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (6)
- **Intervals:** median 4.17s (p5 2.26s / p95 233.50s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.chatID  (string, 6/6 records)
    "NA"  x3
    "[]"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time."  x1
    "The root document of this element is not valid for pointer lock."  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 3 empty-string)
    ""  x3
    "NotAllowedError: Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time.
    at requestPointerLock (blob:https://mhs.adroit.games/9ba1841f-c663-4e14-ac8d-b1694628902c:9:213829)
    at Object.runDeferredCalls (blob:https://mhs.adroit.games/9ba1841f-c663-4e14-ac8d-b1694628902c:9:204819)
    at HTMLCanvasElement.jsEventHandler (blob:https://mhs.adroit.games/9ba1841f-c663-4e14-ac8d-b1694628902c:9:205513)"  x1
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x2
    "unit1"  x1
    "unit3"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 87246.80s (p5 87246.80s / p95 87246.80s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 86143.74s (p5 86143.74s / p95 86143.74s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Freshwater"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - "  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (50 records)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "Unselected" (1x); "WaypointMoveEvent" (9x); "WaypointResetEvent" (1x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (3x); "Waypoint" (16x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*