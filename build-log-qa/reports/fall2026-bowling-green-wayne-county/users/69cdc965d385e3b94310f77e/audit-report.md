# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77e
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f77e.jsonl
- **Records:** 3038 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f77e
- **Time span:** 2026-04-14T13:39:40.181000+00:00 .. 2026-04-22T14:13:31.915000+00:00 (192h 33m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 3038 records, 9 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 67 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 2129 | 70.08 | 1 | 9 | 1503 | 2026-04-14T13:39:58.508000+00:00 | 2026-04-22T14:13:31.915000+00:00 | 192h 33m |
| PlayerPositionEvent | 483 | 15.9 | 1 | 9 | 0 | 2026-04-14T13:39:40.181000+00:00 | 2026-04-22T14:13:08.147000+00:00 | 192h 33m |
| WaterChamberEvent | 135 | 4.44 | 1 | 1 | 0 | 2026-04-22T13:46:14.130000+00:00 | 2026-04-22T14:04:43.477000+00:00 | 18m 29s |
| Topographic Map Event | 98 | 3.23 | 1 | 2 | 0 | 2026-04-14T14:31:15.361000+00:00 | 2026-04-20T14:20:16.444000+00:00 | 143h 49m |
| questEvent | 84 | 2.76 | 1 | 9 | 84 | 2026-04-14T13:39:58.491000+00:00 | 2026-04-22T14:13:09.978000+00:00 | 192h 33m |
| TopographicMapEvent | 24 | 0.79 | 1 | 2 | 0 | 2026-04-16T13:52:19.232000+00:00 | 2026-04-20T14:20:15.414000+00:00 | 96h 27m |
| argumentationNodeEvent | 23 | 0.76 | 1 | 3 | 0 | 2026-04-14T14:02:47.855000+00:00 | 2026-04-20T13:38:04.052000+00:00 | 143h 35m |
| argumentationToolEvent | 20 | 0.66 | 1 | 3 | 0 | 2026-04-16T14:30:49.688000+00:00 | 2026-04-22T13:35:33.169000+00:00 | 143h 4m |
| Soil Key Puzzle | 12 | 0.39 | 1 | 3 | 0 | 2026-04-14T14:17:07+00:00 | 2026-04-20T14:27:04.334000+00:00 | 144h 9m |
| argumentationEvent | 12 | 0.39 | 1 | 5 | 0 | 2026-04-14T14:02:13.539000+00:00 | 2026-04-22T14:09:46.832000+00:00 | 192h 7m |
| soilMachine | 8 | 0.26 | 1 | 1 | 0 | 2026-04-22T13:19:54.437000+00:00 | 2026-04-22T13:23:36.703000+00:00 | 3m 42s |
| EndOfUnit | 6 | 0.2 | 1 | 5 | 0 | 2026-04-14T14:07:37.642000+00:00 | 2026-04-22T14:12:57.966000+00:00 | 192h 5m |
| TerasGardenBox | 4 | 0.13 | 1 | 1 | 0 | 2026-04-22T13:38:02.933000+00:00 | 2026-04-22T13:38:29.987000+00:00 | 27.1s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.179s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 170285.495s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.008s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 30.678s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 9.153s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 0.724s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.843s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.804s median 
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
  - Observed: 8.502s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 98 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
  - Expected: 83 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 6.8x vs baseline. 
  - Observed: 135 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 23 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C 
  - Expected: may simply not have been exercised — review
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 53 mismatch(es); e.g. 'DialogueNodeEvent:31:70' vs expected 'DialogueNodeEvent:31:71' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[641] _id=69de48e67957a33870f339af ts=2026-04-14T14:02:14.1610000Z`; `69cdc965d385e3b94310f77e.jsonl[32] _id=69de48e67957a33870f339b1 ts=2026-04-14T14:02:14.2700000Z`; `69cdc965d385e3b94310f77e.jsonl[33] _id=69de48e67957a33870f339b3 ts=2026-04-14T14:02:14.5830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 98 records, TopographicMapEvent: 24 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2128 | 0.0 | 1.179 | 325.758 | 30.117 | 341034.0 | 0.18 | 518 | 4 |
| PlayerPositionEvent | 471 | 14.322 | 30.008 | 1471.133 | 39.904 | 340976.108 | 0.04 | 0 | 3 |
| WaterChamberEvent | 134 | 0.054 | 0.724 | 8.279 | 27.88 | 344.968 | 7.25 | 0 | 0 |
| Topographic Map Event | 97 | 0.064 | 10.419 | 5337.537 | 320.762 | 341497.587 | 0.01 | 0 | 4 |
| questEvent | 83 | 0.002 | 107.173 | 8351.705 | 1164.898 | 341002.578 | 0.01 | 14 | 7 |
| TopographicMapEvent | 23 | 1.049 | 3.404 | 15098.964 | 2582.474 | 343957.854 | 0.0 | 0 | 2 |
| argumentationNodeEvent | 22 | 0.862 | 5.843 | 23496.191 | 165725.777 | 342269.29 | 0.0 | 0 | 2 |
| argumentationToolEvent | 19 | 0.002 | 0.804 | 27109.657 | 189511.412 | 342389.43 | 0.0 | 3 | 2 |
| Soil Key Puzzle | 11 | 2.924 | 30.678 | 47181.576 | 257170.014 | 344607.218 | 0.0 | 0 | 5 |
| argumentationEvent | 11 | 0.077 | 71.668 | 62877.572 | 258331.207 | 342245.228 | 0.0 | 0 | 4 |
| soilMachine | 7 | 0.664 | 8.502 | 31.752 | 129.819 | 178.874 | 1.89 | 0 | 0 |
| EndOfUnit | 5 | 0.0 | 170285.495 | 138304.065 | 310836.404 | 344969.549 | 0.0 | 1 | 4 |
| TerasGardenBox | 3 | 8.726 | 9.153 | 9.018 | 9.173 | 9.175 | 6.65 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.96s, p95 39.90s, n=471) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc965d385e3b94310f77e.jsonl[2718] _id=69e8cfc11724f0c9e2fa2f05 ts=2026-04-22T13:40:16.5100000Z ~ 69cdc965d385e3b94310f77e.jsonl[2712] _id=69e8cfcf1724f0c9e2fa2f69 ts=2026-04-22T13:40:16.51Z`
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `211ms: 69cdc965d385e3b94310f77e.jsonl[1037] _id=69e0e73b7957a33870f508b1 ts=2026-04-16T13:42:18.3710000Z ~ 69cdc965d385e3b94310f77e.jsonl[1038] _id=69e0e73b7957a33870f508b9 ts=2026-04-16T13:42:18.5820000Z`; `74ms: 69cdc965d385e3b94310f77e.jsonl[1038] _id=69e0e73b7957a33870f508b9 ts=2026-04-16T13:42:18.5820000Z ~ 69cdc965d385e3b94310f77e.jsonl[1039] _id=69e0e73b7957a33870f508bb ts=2026-04-16T13:42:18.6560000Z`; `632ms: 69cdc965d385e3b94310f77e.jsonl[1665] _id=69e62a801724f0c9e2f859ff ts=2026-04-20T13:30:38.7520000Z ~ 69cdc965d385e3b94310f77e.jsonl[1663] _id=69e62a811724f0c9e2f85a07 ts=2026-04-20T13:30:39.3840000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 48 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `965ms: 69cdc965d385e3b94310f77e.jsonl[2796] _id=69e8d34e1724f0c9e2fa43bf ts=2026-04-22T13:55:26.2670000Z ~ 69cdc965d385e3b94310f77e.jsonl[2800] _id=69e8d34f1724f0c9e2fa43cb ts=2026-04-22T13:55:27.2320000Z`; `771ms: 69cdc965d385e3b94310f77e.jsonl[2797] _id=69e8d34f1724f0c9e2fa43c3 ts=2026-04-22T13:55:26.6210000Z ~ 69cdc965d385e3b94310f77e.jsonl[2801] _id=69e8d34f1724f0c9e2fa43cd ts=2026-04-22T13:55:27.3920000Z`; `369ms: 69cdc965d385e3b94310f77e.jsonl[2800] _id=69e8d34f1724f0c9e2fa43cb ts=2026-04-22T13:55:27.2320000Z ~ 69cdc965d385e3b94310f77e.jsonl[2798] _id=69e8d3501724f0c9e2fa43d1 ts=2026-04-22T13:55:27.6010000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `77ms: 69cdc965d385e3b94310f77e.jsonl[1780] _id=69e62c3f1724f0c9e2f86709 ts=2026-04-20T13:38:05.5540000Z ~ 69cdc965d385e3b94310f77e.jsonl[261] _id=69e62c3f1724f0c9e2f86719 ts=2026-04-20T13:38:05.6310000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `563ms: 69cdc965d385e3b94310f77e.jsonl[1761] _id=69e62c151724f0c9e2f865c3 ts=2026-04-20T13:37:23.9050000Z ~ 69cdc965d385e3b94310f77e.jsonl[1748] _id=69e62c161724f0c9e2f865c7 ts=2026-04-20T13:37:24.4680000Z`; `2ms: 69cdc965d385e3b94310f77e.jsonl[2545] _id=69e8ce031724f0c9e2fa21bb ts=2026-04-22T13:32:50.5500000Z ~ 69cdc965d385e3b94310f77e.jsonl[2548] _id=69e8ce031724f0c9e2fa21bd ts=2026-04-22T13:32:50.5520000Z`; `846ms: 69cdc965d385e3b94310f77e.jsonl[2577] _id=69e8cea41724f0c9e2fa2642 ts=2026-04-22T13:35:31.7720000Z ~ 69cdc965d385e3b94310f77e.jsonl[2583] _id=69e8cea51724f0c9e2fa264b ts=2026-04-22T13:35:32.6180000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 69cdc965d385e3b94310f77e.jsonl[2960] _id=69e8d6b31724f0c9e2fa5b21 ts=2026-04-22T14:09:55.0070000Z ~ 69cdc965d385e3b94310f77e.jsonl[448] _id=69e8d6b31724f0c9e2fa5b23 ts=2026-04-22T14:09:55.0140000Z`; `10ms: 69cdc965d385e3b94310f77e.jsonl[2988] _id=69e8d71e1724f0c9e2fa5ebd ts=2026-04-22T14:11:42.1870000Z ~ 69cdc965d385e3b94310f77e.jsonl[2989] _id=69e8d71e1724f0c9e2fa5ec1 ts=2026-04-22T14:11:42.1970000Z`; `2ms: 69cdc965d385e3b94310f77e.jsonl[3031] _id=69e8d7761724f0c9e2fa6151 ts=2026-04-22T14:13:09.9760000Z ~ 69cdc965d385e3b94310f77e.jsonl[3029] _id=69e8d7771724f0c9e2fa6155 ts=2026-04-22T14:13:09.9780000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `664ms: 69cdc965d385e3b94310f77e.jsonl[330] _id=69e8cbd71724f0c9e2fa140d ts=2026-04-22T13:23:35.0140000Z ~ 69cdc965d385e3b94310f77e.jsonl[331] _id=69e8cbd81724f0c9e2fa1411 ts=2026-04-22T13:23:35.6780000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f77e.jsonl[1559] _id=69e0f3917957a33870f5587b ts=2026-04-16T14:34:56.4960000Z -> 69cdc965d385e3b94310f77e.jsonl[1570] _id=69e627bc1724f0c9e2f84b89 ts=2026-04-20T13:18:50.4960000Z; 47h 1m: 69cdc965d385e3b94310f77e.jsonl[932] _id=69de4fc37957a33870f36aa4 ts=2026-04-14T14:31:31.3960000Z -> 69cdc965d385e3b94310f77e.jsonl[86] _id=69e0e4fb7957a33870f4f9ad ts=2026-04-16T13:32:42.7650000Z; 46h 39m: 69cdc965d385e3b94310f77e.jsonl[322] _id=69e639a01724f0c9e2f8b56b ts=2026-04-20T14:35:10.6780000Z -> 69cdc965d385e3b94310f77e.jsonl[2354] _id=69e8c9d61724f0c9e2fa09e9 ts=2026-04-22T13:15:01.4470000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 518 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77e.jsonl[232] _id=69e0f30a7957a33870f5535f ts=2026-04-16T14:32:41.4900000Z -> 69cdc965d385e3b94310f77e.jsonl[1543] _id=69e0f31b7957a33870f553df ts=2026-04-16T14:32:41.49Z; 2ms: 69cdc965d385e3b94310f77e.jsonl[2597] _id=69e8ceae1724f0c9e2fa26a7 ts=2026-04-22T13:35:41.5640000Z -> 69cdc965d385e3b94310f77e.jsonl[2588] _id=69e8ceae1724f0c9e2fa26ab ts=2026-04-22T13:35:41.5660000Z; 3ms: 69cdc965d385e3b94310f77e.jsonl[1220] _id=69e0ed057957a33870f52b49 ts=2026-04-16T14:07:00.7370000Z -> 69cdc965d385e3b94310f77e.jsonl[1221] _id=69e0ed067957a33870f52b4b ts=2026-04-16T14:07:00.7400000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 49m 
  - Evidence: 95h 49m: 69cdc965d385e3b94310f77e.jsonl[1541] _id=69e0f30a7957a33870f5535b ts=2026-04-16T14:32:41.4660000Z -> 69cdc965d385e3b94310f77e.jsonl[2241] _id=69e636941724f0c9e2f8a365 ts=2026-04-20T14:22:11.0150000Z; 48h 25m: 69cdc965d385e3b94310f77e.jsonl[708] _id=69de4a297957a33870f3434b ts=2026-04-14T14:07:37.6420000Z -> 69cdc965d385e3b94310f77e.jsonl[1541] _id=69e0f30a7957a33870f5535b ts=2026-04-16T14:32:41.4660000Z; 47h 18m: 69cdc965d385e3b94310f77e.jsonl[2241] _id=69e636941724f0c9e2f8a365 ts=2026-04-20T14:22:11.0150000Z -> 69cdc965d385e3b94310f77e.jsonl[2718] _id=69e8cfc11724f0c9e2fa2f05 ts=2026-04-22T13:40:16.5100000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77e.jsonl[2718] _id=69e8cfc11724f0c9e2fa2f05 ts=2026-04-22T13:40:16.5100000Z -> 69cdc965d385e3b94310f77e.jsonl[2712] _id=69e8cfcf1724f0c9e2fa2f69 ts=2026-04-22T13:40:16.51Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc965d385e3b94310f77e.jsonl[1560] _id=69e0f3a77957a33870f558d1 ts=2026-04-16T14:35:18.6110000Z -> 69cdc965d385e3b94310f77e.jsonl[1564] _id=69e627991724f0c9e2f84add ts=2026-04-20T13:18:14.7190000Z; 47h 1m: 69cdc965d385e3b94310f77e.jsonl[926] _id=69de4faf7957a33870f36a22 ts=2026-04-14T14:31:11.2390000Z -> 69cdc965d385e3b94310f77e.jsonl[933] _id=69e0e4f77957a33870f4f9a9 ts=2026-04-16T13:32:38.6250000Z; 46h 39m: 69cdc965d385e3b94310f77e.jsonl[2294] _id=69e639a31724f0c9e2f8b579 ts=2026-04-20T14:35:13.3290000Z -> 69cdc965d385e3b94310f77e.jsonl[2358] _id=69e8c9d31724f0c9e2fa09db ts=2026-04-22T13:14:58.7340000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 43m 
  - Evidence: 95h 43m: 69cdc965d385e3b94310f77e.jsonl[1167] _id=69e0eb487957a33870f52287 ts=2026-04-16T13:59:35.6970000Z -> 69cdc965d385e3b94310f77e.jsonl[1831] _id=69e62d681724f0c9e2f86e9f ts=2026-04-20T13:43:02.9150000Z; 47h 8m: 69cdc965d385e3b94310f77e.jsonl[869] _id=69de4ee07957a33870f36321 ts=2026-04-14T14:27:44.2300000Z -> 69cdc965d385e3b94310f77e.jsonl[967] _id=69e0e5e67957a33870f4ffe7 ts=2026-04-16T13:36:37.0390000Z; 43m 15s: 69cdc965d385e3b94310f77e.jsonl[1834] _id=69e62d871724f0c9e2f86f1b ts=2026-04-20T13:43:33.5930000Z -> 69cdc965d385e3b94310f77e.jsonl[2275] _id=69e637aa1724f0c9e2f8ab23 ts=2026-04-20T14:26:48.9610000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc965d385e3b94310f77e.jsonl[1432] _id=69e0f2087957a33870f54a1f ts=2026-04-16T14:28:23.5730000Z -> 69cdc965d385e3b94310f77e.jsonl[1562] _id=69e628031724f0c9e2f84d39 ts=2026-04-20T13:20:01.1600000Z; 47h 7m: 69cdc965d385e3b94310f77e.jsonl[931] _id=69de4fc37957a33870f36a9e ts=2026-04-14T14:31:31.3800000Z -> 69cdc965d385e3b94310f77e.jsonl[984] _id=69e0e67d7957a33870f50344 ts=2026-04-16T13:39:07.6540000Z; 46m 34s: 69cdc965d385e3b94310f77e.jsonl[1675] _id=69e62ac31724f0c9e2f85bb9 ts=2026-04-20T13:31:45.7140000Z -> 69cdc965d385e3b94310f77e.jsonl[2178] _id=69e635ae1724f0c9e2f89d75 ts=2026-04-20T14:18:20.6940000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 32m 
  - Evidence: 95h 32m: 69cdc965d385e3b94310f77e.jsonl[1149] _id=69e0ea8d7957a33870f51edf ts=2026-04-16T13:56:28.6550000Z -> 69cdc965d385e3b94310f77e.jsonl[1656] _id=69e62a241724f0c9e2f8582b ts=2026-04-20T13:29:06.5090000Z; 47m 29s: 69cdc965d385e3b94310f77e.jsonl[1670] _id=69e62a901724f0c9e2f85a4b ts=2026-04-20T13:30:54.6980000Z -> 69cdc965d385e3b94310f77e.jsonl[2109] _id=69e635b21724f0c9e2f89d8f ts=2026-04-20T14:18:24.2450000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 4m 
  - Evidence: 95h 4m: 69cdc965d385e3b94310f77e.jsonl[1499] _id=69e0f2b27957a33870f54ff7 ts=2026-04-16T14:31:13.1480000Z -> 69cdc965d385e3b94310f77e.jsonl[1744] _id=69e62b981724f0c9e2f86293 ts=2026-04-20T13:35:18.3760000Z; 48h 26m: 69cdc965d385e3b94310f77e.jsonl[47] _id=69de49187957a33870f33b43 ts=2026-04-14T14:03:04.2940000Z -> 69cdc965d385e3b94310f77e.jsonl[1470] _id=69e0f26a7957a33870f54d75 ts=2026-04-16T14:30:01.4800000Z; 47h 54m: 69cdc965d385e3b94310f77e.jsonl[261] _id=69e62c3f1724f0c9e2f86719 ts=2026-04-20T13:38:05.6310000Z -> 69cdc965d385e3b94310f77e.jsonl[2549] _id=69e8ce0a1724f0c9e2fa2211 ts=2026-04-22T13:32:57.5110000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 4m 
  - Evidence: 95h 4m: 69cdc965d385e3b94310f77e.jsonl[1494] _id=69e0f2b07957a33870f54fe7 ts=2026-04-16T14:31:12.0040000Z -> 69cdc965d385e3b94310f77e.jsonl[1661] _id=69e62baf1724f0c9e2f8633d ts=2026-04-20T13:35:41.2940000Z; 48h 27m: 69cdc965d385e3b94310f77e.jsonl[46] _id=69de49167957a33870f33b2d ts=2026-04-14T14:03:02.5730000Z -> 69cdc965d385e3b94310f77e.jsonl[1474] _id=69e0f2847957a33870f54e19 ts=2026-04-16T14:30:27.8990000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 6m 
  - Evidence: 95h 6m: 69cdc965d385e3b94310f77e.jsonl[216] _id=69e0f29c7957a33870f54f2f ts=2026-04-16T14:30:51.7530000Z -> 69cdc965d385e3b94310f77e.jsonl[1759] _id=69e62c131724f0c9e2f865a7 ts=2026-04-20T13:37:21.1830000Z; 47h 55m: 69cdc965d385e3b94310f77e.jsonl[255] _id=69e62c171724f0c9e2f865cf ts=2026-04-20T13:37:25.5850000Z -> 69cdc965d385e3b94310f77e.jsonl[2545] _id=69e8ce031724f0c9e2fa21bb ts=2026-04-22T13:32:50.5500000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.042s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f77e.jsonl[2545] _id=69e8ce031724f0c9e2fa21bb ts=2026-04-22T13:32:50.5500000Z -> 69cdc965d385e3b94310f77e.jsonl[2548] _id=69e8ce031724f0c9e2fa21bd ts=2026-04-22T13:32:50.5520000Z; 6ms: 69cdc965d385e3b94310f77e.jsonl[1760] _id=69e62c151724f0c9e2f865bf ts=2026-04-20T13:37:23.8990000Z -> 69cdc965d385e3b94310f77e.jsonl[1761] _id=69e62c151724f0c9e2f865c3 ts=2026-04-20T13:37:23.9050000Z; 42ms: 69cdc965d385e3b94310f77e.jsonl[2577] _id=69e8cea41724f0c9e2fa2642 ts=2026-04-22T13:35:31.7720000Z -> 69cdc965d385e3b94310f77e.jsonl[2581] _id=69e8cea41724f0c9e2fa2647 ts=2026-04-22T13:35:31.8140000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f77e.jsonl[1555] _id=69e0f3907957a33870f5586f ts=2026-04-16T14:34:55.6540000Z -> 69cdc965d385e3b94310f77e.jsonl[1565] _id=69e6279c1724f0c9e2f84af3 ts=2026-04-20T13:18:18.2320000Z; 47h 1m: 69cdc965d385e3b94310f77e.jsonl[927] _id=69de4fb17957a33870f36a2e ts=2026-04-14T14:31:13.7210000Z -> 69cdc965d385e3b94310f77e.jsonl[934] _id=69e0e4fa7957a33870f4f9ab ts=2026-04-16T13:32:41.2250000Z; 46h 39m: 69cdc965d385e3b94310f77e.jsonl[2348] _id=69e639981724f0c9e2f8b531 ts=2026-04-20T14:35:01.9930000Z -> 69cdc965d385e3b94310f77e.jsonl[2360] _id=69e8c9d61724f0c9e2fa09e7 ts=2026-04-22T13:15:01.2250000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f77e.jsonl[3031] _id=69e8d7761724f0c9e2fa6151 ts=2026-04-22T14:13:09.9760000Z -> 69cdc965d385e3b94310f77e.jsonl[3029] _id=69e8d7771724f0c9e2fa6155 ts=2026-04-22T14:13:09.9780000Z; 3ms: 69cdc965d385e3b94310f77e.jsonl[631] _id=69de48c37957a33870f33885 ts=2026-04-14T14:01:38.6400000Z -> 69cdc965d385e3b94310f77e.jsonl[634] _id=69de48c37957a33870f33887 ts=2026-04-14T14:01:38.6430000Z; 4ms: 69cdc965d385e3b94310f77e.jsonl[2293] _id=69e639981724f0c9e2f8b52e ts=2026-04-20T14:35:01.9890000Z -> 69cdc965d385e3b94310f77e.jsonl[2348] _id=69e639981724f0c9e2f8b531 ts=2026-04-20T14:35:01.9930000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc965d385e3b94310f77e.jsonl:69cdc965d385e3b94310f77e, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[778] _id=69de4c667957a33870f3547f ts=2026-04-14T14:17:09.9240000Z`; `69cdc965d385e3b94310f77e.jsonl[869] _id=69de4ee07957a33870f36321 ts=2026-04-14T14:27:44.2300000Z`; `69cdc965d385e3b94310f77e.jsonl[969] _id=69e0e5e87957a33870f4fffd ts=2026-04-16T13:36:39.9900000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 24 record(s) match the trigger in 69cdc965d385e3b94310f77e.jsonl:69cdc965d385e3b94310f77e, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[1091] _id=69e0e9947957a33870f51809 ts=2026-04-16T13:52:19.2320000Z`; `69cdc965d385e3b94310f77e.jsonl[1089] _id=69e0e9967957a33870f51817 ts=2026-04-16T13:52:21.5330000Z`; `69cdc965d385e3b94310f77e.jsonl[1131] _id=69e0ea497957a33870f51d05 ts=2026-04-16T13:55:20.3460000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[180] _id=69e0edbb7957a33870f53035 ts=2026-04-16T14:10:02.7090000Z`; `69cdc965d385e3b94310f77e.jsonl[238] _id=69e629381724f0c9e2f852a7 ts=2026-04-20T13:25:10.3260000Z`; `69cdc965d385e3b94310f77e.jsonl[1634] _id=69e629961724f0c9e2f85467 ts=2026-04-20T13:26:44.2940000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[261] _id=69e62c3f1724f0c9e2f86719 ts=2026-04-20T13:38:05.6310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[1762] _id=69e62c161724f0c9e2f865c5 ts=2026-04-20T13:37:24.4060000Z`; `69cdc965d385e3b94310f77e.jsonl[255] _id=69e62c171724f0c9e2f865cf ts=2026-04-20T13:37:25.5850000Z`; `69cdc965d385e3b94310f77e.jsonl[2545] _id=69e8ce031724f0c9e2fa21bb ts=2026-04-22T13:32:50.5500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[324] _id=69e8c9da1724f0c9e2fa09f9 ts=2026-04-22T13:15:06.3090000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f77e.jsonl[1748] _id=69e62c161724f0c9e2f865c7 ts=2026-04-20T13:37:24.4680000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 212 unmatched 'DialogueStartEvent' (totals: 417 start, 209 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 9 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 49 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.92s, min -17.55s, max +0.01s over 3038 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77e\coverage.yaml

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
  - Observed: 98 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2129 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (740); Unit 3 Dev (318); Unit 3 Dungeon Dev (261); Unit 4 Dev (228); Unit 1 Dev (203); Unit 5 Dev (153); Unit 4 Dev - Dungeon (100); Unit 4 Dev - Anderson Base (97); Unit 5 Dev - Dungeon (29)
- **eventKey:** present on 1503 of 2129 records
- **Intervals:** median 1.18s (p5 0.01s / p95 30.12s, n=2128)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1503; [conversationId, dialogueEventType] x626
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2129/2129 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 2129/2129 records)
    "DialogueNodeEvent"  x1503
    "DialogueStartEvent"  x417
    "DialogueFinishEvent"  x209
data.nodeId  (number, 1503/2129 records)
    numeric range 0 .. 290 (234 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 483 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (158); Unit 3 Dungeon Dev (66); Unit 3 Dev (64); Unit 1 Dev (56); Unit 5 Dev - Dungeon (49); Unit 4 Dev (30); Unit 4 Dev - Dungeon (29); Unit 5 Dev (16); Unit 4 Dev - Anderson Base (15)
- **Intervals:** median 30.01s (p5 29.96s / p95 39.90s, n=471)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 483/483 records)
data.position.x  (number, 483/483 records)
    numeric range -695.098 .. 1557.17 (297 unique)
data.position.y  (number, 483/483 records)
    numeric range -115.127 .. 219.581 (250 unique)
data.position.z  (number, 483/483 records)
    numeric range -1112.14 .. 2061.74 (297 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `WaterChamberEvent` — 135 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (135)
- **Intervals:** median 0.72s (p5 0.14s / p95 27.88s, n=134)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 135/135 records)
    "On"  x74
    "Off"  x61
data.floor  (string, 135/135 records)
    "4"  x93
    "3"  x37
    "2"  x3
    "1"  x2
data.machineNumber  (string, 135/135 records)
    "One"  x123
    "Two"  x12
data.machineType  (string, 135/135 records)
    "Condenser"  x90
    "Evaporator"  x37
    "DualChamber_Condenser"  x4
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 135/135 records)
    "3"  x72
    "2"  x37
    "4"  x16
    "1"  x10
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 98 records

- **Scenes:** Unit 2 Prod (Refactor) (64); Unit 3 Dev (34)
- **Intervals:** median 10.42s (p5 0.44s / p95 320.76s, n=97)
- **Fields under `data`:**

```text
data.actionType  (string, 98/98 records)
    "MapCloseEvent"  x50
    "MapOpenEvent"  x48
data.featureUsed  (string, 98/98 records)
    "Map"  x98
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (12); Unit 4 Dev - Dungeon (11); Unit 3 Dev (10); Unit 5 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 107.17s (p5 0.01s / p95 1164.90s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x35
data.questID  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/84 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 24 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (14); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 3.40s (p5 1.11s / p95 2582.47s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "dragEnd"  x12
    "dragStart"  x12
data.featureUsed  (string, 24/24 records)
    "waypoint"  x24
data.location  (object, 24/24 records)
data.location.x  (number, 24/24 records)
    numeric range -770.79 .. 396.686 (13 unique)
data.location.y  (number, 24/24 records)
    numeric range -307.4 .. 254.963 (13 unique)
data.location.z  (number, 24/24 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 23 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 2 Prod (Refactor) (7); Unit 1 Dev (5)
- **Intervals:** median 5.84s (p5 0.88s / p95 165725.78s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "argumentationNodeAdd"  x16
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 23/23 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 2 – Watershed"  x7
    "Unit 1 - Freshwater"  x5
data.nodeName  (string, 23/23 records)
    "1"  x4
    "A"  x4
    "II"  x3
    "2"  x2
    "3"  x2
    "4"  x2
    "D"  x2
    "I"  x2
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (10); Unit 3 Dev (6); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 0.80s (p5 0.01s / p95 189511.41s, n=19)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolClose"  x11
    "argumentationToolOpen"  x9
data.argumentationTitle  (string, 20/20 records)
    "Unit 4 - Flooding"  x10
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x4
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Soil Flow Rates"  x8
    "BackingInfoPanel - "  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 30.68s (p5 2.94s / p95 257170.01s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/12 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/12 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 71.67s (p5 0.60s / p95 258331.21s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 8.50s (p5 0.77s / p95 129.82s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Sand"  x5
    "Gravel"  x3
data.floor  (string, 8/8 records)
    "5"  x7
    "4"  x1
data.machine  (string, 8/8 records)
    "2"  x7
    "1"  x1
data.row  (string, 8/8 records)
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 4 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 170285.49s (p5 392.29s / p95 310836.40s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "4"  x2
    "1"  x1
    "2"  x1
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 4 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (4)
- **Intervals:** median 9.15s (p5 8.77s / p95 9.17s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "cameraPlaced"  x4
data.boxId  (string, 4/4 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 4/4 records)
    "None"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

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
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "dragStart" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*