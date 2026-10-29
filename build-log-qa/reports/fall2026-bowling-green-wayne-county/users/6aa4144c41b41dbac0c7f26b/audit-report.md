# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26b
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f26b.jsonl
- **Records:** 13684 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f26b
- **Time span:** 2026-09-23T18:08:28.981000+00:00 .. 2026-10-07T18:50:25.636000+00:00 (336h 41m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 13684 records, 7 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 95 INFO, 0 NOT_TESTED, 76 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6581 | 48.09 | 1 | 5 | 0 | 2026-09-23T18:15:52.694000+00:00 | 2026-10-07T18:50:19.006000+00:00 | 336h 34m |
| PuzzlePieceVisibleEvent | 3668 | 26.81 | 1 | 3 | 0 | 2026-09-24T17:57:17.874000+00:00 | 2026-10-07T18:48:49.453000+00:00 | 312h 51m |
| PlayerPositionEvent | 1650 | 12.06 | 1 | 5 | 0 | 2026-09-23T18:15:47.485000+00:00 | 2026-10-07T18:50:25.636000+00:00 | 336h 34m |
| DialogueEvent | 1082 | 7.91 | 1 | 5 | 680 | 2026-09-23T18:16:09.482000+00:00 | 2026-10-07T18:50:20.563000+00:00 | 336h 34m |
| argumentationNodeEvent | 209 | 1.53 | 1 | 1 | 0 | 2026-09-23T18:41:21.393000+00:00 | 2026-09-24T17:47:27.653000+00:00 | 23h 6m |
| Soil Key Puzzle | 118 | 0.86 | 1 | 2 | 0 | 2026-09-24T18:07:08.922000+00:00 | 2026-10-06T18:47:40.767000+00:00 | 288h 40m |
| ObjectInterEvent | 106 | 0.77 | 1 | 5 | 0 | 2026-09-23T18:22:34.486000+00:00 | 2026-10-07T18:49:21.975000+00:00 | 336h 26m |
| TopographicMapEvent | 56 | 0.41 | 1 | 3 | 0 | 2026-09-24T17:58:14.516000+00:00 | 2026-10-07T18:42:05.258000+00:00 | 312h 43m |
| questEvent | 56 | 0.41 | 1 | 5 | 56 | 2026-09-23T18:16:09.457000+00:00 | 2026-10-07T18:49:36.250000+00:00 | 336h 33m |
| gameWindowFocusEvent | 47 | 0.34 | 1 | 4 | 0 | 2026-09-23T18:08:28.981000+00:00 | 2026-10-07T18:42:52.576000+00:00 | 336h 34m |
| gameWindowUnfocusEvent | 33 | 0.24 | 1 | 5 | 0 | 2026-09-23T18:08:50.945000+00:00 | 2026-10-07T16:12:01.807000+00:00 | 334h 3m |
| DEBUGMenu | 23 | 0.17 | 1 | 6 | 0 | 2026-09-23T18:15:47.476000+00:00 | 2026-10-07T18:43:24.687000+00:00 | 336h 27m |
| gameStartEvent | 21 | 0.15 | 1 | 1 | 0 | 2026-09-23T18:08:28.982000+00:00 | 2026-10-07T18:42:52.576000+00:00 | 336h 34m |
| argumentationAnswerEvent | 12 | 0.09 | 1 | 1 | 0 | 2026-09-23T18:43:08.558000+00:00 | 2026-09-24T17:47:30.577000+00:00 | 23h 4m |
| argumentationEvent | 8 | 0.06 | 1 | 1 | 0 | 2026-09-23T18:42:35.380000+00:00 | 2026-09-24T17:47:30.611000+00:00 | 23h 4m |
| DaniEvent | 6 | 0.04 | 1 | 2 | 0 | 2026-09-25T18:43:31.102000+00:00 | 2026-10-07T18:41:56.438000+00:00 | 287h 58m |
| WaterChamberEvent | 3 | 0.02 | 1 | 1 | 0 | 2026-10-07T18:47:58.523000+00:00 | 2026-10-07T18:50:20.565000+00:00 | 2m 22s |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-24T17:50:27.614000+00:00 | 2026-09-24T17:50:27.614000+00:00 | 0.0s |
| chatEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-10-07T18:43:24.573000+00:00 | 2026-10-07T18:43:24.573000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.6s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 71.021s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 2.842s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 5360.953s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 242.671s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 29.826s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev 
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
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.1x vs baseline. 
  - Observed: 118 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 300 ft; 330 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 3 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `WaterChamberEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Off 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — baseline categorical value(s) not seen this build. 
  - Observed: Two 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Condenser; DualChamber_Evaporator; VentSwitch 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.room` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,1, 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 36; 40; 41; 44; 45; 46; 47; 48; 49; 50; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 11 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[163] _id=6ab4197c485cab4c954f47bc ts=2026-09-23T18:25:00.3780000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[216] _id=6ab41a76485cab4c954f4fc6 ts=2026-09-23T18:29:10.1130000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[255] _id=6ab41b3b485cab4c954f5512 ts=2026-09-23T18:32:27.3300000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:23' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[4296] _id=6abaacbd485cab4c956f725f ts=2026-09-28T18:06:53.8490000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[4808] _id=6abab025485cab4c956fdf4f ts=2026-09-28T18:21:24.2780000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[5108] _id=6abab1e5485cab4c957005f5 ts=2026-09-28T18:28:52.5180000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[23] _id=6ab4159d485cab4c954f366a ts=2026-09-23T18:08:28.9820000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[22] _id=6ab41743485cab4c954f367c ts=2026-09-23T18:15:31.2360000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[579] _id=6ab560f9485cab4c95537c3b ts=2026-09-24T17:42:17.4610000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 47 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 47} 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[26] _id=6ab4159d485cab4c954f3668 ts=2026-09-23T18:08:28.9810000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[25] _id=6ab41743485cab4c954f367a ts=2026-09-23T18:15:31.2340000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[578] _id=6ab560f9485cab4c95537c37 ts=2026-09-24T17:42:17.4590000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 33 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 33} 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[21] _id=6ab415b3485cab4c954f366c ts=2026-09-23T18:08:50.9450000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[24] _id=6ab41743485cab4c954f3676 ts=2026-09-23T18:08:50.945Z`; `6aa4144c41b41dbac0c7f26b.jsonl[4280] _id=6abaac7b485cab4c956f6e23 ts=2026-09-28T18:05:47.9240000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 4 of 56 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[1175] _id=6ab564b6485cab4c9553cabc ts=2026-09-24T17:58:14.5160000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1186] _id=6ab564c3485cab4c9553cc20 ts=2026-09-24T17:58:27.3090000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[2944] _id=6ab6bbab485cab4c955e156f ts=2026-09-25T18:21:31.6780000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6580 | 0.0 | 0.36 | 184.144 | 4.421 | 431260.121 | 0.33 | 668 | 9 |
| PuzzlePieceVisibleEvent | 3667 | 0.0 | 0.031 | 307.143 | 1.133 | 605851.032 | 0.2 | 2279 | 6 |
| PlayerPositionEvent | 1645 | 0.0 | 10.0 | 736.347 | 10.381 | 430923.932 | 0.08 | 1 | 9 |
| DialogueEvent | 1081 | 0.001 | 4.917 | 1120.861 | 54.504 | 432139.54 | 0.05 | 281 | 9 |
| argumentationNodeEvent | 208 | 0.009 | 0.418 | 399.838 | 9.581 | 82689.881 | 0.15 | 22 | 1 |
| Soil Key Puzzle | 117 | 0.116 | 0.57 | 8882.323 | 11.79 | 691022.76 | 0.01 | 0 | 2 |
| ObjectInterEvent | 105 | 0.005 | 6.771 | 11535.309 | 84742.916 | 518503.92 | 0.01 | 1 | 8 |
| TopographicMapEvent | 55 | 0.838 | 8.6 | 20469.65 | 87179.441 | 432508.358 | 0.0 | 0 | 7 |
| questEvent | 55 | 0.001 | 280.4 | 22029.214 | 85571.454 | 431210.197 | 0.0 | 10 | 18 |
| gameWindowFocusEvent | 46 | 1.673 | 242.671 | 26340.513 | 87398.394 | 352887.006 | 0.0 | 0 | 15 |
| gameWindowUnfocusEvent | 32 | 0.0 | 29.826 | 37580.964 | 241920.468 | 434254.073 | 0.0 | 2 | 8 |
| DEBUGMenu | 22 | 11.077 | 879.334 | 55057.146 | 250213.805 | 431985.515 | 0.0 | 0 | 12 |
| gameStartEvent | 20 | 217.058 | 5360.953 | 60583.18 | 263417.236 | 352887.006 | 0.0 | 0 | 13 |
| argumentationAnswerEvent | 11 | 0.234 | 2.842 | 7551.093 | 41461.382 | 82836.848 | 0.01 | 0 | 1 |
| argumentationEvent | 7 | 19.667 | 47.722 | 11870.747 | 57999.005 | 82822.29 | 0.01 | 0 | 1 |
| DaniEvent | 5 | 0.662 | 6.582 | 207341.067 | 823297.688 | 1026597.603 | 0.0 | 0 | 2 |
| WaterChamberEvent | 2 | 52.773 | 71.021 | 71.021 | 87.444 | 89.269 | 0.84 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 17 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[11922] _id=6ac667b3de269131f9bc0b4a ts=2026-10-07T15:39:32.0640000Z == 6aa4144c41b41dbac0c7f26b.jsonl[11923] _id=6ac667b3de269131f9bc0b4b ts=2026-10-07T15:39:32.0640000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[11928] _id=6ac667b9de269131f9bc0b8f ts=2026-10-07T15:39:38.0140000Z == 6aa4144c41b41dbac0c7f26b.jsonl[11931] _id=6ac667b9de269131f9bc0b90 ts=2026-10-07T15:39:38.0140000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[13219] _id=6ac691b4de269131f9bdd977 ts=2026-10-07T18:38:44.2610000Z == 6aa4144c41b41dbac0c7f26b.jsonl[13220] _id=6ac691b4de269131f9bdd978 ts=2026-10-07T18:38:44.2610000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 224 group(s), 340 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[1005] _id=6ab5647e485cab4c9553c54e ts=2026-09-24T17:57:17.8740000Z == 6aa4144c41b41dbac0c7f26b.jsonl[1006] _id=6ab5647e485cab4c9553c556 ts=2026-09-24T17:57:17.8740000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[998] _id=6ab56484485cab4c9553c5ec ts=2026-09-24T17:57:19.3410000Z == 6aa4144c41b41dbac0c7f26b.jsonl[1036] _id=6ab56484485cab4c9553c5f0 ts=2026-09-24T17:57:19.3410000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1046] _id=6ab56486485cab4c9553c622 ts=2026-09-24T17:57:20.5090000Z == 6aa4144c41b41dbac0c7f26b.jsonl[1047] _id=6ab56486485cab4c9553c628 ts=2026-09-24T17:57:20.5090000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[2535] _id=6ab6b9f0485cab4c955dd02b ts=? == 6aa4144c41b41dbac0c7f26b.jsonl[4288] _id=6abaacbd485cab4c956f724d ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 28 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4144c41b41dbac0c7f26b.jsonl[102] _id=6ab418ea485cab4c954f41c0 ts=2026-09-23T18:22:34.4860000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[120] _id=6ab418ea485cab4c954f41c7 ts=2026-09-23T18:22:34.4910000Z`; `595ms: 6aa4144c41b41dbac0c7f26b.jsonl[586] _id=6ab5611a485cab4c95537e3b ts=2026-09-24T17:42:50.3870000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[589] _id=6ab5611a485cab4c95537e4d ts=2026-09-24T17:42:50.9820000Z`; `236ms: 6aa4144c41b41dbac0c7f26b.jsonl[589] _id=6ab5611a485cab4c95537e4d ts=2026-09-24T17:42:50.9820000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[596] _id=6ab5611b485cab4c95537e53 ts=2026-09-24T17:42:51.2180000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 721 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 6aa4144c41b41dbac0c7f26b.jsonl[1027] _id=6ab5647f485cab4c9553c57c ts=2026-09-24T17:57:18.5530000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[1020] _id=6ab56480485cab4c9553c58f ts=2026-09-24T17:57:18.5640000Z`; `54ms: 6aa4144c41b41dbac0c7f26b.jsonl[1019] _id=6ab56483485cab4c9553c5d0 ts=2026-09-24T17:57:18.9180000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[1034] _id=6ab56483485cab4c9553c5d6 ts=2026-09-24T17:57:18.9720000Z`; `63ms: 6aa4144c41b41dbac0c7f26b.jsonl[1034] _id=6ab56483485cab4c9553c5d6 ts=2026-09-24T17:57:18.9720000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[1021] _id=6ab56483485cab4c9553c5da ts=2026-09-24T17:57:19.0350000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `976ms: 6aa4144c41b41dbac0c7f26b.jsonl[11251] _id=6ac541e2de269131f9b6d755 ts=2026-10-06T18:45:54.6100000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[11262] _id=6ac541e3de269131f9b6d789 ts=2026-10-06T18:45:55.5860000Z`; `988ms: 6aa4144c41b41dbac0c7f26b.jsonl[11334] _id=6ac54207de269131f9b6dd63 ts=2026-10-06T18:46:31.1060000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[11335] _id=6ac54208de269131f9b6dd83 ts=2026-10-06T18:46:32.0940000Z`; `691ms: 6aa4144c41b41dbac0c7f26b.jsonl[11337] _id=6ac54208de269131f9b6dd9f ts=2026-10-06T18:46:32.8000000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[11338] _id=6ac54209de269131f9b6ddcb ts=2026-10-06T18:46:33.4910000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `325ms: 6aa4144c41b41dbac0c7f26b.jsonl[482] _id=6ab41e0b485cab4c954f6d11 ts=2026-09-23T18:44:27.0470000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[477] _id=6ab41e0b485cab4c954f6d13 ts=2026-09-23T18:44:27.3720000Z`; `522ms: 6aa4144c41b41dbac0c7f26b.jsonl[477] _id=6ab41e0b485cab4c954f6d13 ts=2026-09-23T18:44:27.3720000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[473] _id=6ab41e0b485cab4c954f6d19 ts=2026-09-23T18:44:27.8940000Z`; `234ms: 6aa4144c41b41dbac0c7f26b.jsonl[473] _id=6ab41e0b485cab4c954f6d19 ts=2026-09-23T18:44:27.8940000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[485] _id=6ab41e0c485cab4c954f6d1b ts=2026-09-23T18:44:28.1280000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 31 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `323ms: 6aa4144c41b41dbac0c7f26b.jsonl[380] _id=6ab41d53485cab4c954f65d9 ts=2026-09-23T18:41:23.6220000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[393] _id=6ab41d53485cab4c954f65dd ts=2026-09-23T18:41:23.9450000Z`; `45ms: 6aa4144c41b41dbac0c7f26b.jsonl[422] _id=6ab41db6485cab4c954f6993 ts=2026-09-23T18:43:02.6840000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[409] _id=6ab41db6485cab4c954f6995 ts=2026-09-23T18:43:02.7290000Z`; `42ms: 6aa4144c41b41dbac0c7f26b.jsonl[429] _id=6ab41db8485cab4c954f69b3 ts=2026-09-23T18:43:04.3910000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[430] _id=6ab41db8485cab4c954f69b5 ts=2026-09-23T18:43:04.4330000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4144c41b41dbac0c7f26b.jsonl[21] _id=6ab415b3485cab4c954f366c ts=2026-09-23T18:08:50.9450000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[24] _id=6ab41743485cab4c954f3676 ts=2026-09-23T18:08:50.945Z`; `0ms: 6aa4144c41b41dbac0c7f26b.jsonl[4790] _id=6abaafff485cab4c956fda47 ts=2026-09-28T18:20:47.1340000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[4794] _id=6abab017485cab4c956fdd93 ts=2026-09-28T18:20:47.134Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6aa4144c41b41dbac0c7f26b.jsonl[4296] _id=6abaacbd485cab4c956f725f ts=2026-09-28T18:06:53.8490000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[4297] _id=6abaacbd485cab4c956f7263 ts=2026-09-28T18:06:53.8850000Z`; `8ms: 6aa4144c41b41dbac0c7f26b.jsonl[4808] _id=6abab025485cab4c956fdf4f ts=2026-09-28T18:21:24.2780000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[4800] _id=6abab025485cab4c956fdf57 ts=2026-09-28T18:21:24.2860000Z`; `7ms: 6aa4144c41b41dbac0c7f26b.jsonl[5108] _id=6abab1e5485cab4c957005f5 ts=2026-09-28T18:28:52.5180000Z ~ 6aa4144c41b41dbac0c7f26b.jsonl[5106] _id=6abab1e5485cab4c957005f7 ts=2026-09-28T18:28:52.5250000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6aa4144c41b41dbac0c7f26b.jsonl[7942] _id=6abd52bb485cab4c95912b65 ts=2026-09-30T18:19:39.6920000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[8562] _id=6ac3ea2dde269131f9aee025 ts=2026-10-05T18:19:25.2070000Z; 71h 52m: 6aa4144c41b41dbac0c7f26b.jsonl[2526] _id=6ab6b9e9485cab4c955dcf1e ts=2026-09-25T18:14:01.4540000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4292] _id=6abaacb7485cab4c956f71e7 ts=2026-09-28T18:06:47.9780000Z; 24h 21m: 6aa4144c41b41dbac0c7f26b.jsonl[896] _id=6ab56349485cab4c9553ad62 ts=2026-09-24T17:52:09.3040000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2526] _id=6ab6b9e9485cab4c955dcf1e ts=2026-09-25T18:14:01.4540000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 285h 9m 
  - Evidence: 285h 9m: 6aa4144c41b41dbac0c7f26b.jsonl[4240] _id=6ab6c0d3485cab4c955e6847 ts=2026-09-25T18:43:31.7640000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[12634] _id=6ac66af9de269131f9bc3916 ts=2026-10-07T15:53:29.3670000Z; 2h 48m: 6aa4144c41b41dbac0c7f26b.jsonl[12635] _id=6ac66affde269131f9bc393a ts=2026-10-07T15:53:35.9490000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[13338] _id=6ac69272de269131f9bde767 ts=2026-10-07T18:41:53.9770000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 2m 
  - Evidence: 120h 2m: 6aa4144c41b41dbac0c7f26b.jsonl[8548] _id=6abd56d9485cab4c9591d3a9 ts=2026-09-30T18:37:13.2620000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[9634] _id=6ac3eee4de269131f9af3d6b ts=2026-10-05T18:39:32.8020000Z; 71h 34m: 6aa4144c41b41dbac0c7f26b.jsonl[3770] _id=6ab6be86485cab4c955e4b8d ts=2026-09-25T18:33:42.7930000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4364] _id=6abaad28485cab4c956f7a12 ts=2026-09-28T18:08:41.0000000Z; 24h 5m: 6aa4144c41b41dbac0c7f26b.jsonl[2507] _id=6ab5683f485cab4c9554245e ts=2026-09-24T18:13:19.3610000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2619] _id=6ab6baf9485cab4c955df565 ts=2026-09-25T18:18:33.5840000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 281 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26b.jsonl[5707] _id=6abc0448485cab4c9584892b ts=2026-09-29T18:32:40.5290000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[5708] _id=6abc0448485cab4c9584892d ts=2026-09-29T18:32:40.5300000Z; 1ms: 6aa4144c41b41dbac0c7f26b.jsonl[856] _id=6ab562bc485cab4c9553a04c ts=2026-09-24T17:49:48.2930000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[860] _id=6ab562bc485cab4c9553a050 ts=2026-09-24T17:49:48.2940000Z; 2ms: 6aa4144c41b41dbac0c7f26b.jsonl[1965] _id=6ab5665b485cab4c95540508 ts=2026-09-24T18:05:14.8270000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2102] _id=6ab5665b485cab4c9554050a ts=2026-09-24T18:05:14.8290000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6aa4144c41b41dbac0c7f26b.jsonl[8485] _id=6abd55a5485cab4c9591a439 ts=2026-09-30T18:32:05.0700000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[8567] _id=6ac3ea42de269131f9aee1d9 ts=2026-10-05T18:19:45.1910000Z; 71h 23m: 6aa4144c41b41dbac0c7f26b.jsonl[4239] _id=6ab6c0d3485cab4c955e6845 ts=2026-09-25T18:43:31.7520000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4289] _id=6abaacbd485cab4c956f7251 ts=2026-09-28T18:06:53.8130000Z; 24h 5m: 6aa4144c41b41dbac0c7f26b.jsonl[2465] _id=6ab56719485cab4c955416c5 ts=2026-09-24T18:08:25.9910000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2543] _id=6ab6b9f0485cab4c955dd037 ts=2026-09-25T18:14:07.8360000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 668 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[11922] _id=6ac667b3de269131f9bc0b4a ts=2026-10-07T15:39:32.0640000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[11923] _id=6ac667b3de269131f9bc0b4b ts=2026-10-07T15:39:32.0640000Z; 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[11928] _id=6ac667b9de269131f9bc0b8f ts=2026-10-07T15:39:38.0140000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[11931] _id=6ac667b9de269131f9bc0b90 ts=2026-10-07T15:39:38.0140000Z; 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[11932] _id=6ac667b9de269131f9bc0b92 ts=2026-10-07T15:39:38.2380000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[11933] _id=6ac667b9de269131f9bc0b93 ts=2026-10-07T15:39:38.2380000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 144h 1m 
  - Evidence: 144h 1m: 6aa4144c41b41dbac0c7f26b.jsonl[7872] _id=6abd552a485cab4c959193a9 ts=2026-09-30T18:30:02.0090000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[10943] _id=6ac53e91de269131f9b67753 ts=2026-10-06T18:31:45.9290000Z; 72h 17m: 6aa4144c41b41dbac0c7f26b.jsonl[3622] _id=6ab6bcd5485cab4c955e32e3 ts=2026-09-25T18:26:29.6500000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[5565] _id=6abab56d485cab4c9570518d ts=2026-09-28T18:43:57.8060000Z; 24h 12m: 6aa4144c41b41dbac0c7f26b.jsonl[2435] _id=6ab566cc485cab4c95540f50 ts=2026-09-24T18:07:08.9290000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2641] _id=6ab6bb1f485cab4c955dfd0b ts=2026-09-25T18:19:12.0430000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6aa4144c41b41dbac0c7f26b.jsonl[102] _id=6ab418ea485cab4c954f41c0 ts=2026-09-23T18:22:34.4860000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[120] _id=6ab418ea485cab4c954f41c7 ts=2026-09-23T18:22:34.4910000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6aa4144c41b41dbac0c7f26b.jsonl[8549] _id=6abd56e1485cab4c9591d527 ts=2026-09-30T18:37:21.2820000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[8563] _id=6ac3ea32de269131f9aee07b ts=2026-10-05T18:19:25.2140000Z; 71h 23m: 6aa4144c41b41dbac0c7f26b.jsonl[4279] _id=6ab6c0d8485cab4c955e685f ts=2026-09-25T18:43:36.7480000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4298] _id=6abaacbd485cab4c956f724f ts=2026-09-28T18:06:47.9850000Z; 23h 59m: 6aa4144c41b41dbac0c7f26b.jsonl[2513] _id=6ab56872485cab4c95542528 ts=2026-09-24T18:14:10.4990000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2542] _id=6ab6b9f0485cab4c955dd02f ts=2026-09-25T18:14:01.4610000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[13360] _id=6ac69295de269131f9bdeb19 ts=2026-10-07T18:42:29.7390000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[13363] _id=6ac692acde269131f9bded82 ts=2026-10-07T18:42:29.739Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 168h 17m 
  - Evidence: 168h 17m: 6aa4144c41b41dbac0c7f26b.jsonl[7626] _id=6abc03bb485cab4c9584819f ts=2026-09-29T18:30:16.5460000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[11376] _id=6ac54254de269131f9b6e7df ts=2026-10-06T18:47:47.5780000Z; 71h 58m: 6aa4144c41b41dbac0c7f26b.jsonl[3629] _id=6ab6bcd6485cab4c955e3323 ts=2026-09-25T18:26:29.7130000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4910] _id=6abab0e8485cab4c956ff48f ts=2026-09-28T18:24:39.3550000Z; 24h 16m: 6aa4144c41b41dbac0c7f26b.jsonl[2251] _id=6ab56631485cab4c955400f6 ts=2026-09-24T18:04:32.1510000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[3121] _id=6ab6bc7f485cab4c955e2678 ts=2026-09-25T18:20:53.0410000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2279 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[1005] _id=6ab5647e485cab4c9553c54e ts=2026-09-24T17:57:17.8740000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[1014] _id=6ab5647e485cab4c9553c552 ts=2026-09-24T17:57:17.8740000Z; 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[1007] _id=6ab5647f485cab4c9553c562 ts=2026-09-24T17:57:17.9820000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[1010] _id=6ab5647f485cab4c9553c568 ts=2026-09-24T17:57:17.9820000Z; 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[1009] _id=6ab5647e485cab4c9553c55c ts=2026-09-24T17:57:17.9820000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[1007] _id=6ab5647f485cab4c9553c562 ts=2026-09-24T17:57:17.9820000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 57m 
  - Evidence: 191h 57m: 6aa4144c41b41dbac0c7f26b.jsonl[5583] _id=6abab5b9485cab4c95705729 ts=2026-09-28T18:45:13.6070000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[11168] _id=6ac54108de269131f9b6bde1 ts=2026-10-06T18:42:16.3670000Z; 96h 36m: 6aa4144c41b41dbac0c7f26b.jsonl[2436] _id=6ab566cf485cab4c95540fa1 ts=2026-09-24T18:07:11.8960000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[5564] _id=6abab56d485cab4c9570518b ts=2026-09-28T18:43:57.8010000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 8m 
  - Evidence: 120h 8m: 6aa4144c41b41dbac0c7f26b.jsonl[8257] _id=6abd546a485cab4c959174b5 ts=2026-09-30T18:26:50.6000000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[9511] _id=6ac3ede7de269131f9af24c5 ts=2026-10-05T18:35:18.9580000Z; 71h 33m: 6aa4144c41b41dbac0c7f26b.jsonl[4162] _id=6ab6bf57485cab4c955e5521 ts=2026-09-25T18:37:11.3380000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4404] _id=6abaada5485cab4c956f8c35 ts=2026-09-28T18:10:46.1090000Z; 24h 23m: 6aa4144c41b41dbac0c7f26b.jsonl[1186] _id=6ab564c3485cab4c9553cc20 ts=2026-09-24T17:58:27.3090000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2944] _id=6ab6bbab485cab4c955e156f ts=2026-09-25T18:21:31.6780000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 0m 
  - Evidence: 23h 0m: 6aa4144c41b41dbac0c7f26b.jsonl[551] _id=6ab41e47485cab4c954f6f53 ts=2026-09-23T18:45:27.8140000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[709] _id=6ab561dc485cab4c95539041 ts=2026-09-24T17:46:04.6620000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 0m 
  - Evidence: 23h 0m: 6aa4144c41b41dbac0c7f26b.jsonl[558] _id=6ab41e47485cab4c954f6f55 ts=2026-09-23T18:45:27.8440000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[665] _id=6ab561ce485cab4c95538ee9 ts=2026-09-24T17:45:50.1340000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22h 58m 
  - Evidence: 22h 58m: 6aa4144c41b41dbac0c7f26b.jsonl[555] _id=6ab41e43485cab4c954f6f23 ts=2026-09-23T18:45:23.6000000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[613] _id=6ab56145485cab4c955381ad ts=2026-09-24T17:43:33.4810000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.009s..0.037s shown 
  - Evidence: 9ms: 6aa4144c41b41dbac0c7f26b.jsonl[439] _id=6ab41dc2485cab4c954f6a23 ts=2026-09-23T18:43:14.7840000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[441] _id=6ab41dc2485cab4c954f6a25 ts=2026-09-23T18:43:14.7930000Z; 32ms: 6aa4144c41b41dbac0c7f26b.jsonl[712] _id=6ab561d9485cab4c95538fe1 ts=2026-09-24T17:46:01.0510000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[705] _id=6ab561d9485cab4c95538fe4 ts=2026-09-24T17:46:01.0830000Z; 37ms: 6aa4144c41b41dbac0c7f26b.jsonl[713] _id=6ab561da485cab4c9553900c ts=2026-09-24T17:46:02.5910000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[707] _id=6ab561da485cab4c95539011 ts=2026-09-24T17:46:02.6280000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 98h 1m 
  - Evidence: 98h 1m: 6aa4144c41b41dbac0c7f26b.jsonl[8551] _id=6abe878f485cab4c95abd474 ts=2026-10-01T16:17:20.1060000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[8558] _id=6ac3ea07de269131f9aeddcf ts=2026-10-05T18:18:47.1120000Z; 71h 51m: 6aa4144c41b41dbac0c7f26b.jsonl[2524] _id=6ab6b9e0485cab4c955dce45 ts=2026-09-25T18:13:52.3810000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4282] _id=6abaac73485cab4c956f6ded ts=2026-09-28T18:05:40.6820000Z; 24h 22m: 6aa4144c41b41dbac0c7f26b.jsonl[891] _id=6ab56333485cab4c9553abc1 ts=2026-09-24T17:51:47.2190000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2524] _id=6ab6b9e0485cab4c955dce45 ts=2026-09-25T18:13:52.3810000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 98h 1m 
  - Evidence: 98h 1m: 6aa4144c41b41dbac0c7f26b.jsonl[8550] _id=6abe878f485cab4c95abd472 ts=2026-10-01T16:17:20.1050000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[8557] _id=6ac3ea07de269131f9aeddcd ts=2026-10-05T18:18:47.1110000Z; 71h 51m: 6aa4144c41b41dbac0c7f26b.jsonl[2525] _id=6ab6b9e0485cab4c955dce41 ts=2026-09-25T18:13:52.3810000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4281] _id=6abaac73485cab4c956f6de9 ts=2026-09-28T18:05:40.6800000Z; 24h 22m: 6aa4144c41b41dbac0c7f26b.jsonl[892] _id=6ab56333485cab4c9553abbc ts=2026-09-24T17:51:47.2180000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2525] _id=6ab6b9e0485cab4c955dce41 ts=2026-09-25T18:13:52.3810000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 37m 
  - Evidence: 120h 37m: 6aa4144c41b41dbac0c7f26b.jsonl[7904] _id=6abd514e485cab4c9590fdf1 ts=2026-09-30T18:13:35.2890000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[10184] _id=6ac3f19dde269131f9af6701 ts=2026-10-05T18:51:09.3620000Z; 119h 56m: 6aa4144c41b41dbac0c7f26b.jsonl[24] _id=6ab41743485cab4c954f3676 ts=2026-09-23T18:08:50.945Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4280] _id=6abaac7b485cab4c956f6e23 ts=2026-09-28T18:05:47.9240000Z; 24h 2m: 6aa4144c41b41dbac0c7f26b.jsonl[5100] _id=6abab17d485cab4c956ffeb3 ts=2026-09-28T18:27:09.2390000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[7536] _id=6abc0393485cab4c95847ed5 ts=2026-09-29T18:29:39.8340000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[21] _id=6ab415b3485cab4c954f366c ts=2026-09-23T18:08:50.9450000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[24] _id=6ab41743485cab4c954f3676 ts=2026-09-23T18:08:50.945Z; 0ms: 6aa4144c41b41dbac0c7f26b.jsonl[4790] _id=6abaafff485cab4c956fda47 ts=2026-09-28T18:20:47.1340000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4794] _id=6abab017485cab4c956fdd93 ts=2026-09-28T18:20:47.134Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6aa4144c41b41dbac0c7f26b.jsonl[8498] _id=6abd55c7485cab4c9591a84b ts=2026-09-30T18:32:39.7510000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[8564] _id=6ac3ea32de269131f9aee07f ts=2026-10-05T18:19:29.9480000Z; 71h 33m: 6aa4144c41b41dbac0c7f26b.jsonl[3773] _id=6ab6be80485cab4c955e4b65 ts=2026-09-25T18:33:36.3260000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[4296] _id=6abaacbd485cab4c956f725f ts=2026-09-28T18:06:53.8490000Z; 24h 6m: 6aa4144c41b41dbac0c7f26b.jsonl[2456] _id=6ab56703485cab4c955414da ts=2026-09-24T18:08:04.0810000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[2550] _id=6ab6b9f1485cab4c955dd086 ts=2026-09-25T18:14:07.8860000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26b.jsonl[13616] _id=6ac69440de269131f9be25de ts=2026-10-07T18:49:36.2490000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[13617] _id=6ac69440de269131f9be25df ts=2026-10-07T18:49:36.2500000Z; 3ms: 6aa4144c41b41dbac0c7f26b.jsonl[5723] _id=6abc00d1485cab4c95844421 ts=2026-09-29T18:17:51.9990000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[5724] _id=6abc00d1485cab4c95844427 ts=2026-09-29T18:17:52.0020000Z; 3ms: 6aa4144c41b41dbac0c7f26b.jsonl[595] _id=6ab56123485cab4c95537ed7 ts=2026-09-24T17:42:59.5270000Z -> 6aa4144c41b41dbac0c7f26b.jsonl[597] _id=6ab56123485cab4c95537edd ts=2026-09-24T17:42:59.5300000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[366] _id=6ab41cfd485cab4c954f6347 ts=2026-09-23T18:39:57.6740000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[571] _id=6ab41e76485cab4c954f7101 ts=2026-09-23T18:46:14.1840000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[765] _id=6ab5624b485cab4c95539816 ts=2026-09-24T17:47:55.4970000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 61 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[1508] _id=6ab56533485cab4c9553d82a ts=2026-09-24T18:00:17.1540000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1571] _id=6ab5653b485cab4c9553d9dc ts=2026-09-24T18:00:24.1940000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1586] _id=6ab5653e485cab4c9553da92 ts=2026-09-24T18:00:26.3070000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 516 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[1021] _id=6ab56483485cab4c9553c5da ts=2026-09-24T17:57:19.0350000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1047] _id=6ab56486485cab4c9553c628 ts=2026-09-24T17:57:20.5090000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1041] _id=6ab56486485cab4c9553c62a ts=2026-09-24T17:57:20.6080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[409] _id=6ab41db6485cab4c954f6995 ts=2026-09-23T18:43:02.7290000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[430] _id=6ab41db8485cab4c954f69b5 ts=2026-09-23T18:43:04.4330000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[705] _id=6ab561d9485cab4c95538fe4 ts=2026-09-24T17:46:01.0830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[13367] _id=6ac692ccde269131f9bdf08d ts=2026-10-07T18:43:24.5730000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[35] _id=6ab41758485cab4c954f36ec ts=?`; `6aa4144c41b41dbac0c7f26b.jsonl[2535] _id=6ab6b9f0485cab4c955dd02b ts=?`; `6aa4144c41b41dbac0c7f26b.jsonl[4288] _id=6abaacbd485cab4c956f724d ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 467 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[1372] _id=6ab5652a485cab4c9553d648 ts=2026-09-24T18:00:04.6500000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1464] _id=6ab5652a485cab4c9553d654 ts=2026-09-24T18:00:04.8340000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1465] _id=6ab5652a485cab4c9553d670 ts=2026-09-24T18:00:05.0400000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 750 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[1006] _id=6ab5647e485cab4c9553c556 ts=2026-09-24T17:57:17.8740000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1027] _id=6ab5647f485cab4c9553c57c ts=2026-09-24T17:57:18.5530000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[1020] _id=6ab56480485cab4c9553c58f ts=2026-09-24T17:57:18.5640000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[13332] _id=6ac69245de269131f9bde347 ts=2026-10-07T18:41:09.5030000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[13325] _id=6ac6927ade269131f9bde877 ts=2026-10-07T18:42:02.5720000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 10 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[668] _id=6ab561a5485cab4c95538b3b ts=2026-09-24T17:45:09.1450000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[671] _id=6ab561a5485cab4c95538b59 ts=2026-09-24T17:45:09.8900000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[680] _id=6ab561b9485cab4c95538d35 ts=2026-09-24T17:45:29.7780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 PlayerPositionEvent record in 'Unit 4 Dev' inside a 'Unit 3 Dev' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[11160] _id=6ac540a0de269131f9b6b1a9 ts=2026-10-06T18:40:32.0700000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'DialogueStartEvent' (totals: 204 start, 198 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 162 unmatched 'BecameCameraCentered' (totals: 638 open, 537 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 123 unmatched 'BecameVisible' (totals: 1050 open, 1443 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 20 open, 19 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'questActiveEvent' (totals: 40 start, 16 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 350 of 13680 adjacent _id pairs reverse in client time; worst 249.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f26b.jsonl[3120] _id=6ab6bc7e485cab4c955e2664 ts=2026-09-25T18:25:02.4450000Z`; `6aa4144c41b41dbac0c7f26b.jsonl[3121] _id=6ab6bc7f485cab4c955e2678 ts=2026-09-25T18:20:53.0410000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -400.48s, max +0.93s over 13681 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 6581 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2561); Unit 3 Dev (2491); Unit 4 Dev (1353); Unit 1 Dev (149); Unit 5 Dev - Dungeon (27)
- **Intervals:** median 0.36s (p5 0.03s / p95 4.42s, n=6580)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6581/6581 records)
    "pressed"  x6581
data.actionType  (string, 6581/6581 records)
    "Move"  x4800
    "Jump"  x1367
    "Interact"  x287
    "Hoverboard"  x49
    "Ascend"  x34
    "Sprint"  x19
    "Map"  x13
    "Pause"  x5
    "SkipCinematic"  x5
    "Descend"  x2
data.key  (string, 6581/6581 records, 2 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6581/6581 records)
    "Player"  x5560
    "Drone"  x1021
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3668 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3036); Unit 4 Dev (442); Unit 5 Dev - Dungeon (190)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.13s, n=3667)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3668/3668 records)
    "BecameInvisible"  x1443
    "BecameVisible"  x1050
    "BecameCameraCentered"  x638
    "BecameCameraUncentered"  x537
data.pieceId  (string, 3668/3668 records)
    35 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3668/3668 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1650 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (760); Unit 3 Dev (390); Unit 1 Dev (231); Unit 4 Dev (226); Unit 5 Dev - Dungeon (43)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.38s, n=1645)
- **Fields under `data`:**

```text
data.position  (object, 1650/1650 records)
data.position.x  (number, 1650/1650 records)
    numeric range -58.7138 .. 1411.82 (563 unique)
data.position.y  (number, 1650/1650 records)
    numeric range -113.686 .. 162.217 (481 unique)
data.position.z  (number, 1650/1650 records)
    numeric range -639.68 .. 2103.74 (563 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1082 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (506); Unit 3 Dev (259); Unit 1 Dev (228); Unit 5 Dev - Dungeon (48); Unit 4 Dev (41)
- **eventKey:** present on 680 of 1082 records
- **Intervals:** median 4.92s (p5 0.01s / p95 54.50s, n=1081)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x680; [conversationId, dialogueEventType] x402
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1082/1082 records)
    numeric range 8 .. 102 (27 unique)
data.dialogueEventType  (string, 1082/1082 records)
    "DialogueNodeEvent"  x680
    "DialogueStartEvent"  x204
    "DialogueFinishEvent"  x198
data.nodeId  (number, 680/1082 records)
    numeric range 0 .. 290 (172 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 209 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (209)
- **Intervals:** median 0.42s (p5 0.05s / p95 9.58s, n=208)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 209/209 records)
    "argumentationNodeHoverEnd"  x99
    "argumentationNodeHoverStart"  x96
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 209/209 records)
    "Unit 1 - Argumentation Tutorial"  x107
    "Unit 1 - Freshwater"  x102
data.nodeName  (string, 209/209 records)
    "1"  x69
    "A"  x64
    "I"  x58
    "II"  x18
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 118 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (106); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 0.57s (p5 0.16s / p95 11.79s, n=117)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x112; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/118 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/118 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 112/118 records)
    "RightDrag"  x58
    "LeftDrag"  x54
data.currentSoilType  (string, 112/118 records)
    "SANDGRAVEL"  x27
    "SAND"  x19
    "CLAY"  x16
    "CLAYSAND"  x15
    "GRAVEL"  x15
    "CLAYROCK"  x14
    "BEDROCK"  x6
data.isCorrectSelection  (string, 112/118 records)
    "false"  x96
    "true"  x16
data.waterLevelStatus  (string, 112/118 records)
    "TooLow"  x81
    "Proper"  x19
    "TooHigh"  x12
data.waterRetentionChange  (string, 112/118 records)
    "Decrease"  x59
    "Increase"  x37
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `ObjectInterEvent` — 106 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (78); Unit 1 Dev (16); Unit 3 Dev (5); Unit 4 Dev (4); Unit 5 Dev - Dungeon (3)
- **Intervals:** median 6.77s (p5 0.13s / p95 84742.92s, n=105)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 106/106 records)
    16 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 106/106 records)
    37 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 56 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (37); Unit 3 Dev (15); Unit 4 Dev (4)
- **Intervals:** median 8.60s (p5 1.01s / p95 87179.44s, n=55)
- **`data` key-set variants:** [actionType, featureUsed] x39; [actionType, featureUsed, location] x13; [actionType, featureUsed, legendName] x4
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 56/56 records)
    "MapOpenEvent"  x20
    "MapCloseEvent"  x19
    "WaypointMoveEvent"  x9
    "WaypointSetEvent"  x4
    "Selected"  x3
    "Unselected"  x1
data.featureUsed  (string, 56/56 records)
    "Map"  x39
    "Waypoint"  x13
    "Legend"  x4
data.legendName  (string, 4/56 records)
    "360 ft"  x2
    "300 ft"  x1
    "330 ft"  x1
data.location  (object, 13/56 records)
data.location.x  (number, 13/56 records)
    numeric range -328.09 .. 642.91 (13 unique)
data.location.y  (number, 13/56 records)
    numeric range -156.5 .. 352.5 (13 unique)
data.location.z  (number, 13/56 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 56 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 1 Dev (17); Unit 3 Dev (9); Unit 4 Dev (4); Unit 5 Dev - Dungeon (3)
- **eventKey:** present on 56 of 56 records
- **Intervals:** median 280.40s (p5 0.00s / p95 85571.45s, n=55)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x16
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 56/56 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x16
data.questID  (string, 56/56 records)
    16 unique values (see csv/event_unique_values.csv)
data.questName  (string, 56/56 records)
    16 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 16/56 records)
    "Succeeded"  x16
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 47 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 4 Dev (16); Unit 2 Prod (Refactor) (5); Unit 3 Dev (4)
- **Intervals:** median 242.67s (p5 2.80s / p95 87398.39s, n=46)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 47/47 records)
    true  x47
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 33 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (17); Unit 2 Prod (Refactor) (7); Unit 3 Dev (6); Transition (2); MainMenu (1)
- **Intervals:** median 29.83s (p5 0.80s / p95 241920.47s, n=32)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); MainMenu (4); Unit 3 Dev (4); Unit 4 Dev (4); Unit 1 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 879.33s (p5 21.14s / p95 250213.81s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 5360.95s (p5 219.35s / p95 263417.24s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 12 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (12)
- **Intervals:** median 2.84s (p5 0.28s / p95 41461.38s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "submitAnswerEvent"  x12
data.answerSubmitted  (string, 12/12 records)
    "A,1,I"  x10
    "1,I"  x1
    "A,1,"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Freshwater"  x10
    "Unit 1 - Argumentation Tutorial"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8)
- **Intervals:** median 47.72s (p5 21.57s / p95 57999.01s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 6.58s (p5 1.02s / p95 823297.69s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `WaterChamberEvent` — 3 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (3)
- **Intervals:** median 71.02s (p5 54.60s / p95 87.44s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "On"  x3
data.floor  (string, 3/3 records)
    "1"  x2
    "2"  x1
data.machineNumber  (string, 3/3 records)
    "One"  x3
data.machineType  (string, 3/3 records)
    "Condenser"  x2
    "Evaporator"  x1
data.room  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

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
    "unit1"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
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

### `chatEvent` — 1 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "Close"  x1
data.chatID  (string, 1/1 records)
    "NA"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TopographicMapEvent` data.actionType: "Selected" (3x); "Unselected" (1x); "WaypointMoveEvent" (9x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (4x); "Waypoint" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*