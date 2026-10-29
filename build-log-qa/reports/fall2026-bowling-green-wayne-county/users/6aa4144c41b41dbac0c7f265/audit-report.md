# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f265

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f265
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f265.jsonl
- **Records:** 12603 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f265
- **Time span:** 2026-09-23T18:19:15.168000+00:00 .. 2026-10-07T18:49:30.310000+00:00 (336h 30m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f265\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 12603 records, 8 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 94 INFO, 2 NOT_TESTED, 78 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4654 | 36.93 | 1 | 7 | 0 | 2026-09-23T18:19:31.868000+00:00 | 2026-10-07T18:38:15.315000+00:00 | 336h 18m |
| PuzzlePieceVisibleEvent | 2897 | 22.99 | 1 | 3 | 0 | 2026-09-25T18:16:57.165000+00:00 | 2026-10-07T18:27:27.425000+00:00 | 288h 10m |
| PlayerPositionEvent | 1993 | 15.81 | 1 | 7 | 0 | 2026-09-23T18:19:26.789000+00:00 | 2026-10-07T18:49:30.310000+00:00 | 336h 30m |
| DialogueEvent | 1850 | 14.68 | 1 | 7 | 1112 | 2026-09-23T18:19:48.716000+00:00 | 2026-10-07T18:49:07.457000+00:00 | 336h 29m |
| argumentationNodeEvent | 435 | 3.45 | 1 | 3 | 0 | 2026-09-24T17:43:40.414000+00:00 | 2026-10-07T18:49:04.669000+00:00 | 313h 5m |
| ObjectInterEvent | 309 | 2.45 | 1 | 7 | 0 | 2026-09-23T18:24:33.828000+00:00 | 2026-10-07T18:38:21.057000+00:00 | 336h 13m |
| TopographicMapEvent | 168 | 1.33 | 1 | 4 | 0 | 2026-09-24T17:43:26.898000+00:00 | 2026-10-06T18:15:26.115000+00:00 | 288h 31m |
| questEvent | 66 | 0.52 | 1 | 7 | 66 | 2026-09-23T18:19:48.683000+00:00 | 2026-10-07T18:32:51.276000+00:00 | 336h 13m |
| Soil Key Puzzle | 52 | 0.41 | 1 | 3 | 0 | 2026-09-25T18:25:08.529000+00:00 | 2026-10-06T18:20:35.356000+00:00 | 263h 55m |
| argumentationAnswerEvent | 40 | 0.32 | 1 | 3 | 0 | 2026-09-24T18:06:58.173000+00:00 | 2026-10-07T18:49:06.583000+00:00 | 312h 42m |
| soilMachine | 40 | 0.32 | 1 | 1 | 0 | 2026-10-06T18:32:10.590000+00:00 | 2026-10-06T18:40:55.848000+00:00 | 8m 45s |
| DEBUGMenu | 23 | 0.18 | 1 | 8 | 0 | 2026-09-23T18:19:26.783000+00:00 | 2026-10-07T18:32:50.031000+00:00 | 336h 13m |
| gameWindowFocusEvent | 23 | 0.18 | 1 | 4 | 0 | 2026-09-23T18:19:15.168000+00:00 | 2026-10-07T18:24:34.808000+00:00 | 336h 5m |
| gameStartEvent | 17 | 0.13 | 1 | 1 | 0 | 2026-09-23T18:19:15.169000+00:00 | 2026-10-07T18:24:34.808000+00:00 | 336h 5m |
| DaniEvent | 10 | 0.08 | 1 | 3 | 0 | 2026-09-24T17:43:34.924000+00:00 | 2026-09-29T18:24:40.035000+00:00 | 120h 41m |
| argumentationEvent | 8 | 0.06 | 1 | 3 | 0 | 2026-09-24T18:04:40.066000+00:00 | 2026-10-07T18:43:46.409000+00:00 | 312h 39m |
| gameWindowUnfocusEvent | 8 | 0.06 | 1 | 4 | 0 | 2026-09-25T18:19:16.495000+00:00 | 2026-10-06T18:41:25.456000+00:00 | 264h 22m |
| argumentationToolEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-09-24T18:04:38.289000+00:00 | 2026-09-30T18:26:14.583000+00:00 | 144h 21m |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-24T18:10:00.690000+00:00 | 2026-10-05T18:42:13.975000+00:00 | 264h 32m |
| chatEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-24T17:43:48.925000+00:00 | 2026-09-24T17:43:51.391000+00:00 | 2.5s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1969.799s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 952333.285s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.418s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.978s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.722s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2.466s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 66671.755s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 6970.841s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1895.119s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.407s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 10 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E to Collect; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 270 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 8.0x vs baseline. 
  - Observed: 40 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,3,II; A,4,I; A,4,II; B,2,I; B,2,II; C,2,II; C,3,II; D,2,II; D,3,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 435 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [30-33, 30-37] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 8.0x vs baseline. 
  - Observed: 40 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 96 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[177] _id=6ab41a1a485cab4c954f4d8a ts=2026-09-23T18:27:38.4880000Z`; `6aa4144c41b41dbac0c7f265.jsonl[331] _id=6ab41bee485cab4c954f5ad5 ts=2026-09-23T18:35:26.5930000Z`; `6aa4144c41b41dbac0c7f265.jsonl[419] _id=6ab41d2e485cab4c954f64d1 ts=2026-09-23T18:40:46.6140000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questFinishEvent:21' vs expected 'questFinishEvent:23' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[2614] _id=6abaaba3485cab4c956f63c3 ts=2026-09-25T18:25:40.086Z`; `6aa4144c41b41dbac0c7f265.jsonl[2683] _id=6abaaba9485cab4c956f6441 ts=2026-09-25T18:30:01.308Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[21] _id=6ab41823485cab4c954f3af6 ts=2026-09-23T18:19:15.1690000Z`; `6aa4144c41b41dbac0c7f265.jsonl[545] _id=6ab5602a485cab4c95536dff ts=2026-09-24T17:38:50.8050000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1222] _id=6ab567c9485cab4c9554204a ts=2026-09-24T18:11:21.6120000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[19] _id=6ab41823485cab4c954f3af4 ts=2026-09-23T18:19:15.1680000Z`; `6aa4144c41b41dbac0c7f265.jsonl[542] _id=6ab5602a485cab4c95536dfb ts=2026-09-24T17:38:50.8040000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1223] _id=6ab567c9485cab4c95542046 ts=2026-09-24T18:11:21.6110000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1728] _id=6ab6bb24485cab4c955dfdda ts=2026-09-25T18:19:16.4950000Z`; `6aa4144c41b41dbac0c7f265.jsonl[2189] _id=6ab6bb8b485cab4c955e1167 ts=2026-09-25T18:20:59.2810000Z`; `6aa4144c41b41dbac0c7f265.jsonl[2208] _id=6abaab6f485cab4c956f6077 ts=2026-09-25T18:21:00.658Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 18 of 168 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[637] _id=6ab5613e485cab4c955380fd ts=2026-09-24T17:43:26.8980000Z`; `6aa4144c41b41dbac0c7f265.jsonl[638] _id=6ab56146485cab4c955381e3 ts=2026-09-24T17:43:34.9170000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1368] _id=6ab6bab1485cab4c955dea29 ts=2026-09-25T18:17:21.8000000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4653 | 0.0 | 0.71 | 260.203 | 11.979 | 352181.679 | 0.23 | 176 | 10 |
| PuzzlePieceVisibleEvent | 2896 | 0.0 | 0.025 | 358.229 | 1.298 | 352703.929 | 0.17 | 1793 | 9 |
| PlayerPositionEvent | 1982 | 9.763 | 10.0 | 433.422 | 10.351 | 256605.594 | 0.14 | 0 | 9 |
| DialogueEvent | 1849 | 0.0 | 4.593 | 655.143 | 39.598 | 352172.225 | 0.09 | 528 | 10 |
| argumentationNodeEvent | 434 | 0.007 | 0.27 | 2597.06 | 6.539 | 605670.646 | 0.02 | 90 | 3 |
| ObjectInterEvent | 308 | 0.0 | 5.699 | 3929.959 | 401.076 | 352334.63 | 0.02 | 4 | 13 |
| TopographicMapEvent | 167 | 0.101 | 5.418 | 6219.876 | 684.605 | 431307.456 | 0.01 | 0 | 11 |
| questEvent | 65 | 0.001 | 273.836 | 18621.271 | 85098.506 | 352234.015 | 0.0 | 10 | 18 |
| Soil Key Puzzle | 51 | 0.029 | 0.968 | 18629.938 | 86889.35 | 517521.704 | 0.0 | 1 | 3 |
| argumentationAnswerEvent | 39 | 0.202 | 7.978 | 28864.831 | 52016.342 | 605690.479 | 0.0 | 0 | 2 |
| soilMachine | 39 | 0.173 | 1.407 | 13.468 | 45.734 | 225.197 | 4.45 | 0 | 0 |
| DEBUGMenu | 22 | 9.139 | 1969.799 | 55018.329 | 250094.28 | 352165.361 | 0.0 | 0 | 17 |
| gameWindowFocusEvent | 22 | 1.399 | 6970.841 | 54996.347 | 249462.783 | 352763.144 | 0.0 | 0 | 16 |
| gameStartEvent | 16 | 100.77 | 66671.755 | 75619.977 | 282212.16 | 352763.144 | 0.0 | 0 | 14 |
| DaniEvent | 9 | 1.404 | 2.64 | 48273.901 | 243129.418 | 346760.01 | 0.0 | 0 | 2 |
| argumentationEvent | 7 | 0.06 | 54.33 | 160792.335 | 579834.046 | 605681.567 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 7 | 1.377 | 1895.119 | 135961.28 | 464675.868 | 515815.654 | 0.0 | 0 | 5 |
| argumentationToolEvent | 5 | 1.002 | 1.722 | 103939.259 | 415672.321 | 519556.514 | 0.0 | 0 | 1 |
| EndOfUnit | 1 | 952333.285 | 952333.285 | 952333.285 | 952333.285 | 952333.285 | 0.0 | 0 | 1 |
| chatEvent | 1 | 2.466 | 2.466 | 2.466 | 2.466 | 2.466 | 24.33 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[11775] _id=6ac68f15de269131f9bdb9ab ts=2026-10-07T18:27:33.4690000Z == 6aa4144c41b41dbac0c7f265.jsonl[11776] _id=6ac68f15de269131f9bdb9ac ts=2026-10-07T18:27:33.4690000Z`; `6aa4144c41b41dbac0c7f265.jsonl[12062] _id=6ac69052de269131f9bdc074 ts=2026-10-07T18:32:50.2820000Z == 6aa4144c41b41dbac0c7f265.jsonl[12063] _id=6ac69052de269131f9bdc075 ts=2026-10-07T18:32:50.2820000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 145 group(s), 216 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1486] _id=6ab6bb09485cab4c955df863 ts=2026-09-25T18:16:58.1940000Z == 6aa4144c41b41dbac0c7f265.jsonl[1494] _id=6ab6bb0a485cab4c955df865 ts=2026-09-25T18:16:58.1940000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1491] _id=6ab6bb0b485cab4c955df8a0 ts=2026-09-25T18:16:58.5320000Z == 6aa4144c41b41dbac0c7f265.jsonl[1509] _id=6ab6bb0b485cab4c955df8a5 ts=2026-09-25T18:16:58.5320000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1347] _id=6ab6ba9c485cab4c955de67d ts=2026-09-25T18:17:00.7710000Z == 6aa4144c41b41dbac0c7f265.jsonl[1348] _id=6ab6ba9c485cab4c955de67f ts=2026-09-25T18:17:00.7710000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 60 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4144c41b41dbac0c7f265.jsonl[137] _id=6ab4198c485cab4c954f485e ts=2026-09-23T18:25:16.4570000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[136] _id=6ab4198c485cab4c954f4860 ts=2026-09-23T18:25:16.4650000Z`; `463ms: 6aa4144c41b41dbac0c7f265.jsonl[538] _id=6ab5609d485cab4c95537577 ts=2026-09-24T17:40:45.5380000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[541] _id=6ab5609d485cab4c9553758e ts=2026-09-24T17:40:46.0010000Z`; `164ms: 6aa4144c41b41dbac0c7f265.jsonl[541] _id=6ab5609d485cab4c9553758e ts=2026-09-24T17:40:46.0010000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[543] _id=6ab5609e485cab4c955375a1 ts=2026-09-24T17:40:46.1650000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 598 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa4144c41b41dbac0c7f265.jsonl[1505] _id=6ab6bb0b485cab4c955df8cb ts=2026-09-25T18:16:58.6220000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[1506] _id=6ab6bb0b485cab4c955df8cd ts=2026-09-25T18:16:58.6420000Z`; `21ms: 6aa4144c41b41dbac0c7f265.jsonl[1566] _id=6ab6bb0f485cab4c955df97f ts=2026-09-25T18:18:31.7540000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[1571] _id=6ab6bb0f485cab4c955df983 ts=2026-09-25T18:18:31.7750000Z`; `21ms: 6aa4144c41b41dbac0c7f265.jsonl[1607] _id=6ab6bb12485cab4c955dfa29 ts=2026-09-25T18:18:33.6720000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[1608] _id=6ab6bb12485cab4c955dfa2d ts=2026-09-25T18:18:33.6930000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `972ms: 6aa4144c41b41dbac0c7f265.jsonl[3061] _id=6abaad1f485cab4c956f78db ts=2026-09-28T18:08:31.9020000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[3065] _id=6abaad20485cab4c956f78fb ts=2026-09-28T18:08:32.8740000Z`; `654ms: 6aa4144c41b41dbac0c7f265.jsonl[3064] _id=6abaad20485cab4c956f78f5 ts=2026-09-28T18:08:32.5890000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[3063] _id=6abaad21485cab4c956f790f ts=2026-09-28T18:08:33.2430000Z`; `797ms: 6aa4144c41b41dbac0c7f265.jsonl[3065] _id=6abaad20485cab4c956f78fb ts=2026-09-28T18:08:32.8740000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[3066] _id=6abaad21485cab4c956f7923 ts=2026-09-28T18:08:33.6710000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `595ms: 6aa4144c41b41dbac0c7f265.jsonl[12406] _id=6ac69337de269131f9bdfd0e ts=2026-10-07T18:45:11.1220000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[12402] _id=6ac69337de269131f9bdfd37 ts=2026-10-07T18:45:11.7170000Z`; `202ms: 6aa4144c41b41dbac0c7f265.jsonl[12402] _id=6ac69337de269131f9bdfd37 ts=2026-10-07T18:45:11.7170000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[12403] _id=6ac69337de269131f9bdfd3f ts=2026-10-07T18:45:11.9190000Z`; `302ms: 6aa4144c41b41dbac0c7f265.jsonl[12414] _id=6ac6935dde269131f9be0284 ts=2026-10-07T18:45:49.7490000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[12415] _id=6ac6935ede269131f9be0292 ts=2026-10-07T18:45:50.0510000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `60ms: 6aa4144c41b41dbac0c7f265.jsonl[7318] _id=6abd54f0485cab4c95918a46 ts=2026-09-30T18:29:04.7820000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[7319] _id=6abd54f1485cab4c95918a55 ts=2026-09-30T18:29:04.8420000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 54 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `383ms: 6aa4144c41b41dbac0c7f265.jsonl[645] _id=6ab5614d485cab4c955382a7 ts=2026-09-24T17:43:41.6250000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[647] _id=6ab5614d485cab4c955382b9 ts=2026-09-24T17:43:42.0080000Z`; `543ms: 6aa4144c41b41dbac0c7f265.jsonl[646] _id=6ab5614d485cab4c955382ad ts=2026-09-24T17:43:41.7350000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[643] _id=6ab5614e485cab4c955382c7 ts=2026-09-24T17:43:42.2780000Z`; `977ms: 6aa4144c41b41dbac0c7f265.jsonl[1111] _id=6ab566ce485cab4c95540f7a ts=2026-09-24T18:07:10.3210000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[1119] _id=6ab566cf485cab4c95540f92 ts=2026-09-24T18:07:11.2980000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `778ms: 6aa4144c41b41dbac0c7f265.jsonl[11122] _id=6ac54017de269131f9b6a1a9 ts=2026-10-06T18:38:15.4390000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[11127] _id=6ac54018de269131f9b6a1c3 ts=2026-10-06T18:38:16.2170000Z`; `227ms: 6aa4144c41b41dbac0c7f265.jsonl[11127] _id=6ac54018de269131f9b6a1c3 ts=2026-10-06T18:38:16.2170000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[11131] _id=6ac54018de269131f9b6a1cd ts=2026-10-06T18:38:16.4440000Z`; `173ms: 6aa4144c41b41dbac0c7f265.jsonl[11131] _id=6ac54018de269131f9b6a1cd ts=2026-10-06T18:38:16.4440000Z ~ 6aa4144c41b41dbac0c7f265.jsonl[11126] _id=6ac54018de269131f9b6a1dd ts=2026-10-06T18:38:16.6170000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 97h 49m 
  - Evidence: 97h 49m: 6aa4144c41b41dbac0c7f265.jsonl[8470] _id=6abe8744485cab4c95abd098 ts=2026-10-01T16:16:04.9010000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8507] _id=6ac3e6eade269131f9aeb269 ts=2026-10-05T18:05:30.2620000Z; 71h 51m: 6aa4144c41b41dbac0c7f265.jsonl[1246] _id=6ab6b8fc485cab4c955db537 ts=2026-09-25T18:10:04.7790000Z -> 6aa4144c41b41dbac0c7f265.jsonl[2927] _id=6abaabbc485cab4c956f6625 ts=2026-09-28T18:01:28.7690000Z; 24h 8m: 6aa4144c41b41dbac0c7f265.jsonl[2927] _id=6abaabbc485cab4c956f6625 ts=2026-09-28T18:01:28.7690000Z -> 6aa4144c41b41dbac0c7f265.jsonl[4727] _id=6abbfee2485cab4c95841b81 ts=2026-09-29T18:09:38.5590000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 19m 
  - Evidence: 96h 19m: 6aa4144c41b41dbac0c7f265.jsonl[656] _id=6ab56159485cab4c955383ff ts=2026-09-24T17:43:53.2650000Z -> 6aa4144c41b41dbac0c7f265.jsonl[2962] _id=6abaabe1485cab4c956f6679 ts=2026-09-28T18:03:13.2750000Z; 24h 21m: 6aa4144c41b41dbac0c7f265.jsonl[2963] _id=6abaabe3485cab4c956f667b ts=2026-09-28T18:03:15.1000000Z -> 6aa4144c41b41dbac0c7f265.jsonl[4892] _id=6abc0266485cab4c9584672f ts=2026-09-29T18:24:38.6310000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 97h 49m 
  - Evidence: 97h 49m: 6aa4144c41b41dbac0c7f265.jsonl[8497] _id=6abe876c485cab4c95abd332 ts=2026-10-01T16:16:44.8690000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8744] _id=6ac3e719de269131f9aeb4db ts=2026-10-05T18:06:17.0940000Z; 71h 18m: 6aa4144c41b41dbac0c7f265.jsonl[2905] _id=6abaabbb485cab4c956f6607 ts=2026-09-25T18:44:02.869Z -> 6aa4144c41b41dbac0c7f265.jsonl[2951] _id=6abaabbe485cab4c956f6651 ts=2026-09-28T18:02:17.4200000Z; 23h 57m: 6aa4144c41b41dbac0c7f265.jsonl[1236] _id=6ab567f8485cab4c95542212 ts=2026-09-24T18:12:08.7540000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1244] _id=6ab6b8fe485cab4c955db565 ts=2026-09-25T18:10:06.8020000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 528 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f265.jsonl[12315] _id=6ac692ebde269131f9bdf426 ts=2026-10-07T18:43:55.2630000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12316] _id=6ac692ebde269131f9bdf427 ts=2026-10-07T18:43:55.2630000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[12338] _id=6ac692ffde269131f9bdf606 ts=2026-10-07T18:44:14.9390000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12339] _id=6ac692ffde269131f9bdf607 ts=2026-10-07T18:44:14.9390000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[12421] _id=6ac6934ede269131f9be0056 ts=2026-10-07T18:45:34.6200000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12422] _id=6ac6934ede269131f9be0057 ts=2026-10-07T18:45:34.6200000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 264h 32m 
  - Evidence: 264h 32m: 6aa4144c41b41dbac0c7f265.jsonl[1219] _id=6ab56778485cab4c95541d8f ts=2026-09-24T18:10:00.6900000Z -> 6aa4144c41b41dbac0c7f265.jsonl[9726] _id=6ac3ef86de269131f9af48ad ts=2026-10-05T18:42:13.9750000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 97h 49m 
  - Evidence: 97h 49m: 6aa4144c41b41dbac0c7f265.jsonl[8465] _id=6abe8741485cab4c95abd04b ts=2026-10-01T16:16:00.0560000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8513] _id=6ac3e6f6de269131f9aeb2ad ts=2026-10-05T18:05:41.7350000Z; 71h 17m: 6aa4144c41b41dbac0c7f265.jsonl[2910] _id=6abaabbc485cab4c956f6619 ts=2026-09-25T18:44:27.023Z -> 6aa4144c41b41dbac0c7f265.jsonl[2928] _id=6abaabbc485cab4c956f6629 ts=2026-09-28T18:01:35.5040000Z; 23h 58m: 6aa4144c41b41dbac0c7f265.jsonl[1230] _id=6ab567e0485cab4c955420fc ts=2026-09-24T18:11:44.8850000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1247] _id=6ab6b90b485cab4c955db694 ts=2026-09-25T18:10:19.6280000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 176 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f265.jsonl[11773] _id=6ac68f15de269131f9bdb9a9 ts=2026-10-07T18:27:33.4680000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11774] _id=6ac68f15de269131f9bdb9aa ts=2026-10-07T18:27:33.4680000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[11775] _id=6ac68f15de269131f9bdb9ab ts=2026-10-07T18:27:33.4690000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11776] _id=6ac68f15de269131f9bdb9ac ts=2026-10-07T18:27:33.4690000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[11776] _id=6ac68f15de269131f9bdb9ac ts=2026-10-07T18:27:33.4690000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11777] _id=6ac68f15de269131f9bdb9ad ts=2026-10-07T18:27:33.4690000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 97h 52m 
  - Evidence: 97h 52m: 6aa4144c41b41dbac0c7f265.jsonl[8408] _id=6abe86bd485cab4c95abcafa ts=2026-10-01T16:13:49.2290000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8693] _id=6ac3e70cde269131f9aeb41d ts=2026-10-05T18:06:03.8590000Z; 71h 52m: 6aa4144c41b41dbac0c7f265.jsonl[2634] _id=6abaaba2485cab4c956f63b1 ts=2026-09-25T18:25:08.545Z -> 6aa4144c41b41dbac0c7f265.jsonl[3287] _id=6abaaf56485cab4c956fc317 ts=2026-09-28T18:17:58.7220000Z; 24h 6m: 6aa4144c41b41dbac0c7f265.jsonl[1200] _id=6ab5674f485cab4c95541b1d ts=2026-09-24T18:09:19.1520000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1316] _id=6ab6ba52485cab4c955ddb23 ts=2026-09-25T18:15:46.3320000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.007s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f265.jsonl[12133] _id=6ac690eede269131f9bdcd7e ts=2026-10-07T18:35:26.7440000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12134] _id=6ac690eede269131f9bdcd7f ts=2026-10-07T18:35:26.7440000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[12185] _id=6ac69174de269131f9bdd5c1 ts=2026-10-07T18:37:39.9260000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12186] _id=6ac69174de269131f9bdd5c2 ts=2026-10-07T18:37:39.9260000Z; 7ms: 6aa4144c41b41dbac0c7f265.jsonl[759] _id=6ab561a8485cab4c95538ba3 ts=2026-09-24T17:45:12.7030000Z -> 6aa4144c41b41dbac0c7f265.jsonl[760] _id=6ab561a8485cab4c95538ba6 ts=2026-09-24T17:45:12.7100000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 71h 16m 
  - Evidence: 71h 16m: 6aa4144c41b41dbac0c7f265.jsonl[2925] _id=6abaabbc485cab4c956f661d ts=2026-09-25T18:44:43.209Z -> 6aa4144c41b41dbac0c7f265.jsonl[2912] _id=6abaabbc485cab4c956f6627 ts=2026-09-28T18:01:28.8030000Z; 23h 57m: 6aa4144c41b41dbac0c7f265.jsonl[1238] _id=6ab5680b485cab4c955422a8 ts=2026-09-24T18:12:27.6300000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1243] _id=6ab6b8fd485cab4c955db54b ts=2026-09-25T18:10:04.7850000Z; 23h 34m: 6aa4144c41b41dbac0c7f265.jsonl[11618] _id=6ac542c8de269131f9b6f6a7 ts=2026-10-06T18:49:44.0410000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11638] _id=6ac68e71de269131f9bdb6cd ts=2026-10-07T18:24:43.4190000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 97h 58m 
  - Evidence: 97h 58m: 6aa4144c41b41dbac0c7f265.jsonl[8162] _id=6abe852f485cab4c95abbcbc ts=2026-10-01T16:07:08.9680000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8512] _id=6ac3e6efde269131f9aeb299 ts=2026-10-05T18:05:32.8970000Z; 71h 55m: 6aa4144c41b41dbac0c7f265.jsonl[2587] _id=6abaab9e485cab4c956f634f ts=2026-09-25T18:23:22.414Z -> 6aa4144c41b41dbac0c7f265.jsonl[3326] _id=6abaaf8c485cab4c956fcd93 ts=2026-09-28T18:18:52.5190000Z; 47h 47m: 6aa4144c41b41dbac0c7f265.jsonl[4711] _id=6abab64f485cab4c957068bc ts=2026-09-28T18:47:42.8210000Z -> 6aa4144c41b41dbac0c7f265.jsonl[7537] _id=6abd5673485cab4c9591c087 ts=2026-09-30T18:35:30.7880000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1793 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f265.jsonl[10238] _id=6ac53c1dde269131f9b64d2b ts=2026-10-06T18:21:16.3240000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10303] _id=6ac53c1dde269131f9b64d2f ts=2026-10-06T18:21:16.3240000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[10273] _id=6ac53bfbde269131f9b64b07 ts=2026-10-06T18:20:41.9850000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10274] _id=6ac53bfbde269131f9b64b0b ts=2026-10-06T18:20:41.9850000Z; 0ms: 6aa4144c41b41dbac0c7f265.jsonl[10274] _id=6ac53bfbde269131f9b64b0b ts=2026-10-06T18:20:41.9850000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10282] _id=6ac53bfbde269131f9b64b0d ts=2026-10-06T18:20:41.9850000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 45m 
  - Evidence: 143h 45m: 6aa4144c41b41dbac0c7f265.jsonl[7510] _id=6abd5649485cab4c9591bb5f ts=2026-09-30T18:34:49.3700000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10241] _id=6ac53bdbde269131f9b64933 ts=2026-10-06T18:20:11.0740000Z; 71h 52m: 6aa4144c41b41dbac0c7f265.jsonl[2635] _id=6abaaba3485cab4c956f63b3 ts=2026-09-25T18:25:11.531Z -> 6aa4144c41b41dbac0c7f265.jsonl[3294] _id=6abaaf56485cab4c956fc30f ts=2026-09-28T18:17:58.7150000Z; 48h 16m: 6aa4144c41b41dbac0c7f265.jsonl[3305] _id=6abaaf6e485cab4c956fc7fc ts=2026-09-28T18:18:22.2550000Z -> 6aa4144c41b41dbac0c7f265.jsonl[6022] _id=6abd5635485cab4c9591b887 ts=2026-09-30T18:34:29.4770000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.029s..0.029s shown 
  - Evidence: 29ms: 6aa4144c41b41dbac0c7f265.jsonl[10241] _id=6ac53bdbde269131f9b64933 ts=2026-10-06T18:20:11.0740000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10243] _id=6ac53bdbde269131f9b64939 ts=2026-10-06T18:20:11.1030000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6aa4144c41b41dbac0c7f265.jsonl[7464] _id=6abd55cc485cab4c9591a8e3 ts=2026-09-30T18:32:44.1770000Z -> 6aa4144c41b41dbac0c7f265.jsonl[9337] _id=6ac3ea97de269131f9aee92f ts=2026-10-05T18:21:11.6330000Z; 71h 18m: 6aa4144c41b41dbac0c7f265.jsonl[2920] _id=6abaabbb485cab4c956f6609 ts=2026-09-25T18:44:10.084Z -> 6aa4144c41b41dbac0c7f265.jsonl[2820] _id=6abaabd2485cab4c956f6671 ts=2026-09-28T18:02:58.6140000Z; 24h 33m: 6aa4144c41b41dbac0c7f265.jsonl[638] _id=6ab56146485cab4c955381e3 ts=2026-09-24T17:43:34.9170000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1368] _id=6ab6bab1485cab4c955dea29 ts=2026-09-25T18:17:21.8000000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 14m 
  - Evidence: 168h 14m: 6aa4144c41b41dbac0c7f265.jsonl[7316] _id=6abd54f0485cab4c95918a3f ts=2026-09-30T18:29:04.7630000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12314] _id=6ac692ebde269131f9bdf422 ts=2026-10-07T18:43:55.2420000Z; 144h 19m: 6aa4144c41b41dbac0c7f265.jsonl[1114] _id=6ab566d1485cab4c95540fbe ts=2026-09-24T18:07:13.1040000Z -> 6aa4144c41b41dbac0c7f265.jsonl[7225] _id=6abd5477485cab4c9591768d ts=2026-09-30T18:27:03.2980000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 14m 
  - Evidence: 168h 14m: 6aa4144c41b41dbac0c7f265.jsonl[7319] _id=6abd54f1485cab4c95918a55 ts=2026-09-30T18:29:04.8420000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12281] _id=6ac692e2de269131f9bdf31a ts=2026-10-07T18:43:46.4090000Z; 144h 18m: 6aa4144c41b41dbac0c7f265.jsonl[1122] _id=6ab566d1485cab4c95540fc0 ts=2026-09-24T18:07:13.1270000Z -> 6aa4144c41b41dbac0c7f265.jsonl[7094] _id=6abd5434485cab4c95916d4b ts=2026-09-30T18:25:56.2890000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 14m 
  - Evidence: 168h 14m: 6aa4144c41b41dbac0c7f265.jsonl[7313] _id=6abd54ea485cab4c95918946 ts=2026-09-30T18:28:58.9070000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12275] _id=6ac692d1de269131f9bdf10b ts=2026-10-07T18:43:29.5530000Z; 144h 18m: 6aa4144c41b41dbac0c7f265.jsonl[1121] _id=6ab566cf485cab4c95540f98 ts=2026-09-24T18:07:11.5420000Z -> 6aa4144c41b41dbac0c7f265.jsonl[7095] _id=6abd542f485cab4c95916c6b ts=2026-09-30T18:25:51.0750000Z; 20m 6s: 6aa4144c41b41dbac0c7f265.jsonl[643] _id=6ab5614e485cab4c955382c7 ts=2026-09-24T17:43:42.2780000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1021] _id=6ab56604485cab4c9553fa78 ts=2026-09-24T18:03:48.6560000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 90 interval(s) ≤ 0.007s..0.021s shown 
  - Evidence: 7ms: 6aa4144c41b41dbac0c7f265.jsonl[12539] _id=6ac693f3de269131f9be17f7 ts=2026-10-07T18:48:19.5910000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12538] _id=6ac693f3de269131f9be17f9 ts=2026-10-07T18:48:19.5980000Z; 20ms: 6aa4144c41b41dbac0c7f265.jsonl[12525] _id=6ac693eade269131f9be16b3 ts=2026-10-07T18:48:10.4420000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12520] _id=6ac693eade269131f9be16b9 ts=2026-10-07T18:48:10.4620000Z; 21ms: 6aa4144c41b41dbac0c7f265.jsonl[12374] _id=6ac69320de269131f9bdf9f3 ts=2026-10-07T18:44:48.7900000Z -> 6aa4144c41b41dbac0c7f265.jsonl[12377] _id=6ac69320de269131f9bdf9f7 ts=2026-10-07T18:44:48.8110000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 19m 
  - Evidence: 144h 19m: 6aa4144c41b41dbac0c7f265.jsonl[1107] _id=6ab566c2485cab4c95540e0a ts=2026-09-24T18:06:58.0690000Z -> 6aa4144c41b41dbac0c7f265.jsonl[7137] _id=6abd5446485cab4c95916fce ts=2026-09-30T18:26:14.5830000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 97h 59m 
  - Evidence: 97h 59m: 6aa4144c41b41dbac0c7f265.jsonl[7999] _id=6abe84e3485cab4c95abb6c8 ts=2026-10-01T16:05:54.8380000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8505] _id=6ac3e6dede269131f9aeb19d ts=2026-10-05T18:05:17.9820000Z; 71h 51m: 6aa4144c41b41dbac0c7f265.jsonl[1242] _id=6ab6b8e9485cab4c955db40d ts=2026-09-25T18:09:45.1460000Z -> 6aa4144c41b41dbac0c7f265.jsonl[2926] _id=6abaabbc485cab4c956f6623 ts=2026-09-28T18:01:20.3110000Z; 24h 8m: 6aa4144c41b41dbac0c7f265.jsonl[10181] _id=6ac53afade269131f9b63cef ts=2026-10-06T18:16:26.4770000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11637] _id=6ac68e62de269131f9bdb6b6 ts=2026-10-07T18:24:34.8080000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 97h 59m 
  - Evidence: 97h 59m: 6aa4144c41b41dbac0c7f265.jsonl[8000] _id=6abe84e2485cab4c95abb6be ts=2026-10-01T16:05:54.8370000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8504] _id=6ac3e6dede269131f9aeb19b ts=2026-10-05T18:05:17.9810000Z; 71h 40m: 6aa4144c41b41dbac0c7f265.jsonl[2209] _id=6abaab70485cab4c956f6079 ts=2026-09-25T18:21:00.77Z -> 6aa4144c41b41dbac0c7f265.jsonl[2911] _id=6abaabbc485cab4c956f6621 ts=2026-09-28T18:01:20.2590000Z; 24h 8m: 6aa4144c41b41dbac0c7f265.jsonl[2911] _id=6abaabbc485cab4c956f6621 ts=2026-09-28T18:01:20.2590000Z -> 6aa4144c41b41dbac0c7f265.jsonl[4726] _id=6abbfed5485cab4c95841b73 ts=2026-09-29T18:09:25.6340000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 16m 
  - Evidence: 143h 16m: 6aa4144c41b41dbac0c7f265.jsonl[6008] _id=6abc07f9485cab4c9584c92d ts=2026-09-29T18:48:25.4790000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8502] _id=6ac3e6e1de269131f9aeb1f7 ts=2026-10-05T18:05:21.1330000Z; 95h 55m: 6aa4144c41b41dbac0c7f265.jsonl[2208] _id=6abaab6f485cab4c956f6077 ts=2026-09-25T18:21:00.658Z -> 6aa4144c41b41dbac0c7f265.jsonl[4773] _id=6abc0092485cab4c9584398d ts=2026-09-29T18:16:50.3600000Z; 24h 20m: 6aa4144c41b41dbac0c7f265.jsonl[9327] _id=6ac3ea72de269131f9aee5fd ts=2026-10-05T18:20:34.3700000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11338] _id=6ac540d5de269131f9b6b889 ts=2026-10-06T18:41:25.4560000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 97h 50m 
  - Evidence: 97h 50m: 6aa4144c41b41dbac0c7f265.jsonl[8450] _id=6abe8704485cab4c95abcd24 ts=2026-10-01T16:15:00.3280000Z -> 6aa4144c41b41dbac0c7f265.jsonl[8508] _id=6ac3e6efde269131f9aeb289 ts=2026-10-05T18:05:34.3430000Z; 71h 22m: 6aa4144c41b41dbac0c7f265.jsonl[2830] _id=6abaabb4485cab4c956f6569 ts=2026-09-25T18:39:06.653Z -> 6aa4144c41b41dbac0c7f265.jsonl[2929] _id=6abaabbd485cab4c956f662d ts=2026-09-28T18:01:35.6530000Z; 24h 3m: 6aa4144c41b41dbac0c7f265.jsonl[1203] _id=6ab56751485cab4c95541b56 ts=2026-09-24T18:09:21.3140000Z -> 6aa4144c41b41dbac0c7f265.jsonl[1276] _id=6ab6b9bc485cab4c955dcafb ts=2026-09-25T18:13:16.8050000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f265.jsonl[11640] _id=6ac68e71de269131f9bdb6cf ts=2026-10-07T18:24:48.4360000Z -> 6aa4144c41b41dbac0c7f265.jsonl[11641] _id=6ac68e71de269131f9bdb6d0 ts=2026-10-07T18:24:48.4370000Z; 6ms: 6aa4144c41b41dbac0c7f265.jsonl[10675] _id=6ac53d0dde269131f9b65edf ts=2026-10-06T18:25:17.7790000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10676] _id=6ac53d0dde269131f9b65ee3 ts=2026-10-06T18:25:17.7850000Z; 6ms: 6aa4144c41b41dbac0c7f265.jsonl[10830] _id=6ac53e28de269131f9b670c4 ts=2026-10-06T18:30:00.1860000Z -> 6aa4144c41b41dbac0c7f265.jsonl[10822] _id=6ac53e28de269131f9b670c7 ts=2026-10-06T18:30:00.1920000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[999] _id=6ab565c4485cab4c9553efce ts=2026-09-24T18:02:44.1440000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1130] _id=6ab566e3485cab4c9554119e ts=2026-09-24T18:07:31.1300000Z`; `6aa4144c41b41dbac0c7f265.jsonl[4008] _id=6abab170485cab4c956ffd0b ts=2026-09-28T18:26:56.2890000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 383 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1711] _id=6ab6bb1f485cab4c955dfce9 ts=2026-09-25T18:19:09.8580000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1769] _id=6ab6bb31485cab4c955dffb2 ts=2026-09-25T18:19:28.3160000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1879] _id=6ab6bb45485cab4c955e03db ts=2026-09-25T18:19:48.2590000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 169 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1516] _id=6ab6bb0b485cab4c955df8b5 ts=2026-09-25T18:16:58.5410000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1542] _id=6ab6bb0e485cab4c955df94f ts=2026-09-25T18:17:00.5550000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1553] _id=6ab6bb0f485cab4c955df955 ts=2026-09-25T18:17:00.5550000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Finished' preceded by 'Started' per Unit 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[2629] _id=6abaaba2485cab4c956f63af ts=2026-09-25T18:25:08.529Z`; `6aa4144c41b41dbac0c7f265.jsonl[2635] _id=6abaaba3485cab4c956f63b3 ts=2026-09-25T18:25:11.531Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[2832] _id=6abaabb5485cab4c956f6575 ts=2026-09-25T18:39:23.962Z`; `6aa4144c41b41dbac0c7f265.jsonl[2849] _id=6abaabb5485cab4c956f6583 ts=2026-09-25T18:40:03.035Z`; `6aa4144c41b41dbac0c7f265.jsonl[2903] _id=6abaabbb485cab4c956f6601 ts=2026-09-25T18:43:52.08Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[7319] _id=6abd54f1485cab4c95918a55 ts=2026-09-30T18:29:04.8420000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[7116] _id=6abd5474485cab4c959175ef ts=2026-09-30T18:27:00.3640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[2614] _id=6abaaba3485cab4c956f63c3 ts=2026-09-25T18:25:40.086Z`; `6aa4144c41b41dbac0c7f265.jsonl[2753] _id=6abaabb4485cab4c956f655b ts=2026-09-25T18:38:32.795Z`; `6aa4144c41b41dbac0c7f265.jsonl[10675] _id=6ac53d0dde269131f9b65edf ts=2026-10-06T18:25:17.7790000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 358 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1628] _id=6ab6bb14485cab4c955dfabf ts=2026-09-25T18:18:43.5030000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1638] _id=6ab6bb15485cab4c955dfad1 ts=2026-09-25T18:18:43.6540000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1621] _id=6ab6bb15485cab4c955dfad3 ts=2026-09-25T18:18:43.7210000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 491 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1450] _id=6ab6bb08485cab4c955df7ed ts=2026-09-25T18:16:57.7320000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1475] _id=6ab6bb09485cab4c955df837 ts=2026-09-25T18:16:58.1350000Z`; `6aa4144c41b41dbac0c7f265.jsonl[1494] _id=6ab6bb0a485cab4c955df865 ts=2026-09-25T18:16:58.1940000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 39 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[6050] _id=6abd4efe485cab4c9590d3e7 ts=2026-09-30T18:03:42.0640000Z`; `6aa4144c41b41dbac0c7f265.jsonl[6029] _id=6abd4f05485cab4c9590d40b ts=2026-09-30T18:03:49.7850000Z`; `6aa4144c41b41dbac0c7f265.jsonl[6755] _id=6abd51be485cab4c95910b6d ts=2026-09-30T18:15:26.5970000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[1106] _id=6ab566c0485cab4c95540dec ts=2026-09-24T18:06:56.5610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 372 start, 366 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 110 unmatched 'BecameCameraCentered' (totals: 528 open, 801 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 87 unmatched 'BecameVisible' (totals: 743 open, 825 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 62 open, 65 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 4 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 41 start, 25 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 208 of 12602 adjacent _id pairs reverse in client time; worst 77969.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f265.jsonl[8499] _id=6abe876d485cab4c95abd34a ts=2026-10-01T16:16:45.9430000Z`; `6aa4144c41b41dbac0c7f265.jsonl[8503] _id=6ac3e6dede269131f9aeb191 ts=2026-09-30T18:37:16.222Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -430081.93s, max +1.20s over 12603 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f265\coverage.yaml

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
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `InputEvent` — 4654 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1916); Unit 2 Prod (Refactor) (667); Unit 4 Dev (625); Unit 3 Dungeon Dev (496); Unit 4 Dev - Dungeon (433); Unit 1 Dev (427); Unit 4 Dev - Anderson Base (90)
- **Intervals:** median 0.71s (p5 0.08s / p95 11.98s, n=4653)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4654/4654 records)
    "pressed"  x4654
data.actionType  (string, 4654/4654 records)
    "Move"  x3419
    "Interact"  x564
    "Jump"  x364
    "Sprint"  x83
    "Hoverboard"  x73
    "Ascend"  x71
    "Map"  x55
    "Descend"  x16
    "SkipCinematic"  x8
    "ToggleDebug"  x1
data.key  (string, 4654/4654 records, 21 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4654/4654 records)
    "Player"  x2866
    "Drone"  x1788
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2897 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1778); Unit 3 Dungeon Dev (667); Unit 4 Dev (452)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.30s, n=2896)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2897/2897 records)
    "BecameInvisible"  x825
    "BecameCameraUncentered"  x801
    "BecameVisible"  x743
    "BecameCameraCentered"  x528
data.pieceId  (string, 2897/2897 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2897/2897 records)
    1605 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1993 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (517); Unit 3 Dev (502); Unit 1 Dev (344); Unit 4 Dev (230); Unit 3 Dungeon Dev (184); Unit 4 Dev - Dungeon (115); Unit 4 Dev - Anderson Base (101)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.35s, n=1982)
- **Fields under `data`:**

```text
data.position  (object, 1993/1993 records)
data.position.x  (number, 1993/1993 records)
    numeric range -813.212 .. 1456.51 (578 unique)
data.position.y  (number, 1993/1993 records)
    numeric range -112.487 .. 173.877 (462 unique)
data.position.z  (number, 1993/1993 records)
    numeric range -1048.33 .. 2287.45 (579 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1850 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (524); Unit 2 Prod (Refactor) (449); Unit 3 Dungeon Dev (282); Unit 1 Dev (268); Unit 4 Dev (145); Unit 4 Dev - Anderson Base (100); Unit 4 Dev - Dungeon (82)
- **eventKey:** present on 1112 of 1850 records
- **Intervals:** median 4.59s (p5 0.00s / p95 39.60s, n=1849)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1112; [conversationId, dialogueEventType] x738
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1850/1850 records)
    numeric range 8 .. 107 (40 unique)
data.dialogueEventType  (string, 1850/1850 records)
    "DialogueNodeEvent"  x1112
    "DialogueStartEvent"  x372
    "DialogueFinishEvent"  x366
data.nodeId  (number, 1112/1850 records)
    numeric range 0 .. 290 (216 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 435 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (219); Unit 3 Dev (153); Unit 1 Dev (63)
- **Intervals:** median 0.27s (p5 0.03s / p95 6.54s, n=434)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 435/435 records)
    "argumentationNodeHoverEnd"  x182
    "argumentationNodeHoverStart"  x181
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x31
data.argumentationTitle  (string, 435/435 records)
    "Unit 4 - Flooding"  x219
    "Unit 3 - Pollution Upstream"  x153
    "Unit 1 - Freshwater"  x47
    "Unit 1 - Argumentation Tutorial"  x16
data.nodeName  (string, 435/435 records)
    "3"  x60
    "II"  x59
    "I"  x48
    "A"  x46
    "2"  x43
    "B"  x42
    "4"  x40
    "1"  x35
    "C"  x33
    "D"  x20
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 309 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (103); Unit 3 Dungeon Dev (75); Unit 1 Dev (73); Unit 2 Prod (Refactor) (25); Unit 3 Dev (12); Unit 4 Dev (12); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 5.70s (p5 0.16s / p95 401.08s, n=308)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 309/309 records)
    32 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 309/309 records)
    77 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 168 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (69); Unit 3 Dev (68); Unit 4 Dev (29); Unit 1 Dev (2)
- **Intervals:** median 5.42s (p5 0.56s / p95 684.61s, n=167)
- **`data` key-set variants:** [actionType, featureUsed] x127; [actionType, featureUsed, location] x23; [actionType, featureUsed, legendName] x18
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 168/168 records)
    "MapCloseEvent"  x65
    "MapOpenEvent"  x62
    "WaypointMoveEvent"  x18
    "Selected"  x12
    "Unselected"  x6
    "WaypointSetEvent"  x5
data.featureUsed  (string, 168/168 records)
    "Map"  x127
    "Waypoint"  x23
    "Legend"  x18
data.legendName  (string, 18/168 records)
    "Water"  x9
    "0 ft"  x3
    "90 ft"  x3
    "270 ft"  x1
    "360 ft"  x1
    "60 ft"  x1
data.location  (object, 23/168 records)
data.location.x  (number, 23/168 records)
    numeric range -653.09 .. 106.91 (22 unique)
data.location.y  (number, 23/168 records)
    numeric range -285.5 .. 179.5 (20 unique)
data.location.z  (number, 23/168 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 66 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 3 Dev (12); Unit 2 Prod (Refactor) (11); Unit 4 Dev (11); Unit 4 Dev - Dungeon (8); Unit 3 Dungeon Dev (6); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 66 of 66 records
- **Intervals:** median 273.84s (p5 0.01s / p95 85098.51s, n=65)
- **`data` key-set variants:** [questEventType, questID, questName] x41; [questEventType, questID, questName, questSuccessOrFailure] x25
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 66/66 records)
    "questActiveEvent"  x41
    "questFinishEvent"  x25
data.questID  (string, 66/66 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 66/66 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 25/66 records)
    "Succeeded"  x25
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 52 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (22); Unit 3 Dev (18); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 0.97s (p5 0.20s / p95 86889.35s, n=51)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/52 records)
    "Finished"  x5
    "Started"  x3
data.Unit  (string, 8/52 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 44/52 records)
    "RightDrag"  x25
    "LeftDrag"  x19
data.currentSoilType  (string, 44/52 records)
    "CLAY"  x9
    "CLAYSAND"  x9
    "CLAYROCK"  x8
    "SAND"  x8
    "SANDGRAVEL"  x5
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 44/52 records)
    "false"  x33
    "true"  x11
data.waterLevelStatus  (string, 44/52 records)
    "Proper"  x26
    "TooHigh"  x13
    "TooLow"  x5
data.waterRetentionChange  (string, 44/52 records)
    "Increase"  x17
    "Decrease"  x16
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 40 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (28); Unit 3 Dev (10); Unit 1 Dev (2)
- **Intervals:** median 7.98s (p5 0.57s / p95 52016.34s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "submitAnswerEvent"  x40
data.answerSubmitted  (string, 40/40 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 40/40 records)
    "Unit 4 - Flooding"  x28
    "Unit 3 - Pollution Upstream"  x10
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 40 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (40)
- **Intervals:** median 1.41s (p5 0.22s / p95 45.73s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "ChangeCanister"  x40
data.canisterType  (string, 40/40 records)
    "Bedrock"  x22
    "Clay"  x15
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 40/40 records)
    "5"  x38
    "3"  x1
    "4"  x1
data.machine  (string, 40/40 records)
    "1"  x39
    "2"  x1
data.row  (string, 40/40 records)
    "BottomRow"  x21
    "TopRow"  x19
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (6); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 3 Dungeon Dev (4); Unit 1 Dev (2); MainMenu (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1969.80s (p5 115.93s / p95 250094.28s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 23 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (3); Unit 3 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 6970.84s (p5 10.85s / p95 249462.78s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 66671.75s (p5 387.55s / p95 282212.16s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 10 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (6); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 2.64s (p5 1.57s / p95 243129.42s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "Close"  x5
    "Open"  x5
data.toolName  (string, 10/10 records, 10 empty-string)
    ""  x10
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 54.33s (p5 14.16s / p95 579834.05s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); MainMenu (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1895.12s (p5 31.80s / p95 464675.87s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 3 Dev (1)
- **Intervals:** median 1.72s (p5 1.10s / p95 415672.32s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 952333.29s (p5 952333.29s / p95 952333.29s, n=1)
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

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 2.47s (p5 2.47s / p95 2.47s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[30-33, 30-37]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TopographicMapEvent` data.actionType: "Selected" (12x); "Unselected" (6x); "WaypointMoveEvent" (18x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (18x); "Waypoint" (23x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (31x)
- `soilMachine` data.canisterType: "Bedrock" (22x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*