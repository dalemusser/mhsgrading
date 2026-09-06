# MHS Gameplay Log Audit Report — build 09-03-26-4

## 1. Build Information

- **Build ID:** 09-03-26-4
- **Game version string(s) in log:** 2.5.1, 2.5.8, 20260721-11840, 20260902-12353
- **Audit date:** 2026-09-06
- **Log file(s):** wenyi090326-4.stratalog.logdata.json
- **Records:** 8817 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6a9a078fe2ada9cb13ea75c4
- **Time span:** 2026-09-06T00:14:37.471000+00:00 .. 2026-09-06T16:32:00.736000+00:00 (16h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-03-26-4.yaml
- **Baseline:** snapshot build-log-qa\reports\08-31-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 8817 records, 9 scenes.
- Findings: **0 FAIL**, **27 WARNING**, 94 INFO, 0 NOT_TESTED, 87 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `WaterChamberEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DaniEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 08-31-26 but absent now
  - WARNING/Medium `TerasGardenBox`: baseline field(s) absent this build
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 08-31-26 but absent now
  - WARNING/Medium `DialogueEvent`: eventKey does not match its documented format

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3244 | 36.79 | 1 | 4 | 0 | 2026-09-06T02:00:25.853000+00:00 | 2026-09-06T16:32:00.736000+00:00 | 14h 31m |
| InputEvent | 2033 | 23.06 | 1 | 8 | 0 | 2026-09-06T00:15:38.310000+00:00 | 2026-09-06T16:32:00.701000+00:00 | 16h 16m |
| DialogueEvent | 1655 | 18.77 | 1 | 8 | 1063 | 2026-09-06T00:15:00.763000+00:00 | 2026-09-06T16:31:42.864000+00:00 | 16h 16m |
| PlayerPositionEvent | 1280 | 14.52 | 1 | 8 | 0 | 2026-09-06T00:14:44.230000+00:00 | 2026-09-06T16:31:57.735000+00:00 | 16h 17m |
| ObjectInterEvent | 253 | 2.87 | 1 | 8 | 0 | 2026-09-06T00:14:44.232000+00:00 | 2026-09-06T16:31:58.968000+00:00 | 16h 17m |
| argumentationNodeEvent | 125 | 1.42 | 1 | 4 | 0 | 2026-09-06T01:53:42.905000+00:00 | 2026-09-06T16:20:57.375000+00:00 | 14h 27m |
| questEvent | 64 | 0.73 | 1 | 8 | 64 | 2026-09-06T00:15:00.760000+00:00 | 2026-09-06T16:28:47.131000+00:00 | 16h 13m |
| Soil Key Puzzle | 38 | 0.43 | 1 | 3 | 0 | 2026-09-06T02:08:45.039000+00:00 | 2026-09-06T16:10:12.636000+00:00 | 14h 1m |
| gameWindowUnfocusEvent | 25 | 0.28 | 1 | 4 | 0 | 2026-09-06T00:15:01.809000+00:00 | 2026-09-06T16:27:21.756000+00:00 | 16h 12m |
| gameWindowFocusEvent | 24 | 0.27 | 1 | 4 | 0 | 2026-09-06T00:15:05.450000+00:00 | 2026-09-06T16:27:32.192000+00:00 | 16h 12m |
| TopographicMapEvent | 22 | 0.25 | 1 | 2 | 0 | 2026-09-06T02:00:44.258000+00:00 | 2026-09-06T15:58:34.796000+00:00 | 13h 57m |
| argumentationEvent | 12 | 0.14 | 1 | 4 | 0 | 2026-09-06T01:53:49.975000+00:00 | 2026-09-06T16:20:59.510000+00:00 | 14h 27m |
| argumentationToolEvent | 8 | 0.09 | 1 | 3 | 0 | 2026-09-06T01:53:49.241000+00:00 | 2026-09-06T15:43:43.777000+00:00 | 13h 49m |
| gameStartEvent | 7 | 0.08 | 1 | 1 | 0 | 2026-09-06T00:14:37.471000+00:00 | 2026-09-06T16:28:44.725000+00:00 | 16h 14m |
| TerasGardenBox | 6 | 0.07 | 1 | 1 | 0 | 2026-09-06T16:23:06.629000+00:00 | 2026-09-06T16:23:45.678000+00:00 | 39.0s |
| argumentationAnswerEvent | 5 | 0.06 | 1 | 4 | 0 | 2026-09-06T01:53:56.011000+00:00 | 2026-09-06T16:20:59.476000+00:00 | 14h 27m |
| soilMachine | 5 | 0.06 | 1 | 1 | 0 | 2026-09-06T16:13:43.349000+00:00 | 2026-09-06T16:15:49.800000+00:00 | 2m 6s |
| EndOfUnit | 4 | 0.05 | 1 | 4 | 0 | 2026-09-06T01:56:37.548000+00:00 | 2026-09-06T16:28:25.460000+00:00 | 14h 31m |
| DEBUGMenu | 2 | 0.02 | 1 | 1 | 0 | 2026-09-06T15:49:44.442000+00:00 | 2026-09-06T15:49:46.914000+00:00 | 2.5s |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-06T02:21:45.541000+00:00 | 2026-09-06T14:58:13.303000+00:00 | 12h 36m |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-09-06T16:28:47.103000+00:00 | 2026-09-06T16:28:47.103000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DaniEvent` — median interval between records changed substantially. 
  - Observed: 45387.762s median 
  - Expected: 14.09s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 08-31-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — baseline field(s) absent this build. 
  - Observed: data.boxID 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 08-31-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 18 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — event type not present in baseline 08-31-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `DaniEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 2 records 
  - Expected: 42 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: Argumentation; Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `DaniEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: backquote; tab 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to examine; Press E to pick up 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to place; Press E to place glyph; TurnOff 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 3244 records 
  - Expected: 1018 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — categorical value(s) not seen in baseline. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: soilSelected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` — field(s) not present in baseline schema. 
  - Observed: data.legendName
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointMoveEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Selected; Unselected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: Legend 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: C,D,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 08-31-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 51; 52; 53; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 19 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi090326-4.stratalog.logdata.json[8710] _id=6a9cb0ee485cab4c954055be ts=2026-09-06T00:16:46.6950000Z`; `wenyi090326-4.stratalog.logdata.json[8669] _id=6a9cb149485cab4c9540560e ts=2026-09-06T00:18:17.8380000Z`; `wenyi090326-4.stratalog.logdata.json[8645] _id=6a9cb15b485cab4c95405640 ts=2026-09-06T00:18:35.4460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `wenyi090326-4.stratalog.logdata.json[8814] _id=6a9cb06d485cab4c954054ee ts=2026-09-06T00:14:37.4710000Z`; `wenyi090326-4.stratalog.logdata.json[8612] _id=6a9cb1c2485cab4c95405684 ts=2026-09-06T00:20:18.7820000Z`; `wenyi090326-4.stratalog.logdata.json[7641] _id=6a9cc89a485cab4c95405e22 ts=2026-09-06T01:57:46.9010000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `wenyi090326-4.stratalog.logdata.json[8805] _id=6a9cb089485cab4c95405500 ts=2026-09-06T00:15:05.4500000Z`; `wenyi090326-4.stratalog.logdata.json[8613] _id=6a9cb170485cab4c95405680 ts=2026-09-06T00:18:56.5610000Z`; `wenyi090326-4.stratalog.logdata.json[8078] _id=6a9cc466485cab4c95405ab4 ts=2026-09-06T01:39:50.9770000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `wenyi090326-4.stratalog.logdata.json[8807] _id=6a9cb085485cab4c954054fc ts=2026-09-06T00:15:01.8090000Z`; `wenyi090326-4.stratalog.logdata.json[8614] _id=6a9cb16f485cab4c9540567e ts=2026-09-06T00:18:55.2830000Z`; `wenyi090326-4.stratalog.logdata.json[8251] _id=6a9cbdab485cab4c9540595a ts=2026-09-06T01:11:08.1980000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 3 of 22 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7533] _id=6a9cc94c485cab4c95405eb6 ts=2026-09-06T02:00:44.2580000Z`; `wenyi090326-4.stratalog.logdata.json[7527] _id=6a9cc951485cab4c95405ec2 ts=2026-09-06T02:00:49.5280000Z`; `wenyi090326-4.stratalog.logdata.json[4428] _id=6a9ccbe3485cab4c9540773e ts=2026-09-06T02:11:47.8380000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3243 | 0.0 | 0.033 | 16.125 | 0.667 | 46285.816 | 3.72 | 1966 | 4 |
| InputEvent | 2032 | 0.0 | 0.401 | 28.83 | 11.724 | 45409.539 | 2.08 | 93 | 3 |
| DialogueEvent | 1654 | 0.0 | 0.665 | 35.431 | 17.159 | 45440.821 | 1.69 | 442 | 2 |
| PlayerPositionEvent | 1269 | 9.968 | 10.005 | 45.839 | 10.006 | 45397.766 | 1.31 | 0 | 1 |
| ObjectInterEvent | 252 | 0.0 | 3.802 | 232.678 | 174.098 | 46170.331 | 0.26 | 4 | 4 |
| argumentationNodeEvent | 124 | 0.031 | 0.35 | 419.633 | 11.119 | 48990.998 | 0.14 | 24 | 3 |
| questEvent | 63 | 0.001 | 62.356 | 927.403 | 569.944 | 45589.272 | 0.06 | 10 | 3 |
| Soil Key Puzzle | 37 | 0.133 | 0.534 | 1364.53 | 1596.751 | 46167.363 | 0.04 | 0 | 3 |
| gameWindowUnfocusEvent | 24 | 0.0 | 405.531 | 2430.831 | 4267.33 | 41230.904 | 0.02 | 1 | 9 |
| gameWindowFocusEvent | 23 | 7.15 | 369.552 | 2536.815 | 4493.26 | 45675.335 | 0.02 | 0 | 5 |
| TopographicMapEvent | 21 | 0.004 | 2.771 | 2393.835 | 1362.914 | 46966.578 | 0.03 | 4 | 4 |
| argumentationEvent | 11 | 0.031 | 30.681 | 4729.958 | 25587.553 | 48987.264 | 0.01 | 2 | 3 |
| argumentationToolEvent | 7 | 0.434 | 0.967 | 7113.505 | 34536.657 | 49017.777 | 0.01 | 0 | 2 |
| gameStartEvent | 6 | 341.311 | 1204.884 | 9741.209 | 38141.378 | 48905.797 | 0.01 | 0 | 5 |
| TerasGardenBox | 5 | 1.334 | 2.435 | 7.81 | 17.346 | 17.705 | 7.68 | 0 | 0 |
| argumentationAnswerEvent | 4 | 21.71 | 1491.905 | 13005.866 | 41999.072 | 49017.945 | 0.0 | 0 | 3 |
| soilMachine | 4 | 7.404 | 31.396 | 31.613 | 54.309 | 56.255 | 1.9 | 0 | 0 |
| EndOfUnit | 3 | 1551.574 | 1835.243 | 17435.971 | 44212.51 | 48921.095 | 0.0 | 0 | 3 |
| DEBUGMenu | 1 | 2.472 | 2.472 | 2.472 | 2.472 | 2.472 | 24.27 | 0 | 0 |
| DaniEvent | 1 | 45387.762 | 45387.762 | 45387.762 | 45387.762 | 45387.762 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-4.stratalog.logdata.json[972] _id=6a9d9175485cab4c95409262 ts=2026-09-06T16:14:45.5090000Z == wenyi090326-4.stratalog.logdata.json[971] _id=6a9d9175485cab4c95409264 ts=2026-09-06T16:14:45.5090000Z`; `wenyi090326-4.stratalog.logdata.json[863] _id=6a9d91a8485cab4c9540933a ts=2026-09-06T16:15:36.2610000Z == wenyi090326-4.stratalog.logdata.json[864] _id=6a9d91a8485cab4c9540933c ts=2026-09-06T16:15:36.2610000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-4.stratalog.logdata.json[597] _id=6a9d928f485cab4c95409550 ts=2026-09-06T16:19:28.0400000Z == wenyi090326-4.stratalog.logdata.json[596] _id=6a9d928f485cab4c95409552 ts=2026-09-06T16:19:28.0400000Z`; `wenyi090326-4.stratalog.logdata.json[566] _id=6a9d92ad485cab4c9540958e ts=2026-09-06T16:19:57.5200000Z == wenyi090326-4.stratalog.logdata.json[565] _id=6a9d92ad485cab4c95409590 ts=2026-09-06T16:19:57.5200000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 55 group(s), 78 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7570] _id=6a9cc95c485cab4c95405ee6 ts=2026-09-06T02:00:25.9860000Z == wenyi090326-4.stratalog.logdata.json[7569] _id=6a9cc95c485cab4c95405ee8 ts=2026-09-06T02:00:25.9860000Z`; `wenyi090326-4.stratalog.logdata.json[7567] _id=6a9cc95c485cab4c95405eea ts=2026-09-06T02:00:26.0500000Z == wenyi090326-4.stratalog.logdata.json[7568] _id=6a9cc95c485cab4c95405eec ts=2026-09-06T02:00:26.0500000Z`; `wenyi090326-4.stratalog.logdata.json[7509] _id=6a9cc95f485cab4c95405f3e ts=2026-09-06T02:00:55.2290000Z == wenyi090326-4.stratalog.logdata.json[7508] _id=6a9cc95f485cab4c95405f40 ts=2026-09-06T02:00:55.2290000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi090326-4.stratalog.logdata.json[8743] _id=6a9cb0c1485cab4c9540557c ts=2026-09-06T00:16:02.0880000Z ~ wenyi090326-4.stratalog.logdata.json[8742] _id=6a9cb0c2485cab4c9540557e ts=2026-09-06T00:16:02.0890000Z`; `1ms: wenyi090326-4.stratalog.logdata.json[7997] _id=6a9cc4e6485cab4c95405b58 ts=2026-09-06T01:41:58.5000000Z ~ wenyi090326-4.stratalog.logdata.json[7996] _id=6a9cc4e6485cab4c95405b5a ts=2026-09-06T01:41:58.5010000Z`; `634ms: wenyi090326-4.stratalog.logdata.json[1179] _id=6a9d910a485cab4c954090c4 ts=2026-09-06T16:12:58.8000000Z ~ wenyi090326-4.stratalog.logdata.json[1176] _id=6a9d910b485cab4c954090ca ts=2026-09-06T16:12:59.4340000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 62 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `33ms: wenyi090326-4.stratalog.logdata.json[7502] _id=6a9cc960485cab4c95405f48 ts=2026-09-06T02:00:57.9990000Z ~ wenyi090326-4.stratalog.logdata.json[7501] _id=6a9cc960485cab4c95405f4a ts=2026-09-06T02:00:58.0320000Z`; `367ms: wenyi090326-4.stratalog.logdata.json[7501] _id=6a9cc960485cab4c95405f4a ts=2026-09-06T02:00:58.0320000Z ~ wenyi090326-4.stratalog.logdata.json[7500] _id=6a9cc960485cab4c95405f4c ts=2026-09-06T02:00:58.3990000Z`; `33ms: wenyi090326-4.stratalog.logdata.json[7500] _id=6a9cc960485cab4c95405f4c ts=2026-09-06T02:00:58.3990000Z ~ wenyi090326-4.stratalog.logdata.json[7499] _id=6a9cc960485cab4c95405f4e ts=2026-09-06T02:00:58.4320000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: wenyi090326-4.stratalog.logdata.json[2503] _id=6a9d8a39485cab4c95408664 ts=2026-09-06T15:43:54.0180000Z ~ wenyi090326-4.stratalog.logdata.json[2500] _id=6a9d8a39485cab4c9540866a ts=2026-09-06T15:43:54.0500000Z`; `31ms: wenyi090326-4.stratalog.logdata.json[496] _id=6a9d92eb485cab4c9540961a ts=2026-09-06T16:20:59.4790000Z ~ wenyi090326-4.stratalog.logdata.json[493] _id=6a9d92eb485cab4c95409620 ts=2026-09-06T16:20:59.5100000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `633ms: wenyi090326-4.stratalog.logdata.json[7786] _id=6a9cc7a6485cab4c95405cfe ts=2026-09-06T01:53:42.9050000Z ~ wenyi090326-4.stratalog.logdata.json[7782] _id=6a9cc7a7485cab4c95405d06 ts=2026-09-06T01:53:43.5380000Z`; `934ms: wenyi090326-4.stratalog.logdata.json[7770] _id=6a9cc7b0485cab4c95405d1e ts=2026-09-06T01:53:52.3420000Z ~ wenyi090326-4.stratalog.logdata.json[7764] _id=6a9cc7b1485cab4c95405d2a ts=2026-09-06T01:53:53.2760000Z`; `100ms: wenyi090326-4.stratalog.logdata.json[3053] _id=6a9d8725485cab4c95408216 ts=2026-09-06T15:30:46.4850000Z ~ wenyi090326-4.stratalog.logdata.json[3051] _id=6a9d8726485cab4c9540821a ts=2026-09-06T15:30:46.5850000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `434ms: wenyi090326-4.stratalog.logdata.json[2507] _id=6a9d8a2e485cab4c9540865c ts=2026-09-06T15:43:43.3430000Z ~ wenyi090326-4.stratalog.logdata.json[2506] _id=6a9d8a2f485cab4c9540865e ts=2026-09-06T15:43:43.7770000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: wenyi090326-4.stratalog.logdata.json[2384] _id=6a9d8b88485cab4c95408754 ts=2026-09-06T15:49:28.9030000Z ~ wenyi090326-4.stratalog.logdata.json[2383] _id=6a9d8b92485cab4c95408756 ts=2026-09-06T15:49:28.903Z`
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 12h 36m 
  - Evidence: 12h 36m: wenyi090326-4.stratalog.logdata.json[4095] _id=6a9cce39485cab4c954079d8 ts=2026-09-06T02:21:45.5410000Z -> wenyi090326-4.stratalog.logdata.json[4086] _id=6a9d7f84485cab4c95407a04 ts=2026-09-06T14:58:13.3030000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 12h 37m 
  - Evidence: 12h 37m: wenyi090326-4.stratalog.logdata.json[4103] _id=6a9cce1f485cab4c954079c8 ts=2026-09-06T02:21:19.7300000Z -> wenyi090326-4.stratalog.logdata.json[4063] _id=6a9d7f9f485cab4c95407a32 ts=2026-09-06T14:58:40.5510000Z; 1h 20m: wenyi090326-4.stratalog.logdata.json[8554] _id=6a9cb210485cab4c954056f8 ts=2026-09-06T00:21:36.2480000Z -> wenyi090326-4.stratalog.logdata.json[8003] _id=6a9cc4e2485cab4c95405b4c ts=2026-09-06T01:41:54.3340000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 442 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-4.stratalog.logdata.json[1856] _id=6a9d8d8f485cab4c95408b76 ts=2026-09-06T15:58:07.6410000Z -> wenyi090326-4.stratalog.logdata.json[1855] _id=6a9d8d8f485cab4c95408b78 ts=2026-09-06T15:58:07.6410000Z; 0ms: wenyi090326-4.stratalog.logdata.json[1862] _id=6a9d8d84485cab4c95408b68 ts=2026-09-06T15:57:57.1030000Z -> wenyi090326-4.stratalog.logdata.json[1863] _id=6a9d8d84485cab4c95408b6a ts=2026-09-06T15:57:57.1030000Z; 0ms: wenyi090326-4.stratalog.logdata.json[1866] _id=6a9d8d7c485cab4c95408b60 ts=2026-09-06T15:57:48.7660000Z -> wenyi090326-4.stratalog.logdata.json[1867] _id=6a9d8d7c485cab4c95408b62 ts=2026-09-06T15:57:48.7660000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 13h 35m 
  - Evidence: 13h 35m: wenyi090326-4.stratalog.logdata.json[7642] _id=6a9cc855485cab4c95405e1e ts=2026-09-06T01:56:37.5480000Z -> wenyi090326-4.stratalog.logdata.json[2931] _id=6a9d876e485cab4c9540830a ts=2026-09-06T15:31:58.6430000Z; 30m 35s: wenyi090326-4.stratalog.logdata.json[2931] _id=6a9d876e485cab4c9540830a ts=2026-09-06T15:31:58.6430000Z -> wenyi090326-4.stratalog.logdata.json[1710] _id=6a9d8e99485cab4c95408c9a ts=2026-09-06T16:02:33.8860000Z; 25m 51s: wenyi090326-4.stratalog.logdata.json[1710] _id=6a9d8e99485cab4c95408c9a ts=2026-09-06T16:02:33.8860000Z -> wenyi090326-4.stratalog.logdata.json[182] _id=6a9d94a9485cab4c9540988e ts=2026-09-06T16:28:25.4600000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 12h 36m 
  - Evidence: 12h 36m: wenyi090326-4.stratalog.logdata.json[4096] _id=6a9cce39485cab4c954079d6 ts=2026-09-06T02:21:45.5390000Z -> wenyi090326-4.stratalog.logdata.json[4070] _id=6a9d7f9a485cab4c95407a24 ts=2026-09-06T14:58:35.0780000Z; 1h 18m: wenyi090326-4.stratalog.logdata.json[8549] _id=6a9cb214485cab4c95405702 ts=2026-09-06T00:21:40.5980000Z -> wenyi090326-4.stratalog.logdata.json[8076] _id=6a9cc46b485cab4c95405ab8 ts=2026-09-06T01:39:55.1630000Z; 18m 10s: wenyi090326-4.stratalog.logdata.json[3540] _id=6a9d804e485cab4c95407e48 ts=2026-09-06T15:01:35.0800000Z -> wenyi090326-4.stratalog.logdata.json[3324] _id=6a9d8490485cab4c95407ff8 ts=2026-09-06T15:19:45.6550000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 93 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi090326-4.stratalog.logdata.json[863] _id=6a9d91a8485cab4c9540933a ts=2026-09-06T16:15:36.2610000Z -> wenyi090326-4.stratalog.logdata.json[864] _id=6a9d91a8485cab4c9540933c ts=2026-09-06T16:15:36.2610000Z; 0ms: wenyi090326-4.stratalog.logdata.json[972] _id=6a9d9175485cab4c95409262 ts=2026-09-06T16:14:45.5090000Z -> wenyi090326-4.stratalog.logdata.json[971] _id=6a9d9175485cab4c95409264 ts=2026-09-06T16:14:45.5090000Z; 1ms: wenyi090326-4.stratalog.logdata.json[1052] _id=6a9d914d485cab4c954091c2 ts=2026-09-06T16:14:05.7600000Z -> wenyi090326-4.stratalog.logdata.json[1051] _id=6a9d914d485cab4c954091c6 ts=2026-09-06T16:14:05.7610000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 12h 49m 
  - Evidence: 12h 49m: wenyi090326-4.stratalog.logdata.json[4530] _id=6a9ccb2c485cab4c95407670 ts=2026-09-06T02:08:45.0400000Z -> wenyi090326-4.stratalog.logdata.json[4084] _id=6a9d7f86485cab4c95407a08 ts=2026-09-06T14:58:15.3710000Z; 1h 22m: wenyi090326-4.stratalog.logdata.json[8619] _id=6a9cb16c485cab4c95405674 ts=2026-09-06T00:18:52.8530000Z -> wenyi090326-4.stratalog.logdata.json[8046] _id=6a9cc4c1485cab4c95405af6 ts=2026-09-06T01:41:21.8860000Z; 22m 37s: wenyi090326-4.stratalog.logdata.json[4084] _id=6a9d7f86485cab4c95407a08 ts=2026-09-06T14:58:15.3710000Z -> wenyi090326-4.stratalog.logdata.json[3264] _id=6a9d84d4485cab4c95408070 ts=2026-09-06T15:20:53.0060000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi090326-4.stratalog.logdata.json[566] _id=6a9d92ad485cab4c9540958e ts=2026-09-06T16:19:57.5200000Z -> wenyi090326-4.stratalog.logdata.json[565] _id=6a9d92ad485cab4c95409590 ts=2026-09-06T16:19:57.5200000Z; 0ms: wenyi090326-4.stratalog.logdata.json[597] _id=6a9d928f485cab4c95409550 ts=2026-09-06T16:19:28.0400000Z -> wenyi090326-4.stratalog.logdata.json[596] _id=6a9d928f485cab4c95409552 ts=2026-09-06T16:19:28.0400000Z; 1ms: wenyi090326-4.stratalog.logdata.json[7997] _id=6a9cc4e6485cab4c95405b58 ts=2026-09-06T01:41:58.5000000Z -> wenyi090326-4.stratalog.logdata.json[7996] _id=6a9cc4e6485cab4c95405b5a ts=2026-09-06T01:41:58.5010000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 12h 36m 
  - Evidence: 12h 36m: wenyi090326-4.stratalog.logdata.json[4097] _id=6a9cce35485cab4c954079d4 ts=2026-09-06T02:21:41.2040000Z -> wenyi090326-4.stratalog.logdata.json[4083] _id=6a9d7f8a485cab4c95407a0a ts=2026-09-06T14:58:18.9700000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 12h 51m 
  - Evidence: 12h 51m: wenyi090326-4.stratalog.logdata.json[4560] _id=6a9ccade485cab4c95407634 ts=2026-09-06T02:07:23.7370000Z -> wenyi090326-4.stratalog.logdata.json[4051] _id=6a9d7fa8485cab4c95407a48 ts=2026-09-06T14:58:49.5530000Z; 48m 17s: wenyi090326-4.stratalog.logdata.json[3543] _id=6a9d804b485cab4c95407e44 ts=2026-09-06T15:01:30.7440000Z -> wenyi090326-4.stratalog.logdata.json[2369] _id=6a9d8b9d485cab4c95408774 ts=2026-09-06T15:49:48.5070000Z; 19m 56s: wenyi090326-4.stratalog.logdata.json[2196] _id=6a9d8bbc485cab4c954088d4 ts=2026-09-06T15:50:19.3980000Z -> wenyi090326-4.stratalog.logdata.json[1620] _id=6a9d9067485cab4c95408d4e ts=2026-09-06T16:10:15.7720000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1966 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-4.stratalog.logdata.json[100] _id=6a9d956a485cab4c95409926 ts=2026-09-06T16:31:38.5270000Z -> wenyi090326-4.stratalog.logdata.json[102] _id=6a9d956a485cab4c95409928 ts=2026-09-06T16:31:38.5270000Z; 0ms: wenyi090326-4.stratalog.logdata.json[101] _id=6a9d956b485cab4c9540992c ts=2026-09-06T16:31:38.5270000Z -> wenyi090326-4.stratalog.logdata.json[105] _id=6a9d956b485cab4c9540992e ts=2026-09-06T16:31:38.5270000Z; 0ms: wenyi090326-4.stratalog.logdata.json[102] _id=6a9d956a485cab4c95409928 ts=2026-09-06T16:31:38.5270000Z -> wenyi090326-4.stratalog.logdata.json[103] _id=6a9d956a485cab4c9540992a ts=2026-09-06T16:31:38.5270000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 12h 49m 
  - Evidence: 12h 49m: wenyi090326-4.stratalog.logdata.json[4529] _id=6a9ccb2f485cab4c95407672 ts=2026-09-06T02:08:48.0070000Z -> wenyi090326-4.stratalog.logdata.json[4085] _id=6a9d7f86485cab4c95407a06 ts=2026-09-06T14:58:15.3700000Z; 50m 44s: wenyi090326-4.stratalog.logdata.json[4074] _id=6a9d7f94485cab4c95407a1c ts=2026-09-06T14:58:28.9460000Z -> wenyi090326-4.stratalog.logdata.json[2401] _id=6a9d8b79485cab4c95408730 ts=2026-09-06T15:49:13.7670000Z; 20m 34s: wenyi090326-4.stratalog.logdata.json[2388] _id=6a9d8b84485cab4c9540874a ts=2026-09-06T15:49:24.5640000Z -> wenyi090326-4.stratalog.logdata.json[1641] _id=6a9d9056485cab4c95408d28 ts=2026-09-06T16:09:59.2970000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 13h 2m 
  - Evidence: 13h 2m: wenyi090326-4.stratalog.logdata.json[4200] _id=6a9ccd0e485cab4c95407906 ts=2026-09-06T02:16:46.9730000Z -> wenyi090326-4.stratalog.logdata.json[3334] _id=6a9d8484485cab4c95407fe4 ts=2026-09-06T15:19:33.5510000Z; 22m 42s: wenyi090326-4.stratalog.logdata.json[2874] _id=6a9d8857485cab4c9540837e ts=2026-09-06T15:35:51.6820000Z -> wenyi090326-4.stratalog.logdata.json[1837] _id=6a9d8daa485cab4c95408b9c ts=2026-09-06T15:58:34.5960000Z; 16m 9s: wenyi090326-4.stratalog.logdata.json[3328] _id=6a9d848d485cab4c95407ff0 ts=2026-09-06T15:19:42.2200000Z -> wenyi090326-4.stratalog.logdata.json[2876] _id=6a9d8857485cab4c9540837a ts=2026-09-06T15:35:51.5480000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.033s shown 
  - Evidence: 4ms: wenyi090326-4.stratalog.logdata.json[4424] _id=6a9ccbea485cab4c95407746 ts=2026-09-06T02:11:54.7080000Z -> wenyi090326-4.stratalog.logdata.json[4420] _id=6a9ccbea485cab4c9540774e ts=2026-09-06T02:11:54.7120000Z; 31ms: wenyi090326-4.stratalog.logdata.json[4425] _id=6a9ccbea485cab4c95407744 ts=2026-09-06T02:11:54.6770000Z -> wenyi090326-4.stratalog.logdata.json[4424] _id=6a9ccbea485cab4c95407746 ts=2026-09-06T02:11:54.7080000Z; 33ms: wenyi090326-4.stratalog.logdata.json[4202] _id=6a9ccd0e485cab4c95407902 ts=2026-09-06T02:16:46.9400000Z -> wenyi090326-4.stratalog.logdata.json[4200] _id=6a9ccd0e485cab4c95407906 ts=2026-09-06T02:16:46.9730000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 13h 36m 
  - Evidence: 13h 36m: wenyi090326-4.stratalog.logdata.json[7733] _id=6a9cc7c9485cab4c95405d68 ts=2026-09-06T01:54:17.7210000Z -> wenyi090326-4.stratalog.logdata.json[3011] _id=6a9d8743485cab4c9540826a ts=2026-09-06T15:31:15.6660000Z; 37m 5s: wenyi090326-4.stratalog.logdata.json[2504] _id=6a9d8a39485cab4c95408662 ts=2026-09-06T15:43:54.0150000Z -> wenyi090326-4.stratalog.logdata.json[497] _id=6a9d92eb485cab4c95409618 ts=2026-09-06T16:20:59.4760000Z; 12m 38s: wenyi090326-4.stratalog.logdata.json[3011] _id=6a9d8743485cab4c9540826a ts=2026-09-06T15:31:15.6660000Z -> wenyi090326-4.stratalog.logdata.json[2504] _id=6a9d8a39485cab4c95408662 ts=2026-09-06T15:43:54.0150000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 13h 36m 
  - Evidence: 13h 36m: wenyi090326-4.stratalog.logdata.json[7732] _id=6a9cc7c9485cab4c95405d6a ts=2026-09-06T01:54:17.7240000Z -> wenyi090326-4.stratalog.logdata.json[3056] _id=6a9d8724485cab4c95408210 ts=2026-09-06T15:30:44.9880000Z; 36m 27s: wenyi090326-4.stratalog.logdata.json[2500] _id=6a9d8a39485cab4c9540866a ts=2026-09-06T15:43:54.0500000Z -> wenyi090326-4.stratalog.logdata.json[531] _id=6a9d92c5485cab4c954095d4 ts=2026-09-06T16:20:21.8920000Z; 10m 20s: wenyi090326-4.stratalog.logdata.json[3010] _id=6a9d8743485cab4c9540826c ts=2026-09-06T15:31:15.6690000Z -> wenyi090326-4.stratalog.logdata.json[2557] _id=6a9d89af485cab4c954085f8 ts=2026-09-06T15:41:36.1690000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.032s shown 
  - Evidence: 31ms: wenyi090326-4.stratalog.logdata.json[496] _id=6a9d92eb485cab4c9540961a ts=2026-09-06T16:20:59.4790000Z -> wenyi090326-4.stratalog.logdata.json[493] _id=6a9d92eb485cab4c95409620 ts=2026-09-06T16:20:59.5100000Z; 32ms: wenyi090326-4.stratalog.logdata.json[2503] _id=6a9d8a39485cab4c95408664 ts=2026-09-06T15:43:54.0180000Z -> wenyi090326-4.stratalog.logdata.json[2500] _id=6a9d8a39485cab4c9540866a ts=2026-09-06T15:43:54.0500000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 13h 36m 
  - Evidence: 13h 36m: wenyi090326-4.stratalog.logdata.json[7735] _id=6a9cc7c7485cab4c95405d64 ts=2026-09-06T01:54:15.4870000Z -> wenyi090326-4.stratalog.logdata.json[3053] _id=6a9d8725485cab4c95408216 ts=2026-09-06T15:30:46.4850000Z; 36m 41s: wenyi090326-4.stratalog.logdata.json[2509] _id=6a9d8a2c485cab4c95408658 ts=2026-09-06T15:43:41.3420000Z -> wenyi090326-4.stratalog.logdata.json[528] _id=6a9d92c6485cab4c954095da ts=2026-09-06T16:20:23.1590000Z; 10m 23s: wenyi090326-4.stratalog.logdata.json[3014] _id=6a9d8741485cab4c95408264 ts=2026-09-06T15:31:13.7980000Z -> wenyi090326-4.stratalog.logdata.json[2553] _id=6a9d89b1485cab4c95408600 ts=2026-09-06T15:41:37.7350000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 24 interval(s) ≤ 0.031s..0.033s shown 
  - Evidence: 31ms: wenyi090326-4.stratalog.logdata.json[7767] _id=6a9cc7b0485cab4c95405d24 ts=2026-09-06T01:53:52.6450000Z -> wenyi090326-4.stratalog.logdata.json[7766] _id=6a9cc7b0485cab4c95405d26 ts=2026-09-06T01:53:52.6760000Z; 32ms: wenyi090326-4.stratalog.logdata.json[7761] _id=6a9cc7b1485cab4c95405d30 ts=2026-09-06T01:53:53.8450000Z -> wenyi090326-4.stratalog.logdata.json[7760] _id=6a9cc7b1485cab4c95405d32 ts=2026-09-06T01:53:53.8770000Z; 33ms: wenyi090326-4.stratalog.logdata.json[2510] _id=6a9d8a2c485cab4c95408656 ts=2026-09-06T15:43:41.3090000Z -> wenyi090326-4.stratalog.logdata.json[2509] _id=6a9d8a2c485cab4c95408658 ts=2026-09-06T15:43:41.3420000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 13h 36m 
  - Evidence: 13h 36m: wenyi090326-4.stratalog.logdata.json[7734] _id=6a9cc7c8485cab4c95405d66 ts=2026-09-06T01:54:16.6210000Z -> wenyi090326-4.stratalog.logdata.json[3013] _id=6a9d8741485cab4c95408266 ts=2026-09-06T15:31:14.3980000Z; 12m 27s: wenyi090326-4.stratalog.logdata.json[3012] _id=6a9d8742485cab4c95408268 ts=2026-09-06T15:31:14.9980000Z -> wenyi090326-4.stratalog.logdata.json[2508] _id=6a9d8a2d485cab4c9540865a ts=2026-09-06T15:43:42.3760000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 13h 35m 
  - Evidence: 13h 35m: wenyi090326-4.stratalog.logdata.json[7641] _id=6a9cc89a485cab4c95405e22 ts=2026-09-06T01:57:46.9010000Z -> wenyi090326-4.stratalog.logdata.json[2929] _id=6a9d87a4485cab4c95408310 ts=2026-09-06T15:32:52.6980000Z; 1h 37m: wenyi090326-4.stratalog.logdata.json[8612] _id=6a9cb1c2485cab4c95405684 ts=2026-09-06T00:20:18.7820000Z -> wenyi090326-4.stratalog.logdata.json[7641] _id=6a9cc89a485cab4c95405e22 ts=2026-09-06T01:57:46.9010000Z; 23m 23s: wenyi090326-4.stratalog.logdata.json[1708] _id=6a9d8f41485cab4c95408ca0 ts=2026-09-06T16:05:21.5540000Z -> wenyi090326-4.stratalog.logdata.json[180] _id=6a9d94bc485cab4c95409894 ts=2026-09-06T16:28:44.7250000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 12h 41m 
  - Evidence: 12h 41m: wenyi090326-4.stratalog.logdata.json[4326] _id=6a9ccc63485cab4c9540780a ts=2026-09-06T02:13:55.8680000Z -> wenyi090326-4.stratalog.logdata.json[4093] _id=6a9d7ece485cab4c954079f6 ts=2026-09-06T14:55:11.2030000Z; 1h 20m: wenyi090326-4.stratalog.logdata.json[8613] _id=6a9cb170485cab4c95405680 ts=2026-09-06T00:18:56.5610000Z -> wenyi090326-4.stratalog.logdata.json[8078] _id=6a9cc466485cab4c95405ab4 ts=2026-09-06T01:39:50.9770000Z; 20m 42s: wenyi090326-4.stratalog.logdata.json[1695] _id=6a9d8f99485cab4c95408cbc ts=2026-09-06T16:06:49.3310000Z -> wenyi090326-4.stratalog.logdata.json[233] _id=6a9d9473485cab4c95409828 ts=2026-09-06T16:27:32.1920000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 11h 27m 
  - Evidence: 11h 27m: wenyi090326-4.stratalog.logdata.json[4094] _id=6a9cddc4485cab4c954079de ts=2026-09-06T03:28:03.8790000Z -> wenyi090326-4.stratalog.logdata.json[4092] _id=6a9d7ed1485cab4c954079f8 ts=2026-09-06T14:55:14.7830000Z; 1h 14m: wenyi090326-4.stratalog.logdata.json[4331] _id=6a9ccc50485cab4c95407800 ts=2026-09-06T02:13:36.3580000Z -> wenyi090326-4.stratalog.logdata.json[4094] _id=6a9cddc4485cab4c954079de ts=2026-09-06T03:28:03.8790000Z; 52m 12s: wenyi090326-4.stratalog.logdata.json[8614] _id=6a9cb16f485cab4c9540567e ts=2026-09-06T00:18:55.2830000Z -> wenyi090326-4.stratalog.logdata.json[8251] _id=6a9cbdab485cab4c9540595a ts=2026-09-06T01:11:08.1980000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-4.stratalog.logdata.json[2384] _id=6a9d8b88485cab4c95408754 ts=2026-09-06T15:49:28.9030000Z -> wenyi090326-4.stratalog.logdata.json[2383] _id=6a9d8b92485cab4c95408756 ts=2026-09-06T15:49:28.903Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 12h 39m 
  - Evidence: 12h 39m: wenyi090326-4.stratalog.logdata.json[4105] _id=6a9cce1f485cab4c954079c4 ts=2026-09-06T02:21:19.5630000Z -> wenyi090326-4.stratalog.logdata.json[3581] _id=6a9d8033485cab4c95407df6 ts=2026-09-06T15:01:08.8350000Z; 1h 21m: wenyi090326-4.stratalog.logdata.json[8562] _id=6a9cb20c485cab4c954056e8 ts=2026-09-06T00:21:33.0470000Z -> wenyi090326-4.stratalog.logdata.json[7981] _id=6a9cc510485cab4c95405b78 ts=2026-09-06T01:42:40.8180000Z; 21m 25s: wenyi090326-4.stratalog.logdata.json[3445] _id=6a9d823f485cab4c95407f06 ts=2026-09-06T15:09:52.6450000Z -> wenyi090326-4.stratalog.logdata.json[3006] _id=6a9d8745485cab4c95408274 ts=2026-09-06T15:31:17.8910000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: wenyi090326-4.stratalog.logdata.json[1044] _id=6a9d9151485cab4c954091d2 ts=2026-09-06T16:14:10.1630000Z -> wenyi090326-4.stratalog.logdata.json[1043] _id=6a9d9151485cab4c954091d4 ts=2026-09-06T16:14:10.1640000Z; 1ms: wenyi090326-4.stratalog.logdata.json[1170] _id=6a9d910e485cab4c954090d6 ts=2026-09-06T16:13:03.0360000Z -> wenyi090326-4.stratalog.logdata.json[1169] _id=6a9d910e485cab4c954090d8 ts=2026-09-06T16:13:03.0370000Z; 1ms: wenyi090326-4.stratalog.logdata.json[1276] _id=6a9d90d9485cab4c95409002 ts=2026-09-06T16:12:09.4480000Z -> wenyi090326-4.stratalog.logdata.json[1275] _id=6a9d90d9485cab4c95409004 ts=2026-09-06T16:12:09.4490000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7806] _id=6a9cc790485cab4c95405cd6 ts=2026-09-06T01:53:20.5980000Z`; `wenyi090326-4.stratalog.logdata.json[7724] _id=6a9cc7ce485cab4c95405d7a ts=2026-09-06T01:54:22.6280000Z`; `wenyi090326-4.stratalog.logdata.json[4146] _id=6a9ccdd8485cab4c95407972 ts=2026-09-06T02:20:08.6970000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 17 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7290] _id=6a9cc973485cab4c954060ee ts=2026-09-06T02:01:21.6430000Z`; `wenyi090326-4.stratalog.logdata.json[6596] _id=6a9cc9d4485cab4c9540665a ts=2026-09-06T02:02:58.5520000Z`; `wenyi090326-4.stratalog.logdata.json[6521] _id=6a9cc9dc485cab4c954066ee ts=2026-09-06T02:03:07.4880000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 30 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7569] _id=6a9cc95c485cab4c95405ee8 ts=2026-09-06T02:00:25.9860000Z`; `wenyi090326-4.stratalog.logdata.json[7568] _id=6a9cc95c485cab4c95405eec ts=2026-09-06T02:00:26.0500000Z`; `wenyi090326-4.stratalog.logdata.json[7474] _id=6a9cc962485cab4c95405f7a ts=2026-09-06T02:01:02.5320000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi090326-4.stratalog.logdata.json[2500] _id=6a9d8a39485cab4c9540866a ts=2026-09-06T15:43:54.0500000Z`; `wenyi090326-4.stratalog.logdata.json[493] _id=6a9d92eb485cab4c95409620 ts=2026-09-06T16:20:59.5100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `wenyi090326-4.stratalog.logdata.json[179] _id=6a9d94be485cab4c95409896 ts=2026-09-06T16:28:47.1030000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `wenyi090326-4.stratalog.logdata.json[2375] _id=6a9d8b9b485cab4c95408768 ts=2026-09-06T15:49:46.9210000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `wenyi090326-4.stratalog.logdata.json[8815] _id=6a9d8b87485cab4c95408752 ts=?`; `wenyi090326-4.stratalog.logdata.json[8816] _id=6a9d8f8f485cab4c95408cb8 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 159 occurrence(s) 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7337] _id=6a9cc96e485cab4c95406088 ts=2026-09-06T02:01:17.0400000Z`; `wenyi090326-4.stratalog.logdata.json[7292] _id=6a9cc972485cab4c954060e4 ts=2026-09-06T02:01:21.5760000Z`; `wenyi090326-4.stratalog.logdata.json[7220] _id=6a9cc979485cab4c95406170 ts=2026-09-06T02:01:27.8770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 513 occurrence(s) 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7551] _id=6a9cc95d485cab4c95405f0c ts=2026-09-06T02:00:26.2190000Z`; `wenyi090326-4.stratalog.logdata.json[7552] _id=6a9cc95e485cab4c95405f12 ts=2026-09-06T02:00:26.2190000Z`; `wenyi090326-4.stratalog.logdata.json[7547] _id=6a9cc95e485cab4c95405f18 ts=2026-09-06T02:00:26.3190000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `wenyi090326-4.stratalog.logdata.json[2506] _id=6a9d8a2f485cab4c9540865e ts=2026-09-06T15:43:43.7770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 298 start, 294 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 38 unmatched 'BecameCameraCentered' (totals: 552 open, 531 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 83 unmatched 'BecameVisible' (totals: 1107 open, 1054 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 7 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 35 start, 29 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 475 of 8814 adjacent _id pairs reverse in client time; worst 35.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi090326-4.stratalog.logdata.json[7488] _id=6a9cc95d485cab4c95405ef8 ts=2026-09-06T02:01:01.1320000Z`; `wenyi090326-4.stratalog.logdata.json[7561] _id=6a9cc95d485cab4c95405efa ts=2026-09-06T02:00:26.0850000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.11s, min -36.57s, max +0.84s over 8815 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-03-26-4.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Playthrough by one tester on 2026-09-06 (log shows EndOfUnit for units 1-4 only).; Unit 5 barely started: ~3 minutes / 180 records in 'Unit 5 Dev - Dungeon' at the very end of the session (16:28-16:32Z), no 'Unit 5 Dev' scene records and no Unit 5 EndOfUnit.; First ~4 minutes (202 records, Unit 1 only, 00:14-00:18Z) were logged on the older build 20260721-11840 before the tester switched to 20260902-12353; Unit 1 was completed on the new build.; Debug menu opened briefly (DebugMenuStateChanged toggle in Unit 3; no debug actions logged). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `WaterChamberEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3244 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2768); Unit 4 Dev (236); Unit 3 Dungeon Dev (126); Unit 5 Dev - Dungeon (114)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.67s, n=3243)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3244/3244 records)
    "BecameVisible"  x1107
    "BecameInvisible"  x1054
    "BecameCameraCentered"  x552
    "BecameCameraUncentered"  x531
data.pieceId  (string, 3244/3244 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3244/3244 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2033 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (813); Unit 4 Dev - Dungeon (377); Unit 3 Dev (227); Unit 1 Dev (205); Unit 3 Dungeon Dev (188); Unit 4 Dev (151); Unit 4 Dev - Anderson Base (39); Unit 5 Dev - Dungeon (33)
- **Intervals:** median 0.40s (p5 0.07s / p95 11.72s, n=2032)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2033/2033 records)
    "pressed"  x2033
data.actionType  (string, 2033/2033 records)
    "Move"  x1494
    "Interact"  x310
    "Sprint"  x167
    "Ascend"  x32
    "Jump"  x11
    "Hoverboard"  x9
    "Descend"  x8
    "Pause"  x1
    "ToggleDebug"  x1
data.key  (string, 2033/2033 records)
    "w"  x568
    "a"  x323
    "s"  x314
    "leftButton"  x302
    "d"  x289
    "leftShift"  x175
    "space"  x27
    "e"  x24
    "h"  x9
    "backquote"  x1
    "tab"  x1
data.playerOrDrone  (string, 2033/2033 records)
    "Player"  x1778
    "Drone"  x255
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1655 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (560); Unit 3 Dev (278); Unit 1 Dev (271); Unit 4 Dev (244); Unit 3 Dungeon Dev (115); Unit 4 Dev - Dungeon (108); Unit 4 Dev - Anderson Base (69); Unit 5 Dev - Dungeon (10)
- **eventKey:** present on 1063 of 1655 records
- **Intervals:** median 0.67s (p5 0.00s / p95 17.16s, n=1654)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1063; [conversationId, dialogueEventType] x592
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1655/1655 records)
    numeric range 8 .. 114 (45 unique)
data.dialogueEventType  (string, 1655/1655 records)
    "DialogueNodeEvent"  x1063
    "DialogueStartEvent"  x298
    "DialogueFinishEvent"  x294
data.nodeId  (number, 1063/1655 records)
    numeric range 0 .. 290 (216 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1280 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 1 Dev (604); Unit 2 Prod (Refactor) (346); Unit 3 Dev (129); Unit 4 Dev (90); Unit 3 Dungeon Dev (43); Unit 4 Dev - Dungeon (31); Unit 5 Dev - Dungeon (20); Unit 4 Dev - Anderson Base (17)
- **Intervals:** median 10.01s (p5 9.97s / p95 10.01s, n=1269)
- **Fields under `data`:**

```text
data.position  (object, 1280/1280 records)
data.position.x  (number, 1280/1280 records)
    numeric range -656.07 .. 1555.75 (307 unique)
data.position.y  (number, 1280/1280 records)
    numeric range -114.157 .. 155.172 (262 unique)
data.position.z  (number, 1280/1280 records)
    numeric range -1027.58 .. 2213.43 (307 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 253 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (111); Unit 4 Dev - Dungeon (59); Unit 3 Dungeon Dev (23); Unit 1 Dev (22); Unit 4 Dev (17); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 3.80s (p5 1.41s / p95 174.10s, n=252)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 253/253 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 253/253 records)
    95 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 125 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (37); Unit 3 Dev (33); Unit 1 Dev (28); Unit 4 Dev - Anderson Base (27)
- **Intervals:** median 0.35s (p5 0.03s / p95 11.12s, n=124)
- **Fields under `data`:**

```text
data.actionType  (string, 125/125 records)
    "argumentationNodeHoverEnd"  x53
    "argumentationNodeHoverStart"  x53
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 125/125 records)
    "Unit 2 – Watershed"  x37
    "Unit 3 - Pollution Upstream"  x33
    "Unit 4 - Flooding"  x27
    "Unit 1 - Argumentation Tutorial"  x19
    "Unit 1 - Freshwater"  x9
data.nodeName  (string, 125/125 records)
    "I"  x23
    "1"  x21
    "A"  x19
    "B"  x14
    "II"  x14
    "2"  x7
    "C"  x7
    "D"  x7
    "3"  x6
    "4"  x4
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 64 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (19); Unit 2 Prod (Refactor) (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (1)
- **eventKey:** present on 64 of 64 records
- **Intervals:** median 62.36s (p5 0.00s / p95 569.94s, n=63)
- **`data` key-set variants:** [questEventType, questID, questName] x35; [questEventType, questID, questName, questSuccessOrFailure] x29
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 64/64 records)
    "questActiveEvent"  x35
    "questFinishEvent"  x29
data.questID  (string, 64/64 records)
    28 unique values (see csv/event_unique_values.csv)
data.questName  (string, 64/64 records)
    28 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 29/64 records)
    "Succeeded"  x29
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 38 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (14); Unit 2 Prod (Refactor) (12); Unit 3 Dev (12)
- **Intervals:** median 0.53s (p5 0.17s / p95 1596.75s, n=37)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x30; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/38 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/38 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 30/38 records)
    "RightDrag"  x18
    "LeftDrag"  x12
data.currentSoilType  (string, 30/38 records)
    "SAND"  x6
    "SANDGRAVEL"  x6
    "CLAY"  x5
    "CLAYSAND"  x5
    "CLAYROCK"  x4
    "GRAVEL"  x3
    "BEDROCK"  x1
data.isCorrectSelection  (string, 30/38 records)
    "false"  x24
    "true"  x6
data.waterLevelStatus  (string, 30/38 records)
    "TooHigh"  x12
    "Proper"  x9
    "TooLow"  x9
data.waterRetentionChange  (string, 30/38 records)
    "Decrease"  x15
    "Increase"  x9
    "NoChange"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowUnfocusEvent` — 25 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (6); Unit 3 Dev (4); Unit 4 Dev (2)
- **Intervals:** median 405.53s (p5 5.61s / p95 4267.33s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameWindowFocusEvent` — 24 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (6); Unit 3 Dev (3); Unit 4 Dev (2)
- **Intervals:** median 369.55s (p5 12.29s / p95 4493.26s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TopographicMapEvent` — 22 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (4)
- **Intervals:** median 2.77s (p5 0.03s / p95 1362.91s, n=21)
- **`data` key-set variants:** [actionType, featureUsed] x16; [actionType, featureUsed, legendName] x3; [actionType, featureUsed, location] x3
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "MapCloseEvent"  x8
    "MapOpenEvent"  x8
    "Selected"  x2
    "WaypointSetEvent"  x2
    "Unselected"  x1
    "WaypointResetEvent"  x1
data.featureUsed  (string, 22/22 records)
    "Map"  x16
    "Legend"  x3
    "Waypoint"  x3
data.legendName  (string, 3/22 records)
    "0 ft"  x2
    "90 ft"  x1
data.location  (object, 3/22 records)
data.location.x  (number, 3/22 records)
    2 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 3/22 records)
    2 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 3/22 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 30.68s (p5 0.03s / p95 25587.55s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 0.97s (p5 0.48s / p95 34536.66s, n=7)
- **Open findings:** 1 — see sections 5-8
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
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 7 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (7)
- **Intervals:** median 1204.88s (p5 491.55s / p95 38141.38s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    true  x7
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.44s (p5 1.40s / p95 17.35s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationAnswerEvent` — 5 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1491.90s (p5 132.21s / p95 41999.07s, n=4)
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "submitAnswerEvent"  x5
data.answerSubmitted  (string, 5/5 records)
    "A,1,I"  x2
    "A,1,II"  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 5 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (5)
- **Intervals:** median 31.40s (p5 9.22s / p95 54.31s, n=4)
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "ChangeCanister"  x5
data.canisterType  (string, 5/5 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 5/5 records)
    "5"  x3
    "3"  x1
    "4"  x1
data.machine  (string, 5/5 records)
    "1"  x4
    "2"  x1
data.row  (string, 5/5 records)
    "TopRow"  x4
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 1835.24s (p5 1579.94s / p95 44212.51s, n=3)
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `DEBUGMenu` — 2 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 2.47s (p5 2.47s / p95 2.47s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "DebugMenuStateChanged"  x2
data.isOpened  (bool, 2/2 records)
    false  x1
    true  x1
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 45387.76s (p5 45387.76s / p95 45387.76s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a8f363e:wasm-function[73291]:0x1563591
    at wasm://wasm/0a8f363e:wasm-function[73290]:0x15634d3
    at wasm://wasm/0a8f363e:wasm-function[59956]:0x11d11ac
    at wasm://wasm/0a8f363e:wasm-function[59957]:0x11d11f3
    at wasm://wasm/0a8f363e:wasm-function[80769]:0x16e045b
    at wasm://wasm/0a8f363e:wasm-function[83409]:0x1717ed2
    at wasm://wasm/0a8f363e:wasm-function[110254]:0x259781d
    at invoke_iiii (blob:https://dev.adroit.games/e47e2f65-11a9-44ff-b9a7-658d59ae7510:9:474038)
    at wasm://wasm/0a8f363e:wasm-function[83394]:0x1717572
    at wasm://wasm/0a8f363e:wasm-function[1942]:0xf57d9
    at wasm://wasm/0a8f363e:wasm-function[109911]:0x255e832
    at wasm://wasm/0a8f363e:wasm-function[106216]:0x24af5b6
    at wasm://wasm/0a8f363e:wasm-function[87318]:0x190fbf2
    at wasm://wasm/0a8f363e:wasm-function[102624]:0x2291c25
    at wasm://wasm/0a8f363e:wasm-function[105694]:0x245a569
    at wasm://wasm/0a8f363e:wasm-function[105709]:0x245ab0e
    at wasm://wasm/0a8f363e:wasm-function[104647]:0x23edaa7
    at wasm://wasm/0a8f363e:wasm-function[103118]:0x22d15fa
    at wasm://wasm/0a8f363e:wasm-function[86343]:0x18ae5bb
    at wasm://wasm/0a8f363e:wasm-function[103047]:0x22c2f96
    at wasm://wasm/0a8f363e:wasm-function[108883]:0x24f4871
    at wasm://wasm/0a8f363e:wasm-function[3934]:0x15e018
    at wasm://wasm/0a8f363e:wasm-function[110265]:0x25978c4
    at invoke_viiii (blob:https://dev.adroit.games/e47e2f65-11a9-44ff-b9a7-658d59ae7510:9:474821)
    at wasm://wasm/0a8f363e:wasm-function[30556]:0x8ef73a
    at wasm://wasm/0a8f363e:wasm-function[110258]:0x2597858
    at invoke_viii (blob:https://dev.adroit.games/e47e2f65-11a9-44ff-b9a7-658d59ae7510:9:474188)
    at wasm://wasm/0a8f363e:wasm-function[30543]:0x8e931b
    at wasm://wasm/0a8f363e:wasm-function[110258]:0x2597858
    at invoke_viii (blob:https://dev.adroit.games/e47e2f65-11a9-44ff-b9a7-658d59ae7510:9:474188)
    at wasm://wasm/0a8f363e:wasm-function[30537]:0x8e66c3
    at wasm://wasm/0a8f363e:wasm-function[3753]:0x15846a
    at wasm://wasm/0a8f363e:wasm-function[110265]:0x25978c4
    at invoke_viiii (blob:https://dev.adroit.games/e47e2f65-11a9-44ff-b9a7-658d59ae7510:9:474821)
    at wasm://wasm/0a8f363e:wasm-function[3789]:0x159d6b
    at wasm://wasm/0a8f363e:wasm-function[82090]:0x16fd557
    at wasm://wasm/0a8f363e:wasm-function[83409]:0x1717ed2
    at wasm://wasm/0a8f363e:wasm-function[110254]:0x259781d
    at invoke_iiii (blob:https://dev.adroit.games/e47e2f65-11a9-44ff-b9a7-658d59ae7510:9:474038)
    at wasm://wasm/0a8f363e:wasm-function[83394]:0x1717572
    at wasm://wasm/0a8f363e:wasm-function[1942]:0xf57d9
    at wasm://wasm/0a8f363e:wasm-function[109911]:0x255e832
    at wasm://wasm/0a8f363e:wasm-function[106216]:0x24af5b6
    at wasm://wasm/0a8f363e:wasm-function[106219]:0x24af67c
    at wasm://wasm/0a8f363e:wasm-function[84651]:0x1792b0b
    at wasm://wasm/0a8f363e:wasm-function[85941]:0x185d320
    at wasm://wasm/0a8f363e:wasm-function[103890]:0x234f7d5
    at wasm://wasm/0a8f363e:wasm-function[105636]:0x2457674
    at wasm://wasm/0a8f363e:wasm-function[105636]:0x24576e9
    at wasm://wasm/0a8f363e:wasm-function[109989]:0x2566c65"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit3"  x1
    "unit4"  x1
data.workspace  (string, 2/2 records)
    "dev"  x2
```

Raw examples: `event_examples.json` -> `crash`.

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

Baseline: snapshot build-log-qa\reports\08-31-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `WaterChamberEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DaniEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 08-31-26 but absent now
- `TerasGardenBox` : baseline field(s) absent this build
- `WaterChamberEvent` : event type present in baseline 08-31-26 but absent now
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open
- `chatEvent` actionType: chat open/close: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "Unselected" (1x); "WaypointResetEvent" (1x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (3x); "Waypoint" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*