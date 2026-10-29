# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f250

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f250
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f250.jsonl
- **Records:** 22550 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f250
- **Time span:** 2026-09-23T16:28:17.545000+00:00 .. 2026-10-07T17:07:35.700000+00:00 (336h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f250\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 22550 records, 5 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 97 INFO, 5 NOT_TESTED, 68 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 12732 | 56.46 | 1 | 4 | 0 | 2026-09-23T16:28:40.169000+00:00 | 2026-10-07T17:07:20.060000+00:00 | 336h 38m |
| PuzzlePieceVisibleEvent | 5459 | 24.21 | 1 | 2 | 0 | 2026-09-25T16:36:06.283000+00:00 | 2026-10-07T17:06:07.618000+00:00 | 288h 30m |
| PlayerPositionEvent | 1918 | 8.51 | 1 | 4 | 0 | 2026-09-23T16:28:35.173000+00:00 | 2026-10-07T17:07:31.052000+00:00 | 336h 38m |
| DialogueEvent | 1451 | 6.43 | 1 | 4 | 885 | 2026-09-23T16:28:56.742000+00:00 | 2026-10-07T17:07:21.122000+00:00 | 336h 38m |
| argumentationNodeEvent | 467 | 2.07 | 1 | 2 | 0 | 2026-09-23T17:03:34.080000+00:00 | 2026-10-07T15:01:47.504000+00:00 | 333h 58m |
| ObjectInterEvent | 151 | 0.67 | 1 | 4 | 0 | 2026-09-23T16:41:16.386000+00:00 | 2026-10-07T17:04:56.326000+00:00 | 336h 23m |
| TopographicMapEvent | 99 | 0.44 | 1 | 2 | 0 | 2026-09-24T16:29:43.284000+00:00 | 2026-10-06T17:06:17.505000+00:00 | 288h 36m |
| argumentationAnswerEvent | 51 | 0.23 | 1 | 2 | 0 | 2026-09-24T16:20:19.490000+00:00 | 2026-10-07T15:01:48.362000+00:00 | 310h 41m |
| questEvent | 51 | 0.23 | 1 | 4 | 51 | 2026-09-23T16:28:56.723000+00:00 | 2026-10-07T16:57:10.239000+00:00 | 336h 28m |
| Soil Key Puzzle | 44 | 0.2 | 1 | 2 | 0 | 2026-09-25T16:47:23.987000+00:00 | 2026-10-07T15:05:36.229000+00:00 | 286h 18m |
| gameWindowFocusEvent | 36 | 0.16 | 1 | 4 | 0 | 2026-09-23T16:28:17.545000+00:00 | 2026-10-07T16:57:00.332000+00:00 | 336h 28m |
| gameWindowUnfocusEvent | 26 | 0.12 | 1 | 4 | 0 | 2026-09-23T16:34:31.234000+00:00 | 2026-10-07T17:07:35.700000+00:00 | 336h 33m |
| DEBUGMenu | 17 | 0.08 | 1 | 5 | 0 | 2026-09-23T16:28:35.166000+00:00 | 2026-10-07T16:57:06.725000+00:00 | 336h 28m |
| DaniEvent | 16 | 0.07 | 1 | 2 | 0 | 2026-09-24T16:29:35.097000+00:00 | 2026-10-07T17:02:38.020000+00:00 | 312h 33m |
| gameStartEvent | 14 | 0.06 | 1 | 1 | 0 | 2026-09-23T16:28:17.546000+00:00 | 2026-10-07T16:57:00.332000+00:00 | 336h 28m |
| argumentationToolEvent | 8 | 0.04 | 1 | 2 | 0 | 2026-09-24T16:19:59.343000+00:00 | 2026-10-07T14:59:31.715000+00:00 | 310h 39m |
| argumentationEvent | 7 | 0.03 | 1 | 2 | 0 | 2026-09-24T16:20:01.848000+00:00 | 2026-10-07T15:01:48.417000+00:00 | 310h 41m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 1 | 0.0 | 1 | 1 | 0 | 2026-09-24T16:27:43.014000+00:00 | 2026-09-24T16:27:43.014000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 42473.991s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 0.179s median 
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
  - Observed: 0.232s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 134.939s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.879s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 85764.696s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 684.567s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 907.477s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 16 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 5.3x vs baseline. 
  - Observed: 12732 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; p; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: E to Talk; Press E; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Return To Base; Press E To Scan; Press E to Open Locker; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.waterLevelStatus` — baseline categorical value(s) not seen this build. 
  - Observed: TooLow 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 240 ft; 270 ft; 300 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.2x vs baseline. 
  - Observed: 51 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,; A,2,I; B,1,I; B,1,II; B,4,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 467 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 31; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; TK, Reporting In!; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 84 mismatch(es); e.g. 'DialogueNodeEvent:30:37' vs expected 'DialogueNodeEvent:31:68' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[7708] _id=6abd37cf485cab4c958d8f4c ts=2026-09-23T16:40:59.691Z`; `6aa4142c41b41dbac0c7f250.jsonl[7724] _id=6abd37cf485cab4c958d8f89 ts=2026-09-23T16:41:16.4Z`; `6aa4142c41b41dbac0c7f250.jsonl[7725] _id=6abd37d0485cab4c958d8fa6 ts=2026-09-23T16:41:31.058Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'questFinishEvent:29' vs expected 'questFinishEvent:32' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[7676] _id=6abd37d1485cab4c958d8ff7 ts=2026-09-23T16:42:31.209Z`; `6aa4142c41b41dbac0c7f250.jsonl[7738] _id=6abd37d1485cab4c958d8ffd ts=2026-09-23T16:42:31.216Z`; `6aa4142c41b41dbac0c7f250.jsonl[7785] _id=6abd37d7485cab4c958d9148 ts=2026-09-23T16:46:03.163Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[5] _id=6ab3fe21485cab4c954e611a ts=2026-09-23T16:28:17.5460000Z`; `6aa4142c41b41dbac0c7f250.jsonl[157] _id=6ab54d25485cab4c9552e6ae ts=2026-09-24T16:17:42.2420000Z`; `6aa4142c41b41dbac0c7f250.jsonl[636] _id=6ab54fd2485cab4c95530e1b ts=2026-09-24T16:29:06.8110000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 36 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 36} 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[3] _id=6ab3fe21485cab4c954e6118 ts=2026-09-23T16:28:17.5450000Z`; `6aa4142c41b41dbac0c7f250.jsonl[107] _id=6ab3ff98485cab4c954e6856 ts=2026-09-23T16:34:32.9180000Z`; `6aa4142c41b41dbac0c7f250.jsonl[143] _id=6ab3ffba485cab4c954e69f4 ts=2026-09-23T16:35:06.4620000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[106] _id=6ab3ff97485cab4c954e6842 ts=2026-09-23T16:34:31.2340000Z`; `6aa4142c41b41dbac0c7f250.jsonl[152] _id=6ab3ffba485cab4c954e69f2 ts=2026-09-23T16:35:06.3790000Z`; `6aa4142c41b41dbac0c7f250.jsonl[8071] _id=6abd37ed485cab4c958d95d8 ts=2026-09-23T17:01:28.782Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 14 of 99 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[665] _id=6ab54ff7485cab4c95531109 ts=2026-09-24T16:29:43.2840000Z`; `6aa4142c41b41dbac0c7f250.jsonl[667] _id=6ab54ff8485cab4c9553111f ts=2026-09-24T16:29:44.8920000Z`; `6aa4142c41b41dbac0c7f250.jsonl[1010] _id=6ab6a30e485cab4c955ade5b ts=2026-09-25T16:36:30.4050000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 12731 | 0.0 | 0.179 | 95.194 | 1.452 | 343842.219 | 0.63 | 1704 | 16 |
| PuzzlePieceVisibleEvent | 5458 | 0.0 | 0.021 | 190.29 | 0.593 | 343836.907 | 0.32 | 3617 | 8 |
| PlayerPositionEvent | 1914 | 9.31 | 10.0 | 633.108 | 10.156 | 327448.457 | 0.09 | 0 | 13 |
| DialogueEvent | 1450 | 0.0 | 4.534 | 835.796 | 48.105 | 342983.692 | 0.07 | 432 | 11 |
| argumentationNodeEvent | 466 | 0.015 | 0.328 | 2580.029 | 5.432 | 1117821.956 | 0.02 | 125 | 2 |
| ObjectInterEvent | 150 | 0.005 | 4.926 | 8073.466 | 4032.602 | 431154.984 | 0.01 | 1 | 10 |
| TopographicMapEvent | 98 | 0.02 | 2.423 | 10601.982 | 84770.589 | 347978.004 | 0.01 | 2 | 8 |
| argumentationAnswerEvent | 50 | 0.107 | 0.232 | 22369.777 | 94.763 | 1117852.319 | 0.0 | 0 | 1 |
| questEvent | 50 | 0.002 | 282.981 | 24225.87 | 134193.713 | 343592.135 | 0.0 | 7 | 17 |
| Soil Key Puzzle | 43 | 0.16 | 0.992 | 23969.587 | 921.526 | 598431.19 | 0.0 | 0 | 3 |
| gameWindowFocusEvent | 35 | 3.109 | 684.567 | 34609.222 | 193904.1 | 295677.514 | 0.0 | 0 | 18 |
| gameWindowUnfocusEvent | 25 | 0.537 | 907.477 | 48463.379 | 240780.145 | 297864.918 | 0.0 | 0 | 13 |
| DEBUGMenu | 16 | 6.939 | 42473.991 | 75706.972 | 280503.245 | 345003.185 | 0.0 | 0 | 12 |
| DaniEvent | 15 | 0.701 | 2.403 | 75012.195 | 398108.875 | 520496.673 | 0.0 | 0 | 3 |
| gameStartEvent | 13 | 205.97 | 85764.696 | 93178.676 | 293412.408 | 345041.233 | 0.0 | 0 | 11 |
| argumentationToolEvent | 7 | 0.849 | 2.879 | 159767.482 | 782738.815 | 1118135.562 | 0.0 | 0 | 1 |
| argumentationEvent | 6 | 0.031 | 134.939 | 186417.761 | 838456.516 | 1117805.055 | 0.0 | 1 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 13 group(s), 15 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[116] _id=6ab3ff9e485cab4c954e68a2 ts=2026-09-23T16:34:38.3050000Z == 6aa4142c41b41dbac0c7f250.jsonl[118] _id=6ab3ff9e485cab4c954e68a4 ts=2026-09-23T16:34:38.3050000Z`; `6aa4142c41b41dbac0c7f250.jsonl[113] _id=6ab3ff9e485cab4c954e68a6 ts=2026-09-23T16:34:38.3060000Z == 6aa4142c41b41dbac0c7f250.jsonl[119] _id=6ab3ff9e485cab4c954e68aa ts=2026-09-23T16:34:38.3060000Z`; `6aa4142c41b41dbac0c7f250.jsonl[6259] _id=6aba9d06485cab4c956b456c ts=2026-09-28T16:59:50.6050000Z == 6aa4142c41b41dbac0c7f250.jsonl[6257] _id=6aba9d06485cab4c956b4577 ts=2026-09-28T16:59:50.6050000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 399 group(s), 687 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[945] _id=6ab6a2f7485cab4c955acea7 ts=2026-09-25T16:36:06.4770000Z == 6aa4142c41b41dbac0c7f250.jsonl[947] _id=6ab6a2f7485cab4c955acf22 ts=2026-09-25T16:36:06.4770000Z`; `6aa4142c41b41dbac0c7f250.jsonl[964] _id=6ab6a2f9485cab4c955ad04c ts=2026-09-25T16:36:07.3740000Z == 6aa4142c41b41dbac0c7f250.jsonl[971] _id=6ab6a2f9485cab4c955ad058 ts=2026-09-25T16:36:07.3740000Z`; `6aa4142c41b41dbac0c7f250.jsonl[953] _id=6ab6a2f9485cab4c955ad094 ts=2026-09-25T16:36:07.9410000Z == 6aa4142c41b41dbac0c7f250.jsonl[970] _id=6ab6a2f9485cab4c955ad0a4 ts=2026-09-25T16:36:07.9410000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[3682] _id=6aba946d485cab4c956a6ca1 ts=? == 6aa4142c41b41dbac0c7f250.jsonl[8195] _id=6abd3817485cab4c958d9cf4 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4142c41b41dbac0c7f250.jsonl[7723] _id=6abd37cf485cab4c958d8f80 ts=2026-09-23T16:41:16.386Z ~ 6aa4142c41b41dbac0c7f250.jsonl[7720] _id=6abd37cf485cab4c958d8f84 ts=2026-09-23T16:41:16.391Z`; `150ms: 6aa4142c41b41dbac0c7f250.jsonl[8073] _id=6abd37ed485cab4c958d95e2 ts=2026-09-23T17:01:30.743Z ~ 6aa4142c41b41dbac0c7f250.jsonl[8057] _id=6abd37ed485cab4c958d95ea ts=2026-09-23T17:01:30.893Z`; `121ms: 6aa4142c41b41dbac0c7f250.jsonl[8057] _id=6abd37ed485cab4c958d95ea ts=2026-09-23T17:01:30.893Z ~ 6aa4142c41b41dbac0c7f250.jsonl[8080] _id=6abd37ed485cab4c958d95f2 ts=2026-09-23T17:01:31.014Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1257 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `57ms: 6aa4142c41b41dbac0c7f250.jsonl[947] _id=6ab6a2f7485cab4c955acf22 ts=2026-09-25T16:36:06.4770000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[942] _id=6ab6a2f7485cab4c955acf2d ts=2026-09-25T16:36:06.5340000Z`; `71ms: 6aa4142c41b41dbac0c7f250.jsonl[942] _id=6ab6a2f7485cab4c955acf2d ts=2026-09-25T16:36:06.5340000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[948] _id=6ab6a2f7485cab4c955acf41 ts=2026-09-25T16:36:06.6050000Z`; `22ms: 6aa4142c41b41dbac0c7f250.jsonl[948] _id=6ab6a2f7485cab4c955acf41 ts=2026-09-25T16:36:06.6050000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[937] _id=6ab6a2f8485cab4c955acf5b ts=2026-09-25T16:36:06.6270000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `910ms: 6aa4142c41b41dbac0c7f250.jsonl[9070] _id=6abd39d0485cab4c958dd00e ts=2026-09-30T16:33:20.0980000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[9071] _id=6abd39d1485cab4c958dd01c ts=2026-09-30T16:33:21.0080000Z`; `306ms: 6aa4142c41b41dbac0c7f250.jsonl[9088] _id=6abd39f8485cab4c958dd2f8 ts=2026-09-30T16:34:00.5000000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[9089] _id=6abd39f8485cab4c958dd2fc ts=2026-09-30T16:34:00.8060000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa4142c41b41dbac0c7f250.jsonl[3314] _id=6ab6a76e485cab4c955cfdb7 ts=2026-09-25T16:55:10.8520000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[3312] _id=6ab6a76f485cab4c955cfdc3 ts=2026-09-25T16:55:10.8750000Z`; `440ms: 6aa4142c41b41dbac0c7f250.jsonl[3787] _id=6aba9505485cab4c956a7eba ts=2026-09-28T16:25:41.3440000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[3805] _id=6aba9505485cab4c956a7ec6 ts=2026-09-28T16:25:41.7840000Z`; `536ms: 6aa4142c41b41dbac0c7f250.jsonl[3807] _id=6aba9508485cab4c956a7f40 ts=2026-09-28T16:25:44.7120000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[3808] _id=6aba9509485cab4c956a7f51 ts=2026-09-28T16:25:45.2480000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 32 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `433ms: 6aa4142c41b41dbac0c7f250.jsonl[340] _id=6ab54e48485cab4c9552f4b3 ts=2026-09-24T16:22:33.6260000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[341] _id=6ab54e49485cab4c9552f4c3 ts=2026-09-24T16:22:34.0590000Z`; `183ms: 6aa4142c41b41dbac0c7f250.jsonl[341] _id=6ab54e49485cab4c9552f4c3 ts=2026-09-24T16:22:34.0590000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[342] _id=6ab54e49485cab4c9552f4c9 ts=2026-09-24T16:22:34.2420000Z`; `475ms: 6aa4142c41b41dbac0c7f250.jsonl[342] _id=6ab54e49485cab4c9552f4c9 ts=2026-09-24T16:22:34.2420000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[343] _id=6ab54e49485cab4c9552f4d1 ts=2026-09-24T16:22:34.7170000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `31ms: 6aa4142c41b41dbac0c7f250.jsonl[19835] _id=6ac65edcde269131f9bb6442 ts=2026-10-07T15:01:48.3860000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[19838] _id=6ac65edcde269131f9bb6445 ts=2026-10-07T15:01:48.4170000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 85 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `82ms: 6aa4142c41b41dbac0c7f250.jsonl[8158] _id=6abd37f4485cab4c958d9854 ts=2026-09-23T17:03:34.08Z ~ 6aa4142c41b41dbac0c7f250.jsonl[8159] _id=6abd37f4485cab4c958d9859 ts=2026-09-23T17:03:34.162Z`; `55ms: 6aa4142c41b41dbac0c7f250.jsonl[8159] _id=6abd37f4485cab4c958d9859 ts=2026-09-23T17:03:34.162Z ~ 6aa4142c41b41dbac0c7f250.jsonl[8160] _id=6abd37f4485cab4c958d9860 ts=2026-09-23T17:03:34.217Z`; `193ms: 6aa4142c41b41dbac0c7f250.jsonl[8160] _id=6abd37f4485cab4c958d9860 ts=2026-09-23T17:03:34.217Z ~ 6aa4142c41b41dbac0c7f250.jsonl[8161] _id=6abd37f4485cab4c958d9867 ts=2026-09-23T17:03:34.41Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `727ms: 6aa4142c41b41dbac0c7f250.jsonl[7657] _id=6abd37f2485cab4c958d977a ts=2026-09-23T17:02:25.148Z ~ 6aa4142c41b41dbac0c7f250.jsonl[8015] _id=6abd37f2485cab4c958d9782 ts=2026-09-23T17:02:25.875Z`; `537ms: 6aa4142c41b41dbac0c7f250.jsonl[13020] _id=6abe8af6485cab4c95ac098a ts=2026-10-01T16:31:50.3390000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[13028] _id=6abe8af7485cab4c95ac09a1 ts=2026-10-01T16:31:50.8760000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f250.jsonl[11146] _id=6abe89a3485cab4c95abe63a ts=2026-10-01T16:26:10.0950000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[11147] _id=6abe89a3485cab4c95abe63c ts=2026-10-01T16:26:10.1010000Z`; `2ms: 6aa4142c41b41dbac0c7f250.jsonl[13052] _id=6abe8b50485cab4c95ac0e18 ts=2026-10-01T16:33:19.3100000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[13038] _id=6abe8b50485cab4c95ac0e1a ts=2026-10-01T16:33:19.3120000Z`; `4ms: 6aa4142c41b41dbac0c7f250.jsonl[13916] _id=6ac3cf01de269131f9ada45d ts=2026-10-05T16:23:28.1940000Z ~ 6aa4142c41b41dbac0c7f250.jsonl[13921] _id=6ac3cf01de269131f9ada45f ts=2026-10-05T16:23:28.1980000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 6aa4142c41b41dbac0c7f250.jsonl[13035] _id=6abe8b4e485cab4c95ac0df8 ts=2026-10-01T16:33:18.5620000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13910] _id=6ac3cef9de269131f9ada441 ts=2026-10-05T16:23:21.7470000Z; 71h 56m: 6aa4142c41b41dbac0c7f250.jsonl[779] _id=6ab6a0ac485cab4c95595055 ts=2026-09-25T16:26:20.1520000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3679] _id=6aba9467485cab4c956a6c13 ts=2026-09-28T16:23:03.4170000Z; 48h 2m: 6aa4142c41b41dbac0c7f250.jsonl[3679] _id=6aba9467485cab4c956a6c13 ts=2026-09-28T16:23:03.4170000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8186] _id=6abd3810485cab4c958d9c56 ts=2026-09-30T16:25:52.9200000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 34m 
  - Evidence: 144h 34m: 6aa4142c41b41dbac0c7f250.jsonl[11223] _id=6abe89f8485cab4c95abec68 ts=2026-10-01T16:27:36.2620000Z -> 6aa4142c41b41dbac0c7f250.jsonl[21954] _id=6ac67b29de269131f9bd8543 ts=2026-10-07T17:02:32.9350000Z; 96h 0m: 6aa4142c41b41dbac0c7f250.jsonl[662] _id=6ab54ff1485cab4c95531069 ts=2026-09-24T16:29:37.5000000Z -> 6aa4142c41b41dbac0c7f250.jsonl[4363] _id=6aba962a485cab4c956aa009 ts=2026-09-28T16:30:34.4610000Z; 71h 52m: 6aa4142c41b41dbac0c7f250.jsonl[4985] _id=6aba973f485cab4c956ab84b ts=2026-09-28T16:35:11.7250000Z -> 6aa4142c41b41dbac0c7f250.jsonl[11222] _id=6abe89f6485cab4c95abec56 ts=2026-10-01T16:27:34.7820000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa4142c41b41dbac0c7f250.jsonl[13901] _id=6abe9338485cab4c95ac42c0 ts=2026-10-01T17:07:04.4620000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13914] _id=6ac3cf01de269131f9ada457 ts=2026-10-05T16:23:28.1540000Z; 71h 19m: 6aa4142c41b41dbac0c7f250.jsonl[3640] _id=6ab6a975485cab4c955d32b9 ts=2026-09-25T17:03:49.6630000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3768] _id=6aba9494485cab4c956a718c ts=2026-09-28T16:23:48.0150000Z; 47h 34m: 6aa4142c41b41dbac0c7f250.jsonl[5147] _id=6aba9b27485cab4c956ad7ba ts=2026-09-28T16:51:51.0420000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8192] _id=6abd3817485cab4c958d9d02 ts=2026-09-30T16:25:59.2430000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 432 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f250.jsonl[19782] _id=6ac65e40de269131f9bb52f6 ts=2026-10-07T14:59:12.5850000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19783] _id=6ac65e40de269131f9bb52f7 ts=2026-10-07T14:59:12.5850000Z; 0ms: 6aa4142c41b41dbac0c7f250.jsonl[19866] _id=6ac65e7ede269131f9bb58bc ts=2026-10-07T15:00:14.6380000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19867] _id=6ac65e7ede269131f9bb58bd ts=2026-10-07T15:00:14.6380000Z; 1ms: 6aa4142c41b41dbac0c7f250.jsonl[10936] _id=6abd3d8f485cab4c958ea5ec ts=2026-09-30T16:49:19.2400000Z -> 6aa4142c41b41dbac0c7f250.jsonl[10934] _id=6abd3d8f485cab4c958ea5f2 ts=2026-09-30T16:49:19.2410000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 30m 
  - Evidence: 95h 30m: 6aa4142c41b41dbac0c7f250.jsonl[13751] _id=6abe8ffb485cab4c95ac2a67 ts=2026-10-01T16:53:15.1760000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13936] _id=6ac3cf1dde269131f9ada4b5 ts=2026-10-05T16:23:57.3950000Z; 71h 23m: 6aa4142c41b41dbac0c7f250.jsonl[3597] _id=6ab6a868485cab4c955d0eb9 ts=2026-09-25T16:59:20.1860000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3685] _id=6aba946f485cab4c956a6ccc ts=2026-09-28T16:23:11.1660000Z; 46h 18m: 6aa4142c41b41dbac0c7f250.jsonl[7639] _id=6abaacf4485cab4c956f7569 ts=2026-09-28T18:07:48.2800000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8190] _id=6abd3817485cab4c958d9cfb ts=2026-09-30T16:25:59.2200000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1704 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f250.jsonl[113] _id=6ab3ff9e485cab4c954e68a6 ts=2026-09-23T16:34:38.3060000Z -> 6aa4142c41b41dbac0c7f250.jsonl[119] _id=6ab3ff9e485cab4c954e68aa ts=2026-09-23T16:34:38.3060000Z; 0ms: 6aa4142c41b41dbac0c7f250.jsonl[116] _id=6ab3ff9e485cab4c954e68a2 ts=2026-09-23T16:34:38.3050000Z -> 6aa4142c41b41dbac0c7f250.jsonl[118] _id=6ab3ff9e485cab4c954e68a4 ts=2026-09-23T16:34:38.3050000Z; 0ms: 6aa4142c41b41dbac0c7f250.jsonl[17019] _id=6ac525d4de269131f9b542cf ts=2026-10-06T16:46:12.4520000Z -> 6aa4142c41b41dbac0c7f250.jsonl[17044] _id=6ac525d4de269131f9b542d3 ts=2026-10-06T16:46:12.4520000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6aa4142c41b41dbac0c7f250.jsonl[3069] _id=6ab6a59b485cab4c955c815c ts=2026-09-25T16:47:23.9890000Z -> 6aa4142c41b41dbac0c7f250.jsonl[9069] _id=6abd39cf485cab4c958dcffe ts=2026-09-30T16:33:18.9730000Z; 95h 38m: 6aa4142c41b41dbac0c7f250.jsonl[13447] _id=6abe8f17485cab4c95ac1e59 ts=2026-10-01T16:49:25.2420000Z -> 6aa4142c41b41dbac0c7f250.jsonl[14094] _id=6ac3d00cde269131f9adac43 ts=2026-10-05T16:27:54.5970000Z; 24h 13m: 6aa4142c41b41dbac0c7f250.jsonl[14539] _id=6ac3d036de269131f9adb25b ts=2026-10-05T16:28:25.3420000Z -> 6aa4142c41b41dbac0c7f250.jsonl[16677] _id=6ac524dfde269131f9b528bd ts=2026-10-06T16:42:07.1740000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6aa4142c41b41dbac0c7f250.jsonl[7723] _id=6abd37cf485cab4c958d8f80 ts=2026-09-23T16:41:16.386Z -> 6aa4142c41b41dbac0c7f250.jsonl[7720] _id=6abd37cf485cab4c958d8f84 ts=2026-09-23T16:41:16.391Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 90h 57m 
  - Evidence: 90h 57m: 6aa4142c41b41dbac0c7f250.jsonl[13890] _id=6abe933c485cab4c95ac42c8 ts=2026-10-01T17:07:08.5080000Z -> 6aa4142c41b41dbac0c7f250.jsonl[21209] _id=6ac679dbde269131f9bd5e8e ts=2026-10-05T12:04:36.965Z; 71h 18m: 6aa4142c41b41dbac0c7f250.jsonl[3643] _id=6ab6a984485cab4c955d3409 ts=2026-09-25T17:04:04.1640000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3683] _id=6aba946d485cab4c956a6ca4 ts=2026-09-28T16:23:03.4230000Z; 46h 17m: 6aa4142c41b41dbac0c7f250.jsonl[7643] _id=6abaad01485cab4c956f75dd ts=2026-09-28T18:08:01.7680000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8191] _id=6abd3817485cab4c958d9cf6 ts=2026-09-30T16:25:52.9250000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 30m 
  - Evidence: 95h 30m: 6aa4142c41b41dbac0c7f250.jsonl[13657] _id=6abe8fe6485cab4c95ac2887 ts=2026-10-01T16:52:51.6880000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13922] _id=6ac3cf02de269131f9ada463 ts=2026-10-05T16:23:28.5950000Z; 72h 13m: 6aa4142c41b41dbac0c7f250.jsonl[3020] _id=6ab6a549485cab4c955c5257 ts=2026-09-25T16:46:01.5290000Z -> 6aa4142c41b41dbac0c7f250.jsonl[6255] _id=6aba9d06485cab4c956b458b ts=2026-09-28T16:59:49.7280000Z; 47h 35m: 6aa4142c41b41dbac0c7f250.jsonl[6265] _id=6aba9d07485cab4c956b4591 ts=2026-09-28T16:59:50.6140000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8849] _id=6abd3a34485cab4c958ddb4a ts=2026-09-30T16:35:00.2820000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3617 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f250.jsonl[10000] _id=6abd3c28485cab4c958e75f3 ts=2026-09-30T16:43:18.5350000Z -> 6aa4142c41b41dbac0c7f250.jsonl[10009] _id=6abd3c28485cab4c958e75fb ts=2026-09-30T16:43:18.5350000Z; 0ms: 6aa4142c41b41dbac0c7f250.jsonl[10003] _id=6abd3c29485cab4c958e7643 ts=2026-09-30T16:43:18.8150000Z -> 6aa4142c41b41dbac0c7f250.jsonl[10004] _id=6abd3c29485cab4c958e764a ts=2026-09-30T16:43:18.8150000Z; 0ms: 6aa4142c41b41dbac0c7f250.jsonl[10004] _id=6abd3c29485cab4c958e764a ts=2026-09-30T16:43:18.8150000Z -> 6aa4142c41b41dbac0c7f250.jsonl[10014] _id=6abd3c29485cab4c958e7657 ts=2026-09-30T16:43:18.8150000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 166h 13m 
  - Evidence: 166h 13m: 6aa4142c41b41dbac0c7f250.jsonl[9094] _id=6abd3a02485cab4c958dd3ba ts=2026-09-30T16:34:10.4980000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19447] _id=6ac65ba1de269131f9bb19ec ts=2026-10-07T14:48:01.6880000Z; 119h 45m: 6aa4142c41b41dbac0c7f250.jsonl[3071] _id=6ab6a59e485cab4c955c8341 ts=2026-09-25T16:47:26.9640000Z -> 6aa4142c41b41dbac0c7f250.jsonl[9067] _id=6abd39ce485cab4c958dcffc ts=2026-09-30T16:33:18.9690000Z; 17m 2s: 6aa4142c41b41dbac0c7f250.jsonl[19493] _id=6ac65bb0de269131f9bb1b39 ts=2026-10-07T14:48:16.4630000Z -> 6aa4142c41b41dbac0c7f250.jsonl[20329] _id=6ac65faede269131f9bb7864 ts=2026-10-07T15:05:18.8280000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 96h 39m 
  - Evidence: 96h 39m: 6aa4142c41b41dbac0c7f250.jsonl[11220] _id=6abe89f6485cab4c95abec52 ts=2026-10-01T16:27:34.7750000Z -> 6aa4142c41b41dbac0c7f250.jsonl[15188] _id=6ac3d940de269131f9ae7945 ts=2026-10-05T17:07:12.7790000Z; 71h 30m: 6aa4142c41b41dbac0c7f250.jsonl[3324] _id=6ab6a77b485cab4c955cff1f ts=2026-09-25T16:55:23.8910000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3793] _id=6aba94fb485cab4c956a7dff ts=2026-09-28T16:25:31.2780000Z; 47h 42m: 6aa4142c41b41dbac0c7f250.jsonl[5024] _id=6aba99c1485cab4c956aca81 ts=2026-09-28T16:45:53.7050000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8578] _id=6abd38ad485cab4c958daea1 ts=2026-09-30T16:28:29.7280000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.023s shown 
  - Evidence: 20ms: 6aa4142c41b41dbac0c7f250.jsonl[3311] _id=6ab6a76e485cab4c955cfdb5 ts=2026-09-25T16:55:10.8320000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3314] _id=6ab6a76e485cab4c955cfdb7 ts=2026-09-25T16:55:10.8520000Z; 23ms: 6aa4142c41b41dbac0c7f250.jsonl[3314] _id=6ab6a76e485cab4c955cfdb7 ts=2026-09-25T16:55:10.8520000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3312] _id=6ab6a76f485cab4c955cfdc3 ts=2026-09-25T16:55:10.8750000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 310h 30m 
  - Evidence: 310h 30m: 6aa4142c41b41dbac0c7f250.jsonl[495] _id=6ab54ed4485cab4c9552faf3 ts=2026-09-24T16:24:52.4050000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19635] _id=6ac65d70de269131f9bb3cbe ts=2026-10-07T14:55:44.7240000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 310h 30m 
  - Evidence: 310h 30m: 6aa4142c41b41dbac0c7f250.jsonl[493] _id=6ab54ed4485cab4c9552faf7 ts=2026-09-24T16:24:52.4330000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19592] _id=6ac65d41de269131f9bb3a88 ts=2026-10-07T14:54:57.4880000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.031s..0.031s shown 
  - Evidence: 31ms: 6aa4142c41b41dbac0c7f250.jsonl[19835] _id=6ac65edcde269131f9bb6442 ts=2026-10-07T15:01:48.3860000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19838] _id=6ac65edcde269131f9bb6445 ts=2026-10-07T15:01:48.4170000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 310h 30m 
  - Evidence: 310h 30m: 6aa4142c41b41dbac0c7f250.jsonl[478] _id=6ab54ecf485cab4c9552fa79 ts=2026-09-24T16:24:47.4230000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19597] _id=6ac65d4dde269131f9bb3af7 ts=2026-10-07T14:55:09.3790000Z; 23h 15m: 6aa4142c41b41dbac0c7f250.jsonl[8167] _id=6abd37f5485cab4c958d98c6 ts=2026-09-23T17:03:50.243Z -> 6aa4142c41b41dbac0c7f250.jsonl[213] _id=6ab54d7d485cab4c9552e985 ts=2026-09-24T16:19:11.0110000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 125 interval(s) ≤ 0.015s..0.017s shown 
  - Evidence: 15ms: 6aa4142c41b41dbac0c7f250.jsonl[19661] _id=6ac65d90de269131f9bb3f57 ts=2026-10-07T14:56:16.4850000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19662] _id=6ac65d90de269131f9bb3f58 ts=2026-10-07T14:56:16.5000000Z; 15ms: 6aa4142c41b41dbac0c7f250.jsonl[19799] _id=6ac65e5bde269131f9bb551f ts=2026-10-07T14:59:39.3470000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19800] _id=6ac65e5bde269131f9bb5521 ts=2026-10-07T14:59:39.3620000Z; 17ms: 6aa4142c41b41dbac0c7f250.jsonl[19596] _id=6ac65d6bde269131f9bb3c6e ts=2026-10-07T14:55:39.1260000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19622] _id=6ac65d6bde269131f9bb3c70 ts=2026-10-07T14:55:39.1430000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 310h 35m 
  - Evidence: 310h 35m: 6aa4142c41b41dbac0c7f250.jsonl[413] _id=6ab54e97485cab4c9552f7b3 ts=2026-09-24T16:23:52.4250000Z -> 6aa4142c41b41dbac0c7f250.jsonl[19788] _id=6ac65e50de269131f9bb5440 ts=2026-10-07T14:59:27.9870000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 6aa4142c41b41dbac0c7f250.jsonl[13033] _id=6abe8b22485cab4c95ac0ca5 ts=2026-10-01T16:32:34.2810000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13913] _id=6ac3cef3de269131f9ada439 ts=2026-10-05T16:23:15.5140000Z; 71h 56m: 6aa4142c41b41dbac0c7f250.jsonl[778] _id=6ab6a0a5485cab4c95594c0a ts=2026-09-25T16:26:13.9090000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3674] _id=6aba9457485cab4c956a6aa2 ts=2026-09-28T16:22:47.1010000Z; 48h 1m: 6aa4142c41b41dbac0c7f250.jsonl[3674] _id=6aba9457485cab4c956a6aa2 ts=2026-09-28T16:22:47.1010000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8183] _id=6abd37f6485cab4c958d98ee ts=2026-09-30T16:24:44.9280000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 82h 7m 
  - Evidence: 82h 7m: 6aa4142c41b41dbac0c7f250.jsonl[21208] _id=6ac679dbde269131f9bd5e8d ts=2026-10-02T06:15:17.999Z -> 6aa4142c41b41dbac0c7f250.jsonl[13920] _id=6ac3cef3de269131f9ada437 ts=2026-10-05T16:23:15.5130000Z; 71h 33m: 6aa4142c41b41dbac0c7f250.jsonl[3130] _id=6ab6a604485cab4c955cbcf9 ts=2026-09-25T16:49:08.5460000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3675] _id=6aba9457485cab4c956a6a9e ts=2026-09-28T16:22:47.1000000Z; 46h 16m: 6aa4142c41b41dbac0c7f250.jsonl[7642] _id=6abaad06485cab4c956f7609 ts=2026-09-28T18:08:06.9820000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8174] _id=6abd37f6485cab4c958d98e8 ts=2026-09-30T16:24:44.8880000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 82h 44m 
  - Evidence: 82h 44m: 6aa4142c41b41dbac0c7f250.jsonl[21207] _id=6ac679dbde269131f9bd5e8c ts=2026-10-02T06:15:17.494Z -> 6aa4142c41b41dbac0c7f250.jsonl[15075] _id=6ac3d77ede269131f9ae58a1 ts=2026-10-05T16:59:42.4120000Z; 71h 40m: 6aa4142c41b41dbac0c7f250.jsonl[3641] _id=6ab6a98a485cab4c955d3455 ts=2026-09-25T17:04:11.0290000Z -> 6aa4142c41b41dbac0c7f250.jsonl[5014] _id=6aba995c485cab4c956ac7fb ts=2026-09-28T16:44:12.2900000Z; 47h 44m: 6aa4142c41b41dbac0c7f250.jsonl[8184] _id=6abd37f6485cab4c958d98da ts=2026-09-23T17:04:07.872Z -> 6aa4142c41b41dbac0c7f250.jsonl[3128] _id=6ab6a5ff485cab4c955cba2f ts=2026-09-25T16:49:03.5520000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4142c41b41dbac0c7f250.jsonl[13817] _id=6abe90d8485cab4c95ac35aa ts=2026-10-01T16:56:56.0590000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13916] _id=6ac3cf01de269131f9ada45d ts=2026-10-05T16:23:28.1940000Z; 71h 28m: 6aa4142c41b41dbac0c7f250.jsonl[3305] _id=6ab6a750485cab4c955cfa1f ts=2026-09-25T16:54:40.4820000Z -> 6aa4142c41b41dbac0c7f250.jsonl[3684] _id=6aba946d485cab4c956a6caf ts=2026-09-28T16:23:09.2410000Z; 48h 2m: 6aa4142c41b41dbac0c7f250.jsonl[3684] _id=6aba946d485cab4c956a6caf ts=2026-09-28T16:23:09.2410000Z -> 6aa4142c41b41dbac0c7f250.jsonl[8194] _id=6abd3817485cab4c958d9d0a ts=2026-09-30T16:25:59.2880000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 6aa4142c41b41dbac0c7f250.jsonl[13052] _id=6abe8b50485cab4c95ac0e18 ts=2026-10-01T16:33:19.3100000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13038] _id=6abe8b50485cab4c95ac0e1a ts=2026-10-01T16:33:19.3120000Z; 2ms: 6aa4142c41b41dbac0c7f250.jsonl[195] _id=6ab54d51485cab4c9552e84d ts=2026-09-24T16:18:26.1530000Z -> 6aa4142c41b41dbac0c7f250.jsonl[196] _id=6ab54d51485cab4c9552e84f ts=2026-09-24T16:18:26.1550000Z; 4ms: 6aa4142c41b41dbac0c7f250.jsonl[13916] _id=6ac3cf01de269131f9ada45d ts=2026-10-05T16:23:28.1940000Z -> 6aa4142c41b41dbac0c7f250.jsonl[13921] _id=6ac3cf01de269131f9ada45f ts=2026-10-05T16:23:28.1980000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 21 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[7718] _id=6abd37cf485cab4c958d8f5e ts=2026-09-23T16:41:12.302Z`; `6aa4142c41b41dbac0c7f250.jsonl[7729] _id=6abd37d0485cab4c958d8fcf ts=2026-09-23T16:41:56.475Z`; `6aa4142c41b41dbac0c7f250.jsonl[7747] _id=6abd37d1485cab4c958d9012 ts=2026-09-23T16:42:45.462Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 355 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[1255] _id=6ab6a372485cab4c955b1d6c ts=2026-09-25T16:38:06.9180000Z`; `6aa4142c41b41dbac0c7f250.jsonl[1236] _id=6ab6a372485cab4c955b1d8c ts=2026-09-25T16:38:06.9300000Z`; `6aa4142c41b41dbac0c7f250.jsonl[1265] _id=6ab6a374485cab4c955b1ece ts=2026-09-25T16:38:10.5080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 684 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[942] _id=6ab6a2f7485cab4c955acf2d ts=2026-09-25T16:36:06.5340000Z`; `6aa4142c41b41dbac0c7f250.jsonl[948] _id=6ab6a2f7485cab4c955acf41 ts=2026-09-25T16:36:06.6050000Z`; `6aa4142c41b41dbac0c7f250.jsonl[937] _id=6ab6a2f8485cab4c955acf5b ts=2026-09-25T16:36:06.6270000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[19838] _id=6ac65edcde269131f9bb6445 ts=2026-10-07T15:01:48.4170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 25 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[8158] _id=6abd37f4485cab4c958d9854 ts=2026-09-23T17:03:34.08Z`; `6aa4142c41b41dbac0c7f250.jsonl[8159] _id=6abd37f4485cab4c958d9859 ts=2026-09-23T17:03:34.162Z`; `6aa4142c41b41dbac0c7f250.jsonl[8160] _id=6abd37f4485cab4c958d9860 ts=2026-09-23T17:03:34.217Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[7676] _id=6abd37d1485cab4c958d8ff7 ts=2026-09-23T16:42:31.209Z`; `6aa4142c41b41dbac0c7f250.jsonl[7785] _id=6abd37d7485cab4c958d9148 ts=2026-09-23T16:46:03.163Z`; `6aa4142c41b41dbac0c7f250.jsonl[8154] _id=6abd37f3485cab4c958d9811 ts=2026-09-23T17:02:46.957Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[3682] _id=6aba946d485cab4c956a6ca1 ts=?`; `6aa4142c41b41dbac0c7f250.jsonl[8195] _id=6abd3817485cab4c958d9cf4 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 706 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[1275] _id=6ab6a374485cab4c955b1ee8 ts=2026-09-25T16:38:10.5240000Z`; `6aa4142c41b41dbac0c7f250.jsonl[1266] _id=6ab6a374485cab4c955b1eff ts=2026-09-25T16:38:10.5400000Z`; `6aa4142c41b41dbac0c7f250.jsonl[1278] _id=6ab6a374485cab4c955b1f15 ts=2026-09-25T16:38:10.5420000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1126 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[939] _id=6ab6a2f7485cab4c955ace94 ts=2026-09-25T16:36:06.4770000Z`; `6aa4142c41b41dbac0c7f250.jsonl[983] _id=6ab6a2fa485cab4c955ad185 ts=2026-09-25T16:36:08.7600000Z`; `6aa4142c41b41dbac0c7f250.jsonl[1103] _id=6ab6a358485cab4c955b0d38 ts=2026-09-25T16:36:10.2100000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 19 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[3314] _id=6ab6a76e485cab4c955cfdb7 ts=2026-09-25T16:55:10.8520000Z`; `6aa4142c41b41dbac0c7f250.jsonl[3312] _id=6ab6a76f485cab4c955cfdc3 ts=2026-09-25T16:55:10.8750000Z`; `6aa4142c41b41dbac0c7f250.jsonl[3793] _id=6aba94fb485cab4c956a7dff ts=2026-09-28T16:25:31.2780000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[412] _id=6ab54e96485cab4c9552f7a3 ts=2026-09-24T16:23:51.3450000Z`; `6aa4142c41b41dbac0c7f250.jsonl[19789] _id=6ac65e52de269131f9bb5475 ts=2026-10-07T14:59:30.8660000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 29 unmatched 'DialogueStartEvent' (totals: 287 start, 279 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 182 unmatched 'BecameCameraCentered' (totals: 1002 open, 1175 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 284 unmatched 'BecameVisible' (totals: 1441 open, 1841 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 22 open, 20 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 6 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 32 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 880 of 22547 adjacent _id pairs reverse in client time; worst 464309.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f250.jsonl[21203] _id=6ac661aade269131f9bb959f ts=2026-10-07T15:13:46.8530000Z`; `6aa4142c41b41dbac0c7f250.jsonl[21207] _id=6ac679dbde269131f9bd5e8c ts=2026-10-02T06:15:17.494Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.06s, min -604171.13s, max +1.29s over 22548 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f250\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `InputEvent` — 12732 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (7023); Unit 3 Dev (4030); Unit 3 Dungeon Dev (1265); Unit 1 Dev (414)
- **Intervals:** median 0.18s (p5 0.02s / p95 1.45s, n=12731)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 12732/12732 records)
    "pressed"  x12732
data.actionType  (string, 12732/12732 records)
    "Move"  x10155
    "Jump"  x1325
    "Interact"  x611
    "Sprint"  x266
    "SkipCinematic"  x256
    "Hoverboard"  x59
    "Descend"  x20
    "Map"  x17
    "Ascend"  x14
    "Pause"  x5
    "ToggleDebug"  x4
data.key  (string, 12732/12732 records, 16 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 12732/12732 records)
    "Player"  x11738
    "Drone"  x994
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 5459 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (4859); Unit 3 Dungeon Dev (600)
- **Intervals:** median 0.02s (p5 0.00s / p95 0.59s, n=5458)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5459/5459 records)
    "BecameInvisible"  x1841
    "BecameVisible"  x1441
    "BecameCameraUncentered"  x1175
    "BecameCameraCentered"  x1002
data.pieceId  (string, 5459/5459 records)
    24 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5459/5459 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1918 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1186); Unit 3 Dev (385); Unit 1 Dev (239); Unit 3 Dungeon Dev (108)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.16s, n=1914)
- **Fields under `data`:**

```text
data.position  (object, 1918/1918 records)
data.position.x  (number, 1918/1918 records)
    numeric range -594.592 .. 1548.1 (504 unique)
data.position.y  (number, 1918/1918 records)
    numeric range -114.818 .. 405.22 (395 unique)
data.position.z  (number, 1918/1918 records)
    numeric range -1048.47 .. 1962.15 (504 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1451 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (712); Unit 3 Dev (344); Unit 1 Dev (219); Unit 3 Dungeon Dev (176)
- **eventKey:** present on 885 of 1451 records
- **Intervals:** median 4.53s (p5 0.00s / p95 48.11s, n=1450)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x885; [conversationId, dialogueEventType] x566
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1451/1451 records)
    numeric range 8 .. 101 (27 unique)
data.dialogueEventType  (string, 1451/1451 records)
    "DialogueNodeEvent"  x885
    "DialogueStartEvent"  x287
    "DialogueFinishEvent"  x279
data.nodeId  (number, 885/1451 records)
    numeric range 0 .. 290 (189 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 467 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (273); Unit 1 Dev (194)
- **Intervals:** median 0.33s (p5 0.02s / p95 5.43s, n=466)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 467/467 records)
    "argumentationNodeHoverEnd"  x212
    "argumentationNodeHoverStart"  x187
    "argumentationNodeAdd"  x37
    "argumentationNodeRemove"  x31
data.argumentationTitle  (string, 467/467 records)
    "Unit 3 - Pollution Upstream"  x273
    "Unit 1 - Freshwater"  x145
    "Unit 1 - Argumentation Tutorial"  x49
data.nodeName  (string, 467/467 records)
    "A"  x97
    "1"  x86
    "I"  x75
    "II"  x60
    "B"  x56
    "4"  x34
    "2"  x26
    "3"  x24
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 151 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (75); Unit 3 Dungeon Dev (51); Unit 1 Dev (19); Unit 3 Dev (6)
- **Intervals:** median 4.93s (p5 0.85s / p95 4032.60s, n=150)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 151/151 records)
    15 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 151/151 records)
    40 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 99 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (78); Unit 3 Dev (21)
- **Intervals:** median 2.42s (p5 0.32s / p95 84770.59s, n=98)
- **`data` key-set variants:** [actionType, featureUsed, location] x43; [actionType, featureUsed] x42; [actionType, featureUsed, legendName] x14
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 99/99 records)
    "WaypointMoveEvent"  x40
    "MapOpenEvent"  x22
    "MapCloseEvent"  x20
    "Selected"  x10
    "Unselected"  x4
    "WaypointSetEvent"  x3
data.featureUsed  (string, 99/99 records)
    "Waypoint"  x43
    "Map"  x42
    "Legend"  x14
data.legendName  (string, 14/99 records)
    "240 ft"  x3
    "360 ft"  x3
    "Water"  x3
    "270 ft"  x2
    "330 ft"  x2
    "300 ft"  x1
data.location  (object, 43/99 records)
data.location.x  (number, 43/99 records)
    numeric range -332.09 .. 481.91 (38 unique)
data.location.y  (number, 43/99 records)
    numeric range -315.5 .. 297.5 (38 unique)
data.location.z  (number, 43/99 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 51 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (43); Unit 3 Dev (8)
- **Intervals:** median 0.23s (p5 0.11s / p95 94.76s, n=50)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 51/51 records)
    "submitAnswerEvent"  x51
data.answerSubmitted  (string, 51/51 records)
    "1,"  x36
    "A,1,I"  x6
    "A,"  x2
    "B,4,II"  x2
    "A,1,II"  x1
    "A,2,I"  x1
    "A,5,I"  x1
    "B,1,I"  x1
    "B,1,II"  x1
data.argumentationTitle  (string, 51/51 records)
    "Unit 1 - Freshwater"  x42
    "Unit 3 - Pollution Upstream"  x8
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `questEvent` — 51 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 1 Dev (15); Unit 3 Dev (10); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 51 of 51 records
- **Intervals:** median 282.98s (p5 0.00s / p95 134193.71s, n=50)
- **`data` key-set variants:** [questEventType, questID, questName] x32; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 51/51 records)
    "questActiveEvent"  x32
    "questFinishEvent"  x19
data.questID  (string, 51/51 records)
    13 unique values (see csv/event_unique_values.csv)
data.questName  (string, 51/51 records)
    13 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/51 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 44 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (16)
- **Intervals:** median 0.99s (p5 0.19s / p95 921.53s, n=43)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x38; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/44 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/44 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 38/44 records)
    "RightDrag"  x22
    "LeftDrag"  x16
data.currentSoilType  (string, 38/44 records)
    "CLAY"  x8
    "SANDGRAVEL"  x8
    "SAND"  x7
    "CLAYSAND"  x6
    "CLAYROCK"  x5
    "GRAVEL"  x4
data.isCorrectSelection  (string, 38/44 records)
    "false"  x30
    "true"  x8
data.waterLevelStatus  (string, 38/44 records)
    "TooHigh"  x26
    "Proper"  x12
data.waterRetentionChange  (string, 38/44 records)
    "Decrease"  x16
    "Increase"  x14
    "NoChange"  x8
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 36 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 2 Prod (Refactor) (13); Unit 1 Dev (7); Unit 3 Dev (2)
- **Intervals:** median 684.57s (p5 5.33s / p95 193904.10s, n=35)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 36/36 records)
    true  x36
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 26 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (6); Unit 3 Dev (3); Unit 3 Dungeon Dev (1)
- **Intervals:** median 907.48s (p5 4.45s / p95 240780.14s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 17 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (3); MainMenu (2); Unit 1 Dev (2); Unit 3 Dungeon Dev (2)
- **Intervals:** median 42473.99s (p5 11.91s / p95 280503.24s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "DebugMenuStateChanged"  x17
data.isOpened  (bool, 17/17 records)
    false  x17
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 16 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dungeon Dev (2)
- **Intervals:** median 2.40s (p5 1.04s / p95 398108.87s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "Close"  x8
    "Open"  x8
data.toolName  (string, 16/16 records, 16 empty-string)
    ""  x16
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 85764.70s (p5 321.26s / p95 293412.41s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 3 Dev (3)
- **Intervals:** median 2.88s (p5 0.92s / p95 782738.81s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x6
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 134.94s (p5 5.20s / p95 838456.52s, n=6)
- **Open findings:** 2 — see sections 5-8
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

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x2
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

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
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (28 records)
- `TopographicMapEvent` data.actionType: "Selected" (10x); "Unselected" (4x); "WaypointMoveEvent" (40x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (14x); "Waypoint" (43x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (31x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*