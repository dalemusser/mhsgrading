# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f78b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f78b
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f78b.jsonl
- **Records:** 2942 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f78b
- **Time span:** 2026-04-14T13:50:53.688000+00:00 .. 2026-04-24T14:33:16.692000+00:00 (240h 42m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f78b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2942 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 70 INFO, 0 NOT_TESTED, 58 PASS.
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
| DialogueEvent | 2044 | 69.48 | 1 | 9 | 1402 | 2026-04-14T13:51:11.766000+00:00 | 2026-04-24T14:33:09.788000+00:00 | 240h 41m |
| PlayerPositionEvent | 550 | 18.69 | 1 | 9 | 0 | 2026-04-14T13:50:53.688000+00:00 | 2026-04-24T14:32:57.515000+00:00 | 240h 42m |
| questEvent | 77 | 2.62 | 1 | 9 | 77 | 2026-04-14T13:51:11.753000+00:00 | 2026-04-24T14:32:29.499000+00:00 | 240h 41m |
| WaterChamberEvent | 62 | 2.11 | 1 | 1 | 0 | 2026-04-24T14:17:41.719000+00:00 | 2026-04-24T14:25:23.876000+00:00 | 7m 42s |
| soilMachine | 52 | 1.77 | 1 | 1 | 0 | 2026-04-22T14:07:31.661000+00:00 | 2026-04-22T14:16:15.541000+00:00 | 8m 43s |
| Topographic Map Event | 40 | 1.36 | 1 | 2 | 0 | 2026-04-16T13:57:31.720000+00:00 | 2026-04-20T14:34:37.835000+00:00 | 96h 37m |
| argumentationNodeEvent | 34 | 1.16 | 1 | 2 | 0 | 2026-04-14T14:19:54.281000+00:00 | 2026-04-20T14:13:52.372000+00:00 | 143h 53m |
| TopographicMapEvent | 28 | 0.95 | 1 | 2 | 0 | 2026-04-16T14:01:22.688000+00:00 | 2026-04-20T14:34:34.500000+00:00 | 96h 33m |
| argumentationToolEvent | 28 | 0.95 | 1 | 3 | 0 | 2026-04-20T14:07:11.432000+00:00 | 2026-04-24T14:28:43.004000+00:00 | 96h 21m |
| argumentationEvent | 10 | 0.34 | 1 | 4 | 0 | 2026-04-14T14:18:31.479000+00:00 | 2026-04-24T14:30:47.416000+00:00 | 240h 12m |
| Soil Key Puzzle | 6 | 0.2 | 1 | 3 | 0 | 2026-04-16T14:14:13.189000+00:00 | 2026-04-22T13:56:23.356000+00:00 | 143h 42m |
| TerasGardenBox | 6 | 0.2 | 1 | 1 | 0 | 2026-04-24T14:10:40.591000+00:00 | 2026-04-24T14:11:17.315000+00:00 | 36.7s |
| EndOfUnit | 4 | 0.14 | 1 | 4 | 0 | 2026-04-14T14:23:15.476000+00:00 | 2026-04-24T14:33:16.692000+00:00 | 240h 10m |
| crash | 1 | 0.03 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.717s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 174338.42s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.003s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 42.284s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 1.911s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 9.024s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.235s median 
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
  - Observed: 1.601s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 62 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 34 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 28 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 10.4x vs baseline. 
  - Observed: 52 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 16 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[101] _id=69de4d217957a33870f35871 ts=2026-04-14T14:20:17.4120000Z`; `69cdc965d385e3b94310f78b.jsonl[1817] _id=69e0e5b07957a33870f4fe8f ts=2026-04-16T13:35:43.5220000Z`; `69cdc965d385e3b94310f78b.jsonl[1804] _id=69e0e5b07957a33870f4fe95 ts=2026-04-16T13:35:43.9620000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 28 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2043 | 0.0 | 1.717 | 424.14 | 36.164 | 341040.218 | 0.14 | 546 | 5 |
| PlayerPositionEvent | 536 | 5.277 | 30.003 | 1615.966 | 36.168 | 340932.521 | 0.04 | 0 | 4 |
| questEvent | 76 | 0.003 | 130.52 | 11401.023 | 43922.863 | 341569.492 | 0.01 | 13 | 9 |
| WaterChamberEvent | 61 | 0.188 | 1.911 | 7.576 | 32.257 | 68.913 | 7.92 | 0 | 0 |
| soilMachine | 51 | 0.19 | 1.601 | 10.272 | 45.681 | 134.129 | 5.84 | 0 | 0 |
| Topographic Map Event | 39 | 0.16 | 38.318 | 8918.618 | 1193.16 | 341767.255 | 0.01 | 0 | 4 |
| argumentationNodeEvent | 33 | 0.773 | 9.024 | 15698.124 | 118.009 | 517394.635 | 0.0 | 0 | 1 |
| TopographicMapEvent | 27 | 0.279 | 3.4 | 12873.771 | 1533.186 | 343201.831 | 0.0 | 0 | 3 |
| argumentationToolEvent | 27 | 0.004 | 1.235 | 12847.836 | 1018.126 | 345113.61 | 0.0 | 4 | 2 |
| argumentationEvent | 9 | 0.074 | 131.293 | 96081.771 | 448392.471 | 517365.639 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 5 | 17.723 | 42.284 | 103466.033 | 412352.907 | 514839.661 | 0.0 | 0 | 2 |
| TerasGardenBox | 5 | 1.298 | 3.266 | 7.345 | 15.282 | 15.362 | 8.17 | 0 | 0 |
| EndOfUnit | 3 | 1192.005 | 174338.42 | 288200.405 | 637597.554 | 689070.791 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.003s (p5 29.96s, p95 36.17s, n=536) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `655ms: 69cdc965d385e3b94310f78b.jsonl[1510] _id=69eb7d301724f0c9e2fb96df ts=2026-04-24T14:24:47.5710000Z ~ 69cdc965d385e3b94310f78b.jsonl[1511] _id=69eb7d311724f0c9e2fb96e3 ts=2026-04-24T14:24:48.2260000Z`; `616ms: 69cdc965d385e3b94310f78b.jsonl[2846] _id=69eb7d301724f0c9e2fb96e1 ts=2026-04-24T14:24:47.8780000Z ~ 69cdc965d385e3b94310f78b.jsonl[1512] _id=69eb7d311724f0c9e2fb96e7 ts=2026-04-24T14:24:48.4940000Z`; `590ms: 69cdc965d385e3b94310f78b.jsonl[1511] _id=69eb7d311724f0c9e2fb96e3 ts=2026-04-24T14:24:48.2260000Z ~ 69cdc965d385e3b94310f78b.jsonl[1513] _id=69eb7d311724f0c9e2fb96e9 ts=2026-04-24T14:24:48.8160000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `74ms: 69cdc965d385e3b94310f78b.jsonl[759] _id=69e634a21724f0c9e2f89629 ts=2026-04-20T14:13:53.6180000Z ~ 69cdc965d385e3b94310f78b.jsonl[762] _id=69e634a21724f0c9e2f8962f ts=2026-04-20T14:13:53.6920000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `795ms: 69cdc965d385e3b94310f78b.jsonl[722] _id=69e633141724f0c9e2f88dc3 ts=2026-04-20T14:07:15.9990000Z ~ 69cdc965d385e3b94310f78b.jsonl[723] _id=69e633151724f0c9e2f88dcf ts=2026-04-20T14:07:16.7940000Z`; `4ms: 69cdc965d385e3b94310f78b.jsonl[2660] _id=69eb77fd1724f0c9e2fb7ca3 ts=2026-04-24T14:02:36.1310000Z ~ 69cdc965d385e3b94310f78b.jsonl[2663] _id=69eb77fd1724f0c9e2fb7ca5 ts=2026-04-24T14:02:36.1350000Z`; `769ms: 69cdc965d385e3b94310f78b.jsonl[1355] _id=69eb78ac1724f0c9e2fb80df ts=2026-04-24T14:05:31.5330000Z ~ 69cdc965d385e3b94310f78b.jsonl[1356] _id=69eb78ad1724f0c9e2fb80e5 ts=2026-04-24T14:05:32.3020000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 69cdc965d385e3b94310f78b.jsonl[1571] _id=69eb7ea21724f0c9e2fb9d8f ts=2026-04-24T14:30:57.5630000Z ~ 69cdc965d385e3b94310f78b.jsonl[2904] _id=69eb7ea21724f0c9e2fb9d95 ts=2026-04-24T14:30:57.5680000Z`; `14ms: 69cdc965d385e3b94310f78b.jsonl[2922] _id=69eb7ee81724f0c9e2fb9f43 ts=2026-04-24T14:32:07.8680000Z ~ 69cdc965d385e3b94310f78b.jsonl[2927] _id=69eb7ee81724f0c9e2fb9f47 ts=2026-04-24T14:32:07.8820000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `554ms: 69cdc965d385e3b94310f78b.jsonl[1205] _id=69e8d7791724f0c9e2fa6165 ts=2026-04-22T14:13:13.1110000Z ~ 69cdc965d385e3b94310f78b.jsonl[2568] _id=69e8d77a1724f0c9e2fa616d ts=2026-04-22T14:13:13.6650000Z`; `376ms: 69cdc965d385e3b94310f78b.jsonl[2570] _id=69e8d77c1724f0c9e2fa617b ts=2026-04-22T14:13:16.0840000Z ~ 69cdc965d385e3b94310f78b.jsonl[1206] _id=69e8d77d1724f0c9e2fa6183 ts=2026-04-22T14:13:16.4600000Z`; `265ms: 69cdc965d385e3b94310f78b.jsonl[1206] _id=69e8d77d1724f0c9e2fa6183 ts=2026-04-22T14:13:16.4600000Z ~ 69cdc965d385e3b94310f78b.jsonl[1207] _id=69e8d77d1724f0c9e2fa6187 ts=2026-04-22T14:13:16.7250000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc965d385e3b94310f78b.jsonl[2040] _id=69e0f3637957a33870f55761 ts=2026-04-16T14:34:10.2930000Z -> 69cdc965d385e3b94310f78b.jsonl[567] _id=69e627931724f0c9e2f84ac7 ts=2026-04-20T13:18:10.5110000Z; 47h 28m: 69cdc965d385e3b94310f78b.jsonl[2620] _id=69e8db1d1724f0c9e2fa7455 ts=2026-04-22T14:28:45.1770000Z -> 69cdc965d385e3b94310f78b.jsonl[2627] _id=69eb76cf1724f0c9e2fb76af ts=2026-04-24T13:57:34.2960000Z; 47h 3m: 69cdc965d385e3b94310f78b.jsonl[1798] _id=69de4f8b7957a33870f3694e ts=2026-04-14T14:30:35.5790000Z -> 69cdc965d385e3b94310f78b.jsonl[167] _id=69e0e55c7957a33870f4fa85 ts=2026-04-16T13:34:19.9320000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 546 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f78b.jsonl[1105] _id=69e8d1831724f0c9e2fa3bff ts=2026-04-22T13:47:46.2950000Z -> 69cdc965d385e3b94310f78b.jsonl[1107] _id=69e8d1911724f0c9e2fa3c41 ts=2026-04-22T13:47:46.295Z; 2ms: 69cdc965d385e3b94310f78b.jsonl[183] _id=69e0e6b37957a33870f504a7 ts=2026-04-16T13:40:03.4360000Z -> 69cdc965d385e3b94310f78b.jsonl[184] _id=69e0e6b37957a33870f504a9 ts=2026-04-16T13:40:03.4380000Z; 2ms: 69cdc965d385e3b94310f78b.jsonl[754] _id=69e6348b1724f0c9e2f8957d ts=2026-04-20T14:13:30.0970000Z -> 69cdc965d385e3b94310f78b.jsonl[751] _id=69e6348b1724f0c9e2f8957f ts=2026-04-20T14:13:30.0990000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 24m 
  - Evidence: 191h 24m: 69cdc965d385e3b94310f78b.jsonl[135] _id=69de4dd37957a33870f35d07 ts=2026-04-14T14:23:15.4760000Z -> 69cdc965d385e3b94310f78b.jsonl[1106] _id=69e8d1821724f0c9e2fa3bfd ts=2026-04-22T13:47:46.2670000Z; 48h 25m: 69cdc965d385e3b94310f78b.jsonl[1106] _id=69e8d1821724f0c9e2fa3bfd ts=2026-04-22T13:47:46.2670000Z -> 69cdc965d385e3b94310f78b.jsonl[1479] _id=69eb7a851724f0c9e2fb89dd ts=2026-04-24T14:13:24.6870000Z; 19m 52s: 69cdc965d385e3b94310f78b.jsonl[1479] _id=69eb7a851724f0c9e2fb89dd ts=2026-04-24T14:13:24.6870000Z -> 69cdc965d385e3b94310f78b.jsonl[2941] _id=69eb7f2d1724f0c9e2fba117 ts=2026-04-24T14:33:16.6920000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc965d385e3b94310f78b.jsonl[2045] _id=69e0f3b07957a33870f558f5 ts=2026-04-16T14:35:28.6800000Z -> 69cdc965d385e3b94310f78b.jsonl[565] _id=69e627761724f0c9e2f84a83 ts=2026-04-20T13:17:41.2010000Z; 47h 27m: 69cdc965d385e3b94310f78b.jsonl[2622] _id=69e8db6f1724f0c9e2fa74fd ts=2026-04-22T14:30:07.3880000Z -> 69cdc965d385e3b94310f78b.jsonl[2624] _id=69eb76cd1724f0c9e2fb76a9 ts=2026-04-24T13:57:31.9910000Z; 47h 2m: 69cdc965d385e3b94310f78b.jsonl[1799] _id=69de4fbe7957a33870f36a82 ts=2026-04-14T14:31:26.2740000Z -> 69cdc965d385e3b94310f78b.jsonl[1800] _id=69e0e5587957a33870f4fa41 ts=2026-04-16T13:34:15.3240000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 0m 
  - Evidence: 143h 0m: 69cdc965d385e3b94310f78b.jsonl[1936] _id=69e0eee07957a33870f537d1 ts=2026-04-16T14:14:55.4730000Z -> 69cdc965d385e3b94310f78b.jsonl[2350] _id=69e8c9f71724f0c9e2fa0abd ts=2026-04-22T13:15:35.1340000Z; 40m 5s: 69cdc965d385e3b94310f78b.jsonl[2351] _id=69e8ca101724f0c9e2fa0b26 ts=2026-04-22T13:15:59.7430000Z -> 69cdc965d385e3b94310f78b.jsonl[2492] _id=69e8d3761724f0c9e2fa448d ts=2026-04-22T13:56:05.6330000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 56m 
  - Evidence: 94h 56m: 69cdc965d385e3b94310f78b.jsonl[2044] _id=69e0f3847957a33870f5582b ts=2026-04-16T14:34:44.1720000Z -> 69cdc965d385e3b94310f78b.jsonl[619] _id=69e62a8c1724f0c9e2f85a35 ts=2026-04-20T13:30:51.4270000Z; 21m 30s: 69cdc965d385e3b94310f78b.jsonl[384] _id=69e0edbb7957a33870f53029 ts=2026-04-16T14:10:02.8000000Z -> 69cdc965d385e3b94310f78b.jsonl[1998] _id=69e0f2c57957a33870f550c9 ts=2026-04-16T14:31:33.0750000Z; 19m 42s: 69cdc965d385e3b94310f78b.jsonl[681] _id=69e631261724f0c9e2f881fb ts=2026-04-20T13:59:01.5470000Z -> 69cdc965d385e3b94310f78b.jsonl[810] _id=69e635c41724f0c9e2f89ded ts=2026-04-20T14:18:43.9170000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 69cdc965d385e3b94310f78b.jsonl[379] _id=69e0eda07957a33870f52f6f ts=2026-04-16T14:09:36.1810000Z -> 69cdc965d385e3b94310f78b.jsonl[2089] _id=69e62a431724f0c9e2f858ad ts=2026-04-20T13:29:38.0120000Z; 30m 33s: 69cdc965d385e3b94310f78b.jsonl[659] _id=69e62ffb1724f0c9e2f87be3 ts=2026-04-20T13:54:02.7910000Z -> 69cdc965d385e3b94310f78b.jsonl[2321] _id=69e637251724f0c9e2f8a7ff ts=2026-04-20T14:24:36.2040000Z; 13m 52s: 69cdc965d385e3b94310f78b.jsonl[2104] _id=69e62a9e1724f0c9e2f85aad ts=2026-04-20T13:31:09.3010000Z -> 69cdc965d385e3b94310f78b.jsonl[647] _id=69e62dde1724f0c9e2f87055 ts=2026-04-20T13:45:01.9580000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 42m 
  - Evidence: 143h 42m: 69cdc965d385e3b94310f78b.jsonl[1741] _id=69de4d217957a33870f3586f ts=2026-04-14T14:20:17.3890000Z -> 69cdc965d385e3b94310f78b.jsonl[703] _id=69e632181724f0c9e2f88810 ts=2026-04-20T14:03:03.0280000Z; 95h 48m: 69cdc965d385e3b94310f78b.jsonl[762] _id=69e634a21724f0c9e2f8962f ts=2026-04-20T14:13:53.6920000Z -> 69cdc965d385e3b94310f78b.jsonl[2665] _id=69eb78071724f0c9e2fb7cdb ts=2026-04-24T14:02:46.4100000Z; 25m 49s: 69cdc965d385e3b94310f78b.jsonl[2665] _id=69eb78071724f0c9e2fb7cdb ts=2026-04-24T14:02:46.4100000Z -> 69cdc965d385e3b94310f78b.jsonl[1545] _id=69eb7e151724f0c9e2fb9aef ts=2026-04-24T14:28:36.1230000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 43m 
  - Evidence: 143h 43m: 69cdc965d385e3b94310f78b.jsonl[100] _id=69de4d1e7957a33870f35863 ts=2026-04-14T14:20:14.3440000Z -> 69cdc965d385e3b94310f78b.jsonl[2216] _id=69e632311724f0c9e2f8889d ts=2026-04-20T14:03:28.9790000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 69cdc965d385e3b94310f78b.jsonl[2256] _id=69e633e31724f0c9e2f89281 ts=2026-04-20T14:10:42.5210000Z -> 69cdc965d385e3b94310f78b.jsonl[2660] _id=69eb77fd1724f0c9e2fb7ca3 ts=2026-04-24T14:02:36.1310000Z; 23m 5s: 69cdc965d385e3b94310f78b.jsonl[1356] _id=69eb78ad1724f0c9e2fb80e5 ts=2026-04-24T14:05:32.3020000Z -> 69cdc965d385e3b94310f78b.jsonl[1548] _id=69eb7e161724f0c9e2fb9aff ts=2026-04-24T14:28:37.9950000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 69cdc965d385e3b94310f78b.jsonl[2660] _id=69eb77fd1724f0c9e2fb7ca3 ts=2026-04-24T14:02:36.1310000Z -> 69cdc965d385e3b94310f78b.jsonl[2663] _id=69eb77fd1724f0c9e2fb7ca5 ts=2026-04-24T14:02:36.1350000Z; 5ms: 69cdc965d385e3b94310f78b.jsonl[1355] _id=69eb78ac1724f0c9e2fb80df ts=2026-04-24T14:05:31.5330000Z -> 69cdc965d385e3b94310f78b.jsonl[2676] _id=69eb78ac1724f0c9e2fb80e1 ts=2026-04-24T14:05:31.5380000Z; 7ms: 69cdc965d385e3b94310f78b.jsonl[1549] _id=69eb7e191724f0c9e2fb9b09 ts=2026-04-24T14:28:40.1350000Z -> 69cdc965d385e3b94310f78b.jsonl[1550] _id=69eb7e191724f0c9e2fb9b0d ts=2026-04-24T14:28:40.1420000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc965d385e3b94310f78b.jsonl[456] _id=69e0f15f7957a33870f544af ts=2026-04-16T14:25:34.8480000Z -> 69cdc965d385e3b94310f78b.jsonl[575] _id=69e627a11724f0c9e2f84b0b ts=2026-04-20T13:18:24.3400000Z; 47h 28m: 69cdc965d385e3b94310f78b.jsonl[1306] _id=69e8db151724f0c9e2fa7411 ts=2026-04-22T14:28:36.6000000Z -> 69cdc965d385e3b94310f78b.jsonl[2623] _id=69eb76ce1724f0c9e2fb76ab ts=2026-04-24T13:57:33.1810000Z; 47h 9m: 69cdc965d385e3b94310f78b.jsonl[140] _id=69de4e4c7957a33870f35fd0 ts=2026-04-14T14:25:16.5420000Z -> 69cdc965d385e3b94310f78b.jsonl[166] _id=69e0e55b7957a33870f4fa71 ts=2026-04-16T13:34:18.3130000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f78b.jsonl[1729] _id=69de4c487957a33870f3539d ts=2026-04-14T14:16:39.9190000Z -> 69cdc965d385e3b94310f78b.jsonl[1731] _id=69de4c487957a33870f353a1 ts=2026-04-14T14:16:39.9220000Z; 5ms: 69cdc965d385e3b94310f78b.jsonl[1571] _id=69eb7ea21724f0c9e2fb9d8f ts=2026-04-24T14:30:57.5630000Z -> 69cdc965d385e3b94310f78b.jsonl[2904] _id=69eb7ea21724f0c9e2fb9d95 ts=2026-04-24T14:30:57.5680000Z; 6ms: 69cdc965d385e3b94310f78b.jsonl[2552] _id=69e8d7191724f0c9e2fa5e93 ts=2026-04-22T14:11:37.2630000Z -> 69cdc965d385e3b94310f78b.jsonl[1198] _id=69e8d7191724f0c9e2fa5e95 ts=2026-04-22T14:11:37.2690000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc965d385e3b94310f78b.jsonl:69cdc965d385e3b94310f78b, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[1936] _id=69e0eee07957a33870f537d1 ts=2026-04-16T14:14:55.4730000Z`; `69cdc965d385e3b94310f78b.jsonl[2351] _id=69e8ca101724f0c9e2fa0b26 ts=2026-04-22T13:15:59.7430000Z`; `69cdc965d385e3b94310f78b.jsonl[1121] _id=69e8d3871724f0c9e2fa44cf ts=2026-04-22T13:56:23.3560000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 28 record(s) match the trigger in 69cdc965d385e3b94310f78b.jsonl:69cdc965d385e3b94310f78b, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[1906] _id=69e0ebb37957a33870f52499 ts=2026-04-16T14:01:22.6880000Z`; `69cdc965d385e3b94310f78b.jsonl[1907] _id=69e0ebbb7957a33870f524b1 ts=2026-04-16T14:01:30.7060000Z`; `69cdc965d385e3b94310f78b.jsonl[342] _id=69e0ec347957a33870f52699 ts=2026-04-16T14:03:32.1280000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[485] _id=69e0f1717957a33870f54557 ts=2026-04-16T14:25:53.4020000Z`; `69cdc965d385e3b94310f78b.jsonl[634] _id=69e62b701724f0c9e2f86113 ts=2026-04-20T13:34:39.8210000Z`; `69cdc965d385e3b94310f78b.jsonl[2141] _id=69e62c0e1724f0c9e2f86587 ts=2026-04-20T13:37:17.1630000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[762] _id=69e634a21724f0c9e2f8962f ts=2026-04-20T14:13:53.6920000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[2256] _id=69e633e31724f0c9e2f89281 ts=2026-04-20T14:10:42.5210000Z`; `69cdc965d385e3b94310f78b.jsonl[2660] _id=69eb77fd1724f0c9e2fb7ca3 ts=2026-04-24T14:02:36.1310000Z`; `69cdc965d385e3b94310f78b.jsonl[2663] _id=69eb77fd1724f0c9e2fb7ca5 ts=2026-04-24T14:02:36.1350000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[2353] _id=69e8ca131724f0c9e2fa0b39 ts=2026-04-22T13:16:03.0060000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[950] _id=69e8cda71724f0c9e2fa1ef9 ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[1541] _id=69eb7e181724f0c9e2fb9b05 ts=2026-04-24T14:28:39.1800000Z`; `69cdc965d385e3b94310f78b.jsonl[1551] _id=69eb7e191724f0c9e2fb9b11 ts=2026-04-24T14:28:40.6440000Z`; `69cdc965d385e3b94310f78b.jsonl[1553] _id=69eb7e1a1724f0c9e2fb9b1f ts=2026-04-24T14:28:41.9190000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 PlayerPositionEvent record in 'Unit 3 Dungeon Dev' inside a 'Unit 3 Dev' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `69cdc965d385e3b94310f78b.jsonl[1078] _id=69e8d0f11724f0c9e2fa37db ts=2026-04-22T13:45:20.6580000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 214 unmatched 'DialogueStartEvent' (totals: 426 start, 216 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 14 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 46 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.70s, min -14.85s, max +0.02s over 2941 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f78b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=complete 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 40 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2044 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (584); Unit 3 Dev (459); Unit 4 Dev (233); Unit 1 Dev (183); Unit 5 Dev (164); Unit 3 Dungeon Dev (161); Unit 4 Dev - Anderson Base (134); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (27)
- **eventKey:** present on 1402 of 2044 records
- **Intervals:** median 1.72s (p5 0.01s / p95 36.16s, n=2043)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1402; [conversationId, dialogueEventType] x642
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2044/2044 records)
    numeric range 8 .. 114 (48 unique)
data.dialogueEventType  (string, 2044/2044 records)
    "DialogueNodeEvent"  x1402
    "DialogueStartEvent"  x426
    "DialogueFinishEvent"  x216
data.nodeId  (number, 1402/2044 records)
    numeric range 0 .. 290 (212 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 550 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (148); Unit 3 Dev (136); Unit 1 Dev (64); Unit 3 Dungeon Dev (51); Unit 4 Dev (45); Unit 4 Dev - Dungeon (37); Unit 4 Dev - Anderson Base (30); Unit 5 Dev - Dungeon (24); Unit 5 Dev (15)
- **Intervals:** median 30.00s (p5 29.96s / p95 36.17s, n=536)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 550/550 records)
data.position.x  (number, 550/550 records)
    numeric range -661.022 .. 1601.95 (296 unique)
data.position.y  (number, 550/550 records)
    numeric range -111.241 .. 217.708 (244 unique)
data.position.z  (number, 550/550 records)
    numeric range -1120.99 .. 1977.73 (296 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 77 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (13); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 77 of 77 records
- **Intervals:** median 130.52s (p5 0.01s / p95 43922.86s, n=76)
- **`data` key-set variants:** [questEventType, questID, questName] x46; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 77/77 records)
    "questActiveEvent"  x46
    "questFinishEvent"  x31
data.questID  (string, 77/77 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 77/77 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/77 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 62 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (62)
- **Intervals:** median 1.91s (p5 0.23s / p95 32.26s, n=61)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "On"  x36
    "Off"  x26
data.floor  (string, 62/62 records)
    "4"  x38
    "1"  x12
    "2"  x6
    "3"  x6
data.machineNumber  (string, 62/62 records)
    "One"  x61
    "Two"  x1
data.machineType  (string, 62/62 records)
    "Condenser"  x33
    "Evaporator"  x26
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 62/62 records)
    "3"  x36
    "2"  x20
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 52 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (52)
- **Intervals:** median 1.60s (p5 0.24s / p95 45.68s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "ChangeCanister"  x52
data.canisterType  (string, 52/52 records)
    "Clay"  x26
    "Bedrock"  x21
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 52/52 records)
    "5"  x48
    "4"  x3
    "3"  x1
data.machine  (string, 52/52 records)
    "1"  x51
    "2"  x1
data.row  (string, 52/52 records)
    "BottomRow"  x32
    "TopRow"  x20
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (18)
- **Intervals:** median 38.32s (p5 2.05s / p95 1193.16s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 34 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (31); Unit 1 Dev (3)
- **Intervals:** median 9.02s (p5 1.18s / p95 118.01s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "argumentationNodeAdd"  x20
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 34/34 records)
    "Unit 3 - Pollution Upstream"  x31
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 34/34 records)
    "A"  x7
    "B"  x7
    "1"  x5
    "4"  x4
    "I"  x4
    "2"  x2
    "3"  x2
    "II"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 28 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (14)
- **Intervals:** median 3.40s (p5 0.31s / p95 1533.19s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "dragEnd"  x14
    "dragStart"  x14
data.featureUsed  (string, 28/28 records)
    "waypoint"  x28
data.location  (object, 28/28 records)
data.location.x  (number, 28/28 records)
    numeric range -770.79 .. 413.639 (15 unique)
data.location.y  (number, 28/28 records)
    numeric range -338.283 .. 174.744 (15 unique)
data.location.z  (number, 28/28 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 28 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (12); Unit 4 Dev - Anderson Base (8); Unit 5 Dev (8)
- **Intervals:** median 1.24s (p5 0.01s / p95 1018.13s, n=27)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "argumentationToolClose"  x14
    "argumentationToolOpen"  x14
data.argumentationTitle  (string, 28/28 records)
    "Unit 3 - Pollution Upstream"  x12
    "Unit 4 - Flooding"  x8
    "Unit 5"  x8
data.toolName  (string, 28/28 records)
    "BackingInfoPanel - Pollution Site Data"  x10
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Heat Added/Released Chart"  x5
    "BackingInfoPanel - Evaporation Flow Diagram"  x3
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 131.29s (p5 7.74s / p95 448392.47s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 42.28s (p5 19.10s / p95 412352.91s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 3.27s (p5 1.41s / p95 15.28s, n=5)
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

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 174338.42s (p5 18506.65s / p95 637597.55s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 1/1 records)
    "runtime_error"  x1
data.unitId  (string, 1/1 records)
    "unit3"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (21x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*