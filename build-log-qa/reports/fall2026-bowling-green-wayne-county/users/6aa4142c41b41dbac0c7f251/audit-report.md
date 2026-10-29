# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f251

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f251
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f251.jsonl
- **Records:** 12960 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f251
- **Time span:** 2026-09-23T16:28:38.116000+00:00 .. 2026-10-07T17:07:37.985000+00:00 (336h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f251\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 12960 records, 8 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 89 INFO, 2 NOT_TESTED, 73 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3862 | 29.8 | 1 | 3 | 0 | 2026-09-24T16:37:19.433000+00:00 | 2026-10-06T16:56:56.257000+00:00 | 288h 19m |
| InputEvent | 3733 | 28.8 | 1 | 7 | 0 | 2026-09-23T16:30:32.767000+00:00 | 2026-10-07T17:07:24.894000+00:00 | 336h 36m |
| PlayerPositionEvent | 2175 | 16.78 | 1 | 7 | 0 | 2026-09-23T16:30:27.614000+00:00 | 2026-10-07T17:07:35.506000+00:00 | 336h 37m |
| DialogueEvent | 2062 | 15.91 | 1 | 7 | 1274 | 2026-09-23T16:30:49.622000+00:00 | 2026-10-07T17:07:37.985000+00:00 | 336h 36m |
| ObjectInterEvent | 377 | 2.91 | 1 | 7 | 0 | 2026-09-23T16:34:54.317000+00:00 | 2026-10-07T17:07:32.873000+00:00 | 336h 32m |
| argumentationNodeEvent | 359 | 2.77 | 1 | 3 | 0 | 2026-09-24T16:26:12.465000+00:00 | 2026-10-07T17:03:35.789000+00:00 | 312h 37m |
| TopographicMapEvent | 112 | 0.86 | 1 | 2 | 0 | 2026-09-24T16:37:48.456000+00:00 | 2026-10-01T16:54:00.085000+00:00 | 168h 16m |
| questEvent | 81 | 0.62 | 1 | 7 | 81 | 2026-09-23T16:30:49.579000+00:00 | 2026-10-07T17:06:51.043000+00:00 | 336h 36m |
| Soil Key Puzzle | 70 | 0.54 | 1 | 3 | 0 | 2026-09-24T16:44:14.967000+00:00 | 2026-10-05T16:44:29.804000+00:00 | 264h 0m |
| argumentationAnswerEvent | 28 | 0.22 | 1 | 3 | 0 | 2026-09-24T16:27:34.798000+00:00 | 2026-10-07T17:03:36.670000+00:00 | 312h 36m |
| soilMachine | 26 | 0.2 | 1 | 1 | 0 | 2026-10-05T17:00:09.058000+00:00 | 2026-10-06T16:52:59.893000+00:00 | 23h 52m |
| DEBUGMenu | 23 | 0.18 | 1 | 8 | 0 | 2026-09-23T16:30:27.606000+00:00 | 2026-10-07T17:04:31.606000+00:00 | 336h 34m |
| gameWindowFocusEvent | 18 | 0.14 | 1 | 3 | 0 | 2026-09-23T16:28:38.116000+00:00 | 2026-10-07T17:06:39.765000+00:00 | 336h 38m |
| gameStartEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-09-23T16:28:38.117000+00:00 | 2026-10-07T16:53:01.431000+00:00 | 336h 24m |
| argumentationEvent | 10 | 0.08 | 1 | 3 | 0 | 2026-09-24T16:27:02.034000+00:00 | 2026-10-07T17:03:36.700000+00:00 | 312h 36m |
| gameWindowUnfocusEvent | 4 | 0.03 | 1 | 4 | 0 | 2026-09-23T17:04:17.785000+00:00 | 2026-10-07T17:06:39.519000+00:00 | 336h 2m |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-24T16:32:10.993000+00:00 | 2026-10-05T16:38:06.367000+00:00 | 264h 5m |
| argumentationToolEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-09-30T16:47:31.896000+00:00 | 2026-09-30T16:47:31.896000+00:00 | 0.0s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 950755.374s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.108s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 17.622s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 85276.39s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 80261.554s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 88480.285s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.265s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.6x vs baseline. 
  - Observed: 28 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,I; A,3,I; A,4,I; A,D,B,2,II; A,D,C,2,II; B,2,II; B,4,I; B,A,1,I; C,1,I; C,1,II; C,2,II; D,2,II; D,A,2,II; I 
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
  - Observed: Unit 2 – Watershed; Unit 5 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 4 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 29 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[195] _id=6ab400e0485cab4c954e71e0 ts=2026-09-23T16:40:00.3460000Z`; `6aa4142c41b41dbac0c7f251.jsonl[316] _id=6ab40382485cab4c954e7efc ts=2026-09-23T16:51:14.4780000Z`; `6aa4142c41b41dbac0c7f251.jsonl[361] _id=6ab4043c485cab4c954e83d2 ts=2026-09-23T16:54:20.5860000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[6] _id=6ab3fe36485cab4c954e612c ts=2026-09-23T16:28:38.1170000Z`; `6aa4142c41b41dbac0c7f251.jsonl[481] _id=6ab54b52485cab4c9552ddc1 ts=2026-09-24T16:09:54.5070000Z`; `6aa4142c41b41dbac0c7f251.jsonl[873] _id=6ab550da485cab4c95531d01 ts=2026-09-24T16:33:30.2520000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[5] _id=6ab3fe36485cab4c954e612a ts=2026-09-23T16:28:38.1160000Z`; `6aa4142c41b41dbac0c7f251.jsonl[472] _id=6ab54b52485cab4c9552ddbf ts=2026-09-24T16:09:54.5050000Z`; `6aa4142c41b41dbac0c7f251.jsonl[872] _id=6ab550da485cab4c95531cff ts=2026-09-24T16:33:30.2510000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 4 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 4} 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[466] _id=6ab40691485cab4c954e93f6 ts=2026-09-23T17:04:17.7850000Z`; `6aa4142c41b41dbac0c7f251.jsonl[2565] _id=6ab56033485cab4c95536e97 ts=2026-09-24T17:38:58.0700000Z`; `6aa4142c41b41dbac0c7f251.jsonl[11717] _id=6ac5255dde269131f9b5339f ts=2026-10-06T16:44:13.7440000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 112 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[991] _id=6ab551dc485cab4c95532491 ts=2026-09-24T16:37:48.4560000Z`; `6aa4142c41b41dbac0c7f251.jsonl[1019] _id=6ab551f0485cab4c95532575 ts=2026-09-24T16:38:08.1020000Z`; `6aa4142c41b41dbac0c7f251.jsonl[2647] _id=6ab6a141485cab4c9559b2e0 ts=2026-09-25T16:28:49.4280000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3861 | 0.0 | 0.032 | 268.836 | 1.007 | 347041.113 | 0.22 | 2359 | 6 |
| InputEvent | 3732 | 0.001 | 0.905 | 324.709 | 18.03 | 344015.562 | 0.18 | 102 | 12 |
| PlayerPositionEvent | 2165 | 6.357 | 10.0 | 559.621 | 10.046 | 343535.622 | 0.11 | 0 | 11 |
| DialogueEvent | 2061 | 0.0 | 5.124 | 587.971 | 39.651 | 343567.319 | 0.1 | 576 | 11 |
| ObjectInterEvent | 376 | 0.0 | 7.015 | 3222.23 | 417.788 | 344136.331 | 0.02 | 6 | 15 |
| argumentationNodeEvent | 358 | 0.018 | 0.249 | 3143.696 | 7.701 | 605356.959 | 0.02 | 103 | 2 |
| TopographicMapEvent | 111 | 0.03 | 4.108 | 5457.402 | 3055.997 | 258892.531 | 0.01 | 2 | 8 |
| questEvent | 80 | 0.004 | 200.99 | 15147.018 | 85221.475 | 343998.824 | 0.0 | 13 | 17 |
| Soil Key Puzzle | 69 | 0.11 | 0.942 | 13774.128 | 52170.464 | 431471.977 | 0.0 | 0 | 5 |
| argumentationAnswerEvent | 27 | 2.887 | 17.622 | 41680.069 | 363697.123 | 605362.176 | 0.0 | 0 | 2 |
| soilMachine | 25 | 0.678 | 5.265 | 3438.833 | 636.372 | 84256.869 | 0.02 | 0 | 2 |
| DEBUGMenu | 22 | 14.512 | 1576.87 | 55074.727 | 250451.847 | 345572.235 | 0.0 | 0 | 16 |
| gameWindowFocusEvent | 17 | 51.032 | 80261.554 | 71287.156 | 276492.318 | 346194.279 | 0.0 | 0 | 13 |
| gameStartEvent | 15 | 202.246 | 85276.39 | 80737.554 | 285205.063 | 346194.279 | 0.0 | 0 | 12 |
| argumentationEvent | 9 | 0.017 | 48.101 | 125043.852 | 571016.703 | 605357.267 | 0.0 | 2 | 2 |
| gameWindowUnfocusEvent | 3 | 87745.775 | 88480.285 | 403247.245 | 939012.135 | 1033515.674 | 0.0 | 0 | 3 |
| EndOfUnit | 1 | 950755.374 | 950755.374 | 950755.374 | 950755.374 | 950755.374 | 0.0 | 0 | 1 |
| argumentationToolEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 264 group(s), 378 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[962] _id=6ab551bf485cab4c95532349 ts=2026-09-24T16:37:19.4330000Z == 6aa4142c41b41dbac0c7f251.jsonl[963] _id=6ab551bf485cab4c9553234b ts=2026-09-24T16:37:19.4330000Z`; `6aa4142c41b41dbac0c7f251.jsonl[947] _id=6ab551c3485cab4c95532375 ts=2026-09-24T16:37:20.3910000Z == 6aa4142c41b41dbac0c7f251.jsonl[972] _id=6ab551c4485cab4c95532377 ts=2026-09-24T16:37:20.3910000Z`; `6aa4142c41b41dbac0c7f251.jsonl[956] _id=6ab551c4485cab4c95532379 ts=2026-09-24T16:37:20.4220000Z == 6aa4142c41b41dbac0c7f251.jsonl[973] _id=6ab551c4485cab4c9553237b ts=2026-09-24T16:37:20.4220000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 27 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4142c41b41dbac0c7f251.jsonl[134] _id=6ab40036485cab4c954e6dde ts=2026-09-23T16:37:10.2800000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[135] _id=6ab40036485cab4c954e6de0 ts=2026-09-23T16:37:10.2880000Z`; `150ms: 6aa4142c41b41dbac0c7f251.jsonl[237] _id=6ab4036d485cab4c954e7e30 ts=2026-09-23T16:50:53.3050000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[304] _id=6ab4036d485cab4c954e7e34 ts=2026-09-23T16:50:53.4550000Z`; `13ms: 6aa4142c41b41dbac0c7f251.jsonl[494] _id=6ab54b99485cab4c9552de8b ts=2026-09-24T16:11:05.3800000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[495] _id=6ab54b99485cab4c9552de8f ts=2026-09-24T16:11:05.3930000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1096 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `371ms: 6aa4142c41b41dbac0c7f251.jsonl[946] _id=6ab551c2485cab4c9553236f ts=2026-09-24T16:37:19.8010000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[970] _id=6ab551c3485cab4c95532371 ts=2026-09-24T16:37:20.1720000Z`; `114ms: 6aa4142c41b41dbac0c7f251.jsonl[970] _id=6ab551c3485cab4c95532371 ts=2026-09-24T16:37:20.1720000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[971] _id=6ab551c3485cab4c95532373 ts=2026-09-24T16:37:20.2860000Z`; `31ms: 6aa4142c41b41dbac0c7f251.jsonl[972] _id=6ab551c4485cab4c95532377 ts=2026-09-24T16:37:20.3910000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[956] _id=6ab551c4485cab4c95532379 ts=2026-09-24T16:37:20.4220000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `156ms: 6aa4142c41b41dbac0c7f251.jsonl[4263] _id=6aba94dd485cab4c956a7bfd ts=2026-09-28T16:25:01.4370000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[4266] _id=6aba94dd485cab4c956a7c00 ts=2026-09-28T16:25:01.5930000Z`; `155ms: 6aa4142c41b41dbac0c7f251.jsonl[4266] _id=6aba94dd485cab4c956a7c00 ts=2026-09-28T16:25:01.5930000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[4252] _id=6aba94de485cab4c956a7c04 ts=2026-09-28T16:25:01.7480000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6aa4142c41b41dbac0c7f251.jsonl[3898] _id=6ab6a4f4485cab4c955c1eb9 ts=2026-09-25T16:44:36.7990000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[3897] _id=6ab6a4f5485cab4c955c1f07 ts=2026-09-25T16:44:36.8290000Z`; `965ms: 6aa4142c41b41dbac0c7f251.jsonl[7296] _id=6abd397e485cab4c958dc972 ts=2026-09-30T16:31:58.7530000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[7299] _id=6abd397f485cab4c958dc982 ts=2026-09-30T16:31:59.7180000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6aa4142c41b41dbac0c7f251.jsonl[8269] _id=6abd3db5485cab4c958ea84e ts=2026-09-30T16:49:57.0220000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[8274] _id=6abd3db5485cab4c958ea858 ts=2026-09-30T16:49:57.0510000Z`; `17ms: 6aa4142c41b41dbac0c7f251.jsonl[12845] _id=6ac67b68de269131f9bd8c03 ts=2026-10-07T17:03:36.6830000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[12848] _id=6ac67b68de269131f9bd8c06 ts=2026-10-07T17:03:36.7000000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 52 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `834ms: 6aa4142c41b41dbac0c7f251.jsonl[761] _id=6ab54fc7485cab4c95530d5b ts=2026-09-24T16:28:55.5440000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[763] _id=6ab54fc8485cab4c95530d63 ts=2026-09-24T16:28:56.3780000Z`; `651ms: 6aa4142c41b41dbac0c7f251.jsonl[769] _id=6ab54fcb485cab4c95530dad ts=2026-09-24T16:28:59.5350000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[765] _id=6ab54fcc485cab4c95530dbc ts=2026-09-24T16:29:00.1860000Z`; `561ms: 6aa4142c41b41dbac0c7f251.jsonl[770] _id=6ab54fcb485cab4c95530db3 ts=2026-09-24T16:28:59.7160000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[771] _id=6ab54fcc485cab4c95530dc1 ts=2026-09-24T16:29:00.2770000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `678ms: 6aa4142c41b41dbac0c7f251.jsonl[11480] _id=6ac522fade269131f9b5140f ts=2026-10-06T16:34:02.3100000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[11484] _id=6ac522fbde269131f9b51419 ts=2026-10-06T16:34:02.9880000Z`; `734ms: 6aa4142c41b41dbac0c7f251.jsonl[11966] _id=6ac5273cde269131f9b57613 ts=2026-10-06T16:52:12.1290000Z ~ 6aa4142c41b41dbac0c7f251.jsonl[11968] _id=6ac5273cde269131f9b57623 ts=2026-10-06T16:52:12.8630000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 59m 
  - Evidence: 95h 59m: 6aa4142c41b41dbac0c7f251.jsonl[9482] _id=6abe8a87485cab4c95ac0036 ts=2026-10-01T16:29:59.9010000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9838] _id=6ac3d058de269131f9adb5ab ts=2026-10-05T16:29:32.1360000Z; 71h 57m: 6aa4142c41b41dbac0c7f251.jsonl[2569] _id=6ab6a052485cab4c955917e6 ts=2026-09-25T16:24:50.9170000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4191] _id=6aba944e485cab4c956a69f6 ts=2026-09-28T16:22:39.0160000Z; 24h 5m: 6aa4142c41b41dbac0c7f251.jsonl[4191] _id=6aba944e485cab4c956a69f6 ts=2026-09-28T16:22:39.0160000Z -> 6aa4142c41b41dbac0c7f251.jsonl[5664] _id=6abbe726485cab4c9580c147 ts=2026-09-29T16:28:22.0710000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4142c41b41dbac0c7f251.jsonl[9824] _id=6abe927e485cab4c95ac4092 ts=2026-10-01T17:03:58.0950000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9846] _id=6ac3d079de269131f9adb763 ts=2026-10-05T16:30:05.4140000Z; 71h 18m: 6aa4142c41b41dbac0c7f251.jsonl[4185] _id=6ab6a988485cab4c955d3435 ts=2026-09-25T17:04:08.6880000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4195] _id=6aba9455485cab4c956a6a87 ts=2026-09-28T16:22:45.1850000Z; 23h 46m: 6aa4142c41b41dbac0c7f251.jsonl[12408] _id=6ac52a98de269131f9b6139f ts=2026-10-06T17:06:32.0530000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12422] _id=6ac67900de269131f9bd4ce3 ts=2026-10-07T16:53:20.3660000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 576 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f251.jsonl[12577] _id=6ac67a67de269131f9bd6eb2 ts=2026-10-07T16:59:19.1870000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12579] _id=6ac67a67de269131f9bd6eb3 ts=2026-10-07T16:59:19.1870000Z; 0ms: 6aa4142c41b41dbac0c7f251.jsonl[12610] _id=6ac67a7dde269131f9bd7168 ts=2026-10-07T16:59:41.3100000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12611] _id=6ac67a7dde269131f9bd7169 ts=2026-10-07T16:59:41.3100000Z; 0ms: 6aa4142c41b41dbac0c7f251.jsonl[12618] _id=6ac67b37de269131f9bd86a4 ts=2026-10-07T17:02:47.2510000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12619] _id=6ac67b37de269131f9bd86a5 ts=2026-10-07T17:02:47.2510000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 264h 5m 
  - Evidence: 264h 5m: 6aa4142c41b41dbac0c7f251.jsonl[870] _id=6ab5508b485cab4c955318a3 ts=2026-09-24T16:32:10.9930000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9998] _id=6ac3d26dde269131f9ade089 ts=2026-10-05T16:38:06.3670000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 6aa4142c41b41dbac0c7f251.jsonl[9768] _id=6abe90a5485cab4c95ac32d1 ts=2026-10-01T16:56:05.9310000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9841] _id=6ac3d062de269131f9adb67f ts=2026-10-05T16:29:41.4930000Z; 71h 19m: 6aa4142c41b41dbac0c7f251.jsonl[4179] _id=6ab6a970485cab4c955d31f9 ts=2026-09-25T17:03:44.8190000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4192] _id=6aba9455485cab4c956a6a83 ts=2026-09-28T16:22:45.1680000Z; 23h 48m: 6aa4142c41b41dbac0c7f251.jsonl[12377] _id=6ac52a11de269131f9b609bb ts=2026-10-06T17:04:17.6120000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12418] _id=6ac678ffde269131f9bd4cc3 ts=2026-10-07T16:53:15.3080000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 102 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f251.jsonl[2571] _id=6ab6a054485cab4c9559195b ts=2026-09-25T16:24:51.6490000Z -> 6aa4142c41b41dbac0c7f251.jsonl[2573] _id=6ab6a054485cab4c9559196b ts=2026-09-25T16:24:51.6500000Z; 1ms: 6aa4142c41b41dbac0c7f251.jsonl[2572] _id=6ab6a054485cab4c9559191a ts=2026-09-25T16:24:51.6480000Z -> 6aa4142c41b41dbac0c7f251.jsonl[2571] _id=6ab6a054485cab4c9559195b ts=2026-09-25T16:24:51.6490000Z; 1ms: 6aa4142c41b41dbac0c7f251.jsonl[2573] _id=6ab6a054485cab4c9559196b ts=2026-09-25T16:24:51.6500000Z -> 6aa4142c41b41dbac0c7f251.jsonl[2574] _id=6ab6a055485cab4c95591989 ts=2026-09-25T16:24:51.6510000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa4142c41b41dbac0c7f251.jsonl[9733] _id=6abe9045485cab4c95ac2ea5 ts=2026-10-01T16:54:29.0590000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9845] _id=6ac3d079de269131f9adb75f ts=2026-10-05T16:30:05.3900000Z; 71h 21m: 6aa4142c41b41dbac0c7f251.jsonl[4160] _id=6ab6a93b485cab4c955d287f ts=2026-09-25T17:02:51.8510000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4243] _id=6aba94c9485cab4c956a7a75 ts=2026-09-28T16:24:41.3800000Z; 23h 50m: 6aa4142c41b41dbac0c7f251.jsonl[12380] _id=6ac52a17de269131f9b60aff ts=2026-10-06T17:04:23.4330000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12438] _id=6ac6794bde269131f9bd5285 ts=2026-10-07T16:54:34.9970000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f251.jsonl[12459] _id=6ac6798ade269131f9bd57fc ts=2026-10-07T16:55:38.4490000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12460] _id=6ac6798ade269131f9bd57fd ts=2026-10-07T16:55:38.4490000Z; 0ms: 6aa4142c41b41dbac0c7f251.jsonl[12508] _id=6ac679ccde269131f9bd5d2a ts=2026-10-07T16:56:44.1140000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12509] _id=6ac679ccde269131f9bd5d2b ts=2026-10-07T16:56:44.1140000Z; 1ms: 6aa4142c41b41dbac0c7f251.jsonl[12342] _id=6ac529cade269131f9b5fcb4 ts=2026-10-06T17:03:06.7820000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12344] _id=6ac529cbde269131f9b5fcb9 ts=2026-10-06T17:03:06.7830000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4142c41b41dbac0c7f251.jsonl[9820] _id=6abe927c485cab4c95ac4088 ts=2026-10-01T17:03:56.5240000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9839] _id=6ac3d059de269131f9adb5d1 ts=2026-10-05T16:29:32.1460000Z; 71h 18m: 6aa4142c41b41dbac0c7f251.jsonl[4186] _id=6ab6a986485cab4c955d341f ts=2026-09-25T17:04:06.4800000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4193] _id=6aba9455485cab4c956a6a81 ts=2026-09-28T16:22:39.0230000Z; 23h 46m: 6aa4142c41b41dbac0c7f251.jsonl[12409] _id=6ac52a99de269131f9b613b6 ts=2026-10-06T17:06:33.7460000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12416] _id=6ac678ffde269131f9bd4cc2 ts=2026-10-07T16:53:15.3040000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 24m 
  - Evidence: 96h 24m: 6aa4142c41b41dbac0c7f251.jsonl[9128] _id=6abe886c485cab4c95abd6bc ts=2026-10-01T16:20:57.6090000Z -> 6aa4142c41b41dbac0c7f251.jsonl[10102] _id=6ac3d40ade269131f9ae0048 ts=2026-10-05T16:44:58.7220000Z; 71h 52m: 6aa4142c41b41dbac0c7f251.jsonl[3717] _id=6ab6a27e485cab4c955a82e6 ts=2026-09-25T16:34:02.3370000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4286] _id=6aba9523485cab4c956a81da ts=2026-09-28T16:26:10.3400000Z; 48h 16m: 6aa4142c41b41dbac0c7f251.jsonl[5229] _id=6aba97c0485cab4c956abc6b ts=2026-09-28T16:37:16.1910000Z -> 6aa4142c41b41dbac0c7f251.jsonl[8402] _id=6abd3e93485cab4c958ebd9c ts=2026-09-30T16:53:38.4450000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2359 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f251.jsonl[1001] _id=6ab55226485cab4c955328b8 ts=2026-09-24T16:37:26.9210000Z -> 6aa4142c41b41dbac0c7f251.jsonl[1002] _id=6ab55226485cab4c955328bf ts=2026-09-24T16:37:26.9210000Z; 0ms: 6aa4142c41b41dbac0c7f251.jsonl[1002] _id=6ab55226485cab4c955328bf ts=2026-09-24T16:37:26.9210000Z -> 6aa4142c41b41dbac0c7f251.jsonl[1003] _id=6ab55226485cab4c955328c2 ts=2026-09-24T16:37:26.9210000Z; 0ms: 6aa4142c41b41dbac0c7f251.jsonl[1003] _id=6ab55226485cab4c955328c2 ts=2026-09-24T16:37:26.9210000Z -> 6aa4142c41b41dbac0c7f251.jsonl[1053] _id=6ab55226485cab4c955328c5 ts=2026-09-24T16:37:26.9210000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6aa4142c41b41dbac0c7f251.jsonl[8370] _id=6abd3e6e485cab4c958eb8e4 ts=2026-09-30T16:53:02.3530000Z -> 6aa4142c41b41dbac0c7f251.jsonl[10084] _id=6ac3d3ddde269131f9adfc8b ts=2026-10-05T16:44:14.3300000Z; 71h 20m: 6aa4142c41b41dbac0c7f251.jsonl[4177] _id=6ab6a96d485cab4c955d317f ts=2026-09-25T17:03:41.7120000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4242] _id=6aba94c9485cab4c956a7a71 ts=2026-09-28T16:24:41.3760000Z; 48h 27m: 6aa4142c41b41dbac0c7f251.jsonl[4271] _id=6aba94e5485cab4c956a7c9b ts=2026-09-28T16:25:09.8970000Z -> 6aa4142c41b41dbac0c7f251.jsonl[8359] _id=6abd3e5e485cab4c958eb6c0 ts=2026-09-30T16:52:46.2870000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 71h 54m 
  - Evidence: 71h 54m: 6aa4142c41b41dbac0c7f251.jsonl[3996] _id=6ab6a7f7485cab4c955d07c5 ts=2026-09-25T16:57:27.2840000Z -> 6aa4142c41b41dbac0c7f251.jsonl[5484] _id=6aba9b43485cab4c956ad96e ts=2026-09-28T16:52:19.8150000Z; 23h 50m: 6aa4142c41b41dbac0c7f251.jsonl[1019] _id=6ab551f0485cab4c95532575 ts=2026-09-24T16:38:08.1020000Z -> 6aa4142c41b41dbac0c7f251.jsonl[2647] _id=6ab6a141485cab4c9559b2e0 ts=2026-09-25T16:28:49.4280000Z; 23h 49m: 6aa4142c41b41dbac0c7f251.jsonl[5499] _id=6aba9b60485cab4c956adb85 ts=2026-09-28T16:52:48.1500000Z -> 6aa4142c41b41dbac0c7f251.jsonl[5817] _id=6abbea5c485cab4c9581024d ts=2026-09-29T16:42:04.6890000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.030s..0.044s shown 
  - Evidence: 30ms: 6aa4142c41b41dbac0c7f251.jsonl[3898] _id=6ab6a4f4485cab4c955c1eb9 ts=2026-09-25T16:44:36.7990000Z -> 6aa4142c41b41dbac0c7f251.jsonl[3897] _id=6ab6a4f5485cab4c955c1f07 ts=2026-09-25T16:44:36.8290000Z; 44ms: 6aa4142c41b41dbac0c7f251.jsonl[3896] _id=6ab6a4f4485cab4c955c1ea0 ts=2026-09-25T16:44:36.7550000Z -> 6aa4142c41b41dbac0c7f251.jsonl[3898] _id=6ab6a4f4485cab4c955c1eb9 ts=2026-09-25T16:44:36.7990000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 9m 
  - Evidence: 168h 9m: 6aa4142c41b41dbac0c7f251.jsonl[8272] _id=6abd3db5485cab4c958ea84c ts=2026-09-30T16:49:56.9960000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12571] _id=6ac67a67de269131f9bd6eb0 ts=2026-10-07T16:59:19.1720000Z; 144h 18m: 6aa4142c41b41dbac0c7f251.jsonl[772] _id=6ab54fcf485cab4c95530dfc ts=2026-09-24T16:29:03.6640000Z -> 6aa4142c41b41dbac0c7f251.jsonl[8026] _id=6abd3d41485cab4c958e9f8a ts=2026-09-30T16:48:01.6130000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 9m 
  - Evidence: 168h 9m: 6aa4142c41b41dbac0c7f251.jsonl[8274] _id=6abd3db5485cab4c958ea858 ts=2026-09-30T16:49:57.0510000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12560] _id=6ac67a62de269131f9bd6e35 ts=2026-10-07T16:59:14.3180000Z; 144h 18m: 6aa4142c41b41dbac0c7f251.jsonl[773] _id=6ab54fcf485cab4c95530dff ts=2026-09-24T16:29:03.6990000Z -> 6aa4142c41b41dbac0c7f251.jsonl[8056] _id=6abd3d21485cab4c958e9bda ts=2026-09-30T16:47:29.5570000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.017s..0.029s shown 
  - Evidence: 17ms: 6aa4142c41b41dbac0c7f251.jsonl[12845] _id=6ac67b68de269131f9bd8c03 ts=2026-10-07T17:03:36.6830000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12848] _id=6ac67b68de269131f9bd8c06 ts=2026-10-07T17:03:36.7000000Z; 29ms: 6aa4142c41b41dbac0c7f251.jsonl[8269] _id=6abd3db5485cab4c958ea84e ts=2026-09-30T16:49:57.0220000Z -> 6aa4142c41b41dbac0c7f251.jsonl[8274] _id=6abd3db5485cab4c958ea858 ts=2026-09-30T16:49:57.0510000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 9m 
  - Evidence: 168h 9m: 6aa4142c41b41dbac0c7f251.jsonl[8268] _id=6abd3db2485cab4c958ea830 ts=2026-09-30T16:49:54.5230000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12557] _id=6ac67a5fde269131f9bd6de9 ts=2026-10-07T16:59:11.4820000Z; 144h 18m: 6aa4142c41b41dbac0c7f251.jsonl[747] _id=6ab54fcd485cab4c95530dea ts=2026-09-24T16:29:01.4400000Z -> 6aa4142c41b41dbac0c7f251.jsonl[8054] _id=6abd3d20485cab4c958e9bc8 ts=2026-09-30T16:47:28.4560000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 103 interval(s) ≤ 0.018s..0.019s shown 
  - Evidence: 18ms: 6aa4142c41b41dbac0c7f251.jsonl[12557] _id=6ac67a5fde269131f9bd6de9 ts=2026-10-07T16:59:11.4820000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12558] _id=6ac67a5fde269131f9bd6dee ts=2026-10-07T16:59:11.5000000Z; 18ms: 6aa4142c41b41dbac0c7f251.jsonl[12682] _id=6ac67aa5de269131f9bd759e ts=2026-10-07T17:00:20.9750000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12692] _id=6ac67aa5de269131f9bd75a6 ts=2026-10-07T17:00:20.9930000Z; 19ms: 6aa4142c41b41dbac0c7f251.jsonl[12661] _id=6ac67a9ade269131f9bd7439 ts=2026-10-07T17:00:10.6800000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12662] _id=6ac67a9ade269131f9bd743a ts=2026-10-07T17:00:10.6990000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 6aa4142c41b41dbac0c7f251.jsonl[8935] _id=6abe8813485cab4c95abd480 ts=2026-10-01T16:19:30.8960000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9836] _id=6ac3d051de269131f9adb4e9 ts=2026-10-05T16:29:25.1750000Z; 71h 57m: 6aa4142c41b41dbac0c7f251.jsonl[2568] _id=6ab6a04c485cab4c955913e0 ts=2026-09-25T16:24:44.4570000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4190] _id=6aba9447485cab4c956a6960 ts=2026-09-28T16:22:31.2850000Z; 24h 9m: 6aa4142c41b41dbac0c7f251.jsonl[11693] _id=6ac5252cde269131f9b52ee5 ts=2026-10-06T16:43:24.7260000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12414] _id=6ac678edde269131f9bd4b7a ts=2026-10-07T16:53:01.4310000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 6aa4142c41b41dbac0c7f251.jsonl[8934] _id=6abe8813485cab4c95abd47e ts=2026-10-01T16:19:30.8940000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9837] _id=6ac3d051de269131f9adb4e3 ts=2026-10-05T16:29:25.1730000Z; 71h 57m: 6aa4142c41b41dbac0c7f251.jsonl[2567] _id=6ab6a04c485cab4c955913d7 ts=2026-09-25T16:24:44.4560000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4189] _id=6aba9447485cab4c956a695c ts=2026-09-28T16:22:31.2840000Z; 24h 8m: 6aa4142c41b41dbac0c7f251.jsonl[11714] _id=6ac5255fde269131f9b533db ts=2026-10-06T16:44:15.7570000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12413] _id=6ac678edde269131f9bd4b79 ts=2026-10-07T16:53:01.4310000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 287h 5m 
  - Evidence: 287h 5m: 6aa4142c41b41dbac0c7f251.jsonl[2565] _id=6ab56033485cab4c95536e97 ts=2026-09-24T17:38:58.0700000Z -> 6aa4142c41b41dbac0c7f251.jsonl[11717] _id=6ac5255dde269131f9b5339f ts=2026-10-06T16:44:13.7440000Z; 24h 34m: 6aa4142c41b41dbac0c7f251.jsonl[466] _id=6ab40691485cab4c954e93f6 ts=2026-09-23T17:04:17.7850000Z -> 6aa4142c41b41dbac0c7f251.jsonl[2565] _id=6ab56033485cab4c95536e97 ts=2026-09-24T17:38:58.0700000Z; 24h 22m: 6aa4142c41b41dbac0c7f251.jsonl[11717] _id=6ac5255dde269131f9b5339f ts=2026-10-06T16:44:13.7440000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12923] _id=6ac67c1fde269131f9bd94e1 ts=2026-10-07T17:06:39.5190000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 6aa4142c41b41dbac0c7f251.jsonl[9771] _id=6abe90ae485cab4c95ac3345 ts=2026-10-01T16:56:14.4700000Z -> 6aa4142c41b41dbac0c7f251.jsonl[9840] _id=6ac3d05ade269131f9adb5d3 ts=2026-10-05T16:29:33.2940000Z; 71h 20m: 6aa4142c41b41dbac0c7f251.jsonl[4121] _id=6ab6a928485cab4c955d25a1 ts=2026-09-25T17:02:32.7700000Z -> 6aa4142c41b41dbac0c7f251.jsonl[4196] _id=6aba9456485cab4c956a6a8d ts=2026-09-28T16:22:45.2330000Z; 23h 51m: 6aa4142c41b41dbac0c7f251.jsonl[12296] _id=6ac52964de269131f9b5e981 ts=2026-10-06T17:01:24.7380000Z -> 6aa4142c41b41dbac0c7f251.jsonl[12420] _id=6ac678ffde269131f9bd4cc5 ts=2026-10-07T16:53:19.1800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6aa4142c41b41dbac0c7f251.jsonl[11289] _id=6ac521b4de269131f9b5027b ts=2026-10-06T16:28:38.0360000Z -> 6aa4142c41b41dbac0c7f251.jsonl[11160] _id=6ac521b5de269131f9b5027d ts=2026-10-06T16:28:38.0400000Z; 4ms: 6aa4142c41b41dbac0c7f251.jsonl[11819] _id=6ac52631de269131f9b55151 ts=2026-10-06T16:47:45.5860000Z -> 6aa4142c41b41dbac0c7f251.jsonl[11818] _id=6ac52631de269131f9b5515a ts=2026-10-06T16:47:45.5900000Z; 5ms: 6aa4142c41b41dbac0c7f251.jsonl[11137] _id=6ac3d88ade269131f9ae71a1 ts=2026-10-05T17:04:10.0870000Z -> 6aa4142c41b41dbac0c7f251.jsonl[11140] _id=6ac3d88ade269131f9ae71a3 ts=2026-10-05T17:04:10.0920000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 24m 
  - Evidence: 23h 24m: 6aa4142c41b41dbac0c7f251.jsonl[11008] _id=6ac3d822de269131f9ae6961 ts=2026-10-05T17:02:26.1030000Z -> 6aa4142c41b41dbac0c7f251.jsonl[11234] _id=6ac52141de269131f9b4fd57 ts=2026-10-06T16:26:42.9720000Z; 12m 19s: 6aa4142c41b41dbac0c7f251.jsonl[11487] _id=6ac522fcde269131f9b51429 ts=2026-10-06T16:34:04.9320000Z -> 6aa4142c41b41dbac0c7f251.jsonl[11785] _id=6ac525e0de269131f9b5455d ts=2026-10-06T16:46:24.0660000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[683] _id=6ab54ed6485cab4c9552fb4f ts=2026-09-24T16:24:54.7830000Z`; `6aa4142c41b41dbac0c7f251.jsonl[779] _id=6ab54fe5485cab4c95530f4a ts=2026-09-24T16:29:25.7130000Z`; `6aa4142c41b41dbac0c7f251.jsonl[5201] _id=6aba97af485cab4c956abb61 ts=2026-09-28T16:37:03.4550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 250 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[1248] _id=6ab5523a485cab4c95532bc7 ts=2026-09-24T16:39:19.8700000Z`; `6aa4142c41b41dbac0c7f251.jsonl[1240] _id=6ab5523a485cab4c95532bc9 ts=2026-09-24T16:39:19.8910000Z`; `6aa4142c41b41dbac0c7f251.jsonl[1250] _id=6ab5523a485cab4c95532bcd ts=2026-09-24T16:39:20.1830000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 448 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[946] _id=6ab551c2485cab4c9553236f ts=2026-09-24T16:37:19.8010000Z`; `6aa4142c41b41dbac0c7f251.jsonl[970] _id=6ab551c3485cab4c95532371 ts=2026-09-24T16:37:20.1720000Z`; `6aa4142c41b41dbac0c7f251.jsonl[971] _id=6ab551c3485cab4c95532373 ts=2026-09-24T16:37:20.2860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[8274] _id=6abd3db5485cab4c958ea858 ts=2026-09-30T16:49:57.0510000Z`; `6aa4142c41b41dbac0c7f251.jsonl[12848] _id=6ac67b68de269131f9bd8c06 ts=2026-10-07T17:03:36.7000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[11176] _id=6ac520dade269131f9b4f8c6 ts=2026-10-06T16:24:59.1820000Z`; `6aa4142c41b41dbac0c7f251.jsonl[11695] _id=6ac52542de269131f9b53065 ts=2026-10-06T16:43:46.2860000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[7] _id=6ab3fea8485cab4c954e6202 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 644 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[1183] _id=6ab55236485cab4c95532b35 ts=2026-09-24T16:39:12.8070000Z`; `6aa4142c41b41dbac0c7f251.jsonl[1200] _id=6ab55236485cab4c95532b37 ts=2026-09-24T16:39:12.8070000Z`; `6aa4142c41b41dbac0c7f251.jsonl[1209] _id=6ab55237485cab4c95532b39 ts=2026-09-24T16:39:12.8360000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 715 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[963] _id=6ab551bf485cab4c9553234b ts=2026-09-24T16:37:19.4330000Z`; `6aa4142c41b41dbac0c7f251.jsonl[952] _id=6ab551c0485cab4c9553234d ts=2026-09-24T16:37:19.4330000Z`; `6aa4142c41b41dbac0c7f251.jsonl[964] _id=6ab551c0485cab4c95532351 ts=2026-09-24T16:37:19.5440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 42 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[3898] _id=6ab6a4f4485cab4c955c1eb9 ts=2026-09-25T16:44:36.7990000Z`; `6aa4142c41b41dbac0c7f251.jsonl[3897] _id=6ab6a4f5485cab4c955c1f07 ts=2026-09-25T16:44:36.8290000Z`; `6aa4142c41b41dbac0c7f251.jsonl[3975] _id=6ab6a670485cab4c955cdc15 ts=2026-09-25T16:50:56.1230000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 397 start, 391 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 281 unmatched 'BecameCameraCentered' (totals: 817 open, 786 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 143 unmatched 'BecameVisible' (totals: 977 open, 1282 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 45 open, 43 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 48 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 278 of 12958 adjacent _id pairs reverse in client time; worst 142.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f251.jsonl[2681] _id=6ab6a1bc485cab4c955a0052 ts=2026-09-25T16:30:52.2680000Z`; `6aa4142c41b41dbac0c7f251.jsonl[2682] _id=6ab6a1bc485cab4c955a00a5 ts=2026-09-25T16:28:30.0900000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -142.91s, max +19.49s over 12959 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f251\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
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

### `PuzzlePieceVisibleEvent` — 3862 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3022); Unit 4 Dev (570); Unit 3 Dungeon Dev (270)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.01s, n=3861)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3862/3862 records)
    "BecameInvisible"  x1282
    "BecameVisible"  x977
    "BecameCameraCentered"  x817
    "BecameCameraUncentered"  x786
data.pieceId  (string, 3862/3862 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3862/3862 records)
    1860 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3733 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1818); Unit 4 Dev - Dungeon (676); Unit 2 Prod (Refactor) (484); Unit 3 Dungeon Dev (406); Unit 1 Dev (152); Unit 4 Dev (121); Unit 4 Dev - Anderson Base (76)
- **Intervals:** median 0.90s (p5 0.09s / p95 18.03s, n=3732)
- **Fields under `data`:**

```text
data.Value  (string, 3733/3733 records)
    "pressed"  x3733
data.actionType  (string, 3733/3733 records)
    "Move"  x2582
    "Interact"  x702
    "Ascend"  x194
    "Jump"  x122
    "Sprint"  x61
    "Hoverboard"  x44
    "Map"  x24
    "Pause"  x2
    "SkipCinematic"  x1
    "ToggleDebug"  x1
data.key  (string, 3733/3733 records, 23 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3733/3733 records)
    "Player"  x2094
    "Drone"  x1639
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2175 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (604); Unit 3 Dev (602); Unit 1 Dev (336); Unit 4 Dev - Dungeon (280); Unit 3 Dungeon Dev (138); Unit 4 Dev (116); Unit 4 Dev - Anderson Base (99)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.05s, n=2165)
- **Fields under `data`:**

```text
data.position  (object, 2175/2175 records)
data.position.x  (number, 2175/2175 records)
    numeric range -692.295 .. 1549.85 (542 unique)
data.position.y  (number, 2175/2175 records)
    numeric range -112.489 .. 158.187 (405 unique)
data.position.z  (number, 2175/2175 records)
    numeric range -1040.02 .. 2051.8 (541 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2062 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (558); Unit 3 Dev (457); Unit 1 Dev (304); Unit 4 Dev - Dungeon (230); Unit 3 Dungeon Dev (186); Unit 4 Dev - Anderson Base (178); Unit 4 Dev (149)
- **eventKey:** present on 1274 of 2062 records
- **Intervals:** median 5.12s (p5 0.01s / p95 39.65s, n=2061)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1274; [conversationId, dialogueEventType] x788
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2062/2062 records)
    numeric range 8 .. 114 (43 unique)
data.dialogueEventType  (string, 2062/2062 records)
    "DialogueNodeEvent"  x1274
    "DialogueStartEvent"  x397
    "DialogueFinishEvent"  x391
data.nodeId  (number, 1274/2062 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 377 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (153); Unit 3 Dungeon Dev (81); Unit 2 Prod (Refactor) (74); Unit 1 Dev (21); Unit 3 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 4 Dev (12)
- **Intervals:** median 7.02s (p5 0.24s / p95 417.79s, n=376)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 377/377 records)
    35 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 377/377 records)
    86 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 359 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (189); Unit 3 Dev (149); Unit 1 Dev (21)
- **Intervals:** median 0.25s (p5 0.02s / p95 7.70s, n=358)
- **Fields under `data`:**

```text
data.actionType  (string, 359/359 records)
    "argumentationNodeHoverEnd"  x148
    "argumentationNodeHoverStart"  x148
    "argumentationNodeAdd"  x37
    "argumentationNodeRemove"  x26
data.argumentationTitle  (string, 359/359 records)
    "Unit 4 - Flooding"  x189
    "Unit 3 - Pollution Upstream"  x149
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 359/359 records)
    "B"  x66
    "A"  x51
    "1"  x41
    "2"  x37
    "C"  x35
    "I"  x32
    "3"  x30
    "II"  x25
    "4"  x22
    "D"  x13
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 112 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (75); Unit 2 Prod (Refactor) (37)
- **Intervals:** median 4.11s (p5 0.61s / p95 3056.00s, n=111)
- **`data` key-set variants:** [actionType, featureUsed] x88; [actionType, featureUsed, location] x22; [actionType, featureUsed, legendName] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 112/112 records)
    "MapOpenEvent"  x45
    "MapCloseEvent"  x43
    "WaypointMoveEvent"  x18
    "WaypointSetEvent"  x4
    "Selected"  x2
data.featureUsed  (string, 112/112 records)
    "Map"  x88
    "Waypoint"  x22
    "Legend"  x2
data.legendName  (string, 2/112 records)
    "120 ft"  x1
    "360 ft"  x1
data.location  (object, 22/112 records)
data.location.x  (number, 22/112 records)
    numeric range -343.09 .. 216.91 (21 unique)
data.location.y  (number, 22/112 records)
    numeric range -249.5 .. 183.5 (21 unique)
data.location.z  (number, 22/112 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (21); Unit 1 Dev (17); Unit 3 Dev (17); Unit 2 Prod (Refactor) (15); Unit 4 Dev (5); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 200.99s (p5 0.01s / p95 85221.48s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x48; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x48
    "questFinishEvent"  x33
data.questID  (string, 81/81 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/81 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 70 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (44); Unit 3 Dev (16); Unit 4 Dev (10)
- **Intervals:** median 0.94s (p5 0.15s / p95 52170.46s, n=69)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x12
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/70 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/70 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 58/70 records)
    "RightDrag"  x34
    "LeftDrag"  x24
data.currentSoilType  (string, 58/70 records)
    "SAND"  x12
    "CLAY"  x10
    "CLAYSAND"  x10
    "SANDGRAVEL"  x9
    "CLAYROCK"  x8
    "GRAVEL"  x7
    "BEDROCK"  x2
data.isCorrectSelection  (string, 58/70 records)
    "false"  x43
    "true"  x15
data.waterLevelStatus  (string, 58/70 records)
    "Proper"  x27
    "TooHigh"  x26
    "TooLow"  x5
data.waterRetentionChange  (string, 58/70 records)
    "Decrease"  x22
    "Increase"  x21
    "NoChange"  x15
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 28 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (12); Unit 4 Dev - Anderson Base (12); Unit 1 Dev (4)
- **Intervals:** median 17.62s (p5 3.64s / p95 363697.12s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "submitAnswerEvent"  x28
data.answerSubmitted  (string, 28/28 records, 1 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 28/28 records)
    "Unit 3 - Pollution Upstream"  x12
    "Unit 4 - Flooding"  x12
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 5.26s (p5 0.79s / p95 636.37s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Gravel"  x10
    "Bedrock"  x6
    "Clay"  x5
    "Sand"  x5
data.floor  (string, 26/26 records)
    "4"  x11
    "5"  x9
    "3"  x6
data.machine  (string, 26/26 records)
    "1"  x25
    "2"  x1
data.row  (string, 26/26 records)
    "TopRow"  x20
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev (3); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); MainMenu (1)
- **Intervals:** median 1576.87s (p5 191.29s / p95 250451.85s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 18 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 80261.55s (p5 172.00s / p95 276492.32s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 85276.39s (p5 225.83s / p95 285205.06s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 48.10s (p5 0.02s / p95 571016.70s, n=9)
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

### `gameWindowUnfocusEvent` — 4 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 88480.29s (p5 87819.23s / p95 939012.14s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 4/4 records)
    false  x4
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 950755.37s (p5 950755.37s / p95 950755.37s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
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
    "unit1"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (44 records)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (18x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (26x)
- `soilMachine` data.canisterType: "Bedrock" (6x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*