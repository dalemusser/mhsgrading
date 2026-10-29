# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f761

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f761
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f761.jsonl
- **Records:** 2204 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f761
- **Time span:** 2026-04-13T19:14:31.360000+00:00 .. 2026-04-21T20:06:03.266000+00:00 (192h 51m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f761\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2204 records, 9 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 68 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 1500 | 68.06 | 1 | 9 | 1028 | 2026-04-13T19:14:49.698000+00:00 | 2026-04-21T20:05:56.530000+00:00 | 192h 51m |
| PlayerPositionEvent | 408 | 18.51 | 1 | 9 | 0 | 2026-04-13T19:14:31.360000+00:00 | 2026-04-21T20:05:35.340000+00:00 | 192h 51m |
| questEvent | 72 | 3.27 | 1 | 9 | 72 | 2026-04-13T19:14:49.657000+00:00 | 2026-04-21T20:04:44.561000+00:00 | 192h 49m |
| WaterChamberEvent | 53 | 2.4 | 1 | 1 | 0 | 2026-04-21T19:45:59.708000+00:00 | 2026-04-21T19:51:19.178000+00:00 | 5m 19s |
| Topographic Map Event | 46 | 2.09 | 1 | 2 | 0 | 2026-04-15T19:56:44.971000+00:00 | 2026-04-17T19:51:55.830000+00:00 | 47h 55m |
| soilMachine | 43 | 1.95 | 1 | 1 | 0 | 2026-04-17T20:09:13.857000+00:00 | 2026-04-21T19:07:55.831000+00:00 | 94h 58m |
| argumentationToolEvent | 20 | 0.91 | 1 | 3 | 0 | 2026-04-17T19:21:19.316000+00:00 | 2026-04-21T19:54:56.841000+00:00 | 96h 33m |
| TopographicMapEvent | 18 | 0.82 | 1 | 2 | 0 | 2026-04-15T19:57:23.380000+00:00 | 2026-04-17T19:51:53.659000+00:00 | 47h 54m |
| argumentationNodeEvent | 14 | 0.64 | 1 | 2 | 0 | 2026-04-15T19:24:17.077000+00:00 | 2026-04-17T19:21:51.246000+00:00 | 47h 57m |
| TerasGardenBox | 10 | 0.45 | 1 | 1 | 0 | 2026-04-21T19:32:56.115000+00:00 | 2026-04-21T19:34:00.668000+00:00 | 1m 4s |
| argumentationEvent | 10 | 0.45 | 1 | 4 | 0 | 2026-04-15T19:24:09.251000+00:00 | 2026-04-21T20:00:08.150000+00:00 | 144h 35m |
| Soil Key Puzzle | 6 | 0.27 | 1 | 3 | 0 | 2026-04-15T20:08:24.154000+00:00 | 2026-04-17T20:02:44.394000+00:00 | 47h 54m |
| EndOfUnit | 4 | 0.18 | 1 | 4 | 0 | 2026-04-15T19:29:36.374000+00:00 | 2026-04-21T20:06:03.266000+00:00 | 144h 36m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 174334.698s median 
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
  - Observed: 1983.664s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.902s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 3.635s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 254.84s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.7s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.366s median 
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
  - Observed: 3.645s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 408 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 46 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
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
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 14 records 
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
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 8.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f761.jsonl[712] _id=69dfe67b7957a33870f476a3 ts=2026-04-15T19:26:50.4560000Z`; `69cdc937d385e3b94310f761.jsonl[155] _id=69dfeace7957a33870f487c5 ts=2026-04-15T19:45:17.1330000Z`; `69cdc937d385e3b94310f761.jsonl[920] _id=69dfee877957a33870f49639 ts=2026-04-15T20:01:10.9040000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 46 records, TopographicMapEvent: 18 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 6 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1499 | 0.0 | 2.078 | 463.153 | 37.996 | 341057.475 | 0.13 | 387 | 3 |
| PlayerPositionEvent | 396 | 28.352 | 30.008 | 1752.067 | 37.605 | 341050.021 | 0.03 | 0 | 3 |
| questEvent | 71 | 0.003 | 126.654 | 9777.393 | 960.033 | 341157.341 | 0.01 | 14 | 6 |
| WaterChamberEvent | 52 | 0.376 | 3.635 | 6.144 | 21.754 | 22.954 | 9.77 | 0 | 0 |
| Topographic Map Event | 45 | 2.456 | 14.464 | 3833.575 | 241.979 | 168638.842 | 0.02 | 0 | 2 |
| soilMachine | 42 | 0.465 | 3.645 | 8140.999 | 106.603 | 341319.402 | 0.01 | 0 | 1 |
| argumentationToolEvent | 19 | 0.002 | 4.366 | 18295.659 | 35923.591 | 345368.323 | 0.0 | 1 | 2 |
| TopographicMapEvent | 17 | 0.361 | 5.902 | 10145.311 | 34550.793 | 171870.589 | 0.01 | 0 | 1 |
| argumentationNodeEvent | 13 | 1.216 | 7.7 | 13281.09 | 69040.232 | 172265.641 | 0.0 | 0 | 1 |
| TerasGardenBox | 9 | 1.248 | 2.245 | 7.173 | 19.586 | 24.153 | 8.37 | 0 | 0 |
| argumentationEvent | 9 | 0.092 | 254.84 | 57839.878 | 276122.562 | 345372.508 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 5 | 18.008 | 1983.664 | 34492.048 | 135022.285 | 168226.306 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 1399.395 | 174334.698 | 173528.964 | 327800.989 | 344852.799 | 0.0 | 0 | 3 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.97s, p95 37.60s, n=396) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `819ms: 69cdc937d385e3b94310f761.jsonl[2039] _id=69e7d4b51724f0c9e2f9ee11 ts=2026-04-21T19:49:08.8370000Z ~ 69cdc937d385e3b94310f761.jsonl[2042] _id=69e7d4b61724f0c9e2f9ee19 ts=2026-04-21T19:49:09.6560000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `92ms: 69cdc937d385e3b94310f761.jsonl[1156] _id=69e288511724f0c9e2f7aa82 ts=2026-04-17T19:21:52.9200000Z ~ 69cdc937d385e3b94310f761.jsonl[297] _id=69e288511724f0c9e2f7aa88 ts=2026-04-17T19:21:53.0120000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc937d385e3b94310f761.jsonl[1778] _id=69e7cd671724f0c9e2f9cde4 ts=2026-04-21T19:17:58.5340000Z ~ 69cdc937d385e3b94310f761.jsonl[1773] _id=69e7cd671724f0c9e2f9cde7 ts=2026-04-21T19:17:58.5360000Z`; `757ms: 69cdc937d385e3b94310f761.jsonl[1785] _id=69e7cda61724f0c9e2f9cf5b ts=2026-04-21T19:19:01.9170000Z ~ 69cdc937d385e3b94310f761.jsonl[456] _id=69e7cda71724f0c9e2f9cf65 ts=2026-04-21T19:19:02.6740000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 69cdc937d385e3b94310f761.jsonl[568] _id=69e7d7531724f0c9e2f9f92b ts=2026-04-21T20:00:18.6650000Z ~ 69cdc937d385e3b94310f761.jsonl[569] _id=69e7d7531724f0c9e2f9f933 ts=2026-04-21T20:00:18.6750000Z`; `8ms: 69cdc937d385e3b94310f761.jsonl[2163] _id=69e7d84c1724f0c9e2f9fcb3 ts=2026-04-21T20:04:27.3270000Z ~ 69cdc937d385e3b94310f761.jsonl[2164] _id=69e7d84c1724f0c9e2f9fcb7 ts=2026-04-21T20:04:27.3350000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `588ms: 69cdc937d385e3b94310f761.jsonl[420] _id=69e2936b1724f0c9e2f7dbf8 ts=2026-04-17T20:09:15.4020000Z ~ 69cdc937d385e3b94310f761.jsonl[1525] _id=69e2936c1724f0c9e2f7dbfa ts=2026-04-17T20:09:15.9900000Z`; `465ms: 69cdc937d385e3b94310f761.jsonl[1526] _id=69e293721724f0c9e2f7dc1a ts=2026-04-17T20:09:22.1390000Z ~ 69cdc937d385e3b94310f761.jsonl[421] _id=69e293721724f0c9e2f7dc1e ts=2026-04-17T20:09:22.6040000Z`; `479ms: 69cdc937d385e3b94310f761.jsonl[1624] _id=69e7c9ad1724f0c9e2f9b6f3 ts=2026-04-21T19:02:04.5140000Z ~ 69cdc937d385e3b94310f761.jsonl[1610] _id=69e7c9ae1724f0c9e2f9b6f7 ts=2026-04-21T19:02:04.9930000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f761.jsonl[1524] _id=69e293641724f0c9e2f7dbce ts=2026-04-17T20:09:08.6110000Z -> 69cdc937d385e3b94310f761.jsonl[1528] _id=69e7c7a71724f0c9e2f9ad1d ts=2026-04-21T18:53:26.0860000Z; 47h 54m: 69cdc937d385e3b94310f761.jsonl[600] _id=69dd40b57957a33870f293d8 ts=2026-04-13T19:15:00.2460000Z -> 69cdc937d385e3b94310f761.jsonl[605] _id=69dfe26d7957a33870f46725 ts=2026-04-15T19:09:32.0480000Z; 46h 40m: 69cdc937d385e3b94310f761.jsonl[971] _id=69dff0417957a33870f49e83 ts=2026-04-15T20:08:32.4510000Z -> 69cdc937d385e3b94310f761.jsonl[976] _id=69e280ae1724f0c9e2f78da2 ts=2026-04-17T18:49:16.3350000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 387 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f761.jsonl[1974] _id=69e7d3341724f0c9e2f9e9b9 ts=2026-04-21T19:42:43.8860000Z -> 69cdc937d385e3b94310f761.jsonl[1994] _id=69e7d3411724f0c9e2f9e9e3 ts=2026-04-21T19:42:43.886Z; 0ms: 69cdc937d385e3b94310f761.jsonl[398] _id=69e2901f1724f0c9e2f7cfa6 ts=2026-04-17T19:55:11.0890000Z -> 69cdc937d385e3b94310f761.jsonl[399] _id=69e2902b1724f0c9e2f7cfb4 ts=2026-04-17T19:55:11.089Z; 1ms: 69cdc937d385e3b94310f761.jsonl[1862] _id=69e7d09a1724f0c9e2f9dbc5 ts=2026-04-21T19:31:37.2100000Z -> 69cdc937d385e3b94310f761.jsonl[1865] _id=69e7d09a1724f0c9e2f9dbc7 ts=2026-04-21T19:31:37.2110000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 47m 
  - Evidence: 95h 47m: 69cdc937d385e3b94310f761.jsonl[397] _id=69e2901f1724f0c9e2f7cfa4 ts=2026-04-17T19:55:11.0720000Z -> 69cdc937d385e3b94310f761.jsonl[506] _id=69e7d3341724f0c9e2f9e9b7 ts=2026-04-21T19:42:43.8710000Z; 48h 25m: 69cdc937d385e3b94310f761.jsonl[739] _id=69dfe7217957a33870f4795d ts=2026-04-15T19:29:36.3740000Z -> 69cdc937d385e3b94310f761.jsonl[397] _id=69e2901f1724f0c9e2f7cfa4 ts=2026-04-17T19:55:11.0720000Z; 23m 19s: 69cdc937d385e3b94310f761.jsonl[506] _id=69e7d3341724f0c9e2f9e9b7 ts=2026-04-21T19:42:43.8710000Z -> 69cdc937d385e3b94310f761.jsonl[591] _id=69e7d8ac1724f0c9e2f9fed1 ts=2026-04-21T20:06:03.2660000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f761.jsonl[1520] _id=69e293601724f0c9e2f7dbae ts=2026-04-17T20:09:03.7710000Z -> 69cdc937d385e3b94310f761.jsonl[1527] _id=69e7c79b1724f0c9e2f9accd ts=2026-04-21T18:53:13.7920000Z; 47h 54m: 69cdc937d385e3b94310f761.jsonl[599] _id=69dd40b87957a33870f293e0 ts=2026-04-13T19:15:03.6210000Z -> 69cdc937d385e3b94310f761.jsonl[601] _id=69dfe25c7957a33870f4670f ts=2026-04-15T19:09:15.4030000Z; 46h 40m: 69cdc937d385e3b94310f761.jsonl[969] _id=69dff0357957a33870f49e4d ts=2026-04-15T20:08:20.5860000Z -> 69cdc937d385e3b94310f761.jsonl[978] _id=69e280aa1724f0c9e2f78d98 ts=2026-04-17T18:49:13.4750000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 46h 43m 
  - Evidence: 46h 43m: 69cdc937d385e3b94310f761.jsonl[235] _id=69dff0397957a33870f49e61 ts=2026-04-15T20:08:24.1540000Z -> 69cdc937d385e3b94310f761.jsonl[987] _id=69e2815b1724f0c9e2f78f9e ts=2026-04-17T18:52:10.4600000Z; 36m 46s: 69cdc937d385e3b94310f761.jsonl[1197] _id=69e289341724f0c9e2f7ae48 ts=2026-04-17T19:25:40.1860000Z -> 69cdc937d385e3b94310f761.jsonl[1477] _id=69e291d21724f0c9e2f7d3e2 ts=2026-04-17T20:02:26.3860000Z; 33m 3s: 69cdc937d385e3b94310f761.jsonl[987] _id=69e2815b1724f0c9e2f78f9e ts=2026-04-17T18:52:10.4600000Z -> 69cdc937d385e3b94310f761.jsonl[1188] _id=69e2891a1724f0c9e2f7adfc ts=2026-04-17T19:25:14.1240000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 50m 
  - Evidence: 46h 50m: 69cdc937d385e3b94310f761.jsonl[230] _id=69dfeffd7957a33870f49cff ts=2026-04-15T20:07:25.1120000Z -> 69cdc937d385e3b94310f761.jsonl[260] _id=69e282bc1724f0c9e2f7946e ts=2026-04-17T18:58:03.9540000Z; 39m 48s: 69cdc937d385e3b94310f761.jsonl[287] _id=69e285ad1724f0c9e2f79ff4 ts=2026-04-17T19:10:37.5230000Z -> 69cdc937d385e3b94310f761.jsonl[1409] _id=69e28f021724f0c9e2f7ca9c ts=2026-04-17T19:50:26.2000000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 44m 
  - Evidence: 47h 44m: 69cdc937d385e3b94310f761.jsonl[961] _id=69dfefa87957a33870f49b6d ts=2026-04-15T20:05:59.6410000Z -> 69cdc937d385e3b94310f761.jsonl[363] _id=69e28f061724f0c9e2f7caae ts=2026-04-17T19:50:30.2300000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 69cdc937d385e3b94310f761.jsonl[297] _id=69e288511724f0c9e2f7aa88 ts=2026-04-17T19:21:53.0120000Z -> 69cdc937d385e3b94310f761.jsonl[1779] _id=69e7cd6e1724f0c9e2f9ce17 ts=2026-04-21T19:18:05.5200000Z; 47h 50m: 69cdc937d385e3b94310f761.jsonl[94] _id=69dfe67b7957a33870f476a1 ts=2026-04-15T19:26:50.4370000Z -> 69cdc937d385e3b94310f761.jsonl[295] _id=69e287521724f0c9e2f7a64e ts=2026-04-17T19:17:38.0800000Z; 36m 46s: 69cdc937d385e3b94310f761.jsonl[1779] _id=69e7cd6e1724f0c9e2f9ce17 ts=2026-04-21T19:18:05.5200000Z -> 69cdc937d385e3b94310f761.jsonl[548] _id=69e7d60d1724f0c9e2f9f3b9 ts=2026-04-21T19:54:52.2820000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 51m 
  - Evidence: 47h 51m: 69cdc937d385e3b94310f761.jsonl[92] _id=69dfe66d7957a33870f4766d ts=2026-04-15T19:26:36.7650000Z -> 69cdc937d385e3b94310f761.jsonl[1140] _id=69e287561724f0c9e2f7a676 ts=2026-04-17T19:17:42.4060000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 69cdc937d385e3b94310f761.jsonl[1160] _id=69e2884e1724f0c9e2f7aa74 ts=2026-04-17T19:21:50.2110000Z -> 69cdc937d385e3b94310f761.jsonl[1778] _id=69e7cd671724f0c9e2f9cde4 ts=2026-04-21T19:17:58.5340000Z; 25m 40s: 69cdc937d385e3b94310f761.jsonl[1834] _id=69e7d0091724f0c9e2f9d8cd ts=2026-04-21T19:29:12.6820000Z -> 69cdc937d385e3b94310f761.jsonl[2100] _id=69e7d60e1724f0c9e2f9f3c3 ts=2026-04-21T19:54:53.5250000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f761.jsonl[1778] _id=69e7cd671724f0c9e2f9cde4 ts=2026-04-21T19:17:58.5340000Z -> 69cdc937d385e3b94310f761.jsonl[1773] _id=69e7cd671724f0c9e2f9cde7 ts=2026-04-21T19:17:58.5360000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f761.jsonl[1512] _id=69e292f71724f0c9e2f7d954 ts=2026-04-17T20:07:18.7440000Z -> 69cdc937d385e3b94310f761.jsonl[1531] _id=69e7c79d1724f0c9e2f9ace5 ts=2026-04-21T18:53:16.0850000Z; 47h 54m: 69cdc937d385e3b94310f761.jsonl[596] _id=69dd40aa7957a33870f293ae ts=2026-04-13T19:14:49.6570000Z -> 69cdc937d385e3b94310f761.jsonl[602] _id=69dfe26d7957a33870f46723 ts=2026-04-15T19:09:32.0360000Z; 46h 41m: 69cdc937d385e3b94310f761.jsonl[967] _id=69dff02c7957a33870f49e15 ts=2026-04-15T20:08:11.8190000Z -> 69cdc937d385e3b94310f761.jsonl[977] _id=69e280b11724f0c9e2f78db2 ts=2026-04-17T18:49:17.6250000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.003s..0.007s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f761.jsonl[69] _id=69dfe5ae7957a33870f472cf ts=2026-04-15T19:23:24.8090000Z -> 69cdc937d385e3b94310f761.jsonl[691] _id=69dfe5ae7957a33870f472d1 ts=2026-04-15T19:23:24.8120000Z; 6ms: 69cdc937d385e3b94310f761.jsonl[2052] _id=69e7d4ec1724f0c9e2f9eedb ts=2026-04-21T19:50:03.9080000Z -> 69cdc937d385e3b94310f761.jsonl[527] _id=69e7d4ec1724f0c9e2f9eedd ts=2026-04-21T19:50:03.9140000Z; 7ms: 69cdc937d385e3b94310f761.jsonl[1546] _id=69e7c8001724f0c9e2f9ae5f ts=2026-04-21T18:54:55.2340000Z -> 69cdc937d385e3b94310f761.jsonl[1548] _id=69e7c8001724f0c9e2f9ae61 ts=2026-04-21T18:54:55.2410000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 69cdc937d385e3b94310f761.jsonl[421] _id=69e293721724f0c9e2f7dc1e ts=2026-04-17T20:09:22.6040000Z -> 69cdc937d385e3b94310f761.jsonl[1579] _id=69e7c8bb1724f0c9e2f9b2bd ts=2026-04-21T18:58:02.0060000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 2 record(s) match the trigger in 69cdc937d385e3b94310f761.jsonl:69cdc937d385e3b94310f761, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f761.jsonl[1197] _id=69e289341724f0c9e2f7ae48 ts=2026-04-17T19:25:40.1860000Z`; `69cdc937d385e3b94310f761.jsonl[1479] _id=69e291e41724f0c9e2f7d414 ts=2026-04-17T20:02:44.3940000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 18 record(s) match the trigger in 69cdc937d385e3b94310f761.jsonl:69cdc937d385e3b94310f761, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f761.jsonl[886] _id=69dfeda47957a33870f4928b ts=2026-04-15T19:57:23.3800000Z`; `69cdc937d385e3b94310f761.jsonl[884] _id=69dfeda47957a33870f4928d ts=2026-04-15T19:57:23.7410000Z`; `69cdc937d385e3b94310f761.jsonl[889] _id=69dfedaa7957a33870f492c5 ts=2026-04-15T19:57:30.0560000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f761.jsonl[1053] _id=69e2846c1724f0c9e2f79abe ts=2026-04-17T19:05:16.4410000Z`; `69cdc937d385e3b94310f761.jsonl[1067] _id=69e284d11724f0c9e2f79c5c ts=2026-04-17T19:06:56.9980000Z`; `69cdc937d385e3b94310f761.jsonl[1695] _id=69e7cb901724f0c9e2f9c29b ts=2026-04-21T19:10:07.3380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f761.jsonl[297] _id=69e288511724f0c9e2f7aa88 ts=2026-04-17T19:21:53.0120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f761.jsonl[1778] _id=69e7cd671724f0c9e2f9cde4 ts=2026-04-21T19:17:58.5340000Z`; `69cdc937d385e3b94310f761.jsonl[1773] _id=69e7cd671724f0c9e2f9cde7 ts=2026-04-21T19:17:58.5360000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f761.jsonl[987] _id=69e2815b1724f0c9e2f78f9e ts=2026-04-17T18:52:10.4600000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 161 unmatched 'DialogueStartEvent' (totals: 315 start, 157 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 4 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 10 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 44 start, 28 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.93s, min -13.28s, max -0.27s over 2204 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f761\coverage.yaml

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
  - Observed: 46 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1500 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (280); Unit 2 Prod (Refactor) (260); Unit 4 Dev (215); Unit 1 Dev (193); Unit 5 Dev (164); Unit 3 Dungeon Dev (155); Unit 4 Dev - Dungeon (116); Unit 4 Dev - Anderson Base (97); Unit 5 Dev - Dungeon (20)
- **eventKey:** present on 1028 of 1500 records
- **Intervals:** median 2.08s (p5 0.01s / p95 38.00s, n=1499)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1028; [conversationId, dialogueEventType] x472
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1500/1500 records)
    numeric range 10 .. 114 (44 unique)
data.dialogueEventType  (string, 1500/1500 records)
    "DialogueNodeEvent"  x1028
    "DialogueStartEvent"  x315
    "DialogueFinishEvent"  x157
data.nodeId  (number, 1028/1500 records)
    numeric range 0 .. 289 (198 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 408 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (82); Unit 3 Dev (72); Unit 4 Dev (49); Unit 3 Dungeon Dev (44); Unit 1 Dev (43); Unit 4 Dev - Dungeon (38); Unit 4 Dev - Anderson Base (35); Unit 5 Dev (28); Unit 5 Dev - Dungeon (17)
- **Intervals:** median 30.01s (p5 29.97s / p95 37.60s, n=396)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 408/408 records)
data.position.x  (number, 408/408 records)
    numeric range -688.516 .. 1555.74 (241 unique)
data.position.y  (number, 408/408 records)
    numeric range -115.127 .. 217.708 (193 unique)
data.position.z  (number, 408/408 records)
    numeric range -1107.66 .. 1722.52 (241 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 72 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (13); Unit 4 Dev - Dungeon (12); Unit 2 Prod (Refactor) (10); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 72 of 72 records
- **Intervals:** median 126.65s (p5 0.01s / p95 960.03s, n=71)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x28
- **Fields under `data`:**

```text
data.questEventType  (string, 72/72 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x28
data.questID  (string, 72/72 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 72/72 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 28/72 records)
    "Succeeded"  x28
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 53 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (53)
- **Intervals:** median 3.64s (p5 0.64s / p95 21.75s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "On"  x32
    "Off"  x21
data.floor  (string, 53/53 records)
    "3"  x31
    "4"  x15
    "2"  x4
    "1"  x3
data.machineNumber  (string, 53/53 records)
    "One"  x52
    "Two"  x1
data.machineType  (string, 53/53 records)
    "Condenser"  x19
    "DualChamber_Condenser"  x12
    "DualChamber_Evaporator"  x10
    "Evaporator"  x10
    "VentSwitch"  x2
data.room  (string, 53/53 records)
    "2"  x31
    "3"  x15
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 46 records

- **Scenes:** Unit 3 Dev (28); Unit 2 Prod (Refactor) (18)
- **Intervals:** median 14.46s (p5 3.85s / p95 241.98s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "MapCloseEvent"  x23
    "MapOpenEvent"  x23
data.featureUsed  (string, 46/46 records)
    "Map"  x46
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 43 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (43)
- **Intervals:** median 3.65s (p5 0.61s / p95 106.60s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "ChangeCanister"  x43
data.canisterType  (string, 43/43 records)
    "Bedrock"  x18
    "Clay"  x16
    "Sand"  x7
    "Gravel"  x2
data.floor  (string, 43/43 records)
    "5"  x34
    "2"  x5
    "3"  x3
    "4"  x1
data.machine  (string, 43/43 records)
    "1"  x42
    "2"  x1
data.row  (string, 43/43 records)
    "TopRow"  x25
    "BottomRow"  x18
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (14); Unit 3 Dev (4); Unit 5 Dev (2)
- **Intervals:** median 4.37s (p5 0.05s / p95 35923.59s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolClose"  x10
    "argumentationToolOpen"  x10
data.argumentationTitle  (string, 20/20 records)
    "Unit 4 - Flooding"  x14
    "Unit 3 - Pollution Upstream"  x4
    "Unit 5"  x2
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x8
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TopographicMapEvent` — 18 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (8)
- **Intervals:** median 5.90s (p5 0.38s / p95 34550.79s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "dragEnd"  x9
    "dragStart"  x9
data.featureUsed  (string, 18/18 records)
    "waypoint"  x18
data.location  (object, 18/18 records)
data.location.x  (number, 18/18 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 18/18 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 18/18 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 14 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (7)
- **Intervals:** median 7.70s (p5 2.55s / p95 69040.23s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationNodeAdd"  x11
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 14/14 records)
    "I"  x5
    "A"  x4
    "II"  x2
    "1"  x1
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 2.25s (p5 1.26s / p95 19.59s, n=9)
- **`data` key-set variants:** [actionType, boxID, soilType] x6; [actionType, boxId, soilType] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "soilSelected"  x6
    "cameraPlaced"  x4
data.boxID  (string, 6/10 records)
    "0"  x4
    "1"  x1
    "2"  x1
data.boxId  (string, 4/10 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 10/10 records)
    "Gravel"  x4
    "Clay"  x3
    "Sand"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 254.84s (p5 16.44s / p95 276122.56s, n=9)
- **Open findings:** 2 — see sections 5-8
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
- **Intervals:** median 1983.66s (p5 19.62s / p95 135022.28s, n=5)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Started"  x4
    "Finished"  x2
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 174334.70s (p5 18692.93s / p95 327800.99s, n=3)
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
- `TopographicMapEvent` data.actionType: "dragStart" (9x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (18x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*