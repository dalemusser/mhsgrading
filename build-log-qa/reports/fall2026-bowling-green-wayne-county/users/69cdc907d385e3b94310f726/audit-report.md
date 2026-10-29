# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f726

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f726
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f726.jsonl
- **Records:** 2521 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f726
- **Time span:** 2026-04-13T17:53:15.194000+00:00 .. 2026-04-23T18:32:15.249000+00:00 (240h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f726\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2521 records, 8 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 77 INFO, 0 NOT_TESTED, 56 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1502 | 59.58 | 1 | 8 | 1005 | 2026-04-13T17:53:33.464000+00:00 | 2026-04-23T18:29:26.896000+00:00 | 240h 35m |
| PlayerPositionEvent | 547 | 21.7 | 1 | 8 | 0 | 2026-04-13T17:53:15.194000+00:00 | 2026-04-23T18:32:15.249000+00:00 | 240h 39m |
| Topographic Map Event | 173 | 6.86 | 1 | 2 | 0 | 2026-04-13T18:30:14.318000+00:00 | 2026-04-21T18:00:34.500000+00:00 | 191h 30m |
| TopographicMapEvent | 120 | 4.76 | 1 | 2 | 0 | 2026-04-13T18:31:10.795000+00:00 | 2026-04-21T18:00:12.133000+00:00 | 191h 29m |
| questEvent | 72 | 2.86 | 1 | 8 | 72 | 2026-04-13T17:53:33.450000+00:00 | 2026-04-23T18:30:38.923000+00:00 | 240h 37m |
| argumentationToolEvent | 42 | 1.67 | 1 | 2 | 0 | 2026-04-17T17:57:31.755000+00:00 | 2026-04-23T18:07:50.659000+00:00 | 144h 10m |
| soilMachine | 18 | 0.71 | 1 | 1 | 0 | 2026-04-21T18:21:47.955000+00:00 | 2026-04-21T18:29:58.207000+00:00 | 8m 10s |
| Soil Key Puzzle | 13 | 0.52 | 1 | 3 | 0 | 2026-04-13T18:23:29.133000+00:00 | 2026-04-21T18:10:30.682000+00:00 | 191h 47m |
| TerasGardenBox | 11 | 0.44 | 1 | 1 | 0 | 2026-04-23T18:13:53.523000+00:00 | 2026-04-23T18:15:07.867000+00:00 | 1m 14s |
| argumentationNodeEvent | 9 | 0.36 | 1 | 2 | 0 | 2026-04-13T18:06:27.030000+00:00 | 2026-04-17T18:25:00.245000+00:00 | 96h 18m |
| argumentationEvent | 8 | 0.32 | 1 | 3 | 0 | 2026-04-13T18:06:20.961000+00:00 | 2026-04-23T18:07:22.896000+00:00 | 240h 1m |
| EndOfUnit | 3 | 0.12 | 1 | 3 | 0 | 2026-04-13T18:10:46.571000+00:00 | 2026-04-23T18:20:53.282000+00:00 | 240h 10m |
| WaterChamberEvent | 2 | 0.08 | 1 | 1 | 0 | 2026-04-23T18:28:57.223000+00:00 | 2026-04-23T18:29:14.541000+00:00 | 17.3s |
| crash | 1 | 0.04 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 432303.356s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.029s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 372.031s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.941s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 29.617s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 17.027s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.175s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 6 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowFocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 82 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowUnfocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 76 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.314s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 173 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: MapCloseEvent; MapOpenEvent; Selected; Unselected; WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: dragEnd; dragStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend; Map; Waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: waypoint 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `WaterChamberEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Off 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — baseline categorical value(s) not seen this build. 
  - Observed: Two 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Condenser; DualChamber_Evaporator; VentSwitch 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.room` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 9 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 4.7x vs baseline. 
  - Observed: 42 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 44; 45; 52; 53; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f726.jsonl[174] _id=69dd30e47957a33870f25ba4 ts=2026-04-13T18:07:31.3160000Z`; `69cdc907d385e3b94310f726.jsonl[430] _id=69dd36ea7957a33870f285aa ts=2026-04-13T18:33:12.3870000Z`; `69cdc907d385e3b94310f726.jsonl[1248] _id=69e27aff1724f0c9e2f77e2a ts=2026-04-17T18:25:02.1620000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 173 records, TopographicMapEvent: 120 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 7 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1501 | 0.0 | 2.068 | 577.051 | 46.044 | 339391.804 | 0.1 | 430 | 7 |
| PlayerPositionEvent | 536 | 23.043 | 30.029 | 1615.755 | 57.729 | 339361.543 | 0.04 | 0 | 5 |
| Topographic Map Event | 172 | 0.0 | 15.918 | 4008.257 | 288.028 | 343611.763 | 0.01 | 1 | 6 |
| TopographicMapEvent | 119 | 0.291 | 3.407 | 5792.784 | 407.548 | 343607.71 | 0.01 | 0 | 6 |
| questEvent | 71 | 0.003 | 141.394 | 12200.359 | 84948.867 | 339729.15 | 0.0 | 9 | 10 |
| argumentationToolEvent | 41 | 0.002 | 1.175 | 12658.998 | 413.711 | 517403.972 | 0.0 | 6 | 1 |
| soilMachine | 17 | 1.016 | 6.314 | 28.838 | 121.518 | 148.761 | 2.08 | 0 | 0 |
| Soil Key Puzzle | 12 | 2.951 | 372.031 | 57535.129 | 249027.573 | 344229.161 | 0.0 | 0 | 5 |
| TerasGardenBox | 10 | 0.982 | 1.941 | 7.434 | 23.33 | 26.277 | 8.07 | 0 | 0 |
| argumentationNodeEvent | 8 | 3.047 | 17.027 | 43339.152 | 225282.986 | 346548.816 | 0.0 | 0 | 1 |
| argumentationEvent | 7 | 0.088 | 29.617 | 123437.419 | 466099.58 | 517340.673 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 173826.934 | 432303.356 | 432303.356 | 664932.135 | 690779.777 | 0.0 | 0 | 2 |
| WaterChamberEvent | 1 | 17.318 | 17.318 | 17.318 | 17.318 | 17.318 | 3.46 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.029s (p5 29.97s, p95 57.73s, n=536) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `441ms: 69cdc907d385e3b94310f726.jsonl[2208] _id=69e2761f1724f0c9e2f76496 ts=2026-04-17T18:03:50.607Z ~ 69cdc907d385e3b94310f726.jsonl[1057] _id=69e276201724f0c9e2f76498 ts=2026-04-17T18:03:51.048Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `88ms: 69cdc907d385e3b94310f726.jsonl[2238] _id=69e27aff1724f0c9e2f77e28 ts=2026-04-17T18:25:02.1350000Z ~ 69cdc907d385e3b94310f726.jsonl[1247] _id=69e27aff1724f0c9e2f77e2e ts=2026-04-17T18:25:02.2230000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `805ms: 69cdc907d385e3b94310f726.jsonl[1027] _id=69e2748c1724f0c9e2f75b1a ts=2026-04-17T17:57:31.7550000Z ~ 69cdc907d385e3b94310f726.jsonl[1032] _id=69e2748e1724f0c9e2f75b22 ts=2026-04-17T17:57:32.5600000Z`; `818ms: 69cdc907d385e3b94310f726.jsonl[1047] _id=69e2757d1724f0c9e2f7619c ts=2026-04-17T18:01:32.9300000Z ~ 69cdc907d385e3b94310f726.jsonl[1050] _id=69e2757e1724f0c9e2f761a0 ts=2026-04-17T18:01:33.7480000Z`; `753ms: 69cdc907d385e3b94310f726.jsonl[1048] _id=69e2757d1724f0c9e2f7619e ts=2026-04-17T18:01:33.0030000Z ~ 69cdc907d385e3b94310f726.jsonl[1049] _id=69e2757e1724f0c9e2f761a2 ts=2026-04-17T18:01:33.7560000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f726.jsonl[1347] _id=69e27e561724f0c9e2f78c2a ts=2026-04-17T18:39:16.9570000Z -> 69cdc907d385e3b94310f726.jsonl[1351] _id=69e7ac151724f0c9e2f91639 ts=2026-04-21T16:55:48.7610000Z; 47h 21m: 69cdc907d385e3b94310f726.jsonl[1873] _id=69e7c46a1724f0c9e2f9a6a9 ts=2026-04-21T18:39:37.9520000Z -> 69cdc907d385e3b94310f726.jsonl[1883] _id=69ea5e761724f0c9e2fb05bf ts=2026-04-23T18:01:25.9900000Z; 47h 8m: 69cdc907d385e3b94310f726.jsonl[510] _id=69dd389a7957a33870f290ff ts=2026-04-13T18:40:25.1630000Z -> 69cdc907d385e3b94310f726.jsonl[525] _id=69dfcf897957a33870f40f21 ts=2026-04-15T17:48:55.0930000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 430 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f726.jsonl[2506] _id=69ea63051724f0c9e2fb2b75 ts=2026-04-23T18:20:53.3030000Z -> 69cdc907d385e3b94310f726.jsonl[2504] _id=69ea63121724f0c9e2fb2bcb ts=2026-04-23T18:20:53.303Z; 1ms: 69cdc907d385e3b94310f726.jsonl[1267] _id=69e27c1b1724f0c9e2f77f68 ts=2026-04-17T18:29:46.3080000Z -> 69cdc907d385e3b94310f726.jsonl[1272] _id=69e27c1b1724f0c9e2f77f6a ts=2026-04-17T18:29:46.3090000Z; 3ms: 69cdc907d385e3b94310f726.jsonl[1300] _id=69e27ce81724f0c9e2f7834c ts=2026-04-17T18:33:11.1230000Z -> 69cdc907d385e3b94310f726.jsonl[1301] _id=69e27ce81724f0c9e2f7834e ts=2026-04-17T18:33:11.1260000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 52m 
  - Evidence: 191h 52m: 69cdc907d385e3b94310f726.jsonl[227] _id=69dd31a77957a33870f260e2 ts=2026-04-13T18:10:46.5710000Z -> 69cdc907d385e3b94310f726.jsonl[1635] _id=69e7bc021724f0c9e2f966f9 ts=2026-04-21T18:03:46.3480000Z; 48h 17m: 69cdc907d385e3b94310f726.jsonl[1635] _id=69e7bc021724f0c9e2f966f9 ts=2026-04-21T18:03:46.3480000Z -> 69cdc907d385e3b94310f726.jsonl[2505] _id=69ea63051724f0c9e2fb2b73 ts=2026-04-23T18:20:53.2820000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f726.jsonl[1350] _id=69e27e721724f0c9e2f78ca8 ts=2026-04-17T18:39:45.7450000Z -> 69cdc907d385e3b94310f726.jsonl[2245] _id=69e7ac141724f0c9e2f91631 ts=2026-04-21T16:55:47.2880000Z; 47h 21m: 69cdc907d385e3b94310f726.jsonl[1878] _id=69e7c48d1724f0c9e2f9a731 ts=2026-04-21T18:40:13.1360000Z -> 69cdc907d385e3b94310f726.jsonl[1880] _id=69ea5e731724f0c9e2fb05b4 ts=2026-04-23T18:01:23.4440000Z; 47h 7m: 69cdc907d385e3b94310f726.jsonl[522] _id=69dd38d17957a33870f291fe ts=2026-04-13T18:41:20.1190000Z -> 69cdc907d385e3b94310f726.jsonl[527] _id=69dfcf847957a33870f40efd ts=2026-04-15T17:48:51.6900000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 69cdc907d385e3b94310f726.jsonl[1302] _id=69e27cdb1724f0c9e2f782ee ts=2026-04-17T18:32:58.8190000Z -> 69cdc907d385e3b94310f726.jsonl[1664] _id=69e7bd801724f0c9e2f97175 ts=2026-04-21T18:10:07.9800000Z; 47h 32m: 69cdc907d385e3b94310f726.jsonl[310] _id=69dd34a47957a33870f275b8 ts=2026-04-13T18:23:32.0840000Z -> 69cdc907d385e3b94310f726.jsonl[573] _id=69dfd1247957a33870f41ae5 ts=2026-04-15T17:55:47.4490000Z; 47h 29m: 69cdc907d385e3b94310f726.jsonl[760] _id=69dfd9b57957a33870f45431 ts=2026-04-15T18:32:20.5720000Z -> 69cdc907d385e3b94310f726.jsonl[1056] _id=69e275aa1724f0c9e2f76262 ts=2026-04-17T18:02:17.4080000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 69cdc907d385e3b94310f726.jsonl[1288] _id=69e27c7b1724f0c9e2f780fc ts=2026-04-17T18:31:23.0030000Z -> 69cdc907d385e3b94310f726.jsonl[2306] _id=69e7bab71724f0c9e2f95d2d ts=2026-04-21T17:58:14.7660000Z; 47h 8m: 69cdc907d385e3b94310f726.jsonl[519] _id=69dd38af7957a33870f29172 ts=2026-04-13T18:40:46.8310000Z -> 69cdc907d385e3b94310f726.jsonl[533] _id=69dfcf9b7957a33870f40f6b ts=2026-04-15T17:49:14.9640000Z; 46h 21m: 69cdc907d385e3b94310f726.jsonl[804] _id=69dfdafc7957a33870f460f1 ts=2026-04-15T18:37:47.5000000Z -> 69cdc907d385e3b94310f726.jsonl[854] _id=69e267001724f0c9e2f728a4 ts=2026-04-17T16:59:43.4650000Z
- **INFO / Info** `Topographic Map Event` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f726.jsonl[2207] _id=69e275d11724f0c9e2f76328 ts=2026-04-17T18:02:56.8730000Z -> 69cdc907d385e3b94310f726.jsonl[2209] _id=69e2761e1724f0c9e2f7648c ts=2026-04-17T18:02:56.873Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 69cdc907d385e3b94310f726.jsonl[1283] _id=69e27c651724f0c9e2f7807c ts=2026-04-17T18:31:00.1030000Z -> 69cdc907d385e3b94310f726.jsonl[2302] _id=69e7ba9c1724f0c9e2f95c19 ts=2026-04-21T17:57:47.8130000Z; 47h 9m: 69cdc907d385e3b94310f726.jsonl[516] _id=69dd38987957a33870f290f4 ts=2026-04-13T18:40:23.3850000Z -> 69cdc907d385e3b94310f726.jsonl[531] _id=69dfcfa67957a33870f40fc1 ts=2026-04-15T17:49:25.8910000Z; 46h 22m: 69cdc907d385e3b94310f726.jsonl[788] _id=69dfda777957a33870f45d23 ts=2026-04-15T18:35:35.0170000Z -> 69cdc907d385e3b94310f726.jsonl[847] _id=69e266a21724f0c9e2f725dc ts=2026-04-17T16:58:09.4850000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 42m 
  - Evidence: 143h 42m: 69cdc907d385e3b94310f726.jsonl[1247] _id=69e27aff1724f0c9e2f77e2e ts=2026-04-17T18:25:02.2230000Z -> 69cdc907d385e3b94310f726.jsonl[1920] _id=69ea5fda1724f0c9e2fb0fd9 ts=2026-04-23T18:07:22.8960000Z; 96h 15m: 69cdc907d385e3b94310f726.jsonl[170] _id=69dd30e47957a33870f25ba2 ts=2026-04-13T18:07:31.2790000Z -> 69cdc907d385e3b94310f726.jsonl[1221] _id=69e27a8d1724f0c9e2f77b7c ts=2026-04-17T18:23:08.3090000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 15m 
  - Evidence: 96h 15m: 69cdc907d385e3b94310f726.jsonl[172] _id=69dd30df7957a33870f25b8e ts=2026-04-13T18:07:26.5700000Z -> 69cdc907d385e3b94310f726.jsonl[1223] _id=69e27a941724f0c9e2f77bb6 ts=2026-04-17T18:23:15.3860000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 43m 
  - Evidence: 143h 43m: 69cdc907d385e3b94310f726.jsonl[1230] _id=69e27abc1724f0c9e2f77c8c ts=2026-04-17T18:23:55.8670000Z -> 69cdc907d385e3b94310f726.jsonl[2413] _id=69ea5fd71724f0c9e2fb0fbb ts=2026-04-23T18:07:19.8390000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.002s..0.008s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f726.jsonl[2413] _id=69ea5fd71724f0c9e2fb0fbb ts=2026-04-23T18:07:19.8390000Z -> 69cdc907d385e3b94310f726.jsonl[1919] _id=69ea5fd81724f0c9e2fb0fbf ts=2026-04-23T18:07:19.8410000Z; 8ms: 69cdc907d385e3b94310f726.jsonl[1050] _id=69e2757e1724f0c9e2f761a0 ts=2026-04-17T18:01:33.7480000Z -> 69cdc907d385e3b94310f726.jsonl[1049] _id=69e2757e1724f0c9e2f761a2 ts=2026-04-17T18:01:33.7560000Z; 8ms: 69cdc907d385e3b94310f726.jsonl[1091] _id=69e277241724f0c9e2f76a60 ts=2026-04-17T18:08:35.9690000Z -> 69cdc907d385e3b94310f726.jsonl[1094] _id=69e277251724f0c9e2f76a62 ts=2026-04-17T18:08:35.9770000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 22m 
  - Evidence: 94h 22m: 69cdc907d385e3b94310f726.jsonl[1307] _id=69e27d041724f0c9e2f783f8 ts=2026-04-17T18:33:39.3940000Z -> 69cdc907d385e3b94310f726.jsonl[1353] _id=69e7ac151724f0c9e2f91637 ts=2026-04-21T16:55:48.5440000Z; 47h 22m: 69cdc907d385e3b94310f726.jsonl[1854] _id=69e7c4341724f0c9e2f9a523 ts=2026-04-21T18:38:44.0430000Z -> 69cdc907d385e3b94310f726.jsonl[1881] _id=69ea5e751724f0c9e2fb05bd ts=2026-04-23T18:01:24.6910000Z; 47h 18m: 69cdc907d385e3b94310f726.jsonl[390] _id=69dd362d7957a33870f2802a ts=2026-04-13T18:30:04.1860000Z -> 69cdc907d385e3b94310f726.jsonl[529] _id=69dfcf897957a33870f40f27 ts=2026-04-15T17:48:55.9800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.003s..0.009s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f726.jsonl[144] _id=69dd30857957a33870f25958 ts=2026-04-13T18:05:56.4560000Z -> 69cdc907d385e3b94310f726.jsonl[145] _id=69dd30867957a33870f2595a ts=2026-04-13T18:05:56.4590000Z; 7ms: 69cdc907d385e3b94310f726.jsonl[2123] _id=69ea654e1724f0c9e2fb3c09 ts=2026-04-23T18:30:38.9160000Z -> 69cdc907d385e3b94310f726.jsonl[2124] _id=69ea654f1724f0c9e2fb3c0b ts=2026-04-23T18:30:38.9230000Z; 9ms: 69cdc907d385e3b94310f726.jsonl[1737] _id=69e7bfab1724f0c9e2f9816d ts=2026-04-21T18:19:23.0010000Z -> 69cdc907d385e3b94310f726.jsonl[1738] _id=69e7bfab1724f0c9e2f9816f ts=2026-04-21T18:19:23.0100000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f726.jsonl:69cdc907d385e3b94310f726, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f726.jsonl[310] _id=69dd34a47957a33870f275b8 ts=2026-04-13T18:23:32.0840000Z`; `69cdc907d385e3b94310f726.jsonl[1302] _id=69e27cdb1724f0c9e2f782ee ts=2026-04-17T18:32:58.8190000Z`; `69cdc907d385e3b94310f726.jsonl[1666] _id=69e7bd971724f0c9e2f97223 ts=2026-04-21T18:10:30.6820000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 120 record(s) match the trigger in 69cdc907d385e3b94310f726.jsonl:69cdc907d385e3b94310f726, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f726.jsonl[399] _id=69dd366f7957a33870f2821e ts=2026-04-13T18:31:10.7950000Z`; `69cdc907d385e3b94310f726.jsonl[397] _id=69dd36707957a33870f2822a ts=2026-04-13T18:31:11.2910000Z`; `69cdc907d385e3b94310f726.jsonl[400] _id=69dd36777957a33870f28252 ts=2026-04-13T18:31:18.3840000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f726.jsonl[844] _id=69e266831724f0c9e2f72514 ts=2026-04-17T16:57:38.2640000Z`; `69cdc907d385e3b94310f726.jsonl[1850] _id=69e7c3531724f0c9e2f99dcf ts=2026-04-21T18:34:58.8680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f726.jsonl[1247] _id=69e27aff1724f0c9e2f77e2e ts=2026-04-17T18:25:02.2230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f726.jsonl[1028] _id=69e2748d1724f0c9e2f75b20 ts=2026-04-17T17:57:32.5510000Z`; `69cdc907d385e3b94310f726.jsonl[2200] _id=69e274931724f0c9e2f75b56 ts=2026-04-17T17:57:38.9180000Z`; `69cdc907d385e3b94310f726.jsonl[1033] _id=69e274981724f0c9e2f75b79 ts=2026-04-17T17:57:43.7680000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f726.jsonl[2089] _id=69ea63061724f0c9e2fb2b83 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f726.jsonl[603] _id=69dfd1f37957a33870f420f9 ts=2026-04-15T17:59:14.5140000Z`; `69cdc907d385e3b94310f726.jsonl[635] _id=69dfd3497957a33870f42acf ts=2026-04-15T18:04:56.9430000Z`; `69cdc907d385e3b94310f726.jsonl[676] _id=69dfd4db7957a33870f434ad ts=2026-04-15T18:11:38.5760000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f726.jsonl[1032] _id=69e2748e1724f0c9e2f75b22 ts=2026-04-17T17:57:32.5600000Z`; `69cdc907d385e3b94310f726.jsonl[1034] _id=69e274971724f0c9e2f75b70 ts=2026-04-17T17:57:42.5930000Z`; `69cdc907d385e3b94310f726.jsonl[956] _id=69e274991724f0c9e2f75b7c ts=2026-04-17T17:57:43.8070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 181 unmatched 'DialogueStartEvent' (totals: 338 start, 159 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'Started' (totals: 10 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'argumentationToolOpen' (totals: 20 open, 22 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'questActiveEvent' (totals: 48 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.90s, min -78.12s, max -0.06s over 2520 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f726\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 173 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1502 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (388); Unit 2 Prod (Refactor) (307); Unit 4 Dev (226); Unit 1 Dev (174); Unit 3 Dungeon Dev (156); Unit 4 Dev - Anderson Base (128); Unit 4 Dev - Dungeon (100); Unit 5 Dev - Dungeon (23)
- **eventKey:** present on 1005 of 1502 records
- **Intervals:** median 2.07s (p5 0.01s / p95 46.04s, n=1501)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1005; [conversationId, dialogueEventType] x497
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1502/1502 records)
    numeric range 10 .. 114 (40 unique)
data.dialogueEventType  (string, 1502/1502 records)
    "DialogueNodeEvent"  x1005
    "DialogueStartEvent"  x338
    "DialogueFinishEvent"  x159
data.nodeId  (number, 1005/1502 records)
    numeric range 0 .. 289 (204 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 547 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dungeon Dev (131); Unit 2 Prod (Refactor) (126); Unit 3 Dev (119); Unit 4 Dev (56); Unit 1 Dev (35); Unit 4 Dev - Dungeon (33); Unit 4 Dev - Anderson Base (24); Unit 5 Dev - Dungeon (23)
- **Intervals:** median 30.03s (p5 29.97s / p95 57.73s, n=536)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 547/547 records)
data.position.x  (number, 547/547 records)
    numeric range -682.131 .. 1558.57 (272 unique)
data.position.y  (number, 547/547 records)
    numeric range -112.933 .. 155.539 (227 unique)
data.position.z  (number, 547/547 records)
    numeric range -1119.42 .. 1800.12 (272 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 173 records

- **Scenes:** Unit 3 Dev (125); Unit 2 Prod (Refactor) (48)
- **Intervals:** median 15.92s (p5 1.60s / p95 288.03s, n=172)
- **Fields under `data`:**

```text
data.actionType  (string, 173/173 records)
    "MapCloseEvent"  x88
    "MapOpenEvent"  x85
data.featureUsed  (string, 173/173 records)
    "Map"  x173
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 120 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (70); Unit 2 Prod (Refactor) (50)
- **Intervals:** median 3.41s (p5 0.58s / p95 407.55s, n=119)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 120/120 records)
    "dragEnd"  x60
    "dragStart"  x60
data.featureUsed  (string, 120/120 records)
    "waypoint"  x120
data.location  (object, 120/120 records)
data.location.x  (number, 120/120 records)
    numeric range -770.79 .. 299.322 (60 unique)
data.location.y  (number, 120/120 records)
    numeric range -369.764 .. 324.745 (61 unique)
data.location.z  (number, 120/120 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 72 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 3 Dev (16); Unit 1 Dev (12); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (3); Unit 5 Dev - Dungeon (3)
- **eventKey:** present on 72 of 72 records
- **Intervals:** median 141.39s (p5 0.01s / p95 84948.87s, n=71)
- **`data` key-set variants:** [questEventType, questID, questName] x48; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Fields under `data`:**

```text
data.questEventType  (string, 72/72 records)
    "questActiveEvent"  x48
    "questFinishEvent"  x24
data.questID  (string, 72/72 records)
    27 unique values (see csv/event_unique_values.csv)
data.questName  (string, 72/72 records)
    27 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/72 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 42 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (30); Unit 4 Dev - Anderson Base (12)
- **Intervals:** median 1.18s (p5 0.01s / p95 413.71s, n=41)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "argumentationToolClose"  x22
    "argumentationToolOpen"  x20
data.argumentationTitle  (string, 42/42 records)
    "Unit 3 - Pollution Upstream"  x30
    "Unit 4 - Flooding"  x12
data.toolName  (string, 42/42 records)
    "BackingInfoPanel - "  x12
    "BackingInfoPanel - Watershed Image"  x12
    "BackingInfoPanel - Soil Flow Rates"  x8
    "BackingInfoPanel - Pollution Site Data"  x6
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 18 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (18)
- **Intervals:** median 6.31s (p5 1.25s / p95 121.52s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "ChangeCanister"  x18
data.canisterType  (string, 18/18 records)
    "Gravel"  x6
    "Bedrock"  x4
    "Clay"  x4
    "Sand"  x4
data.floor  (string, 18/18 records)
    "4"  x9
    "3"  x5
    "5"  x4
data.machine  (string, 18/18 records)
    "1"  x17
    "2"  x1
data.row  (string, 18/18 records)
    "TopRow"  x16
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 13 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (3); Unit 4 Dev (2)
- **Intervals:** median 372.03s (p5 13.81s / p95 249027.57s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 13/13 records)
    "Started"  x10
    "Finished"  x3
data.Unit  (string, 13/13 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x3
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 1.94s (p5 1.05s / p95 23.33s, n=10)
- **`data` key-set variants:** [actionType, boxID, soilType] x7; [actionType, boxId, soilType] x4
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "soilSelected"  x7
    "cameraPlaced"  x4
data.boxID  (string, 7/11 records)
    "1"  x5
    "0"  x1
    "2"  x1
data.boxId  (string, 4/11 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 11/11 records)
    "Clay"  x5
    "Gravel"  x3
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationNodeEvent` — 9 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (5); Unit 1 Dev (4)
- **Intervals:** median 17.03s (p5 3.19s / p95 225282.99s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationNodeAdd"  x8
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
data.nodeName  (string, 9/9 records)
    "I"  x3
    "3"  x2
    "1"  x1
    "5"  x1
    "A"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 29.62s (p5 5.77s / p95 466099.58s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 432303.36s (p5 199674.58s / p95 664932.13s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `WaterChamberEvent` — 2 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (2)
- **Intervals:** median 17.32s (p5 17.32s / p95 17.32s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "On"  x2
data.floor  (string, 2/2 records)
    "1"  x2
data.machineNumber  (string, 2/2 records)
    "One"  x2
data.machineType  (string, 2/2 records)
    "Condenser"  x1
    "Evaporator"  x1
data.room  (string, 2/2 records)
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DEBUGMenu` : expected event type absent although its content was played — possible logging failure
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : expected event type absent although its content was played — possible logging failure
- `ObjectInterEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : expected event type absent although its content was played — possible logging failure
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "dragStart" (60x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*