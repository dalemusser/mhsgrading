# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72e
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f72e.jsonl
- **Records:** 2975 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f72e
- **Time span:** 2026-04-13T17:50:16.415000+00:00 .. 2026-04-23T18:32:32.061000+00:00 (240h 42m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2975 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 60 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 2054 | 69.04 | 1 | 9 | 1437 | 2026-04-13T17:50:34.476000+00:00 | 2026-04-23T18:32:28.805000+00:00 | 240h 41m |
| PlayerPositionEvent | 657 | 22.08 | 1 | 9 | 0 | 2026-04-13T17:50:16.415000+00:00 | 2026-04-23T18:32:07.782000+00:00 | 240h 41m |
| WaterChamberEvent | 78 | 2.62 | 1 | 1 | 0 | 2026-04-23T18:04:33.272000+00:00 | 2026-04-23T18:11:34.643000+00:00 | 7m 1s |
| questEvent | 74 | 2.49 | 1 | 9 | 74 | 2026-04-13T17:50:34.455000+00:00 | 2026-04-23T18:31:57.978000+00:00 | 240h 41m |
| soilMachine | 25 | 0.84 | 1 | 1 | 0 | 2026-04-21T18:06:09.975000+00:00 | 2026-04-21T18:14:48.385000+00:00 | 8m 38s |
| argumentationNodeEvent | 24 | 0.81 | 1 | 3 | 0 | 2026-04-13T18:24:48.845000+00:00 | 2026-04-17T17:59:43.907000+00:00 | 95h 34m |
| Topographic Map Event | 14 | 0.47 | 1 | 1 | 0 | 2026-04-15T17:54:54.687000+00:00 | 2026-04-15T18:37:23.896000+00:00 | 42m 29s |
| argumentationEvent | 13 | 0.44 | 1 | 5 | 0 | 2026-04-13T18:24:18.138000+00:00 | 2026-04-23T18:28:00.473000+00:00 | 240h 3m |
| argumentationToolEvent | 12 | 0.4 | 1 | 3 | 0 | 2026-04-17T17:01:58.784000+00:00 | 2026-04-23T18:24:12.833000+00:00 | 145h 22m |
| Soil Key Puzzle | 10 | 0.34 | 1 | 3 | 0 | 2026-04-13T18:39:03.653000+00:00 | 2026-04-21T17:56:14.722000+00:00 | 191h 17m |
| TerasGardenBox | 6 | 0.2 | 1 | 1 | 0 | 2026-04-21T18:30:11.725000+00:00 | 2026-04-21T18:30:45.078000+00:00 | 33.4s |
| EndOfUnit | 5 | 0.17 | 1 | 5 | 0 | 2026-04-13T18:28:09.751000+00:00 | 2026-04-23T18:32:32.061000+00:00 | 240h 4m |
| TopographicMapEvent | 3 | 0.1 | 1 | 2 | 0 | 2026-04-15T17:56:44.727000+00:00 | 2026-04-21T17:03:34.871000+00:00 | 143h 6m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.492s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 256561.453s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.007s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 76.221s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.888s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 257605.072s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 1.103s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 445.143s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 3.777s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.047s median 
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
  - Observed: 3.776s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 10 records 
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
  - Observed: 14 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 3 records 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.9x vs baseline. 
  - Observed: 78 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 24 records 
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
  - Observed: 2; 3; 4; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` — record volume changed 5.0x vs baseline. 
  - Observed: 25 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 19 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[899] _id=69dd35187957a33870f278a4 ts=2026-04-13T18:25:28.4480000Z`; `69cdc907d385e3b94310f72e.jsonl[117] _id=69dfd20f7957a33870f42215 ts=2026-04-15T17:59:42.8090000Z`; `69cdc907d385e3b94310f72e.jsonl[1599] _id=69e267d41724f0c9e2f72ee4 ts=2026-04-17T17:03:15.6300000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 14 records, TopographicMapEvent: 3 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2053 | 0.0 | 1.492 | 422.072 | 30.867 | 339324.686 | 0.14 | 510 | 8 |
| PlayerPositionEvent | 645 | 29.828 | 30.007 | 1342.681 | 32.642 | 339318.523 | 0.04 | 0 | 4 |
| WaterChamberEvent | 77 | 0.114 | 1.103 | 5.472 | 18.432 | 148.069 | 10.96 | 0 | 0 |
| questEvent | 73 | 0.002 | 145.5 | 11869.637 | 68472.26 | 339627.116 | 0.01 | 13 | 11 |
| soilMachine | 24 | 0.519 | 3.776 | 21.6 | 79.423 | 203.632 | 2.78 | 0 | 0 |
| argumentationNodeEvent | 23 | 0.67 | 3.777 | 14960.655 | 150574.487 | 173719.393 | 0.0 | 0 | 3 |
| Topographic Map Event | 13 | 1.873 | 37.143 | 196.093 | 903.822 | 1521.127 | 0.31 | 0 | 1 |
| argumentationEvent | 12 | 0.107 | 445.143 | 72018.528 | 251762.543 | 347165.865 | 0.0 | 0 | 6 |
| argumentationToolEvent | 11 | 0.003 | 3.047 | 47575.823 | 261600.146 | 350599.708 | 0.0 | 2 | 2 |
| Soil Key Puzzle | 9 | 3.004 | 76.221 | 76514.563 | 276063.671 | 345128.69 | 0.0 | 0 | 4 |
| TerasGardenBox | 5 | 1.627 | 1.888 | 6.671 | 14.798 | 15.288 | 8.99 | 0 | 0 |
| EndOfUnit | 4 | 2868.053 | 256561.453 | 216065.578 | 347122.747 | 348271.352 | 0.0 | 0 | 4 |
| TopographicMapEvent | 2 | 4.048 | 257605.072 | 257605.072 | 489445.994 | 515206.096 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.007s (p5 29.96s, p95 32.64s, n=645) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 29 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `846ms: 69cdc907d385e3b94310f72e.jsonl[2744] _id=69ea60ac1724f0c9e2fb171b ts=2026-04-23T18:10:51.7210000Z ~ 69cdc907d385e3b94310f72e.jsonl[2746] _id=69ea60ad1724f0c9e2fb1727 ts=2026-04-23T18:10:52.5670000Z`; `450ms: 69cdc907d385e3b94310f72e.jsonl[2743] _id=69ea60b01724f0c9e2fb1751 ts=2026-04-23T18:10:55.8980000Z ~ 69cdc907d385e3b94310f72e.jsonl[2748] _id=69ea60b11724f0c9e2fb1759 ts=2026-04-23T18:10:56.3480000Z`; `752ms: 69cdc907d385e3b94310f72e.jsonl[2755] _id=69ea60b11724f0c9e2fb1755 ts=2026-04-23T18:10:56.1130000Z ~ 69cdc907d385e3b94310f72e.jsonl[2756] _id=69ea60b11724f0c9e2fb175f ts=2026-04-23T18:10:56.8650000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `107ms: 69cdc907d385e3b94310f72e.jsonl[308] _id=69e275161724f0c9e2f75ef0 ts=2026-04-17T17:59:49.2820000Z ~ 69cdc907d385e3b94310f72e.jsonl[310] _id=69e275161724f0c9e2f75efc ts=2026-04-17T17:59:49.3890000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc907d385e3b94310f72e.jsonl[2515] _id=69e7c12f1724f0c9e2f98e2b ts=2026-04-21T18:25:50.7130000Z ~ 69cdc907d385e3b94310f72e.jsonl[517] _id=69e7c12f1724f0c9e2f98e2f ts=2026-04-21T18:25:50.7160000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 69cdc907d385e3b94310f72e.jsonl[678] _id=69ea64bc1724f0c9e2fb3786 ts=2026-04-23T18:28:11.4690000Z ~ 69cdc907d385e3b94310f72e.jsonl[2928] _id=69ea64bc1724f0c9e2fb378f ts=2026-04-23T18:28:11.4740000Z`; `6ms: 69cdc907d385e3b94310f72e.jsonl[696] _id=69ea658d1724f0c9e2fb3def ts=2026-04-23T18:31:40.3620000Z ~ 69cdc907d385e3b94310f72e.jsonl[697] _id=69ea658d1724f0c9e2fb3df1 ts=2026-04-23T18:31:40.3680000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f72e.jsonl[349] _id=69e27e731724f0c9e2f78cb4 ts=2026-04-17T18:39:46.8930000Z -> 69cdc907d385e3b94310f72e.jsonl[2037] _id=69e7abf01724f0c9e2f91599 ts=2026-04-21T16:55:11.5790000Z; 47h 22m: 69cdc907d385e3b94310f72e.jsonl[573] _id=69e7c45a1724f0c9e2f9a64b ts=2026-04-21T18:39:22.1420000Z -> 69cdc907d385e3b94310f72e.jsonl[2682] _id=69ea5e791724f0c9e2fb05cd ts=2026-04-23T18:01:28.0550000Z; 47h 4m: 69cdc907d385e3b94310f72e.jsonl[1011] _id=69dd38ce7957a33870f291f6 ts=2026-04-13T18:41:18.8670000Z -> 69cdc907d385e3b94310f72e.jsonl[1012] _id=69dfcedb7957a33870f40bc3 ts=2026-04-15T17:46:03.1420000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 510 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72e.jsonl[259] _id=69e268401724f0c9e2f732fc ts=2026-04-17T17:05:03.7590000Z -> 69cdc907d385e3b94310f72e.jsonl[1644] _id=69e268721724f0c9e2f7346e ts=2026-04-17T17:05:03.759Z; 0ms: 69cdc907d385e3b94310f72e.jsonl[2662] _id=69e7c3e31724f0c9e2f9a2df ts=2026-04-21T18:37:23.1670000Z -> 69cdc907d385e3b94310f72e.jsonl[2664] _id=69e7c4221724f0c9e2f9a4a5 ts=2026-04-21T18:37:23.167Z; 2ms: 69cdc907d385e3b94310f72e.jsonl[1286] _id=69dfd78a7957a33870f4441f ts=2026-04-15T18:23:05.3300000Z -> 69cdc907d385e3b94310f72e.jsonl[1295] _id=69dfd78a7957a33870f44421 ts=2026-04-15T18:23:05.3320000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 44m 
  - Evidence: 96h 44m: 69cdc907d385e3b94310f72e.jsonl[1643] _id=69e268401724f0c9e2f732f9 ts=2026-04-17T17:05:03.7360000Z -> 69cdc907d385e3b94310f72e.jsonl[439] _id=69e7b8af1724f0c9e2f9504b ts=2026-04-21T17:49:35.0880000Z; 94h 36m: 69cdc907d385e3b94310f72e.jsonl[70] _id=69dd35b97957a33870f27d02 ts=2026-04-13T18:28:09.7510000Z -> 69cdc907d385e3b94310f72e.jsonl[1643] _id=69e268401724f0c9e2f732f9 ts=2026-04-17T17:05:03.7360000Z; 47h 55m: 69cdc907d385e3b94310f72e.jsonl[570] _id=69e7c3e31724f0c9e2f9a2db ts=2026-04-21T18:37:23.1410000Z -> 69cdc907d385e3b94310f72e.jsonl[729] _id=69ea65c11724f0c9e2fb402b ts=2026-04-23T18:32:32.0610000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f72e.jsonl[2035] _id=69e27e781724f0c9e2f78cc2 ts=2026-04-17T18:39:51.3420000Z -> 69cdc907d385e3b94310f72e.jsonl[2036] _id=69e7abee1724f0c9e2f9158f ts=2026-04-21T16:55:09.8650000Z; 47h 20m: 69cdc907d385e3b94310f72e.jsonl[2677] _id=69e7c48a1724f0c9e2f9a72b ts=2026-04-21T18:40:10.5040000Z -> 69cdc907d385e3b94310f72e.jsonl[2678] _id=69ea5e3a1724f0c9e2fb049f ts=2026-04-23T18:00:25.2250000Z; 47h 4m: 69cdc907d385e3b94310f72e.jsonl[1001] _id=69dd38d17957a33870f29200 ts=2026-04-13T18:41:21.3880000Z -> 69cdc907d385e3b94310f72e.jsonl[1016] _id=69dfced77957a33870f40bb7 ts=2026-04-15T17:45:58.8740000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 69cdc907d385e3b94310f72e.jsonl[1890] _id=69e275ca1724f0c9e2f7630a ts=2026-04-17T18:02:49.8110000Z -> 69cdc907d385e3b94310f72e.jsonl[2271] _id=69e7b9f21724f0c9e2f95727 ts=2026-04-21T17:54:58.5010000Z; 47h 54m: 69cdc907d385e3b94310f72e.jsonl[1210] _id=69dfd4047957a33870f42fe3 ts=2026-04-15T18:08:03.8530000Z -> 69cdc907d385e3b94310f72e.jsonl[1889] _id=69e275b61724f0c9e2f762ae ts=2026-04-17T18:02:29.9960000Z; 47h 12m: 69cdc907d385e3b94310f72e.jsonl[907] _id=69dd384a7957a33870f28eda ts=2026-04-13T18:39:06.8190000Z -> 69cdc907d385e3b94310f72e.jsonl[1067] _id=69dfd0147957a33870f412a7 ts=2026-04-15T17:51:16.2100000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 25m 21s 
  - Evidence: 25m 21s: 69cdc907d385e3b94310f72e.jsonl[1173] _id=69dfd2d97957a33870f427eb ts=2026-04-15T18:03:04.4320000Z -> 69cdc907d385e3b94310f72e.jsonl[1380] _id=69dfd8c97957a33870f44e35 ts=2026-04-15T18:28:25.5590000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 6m 
  - Evidence: 143h 6m: 69cdc907d385e3b94310f72e.jsonl[112] _id=69dfd15d7957a33870f41c85 ts=2026-04-15T17:56:44.7270000Z -> 69cdc907d385e3b94310f72e.jsonl[403] _id=69e7ade31724f0c9e2f92195 ts=2026-04-21T17:03:30.8230000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 26m 
  - Evidence: 96h 26m: 69cdc907d385e3b94310f72e.jsonl[310] _id=69e275161724f0c9e2f75efc ts=2026-04-17T17:59:49.3890000Z -> 69cdc907d385e3b94310f72e.jsonl[518] _id=69e7c1331724f0c9e2f98e63 ts=2026-04-21T18:25:55.2540000Z; 48h 15m: 69cdc907d385e3b94310f72e.jsonl[898] _id=69dd35187957a33870f278a2 ts=2026-04-13T18:25:28.4290000Z -> 69cdc907d385e3b94310f72e.jsonl[200] _id=69dfdba17957a33870f465d7 ts=2026-04-15T18:40:33.7080000Z; 47h 49m: 69cdc907d385e3b94310f72e.jsonl[518] _id=69e7c1331724f0c9e2f98e63 ts=2026-04-21T18:25:55.2540000Z -> 69cdc907d385e3b94310f72e.jsonl[2824] _id=69ea61ab1724f0c9e2fb1fd7 ts=2026-04-23T18:15:06.4540000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 48h 15m 
  - Evidence: 48h 15m: 69cdc907d385e3b94310f72e.jsonl[896] _id=69dd35107957a33870f2785a ts=2026-04-13T18:25:19.9830000Z -> 69cdc907d385e3b94310f72e.jsonl[1492] _id=69dfdba77957a33870f46611 ts=2026-04-15T18:40:39.3760000Z; 46h 22m: 69cdc907d385e3b94310f72e.jsonl[1494] _id=69dfdbaf7957a33870f46654 ts=2026-04-15T18:40:46.7660000Z -> 69cdc907d385e3b94310f72e.jsonl[1595] _id=69e267ca1724f0c9e2f72e72 ts=2026-04-17T17:03:05.5530000Z; 54m 55s: 69cdc907d385e3b94310f72e.jsonl[1597] _id=69e267d11724f0c9e2f72eca ts=2026-04-17T17:03:12.7330000Z -> 69cdc907d385e3b94310f72e.jsonl[1830] _id=69e274b11724f0c9e2f75bf1 ts=2026-04-17T17:58:08.5250000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 97h 23m 
  - Evidence: 97h 23m: 69cdc907d385e3b94310f72e.jsonl[1593] _id=69e267a71724f0c9e2f72d42 ts=2026-04-17T17:02:31.0050000Z -> 69cdc907d385e3b94310f72e.jsonl[2515] _id=69e7c12f1724f0c9e2f98e2b ts=2026-04-21T18:25:50.7130000Z; 47h 56m: 69cdc907d385e3b94310f72e.jsonl[2530] _id=69e7c1911724f0c9e2f991b1 ts=2026-04-21T18:27:29.2010000Z -> 69cdc907d385e3b94310f72e.jsonl[2903] _id=69ea63ca1724f0c9e2fb30cc ts=2026-04-23T18:24:09.7860000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.049s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f72e.jsonl[2515] _id=69e7c12f1724f0c9e2f98e2b ts=2026-04-21T18:25:50.7130000Z -> 69cdc907d385e3b94310f72e.jsonl[517] _id=69e7c12f1724f0c9e2f98e2f ts=2026-04-21T18:25:50.7160000Z; 49ms: 69cdc907d385e3b94310f72e.jsonl[2529] _id=69e7c1901724f0c9e2f991a1 ts=2026-04-21T18:27:27.8870000Z -> 69cdc907d385e3b94310f72e.jsonl[2523] _id=69e7c1901724f0c9e2f991a5 ts=2026-04-21T18:27:27.9360000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 20m 
  - Evidence: 94h 20m: 69cdc907d385e3b94310f72e.jsonl[1992] _id=69e27d451724f0c9e2f7851c ts=2026-04-17T18:34:44.2390000Z -> 69cdc907d385e3b94310f72e.jsonl[2040] _id=69e7abf01724f0c9e2f91597 ts=2026-04-21T16:55:11.3550000Z; 47h 21m: 69cdc907d385e3b94310f72e.jsonl[2665] _id=69e7c4291724f0c9e2f9a4d1 ts=2026-04-21T18:38:32.8870000Z -> 69cdc907d385e3b94310f72e.jsonl[2679] _id=69ea5e3c1724f0c9e2fb04ad ts=2026-04-23T18:00:27.3290000Z; 47h 5m: 69cdc907d385e3b94310f72e.jsonl[998] _id=69dd388c7957a33870f2909a ts=2026-04-13T18:40:12.9000000Z -> 69cdc907d385e3b94310f72e.jsonl[90] _id=69dfceda7957a33870f40bbd ts=2026-04-15T17:46:01.6490000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f72e.jsonl[37] _id=69dd34977957a33870f27576 ts=2026-04-13T18:23:18.9980000Z -> 69cdc907d385e3b94310f72e.jsonl[865] _id=69dd34977957a33870f27578 ts=2026-04-13T18:23:19.0000000Z; 3ms: 69cdc907d385e3b94310f72e.jsonl[2717] _id=69ea60231724f0c9e2fb11d7 ts=2026-04-23T18:08:34.2710000Z -> 69cdc907d385e3b94310f72e.jsonl[2709] _id=69ea60231724f0c9e2fb11df ts=2026-04-23T18:08:34.2740000Z; 5ms: 69cdc907d385e3b94310f72e.jsonl[678] _id=69ea64bc1724f0c9e2fb3786 ts=2026-04-23T18:28:11.4690000Z -> 69cdc907d385e3b94310f72e.jsonl[2928] _id=69ea64bc1724f0c9e2fb378f ts=2026-04-23T18:28:11.4740000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc907d385e3b94310f72e.jsonl:69cdc907d385e3b94310f72e, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[907] _id=69dd384a7957a33870f28eda ts=2026-04-13T18:39:06.8190000Z`; `69cdc907d385e3b94310f72e.jsonl[1068] _id=69dfd0177957a33870f412bd ts=2026-04-15T17:51:19.2140000Z`; `69cdc907d385e3b94310f72e.jsonl[1210] _id=69dfd4047957a33870f42fe3 ts=2026-04-15T18:08:03.8530000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f72e.jsonl:69cdc907d385e3b94310f72e, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[112] _id=69dfd15d7957a33870f41c85 ts=2026-04-15T17:56:44.7270000Z`; `69cdc907d385e3b94310f72e.jsonl[403] _id=69e7ade31724f0c9e2f92195 ts=2026-04-21T17:03:30.8230000Z`; `69cdc907d385e3b94310f72e.jsonl[2135] _id=69e7ade71724f0c9e2f921bd ts=2026-04-21T17:03:34.8710000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[148] _id=69dfd82b7957a33870f448a3 ts=2026-04-15T18:25:47.2620000Z`; `69cdc907d385e3b94310f72e.jsonl[1775] _id=69e273071724f0c9e2f75132 ts=2026-04-17T17:51:02.1350000Z`; `69cdc907d385e3b94310f72e.jsonl[291] _id=69e273471724f0c9e2f752e0 ts=2026-04-17T17:52:05.6980000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[310] _id=69e275161724f0c9e2f75efc ts=2026-04-17T17:59:49.3890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[2515] _id=69e7c12f1724f0c9e2f98e2b ts=2026-04-21T18:25:50.7130000Z`; `69cdc907d385e3b94310f72e.jsonl[517] _id=69e7c12f1724f0c9e2f98e2f ts=2026-04-21T18:25:50.7160000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f72e.jsonl[1591] _id=69e267851724f0c9e2f72c74 ts=2026-04-17T17:01:56.5300000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 185 unmatched 'DialogueStartEvent' (totals: 399 start, 218 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 7 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 42 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.47s, min -63.50s, max -0.04s over 2975 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72e\coverage.yaml

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
  - Observed: 14 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2054 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (704); Unit 3 Dev (295); Unit 5 Dev (277); Unit 4 Dev (228); Unit 1 Dev (180); Unit 3 Dungeon Dev (178); Unit 4 Dev - Dungeon (92); Unit 4 Dev - Anderson Base (69); Unit 5 Dev - Dungeon (31)
- **eventKey:** present on 1437 of 2054 records
- **Intervals:** median 1.49s (p5 0.01s / p95 30.87s, n=2053)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1437; [conversationId, dialogueEventType] x617
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2054/2054 records)
    numeric range 8 .. 114 (51 unique)
data.dialogueEventType  (string, 2054/2054 records)
    "DialogueNodeEvent"  x1437
    "DialogueStartEvent"  x399
    "DialogueFinishEvent"  x218
data.nodeId  (number, 1437/2054 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 657 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (204); Unit 2 Prod (Refactor) (151); Unit 3 Dungeon Dev (80); Unit 1 Dev (62); Unit 4 Dev (47); Unit 5 Dev (41); Unit 4 Dev - Dungeon (33); Unit 5 Dev - Dungeon (25); Unit 4 Dev - Anderson Base (14)
- **Intervals:** median 30.01s (p5 29.96s / p95 32.64s, n=645)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 657/657 records)
data.position.x  (number, 657/657 records)
    numeric range -737.597 .. 1557.34 (287 unique)
data.position.y  (number, 657/657 records)
    numeric range -112.492 .. 217.708 (227 unique)
data.position.z  (number, 657/657 records)
    numeric range -1110.21 .. 1870.9 (287 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `WaterChamberEvent` — 78 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (78)
- **Intervals:** median 1.10s (p5 0.12s / p95 18.43s, n=77)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 78/78 records)
    "On"  x46
    "Off"  x32
data.floor  (string, 78/78 records)
    "4"  x53
    "3"  x16
    "1"  x6
    "2"  x3
data.machineNumber  (string, 78/78 records)
    "One"  x77
    "Two"  x1
data.machineType  (string, 78/78 records)
    "Condenser"  x48
    "Evaporator"  x21
    "DualChamber_Evaporator"  x4
    "DualChamber_Condenser"  x3
    "VentSwitch"  x2
data.room  (string, 78/78 records)
    "3"  x52
    "2"  x18
    "1"  x4
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `questEvent` — 74 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 74 of 74 records
- **Intervals:** median 145.50s (p5 0.01s / p95 68472.26s, n=73)
- **`data` key-set variants:** [questEventType, questID, questName] x42; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Fields under `data`:**

```text
data.questEventType  (string, 74/74 records)
    "questActiveEvent"  x42
    "questFinishEvent"  x32
data.questID  (string, 74/74 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 74/74 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/74 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 25 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (25)
- **Intervals:** median 3.78s (p5 0.75s / p95 79.42s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "ChangeCanister"  x25
data.canisterType  (string, 25/25 records)
    "Clay"  x13
    "Bedrock"  x9
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 25/25 records)
    "5"  x22
    "4"  x2
    "3"  x1
data.machine  (string, 25/25 records)
    "1"  x24
    "2"  x1
data.row  (string, 25/25 records)
    "BottomRow"  x15
    "TopRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 24 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (11); Unit 3 Dev (7); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 3.78s (p5 0.93s / p95 150574.49s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 24/24 records)
    "Unit 1 - Freshwater"  x11
    "Unit 3 - Pollution Upstream"  x7
    "Unit 2 – Watershed"  x6
data.nodeName  (string, 24/24 records)
    "I"  x7
    "1"  x5
    "A"  x4
    "B"  x3
    "II"  x3
    "5"  x1
    "D"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 14 records

- **Scenes:** Unit 2 Prod (Refactor) (14)
- **Intervals:** median 37.14s (p5 6.09s / p95 903.82s, n=13)
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "MapCloseEvent"  x7
    "MapOpenEvent"  x7
data.featureUsed  (string, 14/14 records)
    "Map"  x14
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 445.14s (p5 2.57s / p95 251762.54s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionOpen"  x7
    "argumentationSessionClose"  x6
data.argumentationDescription  (string, 13/13 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 13/13 records)
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 2 Prod (Refactor) (4); Unit 5 Dev (2)
- **Intervals:** median 3.05s (p5 0.03s / p95 261600.15s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x6
data.argumentationTitle  (string, 12/12 records)
    "Unit 4 - Flooding"  x6
    "Unit 2 – Watershed"  x4
    "Unit 5"  x2
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 76.22s (p5 3.07s / p95 276063.67s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/10 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/10 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.89s (p5 1.64s / p95 14.80s, n=5)
- **`data` key-set variants:** [actionType, boxId, soilType] x3; [actionType, boxID, soilType] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x3
    "soilSelected"  x3
data.boxID  (string, 3/6 records)
    "1"  x2
    "2"  x1
data.boxId  (string, 3/6 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "None"  x1
    "Sand"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 256561.45s (p5 28314.18s / p95 347122.75s, n=4)
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

### `TopographicMapEvent` — 3 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 257605.07s (p5 25764.15s / p95 489445.99s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "dragStart"  x2
    "dragEnd"  x1
data.featureUsed  (string, 3/3 records)
    "waypoint"  x3
data.location  (object, 3/3 records)
data.location.x  (number, 3/3 records)
    2 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 3/3 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 3/3 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "dragStart" (2x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)
- `soilMachine` data.canisterType: "Bedrock" (9x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*