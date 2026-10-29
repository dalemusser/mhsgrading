# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b03

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b03
- **Game version string(s) in log:** 2.8.9, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b03.jsonl
- **Records:** 12112 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b03
- **Time span:** 2026-10-05T15:15:59.403000+00:00 .. 2026-10-19T12:30:03.119000+00:00 (333h 14m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b03\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 12112 records, 9 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 104 INFO, 2 NOT_TESTED, 85 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4819 | 39.79 | 1 | 7 | 0 | 2026-10-05T15:19:27.069000+00:00 | 2026-10-19T12:29:40.490000+00:00 | 333h 10m |
| PuzzlePieceVisibleEvent | 2844 | 23.48 | 1 | 3 | 0 | 2026-10-06T15:31:39.005000+00:00 | 2026-10-19T02:01:37.247000+00:00 | 298h 29m |
| PlayerPositionEvent | 1737 | 14.34 | 1 | 7 | 0 | 2026-10-05T15:16:08.826000+00:00 | 2026-10-19T12:29:58.278000+00:00 | 333h 13m |
| DialogueEvent | 1583 | 13.07 | 1 | 7 | 964 | 2026-10-05T15:16:28.694000+00:00 | 2026-10-19T12:30:03.119000+00:00 | 333h 13m |
| ObjectInterEvent | 294 | 2.43 | 1 | 7 | 0 | 2026-10-05T15:21:53.432000+00:00 | 2026-10-19T12:29:45.749000+00:00 | 333h 7m |
| argumentationNodeEvent | 267 | 2.2 | 1 | 4 | 0 | 2026-10-05T15:40:02.187000+00:00 | 2026-10-19T12:13:24.946000+00:00 | 332h 33m |
| TopographicMapEvent | 178 | 1.47 | 1 | 3 | 0 | 2026-10-06T15:32:08.647000+00:00 | 2026-10-15T15:29:14.957000+00:00 | 215h 57m |
| Soil Key Puzzle | 109 | 0.9 | 1 | 2 | 0 | 2026-10-14T15:41:15.114000+00:00 | 2026-10-19T02:02:50.079000+00:00 | 106h 21m |
| questEvent | 59 | 0.49 | 1 | 7 | 59 | 2026-10-05T15:16:28.668000+00:00 | 2026-10-19T12:29:52.318000+00:00 | 333h 13m |
| argumentationAnswerEvent | 46 | 0.38 | 1 | 3 | 0 | 2026-10-05T15:40:22.077000+00:00 | 2026-10-19T12:13:29.953000+00:00 | 332h 33m |
| DEBUGMenu | 42 | 0.35 | 1 | 8 | 0 | 2026-10-05T15:16:08.808000+00:00 | 2026-10-19T12:14:23.408000+00:00 | 332h 58m |
| gameWindowFocusEvent | 26 | 0.21 | 1 | 4 | 0 | 2026-10-05T15:15:59.403000+00:00 | 2026-10-19T11:57:49.108000+00:00 | 332h 41m |
| DaniEvent | 25 | 0.21 | 1 | 2 | 0 | 2026-10-06T15:36:22.081000+00:00 | 2026-10-13T15:36:55.565000+00:00 | 168h 0m |
| gameStartEvent | 20 | 0.17 | 1 | 1 | 0 | 2026-10-05T15:15:59.405000+00:00 | 2026-10-19T11:57:49.108000+00:00 | 332h 41m |
| soilMachine | 17 | 0.14 | 1 | 1 | 0 | 2026-10-15T15:32:58.378000+00:00 | 2026-10-15T15:43:09.733000+00:00 | 10m 11s |
| TerasGardenBox | 13 | 0.11 | 1 | 1 | 0 | 2026-10-19T12:18:26.099000+00:00 | 2026-10-19T12:20:36.700000+00:00 | 2m 10s |
| gameWindowUnfocusEvent | 13 | 0.11 | 1 | 5 | 0 | 2026-10-05T15:48:12.596000+00:00 | 2026-10-19T11:54:39.220000+00:00 | 332h 6m |
| argumentationEvent | 10 | 0.08 | 1 | 3 | 0 | 2026-10-05T15:39:55.568000+00:00 | 2026-10-19T12:13:30.003000+00:00 | 332h 33m |
| argumentationToolEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-05T15:39:55.490000+00:00 | 2026-10-14T15:36:48.982000+00:00 | 215h 56m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-10-05T15:45:02.949000+00:00 | 2026-10-19T12:30:03.091000+00:00 | 332h 45m |
| chatEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-13T15:36:55.818000+00:00 | 2026-10-13T15:37:02.412000+00:00 | 6.6s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 160.449s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 598950.071s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.081s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.891s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.014s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.844s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 6.594s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 881.48s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 84951.893s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.244s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.5x vs baseline. 
  - Observed: 42 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 25 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to Insert; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Watershed Piece 1; WatershedSlotWall 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 Prod (Refactor) 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 9.2x vs baseline. 
  - Observed: 46 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,II; A,3,I; A,4,II; A,B,D,2,I; A,B,D,2,II; A,D,2,II; A,D,B,2,II; B,2,II; B,3,I; C,2,II; C,D,A,2,II; D,2,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [11-226, 11-23, 11-24, 11-25, 11-25] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 22; 24; 25; 43; 44; 45; 51; 52; 53; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.4x vs baseline. 
  - Observed: 17 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[175] _id=6ac3c117de269131f9ad1d5f ts=2026-10-05T15:24:07.0440000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[228] _id=6ac3c20cde269131f9ad2ec1 ts=2026-10-05T15:28:11.8500000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[273] _id=6ac3c2b8de269131f9ad37bb ts=2026-10-05T15:31:03.9470000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[3] _id=6ac3bf30de269131f9ace739 ts=2026-10-05T15:15:59.4050000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[560] _id=6ac3c659de269131f9ad708d ts=2026-10-05T15:46:32.9740000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[595] _id=6ac51365de269131f9b45d43 ts=2026-10-06T15:27:32.2650000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[5] _id=6ac3bf2fde269131f9ace737 ts=2026-10-05T15:15:59.4030000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[559] _id=6ac3c659de269131f9ad7083 ts=2026-10-05T15:46:32.9730000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[594] _id=6ac51365de269131f9b45d41 ts=2026-10-06T15:27:32.2640000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[593] _id=6ac51364de269131f9b45d3d ts=2026-10-05T15:48:12.596Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[2379] _id=6ac662fcde269131f9bb9a91 ts=2026-10-06T15:47:46.642Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[3655] _id=6ac7b528de269131f9c3932d ts=2026-10-07T15:47:21.627Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 178 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[755] _id=6ac51479de269131f9b46b9d ts=2026-10-06T15:32:08.6470000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[774] _id=6ac5147cde269131f9b46be1 ts=2026-10-06T15:32:11.6100000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[784] _id=6ac51493de269131f9b46d59 ts=2026-10-06T15:32:34.2600000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4818 | 0.0 | 0.834 | 248.944 | 11.401 | 429632.681 | 0.24 | 97 | 11 |
| PuzzlePieceVisibleEvent | 2843 | 0.0 | 0.081 | 377.98 | 2.358 | 605879.19 | 0.16 | 1124 | 7 |
| PlayerPositionEvent | 1727 | 9.768 | 10.003 | 666.32 | 11.548 | 429605.525 | 0.09 | 0 | 9 |
| DialogueEvent | 1582 | 0.0 | 4.115 | 758.29 | 35.924 | 429636.724 | 0.08 | 446 | 12 |
| ObjectInterEvent | 293 | 0.0 | 10.528 | 4093.08 | 320.821 | 430234.566 | 0.01 | 4 | 13 |
| argumentationNodeEvent | 266 | 0.023 | 0.579 | 4500.762 | 17.313 | 604358.206 | 0.01 | 35 | 3 |
| TopographicMapEvent | 177 | 0.586 | 3.891 | 4392.239 | 349.532 | 430297.016 | 0.01 | 0 | 8 |
| Soil Key Puzzle | 108 | 0.001 | 0.762 | 3545.324 | 12.572 | 298311.663 | 0.02 | 2 | 2 |
| questEvent | 58 | 0.002 | 239.251 | 20682.822 | 85968.473 | 429858.448 | 0.0 | 8 | 16 |
| argumentationAnswerEvent | 45 | 0.22 | 7.014 | 26604.175 | 67.969 | 777248.039 | 0.0 | 0 | 2 |
| DEBUGMenu | 41 | 7.696 | 160.449 | 29236.454 | 86561.554 | 429977.312 | 0.0 | 0 | 17 |
| gameWindowFocusEvent | 25 | 36.007 | 881.48 | 47908.388 | 254111.386 | 429986.007 | 0.0 | 0 | 13 |
| DaniEvent | 24 | 1.233 | 21.286 | 25201.395 | 86561.696 | 431422.41 | 0.0 | 0 | 3 |
| gameStartEvent | 19 | 36.007 | 3569.232 | 63037.353 | 310188.337 | 429986.007 | 0.0 | 0 | 12 |
| soilMachine | 16 | 0.954 | 3.244 | 38.21 | 159.34 | 231.129 | 1.57 | 0 | 0 |
| TerasGardenBox | 12 | 1.545 | 6.038 | 10.883 | 30.674 | 31.688 | 5.51 | 0 | 0 |
| gameWindowUnfocusEvent | 12 | 58.667 | 84951.893 | 99632.219 | 376099.67 | 430215.474 | 0.0 | 0 | 9 |
| argumentationEvent | 9 | 0.031 | 39.07 | 133023.826 | 634046.451 | 777218.026 | 0.0 | 2 | 2 |
| argumentationToolEvent | 3 | 0.341 | 2.844 | 259137.831 | 699669.561 | 777410.307 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 384990.225 | 598950.071 | 598950.071 | 791513.932 | 812909.917 | 0.0 | 0 | 2 |
| chatEvent | 1 | 6.594 | 6.594 | 6.594 | 6.594 | 6.594 | 9.1 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 5 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[10730] _id=6ad0f586de269131f9dcddf9 ts=2026-10-15T15:47:17.4810000Z == 6ab9a8bc9a8420a1e6b56b03.jsonl[10731] _id=6ad0f586de269131f9dcddfa ts=2026-10-15T15:47:17.4810000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[11236] _id=6ad605cade269131f9e963a4 ts=2026-10-19T11:58:01.2690000Z == 6ab9a8bc9a8420a1e6b56b03.jsonl[11237] _id=6ad605cade269131f9e963a5 ts=2026-10-19T11:58:01.2690000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[11374] _id=6ad60681de269131f9e96454 ts=2026-10-19T12:01:04.8690000Z == 6ab9a8bc9a8420a1e6b56b03.jsonl[11375] _id=6ad60681de269131f9e96455 ts=2026-10-19T12:01:04.8690000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 43 group(s), 56 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[632] _id=6ac514eede269131f9b47399 ts=2026-10-06T15:31:44.5470000Z == 6ab9a8bc9a8420a1e6b56b03.jsonl[633] _id=6ac514eede269131f9b4739b ts=2026-10-06T15:31:44.5470000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[636] _id=6ac514eede269131f9b473af ts=2026-10-06T15:31:44.5470000Z == 6ab9a8bc9a8420a1e6b56b03.jsonl[719] _id=6ac514eede269131f9b473b7 ts=2026-10-06T15:31:44.5470000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[828] _id=6ac514dede269131f9b47259 ts=2026-10-06T15:33:48.5320000Z == 6ab9a8bc9a8420a1e6b56b03.jsonl[829] _id=6ac514dede269131f9b47267 ts=2026-10-06T15:33:48.5320000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 18 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[130] _id=6ac3c091de269131f9ad0d25 ts=2026-10-05T15:21:53.4320000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[131] _id=6ac3c092de269131f9ad0d2b ts=2026-10-05T15:21:53.4370000Z`; `400ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[673] _id=6ac51408de269131f9b4648d ts=2026-10-06T15:30:16.1380000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[675] _id=6ac51409de269131f9b46499 ts=2026-10-06T15:30:16.5380000Z`; `412ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[677] _id=6ac5140ade269131f9b464b1 ts=2026-10-06T15:30:17.8890000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[682] _id=6ac5140ade269131f9b464c1 ts=2026-10-06T15:30:18.3010000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 225 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `75ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[631] _id=6ac514edde269131f9b47385 ts=2026-10-06T15:31:43.0890000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[630] _id=6ac514edde269131f9b4738b ts=2026-10-06T15:31:43.1640000Z`; `617ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[858] _id=6ac514f1de269131f9b47425 ts=2026-10-06T15:33:06.7030000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[857] _id=6ac514f1de269131f9b47427 ts=2026-10-06T15:33:07.3200000Z`; `242ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[816] _id=6ac514d5de269131f9b471a9 ts=2026-10-06T15:33:39.3600000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[810] _id=6ac514d5de269131f9b471b5 ts=2026-10-06T15:33:39.6020000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `585ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7468] _id=6acfa2b5de269131f9d4e1c0 ts=2026-10-14T15:41:40.4610000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7473] _id=6acfa2b5de269131f9d4e1d8 ts=2026-10-14T15:41:41.0460000Z`; `978ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7471] _id=6acfa2b5de269131f9d4e1cd ts=2026-10-14T15:41:40.8470000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7472] _id=6acfa2b6de269131f9d4e1f1 ts=2026-10-14T15:41:41.8250000Z`; `209ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7533] _id=6acfa314de269131f9d4e6f7 ts=2026-10-14T15:43:15.4030000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7535] _id=6acfa314de269131f9d4e6fc ts=2026-10-14T15:43:15.6120000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `713ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[6047] _id=6acf9c30de269131f9d478ef ts=2026-10-14T15:13:51.9430000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[6037] _id=6acf9c31de269131f9d478f7 ts=2026-10-14T15:13:52.6560000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `733ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7260] _id=6acfa15fde269131f9d4c7e4 ts=2026-10-14T15:35:58.6610000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7236] _id=6acfa160de269131f9d4c805 ts=2026-10-14T15:35:59.3940000Z`; `782ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7236] _id=6acfa160de269131f9d4c805 ts=2026-10-14T15:35:59.3940000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7206] _id=6acfa161de269131f9d4c822 ts=2026-10-14T15:36:00.1760000Z`; `680ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7206] _id=6acfa161de269131f9d4c822 ts=2026-10-14T15:36:00.1760000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7257] _id=6acfa161de269131f9d4c82e ts=2026-10-14T15:36:00.8560000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7303] _id=6acfa197de269131f9d4cc95 ts=2026-10-14T15:36:54.6650000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[7310] _id=6acfa197de269131f9d4cc98 ts=2026-10-14T15:36:54.7010000Z`; `31ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11785] _id=6ad6096ade269131f9e9676f ts=2026-10-19T12:13:29.9720000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[11788] _id=6ad6096ade269131f9e96772 ts=2026-10-19T12:13:30.0030000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `71ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[409] _id=6ac3c4d3de269131f9ad59b5 ts=2026-10-05T15:40:02.7130000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[405] _id=6ac3c4d3de269131f9ad59b9 ts=2026-10-05T15:40:02.7840000Z`; `432ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[408] _id=6ac3c4e2de269131f9ad5a55 ts=2026-10-05T15:40:17.6260000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[417] _id=6ac3c4e2de269131f9ad5a5f ts=2026-10-05T15:40:18.0580000Z`; `76ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[430] _id=6ac3c51fde269131f9ad5ced ts=2026-10-05T15:41:18.5370000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[431] _id=6ac3c51fde269131f9ad5cef ts=2026-10-05T15:41:18.6130000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `954ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[10418] _id=6ad0f38dde269131f9dcbf6b ts=2026-10-15T15:38:52.8640000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[10415] _id=6ad0f38ede269131f9dcbf78 ts=2026-10-15T15:38:53.8180000Z`; `995ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[10481] _id=6ad0f3d9de269131f9dcc543 ts=2026-10-15T15:40:08.2670000Z ~ 6ab9a8bc9a8420a1e6b56b03.jsonl[10482] _id=6ad0f3dade269131f9dcc56e ts=2026-10-15T15:40:09.2620000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4177] _id=6ac7b918de269131f9c40dd0 ts=2026-10-08T15:39:04.3200000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4311] _id=6ace48b1de269131f9cf0400 ts=2026-10-13T15:05:21.6320000Z; 82h 13m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10604] _id=6ad0f4cede269131f9dcd344 ts=2026-10-15T15:44:13.8890000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10764] _id=6ad5790dde269131f9e926a0 ts=2026-10-19T01:57:33.2930000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b03.jsonl[2383] _id=6ac66307de269131f9bb9ace ts=2026-10-07T15:19:34.7780000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3656] _id=6ac7b528de269131f9c39333 ts=2026-10-08T15:22:16.3320000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4211] _id=6ac7b9a9de269131f9c415c6 ts=2026-10-08T15:41:29.4630000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4867] _id=6ace4ee8de269131f9cf2530 ts=2026-10-13T15:31:51.8730000Z; 24h 6m: 6ab9a8bc9a8420a1e6b56b03.jsonl[1293] _id=6ac5157dde269131f9b47f88 ts=2026-10-06T15:36:29.1470000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3469] _id=6ac66869de269131f9bc1aa3 ts=2026-10-07T15:42:32.4680000Z; 23h 43m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3480] _id=6ac66876de269131f9bc1b37 ts=2026-10-07T15:42:46.1590000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3926] _id=6ac7b621de269131f9c3afb2 ts=2026-10-08T15:26:25.3110000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4307] _id=6ac7ba8dde269131f9c41e9b ts=2026-10-08T15:45:17.4650000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4321] _id=6ace48d2de269131f9cf049f ts=2026-10-13T15:05:54.1890000Z; 82h 12m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10678] _id=6ad0f56fde269131f9dcdc7d ts=2026-10-15T15:46:54.7330000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10816] _id=6ad57963de269131f9e9279a ts=2026-10-19T01:58:59.7970000Z; 23h 41m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3588] _id=6ac66941de269131f9bc28d4 ts=2026-10-07T15:46:09.0490000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3972] _id=6ac7b672de269131f9c3bed8 ts=2026-10-08T15:27:46.5000000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 446 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11491] _id=6ad607aade269131f9e96574 ts=2026-10-19T12:06:02.4420000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11492] _id=6ad607aade269131f9e96575 ts=2026-10-19T12:06:02.4420000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11613] _id=6ad6084ade269131f9e9661a ts=2026-10-19T12:08:41.6840000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11614] _id=6ad6084ade269131f9e9661b ts=2026-10-19T12:08:41.6840000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11648] _id=6ad60899de269131f9e9667c ts=2026-10-19T12:10:01.0070000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11649] _id=6ad60899de269131f9e9667d ts=2026-10-19T12:10:01.0070000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 225h 48m 
  - Evidence: 225h 48m: 6ab9a8bc9a8420a1e6b56b03.jsonl[556] _id=6ac3c5ffde269131f9ad6a09 ts=2026-10-05T15:45:02.9490000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[9044] _id=6ad02d6dde269131f9da1047 ts=2026-10-15T01:33:32.8660000Z; 106h 56m: 6ab9a8bc9a8420a1e6b56b03.jsonl[9044] _id=6ad02d6dde269131f9da1047 ts=2026-10-15T01:33:32.8660000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[12104] _id=6ad60d4bde269131f9e96a01 ts=2026-10-19T12:30:03.0910000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4304] _id=6ac7ba8bde269131f9c41e70 ts=2026-10-08T15:45:14.7090000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4315] _id=6ace48cbde269131f9cf047c ts=2026-10-13T15:05:47.3900000Z; 82h 11m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10757] _id=6ad0f588de269131f9dcde43 ts=2026-10-15T15:47:19.8050000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10774] _id=6ad57948de269131f9e92714 ts=2026-10-19T01:58:31.8790000Z; 23h 40m: 6ab9a8bc9a8420a1e6b56b03.jsonl[568] _id=6ac3c677de269131f9ad73b5 ts=2026-10-05T15:47:02.7420000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[598] _id=6ac51376de269131f9b45d9f ts=2026-10-06T15:27:48.7510000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 97 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[10730] _id=6ad0f586de269131f9dcddf9 ts=2026-10-15T15:47:17.4810000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10731] _id=6ad0f586de269131f9dcddfa ts=2026-10-15T15:47:17.4810000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11236] _id=6ad605cade269131f9e963a4 ts=2026-10-19T11:58:01.2690000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11237] _id=6ad605cade269131f9e963a5 ts=2026-10-19T11:58:01.2690000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11237] _id=6ad605cade269131f9e963a5 ts=2026-10-19T11:58:01.2690000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11238] _id=6ad605cade269131f9e963a6 ts=2026-10-19T11:58:01.2690000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4299] _id=6ac7ba7fde269131f9c41dff ts=2026-10-08T15:45:03.5130000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4383] _id=6ace4b1ade269131f9cf0b9a ts=2026-10-13T15:15:38.0790000Z; 82h 14m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10625] _id=6ad0f4e0de269131f9dcd454 ts=2026-10-15T15:44:31.4570000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10793] _id=6ad57956de269131f9e9275a ts=2026-10-19T01:58:46.5100000Z; 24h 17m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3038] _id=6ac6648ede269131f9bbbbbb ts=2026-10-07T15:26:05.4180000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4258] _id=6ac7ba39de269131f9c41bac ts=2026-10-08T15:43:53.0660000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11110] _id=6ad60578de269131f9e96354 ts=2026-10-19T11:56:40.2370000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11111] _id=6ad60578de269131f9e96355 ts=2026-10-19T11:56:40.2370000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11343] _id=6ad60656de269131f9e96424 ts=2026-10-19T12:00:22.3790000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11344] _id=6ad60656de269131f9e96425 ts=2026-10-19T12:00:22.3790000Z; 1ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11392] _id=6ad606c0de269131f9e964a1 ts=2026-10-19T12:02:07.8150000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11393] _id=6ad606c0de269131f9e964a2 ts=2026-10-19T12:02:07.8160000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4308] _id=6ac7ba97de269131f9c41ec9 ts=2026-10-08T15:45:27.0790000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4319] _id=6ace48bfde269131f9cf0450 ts=2026-10-13T15:05:32.6040000Z; 82h 10m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10758] _id=6ad0f592de269131f9dcde8a ts=2026-10-15T15:47:29.7250000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10767] _id=6ad5791ade269131f9e926b3 ts=2026-10-19T01:57:43.6500000Z; 23h 39m: 6ab9a8bc9a8420a1e6b56b03.jsonl[570] _id=6ac3c6b5de269131f9ad788f ts=2026-10-05T15:48:04.9550000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[597] _id=6ac51376de269131f9b45d9d ts=2026-10-06T15:27:46.2950000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 168h 17m 
  - Evidence: 168h 17m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3050] _id=6ac6648fde269131f9bbbbf0 ts=2026-10-07T15:26:05.4600000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7566] _id=6acfa346de269131f9d4e92c ts=2026-10-14T15:44:04.6500000Z; 82h 11m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10756] _id=6ad0f588de269131f9dcde34 ts=2026-10-15T15:47:17.4760000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10785] _id=6ad5794cde269131f9e9271e ts=2026-10-19T01:58:35.7000000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b03.jsonl[1725] _id=6ac517f1de269131f9b4bc19 ts=2026-10-06T15:46:55.2910000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[2436] _id=6ac66380de269131f9bba030 ts=2026-10-07T15:21:35.3530000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1124 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[1025] _id=6ac5151cde269131f9b477a1 ts=2026-10-06T15:34:50.4650000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[1026] _id=6ac5151dde269131f9b477a5 ts=2026-10-06T15:34:50.4650000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[1043] _id=6ac51528de269131f9b47850 ts=2026-10-06T15:35:02.0690000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[1069] _id=6ac51528de269131f9b47855 ts=2026-10-06T15:35:02.0690000Z; 0ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[1044] _id=6ac5151fde269131f9b477cd ts=2026-10-06T15:34:53.6920000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[1035] _id=6ac51520de269131f9b477cf ts=2026-10-06T15:34:53.6920000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 82h 51m 
  - Evidence: 82h 51m: 6ab9a8bc9a8420a1e6b56b03.jsonl[9151] _id=6ad0ed01de269131f9dc4d82 ts=2026-10-15T15:10:56.4200000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10922] _id=6ad57a48de269131f9e92a66 ts=2026-10-19T02:02:48.0830000Z; 23h 22m: 6ab9a8bc9a8420a1e6b56b03.jsonl[7553] _id=6acfa31cde269131f9d4e74f ts=2026-10-14T15:43:23.5720000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[9060] _id=6ad0ebbfde269131f9dc287c ts=2026-10-15T15:05:34.8500000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7533] _id=6acfa314de269131f9d4e6f7 ts=2026-10-14T15:43:15.4030000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7534] _id=6acfa314de269131f9d4e6f8 ts=2026-10-14T15:43:15.4040000Z; 1ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7535] _id=6acfa314de269131f9d4e6fc ts=2026-10-14T15:43:15.6120000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7536] _id=6acfa314de269131f9d4e6fd ts=2026-10-14T15:43:15.6130000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4254] _id=6ac7ba33de269131f9c41b73 ts=2026-10-08T15:43:47.0940000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4372] _id=6ace4b0cde269131f9cf0b51 ts=2026-10-13T15:15:24.1100000Z; 23h 45m: 6ab9a8bc9a8420a1e6b56b03.jsonl[1290] _id=6ac5157cde269131f9b47f64 ts=2026-10-06T15:36:27.9070000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[2438] _id=6ac66394de269131f9bba1fd ts=2026-10-07T15:21:55.9130000Z; 23h 41m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3543] _id=6ac6690cde269131f9bc24d2 ts=2026-10-07T15:45:16.1610000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3929] _id=6ac7b624de269131f9c3affa ts=2026-10-08T15:26:27.7880000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 54m 
  - Evidence: 215h 54m: 6ab9a8bc9a8420a1e6b56b03.jsonl[463] _id=6ac3c53fde269131f9ad5e4f ts=2026-10-05T15:41:50.6220000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7260] _id=6acfa15fde269131f9d4c7e4 ts=2026-10-14T15:35:58.6610000Z; 116h 29m: 6ab9a8bc9a8420a1e6b56b03.jsonl[7305] _id=6acfa197de269131f9d4cc92 ts=2026-10-14T15:36:54.6360000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11503] _id=6ad607aade269131f9e96572 ts=2026-10-19T12:06:02.4130000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 53m 
  - Evidence: 215h 53m: 6ab9a8bc9a8420a1e6b56b03.jsonl[464] _id=6ac3c53fde269131f9ad5e51 ts=2026-10-05T15:41:50.6470000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7222] _id=6acfa141de269131f9d4c51d ts=2026-10-14T15:35:28.6730000Z; 116h 28m: 6ab9a8bc9a8420a1e6b56b03.jsonl[7310] _id=6acfa197de269131f9d4cc98 ts=2026-10-14T15:36:54.7010000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11460] _id=6ad60770de269131f9e96525 ts=2026-10-19T12:05:03.7900000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.036s shown 
  - Evidence: 31ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11785] _id=6ad6096ade269131f9e9676f ts=2026-10-19T12:13:29.9720000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11788] _id=6ad6096ade269131f9e96772 ts=2026-10-19T12:13:30.0030000Z; 36ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7303] _id=6acfa197de269131f9d4cc95 ts=2026-10-14T15:36:54.6650000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7310] _id=6acfa197de269131f9d4cc98 ts=2026-10-14T15:36:54.7010000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 52m 
  - Evidence: 167h 52m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3473] _id=6ac66871de269131f9bc1b08 ts=2026-10-07T15:42:41.0020000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7213] _id=6acfa138de269131f9d4c461 ts=2026-10-14T15:35:19.2080000Z; 116h 28m: 6ab9a8bc9a8420a1e6b56b03.jsonl[7292] _id=6acfa185de269131f9d4cb35 ts=2026-10-14T15:36:36.6320000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11453] _id=6ad60767de269131f9e9651b ts=2026-10-19T12:04:55.3590000Z; 48h 1m: 6ab9a8bc9a8420a1e6b56b03.jsonl[454] _id=6ac3c52cde269131f9ad5d75 ts=2026-10-05T15:41:32.2880000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3470] _id=6ac6686ede269131f9bc1ade ts=2026-10-07T15:42:37.6810000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 35 interval(s) ≤ 0.023s..0.026s shown 
  - Evidence: 23ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11568] _id=6ad60813de269131f9e965da ts=2026-10-19T12:07:47.5660000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11569] _id=6ad60813de269131f9e965dc ts=2026-10-19T12:07:47.5890000Z; 25ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[7231] _id=6acfa148de269131f9d4c5d7 ts=2026-10-14T15:35:36.0090000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7228] _id=6acfa148de269131f9d4c5d9 ts=2026-10-14T15:35:36.0340000Z; 26ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[11477] _id=6ad6079ade269131f9e9654e ts=2026-10-19T12:05:46.3700000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11485] _id=6ad6079ade269131f9e96550 ts=2026-10-19T12:05:46.3960000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 56m 
  - Evidence: 215h 56m: 6ab9a8bc9a8420a1e6b56b03.jsonl[404] _id=6ac3c4ccde269131f9ad593d ts=2026-10-05T15:39:55.8310000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[7300] _id=6acfa18ede269131f9d4cbd6 ts=2026-10-14T15:36:46.1380000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4176] _id=6ac7b910de269131f9c40d5f ts=2026-10-08T15:38:55.7780000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4313] _id=6ace48b2de269131f9cf0403 ts=2026-10-13T15:05:21.7850000Z; 82h 27m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10148] _id=6ad0f160de269131f9dc9a75 ts=2026-10-15T15:29:35.9770000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10762] _id=6ad5790dde269131f9e926a3 ts=2026-10-19T01:57:33.4620000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b03.jsonl[2382] _id=6ac662fcde269131f9bb9a95 ts=2026-10-07T15:19:23.5810000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3658] _id=6ac7b528de269131f9c39335 ts=2026-10-08T15:22:16.4910000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4173] _id=6ac7b910de269131f9c40d5e ts=2026-10-08T15:38:55.7780000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4312] _id=6ace48b2de269131f9cf0402 ts=2026-10-13T15:05:21.7850000Z; 82h 13m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10611] _id=6ad0f4d2de269131f9dcd38f ts=2026-10-15T15:44:17.4570000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10761] _id=6ad5790dde269131f9e926a2 ts=2026-10-19T01:57:33.4620000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b03.jsonl[2381] _id=6ac662fcde269131f9bb9a94 ts=2026-10-07T15:19:23.5800000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[3657] _id=6ac7b528de269131f9c39334 ts=2026-10-08T15:22:16.4900000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4171] _id=6ac7b8f4de269131f9c40ba9 ts=2026-10-08T15:38:28.2580000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4360] _id=6ace497cde269131f9cf0747 ts=2026-10-13T15:08:43.7320000Z; 92h 10m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10610] _id=6ad0f4d1de269131f9dcd374 ts=2026-10-15T15:44:16.1160000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[11138] _id=6ad604ffde269131f9e962b5 ts=2026-10-19T11:54:39.2200000Z; 24h 30m: 6ab9a8bc9a8420a1e6b56b03.jsonl[6051] _id=6acf9c37de269131f9d4795e ts=2026-10-14T15:13:58.1210000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10610] _id=6ad0f4d1de269131f9dcd374 ts=2026-10-15T15:44:16.1160000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 24m 
  - Evidence: 119h 24m: 6ab9a8bc9a8420a1e6b56b03.jsonl[4204] _id=6ac7b99cde269131f9c414e2 ts=2026-10-08T15:41:16.4880000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4320] _id=6ace48bfde269131f9cf0451 ts=2026-10-13T15:05:34.9360000Z; 82h 10m: 6ab9a8bc9a8420a1e6b56b03.jsonl[10687] _id=6ad0f56dde269131f9dcdc5d ts=2026-10-15T15:46:52.3170000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10768] _id=6ad5791ade269131f9e926b4 ts=2026-10-19T01:57:45.5570000Z; 24h 6m: 6ab9a8bc9a8420a1e6b56b03.jsonl[3229] _id=6ac666adde269131f9bbfc43 ts=2026-10-07T15:35:09.1680000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[4204] _id=6ac7b99cde269131f9c414e2 ts=2026-10-08T15:41:16.4880000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[373] _id=6ac3c472de269131f9ad5296 ts=2026-10-05T15:38:25.6800000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[380] _id=6ac3c472de269131f9ad529d ts=2026-10-05T15:38:25.6820000Z; 5ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[10389] _id=6ad0f35cde269131f9dcbd33 ts=2026-10-15T15:38:03.7540000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10390] _id=6ad0f35cde269131f9dcbd35 ts=2026-10-15T15:38:03.7590000Z; 6ms: 6ab9a8bc9a8420a1e6b56b03.jsonl[10011] _id=6ad0f02cde269131f9dc8478 ts=2026-10-15T15:24:27.8510000Z -> 6ab9a8bc9a8420a1e6b56b03.jsonl[10012] _id=6ad0f02cde269131f9dc847a ts=2026-10-15T15:24:27.8570000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[365] _id=6ac3c450de269131f9ad4ffd ts=2026-10-05T15:37:51.5440000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[469] _id=6ac3c557de269131f9ad5f7b ts=2026-10-05T15:42:15.0280000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[4471] _id=6ace4bdcde269131f9cf0f18 ts=2026-10-13T15:18:51.9690000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 42 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[1035] _id=6ac51520de269131f9b477cf ts=2026-10-06T15:34:53.6920000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[1051] _id=6ac51526de269131f9b4781d ts=2026-10-06T15:35:00.4640000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[1052] _id=6ac51526de269131f9b4781f ts=2026-10-06T15:35:00.5160000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 124 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[630] _id=6ac514edde269131f9b4738b ts=2026-10-06T15:31:43.1640000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[658] _id=6ac514eede269131f9b47392 ts=2026-10-06T15:31:44.5470000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[633] _id=6ac514eede269131f9b4739b ts=2026-10-06T15:31:44.5470000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[7310] _id=6acfa197de269131f9d4cc98 ts=2026-10-14T15:36:54.7010000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[11788] _id=6ad6096ade269131f9e96772 ts=2026-10-19T12:13:30.0030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[405] _id=6ac3c4d3de269131f9ad59b9 ts=2026-10-05T15:40:02.7840000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[431] _id=6ac3c51fde269131f9ad5cef ts=2026-10-05T15:41:18.6130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[10157] _id=6ad0f17ede269131f9dc9c7e ts=2026-10-15T15:30:06.0470000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[10773] _id=6ad57948de269131f9e92716 ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[4067] _id=6ac7b7e7de269131f9c3ef97 ts=2026-10-08T15:33:59.2380000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[4167] _id=6ac7b8f1de269131f9c40b33 ts=2026-10-08T15:38:25.2830000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[4207] _id=6ac7b9a7de269131f9c415a8 ts=2026-10-08T15:41:27.4520000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 214 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[948] _id=6ac51510de269131f9b476d9 ts=2026-10-06T15:34:37.9020000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[949] _id=6ac51510de269131f9b476dd ts=2026-10-06T15:34:37.9020000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[981] _id=6ac51510de269131f9b476e1 ts=2026-10-06T15:34:37.9020000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 447 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[719] _id=6ac514eede269131f9b473b7 ts=2026-10-06T15:31:44.5470000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[870] _id=6ac514f2de269131f9b47439 ts=2026-10-06T15:33:08.0270000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[721] _id=6ac514f2de269131f9b47443 ts=2026-10-06T15:33:08.1180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 DEBUGMenu record in 'Unit 2 Prod (Refactor)' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[4028] _id=6ac7b756de269131f9c3e11c ts=2026-10-08T15:31:29.8840000Z`
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Open' (totals: 14 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'DialogueStartEvent' (totals: 312 start, 307 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 44 unmatched 'BecameCameraCentered' (totals: 542 open, 540 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 64 unmatched 'BecameVisible' (totals: 851 open, 911 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 54 open, 53 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 36 start, 23 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 237 of 12110 adjacent _id pairs reverse in client time; worst 142.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b03.jsonl[656] _id=6ac514ebde269131f9b4733d ts=2026-10-06T15:34:02.8660000Z`; `6ab9a8bc9a8420a1e6b56b03.jsonl[663] _id=6ac514ecde269131f9b47349 ts=2026-10-06T15:31:40.2290000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.82s, min -85160.24s, max -0.15s over 12111 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b03\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

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

### `InputEvent` — 4819 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2370); Unit 2 Prod (Refactor) (1034); Unit 4 Dev - Dungeon (454); Unit 3 Dungeon Dev (412); Unit 4 Dev - Anderson Base (255); Unit 4 Dev (175); Unit 1 Dev (119)
- **Intervals:** median 0.83s (p5 0.12s / p95 11.40s, n=4818)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4819/4819 records)
    "pressed"  x4819
data.actionType  (string, 4819/4819 records)
    "Move"  x3231
    "Interact"  x1032
    "Jump"  x249
    "Ascend"  x112
    "Hoverboard"  x89
    "Sprint"  x54
    "Descend"  x41
    "Map"  x8
    "Pause"  x3
data.key  (string, 4819/4819 records, 44 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4819/4819 records)
    "Player"  x2464
    "Drone"  x2355
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2844 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1838); Unit 4 Dev (638); Unit 3 Dungeon Dev (368)
- **Intervals:** median 0.08s (p5 0.00s / p95 2.36s, n=2843)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2844/2844 records)
    "BecameInvisible"  x911
    "BecameVisible"  x851
    "BecameCameraCentered"  x542
    "BecameCameraUncentered"  x540
data.pieceId  (string, 2844/2844 records)
    30 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2844/2844 records)
    1931 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1737 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (514); Unit 2 Prod (Refactor) (351); Unit 4 Dev (224); Unit 3 Dungeon Dev (175); Unit 1 Dev (173); Unit 4 Dev - Dungeon (172); Unit 4 Dev - Anderson Base (128)
- **Intervals:** median 10.00s (p5 9.95s / p95 11.55s, n=1727)
- **Fields under `data`:**

```text
data.position  (object, 1737/1737 records)
data.position.x  (number, 1737/1737 records)
    numeric range -715.554 .. 1550.35 (610 unique)
data.position.y  (number, 1737/1737 records)
    numeric range -113.43 .. 158.182 (424 unique)
data.position.z  (number, 1737/1737 records)
    numeric range -1169.81 .. 1923.28 (609 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1583 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (374); Unit 4 Dev (297); Unit 2 Prod (Refactor) (219); Unit 3 Dungeon Dev (216); Unit 1 Dev (197); Unit 4 Dev - Anderson Base (166); Unit 4 Dev - Dungeon (114)
- **eventKey:** present on 964 of 1583 records
- **Intervals:** median 4.12s (p5 0.01s / p95 35.92s, n=1582)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x964; [conversationId, dialogueEventType] x619
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1583/1583 records)
    numeric range 10 .. 114 (38 unique)
data.dialogueEventType  (string, 1583/1583 records)
    "DialogueNodeEvent"  x964
    "DialogueStartEvent"  x312
    "DialogueFinishEvent"  x307
data.nodeId  (number, 964/1583 records)
    numeric range 0 .. 289 (208 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 294 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (91); Unit 2 Prod (Refactor) (81); Unit 3 Dungeon Dev (56); Unit 4 Dev (27); Unit 3 Dev (15); Unit 4 Dev - Anderson Base (14); Unit 1 Dev (10)
- **Intervals:** median 10.53s (p5 0.40s / p95 320.82s, n=293)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 294/294 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 294/294 records)
    85 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 267 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (169); Unit 3 Dev (59); Unit 1 Dev (33); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 0.58s (p5 0.05s / p95 17.31s, n=266)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 267/267 records)
    "argumentationNodeHoverEnd"  x118
    "argumentationNodeHoverStart"  x116
    "argumentationNodeAdd"  x22
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 267/267 records)
    "Unit 4 - Flooding"  x169
    "Unit 3 - Pollution Upstream"  x59
    "Unit 1 - Freshwater"  x21
    "Unit 1 - Argumentation Tutorial"  x12
    "Unit 2 – Watershed"  x6
data.nodeName  (string, 267/267 records)
    "B"  x44
    "A"  x32
    "I"  x32
    "1"  x26
    "II"  x25
    "4"  x22
    "D"  x21
    "2"  x19
    "C"  x19
    "3"  x18
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 178 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (155); Unit 2 Prod (Refactor) (22); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 3.89s (p5 0.80s / p95 349.53s, n=177)
- **`data` key-set variants:** [actionType, featureUsed] x107; [actionType, featureUsed, location] x70; [actionType, featureUsed, legendName] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 178/178 records)
    "WaypointMoveEvent"  x60
    "MapOpenEvent"  x54
    "MapCloseEvent"  x53
    "WaypointSetEvent"  x8
    "WaypointResetEvent"  x2
    "Selected"  x1
data.featureUsed  (string, 178/178 records)
    "Map"  x107
    "Waypoint"  x70
    "Legend"  x1
data.legendName  (string, 1/178 records)
    "0 ft"  x1
data.location  (object, 70/178 records)
data.location.x  (number, 70/178 records)
    numeric range -527.73 .. 433.576 (55 unique)
data.location.y  (number, 70/178 records)
    numeric range -287.235 .. 334.442 (61 unique)
data.location.z  (number, 70/178 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 109 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (84); Unit 4 Dev (25)
- **Intervals:** median 0.76s (p5 0.11s / p95 12.57s, n=108)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x105; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/109 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/109 records)
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 105/109 records)
    "RightDrag"  x55
    "LeftDrag"  x50
data.currentSoilType  (string, 105/109 records)
    "SANDGRAVEL"  x20
    "CLAY"  x19
    "CLAYROCK"  x16
    "CLAYSAND"  x16
    "GRAVEL"  x14
    "SAND"  x14
    "BEDROCK"  x6
data.isCorrectSelection  (string, 105/109 records)
    "false"  x85
    "true"  x20
data.waterLevelStatus  (string, 105/109 records)
    "TooLow"  x72
    "Proper"  x20
    "TooHigh"  x13
data.waterRetentionChange  (string, 105/109 records)
    "Decrease"  x60
    "Increase"  x25
    "NoChange"  x20
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 59 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev (11); Unit 4 Dev - Dungeon (11); Unit 2 Prod (Refactor) (4); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (4)
- **eventKey:** present on 59 of 59 records
- **Intervals:** median 239.25s (p5 0.01s / p95 85968.47s, n=58)
- **`data` key-set variants:** [questEventType, questID, questName] x36; [questEventType, questID, questName, questSuccessOrFailure] x23
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 59/59 records)
    "questActiveEvent"  x36
    "questFinishEvent"  x23
data.questID  (string, 59/59 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 59/59 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 23/59 records)
    "Succeeded"  x23
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 46 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (25); Unit 3 Dev (16); Unit 1 Dev (5)
- **Intervals:** median 7.01s (p5 0.27s / p95 67.97s, n=45)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "submitAnswerEvent"  x46
data.answerSubmitted  (string, 46/46 records)
    16 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 46/46 records)
    "Unit 4 - Flooding"  x25
    "Unit 3 - Pollution Upstream"  x16
    "Unit 1 - Freshwater"  x4
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 42 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (8); Unit 3 Dev (4); Unit 4 Dev (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1)
- **Intervals:** median 160.45s (p5 8.04s / p95 86561.55s, n=41)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "DebugMenuStateChanged"  x42
data.isOpened  (bool, 42/42 records)
    false  x42
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 26 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 3 Dev (4); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 881.48s (p5 48.91s / p95 254111.39s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 25 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 3 Dev (6)
- **Intervals:** median 21.29s (p5 1.56s / p95 86561.70s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "Open"  x14
    "Close"  x11
data.toolName  (string, 25/25 records, 25 empty-string)
    ""  x25
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 3569.23s (p5 56.12s / p95 310188.34s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 17 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (17)
- **Intervals:** median 3.24s (p5 0.98s / p95 159.34s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "ChangeCanister"  x17
data.canisterType  (string, 17/17 records)
    "Bedrock"  x6
    "Clay"  x6
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 17/17 records)
    "5"  x15
    "3"  x1
    "4"  x1
data.machine  (string, 17/17 records)
    "1"  x14
    "2"  x3
data.row  (string, 17/17 records)
    "BottomRow"  x11
    "TopRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 13 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (13)
- **Intervals:** median 6.04s (p5 1.77s / p95 30.67s, n=12)
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x6
data.boxId  (string, 13/13 records)
    "1"  x6
    "0"  x5
    "2"  x2
data.soilType  (string, 13/13 records)
    "Clay"  x5
    "Gravel"  x5
    "Sand"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Transition (1); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 84951.89s (p5 72.18s / p95 376099.67s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 39.07s (p5 0.03s / p95 634046.45s, n=9)
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

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 2.84s (p5 0.59s / p95 699669.56s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 598950.07s (p5 406386.21s / p95 791513.93s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 6.59s (p5 6.59s / p95 6.59s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[11-226, 11-23, 11-24, 11-25, 11-25]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `TerasGardenBox` data.actionType: "" (7x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (60x); "WaypointResetEvent" (2x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (70x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (6x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*