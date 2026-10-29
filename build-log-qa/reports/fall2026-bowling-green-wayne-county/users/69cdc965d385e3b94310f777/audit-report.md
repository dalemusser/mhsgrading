# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f777

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f777
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f777.jsonl
- **Records:** 2586 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f777
- **Time span:** 2026-04-14T13:44:35.238000+00:00 .. 2026-04-24T14:33:40.685000+00:00 (240h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f777\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2586 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 64 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 1752 | 67.75 | 1 | 9 | 1224 | 2026-04-14T13:44:53.636000+00:00 | 2026-04-24T14:33:33.184000+00:00 | 240h 48m |
| PlayerPositionEvent | 574 | 22.2 | 1 | 9 | 0 | 2026-04-14T13:44:35.238000+00:00 | 2026-04-24T14:33:15.987000+00:00 | 240h 48m |
| questEvent | 95 | 3.67 | 1 | 9 | 95 | 2026-04-14T13:44:53.619000+00:00 | 2026-04-24T14:32:16.150000+00:00 | 240h 47m |
| WaterChamberEvent | 36 | 1.39 | 1 | 1 | 0 | 2026-04-24T14:02:02.361000+00:00 | 2026-04-24T14:09:30.987000+00:00 | 7m 28s |
| Topographic Map Event | 30 | 1.16 | 1 | 2 | 0 | 2026-04-16T13:47:56.010000+00:00 | 2026-04-20T14:27:33.060000+00:00 | 96h 39m |
| TopographicMapEvent | 20 | 0.77 | 1 | 2 | 0 | 2026-04-16T13:48:06.817000+00:00 | 2026-04-20T14:27:29.685000+00:00 | 96h 39m |
| Soil Key Puzzle | 18 | 0.7 | 1 | 3 | 0 | 2026-04-14T14:22:20.857000+00:00 | 2026-04-22T13:27:44.900000+00:00 | 191h 5m |
| argumentationNodeEvent | 14 | 0.54 | 1 | 2 | 0 | 2026-04-14T14:06:10.074000+00:00 | 2026-04-20T13:46:55.019000+00:00 | 143h 40m |
| soilMachine | 14 | 0.54 | 1 | 1 | 0 | 2026-04-22T13:51:44.174000+00:00 | 2026-04-22T14:00:49.197000+00:00 | 9m 5s |
| argumentationEvent | 10 | 0.39 | 1 | 4 | 0 | 2026-04-14T14:05:55.263000+00:00 | 2026-04-24T14:17:25.550000+00:00 | 240h 11m |
| argumentationToolEvent | 8 | 0.31 | 1 | 1 | 0 | 2026-04-22T14:11:40.593000+00:00 | 2026-04-22T14:13:21.442000+00:00 | 1m 40s |
| TerasGardenBox | 7 | 0.27 | 1 | 1 | 0 | 2026-04-22T14:19:09.389000+00:00 | 2026-04-22T14:20:04.343000+00:00 | 55.0s |
| EndOfUnit | 5 | 0.19 | 1 | 4 | 0 | 2026-04-14T14:11:12.320000+00:00 | 2026-04-24T14:33:40.685000+00:00 | 240h 22m |
| crash | 3 | 0.12 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 88383.163s median 
  - Expected: 2855.05s in 09-23-26 
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
  - Observed: 167.569s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.199s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.781s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.076s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.144s median 
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
  - Observed: 10.363s median 
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
  - Observed: 30 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
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
  - Observed: 2; 4; C; D; II 
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
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
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
  - Examples: `69cdc965d385e3b94310f777.jsonl[406] _id=69de4a327957a33870f3437d ts=2026-04-14T14:07:46.5700000Z`; `69cdc965d385e3b94310f777.jsonl[746] _id=69e0e9397957a33870f51563 ts=2026-04-16T13:50:48.5790000Z`; `69cdc965d385e3b94310f777.jsonl[1246] _id=69e62e511724f0c9e2f87293 ts=2026-04-20T13:46:57.3060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 30 records, TopographicMapEvent: 20 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 4 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1751 | 0.0 | 2.593 | 495.1 | 45.883 | 340809.081 | 0.12 | 426 | 4 |
| PlayerPositionEvent | 562 | 20.51 | 30.011 | 1541.994 | 36.367 | 340754.368 | 0.04 | 0 | 4 |
| questEvent | 94 | 0.002 | 142.0 | 9221.729 | 961.397 | 340819.552 | 0.01 | 16 | 9 |
| WaterChamberEvent | 35 | 1.251 | 8.781 | 12.818 | 44.024 | 56.807 | 4.68 | 0 | 0 |
| Topographic Map Event | 29 | 5.236 | 15.625 | 11999.209 | 1902.287 | 343450.132 | 0.01 | 0 | 2 |
| TopographicMapEvent | 19 | 1.06 | 5.199 | 18313.835 | 35009.914 | 346843.768 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 17 | 2.697 | 167.569 | 40466.12 | 205207.393 | 341140.567 | 0.0 | 0 | 6 |
| argumentationNodeEvent | 13 | 1.406 | 7.076 | 39788.073 | 206854.366 | 517025.413 | 0.0 | 0 | 1 |
| soilMachine | 13 | 0.829 | 10.363 | 41.925 | 183.86 | 371.07 | 1.43 | 0 | 0 |
| argumentationEvent | 9 | 0.104 | 132.539 | 96076.699 | 379921.559 | 517010.55 | 0.0 | 0 | 3 |
| argumentationToolEvent | 7 | 0.001 | 2.144 | 14.407 | 62.18 | 85.917 | 4.16 | 2 | 0 |
| TerasGardenBox | 6 | 1.537 | 4.114 | 9.159 | 24.172 | 26.744 | 6.55 | 0 | 0 |
| EndOfUnit | 4 | 343.392 | 88383.163 | 216337.091 | 610928.496 | 688238.647 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc965d385e3b94310f777.jsonl[1825] _id=69e8d14b1724f0c9e2fa3a87 ts=? == 69cdc965d385e3b94310f777.jsonl[2109] _id=69e8d8ae1724f0c9e2fa6719 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.011s (p5 29.96s, p95 36.37s, n=562) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `104ms: 69cdc965d385e3b94310f777.jsonl[73] _id=69e62e511724f0c9e2f87291 ts=2026-04-20T13:46:57.2670000Z ~ 69cdc965d385e3b94310f777.jsonl[77] _id=69e62e521724f0c9e2f8729d ts=2026-04-20T13:46:57.3710000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc965d385e3b94310f777.jsonl[2032] _id=69e8d71d1724f0c9e2fa5eb5 ts=2026-04-22T14:11:40.5930000Z ~ 69cdc965d385e3b94310f777.jsonl[2035] _id=69e8d71d1724f0c9e2fa5eb7 ts=2026-04-22T14:11:40.5940000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: 69cdc965d385e3b94310f777.jsonl[2374] _id=69eb7b8d1724f0c9e2fb8eff ts=2026-04-24T14:17:49.0270000Z ~ 69cdc965d385e3b94310f777.jsonl[2398] _id=69eb7b8e1724f0c9e2fb8f03 ts=2026-04-24T14:17:49.0410000Z`; `7ms: 69cdc965d385e3b94310f777.jsonl[2451] _id=69eb7d1d1724f0c9e2fb966f ts=2026-04-24T14:24:28.4090000Z ~ 69cdc965d385e3b94310f777.jsonl[2454] _id=69eb7d1d1724f0c9e2fb9671 ts=2026-04-24T14:24:28.4160000Z`; `2ms: 69cdc965d385e3b94310f777.jsonl[2512] _id=69eb7dfa1724f0c9e2fb9a4d ts=2026-04-24T14:28:09.6650000Z ~ 69cdc965d385e3b94310f777.jsonl[2513] _id=69eb7dfa1724f0c9e2fb9a4f ts=2026-04-24T14:28:09.6670000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `829ms: 69cdc965d385e3b94310f777.jsonl[143] _id=69e8d4361724f0c9e2fa48e5 ts=2026-04-22T13:59:18.1240000Z ~ 69cdc965d385e3b94310f777.jsonl[1896] _id=69e8d4371724f0c9e2fa48e9 ts=2026-04-22T13:59:18.9530000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc965d385e3b94310f777.jsonl[993] _id=69e0f3707957a33870f557bd ts=2026-04-16T14:34:24.2140000Z -> 69cdc965d385e3b94310f777.jsonl[1000] _id=69e626bb1724f0c9e2f84a4f ts=2026-04-20T13:14:33.2950000Z; 47h 28m: 69cdc965d385e3b94310f777.jsonl[2220] _id=69e8db331724f0c9e2fa748f ts=2026-04-22T14:29:07.2860000Z -> 69cdc965d385e3b94310f777.jsonl[2224] _id=69eb76e71724f0c9e2fb76ed ts=2026-04-24T13:57:58.7090000Z; 47h 7m: 69cdc965d385e3b94310f777.jsonl[575] _id=69de4e947957a33870f3616a ts=2026-04-14T14:26:28.3030000Z -> 69cdc965d385e3b94310f777.jsonl[592] _id=69e0e5597957a33870f4fa45 ts=2026-04-16T13:34:16.5410000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 426 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f777.jsonl[1668] _id=69e8cb701724f0c9e2fa11fd ts=2026-04-22T13:21:50.9810000Z -> 69cdc965d385e3b94310f777.jsonl[1674] _id=69e8cb7d1724f0c9e2fa1223 ts=2026-04-22T13:21:50.981Z; 2ms: 69cdc965d385e3b94310f777.jsonl[2077] _id=69e8d7eb1724f0c9e2fa6373 ts=2026-04-22T14:15:06.3170000Z -> 69cdc965d385e3b94310f777.jsonl[161] _id=69e8d7eb1724f0c9e2fa6375 ts=2026-04-22T14:15:06.3190000Z; 3ms: 69cdc965d385e3b94310f777.jsonl[1316] _id=69e62ffd1724f0c9e2f87bed ts=2026-04-20T13:54:04.6360000Z -> 69cdc965d385e3b94310f777.jsonl[1320] _id=69e62ffd1724f0c9e2f87bf5 ts=2026-04-20T13:54:04.6390000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 10m 
  - Evidence: 191h 10m: 69cdc965d385e3b94310f777.jsonl[455] _id=69de4b007957a33870f34935 ts=2026-04-14T14:11:12.3200000Z -> 69cdc965d385e3b94310f777.jsonl[1676] _id=69e8cb6f1724f0c9e2fa11fb ts=2026-04-22T13:21:50.9670000Z; 48h 0m: 69cdc965d385e3b94310f777.jsonl[2212] _id=69e8dac81724f0c9e2fa71eb ts=2026-04-22T14:27:19.6550000Z -> 69cdc965d385e3b94310f777.jsonl[2511] _id=69eb7dee1724f0c9e2fb9a0f ts=2026-04-24T14:27:57.2930000Z; 1h 5m: 69cdc965d385e3b94310f777.jsonl[1676] _id=69e8cb6f1724f0c9e2fa11fb ts=2026-04-22T13:21:50.9670000Z -> 69cdc965d385e3b94310f777.jsonl[2212] _id=69e8dac81724f0c9e2fa71eb ts=2026-04-22T14:27:19.6550000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 39m 
  - Evidence: 94h 39m: 69cdc965d385e3b94310f777.jsonl[995] _id=69e0f3a47957a33870f558cf ts=2026-04-16T14:35:16.1260000Z -> 69cdc965d385e3b94310f777.jsonl[996] _id=69e626b81724f0c9e2f84a4d ts=2026-04-20T13:14:30.4940000Z; 47h 28m: 69cdc965d385e3b94310f777.jsonl[2221] _id=69e8db441724f0c9e2fa74b5 ts=2026-04-22T14:29:23.7670000Z -> 69cdc965d385e3b94310f777.jsonl[2223] _id=69eb76e11724f0c9e2fb76dd ts=2026-04-24T13:57:50.9740000Z; 47h 2m: 69cdc965d385e3b94310f777.jsonl[588] _id=69de4fc07957a33870f36a92 ts=2026-04-14T14:31:28.0150000Z -> 69cdc965d385e3b94310f777.jsonl[589] _id=69e0e5557957a33870f4fa19 ts=2026-04-16T13:34:12.2010000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc965d385e3b94310f777.jsonl[981] _id=69e0f3127957a33870f553a1 ts=2026-04-16T14:32:49.8120000Z -> 69cdc965d385e3b94310f777.jsonl[1014] _id=69e627a71724f0c9e2f84b29 ts=2026-04-20T13:18:30.3790000Z; 47h 33m: 69cdc965d385e3b94310f777.jsonl[1322] _id=69e62fe81724f0c9e2f87b91 ts=2026-04-20T13:53:43.7390000Z -> 69cdc965d385e3b94310f777.jsonl[1706] _id=69e8ccc01724f0c9e2fa196b ts=2026-04-22T13:27:27.8390000Z; 47h 19m: 69cdc965d385e3b94310f777.jsonl[533] _id=69de4d9f7957a33870f35bc9 ts=2026-04-14T14:22:23.5540000Z -> 69cdc965d385e3b94310f777.jsonl[644] _id=69e0e72b7957a33870f5084b ts=2026-04-16T13:42:03.4700000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 69cdc965d385e3b94310f777.jsonl[47] _id=69e0ec5d7957a33870f52755 ts=2026-04-16T14:04:13.4040000Z -> 69cdc965d385e3b94310f777.jsonl[1085] _id=69e629f71724f0c9e2f856ed ts=2026-04-20T13:28:23.5360000Z; 47m 30s: 69cdc965d385e3b94310f777.jsonl[1165] _id=69e62c371724f0c9e2f866d3 ts=2026-04-20T13:37:59.2890000Z -> 69cdc965d385e3b94310f777.jsonl[1567] _id=69e6375a1724f0c9e2f8a94b ts=2026-04-20T14:25:29.8610000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 20m 
  - Evidence: 96h 20m: 69cdc965d385e3b94310f777.jsonl[821] _id=69e0ec5a7957a33870f52741 ts=2026-04-16T14:04:09.6660000Z -> 69cdc965d385e3b94310f777.jsonl[116] _id=69e637351724f0c9e2f8a87d ts=2026-04-20T14:24:53.4340000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 36m 
  - Evidence: 143h 36m: 69cdc965d385e3b94310f777.jsonl[405] _id=69de4a327957a33870f3437b ts=2026-04-14T14:07:46.5330000Z -> 69cdc965d385e3b94310f777.jsonl[1228] _id=69e62dc51724f0c9e2f86fe9 ts=2026-04-20T13:44:37.0830000Z; 48h 24m: 69cdc965d385e3b94310f777.jsonl[77] _id=69e62e521724f0c9e2f8729d ts=2026-04-20T13:46:57.3710000Z -> 69cdc965d385e3b94310f777.jsonl[2036] _id=69e8d7221724f0c9e2fa5ee3 ts=2026-04-22T14:11:45.4430000Z; 48h 3m: 69cdc965d385e3b94310f777.jsonl[2036] _id=69e8d7221724f0c9e2fa5ee3 ts=2026-04-22T14:11:45.4430000Z -> 69cdc965d385e3b94310f777.jsonl[2369] _id=69eb7af11724f0c9e2fb8bbd ts=2026-04-24T14:15:13.0110000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 69cdc965d385e3b94310f777.jsonl[398] _id=69de4a307957a33870f34369 ts=2026-04-14T14:07:44.2970000Z -> 69cdc965d385e3b94310f777.jsonl[1229] _id=69e62dd21724f0c9e2f87027 ts=2026-04-20T13:44:49.7100000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.001s..0.012s shown 
  - Evidence: 1ms: 69cdc965d385e3b94310f777.jsonl[2032] _id=69e8d71d1724f0c9e2fa5eb5 ts=2026-04-22T14:11:40.5930000Z -> 69cdc965d385e3b94310f777.jsonl[2035] _id=69e8d71d1724f0c9e2fa5eb7 ts=2026-04-22T14:11:40.5940000Z; 12ms: 69cdc965d385e3b94310f777.jsonl[2052] _id=69e8d7801724f0c9e2fa6199 ts=2026-04-22T14:13:20.0560000Z -> 69cdc965d385e3b94310f777.jsonl[2053] _id=69e8d7801724f0c9e2fa619b ts=2026-04-22T14:13:20.0680000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc965d385e3b94310f777.jsonl[990] _id=69e0f3697957a33870f55793 ts=2026-04-16T14:34:15.0410000Z -> 69cdc965d385e3b94310f777.jsonl[1001] _id=69e626bc1724f0c9e2f84a53 ts=2026-04-20T13:14:34.5930000Z; 47h 29m: 69cdc965d385e3b94310f777.jsonl[2216] _id=69e8db081724f0c9e2fa73bf ts=2026-04-22T14:28:23.9680000Z -> 69cdc965d385e3b94310f777.jsonl[2222] _id=69eb76e01724f0c9e2fb76d9 ts=2026-04-24T13:57:50.9140000Z; 47h 7m: 69cdc965d385e3b94310f777.jsonl[579] _id=69de4e917957a33870f3614e ts=2026-04-14T14:26:25.3370000Z -> 69cdc965d385e3b94310f777.jsonl[591] _id=69e0e5587957a33870f4fa3a ts=2026-04-16T13:34:14.9790000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.002s..0.007s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f777.jsonl[2512] _id=69eb7dfa1724f0c9e2fb9a4d ts=2026-04-24T14:28:09.6650000Z -> 69cdc965d385e3b94310f777.jsonl[2513] _id=69eb7dfa1724f0c9e2fb9a4f ts=2026-04-24T14:28:09.6670000Z; 6ms: 69cdc965d385e3b94310f777.jsonl[180] _id=69eb78ac1724f0c9e2fb80db ts=2026-04-24T14:05:31.2590000Z -> 69cdc965d385e3b94310f777.jsonl[2287] _id=69eb78ac1724f0c9e2fb80dd ts=2026-04-24T14:05:31.2650000Z; 7ms: 69cdc965d385e3b94310f777.jsonl[2451] _id=69eb7d1d1724f0c9e2fb966f ts=2026-04-24T14:24:28.4090000Z -> 69cdc965d385e3b94310f777.jsonl[2454] _id=69eb7d1d1724f0c9e2fb9671 ts=2026-04-24T14:24:28.4160000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc965d385e3b94310f777.jsonl:69cdc965d385e3b94310f777, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f777.jsonl[533] _id=69de4d9f7957a33870f35bc9 ts=2026-04-14T14:22:23.5540000Z`; `69cdc965d385e3b94310f777.jsonl[645] _id=69e0e72e7957a33870f50859 ts=2026-04-16T13:42:06.4520000Z`; `69cdc965d385e3b94310f777.jsonl[847] _id=69e0ed447957a33870f52cb3 ts=2026-04-16T14:08:04.5320000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 20 record(s) match the trigger in 69cdc965d385e3b94310f777.jsonl:69cdc965d385e3b94310f777, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f777.jsonl[713] _id=69e0e8977957a33870f51187 ts=2026-04-16T13:48:06.8170000Z`; `69cdc965d385e3b94310f777.jsonl[714] _id=69e0e89b7957a33870f511ab ts=2026-04-16T13:48:11.5460000Z`; `69cdc965d385e3b94310f777.jsonl[743] _id=69e0e9427957a33870f51595 ts=2026-04-16T13:50:58.1430000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f777.jsonl[1129] _id=69e62b241724f0c9e2f85e9b ts=2026-04-20T13:33:23.6810000Z`; `69cdc965d385e3b94310f777.jsonl[1157] _id=69e62bc71724f0c9e2f863b7 ts=2026-04-20T13:36:06.6400000Z`; `69cdc965d385e3b94310f777.jsonl[1940] _id=69e8d5501724f0c9e2fa50a1 ts=2026-04-22T14:04:00.0060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f777.jsonl[77] _id=69e62e521724f0c9e2f8729d ts=2026-04-20T13:46:57.3710000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f777.jsonl[2032] _id=69e8d71d1724f0c9e2fa5eb5 ts=2026-04-22T14:11:40.5930000Z`; `69cdc965d385e3b94310f777.jsonl[2035] _id=69e8d71d1724f0c9e2fa5eb7 ts=2026-04-22T14:11:40.5940000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f777.jsonl[1835] _id=69e8d16f1724f0c9e2fa3b87 ts=2026-04-22T13:47:27.2440000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `69cdc965d385e3b94310f777.jsonl[1825] _id=69e8d14b1724f0c9e2fa3a87 ts=?`; `69cdc965d385e3b94310f777.jsonl[2109] _id=69e8d8ae1724f0c9e2fa6719 ts=?`; `69cdc965d385e3b94310f777.jsonl[2261] _id=69eb77ff1724f0c9e2fb7cb9 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f777.jsonl[920] _id=69e0f0e27957a33870f541b7 ts=2026-04-16T14:23:30.1240000Z`; `69cdc965d385e3b94310f777.jsonl[937] _id=69e0f18a7957a33870f54621 ts=2026-04-16T14:26:17.3790000Z`; `69cdc965d385e3b94310f777.jsonl[957] _id=69e0f2267957a33870f54b3f ts=2026-04-16T14:28:54.0090000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 161 unmatched 'DialogueStartEvent' (totals: 343 start, 185 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'Started' (totals: 13 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 32 unmatched 'questActiveEvent' (totals: 63 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.52s, min -14.14s, max -0.17s over 2583 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f777\coverage.yaml

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
  - Observed: 30 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1752 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (405); Unit 3 Dev (327); Unit 5 Dev (241); Unit 4 Dev (213); Unit 1 Dev (184); Unit 3 Dungeon Dev (155); Unit 4 Dev - Dungeon (119); Unit 4 Dev - Anderson Base (71); Unit 5 Dev - Dungeon (37)
- **eventKey:** present on 1224 of 1752 records
- **Intervals:** median 2.59s (p5 0.01s / p95 45.88s, n=1751)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1224; [conversationId, dialogueEventType] x528
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1752/1752 records)
    numeric range 10 .. 114 (45 unique)
data.dialogueEventType  (string, 1752/1752 records)
    "DialogueNodeEvent"  x1224
    "DialogueStartEvent"  x343
    "DialogueFinishEvent"  x185
data.nodeId  (number, 1224/1752 records)
    numeric range 0 .. 289 (207 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 574 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (175); Unit 3 Dev (85); Unit 4 Dev - Dungeon (59); Unit 4 Dev (58); Unit 3 Dungeon Dev (57); Unit 1 Dev (54); Unit 5 Dev (46); Unit 5 Dev - Dungeon (27); Unit 4 Dev - Anderson Base (13)
- **Intervals:** median 30.01s (p5 29.96s / p95 36.37s, n=562)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 574/574 records)
data.position.x  (number, 574/574 records)
    numeric range -695.009 .. 1558.56 (359 unique)
data.position.y  (number, 574/574 records)
    numeric range -114.078 .. 219.432 (300 unique)
data.position.z  (number, 574/574 records)
    numeric range -1115.42 .. 2061.54 (359 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 95 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev - Dungeon (13); Unit 1 Dev (12); Unit 5 Dev (12); Unit 3 Dev (10); Unit 4 Dev (8); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 95 of 95 records
- **Intervals:** median 142.00s (p5 0.01s / p95 961.40s, n=94)
- **`data` key-set variants:** [questEventType, questID, questName] x63; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 95/95 records)
    "questActiveEvent"  x63
    "questFinishEvent"  x32
data.questID  (string, 95/95 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 95/95 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/95 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 36 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (36)
- **Intervals:** median 8.78s (p5 1.53s / p95 44.02s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "On"  x23
    "Off"  x13
data.floor  (string, 36/36 records)
    "4"  x20
    "3"  x8
    "1"  x5
    "2"  x3
data.machineNumber  (string, 36/36 records)
    "One"  x35
    "Two"  x1
data.machineType  (string, 36/36 records)
    "Condenser"  x19
    "Evaporator"  x12
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 36/36 records)
    "3"  x18
    "2"  x12
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `Topographic Map Event` — 30 records

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (14)
- **Intervals:** median 15.62s (p5 5.86s / p95 1902.29s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "MapCloseEvent"  x15
    "MapOpenEvent"  x15
data.featureUsed  (string, 30/30 records)
    "Map"  x30
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 20 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (10)
- **Intervals:** median 5.20s (p5 1.55s / p95 35009.91s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "dragEnd"  x10
    "dragStart"  x10
data.featureUsed  (string, 20/20 records)
    "waypoint"  x20
data.location  (object, 20/20 records)
data.location.x  (number, 20/20 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 20/20 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 20/20 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 18 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 167.57s (p5 2.93s / p95 205207.39s, n=17)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 18/18 records)
    "Started"  x13
    "Finished"  x5
data.Unit  (string, 18/18 records)
    "Unit 2 Prod (Refactor)"  x14
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 14 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (9); Unit 1 Dev (5)
- **Intervals:** median 7.08s (p5 1.55s / p95 206854.37s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationNodeAdd"  x11
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 14/14 records)
    "1"  x4
    "5"  x3
    "3"  x2
    "A"  x2
    "I"  x2
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 14 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (14)
- **Intervals:** median 10.36s (p5 1.31s / p95 183.86s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "ChangeCanister"  x14
data.canisterType  (string, 14/14 records)
    "Bedrock"  x7
    "Clay"  x4
    "Sand"  x2
    "Gravel"  x1
data.floor  (string, 14/14 records)
    "5"  x13
    "4"  x1
data.machine  (string, 14/14 records)
    "1"  x12
    "2"  x2
data.row  (string, 14/14 records)
    "BottomRow"  x8
    "TopRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 132.54s (p5 12.72s / p95 379921.56s, n=9)
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

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (8)
- **Intervals:** median 2.14s (p5 0.00s / p95 62.18s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolClose"  x5
    "argumentationToolOpen"  x3
data.argumentationTitle  (string, 8/8 records)
    "Unit 4 - Flooding"  x8
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 4.11s (p5 1.65s / p95 24.17s, n=6)
- **`data` key-set variants:** [actionType, boxID, soilType] x4; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "soilSelected"  x4
    "cameraPlaced"  x3
data.boxID  (string, 4/7 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.boxId  (string, 3/7 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 7/7 records)
    "Gravel"  x3
    "Clay"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 5 Dev (2); Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 88383.16s (p5 881.19s / p95 610928.50s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "5"  x2
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Uncaught ReferenceError: onResize is not defined"  x3
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit5:831:9)"  x1
data.type  (string, 3/3 records)
    "runtime_error"  x3
data.unitId  (string, 3/3 records)
    "unit4"  x2
    "unit5"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
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
- `crash` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (14 records)
- `TopographicMapEvent` data.actionType: "dragStart" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (7x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*