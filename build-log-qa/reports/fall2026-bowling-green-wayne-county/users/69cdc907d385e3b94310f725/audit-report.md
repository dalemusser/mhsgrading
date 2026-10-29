# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f725

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f725
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f725.jsonl
- **Records:** 3564 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f725
- **Time span:** 2026-04-13T17:57:14.238000+00:00 .. 2026-05-03T16:47:26.759000+00:00 (478h 50m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f725\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 3564 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 65 INFO, 0 NOT_TESTED, 58 PASS.
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
| DialogueEvent | 2302 | 64.59 | 1 | 9 | 1637 | 2026-04-13T17:57:33.102000+00:00 | 2026-05-03T16:47:22.661000+00:00 | 478h 49m |
| PlayerPositionEvent | 884 | 24.8 | 1 | 9 | 0 | 2026-04-13T17:57:14.238000+00:00 | 2026-05-03T16:47:26.759000+00:00 | 478h 50m |
| questEvent | 95 | 2.67 | 1 | 9 | 95 | 2026-04-13T17:57:33.061000+00:00 | 2026-05-03T16:46:25.176000+00:00 | 478h 48m |
| WaterChamberEvent | 79 | 2.22 | 1 | 1 | 0 | 2026-05-01T18:00:56.199000+00:00 | 2026-05-03T16:20:21.105000+00:00 | 46h 19m |
| Topographic Map Event | 54 | 1.52 | 1 | 2 | 0 | 2026-04-15T17:50:13.744000+00:00 | 2026-04-23T18:22:24.450000+00:00 | 192h 32m |
| TopographicMapEvent | 41 | 1.15 | 1 | 2 | 0 | 2026-04-15T18:21:13.278000+00:00 | 2026-04-23T18:21:06.436000+00:00 | 191h 59m |
| argumentationToolEvent | 30 | 0.84 | 1 | 3 | 0 | 2026-04-21T17:44:10.030000+00:00 | 2026-05-01T00:31:02.503000+00:00 | 222h 46m |
| argumentationNodeEvent | 21 | 0.59 | 1 | 3 | 0 | 2026-04-13T18:23:40.598000+00:00 | 2026-04-21T18:17:41.649000+00:00 | 191h 54m |
| soilMachine | 21 | 0.59 | 1 | 1 | 0 | 2026-04-29T23:14:18.984000+00:00 | 2026-04-29T23:29:16.544000+00:00 | 14m 57s |
| argumentationEvent | 12 | 0.34 | 1 | 5 | 0 | 2026-04-13T18:23:26.963000+00:00 | 2026-05-03T16:32:19.346000+00:00 | 478h 8m |
| crash | 7 | 0.2 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 6 | 0.17 | 1 | 5 | 0 | 2026-04-13T18:29:42.105000+00:00 | 2026-05-03T16:46:07.337000+00:00 | 478h 16m |
| Soil Key Puzzle | 6 | 0.17 | 1 | 3 | 0 | 2026-04-17T17:55:20.572000+00:00 | 2026-04-23T18:34:39.611000+00:00 | 144h 39m |
| TerasGardenBox | 6 | 0.17 | 1 | 1 | 0 | 2026-05-01T00:38:10.053000+00:00 | 2026-05-01T00:38:55.291000+00:00 | 45.2s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 230413.821s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.678s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 90.794s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.143s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.841s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 155.074s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 12.741s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.045s median 
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
  - Observed: 5.728s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
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
  - Observed: 54 records this build 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 79 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 21 records 
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
  - Observed: 2; 3; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 30 records 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `soilMachine` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:20:111' vs expected 'DialogueNodeEvent:20:33' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f725.jsonl[2072] _id=69dfd8297957a33870f44893 ts=2026-04-15T18:25:45.0870000Z`; `69cdc907d385e3b94310f725.jsonl[213] _id=69e2689f1724f0c9e2f735c8 ts=2026-04-17T17:06:39.2530000Z`; `69cdc907d385e3b94310f725.jsonl[410] _id=69e7b7e91724f0c9e2f94a9b ts=2026-04-21T17:46:16.8270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 54 records, TopographicMapEvent: 41 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2301 | 0.0 | 2.877 | 749.148 | 47.397 | 534159.037 | 0.08 | 540 | 11 |
| PlayerPositionEvent | 872 | 29.891 | 30.678 | 1976.44 | 42.221 | 534149.261 | 0.03 | 0 | 11 |
| questEvent | 94 | 0.003 | 210.615 | 18337.576 | 165750.482 | 534320.965 | 0.0 | 17 | 17 |
| WaterChamberEvent | 78 | 0.006 | 6.841 | 2138.012 | 83.013 | 165395.994 | 0.03 | 1 | 1 |
| Topographic Map Event | 53 | 3.348 | 16.834 | 13077.938 | 68206.755 | 344283.674 | 0.0 | 0 | 7 |
| TopographicMapEvent | 40 | 0.884 | 5.143 | 17279.829 | 167742.37 | 345727.385 | 0.0 | 0 | 5 |
| argumentationToolEvent | 29 | 0.002 | 4.045 | 27655.603 | 1097.003 | 799919.443 | 0.0 | 4 | 2 |
| argumentationNodeEvent | 20 | 2.25 | 12.741 | 34542.053 | 36065.741 | 688776.651 | 0.0 | 0 | 2 |
| soilMachine | 20 | 1.391 | 5.728 | 44.878 | 143.255 | 258.168 | 1.34 | 0 | 0 |
| argumentationEvent | 11 | 0.138 | 155.074 | 156484.762 | 744291.959 | 799891.163 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 5 | 0.0 | 230413.821 | 344357.046 | 676537.453 | 688810.611 | 0.0 | 1 | 4 |
| Soil Key Puzzle | 5 | 23.54 | 90.794 | 104151.808 | 312409.19 | 347145.487 | 0.0 | 0 | 2 |
| TerasGardenBox | 5 | 1.368 | 2.165 | 9.048 | 20.358 | 20.485 | 6.63 | 0 | 0 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f725.jsonl[2639] _id=69e6f3a01724f0c9e2f9107f ts=? == 69cdc907d385e3b94310f725.jsonl[2644] _id=69e7ac611724f0c9e2f91785 ts=?`; `69cdc907d385e3b94310f725.jsonl[1088] _id=69f4e94b1724f0c9e2fdcf1d ts=? == 69cdc907d385e3b94310f725.jsonl[1233] _id=69f772c01724f0c9e2fdf993 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.678s (p5 29.97s, p95 42.22s, n=872) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc907d385e3b94310f725.jsonl[1771] _id=69dd36167957a33870f27f9c ts=2026-04-13T18:29:42.1050000Z ~ 69cdc907d385e3b94310f725.jsonl[1772] _id=69dd36377957a33870f28080 ts=2026-04-13T18:29:42.105Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 69cdc907d385e3b94310f725.jsonl[1224] _id=69f4edc41724f0c9e2fdd11d ts=2026-05-01T18:15:31.3890000Z ~ 69cdc907d385e3b94310f725.jsonl[1219] _id=69f4edc41724f0c9e2fdd11f ts=2026-05-01T18:15:31.3950000Z`; `132ms: 69cdc907d385e3b94310f725.jsonl[1219] _id=69f4edc41724f0c9e2fdd11f ts=2026-05-01T18:15:31.3950000Z ~ 69cdc907d385e3b94310f725.jsonl[1225] _id=69f4edc41724f0c9e2fdd121 ts=2026-05-01T18:15:31.5270000Z`; `497ms: 69cdc907d385e3b94310f725.jsonl[1225] _id=69f4edc41724f0c9e2fdd121 ts=2026-05-01T18:15:31.5270000Z ~ 69cdc907d385e3b94310f725.jsonl[1226] _id=69f4edc41724f0c9e2fdd125 ts=2026-05-01T18:15:32.0240000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `138ms: 69cdc907d385e3b94310f725.jsonl[3060] _id=69e7bf471724f0c9e2f97e45 ts=2026-04-21T18:17:43.7460000Z ~ 69cdc907d385e3b94310f725.jsonl[3058] _id=69e7bf481724f0c9e2f97e4f ts=2026-04-21T18:17:43.8840000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc907d385e3b94310f725.jsonl[843] _id=69f3f3d41724f0c9e2fdbe5b ts=2026-05-01T00:29:08.0250000Z ~ 69cdc907d385e3b94310f725.jsonl[844] _id=69f3f3d41724f0c9e2fdbe5d ts=2026-05-01T00:29:08.0270000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 69cdc907d385e3b94310f725.jsonl[1385] _id=69f778ad1724f0c9e2fdfacb ts=2026-05-03T16:32:44.7960000Z ~ 69cdc907d385e3b94310f725.jsonl[1403] _id=69f778ad1724f0c9e2fdfacd ts=2026-05-03T16:32:44.8030000Z`; `6ms: 69cdc907d385e3b94310f725.jsonl[1457] _id=69f77a4e1724f0c9e2fdfb49 ts=2026-05-03T16:39:41.4980000Z ~ 69cdc907d385e3b94310f725.jsonl[1453] _id=69f77a4e1724f0c9e2fdfb4b ts=2026-05-03T16:39:41.5040000Z`; `3ms: 69cdc907d385e3b94310f725.jsonl[1496] _id=69f77be21724f0c9e2fdfbdd ts=2026-05-03T16:46:25.1730000Z ~ 69cdc907d385e3b94310f725.jsonl[1497] _id=69f77be21724f0c9e2fdfbdf ts=2026-05-03T16:46:25.1760000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 148h 22m 
  - Evidence: 148h 22m: 69cdc907d385e3b94310f725.jsonl[3526] _id=69ea67b01724f0c9e2fb4de1 ts=2026-04-23T18:40:48.2200000Z -> 69cdc907d385e3b94310f725.jsonl[3530] _id=69f28e3f1724f0c9e2fd473d ts=2026-04-29T23:03:27.2570000Z; 94h 18m: 69cdc907d385e3b94310f725.jsonl[2636] _id=69e27e4b1724f0c9e2f78bea ts=2026-04-17T18:39:07.1760000Z -> 69cdc907d385e3b94310f725.jsonl[2642] _id=69e7ac721724f0c9e2f917f5 ts=2026-04-21T16:57:21.9100000Z; 47h 21m: 69cdc907d385e3b94310f725.jsonl[3200] _id=69e7c4451724f0c9e2f9a5c3 ts=2026-04-21T18:39:01.7410000Z -> 69cdc907d385e3b94310f725.jsonl[3205] _id=69ea5e271724f0c9e2fb046b ts=2026-04-23T18:00:05.6200000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 540 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f725.jsonl[505] _id=69ea64cd1724f0c9e2fb3835 ts=2026-04-23T18:28:28.7240000Z -> 69cdc907d385e3b94310f725.jsonl[3457] _id=69ea64e01724f0c9e2fb38f5 ts=2026-04-23T18:28:28.724Z; 2ms: 69cdc907d385e3b94310f725.jsonl[921] _id=69f3f5691724f0c9e2fdbfe3 ts=2026-05-01T00:35:53.0730000Z -> 69cdc907d385e3b94310f725.jsonl[927] _id=69f3f5691724f0c9e2fdbfe9 ts=2026-05-01T00:35:53.0750000Z; 4ms: 69cdc907d385e3b94310f725.jsonl[1626] _id=69dd35667957a33870f27af2 ts=2026-04-13T18:26:46.5540000Z -> 69cdc907d385e3b94310f725.jsonl[1627] _id=69dd35677957a33870f27af4 ts=2026-04-13T18:26:46.5580000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 20m 
  - Evidence: 191h 20m: 69cdc907d385e3b94310f725.jsonl[1772] _id=69dd36377957a33870f28080 ts=2026-04-13T18:29:42.105Z -> 69cdc907d385e3b94310f725.jsonl[3] _id=69e7b8c01724f0c9e2f950b9 ts=2026-04-21T17:49:52.7160000Z; 174h 17m: 69cdc907d385e3b94310f725.jsonl[3454] _id=69ea64cc1724f0c9e2fb3833 ts=2026-04-23T18:28:28.6940000Z -> 69cdc907d385e3b94310f725.jsonl[1063] _id=69f3f7c11724f0c9e2fdc325 ts=2026-05-01T00:45:53.5160000Z; 64h 0m: 69cdc907d385e3b94310f725.jsonl[1063] _id=69f3f7c11724f0c9e2fdc325 ts=2026-05-01T00:45:53.5160000Z -> 69cdc907d385e3b94310f725.jsonl[1535] _id=69f77bd01724f0c9e2fdfbd9 ts=2026-05-03T16:46:07.3370000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f725.jsonl[1771] _id=69dd36167957a33870f27f9c ts=2026-04-13T18:29:42.1050000Z -> 69cdc907d385e3b94310f725.jsonl[1772] _id=69dd36377957a33870f28080 ts=2026-04-13T18:29:42.105Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 148h 22m 
  - Evidence: 148h 22m: 69cdc907d385e3b94310f725.jsonl[3527] _id=69ea67ab1724f0c9e2fb4dbb ts=2026-04-23T18:40:42.7560000Z -> 69cdc907d385e3b94310f725.jsonl[3528] _id=69f28e311724f0c9e2fd4739 ts=2026-04-29T23:03:12.0170000Z; 81h 8m: 69cdc907d385e3b94310f725.jsonl[2637] _id=69e27e731724f0c9e2f78cb2 ts=2026-04-17T18:39:47.0370000Z -> 69cdc907d385e3b94310f725.jsonl[2638] _id=69e6f3871724f0c9e2f9107b ts=2026-04-21T03:48:23.2680000Z; 47h 19m: 69cdc907d385e3b94310f725.jsonl[482] _id=69e7c49b1724f0c9e2f9a784 ts=2026-04-21T18:40:27.6130000Z -> 69cdc907d385e3b94310f725.jsonl[3203] _id=69ea5e241724f0c9e2fb0465 ts=2026-04-23T18:00:03.8910000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 25m 
  - Evidence: 96h 25m: 69cdc907d385e3b94310f725.jsonl[257] _id=69e274631724f0c9e2f75a2a ts=2026-04-17T17:56:51.3660000Z -> 69cdc907d385e3b94310f725.jsonl[3099] _id=69e7c06c1724f0c9e2f987ad ts=2026-04-21T18:22:36.8530000Z; 48h 11m: 69cdc907d385e3b94310f725.jsonl[3100] _id=69e7c0901724f0c9e2f988e5 ts=2026-04-21T18:23:12.0700000Z -> 69cdc907d385e3b94310f725.jsonl[3481] _id=69ea66281724f0c9e2fb437b ts=2026-04-23T18:34:16.0710000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 69cdc907d385e3b94310f725.jsonl[2570] _id=69e279751724f0c9e2f7761a ts=2026-04-17T18:18:29.3380000Z -> 69cdc907d385e3b94310f725.jsonl[2907] _id=69e7ba511724f0c9e2f959c0 ts=2026-04-21T17:56:33.0120000Z; 48h 11m: 69cdc907d385e3b94310f725.jsonl[2984] _id=69e7bce71724f0c9e2f96dab ts=2026-04-21T18:07:35.5000000Z -> 69cdc907d385e3b94310f725.jsonl[3373] _id=69ea629b1724f0c9e2fb2860 ts=2026-04-23T18:19:07.0950000Z; 46h 30m: 69cdc907d385e3b94310f725.jsonl[152] _id=69dfda1d7957a33870f4574d ts=2026-04-15T18:34:04.6060000Z -> 69cdc907d385e3b94310f725.jsonl[2275] _id=69e268101724f0c9e2f73141 ts=2026-04-17T17:04:15.3780000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 69cdc907d385e3b94310f725.jsonl[2418] _id=69e273511724f0c9e2f7531a ts=2026-04-17T17:52:17.1310000Z -> 69cdc907d385e3b94310f725.jsonl[2892] _id=69e7b9d01724f0c9e2f9561b ts=2026-04-21T17:54:24.5160000Z; 48h 19m: 69cdc907d385e3b94310f725.jsonl[2933] _id=69e7bb1a1724f0c9e2f9602d ts=2026-04-21T17:59:54.5720000Z -> 69cdc907d385e3b94310f725.jsonl[3374] _id=69ea62a01724f0c9e2fb288f ts=2026-04-23T18:19:12.6020000Z; 46h 30m: 69cdc907d385e3b94310f725.jsonl[2137] _id=69dfda1c7957a33870f4573f ts=2026-04-15T18:34:03.3800000Z -> 69cdc907d385e3b94310f725.jsonl[2276] _id=69e268131724f0c9e2f73190 ts=2026-04-17T17:04:18.6100000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 45h 56m 
  - Evidence: 45h 56m: 69cdc907d385e3b94310f725.jsonl[1226] _id=69f4edc41724f0c9e2fdd125 ts=2026-05-01T18:15:32.0240000Z -> 69cdc907d385e3b94310f725.jsonl[1250] _id=69f773d91724f0c9e2fdf9b5 ts=2026-05-03T16:12:08.0180000Z
- **INFO / Info** `WaterChamberEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 69cdc907d385e3b94310f725.jsonl[1224] _id=69f4edc41724f0c9e2fdd11d ts=2026-05-01T18:15:31.3890000Z -> 69cdc907d385e3b94310f725.jsonl[1219] _id=69f4edc41724f0c9e2fdd11f ts=2026-05-01T18:15:31.3950000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 222h 11m 
  - Evidence: 222h 11m: 69cdc907d385e3b94310f725.jsonl[3058] _id=69e7bf481724f0c9e2f97e4f ts=2026-04-21T18:17:43.8840000Z -> 69cdc907d385e3b94310f725.jsonl[850] _id=69f3f3db1724f0c9e2fdbe5f ts=2026-05-01T00:29:15.0470000Z; 191h 18m: 69cdc907d385e3b94310f725.jsonl[1731] _id=69dd35197957a33870f278ae ts=2026-04-13T18:25:28.9620000Z -> 69cdc907d385e3b94310f725.jsonl[405] _id=69e7b74d1724f0c9e2f94667 ts=2026-04-21T17:43:41.7180000Z; 64h 1m: 69cdc907d385e3b94310f725.jsonl[850] _id=69f3f3db1724f0c9e2fdbe5f ts=2026-05-01T00:29:15.0470000Z -> 69cdc907d385e3b94310f725.jsonl[1375] _id=69f7783c1724f0c9e2fdfaa5 ts=2026-05-03T16:30:51.8550000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 19m 
  - Evidence: 191h 19m: 69cdc907d385e3b94310f725.jsonl[1732] _id=69dd35137957a33870f27870 ts=2026-04-13T18:25:23.1590000Z -> 69cdc907d385e3b94310f725.jsonl[2809] _id=69e7b79b1724f0c9e2f94837 ts=2026-04-21T17:44:59.8100000Z; 28m 32s: 69cdc907d385e3b94310f725.jsonl[2822] _id=69e7b7e11724f0c9e2f94a65 ts=2026-04-21T17:46:09.2260000Z -> 69cdc907d385e3b94310f725.jsonl[3034] _id=69e7be911724f0c9e2f9789d ts=2026-04-21T18:14:41.7610000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 222h 11m 
  - Evidence: 222h 11m: 69cdc907d385e3b94310f725.jsonl[3054] _id=69e7bf241724f0c9e2f97d29 ts=2026-04-21T18:17:08.5820000Z -> 69cdc907d385e3b94310f725.jsonl[843] _id=69f3f3d41724f0c9e2fdbe5b ts=2026-05-01T00:29:08.0250000Z; 28m 50s: 69cdc907d385e3b94310f725.jsonl[2814] _id=69e7b7b51724f0c9e2f948ef ts=2026-04-21T17:45:25.2620000Z -> 69cdc907d385e3b94310f725.jsonl[450] _id=69e7be771724f0c9e2f977f1 ts=2026-04-21T18:14:15.5980000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.017s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f725.jsonl[843] _id=69f3f3d41724f0c9e2fdbe5b ts=2026-05-01T00:29:08.0250000Z -> 69cdc907d385e3b94310f725.jsonl[844] _id=69f3f3d41724f0c9e2fdbe5d ts=2026-05-01T00:29:08.0270000Z; 10ms: 69cdc907d385e3b94310f725.jsonl[855] _id=69f3f4421724f0c9e2fdbe81 ts=2026-05-01T00:30:57.7220000Z -> 69cdc907d385e3b94310f725.jsonl[856] _id=69f3f4421724f0c9e2fdbe83 ts=2026-05-01T00:30:57.7320000Z; 17ms: 69cdc907d385e3b94310f725.jsonl[3053] _id=69e7bf211724f0c9e2f97d17 ts=2026-04-21T18:17:05.1530000Z -> 69cdc907d385e3b94310f725.jsonl[3036] _id=69e7bf211724f0c9e2f97d19 ts=2026-04-21T18:17:05.1700000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 148h 25m 
  - Evidence: 148h 25m: 69cdc907d385e3b94310f725.jsonl[3504] _id=69ea67011724f0c9e2fb4987 ts=2026-04-23T18:37:53.6020000Z -> 69cdc907d385e3b94310f725.jsonl[3529] _id=69f28e331724f0c9e2fd473b ts=2026-04-29T23:03:14.5670000Z; 81h 36m: 69cdc907d385e3b94310f725.jsonl[262] _id=69e277fb1724f0c9e2f76e8e ts=2026-04-17T18:12:10.6000000Z -> 69cdc907d385e3b94310f725.jsonl[359] _id=69e6f38d1724f0c9e2f9107d ts=2026-04-21T03:48:28.9000000Z; 47h 36m: 69cdc907d385e3b94310f725.jsonl[3108] _id=69e7c0b61724f0c9e2f98a91 ts=2026-04-21T18:23:50.8820000Z -> 69cdc907d385e3b94310f725.jsonl[3204] _id=69ea5e261724f0c9e2fb0469 ts=2026-04-23T18:00:05.3550000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.003s..0.007s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f725.jsonl[1496] _id=69f77be21724f0c9e2fdfbdd ts=2026-05-03T16:46:25.1730000Z -> 69cdc907d385e3b94310f725.jsonl[1497] _id=69f77be21724f0c9e2fdfbdf ts=2026-05-03T16:46:25.1760000Z; 6ms: 69cdc907d385e3b94310f725.jsonl[1457] _id=69f77a4e1724f0c9e2fdfb49 ts=2026-05-03T16:39:41.4980000Z -> 69cdc907d385e3b94310f725.jsonl[1453] _id=69f77a4e1724f0c9e2fdfb4b ts=2026-05-03T16:39:41.5040000Z; 7ms: 69cdc907d385e3b94310f725.jsonl[1385] _id=69f778ad1724f0c9e2fdfacb ts=2026-05-03T16:32:44.7960000Z -> 69cdc907d385e3b94310f725.jsonl[1403] _id=69f778ad1724f0c9e2fdfacd ts=2026-05-03T16:32:44.8030000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f725.jsonl:69cdc907d385e3b94310f725, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f725.jsonl[257] _id=69e274631724f0c9e2f75a2a ts=2026-04-17T17:56:51.3660000Z`; `69cdc907d385e3b94310f725.jsonl[3100] _id=69e7c0901724f0c9e2f988e5 ts=2026-04-21T18:23:12.0700000Z`; `69cdc907d385e3b94310f725.jsonl[3483] _id=69ea663f1724f0c9e2fb444d ts=2026-04-23T18:34:39.6110000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 41 record(s) match the trigger in 69cdc907d385e3b94310f725.jsonl:69cdc907d385e3b94310f725, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f725.jsonl[2028] _id=69dfd7197957a33870f4416f ts=2026-04-15T18:21:13.2780000Z`; `69cdc907d385e3b94310f725.jsonl[2136] _id=69dfda177957a33870f4571b ts=2026-04-15T18:33:58.4130000Z`; `69cdc907d385e3b94310f725.jsonl[2137] _id=69dfda1c7957a33870f4573f ts=2026-04-15T18:34:03.3800000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f725.jsonl[2534] _id=69e2785a1724f0c9e2f7709a ts=2026-04-17T18:13:46.1280000Z`; `69cdc907d385e3b94310f725.jsonl[2949] _id=69e7bb661724f0c9e2f9628b ts=2026-04-21T18:01:10.3520000Z`; `69cdc907d385e3b94310f725.jsonl[2976] _id=69e7bc261724f0c9e2f96821 ts=2026-04-21T18:04:21.6400000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f725.jsonl[3058] _id=69e7bf481724f0c9e2f97e4f ts=2026-04-21T18:17:43.8840000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f725.jsonl[3015] _id=69e7be841724f0c9e2f97849 ts=2026-04-21T18:14:28.1710000Z`; `69cdc907d385e3b94310f725.jsonl[843] _id=69f3f3d41724f0c9e2fdbe5b ts=2026-05-01T00:29:08.0250000Z`; `69cdc907d385e3b94310f725.jsonl[844] _id=69f3f3d41724f0c9e2fdbe5d ts=2026-05-01T00:29:08.0270000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 7 records 
  - Examples: `69cdc907d385e3b94310f725.jsonl[2639] _id=69e6f3a01724f0c9e2f9107f ts=?`; `69cdc907d385e3b94310f725.jsonl[2644] _id=69e7ac611724f0c9e2f91785 ts=?`; `69cdc907d385e3b94310f725.jsonl[3455] _id=69ea64ce1724f0c9e2fb384b ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 231 unmatched 'DialogueStartEvent' (totals: 446 start, 219 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 14 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 57 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.50s, min -33.58s, max +0.04s over 3557 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f725\coverage.yaml

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
  - Observed: 54 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 7 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2302 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (943); Unit 3 Dev (263); Unit 4 Dev (213); Unit 1 Dev (206); Unit 5 Dev (184); Unit 3 Dungeon Dev (179); Unit 4 Dev - Dungeon (134); Unit 4 Dev - Anderson Base (91); Unit 5 Dev - Dungeon (89)
- **eventKey:** present on 1637 of 2302 records
- **Intervals:** median 2.88s (p5 0.01s / p95 47.40s, n=2301)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1637; [conversationId, dialogueEventType] x665
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2302/2302 records)
    numeric range 8 .. 114 (51 unique)
data.dialogueEventType  (string, 2302/2302 records)
    "DialogueNodeEvent"  x1637
    "DialogueStartEvent"  x446
    "DialogueFinishEvent"  x219
data.nodeId  (number, 1637/2302 records)
    numeric range 0 .. 290 (234 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 884 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (400); Unit 3 Dev (84); Unit 5 Dev - Dungeon (72); Unit 3 Dungeon Dev (68); Unit 1 Dev (65); Unit 4 Dev - Dungeon (62); Unit 4 Dev (59); Unit 5 Dev (51); Unit 4 Dev - Anderson Base (23)
- **Intervals:** median 30.68s (p5 29.97s / p95 42.22s, n=872)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 884/884 records)
data.position.x  (number, 884/884 records)
    numeric range -597.445 .. 1557.91 (438 unique)
data.position.y  (number, 884/884 records)
    numeric range -114.326 .. 219.291 (321 unique)
data.position.z  (number, 884/884 records)
    numeric range -1120.78 .. 1957.93 (438 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 95 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 5 Dev - Dungeon (15); Unit 1 Dev (12); Unit 4 Dev - Dungeon (10); Unit 3 Dev (9); Unit 4 Dev (9); Unit 5 Dev (9); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 95 of 95 records
- **Intervals:** median 210.61s (p5 0.01s / p95 165750.48s, n=94)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Fields under `data`:**

```text
data.questEventType  (string, 95/95 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x38
data.questID  (string, 95/95 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 95/95 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/95 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 79 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (79)
- **Intervals:** median 6.84s (p5 0.19s / p95 83.01s, n=78)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 79/79 records)
    "On"  x52
    "Off"  x27
data.floor  (string, 79/79 records)
    "4"  x36
    "3"  x26
    "2"  x10
    "1"  x7
data.machineNumber  (string, 79/79 records)
    "One"  x77
    "Two"  x2
data.machineType  (string, 79/79 records)
    "Condenser"  x43
    "Evaporator"  x19
    "DualChamber_Evaporator"  x8
    "DualChamber_Condenser"  x6
    "VentSwitch"  x3
data.room  (string, 79/79 records)
    "3"  x35
    "2"  x28
    "1"  x10
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 54 records

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (20)
- **Intervals:** median 16.83s (p5 5.07s / p95 68206.75s, n=53)
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "MapCloseEvent"  x27
    "MapOpenEvent"  x27
data.featureUsed  (string, 54/54 records)
    "Map"  x54
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 41 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (17)
- **Intervals:** median 5.14s (p5 1.43s / p95 167742.37s, n=40)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "dragStart"  x21
    "dragEnd"  x20
data.featureUsed  (string, 41/41 records)
    "waypoint"  x41
data.location  (object, 41/41 records)
data.location.x  (number, 41/41 records)
    numeric range -779.225 .. 120.555 (20 unique)
data.location.y  (number, 41/41 records)
    numeric range -315.836 .. 152.331 (21 unique)
data.location.z  (number, 41/41 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 30 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (10); Unit 4 Dev - Anderson Base (6)
- **Intervals:** median 4.04s (p5 0.01s / p95 1097.00s, n=29)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "argumentationToolClose"  x16
    "argumentationToolOpen"  x14
data.argumentationTitle  (string, 30/30 records)
    "Unit 2 – Watershed"  x14
    "Unit 3 - Pollution Upstream"  x10
    "Unit 4 - Flooding"  x6
data.toolName  (string, 30/30 records)
    "BackingInfoPanel - Waterfall Data"  x12
    "BackingInfoPanel - Pollution Site Data"  x8
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationNodeEvent` — 21 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (5); Unit 2 Prod (Refactor) (5)
- **Intervals:** median 12.74s (p5 2.27s / p95 36065.74s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 21/21 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 2 – Watershed"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 21/21 records)
    "1"  x6
    "A"  x4
    "I"  x4
    "B"  x3
    "4"  x2
    "5"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 5.73s (p5 2.03s / p95 143.26s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Bedrock"  x8
    "Clay"  x5
    "Gravel"  x4
    "Sand"  x4
data.floor  (string, 21/21 records)
    "5"  x11
    "3"  x8
    "4"  x2
data.machine  (string, 21/21 records)
    "1"  x19
    "2"  x2
data.row  (string, 21/21 records)
    "TopRow"  x17
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 155.07s (p5 19.05s / p95 744291.96s, n=11)
- **Open findings:** 2 — see sections 5-8
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

### `crash` — 7 records

- **Scenes:** <missing sceneName> (7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 7/7 records)
    true  x7
data.message  (string, 7/7 records)
    "Uncaught ReferenceError: onResize is not defined"  x5
    "Cannot close a closed AudioContext."  x2
data.phase  (string, 7/7 records)
    "running"  x7
data.stack  (string, 7/7 records, 2 empty-string)
    ""  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit2:831:9)"  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit5:831:9)"  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x1
data.type  (string, 7/7 records)
    "runtime_error"  x5
    "unhandled_rejection"  x2
data.unitId  (string, 7/7 records)
    "unit2"  x2
    "unit4"  x2
    "unit5"  x2
    "unit3"  x1
data.workspace  (string, 7/7 records)
    "mhs"  x7
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 230413.82s (p5 35023.20s / p95 676537.45s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "1"  x2
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 90.79s (p5 25.88s / p95 312409.19s, n=5)
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
- **Intervals:** median 2.17s (p5 1.37s / p95 20.36s, n=5)
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
- `crash` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)
- `soilMachine` data.canisterType: "Bedrock" (8x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*