# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b81

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b81
- **Game version string(s) in log:** 2.9.0, 2.9.1, 2.9.5, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b81.jsonl
- **Records:** 8191 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b81
- **Time span:** 2026-10-06T18:37:03.979000+00:00 .. 2026-10-19T02:02:13.753000+00:00 (295h 25m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b81\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **17 event types**, 8191 records, 4 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 76 INFO, 5 NOT_TESTED, 62 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2664 | 32.52 | 1 | 1 | 0 | 2026-10-07T19:07:26.810000+00:00 | 2026-10-14T18:45:18.681000+00:00 | 167h 37m |
| InputEvent | 2231 | 27.24 | 1 | 3 | 0 | 2026-10-06T18:37:16.754000+00:00 | 2026-10-19T02:02:13.753000+00:00 | 295h 24m |
| PlayerPositionEvent | 1510 | 18.43 | 1 | 3 | 0 | 2026-10-06T18:37:13.329000+00:00 | 2026-10-19T02:02:11.457000+00:00 | 295h 24m |
| DialogueEvent | 1113 | 13.59 | 1 | 3 | 764 | 2026-10-06T18:37:33.116000+00:00 | 2026-10-19T01:58:41.012000+00:00 | 295h 21m |
| ObjectInterEvent | 298 | 3.64 | 1 | 3 | 0 | 2026-10-06T18:43:12.477000+00:00 | 2026-10-19T01:58:10.474000+00:00 | 295h 14m |
| argumentationNodeEvent | 167 | 2.04 | 1 | 2 | 0 | 2026-10-06T19:12:42.333000+00:00 | 2026-10-15T14:49:37.386000+00:00 | 211h 36m |
| TopographicMapEvent | 51 | 0.62 | 1 | 2 | 0 | 2026-10-07T19:08:33.013000+00:00 | 2026-10-16T18:42:57.546000+00:00 | 215h 34m |
| questEvent | 41 | 0.5 | 1 | 3 | 41 | 2026-10-06T18:37:33.095000+00:00 | 2026-10-19T01:57:52.668000+00:00 | 295h 20m |
| DEBUGMenu | 27 | 0.33 | 1 | 4 | 0 | 2026-10-06T18:37:13.309000+00:00 | 2026-10-19T01:54:59.456000+00:00 | 295h 17m |
| Soil Key Puzzle | 22 | 0.27 | 1 | 1 | 0 | 2026-10-13T19:04:27.887000+00:00 | 2026-10-13T19:05:01.979000+00:00 | 34.1s |
| gameWindowFocusEvent | 15 | 0.18 | 1 | 3 | 0 | 2026-10-06T18:37:03.979000+00:00 | 2026-10-19T01:54:47.259000+00:00 | 295h 17m |
| argumentationAnswerEvent | 14 | 0.17 | 1 | 2 | 0 | 2026-10-06T19:13:50.915000+00:00 | 2026-10-15T14:49:39.476000+00:00 | 211h 35m |
| gameStartEvent | 13 | 0.16 | 1 | 1 | 0 | 2026-10-06T18:37:03.980000+00:00 | 2026-10-19T01:54:47.259000+00:00 | 295h 17m |
| argumentationEvent | 10 | 0.12 | 1 | 2 | 0 | 2026-10-06T19:13:39.408000+00:00 | 2026-10-15T14:49:39.500000+00:00 | 211h 36m |
| gameWindowUnfocusEvent | 8 | 0.1 | 1 | 3 | 0 | 2026-10-06T19:02:22.712000+00:00 | 2026-10-16T18:58:56.721000+00:00 | 239h 56m |
| crash | 5 | 0.06 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-10-07T18:57:29.602000+00:00 | 2026-10-15T15:59:56.589000+00:00 | 189h 2m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 20.675s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 680546.987s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 0.323s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.088s median 
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
  - Observed: 8.598s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 78193.962s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 38333.632s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 70595.958s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 307.03s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.waterLevelStatus` — baseline categorical value(s) not seen this build. 
  - Observed: TooLow 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 180 ft; 210 ft; 300 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: D,A,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[681] _id=6ac5444cde269131f9b71586 ts=2026-10-06T18:56:12.0040000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[739] _id=6ac5457bde269131f9b72a61 ts=2026-10-06T19:01:14.4380000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[789] _id=6ac54633de269131f9b73bdd ts=2026-10-06T19:04:18.5490000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[9] _id=6ac53fd0de269131f9b69959 ts=2026-10-06T18:37:03.9800000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1054] _id=6ac692e4de269131f9bdf362 ts=2026-10-07T18:43:48.3130000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1242] _id=6ac6941bde269131f9be2016 ts=2026-10-07T18:48:58.8340000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[8] _id=6ac53fd0de269131f9b69957 ts=2026-10-06T18:37:03.9790000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[756] _id=6ac545c2de269131f9b72fdc ts=2026-10-06T19:02:25.6290000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1053] _id=6ac692e4de269131f9bdf361 ts=2026-10-07T18:43:48.3130000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[755] _id=6ac545bfde269131f9b72fad ts=2026-10-06T19:02:22.7120000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1051] _id=6ac692e4de269131f9bdf356 ts=2026-10-06T19:17:30.677Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1238] _id=6ac6941bde269131f9be200a ts=2026-10-07T18:47:37.946Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 14 of 51 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1853] _id=6ac698b1de269131f9bef36f ts=2026-10-07T19:08:33.0130000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1825] _id=6ac698b3de269131f9bef3c2 ts=2026-10-07T19:08:35.1130000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1855] _id=6ac698b8de269131f9bef423 ts=2026-10-07T19:08:40.0070000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2663 | 0.0 | 0.088 | 226.614 | 3.234 | 431419.284 | 0.26 | 986 | 4 |
| InputEvent | 2230 | 0.0 | 0.917 | 476.904 | 22.819 | 430173.066 | 0.13 | 92 | 9 |
| PlayerPositionEvent | 1507 | 0.0 | 10.001 | 705.597 | 10.09 | 430154.489 | 0.09 | 2 | 8 |
| DialogueEvent | 1112 | 0.0 | 5.915 | 956.176 | 50.512 | 430369.553 | 0.06 | 287 | 8 |
| ObjectInterEvent | 297 | 0.005 | 0.323 | 3578.781 | 250.233 | 432335.23 | 0.02 | 1 | 8 |
| argumentationNodeEvent | 166 | 0.016 | 0.645 | 4589.247 | 16.609 | 676405.333 | 0.01 | 15 | 2 |
| TopographicMapEvent | 50 | 0.031 | 3.248 | 15521.291 | 86154.498 | 430614.531 | 0.0 | 2 | 5 |
| questEvent | 40 | 0.001 | 307.03 | 26580.489 | 100929.348 | 430642.035 | 0.0 | 5 | 14 |
| DEBUGMenu | 26 | 4.665 | 20.675 | 40887.16 | 173340.934 | 431868.772 | 0.0 | 0 | 8 |
| Soil Key Puzzle | 21 | 0.007 | 0.497 | 1.623 | 6.377 | 7.68 | 36.96 | 1 | 0 |
| gameWindowFocusEvent | 14 | 154.593 | 38333.632 | 75933.091 | 279750.455 | 431880.057 | 0.0 | 0 | 11 |
| argumentationAnswerEvent | 13 | 0.654 | 8.598 | 58596.043 | 321587.664 | 676534.655 | 0.0 | 0 | 2 |
| gameStartEvent | 12 | 154.594 | 78193.962 | 88588.607 | 303944.467 | 431880.057 | 0.0 | 0 | 9 |
| argumentationEvent | 9 | 16.715 | 48.578 | 84640.01 | 439825.649 | 676414.035 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 7 | 86.665 | 70595.958 | 123399.144 | 453682.638 | 604845.075 | 0.0 | 0 | 6 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 680546.987 | 680546.987 | 680546.987 | 680546.987 | 680546.987 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 14 group(s), 47 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1062] _id=6ac69302de269131f9bdf668 ts=2026-10-07T18:44:17.7450000Z == 6ab9a9279a8420a1e6b56b81.jsonl[1063] _id=6ac69302de269131f9bdf669 ts=2026-10-07T18:44:17.7450000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1066] _id=6ac69302de269131f9bdf66c ts=2026-10-07T18:44:17.7460000Z == 6ab9a9279a8420a1e6b56b81.jsonl[1067] _id=6ac69302de269131f9bdf66d ts=2026-10-07T18:44:17.7460000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1247] _id=6ac69437de269131f9be2493 ts=2026-10-07T18:49:25.8750000Z == 6ab9a9279a8420a1e6b56b81.jsonl[1248] _id=6ac69437de269131f9be2494 ts=2026-10-07T18:49:25.8750000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 64 group(s), 92 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1812] _id=6ac69883de269131f9bef00a ts=2026-10-07T19:07:46.8440000Z == 6ab9a9279a8420a1e6b56b81.jsonl[1808] _id=6ac69884de269131f9bef00e ts=2026-10-07T19:07:46.8440000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1814] _id=6ac69885de269131f9bef047 ts=2026-10-07T19:07:48.1350000Z == 6ab9a9279a8420a1e6b56b81.jsonl[1815] _id=6ac69886de269131f9bef04d ts=2026-10-07T19:07:48.1350000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1818] _id=6ac69886de269131f9bef05b ts=2026-10-07T19:07:48.9670000Z == 6ab9a9279a8420a1e6b56b81.jsonl[1819] _id=6ac69886de269131f9bef05c ts=2026-10-07T19:07:48.9670000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1058] _id=6ac692fcde269131f9bdf5bd ts=? == 6ab9a9279a8420a1e6b56b81.jsonl[1244] _id=6ac69437de269131f9be2483 ts=?`; `6ab9a9279a8420a1e6b56b81.jsonl[1601] _id=6ac69738de269131f9bec415 ts=? == 6ab9a9279a8420a1e6b56b81.jsonl[3353] _id=6ac7e81cde269131f9c5e25f ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 192 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `288ms: 6ab9a9279a8420a1e6b56b81.jsonl[101] _id=6ac54143de269131f9b6c501 ts=2026-10-06T18:43:15.2050000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[94] _id=6ac54144de269131f9b6c509 ts=2026-10-06T18:43:15.4930000Z`; `262ms: 6ab9a9279a8420a1e6b56b81.jsonl[94] _id=6ac54144de269131f9b6c509 ts=2026-10-06T18:43:15.4930000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[102] _id=6ac54144de269131f9b6c51a ts=2026-10-06T18:43:15.7550000Z`; `483ms: 6ab9a9279a8420a1e6b56b81.jsonl[96] _id=6ac54145de269131f9b6c540 ts=2026-10-06T18:43:16.8520000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[97] _id=6ac54146de269131f9b6c555 ts=2026-10-06T18:43:17.3350000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `900ms: 6ab9a9279a8420a1e6b56b81.jsonl[996] _id=6ac548ddde269131f9b78bfd ts=2026-10-06T19:15:41.1360000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[998] _id=6ac548dede269131f9b78c2b ts=2026-10-06T19:15:42.0360000Z`; `654ms: 6ab9a9279a8420a1e6b56b81.jsonl[998] _id=6ac548dede269131f9b78c2b ts=2026-10-06T19:15:42.0360000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[981] _id=6ac548dfde269131f9b78c3b ts=2026-10-06T19:15:42.6900000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6ab9a9279a8420a1e6b56b81.jsonl[919] _id=6ac54868de269131f9b77af8 ts=2026-10-06T19:13:43.8600000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[920] _id=6ac54868de269131f9b77b01 ts=2026-10-06T19:13:43.8820000Z`; `38ms: 6ab9a9279a8420a1e6b56b81.jsonl[931] _id=6ac5486bde269131f9b77b80 ts=2026-10-06T19:13:46.5230000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[932] _id=6ac5486bde269131f9b77b87 ts=2026-10-06T19:13:46.5610000Z`; `338ms: 6ab9a9279a8420a1e6b56b81.jsonl[1312] _id=6ac694c2de269131f9be3ea8 ts=2026-10-07T18:51:46.5520000Z ~ 6ab9a9279a8420a1e6b56b81.jsonl[1288] _id=6ac694c3de269131f9be3ebc ts=2026-10-07T18:51:46.8900000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 57m 
  - Evidence: 119h 57m: 6ab9a9279a8420a1e6b56b81.jsonl[2646] _id=6ac7e581de269131f9c58935 ts=2026-10-08T18:48:32.8610000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3713] _id=6ace7c7ede269131f9d12053 ts=2026-10-13T18:46:21.6330000Z; 55h 20m: 6ab9a9279a8420a1e6b56b81.jsonl[7393] _id=6ad26e0dde269131f9e7097e ts=2026-10-16T18:33:48.5650000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7950] _id=6ad57868de269131f9e925c0 ts=2026-10-19T01:54:47.1180000Z; 26h 33m: 6ab9a9279a8420a1e6b56b81.jsonl[7380] _id=6ad0f89dde269131f9dd0850 ts=2026-10-15T16:00:29.1280000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7390] _id=6ad26e01de269131f9e7084f ts=2026-10-16T18:33:37.2060000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a9279a8420a1e6b56b81.jsonl[3660] _id=6ac7ec28de269131f9c681ed ts=2026-10-08T19:16:55.8510000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3772] _id=6ace7d4ade269131f9d129b1 ts=2026-10-13T18:49:45.4040000Z; 55h 0m: 6ab9a9279a8420a1e6b56b81.jsonl[7860] _id=6ad27334de269131f9e7783f ts=2026-10-16T18:55:48.1800000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7994] _id=6ad578cade269131f9e92659 ts=2026-10-19T01:56:25.0470000Z; 26h 33m: 6ab9a9279a8420a1e6b56b81.jsonl[7388] _id=6ad0f8aade269131f9dd09f1 ts=2026-10-15T16:00:42.4820000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7404] _id=6ad26e17de269131f9e70a92 ts=2026-10-16T18:33:59.0410000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 287 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1355] _id=6ac69516de269131f9be4fd9 ts=2026-10-07T18:53:09.9660000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1356] _id=6ac69516de269131f9be4fda ts=2026-10-07T18:53:09.9660000Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[6067] _id=6acfd046de269131f9d7bedc ts=2026-10-14T18:56:06.5280000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[6068] _id=6acfd046de269131f9d7bedd ts=2026-10-14T18:56:06.5280000Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[7175] _id=6ad0e7dade269131f9dbdde5 ts=2026-10-15T14:48:57.9240000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7176] _id=6ad0e7dade269131f9dbdde6 ts=2026-10-15T14:48:57.9240000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 189h 2m 
  - Evidence: 189h 2m: 6ab9a9279a8420a1e6b56b81.jsonl[1520] _id=6ac69619de269131f9be905b ts=2026-10-07T18:57:29.6020000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7375] _id=6ad0f87cde269131f9dd059b ts=2026-10-15T15:59:56.5890000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a9279a8420a1e6b56b81.jsonl[3706] _id=6ac7ec39de269131f9c68446 ts=2026-10-08T19:17:12.6740000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3717] _id=6ace7c97de269131f9d121dd ts=2026-10-13T18:46:45.7400000Z; 54h 57m: 6ab9a9279a8420a1e6b56b81.jsonl[7922] _id=6ad2739fde269131f9e77fc7 ts=2026-10-16T18:57:34.9320000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7955] _id=6ad5788fde269131f9e92606 ts=2026-10-19T01:55:26.0010000Z; 26h 33m: 6ab9a9279a8420a1e6b56b81.jsonl[7382] _id=6ad0f89fde269131f9dd0879 ts=2026-10-15T16:00:30.7330000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7395] _id=6ad26e0fde269131f9e709e2 ts=2026-10-16T18:33:50.6390000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 92 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1062] _id=6ac69302de269131f9bdf668 ts=2026-10-07T18:44:17.7450000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1063] _id=6ac69302de269131f9bdf669 ts=2026-10-07T18:44:17.7450000Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1063] _id=6ac69302de269131f9bdf669 ts=2026-10-07T18:44:17.7450000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1064] _id=6ac69302de269131f9bdf66a ts=2026-10-07T18:44:17.7450000Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1064] _id=6ac69302de269131f9bdf66a ts=2026-10-07T18:44:17.7450000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1065] _id=6ac69302de269131f9bdf66b ts=2026-10-07T18:44:17.7450000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 5m 
  - Evidence: 120h 5m: 6ab9a9279a8420a1e6b56b81.jsonl[3348] _id=6ac7e7edde269131f9c5dd17 ts=2026-10-08T18:58:52.6630000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3952] _id=6ace80bcde269131f9d14fc0 ts=2026-10-13T19:04:27.8930000Z; 55h 5m: 6ab9a9279a8420a1e6b56b81.jsonl[7723] _id=6ad2725dde269131f9e767ad ts=2026-10-16T18:52:12.8590000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[8020] _id=6ad57933de269131f9e926eb ts=2026-10-19T01:58:10.4740000Z; 28h 2m: 6ab9a9279a8420a1e6b56b81.jsonl[6976] _id=6ad0e5e5de269131f9dbbb72 ts=2026-10-15T14:40:37.1330000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7520] _id=6ad27037de269131f9e73d99 ts=2026-10-16T18:43:03.4770000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b81.jsonl[641] _id=6ac543c4de269131f9b70b2d ts=2026-10-06T18:53:55.8840000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[638] _id=6ac543c4de269131f9b70b2f ts=2026-10-06T18:53:55.8890000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a9279a8420a1e6b56b81.jsonl[3707] _id=6ac7ec3fde269131f9c68501 ts=2026-10-08T19:17:18.7920000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3715] _id=6ace7c90de269131f9d12150 ts=2026-10-13T18:46:33.2810000Z; 54h 56m: 6ab9a9279a8420a1e6b56b81.jsonl[7942] _id=6ad273ebde269131f9e78565 ts=2026-10-16T18:58:50.8090000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7962] _id=6ad57876de269131f9e925dc ts=2026-10-19T01:54:59.4760000Z; 26h 33m: 6ab9a9279a8420a1e6b56b81.jsonl[7385] _id=6ad0f8a9de269131f9dd0996 ts=2026-10-15T16:00:41.0480000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7394] _id=6ad26e0fde269131f9e709e1 ts=2026-10-16T18:33:48.5790000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1595] _id=6ac696e4de269131f9bebab6 ts=2026-10-07T19:00:52.6530000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1596] _id=6ac69723de269131f9bec1f4 ts=2026-10-07T19:00:52.653Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[4960] _id=6ace83d8de269131f9d1bf11 ts=2026-10-13T19:17:43.2230000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[4961] _id=6acfcb3dde269131f9d71e8c ts=2026-10-13T19:17:43.223Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a9279a8420a1e6b56b81.jsonl[3619] _id=6ac7ebd9de269131f9c67836 ts=2026-10-08T19:15:36.5470000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3987] _id=6ace8115de269131f9d15588 ts=2026-10-13T19:05:55.8310000Z; 23h 34m: 6ab9a9279a8420a1e6b56b81.jsonl[2643] _id=6ac69aa7de269131f9bf1f7f ts=2026-10-07T19:16:54.2940000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[2792] _id=6ac7e699de269131f9c5a8d6 ts=2026-10-08T18:51:30.2050000Z; 23h 17m: 6ab9a9279a8420a1e6b56b81.jsonl[4958] _id=6ace83c6de269131f9d1bd1b ts=2026-10-13T19:17:24.2930000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[4966] _id=6acfcb51de269131f9d72062 ts=2026-10-14T18:34:55.9310000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 986 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1801] _id=6ac69883de269131f9beefe2 ts=2026-10-07T19:07:46.3190000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1806] _id=6ac69883de269131f9beefea ts=2026-10-07T19:07:46.3190000Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1808] _id=6ac69884de269131f9bef00e ts=2026-10-07T19:07:46.8440000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1809] _id=6ac69884de269131f9bef015 ts=2026-10-07T19:07:46.8440000Z; 0ms: 6ab9a9279a8420a1e6b56b81.jsonl[1809] _id=6ac69884de269131f9bef015 ts=2026-10-07T19:07:46.8440000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1810] _id=6ac69884de269131f9bef01b ts=2026-10-07T19:07:46.8440000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 6ab9a9279a8420a1e6b56b81.jsonl[3961] _id=6ace80cfde269131f9d150fd ts=2026-10-13T19:04:47.0000000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3963] _id=6ace80d0de269131f9d15101 ts=2026-10-13T19:04:47.0070000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 36m 
  - Evidence: 119h 36m: 6ab9a9279a8420a1e6b56b81.jsonl[3594] _id=6ac7eb8ede269131f9c6701d ts=2026-10-08T19:14:21.0650000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3793] _id=6ace7da4de269131f9d12c89 ts=2026-10-13T18:51:15.5960000Z; 47h 43m: 6ab9a9279a8420a1e6b56b81.jsonl[6117] _id=6acfd0ebde269131f9d7d1a6 ts=2026-10-14T18:58:51.5160000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7514] _id=6ad27023de269131f9e73c74 ts=2026-10-16T18:42:42.9630000Z; 24h 7m: 6ab9a9279a8420a1e6b56b81.jsonl[3799] _id=6ace7db1de269131f9d12ccc ts=2026-10-13T18:51:28.6520000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[6110] _id=6acfd0d5de269131f9d7cecc ts=2026-10-14T18:58:29.0740000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.048s shown 
  - Evidence: 31ms: 6ab9a9279a8420a1e6b56b81.jsonl[3519] _id=6ac7ea76de269131f9c65033 ts=2026-10-08T19:09:40.8930000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3523] _id=6ac7ea76de269131f9c65037 ts=2026-10-08T19:09:40.9240000Z; 48ms: 6ab9a9279a8420a1e6b56b81.jsonl[3518] _id=6ac7ea75de269131f9c6502b ts=2026-10-08T19:09:40.8450000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3519] _id=6ac7ea76de269131f9c65033 ts=2026-10-08T19:09:40.8930000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 187h 55m 
  - Evidence: 187h 55m: 6ab9a9279a8420a1e6b56b81.jsonl[1375] _id=6ac69523de269131f9be53b0 ts=2026-10-07T18:53:23.2400000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7180] _id=6ad0e7dade269131f9dbdddf ts=2026-10-15T14:48:57.8950000Z; 23h 35m: 6ab9a9279a8420a1e6b56b81.jsonl[1003] _id=6ac548edde269131f9b78e3b ts=2026-10-06T19:15:56.7540000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1324] _id=6ac694c9de269131f9be4027 ts=2026-10-07T18:51:53.0900000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 187h 53m 
  - Evidence: 187h 53m: 6ab9a9279a8420a1e6b56b81.jsonl[1373] _id=6ac69523de269131f9be53be ts=2026-10-07T18:53:23.2570000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7114] _id=6ad0e761de269131f9dbd2ce ts=2026-10-15T14:46:57.2920000Z; 23h 35m: 6ab9a9279a8420a1e6b56b81.jsonl[1007] _id=6ac548edde269131f9b78e3d ts=2026-10-06T19:15:56.7780000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1310] _id=6ac694bcde269131f9be3d4b ts=2026-10-07T18:51:39.8490000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 187h 53m 
  - Evidence: 187h 53m: 6ab9a9279a8420a1e6b56b81.jsonl[1370] _id=6ac6951dde269131f9be518f ts=2026-10-07T18:53:16.7360000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7104] _id=6ad0e752de269131f9dbd13f ts=2026-10-15T14:46:42.0690000Z; 23h 34m: 6ab9a9279a8420a1e6b56b81.jsonl[1001] _id=6ac548e3de269131f9b78cad ts=2026-10-06T19:15:46.4360000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1267] _id=6ac6947dde269131f9be31a8 ts=2026-10-07T18:50:37.4650000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.016s..0.022s shown 
  - Evidence: 16ms: 6ab9a9279a8420a1e6b56b81.jsonl[1320] _id=6ac694c5de269131f9be3f52 ts=2026-10-07T18:51:49.5350000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1321] _id=6ac694c5de269131f9be3f53 ts=2026-10-07T18:51:49.5510000Z; 22ms: 6ab9a9279a8420a1e6b56b81.jsonl[1268] _id=6ac694c1de269131f9be3e77 ts=2026-10-07T18:51:45.1940000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1269] _id=6ac694c1de269131f9be3e78 ts=2026-10-07T18:51:45.2160000Z; 22ms: 6ab9a9279a8420a1e6b56b81.jsonl[919] _id=6ac54868de269131f9b77af8 ts=2026-10-06T19:13:43.8600000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[920] _id=6ac54868de269131f9b77b01 ts=2026-10-06T19:13:43.8820000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a9279a8420a1e6b56b81.jsonl[2651] _id=6ac7e577de269131f9c588ad ts=2026-10-08T18:48:21.9080000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3712] _id=6ace7c7ede269131f9d1205b ts=2026-10-13T18:46:21.9650000Z; 55h 21m: 6ab9a9279a8420a1e6b56b81.jsonl[7392] _id=6ad26e02de269131f9e70854 ts=2026-10-16T18:33:37.3650000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7952] _id=6ad57868de269131f9e925c2 ts=2026-10-19T01:54:47.2590000Z; 26h 33m: 6ab9a9279a8420a1e6b56b81.jsonl[7379] _id=6ad0f88ade269131f9dd06e6 ts=2026-10-15T16:00:10.3530000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7392] _id=6ad26e02de269131f9e70854 ts=2026-10-16T18:33:37.3650000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a9279a8420a1e6b56b81.jsonl[2650] _id=6ac7e577de269131f9c588ac ts=2026-10-08T18:48:21.9080000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3711] _id=6ace7c7ede269131f9d1205a ts=2026-10-13T18:46:21.9650000Z; 54h 57m: 6ab9a9279a8420a1e6b56b81.jsonl[7931] _id=6ad2739dde269131f9e77f81 ts=2026-10-16T18:57:32.7430000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7951] _id=6ad57868de269131f9e925c1 ts=2026-10-19T01:54:47.2590000Z; 26h 33m: 6ab9a9279a8420a1e6b56b81.jsonl[7378] _id=6ad0f88ade269131f9dd06e5 ts=2026-10-15T16:00:10.3530000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7391] _id=6ad26e02de269131f9e70853 ts=2026-10-16T18:33:37.3640000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 168h 0m 
  - Evidence: 168h 0m: 6ab9a9279a8420a1e6b56b81.jsonl[2648] _id=6ac7e576de269131f9c588a9 ts=2026-10-07T19:17:18.738Z -> 6ab9a9279a8420a1e6b56b81.jsonl[6551] _id=6ad0dfcede269131f9db9b55 ts=2026-10-14T19:18:03.813Z; 28h 2m: 6ab9a9279a8420a1e6b56b81.jsonl[7268] _id=6ad0f6b8de269131f9dce629 ts=2026-10-15T14:54:39.771Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7929] _id=6ad2739ade269131f9e77f43 ts=2026-10-16T18:57:30.0560000Z; 23h 30m: 6ab9a9279a8420a1e6b56b81.jsonl[1051] _id=6ac692e4de269131f9bdf356 ts=2026-10-06T19:17:30.677Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1238] _id=6ac6941bde269131f9be200a ts=2026-10-07T18:47:37.946Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 37m 
  - Evidence: 119h 37m: 6ab9a9279a8420a1e6b56b81.jsonl[3506] _id=6ac7ea5dde269131f9c64d3b ts=2026-10-08T19:09:16.3700000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[3716] _id=6ace7c90de269131f9d12151 ts=2026-10-13T18:46:38.4050000Z; 55h 3m: 6ab9a9279a8420a1e6b56b81.jsonl[7708] _id=6ad27247de269131f9e765e5 ts=2026-10-16T18:51:50.7310000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7963] _id=6ad57876de269131f9e925dd ts=2026-10-19T01:55:01.3020000Z; 26h 36m: 6ab9a9279a8420a1e6b56b81.jsonl[7371] _id=6ad0f872de269131f9dd04ae ts=2026-10-15T15:59:45.9620000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[7435] _id=6ad26eb4de269131f9e71952 ts=2026-10-16T18:36:36.2980000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b81.jsonl[1276] _id=6ac6945fde269131f9be2bb0 ts=2026-10-07T18:50:06.8050000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[1277] _id=6ac6945fde269131f9be2bb1 ts=2026-10-07T18:50:06.8060000Z; 2ms: 6ab9a9279a8420a1e6b56b81.jsonl[889] _id=6ac547f9de269131f9b76f74 ts=2026-10-06T19:11:52.2020000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[892] _id=6ac547f9de269131f9b76f78 ts=2026-10-06T19:11:52.2040000Z; 3ms: 6ab9a9279a8420a1e6b56b81.jsonl[4973] _id=6acfcb51de269131f9d7205b ts=2026-10-14T18:34:54.2810000Z -> 6ab9a9279a8420a1e6b56b81.jsonl[4974] _id=6acfcb51de269131f9d7205c ts=2026-10-14T18:34:54.2840000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[836] _id=6ac547d7de269131f9b76cf1 ts=2026-10-06T19:11:18.8230000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1015] _id=6ac54903de269131f9b79158 ts=2026-10-06T19:16:18.9470000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1384] _id=6ac6953fde269131f9be5b0a ts=2026-10-07T18:53:50.6630000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[920] _id=6ac54868de269131f9b77b01 ts=2026-10-06T19:13:43.8820000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[932] _id=6ac5486bde269131f9b77b87 ts=2026-10-06T19:13:46.5610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1058] _id=6ac692fcde269131f9bdf5bd ts=?`; `6ab9a9279a8420a1e6b56b81.jsonl[1244] _id=6ac69437de269131f9be2483 ts=?`; `6ab9a9279a8420a1e6b56b81.jsonl[1601] _id=6ac69738de269131f9bec415 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 159 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[2686] _id=6ac7e6cade269131f9c5ae94 ts=2026-10-08T18:54:00.3930000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[2890] _id=6ac7e6e7de269131f9c5b21e ts=2026-10-08T18:54:29.5790000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[2894] _id=6ac7e6e9de269131f9c5b260 ts=2026-10-08T18:54:31.7830000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 378 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1802] _id=6ac69883de269131f9beefed ts=2026-10-07T19:07:46.6480000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1803] _id=6ac69883de269131f9beeff7 ts=2026-10-07T19:07:46.6620000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1807] _id=6ac69883de269131f9beeffe ts=2026-10-07T19:07:46.6740000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'DialogueStartEvent' (totals: 177 start, 172 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'BecameCameraCentered' (totals: 472 open, 468 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 28 unmatched 'BecameVisible' (totals: 876 open, 848 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 25 start, 16 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 180 of 8185 adjacent _id pairs reverse in client time; worst 223.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b81.jsonl[1863] _id=6ac6994ede269131f9bf00f1 ts=2026-10-07T19:11:10.1740000Z`; `6ab9a9279a8420a1e6b56b81.jsonl[1900] _id=6ac6994fde269131f9bf0100 ts=2026-10-07T19:07:26.8100000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.87s, min -197751.51s, max -0.12s over 8186 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b81\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
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

### `PuzzlePieceVisibleEvent` — 2664 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2664)
- **Intervals:** median 0.09s (p5 0.00s / p95 3.23s, n=2663)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2664/2664 records)
    "BecameVisible"  x876
    "BecameInvisible"  x848
    "BecameCameraCentered"  x472
    "BecameCameraUncentered"  x468
data.pieceId  (string, 2664/2664 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2664/2664 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2231 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1147); Unit 1 Dev (607); Unit 3 Dev (477)
- **Intervals:** median 0.92s (p5 0.08s / p95 22.82s, n=2230)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2231/2231 records)
    "pressed"  x2231
data.actionType  (string, 2231/2231 records)
    "Move"  x1347
    "Interact"  x450
    "Jump"  x202
    "Ascend"  x123
    "Sprint"  x82
    "Hoverboard"  x20
    "SkipCinematic"  x4
    "Map"  x2
    "Pause"  x1
data.key  (string, 2231/2231 records)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2231/2231 records)
    "Player"  x1523
    "Drone"  x708
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1510 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1001); Unit 1 Dev (312); Unit 3 Dev (197)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.09s, n=1507)
- **Fields under `data`:**

```text
data.position  (object, 1510/1510 records)
data.position.x  (number, 1510/1510 records)
    numeric range -34.2217 .. 1427.27 (415 unique)
data.position.y  (number, 1510/1510 records)
    numeric range -112.49 .. 159.495 (297 unique)
data.position.z  (number, 1510/1510 records)
    numeric range -572.566 .. 1825.82 (417 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1113 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (743); Unit 1 Dev (260); Unit 3 Dev (110)
- **eventKey:** present on 764 of 1113 records
- **Intervals:** median 5.92s (p5 0.01s / p95 50.51s, n=1112)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x764; [conversationId, dialogueEventType] x349
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1113/1113 records)
    numeric range 8 .. 103 (26 unique)
data.dialogueEventType  (string, 1113/1113 records)
    "DialogueNodeEvent"  x764
    "DialogueStartEvent"  x177
    "DialogueFinishEvent"  x172
data.nodeId  (number, 764/1113 records)
    numeric range 0 .. 290 (195 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 298 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (181); Unit 2 Prod (Refactor) (111); Unit 3 Dev (6)
- **Intervals:** median 0.32s (p5 0.15s / p95 250.23s, n=297)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 298/298 records)
    15 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 298/298 records)
    41 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 167 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (102); Unit 2 Prod (Refactor) (65)
- **Intervals:** median 0.65s (p5 0.04s / p95 16.61s, n=166)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 167/167 records)
    "argumentationNodeHoverEnd"  x73
    "argumentationNodeHoverStart"  x71
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 167/167 records)
    "Unit 2 – Watershed"  x65
    "Unit 1 - Freshwater"  x64
    "Unit 1 - Argumentation Tutorial"  x38
data.nodeName  (string, 167/167 records)
    "1"  x37
    "A"  x33
    "II"  x33
    "I"  x32
    "C"  x14
    "D"  x10
    "B"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 51 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (49); Unit 3 Dev (2)
- **Intervals:** median 3.25s (p5 0.62s / p95 86154.50s, n=50)
- **`data` key-set variants:** [actionType, featureUsed, location] x21; [actionType, featureUsed] x16; [actionType, featureUsed, legendName] x14
- **Fields under `data`:**

```text
data.actionType  (string, 51/51 records)
    "WaypointMoveEvent"  x19
    "Selected"  x11
    "MapCloseEvent"  x8
    "MapOpenEvent"  x8
    "Unselected"  x3
    "WaypointSetEvent"  x2
data.featureUsed  (string, 51/51 records)
    "Waypoint"  x21
    "Map"  x16
    "Legend"  x14
data.legendName  (string, 14/51 records)
    "Water"  x4
    "360 ft"  x3
    "300 ft"  x2
    "0 ft"  x1
    "180 ft"  x1
    "210 ft"  x1
    "330 ft"  x1
    "90 ft"  x1
data.location  (object, 21/51 records)
data.location.x  (number, 21/51 records)
    numeric range -333.955 .. -13.6306 (16 unique)
data.location.y  (number, 21/51 records)
    numeric range -35.4887 .. 74.4384 (17 unique)
data.location.z  (number, 21/51 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 41 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (17); Unit 3 Dev (6)
- **eventKey:** present on 41 of 41 records
- **Intervals:** median 307.03s (p5 0.00s / p95 100929.35s, n=40)
- **`data` key-set variants:** [questEventType, questID, questName] x25; [questEventType, questID, questName, questSuccessOrFailure] x16
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 41/41 records)
    "questActiveEvent"  x25
    "questFinishEvent"  x16
data.questID  (string, 41/41 records)
    14 unique values (see csv/event_unique_values.csv)
data.questName  (string, 41/41 records)
    14 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 16/41 records)
    "Succeeded"  x16
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 27 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (12); Unit 2 Prod (Refactor) (7); Unit 1 Dev (5); Unit 3 Dev (3)
- **Intervals:** median 20.67s (p5 6.95s / p95 173340.93s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "DebugMenuStateChanged"  x27
data.isOpened  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `Soil Key Puzzle` — 22 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (22)
- **Intervals:** median 0.50s (p5 0.15s / p95 6.38s, n=21)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x20; [Soil Key Puzzle Status, Unit] x2
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/22 records)
    "Finished"  x1
    "Started"  x1
data.Unit  (string, 2/22 records)
    "Unit 2 Prod (Refactor)"  x2
data.actionType  (string, 20/22 records)
    "RightDrag"  x12
    "LeftDrag"  x8
data.currentSoilType  (string, 20/22 records)
    "SAND"  x4
    "SANDGRAVEL"  x4
    "CLAY"  x3
    "CLAYROCK"  x3
    "CLAYSAND"  x3
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 20/22 records)
    "false"  x16
    "true"  x4
data.waterLevelStatus  (string, 20/22 records)
    "TooHigh"  x12
    "Proper"  x8
data.waterRetentionChange  (string, 20/22 records)
    "Increase"  x10
    "Decrease"  x6
    "NoChange"  x4
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 15 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 38333.63s (p5 255.95s / p95 279750.46s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 14 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 8.60s (p5 0.80s / p95 321587.66s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "submitAnswerEvent"  x14
data.answerSubmitted  (string, 14/14 records)
    "A,1,I"  x7
    "A,1,II"  x6
    "D,A,1,II"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Freshwater"  x10
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 78193.96s (p5 240.35s / p95 303944.47s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 48.58s (p5 19.93s / p95 439825.65s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2)
- **Intervals:** median 70595.96s (p5 333.06s / p95 453682.64s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "Permissions check failed"  x3
    "A user gesture is required to request Pointer Lock."  x2
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 2 empty-string)
    "TypeError: Permissions check failed"  x3
    ""  x2
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit1"  x2
    "unit2"  x2
    "unit3"  x1
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 680546.99s (p5 680546.99s / p95 680546.99s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "2"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TopographicMapEvent` data.actionType: "Selected" (11x); "Unselected" (3x); "WaypointMoveEvent" (19x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (14x); "Waypoint" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*