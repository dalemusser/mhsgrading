# MHS Gameplay Log Audit Report — build 08-25-26

## 1. Build Information

- **Build ID:** 08-25-26
- **Game version string(s) in log:** 20260819-12237
- **Audit date:** 2026-08-26
- **Log file(s):** wenyi082526-1.stratalog.logdata.json
- **Records:** 6124 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6a8db41fa68c657728943067
- **Time span:** 2026-08-25T16:49:32.562000+00:00 .. 2026-08-25T19:06:27.534000+00:00 (2h 16m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\gameplay-logs-test\config\coverage\08-25-26.yaml
- **Baseline:** snapshot gameplay-logs-test\reports\08-13-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 6124 records, 11 scenes.
- Findings: **0 FAIL**, **23 WARNING**, 85 INFO, 0 NOT_TESTED, 104 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DialogueEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `DaniEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: median interval between records changed substantially
  - WARNING/Medium `DialogueEvent`: eventKey does not match its documented format
  - WARNING/Medium `DaniEvent`: tool open/close: close without preceding open

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1862 | 30.4 | 1 | 9 | 0 | 2026-08-25T16:52:10.267000+00:00 | 2026-08-25T19:06:27.534000+00:00 | 2h 14m |
| DialogueEvent | 1759 | 28.72 | 1 | 9 | 1124 | 2026-08-25T16:50:02.027000+00:00 | 2026-08-25T19:06:23.681000+00:00 | 2h 16m |
| PuzzlePieceVisibleEvent | 1137 | 18.57 | 1 | 3 | 0 | 2026-08-25T17:08:16.295000+00:00 | 2026-08-25T18:26:08.993000+00:00 | 1h 17m |
| PlayerPositionEvent | 728 | 11.89 | 1 | 9 | 0 | 2026-08-25T16:49:45.141000+00:00 | 2026-08-25T19:06:22.679000+00:00 | 2h 16m |
| argumentationNodeEvent | 167 | 2.73 | 1 | 5 | 0 | 2026-08-25T17:01:32.785000+00:00 | 2026-08-25T18:57:21.554000+00:00 | 1h 55m |
| ObjectInterEvent | 81 | 1.32 | 1 | 7 | 0 | 2026-08-25T16:53:01.958000+00:00 | 2026-08-25T18:51:46.261000+00:00 | 1h 58m |
| DaniEvent | 80 | 1.31 | 1 | 8 | 0 | 2026-08-25T16:49:45.097000+00:00 | 2026-08-25T18:57:26.942000+00:00 | 2h 7m |
| questEvent | 68 | 1.11 | 1 | 9 | 68 | 2026-08-25T16:50:02.023000+00:00 | 2026-08-25T19:05:41.094000+00:00 | 2h 15m |
| TopographicMapEvent | 55 | 0.9 | 1 | 2 | 0 | 2026-08-25T17:09:00.184000+00:00 | 2026-08-25T18:10:34.831000+00:00 | 1h 1m |
| chatEvent | 38 | 0.62 | 1 | 1 | 0 | 2026-08-25T17:09:12.058000+00:00 | 2026-08-25T17:09:23.511000+00:00 | 11.5s |
| Soil Key Puzzle | 34 | 0.56 | 1 | 3 | 0 | 2026-08-25T17:11:07.061000+00:00 | 2026-08-25T18:18:38.029000+00:00 | 1h 7m |
| WaterChamberEvent | 22 | 0.36 | 1 | 1 | 0 | 2026-08-25T18:47:48.719000+00:00 | 2026-08-25T18:53:28.810000+00:00 | 5m 40s |
| argumentationToolEvent | 16 | 0.26 | 1 | 4 | 0 | 2026-08-25T17:01:31.285000+00:00 | 2026-08-25T18:57:25.390000+00:00 | 1h 55m |
| argumentationEvent | 14 | 0.23 | 1 | 5 | 0 | 2026-08-25T17:01:32.452000+00:00 | 2026-08-25T18:57:26.946000+00:00 | 1h 55m |
| gameWindowFocusEvent | 14 | 0.23 | 1 | 6 | 0 | 2026-08-25T16:50:05.914000+00:00 | 2026-08-25T18:37:44.614000+00:00 | 1h 47m |
| gameWindowUnfocusEvent | 14 | 0.23 | 1 | 6 | 0 | 2026-08-25T16:49:59.853000+00:00 | 2026-08-25T18:37:41.834000+00:00 | 1h 47m |
| soilMachine | 7 | 0.11 | 1 | 1 | 0 | 2026-08-25T18:22:13.981000+00:00 | 2026-08-25T18:24:53.408000+00:00 | 2m 39s |
| TerasGardenBox | 6 | 0.1 | 1 | 1 | 0 | 2026-08-25T18:39:21.572000+00:00 | 2026-08-25T18:40:07.677000+00:00 | 46.1s |
| argumentationAnswerEvent | 6 | 0.1 | 1 | 5 | 0 | 2026-08-25T17:01:39.222000+00:00 | 2026-08-25T18:57:26.940000+00:00 | 1h 55m |
| EndOfUnit | 5 | 0.08 | 1 | 5 | 0 | 2026-08-25T17:04:54.015000+00:00 | 2026-08-25T19:06:27.532000+00:00 | 2h 1m |
| gameStartEvent | 5 | 0.08 | 1 | 1 | 0 | 2026-08-25T16:49:32.562000+00:00 | 2026-08-25T18:44:25.787000+00:00 | 1h 54m |
| SolarStillDesignEvent | 4 | 0.07 | 1 | 1 | 0 | 2026-08-25T19:03:59.044000+00:00 | 2026-08-25T19:04:07.237000+00:00 | 8.2s |
| DEBUGMenu | 2 | 0.03 | 1 | 1 | 0 | 2026-08-25T18:18:56.422000+00:00 | 2026-08-25T18:19:00.867000+00:00 | 4.4s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 4.445s median 
  - Expected: 2.008s in 08-13-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `DaniEvent` — median interval between records changed substantially. 
  - Observed: 11.039s median 
  - Expected: 1.859s in 08-13-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 293.986s median 
  - Expected: 142.327s in 08-13-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 15.582s median 
  - Expected: 35.166s in 08-13-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `EndOfUnit` `data.Unit` — categorical value(s) not seen in baseline. 
  - Observed: 1; 2; 3 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Descend 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Inspect Alien Glyph; Press E to Collect; Press E to Place; Press E to Scan; Press [E/Action button] to enter escape pod  
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.objectName` — categorical value(s) not seen in baseline. 
  - Observed: Alien Glyph; Crash Pod; Eastern Ocean; Eastern River Distance; Eastern River Salinity; Eastern River Waterfall Flow; Eastern River Waterfall Height; Glyph Socket 1; Glyph Socket 2; Glyph Socket 3; Glyph Socket 4; Glyph Socket 5; Glyph Socket 6; Soil Key; Soil Key Puzzle Soil Key Room; Soil Key Puzzle Soil Outside Temple; Topography Piece 1; Topography Piece 2; Topography Piece 3; Topography Piece 4; Topography Piece 5; Topography Piece 6; Western River Distance; Western River Salinity; Western River Waterfall Flow; Western River Waterfall Height 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 1137 records 
  - Expected: 346 in 08-13-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — categorical value(s) not seen in baseline. 
  - Observed: Topography Piece 1; Topography Piece 2; Topography Piece 3; Topography Piece 4; Topography Piece 5; Topography Piece 6; Topography Slot 1; Topography Slot 2; Topography Slot 3; Topography Slot 4; Topography Slot 5; Topography Slot 6; Watershed Piece 1; Watershed Piece 2; Watershed Piece 3; Watershed Piece 4; WatershedSlotWall 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — categorical value(s) not seen in baseline. 
  - Observed: Unit 2 Prod (Refactor) 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — event type not present in baseline 08-13-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: dragEnd 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: Waypoint 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: C,D,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 2 – Watershed 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — categorical value(s) not seen in baseline. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 2 – Watershed 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 2 – Watershed 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 2 – Watershed 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — baseline categorical value(s) not seen this build. 
  - Observed: [31-45, 31-48, 31-68, 31-83, 31-84]; [31-51, 31-67, 31-69, 31-70]; [31-55, 31-65, 31-56, 31-59, 31-60]; [31-68, 31-83, 31-84, 31-51, 31-67]; [31-69, 31-70, 31-71, 31-72, 31-73]; [31-71, 31-72, 31-73, 31-74, 31-78]; [31-74, 31-78, 31-82, 70-0, 70-7, 31-55]; [70-0, 70-7, 31-55, 31-65, 31-56, 31-59]; [95-1, 95-4, 95-5, 95-76, 95-77, 95-78]; [95-11, 95-35, 95-83, 95-79, 95-36, 95-37]; [95-36, 95-37, 95-38, 95-36, 95-39, 95-40]; [95-37, 95-38, 95-36, 95-39, 95-40]; [95-76, 95-77, 95-78, 100-44, 95-80, 95-32]; [95-80, 95-32, 95-81, 95-82, 95-35]; [95-82, 95-35, 95-8, 95-9, 95-11, 95-35] 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [16-3, 18-1, 18-2, 18-4, 18-5, 18-7]; [16-3, 18-1, 18-2, 18-4, 18-5]; [17-19, 17-20, 17-22, 17-26, 18-21, 18-22]; [17-22, 17-26, 18-21, 18-22, 18-24, 18-25, 18-33]; [17-22, 17-26, 18-21, 18-22, 18-24]; [18-10, 17-17, 17-19, 17-20, 17-22, 17-26]; [18-22, 18-24, 18-25, 18-33, 18-34, 18-35]; [18-33, 18-34, 18-35, 18-36, 18-37, 18-38, 18-39]; [18-34, 18-35, 18-36, 18-37, 18-38, 18-39]; [18-37, 18-38, 18-39, 18-269, 18-271, 18-273]; [18-38, 18-39, 18-269, 18-271, 18-273]; [18-4, 18-5, 18-7, 18-8, 18-10, 17-17]; [18-4, 18-5, 18-7, 18-8, 18-10]; [18-8, 18-10, 17-17, 17-19, 17-20, 17-22] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — categorical value(s) not seen in baseline. 
  - Observed: 22; 23; 24; 25; 54 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questName` — categorical value(s) not seen in baseline. 
  - Observed: Claim of Command; Foraged Forging; Getting the Band Back Together; Investigate the Temple; Which Watershed? 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 15 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5986] _id=6a8dc8bd485cab4c953bf41e ts=2026-08-25T16:54:21.8990000Z`; `wenyi082526-1.stratalog.logdata.json[5945] _id=6a8dc953485cab4c953bf470 ts=2026-08-25T16:56:51.8700000Z`; `wenyi082526-1.stratalog.logdata.json[5895] _id=6a8dc9bc485cab4c953bf5aa ts=2026-08-25T16:58:37.8220000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 5 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 5} 
  - Examples: `wenyi082526-1.stratalog.logdata.json[6123] _id=6a8dc79b485cab4c953bf255 ts=2026-08-25T16:49:32.5620000Z`; `wenyi082526-1.stratalog.logdata.json[5646] _id=6a8dcba2485cab4c953bf83e ts=2026-08-25T17:06:43.4380000Z`; `wenyi082526-1.stratalog.logdata.json[3577] _id=6a8dd495485cab4c953c0b82 ts=2026-08-25T17:44:54.2670000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `wenyi082526-1.stratalog.logdata.json[6114] _id=6a8dc7bd485cab4c953bf281 ts=2026-08-25T16:50:05.9140000Z`; `wenyi082526-1.stratalog.logdata.json[6105] _id=6a8dc7f3485cab4c953bf2af ts=2026-08-25T16:51:00.5580000Z`; `wenyi082526-1.stratalog.logdata.json[6017] _id=6a8dc88f485cab4c953bf3e0 ts=2026-08-25T16:53:36.1360000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `wenyi082526-1.stratalog.logdata.json[6118] _id=6a8dc7b6485cab4c953bf273 ts=2026-08-25T16:49:59.8530000Z`; `wenyi082526-1.stratalog.logdata.json[6111] _id=6a8dc7c1485cab4c953bf289 ts=2026-08-25T16:50:09.8960000Z`; `wenyi082526-1.stratalog.logdata.json[6021] _id=6a8dc871485cab4c953bf3a4 ts=2026-08-25T16:53:06.7750000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1861 | 0.0 | 0.55 | 4.33 | 12.49 | 553.565 | 13.86 | 63 | 0 |
| DialogueEvent | 1758 | 0.0 | 0.667 | 4.654 | 18.454 | 539.79 | 12.89 | 487 | 0 |
| PuzzlePieceVisibleEvent | 1136 | 0.0 | 0.032 | 4.113 | 0.905 | 2060.739 | 14.59 | 717 | 3 |
| PlayerPositionEvent | 716 | 9.987 | 10.005 | 10.317 | 10.006 | 81.422 | 5.82 | 0 | 0 |
| argumentationNodeEvent | 166 | 0.014 | 0.326 | 41.86 | 11.039 | 2126.349 | 1.43 | 41 | 4 |
| ObjectInterEvent | 80 | 0.001 | 11.896 | 89.054 | 591.065 | 1409.607 | 0.67 | 1 | 4 |
| DaniEvent | 79 | 0.0 | 11.039 | 96.985 | 558.704 | 1461.252 | 0.62 | 30 | 3 |
| questEvent | 67 | 0.0 | 72.317 | 121.479 | 429.422 | 721.411 | 0.49 | 13 | 1 |
| TopographicMapEvent | 54 | 0.417 | 2.343 | 68.419 | 170.529 | 2239.287 | 0.88 | 0 | 2 |
| chatEvent | 37 | 0.033 | 0.282 | 0.31 | 0.499 | 1.564 | 193.84 | 3 | 0 |
| Soil Key Puzzle | 33 | 0.301 | 0.9 | 122.757 | 843.847 | 2187.946 | 0.49 | 0 | 2 |
| WaterChamberEvent | 21 | 1.034 | 15.603 | 16.195 | 34.567 | 37.251 | 3.7 | 0 | 0 |
| argumentationToolEvent | 15 | 0.551 | 6.502 | 463.607 | 2482.135 | 3669.237 | 0.13 | 0 | 3 |
| argumentationEvent | 13 | 0.014 | 40.506 | 534.961 | 2025.053 | 2118.279 | 0.11 | 2 | 4 |
| gameWindowFocusEvent | 13 | 16.134 | 293.986 | 496.823 | 1354.42 | 1484.895 | 0.12 | 0 | 4 |
| gameWindowUnfocusEvent | 13 | 10.043 | 266.416 | 497.075 | 1351.345 | 1481.014 | 0.12 | 0 | 4 |
| soilMachine | 6 | 2.668 | 15.582 | 26.571 | 66.168 | 71.333 | 2.26 | 0 | 0 |
| TerasGardenBox | 5 | 1.484 | 1.951 | 9.221 | 21.227 | 21.794 | 6.51 | 0 | 0 |
| argumentationAnswerEvent | 5 | 25.879 | 1574.218 | 1389.544 | 2132.169 | 2166.619 | 0.04 | 0 | 4 |
| EndOfUnit | 4 | 1330.201 | 1907.095 | 1823.379 | 2117.981 | 2149.126 | 0.03 | 0 | 4 |
| gameStartEvent | 4 | 1030.876 | 1785.76 | 1723.306 | 2229.727 | 2290.829 | 0.03 | 0 | 4 |
| SolarStillDesignEvent | 3 | 1.284 | 2.635 | 2.731 | 4.11 | 4.274 | 21.97 | 0 | 0 |
| DEBUGMenu | 1 | 4.445 | 4.445 | 4.445 | 4.445 | 4.445 | 13.5 | 0 | 0 |

- **WARNING / Medium** `DaniEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 5 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5644] _id=6a8dcba5485cab4c953bf842 ts=2026-08-25T17:06:45.7560000Z == wenyi082526-1.stratalog.logdata.json[5643] _id=6a8dcba5485cab4c953bf844 ts=2026-08-25T17:06:45.7560000Z`; `wenyi082526-1.stratalog.logdata.json[5450] _id=6a8dcc2f485cab4c953bf96e ts=2026-08-25T17:09:04.7690000Z == wenyi082526-1.stratalog.logdata.json[5449] _id=6a8dcc2f485cab4c953bf970 ts=2026-08-25T17:09:04.7690000Z`; `wenyi082526-1.stratalog.logdata.json[5395] _id=6a8dcc42485cab4c953bf9da ts=2026-08-25T17:09:23.5120000Z == wenyi082526-1.stratalog.logdata.json[5396] _id=6a8dcc42485cab4c953bf9dc ts=2026-08-25T17:09:23.5120000Z`
- **WARNING / Medium** `DialogueEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi082526-1.stratalog.logdata.json[2465] _id=6a8dda07485cab4c953c1612 ts=2026-08-25T18:08:08.7470000Z == wenyi082526-1.stratalog.logdata.json[2466] _id=6a8dda07485cab4c953c1614 ts=2026-08-25T18:08:08.7470000Z`
- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi082526-1.stratalog.logdata.json[1727] _id=6a8ddda0485cab4c953c1bd8 ts=2026-08-25T18:23:29.7690000Z == wenyi082526-1.stratalog.logdata.json[1728] _id=6a8ddda0485cab4c953c1bda ts=2026-08-25T18:23:29.7690000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 19 group(s), 25 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5516] _id=6a8dcc1e485cab4c953bf908 ts=2026-08-25T17:08:47.5950000Z == wenyi082526-1.stratalog.logdata.json[5517] _id=6a8dcc1e485cab4c953bf90a ts=2026-08-25T17:08:47.5950000Z`; `wenyi082526-1.stratalog.logdata.json[5514] _id=6a8dcc1f485cab4c953bf90c ts=2026-08-25T17:08:47.6280000Z == wenyi082526-1.stratalog.logdata.json[5515] _id=6a8dcc1f485cab4c953bf90e ts=2026-08-25T17:08:47.6280000Z`; `wenyi082526-1.stratalog.logdata.json[5509] _id=6a8dcc1f485cab4c953bf918 ts=2026-08-25T17:08:47.7110000Z == wenyi082526-1.stratalog.logdata.json[5510] _id=6a8dcc1f485cab4c953bf91a ts=2026-08-25T17:08:47.7110000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: wenyi082526-1.stratalog.logdata.json[5643] _id=6a8dcba5485cab4c953bf844 ts=2026-08-25T17:06:45.7560000Z ~ wenyi082526-1.stratalog.logdata.json[5642] _id=6a8dcba5485cab4c953bf846 ts=2026-08-25T17:06:45.7840000Z`; `1ms: wenyi082526-1.stratalog.logdata.json[5642] _id=6a8dcba5485cab4c953bf846 ts=2026-08-25T17:06:45.7840000Z ~ wenyi082526-1.stratalog.logdata.json[5641] _id=6a8dcba5485cab4c953bf848 ts=2026-08-25T17:06:45.7850000Z`; `1ms: wenyi082526-1.stratalog.logdata.json[5641] _id=6a8dcba5485cab4c953bf848 ts=2026-08-25T17:06:45.7850000Z ~ wenyi082526-1.stratalog.logdata.json[5640] _id=6a8dcba5485cab4c953bf84a ts=2026-08-25T17:06:45.7860000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi082526-1.stratalog.logdata.json[6027] _id=6a8dc86d485cab4c953bf38a ts=2026-08-25T16:53:01.9580000Z ~ wenyi082526-1.stratalog.logdata.json[6026] _id=6a8dc86d485cab4c953bf38c ts=2026-08-25T16:53:01.9590000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 38 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `285ms: wenyi082526-1.stratalog.logdata.json[5367] _id=6a8dcc50485cab4c953bfa78 ts=2026-08-25T17:09:33.2310000Z ~ wenyi082526-1.stratalog.logdata.json[5365] _id=6a8dcc50485cab4c953bfa7a ts=2026-08-25T17:09:33.5160000Z`; `85ms: wenyi082526-1.stratalog.logdata.json[5349] _id=6a8dcc51485cab4c953bfa9c ts=2026-08-25T17:09:35.4990000Z ~ wenyi082526-1.stratalog.logdata.json[5348] _id=6a8dcc51485cab4c953bfa9e ts=2026-08-25T17:09:35.5840000Z`; `133ms: wenyi082526-1.stratalog.logdata.json[5342] _id=6a8dcc51485cab4c953bfaaa ts=2026-08-25T17:09:36.6160000Z ~ wenyi082526-1.stratalog.logdata.json[5341] _id=6a8dcc51485cab4c953bfaae ts=2026-08-25T17:09:36.7490000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `651ms: wenyi082526-1.stratalog.logdata.json[2428] _id=6a8dda4c485cab4c953c165e ts=2026-08-25T18:09:17.9280000Z ~ wenyi082526-1.stratalog.logdata.json[2427] _id=6a8dda4d485cab4c953c1660 ts=2026-08-25T18:09:18.5790000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi082526-1.stratalog.logdata.json[3154] _id=6a8dd6f9485cab4c953c0f6e ts=2026-08-25T17:55:06.1070000Z ~ wenyi082526-1.stratalog.logdata.json[3151] _id=6a8dd6f9485cab4c953c0f74 ts=2026-08-25T17:55:06.1210000Z`; `14ms: wenyi082526-1.stratalog.logdata.json[1196] _id=6a8ddf6f485cab4c953c2000 ts=2026-08-25T18:31:12.7250000Z ~ wenyi082526-1.stratalog.logdata.json[1192] _id=6a8ddf70485cab4c953c2006 ts=2026-08-25T18:31:12.7390000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi082526-1.stratalog.logdata.json[5785] _id=6a8dca6d485cab4c953bf726 ts=2026-08-25T17:01:34.5550000Z ~ wenyi082526-1.stratalog.logdata.json[5784] _id=6a8dca6d485cab4c953bf728 ts=2026-08-25T17:01:34.5690000Z`; `14ms: wenyi082526-1.stratalog.logdata.json[5778] _id=6a8dca6f485cab4c953bf734 ts=2026-08-25T17:01:36.3390000Z ~ wenyi082526-1.stratalog.logdata.json[5777] _id=6a8dca6f485cab4c953bf736 ts=2026-08-25T17:01:36.3530000Z`; `15ms: wenyi082526-1.stratalog.logdata.json[5774] _id=6a8dca70485cab4c953bf73c ts=2026-08-25T17:01:37.4060000Z ~ wenyi082526-1.stratalog.logdata.json[5773] _id=6a8dca70485cab4c953bf73e ts=2026-08-25T17:01:37.4210000Z`
- **INFO / Info** `chatEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `500ms: wenyi082526-1.stratalog.logdata.json[5433] _id=6a8dcc38485cab4c953bf990 ts=2026-08-25T17:09:13.6220000Z ~ wenyi082526-1.stratalog.logdata.json[5431] _id=6a8dcc39485cab4c953bf994 ts=2026-08-25T17:09:14.1220000Z`; `167ms: wenyi082526-1.stratalog.logdata.json[5431] _id=6a8dcc39485cab4c953bf994 ts=2026-08-25T17:09:14.1220000Z ~ wenyi082526-1.stratalog.logdata.json[5430] _id=6a8dcc39485cab4c953bf996 ts=2026-08-25T17:09:14.2890000Z`; `50ms: wenyi082526-1.stratalog.logdata.json[5429] _id=6a8dcc39485cab4c953bf998 ts=2026-08-25T17:09:14.4740000Z ~ wenyi082526-1.stratalog.logdata.json[5428] _id=6a8dcc39485cab4c953bf99a ts=2026-08-25T17:09:14.5240000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi082526-1.stratalog.logdata.json[207] _id=6a8de5d1485cab4c953c2bc0 ts=2026-08-25T18:58:26.0700000Z ~ wenyi082526-1.stratalog.logdata.json[206] _id=6a8de5d1485cab4c953c2bc2 ts=2026-08-25T18:58:26.0710000Z`; `1ms: wenyi082526-1.stratalog.logdata.json[76] _id=6a8de763485cab4c953c2cc6 ts=2026-08-25T19:05:08.8610000Z ~ wenyi082526-1.stratalog.logdata.json[75] _id=6a8de763485cab4c953c2cc8 ts=2026-08-25T19:05:08.8620000Z`
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 24m 21s 
  - Evidence: 24m 21s: wenyi082526-1.stratalog.logdata.json[1169] _id=6a8ddf95485cab4c953c2036 ts=2026-08-25T18:31:50.0530000Z -> wenyi082526-1.stratalog.logdata.json[309] _id=6a8de54a485cab4c953c2af4 ts=2026-08-25T18:56:11.3050000Z; 12m 8s: wenyi082526-1.stratalog.logdata.json[6121] _id=6a8dc7a9485cab4c953bf269 ts=2026-08-25T16:49:45.1220000Z -> wenyi082526-1.stratalog.logdata.json[5765] _id=6a8dca80485cab4c953bf74e ts=2026-08-25T17:01:53.1460000Z; 10m 9s: wenyi082526-1.stratalog.logdata.json[4551] _id=6a8dcee2485cab4c953c00ce ts=2026-08-25T17:20:34.9990000Z -> wenyi082526-1.stratalog.logdata.json[3923] _id=6a8dd144485cab4c953c05d6 ts=2026-08-25T17:30:44.9410000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 30 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi082526-1.stratalog.logdata.json[1341] _id=6a8ddebc485cab4c953c1ede ts=2026-08-25T18:28:13.0760000Z -> wenyi082526-1.stratalog.logdata.json[1340] _id=6a8ddebc485cab4c953c1ee0 ts=2026-08-25T18:28:13.0760000Z; 0ms: wenyi082526-1.stratalog.logdata.json[2149] _id=6a8ddc96485cab4c953c188c ts=2026-08-25T18:19:02.6380000Z -> wenyi082526-1.stratalog.logdata.json[2150] _id=6a8ddc96485cab4c953c188e ts=2026-08-25T18:19:02.6380000Z; 0ms: wenyi082526-1.stratalog.logdata.json[5395] _id=6a8dcc42485cab4c953bf9da ts=2026-08-25T17:09:23.5120000Z -> wenyi082526-1.stratalog.logdata.json[5396] _id=6a8dcc42485cab4c953bf9dc ts=2026-08-25T17:09:23.5120000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 487 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi082526-1.stratalog.logdata.json[1018] _id=6a8de188485cab4c953c2208 ts=2026-08-25T18:40:09.1810000Z -> wenyi082526-1.stratalog.logdata.json[1017] _id=6a8de188485cab4c953c220a ts=2026-08-25T18:40:09.1810000Z; 0ms: wenyi082526-1.stratalog.logdata.json[101] _id=6a8de744485cab4c953c2c92 ts=2026-08-25T19:04:37.9150000Z -> wenyi082526-1.stratalog.logdata.json[102] _id=6a8de745485cab4c953c2c94 ts=2026-08-25T19:04:37.9150000Z; 0ms: wenyi082526-1.stratalog.logdata.json[1050] _id=6a8de15c485cab4c953c2170 ts=2026-08-25T18:39:24.9940000Z -> wenyi082526-1.stratalog.logdata.json[1051] _id=6a8de15c485cab4c953c2172 ts=2026-08-25T18:39:24.9940000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 35m 49s 
  - Evidence: 35m 49s: wenyi082526-1.stratalog.logdata.json[3579] _id=6a8dd285485cab4c953c0ae2 ts=2026-08-25T17:36:06.7100000Z -> wenyi082526-1.stratalog.logdata.json[2313] _id=6a8ddaea485cab4c953c1744 ts=2026-08-25T18:11:55.8360000Z; 32m 21s: wenyi082526-1.stratalog.logdata.json[2313] _id=6a8ddaea485cab4c953c1744 ts=2026-08-25T18:11:55.8360000Z -> wenyi082526-1.stratalog.logdata.json[876] _id=6a8de280485cab4c953c2388 ts=2026-08-25T18:44:17.3310000Z; 31m 12s: wenyi082526-1.stratalog.logdata.json[5649] _id=6a8dcb35485cab4c953bf836 ts=2026-08-25T17:04:54.0150000Z -> wenyi082526-1.stratalog.logdata.json[3579] _id=6a8dd285485cab4c953c0ae2 ts=2026-08-25T17:36:06.7100000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 63 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi082526-1.stratalog.logdata.json[1727] _id=6a8ddda0485cab4c953c1bd8 ts=2026-08-25T18:23:29.7690000Z -> wenyi082526-1.stratalog.logdata.json[1728] _id=6a8ddda0485cab4c953c1bda ts=2026-08-25T18:23:29.7690000Z; 1ms: wenyi082526-1.stratalog.logdata.json[4491] _id=6a8dcf26485cab4c953c0144 ts=2026-08-25T17:21:43.0300000Z -> wenyi082526-1.stratalog.logdata.json[4490] _id=6a8dcf26485cab4c953c0146 ts=2026-08-25T17:21:43.0310000Z; 1ms: wenyi082526-1.stratalog.logdata.json[5116] _id=6a8dcc63485cab4c953bfc48 ts=2026-08-25T17:09:56.1760000Z -> wenyi082526-1.stratalog.logdata.json[5115] _id=6a8dcc63485cab4c953bfc4c ts=2026-08-25T17:09:56.1770000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 23m 29s 
  - Evidence: 23m 29s: wenyi082526-1.stratalog.logdata.json[1609] _id=6a8dddee485cab4c953c1cc6 ts=2026-08-25T18:24:47.4040000Z -> wenyi082526-1.stratalog.logdata.json[756] _id=6a8de370485cab4c953c2662 ts=2026-08-25T18:48:17.0110000Z; 23m 16s: wenyi082526-1.stratalog.logdata.json[3716] _id=6a8dd219485cab4c953c0938 ts=2026-08-25T17:34:18.4750000Z -> wenyi082526-1.stratalog.logdata.json[3077] _id=6a8dd78d485cab4c953c1008 ts=2026-08-25T17:57:34.7270000Z; 12m 54s: wenyi082526-1.stratalog.logdata.json[2576] _id=6a8dd969485cab4c953c14f4 ts=2026-08-25T18:05:30.7520000Z -> wenyi082526-1.stratalog.logdata.json[2236] _id=6a8ddc70485cab4c953c17e0 ts=2026-08-25T18:18:24.9740000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: wenyi082526-1.stratalog.logdata.json[6027] _id=6a8dc86d485cab4c953bf38a ts=2026-08-25T16:53:01.9580000Z -> wenyi082526-1.stratalog.logdata.json[6026] _id=6a8dc86d485cab4c953bf38c ts=2026-08-25T16:53:01.9590000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 34m 20s 
  - Evidence: 34m 20s: wenyi082526-1.stratalog.logdata.json[4102] _id=6a8dcfa4485cab4c953c045a ts=2026-08-25T17:23:47.1390000Z -> wenyi082526-1.stratalog.logdata.json[3050] _id=6a8dd7b0485cab4c953c1042 ts=2026-08-25T17:58:07.8780000Z; 19m 38s: wenyi082526-1.stratalog.logdata.json[2862] _id=6a8dd7e7485cab4c953c1202 ts=2026-08-25T17:59:02.5330000Z -> wenyi082526-1.stratalog.logdata.json[2220] _id=6a8ddc80485cab4c953c17fc ts=2026-08-25T18:18:41.1470000Z; 11m 2s: wenyi082526-1.stratalog.logdata.json[4842] _id=6a8dcc7d485cab4c953bfe86 ts=2026-08-25T17:10:20.8050000Z -> wenyi082526-1.stratalog.logdata.json[4506] _id=6a8dcf13485cab4c953c0126 ts=2026-08-25T17:21:23.2220000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 717 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi082526-1.stratalog.logdata.json[1405] _id=6a8dde41485cab4c953c1e5e ts=2026-08-25T18:26:08.4100000Z -> wenyi082526-1.stratalog.logdata.json[1404] _id=6a8dde41485cab4c953c1e60 ts=2026-08-25T18:26:08.4100000Z; 0ms: wenyi082526-1.stratalog.logdata.json[1407] _id=6a8dde40485cab4c953c1e5a ts=2026-08-25T18:26:08.3940000Z -> wenyi082526-1.stratalog.logdata.json[1406] _id=6a8dde40485cab4c953c1e5c ts=2026-08-25T18:26:08.3940000Z; 0ms: wenyi082526-1.stratalog.logdata.json[1412] _id=6a8dde3f485cab4c953c1e4e ts=2026-08-25T18:26:07.6770000Z -> wenyi082526-1.stratalog.logdata.json[1413] _id=6a8dde3f485cab4c953c1e50 ts=2026-08-25T18:26:07.6770000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 36m 27s 
  - Evidence: 36m 27s: wenyi082526-1.stratalog.logdata.json[4527] _id=6a8dcf01485cab4c953c00fc ts=2026-08-25T17:21:06.7800000Z -> wenyi082526-1.stratalog.logdata.json[3078] _id=6a8dd78d485cab4c953c1006 ts=2026-08-25T17:57:34.7260000Z; 20m 34s: wenyi082526-1.stratalog.logdata.json[3064] _id=6a8dd79d485cab4c953c1022 ts=2026-08-25T17:57:50.8000000Z -> wenyi082526-1.stratalog.logdata.json[2237] _id=6a8ddc70485cab4c953c17de ts=2026-08-25T18:18:24.9730000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 37m 19s 
  - Evidence: 37m 19s: wenyi082526-1.stratalog.logdata.json[3917] _id=6a8dd151485cab4c953c05ee ts=2026-08-25T17:30:58.5300000Z -> wenyi082526-1.stratalog.logdata.json[2463] _id=6a8dda10485cab4c953c1618 ts=2026-08-25T18:08:17.8170000Z; 10m 9s: wenyi082526-1.stratalog.logdata.json[4550] _id=6a8dcee2485cab4c953c00cc ts=2026-08-25T17:20:34.9990000Z -> wenyi082526-1.stratalog.logdata.json[3922] _id=6a8dd144485cab4c953c05d8 ts=2026-08-25T17:30:44.9420000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 36m 6s 
  - Evidence: 36m 6s: wenyi082526-1.stratalog.logdata.json[3156] _id=6a8dd6f9485cab4c953c0f6a ts=2026-08-25T17:55:06.1030000Z -> wenyi082526-1.stratalog.logdata.json[1198] _id=6a8ddf6f485cab4c953c1ffc ts=2026-08-25T18:31:12.7220000Z; 33m 14s: wenyi082526-1.stratalog.logdata.json[5747] _id=6a8dca8c485cab4c953bf772 ts=2026-08-25T17:02:05.1010000Z -> wenyi082526-1.stratalog.logdata.json[3653] _id=6a8dd256485cab4c953c0a36 ts=2026-08-25T17:35:19.4700000Z; 26m 14s: wenyi082526-1.stratalog.logdata.json[1198] _id=6a8ddf6f485cab4c953c1ffc ts=2026-08-25T18:31:12.7220000Z -> wenyi082526-1.stratalog.logdata.json[256] _id=6a8de595485cab4c953c2b5e ts=2026-08-25T18:57:26.9400000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 35m 18s 
  - Evidence: 35m 18s: wenyi082526-1.stratalog.logdata.json[3151] _id=6a8dd6f9485cab4c953c0f74 ts=2026-08-25T17:55:06.1210000Z -> wenyi082526-1.stratalog.logdata.json[1240] _id=6a8ddf3f485cab4c953c1fa8 ts=2026-08-25T18:30:24.4000000Z; 32m 42s: wenyi082526-1.stratalog.logdata.json[5745] _id=6a8dca8c485cab4c953bf776 ts=2026-08-25T17:02:05.1040000Z -> wenyi082526-1.stratalog.logdata.json[3682] _id=6a8dd237485cab4c953c09da ts=2026-08-25T17:34:48.0070000Z; 24m 59s: wenyi082526-1.stratalog.logdata.json[1192] _id=6a8ddf70485cab4c953c2006 ts=2026-08-25T18:31:12.7390000Z -> wenyi082526-1.stratalog.logdata.json[307] _id=6a8de54b485cab4c953c2af8 ts=2026-08-25T18:56:12.1380000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.014s..0.014s shown 
  - Evidence: 14ms: wenyi082526-1.stratalog.logdata.json[1196] _id=6a8ddf6f485cab4c953c2000 ts=2026-08-25T18:31:12.7250000Z -> wenyi082526-1.stratalog.logdata.json[1192] _id=6a8ddf70485cab4c953c2006 ts=2026-08-25T18:31:12.7390000Z; 14ms: wenyi082526-1.stratalog.logdata.json[3154] _id=6a8dd6f9485cab4c953c0f6e ts=2026-08-25T17:55:06.1070000Z -> wenyi082526-1.stratalog.logdata.json[3151] _id=6a8dd6f9485cab4c953c0f74 ts=2026-08-25T17:55:06.1210000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 35m 26s 
  - Evidence: 35m 26s: wenyi082526-1.stratalog.logdata.json[3159] _id=6a8dd6f4485cab4c953c0f64 ts=2026-08-25T17:55:01.6010000Z -> wenyi082526-1.stratalog.logdata.json[1237] _id=6a8ddf42485cab4c953c1fae ts=2026-08-25T18:30:27.9500000Z; 25m 40s: wenyi082526-1.stratalog.logdata.json[5439] _id=6a8dcc35485cab4c953bf984 ts=2026-08-25T17:09:10.0200000Z -> wenyi082526-1.stratalog.logdata.json[3679] _id=6a8dd23a485cab4c953c09e4 ts=2026-08-25T17:34:50.9570000Z; 25m 8s: wenyi082526-1.stratalog.logdata.json[1199] _id=6a8ddf6b485cab4c953c1ffa ts=2026-08-25T18:31:08.7030000Z -> wenyi082526-1.stratalog.logdata.json[302] _id=6a8de550485cab4c953c2b02 ts=2026-08-25T18:56:17.3740000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 41 interval(s) ≤ 0.014s..0.015s shown 
  - Evidence: 14ms: wenyi082526-1.stratalog.logdata.json[5778] _id=6a8dca6f485cab4c953bf734 ts=2026-08-25T17:01:36.3390000Z -> wenyi082526-1.stratalog.logdata.json[5777] _id=6a8dca6f485cab4c953bf736 ts=2026-08-25T17:01:36.3530000Z; 14ms: wenyi082526-1.stratalog.logdata.json[5785] _id=6a8dca6d485cab4c953bf726 ts=2026-08-25T17:01:34.5550000Z -> wenyi082526-1.stratalog.logdata.json[5784] _id=6a8dca6d485cab4c953bf728 ts=2026-08-25T17:01:34.5690000Z; 15ms: wenyi082526-1.stratalog.logdata.json[5774] _id=6a8dca70485cab4c953bf73c ts=2026-08-25T17:01:37.4060000Z -> wenyi082526-1.stratalog.logdata.json[5773] _id=6a8dca70485cab4c953bf73e ts=2026-08-25T17:01:37.4210000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 1h 1m 
  - Evidence: 1h 1m: wenyi082526-1.stratalog.logdata.json[3157] _id=6a8dd6f7485cab4c953c0f68 ts=2026-08-25T17:55:04.3030000Z -> wenyi082526-1.stratalog.logdata.json[304] _id=6a8de54c485cab4c953c2afe ts=2026-08-25T18:56:13.5400000Z; 32m 53s: wenyi082526-1.stratalog.logdata.json[5748] _id=6a8dca8a485cab4c953bf770 ts=2026-08-25T17:02:03.4500000Z -> wenyi082526-1.stratalog.logdata.json[3669] _id=6a8dd23f485cab4c953c09fa ts=2026-08-25T17:34:56.8270000Z; 19m 24s: wenyi082526-1.stratalog.logdata.json[3667] _id=6a8dd246485cab4c953c0a00 ts=2026-08-25T17:35:03.3290000Z -> wenyi082526-1.stratalog.logdata.json[3207] _id=6a8dd6d2485cab4c953c0f04 ts=2026-08-25T17:54:27.8190000Z
- **INFO / Info** `chatEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.033s..0.050s shown 
  - Evidence: 33ms: wenyi082526-1.stratalog.logdata.json[5403] _id=6a8dcc40485cab4c953bf9cc ts=2026-08-25T17:09:21.8110000Z -> wenyi082526-1.stratalog.logdata.json[5402] _id=6a8dcc40485cab4c953bf9ce ts=2026-08-25T17:09:21.8440000Z; 33ms: wenyi082526-1.stratalog.logdata.json[5405] _id=6a8dcc40485cab4c953bf9c8 ts=2026-08-25T17:09:21.6090000Z -> wenyi082526-1.stratalog.logdata.json[5404] _id=6a8dcc40485cab4c953bf9ca ts=2026-08-25T17:09:21.6420000Z; 50ms: wenyi082526-1.stratalog.logdata.json[5429] _id=6a8dcc39485cab4c953bf998 ts=2026-08-25T17:09:14.4740000Z -> wenyi082526-1.stratalog.logdata.json[5428] _id=6a8dcc39485cab4c953bf99a ts=2026-08-25T17:09:14.5240000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 38m 10s 
  - Evidence: 38m 10s: wenyi082526-1.stratalog.logdata.json[5646] _id=6a8dcba2485cab4c953bf83e ts=2026-08-25T17:06:43.4380000Z -> wenyi082526-1.stratalog.logdata.json[3577] _id=6a8dd495485cab4c953c0b82 ts=2026-08-25T17:44:54.2670000Z; 31m 23s: wenyi082526-1.stratalog.logdata.json[2311] _id=6a8ddb2d485cab4c953c174a ts=2026-08-25T18:13:02.3060000Z -> wenyi082526-1.stratalog.logdata.json[874] _id=6a8de288485cab4c953c238e ts=2026-08-25T18:44:25.7870000Z; 28m 8s: wenyi082526-1.stratalog.logdata.json[3577] _id=6a8dd495485cab4c953c0b82 ts=2026-08-25T17:44:54.2670000Z -> wenyi082526-1.stratalog.logdata.json[2311] _id=6a8ddb2d485cab4c953c174a ts=2026-08-25T18:13:02.3060000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 24m 44s 
  - Evidence: 24m 44s: wenyi082526-1.stratalog.logdata.json[4012] _id=6a8dd04b485cab4c953c0510 ts=2026-08-25T17:26:36.1280000Z -> wenyi082526-1.stratalog.logdata.json[3442] _id=6a8dd618485cab4c953c0d2e ts=2026-08-25T17:51:21.0230000Z; 21m 7s: wenyi082526-1.stratalog.logdata.json[2269] _id=6a8ddc04485cab4c953c179e ts=2026-08-25T18:16:37.1770000Z -> wenyi082526-1.stratalog.logdata.json[1118] _id=6a8de0f7485cab4c953c209c ts=2026-08-25T18:37:44.6140000Z; 18m 33s: wenyi082526-1.stratalog.logdata.json[5647] _id=6a8dcb57485cab4c953bf83a ts=2026-08-25T17:05:28.4100000Z -> wenyi082526-1.stratalog.logdata.json[4087] _id=6a8dcfb0485cab4c953c046c ts=2026-08-25T17:24:01.5610000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 24m 41s 
  - Evidence: 24m 41s: wenyi082526-1.stratalog.logdata.json[4017] _id=6a8dd03d485cab4c953c0506 ts=2026-08-25T17:26:22.5910000Z -> wenyi082526-1.stratalog.logdata.json[3448] _id=6a8dd606485cab4c953c0d22 ts=2026-08-25T17:51:03.6050000Z; 21m 4s: wenyi082526-1.stratalog.logdata.json[2270] _id=6a8ddc03485cab4c953c179c ts=2026-08-25T18:16:36.9350000Z -> wenyi082526-1.stratalog.logdata.json[1120] _id=6a8de0f4485cab4c953c2098 ts=2026-08-25T18:37:41.8340000Z; 18m 31s: wenyi082526-1.stratalog.logdata.json[5648] _id=6a8dcb53485cab4c953bf838 ts=2026-08-25T17:05:24.5740000Z -> wenyi082526-1.stratalog.logdata.json[4089] _id=6a8dcfab485cab4c953c0468 ts=2026-08-25T17:23:56.0260000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 12m 1s 
  - Evidence: 12m 1s: wenyi082526-1.stratalog.logdata.json[3582] _id=6a8dd284485cab4c953c0adc ts=2026-08-25T17:36:05.4930000Z -> wenyi082526-1.stratalog.logdata.json[3540] _id=6a8dd555485cab4c953c0c54 ts=2026-08-25T17:48:06.9040000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi082526-1.stratalog.logdata.json[5806] _id=6a8dca63485cab4c953bf6fa ts=2026-08-25T17:01:24.3020000Z -> wenyi082526-1.stratalog.logdata.json[5807] _id=6a8dca63485cab4c953bf6fc ts=2026-08-25T17:01:24.3020000Z; 1ms: wenyi082526-1.stratalog.logdata.json[1688] _id=6a8dddbc485cab4c953c1c28 ts=2026-08-25T18:23:57.3650000Z -> wenyi082526-1.stratalog.logdata.json[1687] _id=6a8dddbc485cab4c953c1c2a ts=2026-08-25T18:23:57.3660000Z; 1ms: wenyi082526-1.stratalog.logdata.json[1806] _id=6a8ddd74485cab4c953c1b3c ts=2026-08-25T18:22:45.0470000Z -> wenyi082526-1.stratalog.logdata.json[1805] _id=6a8ddd74485cab4c953c1b3e ts=2026-08-25T18:22:45.0480000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5643] _id=6a8dcba5485cab4c953bf844 ts=2026-08-25T17:06:45.7560000Z`; `wenyi082526-1.stratalog.logdata.json[5642] _id=6a8dcba5485cab4c953bf846 ts=2026-08-25T17:06:45.7840000Z`; `wenyi082526-1.stratalog.logdata.json[5641] _id=6a8dcba5485cab4c953bf848 ts=2026-08-25T17:06:45.7850000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5818] _id=6a8dca4d485cab4c953bf6e4 ts=2026-08-25T17:01:02.8560000Z`; `wenyi082526-1.stratalog.logdata.json[5737] _id=6a8dca91485cab4c953bf786 ts=2026-08-25T17:02:10.7750000Z`; `wenyi082526-1.stratalog.logdata.json[4602] _id=6a8dce40485cab4c953c0066 ts=2026-08-25T17:17:53.4870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 26 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5251] _id=6a8dcc5a485cab4c953bfb5a ts=2026-08-25T17:09:44.4880000Z`; `wenyi082526-1.stratalog.logdata.json[5228] _id=6a8dcc5c485cab4c953bfb90 ts=2026-08-25T17:09:46.1390000Z`; `wenyi082526-1.stratalog.logdata.json[5076] _id=6a8dcc68485cab4c953bfcb8 ts=2026-08-25T17:10:00.6280000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 24 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5501] _id=6a8dcc20485cab4c953bf92a ts=2026-08-25T17:08:47.9930000Z`; `wenyi082526-1.stratalog.logdata.json[5341] _id=6a8dcc51485cab4c953bfaae ts=2026-08-25T17:09:36.7490000Z`; `wenyi082526-1.stratalog.logdata.json[5322] _id=6a8dcc53485cab4c953bfacc ts=2026-08-25T17:09:39.0670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi082526-1.stratalog.logdata.json[3151] _id=6a8dd6f9485cab4c953c0f74 ts=2026-08-25T17:55:06.1210000Z`; `wenyi082526-1.stratalog.logdata.json[1192] _id=6a8ddf70485cab4c953c2006 ts=2026-08-25T18:31:12.7390000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5784] _id=6a8dca6d485cab4c953bf728 ts=2026-08-25T17:01:34.5690000Z`; `wenyi082526-1.stratalog.logdata.json[5777] _id=6a8dca6f485cab4c953bf736 ts=2026-08-25T17:01:36.3530000Z`; `wenyi082526-1.stratalog.logdata.json[5773] _id=6a8dca70485cab4c953bf73e ts=2026-08-25T17:01:37.4210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 15 occurrence(s) 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5449] _id=6a8dcc2f485cab4c953bf970 ts=2026-08-25T17:09:04.7690000Z`; `wenyi082526-1.stratalog.logdata.json[5437] _id=6a8dcc35485cab4c953bf988 ts=2026-08-25T17:09:10.8220000Z`; `wenyi082526-1.stratalog.logdata.json[5395] _id=6a8dcc42485cab4c953bf9da ts=2026-08-25T17:09:23.5120000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 26 occurrence(s) 
  - Examples: `wenyi082526-1.stratalog.logdata.json[4911] _id=6a8dcc78485cab4c953bfe0c ts=2026-08-25T17:10:15.0850000Z`; `wenyi082526-1.stratalog.logdata.json[4854] _id=6a8dcc7c485cab4c953bfe70 ts=2026-08-25T17:10:20.2880000Z`; `wenyi082526-1.stratalog.logdata.json[4348] _id=6a8dcf8a485cab4c953c0266 ts=2026-08-25T17:23:22.0610000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 165 occurrence(s) 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5517] _id=6a8dcc1e485cab4c953bf90a ts=2026-08-25T17:08:47.5950000Z`; `wenyi082526-1.stratalog.logdata.json[5514] _id=6a8dcc1f485cab4c953bf90c ts=2026-08-25T17:08:47.6280000Z`; `wenyi082526-1.stratalog.logdata.json[5515] _id=6a8dcc1f485cab4c953bf90e ts=2026-08-25T17:08:47.6280000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5749] _id=6a8dca8a485cab4c953bf76e ts=2026-08-25T17:02:02.8990000Z`; `wenyi082526-1.stratalog.logdata.json[3158] _id=6a8dd6f6485cab4c953c0f66 ts=2026-08-25T17:55:03.0190000Z`; `wenyi082526-1.stratalog.logdata.json[3157] _id=6a8dd6f7485cab4c953c0f68 ts=2026-08-25T17:55:04.3030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'Open' (totals: 35 open, 45 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'DialogueStartEvent' (totals: 319 start, 316 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'BecameCameraCentered' (totals: 175 open, 190 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 38 unmatched 'BecameVisible' (totals: 393 open, 379 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 13 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 6 unmatched 'questActiveEvent' (totals: 37 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 160 of 6123 adjacent _id pairs reverse in client time; worst 76.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi082526-1.stratalog.logdata.json[5375] _id=6a8dcc4c485cab4c953bfa04 ts=2026-08-25T17:09:32.9810000Z`; `wenyi082526-1.stratalog.logdata.json[5559] _id=6a8dcc4c485cab4c953bfa06 ts=2026-08-25T17:08:17.0280000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.92s, min -76.06s, max +0.99s over 6124 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\gameplay-logs-test\config\coverage\08-25-26.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Single full playthrough by one tester (log shows EndOfUnit for units 1-5).; Debug menu was opened during the session (DEBUGMenu events present). |

No coverage-related findings.

## 9. Event-Type Details

### `InputEvent` — 1862 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (397); Unit 4 Dev - Dungeon (396); Unit 5 Dev - Dungeon (308); Unit 3 Dev (228); Unit 3 Dungeon Dev (215); Unit 1 Dev (122); Unit 4 Dev (99); Unit 5 Dev (64); Unit 4 Dev - Anderson Base (33)
- **Intervals:** median 0.55s (p5 0.07s / p95 12.49s, n=1861)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1862/1862 records)
    "pressed"  x1862
data.actionType  (string, 1862/1862 records)
    "Move"  x1289
    "Interact"  x278
    "Sprint"  x211
    "Ascend"  x37
    "Hoverboard"  x14
    "Jump"  x13
    "Descend"  x11
    "Map"  x7
    "Pause"  x1
    "ToggleDebug"  x1
data.key  (string, 1862/1862 records, 2 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1862/1862 records)
    "Player"  x1619
    "Drone"  x243
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1759 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (493); Unit 3 Dev (268); Unit 4 Dev (240); Unit 5 Dev (213); Unit 1 Dev (187); Unit 3 Dungeon Dev (119); Unit 4 Dev - Dungeon (105); Unit 4 Dev - Anderson Base (69); Unit 5 Dev - Dungeon (65)
- **eventKey:** present on 1124 of 1759 records
- **Intervals:** median 0.67s (p5 0.00s / p95 18.45s, n=1758)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1124; [conversationId, dialogueEventType] x635
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1759/1759 records)
    numeric range 8 .. 118 (52 unique)
data.dialogueEventType  (string, 1759/1759 records)
    "DialogueNodeEvent"  x1124
    "DialogueStartEvent"  x319
    "DialogueFinishEvent"  x316
data.nodeId  (number, 1124/1759 records)
    numeric range 0 .. 290 (216 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PuzzlePieceVisibleEvent` — 1137 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (826); Unit 4 Dev (175); Unit 3 Dungeon Dev (136)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.90s, n=1136)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1137/1137 records)
    "BecameVisible"  x393
    "BecameInvisible"  x379
    "BecameCameraUncentered"  x190
    "BecameCameraCentered"  x175
data.pieceId  (string, 1137/1137 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1137/1137 records)
    864 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 728 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (158); Unit 4 Dev (129); Unit 3 Dev (104); Unit 1 Dev (91); Unit 5 Dev (73); Unit 5 Dev - Dungeon (58); Unit 3 Dungeon Dev (56); Unit 4 Dev - Dungeon (37); Unit 4 Dev - Anderson Base (22)
- **Intervals:** median 10.01s (p5 9.99s / p95 10.01s, n=716)
- **Fields under `data`:**

```text
data.position  (object, 728/728 records)
data.position.x  (number, 728/728 records)
    numeric range -654.123 .. 1557.25 (296 unique)
data.position.y  (number, 728/728 records)
    numeric range -114.326 .. 222.005 (259 unique)
data.position.z  (number, 728/728 records)
    numeric range -1028.76 .. 1797.7 (296 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 167 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (43); Unit 5 Dev (36); Unit 4 Dev - Anderson Base (35); Unit 2 Prod (Refactor) (29); Unit 1 Dev (24)
- **Intervals:** median 0.33s (p5 0.02s / p95 11.04s, n=166)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 167/167 records)
    "argumentationNodeHoverEnd"  x76
    "argumentationNodeHoverStart"  x72
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 167/167 records)
    "Unit 3 - Pollution Upstream"  x43
    "Unit 5"  x36
    "Unit 4 - Flooding"  x35
    "Unit 2 – Watershed"  x29
    "Unit 1 - Argumentation Tutorial"  x15
    "Unit 1 - Freshwater"  x9
data.nodeName  (string, 167/167 records)
    "1"  x31
    "A"  x25
    "I"  x21
    "II"  x17
    "3"  x15
    "2"  x13
    "4"  x12
    "C"  x12
    "D"  x12
    "B"  x6
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 81 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev - Dungeon (20); Unit 1 Dev (14); Unit 3 Dungeon Dev (13); Unit 5 Dev - Dungeon (6); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 11.90s (p5 2.03s / p95 591.07s, n=80)
- **Fields under `data`:**

```text
data.actionType  (string, 81/81 records)
    "Press E to Pick up"  x36
    "Press E to Install"  x11
    "Press E to Scan"  x9
    "TalkTo"  x7
    "Press E to Place"  x6
    "Press E to Operate"  x4
    "E to Talk"  x3
    "Press E to Open Locker"  x2
    "Inspect Alien Glyph"  x1
    "Press E to Collect"  x1
    "Press [E/Action button] to enter escape pod "  x1
data.objectName  (string, 81/81 records)
    35 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `DaniEvent` — 80 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (16); Unit 4 Dev (12); Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (2); Unit 5 Dev (2)
- **Intervals:** median 11.04s (p5 0.00s / p95 558.70s, n=79)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 80/80 records)
    "Close"  x45
    "Open"  x35
data.toolName  (string, 80/80 records, 10 empty-string)
    "Argumentation"  x44
    "Map"  x23
    ""  x10
    "Settings"  x2
    "Chat"  x1
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `questEvent` — 68 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 68 of 68 records
- **Intervals:** median 72.32s (p5 0.00s / p95 429.42s, n=67)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Fields under `data`:**

```text
data.questEventType  (string, 68/68 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x31
data.questID  (string, 68/68 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 68/68 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/68 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 55 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (29); Unit 3 Dev (26)
- **Intervals:** median 2.34s (p5 0.56s / p95 170.53s, n=54)
- **`data` key-set variants:** [actionType, featureUsed, location] x35; [actionType, featureUsed] x20
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "WaypointMoveEvent"  x31
    "MapCloseEvent"  x10
    "MapOpenEvent"  x10
    "WaypointSetEvent"  x3
    "WaypointResetEvent"  x1
data.featureUsed  (string, 55/55 records)
    "Waypoint"  x35
    "Map"  x20
data.location  (object, 35/55 records)
data.location.x  (number, 35/55 records)
    numeric range -273.277 .. 24.4026 (30 unique)
data.location.y  (number, 35/55 records)
    numeric range -157.387 .. 135.766 (25 unique)
data.location.z  (number, 35/55 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `chatEvent` — 38 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (38)
- **Intervals:** median 0.28s (p5 0.05s / p95 0.50s, n=37)
- **`data` key-set variants:** [actionType, chatID] x20; [actionKey, chatID] x18
- **Fields under `data`:**

```text
data.actionKey  (string, 18/38 records)
    "ScrollStop"  x18
data.actionType  (string, 20/38 records)
    "ScrollStart"  x18
    "Close"  x1
    "Open"  x1
data.chatID  (string, 38/38 records)
    15 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `Soil Key Puzzle` — 34 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (12); Unit 4 Dev (10)
- **Intervals:** median 0.90s (p5 0.36s / p95 843.85s, n=33)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x26; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/34 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/34 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 26/34 records)
    "RightDrag"  x16
    "LeftDrag"  x10
data.currentSoilType  (string, 26/34 records)
    "CLAY"  x6
    "CLAYSAND"  x5
    "CLAYROCK"  x4
    "SAND"  x4
    "SANDGRAVEL"  x4
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 26/34 records)
    "false"  x20
    "true"  x6
data.waterLevelStatus  (string, 26/34 records)
    "TooHigh"  x12
    "Proper"  x9
    "TooLow"  x5
data.waterRetentionChange  (string, 26/34 records)
    "Decrease"  x10
    "Increase"  x10
    "NoChange"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 22 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (22)
- **Intervals:** median 15.60s (p5 1.92s / p95 34.57s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "On"  x15
    "Off"  x7
data.floor  (string, 22/22 records)
    "4"  x9
    "3"  x6
    "2"  x5
    "1"  x2
data.machineNumber  (string, 22/22 records)
    "One"  x21
    "Two"  x1
data.machineType  (string, 22/22 records)
    "Condenser"  x13
    "Evaporator"  x6
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 22/22 records)
    "3"  x8
    "1"  x6
    "2"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 5 Dev (5); Unit 3 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 6.50s (p5 0.91s / p95 2482.14s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 16/16 records)
    "Unit 5"  x5
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 40.51s (p5 0.01s / p95 2025.05s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowFocusEvent` — 14 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (4); Unit 3 Dungeon Dev (2); Unit 4 Dev (2); Transition (1); Unit 3 Dev (1)
- **Intervals:** median 293.99s (p5 36.50s / p95 1354.42s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 14 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (4); Unit 3 Dungeon Dev (2); Unit 4 Dev (2); Transition (1); Unit 3 Dev (1)
- **Intervals:** median 266.42s (p5 18.41s / p95 1351.35s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    false  x14
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 7 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (7)
- **Intervals:** median 15.58s (p5 2.90s / p95 66.17s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "ChangeCanister"  x7
data.canisterType  (string, 7/7 records)
    "Clay"  x3
    "Gravel"  x2
    "Bedrock"  x1
    "Sand"  x1
data.floor  (string, 7/7 records)
    "5"  x5
    "3"  x1
    "4"  x1
data.machine  (string, 7/7 records)
    "1"  x6
    "2"  x1
data.row  (string, 7/7 records)
    "TopRow"  x4
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.95s (p5 1.57s / p95 21.23s, n=5)
- **`data` key-set variants:** [actionType, boxID, soilType] x3; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x3
    "soilSelected"  x3
data.boxID  (string, 3/6 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.boxId  (string, 3/6 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationAnswerEvent` — 6 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1574.22s (p5 258.03s / p95 2132.17s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "submitAnswerEvent"  x6
data.answerSubmitted  (string, 6/6 records)
    "A,1,I"  x2
    "A,1,II"  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "D,C,3,II"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1907.09s (p5 1411.58s / p95 2117.98s, n=4)
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `gameStartEvent` — 5 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (5)
- **Intervals:** median 1785.76s (p5 1129.45s / p95 2229.73s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 5/5 records)
    true  x5
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 2.63s (p5 1.42s / p95 4.11s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted Out"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Cold"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `DEBUGMenu` — 2 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (2)
- **Intervals:** median 4.45s (p5 4.45s / p95 4.45s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "DebugMenuStateChanged"  x2
data.isOpened  (bool, 2/2 records)
    false  x1
    true  x1
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

## 10. Regression Comparison

Baseline: snapshot gameplay-logs-test\reports\08-13-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : exact duplicate records (same timestamp, scene and data)
- `DialogueEvent` : exact duplicate records (same timestamp, scene and data)
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `DaniEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DaniEvent` actionType: tool open/close: close without preceding open
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open
- `argumentationNodeEvent` actionType: node hover: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (31x); "WaypointResetEvent" (1x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (35x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by gameplay-logs-test / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*