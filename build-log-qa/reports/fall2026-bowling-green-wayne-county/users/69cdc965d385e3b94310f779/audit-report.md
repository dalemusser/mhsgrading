# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f779

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f779
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f779.jsonl
- **Records:** 2797 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f779
- **Time span:** 2026-04-14T13:44:42.845000+00:00 .. 2026-04-22T14:10:52.601000+00:00 (192h 26m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f779\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2797 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 67 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 1959 | 70.04 | 1 | 9 | 1369 | 2026-04-14T13:45:00.800000+00:00 | 2026-04-22T14:10:20.732000+00:00 | 192h 25m |
| PlayerPositionEvent | 468 | 16.73 | 1 | 9 | 0 | 2026-04-14T13:44:42.845000+00:00 | 2026-04-22T14:10:51.661000+00:00 | 192h 26m |
| questEvent | 98 | 3.5 | 1 | 9 | 98 | 2026-04-14T13:45:00.787000+00:00 | 2026-04-22T14:10:52.601000+00:00 | 192h 25m |
| Topographic Map Event | 76 | 2.72 | 1 | 2 | 0 | 2026-04-14T14:04:40.012000+00:00 | 2026-04-20T14:08:15.034000+00:00 | 144h 3m |
| soilMachine | 48 | 1.72 | 1 | 1 | 0 | 2026-04-20T14:33:25.020000+00:00 | 2026-04-22T13:26:05.876000+00:00 | 46h 52m |
| TopographicMapEvent | 46 | 1.64 | 1 | 2 | 0 | 2026-04-14T14:19:51.410000+00:00 | 2026-04-20T14:08:13.598000+00:00 | 143h 48m |
| WaterChamberEvent | 29 | 1.04 | 1 | 1 | 0 | 2026-04-22T13:56:00.852000+00:00 | 2026-04-22T13:59:55.538000+00:00 | 3m 54s |
| argumentationNodeEvent | 20 | 0.72 | 1 | 2 | 0 | 2026-04-14T13:58:54.044000+00:00 | 2026-04-20T13:39:49.630000+00:00 | 143h 40m |
| Soil Key Puzzle | 15 | 0.54 | 1 | 3 | 0 | 2026-04-14T14:14:41.786000+00:00 | 2026-04-20T14:17:23.812000+00:00 | 144h 2m |
| argumentationEvent | 14 | 0.5 | 1 | 4 | 0 | 2026-04-14T13:58:49.134000+00:00 | 2026-04-22T14:04:04.837000+00:00 | 192h 5m |
| argumentationToolEvent | 10 | 0.36 | 1 | 1 | 0 | 2026-04-22T13:34:14.897000+00:00 | 2026-04-22T13:38:05.381000+00:00 | 3m 50s |
| TerasGardenBox | 8 | 0.29 | 1 | 1 | 0 | 2026-04-22T13:45:50.298000+00:00 | 2026-04-22T13:46:30.338000+00:00 | 40.0s |
| EndOfUnit | 5 | 0.18 | 1 | 4 | 0 | 2026-04-14T14:03:36.052000+00:00 | 2026-04-22T14:09:33.263000+00:00 | 192h 5m |
| crash | 1 | 0.04 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.09s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172422.709s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.005s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 379.332s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.938s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 7.506s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.718s median 
  - Expected: 0.467s in 09-23-26 
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
  - Observed: 4.109s median 
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
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 76 records this build 
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
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 20 records 
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
  - Observed: 2; 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 9.6x vs baseline. 
  - Observed: 48 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 78 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f779.jsonl[72] _id=69de48847957a33870f3373f ts=2026-04-14T14:00:35.4370000Z`; `69cdc965d385e3b94310f779.jsonl[123] _id=69de4d9f7957a33870f35bcd ts=2026-04-14T14:22:22.7870000Z`; `69cdc965d385e3b94310f779.jsonl[223] _id=69e0ed487957a33870f52ccd ts=2026-04-16T14:08:07.5340000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 76 records, TopographicMapEvent: 46 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 4 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1958 | 0.0 | 1.09 | 353.79 | 30.037 | 340914.692 | 0.17 | 486 | 3 |
| PlayerPositionEvent | 454 | 25.813 | 30.005 | 1524.885 | 39.735 | 340913.64 | 0.04 | 0 | 3 |
| questEvent | 97 | 0.002 | 89.869 | 7141.771 | 605.063 | 341142.048 | 0.01 | 19 | 5 |
| Topographic Map Event | 75 | 1.511 | 11.571 | 6914.867 | 600.313 | 341726.238 | 0.01 | 0 | 4 |
| soilMachine | 47 | 0.513 | 4.109 | 3590.657 | 68.411 | 168052.831 | 0.02 | 0 | 1 |
| TopographicMapEvent | 45 | 0.13 | 5.938 | 11504.493 | 2261.702 | 341693.048 | 0.01 | 0 | 4 |
| WaterChamberEvent | 28 | 0.173 | 7.506 | 8.382 | 21.747 | 27.584 | 7.16 | 0 | 0 |
| argumentationNodeEvent | 19 | 0.947 | 4.718 | 27223.978 | 190386.024 | 343765.344 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 14 | 3.052 | 379.332 | 37040.145 | 230371.341 | 341272.381 | 0.0 | 0 | 6 |
| argumentationEvent | 13 | 0.119 | 50.73 | 53193.516 | 241490.507 | 343753.987 | 0.0 | 0 | 4 |
| argumentationToolEvent | 9 | 0.002 | 13.078 | 25.609 | 79.38 | 90.89 | 2.34 | 1 | 0 |
| TerasGardenBox | 7 | 1.029 | 6.19 | 5.72 | 11.486 | 12.505 | 10.49 | 0 | 0 |
| EndOfUnit | 4 | 1187.784 | 172422.709 | 172889.303 | 319693.725 | 345524.008 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.97s, p95 39.73s, n=454) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `794ms: 69cdc965d385e3b94310f779.jsonl[816] _id=69e8d3881724f0c9e2fa44d7 ts=2026-04-22T13:56:23.8520000Z ~ 69cdc965d385e3b94310f779.jsonl[818] _id=69e8d3891724f0c9e2fa44e3 ts=2026-04-22T13:56:24.6460000Z`; `283ms: 69cdc965d385e3b94310f779.jsonl[2640] _id=69e8d4441724f0c9e2fa4937 ts=2026-04-22T13:59:31.7570000Z ~ 69cdc965d385e3b94310f779.jsonl[2639] _id=69e8d4451724f0c9e2fa4941 ts=2026-04-22T13:59:32.0400000Z`; `173ms: 69cdc965d385e3b94310f779.jsonl[831] _id=69e8d4451724f0c9e2fa4943 ts=2026-04-22T13:59:32.3090000Z ~ 69cdc965d385e3b94310f779.jsonl[2641] _id=69e8d4451724f0c9e2fa4949 ts=2026-04-22T13:59:32.4820000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `119ms: 69cdc965d385e3b94310f779.jsonl[1946] _id=69e62ca81724f0c9e2f86ab9 ts=2026-04-20T13:39:52.5780000Z ~ 69cdc965d385e3b94310f779.jsonl[411] _id=69e62ca91724f0c9e2f86ac3 ts=2026-04-20T13:39:52.6970000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc965d385e3b94310f779.jsonl[700] _id=69e8ce571724f0c9e2fa247b ts=2026-04-22T13:34:14.8970000Z ~ 69cdc965d385e3b94310f779.jsonl[701] _id=69e8ce581724f0c9e2fa247f ts=2026-04-22T13:34:14.8990000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 69cdc965d385e3b94310f779.jsonl[2692] _id=69e8d5631724f0c9e2fa510d ts=2026-04-22T14:04:18.8590000Z ~ 69cdc965d385e3b94310f779.jsonl[2693] _id=69e8d5641724f0c9e2fa5111 ts=2026-04-22T14:04:18.8670000Z`; `12ms: 69cdc965d385e3b94310f779.jsonl[2740] _id=69e8d65c1724f0c9e2fa580d ts=2026-04-22T14:08:27.8460000Z ~ 69cdc965d385e3b94310f779.jsonl[2743] _id=69e8d65d1724f0c9e2fa5811 ts=2026-04-22T14:08:27.8580000Z`; `2ms: 69cdc965d385e3b94310f779.jsonl[2770] _id=69e8d6a91724f0c9e2fa5abd ts=2026-04-22T14:09:43.9190000Z ~ 69cdc965d385e3b94310f779.jsonl[896] _id=69e8d6a91724f0c9e2fa5ac3 ts=2026-04-22T14:09:43.9210000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `884ms: 69cdc965d385e3b94310f779.jsonl[2234] _id=69e639371724f0c9e2f8b115 ts=2026-04-20T14:33:27.6250000Z ~ 69cdc965d385e3b94310f779.jsonl[2235] _id=69e639381724f0c9e2f8b11f ts=2026-04-20T14:33:28.5090000Z`; `869ms: 69cdc965d385e3b94310f779.jsonl[2302] _id=69e8caf01724f0c9e2fa0f47 ts=2026-04-22T13:19:43.7780000Z ~ 69cdc965d385e3b94310f779.jsonl[641] _id=69e8caf11724f0c9e2fa0f4d ts=2026-04-22T13:19:44.6470000Z`; `513ms: 69cdc965d385e3b94310f779.jsonl[641] _id=69e8caf11724f0c9e2fa0f4d ts=2026-04-22T13:19:44.6470000Z ~ 69cdc965d385e3b94310f779.jsonl[640] _id=69e8caf21724f0c9e2fa0f4f ts=2026-04-22T13:19:45.1600000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 41m 
  - Evidence: 94h 41m: 69cdc965d385e3b94310f779.jsonl[1793] _id=69e0f3ab7957a33870f558e3 ts=2026-04-16T14:35:22.4010000Z -> 69cdc965d385e3b94310f779.jsonl[1795] _id=69e6275e1724f0c9e2f84a69 ts=2026-04-20T13:17:17.0930000Z; 47h 5m: 69cdc965d385e3b94310f779.jsonl[1299] _id=69de4f307957a33870f36550 ts=2026-04-14T14:29:03.5870000Z -> 69cdc965d385e3b94310f779.jsonl[1308] _id=69e0e5577957a33870f4fa29 ts=2026-04-16T13:34:13.3390000Z; 46h 38m: 69cdc965d385e3b94310f779.jsonl[614] _id=69e639751724f0c9e2f8b481 ts=2026-04-20T14:34:28.9630000Z -> 69cdc965d385e3b94310f779.jsonl[2253] _id=69e8c9611724f0c9e2fa0979 ts=2026-04-22T13:13:04.2640000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 486 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f779.jsonl[2056] _id=69e633f61724f0c9e2f892ff ts=2026-04-20T14:11:02.2200000Z -> 69cdc965d385e3b94310f779.jsonl[2142] _id=69e634111724f0c9e2f8935d ts=2026-04-20T14:11:02.22Z; 0ms: 69cdc965d385e3b94310f779.jsonl[2588] _id=69e8d1fa1724f0c9e2fa3ef7 ts=2026-04-22T13:49:45.4940000Z -> 69cdc965d385e3b94310f779.jsonl[2591] _id=69e8d2081724f0c9e2fa3f2d ts=2026-04-22T13:49:45.494Z; 2ms: 69cdc965d385e3b94310f779.jsonl[2422] _id=69e8cec21724f0c9e2fa270f ts=2026-04-22T13:36:01.6770000Z -> 69cdc965d385e3b94310f779.jsonl[2419] _id=69e8cec21724f0c9e2fa2711 ts=2026-04-22T13:36:01.6790000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 58m 
  - Evidence: 95h 58m: 69cdc965d385e3b94310f779.jsonl[1589] _id=69e0ee437957a33870f533c3 ts=2026-04-16T14:12:18.1720000Z -> 69cdc965d385e3b94310f779.jsonl[2055] _id=69e633f61724f0c9e2f892fc ts=2026-04-20T14:11:02.1800000Z; 48h 8m: 69cdc965d385e3b94310f779.jsonl[1096] _id=69de49397957a33870f33c45 ts=2026-04-14T14:03:36.0520000Z -> 69cdc965d385e3b94310f779.jsonl[1589] _id=69e0ee437957a33870f533c3 ts=2026-04-16T14:12:18.1720000Z; 47h 38m: 69cdc965d385e3b94310f779.jsonl[2055] _id=69e633f61724f0c9e2f892fc ts=2026-04-20T14:11:02.1800000Z -> 69cdc965d385e3b94310f779.jsonl[2577] _id=69e8d1fa1724f0c9e2fa3ef5 ts=2026-04-22T13:49:45.4790000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 41m 
  - Evidence: 94h 41m: 69cdc965d385e3b94310f779.jsonl[1791] _id=69e0f3aa7957a33870f558dd ts=2026-04-16T14:35:21.2450000Z -> 69cdc965d385e3b94310f779.jsonl[1794] _id=69e6275b1724f0c9e2f84a67 ts=2026-04-20T13:17:14.8850000Z; 47h 2m: 69cdc965d385e3b94310f779.jsonl[1306] _id=69de4fb47957a33870f36a48 ts=2026-04-14T14:31:15.6250000Z -> 69cdc965d385e3b94310f779.jsonl[1307] _id=69e0e5547957a33870f4fa11 ts=2026-04-16T13:34:11.1310000Z; 46h 37m: 69cdc965d385e3b94310f779.jsonl[2251] _id=69e639be1724f0c9e2f8b5a5 ts=2026-04-20T14:35:42.5400000Z -> 69cdc965d385e3b94310f779.jsonl[2252] _id=69e8c95f1724f0c9e2fa0975 ts=2026-04-22T13:13:01.7380000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 47m 
  - Evidence: 94h 47m: 69cdc965d385e3b94310f779.jsonl[1760] _id=69e0f2e07957a33870f55203 ts=2026-04-16T14:31:59.1920000Z -> 69cdc965d385e3b94310f779.jsonl[342] _id=69e627f81724f0c9e2f84cdf ts=2026-04-20T13:19:51.5730000Z; 47h 24m: 69cdc965d385e3b94310f779.jsonl[1168] _id=69de4bd57957a33870f34f0f ts=2026-04-14T14:14:44.8460000Z -> 69cdc965d385e3b94310f779.jsonl[159] _id=69e0e6757957a33870f502f5 ts=2026-04-16T13:39:00.2420000Z; 33m 14s: 69cdc965d385e3b94310f779.jsonl[1976] _id=69e62d781724f0c9e2f86edd ts=2026-04-20T13:43:20.3330000Z -> 69cdc965d385e3b94310f779.jsonl[2158] _id=69e635421724f0c9e2f89a59 ts=2026-04-20T14:16:34.5740000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 55m 
  - Evidence: 94h 55m: 69cdc965d385e3b94310f779.jsonl[1737] _id=69e0f2747957a33870f54dbd ts=2026-04-16T14:30:11.8510000Z -> 69cdc965d385e3b94310f779.jsonl[1848] _id=69e629521724f0c9e2f852fb ts=2026-04-20T13:25:38.0890000Z; 47h 3m: 69cdc965d385e3b94310f779.jsonl[1305] _id=69de4f9f7957a33870f369b2 ts=2026-04-14T14:30:54.5100000Z -> 69cdc965d385e3b94310f779.jsonl[145] _id=69e0e5657957a33870f4fafd ts=2026-04-16T13:34:28.8140000Z; 40m 9s: 69cdc965d385e3b94310f779.jsonl[1858] _id=69e629bb1724f0c9e2f855ab ts=2026-04-20T13:27:23.3200000Z -> 69cdc965d385e3b94310f779.jsonl[2092] _id=69e633251724f0c9e2f88e37 ts=2026-04-20T14:07:32.9360000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 54m 
  - Evidence: 94h 54m: 69cdc965d385e3b94310f779.jsonl[1735] _id=69e0f24d7957a33870f54cb7 ts=2026-04-16T14:29:32.3680000Z -> 69cdc965d385e3b94310f779.jsonl[1838] _id=69e629091724f0c9e2f851cb ts=2026-04-20T13:24:25.4160000Z; 47h 10m: 69cdc965d385e3b94310f779.jsonl[134] _id=69de4e277957a33870f35f1a ts=2026-04-14T14:24:38.1210000Z -> 69cdc965d385e3b94310f779.jsonl[1311] _id=69e0e5757957a33870f4fc0f ts=2026-04-16T13:34:44.2100000Z; 39m 29s: 69cdc965d385e3b94310f779.jsonl[360] _id=69e629ba1724f0c9e2f8559d ts=2026-04-20T13:27:21.8980000Z -> 69cdc965d385e3b94310f779.jsonl[2088] _id=69e632fb1724f0c9e2f88d53 ts=2026-04-20T14:06:51.0560000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 69cdc965d385e3b94310f779.jsonl[1557] _id=69e0edab7957a33870f52fbb ts=2026-04-16T14:09:46.9510000Z -> 69cdc965d385e3b94310f779.jsonl[1930] _id=69e62c751724f0c9e2f86901 ts=2026-04-20T13:39:00.9380000Z; 48h 8m: 69cdc965d385e3b94310f779.jsonl[71] _id=69de48847957a33870f3373d ts=2026-04-14T14:00:35.4210000Z -> 69cdc965d385e3b94310f779.jsonl[231] _id=69e0ed877957a33870f52eaf ts=2026-04-16T14:09:10.2740000Z; 47h 54m: 69cdc965d385e3b94310f779.jsonl[411] _id=69e62ca91724f0c9e2f86ac3 ts=2026-04-20T13:39:52.6970000Z -> 69cdc965d385e3b94310f779.jsonl[698] _id=69e8ce5e1724f0c9e2fa24ab ts=2026-04-22T13:34:21.0890000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 69cdc965d385e3b94310f779.jsonl[1555] _id=69e0edaa7957a33870f52fb5 ts=2026-04-16T14:09:45.8710000Z -> 69cdc965d385e3b94310f779.jsonl[1938] _id=69e62c7f1724f0c9e2f8697d ts=2026-04-20T13:39:11.2150000Z; 48h 9m: 69cdc965d385e3b94310f779.jsonl[1052] _id=69de487e7957a33870f3372b ts=2026-04-14T14:00:29.6540000Z -> 69cdc965d385e3b94310f779.jsonl[1549] _id=69e0ed9e7957a33870f52f61 ts=2026-04-16T14:09:33.5310000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f779.jsonl[700] _id=69e8ce571724f0c9e2fa247b ts=2026-04-22T13:34:14.8970000Z -> 69cdc965d385e3b94310f779.jsonl[701] _id=69e8ce581724f0c9e2fa247f ts=2026-04-22T13:34:14.8990000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc965d385e3b94310f779.jsonl[1763] _id=69e0f2c87957a33870f55105 ts=2026-04-16T14:31:35.7190000Z -> 69cdc965d385e3b94310f779.jsonl[1797] _id=69e6275f1724f0c9e2f84a6d ts=2026-04-20T13:17:17.7670000Z; 47h 14m: 69cdc965d385e3b94310f779.jsonl[108] _id=69de4cf97957a33870f357a3 ts=2026-04-14T14:19:36.4990000Z -> 69cdc965d385e3b94310f779.jsonl[147] _id=69e0e5577957a33870f4fa33 ts=2026-04-16T13:34:13.9260000Z; 46h 38m: 69cdc965d385e3b94310f779.jsonl[610] _id=69e6396d1724f0c9e2f8b405 ts=2026-04-20T14:34:20.9860000Z -> 69cdc965d385e3b94310f779.jsonl[2255] _id=69e8c9611724f0c9e2fa0977 ts=2026-04-22T13:13:04.0500000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f779.jsonl[1020] _id=69de47fd7957a33870f33405 ts=2026-04-14T13:58:19.8950000Z -> 69cdc965d385e3b94310f779.jsonl[1016] _id=69de47fd7957a33870f33407 ts=2026-04-14T13:58:19.8970000Z; 2ms: 69cdc965d385e3b94310f779.jsonl[2770] _id=69e8d6a91724f0c9e2fa5abd ts=2026-04-22T14:09:43.9190000Z -> 69cdc965d385e3b94310f779.jsonl[896] _id=69e8d6a91724f0c9e2fa5ac3 ts=2026-04-22T14:09:43.9210000Z; 3ms: 69cdc965d385e3b94310f779.jsonl[1537] _id=69e0ed7c7957a33870f52e57 ts=2026-04-16T14:08:58.8470000Z -> 69cdc965d385e3b94310f779.jsonl[1538] _id=69e0ed7c7957a33870f52e59 ts=2026-04-16T14:08:58.8500000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 46h 40m 
  - Evidence: 46h 40m: 69cdc965d385e3b94310f779.jsonl[616] _id=69e639831724f0c9e2f8b4bf ts=2026-04-20T14:34:43.5900000Z -> 69cdc965d385e3b94310f779.jsonl[2273] _id=69e8c9f91724f0c9e2fa0ac7 ts=2026-04-22T13:15:36.4210000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc965d385e3b94310f779.jsonl:69cdc965d385e3b94310f779, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f779.jsonl[1168] _id=69de4bd57957a33870f34f0f ts=2026-04-14T14:14:44.8460000Z`; `69cdc965d385e3b94310f779.jsonl[1661] _id=69e0f1377957a33870f543aa ts=2026-04-16T14:24:54.7540000Z`; `69cdc965d385e3b94310f779.jsonl[1760] _id=69e0f2e07957a33870f55203 ts=2026-04-16T14:31:59.1920000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 46 record(s) match the trigger in 69cdc965d385e3b94310f779.jsonl:69cdc965d385e3b94310f779, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f779.jsonl[1231] _id=69de4d087957a33870f357dd ts=2026-04-14T14:19:51.4100000Z`; `69cdc965d385e3b94310f779.jsonl[1232] _id=69de4d087957a33870f357df ts=2026-04-14T14:19:51.6610000Z`; `69cdc965d385e3b94310f779.jsonl[1234] _id=69de4d107957a33870f3580f ts=2026-04-14T14:19:59.1920000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f779.jsonl[364] _id=69e62a0c1724f0c9e2f85782 ts=2026-04-20T13:28:44.1130000Z`; `69cdc965d385e3b94310f779.jsonl[379] _id=69e62a661724f0c9e2f85997 ts=2026-04-20T13:30:13.8910000Z`; `69cdc965d385e3b94310f779.jsonl[663] _id=69e8cd001724f0c9e2fa1b00 ts=2026-04-22T13:28:31.7960000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f779.jsonl[411] _id=69e62ca91724f0c9e2f86ac3 ts=2026-04-20T13:39:52.6970000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f779.jsonl[700] _id=69e8ce571724f0c9e2fa247b ts=2026-04-22T13:34:14.8970000Z`; `69cdc965d385e3b94310f779.jsonl[701] _id=69e8ce581724f0c9e2fa247f ts=2026-04-22T13:34:14.8990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f779.jsonl[617] _id=69e8c9aa1724f0c9e2fa09b1 ts=2026-04-22T13:14:17.3840000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc965d385e3b94310f779.jsonl[2793] _id=69e8d6d41724f0c9e2fa5c29 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f779.jsonl[170] _id=69e0e9157957a33870f5147b ts=2026-04-16T13:50:12.5720000Z`; `69cdc965d385e3b94310f779.jsonl[1414] _id=69e0ea767957a33870f51e3d ts=2026-04-16T13:56:05.4030000Z`; `69cdc965d385e3b94310f779.jsonl[1439] _id=69e0eb1c7957a33870f52155 ts=2026-04-16T13:58:51.0970000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 179 unmatched 'DialogueStartEvent' (totals: 383 start, 207 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'Started' (totals: 10 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 25 unmatched 'questActiveEvent' (totals: 61 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.94s, min -27.74s, max -0.18s over 2796 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f779\coverage.yaml

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
  - Observed: 76 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1959 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (477); Unit 1 Dev (376); Unit 3 Dev (289); Unit 4 Dev (223); Unit 5 Dev (195); Unit 4 Dev - Dungeon (134); Unit 4 Dev - Anderson Base (133); Unit 3 Dungeon Dev (106); Unit 5 Dev - Dungeon (26)
- **eventKey:** present on 1369 of 1959 records
- **Intervals:** median 1.09s (p5 0.01s / p95 30.04s, n=1958)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1369; [conversationId, dialogueEventType] x590
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1959/1959 records)
    numeric range 10 .. 114 (46 unique)
data.dialogueEventType  (string, 1959/1959 records)
    "DialogueNodeEvent"  x1369
    "DialogueStartEvent"  x383
    "DialogueFinishEvent"  x207
data.nodeId  (number, 1369/1959 records)
    numeric range 0 .. 289 (207 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 468 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (153); Unit 1 Dev (60); Unit 4 Dev - Dungeon (56); Unit 3 Dev (52); Unit 4 Dev (45); Unit 3 Dungeon Dev (44); Unit 5 Dev (21); Unit 5 Dev - Dungeon (20); Unit 4 Dev - Anderson Base (17)
- **Intervals:** median 30.00s (p5 29.97s / p95 39.73s, n=454)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 468/468 records)
data.position.x  (number, 468/468 records)
    numeric range -657.564 .. 1943 (329 unique)
data.position.y  (number, 468/468 records)
    numeric range -114.26 .. 222.784 (269 unique)
data.position.z  (number, 468/468 records)
    numeric range -1110.59 .. 1947.8 (330 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 98 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 2 Prod (Refactor) (21); Unit 4 Dev - Dungeon (13); Unit 5 Dev (11); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 98 of 98 records
- **Intervals:** median 89.87s (p5 0.01s / p95 605.06s, n=97)
- **`data` key-set variants:** [questEventType, questID, questName] x61; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 98/98 records)
    "questActiveEvent"  x61
    "questFinishEvent"  x37
data.questID  (string, 98/98 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 98/98 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/98 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 76 records

- **Scenes:** Unit 2 Prod (Refactor) (68); Unit 3 Dev (8)
- **Intervals:** median 11.57s (p5 2.17s / p95 600.31s, n=75)
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapCloseEvent"  x38
    "MapOpenEvent"  x38
data.featureUsed  (string, 76/76 records)
    "Map"  x76
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 48 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (48)
- **Intervals:** median 4.11s (p5 0.67s / p95 68.41s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "ChangeCanister"  x48
data.canisterType  (string, 48/48 records)
    "Clay"  x20
    "Bedrock"  x15
    "Sand"  x9
    "Gravel"  x4
data.floor  (string, 48/48 records)
    "5"  x31
    "4"  x9
    "3"  x8
data.machine  (string, 48/48 records)
    "1"  x46
    "2"  x2
data.row  (string, 48/48 records)
    "BottomRow"  x24
    "TopRow"  x24
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TopographicMapEvent` — 46 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 3 Dev (10)
- **Intervals:** median 5.94s (p5 0.33s / p95 2261.70s, n=45)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "dragEnd"  x23
    "dragStart"  x23
data.featureUsed  (string, 46/46 records)
    "waypoint"  x46
data.location  (object, 46/46 records)
data.location.x  (number, 46/46 records)
    numeric range -812.572 .. 302.826 (24 unique)
data.location.y  (number, 46/46 records)
    numeric range -307.4 .. 292.081 (24 unique)
data.location.z  (number, 46/46 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 29 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (29)
- **Intervals:** median 7.51s (p5 0.27s / p95 21.75s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "On"  x19
    "Off"  x10
data.floor  (string, 29/29 records)
    "4"  x14
    "3"  x6
    "1"  x5
    "2"  x4
data.machineNumber  (string, 29/29 records)
    "One"  x28
    "Two"  x1
data.machineType  (string, 29/29 records)
    "Condenser"  x19
    "Evaporator"  x7
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 29/29 records)
    "3"  x13
    "2"  x10
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 20 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (17); Unit 3 Dev (3)
- **Intervals:** median 4.72s (p5 0.99s / p95 190386.02s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationNodeAdd"  x16
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 20/20 records)
    "Unit 1 - Freshwater"  x14
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 20/20 records)
    "II"  x6
    "A"  x4
    "I"  x4
    "1"  x3
    "B"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 15 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 379.33s (p5 3.06s / p95 230371.34s, n=14)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 15/15 records)
    "Started"  x10
    "Finished"  x5
data.Unit  (string, 15/15 records)
    "Unit 2 Prod (Refactor)"  x11
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 50.73s (p5 2.88s / p95 241490.51s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 14/14 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (10)
- **Intervals:** median 13.08s (p5 0.33s / p95 79.38s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 10/10 records)
    "Unit 4 - Flooding"  x10
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x6
    "BackingInfoPanel - Soil Flow Rates"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 6.19s (p5 1.10s / p95 11.49s, n=7)
- **`data` key-set variants:** [actionType, boxID, soilType] x4; [actionType, boxId, soilType] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "cameraPlaced"  x4
    "soilSelected"  x4
data.boxID  (string, 4/8 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.boxId  (string, 4/8 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 8/8 records)
    "Gravel"  x3
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 172422.71s (p5 26738.11s / p95 319693.72s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x2
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
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit5:831:9)"  x1
data.type  (string, 1/1 records)
    "runtime_error"  x1
data.unitId  (string, 1/1 records)
    "unit5"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (11 records)
- `TopographicMapEvent` data.actionType: "dragStart" (23x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (15x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*