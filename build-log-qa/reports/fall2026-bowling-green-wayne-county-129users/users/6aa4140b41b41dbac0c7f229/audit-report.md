# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f229

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f229
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f229.jsonl
- **Records:** 17722 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f229
- **Time span:** 2026-09-23T14:10:29.156000+00:00 .. 2026-10-07T14:31:58.518000+00:00 (336h 21m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f229\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 17722 records, 8 scenes.
- Findings: **0 FAIL**, **26 WARNING**, 98 INFO, 2 NOT_TESTED, 81 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 9828 | 55.46 | 1 | 6 | 0 | 2026-09-23T14:10:51.628000+00:00 | 2026-10-07T14:31:35.587000+00:00 | 336h 20m |
| PuzzlePieceVisibleEvent | 2856 | 16.12 | 1 | 3 | 0 | 2026-09-25T14:10:06.332000+00:00 | 2026-10-01T14:19:39.319000+00:00 | 144h 9m |
| PlayerPositionEvent | 2032 | 11.47 | 1 | 6 | 0 | 2026-09-23T14:10:46.087000+00:00 | 2026-10-07T14:31:54.821000+00:00 | 336h 21m |
| DialogueEvent | 1692 | 9.55 | 1 | 6 | 1033 | 2026-09-23T14:11:08.549000+00:00 | 2026-10-07T14:30:28.083000+00:00 | 336h 19m |
| ObjectInterEvent | 390 | 2.2 | 1 | 6 | 0 | 2026-09-23T14:15:48.783000+00:00 | 2026-10-07T14:31:23.311000+00:00 | 336h 15m |
| argumentationNodeEvent | 244 | 1.38 | 1 | 2 | 0 | 2026-09-24T14:07:39.057000+00:00 | 2026-09-30T15:50:39.511000+00:00 | 145h 43m |
| TopographicMapEvent | 235 | 1.33 | 1 | 5 | 0 | 2026-09-25T13:56:02.998000+00:00 | 2026-10-07T14:18:08.534000+00:00 | 288h 22m |
| questEvent | 82 | 0.46 | 1 | 6 | 82 | 2026-09-23T14:11:08.535000+00:00 | 2026-10-07T14:30:18.226000+00:00 | 336h 19m |
| Soil Key Puzzle | 70 | 0.39 | 1 | 3 | 0 | 2026-09-25T14:15:58.014000+00:00 | 2026-10-01T14:17:54.031000+00:00 | 144h 1m |
| gameWindowFocusEvent | 70 | 0.39 | 1 | 6 | 0 | 2026-09-23T14:10:29.156000+00:00 | 2026-10-07T14:31:41.143000+00:00 | 336h 21m |
| gameWindowUnfocusEvent | 57 | 0.32 | 1 | 6 | 0 | 2026-09-23T14:19:44.459000+00:00 | 2026-10-07T14:31:58.518000+00:00 | 336h 12m |
| soilMachine | 44 | 0.25 | 1 | 1 | 0 | 2026-10-05T14:01:46.733000+00:00 | 2026-10-07T14:30:58.654000+00:00 | 48h 29m |
| DaniEvent | 35 | 0.2 | 1 | 2 | 0 | 2026-09-25T13:57:04.208000+00:00 | 2026-09-30T14:29:36.933000+00:00 | 120h 32m |
| DEBUGMenu | 30 | 0.17 | 1 | 7 | 0 | 2026-09-23T14:10:46.080000+00:00 | 2026-10-07T14:14:58.250000+00:00 | 336h 4m |
| gameStartEvent | 26 | 0.15 | 1 | 1 | 0 | 2026-09-23T14:10:29.156000+00:00 | 2026-10-07T14:14:46.149000+00:00 | 336h 4m |
| chatEvent | 10 | 0.06 | 1 | 2 | 0 | 2026-09-25T13:57:21.111000+00:00 | 2026-09-30T14:21:30.806000+00:00 | 120h 24m |
| argumentationEvent | 7 | 0.04 | 1 | 2 | 0 | 2026-09-24T14:08:32.600000+00:00 | 2026-09-30T15:50:40.748000+00:00 | 145h 42m |
| argumentationAnswerEvent | 6 | 0.03 | 1 | 2 | 0 | 2026-09-24T14:09:10.962000+00:00 | 2026-09-30T15:50:40.660000+00:00 | 145h 41m |
| crash | 6 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-10-01T14:05:16.622000+00:00 | 2026-10-01T14:05:16.622000+00:00 | 0.0s |
| argumentationToolEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-09-30T15:48:45.311000+00:00 | 2026-09-30T15:48:45.311000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

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
  - Observed: 51.083s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3.227s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.587s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 35 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 4.1x vs baseline. 
  - Observed: 9828 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 330 ft; 360 ft; Teleporter Room 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,I; A,3,I 
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
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 1 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 10 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-0, 10-198, 10-200, 10-202, 10-204, 10-38]; [10-202, 10-204, 10-38, 10-39, 10-40, 10-212]; [11-27, 11-27, 11-27, 11-27, 11-27]; [11-27, 11-29, 11-27, 11-29, 11-230]; [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 8.8x vs baseline. 
  - Observed: 44 records 
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
  - Observed: 24 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[611] _id=6ab3e0e0485cab4c954d201f ts=2026-09-23T14:23:28.8760000Z`; `6aa4140b41b41dbac0c7f229.jsonl[677] _id=6ab3e1b8485cab4c954d285d ts=2026-09-23T14:27:05.3850000Z`; `6aa4140b41b41dbac0c7f229.jsonl[752] _id=6ab3e225485cab4c954d2cc3 ts=2026-09-23T14:28:53.9310000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[84] _id=6ab3ddd5485cab4c954cff18 ts=2026-09-23T14:10:29.1560000Z`; `6aa4140b41b41dbac0c7f229.jsonl[562] _id=6ab3e055485cab4c954d18dd ts=2026-09-23T14:21:10.1550000Z`; `6aa4140b41b41dbac0c7f229.jsonl[803] _id=6ab52819485cab4c95514179 ts=2026-09-24T13:39:37.0290000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 70 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 70} 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[91] _id=6ab3ddd5485cab4c954cff13 ts=2026-09-23T14:10:29.1560000Z`; `6aa4140b41b41dbac0c7f229.jsonl[558] _id=6ab3e002485cab4c954d152b ts=2026-09-23T14:19:46.0740000Z`; `6aa4140b41b41dbac0c7f229.jsonl[561] _id=6ab3e055485cab4c954d18d8 ts=2026-09-23T14:21:10.1530000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 57 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 57} 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[557] _id=6ab3e000485cab4c954d1511 ts=2026-09-23T14:19:44.4590000Z`; `6aa4140b41b41dbac0c7f229.jsonl[559] _id=6ab3e005485cab4c954d1559 ts=2026-09-23T14:19:49.1300000Z`; `6aa4140b41b41dbac0c7f229.jsonl[570] _id=6ab3e065485cab4c954d19ed ts=2026-09-23T14:21:26.6210000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 5 of 235 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2332] _id=6ab67d72485cab4c9555a5b8 ts=2026-09-25T13:56:02.9980000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2328] _id=6ab67d79485cab4c9555a5d6 ts=2026-09-25T13:56:09.2090000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2329] _id=6ab67d7a485cab4c9555a5de ts=2026-09-25T13:56:10.6110000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 9827 | 0.0 | 0.346 | 123.216 | 3.462 | 343382.293 | 0.49 | 761 | 13 |
| PuzzlePieceVisibleEvent | 2855 | 0.0 | 0.029 | 181.777 | 0.81 | 258589.753 | 0.33 | 1761 | 4 |
| PlayerPositionEvent | 2025 | 8.427 | 10.0 | 597.832 | 12.221 | 343345.71 | 0.1 | 0 | 12 |
| DialogueEvent | 1691 | 0.001 | 4.008 | 716.002 | 47.532 | 343355.942 | 0.08 | 464 | 12 |
| ObjectInterEvent | 389 | 0.004 | 5.417 | 3111.914 | 341.156 | 343389.089 | 0.02 | 2 | 14 |
| argumentationNodeEvent | 243 | 0.015 | 0.406 | 2158.767 | 7.82 | 433399.594 | 0.03 | 50 | 3 |
| TopographicMapEvent | 234 | 0.299 | 2.627 | 4436.434 | 701.228 | 518557.775 | 0.01 | 0 | 13 |
| questEvent | 81 | 0.002 | 195.387 | 14947.527 | 84968.824 | 343482.899 | 0.0 | 13 | 20 |
| Soil Key Puzzle | 69 | 0.126 | 0.892 | 7514.725 | 3935.999 | 258463.312 | 0.01 | 0 | 4 |
| gameWindowFocusEvent | 69 | 0.425 | 138.69 | 17548.869 | 85992.33 | 343791.725 | 0.0 | 0 | 21 |
| gameWindowUnfocusEvent | 56 | 0.299 | 102.504 | 21613.108 | 85334.671 | 344162.607 | 0.0 | 0 | 17 |
| soilMachine | 43 | 0.259 | 5.587 | 4059.347 | 526.087 | 87001.219 | 0.01 | 0 | 2 |
| DaniEvent | 34 | 0.005 | 2.562 | 12763.315 | 411.915 | 432673.224 | 0.0 | 3 | 2 |
| DEBUGMenu | 29 | 12.559 | 877.708 | 41719.04 | 190143.048 | 343796.589 | 0.0 | 0 | 19 |
| gameStartEvent | 25 | 39.32 | 1566.511 | 48394.28 | 224193.405 | 343791.725 | 0.0 | 0 | 18 |
| chatEvent | 9 | 1.121 | 3.227 | 48161.077 | 259912.759 | 432731.211 | 0.0 | 0 | 2 |
| argumentationEvent | 6 | 0.061 | 43.192 | 87421.358 | 393232.066 | 524262.223 | 0.0 | 0 | 1 |
| argumentationAnswerEvent | 5 | 27.212 | 51.083 | 104897.94 | 419449.645 | 524290.584 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationToolEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2837] _id=6ab6814f485cab4c9555ddfa ts=2026-09-25T14:12:31.8080000Z == 6aa4140b41b41dbac0c7f229.jsonl[2838] _id=6ab6814f485cab4c9555ddff ts=2026-09-25T14:12:31.8080000Z`; `6aa4140b41b41dbac0c7f229.jsonl[14807] _id=6ac3ac96de269131f9aa3c82 ts=2026-10-05T13:56:38.3890000Z == 6aa4140b41b41dbac0c7f229.jsonl[14810] _id=6ac3ac96de269131f9aa3c84 ts=2026-10-05T13:56:38.3890000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 174 group(s), 258 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2612] _id=6ab680cc485cab4c9555d59c ts=2026-09-25T14:10:19.9510000Z == 6aa4140b41b41dbac0c7f229.jsonl[2613] _id=6ab680cc485cab4c9555d59e ts=2026-09-25T14:10:19.9510000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2603] _id=6ab680cf485cab4c9555d5d8 ts=2026-09-25T14:10:22.0560000Z == 6aa4140b41b41dbac0c7f229.jsonl[2604] _id=6ab680cf485cab4c9555d5dc ts=2026-09-25T14:10:22.0560000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2626] _id=6ab680d8485cab4c9555d626 ts=2026-09-25T14:10:32.8130000Z == 6aa4140b41b41dbac0c7f229.jsonl[2627] _id=6ab680d8485cab4c9555d62a ts=2026-09-25T14:10:32.8130000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[15885] _id=6ac4fc17de269131f9b17261 ts=? == 6aa4140b41b41dbac0c7f229.jsonl[17718] _id=6ac657d0de269131f9bae982 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 41 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `689ms: 6aa4140b41b41dbac0c7f229.jsonl[7] _id=6ab3df14485cab4c954d08b1 ts=2026-09-23T14:15:48.7830000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[230] _id=6ab3df15485cab4c954d08b7 ts=2026-09-23T14:15:49.4720000Z`; `223ms: 6aa4140b41b41dbac0c7f229.jsonl[230] _id=6ab3df15485cab4c954d08b7 ts=2026-09-23T14:15:49.4720000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[231] _id=6ab3df15485cab4c954d08bb ts=2026-09-23T14:15:49.6950000Z`; `167ms: 6aa4140b41b41dbac0c7f229.jsonl[231] _id=6ab3df15485cab4c954d08bb ts=2026-09-23T14:15:49.6950000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[232] _id=6ab3df15485cab4c954d08bf ts=2026-09-23T14:15:49.8620000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 668 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `133ms: 6aa4140b41b41dbac0c7f229.jsonl[2615] _id=6ab680cd485cab4c9555d5a8 ts=2026-09-25T14:10:19.9510000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[2616] _id=6ab680cd485cab4c9555d5ae ts=2026-09-25T14:10:20.0840000Z`; `12ms: 6aa4140b41b41dbac0c7f229.jsonl[2616] _id=6ab680cd485cab4c9555d5ae ts=2026-09-25T14:10:20.0840000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[2617] _id=6ab680cd485cab4c9555d5b2 ts=2026-09-25T14:10:20.0960000Z`; `250ms: 6aa4140b41b41dbac0c7f229.jsonl[2621] _id=6ab680ce485cab4c9555d5be ts=2026-09-25T14:10:20.8200000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[2609] _id=6ab680ce485cab4c9555d5c2 ts=2026-09-25T14:10:21.0700000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `416ms: 6aa4140b41b41dbac0c7f229.jsonl[4628] _id=6aba71f2485cab4c956852d3 ts=2026-09-28T13:56:03.0910000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[4629] _id=6aba71f2485cab4c956852e1 ts=2026-09-28T13:56:03.5070000Z`; `735ms: 6aa4140b41b41dbac0c7f229.jsonl[7905] _id=6abd149b485cab4c95895d57 ts=2026-09-30T13:54:35.0950000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[7915] _id=6abd149b485cab4c95895d6b ts=2026-09-30T13:54:35.8300000Z`; `996ms: 6aa4140b41b41dbac0c7f229.jsonl[7906] _id=6abd149b485cab4c95895d63 ts=2026-09-30T13:54:35.3940000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[7916] _id=6abd149c485cab4c95895d77 ts=2026-09-30T13:54:36.3900000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `61ms: 6aa4140b41b41dbac0c7f229.jsonl[10644] _id=6abd2fcc485cab4c958d027c ts=2026-09-30T15:50:40.6870000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[10666] _id=6abd2fcc485cab4c958d0284 ts=2026-09-30T15:50:40.7480000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 40 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `106ms: 6aa4140b41b41dbac0c7f229.jsonl[1302] _id=6ab52ee8485cab4c9551d62d ts=2026-09-24T14:08:40.0210000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[1306] _id=6ab52ee8485cab4c9551d633 ts=2026-09-24T14:08:40.1270000Z`; `487ms: 6aa4140b41b41dbac0c7f229.jsonl[1305] _id=6ab52ee8485cab4c9551d631 ts=2026-09-24T14:08:40.0460000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[1307] _id=6ab52ee8485cab4c9551d637 ts=2026-09-24T14:08:40.5330000Z`; `167ms: 6aa4140b41b41dbac0c7f229.jsonl[1309] _id=6ab52eea485cab4c9551d653 ts=2026-09-24T14:08:42.8530000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[1303] _id=6ab52eeb485cab4c9551d659 ts=2026-09-24T14:08:43.0200000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `425ms: 6aa4140b41b41dbac0c7f229.jsonl[4438] _id=6aba7092485cab4c95682393 ts=2026-09-28T13:50:18.8360000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[4443] _id=6aba7095485cab4c956823e5 ts=2026-09-28T13:50:19.2610000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `299ms: 6aa4140b41b41dbac0c7f229.jsonl[4442] _id=6aba7092485cab4c95682389 ts=2026-09-28T13:50:18.6080000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[4440] _id=6aba7095485cab4c956823df ts=2026-09-28T13:50:18.9070000Z`; `354ms: 6aa4140b41b41dbac0c7f229.jsonl[15904] _id=6ac4fc5dde269131f9b18a7c ts=2026-10-06T13:49:17.4960000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[15906] _id=6ac4fc5dde269131f9b18aaf ts=2026-10-06T13:49:17.8500000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `613ms: 6aa4140b41b41dbac0c7f229.jsonl[15757] _id=6ac3b062de269131f9aae89d ts=2026-10-05T14:12:50.7010000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[15759] _id=6ac3b063de269131f9aae8a5 ts=2026-10-05T14:12:51.3140000Z`; `386ms: 6aa4140b41b41dbac0c7f229.jsonl[15759] _id=6ac3b063de269131f9aae8a5 ts=2026-10-05T14:12:51.3140000Z ~ 6aa4140b41b41dbac0c7f229.jsonl[15760] _id=6ac3b063de269131f9aae8ae ts=2026-10-05T14:12:51.7000000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa4140b41b41dbac0c7f229.jsonl[14206] _id=6abe6cd5485cab4c95a847df ts=2026-10-01T14:23:17.6240000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14719] _id=6ac3abcade269131f9aa0db2 ts=2026-10-05T13:53:14.2130000Z; 71h 43m: 6aa4140b41b41dbac0c7f229.jsonl[2468] _id=6ab67fd3485cab4c9555c812 ts=2026-09-25T14:06:11.8800000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4418] _id=6aba7086485cab4c9568222d ts=2026-09-28T13:50:07.0560000Z; 24h 26m: 6aa4140b41b41dbac0c7f229.jsonl[15884] _id=6ac4fc10de269131f9b170e3 ts=2026-10-06T13:48:00.8360000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17100] _id=6ac653d5de269131f9ba81bc ts=2026-10-07T14:14:45.6910000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 120h 11m 
  - Evidence: 120h 11m: 6aa4140b41b41dbac0c7f229.jsonl[2403] _id=6ab67dea485cab4c9555b0d1 ts=2026-09-25T13:58:02.9840000Z -> 6aa4140b41b41dbac0c7f229.jsonl[8940] _id=6abd180c485cab4c958a6ef8 ts=2026-09-30T14:09:16.2080000Z; 11m 0s: 6aa4140b41b41dbac0c7f229.jsonl[8977] _id=6abd1844485cab4c958a7a64 ts=2026-09-30T14:10:12.1930000Z -> 6aa4140b41b41dbac0c7f229.jsonl[9493] _id=6abd1ad8485cab4c958afc54 ts=2026-09-30T14:21:12.6600000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.005s..0.008s shown 
  - Evidence: 5ms: 6aa4140b41b41dbac0c7f229.jsonl[8949] _id=6abd1816485cab4c958a70c8 ts=2026-09-30T14:09:26.0080000Z -> 6aa4140b41b41dbac0c7f229.jsonl[8950] _id=6abd1816485cab4c958a70cc ts=2026-09-30T14:09:26.0130000Z; 7ms: 6aa4140b41b41dbac0c7f229.jsonl[2402] _id=6ab67dea485cab4c9555b0c8 ts=2026-09-25T13:58:02.9770000Z -> 6aa4140b41b41dbac0c7f229.jsonl[2403] _id=6ab67dea485cab4c9555b0d1 ts=2026-09-25T13:58:02.9840000Z; 8ms: 6aa4140b41b41dbac0c7f229.jsonl[8952] _id=6abd181a485cab4c958a71ba ts=2026-09-30T14:09:30.7320000Z -> 6aa4140b41b41dbac0c7f229.jsonl[8951] _id=6abd181a485cab4c958a71bf ts=2026-09-30T14:09:30.7400000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa4140b41b41dbac0c7f229.jsonl[14649] _id=6abe6e93485cab4c95a8a7fd ts=2026-10-01T14:30:42.9980000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14723] _id=6ac3abcfde269131f9aa0ecd ts=2026-10-05T13:53:18.9400000Z; 71h 23m: 6aa4140b41b41dbac0c7f229.jsonl[4307] _id=6ab68503485cab4c95564554 ts=2026-09-25T14:28:19.2250000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4470] _id=6aba7100485cab4c95682e38 ts=2026-09-28T13:52:07.7280000Z; 24h 8m: 6aa4140b41b41dbac0c7f229.jsonl[16155] _id=6ac50085de269131f9b25602 ts=2026-10-06T14:07:01.3370000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17106] _id=6ac653e8de269131f9ba8418 ts=2026-10-07T14:15:04.5890000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 464 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f229.jsonl[10600] _id=6abd2f8e485cab4c958d0160 ts=2026-09-30T15:49:38.5330000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10606] _id=6abd2f8e485cab4c958d0162 ts=2026-09-30T15:49:38.5340000Z; 1ms: 6aa4140b41b41dbac0c7f229.jsonl[10665] _id=6abd2fdf485cab4c958d031c ts=2026-09-30T15:50:59.3130000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10680] _id=6abd2fdf485cab4c958d0320 ts=2026-09-30T15:50:59.3140000Z; 1ms: 6aa4140b41b41dbac0c7f229.jsonl[10685] _id=6abd2fea485cab4c958d0376 ts=2026-09-30T15:51:10.1750000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10689] _id=6abd2feb485cab4c958d0378 ts=2026-09-30T15:51:10.1760000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4140b41b41dbac0c7f229.jsonl[14645] _id=6abe6e92485cab4c95a8a7cd ts=2026-10-01T14:30:42.3790000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14712] _id=6ac3abe8de269131f9aa148e ts=2026-10-05T13:53:44.6720000Z; 71h 20m: 6aa4140b41b41dbac0c7f229.jsonl[4405] _id=6ab68545485cab4c95564954 ts=2026-09-25T14:29:25.6970000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4424] _id=6aba708f485cab4c956822e3 ts=2026-09-28T13:50:14.3860000Z; 23h 36m: 6aa4140b41b41dbac0c7f229.jsonl[1723] _id=6ab53065485cab4c9551ed1e ts=2026-09-24T14:15:01.0450000Z -> 6aa4140b41b41dbac0c7f229.jsonl[1834] _id=6ab67c49485cab4c95559a74 ts=2026-09-25T13:51:06.2420000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 761 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f229.jsonl[14807] _id=6ac3ac96de269131f9aa3c82 ts=2026-10-05T13:56:38.3890000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14810] _id=6ac3ac96de269131f9aa3c84 ts=2026-10-05T13:56:38.3890000Z; 0ms: 6aa4140b41b41dbac0c7f229.jsonl[17696] _id=6ac657bbde269131f9bae30a ts=2026-10-07T14:31:23.3220000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17697] _id=6ac657bbde269131f9bae30b ts=2026-10-07T14:31:23.3220000Z; 0ms: 6aa4140b41b41dbac0c7f229.jsonl[2837] _id=6ab6814f485cab4c9555ddfa ts=2026-09-25T14:12:31.8080000Z -> 6aa4140b41b41dbac0c7f229.jsonl[2838] _id=6ab6814f485cab4c9555ddff ts=2026-09-25T14:12:31.8080000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4140b41b41dbac0c7f229.jsonl[14650] _id=6abe6e93485cab4c95a8a803 ts=2026-10-01T14:30:43.0010000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14738] _id=6ac3abf0de269131f9aa165a ts=2026-10-05T13:53:52.0900000Z; 71h 47m: 6aa4140b41b41dbac0c7f229.jsonl[3806] _id=6ab6821d485cab4c955602f8 ts=2026-09-25T14:15:58.0190000Z -> 6aa4140b41b41dbac0c7f229.jsonl[5072] _id=6aba73c0485cab4c95687345 ts=2026-09-28T14:03:44.3580000Z; 24h 2m: 6aa4140b41b41dbac0c7f229.jsonl[16947] _id=6ac501eade269131f9b27347 ts=2026-10-06T14:12:58.4920000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17133] _id=6ac653ffde269131f9ba871d ts=2026-10-07T14:15:27.0410000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.004s shown 
  - Evidence: 4ms: 6aa4140b41b41dbac0c7f229.jsonl[597] _id=6ab3e07b485cab4c954d1b59 ts=2026-09-23T14:21:48.2500000Z -> 6aa4140b41b41dbac0c7f229.jsonl[596] _id=6ab3e07b485cab4c954d1b5d ts=2026-09-23T14:21:48.2540000Z; 4ms: 6aa4140b41b41dbac0c7f229.jsonl[839] _id=6ab52899485cab4c95515185 ts=2026-09-24T13:41:45.7780000Z -> 6aa4140b41b41dbac0c7f229.jsonl[831] _id=6ab52899485cab4c9551518b ts=2026-09-24T13:41:45.7820000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa4140b41b41dbac0c7f229.jsonl[14691] _id=6abe6e98485cab4c95a8a996 ts=2026-10-01T14:30:48.5110000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14722] _id=6ac3abcfde269131f9aa0ebd ts=2026-10-05T13:53:14.2210000Z; 71h 20m: 6aa4140b41b41dbac0c7f229.jsonl[4412] _id=6ab68545485cab4c95564956 ts=2026-09-25T14:29:25.7970000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4422] _id=6aba708e485cab4c956822dd ts=2026-09-28T13:50:07.0620000Z; 23h 35m: 6aa4140b41b41dbac0c7f229.jsonl[1753] _id=6ab5308f485cab4c9551ee5f ts=2026-09-24T14:15:43.0870000Z -> 6aa4140b41b41dbac0c7f229.jsonl[1831] _id=6ab67c40485cab4c955599d6 ts=2026-09-25T13:50:50.7260000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 49m 
  - Evidence: 71h 49m: 6aa4140b41b41dbac0c7f229.jsonl[3604] _id=6ab681df485cab4c9555f8dc ts=2026-09-25T14:14:52.6580000Z -> 6aa4140b41b41dbac0c7f229.jsonl[5130] _id=6aba73fb485cab4c956876e5 ts=2026-09-28T14:04:42.4110000Z; 49h 39m: 6aa4140b41b41dbac0c7f229.jsonl[6612] _id=6aba7677485cab4c9568ab9d ts=2026-09-28T14:15:16.2500000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10345] _id=6abd30b6485cab4c958d0b50 ts=2026-09-30T15:54:33.6300000Z; 22h 9m: 6aa4140b41b41dbac0c7f229.jsonl[11950] _id=6abd340e485cab4c958d4bf8 ts=2026-09-30T16:08:43.8170000Z -> 6aa4140b41b41dbac0c7f229.jsonl[13482] _id=6abe6b95485cab4c95a7e663 ts=2026-10-01T14:17:57.3570000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1761 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f229.jsonl[10333] _id=6abd30c1485cab4c958d0bac ts=2026-09-30T15:54:44.3670000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10415] _id=6abd30c1485cab4c958d0bae ts=2026-09-30T15:54:44.3670000Z; 0ms: 6aa4140b41b41dbac0c7f229.jsonl[10345] _id=6abd30b6485cab4c958d0b50 ts=2026-09-30T15:54:33.6300000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10339] _id=6abd30b6485cab4c958d0b52 ts=2026-09-30T15:54:33.6300000Z; 0ms: 6aa4140b41b41dbac0c7f229.jsonl[10390] _id=6abd30b7485cab4c958d0b70 ts=2026-09-30T15:54:35.4110000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10391] _id=6abd30b7485cab4c958d0b72 ts=2026-09-30T15:54:35.4110000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 47m 
  - Evidence: 71h 47m: 6aa4140b41b41dbac0c7f229.jsonl[3747] _id=6ab68220485cab4c9556036a ts=2026-09-25T14:16:01.0390000Z -> 6aa4140b41b41dbac0c7f229.jsonl[5078] _id=6aba73c0485cab4c95687343 ts=2026-09-28T14:03:44.3510000Z; 47h 59m: 6aa4140b41b41dbac0c7f229.jsonl[5100] _id=6aba73d7485cab4c956874a9 ts=2026-09-28T14:04:08.1460000Z -> 6aa4140b41b41dbac0c7f229.jsonl[8492] _id=6abd16b8485cab4c9589c06b ts=2026-09-30T14:03:36.1120000Z; 22h 23m: 6aa4140b41b41dbac0c7f229.jsonl[10826] _id=6abd308f485cab4c958d0a1e ts=2026-09-30T15:53:55.4110000Z -> 6aa4140b41b41dbac0c7f229.jsonl[13450] _id=6abe6b7c485cab4c95a7e037 ts=2026-10-01T14:17:32.6590000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 144h 2m 
  - Evidence: 144h 2m: 6aa4140b41b41dbac0c7f229.jsonl[13154] _id=6abe6a82485cab4c95a7b2e3 ts=2026-10-01T14:13:22.0880000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17140] _id=6ac6541fde269131f9ba8a58 ts=2026-10-07T14:15:59.8630000Z; 71h 26m: 6aa4140b41b41dbac0c7f229.jsonl[4194] _id=6ab684c9485cab4c955640fc ts=2026-09-25T14:27:21.6800000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4498] _id=6aba7186485cab4c956840a4 ts=2026-09-28T13:54:17.9140000Z; 23h 45m: 6aa4140b41b41dbac0c7f229.jsonl[6836] _id=6aba796b485cab4c9568e075 ts=2026-09-28T14:27:55.4680000Z -> 6aa4140b41b41dbac0c7f229.jsonl[7143] _id=6abbc78e485cab4c957e6e55 ts=2026-09-29T14:13:34.5470000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 145h 38m 
  - Evidence: 145h 38m: 6aa4140b41b41dbac0c7f229.jsonl[1398] _id=6ab52f5c485cab4c9551dd53 ts=2026-09-24T14:10:36.8500000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10486] _id=6abd2f5c485cab4c958d005e ts=2026-09-30T15:48:47.4340000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 145h 37m 
  - Evidence: 145h 37m: 6aa4140b41b41dbac0c7f229.jsonl[1397] _id=6ab52f5c485cab4c9551dd56 ts=2026-09-24T14:10:36.8690000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10505] _id=6abd2f40485cab4c958cffb6 ts=2026-09-30T15:48:19.0920000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 23m 
  - Evidence: 120h 23m: 6aa4140b41b41dbac0c7f229.jsonl[2401] _id=6ab67de6485cab4c9555b060 ts=2026-09-25T13:57:58.4410000Z -> 6aa4140b41b41dbac0c7f229.jsonl[9497] _id=6abd1ade485cab4c958afd6a ts=2026-09-30T14:21:18.0350000Z; 23h 46m: 6aa4140b41b41dbac0c7f229.jsonl[1396] _id=6ab52f59485cab4c9551dd29 ts=2026-09-24T14:10:33.6470000Z -> 6aa4140b41b41dbac0c7f229.jsonl[2344] _id=6ab67db3485cab4c9555a9ee ts=2026-09-25T13:57:07.6670000Z; 1h 18m: 6aa4140b41b41dbac0c7f229.jsonl[9952] _id=6abd1cca485cab4c958b418f ts=2026-09-30T14:29:30.9740000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10507] _id=6abd2f43485cab4c958cffca ts=2026-09-30T15:48:22.4020000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 50 interval(s) ≤ 0.015s..0.018s shown 
  - Evidence: 15ms: 6aa4140b41b41dbac0c7f229.jsonl[10521] _id=6abd2f4e485cab4c958d0008 ts=2026-09-30T15:48:33.2950000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10522] _id=6abd2f4e485cab4c958d000c ts=2026-09-30T15:48:33.3100000Z; 15ms: 6aa4140b41b41dbac0c7f229.jsonl[1315] _id=6ab52ef9485cab4c9551d6e1 ts=2026-09-24T14:08:57.1090000Z -> 6aa4140b41b41dbac0c7f229.jsonl[1321] _id=6ab52ef9485cab4c9551d6e3 ts=2026-09-24T14:08:57.1240000Z; 18ms: 6aa4140b41b41dbac0c7f229.jsonl[1359] _id=6ab52f3f485cab4c9551db91 ts=2026-09-24T14:10:07.0040000Z -> 6aa4140b41b41dbac0c7f229.jsonl[1360] _id=6ab52f3f485cab4c9551db93 ts=2026-09-24T14:10:07.0220000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 120h 12m 
  - Evidence: 120h 12m: 6aa4140b41b41dbac0c7f229.jsonl[2373] _id=6ab67dc2485cab4c9555ac46 ts=2026-09-25T13:57:22.9920000Z -> 6aa4140b41b41dbac0c7f229.jsonl[8954] _id=6abd181e485cab4c958a7280 ts=2026-09-30T14:09:34.2030000Z; 11m 25s: 6aa4140b41b41dbac0c7f229.jsonl[8961] _id=6abd183a485cab4c958a7876 ts=2026-09-30T14:10:02.4990000Z -> 6aa4140b41b41dbac0c7f229.jsonl[9513] _id=6abd1ae7485cab4c958aff48 ts=2026-09-30T14:21:27.5790000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa4140b41b41dbac0c7f229.jsonl[14204] _id=6abe6cd0485cab4c95a846eb ts=2026-10-01T14:23:12.3280000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14714] _id=6ac3abc0de269131f9aa0b81 ts=2026-10-05T13:53:04.0530000Z; 71h 43m: 6aa4140b41b41dbac0c7f229.jsonl[2470] _id=6ab67fca485cab4c9555c76f ts=2026-09-25T14:06:03.7450000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4415] _id=6aba707e485cab4c9568219d ts=2026-09-28T13:49:58.6240000Z; 24h 27m: 6aa4140b41b41dbac0c7f229.jsonl[15881] _id=6ac4fbfbde269131f9b16bc5 ts=2026-10-06T13:47:38.6400000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17102] _id=6ac653d6de269131f9ba81d9 ts=2026-10-07T14:14:46.1490000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa4140b41b41dbac0c7f229.jsonl[14205] _id=6abe6cd0485cab4c95a846e5 ts=2026-10-01T14:23:12.3270000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14715] _id=6ac3abc0de269131f9aa0b79 ts=2026-10-05T13:53:04.0520000Z; 71h 20m: 6aa4140b41b41dbac0c7f229.jsonl[4399] _id=6ab68536485cab4c9556489e ts=2026-09-25T14:29:10.9240000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4414] _id=6aba707e485cab4c95682199 ts=2026-09-28T13:49:58.6230000Z; 24h 0m: 6aa4140b41b41dbac0c7f229.jsonl[16975] _id=6ac50229de269131f9b27b7a ts=2026-10-06T14:14:01.0280000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17101] _id=6ac653d6de269131f9ba81d8 ts=2026-10-07T14:14:46.1490000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 6aa4140b41b41dbac0c7f229.jsonl[14655] _id=6abe6e97485cab4c95a8a957 ts=2026-10-01T14:30:47.7660000Z -> 6aa4140b41b41dbac0c7f229.jsonl[15345] _id=6ac3aefade269131f9aaa117 ts=2026-10-05T14:06:50.3730000Z; 71h 21m: 6aa4140b41b41dbac0c7f229.jsonl[4398] _id=6ab68535485cab4c95564894 ts=2026-09-25T14:29:09.6370000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4442] _id=6aba7092485cab4c95682389 ts=2026-09-28T13:50:18.6080000Z; 24h 0m: 6aa4140b41b41dbac0c7f229.jsonl[7770] _id=6abbcbed485cab4c957ee83d ts=2026-09-29T14:32:13.9030000Z -> 6aa4140b41b41dbac0c7f229.jsonl[10045] _id=6abd1da2485cab4c958b4acf ts=2026-09-30T14:33:06.3850000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4140b41b41dbac0c7f229.jsonl[14528] _id=6abe6e14485cab4c95a88968 ts=2026-10-01T14:28:35.9170000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14721] _id=6ac3abcfde269131f9aa0ec5 ts=2026-10-05T13:53:18.8160000Z; 71h 26m: 6aa4140b41b41dbac0c7f229.jsonl[4033] _id=6ab683de485cab4c95563490 ts=2026-09-25T14:23:26.8290000Z -> 6aa4140b41b41dbac0c7f229.jsonl[4431] _id=6aba7090485cab4c9568231f ts=2026-09-28T13:50:14.4440000Z; 24h 8m: 6aa4140b41b41dbac0c7f229.jsonl[16708] _id=6ac50059de269131f9b25370 ts=2026-10-06T14:06:17.7080000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17105] _id=6ac653e8de269131f9ba8417 ts=2026-10-07T14:15:04.4650000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f229.jsonl[1272] _id=6ab52e8c485cab4c9551d2c7 ts=2026-09-24T14:07:08.1530000Z -> 6aa4140b41b41dbac0c7f229.jsonl[1273] _id=6ab52e8c485cab4c9551d2c9 ts=2026-09-24T14:07:08.1550000Z; 3ms: 6aa4140b41b41dbac0c7f229.jsonl[14940] _id=6ac3acf1de269131f9aa4dc0 ts=2026-10-05T13:58:09.3340000Z -> 6aa4140b41b41dbac0c7f229.jsonl[14941] _id=6ac3acf1de269131f9aa4dc4 ts=2026-10-05T13:58:09.3370000Z; 3ms: 6aa4140b41b41dbac0c7f229.jsonl[16408] _id=6ac4ff32de269131f9b23f55 ts=2026-10-06T14:01:22.6720000Z -> 6aa4140b41b41dbac0c7f229.jsonl[16407] _id=6ac4ff32de269131f9b23f59 ts=2026-10-06T14:01:22.6750000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 24h 10m 
  - Evidence: 24h 10m: 6aa4140b41b41dbac0c7f229.jsonl[16868] _id=6ac501b7de269131f9b26a8c ts=2026-10-06T14:12:07.3930000Z -> 6aa4140b41b41dbac0c7f229.jsonl[17272] _id=6ac65590de269131f9babcb5 ts=2026-10-07T14:22:08.6120000Z; 23h 41m: 6aa4140b41b41dbac0c7f229.jsonl[15750] _id=6ac3b064de269131f9aae8bd ts=2026-10-05T14:12:51.9590000Z -> 6aa4140b41b41dbac0c7f229.jsonl[16065] _id=6ac4fd86de269131f9b1d8ec ts=2026-10-06T13:54:14.7920000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[1212] _id=6ab52e77485cab4c9551d13f ts=2026-09-24T14:06:47.3900000Z`; `6aa4140b41b41dbac0c7f229.jsonl[1405] _id=6ab52f77485cab4c9551de8f ts=2026-09-24T14:11:03.1030000Z`; `6aa4140b41b41dbac0c7f229.jsonl[4505] _id=6aba7194485cab4c956842eb ts=2026-09-28T13:54:32.6250000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 185 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2855] _id=6ab68150485cab4c9555de2c ts=2026-09-25T14:12:30.6620000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2856] _id=6ab68150485cab4c9555de2e ts=2026-09-25T14:12:31.1600000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2857] _id=6ab68151485cab4c9555de30 ts=2026-09-25T14:12:31.4700000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 223 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2696] _id=6ab6813f485cab4c9555db98 ts=2026-09-25T14:10:15.2120000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2707] _id=6ab68140485cab4c9555dbc4 ts=2026-09-25T14:10:16.3630000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2723] _id=6ab68141485cab4c9555dbcc ts=2026-09-25T14:10:16.3710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[10666] _id=6abd2fcc485cab4c958d0284 ts=2026-09-30T15:50:40.7480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[1316] _id=6ab52eeb485cab4c9551d66d ts=2026-09-24T14:08:43.8110000Z`; `6aa4140b41b41dbac0c7f229.jsonl[1321] _id=6ab52ef9485cab4c9551d6e3 ts=2026-09-24T14:08:57.1240000Z`; `6aa4140b41b41dbac0c7f229.jsonl[9505] _id=6abd1adf485cab4c958afdb4 ts=2026-09-30T14:21:19.6860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[14729] _id=6ac3abdbde269131f9aa1148 ts=2026-10-05T13:53:31.0700000Z`; `6aa4140b41b41dbac0c7f229.jsonl[15842] _id=6ac3b340de269131f9aba682 ts=2026-10-05T14:25:04.3970000Z`; `6aa4140b41b41dbac0c7f229.jsonl[15913] _id=6ac4fc88de269131f9b19737 ts=2026-10-06T13:50:00.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[810] _id=6ab52844485cab4c9551459d ts=?`; `6aa4140b41b41dbac0c7f229.jsonl[1836] _id=6ab67c4a485cab4c95559a76 ts=?`; `6aa4140b41b41dbac0c7f229.jsonl[6922] _id=6abbc38f485cab4c957e12ab ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[8950] _id=6abd1816485cab4c958a70cc ts=2026-09-30T14:09:26.0130000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 497 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2871] _id=6ab68153485cab4c9555de68 ts=2026-09-25T14:12:33.2390000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2872] _id=6ab68153485cab4c9555de6a ts=2026-09-25T14:12:33.2390000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2845] _id=6ab68153485cab4c9555de6c ts=2026-09-25T14:12:33.2560000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 527 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2719] _id=6ab68140485cab4c9555dbaa ts=2026-09-25T14:10:15.5310000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2668] _id=6ab68140485cab4c9555dbc2 ts=2026-09-25T14:10:16.3630000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2710] _id=6ab68141485cab4c9555dbe4 ts=2026-09-25T14:10:16.4310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 18 open, 17 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 334 start, 325 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 179 unmatched 'BecameCameraCentered' (totals: 662 open, 668 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 147 unmatched 'BecameVisible' (totals: 725 open, 801 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 49 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 355 of 17715 adjacent _id pairs reverse in client time; worst 128.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f229.jsonl[2714] _id=6ab6813e485cab4c9555db8a ts=2026-09-25T14:12:14.5680000Z`; `6aa4140b41b41dbac0c7f229.jsonl[2695] _id=6ab6813f485cab4c9555db94 ts=2026-09-25T14:10:06.3320000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.02s, min -129.17s, max +8.11s over 17716 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f229\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
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
  - Observed: 6 records 
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

### `InputEvent` — 9828 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2923); Unit 4 Dev - Dungeon (2598); Unit 1 Dev (1556); Unit 2 Prod (Refactor) (1429); Unit 4 Dev (674); Unit 3 Dungeon Dev (648)
- **Intervals:** median 0.35s (p5 0.03s / p95 3.46s, n=9827)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 9828/9828 records)
    "pressed"  x9828
data.actionType  (string, 9828/9828 records)
    "Move"  x7535
    "Interact"  x872
    "Jump"  x438
    "Sprint"  x383
    "Hoverboard"  x278
    "Map"  x139
    "Ascend"  x76
    "Descend"  x57
    "ToggleDebug"  x32
    "Pause"  x14
    "SkipCinematic"  x4
data.key  (string, 9828/9828 records, 97 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 9828/9828 records)
    "Player"  x8451
    "Drone"  x1377
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2856 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2080); Unit 4 Dev (440); Unit 3 Dungeon Dev (336)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.81s, n=2855)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2856/2856 records)
    "BecameInvisible"  x801
    "BecameVisible"  x725
    "BecameCameraUncentered"  x668
    "BecameCameraCentered"  x662
data.pieceId  (string, 2856/2856 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2856/2856 records)
    1588 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2032 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (552); Unit 4 Dev - Dungeon (512); Unit 2 Prod (Refactor) (418); Unit 1 Dev (372); Unit 3 Dungeon Dev (93); Unit 4 Dev (85)
- **Intervals:** median 10.00s (p5 9.98s / p95 12.22s, n=2025)
- **Fields under `data`:**

```text
data.position  (object, 2032/2032 records)
data.position.x  (number, 2032/2032 records)
    numeric range -678.701 .. 1452.37 (666 unique)
data.position.y  (number, 2032/2032 records)
    numeric range -115.127 .. 175.054 (512 unique)
data.position.z  (number, 2032/2032 records)
    numeric range -1029.62 .. 1854.58 (665 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1692 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (603); Unit 2 Prod (Refactor) (434); Unit 1 Dev (254); Unit 4 Dev - Dungeon (236); Unit 3 Dungeon Dev (131); Unit 4 Dev (34)
- **eventKey:** present on 1033 of 1692 records
- **Intervals:** median 4.01s (p5 0.00s / p95 47.53s, n=1691)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1033; [conversationId, dialogueEventType] x659
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1692/1692 records)
    numeric range 8 .. 111 (38 unique)
data.dialogueEventType  (string, 1692/1692 records)
    "DialogueNodeEvent"  x1033
    "DialogueStartEvent"  x334
    "DialogueFinishEvent"  x325
data.nodeId  (number, 1033/1692 records)
    numeric range 0 .. 290 (215 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 390 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (218); Unit 1 Dev (59); Unit 3 Dungeon Dev (47); Unit 2 Prod (Refactor) (44); Unit 3 Dev (18); Unit 4 Dev (4)
- **Intervals:** median 5.42s (p5 0.26s / p95 341.16s, n=389)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 390/390 records)
    28 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 390/390 records)
    71 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 244 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (137); Unit 1 Dev (107)
- **Intervals:** median 0.41s (p5 0.03s / p95 7.82s, n=243)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 244/244 records)
    "argumentationNodeHoverEnd"  x110
    "argumentationNodeHoverStart"  x106
    "argumentationNodeAdd"  x17
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 244/244 records)
    "Unit 3 - Pollution Upstream"  x137
    "Unit 1 - Freshwater"  x81
    "Unit 1 - Argumentation Tutorial"  x26
data.nodeName  (string, 244/244 records)
    "A"  x48
    "I"  x47
    "1"  x44
    "2"  x32
    "II"  x23
    "B"  x20
    "3"  x17
    "4"  x8
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 235 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (169); Unit 2 Prod (Refactor) (41); Unit 1 Dev (13); Unit 4 Dev (6); Unit 4 Dev - Dungeon (6)
- **Intervals:** median 2.63s (p5 0.58s / p95 701.23s, n=234)
- **`data` key-set variants:** [actionType, featureUsed] x212; [actionType, featureUsed, location] x18; [actionType, featureUsed, legendName] x5
- **Fields under `data`:**

```text
data.actionType  (string, 235/235 records)
    "MapCloseEvent"  x106
    "MapOpenEvent"  x106
    "WaypointMoveEvent"  x9
    "WaypointSetEvent"  x7
    "Selected"  x4
    "WaypointResetEvent"  x2
    "Unselected"  x1
data.featureUsed  (string, 235/235 records)
    "Map"  x212
    "Waypoint"  x18
    "Legend"  x5
data.legendName  (string, 5/235 records)
    "Teleporter Room"  x3
    "330 ft"  x1
    "360 ft"  x1
data.location  (object, 18/235 records)
data.location.x  (number, 18/235 records)
    numeric range -275.09 .. 442.91 (14 unique)
data.location.y  (number, 18/235 records)
    numeric range -276.5 .. 350.5 (15 unique)
data.location.z  (number, 18/235 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (26); Unit 3 Dev (22); Unit 1 Dev (18); Unit 2 Prod (Refactor) (12); Unit 3 Dungeon Dev (3); Unit 4 Dev (1)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 195.39s (p5 0.00s / p95 84968.82s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x33
data.questID  (string, 82/82 records)
    22 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    22 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/82 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 70 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (36); Unit 2 Prod (Refactor) (18); Unit 4 Dev (16)
- **Intervals:** median 0.89s (p5 0.17s / p95 3936.00s, n=69)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x62; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/70 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/70 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 62/70 records)
    "RightDrag"  x34
    "LeftDrag"  x28
data.currentSoilType  (string, 62/70 records)
    "CLAY"  x12
    "CLAYSAND"  x12
    "SAND"  x12
    "SANDGRAVEL"  x10
    "CLAYROCK"  x9
    "GRAVEL"  x4
    "BEDROCK"  x3
data.isCorrectSelection  (string, 62/70 records)
    "false"  x50
    "true"  x12
data.waterLevelStatus  (string, 62/70 records)
    "TooHigh"  x42
    "Proper"  x10
    "TooLow"  x10
data.waterRetentionChange  (string, 62/70 records)
    "Decrease"  x29
    "Increase"  x21
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 70 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (27); Unit 1 Dev (16); Unit 4 Dev - Dungeon (11); Unit 2 Prod (Refactor) (8); Unit 3 Dev (7); Transition (1)
- **Intervals:** median 138.69s (p5 4.39s / p95 85992.33s, n=69)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 70/70 records)
    true  x70
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 57 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (20); Unit 4 Dev - Dungeon (16); Unit 3 Dev (10); Unit 2 Prod (Refactor) (9); MainMenu (1); Transition (1)
- **Intervals:** median 102.50s (p5 4.02s / p95 85334.67s, n=56)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 57/57 records)
    false  x57
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 44 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (44)
- **Intervals:** median 5.59s (p5 0.62s / p95 526.09s, n=43)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "ChangeCanister"  x44
data.canisterType  (string, 44/44 records)
    "Clay"  x15
    "Bedrock"  x13
    "Gravel"  x9
    "Sand"  x7
data.floor  (string, 44/44 records)
    "4"  x19
    "5"  x19
    "3"  x6
data.machine  (string, 44/44 records)
    "1"  x44
data.row  (string, 44/44 records)
    "TopRow"  x32
    "BottomRow"  x12
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 35 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (24); Unit 1 Dev (11)
- **Intervals:** median 2.56s (p5 0.01s / p95 411.91s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "Open"  x18
    "Close"  x17
data.toolName  (string, 35/35 records, 32 empty-string)
    ""  x32
    "Settings"  x3
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 3 Dev (9); Unit 1 Dev (7); Unit 4 Dev - Dungeon (6); Unit 2 Prod (Refactor) (4); Unit 3 Dungeon Dev (2); MainMenu (1); Unit 4 Dev (1)
- **Intervals:** median 877.71s (p5 46.63s / p95 190143.05s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 26 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (26)
- **Intervals:** median 1566.51s (p5 63.99s / p95 224193.41s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `chatEvent` — 10 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (8); Unit 1 Dev (2)
- **Intervals:** median 3.23s (p5 1.25s / p95 259912.76s, n=9)
- **`data` key-set variants:** [actionType, chatID] x8; [actionKey, chatID] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/10 records)
    "ScrollStop"  x2
data.actionType  (string, 8/10 records)
    "Close"  x3
    "Open"  x3
    "ScrollStart"  x2
data.chatID  (string, 10/10 records)
    "NA"  x5
    "[10-0, 10-198, 10-200, 10-202, 10-204, 10-38]"  x1
    "[10-202, 10-204, 10-38, 10-39, 10-40, 10-212]"  x1
    "[11-27, 11-27, 11-27, 11-27, 11-27]"  x1
    "[11-27, 11-29, 11-27, 11-29, 11-230]"  x1
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 43.19s (p5 9.52s / p95 393232.07s, n=6)
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

### `argumentationAnswerEvent` — 6 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (4); Unit 1 Dev (2)
- **Intervals:** median 51.08s (p5 28.76s / p95 419449.64s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "submitAnswerEvent"  x6
data.answerSubmitted  (string, 6/6 records)
    "A,2,I"  x2
    "1,I"  x1
    "A,1,I"  x1
    "A,3,I"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x3
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x3
data.type  (string, 6/6 records)
    "unhandled_rejection"  x6
data.unitId  (string, 6/6 records)
    "unit4"  x3
    "unit1"  x2
    "unit2"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 3 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 1 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 1/1 records)
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 1/1 records)
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "Unselected" (1x); "WaypointMoveEvent" (9x); "WaypointResetEvent" (2x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (5x); "Waypoint" (18x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (13x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*