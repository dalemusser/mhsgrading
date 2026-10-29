# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae7

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae7
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae7.jsonl
- **Records:** 8501 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae7
- **Time span:** 2026-10-06T13:14:29.819000+00:00 .. 2026-10-19T05:19:49.220000+00:00 (304h 5m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae7\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 8501 records, 6 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 94 INFO, 2 NOT_TESTED, 72 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2558 | 30.09 | 1 | 2 | 0 | 2026-10-06T13:49:48.852000+00:00 | 2026-10-19T03:50:50.406000+00:00 | 302h 1m |
| PlayerPositionEvent | 1928 | 22.68 | 1 | 5 | 0 | 2026-10-06T13:14:39.341000+00:00 | 2026-10-19T05:19:49.220000+00:00 | 304h 5m |
| InputEvent | 1811 | 21.3 | 1 | 4 | 0 | 2026-10-06T13:14:42.828000+00:00 | 2026-10-19T04:30:04.182000+00:00 | 303h 15m |
| DialogueEvent | 1542 | 18.14 | 1 | 5 | 962 | 2026-10-06T13:14:59.355000+00:00 | 2026-10-19T04:31:53.938000+00:00 | 303h 16m |
| argumentationNodeEvent | 183 | 2.15 | 1 | 3 | 0 | 2026-10-06T13:37:55.713000+00:00 | 2026-10-16T13:39:23.307000+00:00 | 240h 1m |
| ObjectInterEvent | 171 | 2.01 | 1 | 4 | 0 | 2026-10-06T13:19:49.335000+00:00 | 2026-10-19T04:30:16.120000+00:00 | 303h 10m |
| TopographicMapEvent | 104 | 1.22 | 1 | 2 | 0 | 2026-10-06T13:50:31.794000+00:00 | 2026-10-19T04:23:00.103000+00:00 | 302h 32m |
| Soil Key Puzzle | 46 | 0.54 | 1 | 2 | 0 | 2026-10-06T13:56:53.225000+00:00 | 2026-10-16T13:43:18.916000+00:00 | 239h 46m |
| questEvent | 45 | 0.53 | 1 | 4 | 45 | 2026-10-06T13:14:59.327000+00:00 | 2026-10-19T04:30:21.289000+00:00 | 303h 15m |
| DEBUGMenu | 25 | 0.29 | 1 | 6 | 0 | 2026-10-06T13:14:39.319000+00:00 | 2026-10-19T04:31:36.688000+00:00 | 303h 16m |
| DaniEvent | 22 | 0.26 | 1 | 2 | 0 | 2026-10-14T13:58:17.357000+00:00 | 2026-10-16T13:31:07.354000+00:00 | 47h 32m |
| gameStartEvent | 13 | 0.15 | 1 | 1 | 0 | 2026-10-06T13:14:29.820000+00:00 | 2026-10-19T04:30:42.799000+00:00 | 303h 16m |
| gameWindowFocusEvent | 13 | 0.15 | 1 | 1 | 0 | 2026-10-06T13:14:29.819000+00:00 | 2026-10-19T04:30:42.799000+00:00 | 303h 16m |
| argumentationEvent | 9 | 0.11 | 1 | 3 | 0 | 2026-10-06T13:38:38.284000+00:00 | 2026-10-16T13:39:25.655000+00:00 | 240h 0m |
| argumentationAnswerEvent | 8 | 0.09 | 1 | 3 | 0 | 2026-10-06T13:39:16.754000+00:00 | 2026-10-16T13:39:25.595000+00:00 | 240h 0m |
| argumentationToolEvent | 8 | 0.09 | 1 | 3 | 0 | 2026-10-06T13:38:33.714000+00:00 | 2026-10-16T13:38:36.013000+00:00 | 240h 0m |
| chatEvent | 6 | 0.07 | 1 | 2 | 0 | 2026-10-15T13:25:10.150000+00:00 | 2026-10-16T13:26:34.948000+00:00 | 24h 1m |
| gameWindowUnfocusEvent | 6 | 0.07 | 1 | 2 | 0 | 2026-10-06T13:59:31.480000+00:00 | 2026-10-16T13:59:14.292000+00:00 | 239h 59m |
| EndOfUnit | 3 | 0.04 | 1 | 3 | 0 | 2026-10-06T13:44:03.024000+00:00 | 2026-10-19T04:30:29.433000+00:00 | 302h 46m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 544993.204s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.399s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 14.309s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.087s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.39s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 48.307s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 8.406s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 12.629s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 14476.108s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 14476.108s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 48940.268s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 22 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
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
  - Observed: Press E; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,1,; B,1,I; D,1,II; I 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-218, 11-224, 11-226, 11-23, 11-24]; [22-46, 22-48, 22-27, 18-287, 18-289] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
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
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[161] _id=6ac4f5fcde269131f9b04cc2 ts=2026-10-06T13:22:04.3930000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[207] _id=6ac4f6d6de269131f9b07c2c ts=2026-10-06T13:25:41.8820000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[257] _id=6ac4f7a3de269131f9b09c5f ts=2026-10-06T13:29:06.5510000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[5] _id=6ac4f436de269131f9b02f68 ts=2026-10-06T13:14:29.8200000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[548] _id=6ac4fb78de269131f9b1501b ts=2026-10-06T13:45:28.2390000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[1518] _id=6acf8773de269131f9d3559d ts=2026-10-14T13:45:22.7010000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[7] _id=6ac4f436de269131f9b02f66 ts=2026-10-06T13:14:29.8190000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[547] _id=6ac4fb78de269131f9b15016 ts=2026-10-06T13:45:28.2380000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[1517] _id=6acf8773de269131f9d3559c ts=2026-10-14T13:45:22.7010000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[1519] _id=6acf8773de269131f9d35590 ts=2026-10-06T13:59:31.48Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[2519] _id=6acfa67cde269131f9d50763 ts=2026-10-14T14:00:02.407Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[2749] _id=6ad0d076de269131f9da4e5d ts=2026-10-14T16:10:11.214Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 5 of 104 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[708] _id=6ac4fca8de269131f9b1a0ed ts=2026-10-06T13:50:31.7940000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[624] _id=6ac4fcafde269131f9b1a35a ts=2026-10-06T13:50:39.5360000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[695] _id=6ac4fcc2de269131f9b1a823 ts=2026-10-06T13:50:57.4130000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2557 | 0.0 | 0.087 | 425.21 | 2.332 | 690670.708 | 0.14 | 1008 | 6 |
| PlayerPositionEvent | 1922 | 9.724 | 10.001 | 552.925 | 10.092 | 690370.208 | 0.11 | 0 | 7 |
| InputEvent | 1810 | 0.0 | 1.399 | 603.161 | 29.252 | 690469.809 | 0.1 | 30 | 11 |
| DialogueEvent | 1541 | 0.0 | 4.561 | 708.51 | 36.28 | 690425.693 | 0.08 | 433 | 9 |
| argumentationNodeEvent | 182 | 0.025 | 0.919 | 4747.734 | 12.888 | 776930.914 | 0.01 | 10 | 3 |
| ObjectInterEvent | 170 | 0.007 | 14.309 | 6420.158 | 839.226 | 690584.18 | 0.01 | 1 | 9 |
| TopographicMapEvent | 103 | 0.027 | 6.39 | 10574.255 | 1477.281 | 691001.144 | 0.01 | 2 | 6 |
| Soil Key Puzzle | 45 | 0.125 | 1.208 | 19181.904 | 14.579 | 776233.041 | 0.0 | 0 | 2 |
| questEvent | 44 | 0.002 | 258.94 | 24811.863 | 70233.294 | 690452.177 | 0.0 | 3 | 15 |
| DEBUGMenu | 24 | 9.759 | 653.951 | 45492.39 | 187063.881 | 691181.969 | 0.0 | 0 | 12 |
| DaniEvent | 21 | 0.749 | 4.52 | 8150.952 | 84405.147 | 86141.105 | 0.01 | 0 | 2 |
| gameStartEvent | 12 | 52.095 | 14476.108 | 90981.082 | 425768.474 | 691194.462 | 0.0 | 0 | 10 |
| gameWindowFocusEvent | 12 | 52.095 | 14476.108 | 90981.082 | 425768.475 | 691194.463 | 0.0 | 0 | 10 |
| argumentationEvent | 8 | 0.039 | 69.029 | 108005.921 | 551272.161 | 829988.314 | 0.0 | 1 | 2 |
| argumentationAnswerEvent | 7 | 28.961 | 48.307 | 123429.834 | 591148.223 | 830056.638 | 0.0 | 0 | 2 |
| argumentationToolEvent | 7 | 0.851 | 8.406 | 123428.9 | 591170.45 | 830035.39 | 0.0 | 0 | 2 |
| chatEvent | 5 | 8.626 | 12.629 | 17296.96 | 69003.166 | 86187.538 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 5 | 7808.807 | 48940.268 | 172796.562 | 568702.972 | 691230.927 | 0.0 | 0 | 5 |
| EndOfUnit | 2 | 259753.555 | 544993.204 | 544993.204 | 801708.889 | 830232.854 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 73 group(s), 115 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[648] _id=6ac4fc83de269131f9b1951c ts=2026-10-06T13:49:53.1440000Z == 6ab9a88e9a8420a1e6b56ae7.jsonl[650] _id=6ac4fc83de269131f9b19524 ts=2026-10-06T13:49:53.1440000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[641] _id=6ac4fc83de269131f9b19532 ts=2026-10-06T13:49:53.3960000Z == 6ab9a88e9a8420a1e6b56ae7.jsonl[635] _id=6ac4fc83de269131f9b1953f ts=2026-10-06T13:49:53.3960000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[667] _id=6ac4fc84de269131f9b195a5 ts=2026-10-06T13:49:53.4830000Z == 6ab9a88e9a8420a1e6b56ae7.jsonl[668] _id=6ac4fc84de269131f9b195ad ts=2026-10-06T13:49:53.4830000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[109] _id=6ac4f575de269131f9b03ef2 ts=2026-10-06T13:19:49.3350000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[110] _id=6ac4f575de269131f9b03ef4 ts=2026-10-06T13:19:49.3420000Z`; `361ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[919] _id=6ac4fd37de269131f9b1c457 ts=2026-10-06T13:52:54.7350000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[922] _id=6ac4fd37de269131f9b1c47d ts=2026-10-06T13:52:55.0960000Z`; `242ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[921] _id=6ac4fd3cde269131f9b1c5a7 ts=2026-10-06T13:53:00.1680000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[934] _id=6ac4fd3cde269131f9b1c5c2 ts=2026-10-06T13:53:00.4100000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 109 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `68ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[669] _id=6ac4fc84de269131f9b195b2 ts=2026-10-06T13:49:53.4830000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[663] _id=6ac4fc84de269131f9b195d1 ts=2026-10-06T13:49:53.5510000Z`; `91ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[651] _id=6ac4fc85de269131f9b195df ts=2026-10-06T13:49:53.5510000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[664] _id=6ac4fc85de269131f9b19600 ts=2026-10-06T13:49:53.6420000Z`; `148ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[670] _id=6ac4fc87de269131f9b196e7 ts=2026-10-06T13:49:56.5220000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[683] _id=6ac4fc87de269131f9b196f2 ts=2026-10-06T13:49:56.6700000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[6295] _id=6ad2290fde269131f9e3d1b3 ts=2026-10-16T13:39:25.6160000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[6292] _id=6ad2290fde269131f9e3d1b6 ts=2026-10-16T13:39:25.6550000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `55ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[361] _id=6ac4f9f3de269131f9b10185 ts=2026-10-06T13:38:58.5780000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[363] _id=6ac4f9f3de269131f9b1018d ts=2026-10-06T13:38:58.6330000Z`; `70ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[380] _id=6ac4f9f7de269131f9b10273 ts=2026-10-06T13:39:02.9810000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[381] _id=6ac4f9f7de269131f9b10275 ts=2026-10-06T13:39:03.0510000Z`; `794ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[412] _id=6ac4f9fdde269131f9b1040f ts=2026-10-06T13:39:09.6000000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[407] _id=6ac4f9fede269131f9b1043b ts=2026-10-06T13:39:10.3940000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `851ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[6267] _id=6ad228dcde269131f9e3cd33 ts=2026-10-16T13:38:35.1620000Z ~ 6ab9a88e9a8420a1e6b56ae7.jsonl[6266] _id=6ad228dcde269131f9e3cd47 ts=2026-10-16T13:38:36.0130000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 191h 59m 
  - Evidence: 191h 59m: 6ab9a88e9a8420a1e6b56ae7.jsonl[549] _id=6ac4fb84de269131f9b1520c ts=2026-10-06T13:45:40.4130000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1516] _id=6acf8773de269131f9d3559b ts=2026-10-14T13:45:22.3820000Z; 57h 23m: 6ab9a88e9a8420a1e6b56ae7.jsonl[6426] _id=6ad22a1fde269131f9e3e5da ts=2026-10-16T13:43:58.4530000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7093] _id=6ad55136de269131f9e8da9c ts=2026-10-18T23:07:33.8820000Z; 21h 11m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2523] _id=6acfa686de269131f9d507e3 ts=2026-10-14T15:57:58.2260000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2746] _id=6ad0d076de269131f9da4e5f ts=2026-10-15T13:09:09.9990000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 55m 
  - Evidence: 23h 55m: 6ab9a88e9a8420a1e6b56ae7.jsonl[3043] _id=6ad0d57ede269131f9daa0a3 ts=2026-10-15T13:30:37.9750000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5703] _id=6ad225fcde269131f9e39767 ts=2026-10-16T13:26:19.0800000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2478] _id=6acf8a7ede269131f9d3b7ea ts=2026-10-14T13:58:21.8770000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2932] _id=6ad0d433de269131f9da7d71 ts=2026-10-15T13:25:07.0240000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 191h 47m 
  - Evidence: 191h 47m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1511] _id=6ac4fe9dde269131f9b22b6c ts=2026-10-06T13:58:53.1790000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1528] _id=6acf8797de269131f9d35950 ts=2026-10-14T13:45:58.8720000Z; 57h 10m: 6ab9a88e9a8420a1e6b56ae7.jsonl[7089] _id=6ad22dafde269131f9e447fc ts=2026-10-16T13:59:10.8460000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7190] _id=6ad5519ede269131f9e8db57 ts=2026-10-18T23:09:18.1370000Z; 20h 59m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2745] _id=6acfa95ade269131f9d542f2 ts=2026-10-14T16:10:01.4060000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2759] _id=6ad0d0a5de269131f9da4eec ts=2026-10-15T13:09:56.4820000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 433 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[4272] _id=6ad0dc62de269131f9db6a07 ts=2026-10-15T14:00:01.5570000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[4281] _id=6ad16a84de269131f9e2228b ts=2026-10-15T14:00:01.557Z; 0ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[6268] _id=6ad228dede269131f9e3cd5f ts=2026-10-16T13:38:37.3090000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6269] _id=6ad228dede269131f9e3cd60 ts=2026-10-16T13:38:37.3090000Z; 1ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[2490] _id=6acf8abbde269131f9d3c653 ts=2026-10-14T13:59:22.0010000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2491] _id=6acf8abbde269131f9d3c654 ts=2026-10-14T13:59:22.0020000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 230h 37m 
  - Evidence: 230h 37m: 6ab9a88e9a8420a1e6b56ae7.jsonl[545] _id=6ac4fb23de269131f9b13f95 ts=2026-10-06T13:44:03.0240000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5317] _id=6ad1a63cde269131f9e334ed ts=2026-10-16T04:21:15.8780000Z; 72h 9m: 6ab9a88e9a8420a1e6b56ae7.jsonl[5317] _id=6ad1a63cde269131f9e334ed ts=2026-10-16T04:21:15.8780000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[8208] _id=6ad59ce6de269131f9e952a2 ts=2026-10-19T04:30:29.4330000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 191h 47m 
  - Evidence: 191h 47m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1493] _id=6ac4fe5dde269131f9b219ec ts=2026-10-06T13:57:49.1680000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1523] _id=6acf8784de269131f9d3575a ts=2026-10-14T13:45:38.9770000Z; 57h 8m: 6ab9a88e9a8420a1e6b56ae7.jsonl[7082] _id=6ad22daade269131f9e4478f ts=2026-10-16T13:59:05.7790000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7100] _id=6ad55145de269131f9e8daa3 ts=2026-10-18T23:07:48.6350000Z; 21h 0m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2723] _id=6acfa8fdde269131f9d53a7d ts=2026-10-14T16:08:29.3050000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2751] _id=6ad0d089de269131f9da4eb3 ts=2026-10-15T13:09:28.5880000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 30 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[6060] _id=6ad22769de269131f9e3b1a3 ts=2026-10-16T13:32:24.5320000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6061] _id=6ad22769de269131f9e3b1a4 ts=2026-10-16T13:32:24.5320000Z; 1ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[4960] _id=6ad1a2f3de269131f9e32c4b ts=2026-10-16T04:07:15.0920000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[4961] _id=6ad1a2f3de269131f9e32c4c ts=2026-10-16T04:07:15.0930000Z; 1ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[5944] _id=6ad226ddde269131f9e3a86d ts=2026-10-16T13:30:04.5520000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5945] _id=6ad226ddde269131f9e3a86e ts=2026-10-16T13:30:04.5530000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 191h 49m 
  - Evidence: 191h 49m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1482] _id=6ac4fe25de269131f9b2082e ts=2026-10-06T13:56:53.2300000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1545] _id=6acf87bede269131f9d35c8c ts=2026-10-14T13:46:37.4100000Z; 57h 9m: 6ab9a88e9a8420a1e6b56ae7.jsonl[7091] _id=6ad22dafde269131f9e447ee ts=2026-10-16T13:59:10.8240000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7128] _id=6ad55189de269131f9e8db03 ts=2026-10-18T23:08:57.3870000Z; 23h 41m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2370] _id=6acf891bde269131f9d38685 ts=2026-10-14T13:52:26.5610000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[3109] _id=6ad0d651de269131f9dab495 ts=2026-10-15T13:34:09.2020000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[109] _id=6ac4f575de269131f9b03ef2 ts=2026-10-06T13:19:49.3350000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[110] _id=6ac4f575de269131f9b03ef4 ts=2026-10-06T13:19:49.3420000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 191h 46m 
  - Evidence: 191h 46m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1515] _id=6ac4febbde269131f9b23287 ts=2026-10-06T13:59:23.6380000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1522] _id=6acf8784de269131f9d35759 ts=2026-10-14T13:45:33.8460000Z; 57h 8m: 6ab9a88e9a8420a1e6b56ae7.jsonl[7090] _id=6ad22daede269131f9e447de ts=2026-10-16T13:59:09.9730000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7099] _id=6ad55145de269131f9e8daa2 ts=2026-10-18T23:07:45.3670000Z; 20h 59m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2743] _id=6acfa951de269131f9d541de ts=2026-10-14T16:09:52.5630000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2754] _id=6ad0d083de269131f9da4e9e ts=2026-10-15T13:09:19.7740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 51m 
  - Evidence: 191h 51m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1432] _id=6ac4fde9de269131f9b1f726 ts=2026-10-06T13:55:51.2420000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1604] _id=6acf8833de269131f9d366a5 ts=2026-10-14T13:47:01.9500000Z; 57h 19m: 6ab9a88e9a8420a1e6b56ae7.jsonl[6823] _id=6ad22b14de269131f9e3ff7d ts=2026-10-16T13:48:02.8010000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7104] _id=6ad55146de269131f9e8daa7 ts=2026-10-18T23:07:45.4460000Z; 23h 44m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2359] _id=6acf88fdde269131f9d38348 ts=2026-10-14T13:51:54.5940000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[3089] _id=6ad0d6e2de269131f9dabf0a ts=2026-10-15T13:36:33.3150000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1008 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[0] _id=6ac4fdbdde269131f9b1e92e ts=2026-10-06T13:55:07.3160000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1128] _id=6ac4fdbdde269131f9b1e953 ts=2026-10-06T13:55:07.3160000Z; 0ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[1007] _id=6ac4fd4bde269131f9b1ca16 ts=2026-10-06T13:53:15.0020000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1008] _id=6ac4fd4bde269131f9b1ca20 ts=2026-10-06T13:53:15.0020000Z; 0ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[1054] _id=6ac4fd69de269131f9b1d195 ts=2026-10-06T13:53:43.6780000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1068] _id=6ac4fd69de269131f9b1d1a0 ts=2026-10-06T13:53:43.6780000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 37m 
  - Evidence: 215h 37m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1487] _id=6ac4fe28de269131f9b208d8 ts=2026-10-06T13:56:56.1550000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[3108] _id=6ad0d651de269131f9dab48e ts=2026-10-15T13:34:09.1960000Z; 24h 7m: 6ab9a88e9a8420a1e6b56ae7.jsonl[3135] _id=6ad0d689de269131f9dab93f ts=2026-10-15T13:35:04.5430000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6389] _id=6ad229d2de269131f9e3e0e1 ts=2026-10-16T13:42:42.0110000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 56m 
  - Evidence: 191h 56m: 6ab9a88e9a8420a1e6b56ae7.jsonl[695] _id=6ac4fcc2de269131f9b1a823 ts=2026-10-06T13:50:57.4130000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1600] _id=6acf87fbde269131f9d361eb ts=2026-10-14T13:47:38.5570000Z; 62h 37m: 6ab9a88e9a8420a1e6b56ae7.jsonl[6349] _id=6ad2296fde269131f9e3d8ea ts=2026-10-16T13:41:03.0260000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[8031] _id=6ad59a35de269131f9e95108 ts=2026-10-19T04:19:00.3980000Z; 23h 18m: 6ab9a88e9a8420a1e6b56ae7.jsonl[4241] _id=6ad0dbc7de269131f9db585a ts=2026-10-15T13:57:27.3680000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5391] _id=6ad22378de269131f9e3648a ts=2026-10-16T13:15:35.1720000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.045s shown 
  - Evidence: 27ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[2599] _id=6acfa771de269131f9d51abd ts=2026-10-14T16:01:52.9270000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2603] _id=6acfa771de269131f9d51ac1 ts=2026-10-14T16:01:52.9540000Z; 45ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[2604] _id=6acfa771de269131f9d51ab9 ts=2026-10-14T16:01:52.8820000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2599] _id=6acfa771de269131f9d51abd ts=2026-10-14T16:01:52.9270000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 230h 34m 
  - Evidence: 230h 34m: 6ab9a88e9a8420a1e6b56ae7.jsonl[456] _id=6ac4fa69de269131f9b11a1e ts=2026-10-06T13:40:57.5820000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5158] _id=6ad1a4d2de269131f9e33250 ts=2026-10-16T04:15:14.2200000Z; 9h 21m: 6ab9a88e9a8420a1e6b56ae7.jsonl[5251] _id=6ad1a53ede269131f9e3336b ts=2026-10-16T04:17:02.0340000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6271] _id=6ad228dede269131f9e3cd5d ts=2026-10-16T13:38:37.2880000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 230h 33m 
  - Evidence: 230h 33m: 6ab9a88e9a8420a1e6b56ae7.jsonl[452] _id=6ac4fa6ade269131f9b11a28 ts=2026-10-06T13:40:57.6080000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5121] _id=6ad1a48ede269131f9e331a4 ts=2026-10-16T04:14:05.9220000Z; 9h 20m: 6ab9a88e9a8420a1e6b56ae7.jsonl[5256] _id=6ad1a53ede269131f9e3336d ts=2026-10-16T04:17:02.0570000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6243] _id=6ad228b7de269131f9e3ca15 ts=2026-10-16T13:37:58.5050000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.039s..0.039s shown 
  - Evidence: 39ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[6295] _id=6ad2290fde269131f9e3d1b3 ts=2026-10-16T13:39:25.6160000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6292] _id=6ad2290fde269131f9e3d1b6 ts=2026-10-16T13:39:25.6550000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 48m 
  - Evidence: 215h 48m: 6ab9a88e9a8420a1e6b56ae7.jsonl[451] _id=6ac4fa5fde269131f9b1188e ts=2026-10-06T13:40:47.0200000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[3028] _id=6ad0d542de269131f9da9b59 ts=2026-10-15T13:29:37.9340000Z; 14h 44m: 6ab9a88e9a8420a1e6b56ae7.jsonl[3030] _id=6ad0d546de269131f9da9b97 ts=2026-10-15T13:29:40.8720000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5117] _id=6ad1a488de269131f9e33198 ts=2026-10-16T04:14:00.2380000Z; 9h 20m: 6ab9a88e9a8420a1e6b56ae7.jsonl[5255] _id=6ad1a53cde269131f9e33369 ts=2026-10-16T04:16:59.9790000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6242] _id=6ad228b5de269131f9e3c9ec ts=2026-10-16T13:37:56.9280000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.025s..0.032s shown 
  - Evidence: 25ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[5223] _id=6ad1a52cde269131f9e3332b ts=2026-10-16T04:16:43.6630000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5224] _id=6ad1a52cde269131f9e3332d ts=2026-10-16T04:16:43.6880000Z; 31ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[449] _id=6ac4fa5cde269131f9b11814 ts=2026-10-06T13:40:44.1570000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[450] _id=6ac4fa5cde269131f9b11818 ts=2026-10-06T13:40:44.1880000Z; 32ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[5203] _id=6ad1a518de269131f9e33309 ts=2026-10-16T04:16:23.9800000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5204] _id=6ad1a518de269131f9e3330b ts=2026-10-16T04:16:24.0120000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 230h 33m 
  - Evidence: 230h 33m: 6ab9a88e9a8420a1e6b56ae7.jsonl[454] _id=6ac4fa62de269131f9b1190a ts=2026-10-06T13:40:50.2270000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5152] _id=6ad1a4b5de269131f9e33211 ts=2026-10-16T04:14:45.6170000Z; 9h 23m: 6ab9a88e9a8420a1e6b56ae7.jsonl[5153] _id=6ad1a4b8de269131f9e33213 ts=2026-10-16T04:14:47.8320000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[6264] _id=6ad228d3de269131f9e3cc35 ts=2026-10-16T13:38:26.7560000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 56m 
  - Evidence: 23h 56m: 6ab9a88e9a8420a1e6b56ae7.jsonl[3034] _id=6ad0d553de269131f9da9cbf ts=2026-10-15T13:29:54.7810000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[5706] _id=6ad225ffde269131f9e3979d ts=2026-10-16T13:26:22.3190000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 191h 59m 
  - Evidence: 191h 59m: 6ab9a88e9a8420a1e6b56ae7.jsonl[548] _id=6ac4fb78de269131f9b1501b ts=2026-10-06T13:45:28.2390000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1518] _id=6acf8773de269131f9d3559d ts=2026-10-14T13:45:22.7010000Z; 57h 56m: 6ab9a88e9a8420a1e6b56ae7.jsonl[4543] _id=6ad2225dde269131f9e3504d ts=2026-10-16T13:10:52.2630000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7095] _id=6ad55136de269131f9e8da9e ts=2026-10-18T23:07:34.0200000Z; 21h 11m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2518] _id=6acfa67cde269131f9d50769 ts=2026-10-14T15:57:48.3730000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2748] _id=6ad0d076de269131f9da4e61 ts=2026-10-15T13:09:10.1330000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 191h 59m 
  - Evidence: 191h 59m: 6ab9a88e9a8420a1e6b56ae7.jsonl[547] _id=6ac4fb78de269131f9b15016 ts=2026-10-06T13:45:28.2380000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1517] _id=6acf8773de269131f9d3559c ts=2026-10-14T13:45:22.7010000Z; 57h 56m: 6ab9a88e9a8420a1e6b56ae7.jsonl[4542] _id=6ad2225dde269131f9e3504c ts=2026-10-16T13:10:52.2630000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7094] _id=6ad55136de269131f9e8da9d ts=2026-10-18T23:07:34.0200000Z; 21h 11m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2517] _id=6acfa67cde269131f9d50768 ts=2026-10-14T15:57:48.3730000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2747] _id=6ad0d076de269131f9da4e60 ts=2026-10-15T13:09:10.1330000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 192h 0m 
  - Evidence: 192h 0m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1519] _id=6acf8773de269131f9d35590 ts=2026-10-06T13:59:31.48Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2519] _id=6acfa67cde269131f9d50763 ts=2026-10-14T14:00:02.407Z; 21h 49m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2749] _id=6ad0d076de269131f9da4e5d ts=2026-10-14T16:10:11.214Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[4282] _id=6ad16a84de269131f9e2228c ts=2026-10-15T14:00:02.367Z; 13h 35m: 6ab9a88e9a8420a1e6b56ae7.jsonl[4555] _id=6ad1999dde269131f9e2f59b ts=2026-10-16T00:23:34.024Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7092] _id=6ad55136de269131f9e8da9a ts=2026-10-16T13:59:14.292Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 191h 47m 
  - Evidence: 191h 47m: 6ab9a88e9a8420a1e6b56ae7.jsonl[1497] _id=6ac4fe6fde269131f9b21ebe ts=2026-10-06T13:58:06.8450000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[1524] _id=6acf8784de269131f9d3575b ts=2026-10-14T13:45:39.0220000Z; 57h 23m: 6ab9a88e9a8420a1e6b56ae7.jsonl[6402] _id=6ad22a2cde269131f9e3e709 ts=2026-10-16T13:44:12.0240000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[7101] _id=6ad55145de269131f9e8daa4 ts=2026-10-18T23:07:48.6650000Z; 21h 8m: 6ab9a88e9a8420a1e6b56ae7.jsonl[2590] _id=6acfa74cde269131f9d517af ts=2026-10-14T16:01:16.1210000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[2755] _id=6ad0d083de269131f9da4e9f ts=2026-10-15T13:09:22.2960000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.010s shown 
  - Evidence: 2ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[375] _id=6ac4f98ede269131f9b0f164 ts=2026-10-06T13:37:18.2890000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[377] _id=6ac4f98ede269131f9b0f16a ts=2026-10-06T13:37:18.2910000Z; 6ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[187] _id=6ac4f6c0de269131f9b07a2c ts=2026-10-06T13:25:19.6980000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[188] _id=6ac4f6c0de269131f9b07a2e ts=2026-10-06T13:25:19.7040000Z; 10ms: 6ab9a88e9a8420a1e6b56ae7.jsonl[127] _id=6ac4f5bade269131f9b043eb ts=2026-10-06T13:20:58.6350000Z -> 6ab9a88e9a8420a1e6b56ae7.jsonl[128] _id=6ac4f5bbde269131f9b043f5 ts=2026-10-06T13:20:58.6450000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[362] _id=6ac4f973de269131f9b0e8c2 ts=2026-10-06T13:36:51.0920000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[469] _id=6ac4fa84de269131f9b12008 ts=2026-10-06T13:41:24.2800000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[3947] _id=6ad0d8cbde269131f9daf9db ts=2026-10-15T13:44:42.7110000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[962] _id=6ac4fd43de269131f9b1c7a6 ts=2026-10-06T13:53:05.8330000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[977] _id=6ac4fd43de269131f9b1c7b6 ts=2026-10-06T13:53:05.9930000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[949] _id=6ac4fd43de269131f9b1c7bd ts=2026-10-06T13:53:06.2810000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 105 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[807] _id=6ac4fd1bde269131f9b1bd39 ts=2026-10-06T13:49:48.8530000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[667] _id=6ac4fc84de269131f9b195a5 ts=2026-10-06T13:49:53.4830000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[668] _id=6ac4fc84de269131f9b195ad ts=2026-10-06T13:49:53.4830000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[6292] _id=6ad2290fde269131f9e3d1b6 ts=2026-10-16T13:39:25.6550000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[363] _id=6ac4f9f3de269131f9b1018d ts=2026-10-06T13:38:58.6330000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[381] _id=6ac4f9f7de269131f9b10275 ts=2026-10-06T13:39:03.0510000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[409] _id=6ac4f9ffde269131f9b1048d ts=2026-10-06T13:39:11.0100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 173 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[913] _id=6ac4fd35de269131f9b1c3eb ts=2026-10-06T13:52:51.7930000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[972] _id=6ac4fd48de269131f9b1c93e ts=2026-10-06T13:53:10.5730000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[1037] _id=6ac4fd54de269131f9b1cc6c ts=2026-10-06T13:53:22.9920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 419 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[818] _id=6ac4fd1cde269131f9b1bd5d ts=2026-10-06T13:49:50.6360000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[821] _id=6ac4fd1cde269131f9b1bd7f ts=2026-10-06T13:49:50.6360000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[650] _id=6ac4fc83de269131f9b19524 ts=2026-10-06T13:49:53.1440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 22 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[2799] _id=6ad0d25cde269131f9da59ce ts=2026-10-15T13:17:15.4860000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[2865] _id=6ad0d337de269131f9da65e0 ts=2026-10-15T13:20:54.9530000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[2912] _id=6ad0d3f1de269131f9da77fa ts=2026-10-15T13:24:01.1820000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 19 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[410] _id=6ac4fa00de269131f9b10499 ts=2026-10-06T13:39:11.2900000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[414] _id=6ac4fa00de269131f9b104a3 ts=2026-10-06T13:39:11.6160000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[436] _id=6ac4fa4ade269131f9b11475 ts=2026-10-06T13:40:26.1800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[6267] _id=6ad228dcde269131f9e3cd33 ts=2026-10-16T13:38:35.1620000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[6266] _id=6ad228dcde269131f9e3cd47 ts=2026-10-16T13:38:36.0130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 295 start, 285 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 21 unmatched 'BecameCameraCentered' (totals: 529 open, 519 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 43 unmatched 'BecameVisible' (totals: 724 open, 786 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 29 open, 28 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 82 open, 82 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 7 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 26 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 170 of 8500 adjacent _id pairs reverse in client time; worst 157.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae7.jsonl[810] _id=6ac4fd1ade269131f9b1bcc7 ts=2026-10-06T13:52:25.8130000Z`; `6ab9a88e9a8420a1e6b56ae7.jsonl[811] _id=6ac4fd1bde269131f9b1bcf8 ts=2026-10-06T13:49:48.8520000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.92s, min -690352.03s, max -0.28s over 8501 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae7\coverage.yaml

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
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 2558 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2036); Unit 3 Dungeon Dev (522)
- **Intervals:** median 0.09s (p5 0.00s / p95 2.33s, n=2557)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2558/2558 records)
    "BecameInvisible"  x786
    "BecameVisible"  x724
    "BecameCameraCentered"  x529
    "BecameCameraUncentered"  x519
data.pieceId  (string, 2558/2558 records)
    24 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2558/2558 records)
    1852 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1928 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (859); Unit 3 Dungeon Dev (340); Unit 4 Dev (290); Unit 3 Dev (263); Unit 1 Dev (176)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.09s, n=1922)
- **Fields under `data`:**

```text
data.position  (object, 1928/1928 records)
data.position.x  (number, 1928/1928 records)
    numeric range -699.27 .. 1427.02 (483 unique)
data.position.y  (number, 1928/1928 records)
    numeric range -113.124 .. 175.178 (320 unique)
data.position.z  (number, 1928/1928 records)
    numeric range -1036.91 .. 2024.43 (481 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `InputEvent` — 1811 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (802); Unit 3 Dev (587); Unit 3 Dungeon Dev (323); Unit 1 Dev (99)
- **Intervals:** median 1.40s (p5 0.14s / p95 29.25s, n=1810)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1811/1811 records)
    "pressed"  x1811
data.actionType  (string, 1811/1811 records)
    "Move"  x1339
    "Interact"  x276
    "Ascend"  x83
    "Jump"  x47
    "Hoverboard"  x39
    "Sprint"  x14
    "Map"  x11
    "Pause"  x1
    "ToggleDebug"  x1
data.key  (string, 1811/1811 records, 13 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1811/1811 records)
    "Player"  x1055
    "Drone"  x756
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1542 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (724); Unit 3 Dev (347); Unit 3 Dungeon Dev (271); Unit 1 Dev (197); Unit 4 Dev (3)
- **eventKey:** present on 962 of 1542 records
- **Intervals:** median 4.56s (p5 0.01s / p95 36.28s, n=1541)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x962; [conversationId, dialogueEventType] x580
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1542/1542 records)
    numeric range 8 .. 104 (36 unique)
data.dialogueEventType  (string, 1542/1542 records)
    "DialogueNodeEvent"  x962
    "DialogueStartEvent"  x295
    "DialogueFinishEvent"  x285
data.nodeId  (number, 962/1542 records)
    numeric range 0 .. 290 (220 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 183 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (115); Unit 1 Dev (39); Unit 3 Dev (29)
- **Intervals:** median 0.92s (p5 0.05s / p95 12.89s, n=182)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 183/183 records)
    "argumentationNodeHoverEnd"  x82
    "argumentationNodeHoverStart"  x82
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 183/183 records)
    "Unit 2 – Watershed"  x115
    "Unit 3 - Pollution Upstream"  x29
    "Unit 1 - Argumentation Tutorial"  x22
    "Unit 1 - Freshwater"  x17
data.nodeName  (string, 183/183 records)
    "A"  x32
    "I"  x29
    "C"  x28
    "1"  x26
    "II"  x23
    "B"  x20
    "D"  x14
    "5"  x5
    "2"  x2
    "3"  x2
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 171 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (90); Unit 2 Prod (Refactor) (60); Unit 3 Dev (11); Unit 1 Dev (10)
- **Intervals:** median 14.31s (p5 2.91s / p95 839.23s, n=170)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 171/171 records)
    20 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 171/171 records)
    56 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 104 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (61); Unit 3 Dev (43)
- **Intervals:** median 6.39s (p5 1.32s / p95 1477.28s, n=103)
- **`data` key-set variants:** [actionType, featureUsed] x57; [actionType, featureUsed, location] x42; [actionType, featureUsed, legendName] x5
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 104/104 records)
    "MapOpenEvent"  x29
    "MapCloseEvent"  x28
    "WaypointMoveEvent"  x28
    "WaypointSetEvent"  x10
    "Selected"  x5
    "WaypointResetEvent"  x4
data.featureUsed  (string, 104/104 records)
    "Map"  x57
    "Waypoint"  x42
    "Legend"  x5
data.legendName  (string, 5/104 records)
    "0 ft"  x2
    "360 ft"  x1
    "90 ft"  x1
    "Water"  x1
data.location  (object, 42/104 records)
data.location.x  (number, 42/104 records)
    numeric range -320.817 .. 597.24 (34 unique)
data.location.y  (number, 42/104 records)
    numeric range -235.216 .. 227.327 (36 unique)
data.location.z  (number, 42/104 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 46 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (18)
- **Intervals:** median 1.21s (p5 0.16s / p95 14.58s, n=45)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x40; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/46 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/46 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 40/46 records)
    "RightDrag"  x23
    "LeftDrag"  x17
data.currentSoilType  (string, 40/46 records)
    "CLAYROCK"  x8
    "CLAY"  x7
    "CLAYSAND"  x7
    "SAND"  x6
    "SANDGRAVEL"  x5
    "BEDROCK"  x4
    "GRAVEL"  x3
data.isCorrectSelection  (string, 40/46 records)
    "false"  x31
    "true"  x9
data.waterLevelStatus  (string, 40/46 records)
    "TooHigh"  x25
    "Proper"  x13
    "TooLow"  x2
data.waterRetentionChange  (string, 40/46 records)
    "Increase"  x19
    "Decrease"  x12
    "NoChange"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 45 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (12); Unit 3 Dev (9); Unit 3 Dungeon Dev (4)
- **eventKey:** present on 45 of 45 records
- **Intervals:** median 258.94s (p5 0.69s / p95 70233.29s, n=44)
- **`data` key-set variants:** [questEventType, questID, questName] x26; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 45/45 records)
    "questActiveEvent"  x26
    "questFinishEvent"  x19
data.questID  (string, 45/45 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 45/45 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/45 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 25 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (7); Unit 3 Dungeon Dev (3); Unit 3 Dev (2); Unit 1 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 653.95s (p5 10.18s / p95 187063.88s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "DebugMenuStateChanged"  x25
data.isOpened  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 22 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (6)
- **Intervals:** median 4.52s (p5 1.03s / p95 84405.15s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "Close"  x11
    "Open"  x11
data.toolName  (string, 22/22 records, 22 empty-string)
    ""  x22
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 14476.11s (p5 219.23s / p95 425768.47s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowFocusEvent` — 13 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13)
- **Intervals:** median 14476.11s (p5 219.23s / p95 425768.47s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 69.03s (p5 14.09s / p95 551272.16s, n=8)
- **Open findings:** 1 — see sections 5-8
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

### `argumentationAnswerEvent` — 8 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 48.31s (p5 30.36s / p95 591148.22s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "submitAnswerEvent"  x8
data.answerSubmitted  (string, 8/8 records)
    "1,"  x1
    "A,1,"  x1
    "A,1,I"  x1
    "A,1,II"  x1
    "A,5,I"  x1
    "B,1,I"  x1
    "D,1,II"  x1
    "I"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 2 – Watershed"  x4
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 8.41s (p5 1.26s / p95 591170.45s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x7
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2)
- **Intervals:** median 12.63s (p5 8.97s / p95 69003.17s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.chatID  (string, 6/6 records)
    "NA"  x3
    "[22-46, 22-48, 22-27, 18-287, 18-289]"  x2
    "[10-218, 11-224, 11-226, 11-23, 11-24]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `gameWindowUnfocusEvent` — 6 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dungeon Dev (1)
- **Intervals:** median 48940.27s (p5 13729.38s / p95 568702.97s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    false  x6
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 544993.20s (p5 288277.52s / p95 801708.89s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (28 records)
- `TopographicMapEvent` data.actionType: "Selected" (5x); "WaypointMoveEvent" (28x); "WaypointResetEvent" (4x); "WaypointSetEvent" (10x)
- `TopographicMapEvent` data.featureUsed: "Legend" (5x); "Waypoint" (42x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*