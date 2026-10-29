# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22a
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f22a.jsonl
- **Records:** 16646 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f22a
- **Time span:** 2026-09-23T13:56:10.824000+00:00 .. 2026-10-07T14:31:19.408000+00:00 (336h 35m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 16646 records, 8 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 94 INFO, 2 NOT_TESTED, 77 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5620 | 33.76 | 1 | 6 | 0 | 2026-09-23T13:56:28.508000+00:00 | 2026-10-07T14:30:07.901000+00:00 | 336h 33m |
| PuzzlePieceVisibleEvent | 5595 | 33.61 | 1 | 3 | 0 | 2026-09-25T14:14:25.773000+00:00 | 2026-10-07T14:27:40.842000+00:00 | 288h 13m |
| PlayerPositionEvent | 2663 | 16.0 | 1 | 6 | 0 | 2026-09-23T13:56:23.291000+00:00 | 2026-10-07T14:31:18.370000+00:00 | 336h 34m |
| DialogueEvent | 1709 | 10.27 | 1 | 6 | 1100 | 2026-09-23T13:56:45.203000+00:00 | 2026-10-07T14:30:52.295000+00:00 | 336h 34m |
| ObjectInterEvent | 302 | 1.81 | 1 | 6 | 0 | 2026-09-23T14:23:34.504000+00:00 | 2026-10-07T14:30:08.974000+00:00 | 336h 6m |
| argumentationNodeEvent | 154 | 0.93 | 1 | 2 | 0 | 2026-09-24T14:14:25.640000+00:00 | 2026-10-01T14:19:15.438000+00:00 | 168h 4m |
| DaniEvent | 114 | 0.68 | 1 | 4 | 0 | 2026-09-23T14:00:45.252000+00:00 | 2026-10-05T16:10:29.644000+00:00 | 290h 9m |
| Soil Key Puzzle | 110 | 0.66 | 1 | 3 | 0 | 2026-09-25T14:23:35.719000+00:00 | 2026-10-07T14:17:22.877000+00:00 | 287h 53m |
| TopographicMapEvent | 79 | 0.47 | 1 | 4 | 0 | 2026-09-25T14:15:23.715000+00:00 | 2026-10-07T14:13:46.995000+00:00 | 287h 58m |
| questEvent | 79 | 0.47 | 1 | 6 | 79 | 2026-09-23T13:56:45.184000+00:00 | 2026-10-07T14:06:28.469000+00:00 | 336h 9m |
| gameWindowFocusEvent | 61 | 0.37 | 1 | 8 | 0 | 2026-09-23T13:56:10.824000+00:00 | 2026-10-07T14:06:15.471000+00:00 | 336h 10m |
| gameWindowUnfocusEvent | 51 | 0.31 | 1 | 7 | 0 | 2026-09-23T14:01:21.192000+00:00 | 2026-10-07T14:31:19.408000+00:00 | 336h 29m |
| DEBUGMenu | 34 | 0.2 | 1 | 7 | 0 | 2026-09-23T13:56:23.279000+00:00 | 2026-10-07T14:28:18.231000+00:00 | 336h 31m |
| gameStartEvent | 25 | 0.15 | 1 | 1 | 0 | 2026-09-23T13:56:10.824000+00:00 | 2026-10-07T14:06:15.471000+00:00 | 336h 10m |
| argumentationAnswerEvent | 15 | 0.09 | 1 | 2 | 0 | 2026-09-24T14:13:51.542000+00:00 | 2026-10-01T14:19:16.336000+00:00 | 168h 5m |
| argumentationEvent | 14 | 0.08 | 1 | 2 | 0 | 2026-09-24T14:12:05.904000+00:00 | 2026-10-01T14:19:16.384000+00:00 | 168h 7m |
| soilMachine | 9 | 0.05 | 1 | 1 | 0 | 2026-10-06T14:20:49.622000+00:00 | 2026-10-06T14:21:14.121000+00:00 | 24.5s |
| crash | 8 | 0.05 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-25T14:04:56.104000+00:00 | 2026-10-05T13:52:22.967000+00:00 | 239h 47m |
| argumentationToolEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-09-24T14:13:54.200000+00:00 | 2026-09-25T14:01:28.443000+00:00 | 23h 47m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863246.863s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.545s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.951s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.585s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 85654.243s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6837.243s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 389.34s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 326.325s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 0.651s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 114 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; backquote; ctrl; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,1,; A,3,I 
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
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 25 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 20 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[973] _id=6ab52ad9485cab4c95519b01 ts=2026-09-24T13:51:21.8600000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1054] _id=6ab52c58485cab4c9551b793 ts=2026-09-24T13:57:44.3580000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1081] _id=6ab52cb1485cab4c9551bb01 ts=2026-09-24T13:59:13.8550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[5270] _id=6abbc356485cab4c957e0d61 ts=2026-09-29T13:55:32.8130000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[32] _id=6ab3da7a485cab4c954ce3ef ts=2026-09-23T13:56:10.8240000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[361] _id=6ab3ddc6485cab4c954cfed1 ts=2026-09-23T14:10:16.7130000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[857] _id=6ab52973485cab4c95517001 ts=2026-09-24T13:45:24.4550000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 61 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 61} 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[33] _id=6ab3da7a485cab4c954ce3eb ts=2026-09-23T13:56:10.8240000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[309] _id=6ab3dbb4485cab4c954ced01 ts=2026-09-23T14:01:24.4920000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[318] _id=6ab3dbbf485cab4c954ced67 ts=2026-09-23T14:01:35.9250000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 51 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 51} 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[312] _id=6ab3dbb1485cab4c954cece3 ts=2026-09-23T14:01:21.1920000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[317] _id=6ab3dbbd485cab4c954ced4f ts=2026-09-23T14:01:32.9580000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[319] _id=6ab3dbc2485cab4c954ced6f ts=2026-09-23T14:01:38.0360000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5619 | 0.0 | 0.931 | 215.629 | 11.342 | 336846.776 | 0.28 | 243 | 16 |
| PuzzlePieceVisibleEvent | 5594 | 0.0 | 0.033 | 185.484 | 1.376 | 339228.49 | 0.32 | 3424 | 9 |
| PlayerPositionEvent | 2654 | 9.573 | 10.0 | 456.485 | 10.088 | 336283.476 | 0.13 | 0 | 15 |
| DialogueEvent | 1708 | 0.001 | 4.89 | 709.395 | 65.345 | 336767.394 | 0.08 | 455 | 15 |
| ObjectInterEvent | 301 | 0.006 | 12.545 | 4019.915 | 428.043 | 337312.804 | 0.01 | 1 | 12 |
| argumentationNodeEvent | 153 | 0.016 | 0.376 | 3954.835 | 5.826 | 518442.854 | 0.02 | 31 | 3 |
| DaniEvent | 113 | 0.006 | 0.31 | 9244.11 | 34.329 | 432478.11 | 0.01 | 4 | 5 |
| Soil Key Puzzle | 109 | 0.146 | 0.981 | 9508.506 | 11.432 | 343923.483 | 0.01 | 0 | 4 |
| TopographicMapEvent | 78 | 0.594 | 6.951 | 13291.068 | 86702.655 | 345587.847 | 0.0 | 0 | 8 |
| questEvent | 78 | 0.0 | 326.325 | 15515.17 | 84425.269 | 336906.707 | 0.0 | 11 | 26 |
| gameWindowFocusEvent | 60 | 1.364 | 176.591 | 20170.077 | 86228.385 | 338700.261 | 0.0 | 0 | 21 |
| gameWindowUnfocusEvent | 50 | 0.381 | 389.34 | 24227.964 | 86823.099 | 336253.442 | 0.0 | 0 | 23 |
| DEBUGMenu | 33 | 2.729 | 1314.803 | 36712.574 | 155373.864 | 337599.278 | 0.0 | 0 | 24 |
| gameStartEvent | 24 | 144.953 | 6837.243 | 50425.194 | 232335.599 | 338726.691 | 0.0 | 0 | 19 |
| argumentationAnswerEvent | 14 | 0.253 | 7.585 | 43223.2 | 236970.148 | 518447.066 | 0.0 | 0 | 3 |
| argumentationEvent | 13 | 0.03 | 51.142 | 46556.191 | 258605.344 | 518432.253 | 0.0 | 1 | 3 |
| soilMachine | 8 | 0.368 | 0.651 | 3.062 | 12.994 | 18.904 | 19.59 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 863246.863 | 863246.863 | 863246.863 | 863246.863 | 863246.863 | 0.0 | 0 | 1 |
| argumentationToolEvent | 1 | 85654.243 | 85654.243 | 85654.243 | 85654.243 | 85654.243 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[9520] _id=6abe6dde485cab4c95a87f33 ts=2026-10-01T14:27:42.7610000Z == 6aa4140b41b41dbac0c7f22a.jsonl[9521] _id=6abe6ddf485cab4c95a87f39 ts=2026-10-01T14:27:42.7610000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 183 group(s), 234 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1953] _id=6ab6823a485cab4c95560814 ts=2026-09-25T14:14:26.3940000Z == 6aa4140b41b41dbac0c7f22a.jsonl[1954] _id=6ab6823a485cab4c95560818 ts=2026-09-25T14:14:26.3940000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2012] _id=6ab6823c485cab4c95560884 ts=2026-09-25T14:14:26.6870000Z == 6aa4140b41b41dbac0c7f22a.jsonl[1984] _id=6ab6823c485cab4c95560888 ts=2026-09-25T14:14:26.6870000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2024] _id=6ab6823d485cab4c955608c8 ts=2026-09-25T14:14:26.8820000Z == 6aa4140b41b41dbac0c7f22a.jsonl[1969] _id=6ab6823d485cab4c955608cd ts=2026-09-25T14:14:26.8820000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[330] _id=6ab3dbee485cab4c954cef19 ts=? == 6aa4140b41b41dbac0c7f22a.jsonl[358] _id=6ab3dddb485cab4c954cff39 ts=?`; `6aa4140b41b41dbac0c7f22a.jsonl[9069] _id=6abe69c3485cab4c95a7a4e1 ts=? == 6aa4140b41b41dbac0c7f22a.jsonl[11031] _id=6ac3aab5de269131f9a9d16e ts=?`; `6aa4140b41b41dbac0c7f22a.jsonl[14493] _id=6ac51d7dde269131f9b4e51b ts=? == 6aa4140b41b41dbac0c7f22a.jsonl[14559] _id=6ac644ddde269131f9b8b7f6 ts=?`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 75 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `475ms: 6aa4140b41b41dbac0c7f22a.jsonl[7231] _id=6abd2eb6485cab4c958cf38f ts=2026-09-30T15:45:58.7740000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[7242] _id=6abd2eb9485cab4c958cf3f8 ts=2026-09-30T15:45:59.2490000Z`; `857ms: 6aa4140b41b41dbac0c7f22a.jsonl[7238] _id=6abd2eb9485cab4c958cf406 ts=2026-09-30T15:45:59.6250000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[7229] _id=6abd2eb9485cab4c958cf418 ts=2026-09-30T15:46:00.4820000Z`; `957ms: 6aa4140b41b41dbac0c7f22a.jsonl[7229] _id=6abd2eb9485cab4c958cf418 ts=2026-09-30T15:46:00.4820000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[7244] _id=6abd2eba485cab4c958cf448 ts=2026-09-30T15:46:01.4390000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4140b41b41dbac0c7f22a.jsonl[914] _id=6ab52a1d485cab4c95518bd3 ts=2026-09-24T13:48:14.9440000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[915] _id=6ab52a1d485cab4c95518bd5 ts=2026-09-24T13:48:14.9500000Z`; `532ms: 6aa4140b41b41dbac0c7f22a.jsonl[4640] _id=6aba78f4485cab4c9568da5d ts=2026-09-28T14:25:56.4150000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[4671] _id=6aba78f5485cab4c9568da71 ts=2026-09-28T14:25:56.9470000Z`; `257ms: 6aa4140b41b41dbac0c7f22a.jsonl[4671] _id=6aba78f5485cab4c9568da71 ts=2026-09-28T14:25:56.9470000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[4672] _id=6aba78f5485cab4c9568da7a ts=2026-09-28T14:25:57.2040000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 734 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `41ms: 6aa4140b41b41dbac0c7f22a.jsonl[1988] _id=6ab6823c485cab4c95560898 ts=2026-09-25T14:14:26.7120000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[2019] _id=6ab6823c485cab4c9556089a ts=2026-09-25T14:14:26.7530000Z`; `1ms: 6aa4140b41b41dbac0c7f22a.jsonl[1886] _id=6ab6823e485cab4c95560904 ts=2026-09-25T14:14:26.9590000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[2017] _id=6ab6823e485cab4c9556090a ts=2026-09-25T14:14:26.9600000Z`; `17ms: 6aa4140b41b41dbac0c7f22a.jsonl[1806] _id=6ab681c5485cab4c9555f2ce ts=2026-09-25T14:14:28.0810000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1807] _id=6ab681c5485cab4c9555f2d2 ts=2026-09-25T14:14:28.0980000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `863ms: 6aa4140b41b41dbac0c7f22a.jsonl[1520] _id=6ab67ebb485cab4c9555bd46 ts=2026-09-25T14:01:31.3730000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1521] _id=6ab67ebc485cab4c9555bd52 ts=2026-09-25T14:01:32.2360000Z`; `287ms: 6aa4140b41b41dbac0c7f22a.jsonl[1521] _id=6ab67ebc485cab4c9555bd52 ts=2026-09-25T14:01:32.2360000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1511] _id=6ab67ebc485cab4c9555bd56 ts=2026-09-25T14:01:32.5230000Z`; `286ms: 6aa4140b41b41dbac0c7f22a.jsonl[1511] _id=6ab67ebc485cab4c9555bd56 ts=2026-09-25T14:01:32.5230000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1512] _id=6ab67ebc485cab4c9555bd58 ts=2026-09-25T14:01:32.8090000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `60ms: 6aa4140b41b41dbac0c7f22a.jsonl[9057] _id=6abe681b485cab4c95a792c9 ts=2026-10-01T14:03:07.1100000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[9059] _id=6abe681b485cab4c95a792cf ts=2026-10-01T14:03:07.1700000Z`; `30ms: 6aa4140b41b41dbac0c7f22a.jsonl[9281] _id=6abe6be4485cab4c95a7fec1 ts=2026-10-01T14:19:16.3540000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[9279] _id=6abe6be4485cab4c95a7fecf ts=2026-10-01T14:19:16.3840000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 31 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `254ms: 6aa4140b41b41dbac0c7f22a.jsonl[1302] _id=6ab53043485cab4c9551ea53 ts=2026-09-24T14:14:27.5370000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1307] _id=6ab53043485cab4c9551ea61 ts=2026-09-24T14:14:27.7910000Z`; `200ms: 6aa4140b41b41dbac0c7f22a.jsonl[1306] _id=6ab53043485cab4c9551ea57 ts=2026-09-24T14:14:27.6610000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1308] _id=6ab53043485cab4c9551ea65 ts=2026-09-24T14:14:27.8610000Z`; `311ms: 6aa4140b41b41dbac0c7f22a.jsonl[1307] _id=6ab53043485cab4c9551ea61 ts=2026-09-24T14:14:27.7910000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[1309] _id=6ab53044485cab4c9551ea6f ts=2026-09-24T14:14:28.1020000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `381ms: 6aa4140b41b41dbac0c7f22a.jsonl[333] _id=6ab3dbf4485cab4c954cef47 ts=2026-09-23T14:02:28.6890000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[334] _id=6ab3dbf6485cab4c954cef57 ts=2026-09-23T14:02:29.0700000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4140b41b41dbac0c7f22a.jsonl[5270] _id=6abbc356485cab4c957e0d61 ts=2026-09-29T13:55:32.8130000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[5271] _id=6abbc356485cab4c957e0d65 ts=2026-09-29T13:55:32.8180000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `803ms: 6aa4140b41b41dbac0c7f22a.jsonl[14235] _id=6ac503c3de269131f9b2cb7d ts=2026-10-06T14:20:51.6400000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[14237] _id=6ac503c4de269131f9b2cb93 ts=2026-10-06T14:20:52.4430000Z`; `499ms: 6aa4140b41b41dbac0c7f22a.jsonl[14237] _id=6ac503c4de269131f9b2cb93 ts=2026-10-06T14:20:52.4430000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[14245] _id=6ac503c6de269131f9b2cbef ts=2026-10-06T14:20:52.9420000Z`; `368ms: 6aa4140b41b41dbac0c7f22a.jsonl[14245] _id=6ac503c6de269131f9b2cbef ts=2026-10-06T14:20:52.9420000Z ~ 6aa4140b41b41dbac0c7f22a.jsonl[14246] _id=6ac503c7de269131f9b2cbfd ts=2026-10-06T14:20:53.3100000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 93h 46m 
  - Evidence: 93h 46m: 6aa4140b41b41dbac0c7f22a.jsonl[10685] _id=6abe83f1485cab4c95abb028 ts=2026-10-01T16:01:53.2160000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11025] _id=6ac3aab0de269131f9a9d022 ts=2026-10-05T13:48:32.4940000Z; 71h 40m: 6aa4140b41b41dbac0c7f22a.jsonl[1626] _id=6ab67fdd485cab4c9555c8f2 ts=2026-09-25T14:06:21.9730000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3543] _id=6aba6fb6485cab4c95681aef ts=2026-09-28T13:46:30.7710000Z; 24h 9m: 6aa4140b41b41dbac0c7f22a.jsonl[858] _id=6ab52985485cab4c95517363 ts=2026-09-24T13:45:43.0420000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1359] _id=6ab67d2d485cab4c9555a22c ts=2026-09-25T13:54:53.6170000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 7m 
  - Evidence: 120h 7m: 6aa4140b41b41dbac0c7f22a.jsonl[8372] _id=6abd3294485cab4c958d36be ts=2026-09-30T16:02:28.3750000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[13314] _id=6ac3cbf2de269131f9ad9927 ts=2026-10-05T16:10:26.4850000Z; 120h 7m: 6aa4140b41b41dbac0c7f22a.jsonl[1656] _id=6ab6801f485cab4c9555cd9e ts=2026-09-25T14:07:27.7580000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[6811] _id=6abd196a485cab4c958ab9f9 ts=2026-09-30T14:15:06.8450000Z; 48h 5m: 6aa4140b41b41dbac0c7f22a.jsonl[314] _id=6ab3dbb8485cab4c954ced13 ts=2026-09-23T14:01:28.0010000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1648] _id=6ab68015485cab4c9555cd52 ts=2026-09-25T14:07:17.1470000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.006s..0.007s shown 
  - Evidence: 6ms: 6aa4140b41b41dbac0c7f22a.jsonl[1647] _id=6ab6801a485cab4c9555cd7a ts=2026-09-25T14:07:22.3890000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1649] _id=6ab6801a485cab4c9555cd7c ts=2026-09-25T14:07:22.3950000Z; 7ms: 6aa4140b41b41dbac0c7f22a.jsonl[1654] _id=6ab6801d485cab4c9555cd92 ts=2026-09-25T14:07:25.4310000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1650] _id=6ab6801d485cab4c9555cd94 ts=2026-09-25T14:07:25.4380000Z; 7ms: 6aa4140b41b41dbac0c7f22a.jsonl[304] _id=6ab3db90485cab4c954cec09 ts=2026-09-23T14:00:48.1310000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[18] _id=6ab3db90485cab4c954cec0b ts=2026-09-23T14:00:48.1380000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 93h 32m 
  - Evidence: 93h 32m: 6aa4140b41b41dbac0c7f22a.jsonl[11011] _id=6abe8752485cab4c95abd188 ts=2026-10-01T16:16:18.5840000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11040] _id=6ac3aad1de269131f9a9d734 ts=2026-10-05T13:49:05.9780000Z; 71h 19m: 6aa4140b41b41dbac0c7f22a.jsonl[3518] _id=6ab68532485cab4c95564850 ts=2026-09-25T14:29:06.4700000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3581] _id=6aba7026485cab4c95681c7d ts=2026-09-28T13:48:22.7490000Z; 23h 39m: 6aa4140b41b41dbac0c7f22a.jsonl[1338] _id=6ab5308e485cab4c9551ee59 ts=2026-09-24T14:15:42.2990000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1367] _id=6ab67d58485cab4c9555a3e4 ts=2026-09-25T13:55:37.0880000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 455 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[1454] _id=6ab67f6b485cab4c9555c446 ts=2026-09-25T14:04:27.1810000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1614] _id=6ab67f6b485cab4c9555c448 ts=2026-09-25T14:04:27.1820000Z; 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[3591] _id=6aba7057485cab4c95681e83 ts=2026-09-28T13:49:10.8310000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3592] _id=6aba7057485cab4c95681e85 ts=2026-09-28T13:49:10.8320000Z; 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[9449] _id=6abe6d62485cab4c95a8609f ts=2026-10-01T14:25:38.0070000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9450] _id=6abe6d62485cab4c95a860a5 ts=2026-10-01T14:25:38.0080000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 47m 
  - Evidence: 239h 47m: 6aa4140b41b41dbac0c7f22a.jsonl[1615] _id=6ab67f87485cab4c9555c4f4 ts=2026-09-25T14:04:56.1040000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11095] _id=6ac3ab96de269131f9aa02fc ts=2026-10-05T13:52:22.9670000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 93h 34m 
  - Evidence: 93h 34m: 6aa4140b41b41dbac0c7f22a.jsonl[10990] _id=6abe86f8485cab4c95abccb4 ts=2026-10-01T16:14:48.7530000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11034] _id=6ac3aac7de269131f9a9d538 ts=2026-10-05T13:48:55.5290000Z; 71h 17m: 6aa4140b41b41dbac0c7f22a.jsonl[3530] _id=6ab6854b485cab4c95564988 ts=2026-09-25T14:29:31.6370000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3547] _id=6aba6fbd485cab4c95681aff ts=2026-09-28T13:46:37.2270000Z; 23h 39m: 6aa4140b41b41dbac0c7f22a.jsonl[1340] _id=6ab53096485cab4c9551ee7b ts=2026-09-24T14:15:50.9190000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1362] _id=6ab67d33485cab4c9555a264 ts=2026-09-25T13:54:58.7840000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 243 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22a.jsonl[9520] _id=6abe6dde485cab4c95a87f33 ts=2026-10-01T14:27:42.7610000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9521] _id=6abe6ddf485cab4c95a87f39 ts=2026-10-01T14:27:42.7610000Z; 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[13006] _id=6ac3b460de269131f9abe10a ts=2026-10-05T14:29:52.3220000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[13007] _id=6ac3b460de269131f9abe10e ts=2026-10-05T14:29:52.3230000Z; 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[13143] _id=6ac3cabdde269131f9ad8ead ts=2026-10-05T16:05:16.3220000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[13146] _id=6ac3cabdde269131f9ad8eb1 ts=2026-10-05T16:05:16.3230000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 93h 41m 
  - Evidence: 93h 41m: 6aa4140b41b41dbac0c7f22a.jsonl[10909] _id=6abe85e6485cab4c95abc478 ts=2026-10-01T16:10:14.7100000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11088] _id=6ac3ab87de269131f9a9fef4 ts=2026-10-05T13:52:07.5140000Z; 71h 52m: 6aa4140b41b41dbac0c7f22a.jsonl[3429] _id=6ab683e7485cab4c95563530 ts=2026-09-25T14:23:35.7240000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[4284] _id=6aba76a7485cab4c9568b1b7 ts=2026-09-28T14:16:07.6230000Z; 24h 14m: 6aa4140b41b41dbac0c7f22a.jsonl[5314] _id=6abbc54e485cab4c957e4241 ts=2026-09-29T14:03:58.5550000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[6859] _id=6abd1a17485cab4c958adcba ts=2026-09-30T14:17:59.0490000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 6aa4140b41b41dbac0c7f22a.jsonl[914] _id=6ab52a1d485cab4c95518bd3 ts=2026-09-24T13:48:14.9440000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[915] _id=6ab52a1d485cab4c95518bd5 ts=2026-09-24T13:48:14.9500000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 93h 24m 
  - Evidence: 93h 24m: 6aa4140b41b41dbac0c7f22a.jsonl[11017] _id=6abe8914485cab4c95abdd88 ts=2026-10-01T16:23:49.0240000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11030] _id=6ac3aab5de269131f9a9d174 ts=2026-10-05T13:48:32.5000000Z; 71h 16m: 6aa4140b41b41dbac0c7f22a.jsonl[3531] _id=6ab68557485cab4c955649cc ts=2026-09-25T14:29:43.6820000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3545] _id=6aba6fbd485cab4c95681afd ts=2026-09-28T13:46:30.7770000Z; 23h 38m: 6aa4140b41b41dbac0c7f22a.jsonl[1341] _id=6ab530a1485cab4c9551ee89 ts=2026-09-24T14:16:01.8940000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1360] _id=6ab67d33485cab4c9555a260 ts=2026-09-25T13:54:53.6230000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 13m 
  - Evidence: 94h 13m: 6aa4140b41b41dbac0c7f22a.jsonl[10113] _id=6abe8024485cab4c95ab5cb0 ts=2026-10-01T15:45:39.4490000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11195] _id=6ac3ad40de269131f9aa5d00 ts=2026-10-05T13:59:27.9390000Z; 71h 34m: 6aa4140b41b41dbac0c7f22a.jsonl[3369] _id=6ab6839a485cab4c955631b2 ts=2026-09-25T14:22:18.9650000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3800] _id=6aba7209485cab4c95685657 ts=2026-09-28T13:56:24.6020000Z; 48h 16m: 6aa4140b41b41dbac0c7f22a.jsonl[6237] _id=6abbc6f0485cab4c957e652f ts=2026-09-29T14:10:53.4580000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9514] _id=6abe6dda485cab4c95a87e06 ts=2026-10-01T14:27:36.1830000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3424 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22a.jsonl[10007] _id=6abe7fec485cab4c95ab5074 ts=2026-10-01T15:44:42.5450000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[10008] _id=6abe7fec485cab4c95ab5078 ts=2026-10-01T15:44:42.5450000Z; 0ms: 6aa4140b41b41dbac0c7f22a.jsonl[10008] _id=6abe7fec485cab4c95ab5078 ts=2026-10-01T15:44:42.5450000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[10015] _id=6abe7fec485cab4c95ab5082 ts=2026-10-01T15:44:42.5450000Z; 0ms: 6aa4140b41b41dbac0c7f22a.jsonl[10011] _id=6abe7fee485cab4c95ab5103 ts=2026-10-01T15:44:45.4930000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[10035] _id=6abe7fee485cab4c95ab510f ts=2026-10-01T15:44:45.4930000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 32m 
  - Evidence: 95h 32m: 6aa4140b41b41dbac0c7f22a.jsonl[9495] _id=6abe6daa485cab4c95a871ac ts=2026-10-01T14:26:50.8890000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11175] _id=6ac3ad1ede269131f9aa56a0 ts=2026-10-05T13:58:54.3720000Z; 72h 8m: 6aa4140b41b41dbac0c7f22a.jsonl[4340] _id=6aba76fa485cab4c9568bc55 ts=2026-09-28T14:17:30.2950000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9470] _id=6abe6d84485cab4c95a8687b ts=2026-10-01T14:26:12.0130000Z; 71h 52m: 6aa4140b41b41dbac0c7f22a.jsonl[3430] _id=6ab683ea485cab4c95563544 ts=2026-09-25T14:23:38.7160000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[4286] _id=6aba76a7485cab4c9568b1b2 ts=2026-09-28T14:16:07.6160000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 59m 
  - Evidence: 95h 59m: 6aa4140b41b41dbac0c7f22a.jsonl[10928] _id=6abe8601485cab4c95abc57c ts=2026-10-01T16:10:41.8010000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[13312] _id=6ac3cbf5de269131f9ad993f ts=2026-10-05T16:10:29.6480000Z; 71h 35m: 6aa4140b41b41dbac0c7f22a.jsonl[1899] _id=6ab6820f485cab4c95560084 ts=2026-09-25T14:15:43.4530000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3624] _id=6aba70ee485cab4c95682c85 ts=2026-09-28T13:51:42.7520000Z; 46h 1m: 6aa4140b41b41dbac0c7f22a.jsonl[13322] _id=6ac3cc07de269131f9ad99af ts=2026-10-05T16:10:47.2040000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[14635] _id=6ac6532dde269131f9ba6ef4 ts=2026-10-07T14:11:57.5490000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6aa4140b41b41dbac0c7f22a.jsonl[1524] _id=6ab67ec3485cab4c9555bd74 ts=2026-09-25T14:01:39.2450000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9011] _id=6abe67f2485cab4c95a79091 ts=2026-10-01T14:02:26.3110000Z; 23h 43m: 6aa4140b41b41dbac0c7f22a.jsonl[1317] _id=6ab53049485cab4c9551eae3 ts=2026-09-24T14:14:33.7920000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1441] _id=6ab67de7485cab4c9555b06e ts=2026-09-25T13:57:59.4450000Z; 16m 9s: 6aa4140b41b41dbac0c7f22a.jsonl[9061] _id=6abe681b485cab4c95a792c7 ts=2026-10-01T14:03:07.0870000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9259] _id=6abe6be4485cab4c95a7febd ts=2026-10-01T14:19:16.3360000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6aa4140b41b41dbac0c7f22a.jsonl[1529] _id=6ab67ec3485cab4c9555bd76 ts=2026-09-25T14:01:39.2680000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[8991] _id=6abe67e3485cab4c95a78fa5 ts=2026-10-01T14:02:11.5210000Z; 23h 43m: 6aa4140b41b41dbac0c7f22a.jsonl[1318] _id=6ab53049485cab4c9551eae9 ts=2026-09-24T14:14:33.8140000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1418] _id=6ab67dd5485cab4c9555ae4a ts=2026-09-25T13:57:41.2190000Z; 15m 57s: 6aa4140b41b41dbac0c7f22a.jsonl[9059] _id=6abe681b485cab4c95a792cf ts=2026-10-01T14:03:07.1700000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9256] _id=6abe6bd8485cab4c95a7fc57 ts=2026-10-01T14:19:04.3150000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.030s..0.030s shown 
  - Evidence: 30ms: 6aa4140b41b41dbac0c7f22a.jsonl[9281] _id=6abe6be4485cab4c95a7fec1 ts=2026-10-01T14:19:16.3540000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9279] _id=6abe6be4485cab4c95a7fecf ts=2026-10-01T14:19:16.3840000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6aa4140b41b41dbac0c7f22a.jsonl[1517] _id=6ab67eb4485cab4c9555bcf2 ts=2026-09-25T14:01:24.9750000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[8989] _id=6abe67df485cab4c95a78f61 ts=2026-10-01T14:02:07.8290000Z; 23h 42m: 6aa4140b41b41dbac0c7f22a.jsonl[1313] _id=6ab53046485cab4c9551ea8d ts=2026-09-24T14:14:30.5010000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1381] _id=6ab67da2485cab4c9555a864 ts=2026-09-25T13:56:50.3770000Z; 15m 58s: 6aa4140b41b41dbac0c7f22a.jsonl[9034] _id=6abe6816485cab4c95a792a7 ts=2026-10-01T14:03:02.8420000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[9245] _id=6abe6bd5485cab4c95a7fb8a ts=2026-10-01T14:19:01.7220000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 31 interval(s) ≤ 0.016s..0.019s shown 
  - Evidence: 16ms: 6aa4140b41b41dbac0c7f22a.jsonl[1400] _id=6ab67dc8485cab4c9555acfc ts=2026-09-25T13:57:29.0300000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1401] _id=6ab67dc8485cab4c9555ad02 ts=2026-09-25T13:57:29.0460000Z; 19ms: 6aa4140b41b41dbac0c7f22a.jsonl[1411] _id=6ab67dcd485cab4c9555ad9a ts=2026-09-25T13:57:33.2000000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1414] _id=6ab67dcd485cab4c9555ad9c ts=2026-09-25T13:57:33.2190000Z; 19ms: 6aa4140b41b41dbac0c7f22a.jsonl[1414] _id=6ab67dcd485cab4c9555ad9c ts=2026-09-25T13:57:33.2190000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1412] _id=6ab67dcd485cab4c9555ad9e ts=2026-09-25T13:57:33.2380000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 47m 
  - Evidence: 23h 47m: 6aa4140b41b41dbac0c7f22a.jsonl[1299] _id=6ab53022485cab4c9551e76d ts=2026-09-24T14:13:54.2000000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1518] _id=6ab67eb8485cab4c9555bd28 ts=2026-09-25T14:01:28.4430000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 94h 5m 
  - Evidence: 94h 5m: 6aa4140b41b41dbac0c7f22a.jsonl[9736] _id=6abe7f6c485cab4c95ab300a ts=2026-10-01T15:42:36.1360000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11027] _id=6ac3aa92de269131f9a9c96c ts=2026-10-05T13:48:02.8270000Z; 71h 39m: 6aa4140b41b41dbac0c7f22a.jsonl[1617] _id=6ab67fd7485cab4c9555c861 ts=2026-09-25T14:06:15.2400000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3537] _id=6aba6f9d485cab4c95681ad5 ts=2026-09-28T13:46:05.5540000Z; 24h 9m: 6aa4140b41b41dbac0c7f22a.jsonl[857] _id=6ab52973485cab4c95517001 ts=2026-09-24T13:45:24.4550000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1357] _id=6ab67d23485cab4c9555a1e4 ts=2026-09-25T13:54:43.3330000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 94h 5m 
  - Evidence: 94h 5m: 6aa4140b41b41dbac0c7f22a.jsonl[9722] _id=6abe7f86485cab4c95ab3648 ts=2026-10-01T15:43:02.5650000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11026] _id=6ac3aa92de269131f9a9c95d ts=2026-10-05T13:48:02.8260000Z; 71h 39m: 6aa4140b41b41dbac0c7f22a.jsonl[1618] _id=6ab67fd7485cab4c9555c85e ts=2026-09-25T14:06:15.2390000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3536] _id=6aba6f9d485cab4c95681ad3 ts=2026-09-28T13:46:05.5530000Z; 24h 9m: 6aa4140b41b41dbac0c7f22a.jsonl[3536] _id=6aba6f9d485cab4c95681ad3 ts=2026-09-28T13:46:05.5530000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[5261] _id=6abbc33c485cab4c957e0b97 ts=2026-09-29T13:55:08.7650000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 93h 24m 
  - Evidence: 93h 24m: 6aa4140b41b41dbac0c7f22a.jsonl[11018] _id=6abe8918485cab4c95abddb4 ts=2026-10-01T16:23:52.7270000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11028] _id=6ac3aa96de269131f9a9ca18 ts=2026-10-05T13:48:06.1690000Z; 72h 2m: 6aa4140b41b41dbac0c7f22a.jsonl[3527] _id=6ab68555485cab4c955649be ts=2026-09-25T14:29:41.3830000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[5259] _id=6aba7a7b485cab4c9568f3e1 ts=2026-09-28T14:32:27.5250000Z; 24h 13m: 6aa4140b41b41dbac0c7f22a.jsonl[1344] _id=6ab530a4485cab4c9551ee9d ts=2026-09-24T14:16:04.3620000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3527] _id=6ab68555485cab4c955649be ts=2026-09-25T14:29:41.3830000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 93h 35m 
  - Evidence: 93h 35m: 6aa4140b41b41dbac0c7f22a.jsonl[10970] _id=6abe86aa485cab4c95abca5e ts=2026-10-01T16:13:30.4760000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[11032] _id=6ac3aab5de269131f9a9d17a ts=2026-10-05T13:48:37.1830000Z; 71h 17m: 6aa4140b41b41dbac0c7f22a.jsonl[3496] _id=6ab6852d485cab4c955647f0 ts=2026-09-25T14:29:01.6480000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[3546] _id=6aba6fbe485cab4c95681b01 ts=2026-09-28T13:46:37.2590000Z; 23h 39m: 6aa4140b41b41dbac0c7f22a.jsonl[1339] _id=6ab53091485cab4c9551ee69 ts=2026-09-24T14:15:45.3140000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1361] _id=6ab67d33485cab4c9555a266 ts=2026-09-25T13:54:59.3090000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22a.jsonl[14561] _id=6ac644ddde269131f9b8b7f9 ts=2026-10-07T13:10:53.0120000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[14563] _id=6ac644ddde269131f9b8b7fa ts=2026-10-07T13:10:53.0120000Z; 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[1369] _id=6ab67d59485cab4c9555a3e8 ts=2026-09-25T13:55:37.1060000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[1370] _id=6ab67d59485cab4c9555a3ea ts=2026-09-25T13:55:37.1070000Z; 1ms: 6aa4140b41b41dbac0c7f22a.jsonl[14573] _id=6ac651e4de269131f9ba5077 ts=2026-10-07T14:06:28.4680000Z -> 6aa4140b41b41dbac0c7f22a.jsonl[14574] _id=6ac651e4de269131f9ba5078 ts=2026-10-07T14:06:28.4690000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[7258] _id=6abd2eba485cab4c958cf458 ts=2026-09-30T15:46:01.9600000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[7259] _id=6abd2ebb485cab4c958cf465 ts=2026-09-30T15:46:02.6610000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[7298] _id=6abd2ec4485cab4c958cf61d ts=2026-09-30T15:46:10.3220000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1329] _id=6ab53081485cab4c9551ee1e ts=2026-09-24T14:15:29.0290000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1515] _id=6ab67edc485cab4c9555be30 ts=2026-09-25T14:02:04.4630000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[4003] _id=6aba7450485cab4c95687b71 ts=2026-09-28T14:06:08.1590000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 122 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[2260] _id=6ab6824e485cab4c95560d59 ts=2026-09-25T14:16:15.7790000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2309] _id=6ab68264485cab4c95561230 ts=2026-09-25T14:17:07.9270000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2438] _id=6ab68282485cab4c9556186e ts=2026-09-25T14:17:38.2000000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 217 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1953] _id=6ab6823a485cab4c95560814 ts=2026-09-25T14:14:26.3940000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1954] _id=6ab6823a485cab4c95560818 ts=2026-09-25T14:14:26.3940000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2019] _id=6ab6823c485cab4c9556089a ts=2026-09-25T14:14:26.7530000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[9059] _id=6abe681b485cab4c95a792cf ts=2026-10-01T14:03:07.1700000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[9279] _id=6abe6be4485cab4c95a7fecf ts=2026-10-01T14:19:16.3840000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1386] _id=6ab67da3485cab4c9555a89e ts=2026-09-25T13:56:51.5950000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1387] _id=6ab67da3485cab4c9555a8a3 ts=2026-09-25T13:56:51.6170000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1414] _id=6ab67dcd485cab4c9555ad9c ts=2026-09-25T13:57:33.2190000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[13150] _id=6ac3cacade269131f9ad8ee1 ts=2026-10-05T16:05:30.6400000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[13447] _id=6ac4fbb6de269131f9b15c8f ts=2026-10-06T13:46:30.6220000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 8 records 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[330] _id=6ab3dbee485cab4c954cef19 ts=?`; `6aa4140b41b41dbac0c7f22a.jsonl[358] _id=6ab3dddb485cab4c954cff39 ts=?`; `6aa4140b41b41dbac0c7f22a.jsonl[3544] _id=6aba6fbd485cab4c95681afb ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 25 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[7242] _id=6abd2eb9485cab4c958cf3f8 ts=2026-09-30T15:45:59.2490000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[7289] _id=6abd2ec7485cab4c958cf676 ts=2026-09-30T15:46:11.7970000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[7290] _id=6abd2ec7485cab4c958cf682 ts=2026-09-30T15:46:12.1180000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 754 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[2445] _id=6ab68284485cab4c955618e8 ts=2026-09-25T14:17:40.1470000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2435] _id=6ab68284485cab4c955618ec ts=2026-09-25T14:17:40.1620000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[2500] _id=6ab68290485cab4c95561b39 ts=2026-09-25T14:17:51.1060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1380 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[2000] _id=6ab6823a485cab4c95560830 ts=2026-09-25T14:14:26.4030000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1982] _id=6ab6823b485cab4c9556083a ts=2026-09-25T14:14:26.4030000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1997] _id=6ab6823b485cab4c95560856 ts=2026-09-25T14:14:26.4440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 10 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1400] _id=6ab67dc8485cab4c9555acfc ts=2026-09-25T13:57:29.0300000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1401] _id=6ab67dc8485cab4c9555ad02 ts=2026-09-25T13:57:29.0460000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1425] _id=6ab67de0485cab4c9555af72 ts=2026-09-25T13:57:52.7420000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1518] _id=6ab67eb8485cab4c9555bd28 ts=2026-09-25T14:01:28.4430000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 308 start, 301 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 135 unmatched 'BecameCameraCentered' (totals: 1117 open, 1104 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 183 unmatched 'BecameVisible' (totals: 1670 open, 1704 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 69 open, 71 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 27 unmatched 'questActiveEvent' (totals: 52 start, 27 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 387 of 16637 adjacent _id pairs reverse in client time; worst 122.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f22a.jsonl[1971] _id=6ab6823d485cab4c955608dc ts=2026-09-25T14:16:29.5490000Z`; `6aa4140b41b41dbac0c7f22a.jsonl[1972] _id=6ab6823d485cab4c955608e0 ts=2026-09-25T14:14:26.9090000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.06s, min -123.99s, max +2.24s over 16638 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22a\coverage.yaml

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
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 8 records 
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

### `InputEvent` — 5620 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1727); Unit 4 Dev - Dungeon (1601); Unit 2 Prod (Refactor) (854); Unit 1 Dev (743); Unit 3 Dungeon Dev (366); Unit 4 Dev (329)
- **Intervals:** median 0.93s (p5 0.06s / p95 11.34s, n=5619)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5620/5620 records)
    "pressed"  x5620
data.actionType  (string, 5620/5620 records)
    "Move"  x4151
    "Interact"  x575
    "Jump"  x403
    "Sprint"  x219
    "Pause"  x105
    "Ascend"  x49
    "Descend"  x47
    "Hoverboard"  x40
    "Map"  x16
    "SkipCinematic"  x8
    "ToggleDebug"  x7
data.key  (string, 5620/5620 records, 6 empty-string)
    22 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5620/5620 records)
    "Player"  x4504
    "Drone"  x1116
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 5595 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2827); Unit 4 Dev (2280); Unit 3 Dungeon Dev (488)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.38s, n=5594)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5595/5595 records)
    "BecameInvisible"  x1704
    "BecameVisible"  x1670
    "BecameCameraCentered"  x1117
    "BecameCameraUncentered"  x1104
data.pieceId  (string, 5595/5595 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5595/5595 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2663 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (703); Unit 3 Dev (630); Unit 4 Dev - Dungeon (525); Unit 1 Dev (411); Unit 4 Dev (261); Unit 3 Dungeon Dev (133)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.09s, n=2654)
- **Fields under `data`:**

```text
data.position  (object, 2663/2663 records)
data.position.x  (number, 2663/2663 records)
    numeric range -651.138 .. 1422.08 (1003 unique)
data.position.y  (number, 2663/2663 records)
    numeric range -115.665 .. 164.91 (649 unique)
data.position.z  (number, 2663/2663 records)
    numeric range -1140.1 .. 1968.79 (1002 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1709 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (545); Unit 2 Prod (Refactor) (512); Unit 1 Dev (265); Unit 4 Dev - Dungeon (152); Unit 3 Dungeon Dev (128); Unit 4 Dev (107)
- **eventKey:** present on 1100 of 1709 records
- **Intervals:** median 4.89s (p5 0.00s / p95 65.34s, n=1708)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1100; [conversationId, dialogueEventType] x609
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1709/1709 records)
    numeric range 8 .. 111 (39 unique)
data.dialogueEventType  (string, 1709/1709 records)
    "DialogueNodeEvent"  x1100
    "DialogueStartEvent"  x308
    "DialogueFinishEvent"  x301
data.nodeId  (number, 1100/1709 records)
    numeric range 0 .. 290 (220 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 302 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (152); Unit 2 Prod (Refactor) (50); Unit 3 Dungeon Dev (44); Unit 1 Dev (24); Unit 4 Dev (21); Unit 3 Dev (11)
- **Intervals:** median 12.54s (p5 1.14s / p95 428.04s, n=301)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 302/302 records)
    29 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 302/302 records)
    70 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 154 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (82); Unit 1 Dev (72)
- **Intervals:** median 0.38s (p5 0.02s / p95 5.83s, n=153)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 154/154 records)
    "argumentationNodeHoverEnd"  x71
    "argumentationNodeHoverStart"  x69
    "argumentationNodeAdd"  x13
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 154/154 records)
    "Unit 3 - Pollution Upstream"  x82
    "Unit 1 - Argumentation Tutorial"  x44
    "Unit 1 - Freshwater"  x28
data.nodeName  (string, 154/154 records)
    "I"  x47
    "1"  x25
    "A"  x25
    "5"  x14
    "II"  x13
    "3"  x10
    "4"  x8
    "B"  x8
    "2"  x4
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `DaniEvent` — 114 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (100); Unit 1 Dev (6); Unit 2 Prod (Refactor) (6); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 0.31s (p5 0.20s / p95 34.33s, n=113)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 114/114 records)
    "Close"  x60
    "Open"  x54
data.toolName  (string, 114/114 records, 110 empty-string)
    ""  x110
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `Soil Key Puzzle` — 110 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (50); Unit 4 Dev (38); Unit 3 Dev (22)
- **Intervals:** median 0.98s (p5 0.19s / p95 11.43s, n=109)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x100; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/110 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/110 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 100/110 records)
    "RightDrag"  x53
    "LeftDrag"  x47
data.currentSoilType  (string, 100/110 records)
    "CLAYSAND"  x26
    "CLAY"  x21
    "SAND"  x21
    "CLAYROCK"  x12
    "SANDGRAVEL"  x12
    "GRAVEL"  x5
    "BEDROCK"  x3
data.isCorrectSelection  (string, 100/110 records)
    "false"  x70
    "true"  x30
data.waterLevelStatus  (string, 100/110 records)
    "TooHigh"  x43
    "Proper"  x41
    "TooLow"  x16
data.waterRetentionChange  (string, 100/110 records)
    "Increase"  x38
    "Decrease"  x32
    "NoChange"  x30
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 79 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (56); Unit 2 Prod (Refactor) (10); Unit 4 Dev (9); Unit 4 Dev - Dungeon (4)
- **Intervals:** median 6.95s (p5 1.45s / p95 86702.65s, n=78)
- **`data` key-set variants:** [actionType, featureUsed] x58; [actionType, featureUsed, location] x21
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 79/79 records)
    "MapCloseEvent"  x29
    "MapOpenEvent"  x29
    "WaypointMoveEvent"  x17
    "WaypointSetEvent"  x4
data.featureUsed  (string, 79/79 records)
    "Map"  x58
    "Waypoint"  x21
data.location  (object, 21/79 records)
data.location.x  (number, 21/79 records)
    numeric range -232.09 .. 573.91 (21 unique)
data.location.y  (number, 21/79 records)
    numeric range -335.5 .. 157.5 (20 unique)
data.location.z  (number, 21/79 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 79 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (19); Unit 3 Dev (19); Unit 2 Prod (Refactor) (17); Unit 4 Dev - Dungeon (13); Unit 4 Dev (8); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 79 of 79 records
- **Intervals:** median 326.33s (p5 0.00s / p95 84425.27s, n=78)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x27
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 79/79 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x27
data.questID  (string, 79/79 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 79/79 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 27/79 records)
    "Succeeded"  x27
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 61 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (25); Unit 1 Dev (18); Unit 3 Dev (10); Unit 4 Dev - Dungeon (4); Transition (1); Unit 2 Prod (Refactor) (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 176.59s (p5 2.13s / p95 86228.39s, n=60)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 61/61 records)
    true  x61
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 51 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (21); Unit 3 Dev (14); Unit 4 Dev - Dungeon (6); Unit 2 Prod (Refactor) (4); Unit 4 Dev (3); Unit 3 Dungeon Dev (2); Transition (1)
- **Intervals:** median 389.34s (p5 3.24s / p95 86823.10s, n=50)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 51/51 records)
    false  x51
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 34 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 4 Dev (7); Unit 3 Dev (6); MainMenu (4); Unit 1 Dev (4); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (2)
- **Intervals:** median 1314.80s (p5 7.71s / p95 155373.86s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "DebugMenuStateChanged"  x34
data.isOpened  (bool, 34/34 records)
    false  x34
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 25 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (25)
- **Intervals:** median 6837.24s (p5 166.39s / p95 232335.60s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 15 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (11); Unit 3 Dev (4)
- **Intervals:** median 7.59s (p5 0.27s / p95 236970.15s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "submitAnswerEvent"  x15
data.answerSubmitted  (string, 15/15 records, 1 empty-string)
    "A,1,I"  x9
    "A,3,I"  x2
    "A,5,I"  x2
    ""  x1
    "A,1,"  x1
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Freshwater"  x10
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (6)
- **Intervals:** median 51.14s (p5 0.05s / p95 258605.34s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 9 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (9)
- **Intervals:** median 0.65s (p5 0.40s / p95 12.99s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "ChangeCanister"  x9
data.canisterType  (string, 9/9 records)
    "Sand"  x8
    "Gravel"  x1
data.floor  (string, 9/9 records)
    "5"  x9
data.machine  (string, 9/9 records)
    "2"  x9
data.row  (string, 9/9 records)
    "TopRow"  x9
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `crash` — 8 records

- **Scenes:** <missing sceneName> (8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 8/8 records)
    true  x8
data.message  (string, 8/8 records)
    "A user gesture is required to request Pointer Lock."  x5
    "Permissions check failed"  x3
data.phase  (string, 8/8 records)
    "running"  x8
data.stack  (string, 8/8 records, 5 empty-string)
    ""  x5
    "TypeError: Permissions check failed"  x3
data.type  (string, 8/8 records)
    "unhandled_rejection"  x8
data.unitId  (string, 8/8 records)
    "unit1"  x2
    "unit2"  x2
    "unit3"  x2
    "unit4"  x2
data.workspace  (string, 8/8 records)
    "mhs"  x8
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863246.86s (p5 863246.86s / p95 863246.86s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 85654.24s (p5 85654.24s / p95 85654.24s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Freshwater"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - "  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (50 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (17x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*