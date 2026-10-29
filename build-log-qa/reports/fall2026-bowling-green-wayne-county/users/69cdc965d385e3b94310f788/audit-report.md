# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f788

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f788
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f788.jsonl
- **Records:** 2774 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f788
- **Time span:** 2026-04-14T13:45:01.328000+00:00 .. 2026-04-24T14:17:34.328000+00:00 (240h 32m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f788\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2774 records, 9 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 62 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 1912 | 68.93 | 1 | 9 | 1344 | 2026-04-14T13:45:19.672000+00:00 | 2026-04-24T14:17:26.024000+00:00 | 240h 32m |
| PlayerPositionEvent | 498 | 17.95 | 1 | 9 | 0 | 2026-04-14T13:45:01.328000+00:00 | 2026-04-24T14:17:05.395000+00:00 | 240h 32m |
| questEvent | 84 | 3.03 | 1 | 9 | 84 | 2026-04-14T13:45:19.659000+00:00 | 2026-04-24T14:16:35.013000+00:00 | 240h 31m |
| WaterChamberEvent | 69 | 2.49 | 1 | 1 | 0 | 2026-04-22T14:16:15.708000+00:00 | 2026-04-22T14:24:51.827000+00:00 | 8m 36s |
| TopographicMapEvent | 48 | 1.73 | 1 | 2 | 0 | 2026-04-14T14:29:46.363000+00:00 | 2026-04-20T14:04:43.942000+00:00 | 143h 34m |
| Topographic Map Event | 46 | 1.66 | 1 | 2 | 0 | 2026-04-14T14:29:25.010000+00:00 | 2026-04-20T14:04:47.015000+00:00 | 143h 35m |
| argumentationNodeEvent | 34 | 1.23 | 1 | 3 | 0 | 2026-04-14T14:04:25.747000+00:00 | 2026-04-20T13:39:01.171000+00:00 | 143h 34m |
| argumentationToolEvent | 28 | 1.01 | 1 | 3 | 0 | 2026-04-16T14:22:37.859000+00:00 | 2026-04-22T14:02:08.903000+00:00 | 143h 39m |
| soilMachine | 18 | 0.65 | 1 | 1 | 0 | 2026-04-22T13:39:52.530000+00:00 | 2026-04-22T13:44:33.887000+00:00 | 4m 41s |
| argumentationEvent | 13 | 0.47 | 1 | 5 | 0 | 2026-04-14T14:04:20.850000+00:00 | 2026-04-24T14:02:11.262000+00:00 | 239h 57m |
| Soil Key Puzzle | 10 | 0.36 | 1 | 3 | 0 | 2026-04-14T14:22:57.009000+00:00 | 2026-04-20T14:20:43.475000+00:00 | 143h 57m |
| TerasGardenBox | 8 | 0.29 | 1 | 1 | 0 | 2026-04-22T14:05:59.376000+00:00 | 2026-04-22T14:07:02.132000+00:00 | 1m 2s |
| EndOfUnit | 6 | 0.22 | 1 | 5 | 0 | 2026-04-14T14:09:36.709000+00:00 | 2026-04-24T14:17:34.328000+00:00 | 240h 7m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172966.049s median 
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
  - Observed: 55.317s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.327s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 184.887s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.597s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 5.359s median 
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
  - Observed: 0.582s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 10 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 46 records this build 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 69 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 28 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f788.jsonl[108] _id=69de49e77957a33870f34153 ts=2026-04-14T14:06:31.4850000Z`; `69cdc965d385e3b94310f788.jsonl[1259] _id=69e0e88c7957a33870f51121 ts=2026-04-16T13:47:56.1630000Z`; `69cdc965d385e3b94310f788.jsonl[1543] _id=69e0f1877957a33870f54603 ts=2026-04-16T14:26:14.8340000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 46 records, TopographicMapEvent: 48 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 4 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1911 | 0.0 | 2.389 | 453.127 | 31.532 | 341014.088 | 0.13 | 482 | 4 |
| PlayerPositionEvent | 486 | 26.438 | 30.005 | 1780.239 | 37.693 | 340968.63 | 0.03 | 0 | 4 |
| questEvent | 83 | 0.002 | 133.422 | 10432.233 | 1205.884 | 341186.581 | 0.01 | 15 | 10 |
| WaterChamberEvent | 68 | 0.124 | 4.327 | 7.59 | 28.943 | 37.95 | 7.91 | 0 | 0 |
| TopographicMapEvent | 47 | 0.047 | 2.067 | 10997.821 | 1660.117 | 341571.379 | 0.01 | 1 | 5 |
| Topographic Map Event | 45 | 0.495 | 18.602 | 11487.156 | 1575.943 | 341551.403 | 0.01 | 0 | 5 |
| argumentationNodeEvent | 33 | 1.367 | 5.597 | 15662.892 | 69556.45 | 342662.806 | 0.0 | 0 | 2 |
| argumentationToolEvent | 27 | 0.005 | 5.359 | 19154.483 | 121783.435 | 342871.018 | 0.0 | 1 | 2 |
| soilMachine | 17 | 0.199 | 0.582 | 16.55 | 69.857 | 228.06 | 3.63 | 0 | 0 |
| argumentationEvent | 12 | 0.063 | 184.887 | 71989.201 | 249845.76 | 342638.508 | 0.0 | 0 | 5 |
| Soil Key Puzzle | 9 | 2.795 | 55.317 | 57585.163 | 274983.533 | 344796.059 | 0.0 | 0 | 4 |
| TerasGardenBox | 7 | 1.103 | 5.332 | 8.965 | 22.354 | 25.073 | 6.69 | 0 | 0 |
| EndOfUnit | 5 | 349.698 | 172966.049 | 172895.524 | 310310.281 | 344402.123 | 0.0 | 0 | 4 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.97s, p95 37.69s, n=486) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `935ms: 69cdc965d385e3b94310f788.jsonl[2530] _id=69e8d99c1724f0c9e2fa6b93 ts=2026-04-22T14:22:19.2620000Z ~ 69cdc965d385e3b94310f788.jsonl[787] _id=69e8d99d1724f0c9e2fa6b97 ts=2026-04-22T14:22:20.1970000Z`; `133ms: 69cdc965d385e3b94310f788.jsonl[787] _id=69e8d99d1724f0c9e2fa6b97 ts=2026-04-22T14:22:20.1970000Z ~ 69cdc965d385e3b94310f788.jsonl[2515] _id=69e8d99d1724f0c9e2fa6b9b ts=2026-04-22T14:22:20.3300000Z`; `709ms: 69cdc965d385e3b94310f788.jsonl[2514] _id=69e8d99c1724f0c9e2fa6b95 ts=2026-04-22T14:22:19.8280000Z ~ 69cdc965d385e3b94310f788.jsonl[788] _id=69e8d99d1724f0c9e2fa6b9f ts=2026-04-22T14:22:20.5370000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `63ms: 69cdc965d385e3b94310f788.jsonl[1813] _id=69e62c821724f0c9e2f869a7 ts=2026-04-20T13:39:14.5260000Z ~ 69cdc965d385e3b94310f788.jsonl[1810] _id=69e62c821724f0c9e2f869af ts=2026-04-20T13:39:14.5890000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `862ms: 69cdc965d385e3b94310f788.jsonl[1501] _id=69e0f0b67957a33870f5409b ts=2026-04-16T14:22:46.3040000Z ~ 69cdc965d385e3b94310f788.jsonl[1522] _id=69e0f0b77957a33870f540a3 ts=2026-04-16T14:22:47.1660000Z`; `916ms: 69cdc965d385e3b94310f788.jsonl[1519] _id=69e0f0b67957a33870f5409f ts=2026-04-16T14:22:46.3760000Z ~ 69cdc965d385e3b94310f788.jsonl[1520] _id=69e0f0b77957a33870f540a5 ts=2026-04-16T14:22:47.2920000Z`; `5ms: 69cdc965d385e3b94310f788.jsonl[2338] _id=69e8d3e41724f0c9e2fa46e7 ts=2026-04-22T13:57:55.7450000Z ~ 69cdc965d385e3b94310f788.jsonl[2339] _id=69e8d3e51724f0c9e2fa46e9 ts=2026-04-22T13:57:55.7500000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 69cdc965d385e3b94310f788.jsonl[834] _id=69eb77f91724f0c9e2fb7c83 ts=2026-04-24T14:02:32.2920000Z ~ 69cdc965d385e3b94310f788.jsonl[839] _id=69eb77f91724f0c9e2fb7c85 ts=2026-04-24T14:02:32.2960000Z`; `6ms: 69cdc965d385e3b94310f788.jsonl[2649] _id=69eb79341724f0c9e2fb82db ts=2026-04-24T14:07:47.2970000Z ~ 69cdc965d385e3b94310f788.jsonl[2650] _id=69eb79341724f0c9e2fb82df ts=2026-04-24T14:07:47.3030000Z`; `3ms: 69cdc965d385e3b94310f788.jsonl[2703] _id=69eb7a2a1724f0c9e2fb87f9 ts=2026-04-24T14:11:53.7920000Z ~ 69cdc965d385e3b94310f788.jsonl[2701] _id=69eb7a2b1724f0c9e2fb87fd ts=2026-04-24T14:11:53.7950000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `914ms: 69cdc965d385e3b94310f788.jsonl[2232] _id=69e8cfb11724f0c9e2fa2e49 ts=2026-04-22T13:40:00.0910000Z ~ 69cdc965d385e3b94310f788.jsonl[545] _id=69e8cfb11724f0c9e2fa2e5c ts=2026-04-22T13:40:01.0050000Z`; `582ms: 69cdc965d385e3b94310f788.jsonl[545] _id=69e8cfb11724f0c9e2fa2e5c ts=2026-04-22T13:40:01.0050000Z ~ 69cdc965d385e3b94310f788.jsonl[2218] _id=69e8cfb21724f0c9e2fa2e69 ts=2026-04-22T13:40:01.5870000Z`; `401ms: 69cdc965d385e3b94310f788.jsonl[2218] _id=69e8cfb21724f0c9e2fa2e69 ts=2026-04-22T13:40:01.5870000Z ~ 69cdc965d385e3b94310f788.jsonl[541] _id=69e8cfb21724f0c9e2fa2e6b ts=2026-04-22T13:40:01.9880000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f788.jsonl[424] _id=69e0f3a07957a33870f558bb ts=2026-04-16T14:35:12.6150000Z -> 69cdc965d385e3b94310f788.jsonl[1635] _id=69e627b71724f0c9e2f84b73 ts=2026-04-20T13:18:46.7030000Z; 47h 28m: 69cdc965d385e3b94310f788.jsonl[817] _id=69e8db631724f0c9e2fa74eb ts=2026-04-22T14:29:54.6730000Z -> 69cdc965d385e3b94310f788.jsonl[818] _id=69eb771f1724f0c9e2fb77cd ts=2026-04-24T13:58:54.4580000Z; 47h 3m: 69cdc965d385e3b94310f788.jsonl[1159] _id=69de4fbc7957a33870f36a72 ts=2026-04-14T14:31:23.4050000Z -> 69cdc965d385e3b94310f788.jsonl[171] _id=69e0e56b7957a33870f4fb5b ts=2026-04-16T13:34:35.5360000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 482 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f788.jsonl[2066] _id=69e633691724f0c9e2f88fd3 ts=2026-04-20T14:08:41.7860000Z -> 69cdc965d385e3b94310f788.jsonl[2067] _id=69e6344d1724f0c9e2f89445 ts=2026-04-20T14:08:41.786Z; 0ms: 69cdc965d385e3b94310f788.jsonl[758] _id=69e8d7101724f0c9e2fa5e3f ts=2026-04-22T14:11:27.8090000Z -> 69cdc965d385e3b94310f788.jsonl[2462] _id=69e8d72d1724f0c9e2fa5f43 ts=2026-04-22T14:11:27.809Z; 2ms: 69cdc965d385e3b94310f788.jsonl[1378] _id=69e0ec527957a33870f5271d ts=2026-04-16T14:04:02.7090000Z -> 69cdc965d385e3b94310f788.jsonl[1379] _id=69e0ec527957a33870f5271f ts=2026-04-16T14:04:02.7110000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 69cdc965d385e3b94310f788.jsonl[1583] _id=69e0f2177957a33870f54ac7 ts=2026-04-16T14:28:39.6220000Z -> 69cdc965d385e3b94310f788.jsonl[2031] _id=69e633691724f0c9e2f88fd1 ts=2026-04-20T14:08:41.7450000Z; 48h 19m: 69cdc965d385e3b94310f788.jsonl[1018] _id=69de4aa07957a33870f346b3 ts=2026-04-14T14:09:36.7090000Z -> 69cdc965d385e3b94310f788.jsonl[1583] _id=69e0f2177957a33870f54ac7 ts=2026-04-16T14:28:39.6220000Z; 48h 2m: 69cdc965d385e3b94310f788.jsonl[2031] _id=69e633691724f0c9e2f88fd1 ts=2026-04-20T14:08:41.7450000Z -> 69cdc965d385e3b94310f788.jsonl[756] _id=69e8d7101724f0c9e2fa5e39 ts=2026-04-22T14:11:27.7940000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc965d385e3b94310f788.jsonl[1631] _id=69e0f3ac7957a33870f558e9 ts=2026-04-16T14:35:24.6880000Z -> 69cdc965d385e3b94310f788.jsonl[1634] _id=69e627961724f0c9e2f84acf ts=2026-04-20T13:18:13.3180000Z; 47h 28m: 69cdc965d385e3b94310f788.jsonl[2578] _id=69e8db801724f0c9e2fa750b ts=2026-04-22T14:30:23.8100000Z -> 69cdc965d385e3b94310f788.jsonl[2588] _id=69eb77051724f0c9e2fb775b ts=2026-04-24T13:58:28.4640000Z; 47h 3m: 69cdc965d385e3b94310f788.jsonl[1160] _id=69de4fbc7957a33870f36a76 ts=2026-04-14T14:31:24.4270000Z -> 69cdc965d385e3b94310f788.jsonl[1161] _id=69e0e5677957a33870f4fb1b ts=2026-04-16T13:34:31.2180000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 46m 
  - Evidence: 95h 46m: 69cdc965d385e3b94310f788.jsonl[1321] _id=69e0ea597957a33870f51d73 ts=2026-04-16T13:55:37.5200000Z -> 69cdc965d385e3b94310f788.jsonl[1856] _id=69e62d351724f0c9e2f86da5 ts=2026-04-20T13:42:13.5790000Z; 47h 17m: 69cdc965d385e3b94310f788.jsonl[1089] _id=69de4dc37957a33870f35cb5 ts=2026-04-14T14:22:59.8040000Z -> 69cdc965d385e3b94310f788.jsonl[183] _id=69e0e6dc7957a33870f50595 ts=2026-04-16T13:40:44.5470000Z; 37m 38s: 69cdc965d385e3b94310f788.jsonl[1858] _id=69e62d561724f0c9e2f86e2f ts=2026-04-20T13:42:46.5540000Z -> 69cdc965d385e3b94310f788.jsonl[2093] _id=69e636291724f0c9e2f8a093 ts=2026-04-20T14:20:25.3180000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc965d385e3b94310f788.jsonl[1621] _id=69e0f3587957a33870f556df ts=2026-04-16T14:34:00.4420000Z -> 69cdc965d385e3b94310f788.jsonl[1701] _id=69e629871724f0c9e2f85415 ts=2026-04-20T13:26:31.8450000Z; 47h 13m: 69cdc965d385e3b94310f788.jsonl[167] _id=69de4fab7957a33870f36a06 ts=2026-04-14T14:31:07.5270000Z -> 69cdc965d385e3b94310f788.jsonl[1233] _id=69e0e7df7957a33870f50cd9 ts=2026-04-16T13:45:03.6300000Z; 28m 57s: 69cdc965d385e3b94310f788.jsonl[1751] _id=69e62b2b1724f0c9e2f85ecd ts=2026-04-20T13:33:31.7320000Z -> 69cdc965d385e3b94310f788.jsonl[1987] _id=69e631f41724f0c9e2f88739 ts=2026-04-20T14:02:28.8880000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc965d385e3b94310f788.jsonl[1627] _id=69e0f3567957a33870f556c1 ts=2026-04-16T14:33:58.3930000Z -> 69cdc965d385e3b94310f788.jsonl[1711] _id=69e629991724f0c9e2f8547b ts=2026-04-20T13:26:49.7720000Z; 47h 14m: 69cdc965d385e3b94310f788.jsonl[1157] _id=69de4fa97957a33870f369fa ts=2026-04-14T14:31:05.4260000Z -> 69cdc965d385e3b94310f788.jsonl[1234] _id=69e0e7ea7957a33870f50d15 ts=2026-04-16T13:45:14.9750000Z; 29m 1s: 69cdc965d385e3b94310f788.jsonl[1754] _id=69e62b291724f0c9e2f85ec1 ts=2026-04-20T13:33:29.7820000Z -> 69cdc965d385e3b94310f788.jsonl[1989] _id=69e631f71724f0c9e2f88745 ts=2026-04-20T14:02:31.2860000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.047s..0.047s shown 
  - Evidence: 47ms: 69cdc965d385e3b94310f788.jsonl[1156] _id=69de4f9d7957a33870f369a2 ts=2026-04-14T14:30:53.5430000Z -> 69cdc965d385e3b94310f788.jsonl[166] _id=69de4f9e7957a33870f369ac ts=2026-04-14T14:30:53.5900000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 10m 
  - Evidence: 95h 10m: 69cdc965d385e3b94310f788.jsonl[1540] _id=69e0f1867957a33870f545ff ts=2026-04-16T14:26:14.8170000Z -> 69cdc965d385e3b94310f788.jsonl[1784] _id=69e62bf51724f0c9e2f864c3 ts=2026-04-20T13:36:53.3250000Z; 48h 18m: 69cdc965d385e3b94310f788.jsonl[1810] _id=69e62c821724f0c9e2f869af ts=2026-04-20T13:39:14.5890000Z -> 69cdc965d385e3b94310f788.jsonl[2342] _id=69e8d3e71724f0c9e2fa46ff ts=2026-04-22T13:57:59.0090000Z; 48h 15m: 69cdc965d385e3b94310f788.jsonl[985] _id=69de49e77957a33870f34151 ts=2026-04-14T14:06:31.4580000Z -> 69cdc965d385e3b94310f788.jsonl[388] _id=69e0f0a27957a33870f54039 ts=2026-04-16T14:22:26.2440000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 11m 
  - Evidence: 95h 11m: 69cdc965d385e3b94310f788.jsonl[1539] _id=69e0f1807957a33870f545c1 ts=2026-04-16T14:26:08.5780000Z -> 69cdc965d385e3b94310f788.jsonl[1786] _id=69e62c071724f0c9e2f86547 ts=2026-04-20T13:37:11.3840000Z; 48h 16m: 69cdc965d385e3b94310f788.jsonl[105] _id=69de49e37957a33870f34139 ts=2026-04-14T14:06:26.8360000Z -> 69cdc965d385e3b94310f788.jsonl[1515] _id=69e0f0a47957a33870f5404d ts=2026-04-16T14:22:28.4920000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 14m 
  - Evidence: 95h 14m: 69cdc965d385e3b94310f788.jsonl[1529] _id=69e0f0f27957a33870f5420b ts=2026-04-16T14:23:46.9950000Z -> 69cdc965d385e3b94310f788.jsonl[1802] _id=69e62c4a1724f0c9e2f8676f ts=2026-04-20T13:38:18.0130000Z; 48h 18m: 69cdc965d385e3b94310f788.jsonl[1811] _id=69e62c751724f0c9e2f86903 ts=2026-04-20T13:39:01.1120000Z -> 69cdc965d385e3b94310f788.jsonl[2338] _id=69e8d3e41724f0c9e2fa46e7 ts=2026-04-22T13:57:55.7450000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 69cdc965d385e3b94310f788.jsonl[2338] _id=69e8d3e41724f0c9e2fa46e7 ts=2026-04-22T13:57:55.7450000Z -> 69cdc965d385e3b94310f788.jsonl[2339] _id=69e8d3e51724f0c9e2fa46e9 ts=2026-04-22T13:57:55.7500000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc965d385e3b94310f788.jsonl[1602] _id=69e0f2d57957a33870f551a3 ts=2026-04-16T14:31:49.3440000Z -> 69cdc965d385e3b94310f788.jsonl[1633] _id=69e627981724f0c9e2f84ad3 ts=2026-04-20T13:18:15.9250000Z; 47h 31m: 69cdc965d385e3b94310f788.jsonl[2561] _id=69e8daab1724f0c9e2fa7135 ts=2026-04-22T14:26:51.0140000Z -> 69cdc965d385e3b94310f788.jsonl[2590] _id=69eb77081724f0c9e2fb7765 ts=2026-04-24T13:58:31.6630000Z; 47h 5m: 69cdc965d385e3b94310f788.jsonl[1144] _id=69de4f397957a33870f36582 ts=2026-04-14T14:29:13.6270000Z -> 69cdc965d385e3b94310f788.jsonl[169] _id=69e0e56a7957a33870f4fb4d ts=2026-04-16T13:34:33.9410000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f788.jsonl[90] _id=69de49127957a33870f33b09 ts=2026-04-14T14:02:57.7000000Z -> 69cdc965d385e3b94310f788.jsonl[960] _id=69de49127957a33870f33b0d ts=2026-04-14T14:02:57.7020000Z; 3ms: 69cdc965d385e3b94310f788.jsonl[2703] _id=69eb7a2a1724f0c9e2fb87f9 ts=2026-04-24T14:11:53.7920000Z -> 69cdc965d385e3b94310f788.jsonl[2701] _id=69eb7a2b1724f0c9e2fb87fd ts=2026-04-24T14:11:53.7950000Z; 4ms: 69cdc965d385e3b94310f788.jsonl[508] _id=69e639211724f0c9e2f8af9d ts=2026-04-20T14:33:05.2740000Z -> 69cdc965d385e3b94310f788.jsonl[509] _id=69e639211724f0c9e2f8af9f ts=2026-04-20T14:33:05.2780000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc965d385e3b94310f788.jsonl:69cdc965d385e3b94310f788, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f788.jsonl[1089] _id=69de4dc37957a33870f35cb5 ts=2026-04-14T14:22:59.8040000Z`; `69cdc965d385e3b94310f788.jsonl[186] _id=69e0e6df7957a33870f505b1 ts=2026-04-16T13:40:47.4840000Z`; `69cdc965d385e3b94310f788.jsonl[1321] _id=69e0ea597957a33870f51d73 ts=2026-04-16T13:55:37.5200000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 48 record(s) match the trigger in 69cdc965d385e3b94310f788.jsonl:69cdc965d385e3b94310f788, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f788.jsonl[1148] _id=69de4f5a7957a33870f3677a ts=2026-04-14T14:29:46.3630000Z`; `69cdc965d385e3b94310f788.jsonl[164] _id=69de4f5a7957a33870f3677c ts=2026-04-14T14:29:46.7770000Z`; `69cdc965d385e3b94310f788.jsonl[1156] _id=69de4f9d7957a33870f369a2 ts=2026-04-14T14:30:53.5430000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f788.jsonl[1406] _id=69e0ecfd7957a33870f52b27 ts=2026-04-16T14:06:53.0640000Z`; `69cdc965d385e3b94310f788.jsonl[1676] _id=69e628b81724f0c9e2f8503b ts=2026-04-20T13:23:04.8200000Z`; `69cdc965d385e3b94310f788.jsonl[430] _id=69e629491724f0c9e2f852e1 ts=2026-04-20T13:25:29.0410000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f788.jsonl[1810] _id=69e62c821724f0c9e2f869af ts=2026-04-20T13:39:14.5890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f788.jsonl[2338] _id=69e8d3e41724f0c9e2fa46e7 ts=2026-04-22T13:57:55.7450000Z`; `69cdc965d385e3b94310f788.jsonl[2339] _id=69e8d3e51724f0c9e2fa46e9 ts=2026-04-22T13:57:55.7500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f788.jsonl[520] _id=69e8cd7b1724f0c9e2fa1dbd ts=2026-04-22T13:30:34.8650000Z`; `69cdc965d385e3b94310f788.jsonl[527] _id=69e8cea11724f0c9e2fa2631 ts=2026-04-22T13:35:28.4660000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f788.jsonl[2614] _id=69eb778c1724f0c9e2fb7a00 ts=2026-04-24T14:00:44.0230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 162 unmatched 'DialogueStartEvent' (totals: 363 start, 205 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 7 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 47 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.23s, min -227.64s, max +0.10s over 2774 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f788\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=complete 
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
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 46 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1912 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (602); Unit 3 Dev (298); Unit 5 Dev (260); Unit 4 Dev (211); Unit 1 Dev (172); Unit 4 Dev - Anderson Base (132); Unit 4 Dev - Dungeon (125); Unit 3 Dungeon Dev (89); Unit 5 Dev - Dungeon (23)
- **eventKey:** present on 1344 of 1912 records
- **Intervals:** median 2.39s (p5 0.01s / p95 31.53s, n=1911)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1344; [conversationId, dialogueEventType] x568
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1912/1912 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 1912/1912 records)
    "DialogueNodeEvent"  x1344
    "DialogueStartEvent"  x363
    "DialogueFinishEvent"  x205
data.nodeId  (number, 1344/1912 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 498 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (145); Unit 3 Dev (75); Unit 4 Dev - Dungeon (50); Unit 1 Dev (49); Unit 5 Dev (47); Unit 4 Dev (42); Unit 3 Dungeon Dev (37); Unit 4 Dev - Anderson Base (27); Unit 5 Dev - Dungeon (26)
- **Intervals:** median 30.00s (p5 29.97s / p95 37.69s, n=486)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 498/498 records)
data.position.x  (number, 498/498 records)
    numeric range -688.465 .. 1682.09 (294 unique)
data.position.y  (number, 498/498 records)
    numeric range -114.326 .. 222.252 (237 unique)
data.position.z  (number, 498/498 records)
    numeric range -1110.54 .. 1873.98 (294 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 4 Dev - Dungeon (13); Unit 5 Dev (13); Unit 1 Dev (12); Unit 3 Dev (10); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 133.42s (p5 0.01s / p95 1205.88s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x37
data.questID  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/84 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 69 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (69)
- **Intervals:** median 4.33s (p5 0.29s / p95 28.94s, n=68)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 69/69 records)
    "On"  x40
    "Off"  x29
data.floor  (string, 69/69 records)
    "4"  x32
    "3"  x27
    "1"  x5
    "2"  x5
data.machineNumber  (string, 69/69 records)
    "One"  x64
    "Two"  x5
data.machineType  (string, 69/69 records)
    "Condenser"  x44
    "Evaporator"  x13
    "DualChamber_Condenser"  x4
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x4
data.room  (string, 69/69 records)
    "2"  x34
    "3"  x23
    "4"  x8
    "1"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 48 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (20)
- **Intervals:** median 2.07s (p5 0.31s / p95 1660.12s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "dragEnd"  x24
    "dragStart"  x24
data.featureUsed  (string, 48/48 records)
    "waypoint"  x48
data.location  (object, 48/48 records)
data.location.x  (number, 48/48 records)
    numeric range -770.79 .. 268.14 (24 unique)
data.location.y  (number, 48/48 records)
    numeric range -314.487 .. 289.668 (25 unique)
data.location.z  (number, 48/48 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Topographic Map Event` — 46 records

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (18)
- **Intervals:** median 18.60s (p5 2.43s / p95 1575.94s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "MapCloseEvent"  x23
    "MapOpenEvent"  x23
data.featureUsed  (string, 46/46 records)
    "Map"  x46
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 34 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 3 Dev (11); Unit 1 Dev (10)
- **Intervals:** median 5.60s (p5 1.65s / p95 69556.45s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "argumentationNodeAdd"  x23
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 34/34 records)
    "Unit 2 – Watershed"  x13
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 34/34 records)
    "A"  x13
    "B"  x7
    "3"  x4
    "1"  x3
    "I"  x3
    "D"  x2
    "5"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 28 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (14); Unit 2 Prod (Refactor) (10); Unit 3 Dev (4)
- **Intervals:** median 5.36s (p5 0.07s / p95 121783.44s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "argumentationToolClose"  x15
    "argumentationToolOpen"  x13
data.argumentationTitle  (string, 28/28 records)
    "Unit 4 - Flooding"  x14
    "Unit 2 – Watershed"  x10
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 28/28 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x8
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Watershed Graph"  x6
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Waterfall Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 18 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (18)
- **Intervals:** median 0.58s (p5 0.20s / p95 69.86s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "ChangeCanister"  x18
data.canisterType  (string, 18/18 records)
    "Gravel"  x11
    "Bedrock"  x5
    "Clay"  x1
    "Sand"  x1
data.floor  (string, 18/18 records)
    "4"  x11
    "5"  x7
data.machine  (string, 18/18 records)
    "1"  x17
    "2"  x1
data.row  (string, 18/18 records)
    "TopRow"  x13
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 184.89s (p5 18.45s / p95 249845.76s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionOpen"  x7
    "argumentationSessionClose"  x6
data.argumentationDescription  (string, 13/13 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 13/13 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 55.32s (p5 2.85s / p95 274983.53s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/10 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/10 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 5.33s (p5 1.35s / p95 22.35s, n=7)
- **`data` key-set variants:** [actionType, boxId, soilType] x4; [actionType, boxID, soilType] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "cameraPlaced"  x4
    "soilSelected"  x4
data.boxID  (string, 4/8 records)
    "2"  x2
    "0"  x1
    "1"  x1
data.boxId  (string, 4/8 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 8/8 records)
    "Gravel"  x3
    "Clay"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 5 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 172966.05s (p5 34843.13s / p95 310310.28s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "5"  x2
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "dragStart" (24x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*