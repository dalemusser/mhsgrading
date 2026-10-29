# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f733

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f733
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f733.jsonl
- **Records:** 2660 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f733
- **Time span:** 2026-04-13T18:12:29.648000+00:00 .. 2026-04-23T18:32:52.180000+00:00 (240h 20m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f733\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2660 records, 9 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 61 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1747 | 65.68 | 1 | 9 | 1250 | 2026-04-13T18:12:47.675000+00:00 | 2026-04-23T18:32:40.369000+00:00 | 240h 19m |
| PlayerPositionEvent | 624 | 23.46 | 1 | 9 | 0 | 2026-04-13T18:12:29.648000+00:00 | 2026-04-23T18:32:50.951000+00:00 | 240h 20m |
| WaterChamberEvent | 80 | 3.01 | 1 | 1 | 0 | 2026-04-21T18:32:52.321000+00:00 | 2026-04-23T18:11:43.501000+00:00 | 47h 38m |
| questEvent | 77 | 2.89 | 1 | 9 | 77 | 2026-04-13T18:12:47.660000+00:00 | 2026-04-23T18:30:26.018000+00:00 | 240h 17m |
| Topographic Map Event | 30 | 1.13 | 1 | 2 | 0 | 2026-04-15T17:57:57.732000+00:00 | 2026-04-17T18:34:42.296000+00:00 | 48h 36m |
| argumentationNodeEvent | 25 | 0.94 | 1 | 3 | 0 | 2026-04-13T18:34:02.282000+00:00 | 2026-04-17T18:00:52.809000+00:00 | 95h 26m |
| TopographicMapEvent | 24 | 0.9 | 1 | 2 | 0 | 2026-04-15T18:01:30.141000+00:00 | 2026-04-17T18:34:40.328000+00:00 | 48h 33m |
| soilMachine | 21 | 0.79 | 1 | 1 | 0 | 2026-04-21T17:44:12.486000+00:00 | 2026-04-21T17:54:55.487000+00:00 | 10m 43s |
| argumentationEvent | 12 | 0.45 | 1 | 5 | 0 | 2026-04-13T18:33:23.165000+00:00 | 2026-04-23T18:21:07.449000+00:00 | 239h 47m |
| Soil Key Puzzle | 6 | 0.23 | 1 | 3 | 0 | 2026-04-15T18:12:02.723000+00:00 | 2026-04-21T17:02:10.924000+00:00 | 142h 50m |
| argumentationToolEvent | 6 | 0.23 | 1 | 1 | 0 | 2026-04-21T18:11:18.611000+00:00 | 2026-04-21T18:13:09.637000+00:00 | 1m 51s |
| EndOfUnit | 5 | 0.19 | 1 | 5 | 0 | 2026-04-13T18:38:47.849000+00:00 | 2026-04-23T18:32:52.180000+00:00 | 239h 54m |
| TerasGardenBox | 3 | 0.11 | 1 | 1 | 0 | 2026-04-21T18:19:05.211000+00:00 | 2026-04-21T18:19:48.872000+00:00 | 43.7s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 257568.965s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.024s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 63.687s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 21.831s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.674s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.659s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.168s median 
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
  - Observed: 14.095s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 11 in 09-23-26 
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
  - Observed: 30 records this build 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 80 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 25 records 
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
  - Observed: 2; 4 
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
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f733.jsonl[1314] _id=69dd377f7957a33870f28920 ts=2026-04-13T18:35:43.1930000Z`; `69cdc907d385e3b94310f733.jsonl[1429] _id=69dfd2697957a33870f4250d ts=2026-04-15T18:01:12.5210000Z`; `69cdc907d385e3b94310f733.jsonl[496] _id=69e267b01724f0c9e2f72d74 ts=2026-04-17T17:02:40.4210000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 30 records, TopographicMapEvent: 24 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1746 | 0.0 | 3.122 | 495.528 | 32.856 | 339409.919 | 0.12 | 408 | 6 |
| PlayerPositionEvent | 612 | 29.729 | 30.024 | 1413.17 | 36.326 | 339377.164 | 0.04 | 0 | 4 |
| WaterChamberEvent | 79 | 0.115 | 5.674 | 2171.281 | 42.378 | 170663.428 | 0.03 | 0 | 1 |
| questEvent | 76 | 0.003 | 152.25 | 11382.347 | 43482.841 | 339685.301 | 0.01 | 16 | 11 |
| Topographic Map Event | 29 | 0.547 | 19.0 | 6034.64 | 1910.339 | 170228.796 | 0.01 | 0 | 3 |
| argumentationNodeEvent | 24 | 1.113 | 7.659 | 14317.105 | 2873.469 | 339994.502 | 0.0 | 0 | 2 |
| TopographicMapEvent | 23 | 0.164 | 3.098 | 7599.573 | 2427.712 | 171251.02 | 0.01 | 0 | 2 |
| soilMachine | 20 | 1.295 | 14.095 | 32.15 | 110.715 | 196.152 | 1.87 | 0 | 0 |
| argumentationEvent | 11 | 0.079 | 93.684 | 78478.571 | 343101.98 | 346228.627 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 5 | 37.263 | 63.687 | 102841.64 | 307850.897 | 341734.13 | 0.0 | 0 | 2 |
| argumentationToolEvent | 5 | 0.003 | 7.168 | 22.205 | 71.437 | 85.87 | 2.7 | 1 | 0 |
| EndOfUnit | 4 | 3446.836 | 257568.965 | 215911.083 | 344617.796 | 345059.565 | 0.0 | 0 | 4 |
| TerasGardenBox | 2 | 15.814 | 21.831 | 21.831 | 27.245 | 27.847 | 2.75 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.024s (p5 29.95s, p95 36.33s, n=612) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `613ms: 69cdc907d385e3b94310f733.jsonl[2504] _id=69ea60231724f0c9e2fb11ce ts=2026-04-23T18:08:34.9510000Z ~ 69cdc907d385e3b94310f733.jsonl[2513] _id=69ea60231724f0c9e2fb11e1 ts=2026-04-23T18:08:35.5640000Z`; `470ms: 69cdc907d385e3b94310f733.jsonl[2512] _id=69ea60231724f0c9e2fb11dd ts=2026-04-23T18:08:35.2470000Z ~ 69cdc907d385e3b94310f733.jsonl[1084] _id=69ea60241724f0c9e2fb11e3 ts=2026-04-23T18:08:35.7170000Z`; `322ms: 69cdc907d385e3b94310f733.jsonl[2513] _id=69ea60231724f0c9e2fb11e1 ts=2026-04-23T18:08:35.5640000Z ~ 69cdc907d385e3b94310f733.jsonl[1086] _id=69ea60241724f0c9e2fb11e5 ts=2026-04-23T18:08:35.8860000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `79ms: 69cdc907d385e3b94310f733.jsonl[657] _id=69e275571724f0c9e2f76094 ts=2026-04-17T18:00:54.9500000Z ~ 69cdc907d385e3b94310f733.jsonl[658] _id=69e275571724f0c9e2f7609a ts=2026-04-17T18:00:55.0290000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc907d385e3b94310f733.jsonl[945] _id=69e7bdca1724f0c9e2f9734f ts=2026-04-21T18:11:18.6110000Z ~ 69cdc907d385e3b94310f733.jsonl[2280] _id=69e7bdca1724f0c9e2f97351 ts=2026-04-21T18:11:18.6140000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 69cdc907d385e3b94310f733.jsonl[2591] _id=69ea63221724f0c9e2fb2c55 ts=2026-04-23T18:21:21.8810000Z ~ 69cdc907d385e3b94310f733.jsonl[1125] _id=69ea63221724f0c9e2fb2c58 ts=2026-04-23T18:21:21.8920000Z`; `9ms: 69cdc907d385e3b94310f733.jsonl[1152] _id=69ea64ef1724f0c9e2fb398b ts=2026-04-23T18:29:03.4260000Z ~ 69cdc907d385e3b94310f733.jsonl[1153] _id=69ea64ef1724f0c9e2fb398d ts=2026-04-23T18:29:03.4350000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f733.jsonl[788] _id=69e27e6a1724f0c9e2f78c8e ts=2026-04-17T18:39:38.3130000Z -> 69cdc907d385e3b94310f733.jsonl[790] _id=69e7ac3c1724f0c9e2f916c5 ts=2026-04-21T16:56:28.2320000Z; 47h 26m: 69cdc907d385e3b94310f733.jsonl[1058] _id=69e7c3041724f0c9e2f99bad ts=2026-04-21T18:33:39.7120000Z -> 69cdc907d385e3b94310f733.jsonl[2459] _id=69ea5e2d1724f0c9e2fb0477 ts=2026-04-23T18:00:12.9540000Z; 47h 2m: 69cdc907d385e3b94310f733.jsonl[126] _id=69dd38ce7957a33870f291f4 ts=2026-04-13T18:41:17.8600000Z -> 69cdc907d385e3b94310f733.jsonl[1345] _id=69dfce387957a33870f40afd ts=2026-04-15T17:43:19.9370000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 408 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f733.jsonl[1040] _id=69e7c1f51724f0c9e2f99499 ts=2026-04-21T18:29:08.7040000Z -> 69cdc907d385e3b94310f733.jsonl[2415] _id=69e7c2051724f0c9e2f9952d ts=2026-04-21T18:29:08.704Z; 0ms: 69cdc907d385e3b94310f733.jsonl[577] _id=69e2709a1724f0c9e2f74052 ts=2026-04-17T17:40:42.3100000Z -> 69cdc907d385e3b94310f733.jsonl[578] _id=69e270a91724f0c9e2f740ba ts=2026-04-17T17:40:42.31Z; 2ms: 69cdc907d385e3b94310f733.jsonl[496] _id=69e267b01724f0c9e2f72d74 ts=2026-04-17T17:02:40.4210000Z -> 69cdc907d385e3b94310f733.jsonl[497] _id=69e267b01724f0c9e2f72d76 ts=2026-04-17T17:02:40.4230000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc907d385e3b94310f733.jsonl[2030] _id=69e27e111724f0c9e2f78a66 ts=2026-04-17T18:38:09.1230000Z -> 69cdc907d385e3b94310f733.jsonl[2414] _id=69e7c1f51724f0c9e2f99495 ts=2026-04-21T18:29:08.6880000Z; 95h 1m: 69cdc907d385e3b94310f733.jsonl[1330] _id=69dd38387957a33870f28e46 ts=2026-04-13T18:38:47.8490000Z -> 69cdc907d385e3b94310f733.jsonl[1719] _id=69e2709a1724f0c9e2f74050 ts=2026-04-17T17:40:42.2870000Z; 48h 3m: 69cdc907d385e3b94310f733.jsonl[2414] _id=69e7c1f51724f0c9e2f99495 ts=2026-04-21T18:29:08.6880000Z -> 69cdc907d385e3b94310f733.jsonl[2642] _id=69ea65d41724f0c9e2fb40c9 ts=2026-04-23T18:32:52.1800000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f733.jsonl[789] _id=69e27e791724f0c9e2f78cca ts=2026-04-17T18:39:53.4860000Z -> 69cdc907d385e3b94310f733.jsonl[2034] _id=69e7ac2b1724f0c9e2f9166d ts=2026-04-21T16:56:10.6500000Z; 47h 20m: 69cdc907d385e3b94310f733.jsonl[1070] _id=69e7c47a1724f0c9e2f9a6e3 ts=2026-04-21T18:39:53.8990000Z -> 69cdc907d385e3b94310f733.jsonl[2457] _id=69ea5e231724f0c9e2fb0461 ts=2026-04-23T18:00:03.0780000Z; 47h 2m: 69cdc907d385e3b94310f733.jsonl[124] _id=69dd38bd7957a33870f29198 ts=2026-04-13T18:41:01.4080000Z -> 69cdc907d385e3b94310f733.jsonl[1341] _id=69dfce347957a33870f40af7 ts=2026-04-15T17:43:15.8900000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 55m 
  - Evidence: 94h 55m: 69cdc907d385e3b94310f733.jsonl[1880] _id=69e276751724f0c9e2f766aa ts=2026-04-17T18:05:41.6390000Z -> 69cdc907d385e3b94310f733.jsonl[2047] _id=69e7ad5c1724f0c9e2f91d33 ts=2026-04-21T17:01:15.7690000Z; 47h 51m: 69cdc907d385e3b94310f733.jsonl[1484] _id=69dfd5337957a33870f43665 ts=2026-04-15T18:13:06.4100000Z -> 69cdc907d385e3b94310f733.jsonl[1875] _id=69e276501724f0c9e2f76588 ts=2026-04-17T18:05:04.3760000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 17m 
  - Evidence: 47h 17m: 69cdc907d385e3b94310f733.jsonl[359] _id=69dfd8bd7957a33870f44db7 ts=2026-04-15T18:28:12.2830000Z -> 69cdc907d385e3b94310f733.jsonl[1748] _id=69e271b11724f0c9e2f7486e ts=2026-04-17T17:45:21.0790000Z; 41m 15s: 69cdc907d385e3b94310f733.jsonl[1775] _id=69e272bd1724f0c9e2f74f7e ts=2026-04-17T17:49:48.9180000Z -> 69cdc907d385e3b94310f733.jsonl[1988] _id=69e27c681724f0c9e2f7809e ts=2026-04-17T18:31:04.2070000Z; 17m 42s: 69cdc907d385e3b94310f733.jsonl[236] _id=69dfd4897957a33870f432f5 ts=2026-04-15T18:10:16.6750000Z -> 69cdc907d385e3b94310f733.jsonl[354] _id=69dfd8b07957a33870f44d25 ts=2026-04-15T18:27:59.5880000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 34m 
  - Evidence: 47h 34m: 69cdc907d385e3b94310f733.jsonl[1469] _id=69dfd46f7957a33870f43257 ts=2026-04-15T18:09:50.9280000Z -> 69cdc907d385e3b94310f733.jsonl[1733] _id=69e271621724f0c9e2f745b6 ts=2026-04-17T17:44:01.9480000Z; 44m 24s: 69cdc907d385e3b94310f733.jsonl[1774] _id=69e272ba1724f0c9e2f74f6e ts=2026-04-17T17:49:45.9850000Z -> 69cdc907d385e3b94310f733.jsonl[752] _id=69e27d231724f0c9e2f78474 ts=2026-04-17T18:34:10.9520000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 24m 
  - Evidence: 47h 24m: 69cdc907d385e3b94310f733.jsonl[2456] _id=69e7c43c1724f0c9e2f9a577 ts=2026-04-21T18:38:52.0610000Z -> 69cdc907d385e3b94310f733.jsonl[1074] _id=69ea5ee31724f0c9e2fb0811 ts=2026-04-23T18:03:15.4890000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 10m 
  - Evidence: 96h 10m: 69cdc907d385e3b94310f733.jsonl[658] _id=69e275571724f0c9e2f7609a ts=2026-04-17T18:00:55.0290000Z -> 69cdc907d385e3b94310f733.jsonl[942] _id=69e7bdcc1724f0c9e2f9735d ts=2026-04-21T18:11:23.6560000Z; 94h 26m: 69cdc907d385e3b94310f733.jsonl[1313] _id=69dd377f7957a33870f2891c ts=2026-04-13T18:35:43.1650000Z -> 69cdc907d385e3b94310f733.jsonl[485] _id=69e267861724f0c9e2f72c7c ts=2026-04-17T17:01:58.4970000Z; 48h 6m: 69cdc907d385e3b94310f733.jsonl[942] _id=69e7bdcc1724f0c9e2f9735d ts=2026-04-21T18:11:23.6560000Z -> 69cdc907d385e3b94310f733.jsonl[1113] _id=69ea62471724f0c9e2fb256b ts=2026-04-23T18:17:43.6610000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 26m 
  - Evidence: 94h 26m: 69cdc907d385e3b94310f733.jsonl[1312] _id=69dd37757957a33870f288c4 ts=2026-04-13T18:35:32.9370000Z -> 69cdc907d385e3b94310f733.jsonl[486] _id=69e2678f1724f0c9e2f72c9c ts=2026-04-17T17:02:07.4390000Z; 56m 8s: 69cdc907d385e3b94310f733.jsonl[1657] _id=69e267e01724f0c9e2f72f48 ts=2026-04-17T17:03:28.1440000Z -> 69cdc907d385e3b94310f733.jsonl[653] _id=69e275081724f0c9e2f75e96 ts=2026-04-17T17:59:36.8260000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f733.jsonl[945] _id=69e7bdca1724f0c9e2f9734f ts=2026-04-21T18:11:18.6110000Z -> 69cdc907d385e3b94310f733.jsonl[2280] _id=69e7bdca1724f0c9e2f97351 ts=2026-04-21T18:11:18.6140000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc907d385e3b94310f733.jsonl[2029] _id=69e27e071724f0c9e2f78a24 ts=2026-04-17T18:37:59.4320000Z -> 69cdc907d385e3b94310f733.jsonl[2040] _id=69e7aced1724f0c9e2f91a6b ts=2026-04-21T16:59:24.7330000Z; 47h 23m: 69cdc907d385e3b94310f733.jsonl[1066] _id=69e7c3951724f0c9e2f99fcd ts=2026-04-21T18:36:05.2570000Z -> 69cdc907d385e3b94310f733.jsonl[2458] _id=69ea5e261724f0c9e2fb0467 ts=2026-04-23T18:00:04.9770000Z; 47h 2m: 69cdc907d385e3b94310f733.jsonl[127] _id=69dd38cd7957a33870f291f2 ts=2026-04-13T18:41:17.6460000Z -> 69cdc907d385e3b94310f733.jsonl[130] _id=69dfce377957a33870f40af9 ts=2026-04-15T17:43:18.4680000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f733.jsonl[1289] _id=69dd369d7957a33870f28376 ts=2026-04-13T18:31:57.5060000Z -> 69cdc907d385e3b94310f733.jsonl[1286] _id=69dd369e7957a33870f2837c ts=2026-04-13T18:31:57.5090000Z; 6ms: 69cdc907d385e3b94310f733.jsonl[1076] _id=69ea5f071724f0c9e2fb08f9 ts=2026-04-23T18:03:50.8000000Z -> 69cdc907d385e3b94310f733.jsonl[2473] _id=69ea5f071724f0c9e2fb08fb ts=2026-04-23T18:03:50.8060000Z; 6ms: 69cdc907d385e3b94310f733.jsonl[1079] _id=69ea5f331724f0c9e2fb0a55 ts=2026-04-23T18:04:35.2270000Z -> 69cdc907d385e3b94310f733.jsonl[1080] _id=69ea5f331724f0c9e2fb0a57 ts=2026-04-23T18:04:35.2330000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f733.jsonl:69cdc907d385e3b94310f733, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f733.jsonl[1484] _id=69dfd5337957a33870f43665 ts=2026-04-15T18:13:06.4100000Z`; `69cdc907d385e3b94310f733.jsonl[1880] _id=69e276751724f0c9e2f766aa ts=2026-04-17T18:05:41.6390000Z`; `69cdc907d385e3b94310f733.jsonl[803] _id=69e7ad931724f0c9e2f91ebb ts=2026-04-21T17:02:10.9240000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 24 record(s) match the trigger in 69cdc907d385e3b94310f733.jsonl:69cdc907d385e3b94310f733, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f733.jsonl[207] _id=69dfd27a7957a33870f4259d ts=2026-04-15T18:01:30.1410000Z`; `69cdc907d385e3b94310f733.jsonl[208] _id=69dfd27b7957a33870f425a1 ts=2026-04-15T18:01:31.0710000Z`; `69cdc907d385e3b94310f733.jsonl[219] _id=69dfd32c7957a33870f42a19 ts=2026-04-15T18:04:27.3030000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f733.jsonl[1528] _id=69dfd8497957a33870f44989 ts=2026-04-15T18:26:16.9020000Z`; `69cdc907d385e3b94310f733.jsonl[605] _id=69e272ac1724f0c9e2f74f0c ts=2026-04-17T17:49:31.9350000Z`; `69cdc907d385e3b94310f733.jsonl[617] _id=69e2733a1724f0c9e2f75286 ts=2026-04-17T17:51:53.7390000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f733.jsonl[658] _id=69e275571724f0c9e2f7609a ts=2026-04-17T18:00:55.0290000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f733.jsonl[945] _id=69e7bdca1724f0c9e2f9734f ts=2026-04-21T18:11:18.6110000Z`; `69cdc907d385e3b94310f733.jsonl[2280] _id=69e7bdca1724f0c9e2f97351 ts=2026-04-21T18:11:18.6140000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 145 unmatched 'DialogueStartEvent' (totals: 319 start, 178 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 43 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.46s, min -17.07s, max -0.06s over 2660 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f733\coverage.yaml

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
  - Observed: 30 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1747 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (583); Unit 3 Dev (274); Unit 4 Dev (217); Unit 1 Dev (192); Unit 5 Dev (163); Unit 4 Dev - Anderson Base (95); Unit 4 Dev - Dungeon (95); Unit 3 Dungeon Dev (89); Unit 5 Dev - Dungeon (39)
- **eventKey:** present on 1250 of 1747 records
- **Intervals:** median 3.12s (p5 0.01s / p95 32.86s, n=1746)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1250; [conversationId, dialogueEventType] x497
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1747/1747 records)
    numeric range 8 .. 114 (50 unique)
data.dialogueEventType  (string, 1747/1747 records)
    "DialogueNodeEvent"  x1250
    "DialogueStartEvent"  x319
    "DialogueFinishEvent"  x178
data.nodeId  (number, 1250/1747 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 624 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (207); Unit 4 Dev - Dungeon (92); Unit 3 Dev (68); Unit 4 Dev (59); Unit 1 Dev (53); Unit 5 Dev - Dungeon (43); Unit 5 Dev (38); Unit 3 Dungeon Dev (37); Unit 4 Dev - Anderson Base (27)
- **Intervals:** median 30.02s (p5 29.95s / p95 36.33s, n=612)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 624/624 records)
data.position.x  (number, 624/624 records)
    numeric range -694.504 .. 1557.79 (270 unique)
data.position.y  (number, 624/624 records)
    numeric range -114.326 .. 221.396 (225 unique)
data.position.z  (number, 624/624 records)
    numeric range -1123.12 .. 1809.75 (270 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `WaterChamberEvent` — 80 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (80)
- **Intervals:** median 5.67s (p5 0.17s / p95 42.38s, n=79)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 80/80 records)
    "On"  x50
    "Off"  x30
data.floor  (string, 80/80 records)
    "4"  x51
    "3"  x18
    "2"  x6
    "1"  x5
data.machineNumber  (string, 80/80 records)
    "One"  x78
    "Two"  x2
data.machineType  (string, 80/80 records)
    "Condenser"  x40
    "Evaporator"  x29
    "VentSwitch"  x5
    "DualChamber_Evaporator"  x4
    "DualChamber_Condenser"  x2
data.room  (string, 80/80 records)
    "3"  x46
    "2"  x20
    "1"  x10
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `questEvent` — 77 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 5 Dev - Dungeon (14); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 77 of 77 records
- **Intervals:** median 152.25s (p5 0.01s / p95 43482.84s, n=76)
- **`data` key-set variants:** [questEventType, questID, questName] x43; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Fields under `data`:**

```text
data.questEventType  (string, 77/77 records)
    "questActiveEvent"  x43
    "questFinishEvent"  x34
data.questID  (string, 77/77 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 77/77 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/77 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 30 records

- **Scenes:** Unit 3 Dev (18); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 19.00s (p5 3.88s / p95 1910.34s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "MapCloseEvent"  x15
    "MapOpenEvent"  x15
data.featureUsed  (string, 30/30 records)
    "Map"  x30
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 25 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (5); Unit 3 Dev (5)
- **Intervals:** median 7.66s (p5 1.47s / p95 2873.47s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 25/25 records)
    "Unit 2 – Watershed"  x15
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 25/25 records)
    "A"  x5
    "C"  x4
    "I"  x4
    "1"  x3
    "B"  x3
    "3"  x2
    "D"  x2
    "5"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 24 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (14); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 3.10s (p5 0.48s / p95 2427.71s, n=23)
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
    numeric range -770.79 .. 122.151 (13 unique)
data.location.y  (number, 24/24 records)
    numeric range -307.4 .. 126.314 (13 unique)
data.location.z  (number, 24/24 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 14.10s (p5 1.36s / p95 110.71s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Gravel"  x8
    "Clay"  x6
    "Sand"  x5
    "Bedrock"  x2
data.floor  (string, 21/21 records)
    "5"  x12
    "4"  x8
    "3"  x1
data.machine  (string, 21/21 records)
    "1"  x15
    "2"  x6
data.row  (string, 21/21 records)
    "TopRow"  x16
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 93.68s (p5 16.92s / p95 343101.98s, n=11)
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

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 63.69s (p5 40.84s / p95 307850.90s, n=5)
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

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (6)
- **Intervals:** median 7.17s (p5 0.86s / p95 71.44s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolClose"  x4
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 4 - Flooding"  x6
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 257568.97s (p5 28883.33s / p95 344617.80s, n=4)
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

### `TerasGardenBox` — 3 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (3)
- **Intervals:** median 21.83s (p5 16.42s / p95 27.25s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "cameraPlaced"  x3
data.boxId  (string, 3/3 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 3/3 records)
    "None"  x3
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "dragStart" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*