# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f3

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f3
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f3.jsonl
- **Records:** 10885 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f3
- **Time span:** 2026-09-23T13:10:07.797000+00:00 .. 2026-10-12T12:47:05.954000+00:00 (455h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f3\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 10885 records, 7 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 89 INFO, 2 NOT_TESTED, 76 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5152 | 47.33 | 1 | 2 | 0 | 2026-09-29T13:25:14.508000+00:00 | 2026-10-07T13:30:02.094000+00:00 | 192h 4m |
| InputEvent | 2313 | 21.25 | 1 | 5 | 0 | 2026-09-23T13:14:38.423000+00:00 | 2026-10-12T12:46:56.150000+00:00 | 455h 32m |
| PlayerPositionEvent | 1647 | 15.13 | 1 | 5 | 0 | 2026-09-23T13:10:22.554000+00:00 | 2026-10-12T12:47:00.291000+00:00 | 455h 36m |
| DialogueEvent | 1121 | 10.3 | 1 | 5 | 731 | 2026-09-23T13:10:44.440000+00:00 | 2026-10-12T12:46:07.673000+00:00 | 455h 35m |
| ObjectInterEvent | 250 | 2.3 | 1 | 4 | 0 | 2026-09-23T13:15:25.624000+00:00 | 2026-10-12T12:46:22.004000+00:00 | 455h 30m |
| Soil Key Puzzle | 108 | 0.99 | 1 | 2 | 0 | 2026-09-30T13:29:48.506000+00:00 | 2026-10-07T13:25:37.844000+00:00 | 167h 55m |
| argumentationNodeEvent | 66 | 0.61 | 1 | 1 | 0 | 2026-09-25T13:29:01.036000+00:00 | 2026-09-28T13:17:03.399000+00:00 | 71h 48m |
| TopographicMapEvent | 55 | 0.51 | 1 | 2 | 0 | 2026-09-29T13:25:34.667000+00:00 | 2026-10-07T13:16:33.078000+00:00 | 191h 50m |
| questEvent | 55 | 0.51 | 1 | 5 | 55 | 2026-09-23T13:10:44.422000+00:00 | 2026-10-12T12:45:38.153000+00:00 | 455h 34m |
| gameWindowFocusEvent | 28 | 0.26 | 1 | 6 | 0 | 2026-09-23T13:10:07.797000+00:00 | 2026-10-12T12:47:02.878000+00:00 | 455h 36m |
| DEBUGMenu | 23 | 0.21 | 1 | 6 | 0 | 2026-09-23T13:10:22.545000+00:00 | 2026-10-12T12:34:51.089000+00:00 | 455h 24m |
| gameWindowUnfocusEvent | 19 | 0.17 | 1 | 5 | 0 | 2026-09-25T13:34:37.131000+00:00 | 2026-10-12T12:47:05.954000+00:00 | 407h 12m |
| gameStartEvent | 18 | 0.17 | 1 | 1 | 0 | 2026-09-23T13:10:07.797000+00:00 | 2026-10-12T12:34:44.990000+00:00 | 455h 24m |
| argumentationEvent | 8 | 0.07 | 1 | 1 | 0 | 2026-09-25T13:30:06.683000+00:00 | 2026-09-28T13:17:07.767000+00:00 | 71h 47m |
| soilMachine | 8 | 0.07 | 1 | 1 | 0 | 2026-10-12T12:44:26.539000+00:00 | 2026-10-12T12:46:14.143000+00:00 | 1m 47s |
| argumentationAnswerEvent | 6 | 0.06 | 1 | 1 | 0 | 2026-09-25T13:32:12.488000+00:00 | 2026-09-28T13:17:07.745000+00:00 | 71h 44m |
| crash | 5 | 0.05 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T13:41:10.820000+00:00 | 2026-10-06T13:41:11.459000+00:00 | 0.6s |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-28T13:23:54.936000+00:00 | 2026-09-28T13:23:54.936000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 5116.665s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.location; data.location.x; data.location.y; data.location.z 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.918s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 12.178s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 75089.508s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 869.997s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 4637.117s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 0.623s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
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
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Pick Up; Press E To Place Cameras; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pickup Canister; Press E to Plant Seed; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 30 ft; 60 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; B; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 36; 40; 41; 43; 44; 45; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 19 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[173] _id=6ab3d17a485cab4c954bcb0a ts=2026-09-23T13:17:46.7150000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[382] _id=6ab3d306485cab4c954c037a ts=2026-09-23T13:24:22.6800000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[377] _id=6ab3d368485cab4c954c0e8a ts=2026-09-23T13:26:00.7860000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[5] _id=6ab3cfae485cab4c954b893a ts=2026-09-23T13:10:07.7970000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[451] _id=6ab521a8485cab4c955029f5 ts=2026-09-24T13:12:07.8490000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[567] _id=6ab672d9485cab4c95547dc3 ts=2026-09-25T13:10:50.1390000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[4] _id=6ab3cfae485cab4c954b8938 ts=2026-09-23T13:10:07.7970000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[452] _id=6ab521a7485cab4c955029ef ts=2026-09-24T13:12:07.8480000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[568] _id=6ab672d9485cab4c95547db9 ts=2026-09-25T13:10:50.1380000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[969] _id=6ab6786d485cab4c95552812 ts=2026-09-25T13:34:37.1310000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1138] _id=6aba699b485cab4c9567d769 ts=2026-09-28T13:20:27.8500000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1140] _id=6aba699c485cab4c9567d775 ts=2026-09-28T13:20:28.2160000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 22 of 55 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1581] _id=6abbbc4f485cab4c957ce354 ts=2026-09-29T13:25:34.6670000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1615] _id=6abbbc71485cab4c957ceb82 ts=2026-09-29T13:26:09.7830000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[3166] _id=6abd0bd3485cab4c9586c671 ts=2026-09-30T13:17:07.6540000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5151 | 0.0 | 0.027 | 134.243 | 0.91 | 518196.935 | 0.45 | 3248 | 4 |
| InputEvent | 2312 | 0.0 | 1.014 | 709.316 | 16.378 | 431466.09 | 0.08 | 80 | 13 |
| PlayerPositionEvent | 1642 | 8.296 | 10.0 | 998.752 | 10.1 | 430845.611 | 0.06 | 0 | 11 |
| DialogueEvent | 1120 | 0.001 | 5.282 | 1464.396 | 57.461 | 430866.055 | 0.04 | 299 | 10 |
| ObjectInterEvent | 249 | 0.005 | 4.964 | 6585.769 | 429.259 | 518517.865 | 0.01 | 3 | 12 |
| Soil Key Puzzle | 107 | 0.132 | 0.879 | 5649.994 | 10.769 | 518878.809 | 0.01 | 0 | 3 |
| argumentationNodeEvent | 65 | 0.022 | 0.363 | 3976.652 | 10.355 | 258255.75 | 0.02 | 17 | 1 |
| TopographicMapEvent | 54 | 0.154 | 5.918 | 12789.971 | 32944.198 | 516569.559 | 0.0 | 0 | 6 |
| questEvent | 54 | 0.002 | 275.908 | 30372.106 | 146270.059 | 431383.204 | 0.0 | 10 | 20 |
| gameWindowFocusEvent | 27 | 8.57 | 869.997 | 60748.707 | 378278.878 | 433484.897 | 0.0 | 0 | 17 |
| DEBUGMenu | 22 | 6.602 | 5116.665 | 74521.297 | 420177.481 | 433487.182 | 0.0 | 0 | 15 |
| gameWindowUnfocusEvent | 18 | 0.366 | 4637.117 | 81441.601 | 429099.209 | 431003.919 | 0.0 | 0 | 12 |
| gameStartEvent | 17 | 136.779 | 75089.508 | 96439.835 | 430247.216 | 433484.898 | 0.0 | 0 | 14 |
| argumentationEvent | 7 | 40.293 | 62.707 | 36917.298 | 180601.012 | 257918.017 | 0.0 | 0 | 1 |
| soilMachine | 7 | 0.185 | 0.623 | 15.372 | 72.155 | 102.156 | 3.9 | 0 | 0 |
| argumentationAnswerEvent | 5 | 0.943 | 12.178 | 51659.051 | 206610.354 | 258257.65 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 1 | 0.639 | 0.639 | 0.639 | 0.639 | 0.639 | 93.9 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 15 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[9083] _id=6ac644bade269131f9b8b76c ts=2026-10-07T13:10:18.1950000Z == 6aa413b141b41dbac0c7f1f3.jsonl[9084] _id=6ac644bade269131f9b8b76d ts=2026-10-07T13:10:18.1950000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 258 group(s), 407 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1912] _id=6abbbdb2485cab4c957d3586 ts=2026-09-29T13:25:14.5080000Z == 6aa413b141b41dbac0c7f1f3.jsonl[1913] _id=6abbbdb3485cab4c957d3588 ts=2026-09-29T13:25:14.5080000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1789] _id=6abbbd98485cab4c957d2ce8 ts=2026-09-29T13:31:02.4780000Z == 6aa413b141b41dbac0c7f1f3.jsonl[1856] _id=6abbbd98485cab4c957d2d04 ts=2026-09-29T13:31:02.4780000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1806] _id=6abbbd99485cab4c957d2d1e ts=2026-09-29T13:31:02.5160000Z == 6aa413b141b41dbac0c7f1f3.jsonl[1807] _id=6abbbd99485cab4c957d2d29 ts=2026-09-29T13:31:02.5160000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1357] _id=6abbb9d8485cab4c957c5990 ts=? == 6aa413b141b41dbac0c7f1f3.jsonl[5657] _id=6abd33b3485cab4c958d46a0 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 44 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa413b141b41dbac0c7f1f3.jsonl[97] _id=6ab3d0ed485cab4c954bacde ts=2026-09-23T13:15:25.6240000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[100] _id=6ab3d0ed485cab4c954bace5 ts=2026-09-23T13:15:25.6290000Z`; `989ms: 6aa413b141b41dbac0c7f1f3.jsonl[399] _id=6ab3d34c485cab4c954c0b74 ts=2026-09-23T13:25:32.1840000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[398] _id=6ab3d34d485cab4c954c0b8c ts=2026-09-23T13:25:33.1730000Z`; `224ms: 6aa413b141b41dbac0c7f1f3.jsonl[402] _id=6ab3d34f485cab4c954c0bb0 ts=2026-09-23T13:25:35.3880000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[403] _id=6ab3d34f485cab4c954c0bb6 ts=2026-09-23T13:25:35.6120000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1238 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `13ms: 6aa413b141b41dbac0c7f1f3.jsonl[1940] _id=6abbbdb4485cab4c957d35fa ts=2026-09-29T13:28:56.9670000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1936] _id=6abbbdb4485cab4c957d35fc ts=2026-09-29T13:28:56.9800000Z`; `8ms: 6aa413b141b41dbac0c7f1f3.jsonl[1647] _id=6abbbd1b485cab4c957d11ec ts=2026-09-29T13:28:58.3870000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1648] _id=6abbbd1b485cab4c957d11f4 ts=2026-09-29T13:28:58.3950000Z`; `63ms: 6aa413b141b41dbac0c7f1f3.jsonl[1648] _id=6abbbd1b485cab4c957d11f4 ts=2026-09-29T13:28:58.3950000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1645] _id=6abbbd1c485cab4c957d1202 ts=2026-09-29T13:28:58.4580000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `184ms: 6aa413b141b41dbac0c7f1f3.jsonl[5231] _id=6abd0edd485cab4c95880df2 ts=2026-09-30T13:30:03.1750000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[5089] _id=6abd0ede485cab4c95880e28 ts=2026-09-30T13:30:03.3590000Z`; `301ms: 6aa413b141b41dbac0c7f1f3.jsonl[5089] _id=6abd0ede485cab4c95880e28 ts=2026-09-30T13:30:03.3590000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[5148] _id=6abd0ede485cab4c95880e4b ts=2026-09-30T13:30:03.6600000Z`; `448ms: 6aa413b141b41dbac0c7f1f3.jsonl[5148] _id=6abd0ede485cab4c95880e4b ts=2026-09-30T13:30:03.6600000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[5247] _id=6abd0edf485cab4c95880e74 ts=2026-09-30T13:30:04.1080000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `936ms: 6aa413b141b41dbac0c7f1f3.jsonl[1599] _id=6abbbc61485cab4c957ce6b6 ts=2026-09-29T13:25:53.6190000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1602] _id=6abbbc62485cab4c957ce6de ts=2026-09-29T13:25:54.5550000Z`; `415ms: 6aa413b141b41dbac0c7f1f3.jsonl[1601] _id=6abbbc62485cab4c957ce6d1 ts=2026-09-29T13:25:54.3120000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1598] _id=6abbbc62485cab4c957ce6e8 ts=2026-09-29T13:25:54.7270000Z`; `343ms: 6aa413b141b41dbac0c7f1f3.jsonl[1602] _id=6abbbc62485cab4c957ce6de ts=2026-09-29T13:25:54.5550000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1600] _id=6abbbc62485cab4c957ce6fa ts=2026-09-29T13:25:54.8980000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `943ms: 6aa413b141b41dbac0c7f1f3.jsonl[1087] _id=6aba68c3485cab4c9567c7a3 ts=2026-09-28T13:16:51.3090000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1080] _id=6aba68c4485cab4c9567c7b7 ts=2026-09-28T13:16:52.2520000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa413b141b41dbac0c7f1f3.jsonl[834] _id=6ab67721485cab4c95550272 ts=2026-09-25T13:29:05.6210000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[839] _id=6ab67721485cab4c95550276 ts=2026-09-25T13:29:05.6430000Z`; `69ms: 6aa413b141b41dbac0c7f1f3.jsonl[838] _id=6ab67721485cab4c95550268 ts=2026-09-25T13:29:05.5970000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[835] _id=6ab67721485cab4c95550278 ts=2026-09-25T13:29:05.6660000Z`; `80ms: 6aa413b141b41dbac0c7f1f3.jsonl[840] _id=6ab67721485cab4c9555027c ts=2026-09-25T13:29:05.8090000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[841] _id=6ab67721485cab4c95550280 ts=2026-09-25T13:29:05.8890000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `366ms: 6aa413b141b41dbac0c7f1f3.jsonl[1138] _id=6aba699b485cab4c9567d769 ts=2026-09-28T13:20:27.8500000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[1140] _id=6aba699c485cab4c9567d775 ts=2026-09-28T13:20:28.2160000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `623ms: 6aa413b141b41dbac0c7f1f3.jsonl[10772] _id=6accd62cde269131f9cbb4b7 ts=2026-10-12T12:44:28.6930000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[10775] _id=6accd62dde269131f9cbb4bc ts=2026-10-12T12:44:29.3160000Z`; `329ms: 6aa413b141b41dbac0c7f1f3.jsonl[10650] _id=6accd62fde269131f9cbb4c3 ts=2026-10-12T12:44:31.2850000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[10651] _id=6accd62fde269131f9cbb4c8 ts=2026-10-12T12:44:31.6140000Z`; `185ms: 6aa413b141b41dbac0c7f1f3.jsonl[10651] _id=6accd62fde269131f9cbb4c8 ts=2026-10-12T12:44:31.6140000Z ~ 6aa413b141b41dbac0c7f1f3.jsonl[10779] _id=6accd62fde269131f9cbb4cd ts=2026-10-12T12:44:31.7990000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6aa413b141b41dbac0c7f1f3.jsonl[6415] _id=6abe58f4485cab4c95a407fd ts=2026-10-01T12:58:28.5510000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8232] _id=6ac4f643de269131f9b05f22 ts=2026-10-06T13:23:15.7330000Z; 119h 4m: 6aa413b141b41dbac0c7f1f3.jsonl[10107] _id=6ac6496ade269131f9b93795 ts=2026-10-07T13:30:18.3430000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10405] _id=6accd3e4de269131f9cbb1bc ts=2026-10-12T12:34:44.4870000Z; 71h 54m: 6aa413b141b41dbac0c7f1f3.jsonl[569] _id=6ab672f3485cab4c95547fe7 ts=2026-09-25T13:11:16.5050000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[976] _id=6aba6639485cab4c9567a221 ts=2026-09-28T13:06:09.3920000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 41m 
  - Evidence: 119h 41m: 6aa413b141b41dbac0c7f1f3.jsonl[8224] _id=6abe6338485cab4c95a6895b ts=2026-10-01T13:42:16.2450000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8234] _id=6ac4f64bde269131f9b0612a ts=2026-10-06T13:23:22.3000000Z; 118h 55m: 6aa413b141b41dbac0c7f1f3.jsonl[10358] _id=6ac64bbcde269131f9b9c4b8 ts=2026-10-07T13:40:12.6790000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10420] _id=6accd404de269131f9cbb1e8 ts=2026-10-12T12:35:16.2520000Z; 71h 33m: 6aa413b141b41dbac0c7f1f3.jsonl[968] _id=6ab67857485cab4c955525ba ts=2026-09-25T13:34:15.4890000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[990] _id=6aba6684485cab4c9567a3d9 ts=2026-09-28T13:07:22.1120000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 299 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f3.jsonl[1211] _id=6aba6a43485cab4c9567e3e3 ts=2026-09-28T13:23:15.6580000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1208] _id=6aba6a43485cab4c9567e3e7 ts=2026-09-28T13:23:15.6590000Z; 1ms: 6aa413b141b41dbac0c7f1f3.jsonl[6461] _id=6abe5933485cab4c95a40f55 ts=2026-10-01T12:59:31.3700000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[6459] _id=6abe5933485cab4c95a40f57 ts=2026-10-01T12:59:31.3710000Z; 1ms: 6aa413b141b41dbac0c7f1f3.jsonl[8040] _id=6abe609c485cab4c95a5cf3d ts=2026-10-01T13:31:08.7710000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8038] _id=6abe609c485cab4c95a5cf47 ts=2026-10-01T13:31:08.7720000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6aa413b141b41dbac0c7f1f3.jsonl[8095] _id=6abe6182485cab4c95a6100f ts=2026-10-01T13:34:58.0070000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8262] _id=6ac4f6ecde269131f9b07fa1 ts=2026-10-06T13:26:04.0970000Z; 118h 54m: 6aa413b141b41dbac0c7f1f3.jsonl[10386] _id=6ac64be2de269131f9b9cb51 ts=2026-10-07T13:40:50.4870000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10403] _id=6accd3f3de269131f9cbb1c6 ts=2026-10-12T12:34:59.8940000Z; 71h 33m: 6aa413b141b41dbac0c7f1f3.jsonl[948] _id=6ab67833485cab4c955520ae ts=2026-09-25T13:33:39.6120000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[981] _id=6aba6672485cab4c9567a389 ts=2026-09-28T13:07:03.8610000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 80 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f3.jsonl[9083] _id=6ac644bade269131f9b8b76c ts=2026-10-07T13:10:18.1950000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9084] _id=6ac644bade269131f9b8b76d ts=2026-10-07T13:10:18.1950000Z; 0ms: 6aa413b141b41dbac0c7f1f3.jsonl[9084] _id=6ac644bade269131f9b8b76d ts=2026-10-07T13:10:18.1950000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9085] _id=6ac644bade269131f9b8b76e ts=2026-10-07T13:10:18.1950000Z; 0ms: 6aa413b141b41dbac0c7f1f3.jsonl[9085] _id=6ac644bade269131f9b8b76e ts=2026-10-07T13:10:18.1950000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9086] _id=6ac644bade269131f9b8b76f ts=2026-10-07T13:10:18.1950000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 144h 1m 
  - Evidence: 144h 1m: 6aa413b141b41dbac0c7f1f3.jsonl[7858] _id=6abe5ecb485cab4c95a53c49 ts=2026-10-01T13:23:23.4670000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9332] _id=6ac64841de269131f9b8efc7 ts=2026-10-07T13:25:21.3320000Z; 118h 55m: 6aa413b141b41dbac0c7f1f3.jsonl[10351] _id=6ac64ba6de269131f9b9c092 ts=2026-10-07T13:39:50.7210000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10416] _id=6accd404de269131f9cbb1eb ts=2026-10-12T12:35:16.2680000Z; 71h 38m: 6aa413b141b41dbac0c7f1f3.jsonl[820] _id=6ab676fb485cab4c9554fb44 ts=2026-09-25T13:28:28.0350000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[985] _id=6aba6684485cab4c9567a3d7 ts=2026-09-28T13:07:22.0850000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6aa413b141b41dbac0c7f1f3.jsonl[491] _id=6ab52294485cab4c95506029 ts=2026-09-24T13:16:04.4140000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[492] _id=6ab52294485cab4c9550602c ts=2026-09-24T13:16:04.4190000Z; 5ms: 6aa413b141b41dbac0c7f1f3.jsonl[591] _id=6ab67313485cab4c95548386 ts=2026-09-25T13:11:48.4310000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[589] _id=6ab67313485cab4c95548389 ts=2026-09-25T13:11:48.4360000Z; 5ms: 6aa413b141b41dbac0c7f1f3.jsonl[97] _id=6ab3d0ed485cab4c954bacde ts=2026-09-23T13:15:25.6240000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[100] _id=6ab3d0ed485cab4c954bace5 ts=2026-09-23T13:15:25.6290000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 40m 
  - Evidence: 119h 40m: 6aa413b141b41dbac0c7f1f3.jsonl[8227] _id=6abe6346485cab4c95a68bdd ts=2026-10-01T13:42:30.1280000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8237] _id=6ac4f64ade269131f9b0611f ts=2026-10-06T13:23:15.7390000Z; 118h 53m: 6aa413b141b41dbac0c7f1f3.jsonl[10387] _id=6ac64beade269131f9b9ccc6 ts=2026-10-07T13:40:58.4920000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10389] _id=6accd3f1de269131f9cbb1c3 ts=2026-10-12T12:34:51.0970000Z; 71h 31m: 6aa413b141b41dbac0c7f1f3.jsonl[970] _id=6ab67869485cab4c955527ce ts=2026-09-25T13:34:33.3660000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[977] _id=6aba6640485cab4c9567a241 ts=2026-09-28T13:06:09.3980000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 6aa413b141b41dbac0c7f1f3.jsonl[7998] _id=6abe602b485cab4c95a5b01f ts=2026-10-01T13:29:13.3710000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9362] _id=6ac6485ede269131f9b8f613 ts=2026-10-07T13:25:50.3060000Z; 23h 40m: 6aa413b141b41dbac0c7f1f3.jsonl[2864] _id=6abbbe90485cab4c957d655c ts=2026-09-29T13:35:11.6210000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[3336] _id=6abd0c54485cab4c9586e5d6 ts=2026-09-30T13:15:33.0110000Z; 21h 7m: 6aa413b141b41dbac0c7f1f3.jsonl[6280] _id=6abd3488485cab4c958d5772 ts=2026-09-30T16:10:47.0560000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[6779] _id=6abe5d85485cab4c95a4a8af ts=2026-10-01T13:17:56.5150000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3248 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f3.jsonl[10000] _id=6ac64934de269131f9b9295e ts=2026-10-07T13:29:23.4630000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10018] _id=6ac64934de269131f9b92963 ts=2026-10-07T13:29:23.4630000Z; 0ms: 6aa413b141b41dbac0c7f1f3.jsonl[10005] _id=6ac64934de269131f9b9294f ts=2026-10-07T13:29:23.4460000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10013] _id=6ac64934de269131f9b92958 ts=2026-10-07T13:29:23.4460000Z; 0ms: 6aa413b141b41dbac0c7f1f3.jsonl[10011] _id=6ac64934de269131f9b92970 ts=2026-10-07T13:29:23.5980000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10012] _id=6ac64934de269131f9b92974 ts=2026-10-07T13:29:23.5980000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 7m 
  - Evidence: 144h 7m: 6aa413b141b41dbac0c7f1f3.jsonl[6761] _id=6abe5d62485cab4c95a4a2a1 ts=2026-10-01T13:17:22.5200000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9331] _id=6ac64841de269131f9b8efc0 ts=2026-10-07T13:25:21.3290000Z; 21h 5m: 6aa413b141b41dbac0c7f1f3.jsonl[6305] _id=6abd34ba485cab4c958d5a18 ts=2026-09-30T16:11:38.5410000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[6730] _id=6abe5d4d485cab4c95a49f36 ts=2026-10-01T13:17:01.8160000Z; 2h 39m: 6aa413b141b41dbac0c7f1f3.jsonl[5468] _id=6abd0f5c485cab4c95884465 ts=2026-09-30T13:32:12.4530000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[6288] _id=6abd34b7485cab4c958d59e8 ts=2026-09-30T16:11:35.5580000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 29m 
  - Evidence: 143h 29m: 6aa413b141b41dbac0c7f1f3.jsonl[8219] _id=6abe6323485cab4c95a686e1 ts=2026-10-01T13:41:55.4700000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[9125] _id=6ac644fdde269131f9b8b82c ts=2026-10-07T13:11:25.0290000Z; 23h 38m: 6aa413b141b41dbac0c7f1f3.jsonl[2963] _id=6abbbf6e485cab4c957d8804 ts=2026-09-29T13:38:54.9200000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[3166] _id=6abd0bd3485cab4c9586c671 ts=2026-09-30T13:17:07.6540000Z; 20h 52m: 6aa413b141b41dbac0c7f1f3.jsonl[5715] _id=6abd3418485cab4c958d4c82 ts=2026-09-30T16:08:56.5670000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[6489] _id=6abe5997485cab4c95a418f3 ts=2026-10-01T13:01:11.7720000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 71h 44m 
  - Evidence: 71h 44m: 6aa413b141b41dbac0c7f1f3.jsonl[874] _id=6ab677f1485cab4c95551816 ts=2026-09-25T13:32:33.6590000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1087] _id=6aba68c3485cab4c9567c7a3 ts=2026-09-28T13:16:51.3090000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 71h 38m 
  - Evidence: 71h 38m: 6aa413b141b41dbac0c7f1f3.jsonl[931] _id=6ab677f1485cab4c95551820 ts=2026-09-25T13:32:33.6770000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1025] _id=6aba676f485cab4c9567b24e ts=2026-09-28T13:11:11.6940000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 71h 44m 
  - Evidence: 71h 44m: 6aa413b141b41dbac0c7f1f3.jsonl[932] _id=6ab677f0485cab4c955517ec ts=2026-09-25T13:32:32.4160000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1083] _id=6aba68bf485cab4c9567c759 ts=2026-09-28T13:16:48.1660000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.022s..0.023s shown 
  - Evidence: 22ms: 6aa413b141b41dbac0c7f1f3.jsonl[834] _id=6ab67721485cab4c95550272 ts=2026-09-25T13:29:05.6210000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[839] _id=6ab67721485cab4c95550276 ts=2026-09-25T13:29:05.6430000Z; 23ms: 6aa413b141b41dbac0c7f1f3.jsonl[1074] _id=6aba68cb485cab4c9567c879 ts=2026-09-28T13:16:59.2020000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1075] _id=6aba68cb485cab4c9567c87f ts=2026-09-28T13:16:59.2250000Z; 23ms: 6aa413b141b41dbac0c7f1f3.jsonl[1097] _id=6aba68ce485cab4c9567c8bf ts=2026-09-28T13:17:02.1250000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1091] _id=6aba68cf485cab4c9567c8c2 ts=2026-09-28T13:17:02.1480000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6aa413b141b41dbac0c7f1f3.jsonl[6414] _id=6abe58ee485cab4c95a40748 ts=2026-10-01T12:58:22.6460000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8231] _id=6ac4f63bde269131f9b05ce4 ts=2026-10-06T13:23:07.5440000Z; 119h 17m: 6aa413b141b41dbac0c7f1f3.jsonl[9234] _id=6ac64667de269131f9b8c03c ts=2026-10-07T13:17:27.1950000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10402] _id=6accd3e5de269131f9cbb1bf ts=2026-10-12T12:34:44.9900000Z; 71h 55m: 6aa413b141b41dbac0c7f1f3.jsonl[567] _id=6ab672d9485cab4c95547dc3 ts=2026-09-25T13:10:50.1390000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[975] _id=6aba662e485cab4c9567a1e9 ts=2026-09-28T13:05:58.2120000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6aa413b141b41dbac0c7f1f3.jsonl[6413] _id=6abe58ee485cab4c95a40743 ts=2026-10-01T12:58:22.6450000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8230] _id=6ac4f63bde269131f9b05cd9 ts=2026-10-06T13:23:07.5420000Z; 119h 17m: 6aa413b141b41dbac0c7f1f3.jsonl[9233] _id=6ac64667de269131f9b8c03b ts=2026-10-07T13:17:27.1950000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10401] _id=6accd3e5de269131f9cbb1be ts=2026-10-12T12:34:44.9900000Z; 71h 55m: 6aa413b141b41dbac0c7f1f3.jsonl[568] _id=6ab672d9485cab4c95547db9 ts=2026-09-25T13:10:50.1380000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[974] _id=6aba662e485cab4c9567a1e7 ts=2026-09-28T13:05:58.2110000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6aa413b141b41dbac0c7f1f3.jsonl[8226] _id=6abe6345485cab4c95a68bb5 ts=2026-10-01T13:42:29.2580000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8254] _id=6ac4f6e1de269131f9b07d8c ts=2026-10-06T13:25:53.1770000Z; 119h 6m: 6aa413b141b41dbac0c7f1f3.jsonl[10388] _id=6ac64bebde269131f9b9cd17 ts=2026-10-07T13:40:59.7870000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10883] _id=6accd6c6de269131f9cbb58c ts=2026-10-12T12:47:02.8710000Z; 71h 45m: 6aa413b141b41dbac0c7f1f3.jsonl[969] _id=6ab6786d485cab4c95552812 ts=2026-09-25T13:34:37.1310000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[1138] _id=6aba699b485cab4c9567d769 ts=2026-09-28T13:20:27.8500000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6aa413b141b41dbac0c7f1f3.jsonl[8072] _id=6abe6133485cab4c95a5fc8c ts=2026-10-01T13:33:39.0910000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[8233] _id=6ac4f64ade269131f9b06126 ts=2026-10-06T13:23:22.2950000Z; 118h 58m: 6aa413b141b41dbac0c7f1f3.jsonl[10261] _id=6ac64aebde269131f9b99a00 ts=2026-10-07T13:36:42.9930000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10390] _id=6accd3f1de269131f9cbb1c4 ts=2026-10-12T12:34:56.8950000Z; 71h 33m: 6aa413b141b41dbac0c7f1f3.jsonl[942] _id=6ab6781a485cab4c95551d7a ts=2026-09-25T13:33:14.8600000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[978] _id=6aba6641485cab4c9567a243 ts=2026-09-28T13:06:16.2500000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1f3.jsonl[821] _id=6ab676fc485cab4c9554fb50 ts=2026-09-25T13:28:28.0620000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[819] _id=6ab676fc485cab4c9554fb56 ts=2026-09-25T13:28:28.0640000Z; 3ms: 6aa413b141b41dbac0c7f1f3.jsonl[10526] _id=6accd4b4de269131f9cbb2db ts=2026-10-12T12:38:12.4410000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[10538] _id=6accd4b4de269131f9cbb2dd ts=2026-10-12T12:38:12.4440000Z; 3ms: 6aa413b141b41dbac0c7f1f3.jsonl[991] _id=6aba6684485cab4c9567a3dd ts=2026-09-28T13:07:22.1320000Z -> 6aa413b141b41dbac0c7f1f3.jsonl[992] _id=6aba6684485cab4c9567a3df ts=2026-09-28T13:07:22.1350000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[879] _id=6ab6780a485cab4c95551ae8 ts=2026-09-25T13:32:58.5740000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1124] _id=6aba6973485cab4c9567d397 ts=2026-09-28T13:19:47.2040000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[7945] _id=6abe5ff4485cab4c95a59e89 ts=2026-10-01T13:28:20.5630000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 471 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1927] _id=6abbbdc1485cab4c957d39c8 ts=2026-09-29T13:31:44.6440000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1831] _id=6abbbdc1485cab4c957d39ce ts=2026-09-29T13:31:44.7670000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1798] _id=6abbbdc1485cab4c957d39d2 ts=2026-09-29T13:31:44.7820000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 283 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1929] _id=6abbbdb3485cab4c957d35be ts=2026-09-29T13:25:18.5680000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1640] _id=6abbbd1b485cab4c957d11d0 ts=2026-09-29T13:28:58.2280000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1665] _id=6abbbd1d485cab4c957d128e ts=2026-09-29T13:28:59.7040000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[834] _id=6ab67721485cab4c95550272 ts=2026-09-25T13:29:05.6210000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[839] _id=6ab67721485cab4c95550276 ts=2026-09-25T13:29:05.6430000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[844] _id=6ab6772e485cab4c95550472 ts=2026-09-25T13:29:18.6120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[7] _id=6ab3cfc3485cab4c954b8a1a ts=?`; `6aa413b141b41dbac0c7f1f3.jsonl[1357] _id=6abbb9d8485cab4c957c5990 ts=?`; `6aa413b141b41dbac0c7f1f3.jsonl[2999] _id=6abd0a29485cab4c95869ea9 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 504 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[2103] _id=6abbbdd6485cab4c957d4036 ts=2026-09-29T13:32:06.2380000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[2119] _id=6abbbdda485cab4c957d410f ts=2026-09-29T13:32:09.6940000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[2050] _id=6abbbddb485cab4c957d415d ts=2026-09-29T13:32:09.8790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1207 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1913] _id=6abbbdb3485cab4c957d3588 ts=2026-09-29T13:25:14.5080000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1933] _id=6abbbdb3485cab4c957d35cd ts=2026-09-29T13:25:19.2960000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1940] _id=6abbbdb4485cab4c957d35fa ts=2026-09-29T13:28:56.9670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[9158] _id=6ac64590de269131f9b8ba91 ts=2026-10-07T13:13:52.5500000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[9163] _id=6ac645a2de269131f9b8bb95 ts=2026-10-07T13:14:10.0900000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[9171] _id=6ac645b0de269131f9b8bcae ts=2026-10-07T13:14:24.1380000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[835] _id=6ab67721485cab4c95550278 ts=2026-09-25T13:29:05.6660000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1096] _id=6aba68ce485cab4c9567c8bb ts=2026-09-28T13:17:01.9410000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1097] _id=6aba68ce485cab4c9567c8bf ts=2026-09-28T13:17:02.1250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'DialogueStartEvent' (totals: 198 start, 192 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 99 unmatched 'BecameCameraCentered' (totals: 804 open, 1176 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 233 unmatched 'BecameVisible' (totals: 1561 open, 1611 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 17 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationNodeHoverStart' (totals: 30 open, 31 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 35 start, 20 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 383 of 10879 adjacent _id pairs reverse in client time; worst 375.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f3.jsonl[1907] _id=6abbbdb1485cab4c957d3542 ts=2026-09-29T13:31:29.7440000Z`; `6aa413b141b41dbac0c7f1f3.jsonl[1917] _id=6abbbdb2485cab4c957d3570 ts=2026-09-29T13:25:14.5080000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.33s, min -376.87s, max +7.52s over 10880 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f3\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
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

### `PuzzlePieceVisibleEvent` — 5152 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (4522); Unit 4 Dev (630)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.91s, n=5151)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5152/5152 records)
    "BecameInvisible"  x1611
    "BecameVisible"  x1561
    "BecameCameraUncentered"  x1176
    "BecameCameraCentered"  x804
data.pieceId  (string, 5152/5152 records)
    27 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5152/5152 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2313 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (819); Unit 3 Dev (641); Unit 4 Dev - Dungeon (436); Unit 1 Dev (321); Unit 4 Dev (96)
- **Intervals:** median 1.01s (p5 0.08s / p95 16.38s, n=2312)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2313/2313 records)
    "pressed"  x2313
data.actionType  (string, 2313/2313 records)
    "Move"  x1534
    "Interact"  x310
    "Jump"  x286
    "Sprint"  x122
    "Map"  x26
    "Hoverboard"  x24
    "SkipCinematic"  x7
    "Pause"  x4
data.key  (string, 2313/2313 records)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2313/2313 records)
    "Player"  x2313
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1647 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (746); Unit 1 Dev (460); Unit 3 Dev (228); Unit 4 Dev - Dungeon (138); Unit 4 Dev (75)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.10s, n=1642)
- **Fields under `data`:**

```text
data.position  (object, 1647/1647 records)
data.position.x  (number, 1647/1647 records)
    numeric range -104.624 .. 1400.48 (442 unique)
data.position.y  (number, 1647/1647 records)
    numeric range -93.9074 .. 167.102 (297 unique)
data.position.z  (number, 1647/1647 records)
    numeric range -643.805 .. 1801.84 (442 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1121 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (601); Unit 1 Dev (307); Unit 4 Dev - Dungeon (113); Unit 3 Dev (63); Unit 4 Dev (37)
- **eventKey:** present on 731 of 1121 records
- **Intervals:** median 5.28s (p5 0.00s / p95 57.46s, n=1120)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x731; [conversationId, dialogueEventType] x390
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1121/1121 records)
    numeric range 8 .. 111 (26 unique)
data.dialogueEventType  (string, 1121/1121 records)
    "DialogueNodeEvent"  x731
    "DialogueStartEvent"  x198
    "DialogueFinishEvent"  x192
data.nodeId  (number, 731/1121 records)
    numeric range 0 .. 290 (155 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 250 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (150); Unit 4 Dev - Dungeon (71); Unit 1 Dev (22); Unit 4 Dev (7)
- **Intervals:** median 4.96s (p5 0.15s / p95 429.26s, n=249)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 250/250 records)
    19 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 250/250 records)
    48 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 108 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (90); Unit 4 Dev (18)
- **Intervals:** median 0.88s (p5 0.18s / p95 10.77s, n=107)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x100; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/108 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/108 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 4 Dev"  x2
data.actionType  (string, 100/108 records)
    "RightDrag"  x52
    "LeftDrag"  x48
data.currentSoilType  (string, 100/108 records)
    "CLAY"  x20
    "CLAYSAND"  x19
    "CLAYROCK"  x16
    "SAND"  x16
    "SANDGRAVEL"  x14
    "GRAVEL"  x8
    "BEDROCK"  x7
data.isCorrectSelection  (string, 100/108 records)
    "false"  x78
    "true"  x22
data.waterLevelStatus  (string, 100/108 records)
    "TooHigh"  x51
    "Proper"  x30
    "TooLow"  x19
data.waterRetentionChange  (string, 100/108 records)
    "Increase"  x44
    "Decrease"  x34
    "NoChange"  x22
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 66 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (66)
- **Intervals:** median 0.36s (p5 0.02s / p95 10.35s, n=65)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 66/66 records)
    "argumentationNodeHoverEnd"  x31
    "argumentationNodeHoverStart"  x30
    "argumentationNodeAdd"  x5
data.argumentationTitle  (string, 66/66 records)
    "Unit 1 - Freshwater"  x38
    "Unit 1 - Argumentation Tutorial"  x28
data.nodeName  (string, 66/66 records)
    "I"  x28
    "1"  x21
    "A"  x9
    "II"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 55 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 3 Dev (19)
- **Intervals:** median 5.92s (p5 0.22s / p95 32944.20s, n=54)
- **`data` key-set variants:** [actionType, featureUsed] x33; [actionType, featureUsed, legendName] x22
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "MapOpenEvent"  x17
    "MapCloseEvent"  x16
    "Selected"  x16
    "Unselected"  x6
data.featureUsed  (string, 55/55 records)
    "Map"  x33
    "Legend"  x22
data.legendName  (string, 22/55 records)
    "210 ft"  x6
    "150 ft"  x4
    "180 ft"  x3
    "30 ft"  x3
    "60 ft"  x3
    "0 ft"  x2
    "120 ft"  x1
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 55 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (23); Unit 2 Prod (Refactor) (16); Unit 4 Dev - Dungeon (10); Unit 3 Dev (5); Unit 4 Dev (1)
- **eventKey:** present on 55 of 55 records
- **Intervals:** median 275.91s (p5 0.00s / p95 146270.06s, n=54)
- **`data` key-set variants:** [questEventType, questID, questName] x35; [questEventType, questID, questName, questSuccessOrFailure] x20
- **Fields under `data`:**

```text
data.questEventType  (string, 55/55 records)
    "questActiveEvent"  x35
    "questFinishEvent"  x20
data.questID  (string, 55/55 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 55/55 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 20/55 records)
    "Succeeded"  x20
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (5); Unit 1 Dev (2); Transition (1); Unit 3 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 870.00s (p5 32.34s / p95 378278.88s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (5); MainMenu (4); Unit 1 Dev (4); Unit 4 Dev - Dungeon (2); Unit 4 Dev (1)
- **Intervals:** median 5116.66s (p5 8.01s / p95 420177.48s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 1 Dev (3); Unit 3 Dev (3); Unit 4 Dev - Dungeon (3); Transition (1)
- **Intervals:** median 4637.12s (p5 1.71s / p95 429099.21s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 75089.51s (p5 154.37s / p95 430247.22s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8)
- **Intervals:** median 62.71s (p5 43.54s / p95 180601.01s, n=7)
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

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 0.62s (p5 0.19s / p95 72.16s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Gravel"  x8
data.floor  (string, 8/8 records)
    "3"  x7
    "4"  x1
data.machine  (string, 8/8 records)
    "1"  x8
data.row  (string, 8/8 records)
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 6 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (6)
- **Intervals:** median 12.18s (p5 1.42s / p95 206610.35s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "submitAnswerEvent"  x6
data.answerSubmitted  (string, 6/6 records, 2 empty-string)
    "A,1,I"  x4
    ""  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Freshwater"  x6
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x2
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x2
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit2"  x3
    "unit1"  x1
    "unit3"  x1
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 0.64s (p5 0.64s / p95 0.64s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now
- `chatEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (90 records)
- `TopographicMapEvent` data.actionType: "Selected" (16x); "Unselected" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (22x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*