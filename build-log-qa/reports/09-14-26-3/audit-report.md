# MHS Gameplay Log Audit Report — build 09-14-26-3

## 1. Build Information

- **Build ID:** 09-14-26-3
- **Game version string(s) in log:** 20260914-
- **Audit date:** 2026-09-16
- **Log file(s):** wenyi091426-3.stratalog.logdata.json
- **Records:** 12318 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa8589346b3c45b562092f8
- **Time span:** 2026-09-16T00:22:40.350000+00:00 .. 2026-09-16T19:04:47.192000+00:00 (18h 42m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-14-26-3.yaml
- **Baseline:** snapshot build-log-qa\reports\09-03-26-2\snapshot.json

## 2. Executive Summary

- **23 event types**, 12318 records, 12 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 101 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `DialogueEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `DaniEvent`: median interval between records changed substantially
  - WARNING/Medium `DialogueEvent`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4446 | 36.09 | 1 | 4 | 0 | 2026-09-16T01:14:55.359000+00:00 | 2026-09-16T18:35:38.537000+00:00 | 17h 20m |
| InputEvent | 2744 | 22.28 | 1 | 9 | 0 | 2026-09-16T00:48:50.752000+00:00 | 2026-09-16T19:04:47.192000+00:00 | 18h 15m |
| DialogueEvent | 2203 | 17.88 | 1 | 9 | 1347 | 2026-09-16T00:23:06.955000+00:00 | 2026-09-16T19:04:43.056000+00:00 | 18h 41m |
| PlayerPositionEvent | 1621 | 13.16 | 1 | 9 | 0 | 2026-09-16T00:22:50.377000+00:00 | 2026-09-16T19:04:37.818000+00:00 | 18h 41m |
| argumentationNodeEvent | 504 | 4.09 | 1 | 5 | 0 | 2026-09-16T01:06:36.907000+00:00 | 2026-09-16T18:53:12.001000+00:00 | 17h 46m |
| ObjectInterEvent | 254 | 2.06 | 1 | 9 | 0 | 2026-09-16T00:49:50.791000+00:00 | 2026-09-16T19:04:47.192000+00:00 | 18h 14m |
| TopographicMapEvent | 80 | 0.65 | 1 | 2 | 0 | 2026-09-16T01:15:12.251000+00:00 | 2026-09-16T17:14:02.899000+00:00 | 15h 58m |
| Soil Key Puzzle | 74 | 0.6 | 1 | 3 | 0 | 2026-09-16T01:24:12.604000+00:00 | 2026-09-16T17:29:33.054000+00:00 | 16h 5m |
| questEvent | 70 | 0.57 | 1 | 9 | 70 | 2026-09-16T00:23:06.949000+00:00 | 2026-09-16T19:00:34.451000+00:00 | 18h 37m |
| gameWindowFocusEvent | 69 | 0.56 | 1 | 10 | 0 | 2026-09-16T00:22:40.350000+00:00 | 2026-09-16T18:58:28.584000+00:00 | 18h 35m |
| gameWindowUnfocusEvent | 64 | 0.52 | 1 | 11 | 0 | 2026-09-16T00:22:58.813000+00:00 | 2026-09-16T18:58:26.667000+00:00 | 18h 35m |
| WaterChamberEvent | 47 | 0.38 | 1 | 1 | 0 | 2026-09-16T18:35:13.863000+00:00 | 2026-09-16T18:44:57.543000+00:00 | 9m 43s |
| soilMachine | 43 | 0.35 | 1 | 1 | 0 | 2026-09-16T17:40:17.518000+00:00 | 2026-09-16T17:46:54.128000+00:00 | 6m 36s |
| argumentationAnswerEvent | 37 | 0.3 | 1 | 5 | 0 | 2026-09-16T01:06:32.572000+00:00 | 2026-09-16T18:53:14.519000+00:00 | 17h 46m |
| argumentationEvent | 14 | 0.11 | 1 | 5 | 0 | 2026-09-16T01:05:55.525000+00:00 | 2026-09-16T18:53:14.524000+00:00 | 17h 47m |
| DEBUGMenu | 13 | 0.11 | 1 | 8 | 0 | 2026-09-16T00:22:50.373000+00:00 | 2026-09-16T18:29:20.265000+00:00 | 18h 6m |
| argumentationToolEvent | 9 | 0.07 | 1 | 3 | 0 | 2026-09-16T01:07:19.478000+00:00 | 2026-09-16T18:51:36.121000+00:00 | 17h 44m |
| gameStartEvent | 7 | 0.06 | 1 | 1 | 0 | 2026-09-16T00:22:40.350000+00:00 | 2026-09-16T18:29:18.124000+00:00 | 18h 6m |
| TerasGardenBox | 6 | 0.05 | 1 | 1 | 0 | 2026-09-16T18:15:49.824000+00:00 | 2026-09-16T18:16:56.306000+00:00 | 1m 6s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-09-16T01:10:20.723000+00:00 | 2026-09-16T19:04:47.190000+00:00 | 17h 54m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-09-16T18:58:15.132000+00:00 | 2026-09-16T18:58:18.638000+00:00 | 3.5s |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-16T01:38:05.094000+00:00 | 2026-09-16T01:38:06.110000+00:00 | 1.0s |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-09-16T18:29:20.249000+00:00 | 2026-09-16T18:45:51.444000+00:00 | 16m 31s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 986.431s median 
  - Expected: 7.86s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `DaniEvent` — median interval between records changed substantially. 
  - Observed: 1.016s median 
  - Expected: 2.369s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 3.493s median 
  - Expected: 0.667s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 4953.498s median 
  - Expected: 1864.391s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.434s median 
  - Expected: 8.004s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.144s median 
  - Expected: 13.039s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.302s median 
  - Expected: 1881.866s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 158.479s median 
  - Expected: 52.427s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 15.322s median 
  - Expected: 0.901s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — baseline field(s) absent this build. 
  - Observed: data.actionKey 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 991.195s median 
  - Expected: 0.232s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `crash` — event type present in baseline 09-03-26-2 but absent now. 
  - Observed: 0 records this build 
  - Expected: 3 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 3811.132s median 
  - Expected: 841.528s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 172.948s median 
  - Expected: 74.645s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.434s median 
  - Expected: 42.837s in 09-03-26-2 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: PodsEscapingCopernicus Cutscene; Transition 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` `data.isOpened` — baseline categorical value(s) not seen this build. 
  - Observed: True 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `DaniEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 16 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: Settings 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Pause; ToggleDebug 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: backquote; tab 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to go down 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 4446 records 
  - Expected: 1182 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Tilted Out; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: Gravel 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.9x vs baseline. 
  - Observed: 47 records 
  - Expected: 12 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `WaterChamberEvent` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 3 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — categorical value(s) not seen in baseline. 
  - Observed: Two 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — categorical value(s) not seen in baseline. 
  - Observed: DualChamber_Condenser; DualChamber_Evaporator 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.room` — categorical value(s) not seen in baseline. 
  - Observed: 4 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 37 records 
  - Expected: 6 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 2,I; A,2,I; A,2,II; A,3,I; A,B,1,I; A,B,2,I; A,B,3,I; A,B,4,I; A,D,C,2,II; B,1,I; B,1,II; B,4,II; B,C,1,I; C,1,I; C,1,II; C,3,II; C,4,II; D,1,I; D,1,II; D,2,II; D,3,I; D,4,I; D,4,II; D,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 504 records 
  - Expected: 133 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Argumentation; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 32 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Open; ScrollStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.chatID` — baseline categorical value(s) not seen this build. 
  - Observed: [18-102, 18-103, 18-105, 18-109, 18-110, 18-274]; [18-109, 18-110, 18-274, 18-112, 18-113, 18-114]; [18-112, 18-113, 18-114, 18-276, 18-277]; [18-114, 18-276, 18-277, 18-279, 18-116, 18-117]; [18-243, 18-118, 74-21, 23-1, 23-2, 23-3]; [18-279, 18-116, 18-117, 18-243, 18-118, 74-21]; [22-19, 22-20, 22-22, 22-46, 22-48, 22-27]; [22-46, 22-48, 22-27, 18-102, 18-103, 18-105]; [23-1, 23-2, 23-3, 23-4, 23-59, 23-61]; [23-17, 23-18, 23-20, 23-21, 23-70, 23-72]; [23-21, 23-70, 23-72, 23-73, 23-22, 23-24]; [23-59, 23-61, 23-63, 23-65, 23-67, 23-68]; [23-65, 23-67, 23-68, 23-69, 23-17, 23-18]; [23-73, 23-22, 23-24, 23-25, 23-27] 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 8.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 5 in 09-03-26-2 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 53 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi091426-3.stratalog.logdata.json[12147] _id=6aa9e80b485cab4c9544e945 ts=2026-09-16T00:51:24.1800000Z`; `wenyi091426-3.stratalog.logdata.json[12082] _id=6aa9e92f485cab4c9544eb55 ts=2026-09-16T00:56:15.8550000Z`; `wenyi091426-3.stratalog.logdata.json[12050] _id=6aa9e9a9485cab4c9544ebd5 ts=2026-09-16T00:58:18.1710000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 7 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 7} 
  - Examples: `wenyi091426-3.stratalog.logdata.json[12317] _id=6aa9e150485cab4c9544e701 ts=2026-09-16T00:22:40.3500000Z`; `wenyi091426-3.stratalog.logdata.json[12290] _id=6aa9e69c485cab4c9544e73d ts=2026-09-16T00:45:16.6450000Z`; `wenyi091426-3.stratalog.logdata.json[11725] _id=6aa9ecec485cab4c9544f5ff ts=2026-09-16T01:12:12.3940000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 69 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 69} 
  - Examples: `wenyi091426-3.stratalog.logdata.json[12316] _id=6aa9e14f485cab4c9544e6ff ts=2026-09-16T00:22:40.3500000Z`; `wenyi091426-3.stratalog.logdata.json[12302] _id=6aa9e1a5485cab4c9544e723 ts=2026-09-16T00:24:05.8130000Z`; `wenyi091426-3.stratalog.logdata.json[12299] _id=6aa9e1bc485cab4c9544e729 ts=2026-09-16T00:24:29.3240000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 64 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 64} 
  - Examples: `wenyi091426-3.stratalog.logdata.json[12313] _id=6aa9e162485cab4c9544e707 ts=2026-09-16T00:22:58.8130000Z`; `wenyi091426-3.stratalog.logdata.json[12301] _id=6aa9e1a8485cab4c9544e725 ts=2026-09-16T00:24:08.9080000Z`; `wenyi091426-3.stratalog.logdata.json[12297] _id=6aa9e1c1485cab4c9544e72d ts=2026-09-16T00:24:33.9230000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 5 of 80 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11604] _id=6aa9ed9f485cab4c9544f7fd ts=2026-09-16T01:15:12.2510000Z`; `wenyi091426-3.stratalog.logdata.json[11596] _id=6aa9edaf485cab4c9544f815 ts=2026-09-16T01:15:27.4880000Z`; `wenyi091426-3.stratalog.logdata.json[9660] _id=6aa9f154485cab4c95450e0f ts=2026-09-16T01:31:00.2690000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4445 | 0.0 | 0.019 | 14.048 | 0.817 | 47017.865 | 4.27 | 2926 | 6 |
| InputEvent | 2743 | 0.0 | 0.484 | 23.972 | 19.491 | 46441.357 | 2.5 | 115 | 4 |
| DialogueEvent | 2202 | 0.0 | 3.493 | 30.561 | 25.258 | 46429.695 | 1.96 | 680 | 3 |
| PlayerPositionEvent | 1609 | 9.985 | 10.005 | 39.678 | 10.006 | 46425.155 | 1.51 | 0 | 2 |
| argumentationNodeEvent | 503 | 0.016 | 0.218 | 127.227 | 11.289 | 51883.11 | 0.47 | 161 | 4 |
| ObjectInterEvent | 253 | 0.0 | 4.07 | 259.67 | 361.294 | 48071.817 | 0.23 | 3 | 5 |
| TopographicMapEvent | 79 | 0.003 | 2.169 | 728.236 | 739.914 | 46818.165 | 0.08 | 2 | 5 |
| Soil Key Puzzle | 73 | 0.167 | 0.884 | 793.431 | 23.085 | 48068.832 | 0.08 | 0 | 3 |
| questEvent | 69 | 0.0 | 172.948 | 971.703 | 1093.818 | 47486.885 | 0.06 | 13 | 8 |
| gameWindowFocusEvent | 68 | 4.432 | 181.281 | 984.533 | 1097.769 | 46711.445 | 0.06 | 0 | 9 |
| gameWindowUnfocusEvent | 63 | 2.2 | 167.395 | 1062.347 | 1112.493 | 46849.131 | 0.06 | 0 | 10 |
| WaterChamberEvent | 46 | 0.784 | 6.144 | 12.689 | 54.938 | 69.234 | 4.73 | 0 | 0 |
| soilMachine | 42 | 0.568 | 1.434 | 9.443 | 26.941 | 152.974 | 6.35 | 0 | 0 |
| argumentationAnswerEvent | 36 | 9.855 | 20.302 | 1777.832 | 4369.902 | 51905.155 | 0.03 | 0 | 4 |
| argumentationEvent | 13 | 0.015 | 158.479 | 4926.077 | 23532.683 | 51879.024 | 0.01 | 2 | 4 |
| DEBUGMenu | 12 | 648.578 | 986.431 | 5432.491 | 25478.452 | 48598.145 | 0.01 | 0 | 12 |
| argumentationToolEvent | 8 | 0.417 | 15.322 | 7982.08 | 39339.798 | 56784.297 | 0.01 | 0 | 2 |
| gameStartEvent | 6 | 1356.295 | 3811.132 | 10866.296 | 37949.187 | 48596.641 | 0.01 | 0 | 6 |
| TerasGardenBox | 5 | 0.917 | 1.434 | 13.296 | 37.301 | 41.12 | 4.51 | 0 | 0 |
| EndOfUnit | 4 | 2318.197 | 4953.498 | 16116.617 | 45305.799 | 52241.274 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 0.934 | 1.117 | 1.169 | 1.421 | 1.455 | 51.34 | 0 | 0 |
| DaniEvent | 1 | 1.016 | 1.016 | 1.016 | 1.016 | 1.016 | 59.06 | 0 | 0 |
| chatEvent | 1 | 991.195 | 991.195 | 991.195 | 991.195 | 991.195 | 0.06 | 0 | 1 |

- **WARNING / Medium** `DialogueEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi091426-3.stratalog.logdata.json[4767] _id=6aaace39485cab4c95455c0c ts=2026-09-16T17:13:29.2520000Z == wenyi091426-3.stratalog.logdata.json[4766] _id=6aaace39485cab4c95455c0e ts=2026-09-16T17:13:29.2520000Z`
- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11207] _id=6aa9edf7485cab4c9544fb75 ts=2026-09-16T01:16:39.5880000Z == wenyi091426-3.stratalog.logdata.json[11208] _id=6aa9edf7485cab4c9544fb77 ts=2026-09-16T01:16:39.5880000Z`; `wenyi091426-3.stratalog.logdata.json[10972] _id=6aa9ee17485cab4c9544fd71 ts=2026-09-16T01:17:11.5200000Z == wenyi091426-3.stratalog.logdata.json[10971] _id=6aa9ee17485cab4c9544fd73 ts=2026-09-16T01:17:11.5200000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi091426-3.stratalog.logdata.json[2462] _id=6aaad98b485cab4c95456e22 ts=2026-09-16T18:01:47.5830000Z == wenyi091426-3.stratalog.logdata.json[2463] _id=6aaad98b485cab4c95456e24 ts=2026-09-16T18:01:47.5830000Z`; `wenyi091426-3.stratalog.logdata.json[2425] _id=6aaada1e485cab4c95456e6e ts=2026-09-16T18:04:14.8050000Z == wenyi091426-3.stratalog.logdata.json[2424] _id=6aaada1e485cab4c95456e70 ts=2026-09-16T18:04:14.8050000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 87 group(s), 129 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11637] _id=6aa9edd0485cab4c9544f883 ts=2026-09-16T01:14:55.4080000Z == wenyi091426-3.stratalog.logdata.json[11638] _id=6aa9edd0485cab4c9544f885 ts=2026-09-16T01:14:55.4080000Z`; `wenyi091426-3.stratalog.logdata.json[11633] _id=6aa9edd0485cab4c9544f887 ts=2026-09-16T01:14:55.4080000Z == wenyi091426-3.stratalog.logdata.json[11635] _id=6aa9edd0485cab4c9544f889 ts=2026-09-16T01:14:55.4080000Z`; `wenyi091426-3.stratalog.logdata.json[11586] _id=6aa9edc8485cab4c9544f82f ts=2026-09-16T01:15:52.3020000Z == wenyi091426-3.stratalog.logdata.json[11587] _id=6aa9edc8485cab4c9544f831 ts=2026-09-16T01:15:52.3020000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi091426-3.stratalog.logdata.json[99] _id=6aaae70d485cab4c9545809c ts=2026-09-16T18:59:25.5170000Z == wenyi091426-3.stratalog.logdata.json[98] _id=6aaae70d485cab4c9545809e ts=2026-09-16T18:59:25.5170000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi091426-3.stratalog.logdata.json[12192] _id=6aa9e7ae485cab4c9544e87b ts=2026-09-16T00:49:50.7910000Z ~ wenyi091426-3.stratalog.logdata.json[12191] _id=6aa9e7ae485cab4c9544e87d ts=2026-09-16T00:49:50.7920000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 63 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: wenyi091426-3.stratalog.logdata.json[11640] _id=6aa9edd0485cab4c9544f87d ts=2026-09-16T01:14:55.3590000Z ~ wenyi091426-3.stratalog.logdata.json[11639] _id=6aa9edd0485cab4c9544f87f ts=2026-09-16T01:14:55.3760000Z`; `2ms: wenyi091426-3.stratalog.logdata.json[11634] _id=6aa9edd0485cab4c9544f88b ts=2026-09-16T01:14:55.4080000Z ~ wenyi091426-3.stratalog.logdata.json[11632] _id=6aa9edd0485cab4c9544f88d ts=2026-09-16T01:14:55.4100000Z`; `19ms: wenyi091426-3.stratalog.logdata.json[11631] _id=6aa9edd0485cab4c9544f88f ts=2026-09-16T01:14:55.4410000Z ~ wenyi091426-3.stratalog.logdata.json[11630] _id=6aa9edd1485cab4c9544f891 ts=2026-09-16T01:14:55.4600000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: wenyi091426-3.stratalog.logdata.json[9653] _id=6aa9f165485cab4c95450e57 ts=2026-09-16T01:31:17.9110000Z ~ wenyi091426-3.stratalog.logdata.json[9649] _id=6aa9f165485cab4c95450e5f ts=2026-09-16T01:31:17.9140000Z`; `617ms: wenyi091426-3.stratalog.logdata.json[9647] _id=6aa9f167485cab4c95450e69 ts=2026-09-16T01:31:19.3290000Z ~ wenyi091426-3.stratalog.logdata.json[9646] _id=6aa9f167485cab4c95450e6b ts=2026-09-16T01:31:19.9460000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `15ms: wenyi091426-3.stratalog.logdata.json[5741] _id=6aaaca1a485cab4c95455470 ts=2026-09-16T16:55:54.5710000Z ~ wenyi091426-3.stratalog.logdata.json[5738] _id=6aaaca1a485cab4c95455476 ts=2026-09-16T16:55:54.5860000Z`; `15ms: wenyi091426-3.stratalog.logdata.json[2196] _id=6aaadb82485cab4c95457038 ts=2026-09-16T18:10:10.6270000Z ~ wenyi091426-3.stratalog.logdata.json[2192] _id=6aaadb82485cab4c9545703e ts=2026-09-16T18:10:10.6420000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 62 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `567ms: wenyi091426-3.stratalog.logdata.json[11834] _id=6aa9ebe2485cab4c9544f2b5 ts=2026-09-16T01:07:46.5040000Z ~ wenyi091426-3.stratalog.logdata.json[11831] _id=6aa9ebe2485cab4c9544f2bb ts=2026-09-16T01:07:47.0710000Z`; `400ms: wenyi091426-3.stratalog.logdata.json[11832] _id=6aa9ebe2485cab4c9544f2b9 ts=2026-09-16T01:07:46.7210000Z ~ wenyi091426-3.stratalog.logdata.json[11830] _id=6aa9ebe2485cab4c9544f2bd ts=2026-09-16T01:07:47.1210000Z`; `434ms: wenyi091426-3.stratalog.logdata.json[6764] _id=6aaab6e1485cab4c95454c70 ts=2026-09-16T15:33:54.0390000Z ~ wenyi091426-3.stratalog.logdata.json[6762] _id=6aaab6e2485cab4c95454c74 ts=2026-09-16T15:33:54.4730000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi091426-3.stratalog.logdata.json[221] _id=6aaae5df485cab4c95457fa8 ts=2026-09-16T18:54:23.7540000Z ~ wenyi091426-3.stratalog.logdata.json[220] _id=6aaae5df485cab4c95457faa ts=2026-09-16T18:54:23.7550000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 13h 29m 
  - Evidence: 13h 29m: wenyi091426-3.stratalog.logdata.json[11724] _id=6aa9ecee485cab4c9544f601 ts=2026-09-16T01:12:14.4010000Z -> wenyi091426-3.stratalog.logdata.json[9226] _id=6aaaaac4485cab4c95453934 ts=2026-09-16T14:42:12.5460000Z; 1h 49m: wenyi091426-3.stratalog.logdata.json[9226] _id=6aaaaac4485cab4c95453934 ts=2026-09-16T14:42:12.5460000Z -> wenyi091426-3.stratalog.logdata.json[6553] _id=6aaac466485cab4c95454e18 ts=2026-09-16T16:31:34.8860000Z; 27m 26s: wenyi091426-3.stratalog.logdata.json[6553] _id=6aaac466485cab4c95454e18 ts=2026-09-16T16:31:34.8860000Z -> wenyi091426-3.stratalog.logdata.json[5632] _id=6aaacad5485cab4c9545554a ts=2026-09-16T16:59:01.7320000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 12h 53m 
  - Evidence: 12h 53m: wenyi091426-3.stratalog.logdata.json[9233] _id=6aa9f567485cab4c9545199b ts=2026-09-16T01:48:23.5760000Z -> wenyi091426-3.stratalog.logdata.json[9224] _id=6aaaaac5485cab4c95453938 ts=2026-09-16T14:42:13.2710000Z; 50m 41s: wenyi091426-3.stratalog.logdata.json[6562] _id=6aaab88d485cab4c95454e04 ts=2026-09-16T15:41:02.0000000Z -> wenyi091426-3.stratalog.logdata.json[6550] _id=6aaac46f485cab4c95454e1e ts=2026-09-16T16:31:43.4960000Z; 21m 18s: wenyi091426-3.stratalog.logdata.json[12298] _id=6aa9e1bf485cab4c9544e72b ts=2026-09-16T00:24:32.4660000Z -> wenyi091426-3.stratalog.logdata.json[12283] _id=6aa9e6be485cab4c9544e74b ts=2026-09-16T00:45:50.8040000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 680 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi091426-3.stratalog.logdata.json[102] _id=6aaae702485cab4c95458094 ts=2026-09-16T18:59:15.1130000Z -> wenyi091426-3.stratalog.logdata.json[103] _id=6aaae702485cab4c95458096 ts=2026-09-16T18:59:15.1130000Z; 0ms: wenyi091426-3.stratalog.logdata.json[1039] _id=6aaae1d7485cab4c95457944 ts=2026-09-16T18:37:11.5870000Z -> wenyi091426-3.stratalog.logdata.json[1038] _id=6aaae1d7485cab4c95457946 ts=2026-09-16T18:37:11.5870000Z; 0ms: wenyi091426-3.stratalog.logdata.json[106] _id=6aaae701485cab4c9545808e ts=2026-09-16T18:59:14.3300000Z -> wenyi091426-3.stratalog.logdata.json[105] _id=6aaae702485cab4c95458090 ts=2026-09-16T18:59:14.3300000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 14h 30m 
  - Evidence: 14h 30m: wenyi091426-3.stratalog.logdata.json[11728] _id=6aa9ec7c485cab4c9544f57d ts=2026-09-16T01:10:20.7230000Z -> wenyi091426-3.stratalog.logdata.json[6563] _id=6aaab88d485cab4c95454e02 ts=2026-09-16T15:41:01.9970000Z; 1h 40m: wenyi091426-3.stratalog.logdata.json[6563] _id=6aaab88d485cab4c95454e02 ts=2026-09-16T15:41:01.9970000Z -> wenyi091426-3.stratalog.logdata.json[4632] _id=6aaad002485cab4c95455d1a ts=2026-09-16T17:21:06.7730000Z; 1h 5m: wenyi091426-3.stratalog.logdata.json[4632] _id=6aaad002485cab4c95455d1a ts=2026-09-16T17:21:06.7730000Z -> wenyi091426-3.stratalog.logdata.json[1843] _id=6aaadf40485cab4c954572fa ts=2026-09-16T18:26:08.9930000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 12h 54m 
  - Evidence: 12h 54m: wenyi091426-3.stratalog.logdata.json[9229] _id=6aa9f56e485cab4c954519a5 ts=2026-09-16T01:48:30.6780000Z -> wenyi091426-3.stratalog.logdata.json[9218] _id=6aaaaad8485cab4c95453944 ts=2026-09-16T14:42:32.0350000Z; 55m 16s: wenyi091426-3.stratalog.logdata.json[6575] _id=6aaab874485cab4c95454dea ts=2026-09-16T15:40:36.5520000Z -> wenyi091426-3.stratalog.logdata.json[6503] _id=6aaac569485cab4c95454e7c ts=2026-09-16T16:35:53.4990000Z; 17m 59s: wenyi091426-3.stratalog.logdata.json[7369] _id=6aaaae9f485cab4c954547b6 ts=2026-09-16T14:58:39.0410000Z -> wenyi091426-3.stratalog.logdata.json[7115] _id=6aaab2d6485cab4c954549b2 ts=2026-09-16T15:16:38.2050000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 115 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi091426-3.stratalog.logdata.json[10972] _id=6aa9ee17485cab4c9544fd71 ts=2026-09-16T01:17:11.5200000Z -> wenyi091426-3.stratalog.logdata.json[10971] _id=6aa9ee17485cab4c9544fd73 ts=2026-09-16T01:17:11.5200000Z; 0ms: wenyi091426-3.stratalog.logdata.json[11207] _id=6aa9edf7485cab4c9544fb75 ts=2026-09-16T01:16:39.5880000Z -> wenyi091426-3.stratalog.logdata.json[11208] _id=6aa9edf7485cab4c9544fb77 ts=2026-09-16T01:16:39.5880000Z; 0ms: wenyi091426-3.stratalog.logdata.json[6166] _id=6aaac84c485cab4c9545511e ts=2026-09-16T16:48:13.0100000Z -> wenyi091426-3.stratalog.logdata.json[6165] _id=6aaac84c485cab4c95455120 ts=2026-09-16T16:48:13.0100000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 13h 21m 
  - Evidence: 13h 21m: wenyi091426-3.stratalog.logdata.json[9789] _id=6aa9efbc485cab4c954507b5 ts=2026-09-16T01:24:12.6040000Z -> wenyi091426-3.stratalog.logdata.json[9176] _id=6aaaab84485cab4c95453998 ts=2026-09-16T14:45:24.4210000Z; 1h 9m: wenyi091426-3.stratalog.logdata.json[6880] _id=6aaab584485cab4c95454b88 ts=2026-09-16T15:28:04.5860000Z -> wenyi091426-3.stratalog.logdata.json[6471] _id=6aaac5c2485cab4c95454ebc ts=2026-09-16T16:37:22.6100000Z; 29m 34s: wenyi091426-3.stratalog.logdata.json[8269] _id=6aaaad29485cab4c95454088 ts=2026-09-16T14:52:25.4580000Z -> wenyi091426-3.stratalog.logdata.json[7020] _id=6aaab417485cab4c95454a70 ts=2026-09-16T15:21:59.9080000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi091426-3.stratalog.logdata.json[2425] _id=6aaada1e485cab4c95456e6e ts=2026-09-16T18:04:14.8050000Z -> wenyi091426-3.stratalog.logdata.json[2424] _id=6aaada1e485cab4c95456e70 ts=2026-09-16T18:04:14.8050000Z; 0ms: wenyi091426-3.stratalog.logdata.json[2462] _id=6aaad98b485cab4c95456e22 ts=2026-09-16T18:01:47.5830000Z -> wenyi091426-3.stratalog.logdata.json[2463] _id=6aaad98b485cab4c95456e24 ts=2026-09-16T18:01:47.5830000Z; 1ms: wenyi091426-3.stratalog.logdata.json[12192] _id=6aa9e7ae485cab4c9544e87b ts=2026-09-16T00:49:50.7910000Z -> wenyi091426-3.stratalog.logdata.json[12191] _id=6aa9e7ae485cab4c9544e87d ts=2026-09-16T00:49:50.7920000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 12h 53m 
  - Evidence: 12h 53m: wenyi091426-3.stratalog.logdata.json[9230] _id=6aa9f56b485cab4c954519a1 ts=2026-09-16T01:48:27.3930000Z -> wenyi091426-3.stratalog.logdata.json[9225] _id=6aaaaac5485cab4c95453936 ts=2026-09-16T14:42:12.5480000Z; 17m 1s: wenyi091426-3.stratalog.logdata.json[12294] _id=6aa9e2b0485cab4c9544e733 ts=2026-09-16T00:28:32.5750000Z -> wenyi091426-3.stratalog.logdata.json[12286] _id=6aa9e6ae485cab4c9544e745 ts=2026-09-16T00:45:34.2690000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 13h 3m 
  - Evidence: 13h 3m: wenyi091426-3.stratalog.logdata.json[9323] _id=6aa9f460485cab4c9545178f ts=2026-09-16T01:43:59.9870000Z -> wenyi091426-3.stratalog.logdata.json[9135] _id=6aaaac0a485cab4c954539ea ts=2026-09-16T14:47:37.8520000Z; 2h 0m: wenyi091426-3.stratalog.logdata.json[7371] _id=6aaaae9e485cab4c954547b4 ts=2026-09-16T14:58:37.6400000Z -> wenyi091426-3.stratalog.logdata.json[5629] _id=6aaacad6485cab4c9545554e ts=2026-09-16T16:59:01.8330000Z; 36m 10s: wenyi091426-3.stratalog.logdata.json[2593] _id=6aaad78e485cab4c95456d22 ts=2026-09-16T17:53:15.1960000Z -> wenyi091426-3.stratalog.logdata.json[1829] _id=6aaae005485cab4c9545730c ts=2026-09-16T18:29:25.2730000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2926 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi091426-3.stratalog.logdata.json[10016] _id=6aa9eeee485cab4c95450589 ts=2026-09-16T01:20:44.6260000Z -> wenyi091426-3.stratalog.logdata.json[10018] _id=6aa9eeee485cab4c9545058b ts=2026-09-16T01:20:44.6260000Z; 0ms: wenyi091426-3.stratalog.logdata.json[10017] _id=6aa9eeee485cab4c95450587 ts=2026-09-16T01:20:44.6260000Z -> wenyi091426-3.stratalog.logdata.json[10016] _id=6aa9eeee485cab4c95450589 ts=2026-09-16T01:20:44.6260000Z; 0ms: wenyi091426-3.stratalog.logdata.json[10030] _id=6aa9eeee485cab4c9545056b ts=2026-09-16T01:20:44.1600000Z -> wenyi091426-3.stratalog.logdata.json[10031] _id=6aa9eeee485cab4c9545056d ts=2026-09-16T01:20:44.1600000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 13h 21m 
  - Evidence: 13h 21m: wenyi091426-3.stratalog.logdata.json[9786] _id=6aa9efbf485cab4c954507b9 ts=2026-09-16T01:24:15.5880000Z -> wenyi091426-3.stratalog.logdata.json[9177] _id=6aaaab84485cab4c95453996 ts=2026-09-16T14:45:24.4200000Z; 2h 12m: wenyi091426-3.stratalog.logdata.json[9166] _id=6aaaab91485cab4c954539ac ts=2026-09-16T14:45:37.0260000Z -> wenyi091426-3.stratalog.logdata.json[5660] _id=6aaacaa8485cab4c95455512 ts=2026-09-16T16:58:16.4730000Z; 28m 16s: wenyi091426-3.stratalog.logdata.json[5647] _id=6aaacab3485cab4c9545552c ts=2026-09-16T16:58:28.1610000Z -> wenyi091426-3.stratalog.logdata.json[4568] _id=6aaad154485cab4c95455db0 ts=2026-09-16T17:26:44.5890000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 13h 0m 
  - Evidence: 13h 0m: wenyi091426-3.stratalog.logdata.json[9378] _id=6aa9f402485cab4c9545169d ts=2026-09-16T01:42:26.3100000Z -> wenyi091426-3.stratalog.logdata.json[9212] _id=6aaaaae4485cab4c95453950 ts=2026-09-16T14:42:44.4750000Z; 1h 21m: wenyi091426-3.stratalog.logdata.json[7124] _id=6aaab2a4485cab4c954549a0 ts=2026-09-16T15:15:48.0950000Z -> wenyi091426-3.stratalog.logdata.json[6477] _id=6aaac5b6485cab4c95454eb0 ts=2026-09-16T16:37:10.3210000Z; 32m 8s: wenyi091426-3.stratalog.logdata.json[6441] _id=6aaac61e485cab4c95454ef8 ts=2026-09-16T16:38:54.4040000Z -> wenyi091426-3.stratalog.logdata.json[4829] _id=6aaacda6485cab4c95455b90 ts=2026-09-16T17:11:03.1290000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.015s shown 
  - Evidence: 3ms: wenyi091426-3.stratalog.logdata.json[9653] _id=6aa9f165485cab4c95450e57 ts=2026-09-16T01:31:17.9110000Z -> wenyi091426-3.stratalog.logdata.json[9649] _id=6aa9f165485cab4c95450e5f ts=2026-09-16T01:31:17.9140000Z; 15ms: wenyi091426-3.stratalog.logdata.json[9654] _id=6aa9f165485cab4c95450e55 ts=2026-09-16T01:31:17.8960000Z -> wenyi091426-3.stratalog.logdata.json[9653] _id=6aa9f165485cab4c95450e57 ts=2026-09-16T01:31:17.9110000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 14h 25m 
  - Evidence: 14h 25m: wenyi091426-3.stratalog.logdata.json[11824] _id=6aa9ebe6485cab4c9544f2eb ts=2026-09-16T01:07:50.9390000Z -> wenyi091426-3.stratalog.logdata.json[6798] _id=6aaab6a8485cab4c95454c2c ts=2026-09-16T15:32:56.0940000Z; 1h 17m: wenyi091426-3.stratalog.logdata.json[6652] _id=6aaab760485cab4c95454d50 ts=2026-09-16T15:36:00.9670000Z -> wenyi091426-3.stratalog.logdata.json[5903] _id=6aaac994485cab4c9545532c ts=2026-09-16T16:53:40.4700000Z; 1h 11m: wenyi091426-3.stratalog.logdata.json[5742] _id=6aaaca1a485cab4c9545546e ts=2026-09-16T16:55:54.5680000Z -> wenyi091426-3.stratalog.logdata.json[2363] _id=6aaadacb485cab4c95456eea ts=2026-09-16T18:07:07.9360000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 14h 24m 
  - Evidence: 14h 24m: wenyi091426-3.stratalog.logdata.json[11823] _id=6aa9ebe6485cab4c9544f2ed ts=2026-09-16T01:07:50.9420000Z -> wenyi091426-3.stratalog.logdata.json[6827] _id=6aaab68d485cab4c95454bf2 ts=2026-09-16T15:32:29.9660000Z; 1h 17m: wenyi091426-3.stratalog.logdata.json[6651] _id=6aaab760485cab4c95454d52 ts=2026-09-16T15:36:00.9700000Z -> wenyi091426-3.stratalog.logdata.json[5923] _id=6aaac97b485cab4c95455304 ts=2026-09-16T16:53:16.0920000Z; 1h 11m: wenyi091426-3.stratalog.logdata.json[5738] _id=6aaaca1a485cab4c95455476 ts=2026-09-16T16:55:54.5860000Z -> wenyi091426-3.stratalog.logdata.json[2378] _id=6aaadabf485cab4c95456ecc ts=2026-09-16T18:06:55.3810000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.015s..0.015s shown 
  - Evidence: 15ms: wenyi091426-3.stratalog.logdata.json[2196] _id=6aaadb82485cab4c95457038 ts=2026-09-16T18:10:10.6270000Z -> wenyi091426-3.stratalog.logdata.json[2192] _id=6aaadb82485cab4c9545703e ts=2026-09-16T18:10:10.6420000Z; 15ms: wenyi091426-3.stratalog.logdata.json[5741] _id=6aaaca1a485cab4c95455470 ts=2026-09-16T16:55:54.5710000Z -> wenyi091426-3.stratalog.logdata.json[5738] _id=6aaaca1a485cab4c95455476 ts=2026-09-16T16:55:54.5860000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 14h 24m 
  - Evidence: 14h 24m: wenyi091426-3.stratalog.logdata.json[11827] _id=6aa9ebe3485cab4c9544f2c8 ts=2026-09-16T01:07:48.2220000Z -> wenyi091426-3.stratalog.logdata.json[6824] _id=6aaab68f485cab4c95454bf8 ts=2026-09-16T15:32:31.3320000Z; 1h 17m: wenyi091426-3.stratalog.logdata.json[6653] _id=6aaab75f485cab4c95454d4e ts=2026-09-16T15:35:59.1160000Z -> wenyi091426-3.stratalog.logdata.json[5920] _id=6aaac97f485cab4c9545530a ts=2026-09-16T16:53:19.3260000Z; 1h 11m: wenyi091426-3.stratalog.logdata.json[5746] _id=6aaaca15485cab4c95455466 ts=2026-09-16T16:55:49.6990000Z -> wenyi091426-3.stratalog.logdata.json[2375] _id=6aaadac2485cab4c95456ed2 ts=2026-09-16T18:06:58.7650000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 161 interval(s) ≤ 0.016s..0.016s shown 
  - Evidence: 16ms: wenyi091426-3.stratalog.logdata.json[11838] _id=6aa9ebe0485cab4c9544f2a7 ts=2026-09-16T01:07:45.1370000Z -> wenyi091426-3.stratalog.logdata.json[11837] _id=6aa9ebe0485cab4c9544f2a9 ts=2026-09-16T01:07:45.1530000Z; 16ms: wenyi091426-3.stratalog.logdata.json[11854] _id=6aa9ebcb485cab4c9544f247 ts=2026-09-16T01:07:24.1770000Z -> wenyi091426-3.stratalog.logdata.json[11853] _id=6aa9ebcb485cab4c9544f249 ts=2026-09-16T01:07:24.1930000Z; 16ms: wenyi091426-3.stratalog.logdata.json[2284] _id=6aaadb0d485cab4c95456f88 ts=2026-09-16T18:08:13.6350000Z -> wenyi091426-3.stratalog.logdata.json[2283] _id=6aaadb0d485cab4c95456f8a ts=2026-09-16T18:08:13.6510000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 15h 46m 
  - Evidence: 15h 46m: wenyi091426-3.stratalog.logdata.json[11825] _id=6aa9ebe5485cab4c9544f2e3 ts=2026-09-16T01:07:50.1220000Z -> wenyi091426-3.stratalog.logdata.json[5868] _id=6aaac9b6485cab4c95455372 ts=2026-09-16T16:54:14.4190000Z; 1h 55m: wenyi091426-3.stratalog.logdata.json[5744] _id=6aaaca18485cab4c9545546a ts=2026-09-16T16:55:52.7840000Z -> wenyi091426-3.stratalog.logdata.json[421] _id=6aaae537485cab4c95457e18 ts=2026-09-16T18:51:35.6560000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16m 31s 
  - Evidence: 16m 31s: wenyi091426-3.stratalog.logdata.json[1839] _id=6aaadfff485cab4c95457304 ts=2026-09-16T18:29:20.2490000Z -> wenyi091426-3.stratalog.logdata.json[578] _id=6aaae3df485cab4c95457cde ts=2026-09-16T18:45:51.4440000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 13h 29m 
  - Evidence: 13h 29m: wenyi091426-3.stratalog.logdata.json[11725] _id=6aa9ecec485cab4c9544f5ff ts=2026-09-16T01:12:12.3940000Z -> wenyi091426-3.stratalog.logdata.json[9227] _id=6aaaaac1485cab4c95453932 ts=2026-09-16T14:42:09.0350000Z; 1h 40m: wenyi091426-3.stratalog.logdata.json[6560] _id=6aaab894485cab4c95454e0a ts=2026-09-16T15:41:08.9700000Z -> wenyi091426-3.stratalog.logdata.json[4629] _id=6aaad00b485cab4c95455d22 ts=2026-09-16T17:21:15.7940000Z; 1h 8m: wenyi091426-3.stratalog.logdata.json[4629] _id=6aaad00b485cab4c95455d22 ts=2026-09-16T17:21:15.7940000Z -> wenyi091426-3.stratalog.logdata.json[1841] _id=6aaadffd485cab4c95457302 ts=2026-09-16T18:29:18.1240000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 12h 58m 
  - Evidence: 12h 58m: wenyi091426-3.stratalog.logdata.json[9335] _id=6aa9f449485cab4c9545173f ts=2026-09-16T01:43:37.5890000Z -> wenyi091426-3.stratalog.logdata.json[9228] _id=6aaaaac1485cab4c95453930 ts=2026-09-16T14:42:09.0340000Z; 45m 32s: wenyi091426-3.stratalog.logdata.json[6561] _id=6aaab894485cab4c95454e08 ts=2026-09-16T15:41:08.9700000Z -> wenyi091426-3.stratalog.logdata.json[6558] _id=6aaac341485cab4c95454e0e ts=2026-09-16T16:26:41.1890000Z; 19m 36s: wenyi091426-3.stratalog.logdata.json[7092] _id=6aaab323485cab4c954549e0 ts=2026-09-16T15:17:55.8650000Z -> wenyi091426-3.stratalog.logdata.json[6632] _id=6aaab7bc485cab4c95454d78 ts=2026-09-16T15:37:32.3080000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 13h 0m 
  - Evidence: 13h 0m: wenyi091426-3.stratalog.logdata.json[9337] _id=6aa9f446485cab4c95451739 ts=2026-09-16T01:43:34.6970000Z -> wenyi091426-3.stratalog.logdata.json[9197] _id=6aaaab47485cab4c9545396e ts=2026-09-16T14:44:23.8280000Z; 49m 46s: wenyi091426-3.stratalog.logdata.json[6639] _id=6aaab786485cab4c95454d6a ts=2026-09-16T15:36:38.3580000Z -> wenyi091426-3.stratalog.logdata.json[6559] _id=6aaac330485cab4c95454e0c ts=2026-09-16T16:26:24.4750000Z; 19m 7s: wenyi091426-3.stratalog.logdata.json[2672] _id=6aaad77b485cab4c95456c80 ts=2026-09-16T17:52:59.8800000Z -> wenyi091426-3.stratalog.logdata.json[2150] _id=6aaadbf6485cab4c95457094 ts=2026-09-16T18:12:07.0010000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 13h 11m 
  - Evidence: 13h 11m: wenyi091426-3.stratalog.logdata.json[9666] _id=6aa9f146485cab4c95450dbb ts=2026-09-16T01:30:46.3950000Z -> wenyi091426-3.stratalog.logdata.json[9222] _id=6aaaaac5485cab4c9545393c ts=2026-09-16T14:42:13.2800000Z; 54m 50s: wenyi091426-3.stratalog.logdata.json[6567] _id=6aaab886485cab4c95454dfa ts=2026-09-16T15:40:55.0790000Z -> wenyi091426-3.stratalog.logdata.json[6507] _id=6aaac561485cab4c95454e74 ts=2026-09-16T16:35:45.1960000Z; 32m 15s: wenyi091426-3.stratalog.logdata.json[7295] _id=6aaaafd7485cab4c9545484a ts=2026-09-16T15:03:51.4770000Z -> wenyi091426-3.stratalog.logdata.json[6647] _id=6aaab766485cab4c95454d5a ts=2026-09-16T15:36:06.8050000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi091426-3.stratalog.logdata.json[11908] _id=6aa9eb17485cab4c9544efd5 ts=2026-09-16T01:04:24.1220000Z -> wenyi091426-3.stratalog.logdata.json[11910] _id=6aa9eb17485cab4c9544efd7 ts=2026-09-16T01:04:24.1220000Z; 0ms: wenyi091426-3.stratalog.logdata.json[99] _id=6aaae70d485cab4c9545809c ts=2026-09-16T18:59:25.5170000Z -> wenyi091426-3.stratalog.logdata.json[98] _id=6aaae70d485cab4c9545809e ts=2026-09-16T18:59:25.5170000Z; 1ms: wenyi091426-3.stratalog.logdata.json[1049] _id=6aaae1bc485cab4c95457930 ts=2026-09-16T18:36:44.3860000Z -> wenyi091426-3.stratalog.logdata.json[1048] _id=6aaae1bc485cab4c95457932 ts=2026-09-16T18:36:44.3870000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11810] _id=6aa9ebfc485cab4c9544f387 ts=2026-09-16T01:08:13.1390000Z`; `wenyi091426-3.stratalog.logdata.json[9385] _id=6aa9f3fa485cab4c9545168b ts=2026-09-16T01:42:19.0750000Z`; `wenyi091426-3.stratalog.logdata.json[7389] _id=6aaaae77485cab4c9545478e ts=2026-09-16T14:57:59.2560000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 29 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11514] _id=6aa9edda485cab4c9544f917 ts=2026-09-16T01:16:10.3090000Z`; `wenyi091426-3.stratalog.logdata.json[11513] _id=6aa9edda485cab4c9544f919 ts=2026-09-16T01:16:10.3750000Z`; `wenyi091426-3.stratalog.logdata.json[11076] _id=6aa9ee10485cab4c9544fcc1 ts=2026-09-16T01:17:02.7990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 29 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11642] _id=6aa9edd0485cab4c9544f87b ts=2026-09-16T01:14:55.3590000Z`; `wenyi091426-3.stratalog.logdata.json[11640] _id=6aa9edd0485cab4c9544f87d ts=2026-09-16T01:14:55.3590000Z`; `wenyi091426-3.stratalog.logdata.json[11639] _id=6aa9edd0485cab4c9544f87f ts=2026-09-16T01:14:55.3760000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi091426-3.stratalog.logdata.json[5738] _id=6aaaca1a485cab4c95455476 ts=2026-09-16T16:55:54.5860000Z`; `wenyi091426-3.stratalog.logdata.json[2192] _id=6aaadb82485cab4c9545703e ts=2026-09-16T18:10:10.6420000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi091426-3.stratalog.logdata.json[6686] _id=6aaab72c485cab4c95454d0c ts=2026-09-16T15:35:08.5580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `wenyi091426-3.stratalog.logdata.json[1839] _id=6aaadfff485cab4c95457304 ts=2026-09-16T18:29:20.2490000Z`; `wenyi091426-3.stratalog.logdata.json[578] _id=6aaae3df485cab4c95457cde ts=2026-09-16T18:45:51.4440000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 372 occurrence(s) 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11240] _id=6aa9edf5485cab4c9544fb4f ts=2026-09-16T01:16:36.8680000Z`; `wenyi091426-3.stratalog.logdata.json[11029] _id=6aa9ee13485cab4c9544fd23 ts=2026-09-16T01:17:06.5660000Z`; `wenyi091426-3.stratalog.logdata.json[10979] _id=6aa9ee18485cab4c9544fd89 ts=2026-09-16T01:17:11.0520000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 511 occurrence(s) 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11635] _id=6aa9edd0485cab4c9544f889 ts=2026-09-16T01:14:55.4080000Z`; `wenyi091426-3.stratalog.logdata.json[11630] _id=6aa9edd1485cab4c9544f891 ts=2026-09-16T01:14:55.4600000Z`; `wenyi091426-3.stratalog.logdata.json[11586] _id=6aa9edc8485cab4c9544f82f ts=2026-09-16T01:15:52.3020000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 19 occurrence(s) 
  - Examples: `wenyi091426-3.stratalog.logdata.json[9653] _id=6aa9f165485cab4c95450e57 ts=2026-09-16T01:31:17.9110000Z`; `wenyi091426-3.stratalog.logdata.json[9649] _id=6aa9f165485cab4c95450e5f ts=2026-09-16T01:31:17.9140000Z`; `wenyi091426-3.stratalog.logdata.json[9638] _id=6aa9f174485cab4c95450e81 ts=2026-09-16T01:31:32.3000000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11826] _id=6aa9ebe5485cab4c9544f2db ts=2026-09-16T01:07:49.3890000Z`; `wenyi091426-3.stratalog.logdata.json[5745] _id=6aaaca18485cab4c95455468 ts=2026-09-16T16:55:52.3670000Z`; `wenyi091426-3.stratalog.logdata.json[5744] _id=6aaaca18485cab4c9545546a ts=2026-09-16T16:55:52.7840000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'DialogueStartEvent' (totals: 430 start, 426 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 41 unmatched 'BecameCameraCentered' (totals: 1069 open, 1057 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 41 unmatched 'BecameVisible' (totals: 1166 open, 1154 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 21 open, 19 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 8 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 8 unmatched 'questActiveEvent' (totals: 39 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 652 of 12317 adjacent _id pairs reverse in client time; worst 63.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi091426-3.stratalog.logdata.json[11550] _id=6aa9edcf485cab4c9544f871 ts=2026-09-16T01:15:59.2840000Z`; `wenyi091426-3.stratalog.logdata.json[11644] _id=6aa9edd0485cab4c9544f875 ts=2026-09-16T01:14:55.3590000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.17s, min -66.18s, max +0.50s over 12318 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-14-26-3.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Full playthrough by one tester, logged 2026-09-16 00:22Z to 19:04Z (log shows EndOfUnit for units 1-5). Played in two sittings: Units 1-2 (first half) on the evening of 2026-09-15 local time, then a ~13-hour break mid-Unit 2 (01:48Z-14:42Z) before resuming from the main menu and finishing Units 2-5 on 2026-09-16.; The build's version string is '20260914-' on every record — the build number after the dash is missing (previous builds looked like '20260902-12353'). Worth reporting to the developers.; Unit 1 was started twice: a short first attempt (00:22Z-00:28Z, 24 records) was abandoned, then the tester relaunched at 00:45Z (MainMenu -> Transition -> Unit 1 Dev) and completed Unit 1 from the start.; Seven gameStartEvent records = seven launches from MainMenu (initial launch, Unit 1 restart, overnight resume, and one relaunch before each of Units 2, 3, 4, and 5).; Debug menu was NOT used. The 13 DEBUGMenu records (DebugMenuStateChanged, all isOpened=false) each sit at the exact first instant of a gameplay scene load (13 of the 14 gameplay scene loads; only the final 'Unit 5 Dev' load at 18:45:51Z lacks one). In every earlier build (08-13 through 09-03) DEBUGMenu records came as true/false pairs seconds apart from real toggles, so a scene-load emission of isOpened=false is new behavior in this build.; chatEvent: the two records (actionType Close, chatID NA) coincide exactly with the two Unit 5 scene loads (18:29:20Z dungeon, 18:45:51Z surface), the same pattern as the 08-31-26 and 09-03-26-3 runs; the tester never opened the chat log, so the missing data.actionKey / Open / ScrollStart values are not-exercised rather than a regression.; No 'crash' eventType records this run (the WASM memory-access crash seen in all three 09-03-26 sessions did not recur). |

No coverage-related findings.

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4446 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2826); Unit 4 Dev (850); Unit 5 Dev - Dungeon (500); Unit 3 Dungeon Dev (270)
- **Intervals:** median 0.02s (p5 0.00s / p95 0.82s, n=4445)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4446/4446 records)
    "BecameVisible"  x1166
    "BecameInvisible"  x1154
    "BecameCameraCentered"  x1069
    "BecameCameraUncentered"  x1057
data.pieceId  (string, 4446/4446 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4446/4446 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2744 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (787); Unit 5 Dev - Dungeon (493); Unit 4 Dev - Dungeon (410); Unit 3 Dev (324); Unit 3 Dungeon Dev (255); Unit 4 Dev (250); Unit 1 Dev (135); Unit 5 Dev (66); Unit 4 Dev - Anderson Base (24)
- **Intervals:** median 0.48s (p5 0.07s / p95 19.49s, n=2743)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2744/2744 records)
    "pressed"  x2744
data.actionType  (string, 2744/2744 records)
    "Move"  x1912
    "Interact"  x522
    "Sprint"  x222
    "Jump"  x29
    "Ascend"  x26
    "Hoverboard"  x13
    "Descend"  x10
    "Map"  x10
data.key  (string, 2744/2744 records, 2 empty-string)
    "w"  x699
    "leftButton"  x484
    "a"  x462
    "s"  x377
    "d"  x374
    "leftShift"  x232
    "e"  x47
    "space"  x46
    "h"  x11
    "m"  x10
    ""  x2
data.playerOrDrone  (string, 2744/2744 records)
    "Player"  x2408
    "Drone"  x336
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2203 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (677); Unit 3 Dev (384); Unit 4 Dev (273); Unit 5 Dev (234); Unit 1 Dev (200); Unit 3 Dungeon Dev (130); Unit 4 Dev - Anderson Base (108); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (98)
- **eventKey:** present on 1347 of 2203 records
- **Intervals:** median 3.49s (p5 0.00s / p95 25.26s, n=2202)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1347; [conversationId, dialogueEventType] x856
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2203/2203 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2203/2203 records)
    "DialogueNodeEvent"  x1347
    "DialogueStartEvent"  x430
    "DialogueFinishEvent"  x426
data.nodeId  (number, 1347/2203 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1621 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (566); Unit 3 Dev (230); Unit 4 Dev (228); Unit 1 Dev (161); Unit 5 Dev (113); Unit 5 Dev - Dungeon (98); Unit 4 Dev - Dungeon (88); Unit 4 Dev - Anderson Base (72); Unit 3 Dungeon Dev (65)
- **Intervals:** median 10.01s (p5 9.99s / p95 10.01s, n=1609)
- **Fields under `data`:**

```text
data.position  (object, 1621/1621 records)
data.position.x  (number, 1621/1621 records)
    numeric range -687.837 .. 1558.47 (458 unique)
data.position.y  (number, 1621/1621 records)
    numeric range -112.488 .. 222.252 (356 unique)
data.position.z  (number, 1621/1621 records)
    numeric range -1027.81 .. 2233.65 (458 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 504 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 5 Dev (130); Unit 3 Dev (127); Unit 4 Dev - Anderson Base (109); Unit 2 Prod (Refactor) (107); Unit 1 Dev (31)
- **Intervals:** median 0.22s (p5 0.02s / p95 11.29s, n=503)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 504/504 records)
    "argumentationNodeHoverEnd"  x207
    "argumentationNodeHoverStart"  x206
    "argumentationNodeAdd"  x54
    "argumentationNodeRemove"  x37
data.argumentationTitle  (string, 504/504 records)
    "Unit 5"  x130
    "Unit 3 - Pollution Upstream"  x127
    "Unit 4 - Flooding"  x109
    "Unit 2 – Watershed"  x107
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x6
data.nodeName  (string, 504/504 records)
    "B"  x80
    "A"  x64
    "4"  x48
    "C"  x48
    "3"  x47
    "D"  x46
    "2"  x43
    "I"  x42
    "1"  x40
    "II"  x37
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 254 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (89); Unit 2 Prod (Refactor) (65); Unit 3 Dungeon Dev (34); Unit 4 Dev (16); Unit 1 Dev (12); Unit 3 Dev (11); Unit 5 Dev - Dungeon (10); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (8)
- **Intervals:** median 4.07s (p5 1.00s / p95 361.29s, n=253)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 254/254 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 254/254 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 80 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (52); Unit 3 Dev (28)
- **Intervals:** median 2.17s (p5 0.45s / p95 739.91s, n=79)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, location] x35; [actionType, featureUsed, legendName] x5
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 80/80 records)
    "WaypointMoveEvent"  x31
    "MapOpenEvent"  x21
    "MapCloseEvent"  x19
    "Selected"  x4
    "WaypointSetEvent"  x4
    "Unselected"  x1
data.featureUsed  (string, 80/80 records)
    "Map"  x40
    "Waypoint"  x35
    "Legend"  x5
data.legendName  (string, 5/80 records)
    "0 ft"  x3
    "90 ft"  x1
    "Water"  x1
data.location  (object, 35/80 records)
data.location.x  (number, 35/80 records)
    numeric range -355.498 .. 523.898 (30 unique)
data.location.y  (number, 35/80 records)
    numeric range -270.416 .. 300.5 (32 unique)
data.location.z  (number, 35/80 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 74 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (50); Unit 2 Prod (Refactor) (12); Unit 3 Dev (12)
- **Intervals:** median 0.88s (p5 0.24s / p95 23.09s, n=73)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x66; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/74 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/74 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 66/74 records)
    "RightDrag"  x36
    "LeftDrag"  x30
data.currentSoilType  (string, 66/74 records)
    "CLAY"  x13
    "CLAYSAND"  x12
    "CLAYROCK"  x11
    "SAND"  x11
    "SANDGRAVEL"  x10
    "GRAVEL"  x5
    "BEDROCK"  x4
data.isCorrectSelection  (string, 66/74 records)
    "false"  x53
    "true"  x13
data.waterLevelStatus  (string, 66/74 records)
    "TooHigh"  x32
    "TooLow"  x24
    "Proper"  x10
data.waterRetentionChange  (string, 66/74 records)
    "Increase"  x27
    "Decrease"  x26
    "NoChange"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (13); Unit 2 Prod (Refactor) (13); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 172.95s (p5 0.00s / p95 1093.82s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x39; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x39
    "questFinishEvent"  x31
data.questID  (string, 70/70 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/70 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 69 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (20); MainMenu (11); Unit 1 Dev (9); Unit 3 Dev (9); Unit 4 Dev (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Dungeon (3); Unit 5 Dev - Dungeon (3); Unit 5 Dev (2); Transition (1)
- **Intervals:** median 181.28s (p5 10.48s / p95 1097.77s, n=68)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 69/69 records)
    true  x69
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 64 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (10); Unit 3 Dev (9); Unit 4 Dev (8); MainMenu (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Dungeon (3); Unit 5 Dev - Dungeon (3); Unit 5 Dev (2); PodsEscapingCopernicus Cutscene (1); Transition (1)
- **Intervals:** median 167.40s (p5 6.69s / p95 1112.49s, n=63)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 64/64 records)
    false  x64
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `WaterChamberEvent` — 47 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (47)
- **Intervals:** median 6.14s (p5 1.32s / p95 54.94s, n=46)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "On"  x29
    "Off"  x18
data.floor  (string, 47/47 records)
    "3"  x22
    "2"  x12
    "4"  x11
    "1"  x2
data.machineNumber  (string, 47/47 records)
    "One"  x46
    "Two"  x1
data.machineType  (string, 47/47 records)
    "Condenser"  x17
    "Evaporator"  x15
    "DualChamber_Evaporator"  x8
    "DualChamber_Condenser"  x5
    "VentSwitch"  x2
data.room  (string, 47/47 records)
    "2"  x23
    "3"  x12
    "1"  x6
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 43 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (43)
- **Intervals:** median 1.43s (p5 0.67s / p95 26.94s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "ChangeCanister"  x43
data.canisterType  (string, 43/43 records)
    "Clay"  x18
    "Bedrock"  x16
    "Sand"  x5
    "Gravel"  x4
data.floor  (string, 43/43 records)
    "5"  x18
    "4"  x15
    "3"  x10
data.machine  (string, 43/43 records)
    "1"  x41
    "2"  x2
data.row  (string, 43/43 records)
    "TopRow"  x36
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 37 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (11); Unit 2 Prod (Refactor) (9); Unit 3 Dev (7); Unit 5 Dev (7); Unit 1 Dev (3)
- **Intervals:** median 20.30s (p5 10.63s / p95 4369.90s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "submitAnswerEvent"  x37
data.answerSubmitted  (string, 37/37 records, 1 empty-string)
    29 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 37/37 records)
    "Unit 4 - Flooding"  x11
    "Unit 2 – Watershed"  x9
    "Unit 3 - Pollution Upstream"  x7
    "Unit 5"  x7
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 158.48s (p5 0.01s / p95 23532.68s, n=13)
- **Open findings:** 2 — see sections 5-8
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

### `DEBUGMenu` — 13 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 986.43s (p5 660.05s / p95 25478.45s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "DebugMenuStateChanged"  x13
data.isOpened  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4); Unit 1 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 15.32s (p5 0.43s / p95 39339.80s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x8
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 5"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 7 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (7)
- **Intervals:** median 3811.13s (p5 1421.16s / p95 37949.19s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 7/7 records)
    true  x7
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.43s (p5 0.93s / p95 37.30s, n=5)
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 4953.50s (p5 2555.80s / p95 45305.80s, n=4)
- **Open findings:** 1 — see sections 5-8
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

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 1.12s (p5 0.95s / p95 1.42s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted In"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.02s (p5 1.02s / p95 1.02s, n=1)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 991.20s (p5 991.20s / p95 991.20s, n=1)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-03-26-2\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DialogueEvent` : exact duplicate records (same timestamp, scene and data)
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `DaniEvent` : median interval between records changed substantially
- `DialogueEvent` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : baseline field(s) absent this build

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "Unselected" (1x); "WaypointMoveEvent" (31x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (5x); "Waypoint" (35x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (37x)
- `soilMachine` data.canisterType: "Bedrock" (16x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*