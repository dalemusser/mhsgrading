# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f266

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f266
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f266.jsonl
- **Records:** 5093 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f266
- **Time span:** 2026-09-24T17:42:42.173000+00:00 .. 2026-10-01T12:51:14.810000+00:00 (163h 8m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f266\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 5093 records, 3 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 87 INFO, 6 NOT_TESTED, 61 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium: Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: baseline field(s) absent this build
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2232 | 43.82 | 1 | 1 | 0 | 2026-09-28T18:45:38.213000+00:00 | 2026-09-29T18:29:58.152000+00:00 | 23h 44m |
| InputEvent | 931 | 18.28 | 1 | 2 | 0 | 2026-09-24T17:43:27.470000+00:00 | 2026-10-01T12:51:07.044000+00:00 | 163h 7m |
| PlayerPositionEvent | 772 | 15.16 | 1 | 2 | 0 | 2026-09-24T17:43:05.814000+00:00 | 2026-10-01T12:51:14.810000+00:00 | 163h 8m |
| DialogueEvent | 743 | 14.59 | 1 | 2 | 484 | 2026-09-24T17:43:28.805000+00:00 | 2026-09-30T18:37:04.028000+00:00 | 144h 53m |
| argumentationNodeEvent | 133 | 2.61 | 1 | 1 | 0 | 2026-09-28T18:24:00.694000+00:00 | 2026-09-28T18:33:41.135000+00:00 | 9m 40s |
| ObjectInterEvent | 104 | 2.04 | 1 | 2 | 0 | 2026-09-24T17:49:09.346000+00:00 | 2026-09-29T18:31:39.553000+00:00 | 120h 42m |
| argumentationAnswerEvent | 52 | 1.02 | 1 | 1 | 0 | 2026-09-28T18:25:08.813000+00:00 | 2026-09-28T18:33:43.140000+00:00 | 8m 34s |
| TopographicMapEvent | 41 | 0.81 | 1 | 1 | 0 | 2026-09-28T18:46:19.914000+00:00 | 2026-09-30T18:35:46.703000+00:00 | 47h 49m |
| questEvent | 28 | 0.55 | 1 | 2 | 28 | 2026-09-24T17:43:28.783000+00:00 | 2026-10-01T12:50:54.690000+00:00 | 163h 7m |
| argumentationToolEvent | 17 | 0.33 | 1 | 1 | 0 | 2026-09-28T18:24:35.147000+00:00 | 2026-09-28T18:32:06.938000+00:00 | 7m 31s |
| gameWindowFocusEvent | 9 | 0.18 | 1 | 2 | 0 | 2026-09-24T17:42:42.173000+00:00 | 2026-10-01T12:50:42.114000+00:00 | 163h 7m |
| DEBUGMenu | 7 | 0.14 | 1 | 2 | 0 | 2026-09-24T17:43:05.805000+00:00 | 2026-10-01T12:50:48.695000+00:00 | 163h 7m |
| gameStartEvent | 7 | 0.14 | 1 | 1 | 0 | 2026-09-24T17:42:42.174000+00:00 | 2026-10-01T12:50:42.115000+00:00 | 163h 7m |
| DaniEvent | 6 | 0.12 | 1 | 1 | 0 | 2026-09-29T18:21:41.326000+00:00 | 2026-09-29T18:21:53.318000+00:00 | 12.0s |
| argumentationEvent | 4 | 0.08 | 1 | 1 | 0 | 2026-09-28T18:24:37.069000+00:00 | 2026-09-28T18:33:43.171000+00:00 | 9m 6s |
| Soil Key Puzzle | 2 | 0.04 | 1 | 1 | 0 | 2026-09-29T18:31:39.549000+00:00 | 2026-09-29T18:31:42.538000+00:00 | 3.0s |
| crash | 2 | 0.04 | 1 | 1 | 0 |  |  | ? |
| gameWindowUnfocusEvent | 2 | 0.04 | 1 | 1 | 0 | 2026-09-24T17:47:50.902000+00:00 | 2026-09-24T17:56:43.901000+00:00 | 8m 52s |
| EndOfUnit | 1 | 0.02 | 1 | 1 | 0 | 2026-09-28T18:40:34.131000+00:00 | 2026-09-28T18:40:34.131000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 75210.509s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.273s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.055s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.989s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.694s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 2.904s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.038s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 75220.636s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 33969.313s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 532.999s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dev; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; p; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Insert; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 180 ft; 240 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.4x vs baseline. 
  - Observed: 52 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 1,I; 1,II; A,1,; A,I; A,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 4 records 
  - Expected: 14 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; B; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 9 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 2 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 18 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[170] _id=6ab5630a485cab4c9553a6ea ts=2026-09-24T17:51:06.5090000Z`; `6aa4144c41b41dbac0c7f266.jsonl[237] _id=6ab563f8485cab4c9553bb30 ts=2026-09-24T17:55:04.3520000Z`; `6aa4144c41b41dbac0c7f266.jsonl[333] _id=6ab5665c485cab4c9554052a ts=2026-09-24T18:05:16.4170000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[2] _id=6ab56112485cab4c95537dcd ts=2026-09-24T17:42:42.1740000Z`; `6aa4144c41b41dbac0c7f266.jsonl[418] _id=6abaac98485cab4c956f6f65 ts=2026-09-28T18:06:16.4840000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1263] _id=6abab503485cab4c95704ad7 ts=2026-09-28T18:42:11.4040000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 9 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 9} 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1] _id=6ab56112485cab4c95537dca ts=2026-09-24T17:42:42.1730000Z`; `6aa4144c41b41dbac0c7f266.jsonl[88] _id=6ab56249485cab4c95539800 ts=2026-09-24T17:47:53.9430000Z`; `6aa4144c41b41dbac0c7f266.jsonl[256] _id=6ab5645d485cab4c9553c211 ts=2026-09-24T17:56:45.2450000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 2 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 2} 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[95] _id=6ab56246485cab4c955397d0 ts=2026-09-24T17:47:50.9020000Z`; `6aa4144c41b41dbac0c7f266.jsonl[254] _id=6ab5645b485cab4c9553c1e8 ts=2026-09-24T17:56:43.9010000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 15 of 41 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1426] _id=6abab5fc485cab4c95705d3f ts=2026-09-28T18:46:19.9140000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1437] _id=6abab623485cab4c95705f71 ts=2026-09-28T18:46:59.8320000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1620] _id=6abc003e485cab4c95843260 ts=2026-09-29T18:15:26.1600000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2231 | 0.0 | 0.055 | 38.306 | 1.139 | 84459.077 | 1.57 | 1082 | 1 |
| InputEvent | 930 | 0.001 | 1.273 | 631.462 | 21.858 | 345683.909 | 0.1 | 18 | 4 |
| PlayerPositionEvent | 770 | 9.89 | 10.0 | 762.547 | 10.04 | 345220.786 | 0.08 | 0 | 4 |
| DialogueEvent | 742 | 0.001 | 4.798 | 702.985 | 38.084 | 345279.806 | 0.09 | 200 | 3 |
| argumentationNodeEvent | 132 | 0.039 | 0.268 | 4.397 | 24.603 | 132.498 | 13.64 | 17 | 0 |
| ObjectInterEvent | 103 | 0.003 | 5.684 | 4218.934 | 301.516 | 345748.284 | 0.01 | 2 | 4 |
| argumentationAnswerEvent | 51 | 0.171 | 2.904 | 10.085 | 50.156 | 102.459 | 5.95 | 0 | 0 |
| TopographicMapEvent | 40 | 0.015 | 4.694 | 4304.17 | 5307.69 | 84876.612 | 0.01 | 2 | 3 |
| questEvent | 27 | 0.001 | 253.475 | 21749.848 | 84622.464 | 346333.472 | 0.0 | 5 | 7 |
| argumentationToolEvent | 16 | 0.095 | 2.038 | 28.237 | 113.333 | 150.296 | 2.12 | 0 | 0 |
| gameWindowFocusEvent | 8 | 311.77 | 33969.313 | 73409.993 | 255208.098 | 346171.237 | 0.0 | 0 | 6 |
| DEBUGMenu | 6 | 1396.987 | 75210.509 | 97877.148 | 281820.408 | 347001.726 | 0.0 | 0 | 6 |
| gameStartEvent | 6 | 1392.886 | 75220.636 | 97879.99 | 281829.87 | 347014.31 | 0.0 | 0 | 6 |
| DaniEvent | 5 | 2.081 | 2.171 | 2.398 | 3.053 | 3.21 | 25.02 | 0 | 0 |
| argumentationEvent | 3 | 40.295 | 42.553 | 182.034 | 421.184 | 463.254 | 0.33 | 0 | 0 |
| Soil Key Puzzle | 1 | 2.989 | 2.989 | 2.989 | 2.989 | 2.989 | 20.07 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameWindowUnfocusEvent | 1 | 532.999 | 532.999 | 532.999 | 532.999 | 532.999 | 0.11 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 70 group(s), 95 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1354] _id=6abab5d3485cab4c957059a1 ts=2026-09-28T18:45:38.7900000Z == 6aa4144c41b41dbac0c7f266.jsonl[1355] _id=6abab5d3485cab4c957059a3 ts=2026-09-28T18:45:38.7900000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1356] _id=6abab5d4485cab4c957059a7 ts=2026-09-28T18:45:38.8310000Z == 6aa4144c41b41dbac0c7f266.jsonl[1362] _id=6abab5d4485cab4c957059ab ts=2026-09-28T18:45:38.8310000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1352] _id=6abab5d8485cab4c95705a03 ts=2026-09-28T18:45:43.8220000Z == 6aa4144c41b41dbac0c7f266.jsonl[1371] _id=6abab5d8485cab4c95705a05 ts=2026-09-28T18:45:43.8220000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 24 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4144c41b41dbac0c7f266.jsonl[131] _id=6ab56295485cab4c95539dbf ts=2026-09-24T17:49:09.3460000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[124] _id=6ab56295485cab4c95539dc7 ts=2026-09-24T17:49:09.3490000Z`; `5ms: 6aa4144c41b41dbac0c7f266.jsonl[461] _id=6abaacf0485cab4c956f7549 ts=2026-09-28T18:07:44.6870000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[453] _id=6abaacf0485cab4c956f754d ts=2026-09-28T18:07:44.6920000Z`; `185ms: 6aa4144c41b41dbac0c7f266.jsonl[1880] _id=6abc00c1485cab4c958441a9 ts=2026-09-29T18:17:37.8320000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[1882] _id=6abc00c2485cab4c958441bb ts=2026-09-29T18:17:38.0170000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 501 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `381ms: 6aa4144c41b41dbac0c7f266.jsonl[1337] _id=6abab5d3485cab4c95705992 ts=2026-09-28T18:45:38.2130000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[1341] _id=6abab5d3485cab4c95705995 ts=2026-09-28T18:45:38.5940000Z`; `556ms: 6aa4144c41b41dbac0c7f266.jsonl[1345] _id=6abab5d5485cab4c957059cf ts=2026-09-28T18:45:39.5470000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[1346] _id=6abab5d5485cab4c957059d3 ts=2026-09-28T18:45:40.1030000Z`; `215ms: 6aa4144c41b41dbac0c7f266.jsonl[1346] _id=6abab5d5485cab4c957059d3 ts=2026-09-28T18:45:40.1030000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[1360] _id=6abab5d5485cab4c957059d5 ts=2026-09-28T18:45:40.3180000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `15ms: 6aa4144c41b41dbac0c7f266.jsonl[4331] _id=6abc0637485cab4c9584a971 ts=2026-09-29T18:40:55.3930000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[4329] _id=6abc0637485cab4c9584a985 ts=2026-09-29T18:40:55.4080000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 23 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `310ms: 6aa4144c41b41dbac0c7f266.jsonl[825] _id=6abab158485cab4c956ffbbf ts=2026-09-28T18:26:31.9930000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[826] _id=6abab158485cab4c956ffbc7 ts=2026-09-28T18:26:32.3030000Z`; `651ms: 6aa4144c41b41dbac0c7f266.jsonl[913] _id=6abab1d8485cab4c9570051a ts=2026-09-28T18:28:40.1660000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[917] _id=6abab1d8485cab4c95700525 ts=2026-09-28T18:28:40.8170000Z`; `694ms: 6aa4144c41b41dbac0c7f266.jsonl[917] _id=6abab1d8485cab4c95700525 ts=2026-09-28T18:28:40.8170000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[916] _id=6abab1d9485cab4c95700537 ts=2026-09-28T18:28:41.5110000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 26 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `426ms: 6aa4144c41b41dbac0c7f266.jsonl[780] _id=6abab0c7485cab4c956ff2cb ts=2026-09-28T18:24:07.1350000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[784] _id=6abab0c7485cab4c956ff2d5 ts=2026-09-28T18:24:07.5610000Z`; `281ms: 6aa4144c41b41dbac0c7f266.jsonl[783] _id=6abab0c7485cab4c956ff2d1 ts=2026-09-28T18:24:07.3750000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[781] _id=6abab0c7485cab4c956ff2d9 ts=2026-09-28T18:24:07.6560000Z`; `326ms: 6aa4144c41b41dbac0c7f266.jsonl[822] _id=6abab14c485cab4c956ffb09 ts=2026-09-28T18:26:20.1540000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[814] _id=6abab14c485cab4c956ffb11 ts=2026-09-28T18:26:20.4800000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `691ms: 6aa4144c41b41dbac0c7f266.jsonl[1011] _id=6abab23c485cab4c95700be5 ts=2026-09-28T18:30:20.7980000Z ~ 6aa4144c41b41dbac0c7f266.jsonl[1012] _id=6abab23d485cab4c95700bf1 ts=2026-09-28T18:30:21.4890000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6aa4144c41b41dbac0c7f266.jsonl[3] _id=6ab56129485cab4c95537f3f ts=2026-09-24T17:43:05.8050000Z -> 6aa4144c41b41dbac0c7f266.jsonl[420] _id=6abaaca3485cab4c956f6ffb ts=2026-09-28T18:06:27.5310000Z; 23h 57m: 6aa4144c41b41dbac0c7f266.jsonl[1552] _id=6abbffbc485cab4c95842503 ts=2026-09-29T18:13:16.1650000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4514] _id=6abd50c0485cab4c9590eea7 ts=2026-09-30T18:11:12.6170000Z; 23h 30m: 6aa4144c41b41dbac0c7f266.jsonl[1264] _id=6abab51a485cab4c95704cb5 ts=2026-09-28T18:42:34.2380000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1552] _id=6abbffbc485cab4c95842503 ts=2026-09-29T18:13:16.1650000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 54m 
  - Evidence: 95h 54m: 6aa4144c41b41dbac0c7f266.jsonl[411] _id=6ab56801485cab4c9554224c ts=2026-09-24T18:12:17.3960000Z -> 6aa4144c41b41dbac0c7f266.jsonl[435] _id=6abaacc1485cab4c956f728b ts=2026-09-28T18:06:57.2020000Z; 23h 26m: 6aa4144c41b41dbac0c7f266.jsonl[4505] _id=6abc07f4485cab4c9584c8c5 ts=2026-09-29T18:48:20.4620000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4587] _id=6abd517c485cab4c95910381 ts=2026-09-30T18:14:20.5110000Z; 23h 25m: 6aa4144c41b41dbac0c7f266.jsonl[1513] _id=6abab652485cab4c95706996 ts=2026-09-28T18:47:46.8820000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1560] _id=6abbffd2485cab4c95842627 ts=2026-09-29T18:13:38.3930000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 200 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f266.jsonl[1044] _id=6abab266485cab4c95700e2c ts=2026-09-28T18:31:02.0010000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1018] _id=6abab266485cab4c95700e31 ts=2026-09-28T18:31:02.0020000Z; 1ms: 6aa4144c41b41dbac0c7f266.jsonl[1121] _id=6abab2c2485cab4c95701705 ts=2026-09-28T18:32:34.5520000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1124] _id=6abab2c2485cab4c95701707 ts=2026-09-28T18:32:34.5530000Z; 1ms: 6aa4144c41b41dbac0c7f266.jsonl[4592] _id=6abd5195485cab4c9591068b ts=2026-09-30T18:14:45.0520000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4510] _id=6abd5195485cab4c9591068d ts=2026-09-30T18:14:45.0530000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa4144c41b41dbac0c7f266.jsonl[361] _id=6ab56655485cab4c955404a9 ts=2026-09-24T18:05:09.4400000Z -> 6aa4144c41b41dbac0c7f266.jsonl[425] _id=6abaacab485cab4c956f70fd ts=2026-09-28T18:06:33.3490000Z; 23h 25m: 6aa4144c41b41dbac0c7f266.jsonl[1505] _id=6abab64f485cab4c9570689c ts=2026-09-28T18:47:43.3440000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1550] _id=6abbffbd485cab4c95842509 ts=2026-09-29T18:13:17.0370000Z; 23h 23m: 6aa4144c41b41dbac0c7f266.jsonl[4485] _id=6abc07c5485cab4c9584c64f ts=2026-09-29T18:47:33.4430000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4518] _id=6abd50c7485cab4c9590ef43 ts=2026-09-30T18:11:18.6500000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f266.jsonl[421] _id=6abaacab485cab4c956f7109 ts=2026-09-28T18:06:33.3520000Z -> 6aa4144c41b41dbac0c7f266.jsonl[422] _id=6abaacab485cab4c956f7111 ts=2026-09-28T18:06:33.3530000Z; 1ms: 6aa4144c41b41dbac0c7f266.jsonl[422] _id=6abaacab485cab4c956f7111 ts=2026-09-28T18:06:33.3530000Z -> 6aa4144c41b41dbac0c7f266.jsonl[430] _id=6abaacab485cab4c956f7113 ts=2026-09-28T18:06:33.3540000Z; 1ms: 6aa4144c41b41dbac0c7f266.jsonl[429] _id=6abaacab485cab4c956f7103 ts=2026-09-28T18:06:33.3510000Z -> 6aa4144c41b41dbac0c7f266.jsonl[421] _id=6abaacab485cab4c956f7109 ts=2026-09-28T18:06:33.3520000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa4144c41b41dbac0c7f266.jsonl[355] _id=6ab5665c485cab4c95540528 ts=2026-09-24T18:05:16.4030000Z -> 6aa4144c41b41dbac0c7f266.jsonl[461] _id=6abaacf0485cab4c956f7549 ts=2026-09-28T18:07:44.6870000Z; 23h 29m: 6aa4144c41b41dbac0c7f266.jsonl[1319] _id=6abab5b1485cab4c9570561d ts=2026-09-28T18:45:05.7950000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1580] _id=6abbfff2485cab4c95842a71 ts=2026-09-29T18:14:10.7160000Z; 15m 56s: 6aa4144c41b41dbac0c7f266.jsonl[762] _id=6abab09a485cab4c956fef15 ts=2026-09-28T18:23:22.1440000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1212] _id=6abab457485cab4c95703633 ts=2026-09-28T18:39:19.0590000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6aa4144c41b41dbac0c7f266.jsonl[131] _id=6ab56295485cab4c95539dbf ts=2026-09-24T17:49:09.3460000Z -> 6aa4144c41b41dbac0c7f266.jsonl[124] _id=6ab56295485cab4c95539dc7 ts=2026-09-24T17:49:09.3490000Z; 5ms: 6aa4144c41b41dbac0c7f266.jsonl[461] _id=6abaacf0485cab4c956f7549 ts=2026-09-28T18:07:44.6870000Z -> 6aa4144c41b41dbac0c7f266.jsonl[453] _id=6abaacf0485cab4c956f754d ts=2026-09-28T18:07:44.6920000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa4144c41b41dbac0c7f266.jsonl[415] _id=6ab5681e485cab4c9554232a ts=2026-09-24T18:12:46.7520000Z -> 6aa4144c41b41dbac0c7f266.jsonl[416] _id=6abaacab485cab4c956f70f9 ts=2026-09-28T18:06:27.5380000Z; 23h 25m: 6aa4144c41b41dbac0c7f266.jsonl[1506] _id=6abab652485cab4c95706944 ts=2026-09-28T18:47:46.0450000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1549] _id=6abbffbd485cab4c95842505 ts=2026-09-29T18:13:16.1730000Z; 23h 22m: 6aa4144c41b41dbac0c7f266.jsonl[4506] _id=6abc07f5485cab4c9584c8d9 ts=2026-09-29T18:48:21.5700000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4519] _id=6abd50c7485cab4c9590ef3b ts=2026-09-30T18:11:12.6250000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 27m 
  - Evidence: 23h 27m: 6aa4144c41b41dbac0c7f266.jsonl[1500] _id=6abab642485cab4c957064a2 ts=2026-09-28T18:47:26.8180000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1695] _id=6abc0091485cab4c9584394b ts=2026-09-29T18:15:05.8950000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1082 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f266.jsonl[1340] _id=6abab5d2485cab4c9570598b ts=2026-09-28T18:45:38.2130000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1337] _id=6abab5d3485cab4c95705992 ts=2026-09-28T18:45:38.2130000Z; 0ms: 6aa4144c41b41dbac0c7f266.jsonl[1351] _id=6abab5d8485cab4c95705a01 ts=2026-09-28T18:45:43.8120000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1508] _id=6abab654485cab4c95706a00 ts=2026-09-28T18:45:43.8120000Z; 0ms: 6aa4144c41b41dbac0c7f266.jsonl[1352] _id=6abab5d8485cab4c95705a03 ts=2026-09-28T18:45:43.8220000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1371] _id=6abab5d8485cab4c95705a05 ts=2026-09-28T18:45:43.8220000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 23h 34m 
  - Evidence: 23h 34m: 6aa4144c41b41dbac0c7f266.jsonl[4369] _id=6abc06bf485cab4c9584b4e7 ts=2026-09-29T18:43:11.0650000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4640] _id=6abd524b485cab4c95911c29 ts=2026-09-30T18:17:47.6770000Z; 23h 28m: 6aa4144c41b41dbac0c7f266.jsonl[1437] _id=6abab623485cab4c95705f71 ts=2026-09-28T18:46:59.8320000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1620] _id=6abc003e485cab4c95843260 ts=2026-09-29T18:15:26.1600000Z; 18m 59s: 6aa4144c41b41dbac0c7f266.jsonl[2850] _id=6abc01ba485cab4c95845c37 ts=2026-09-29T18:21:46.6030000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4320] _id=6abc062e485cab4c9584a884 ts=2026-09-29T18:40:45.9440000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.015s..0.025s shown 
  - Evidence: 15ms: 6aa4144c41b41dbac0c7f266.jsonl[4331] _id=6abc0637485cab4c9584a971 ts=2026-09-29T18:40:55.3930000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4329] _id=6abc0637485cab4c9584a985 ts=2026-09-29T18:40:55.4080000Z; 25ms: 6aa4144c41b41dbac0c7f266.jsonl[4328] _id=6abc0637485cab4c9584a96b ts=2026-09-29T18:40:55.3680000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4331] _id=6abc0637485cab4c9584a971 ts=2026-09-29T18:40:55.3930000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.039s..0.043s shown 
  - Evidence: 39ms: 6aa4144c41b41dbac0c7f266.jsonl[844] _id=6abab178485cab4c956ffe33 ts=2026-09-28T18:27:04.8780000Z -> 6aa4144c41b41dbac0c7f266.jsonl[851] _id=6abab178485cab4c956ffe37 ts=2026-09-28T18:27:04.9170000Z; 42ms: 6aa4144c41b41dbac0c7f266.jsonl[880] _id=6abab1b1485cab4c957002db ts=2026-09-28T18:28:01.7830000Z -> 6aa4144c41b41dbac0c7f266.jsonl[886] _id=6abab1b1485cab4c957002dd ts=2026-09-28T18:28:01.8250000Z; 43ms: 6aa4144c41b41dbac0c7f266.jsonl[1107] _id=6abab2bd485cab4c957016a1 ts=2026-09-28T18:32:29.5890000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1114] _id=6abab2bd485cab4c957016a5 ts=2026-09-28T18:32:29.6320000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6aa4144c41b41dbac0c7f266.jsonl[2] _id=6ab56112485cab4c95537dcd ts=2026-09-24T17:42:42.1740000Z -> 6aa4144c41b41dbac0c7f266.jsonl[418] _id=6abaac98485cab4c956f6f65 ts=2026-09-28T18:06:16.4840000Z; 23h 57m: 6aa4144c41b41dbac0c7f266.jsonl[1551] _id=6abbffb5485cab4c958424ed ts=2026-09-29T18:13:08.9710000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4513] _id=6abd50b9485cab4c9590edf3 ts=2026-09-30T18:11:05.5230000Z; 23h 30m: 6aa4144c41b41dbac0c7f266.jsonl[1263] _id=6abab503485cab4c95704ad7 ts=2026-09-28T18:42:11.4040000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1551] _id=6abbffb5485cab4c958424ed ts=2026-09-29T18:13:08.9710000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 6aa4144c41b41dbac0c7f266.jsonl[256] _id=6ab5645d485cab4c9553c211 ts=2026-09-24T17:56:45.2450000Z -> 6aa4144c41b41dbac0c7f266.jsonl[417] _id=6abaac98485cab4c956f6f63 ts=2026-09-28T18:06:16.4820000Z; 23h 57m: 6aa4144c41b41dbac0c7f266.jsonl[1553] _id=6abbffb5485cab4c958424e9 ts=2026-09-29T18:13:08.9690000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4512] _id=6abd50b9485cab4c9590edf1 ts=2026-09-30T18:11:05.5230000Z; 23h 30m: 6aa4144c41b41dbac0c7f266.jsonl[1262] _id=6abab503485cab4c95704ad5 ts=2026-09-28T18:42:11.4020000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1553] _id=6abbffb5485cab4c958424e9 ts=2026-09-29T18:13:08.9690000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 6aa4144c41b41dbac0c7f266.jsonl[204] _id=6ab563cc485cab4c9553b848 ts=2026-09-24T17:54:20.6620000Z -> 6aa4144c41b41dbac0c7f266.jsonl[424] _id=6abaacab485cab4c956f7117 ts=2026-09-28T18:06:34.1340000Z; 23h 30m: 6aa4144c41b41dbac0c7f266.jsonl[4321] _id=6abc0620485cab4c9584a75d ts=2026-09-29T18:40:32.5430000Z -> 6aa4144c41b41dbac0c7f266.jsonl[4515] _id=6abd50c7485cab4c9590ef45 ts=2026-09-30T18:11:18.6990000Z; 23h 29m: 6aa4144c41b41dbac0c7f266.jsonl[1290] _id=6abab565485cab4c95705113 ts=2026-09-28T18:43:49.8970000Z -> 6aa4144c41b41dbac0c7f266.jsonl[1554] _id=6abbffbd485cab4c9584250b ts=2026-09-29T18:13:17.0800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f266.jsonl[761] _id=6abab09a485cab4c956fef1d ts=2026-09-28T18:23:22.1740000Z -> 6aa4144c41b41dbac0c7f266.jsonl[763] _id=6abab09a485cab4c956fef21 ts=2026-09-28T18:23:22.1750000Z; 5ms: 6aa4144c41b41dbac0c7f266.jsonl[202] _id=6ab563cc485cab4c9553b846 ts=2026-09-24T17:54:20.6570000Z -> 6aa4144c41b41dbac0c7f266.jsonl[204] _id=6ab563cc485cab4c9553b848 ts=2026-09-24T17:54:20.6620000Z; 8ms: 6aa4144c41b41dbac0c7f266.jsonl[157] _id=6ab562cf485cab4c9553a210 ts=2026-09-24T17:50:07.1740000Z -> 6aa4144c41b41dbac0c7f266.jsonl[156] _id=6ab562cf485cab4c9553a214 ts=2026-09-24T17:50:07.1820000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 1 record(s) match the trigger in 6aa4144c41b41dbac0c7f266.jsonl:6aa4144c41b41dbac0c7f266, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[4168] _id=6abc040e485cab4c95848549 ts=2026-09-29T18:31:42.5380000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[747] _id=6abab089485cab4c956fec7d ts=2026-09-28T18:23:04.9780000Z`; `6aa4144c41b41dbac0c7f266.jsonl[948] _id=6abab202485cab4c95700813 ts=2026-09-28T18:29:22.7130000Z`; `6aa4144c41b41dbac0c7f266.jsonl[979] _id=6abab223485cab4c95700a91 ts=2026-09-28T18:29:55.2740000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 64 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1749] _id=6abc00a6485cab4c95843c89 ts=2026-09-29T18:17:09.8220000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1800] _id=6abc00b8485cab4c95843f72 ts=2026-09-29T18:17:27.2100000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1853] _id=6abc00bd485cab4c958440cd ts=2026-09-29T18:17:30.8360000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 141 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1359] _id=6abab5d5485cab4c957059cd ts=2026-09-28T18:45:39.5470000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1345] _id=6abab5d5485cab4c957059cf ts=2026-09-28T18:45:39.5470000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1346] _id=6abab5d5485cab4c957059d3 ts=2026-09-28T18:45:40.1030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[5] _id=6ab56130485cab4c95537fa3 ts=?`; `6aa4144c41b41dbac0c7f266.jsonl[4517] _id=6abd50c6485cab4c9590ef39 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 283 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1764] _id=6abc00a9485cab4c95843d4a ts=2026-09-29T18:17:12.3820000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1790] _id=6abc00ae485cab4c95843e13 ts=2026-09-29T18:17:17.5500000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1791] _id=6abc00ae485cab4c95843e15 ts=2026-09-29T18:17:17.7340000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 565 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1337] _id=6abab5d3485cab4c95705992 ts=2026-09-28T18:45:38.2130000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1341] _id=6abab5d3485cab4c95705995 ts=2026-09-28T18:45:38.5940000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1353] _id=6abab5d3485cab4c95705999 ts=2026-09-28T18:45:38.7030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[4331] _id=6abc0637485cab4c9584a971 ts=2026-09-29T18:40:55.3930000Z`; `6aa4144c41b41dbac0c7f266.jsonl[4329] _id=6abc0637485cab4c9584a985 ts=2026-09-29T18:40:55.4080000Z`; `6aa4144c41b41dbac0c7f266.jsonl[4368] _id=6abc06bb485cab4c9584b4af ts=2026-09-29T18:43:07.0620000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[819] _id=6abab149485cab4c956ffad7 ts=2026-09-28T18:26:17.8520000Z`; `6aa4144c41b41dbac0c7f266.jsonl[827] _id=6abab159485cab4c956ffbcf ts=2026-09-28T18:26:33.3420000Z`; `6aa4144c41b41dbac0c7f266.jsonl[830] _id=6abab15d485cab4c956ffbfd ts=2026-09-28T18:26:37.0520000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'DialogueStartEvent' (totals: 132 start, 127 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 70 unmatched 'BecameCameraCentered' (totals: 341 open, 335 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 49 unmatched 'BecameVisible' (totals: 732 open, 824 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 12 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 9 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 6 unmatched 'questActiveEvent' (totals: 17 start, 11 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 183 of 5090 adjacent _id pairs reverse in client time; worst 123.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f266.jsonl[1513] _id=6abab652485cab4c95706996 ts=2026-09-28T18:47:46.8820000Z`; `6aa4144c41b41dbac0c7f266.jsonl[1507] _id=6abab653485cab4c957069da ts=2026-09-28T18:45:43.6810000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.14s, min -84442.74s, max +3.45s over 5091 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f266\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | skipped |
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

### `PuzzlePieceVisibleEvent` — 2232 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2232)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.14s, n=2231)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2232/2232 records)
    "BecameInvisible"  x824
    "BecameVisible"  x732
    "BecameCameraCentered"  x341
    "BecameCameraUncentered"  x335
data.pieceId  (string, 2232/2232 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2232/2232 records)
    1378 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 931 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (705); Unit 1 Dev (226)
- **Intervals:** median 1.27s (p5 0.11s / p95 21.86s, n=930)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 931/931 records)
    "pressed"  x931
data.actionType  (string, 931/931 records)
    "Move"  x507
    "Sprint"  x230
    "Interact"  x129
    "Jump"  x40
    "Hoverboard"  x14
    "Map"  x6
    "Pause"  x4
    "SkipCinematic"  x1
data.key  (string, 931/931 records, 2 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 931/931 records)
    "Player"  x931
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 772 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (391); Unit 1 Dev (381)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.04s, n=770)
- **Fields under `data`:**

```text
data.position  (object, 772/772 records)
data.position.x  (number, 772/772 records)
    numeric range -19.1453 .. 1099.42 (229 unique)
data.position.y  (number, 772/772 records)
    numeric range -4.78012 .. 158.271 (159 unique)
data.position.z  (number, 772/772 records)
    numeric range -100.004 .. 2211.1 (227 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 743 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (403); Unit 2 Prod (Refactor) (340)
- **eventKey:** present on 484 of 743 records
- **Intervals:** median 4.80s (p5 0.01s / p95 38.08s, n=742)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x484; [conversationId, dialogueEventType] x259
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 743/743 records)
    numeric range 16 .. 101 (17 unique)
data.dialogueEventType  (string, 743/743 records)
    "DialogueNodeEvent"  x484
    "DialogueStartEvent"  x132
    "DialogueFinishEvent"  x127
data.nodeId  (number, 484/743 records)
    numeric range 0 .. 283 (117 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 133 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (133)
- **Intervals:** median 0.27s (p5 0.04s / p95 24.60s, n=132)
- **Fields under `data`:**

```text
data.actionType  (string, 133/133 records)
    "argumentationNodeHoverEnd"  x54
    "argumentationNodeHoverStart"  x54
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 133/133 records)
    "Unit 1 - Freshwater"  x123
    "Unit 1 - Argumentation Tutorial"  x10
data.nodeName  (string, 133/133 records)
    "1"  x49
    "A"  x33
    "II"  x26
    "I"  x25
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 104 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (89); Unit 1 Dev (15)
- **Intervals:** median 5.68s (p5 0.19s / p95 301.52s, n=103)
- **Fields under `data`:**

```text
data.actionType  (string, 104/104 records)
    "Press E to Place"  x56
    "Press E to Pick up"  x29
    "TalkTo"  x6
    "Press E to Open Locker"  x4
    "E to Talk"  x3
    "Press E to Install"  x2
    "Inspect Alien Glyph"  x1
    "Press E to Collect"  x1
    "Press E to Operate"  x1
    "Press [E/Action button] to enter escape pod "  x1
data.objectName  (string, 104/104 records)
    24 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationAnswerEvent` — 52 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (52)
- **Intervals:** median 2.90s (p5 0.22s / p95 50.16s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "submitAnswerEvent"  x52
data.answerSubmitted  (string, 52/52 records, 8 empty-string)
    "A,I"  x20
    "1,II"  x10
    ""  x8
    "1,I"  x8
    "A,1,I"  x3
    "A,II"  x2
    "A,1,"  x1
data.argumentationTitle  (string, 52/52 records)
    "Unit 1 - Freshwater"  x51
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 41 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (41)
- **Intervals:** median 4.69s (p5 0.50s / p95 5307.69s, n=40)
- **`data` key-set variants:** [actionType, featureUsed] x22; [actionType, featureUsed, legendName] x15; [actionType, featureUsed, location] x4
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "MapOpenEvent"  x12
    "MapCloseEvent"  x10
    "Selected"  x10
    "Unselected"  x5
    "WaypointSetEvent"  x3
    "WaypointMoveEvent"  x1
data.featureUsed  (string, 41/41 records)
    "Map"  x22
    "Legend"  x15
    "Waypoint"  x4
data.legendName  (string, 15/41 records)
    "360 ft"  x5
    "330 ft"  x4
    "0 ft"  x2
    "Water"  x2
    "180 ft"  x1
    "240 ft"  x1
data.location  (object, 4/41 records)
data.location.x  (number, 4/41 records)
    4 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 4/41 records)
    4 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 4/41 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 28 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (11)
- **eventKey:** present on 28 of 28 records
- **Intervals:** median 253.47s (p5 0.01s / p95 84622.46s, n=27)
- **`data` key-set variants:** [questEventType, questID, questName] x17; [questEventType, questID, questName, questSuccessOrFailure] x11
- **Fields under `data`:**

```text
data.questEventType  (string, 28/28 records)
    "questActiveEvent"  x17
    "questFinishEvent"  x11
data.questID  (string, 28/28 records)
    "22"  x4
    "23"  x4
    "29"  x4
    "31"  x4
    "21"  x3
    "32"  x3
    "28"  x2
    "33"  x2
    "34"  x2
data.questName  (string, 28/28 records)
    "Foraged Forging"  x4
    "Gear Up"  x4
    "Getting the Band Back Together"  x4
    "TK, Reporting In!"  x4
    "Escape the Ruin"  x3
    "Info and Intros"  x3
    "Defend the Expedition"  x2
    "Getting Your Space Legs"  x2
    "What Was That?"  x2
data.questSuccessOrFailure  (string, 11/28 records)
    "Succeeded"  x11
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 17 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (17)
- **Intervals:** median 2.04s (p5 0.13s / p95 113.33s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x8
data.argumentationTitle  (string, 17/17 records)
    "Unit 1 - Freshwater"  x15
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 17/17 records)
    "BackingInfoPanel - "  x15
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowFocusEvent` — 9 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (7); Unit 1 Dev (2)
- **Intervals:** median 33969.31s (p5 388.61s / p95 255208.10s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 9/9 records)
    true  x9
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 7 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 1 Dev (2)
- **Intervals:** median 75210.51s (p5 1589.42s / p95 281820.41s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "DebugMenuStateChanged"  x7
data.isOpened  (bool, 7/7 records)
    false  x7
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 7 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (7)
- **Intervals:** median 75220.64s (p5 1583.39s / p95 281829.87s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    true  x7
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (6)
- **Intervals:** median 2.17s (p5 2.09s / p95 3.05s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 42.55s (p5 40.52s / p95 421.18s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationSessionClose"  x2
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 4/4 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 2 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.99s (p5 2.99s / p95 2.99s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/2 records)
    "Finished"  x1
    "Started"  x1
data.Unit  (string, 2/2 records)
    "Unit 2 Prod (Refactor)"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Permissions check failed"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit1"  x1
    "unit2"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

### `gameWindowUnfocusEvent` — 2 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 533.00s (p5 533.00s / p95 533.00s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 2/2 records)
    false  x2
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

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
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : baseline field(s) absent this build
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "Selected" (10x); "Unselected" (5x); "WaypointMoveEvent" (1x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (15x); "Waypoint" (4x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 3 Dev' has no records of this event
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*