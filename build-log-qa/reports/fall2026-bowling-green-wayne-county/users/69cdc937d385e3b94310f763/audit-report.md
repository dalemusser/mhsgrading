# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f763

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f763
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f763.jsonl
- **Records:** 2425 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f763
- **Time span:** 2026-04-13T19:24:12.752000+00:00 .. 2026-04-23T20:10:14.817000+00:00 (240h 46m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f763\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2425 records, 9 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 61 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 1597 | 65.86 | 1 | 9 | 1116 | 2026-04-13T19:24:31.474000+00:00 | 2026-04-23T20:06:47.067000+00:00 | 240h 42m |
| PlayerPositionEvent | 547 | 22.56 | 1 | 9 | 0 | 2026-04-13T19:24:12.752000+00:00 | 2026-04-23T20:10:14.817000+00:00 | 240h 46m |
| questEvent | 82 | 3.38 | 1 | 9 | 82 | 2026-04-13T19:24:31.451000+00:00 | 2026-04-23T20:07:13.839000+00:00 | 240h 42m |
| Topographic Map Event | 38 | 1.57 | 1 | 3 | 0 | 2026-04-15T19:21:41.410000+00:00 | 2026-04-17T20:03:41.907000+00:00 | 48h 42m |
| TopographicMapEvent | 38 | 1.57 | 1 | 2 | 0 | 2026-04-15T19:21:51.924000+00:00 | 2026-04-17T20:03:39.836000+00:00 | 48h 41m |
| soilMachine | 26 | 1.07 | 1 | 1 | 0 | 2026-04-21T19:20:12.469000+00:00 | 2026-04-21T19:31:46.394000+00:00 | 11m 33s |
| WaterChamberEvent | 25 | 1.03 | 1 | 1 | 0 | 2026-04-23T19:37:33.260000+00:00 | 2026-04-23T19:43:59.923000+00:00 | 6m 26s |
| argumentationNodeEvent | 21 | 0.87 | 1 | 2 | 0 | 2026-04-13T19:44:56.678000+00:00 | 2026-04-17T19:33:42.040000+00:00 | 95h 48m |
| argumentationToolEvent | 18 | 0.74 | 1 | 3 | 0 | 2026-04-17T19:31:57.628000+00:00 | 2026-04-23T19:53:59.757000+00:00 | 144h 22m |
| Soil Key Puzzle | 13 | 0.54 | 1 | 3 | 0 | 2026-04-13T20:01:39.669000+00:00 | 2026-04-21T18:59:51.919000+00:00 | 190h 58m |
| argumentationEvent | 10 | 0.41 | 1 | 4 | 0 | 2026-04-13T19:44:52.424000+00:00 | 2026-04-23T19:54:23.721000+00:00 | 240h 9m |
| TerasGardenBox | 6 | 0.25 | 1 | 1 | 0 | 2026-04-21T19:53:11.256000+00:00 | 2026-04-21T19:53:53.672000+00:00 | 42.4s |
| EndOfUnit | 4 | 0.16 | 1 | 4 | 0 | 2026-04-13T19:50:07.755000+00:00 | 2026-04-23T20:06:57.327000+00:00 | 240h 16m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 345200.087s median 
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
  - Observed: 230.598s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.798s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 180.829s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.431s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.229s median 
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
  - Observed: 6.207s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
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
  - Observed: 38 records this build 
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
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
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
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
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
- **INFO / Info** `soilMachine` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
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
  - Examples: `69cdc937d385e3b94310f763.jsonl[122] _id=69dd48067957a33870f2a815 ts=2026-04-13T19:46:14.6440000Z`; `69cdc937d385e3b94310f763.jsonl[776] _id=69dfe7127957a33870f47929 ts=2026-04-15T19:29:21.4660000Z`; `69cdc937d385e3b94310f763.jsonl[263] _id=69e28b191724f0c9e2f7b470 ts=2026-04-17T19:33:43.5400000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 38 records, TopographicMapEvent: 38 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1596 | 0.0 | 3.622 | 542.942 | 40.865 | 341121.036 | 0.11 | 399 | 4 |
| PlayerPositionEvent | 534 | 20.934 | 30.005 | 983.477 | 34.352 | 170965.301 | 0.06 | 0 | 3 |
| questEvent | 81 | 0.003 | 156.458 | 10698.301 | 1265.391 | 341303.094 | 0.01 | 16 | 9 |
| Topographic Map Event | 37 | 2.582 | 19.905 | 4738.392 | 1163.481 | 170156.13 | 0.01 | 0 | 4 |
| TopographicMapEvent | 37 | 0.13 | 2.031 | 4738.052 | 1299.894 | 170933.328 | 0.01 | 0 | 3 |
| soilMachine | 25 | 1.012 | 6.207 | 27.757 | 147.875 | 156.04 | 2.16 | 0 | 0 |
| WaterChamberEvent | 24 | 1.508 | 8.798 | 16.111 | 41.934 | 82.969 | 3.72 | 0 | 0 |
| argumentationNodeEvent | 20 | 1.17 | 8.431 | 17246.268 | 17307.035 | 344543.757 | 0.0 | 0 | 1 |
| argumentationToolEvent | 17 | 0.003 | 1.229 | 30571.89 | 207848.239 | 346353.181 | 0.0 | 3 | 2 |
| Soil Key Puzzle | 12 | 2.963 | 230.598 | 57291.021 | 248883.469 | 343302.913 | 0.0 | 0 | 4 |
| argumentationEvent | 9 | 0.087 | 180.829 | 96063.477 | 345580.421 | 346275.297 | 0.0 | 0 | 3 |
| TerasGardenBox | 5 | 1.184 | 2.919 | 8.483 | 20.777 | 22.449 | 7.07 | 0 | 0 |
| EndOfUnit | 3 | 173077.315 | 345200.087 | 288336.524 | 346578.962 | 346732.17 | 0.0 | 0 | 3 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.97s, p95 34.35s, n=534) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `87ms: 69cdc937d385e3b94310f763.jsonl[256] _id=69e28b181724f0c9e2f7b46e ts=2026-04-17T19:33:43.5170000Z ~ 69cdc937d385e3b94310f763.jsonl[258] _id=69e28b191724f0c9e2f7b474 ts=2026-04-17T19:33:43.6040000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc937d385e3b94310f763.jsonl[1929] _id=69e7d3b51724f0c9e2f9eb41 ts=2026-04-21T19:44:53.5760000Z ~ 69cdc937d385e3b94310f763.jsonl[1927] _id=69e7d3b51724f0c9e2f9eb43 ts=2026-04-21T19:44:53.5790000Z`; `992ms: 69cdc937d385e3b94310f763.jsonl[1945] _id=69e7d42a1724f0c9e2f9ec8b ts=2026-04-21T19:46:50.3830000Z ~ 69cdc937d385e3b94310f763.jsonl[1947] _id=69e7d42b1724f0c9e2f9ec8f ts=2026-04-21T19:46:51.3750000Z`; `69ms: 69cdc937d385e3b94310f763.jsonl[2281] _id=69ea78d21724f0c9e2fb6041 ts=2026-04-23T19:53:53.3780000Z ~ 69cdc937d385e3b94310f763.jsonl[2279] _id=69ea78d21724f0c9e2fb6043 ts=2026-04-23T19:53:53.4470000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 69cdc937d385e3b94310f763.jsonl[347] _id=69ea790b1724f0c9e2fb612b ts=2026-04-23T19:54:50.6390000Z ~ 69cdc937d385e3b94310f763.jsonl[348] _id=69ea790c1724f0c9e2fb612f ts=2026-04-23T19:54:50.6510000Z`; `7ms: 69cdc937d385e3b94310f763.jsonl[2346] _id=69ea7a661724f0c9e2fb6569 ts=2026-04-23T20:00:37.7730000Z ~ 69cdc937d385e3b94310f763.jsonl[2349] _id=69ea7a671724f0c9e2fb656d ts=2026-04-23T20:00:37.7800000Z`; `3ms: 69cdc937d385e3b94310f763.jsonl[2418] _id=69ea7bf41724f0c9e2fb6a81 ts=2026-04-23T20:07:13.8360000Z ~ 69cdc937d385e3b94310f763.jsonl[2416] _id=69ea7bf41724f0c9e2fb6a83 ts=2026-04-23T20:07:13.8390000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f763.jsonl[1580] _id=69e7c7c51724f0c9e2f9ad65 ts=2026-04-17T20:08:59.951Z -> 69cdc937d385e3b94310f763.jsonl[1584] _id=69e7c7dd1724f0c9e2f9adc9 ts=2026-04-21T18:54:20.9870000Z; 47h 30m: 69cdc937d385e3b94310f763.jsonl[2137] _id=69e7d82e1724f0c9e2f9fc35 ts=2026-04-21T20:03:58.2690000Z -> 69cdc937d385e3b94310f763.jsonl[2142] _id=69ea74551724f0c9e2fb5543 ts=2026-04-23T19:34:44.3290000Z; 47h 1m: 69cdc937d385e3b94310f763.jsonl[570] _id=69dd4d007957a33870f2bb1f ts=2026-04-13T20:07:27.9660000Z -> 69cdc937d385e3b94310f763.jsonl[579] _id=69dfe2617957a33870f46717 ts=2026-04-15T19:09:20.2930000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 399 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f763.jsonl[1578] _id=69e2935d1724f0c9e2f7db99 ts=2026-04-17T20:08:59.9510000Z -> 69cdc937d385e3b94310f763.jsonl[1580] _id=69e7c7c51724f0c9e2f9ad65 ts=2026-04-17T20:08:59.951Z; 2ms: 69cdc937d385e3b94310f763.jsonl[1354] _id=69e28c381724f0c9e2f7b91e ts=2026-04-17T19:38:31.2280000Z -> 69cdc937d385e3b94310f763.jsonl[1353] _id=69e28c381724f0c9e2f7b920 ts=2026-04-17T19:38:31.2300000Z; 2ms: 69cdc937d385e3b94310f763.jsonl[1469] _id=69e291421724f0c9e2f7d199 ts=2026-04-17T19:59:59.3290000Z -> 69cdc937d385e3b94310f763.jsonl[1470] _id=69e291421724f0c9e2f7d1a1 ts=2026-04-17T19:59:59.3310000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 18m 
  - Evidence: 96h 18m: 69cdc937d385e3b94310f763.jsonl[388] _id=69dd48ef7957a33870f2ac67 ts=2026-04-13T19:50:07.7550000Z -> 69cdc937d385e3b94310f763.jsonl[1579] _id=69e2935d1724f0c9e2f7db95 ts=2026-04-17T20:08:59.9250000Z; 95h 53m: 69cdc937d385e3b94310f763.jsonl[1579] _id=69e2935d1724f0c9e2f7db95 ts=2026-04-17T20:08:59.9250000Z -> 69cdc937d385e3b94310f763.jsonl[2125] _id=69e7d7cc1724f0c9e2f9fb49 ts=2026-04-21T20:02:20.0120000Z; 48h 4m: 69cdc937d385e3b94310f763.jsonl[2125] _id=69e7d7cc1724f0c9e2f9fb49 ts=2026-04-21T20:02:20.0120000Z -> 69cdc937d385e3b94310f763.jsonl[2406] _id=69ea7be21724f0c9e2fb6a4d ts=2026-04-23T20:06:57.3270000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 29m 
  - Evidence: 47h 29m: 69cdc937d385e3b94310f763.jsonl[2139] _id=69e7d8751724f0c9e2f9fdcf ts=2026-04-21T20:05:09.0790000Z -> 69cdc937d385e3b94310f763.jsonl[2144] _id=69ea744b1724f0c9e2fb553d ts=2026-04-23T19:34:34.3800000Z; 46h 59m: 69cdc937d385e3b94310f763.jsonl[574] _id=69dd4da37957a33870f2bca7 ts=2026-04-13T20:10:10.9910000Z -> 69cdc937d385e3b94310f763.jsonl[580] _id=69dfe25c7957a33870f46711 ts=2026-04-15T19:09:15.4490000Z; 46h 40m: 69cdc937d385e3b94310f763.jsonl[229] _id=69dff0357957a33870f49e4f ts=2026-04-15T20:08:21.2940000Z -> 69cdc937d385e3b94310f763.jsonl[1023] _id=69e280921724f0c9e2f78d4c ts=2026-04-17T18:48:49.2910000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 69cdc937d385e3b94310f763.jsonl[1351] _id=69e28c0e1724f0c9e2f7b892 ts=2026-04-17T19:37:49.2330000Z -> 69cdc937d385e3b94310f763.jsonl[1609] _id=69e7c9141724f0c9e2f9b469 ts=2026-04-21T18:59:32.1460000Z; 47h 40m: 69cdc937d385e3b94310f763.jsonl[917] _id=69dfed8c7957a33870f491fb ts=2026-04-15T19:56:59.2220000Z -> 69cdc937d385e3b94310f763.jsonl[1347] _id=69e28bfc1724f0c9e2f7b844 ts=2026-04-17T19:37:30.4190000Z; 47h 13m: 69cdc937d385e3b94310f763.jsonl[522] _id=69dd4ba67957a33870f2b5c7 ts=2026-04-13T20:01:42.6730000Z -> 69cdc937d385e3b94310f763.jsonl[632] _id=69dfe3b17957a33870f46b15 ts=2026-04-15T19:14:56.8880000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 15m 
  - Evidence: 47h 15m: 69cdc937d385e3b94310f763.jsonl[834] _id=69dfe8b77957a33870f47f29 ts=2026-04-15T19:36:22.4480000Z -> 69cdc937d385e3b94310f763.jsonl[1030] _id=69e281641724f0c9e2f78fb0 ts=2026-04-17T18:52:18.5780000Z; 38m 15s: 69cdc937d385e3b94310f763.jsonl[1227] _id=69e288af1724f0c9e2f7ac94 ts=2026-04-17T19:23:26.2950000Z -> 69cdc937d385e3b94310f763.jsonl[1492] _id=69e291a61724f0c9e2f7d340 ts=2026-04-17T20:01:41.5090000Z; 14m 40s: 69cdc937d385e3b94310f763.jsonl[1102] _id=69e285091724f0c9e2f79d7c ts=2026-04-17T19:07:52.1950000Z -> 69cdc937d385e3b94310f763.jsonl[1201] _id=69e2887a1724f0c9e2f7ab8a ts=2026-04-17T19:22:32.7430000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 28m 
  - Evidence: 47h 28m: 69cdc937d385e3b94310f763.jsonl[782] _id=69dfe8aa7957a33870f47ee9 ts=2026-04-15T19:36:09.3050000Z -> 69cdc937d385e3b94310f763.jsonl[1077] _id=69e284601724f0c9e2f79a92 ts=2026-04-17T19:05:02.6330000Z; 38m 25s: 69cdc937d385e3b94310f763.jsonl[1225] _id=69e288ad1724f0c9e2f7ac8e ts=2026-04-17T19:23:23.2970000Z -> 69cdc937d385e3b94310f763.jsonl[1493] _id=69e291ae1724f0c9e2f7d35e ts=2026-04-17T20:01:48.6540000Z; 17m 28s: 69cdc937d385e3b94310f763.jsonl[1074] _id=69e284691724f0c9e2f79aa8 ts=2026-04-17T19:05:11.7880000Z -> 69cdc937d385e3b94310f763.jsonl[1212] _id=69e288811724f0c9e2f7abb4 ts=2026-04-17T19:22:40.3160000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 11m 
  - Evidence: 96h 11m: 69cdc937d385e3b94310f763.jsonl[258] _id=69e28b191724f0c9e2f7b474 ts=2026-04-17T19:33:43.6040000Z -> 69cdc937d385e3b94310f763.jsonl[1928] _id=69e7d3bb1724f0c9e2f9eb51 ts=2026-04-21T19:44:58.9010000Z; 95h 42m: 69cdc937d385e3b94310f763.jsonl[125] _id=69dd48067957a33870f2a813 ts=2026-04-13T19:46:14.6230000Z -> 69cdc937d385e3b94310f763.jsonl[1276] _id=69e289e21724f0c9e2f7b0c8 ts=2026-04-17T19:28:32.7290000Z; 48h 6m: 69cdc937d385e3b94310f763.jsonl[1928] _id=69e7d3bb1724f0c9e2f9eb51 ts=2026-04-21T19:44:58.9010000Z -> 69cdc937d385e3b94310f763.jsonl[2264] _id=69ea783b1724f0c9e2fb5e71 ts=2026-04-23T19:51:22.8920000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 69cdc937d385e3b94310f763.jsonl[113] _id=69dd48047957a33870f2a80d ts=2026-04-13T19:46:12.6340000Z -> 69cdc937d385e3b94310f763.jsonl[1275] _id=69e289e51724f0c9e2f7b0d8 ts=2026-04-17T19:28:36.3910000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc937d385e3b94310f763.jsonl[251] _id=69e28ac51724f0c9e2f7b3ac ts=2026-04-17T19:32:20.3950000Z -> 69cdc937d385e3b94310f763.jsonl[1929] _id=69e7d3b51724f0c9e2f9eb41 ts=2026-04-21T19:44:53.5760000Z; 48h 7m: 69cdc937d385e3b94310f763.jsonl[1947] _id=69e7d42b1724f0c9e2f9ec8f ts=2026-04-21T19:46:51.3750000Z -> 69cdc937d385e3b94310f763.jsonl[2281] _id=69ea78d21724f0c9e2fb6041 ts=2026-04-23T19:53:53.3780000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.047s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f763.jsonl[1929] _id=69e7d3b51724f0c9e2f9eb41 ts=2026-04-21T19:44:53.5760000Z -> 69cdc937d385e3b94310f763.jsonl[1927] _id=69e7d3b51724f0c9e2f9eb43 ts=2026-04-21T19:44:53.5790000Z; 40ms: 69cdc937d385e3b94310f763.jsonl[1301] _id=69e28ab51724f0c9e2f7b392 ts=2026-04-17T19:32:04.3200000Z -> 69cdc937d385e3b94310f763.jsonl[1302] _id=69e28ab51724f0c9e2f7b394 ts=2026-04-17T19:32:04.3600000Z; 47ms: 69cdc937d385e3b94310f763.jsonl[1945] _id=69e7d42a1724f0c9e2f9ec8b ts=2026-04-21T19:46:50.3830000Z -> 69cdc937d385e3b94310f763.jsonl[1946] _id=69e7d42b1724f0c9e2f9ec8d ts=2026-04-21T19:46:50.4300000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 69cdc937d385e3b94310f763.jsonl[1576] _id=69e293541724f0c9e2f7db62 ts=2026-04-17T20:08:50.7220000Z -> 69cdc937d385e3b94310f763.jsonl[1590] _id=69e7c88a1724f0c9e2f9b0f1 ts=2026-04-21T18:57:13.8160000Z; 47h 31m: 69cdc937d385e3b94310f763.jsonl[2128] _id=69e7d7fa1724f0c9e2f9fbcd ts=2026-04-21T20:03:06.4450000Z -> 69cdc937d385e3b94310f763.jsonl[2141] _id=69ea744d1724f0c9e2fb553f ts=2026-04-23T19:34:36.2970000Z; 47h 1m: 69cdc937d385e3b94310f763.jsonl[568] _id=69dd4cfb7957a33870f2bb17 ts=2026-04-13T20:07:23.8940000Z -> 69cdc937d385e3b94310f763.jsonl[584] _id=69dfe25f7957a33870f46715 ts=2026-04-15T19:09:18.5760000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.003s..0.004s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f763.jsonl[2418] _id=69ea7bf41724f0c9e2fb6a81 ts=2026-04-23T20:07:13.8360000Z -> 69cdc937d385e3b94310f763.jsonl[2416] _id=69ea7bf41724f0c9e2fb6a83 ts=2026-04-23T20:07:13.8390000Z; 3ms: 69cdc937d385e3b94310f763.jsonl[99] _id=69dd47717957a33870f2a5d9 ts=2026-04-13T19:43:44.9860000Z -> 69cdc937d385e3b94310f763.jsonl[102] _id=69dd47717957a33870f2a5db ts=2026-04-13T19:43:44.9890000Z; 4ms: 69cdc937d385e3b94310f763.jsonl[16] _id=69dd451b7957a33870f29e3f ts=2026-04-13T19:33:47.4800000Z -> 69cdc937d385e3b94310f763.jsonl[21] _id=69dd451b7957a33870f29e41 ts=2026-04-13T19:33:47.4840000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc937d385e3b94310f763.jsonl:69cdc937d385e3b94310f763, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f763.jsonl[522] _id=69dd4ba67957a33870f2b5c7 ts=2026-04-13T20:01:42.6730000Z`; `69cdc937d385e3b94310f763.jsonl[635] _id=69dfe3b47957a33870f46b1f ts=2026-04-15T19:14:59.8510000Z`; `69cdc937d385e3b94310f763.jsonl[854] _id=69dfe9f57957a33870f483cf ts=2026-04-15T19:41:40.7180000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 38 record(s) match the trigger in 69cdc937d385e3b94310f763.jsonl:69cdc937d385e3b94310f763, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f763.jsonl[705] _id=69dfe5507957a33870f4716b ts=2026-04-15T19:21:51.9240000Z`; `69cdc937d385e3b94310f763.jsonl[708] _id=69dfe5517957a33870f4716d ts=2026-04-15T19:21:52.2520000Z`; `69cdc937d385e3b94310f763.jsonl[732] _id=69dfe6327957a33870f4753d ts=2026-04-15T19:25:37.9920000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f763.jsonl[1125] _id=69e285f21724f0c9e2f7a118 ts=2026-04-17T19:11:44.9210000Z`; `69cdc937d385e3b94310f763.jsonl[237] _id=69e286811724f0c9e2f7a2e0 ts=2026-04-17T19:14:07.9130000Z`; `69cdc937d385e3b94310f763.jsonl[1836] _id=69e7d1761724f0c9e2f9e19d ts=2026-04-21T19:35:18.5520000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f763.jsonl[258] _id=69e28b191724f0c9e2f7b474 ts=2026-04-17T19:33:43.6040000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f763.jsonl[250] _id=69e28ab81724f0c9e2f7b396 ts=2026-04-17T19:32:06.5750000Z`; `69cdc937d385e3b94310f763.jsonl[1929] _id=69e7d3b51724f0c9e2f9eb41 ts=2026-04-21T19:44:53.5760000Z`; `69cdc937d385e3b94310f763.jsonl[1927] _id=69e7d3b51724f0c9e2f9eb43 ts=2026-04-21T19:44:53.5790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f763.jsonl[213] _id=69dfec397957a33870f48c9f ts=2026-04-15T19:51:20.3810000Z`; `69cdc937d385e3b94310f763.jsonl[917] _id=69dfed8c7957a33870f491fb ts=2026-04-15T19:56:59.2220000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f763.jsonl[2279] _id=69ea78d21724f0c9e2fb6043 ts=2026-04-23T19:53:53.4470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 174 unmatched 'DialogueStartEvent' (totals: 326 start, 155 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Started' (totals: 8 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 9 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 51 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.78s, min -341097.30s, max -0.06s over 2425 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f763\coverage.yaml

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
  - Observed: 38 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1597 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (338); Unit 3 Dev (308); Unit 1 Dev (270); Unit 4 Dev (211); Unit 5 Dev (164); Unit 4 Dev - Dungeon (95); Unit 3 Dungeon Dev (90); Unit 4 Dev - Anderson Base (90); Unit 5 Dev - Dungeon (31)
- **eventKey:** present on 1116 of 1597 records
- **Intervals:** median 3.62s (p5 0.01s / p95 40.87s, n=1596)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1116; [conversationId, dialogueEventType] x481
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1597/1597 records)
    numeric range 10 .. 114 (45 unique)
data.dialogueEventType  (string, 1597/1597 records)
    "DialogueNodeEvent"  x1116
    "DialogueStartEvent"  x326
    "DialogueFinishEvent"  x155
data.nodeId  (number, 1116/1597 records)
    numeric range 0 .. 289 (201 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 547 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (125); Unit 1 Dev (91); Unit 3 Dev (87); Unit 4 Dev - Dungeon (58); Unit 4 Dev (57); Unit 5 Dev (51); Unit 3 Dungeon Dev (33); Unit 5 Dev - Dungeon (25); Unit 4 Dev - Anderson Base (20)
- **Intervals:** median 30.00s (p5 29.97s / p95 34.35s, n=534)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 547/547 records)
data.position.x  (number, 547/547 records)
    numeric range -688.528 .. 1556.74 (321 unique)
data.position.y  (number, 547/547 records)
    numeric range -115.114 .. 217.46 (268 unique)
data.position.z  (number, 547/547 records)
    numeric range -1109.31 .. 2118.7 (322 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (20); Unit 2 Prod (Refactor) (15); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 156.46s (p5 0.01s / p95 1265.39s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x51; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x51
    "questFinishEvent"  x31
data.questID  (string, 82/82 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/82 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 38 records

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (14); Unit 1 Dev (2)
- **Intervals:** median 19.91s (p5 4.82s / p95 1163.48s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
data.featureUsed  (string, 38/38 records)
    "Map"  x38
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 38 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (18)
- **Intervals:** median 2.03s (p5 0.23s / p95 1299.89s, n=37)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "dragEnd"  x19
    "dragStart"  x19
data.featureUsed  (string, 38/38 records)
    "waypoint"  x38
data.location  (object, 38/38 records)
data.location.x  (number, 38/38 records)
    numeric range -770.79 .. 299.192 (20 unique)
data.location.y  (number, 38/38 records)
    numeric range -307.4 .. 257.565 (20 unique)
data.location.z  (number, 38/38 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 6.21s (p5 1.05s / p95 147.88s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Clay"  x11
    "Bedrock"  x9
    "Gravel"  x3
    "Sand"  x3
data.floor  (string, 26/26 records)
    "5"  x19
    "4"  x6
    "3"  x1
data.machine  (string, 26/26 records)
    "1"  x24
    "2"  x2
data.row  (string, 26/26 records)
    "TopRow"  x16
    "BottomRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 25 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (25)
- **Intervals:** median 8.80s (p5 1.59s / p95 41.93s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "On"  x18
    "Off"  x7
data.floor  (string, 25/25 records)
    "3"  x14
    "4"  x5
    "2"  x4
    "1"  x2
data.machineNumber  (string, 25/25 records)
    "One"  x24
    "Two"  x1
data.machineType  (string, 25/25 records)
    "Condenser"  x10
    "DualChamber_Evaporator"  x6
    "Evaporator"  x4
    "DualChamber_Condenser"  x3
    "VentSwitch"  x2
data.room  (string, 25/25 records)
    "2"  x14
    "1"  x5
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 21 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (15); Unit 1 Dev (6)
- **Intervals:** median 8.43s (p5 1.34s / p95 17307.04s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 21/21 records)
    "Unit 3 - Pollution Upstream"  x15
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 21/21 records)
    "A"  x6
    "B"  x5
    "5"  x3
    "I"  x3
    "1"  x2
    "II"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 18 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (8); Unit 3 Dev (6); Unit 5 Dev (4)
- **Intervals:** median 1.23s (p5 0.03s / p95 207848.24s, n=17)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationToolClose"  x9
    "argumentationToolOpen"  x9
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x8
    "Unit 3 - Pollution Upstream"  x6
    "Unit 5"  x4
data.toolName  (string, 18/18 records)
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - Evaporation Flow Diagram"  x3
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 13 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 230.60s (p5 2.99s / p95 248883.47s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 13/13 records)
    "Started"  x8
    "Finished"  x5
data.Unit  (string, 13/13 records)
    "Unit 2 Prod (Refactor)"  x9
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 180.83s (p5 9.61s / p95 345580.42s, n=9)
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

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.92s (p5 1.30s / p95 20.78s, n=5)
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
- **Intervals:** median 345200.09s (p5 190289.59s / p95 346578.96s, n=3)
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (9 records)
- `TopographicMapEvent` data.actionType: "dragStart" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)
- `soilMachine` data.canisterType: "Bedrock" (9x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*