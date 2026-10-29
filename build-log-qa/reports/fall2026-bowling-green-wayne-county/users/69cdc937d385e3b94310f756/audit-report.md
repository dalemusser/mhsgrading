# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f756

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f756
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f756.jsonl
- **Records:** 2673 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f756
- **Time span:** 2026-04-13T19:15:42.353000+00:00 .. 2026-04-21T19:42:45.402000+00:00 (192h 27m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f756\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2673 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 71 INFO, 0 NOT_TESTED, 55 PASS.
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
| DialogueEvent | 1936 | 72.43 | 1 | 9 | 1372 | 2026-04-13T19:16:00.467000+00:00 | 2026-04-21T19:42:38.753000+00:00 | 192h 26m |
| PlayerPositionEvent | 427 | 15.97 | 1 | 9 | 0 | 2026-04-13T19:15:42.353000+00:00 | 2026-04-21T19:42:42.718000+00:00 | 192h 27m |
| questEvent | 113 | 4.23 | 1 | 9 | 113 | 2026-04-13T19:16:00.444000+00:00 | 2026-04-21T19:42:07.086000+00:00 | 192h 26m |
| WaterChamberEvent | 41 | 1.53 | 1 | 1 | 0 | 2026-04-21T19:20:32.822000+00:00 | 2026-04-21T19:27:41.615000+00:00 | 7m 8s |
| soilMachine | 32 | 1.2 | 1 | 1 | 0 | 2026-04-17T20:08:14.975000+00:00 | 2026-04-21T19:01:13.112000+00:00 | 94h 52m |
| Topographic Map Event | 28 | 1.05 | 1 | 2 | 0 | 2026-04-13T19:47:52.522000+00:00 | 2026-04-17T19:46:28.084000+00:00 | 95h 58m |
| argumentationToolEvent | 22 | 0.82 | 1 | 2 | 0 | 2026-04-17T19:21:03.074000+00:00 | 2026-04-21T19:12:25.247000+00:00 | 95h 51m |
| argumentationEvent | 18 | 0.67 | 1 | 4 | 0 | 2026-04-13T19:29:26.105000+00:00 | 2026-04-21T19:32:32.836000+00:00 | 192h 3m |
| Soil Key Puzzle | 16 | 0.6 | 1 | 3 | 0 | 2026-04-13T19:43:34.291000+00:00 | 2026-04-17T19:59:15.331000+00:00 | 96h 15m |
| argumentationNodeEvent | 16 | 0.6 | 1 | 2 | 0 | 2026-04-13T19:29:59.489000+00:00 | 2026-04-17T19:21:41.489000+00:00 | 95h 51m |
| TopographicMapEvent | 11 | 0.41 | 1 | 2 | 0 | 2026-04-13T19:47:58.330000+00:00 | 2026-04-17T19:46:26.415000+00:00 | 95h 58m |
| EndOfUnit | 7 | 0.26 | 1 | 4 | 0 | 2026-04-13T19:32:58.544000+00:00 | 2026-04-21T19:42:45.402000+00:00 | 192h 9m |
| TerasGardenBox | 6 | 0.22 | 1 | 1 | 0 | 2026-04-21T19:14:18.022000+00:00 | 2026-04-21T19:14:37.883000+00:00 | 19.9s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 0.83s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.011s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 239.026s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 0.181s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.798s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.332s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 25.046s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.14s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.148s median 
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
  - Observed: 3.239s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 427 records 
  - Expected: 1304 in 09-23-26 
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
  - Observed: 28 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
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
  - Observed: 16 records 
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
  - Observed: 2; 3; C; D; II 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.4x vs baseline. 
  - Observed: 32 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 94 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f756.jsonl[323] _id=69dd44457957a33870f29ab2 ts=2026-04-13T19:30:12.6620000Z`; `69cdc937d385e3b94310f756.jsonl[2220] _id=69dd48d07957a33870f2abf9 ts=2026-04-13T19:49:36.0910000Z`; `69cdc937d385e3b94310f756.jsonl[586] _id=69dfeea17957a33870f4969f ts=2026-04-15T20:01:37.8200000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 28 records, TopographicMapEvent: 11 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1935 | 0.0 | 0.83 | 358.035 | 27.52 | 341043.953 | 0.17 | 455 | 5 |
| PlayerPositionEvent | 414 | 17.389 | 30.011 | 1671.798 | 61.663 | 341059.781 | 0.04 | 0 | 3 |
| questEvent | 112 | 0.002 | 83.205 | 6185.416 | 697.877 | 341043.93 | 0.01 | 20 | 7 |
| WaterChamberEvent | 40 | 0.516 | 4.332 | 10.72 | 32.738 | 115.763 | 5.6 | 0 | 0 |
| soilMachine | 31 | 0.059 | 3.239 | 11018.65 | 110.727 | 341163.652 | 0.01 | 0 | 1 |
| Topographic Map Event | 27 | 1.843 | 28.601 | 12796.873 | 119495.482 | 171202.7 | 0.0 | 0 | 4 |
| argumentationToolEvent | 21 | 0.002 | 1.148 | 16432.484 | 238.765 | 344808.314 | 0.0 | 3 | 1 |
| argumentationEvent | 17 | 0.105 | 25.046 | 40669.808 | 209012.208 | 344787.249 | 0.0 | 0 | 5 |
| Soil Key Puzzle | 15 | 3.01 | 239.026 | 23102.736 | 170097.483 | 170948.476 | 0.0 | 0 | 5 |
| argumentationNodeEvent | 15 | 1.368 | 6.14 | 23006.8 | 170161.497 | 175106.694 | 0.0 | 0 | 3 |
| TopographicMapEvent | 10 | 0.382 | 10.798 | 34550.808 | 189638.547 | 343748.809 | 0.0 | 0 | 2 |
| EndOfUnit | 6 | 0.0 | 2397.584 | 115297.81 | 343483.644 | 343603.064 | 0.0 | 1 | 4 |
| TerasGardenBox | 5 | 0.124 | 0.181 | 3.972 | 10.432 | 10.928 | 15.1 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.011s (p5 29.96s, p95 61.66s, n=414) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc937d385e3b94310f756.jsonl[2660] _id=69e7cd231724f0c9e2f9ccad ts=2026-04-21T19:16:51.2170000Z ~ 69cdc937d385e3b94310f756.jsonl[1763] _id=69e7cd311724f0c9e2f9cce9 ts=2026-04-21T19:16:51.217Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `180ms: 69cdc937d385e3b94310f756.jsonl[1652] _id=69e7cc9d1724f0c9e2f9c90b ts=2026-04-21T19:14:37.3980000Z ~ 69cdc937d385e3b94310f756.jsonl[1728] _id=69e7cc9d1724f0c9e2f9c90d ts=2026-04-21T19:14:37.5780000Z`; `181ms: 69cdc937d385e3b94310f756.jsonl[1728] _id=69e7cc9d1724f0c9e2f9c90d ts=2026-04-21T19:14:37.5780000Z ~ 69cdc937d385e3b94310f756.jsonl[1653] _id=69e7cc9d1724f0c9e2f9c90f ts=2026-04-21T19:14:37.7590000Z`; `124ms: 69cdc937d385e3b94310f756.jsonl[1653] _id=69e7cc9d1724f0c9e2f9c90f ts=2026-04-21T19:14:37.7590000Z ~ 69cdc937d385e3b94310f756.jsonl[1729] _id=69e7cc9e1724f0c9e2f9c911 ts=2026-04-21T19:14:37.8830000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `598ms: 69cdc937d385e3b94310f756.jsonl[812] _id=69e280a71724f0c9e2f78d76 ts=2026-04-17T18:49:09.3800000Z ~ 69cdc937d385e3b94310f756.jsonl[815] _id=69e280a71724f0c9e2f78d82 ts=2026-04-17T18:49:09.9780000Z`; `105ms: 69cdc937d385e3b94310f756.jsonl[1138] _id=69e288471724f0c9e2f7aa4b ts=2026-04-17T19:21:43.1110000Z ~ 69cdc937d385e3b94310f756.jsonl[1115] _id=69e288471724f0c9e2f7aa54 ts=2026-04-17T19:21:43.2160000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `685ms: 69cdc937d385e3b94310f756.jsonl[1114] _id=69e288231724f0c9e2f7a9be ts=2026-04-17T19:21:06.2940000Z ~ 69cdc937d385e3b94310f756.jsonl[1120] _id=69e288231724f0c9e2f7a9c2 ts=2026-04-17T19:21:06.9790000Z`; `2ms: 69cdc937d385e3b94310f756.jsonl[1601] _id=69e7cb1a1724f0c9e2f9bfcd ts=2026-04-21T19:08:10.3200000Z ~ 69cdc937d385e3b94310f756.jsonl[1602] _id=69e7cb1a1724f0c9e2f9bfd1 ts=2026-04-21T19:08:10.3220000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 69cdc937d385e3b94310f756.jsonl[1957] _id=69e7d0d91724f0c9e2f9dda3 ts=2026-04-21T19:32:41.7590000Z ~ 69cdc937d385e3b94310f756.jsonl[1958] _id=69e7d0da1724f0c9e2f9dda9 ts=2026-04-21T19:32:41.7650000Z`; `8ms: 69cdc937d385e3b94310f756.jsonl[2010] _id=69e7d1de1724f0c9e2f9e3a3 ts=2026-04-21T19:37:02.8190000Z ~ 69cdc937d385e3b94310f756.jsonl[2004] _id=69e7d1df1724f0c9e2f9e3a5 ts=2026-04-21T19:37:02.8270000Z`; `2ms: 69cdc937d385e3b94310f756.jsonl[2068] _id=69e7d2391724f0c9e2f9e56b ts=2026-04-21T19:38:32.0750000Z ~ 69cdc937d385e3b94310f756.jsonl[2069] _id=69e7d2391724f0c9e2f9e56d ts=2026-04-21T19:38:32.0770000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `554ms: 69cdc937d385e3b94310f756.jsonl[2411] _id=69e293321724f0c9e2f7dac4 ts=2026-04-17T20:08:18.0170000Z ~ 69cdc937d385e3b94310f756.jsonl[1488] _id=69e293321724f0c9e2f7daca ts=2026-04-17T20:08:18.5710000Z`; `882ms: 69cdc937d385e3b94310f756.jsonl[1488] _id=69e293321724f0c9e2f7daca ts=2026-04-17T20:08:18.5710000Z ~ 69cdc937d385e3b94310f756.jsonl[1489] _id=69e293331724f0c9e2f7dace ts=2026-04-17T20:08:19.4530000Z`; `233ms: 69cdc937d385e3b94310f756.jsonl[1489] _id=69e293331724f0c9e2f7dace ts=2026-04-17T20:08:19.4530000Z ~ 69cdc937d385e3b94310f756.jsonl[1484] _id=69e293331724f0c9e2f7dad0 ts=2026-04-17T20:08:19.6860000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f756.jsonl[2419] _id=69e293831724f0c9e2f7dc64 ts=2026-04-17T20:09:38.8510000Z -> 69cdc937d385e3b94310f756.jsonl[1501] _id=69e7c7b71724f0c9e2f9ad39 ts=2026-04-21T18:53:42.8040000Z; 47h 6m: 69cdc937d385e3b94310f756.jsonl[402] _id=69dd4ceb7957a33870f2badd ts=2026-04-13T20:07:07.7000000Z -> 69cdc937d385e3b94310f756.jsonl[433] _id=69dfe3697957a33870f46a21 ts=2026-04-15T19:13:45.3640000Z; 46h 40m: 69cdc937d385e3b94310f756.jsonl[799] _id=69dff04a7957a33870f49ecd ts=2026-04-15T20:08:41.3120000Z -> 69cdc937d385e3b94310f756.jsonl[801] _id=69e280a31724f0c9e2f78d56 ts=2026-04-17T18:49:07.0630000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 455 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f756.jsonl[1379] _id=69e28ef01724f0c9e2f7ca4c ts=2026-04-17T19:50:08.1710000Z -> 69cdc937d385e3b94310f756.jsonl[1378] _id=69e28f021724f0c9e2f7ca9a ts=2026-04-17T19:50:08.171Z; 0ms: 69cdc937d385e3b94310f756.jsonl[855] _id=69e280f21724f0c9e2f78e40 ts=2026-04-17T18:50:20.7920000Z -> 69cdc937d385e3b94310f756.jsonl[868] _id=69e283e91724f0c9e2f798ba ts=2026-04-17T18:50:20.792Z; 2ms: 69cdc937d385e3b94310f756.jsonl[1648] _id=69e7cc111724f0c9e2f9c509 ts=2026-04-21T19:12:16.8560000Z -> 69cdc937d385e3b94310f756.jsonl[1670] _id=69e7cc111724f0c9e2f9c50b ts=2026-04-21T19:12:16.8580000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 69cdc937d385e3b94310f756.jsonl[1368] _id=69e28ef01724f0c9e2f7ca4a ts=2026-04-17T19:50:08.1530000Z -> 69cdc937d385e3b94310f756.jsonl[2660] _id=69e7cd231724f0c9e2f9ccad ts=2026-04-21T19:16:51.2170000Z; 95h 18m: 69cdc937d385e3b94310f756.jsonl[2180] _id=69dd44ea7957a33870f29d9b ts=2026-04-13T19:32:58.5440000Z -> 69cdc937d385e3b94310f756.jsonl[883] _id=69e283f01724f0c9e2f79904 ts=2026-04-17T18:51:43.928Z; 58m 24s: 69cdc937d385e3b94310f756.jsonl[883] _id=69e283f01724f0c9e2f79904 ts=2026-04-17T18:51:43.928Z -> 69cdc937d385e3b94310f756.jsonl[1368] _id=69e28ef01724f0c9e2f7ca4a ts=2026-04-17T19:50:08.1530000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f756.jsonl[2660] _id=69e7cd231724f0c9e2f9ccad ts=2026-04-21T19:16:51.2170000Z -> 69cdc937d385e3b94310f756.jsonl[1763] _id=69e7cd311724f0c9e2f9cce9 ts=2026-04-21T19:16:51.217Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f756.jsonl[1494] _id=69e293701724f0c9e2f7dc0a ts=2026-04-17T20:09:20.4910000Z -> 69cdc937d385e3b94310f756.jsonl[2423] _id=69e7c7b41724f0c9e2f9ad2f ts=2026-04-21T18:53:40.2720000Z; 46h 59m: 69cdc937d385e3b94310f756.jsonl[412] _id=69dd4da17957a33870f2bc9d ts=2026-04-13T20:10:09.4290000Z -> 69cdc937d385e3b94310f756.jsonl[2303] _id=69dfe25b7957a33870f4670d ts=2026-04-15T19:09:14.7450000Z; 46h 40m: 69cdc937d385e3b94310f756.jsonl[793] _id=69dff0417957a33870f49e85 ts=2026-04-15T20:08:33.6870000Z -> 69cdc937d385e3b94310f756.jsonl[800] _id=69e280851724f0c9e2f78d40 ts=2026-04-17T18:48:36.7550000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 47h 29m 
  - Evidence: 47h 29m: 69cdc937d385e3b94310f756.jsonl[597] _id=69dfedb27957a33870f492f1 ts=2026-04-15T19:57:38.4760000Z -> 69cdc937d385e3b94310f756.jsonl[1196] _id=69e289771724f0c9e2f7af4c ts=2026-04-17T19:26:46.9520000Z; 47h 8m: 69cdc937d385e3b94310f756.jsonl[383] _id=69dd4c6e7957a33870f2b91f ts=2026-04-13T20:05:02.6110000Z -> 69cdc937d385e3b94310f756.jsonl[431] _id=69dfe3737957a33870f46a61 ts=2026-04-15T19:13:55.3820000Z; 31m 50s: 69cdc937d385e3b94310f756.jsonl[1199] _id=69e289881724f0c9e2f7af86 ts=2026-04-17T19:27:03.8260000Z -> 69cdc937d385e3b94310f756.jsonl[1401] _id=69e290ff1724f0c9e2f7d0ea ts=2026-04-17T19:58:54.4880000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 33m 
  - Evidence: 47h 33m: 69cdc937d385e3b94310f756.jsonl[562] _id=69dfea527957a33870f48553 ts=2026-04-15T19:43:14.6870000Z -> 69cdc937d385e3b94310f756.jsonl[1039] _id=69e287151724f0c9e2f7a550 ts=2026-04-17T19:16:37.3870000Z; 47h 11m: 69cdc937d385e3b94310f756.jsonl[335] _id=69dd4b577957a33870f2b48b ts=2026-04-13T20:00:22.7740000Z -> 69cdc937d385e3b94310f756.jsonl[426] _id=69dfe30f7957a33870f46921 ts=2026-04-15T19:12:15.8070000Z; 30m 54s: 69cdc937d385e3b94310f756.jsonl[427] _id=69dfe3117957a33870f46935 ts=2026-04-15T19:12:17.6500000Z -> 69cdc937d385e3b94310f756.jsonl[560] _id=69dfea507957a33870f4853f ts=2026-04-15T19:43:12.1790000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 69cdc937d385e3b94310f756.jsonl[2209] _id=69dd486e7957a33870f2aa77 ts=2026-04-13T19:47:58.3300000Z -> 69cdc937d385e3b94310f756.jsonl[1040] _id=69e287331724f0c9e2f7a5be ts=2026-04-17T19:17:07.1390000Z; 21m 21s: 69cdc937d385e3b94310f756.jsonl[1174] _id=69e288a61724f0c9e2f7ac76 ts=2026-04-17T19:23:18.1950000Z -> 69cdc937d385e3b94310f756.jsonl[1357] _id=69e28da81724f0c9e2f7bffe ts=2026-04-17T19:44:39.7560000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 46m 
  - Evidence: 95h 46m: 69cdc937d385e3b94310f756.jsonl[1115] _id=69e288471724f0c9e2f7aa54 ts=2026-04-17T19:21:43.2160000Z -> 69cdc937d385e3b94310f756.jsonl[1603] _id=69e7cb1a1724f0c9e2f9bfd3 ts=2026-04-21T19:08:10.4650000Z; 48h 37m: 69cdc937d385e3b94310f756.jsonl[322] _id=69dd44457957a33870f29ab0 ts=2026-04-13T19:30:12.6380000Z -> 69cdc937d385e3b94310f756.jsonl[783] _id=69dff0217957a33870f49db5 ts=2026-04-15T20:08:01.0860000Z; 46h 40m: 69cdc937d385e3b94310f756.jsonl[791] _id=69dff0497957a33870f49ec1 ts=2026-04-15T20:08:41.2390000Z -> 69cdc937d385e3b94310f756.jsonl[812] _id=69e280a71724f0c9e2f78d76 ts=2026-04-17T18:49:09.3800000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 48h 38m 
  - Evidence: 48h 38m: 69cdc937d385e3b94310f756.jsonl[2276] _id=69dd44427957a33870f29aa8 ts=2026-04-13T19:30:09.8570000Z -> 69cdc937d385e3b94310f756.jsonl[794] _id=69dff0447957a33870f49e9f ts=2026-04-15T20:08:36.5510000Z; 46h 40m: 69cdc937d385e3b94310f756.jsonl[796] _id=69dff0487957a33870f49eb3 ts=2026-04-15T20:08:40.1720000Z -> 69cdc937d385e3b94310f756.jsonl[832] _id=69e280b21724f0c9e2f78db4 ts=2026-04-17T18:49:22.2990000Z; 30m 57s: 69cdc937d385e3b94310f756.jsonl[820] _id=69e280b61724f0c9e2f78dc2 ts=2026-04-17T18:49:26.0950000Z -> 69cdc937d385e3b94310f756.jsonl[1096] _id=69e287f71724f0c9e2f7a920 ts=2026-04-17T19:20:23.5280000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 46m 
  - Evidence: 95h 46m: 69cdc937d385e3b94310f756.jsonl[1128] _id=69e288321724f0c9e2f7a9ee ts=2026-04-17T19:21:22.0060000Z -> 69cdc937d385e3b94310f756.jsonl[1601] _id=69e7cb1a1724f0c9e2f9bfcd ts=2026-04-21T19:08:10.3200000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.038s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f756.jsonl[1601] _id=69e7cb1a1724f0c9e2f9bfcd ts=2026-04-21T19:08:10.3200000Z -> 69cdc937d385e3b94310f756.jsonl[1602] _id=69e7cb1a1724f0c9e2f9bfd1 ts=2026-04-21T19:08:10.3220000Z; 8ms: 69cdc937d385e3b94310f756.jsonl[1123] _id=69e288261724f0c9e2f7a9cd ts=2026-04-17T19:21:09.8060000Z -> 69cdc937d385e3b94310f756.jsonl[1109] _id=69e288261724f0c9e2f7a9d2 ts=2026-04-17T19:21:09.8140000Z; 38ms: 69cdc937d385e3b94310f756.jsonl[1119] _id=69e288231724f0c9e2f7a9c0 ts=2026-04-17T19:21:06.9410000Z -> 69cdc937d385e3b94310f756.jsonl[1120] _id=69e288231724f0c9e2f7a9c2 ts=2026-04-17T19:21:06.9790000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f756.jsonl[2415] _id=69e293831724f0c9e2f7dc60 ts=2026-04-17T20:09:38.6840000Z -> 69cdc937d385e3b94310f756.jsonl[2424] _id=69e7c7b71724f0c9e2f9ad37 ts=2026-04-21T18:53:42.6140000Z; 47h 6m: 69cdc937d385e3b94310f756.jsonl[367] _id=69dd4bf97957a33870f2b6ef ts=2026-04-13T20:03:04.8910000Z -> 69cdc937d385e3b94310f756.jsonl[420] _id=69dfe25f7957a33870f46713 ts=2026-04-15T19:09:18.2940000Z; 46h 40m: 69cdc937d385e3b94310f756.jsonl[770] _id=69dff01a7957a33870f49d81 ts=2026-04-15T20:07:54.3040000Z -> 69cdc937d385e3b94310f756.jsonl[2313] _id=69e280871724f0c9e2f78d44 ts=2026-04-17T18:48:39.1090000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 20 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f756.jsonl[2068] _id=69e7d2391724f0c9e2f9e56b ts=2026-04-21T19:38:32.0750000Z -> 69cdc937d385e3b94310f756.jsonl[2069] _id=69e7d2391724f0c9e2f9e56d ts=2026-04-21T19:38:32.0770000Z; 2ms: 69cdc937d385e3b94310f756.jsonl[2314] _id=69e280a41724f0c9e2f78d5a ts=2026-04-17T18:49:07.0790000Z -> 69cdc937d385e3b94310f756.jsonl[817] _id=69e280a41724f0c9e2f78d5c ts=2026-04-17T18:49:07.0810000Z; 3ms: 69cdc937d385e3b94310f756.jsonl[304] _id=69dd440e7957a33870f2999c ts=2026-04-13T19:29:17.3710000Z -> 69cdc937d385e3b94310f756.jsonl[305] _id=69dd440e7957a33870f299a0 ts=2026-04-13T19:29:17.3740000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc937d385e3b94310f756.jsonl[1492] _id=69e293531724f0c9e2f7db5e ts=2026-04-17T20:08:51.7210000Z -> 69cdc937d385e3b94310f756.jsonl[2429] _id=69e7c7ff1724f0c9e2f9ae5d ts=2026-04-21T18:54:55.3730000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc937d385e3b94310f756.jsonl:69cdc937d385e3b94310f756, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f756.jsonl[103] _id=69dd47697957a33870f2a5c3 ts=2026-04-13T19:43:37.3010000Z`; `69cdc937d385e3b94310f756.jsonl[383] _id=69dd4c6e7957a33870f2b91f ts=2026-04-13T20:05:02.6110000Z`; `69cdc937d385e3b94310f756.jsonl[1199] _id=69e289881724f0c9e2f7af86 ts=2026-04-17T19:27:03.8260000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 11 record(s) match the trigger in 69cdc937d385e3b94310f756.jsonl:69cdc937d385e3b94310f756, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f756.jsonl[2209] _id=69dd486e7957a33870f2aa77 ts=2026-04-13T19:47:58.3300000Z`; `69cdc937d385e3b94310f756.jsonl[1040] _id=69e287331724f0c9e2f7a5be ts=2026-04-17T19:17:07.1390000Z`; `69cdc937d385e3b94310f756.jsonl[1041] _id=69e287351724f0c9e2f7a5c6 ts=2026-04-17T19:17:09.3350000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f756.jsonl[860] _id=69e285081724f0c9e2f79d78 ts=2026-04-17T19:07:52.2030000Z`; `69cdc937d385e3b94310f756.jsonl[970] _id=69e2853d1724f0c9e2f79e68 ts=2026-04-17T19:08:45.0010000Z`; `69cdc937d385e3b94310f756.jsonl[2484] _id=69e7c9f31724f0c9e2f9b8c7 ts=2026-04-21T19:03:15.8070000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f756.jsonl[812] _id=69e280a71724f0c9e2f78d76 ts=2026-04-17T18:49:09.3800000Z`; `69cdc937d385e3b94310f756.jsonl[815] _id=69e280a71724f0c9e2f78d82 ts=2026-04-17T18:49:09.9780000Z`; `69cdc937d385e3b94310f756.jsonl[1115] _id=69e288471724f0c9e2f7aa54 ts=2026-04-17T19:21:43.2160000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f756.jsonl[1119] _id=69e288231724f0c9e2f7a9c0 ts=2026-04-17T19:21:06.9410000Z`; `69cdc937d385e3b94310f756.jsonl[1123] _id=69e288261724f0c9e2f7a9cd ts=2026-04-17T19:21:09.8060000Z`; `69cdc937d385e3b94310f756.jsonl[1601] _id=69e7cb1a1724f0c9e2f9bfcd ts=2026-04-21T19:08:10.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc937d385e3b94310f756.jsonl[2421] _id=69e7c7bd1724f0c9e2f9ad51 ts=2026-04-21T18:53:49.0950000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f756.jsonl[470] _id=69dfe5897957a33870f4724b ts=2026-04-15T19:22:48.9850000Z`; `69cdc937d385e3b94310f756.jsonl[489] _id=69dfe6647957a33870f4763d ts=2026-04-15T19:26:28.4320000Z`; `69cdc937d385e3b94310f756.jsonl[513] _id=69dfe7487957a33870f47a17 ts=2026-04-15T19:30:16.0730000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f756.jsonl[1120] _id=69e288231724f0c9e2f7a9c2 ts=2026-04-17T19:21:06.9790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 185 unmatched 'DialogueStartEvent' (totals: 373 start, 191 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'Started' (totals: 12 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 8 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 10 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 38 unmatched 'questActiveEvent' (totals: 75 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.32s, min -765.12s, max +0.08s over 2673 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f756\coverage.yaml

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
  - Observed: 28 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1936 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (423); Unit 3 Dev (311); Unit 2 Prod (Refactor) (310); Unit 5 Dev (265); Unit 4 Dev (240); Unit 4 Dev - Anderson Base (148); Unit 4 Dev - Dungeon (113); Unit 3 Dungeon Dev (96); Unit 5 Dev - Dungeon (30)
- **eventKey:** present on 1372 of 1936 records
- **Intervals:** median 0.83s (p5 0.01s / p95 27.52s, n=1935)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1372; [conversationId, dialogueEventType] x564
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1936/1936 records)
    numeric range 10 .. 114 (46 unique)
data.dialogueEventType  (string, 1936/1936 records)
    "DialogueNodeEvent"  x1372
    "DialogueStartEvent"  x373
    "DialogueFinishEvent"  x191
data.nodeId  (number, 1372/1936 records)
    numeric range 0 .. 286 (203 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 427 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (134); Unit 1 Dev (72); Unit 3 Dev (59); Unit 4 Dev (33); Unit 3 Dungeon Dev (32); Unit 4 Dev - Dungeon (31); Unit 5 Dev (29); Unit 5 Dev - Dungeon (22); Unit 4 Dev - Anderson Base (15)
- **Intervals:** median 30.01s (p5 29.96s / p95 61.66s, n=414)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 427/427 records)
data.position.x  (number, 427/427 records)
    numeric range -698.038 .. 1554.9 (245 unique)
data.position.y  (number, 427/427 records)
    numeric range -112.487 .. 217.708 (218 unique)
data.position.z  (number, 427/427 records)
    numeric range -1110.2 .. 1833.39 (245 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 113 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 1 Dev (27); Unit 4 Dev - Dungeon (13); Unit 5 Dev (12); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 113 of 113 records
- **Intervals:** median 83.20s (p5 0.01s / p95 697.88s, n=112)
- **`data` key-set variants:** [questEventType, questID, questName] x75; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 113/113 records)
    "questActiveEvent"  x75
    "questFinishEvent"  x38
data.questID  (string, 113/113 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 113/113 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/113 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 41 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (41)
- **Intervals:** median 4.33s (p5 0.55s / p95 32.74s, n=40)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "On"  x26
    "Off"  x15
data.floor  (string, 41/41 records)
    "4"  x28
    "3"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 41/41 records)
    "One"  x40
    "Two"  x1
data.machineType  (string, 41/41 records)
    "Condenser"  x21
    "Evaporator"  x15
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 41/41 records)
    "3"  x18
    "2"  x17
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 32 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (32)
- **Intervals:** median 3.24s (p5 0.20s / p95 110.73s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "ChangeCanister"  x32
data.canisterType  (string, 32/32 records)
    "Bedrock"  x11
    "Sand"  x9
    "Clay"  x8
    "Gravel"  x4
data.floor  (string, 32/32 records)
    "5"  x20
    "3"  x11
    "4"  x1
data.machine  (string, 32/32 records)
    "1"  x31
    "2"  x1
data.row  (string, 32/32 records)
    "TopRow"  x18
    "BottomRow"  x14
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Topographic Map Event` — 28 records

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (14)
- **Intervals:** median 28.60s (p5 2.24s / p95 119495.48s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "MapCloseEvent"  x14
    "MapOpenEvent"  x14
data.featureUsed  (string, 28/28 records)
    "Map"  x28
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationToolEvent` — 22 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (12); Unit 3 Dev (10)
- **Intervals:** median 1.15s (p5 0.01s / p95 238.76s, n=21)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "argumentationToolClose"  x12
    "argumentationToolOpen"  x10
data.argumentationTitle  (string, 22/22 records)
    "Unit 4 - Flooding"  x12
    "Unit 3 - Pollution Upstream"  x10
data.toolName  (string, 22/22 records)
    "BackingInfoPanel - Soil Flow Rates"  x8
    "BackingInfoPanel - Pollution Site Data"  x6
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - "  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (12); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 25.05s (p5 0.50s / p95 209012.21s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 18/18 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x6
    "Unit 1 - Does the planet WAT-247 have freshwater"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 18/18 records)
    "Unit 1 - Argumentation Tutorial"  x6
    "Unit 1 - Freshwater"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 16 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 239.03s (p5 12.71s / p95 170097.48s, n=15)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 16/16 records)
    "Started"  x12
    "Finished"  x4
data.Unit  (string, 16/16 records)
    "Unit 2 Prod (Refactor)"  x12
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 16 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (7)
- **Intervals:** median 6.14s (p5 1.56s / p95 170161.50s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 1 - Freshwater"  x9
    "Unit 3 - Pollution Upstream"  x7
data.nodeName  (string, 16/16 records)
    "B"  x5
    "I"  x4
    "1"  x3
    "4"  x2
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 11 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (10); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 10.80s (p5 0.94s / p95 189638.55s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "dragStart"  x6
    "dragEnd"  x5
data.featureUsed  (string, 11/11 records)
    "waypoint"  x11
data.location  (object, 11/11 records)
data.location.x  (number, 11/11 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 11/11 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 11/11 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `EndOfUnit` — 7 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 4 Dev (2); Unit 5 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 2397.58s (p5 65.81s / p95 343483.64s, n=6)
- **Fields under `data`:**

```text
data.Unit  (string, 7/7 records)
    "1"  x2
    "4"  x2
    "5"  x2
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 0.18s (p5 0.14s / p95 10.43s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x6
data.boxId  (string, 6/6 records)
    "2"  x4
    "0"  x1
    "1"  x1
data.soilType  (string, 6/6 records)
    "None"  x6
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.soilType: "None" (6x)
- `TopographicMapEvent` data.actionType: "dragStart" (6x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (11x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*