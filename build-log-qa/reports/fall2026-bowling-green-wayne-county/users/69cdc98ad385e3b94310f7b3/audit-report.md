# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b3

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7b3
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7b3.jsonl
- **Records:** 2744 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7b3
- **Time span:** 2026-04-16T19:22:06.669000+00:00 .. 2026-05-01T14:29:07.436000+00:00 (355h 7m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b3\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2744 records, 8 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 69 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1850 | 67.42 | 1 | 8 | 1297 | 2026-04-16T19:22:24.693000+00:00 | 2026-05-01T14:25:19.875000+00:00 | 355h 2m |
| PlayerPositionEvent | 538 | 19.61 | 1 | 8 | 0 | 2026-04-16T19:22:06.669000+00:00 | 2026-05-01T14:29:07.436000+00:00 | 355h 7m |
| soilMachine | 73 | 2.66 | 1 | 1 | 0 | 2026-04-24T19:18:12.495000+00:00 | 2026-04-24T19:27:21.809000+00:00 | 9m 9s |
| questEvent | 68 | 2.48 | 1 | 8 | 68 | 2026-04-16T19:22:24.678000+00:00 | 2026-05-01T14:27:21.568000+00:00 | 355h 4m |
| Topographic Map Event | 60 | 2.19 | 1 | 2 | 0 | 2026-04-16T19:51:41.738000+00:00 | 2026-04-24T18:56:29.914000+00:00 | 191h 4m |
| WaterChamberEvent | 52 | 1.9 | 1 | 1 | 0 | 2026-04-24T20:02:34.257000+00:00 | 2026-05-01T14:28:59.763000+00:00 | 162h 26m |
| argumentationNodeEvent | 52 | 1.9 | 1 | 3 | 0 | 2026-04-16T19:43:59.773000+00:00 | 2026-04-22T19:41:00.259000+00:00 | 143h 57m |
| argumentationToolEvent | 20 | 0.73 | 1 | 2 | 0 | 2026-04-22T18:59:46.407000+00:00 | 2026-04-24T19:45:14.986000+00:00 | 48h 45m |
| argumentationEvent | 10 | 0.36 | 1 | 4 | 0 | 2026-04-16T19:43:53.221000+00:00 | 2026-04-24T19:40:23.926000+00:00 | 191h 56m |
| Soil Key Puzzle | 6 | 0.22 | 1 | 3 | 0 | 2026-04-20T19:22:00.855000+00:00 | 2026-04-24T19:07:23.554000+00:00 | 95h 45m |
| TopographicMapEvent | 5 | 0.18 | 1 | 2 | 0 | 2026-04-20T19:06:43.093000+00:00 | 2026-04-22T20:00:40.869000+00:00 | 48h 53m |
| EndOfUnit | 4 | 0.15 | 1 | 4 | 0 | 2026-04-16T19:49:19.996000+00:00 | 2026-04-24T19:57:15.116000+00:00 | 192h 7m |
| TerasGardenBox | 4 | 0.15 | 1 | 1 | 0 | 2026-04-24T19:50:05.621000+00:00 | 2026-04-24T19:50:34.226000+00:00 | 28.6s |
| crash | 2 | 0.07 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172484.184s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.004s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 120.303s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 10.953s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 33.09s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 2.948s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.44s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.738s median 
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
  - Observed: 1.885s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
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
  - Observed: 60 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
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
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
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
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 14.6x vs baseline. 
  - Observed: 73 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 15 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[44] _id=69e13c881724f0c9e2f6fcb6 ts=2026-04-16T19:46:15.8330000Z`; `69cdc98ad385e3b94310f7b3.jsonl[130] _id=69e67a9d1724f0c9e2f8ce71 ts=2026-04-20T19:12:28.2640000Z`; `69cdc98ad385e3b94310f7b3.jsonl[1724] _id=69e918641724f0c9e2fa82d9 ts=2026-04-22T18:49:57.3650000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 60 records, TopographicMapEvent: 5 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1849 | 0.0 | 3.211 | 691.279 | 32.727 | 584304.86 | 0.09 | 452 | 4 |
| PlayerPositionEvent | 527 | 29.74 | 30.004 | 2425.12 | 33.271 | 584309.869 | 0.02 | 0 | 4 |
| soilMachine | 72 | 0.206 | 1.885 | 7.629 | 38.02 | 105.465 | 7.86 | 0 | 0 |
| questEvent | 67 | 0.003 | 186.829 | 19079.058 | 118468.674 | 584286.997 | 0.0 | 12 | 9 |
| Topographic Map Event | 59 | 0.521 | 3.004 | 11659.122 | 19130.577 | 342889.195 | 0.01 | 0 | 6 |
| WaterChamberEvent | 51 | 0.006 | 2.948 | 11466.382 | 21.139 | 584465.159 | 0.01 | 1 | 1 |
| argumentationNodeEvent | 51 | 1.035 | 5.44 | 10161.186 | 54.606 | 515613.796 | 0.01 | 0 | 2 |
| argumentationToolEvent | 19 | 0.002 | 0.738 | 9238.346 | 17781.694 | 175226.798 | 0.01 | 6 | 1 |
| argumentationEvent | 9 | 0.169 | 122.331 | 76776.745 | 378465.95 | 515601.69 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 5 | 20.617 | 120.303 | 68944.54 | 173384.692 | 174123.28 | 0.0 | 0 | 2 |
| TopographicMapEvent | 4 | 1.693 | 33.09 | 44009.444 | 149583.837 | 175969.902 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 3335.884 | 172484.184 | 230558.373 | 481517.965 | 515855.052 | 0.0 | 0 | 3 |
| TerasGardenBox | 3 | 4.223 | 10.953 | 9.535 | 13.181 | 13.429 | 6.29 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.004s (p5 29.95s, p95 33.27s, n=527) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `945ms: 69cdc98ad385e3b94310f7b3.jsonl[2739] _id=69f4b8ab1724f0c9e2fdc6f7 ts=2026-05-01T14:28:58.8180000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[2740] _id=69f4b8ac1724f0c9e2fdc6fb ts=2026-05-01T14:28:59.7630000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `169ms: 69cdc98ad385e3b94310f7b3.jsonl[2036] _id=69e9244d1724f0c9e2fab035 ts=2026-04-22T19:41:01.4170000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[394] _id=69e9244e1724f0c9e2fab03b ts=2026-04-22T19:41:01.5860000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `929ms: 69cdc98ad385e3b94310f7b3.jsonl[295] _id=69e91aa31724f0c9e2fa8bfb ts=2026-04-22T18:59:47.4040000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[281] _id=69e91aa41724f0c9e2fa8bff ts=2026-04-22T18:59:48.3330000Z`; `748ms: 69cdc98ad385e3b94310f7b3.jsonl[1810] _id=69e91aa61724f0c9e2fa8c19 ts=2026-04-22T18:59:50.1240000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[288] _id=69e91aa71724f0c9e2fa8c1d ts=2026-04-22T18:59:50.8720000Z`; `746ms: 69cdc98ad385e3b94310f7b3.jsonl[287] _id=69e91aa61724f0c9e2fa8c1b ts=2026-04-22T18:59:50.1340000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[297] _id=69e91aa71724f0c9e2fa8c1f ts=2026-04-22T18:59:50.8800000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `833ms: 69cdc98ad385e3b94310f7b3.jsonl[531] _id=69ebc2901724f0c9e2fbb9b9 ts=2026-04-24T19:20:48.3240000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[2336] _id=69ebc2911724f0c9e2fbb9bb ts=2026-04-24T19:20:49.1570000Z`; `953ms: 69cdc98ad385e3b94310f7b3.jsonl[2363] _id=69ebc3281724f0c9e2fbbaed ts=2026-04-24T19:23:19.7080000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[580] _id=69ebc3291724f0c9e2fbbaf1 ts=2026-04-24T19:23:20.6610000Z`; `796ms: 69cdc98ad385e3b94310f7b3.jsonl[580] _id=69ebc3291724f0c9e2fbbaf1 ts=2026-04-24T19:23:20.6610000Z ~ 69cdc98ad385e3b94310f7b3.jsonl[581] _id=69ebc32a1724f0c9e2fbbaf3 ts=2026-04-24T19:23:21.4570000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 162h 18m 
  - Evidence: 162h 18m: 69cdc98ad385e3b94310f7b3.jsonl[2661] _id=69ebcca61724f0c9e2fbcaed ts=2026-04-24T20:03:49.6980000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2681] _id=69f4b7171724f0c9e2fdc5ad ts=2026-05-01T14:22:14.5580000Z; 94h 41m: 69cdc98ad385e3b94310f7b3.jsonl[1224] _id=69e1419d1724f0c9e2f71276 ts=2026-04-16T20:07:56.3510000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1244] _id=69e675451724f0c9e2f8b761 ts=2026-04-20T18:49:40.1750000Z; 46h 53m: 69cdc98ad385e3b94310f7b3.jsonl[2196] _id=69e928d71724f0c9e2fac099 ts=2026-04-22T20:00:23.5440000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2213] _id=69ebbc4c1724f0c9e2fbb0e3 ts=2026-04-24T18:54:04.2370000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 452 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7b3.jsonl[1900] _id=69e91c4f1724f0c9e2fa9375 ts=2026-04-22T19:06:55.0660000Z -> 69cdc98ad385e3b94310f7b3.jsonl[331] _id=69e91c5c1724f0c9e2fa93b3 ts=2026-04-22T19:06:55.066Z; 0ms: 69cdc98ad385e3b94310f7b3.jsonl[2260] _id=69ebbe141724f0c9e2fbb41d ts=2026-04-24T19:01:39.2450000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2264] _id=69ebbe201724f0c9e2fbb439 ts=2026-04-24T19:01:39.245Z; 0ms: 69cdc98ad385e3b94310f7b3.jsonl[814] _id=69ebcb1b1724f0c9e2fbc94b ts=2026-04-24T19:57:15.1310000Z -> 69cdc98ad385e3b94310f7b3.jsonl[815] _id=69ebcb421724f0c9e2fbc961 ts=2026-04-24T19:57:15.131Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 17m 
  - Evidence: 143h 17m: 69cdc98ad385e3b94310f7b3.jsonl[1130] _id=69e13d401724f0c9e2f700b0 ts=2026-04-16T19:49:19.9960000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1901] _id=69e91c4f1724f0c9e2fa936f ts=2026-04-22T19:06:55.0480000Z; 47h 54m: 69cdc98ad385e3b94310f7b3.jsonl[1901] _id=69e91c4f1724f0c9e2fa936f ts=2026-04-22T19:06:55.0480000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2259] _id=69ebbe131724f0c9e2fbb41b ts=2026-04-24T19:01:39.2320000Z; 55m 35s: 69cdc98ad385e3b94310f7b3.jsonl[2259] _id=69ebbe131724f0c9e2fbb41b ts=2026-04-24T19:01:39.2320000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2639] _id=69ebcb1b1724f0c9e2fbc949 ts=2026-04-24T19:57:15.1160000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 162h 18m 
  - Evidence: 162h 18m: 69cdc98ad385e3b94310f7b3.jsonl[2671] _id=69ebcc961724f0c9e2fbcadb ts=2026-04-24T20:03:33.5870000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2683] _id=69f4b70d1724f0c9e2fdc5a5 ts=2026-05-01T14:22:03.4560000Z; 94h 41m: 69cdc98ad385e3b94310f7b3.jsonl[1221] _id=69e141a11724f0c9e2f7128e ts=2026-04-16T20:08:00.9200000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1242] _id=69e675411724f0c9e2f8b759 ts=2026-04-20T18:49:36.0560000Z; 46h 49m: 69cdc98ad385e3b94310f7b3.jsonl[2206] _id=69e929a81724f0c9e2fac397 ts=2026-04-22T20:03:52.0260000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2210] _id=69ebbc091724f0c9e2fbb049 ts=2026-04-24T18:52:56.9260000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 48h 22m 
  - Evidence: 48h 22m: 69cdc98ad385e3b94310f7b3.jsonl[1440] _id=69e67d511724f0c9e2f8db5d ts=2026-04-20T19:24:01.1580000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2075] _id=69e9257c1724f0c9e2fab4e7 ts=2026-04-22T19:46:04.4380000Z; 47h 20m: 69cdc98ad385e3b94310f7b3.jsonl[2078] _id=69e925981724f0c9e2fab54b ts=2026-04-22T19:46:32.5970000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2290] _id=69ebbf571724f0c9e2fbb5e1 ts=2026-04-24T19:07:02.9370000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 14m 
  - Evidence: 95h 14m: 69cdc98ad385e3b94310f7b3.jsonl[1135] _id=69e13dcf1724f0c9e2f702ca ts=2026-04-16T19:51:42.7560000Z -> 69cdc98ad385e3b94310f7b3.jsonl[121] _id=69e679391724f0c9e2f8c81d ts=2026-04-20T19:06:31.9510000Z; 47h 13m: 69cdc98ad385e3b94310f7b3.jsonl[217] _id=69e685451724f0c9e2f8fb4b ts=2026-04-20T19:57:56.9280000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1931] _id=69e91d701724f0c9e2fa97ed ts=2026-04-22T19:11:44.5150000Z; 46h 53m: 69cdc98ad385e3b94310f7b3.jsonl[2200] _id=69e928f11724f0c9e2fac105 ts=2026-04-22T20:00:49.2840000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2215] _id=69ebbc6c1724f0c9e2fbb15b ts=2026-04-24T18:54:36.2120000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 52m 
  - Evidence: 48h 52m: 69cdc98ad385e3b94310f7b3.jsonl[111] _id=69e679431724f0c9e2f8c845 ts=2026-04-20T19:06:43.0930000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2188] _id=69e928a51724f0c9e2fabf97 ts=2026-04-22T19:59:32.9950000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 162h 21m 
  - Evidence: 162h 21m: 69cdc98ad385e3b94310f7b3.jsonl[2676] _id=69ebcc9a1724f0c9e2fbcae1 ts=2026-04-24T20:03:38.0520000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2709] _id=69f4b7ac1724f0c9e2fdc64b ts=2026-05-01T14:24:43.2110000Z
- **INFO / Info** `WaterChamberEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 69cdc98ad385e3b94310f7b3.jsonl[833] _id=69f4b80c1724f0c9e2fdc67f ts=2026-05-01T14:26:19.7610000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2697] _id=69f4b80c1724f0c9e2fdc681 ts=2026-05-01T14:26:19.7670000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 13m 
  - Evidence: 143h 13m: 69cdc98ad385e3b94310f7b3.jsonl[43] _id=69e13c881724f0c9e2f6fcb4 ts=2026-04-16T19:46:15.8070000Z -> 69cdc98ad385e3b94310f7b3.jsonl[279] _id=69e91a991724f0c9e2fa8be1 ts=2026-04-22T18:59:37.4970000Z; 47h 59m: 69cdc98ad385e3b94310f7b3.jsonl[394] _id=69e9244e1724f0c9e2fab03b ts=2026-04-22T19:41:01.5860000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2495] _id=69ebc7281724f0c9e2fbc235 ts=2026-04-24T19:40:23.9260000Z; 37m 9s: 69cdc98ad385e3b94310f7b3.jsonl[321] _id=69e91b131724f0c9e2fa8e1d ts=2026-04-22T19:01:39.8280000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2005] _id=69e923c91724f0c9e2faae5b ts=2026-04-22T19:38:48.9030000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 13m 
  - Evidence: 143h 13m: 69cdc98ad385e3b94310f7b3.jsonl[1088] _id=69e13c7f1724f0c9e2f6fc8c ts=2026-04-16T19:46:06.9290000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1808] _id=69e91a9c1724f0c9e2fa8bf1 ts=2026-04-22T18:59:40.7250000Z; 37m 17s: 69cdc98ad385e3b94310f7b3.jsonl[320] _id=69e91b121724f0c9e2fa8e17 ts=2026-04-22T19:01:38.5630000Z -> 69cdc98ad385e3b94310f7b3.jsonl[361] _id=69e923d01724f0c9e2faae79 ts=2026-04-22T19:38:55.9550000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 40m 
  - Evidence: 48h 40m: 69cdc98ad385e3b94310f7b3.jsonl[291] _id=69e91aab1724f0c9e2fa8c2d ts=2026-04-22T18:59:55.0870000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2499] _id=69ebc7261724f0c9e2fbc231 ts=2026-04-24T19:40:21.8850000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.002s..0.010s shown 
  - Evidence: 2ms: 69cdc98ad385e3b94310f7b3.jsonl[2499] _id=69ebc7261724f0c9e2fbc231 ts=2026-04-24T19:40:21.8850000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2494] _id=69ebc7261724f0c9e2fbc233 ts=2026-04-24T19:40:21.8870000Z; 8ms: 69cdc98ad385e3b94310f7b3.jsonl[288] _id=69e91aa71724f0c9e2fa8c1d ts=2026-04-22T18:59:50.8720000Z -> 69cdc98ad385e3b94310f7b3.jsonl[297] _id=69e91aa71724f0c9e2fa8c1f ts=2026-04-22T18:59:50.8800000Z; 10ms: 69cdc98ad385e3b94310f7b3.jsonl[1810] _id=69e91aa61724f0c9e2fa8c19 ts=2026-04-22T18:59:50.1240000Z -> 69cdc98ad385e3b94310f7b3.jsonl[287] _id=69e91aa61724f0c9e2fa8c1b ts=2026-04-22T18:59:50.1340000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 162h 18m 
  - Evidence: 162h 18m: 69cdc98ad385e3b94310f7b3.jsonl[2679] _id=69ebccaf1724f0c9e2fbcaf3 ts=2026-04-24T20:03:58.7720000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2680] _id=69f4b70f1724f0c9e2fdc5a9 ts=2026-05-01T14:22:05.7690000Z; 94h 48m: 69cdc98ad385e3b94310f7b3.jsonl[1184] _id=69e13ff81724f0c9e2f70ad0 ts=2026-04-16T20:00:54.8320000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1243] _id=69e675431724f0c9e2f8b75d ts=2026-04-20T18:49:38.7480000Z; 47h 14m: 69cdc98ad385e3b94310f7b3.jsonl[1512] _id=69e67fe91724f0c9e2f8e797 ts=2026-04-20T19:35:04.6860000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1720] _id=69e9183d1724f0c9e2fa829b ts=2026-04-22T18:49:32.9600000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7b3.jsonl[37] _id=69e13b991724f0c9e2f6f826 ts=2026-04-16T19:42:16.3040000Z -> 69cdc98ad385e3b94310f7b3.jsonl[1039] _id=69e13b991724f0c9e2f6f828 ts=2026-04-16T19:42:16.3070000Z; 4ms: 69cdc98ad385e3b94310f7b3.jsonl[2712] _id=69f4b7c91724f0c9e2fdc65b ts=2026-05-01T14:25:12.5980000Z -> 69cdc98ad385e3b94310f7b3.jsonl[827] _id=69f4b7c91724f0c9e2fdc65d ts=2026-05-01T14:25:12.6020000Z; 6ms: 69cdc98ad385e3b94310f7b3.jsonl[826] _id=69f4b84a1724f0c9e2fdc6ad ts=2026-05-01T14:27:21.5620000Z -> 69cdc98ad385e3b94310f7b3.jsonl[2732] _id=69f4b84a1724f0c9e2fdc6af ts=2026-05-01T14:27:21.5680000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7b3.jsonl:69cdc98ad385e3b94310f7b3, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[1440] _id=69e67d511724f0c9e2f8db5d ts=2026-04-20T19:24:01.1580000Z`; `69cdc98ad385e3b94310f7b3.jsonl[2078] _id=69e925981724f0c9e2fab54b ts=2026-04-22T19:46:32.5970000Z`; `69cdc98ad385e3b94310f7b3.jsonl[2285] _id=69ebbf6c1724f0c9e2fbb609 ts=2026-04-24T19:07:23.5540000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc98ad385e3b94310f7b3.jsonl:69cdc98ad385e3b94310f7b3, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[111] _id=69e679431724f0c9e2f8c845 ts=2026-04-20T19:06:43.0930000Z`; `69cdc98ad385e3b94310f7b3.jsonl[2188] _id=69e928a51724f0c9e2fabf97 ts=2026-04-22T19:59:32.9950000Z`; `69cdc98ad385e3b94310f7b3.jsonl[2190] _id=69e928a81724f0c9e2fabfa9 ts=2026-04-22T19:59:36.3710000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[1528] _id=69e6807c1724f0c9e2f8e9ff ts=2026-04-20T19:37:32.0890000Z`; `69cdc98ad385e3b94310f7b3.jsonl[895] _id=69e91eea1724f0c9e2fa9df3 ts=2026-04-22T19:18:02.4170000Z`; `69cdc98ad385e3b94310f7b3.jsonl[1382] _id=69e9208d1724f0c9e2faa137 ts=2026-04-22T19:25:00.6610000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[394] _id=69e9244e1724f0c9e2fab03b ts=2026-04-22T19:41:01.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[2499] _id=69ebc7261724f0c9e2fbc231 ts=2026-04-24T19:40:21.8850000Z`; `69cdc98ad385e3b94310f7b3.jsonl[2494] _id=69ebc7261724f0c9e2fbc233 ts=2026-04-24T19:40:21.8870000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc98ad385e3b94310f7b3.jsonl[1712] _id=69e921b61724f0c9e2faa5f1 ts=?`; `69cdc98ad385e3b94310f7b3.jsonl[2682] _id=69f4b74d1724f0c9e2fdc5c5 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 157 unmatched 'DialogueStartEvent' (totals: 353 start, 200 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 39 start, 29 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.64s, min -39.63s, max -0.06s over 2742 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7b3\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 60 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1850 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (692); Unit 3 Dev (362); Unit 4 Dev (218); Unit 1 Dev (190); Unit 4 Dev - Anderson Base (168); Unit 4 Dev - Dungeon (90); Unit 3 Dungeon Dev (89); Unit 5 Dev - Dungeon (41)
- **eventKey:** present on 1297 of 1850 records
- **Intervals:** median 3.21s (p5 0.01s / p95 32.73s, n=1849)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1297; [conversationId, dialogueEventType] x553
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1850/1850 records)
    numeric range 8 .. 114 (45 unique)
data.dialogueEventType  (string, 1850/1850 records)
    "DialogueNodeEvent"  x1297
    "DialogueStartEvent"  x353
    "DialogueFinishEvent"  x200
data.nodeId  (number, 1297/1850 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 538 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (215); Unit 3 Dev (106); Unit 1 Dev (55); Unit 4 Dev (52); Unit 4 Dev - Dungeon (37); Unit 5 Dev - Dungeon (27); Unit 3 Dungeon Dev (23); Unit 4 Dev - Anderson Base (23)
- **Intervals:** median 30.00s (p5 29.95s / p95 33.27s, n=527)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 538/538 records)
data.position.x  (number, 538/538 records)
    numeric range -722.071 .. 1558.16 (249 unique)
data.position.y  (number, 538/538 records)
    numeric range -112.487 .. 217.708 (200 unique)
data.position.z  (number, 538/538 records)
    numeric range -1103.07 .. 2041.33 (249 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `soilMachine` — 73 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (73)
- **Intervals:** median 1.89s (p5 0.33s / p95 38.02s, n=72)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 73/73 records)
    "ChangeCanister"  x73
data.canisterType  (string, 73/73 records)
    "Bedrock"  x38
    "Clay"  x30
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 73/73 records)
    "5"  x64
    "4"  x8
    "3"  x1
data.machine  (string, 73/73 records)
    "1"  x72
    "2"  x1
data.row  (string, 73/73 records)
    "BottomRow"  x43
    "TopRow"  x30
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `questEvent` — 68 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (12); Unit 3 Dev (10); Unit 5 Dev - Dungeon (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 68 of 68 records
- **Intervals:** median 186.83s (p5 0.01s / p95 118468.67s, n=67)
- **`data` key-set variants:** [questEventType, questID, questName] x39; [questEventType, questID, questName, questSuccessOrFailure] x29
- **Fields under `data`:**

```text
data.questEventType  (string, 68/68 records)
    "questActiveEvent"  x39
    "questFinishEvent"  x29
data.questID  (string, 68/68 records)
    31 unique values (see csv/event_unique_values.csv)
data.questName  (string, 68/68 records)
    31 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 29/68 records)
    "Succeeded"  x29
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 60 records

- **Scenes:** Unit 3 Dev (48); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 3.00s (p5 0.73s / p95 19130.58s, n=59)
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "MapCloseEvent"  x30
    "MapOpenEvent"  x30
data.featureUsed  (string, 60/60 records)
    "Map"  x60
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 52 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (52)
- **Intervals:** median 2.95s (p5 0.51s / p95 21.14s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "On"  x32
    "Off"  x20
data.floor  (string, 52/52 records)
    "4"  x24
    "3"  x15
    "1"  x10
    "2"  x3
data.machineNumber  (string, 52/52 records)
    "One"  x51
    "Two"  x1
data.machineType  (string, 52/52 records)
    "Condenser"  x32
    "Evaporator"  x14
    "DualChamber_Evaporator"  x4
    "DualChamber_Condenser"  x1
    "VentSwitch"  x1
data.room  (string, 52/52 records)
    "3"  x26
    "2"  x18
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 52 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 3 Dev (17); Unit 1 Dev (12)
- **Intervals:** median 5.44s (p5 1.15s / p95 54.61s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x20
data.argumentationTitle  (string, 52/52 records)
    "Unit 2 – Watershed"  x23
    "Unit 3 - Pollution Upstream"  x17
    "Unit 1 - Freshwater"  x9
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 52/52 records)
    "1"  x11
    "A"  x9
    "B"  x7
    "I"  x7
    "4"  x4
    "C"  x4
    "D"  x4
    "II"  x3
    "3"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 4 Dev - Anderson Base (8)
- **Intervals:** median 0.74s (p5 0.01s / p95 17781.69s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolClose"  x11
    "argumentationToolOpen"  x9
data.argumentationTitle  (string, 20/20 records)
    "Unit 2 – Watershed"  x12
    "Unit 4 - Flooding"  x8
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Waterfall Data"  x8
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - Watershed Graph"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 122.33s (p5 15.67s / p95 378465.95s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 120.30s (p5 22.13s / p95 173384.69s, n=5)
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

### `TopographicMapEvent` — 5 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 33.09s (p5 1.95s / p95 149583.84s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "dragStart"  x3
    "dragEnd"  x2
data.featureUsed  (string, 5/5 records)
    "waypoint"  x5
data.location  (object, 5/5 records)
data.location.x  (number, 5/5 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/5 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/5 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 172484.18s (p5 20250.71s / p95 481517.97s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 4 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (4)
- **Intervals:** median 10.95s (p5 4.90s / p95 13.18s, n=3)
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

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit5:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit3"  x1
    "unit5"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
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
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "dragStart" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (20x)
- `soilMachine` data.canisterType: "Bedrock" (38x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*