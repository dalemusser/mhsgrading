# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77a
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f77a.jsonl
- **Records:** 2356 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f77a
- **Time span:** 2026-04-14T13:56:42.948000+00:00 .. 2026-04-24T14:35:52.106000+00:00 (240h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2356 records, 8 scenes.
- Findings: **0 FAIL**, **40 WARNING**, 70 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1437 | 60.99 | 1 | 8 | 984 | 2026-04-14T13:57:01.133000+00:00 | 2026-04-24T14:33:29.341000+00:00 | 240h 36m |
| PlayerPositionEvent | 554 | 23.51 | 1 | 8 | 0 | 2026-04-14T13:56:42.948000+00:00 | 2026-04-24T14:35:52.106000+00:00 | 240h 39m |
| TopographicMapEvent | 64 | 2.72 | 1 | 2 | 0 | 2026-04-16T13:58:48.450000+00:00 | 2026-04-22T13:39:24.864000+00:00 | 143h 40m |
| questEvent | 61 | 2.59 | 1 | 8 | 61 | 2026-04-14T13:57:01.114000+00:00 | 2026-04-24T14:32:53.293000+00:00 | 240h 35m |
| Topographic Map Event | 60 | 2.55 | 1 | 2 | 0 | 2026-04-16T13:56:16.841000+00:00 | 2026-04-22T13:39:26.399000+00:00 | 143h 43m |
| WaterChamberEvent | 48 | 2.04 | 1 | 1 | 0 | 2026-04-24T14:28:00.197000+00:00 | 2026-04-24T14:35:15.187000+00:00 | 7m 14s |
| argumentationNodeEvent | 43 | 1.83 | 1 | 2 | 0 | 2026-04-14T14:23:23.160000+00:00 | 2026-04-20T14:01:24.411000+00:00 | 143h 38m |
| argumentationToolEvent | 40 | 1.7 | 1 | 2 | 0 | 2026-04-20T14:00:22.229000+00:00 | 2026-04-24T14:15:28.261000+00:00 | 96h 15m |
| TerasGardenBox | 15 | 0.64 | 1 | 1 | 0 | 2026-04-24T14:18:23.393000+00:00 | 2026-04-24T14:20:13.735000+00:00 | 1m 50s |
| soilMachine | 13 | 0.55 | 1 | 1 | 0 | 2026-04-22T14:14:25.002000+00:00 | 2026-04-22T14:21:57.340000+00:00 | 7m 32s |
| argumentationEvent | 8 | 0.34 | 1 | 3 | 0 | 2026-04-14T14:22:57.878000+00:00 | 2026-04-24T14:04:13.850000+00:00 | 239h 41m |
| Soil Key Puzzle | 7 | 0.3 | 1 | 3 | 0 | 2026-04-16T13:48:31.695000+00:00 | 2026-04-22T13:58:16.756000+00:00 | 144h 9m |
| EndOfUnit | 4 | 0.17 | 1 | 3 | 0 | 2026-04-14T14:30:30.008000+00:00 | 2026-04-24T14:24:22.209000+00:00 | 239h 53m |
| crash | 2 | 0.08 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 175042.238s median 
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
  - Observed: 1415.318s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.41s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.564s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.118s median 
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
  - Observed: 9.188s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 7 records 
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
  - Observed: 60 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 43 records 
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
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 4.4x vs baseline. 
  - Observed: 40 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 44; 45; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[433] _id=69de4e687957a33870f3606c ts=2026-04-14T14:25:42.4100000Z`; `69cdc965d385e3b94310f77a.jsonl[714] _id=69e0ebc87957a33870f524e9 ts=2026-04-16T14:01:44.0230000Z`; `69cdc965d385e3b94310f77a.jsonl[1101] _id=69e62f791724f0c9e2f87923 ts=2026-04-20T13:51:53.0340000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 60 records, TopographicMapEvent: 64 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 9 records, data.boxId: 6 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1436 | 0.0 | 2.332 | 603.195 | 56.852 | 341465.214 | 0.1 | 378 | 4 |
| PlayerPositionEvent | 543 | 28.292 | 30.011 | 1594.945 | 34.69 | 340986.549 | 0.04 | 0 | 4 |
| TopographicMapEvent | 63 | 0.252 | 2.34 | 8210.102 | 409.04 | 342076.279 | 0.01 | 0 | 2 |
| questEvent | 60 | 0.004 | 198.06 | 14435.87 | 168814.16 | 343346.469 | 0.0 | 11 | 11 |
| Topographic Map Event | 59 | 0.143 | 13.89 | 8769.315 | 364.449 | 342094.432 | 0.01 | 0 | 2 |
| WaterChamberEvent | 47 | 0.082 | 4.41 | 9.255 | 28.302 | 53.451 | 6.48 | 0 | 0 |
| argumentationNodeEvent | 42 | 0.919 | 4.564 | 12311.458 | 27.355 | 516696.085 | 0.0 | 0 | 1 |
| argumentationToolEvent | 39 | 0.002 | 1.118 | 8884.77 | 137.983 | 345825.201 | 0.01 | 4 | 1 |
| TerasGardenBox | 14 | 0.283 | 3.612 | 7.882 | 21.306 | 29.453 | 7.61 | 0 | 0 |
| soilMachine | 12 | 0.2 | 9.188 | 37.695 | 130.295 | 189.76 | 1.59 | 0 | 0 |
| argumentationEvent | 7 | 0.088 | 60.678 | 123267.996 | 465405.509 | 516679.022 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 6 | 2.951 | 1415.318 | 86497.51 | 300982.004 | 343905.033 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 0.0 | 175042.238 | 287877.4 | 637235.191 | 688589.963 | 0.0 | 1 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.011s (p5 29.95s, p95 34.69s, n=543) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc965d385e3b94310f77a.jsonl[1640] _id=69e8d1541724f0c9e2fa3add ts=2026-04-22T13:46:59.9710000Z ~ 69cdc965d385e3b94310f77a.jsonl[1642] _id=69e8d1851724f0c9e2fa3c07 ts=2026-04-22T13:46:59.971Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `283ms: 69cdc965d385e3b94310f77a.jsonl[2163] _id=69eb7be11724f0c9e2fb9055 ts=2026-04-24T14:19:12.7940000Z ~ 69cdc965d385e3b94310f77a.jsonl[2164] _id=69eb7be11724f0c9e2fb9057 ts=2026-04-24T14:19:13.0770000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `82ms: 69cdc965d385e3b94310f77a.jsonl[2283] _id=69eb7e261724f0c9e2fb9b75 ts=2026-04-24T14:28:53.7810000Z ~ 69cdc965d385e3b94310f77a.jsonl[2286] _id=69eb7e261724f0c9e2fb9b7d ts=2026-04-24T14:28:53.8630000Z`; `216ms: 69cdc965d385e3b94310f77a.jsonl[2286] _id=69eb7e261724f0c9e2fb9b7d ts=2026-04-24T14:28:53.8630000Z ~ 69cdc965d385e3b94310f77a.jsonl[2287] _id=69eb7e261724f0c9e2fb9b81 ts=2026-04-24T14:28:54.0790000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `88ms: 69cdc965d385e3b94310f77a.jsonl[1213] _id=69e631b61724f0c9e2f8857f ts=2026-04-20T14:01:26.4510000Z ~ 69cdc965d385e3b94310f77a.jsonl[59] _id=69e631b71724f0c9e2f88589 ts=2026-04-20T14:01:26.5390000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc965d385e3b94310f77a.jsonl[1928] _id=69eb785c1724f0c9e2fb7f29 ts=2026-04-24T14:04:11.5670000Z ~ 69cdc965d385e3b94310f77a.jsonl[1972] _id=69eb785c1724f0c9e2fb7f2b ts=2026-04-24T14:04:11.5690000Z`; `701ms: 69cdc965d385e3b94310f77a.jsonl[1989] _id=69eb78c41724f0c9e2fb813c ts=2026-04-24T14:05:56.2240000Z ~ 69cdc965d385e3b94310f77a.jsonl[1990] _id=69eb78c51724f0c9e2fb8141 ts=2026-04-24T14:05:56.9250000Z`; `702ms: 69cdc965d385e3b94310f77a.jsonl[140] _id=69eb78c41724f0c9e2fb813f ts=2026-04-24T14:05:56.2760000Z ~ 69cdc965d385e3b94310f77a.jsonl[141] _id=69eb78c51724f0c9e2fb8143 ts=2026-04-24T14:05:56.9780000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `200ms: 69cdc965d385e3b94310f77a.jsonl[1825] _id=69e8d8d61724f0c9e2fa67fb ts=2026-04-22T14:19:02.5720000Z ~ 69cdc965d385e3b94310f77a.jsonl[1827] _id=69e8d8d61724f0c9e2fa67fd ts=2026-04-22T14:19:02.7720000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc965d385e3b94310f77a.jsonl[856] _id=69e0f1cd7957a33870f54873 ts=2026-04-16T14:27:25.0830000Z -> 69cdc965d385e3b94310f77a.jsonl[887] _id=69e627a71724f0c9e2f84b2b ts=2026-04-20T13:18:30.2970000Z; 47h 26m: 69cdc965d385e3b94310f77a.jsonl[1910] _id=69e8dbe21724f0c9e2fa7577 ts=2026-04-22T14:32:02.1880000Z -> 69cdc965d385e3b94310f77a.jsonl[1914] _id=69eb77201724f0c9e2fb77d5 ts=2026-04-24T13:58:55.6400000Z; 47h 3m: 69cdc965d385e3b94310f77a.jsonl[489] _id=69de4fac7957a33870f36a10 ts=2026-04-14T14:31:07.6930000Z -> 69cdc965d385e3b94310f77a.jsonl[493] _id=69e0e55e7957a33870f4fa9d ts=2026-04-16T13:34:21.6890000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 378 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77a.jsonl[2251] _id=69eb7d161724f0c9e2fb965b ts=2026-04-24T14:24:22.2260000Z -> 69cdc965d385e3b94310f77a.jsonl[2254] _id=69eb7d251724f0c9e2fb969b ts=2026-04-24T14:24:22.226Z; 3ms: 69cdc965d385e3b94310f77a.jsonl[1264] _id=69e633311724f0c9e2f88e79 ts=2026-04-20T14:07:45.6310000Z -> 69cdc965d385e3b94310f77a.jsonl[1259] _id=69e633311724f0c9e2f88e7b ts=2026-04-20T14:07:45.6340000Z; 3ms: 69cdc965d385e3b94310f77a.jsonl[159] _id=69eb7b2d1724f0c9e2fb8cd9 ts=2026-04-24T14:16:12.3730000Z -> 69cdc965d385e3b94310f77a.jsonl[2067] _id=69eb7b2d1724f0c9e2fb8cdb ts=2026-04-24T14:16:12.3760000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 16m 
  - Evidence: 191h 16m: 69cdc965d385e3b94310f77a.jsonl[487] _id=69de4f867957a33870f3692a ts=2026-04-14T14:30:30.0080000Z -> 69cdc965d385e3b94310f77a.jsonl[1640] _id=69e8d1541724f0c9e2fa3add ts=2026-04-22T13:46:59.9710000Z; 48h 37m: 69cdc965d385e3b94310f77a.jsonl[1642] _id=69e8d1851724f0c9e2fa3c07 ts=2026-04-22T13:46:59.971Z -> 69cdc965d385e3b94310f77a.jsonl[2250] _id=69eb7d161724f0c9e2fb9659 ts=2026-04-24T14:24:22.2090000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77a.jsonl[1640] _id=69e8d1541724f0c9e2fa3add ts=2026-04-22T13:46:59.9710000Z -> 69cdc965d385e3b94310f77a.jsonl[1642] _id=69e8d1851724f0c9e2fa3c07 ts=2026-04-22T13:46:59.971Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f77a.jsonl[881] _id=69e0f3a97957a33870f558db ts=2026-04-16T14:35:20.6970000Z -> 69cdc965d385e3b94310f77a.jsonl[884] _id=69e627a31724f0c9e2f84b17 ts=2026-04-20T13:18:27.2460000Z; 47h 26m: 69cdc965d385e3b94310f77a.jsonl[123] _id=69e8dbde1724f0c9e2fa7567 ts=2026-04-22T14:31:57.5960000Z -> 69cdc965d385e3b94310f77a.jsonl[1913] _id=69eb771d1724f0c9e2fb77c5 ts=2026-04-24T13:58:52.2550000Z; 47h 2m: 69cdc965d385e3b94310f77a.jsonl[490] _id=69de4fca7957a33870f36ab4 ts=2026-04-14T14:31:36.9360000Z -> 69cdc965d385e3b94310f77a.jsonl[492] _id=69e0e55b7957a33870f4fa6f ts=2026-04-16T13:34:18.0850000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 69cdc965d385e3b94310f77a.jsonl[586] _id=69e0e8b37957a33870f51239 ts=2026-04-16T13:48:34.6460000Z -> 69cdc965d385e3b94310f77a.jsonl[897] _id=69e628141724f0c9e2f84d87 ts=2026-04-20T13:20:19.6790000Z; 47h 50m: 69cdc965d385e3b94310f77a.jsonl[1257] _id=69e633221724f0c9e2f88e23 ts=2026-04-20T14:07:30.3150000Z -> 69cdc965d385e3b94310f77a.jsonl[1674] _id=69e8d3d71724f0c9e2fa468d ts=2026-04-22T13:57:43.2310000Z; 45m 42s: 69cdc965d385e3b94310f77a.jsonl[897] _id=69e628141724f0c9e2f84d87 ts=2026-04-20T13:20:19.6790000Z -> 69cdc965d385e3b94310f77a.jsonl[1209] _id=69e632cb1724f0c9e2f88c09 ts=2026-04-20T14:06:02.6240000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 1m 
  - Evidence: 95h 1m: 69cdc965d385e3b94310f77a.jsonl[879] _id=69e0f3817957a33870f55823 ts=2026-04-16T14:34:40.5940000Z -> 69cdc965d385e3b94310f77a.jsonl[1010] _id=69e62bcf1724f0c9e2f863d5 ts=2026-04-20T13:36:15.0260000Z; 47h 52m: 69cdc965d385e3b94310f77a.jsonl[1045] _id=69e62d661724f0c9e2f86e9d ts=2026-04-20T13:43:02.7080000Z -> 69cdc965d385e3b94310f77a.jsonl[1534] _id=69e8ceb01724f0c9e2fa26b9 ts=2026-04-22T13:35:44.4880000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 1m 
  - Evidence: 95h 1m: 69cdc965d385e3b94310f77a.jsonl[851] _id=69e0f1ca7957a33870f54853 ts=2026-04-16T14:27:22.1180000Z -> 69cdc965d385e3b94310f77a.jsonl[946] _id=69e62a061724f0c9e2f85753 ts=2026-04-20T13:28:38.3970000Z; 47h 59m: 69cdc965d385e3b94310f77a.jsonl[1011] _id=69e62bd81724f0c9e2f863f7 ts=2026-04-20T13:36:24.6290000Z -> 69cdc965d385e3b94310f77a.jsonl[1537] _id=69e8ceba1724f0c9e2fa26eb ts=2026-04-22T13:35:54.4960000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 31m 
  - Evidence: 143h 31m: 69cdc965d385e3b94310f77a.jsonl[436] _id=69de4e677957a33870f36068 ts=2026-04-14T14:25:42.3770000Z -> 69cdc965d385e3b94310f77a.jsonl[1151] _id=69e630ad1724f0c9e2f87f8b ts=2026-04-20T13:57:01.3990000Z; 96h 2m: 69cdc965d385e3b94310f77a.jsonl[59] _id=69e631b71724f0c9e2f88589 ts=2026-04-20T14:01:26.5390000Z -> 69cdc965d385e3b94310f77a.jsonl[136] _id=69eb785e1724f0c9e2fb7f3d ts=2026-04-24T14:04:13.8500000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 31m 
  - Evidence: 143h 31m: 69cdc965d385e3b94310f77a.jsonl[435] _id=69de4e627957a33870f36056 ts=2026-04-14T14:25:37.7310000Z -> 69cdc965d385e3b94310f77a.jsonl[1153] _id=69e630b91724f0c9e2f87fcd ts=2026-04-20T13:57:13.8160000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 69cdc965d385e3b94310f77a.jsonl[1195] _id=69e6317a1724f0c9e2f883fb ts=2026-04-20T14:00:26.3660000Z -> 69cdc965d385e3b94310f77a.jsonl[1928] _id=69eb785c1724f0c9e2fb7f29 ts=2026-04-24T14:04:11.5670000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.024s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f77a.jsonl[1928] _id=69eb785c1724f0c9e2fb7f29 ts=2026-04-24T14:04:11.5670000Z -> 69cdc965d385e3b94310f77a.jsonl[1972] _id=69eb785c1724f0c9e2fb7f2b ts=2026-04-24T14:04:11.5690000Z; 17ms: 69cdc965d385e3b94310f77a.jsonl[2003] _id=69eb796b1724f0c9e2fb83df ts=2026-04-24T14:08:43.1260000Z -> 69cdc965d385e3b94310f77a.jsonl[2014] _id=69eb796b1724f0c9e2fb83e1 ts=2026-04-24T14:08:43.1430000Z; 24ms: 69cdc965d385e3b94310f77a.jsonl[2054] _id=69eb7a271724f0c9e2fb87e7 ts=2026-04-24T14:11:51.1010000Z -> 69cdc965d385e3b94310f77a.jsonl[2055] _id=69eb7a271724f0c9e2fb87e9 ts=2026-04-24T14:11:51.1250000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 69cdc965d385e3b94310f77a.jsonl[657] _id=69e0ea757957a33870f51e2d ts=2026-04-16T13:56:04.5650000Z -> 69cdc965d385e3b94310f77a.jsonl[886] _id=69e627a81724f0c9e2f84b2f ts=2026-04-20T13:18:31.0340000Z; 47h 26m: 69cdc965d385e3b94310f77a.jsonl[1908] _id=69e8dbdf1724f0c9e2fa7569 ts=2026-04-22T14:31:59.0300000Z -> 69cdc965d385e3b94310f77a.jsonl[1912] _id=69eb771f1724f0c9e2fb77cb ts=2026-04-24T13:58:54.3300000Z; 47h 6m: 69cdc965d385e3b94310f77a.jsonl[480] _id=69de4f5d7957a33870f36792 ts=2026-04-14T14:29:48.6300000Z -> 69cdc965d385e3b94310f77a.jsonl[500] _id=69e0e5cc7957a33870f4ff65 ts=2026-04-16T13:36:11.5780000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 69cdc965d385e3b94310f77a.jsonl[394] _id=69de4d697957a33870f35aaf ts=2026-04-14T14:21:28.5290000Z -> 69cdc965d385e3b94310f77a.jsonl[397] _id=69de4d697957a33870f35ab1 ts=2026-04-14T14:21:28.5330000Z; 7ms: 69cdc965d385e3b94310f77a.jsonl[2300] _id=69eb7e841724f0c9e2fb9cf1 ts=2026-04-24T14:30:28.0700000Z -> 69cdc965d385e3b94310f77a.jsonl[2299] _id=69eb7e841724f0c9e2fb9cf3 ts=2026-04-24T14:30:28.0770000Z; 7ms: 69cdc965d385e3b94310f77a.jsonl[2321] _id=69eb7f161724f0c9e2fba055 ts=2026-04-24T14:32:53.2860000Z -> 69cdc965d385e3b94310f77a.jsonl[2320] _id=69eb7f161724f0c9e2fba059 ts=2026-04-24T14:32:53.2930000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc965d385e3b94310f77a.jsonl:69cdc965d385e3b94310f77a, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[586] _id=69e0e8b37957a33870f51239 ts=2026-04-16T13:48:34.6460000Z`; `69cdc965d385e3b94310f77a.jsonl[1257] _id=69e633221724f0c9e2f88e23 ts=2026-04-20T14:07:30.3150000Z`; `69cdc965d385e3b94310f77a.jsonl[1681] _id=69e8d3f81724f0c9e2fa474f ts=2026-04-22T13:58:16.7560000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 64 record(s) match the trigger in 69cdc965d385e3b94310f77a.jsonl:69cdc965d385e3b94310f77a, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[673] _id=69e0eb197957a33870f5213b ts=2026-04-16T13:58:48.4500000Z`; `69cdc965d385e3b94310f77a.jsonl[674] _id=69e0eb197957a33870f5213d ts=2026-04-16T13:58:48.7650000Z`; `69cdc965d385e3b94310f77a.jsonl[678] _id=69e0eb207957a33870f52165 ts=2026-04-16T13:58:55.3760000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[982] _id=69e62b071724f0c9e2f85db3 ts=2026-04-20T13:32:55.1880000Z`; `69cdc965d385e3b94310f77a.jsonl[1003] _id=69e62b991724f0c9e2f862a3 ts=2026-04-20T13:35:21.0380000Z`; `69cdc965d385e3b94310f77a.jsonl[1880] _id=69e8dafd1724f0c9e2fa736b ts=2026-04-22T14:28:13.5480000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[59] _id=69e631b71724f0c9e2f88589 ts=2026-04-20T14:01:26.5390000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[1928] _id=69eb785c1724f0c9e2fb7f29 ts=2026-04-24T14:04:11.5670000Z`; `69cdc965d385e3b94310f77a.jsonl[1972] _id=69eb785c1724f0c9e2fb7f2b ts=2026-04-24T14:04:11.5690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc965d385e3b94310f77a.jsonl[1641] _id=69e8d1551724f0c9e2fa3ae7 ts=?`; `69cdc965d385e3b94310f77a.jsonl[1918] _id=69eb77411724f0c9e2fb787d ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 166 unmatched 'DialogueStartEvent' (totals: 308 start, 145 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 37 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.59s, min -49.24s, max -0.02s over 2354 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=complete 
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
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 60 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1437 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (325); Unit 4 Dev (245); Unit 2 Prod (Refactor) (224); Unit 1 Dev (205); Unit 3 Dungeon Dev (165); Unit 4 Dev - Anderson Base (140); Unit 4 Dev - Dungeon (97); Unit 5 Dev - Dungeon (36)
- **eventKey:** present on 984 of 1437 records
- **Intervals:** median 2.33s (p5 0.01s / p95 56.85s, n=1436)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x984; [conversationId, dialogueEventType] x453
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1437/1437 records)
    numeric range 10 .. 114 (40 unique)
data.dialogueEventType  (string, 1437/1437 records)
    "DialogueNodeEvent"  x984
    "DialogueStartEvent"  x308
    "DialogueFinishEvent"  x145
data.nodeId  (number, 984/1437 records)
    numeric range 0 .. 289 (199 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 554 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (124); Unit 3 Dev (114); Unit 3 Dungeon Dev (85); Unit 1 Dev (68); Unit 4 Dev (66); Unit 4 Dev - Dungeon (38); Unit 4 Dev - Anderson Base (36); Unit 5 Dev - Dungeon (23)
- **Intervals:** median 30.01s (p5 29.95s / p95 34.69s, n=543)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 554/554 records)
data.position.x  (number, 554/554 records)
    numeric range -707.156 .. 1619.29 (346 unique)
data.position.y  (number, 554/554 records)
    numeric range -114.326 .. 220.846 (269 unique)
data.position.z  (number, 554/554 records)
    numeric range -1115.5 .. 2056.28 (346 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `TopographicMapEvent` — 64 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (42); Unit 3 Dev (22)
- **Intervals:** median 2.34s (p5 0.47s / p95 409.04s, n=63)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 64/64 records)
    "dragEnd"  x32
    "dragStart"  x32
data.featureUsed  (string, 64/64 records)
    "waypoint"  x64
data.location  (object, 64/64 records)
data.location.x  (number, 64/64 records)
    numeric range -770.79 .. 159.003 (33 unique)
data.location.y  (number, 64/64 records)
    numeric range -307.4 .. 221.278 (31 unique)
data.location.z  (number, 64/64 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 61 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 2 Prod (Refactor) (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 61 of 61 records
- **Intervals:** median 198.06s (p5 0.01s / p95 168814.16s, n=60)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Fields under `data`:**

```text
data.questEventType  (string, 61/61 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x24
data.questID  (string, 61/61 records)
    29 unique values (see csv/event_unique_values.csv)
data.questName  (string, 61/61 records)
    29 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/61 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 60 records

- **Scenes:** Unit 2 Prod (Refactor) (46); Unit 3 Dev (14)
- **Intervals:** median 13.89s (p5 1.98s / p95 364.45s, n=59)
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "MapCloseEvent"  x30
    "MapOpenEvent"  x30
data.featureUsed  (string, 60/60 records)
    "Map"  x60
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 48 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (48)
- **Intervals:** median 4.41s (p5 0.60s / p95 28.30s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "On"  x27
    "Off"  x21
data.floor  (string, 48/48 records)
    "4"  x22
    "3"  x14
    "1"  x7
    "2"  x5
data.machineNumber  (string, 48/48 records)
    "One"  x47
    "Two"  x1
data.machineType  (string, 48/48 records)
    "Condenser"  x28
    "Evaporator"  x13
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 48/48 records)
    "3"  x26
    "2"  x16
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 43 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (35); Unit 1 Dev (8)
- **Intervals:** median 4.56s (p5 1.35s / p95 27.35s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "argumentationNodeAdd"  x25
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 43/43 records)
    "Unit 3 - Pollution Upstream"  x35
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 43/43 records)
    "I"  x10
    "1"  x6
    "2"  x6
    "B"  x5
    "3"  x4
    "4"  x4
    "II"  x4
    "5"  x3
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 40 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (36); Unit 3 Dev (4)
- **Intervals:** median 1.12s (p5 0.02s / p95 137.98s, n=39)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "argumentationToolClose"  x21
    "argumentationToolOpen"  x19
data.argumentationTitle  (string, 40/40 records)
    "Unit 4 - Flooding"  x36
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 40/40 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x22
    "BackingInfoPanel - Soil Flow Rates"  x14
    "BackingInfoPanel - Pollution Site Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 3.61s (p5 0.98s / p95 21.31s, n=14)
- **`data` key-set variants:** [actionType, boxID, soilType] x9; [actionType, boxId, soilType] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "soilSelected"  x9
    "cameraPlaced"  x6
data.boxID  (string, 9/15 records)
    "2"  x4
    "1"  x3
    "0"  x2
data.boxId  (string, 6/15 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 15/15 records)
    "Clay"  x7
    "Sand"  x4
    "Gravel"  x2
    "None"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 13 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (13)
- **Intervals:** median 9.19s (p5 1.34s / p95 130.30s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "ChangeCanister"  x13
data.canisterType  (string, 13/13 records)
    "Bedrock"  x5
    "Clay"  x4
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 13/13 records)
    "5"  x11
    "3"  x1
    "4"  x1
data.machine  (string, 13/13 records)
    "1"  x11
    "2"  x2
data.row  (string, 13/13 records)
    "BottomRow"  x7
    "TopRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 60.68s (p5 14.61s / p95 465405.51s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 7 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 1415.32s (p5 10.59s / p95 300982.00s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 7/7 records)
    "Started"  x4
    "Finished"  x3
data.Unit  (string, 7/7 records)
    "Unit 2 Prod (Refactor)"  x3
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 3 Dev (2); Unit 1 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 175042.24s (p5 17504.22s / p95 637235.19s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "3"  x2
    "1"  x1
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
    "A user gesture is required to request Pointer Lock."  x1
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit3"  x1
    "unit4"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (3 records)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "dragStart" (32x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*