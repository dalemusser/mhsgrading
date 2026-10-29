# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f738

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f738
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f738.jsonl
- **Records:** 2660 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f738
- **Time span:** 2026-04-13T17:53:02.392000+00:00 .. 2026-04-23T18:41:43.633000+00:00 (240h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f738\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2660 records, 8 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 67 INFO, 0 NOT_TESTED, 49 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `WaterChamberEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1854 | 69.7 | 1 | 8 | 1296 | 2026-04-13T17:53:20.883000+00:00 | 2026-04-23T18:39:35.104000+00:00 | 240h 46m |
| PlayerPositionEvent | 567 | 21.32 | 1 | 8 | 0 | 2026-04-13T17:53:02.392000+00:00 | 2026-04-23T18:41:43.633000+00:00 | 240h 48m |
| questEvent | 70 | 2.63 | 1 | 8 | 70 | 2026-04-13T17:53:20.864000+00:00 | 2026-04-23T18:38:40.349000+00:00 | 240h 45m |
| argumentationNodeEvent | 45 | 1.69 | 1 | 3 | 0 | 2026-04-13T18:06:17.329000+00:00 | 2026-04-21T17:04:39.391000+00:00 | 190h 58m |
| Topographic Map Event | 32 | 1.2 | 1 | 2 | 0 | 2026-04-13T18:18:47.975000+00:00 | 2026-04-21T18:24:22.386000+00:00 | 192h 5m |
| argumentationToolEvent | 22 | 0.83 | 1 | 3 | 0 | 2026-04-17T18:16:37.385000+00:00 | 2026-04-23T18:31:34.214000+00:00 | 144h 14m |
| TopographicMapEvent | 20 | 0.75 | 1 | 2 | 0 | 2026-04-17T17:06:04.326000+00:00 | 2026-04-21T18:24:21.026000+00:00 | 97h 18m |
| soilMachine | 15 | 0.56 | 1 | 1 | 0 | 2026-04-23T18:09:35.102000+00:00 | 2026-04-23T18:16:51.732000+00:00 | 7m 16s |
| Soil Key Puzzle | 12 | 0.45 | 1 | 3 | 0 | 2026-04-13T18:25:24.358000+00:00 | 2026-04-21T18:33:08.221000+00:00 | 192h 7m |
| argumentationEvent | 10 | 0.38 | 1 | 4 | 0 | 2026-04-13T18:05:27.839000+00:00 | 2026-04-23T18:29:13.635000+00:00 | 240h 23m |
| TerasGardenBox | 6 | 0.23 | 1 | 1 | 0 | 2026-04-23T18:33:59.136000+00:00 | 2026-04-23T18:35:05.873000+00:00 | 1m 6s |
| EndOfUnit | 5 | 0.19 | 1 | 4 | 0 | 2026-04-13T18:10:12.361000+00:00 | 2026-04-23T18:38:18.039000+00:00 | 240h 28m |
| crash | 2 | 0.08 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.644s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 259631.109s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.025s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 53.544s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.053s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.728s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.85s median 
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
  - Observed: 16.79s median 
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
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
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
  - Observed: 32 records this build 
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
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 45 records 
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
  - Observed: C; D 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 51; 52; 53; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
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
  - Observed: 22 mismatch(es); e.g. 'DialogueNodeEvent:31:51' vs expected 'DialogueNodeEvent:31:70' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f738.jsonl[475] _id=69dd30697957a33870f258be ts=2026-04-13T18:05:27.7780000Z`; `69cdc907d385e3b94310f738.jsonl[21] _id=69dd30697957a33870f258c2 ts=2026-04-13T18:05:27.9810000Z`; `69cdc907d385e3b94310f738.jsonl[476] _id=69dd30697957a33870f258c4 ts=2026-04-13T18:05:28.2130000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 32 records, TopographicMapEvent: 20 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1853 | 0.0 | 1.644 | 467.768 | 33.902 | 339459.221 | 0.13 | 458 | 6 |
| PlayerPositionEvent | 556 | 29.814 | 30.025 | 1558.644 | 34.491 | 339383.432 | 0.04 | 0 | 3 |
| questEvent | 69 | 0.003 | 128.103 | 12561.152 | 2446.554 | 339477.446 | 0.0 | 9 | 8 |
| argumentationNodeEvent | 44 | 0.609 | 4.728 | 15625.047 | 32.053 | 346174.931 | 0.0 | 0 | 2 |
| Topographic Map Event | 31 | 2.817 | 24.559 | 22307.562 | 170947.761 | 346351.466 | 0.0 | 0 | 4 |
| argumentationToolEvent | 21 | 0.002 | 0.85 | 24728.42 | 177993.044 | 341151.571 | 0.0 | 6 | 2 |
| TopographicMapEvent | 19 | 1.334 | 4.053 | 18436.668 | 36596.175 | 346813.181 | 0.0 | 0 | 2 |
| soilMachine | 14 | 2.22 | 16.79 | 31.188 | 99.35 | 206.666 | 1.92 | 0 | 0 |
| Soil Key Puzzle | 11 | 2.952 | 53.544 | 62878.533 | 342358.387 | 344886.559 | 0.0 | 0 | 5 |
| argumentationEvent | 9 | 0.142 | 100.697 | 96158.422 | 344088.234 | 346142.807 | 0.0 | 0 | 3 |
| TerasGardenBox | 5 | 1.666 | 2.316 | 13.347 | 31.49 | 32.15 | 4.5 | 0 | 0 |
| EndOfUnit | 4 | 0.0 | 259631.109 | 216421.42 | 346332.245 | 346423.46 | 0.0 | 1 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.025s (p5 29.95s, p95 34.49s, n=556) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc907d385e3b94310f738.jsonl[539] _id=69dd31847957a33870f25ff8 ts=2026-04-13T18:10:12.3610000Z ~ 69cdc907d385e3b94310f738.jsonl[544] _id=69dd31a37957a33870f260c4 ts=2026-04-13T18:10:12.361Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `142ms: 69cdc907d385e3b94310f738.jsonl[194] _id=69e7ae291724f0c9e2f9239b ts=2026-04-21T17:04:41.5440000Z ~ 69cdc907d385e3b94310f738.jsonl[193] _id=69e7ae2a1724f0c9e2f923a3 ts=2026-04-21T17:04:41.6860000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `564ms: 69cdc907d385e3b94310f738.jsonl[1628] _id=69e7ada91724f0c9e2f91f81 ts=2026-04-21T17:02:33.0130000Z ~ 69cdc907d385e3b94310f738.jsonl[1629] _id=69e7adaa1724f0c9e2f91f8b ts=2026-04-21T17:02:33.5770000Z`; `2ms: 69cdc907d385e3b94310f738.jsonl[265] _id=69ea64f71724f0c9e2fb39cf ts=2026-04-23T18:29:10.9700000Z ~ 69cdc907d385e3b94310f738.jsonl[2455] _id=69ea64f71724f0c9e2fb39d1 ts=2026-04-23T18:29:10.9720000Z`; `935ms: 69cdc907d385e3b94310f738.jsonl[2482] _id=69ea65811724f0c9e2fb3d6b ts=2026-04-23T18:31:29.0880000Z ~ 69cdc907d385e3b94310f738.jsonl[2488] _id=69ea65821724f0c9e2fb3d7b ts=2026-04-23T18:31:30.0230000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 17m 
  - Evidence: 94h 17m: 69cdc907d385e3b94310f738.jsonl[1535] _id=69e27e541724f0c9e2f78c22 ts=2026-04-17T18:39:15.3690000Z -> 69cdc907d385e3b94310f738.jsonl[1542] _id=69e7ac561724f0c9e2f91743 ts=2026-04-21T16:56:54.5900000Z; 94h 13m: 69cdc907d385e3b94310f738.jsonl[66] _id=69dd38d77957a33870f2920a ts=2026-04-13T18:41:27.5300000Z -> 69cdc907d385e3b94310f738.jsonl[806] _id=69e265f91724f0c9e2f7205e ts=2026-04-17T16:55:20.4510000Z; 47h 20m: 69cdc907d385e3b94310f738.jsonl[234] _id=69e7c45d1724f0c9e2f9a661 ts=2026-04-21T18:39:25.3300000Z -> 69cdc907d385e3b94310f738.jsonl[2214] _id=69ea5e2d1724f0c9e2fb047b ts=2026-04-23T18:00:13.3160000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 458 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f738.jsonl[1457] _id=69e27abd1724f0c9e2f77c90 ts=2026-04-17T18:23:55.8600000Z -> 69cdc907d385e3b94310f738.jsonl[1463] _id=69e27af51724f0c9e2f77de4 ts=2026-04-17T18:23:55.86Z; 0ms: 69cdc907d385e3b94310f738.jsonl[2122] _id=69e7c1931724f0c9e2f991cb ts=2026-04-21T18:27:31.2270000Z -> 69cdc907d385e3b94310f738.jsonl[2124] _id=69e7c1a11724f0c9e2f99251 ts=2026-04-21T18:27:31.227Z; 0ms: 69cdc907d385e3b94310f738.jsonl[319] _id=69ea671a1724f0c9e2fb4a33 ts=2026-04-23T18:38:18.0610000Z -> 69cdc907d385e3b94310f738.jsonl[2638] _id=69ea67281724f0c9e2fb4aa1 ts=2026-04-23T18:38:18.061Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 13m 
  - Evidence: 96h 13m: 69cdc907d385e3b94310f738.jsonl[544] _id=69dd31a37957a33870f260c4 ts=2026-04-13T18:10:12.361Z -> 69cdc907d385e3b94310f738.jsonl[1462] _id=69e27abc1724f0c9e2f77c8e ts=2026-04-17T18:23:55.8210000Z; 96h 3m: 69cdc907d385e3b94310f738.jsonl[1462] _id=69e27abc1724f0c9e2f77c8e ts=2026-04-17T18:23:55.8210000Z -> 69cdc907d385e3b94310f738.jsonl[2120] _id=69e7c1931724f0c9e2f991c9 ts=2026-04-21T18:27:31.1830000Z; 48h 10m: 69cdc907d385e3b94310f738.jsonl[2120] _id=69e7c1931724f0c9e2f991c9 ts=2026-04-21T18:27:31.1830000Z -> 69cdc907d385e3b94310f738.jsonl[2629] _id=69ea671a1724f0c9e2fb4a2f ts=2026-04-23T18:38:18.0390000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f738.jsonl[539] _id=69dd31847957a33870f25ff8 ts=2026-04-13T18:10:12.3610000Z -> 69cdc907d385e3b94310f738.jsonl[544] _id=69dd31a37957a33870f260c4 ts=2026-04-13T18:10:12.361Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f738.jsonl[1537] _id=69e27e771724f0c9e2f78cc0 ts=2026-04-17T18:39:50.7720000Z -> 69cdc907d385e3b94310f738.jsonl[1539] _id=69e7ac2e1724f0c9e2f9167d ts=2026-04-21T16:56:14.2040000Z; 94h 13m: 69cdc907d385e3b94310f738.jsonl[798] _id=69dd38c87957a33870f291c2 ts=2026-04-13T18:41:12.4070000Z -> 69cdc907d385e3b94310f738.jsonl[803] _id=69e265cb1724f0c9e2f71f8c ts=2026-04-17T16:54:33.7120000Z; 47h 19m: 69cdc907d385e3b94310f738.jsonl[2211] _id=69e7c4801724f0c9e2f9a70b ts=2026-04-21T18:39:59.9010000Z -> 69cdc907d385e3b94310f738.jsonl[2213] _id=69ea5e1f1724f0c9e2fb045d ts=2026-04-23T17:59:59.2020000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 69cdc907d385e3b94310f738.jsonl[1093] _id=69e272d31724f0c9e2f74fec ts=2026-04-17T17:50:10.0130000Z -> 69cdc907d385e3b94310f738.jsonl[1797] _id=69e7b6081724f0c9e2f93d8d ts=2026-04-21T17:38:16.5720000Z; 94h 23m: 69cdc907d385e3b94310f738.jsonl[729] _id=69dd37c47957a33870f28a9a ts=2026-04-13T18:36:52.6370000Z -> 69cdc907d385e3b94310f738.jsonl[861] _id=69e2673c1724f0c9e2f72a2a ts=2026-04-17T17:00:42.8520000Z; 53m 52s: 69cdc907d385e3b94310f738.jsonl[1800] _id=69e7b6251724f0c9e2f93e79 ts=2026-04-21T17:38:45.2400000Z -> 69cdc907d385e3b94310f738.jsonl[2144] _id=69e7c2c61724f0c9e2f99a25 ts=2026-04-21T18:32:38.2180000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc907d385e3b94310f738.jsonl[1318] _id=69e277441724f0c9e2f76af8 ts=2026-04-17T18:09:07.5710000Z -> 69cdc907d385e3b94310f738.jsonl[2043] _id=69e7c0331724f0c9e2f985d9 ts=2026-04-21T18:21:39.0370000Z; 94h 23m: 69cdc907d385e3b94310f738.jsonl[792] _id=69dd38a07957a33870f29127 ts=2026-04-13T18:40:32.3690000Z -> 69cdc907d385e3b94310f738.jsonl[923] _id=69e267e81724f0c9e2f72f9c ts=2026-04-17T17:03:34.7360000Z; 35m 13s: 69cdc907d385e3b94310f738.jsonl[955] _id=69e268801724f0c9e2f734ca ts=2026-04-17T17:06:06.9560000Z -> 69cdc907d385e3b94310f738.jsonl[1038] _id=69e270c11724f0c9e2f7414c ts=2026-04-17T17:41:20.1120000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 20m 
  - Evidence: 96h 20m: 69cdc907d385e3b94310f738.jsonl[1249] _id=69e2757b1724f0c9e2f76184 ts=2026-04-17T18:01:30.3190000Z -> 69cdc907d385e3b94310f738.jsonl[2039] _id=69e7c0371724f0c9e2f9860f ts=2026-04-21T18:21:43.5000000Z; 35m 27s: 69cdc907d385e3b94310f738.jsonl[954] _id=69e268801724f0c9e2f734c6 ts=2026-04-17T17:06:06.8170000Z -> 69cdc907d385e3b94310f738.jsonl[1036] _id=69e270cf1724f0c9e2f741ce ts=2026-04-17T17:41:34.4360000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 69cdc907d385e3b94310f738.jsonl[502] _id=69dd30da7957a33870f25b66 ts=2026-04-13T18:07:22.9560000Z -> 69cdc907d385e3b94310f738.jsonl[149] _id=69e278fa1724f0c9e2f7734a ts=2026-04-17T18:16:25.7630000Z; 94h 43m: 69cdc907d385e3b94310f738.jsonl[1399] _id=69e2794d1724f0c9e2f77516 ts=2026-04-17T18:17:48.3910000Z -> 69cdc907d385e3b94310f738.jsonl[1597] _id=69e7ad5b1724f0c9e2f91d25 ts=2026-04-21T17:01:14.7650000Z; 49h 24m: 69cdc907d385e3b94310f738.jsonl[193] _id=69e7ae2a1724f0c9e2f923a3 ts=2026-04-21T17:04:41.6860000Z -> 69cdc907d385e3b94310f738.jsonl[2459] _id=69ea64f91724f0c9e2fb39e9 ts=2026-04-23T18:29:13.6350000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 69cdc907d385e3b94310f738.jsonl[463] _id=69dd30d47957a33870f25b32 ts=2026-04-13T18:07:16.2870000Z -> 69cdc907d385e3b94310f738.jsonl[1381] _id=69e279141724f0c9e2f773cc ts=2026-04-17T18:16:51.2180000Z; 94h 43m: 69cdc907d385e3b94310f738.jsonl[1396] _id=69e279471724f0c9e2f774e4 ts=2026-04-17T18:17:42.4410000Z -> 69cdc907d385e3b94310f738.jsonl[1609] _id=69e7ad721724f0c9e2f91da7 ts=2026-04-21T17:01:38.2430000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc907d385e3b94310f738.jsonl[1385] _id=69e2790a1724f0c9e2f7739a ts=2026-04-17T18:16:41.4420000Z -> 69cdc907d385e3b94310f738.jsonl[1628] _id=69e7ada91724f0c9e2f91f81 ts=2026-04-21T17:02:33.0130000Z; 49h 26m: 69cdc907d385e3b94310f738.jsonl[1632] _id=69e7adae1724f0c9e2f91fab ts=2026-04-21T17:02:37.9260000Z -> 69cdc907d385e3b94310f738.jsonl[265] _id=69ea64f71724f0c9e2fb39cf ts=2026-04-23T18:29:10.9700000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.002s..0.009s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f738.jsonl[265] _id=69ea64f71724f0c9e2fb39cf ts=2026-04-23T18:29:10.9700000Z -> 69cdc907d385e3b94310f738.jsonl[2455] _id=69ea64f71724f0c9e2fb39d1 ts=2026-04-23T18:29:10.9720000Z; 7ms: 69cdc907d385e3b94310f738.jsonl[272] _id=69ea65841724f0c9e2fb3d97 ts=2026-04-23T18:31:32.4880000Z -> 69cdc907d385e3b94310f738.jsonl[273] _id=69ea65841724f0c9e2fb3d99 ts=2026-04-23T18:31:32.4950000Z; 9ms: 69cdc907d385e3b94310f738.jsonl[1578] _id=69e7ada91724f0c9e2f91f89 ts=2026-04-21T17:02:33.5680000Z -> 69cdc907d385e3b94310f738.jsonl[1629] _id=69e7adaa1724f0c9e2f91f8b ts=2026-04-21T17:02:33.5770000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 17m 
  - Evidence: 94h 17m: 69cdc907d385e3b94310f738.jsonl[1532] _id=69e27e1d1724f0c9e2f78aba ts=2026-04-17T18:38:20.5240000Z -> 69cdc907d385e3b94310f738.jsonl[1540] _id=69e7ac321724f0c9e2f9168d ts=2026-04-21T16:56:17.9700000Z; 94h 15m: 69cdc907d385e3b94310f738.jsonl[785] _id=69dd388e7957a33870f290b4 ts=2026-04-13T18:40:13.9770000Z -> 69cdc907d385e3b94310f738.jsonl[813] _id=69e266191724f0c9e2f721aa ts=2026-04-17T16:55:52.7120000Z; 47h 21m: 69cdc907d385e3b94310f738.jsonl[2199] _id=69e7c4391724f0c9e2f9a555 ts=2026-04-21T18:38:48.6060000Z -> 69cdc907d385e3b94310f738.jsonl[2212] _id=69ea5e221724f0c9e2fb045f ts=2026-04-23T18:00:02.1880000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f738.jsonl[17] _id=69dd305e7957a33870f2586e ts=2026-04-13T18:05:17.3200000Z -> 69cdc907d385e3b94310f738.jsonl[471] _id=69dd305e7957a33870f25872 ts=2026-04-13T18:05:17.3230000Z; 5ms: 69cdc907d385e3b94310f738.jsonl[243] _id=69ea5f111724f0c9e2fb0961 ts=2026-04-23T18:04:01.5310000Z -> 69cdc907d385e3b94310f738.jsonl[244] _id=69ea5f111724f0c9e2fb0965 ts=2026-04-23T18:04:01.5360000Z; 6ms: 69cdc907d385e3b94310f738.jsonl[2231] _id=69ea5ea11724f0c9e2fb068b ts=2026-04-23T18:02:09.1580000Z -> 69cdc907d385e3b94310f738.jsonl[2235] _id=69ea5ea11724f0c9e2fb068d ts=2026-04-23T18:02:09.1640000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc907d385e3b94310f738.jsonl:69cdc907d385e3b94310f738, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f738.jsonl[639] _id=69dd35177957a33870f2789a ts=2026-04-13T18:25:27.4230000Z`; `69cdc907d385e3b94310f738.jsonl[729] _id=69dd37c47957a33870f28a9a ts=2026-04-13T18:36:52.6370000Z`; `69cdc907d385e3b94310f738.jsonl[864] _id=69e2673e1724f0c9e2f72a4a ts=2026-04-17T17:00:45.8040000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 20 record(s) match the trigger in 69cdc907d385e3b94310f738.jsonl:69cdc907d385e3b94310f738, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f738.jsonl[82] _id=69e2687d1724f0c9e2f734be ts=2026-04-17T17:06:04.3260000Z`; `69cdc907d385e3b94310f738.jsonl[954] _id=69e268801724f0c9e2f734c6 ts=2026-04-17T17:06:06.8170000Z`; `69cdc907d385e3b94310f738.jsonl[1036] _id=69e270cf1724f0c9e2f741ce ts=2026-04-17T17:41:34.4360000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f738.jsonl[1193] _id=69e274cf1724f0c9e2f75ce0 ts=2026-04-17T17:58:38.6090000Z`; `69cdc907d385e3b94310f738.jsonl[1519] _id=69e27dcd1724f0c9e2f7889c ts=2026-04-17T18:37:00.1580000Z`; `69cdc907d385e3b94310f738.jsonl[1531] _id=69e27e1e1724f0c9e2f78ac5 ts=2026-04-17T18:38:20.5870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f738.jsonl[193] _id=69e7ae2a1724f0c9e2f923a3 ts=2026-04-21T17:04:41.6860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f738.jsonl[1632] _id=69e7adae1724f0c9e2f91fab ts=2026-04-21T17:02:37.9260000Z`; `69cdc907d385e3b94310f738.jsonl[265] _id=69ea64f71724f0c9e2fb39cf ts=2026-04-23T18:29:10.9700000Z`; `69cdc907d385e3b94310f738.jsonl[2455] _id=69ea64f71724f0c9e2fb39d1 ts=2026-04-23T18:29:10.9720000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc907d385e3b94310f738.jsonl[1914] _id=69e7bb181724f0c9e2f9601b ts=?`; `69cdc907d385e3b94310f738.jsonl[2115] _id=69e7c1941724f0c9e2f991d1 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 182 unmatched 'DialogueStartEvent' (totals: 368 start, 190 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 10 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 40 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.35s, min -57.93s, max +0.04s over 2658 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f738\coverage.yaml

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
- **WARNING / Medium** `WaterChamberEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
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
  - Observed: 32 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1854 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (736); Unit 3 Dev (321); Unit 4 Dev (224); Unit 1 Dev (194); Unit 3 Dungeon Dev (146); Unit 4 Dev - Dungeon (121); Unit 4 Dev - Anderson Base (98); Unit 5 Dev - Dungeon (14)
- **eventKey:** present on 1296 of 1854 records
- **Intervals:** median 1.64s (p5 0.01s / p95 33.90s, n=1853)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1296; [conversationId, dialogueEventType] x558
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1854/1854 records)
    numeric range 8 .. 114 (43 unique)
data.dialogueEventType  (string, 1854/1854 records)
    "DialogueNodeEvent"  x1296
    "DialogueStartEvent"  x368
    "DialogueFinishEvent"  x190
data.nodeId  (number, 1296/1854 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 567 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (233); Unit 3 Dev (112); Unit 3 Dungeon Dev (77); Unit 4 Dev - Dungeon (45); Unit 4 Dev (44); Unit 1 Dev (35); Unit 4 Dev - Anderson Base (14); Unit 5 Dev - Dungeon (7)
- **Intervals:** median 30.02s (p5 29.95s / p95 34.49s, n=556)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 567/567 records)
data.position.x  (number, 567/567 records)
    numeric range -571.498 .. 1714.08 (306 unique)
data.position.y  (number, 567/567 records)
    numeric range -115.127 .. 155.28 (229 unique)
data.position.z  (number, 567/567 records)
    numeric range -1110.4 .. 2131.18 (308 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev - Dungeon (12); Unit 4 Dev (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (1)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 128.10s (p5 0.01s / p95 2446.55s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x30
data.questID  (string, 70/70 records)
    28 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    28 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/70 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 45 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (29); Unit 1 Dev (9); Unit 2 Prod (Refactor) (7)
- **Intervals:** median 4.73s (p5 1.14s / p95 32.05s, n=44)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "argumentationNodeAdd"  x27
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 45/45 records)
    "Unit 3 - Pollution Upstream"  x29
    "Unit 1 - Freshwater"  x9
    "Unit 2 – Watershed"  x7
data.nodeName  (string, 45/45 records)
    "1"  x8
    "B"  x7
    "3"  x6
    "I"  x6
    "II"  x5
    "4"  x4
    "A"  x4
    "5"  x3
    "2"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 32 records

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (8)
- **Intervals:** median 24.56s (p5 4.11s / p95 170947.76s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "MapCloseEvent"  x16
    "MapOpenEvent"  x16
data.featureUsed  (string, 32/32 records)
    "Map"  x32
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationToolEvent` — 22 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (14); Unit 3 Dev (6); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 0.85s (p5 0.01s / p95 177993.04s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "argumentationToolClose"  x12
    "argumentationToolOpen"  x10
data.argumentationTitle  (string, 22/22 records)
    "Unit 4 - Flooding"  x14
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x2
data.toolName  (string, 22/22 records)
    "BackingInfoPanel - Soil Flow Rates"  x10
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TopographicMapEvent` — 20 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (8)
- **Intervals:** median 4.05s (p5 1.52s / p95 36596.18s, n=19)
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

### `soilMachine` — 15 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (15)
- **Intervals:** median 16.79s (p5 3.76s / p95 99.35s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "ChangeCanister"  x15
data.canisterType  (string, 15/15 records)
    "Clay"  x6
    "Bedrock"  x4
    "Sand"  x4
    "Gravel"  x1
data.floor  (string, 15/15 records)
    "5"  x8
    "4"  x7
data.machine  (string, 15/15 records)
    "1"  x13
    "2"  x2
data.row  (string, 15/15 records)
    "TopRow"  x10
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 53.54s (p5 2.97s / p95 342358.39s, n=11)
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

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 100.70s (p5 1.46s / p95 344088.23s, n=9)
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

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.32s (p5 1.68s / p95 31.49s, n=5)
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 259631.11s (p5 26017.03s / p95 346332.25s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x2
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Cannot close a closed AudioContext."  x1
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit3"  x2
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
- `WaterChamberEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TopographicMapEvent` data.actionType: "dragStart" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*