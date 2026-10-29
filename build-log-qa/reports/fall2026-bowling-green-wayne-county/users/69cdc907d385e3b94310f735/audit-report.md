# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f735

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f735
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f735.jsonl
- **Records:** 3333 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f735
- **Time span:** 2026-04-13T17:46:40.349000+00:00 .. 2026-04-23T18:38:03.080000+00:00 (240h 51m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f735\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **12 event types**, 3333 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 51 INFO, 0 NOT_TESTED, 53 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2317 | 69.52 | 1 | 9 | 1632 | 2026-04-13T17:46:58.807000+00:00 | 2026-04-23T18:37:55.977000+00:00 | 240h 50m |
| PlayerPositionEvent | 698 | 20.94 | 1 | 9 | 0 | 2026-04-13T17:46:40.349000+00:00 | 2026-04-23T18:37:41.813000+00:00 | 240h 51m |
| questEvent | 98 | 2.94 | 1 | 9 | 98 | 2026-04-13T17:46:58.793000+00:00 | 2026-04-23T18:37:13.245000+00:00 | 240h 50m |
| soilMachine | 80 | 2.4 | 1 | 1 | 0 | 2026-04-17T18:39:49.074000+00:00 | 2026-04-21T18:15:42.672000+00:00 | 95h 35m |
| WaterChamberEvent | 40 | 1.2 | 1 | 1 | 0 | 2026-04-23T18:03:36.804000+00:00 | 2026-04-23T18:07:45.806000+00:00 | 4m 9s |
| argumentationNodeEvent | 37 | 1.11 | 1 | 3 | 0 | 2026-04-13T18:06:26.291000+00:00 | 2026-04-17T17:45:26.461000+00:00 | 95h 39m |
| Topographic Map Event | 20 | 0.6 | 1 | 2 | 0 | 2026-04-13T18:16:47.258000+00:00 | 2026-04-17T17:40:21.223000+00:00 | 95h 23m |
| argumentationEvent | 12 | 0.36 | 1 | 5 | 0 | 2026-04-13T18:06:04.619000+00:00 | 2026-04-23T18:26:19.505000+00:00 | 240h 20m |
| argumentationToolEvent | 10 | 0.3 | 1 | 3 | 0 | 2026-04-15T18:40:22.126000+00:00 | 2026-04-23T18:14:22.249000+00:00 | 191h 34m |
| Soil Key Puzzle | 8 | 0.24 | 1 | 3 | 0 | 2026-04-13T18:26:36.175000+00:00 | 2026-04-17T18:25:22.090000+00:00 | 95h 58m |
| TerasGardenBox | 7 | 0.21 | 1 | 1 | 0 | 2026-04-21T18:37:03.206000+00:00 | 2026-04-21T18:37:40.019000+00:00 | 36.8s |
| EndOfUnit | 6 | 0.18 | 1 | 5 | 0 | 2026-04-13T18:13:08.477000+00:00 | 2026-04-23T18:38:03.080000+00:00 | 240h 24m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 0.839s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172319.06s median 
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
  - Observed: 51.204s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 83 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 3.013s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 164.652s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 3.409s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.765s median 
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
  - Observed: 1.981s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 20 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 37 records 
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
  - Observed: 4; C; D 
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
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` — record volume changed 16.0x vs baseline. 
  - Observed: 80 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 98 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:35' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f735.jsonl[848] _id=69dd305e7957a33870f25864 ts=2026-04-13T18:05:17.3470000Z`; `69cdc907d385e3b94310f735.jsonl[868] _id=69dd308e7957a33870f25982 ts=2026-04-13T18:06:04.7760000Z`; `69cdc907d385e3b94310f735.jsonl[869] _id=69dd308e7957a33870f25984 ts=2026-04-13T18:06:05.1500000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:40' vs expected 'questActiveEvent:36' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc907d385e3b94310f735.jsonl[2610] _id=69e7c1561724f0c9e2f98fb9 ts=2026-04-21T18:26:29.6620000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 4 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2316 | 0.0 | 0.839 | 374.377 | 26.055 | 339399.482 | 0.16 | 546 | 7 |
| PlayerPositionEvent | 684 | 29.799 | 30.004 | 1017.981 | 32.099 | 339409.659 | 0.06 | 0 | 3 |
| questEvent | 97 | 0.001 | 93.007 | 8938.293 | 2513.911 | 339399.455 | 0.01 | 20 | 11 |
| soilMachine | 79 | 0.202 | 1.981 | 4356.375 | 453.247 | 339559.77 | 0.01 | 0 | 3 |
| WaterChamberEvent | 39 | 0.535 | 3.013 | 6.385 | 24.197 | 30.523 | 9.4 | 0 | 0 |
| argumentationNodeEvent | 36 | 0.973 | 3.409 | 9565.005 | 42350.81 | 174799.789 | 0.01 | 0 | 2 |
| Topographic Map Event | 19 | 0.236 | 22.869 | 18074.419 | 170011.955 | 170471.607 | 0.0 | 0 | 4 |
| argumentationEvent | 11 | 0.074 | 164.652 | 78655.899 | 261622.309 | 348458.02 | 0.0 | 0 | 5 |
| argumentationToolEvent | 9 | 0.002 | 2.765 | 76626.68 | 379440.629 | 517948.561 | 0.0 | 2 | 2 |
| Soil Key Puzzle | 7 | 3.008 | 51.204 | 49360.845 | 171648.857 | 171690.085 | 0.0 | 0 | 3 |
| TerasGardenBox | 6 | 1.27 | 2.944 | 6.136 | 14.718 | 15.61 | 9.78 | 0 | 0 |
| EndOfUnit | 5 | 336.602 | 172319.06 | 173098.921 | 346079.208 | 347358.953 | 0.0 | 0 | 4 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.004s (p5 29.96s, p95 32.10s, n=684) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `74ms: 69cdc907d385e3b94310f735.jsonl[339] _id=69e271b91724f0c9e2f748a4 ts=2026-04-17T17:45:28.0670000Z ~ 69cdc907d385e3b94310f735.jsonl[336] _id=69e271ba1724f0c9e2f748ae ts=2026-04-17T17:45:28.1410000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc907d385e3b94310f735.jsonl[2693] _id=69e7c2d51724f0c9e2f99aa9 ts=2026-04-21T18:32:53.4520000Z ~ 69cdc907d385e3b94310f735.jsonl[2694] _id=69e7c2d61724f0c9e2f99aad ts=2026-04-21T18:32:53.4540000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc907d385e3b94310f735.jsonl[2610] _id=69e7c1561724f0c9e2f98fb9 ts=2026-04-21T18:26:29.6620000Z ~ 69cdc907d385e3b94310f735.jsonl[2613] _id=69e7c1571724f0c9e2f98fc3 ts=2026-04-21T18:26:29.6650000Z`; `9ms: 69cdc907d385e3b94310f735.jsonl[3158] _id=69ea64c11724f0c9e2fb37bd ts=2026-04-23T18:28:16.8100000Z ~ 69cdc907d385e3b94310f735.jsonl[3157] _id=69ea64c21724f0c9e2fb37c1 ts=2026-04-23T18:28:16.8190000Z`; `5ms: 69cdc907d385e3b94310f735.jsonl[3213] _id=69ea65561724f0c9e2fb3c3d ts=2026-04-23T18:30:46.6810000Z ~ 69cdc907d385e3b94310f735.jsonl[3214] _id=69ea65561724f0c9e2fb3c3f ts=2026-04-23T18:30:46.6860000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `951ms: 69cdc907d385e3b94310f735.jsonl[2192] _id=69e27e761724f0c9e2f78cb8 ts=2026-04-17T18:39:49.0740000Z ~ 69cdc907d385e3b94310f735.jsonl[2194] _id=69e27e771724f0c9e2f78cbe ts=2026-04-17T18:39:50.0250000Z`; `543ms: 69cdc907d385e3b94310f735.jsonl[472] _id=69e27e781724f0c9e2f78cc6 ts=2026-04-17T18:39:51.1720000Z ~ 69cdc907d385e3b94310f735.jsonl[466] _id=69e27e791724f0c9e2f78cc8 ts=2026-04-17T18:39:51.7150000Z`; `803ms: 69cdc907d385e3b94310f735.jsonl[466] _id=69e27e791724f0c9e2f78cc8 ts=2026-04-17T18:39:51.7150000Z ~ 69cdc907d385e3b94310f735.jsonl[473] _id=69e27e7a1724f0c9e2f78ccc ts=2026-04-17T18:39:52.5180000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f735.jsonl[2201] _id=69e27ebb1724f0c9e2f78d2a ts=2026-04-17T18:40:57.3340000Z -> 69cdc907d385e3b94310f735.jsonl[483] _id=69e7ac811724f0c9e2f91845 ts=2026-04-21T16:57:36.8160000Z; 47h 19m: 69cdc907d385e3b94310f735.jsonl[2850] _id=69e7c4b71724f0c9e2f9a79d ts=2026-04-21T18:40:27.43Z -> 69cdc907d385e3b94310f735.jsonl[2856] _id=69ea5e361724f0c9e2fb0495 ts=2026-04-23T18:00:22.7680000Z; 47h 5m: 69cdc907d385e3b94310f735.jsonl[1092] _id=69dd38c57957a33870f291b8 ts=2026-04-13T18:41:08.7490000Z -> 69cdc907d385e3b94310f735.jsonl[117] _id=69dfceeb7957a33870f40be7 ts=2026-04-15T17:46:18.5610000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 546 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f735.jsonl[1596] _id=69e266161724f0c9e2f7219c ts=2026-04-17T16:55:48.7140000Z -> 69cdc907d385e3b94310f735.jsonl[1599] _id=69e266221724f0c9e2f72209 ts=2026-04-17T16:55:48.714Z; 0ms: 69cdc907d385e3b94310f735.jsonl[2842] _id=69e7c49c1724f0c9e2f9a789 ts=2026-04-21T18:40:27.4300000Z -> 69cdc907d385e3b94310f735.jsonl[2850] _id=69e7c4b71724f0c9e2f9a79d ts=2026-04-21T18:40:27.43Z; 3ms: 69cdc907d385e3b94310f735.jsonl[1175] _id=69dfd1287957a33870f41b2f ts=2026-04-15T17:55:50.7640000Z -> 69cdc907d385e3b94310f735.jsonl[1176] _id=69dfd1287957a33870f41b31 ts=2026-04-15T17:55:50.7670000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 29m 
  - Evidence: 96h 29m: 69cdc907d385e3b94310f735.jsonl[2045] _id=69e277be1724f0c9e2f76d4c ts=2026-04-17T18:11:08.4650000Z -> 69cdc907d385e3b94310f735.jsonl[2847] _id=69e7c49b1724f0c9e2f9a787 ts=2026-04-21T18:40:27.4180000Z; 94h 42m: 69cdc907d385e3b94310f735.jsonl[930] _id=69dd32347957a33870f2650c ts=2026-04-13T18:13:08.4770000Z -> 69cdc907d385e3b94310f735.jsonl[1595] _id=69e266161724f0c9e2f7219a ts=2026-04-17T16:55:48.7030000Z; 47h 51m: 69cdc907d385e3b94310f735.jsonl[2847] _id=69e7c49b1724f0c9e2f9a787 ts=2026-04-21T18:40:27.4180000Z -> 69cdc907d385e3b94310f735.jsonl[3252] _id=69ea65ba1724f0c9e2fb4001 ts=2026-04-23T18:32:26.4780000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f735.jsonl[2199] _id=69e27eae1724f0c9e2f78d1a ts=2026-04-17T18:40:44.3570000Z -> 69cdc907d385e3b94310f735.jsonl[481] _id=69e7ac7f1724f0c9e2f9183d ts=2026-04-21T16:57:34.0160000Z; 47h 5m: 69cdc907d385e3b94310f735.jsonl[1087] _id=69dd38bd7957a33870f29196 ts=2026-04-13T18:41:01.0820000Z -> 69cdc907d385e3b94310f735.jsonl[1093] _id=69dfcee87957a33870f40be1 ts=2026-04-15T17:46:14.3240000Z; 46h 12m: 69cdc907d385e3b94310f735.jsonl[1570] _id=69dfdbdb7957a33870f466f1 ts=2026-04-15T18:41:30.5670000Z -> 69cdc907d385e3b94310f735.jsonl[1574] _id=69e265b21724f0c9e2f71f4c ts=2026-04-17T16:54:08.6370000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 41m 
  - Evidence: 47h 41m: 69cdc907d385e3b94310f735.jsonl[1267] _id=69dfd3b47957a33870f42dd5 ts=2026-04-15T18:06:43.0450000Z -> 69cdc907d385e3b94310f735.jsonl[1903] _id=69e2725e1724f0c9e2f74d04 ts=2026-04-17T17:48:13.1300000Z; 47h 39m: 69cdc907d385e3b94310f735.jsonl[994] _id=69dd355f7957a33870f27ac0 ts=2026-04-13T18:26:39.1830000Z -> 69cdc907d385e3b94310f735.jsonl[1262] _id=69dfd3817957a33870f42c77 ts=2026-04-15T18:05:51.8410000Z; 36m 15s: 69cdc907d385e3b94310f735.jsonl[1904] _id=69e2726c1724f0c9e2f74d94 ts=2026-04-17T17:48:26.8130000Z -> 69cdc907d385e3b94310f735.jsonl[2123] _id=69e27aec1724f0c9e2f77da2 ts=2026-04-17T18:24:42.7040000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 21m 
  - Evidence: 47h 21m: 69cdc907d385e3b94310f735.jsonl[1072] _id=69dd37507957a33870f287d6 ts=2026-04-13T18:34:56.0370000Z -> 69cdc907d385e3b94310f735.jsonl[1190] _id=69dfd13a7957a33870f41bb7 ts=2026-04-15T17:56:07.6440000Z; 47h 12m: 69cdc907d385e3b94310f735.jsonl[224] _id=69dfd8957957a33870f44c23 ts=2026-04-15T18:27:32.1550000Z -> 69cdc907d385e3b94310f735.jsonl[1774] _id=69e2707e1724f0c9e2f73fea ts=2026-04-17T17:40:13.0380000Z; 27m 12s: 69cdc907d385e3b94310f735.jsonl[1222] _id=69dfd2347957a33870f4234a ts=2026-04-15T18:00:18.7820000Z -> 69cdc907d385e3b94310f735.jsonl[221] _id=69dfd8947957a33870f44c15 ts=2026-04-15T18:27:31.0050000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 47m 
  - Evidence: 96h 47m: 69cdc907d385e3b94310f735.jsonl[336] _id=69e271ba1724f0c9e2f748ae ts=2026-04-17T17:45:28.1410000Z -> 69cdc907d385e3b94310f735.jsonl[582] _id=69e7c2e21724f0c9e2f99adf ts=2026-04-21T18:33:06.1610000Z; 48h 33m: 69cdc907d385e3b94310f735.jsonl[888] _id=69dd30d07957a33870f25b16 ts=2026-04-13T18:07:12.3510000Z -> 69cdc907d385e3b94310f735.jsonl[260] _id=69dfdb947957a33870f46571 ts=2026-04-15T18:40:18.9490000Z; 47h 37m: 69cdc907d385e3b94310f735.jsonl[582] _id=69e7c2e21724f0c9e2f99adf ts=2026-04-21T18:33:06.1610000Z -> 69cdc907d385e3b94310f735.jsonl[2981] _id=69ea60b81724f0c9e2fb1795 ts=2026-04-23T18:11:03.8940000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 48h 33m 
  - Evidence: 48h 33m: 69cdc907d385e3b94310f735.jsonl[44] _id=69dd30ce7957a33870f25b08 ts=2026-04-13T18:07:10.5230000Z -> 69cdc907d385e3b94310f735.jsonl[1557] _id=69dfdb9f7957a33870f465cb ts=2026-04-15T18:40:30.3120000Z; 47h 2m: 69cdc907d385e3b94310f735.jsonl[1559] _id=69dfdba87957a33870f46617 ts=2026-04-15T18:40:39.6090000Z -> 69cdc907d385e3b94310f735.jsonl[1809] _id=69e271261724f0c9e2f7441c ts=2026-04-17T17:43:00.3690000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 52m 
  - Evidence: 143h 52m: 69cdc907d385e3b94310f735.jsonl[1554] _id=69dfdb9a7957a33870f4659d ts=2026-04-15T18:40:24.8910000Z -> 69cdc907d385e3b94310f735.jsonl[2693] _id=69e7c2d51724f0c9e2f99aa9 ts=2026-04-21T18:32:53.4520000Z; 47h 41m: 69cdc907d385e3b94310f735.jsonl[2694] _id=69e7c2d61724f0c9e2f99aad ts=2026-04-21T18:32:53.4540000Z -> 69cdc907d385e3b94310f735.jsonl[3038] _id=69ea61741724f0c9e2fb1d65 ts=2026-04-23T18:14:12.1840000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.002s..0.047s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f735.jsonl[2693] _id=69e7c2d51724f0c9e2f99aa9 ts=2026-04-21T18:32:53.4520000Z -> 69cdc907d385e3b94310f735.jsonl[2694] _id=69e7c2d61724f0c9e2f99aad ts=2026-04-21T18:32:53.4540000Z; 47ms: 69cdc907d385e3b94310f735.jsonl[2997] _id=69ea617a1724f0c9e2fb1d9f ts=2026-04-23T18:14:18.2670000Z -> 69cdc907d385e3b94310f735.jsonl[654] _id=69ea617a1724f0c9e2fb1da1 ts=2026-04-23T18:14:18.3140000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f735.jsonl[2202] _id=69e27ebb1724f0c9e2f78d26 ts=2026-04-17T18:40:57.1820000Z -> 69cdc907d385e3b94310f735.jsonl[482] _id=69e7ac811724f0c9e2f91843 ts=2026-04-21T16:57:36.6370000Z; 47h 19m: 69cdc907d385e3b94310f735.jsonl[2848] _id=69e7c4991724f0c9e2f9a779 ts=2026-04-21T18:40:24.8210000Z -> 69cdc907d385e3b94310f735.jsonl[626] _id=69ea5e321724f0c9e2fb0483 ts=2026-04-23T18:00:17.3480000Z; 47h 15m: 69cdc907d385e3b94310f735.jsonl[1044] _id=69dd36457957a33870f280ec ts=2026-04-13T18:30:27.6520000Z -> 69cdc907d385e3b94310f735.jsonl[1094] _id=69dfceea7957a33870f40be3 ts=2026-04-15T17:46:17.1240000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 20 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 69cdc907d385e3b94310f735.jsonl[3257] _id=69ea65c51724f0c9e2fb4059 ts=2026-04-23T18:32:37.0170000Z -> 69cdc907d385e3b94310f735.jsonl[3255] _id=69ea65c51724f0c9e2fb405b ts=2026-04-23T18:32:37.0180000Z; 3ms: 69cdc907d385e3b94310f735.jsonl[2224] _id=69e7ad151724f0c9e2f91b50 ts=2026-04-21T17:00:03.8290000Z -> 69cdc907d385e3b94310f735.jsonl[2220] _id=69e7ad151724f0c9e2f91b56 ts=2026-04-21T17:00:03.8320000Z; 3ms: 69cdc907d385e3b94310f735.jsonl[2502] _id=69e7bbab1724f0c9e2f9647f ts=2026-04-21T18:02:19.2080000Z -> 69cdc907d385e3b94310f735.jsonl[2505] _id=69e7bbab1724f0c9e2f96485 ts=2026-04-21T18:02:19.2110000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 19m 
  - Evidence: 94h 19m: 69cdc907d385e3b94310f735.jsonl[2187] _id=69e27e841724f0c9e2f78cf6 ts=2026-04-17T18:40:02.8410000Z -> 69cdc907d385e3b94310f735.jsonl[2218] _id=69e7aceb1724f0c9e2f91a5d ts=2026-04-21T16:59:22.6110000Z; 30m 6s: 69cdc907d385e3b94310f735.jsonl[2270] _id=69e7ae721724f0c9e2f9256f ts=2026-04-21T17:05:54.1090000Z -> 69cdc907d385e3b94310f735.jsonl[2327] _id=69e7b5801724f0c9e2f936bf ts=2026-04-21T17:36:00.3460000Z; 13m 56s: 69cdc907d385e3b94310f735.jsonl[2376] _id=69e7b82e1724f0c9e2f94cbf ts=2026-04-21T17:47:25.8210000Z -> 69cdc907d385e3b94310f735.jsonl[2493] _id=69e7bb721724f0c9e2f962d7 ts=2026-04-21T18:01:22.2250000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f735.jsonl:69cdc907d385e3b94310f735, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f735.jsonl[994] _id=69dd355f7957a33870f27ac0 ts=2026-04-13T18:26:39.1830000Z`; `69cdc907d385e3b94310f735.jsonl[1267] _id=69dfd3b47957a33870f42dd5 ts=2026-04-15T18:06:43.0450000Z`; `69cdc907d385e3b94310f735.jsonl[1904] _id=69e2726c1724f0c9e2f74d94 ts=2026-04-17T17:48:26.8130000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f735.jsonl[208] _id=69dfd80e7957a33870f447c7 ts=2026-04-15T18:25:17.4380000Z`; `69cdc907d385e3b94310f735.jsonl[303] _id=69e267b71724f0c9e2f72da0 ts=2026-04-17T17:02:45.1930000Z`; `69cdc907d385e3b94310f735.jsonl[308] _id=69e2682a1724f0c9e2f7326a ts=2026-04-17T17:04:40.7320000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f735.jsonl[336] _id=69e271ba1724f0c9e2f748ae ts=2026-04-17T17:45:28.1410000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f735.jsonl[2693] _id=69e7c2d51724f0c9e2f99aa9 ts=2026-04-21T18:32:53.4520000Z`; `69cdc907d385e3b94310f735.jsonl[2694] _id=69e7c2d61724f0c9e2f99aad ts=2026-04-21T18:32:53.4540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f735.jsonl[2038] _id=69e276ae1724f0c9e2f767ce ts=2026-04-17T18:06:36.9390000Z`; `69cdc907d385e3b94310f735.jsonl[2208] _id=69e7ac9b1724f0c9e2f918df ts=2026-04-21T16:58:02.3890000Z`; `69cdc907d385e3b94310f735.jsonl[2447] _id=69e7ba351724f0c9e2f958d9 ts=2026-04-21T17:56:04.5670000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f735.jsonl[664] _id=69ea61751724f0c9e2fb1d6b ts=2026-04-23T18:14:13.8010000Z`; `69cdc907d385e3b94310f735.jsonl[3044] _id=69ea617d1724f0c9e2fb1dc7 ts=2026-04-23T18:14:21.1660000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 181 unmatched 'DialogueStartEvent' (totals: 431 start, 254 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 53 start, 45 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.70s, min -28.19s, max -0.05s over 3333 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f735\coverage.yaml

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
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=complete, Unit3=complete 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
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
  - Observed: 20 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2317 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (679); Unit 5 Dev (413); Unit 3 Dev (350); Unit 4 Dev (288); Unit 4 Dev - Dungeon (201); Unit 1 Dev (184); Unit 3 Dungeon Dev (90); Unit 4 Dev - Anderson Base (78); Unit 5 Dev - Dungeon (34)
- **eventKey:** present on 1632 of 2317 records
- **Intervals:** median 0.84s (p5 0.01s / p95 26.05s, n=2316)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1632; [conversationId, dialogueEventType] x685
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2317/2317 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 2317/2317 records)
    "DialogueNodeEvent"  x1632
    "DialogueStartEvent"  x431
    "DialogueFinishEvent"  x254
data.nodeId  (number, 1632/2317 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 698 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 4 Dev - Dungeon (164); Unit 2 Prod (Refactor) (163); Unit 3 Dev (130); Unit 4 Dev (83); Unit 5 Dev (57); Unit 1 Dev (53); Unit 3 Dungeon Dev (21); Unit 5 Dev - Dungeon (16); Unit 4 Dev - Anderson Base (11)
- **Intervals:** median 30.00s (p5 29.96s / p95 32.10s, n=684)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 698/698 records)
data.position.x  (number, 698/698 records)
    numeric range -788.282 .. 2477.11 (369 unique)
data.position.y  (number, 698/698 records)
    numeric range -112.49 .. 554.903 (306 unique)
data.position.z  (number, 698/698 records)
    numeric range -1245.94 .. 2596.97 (369 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 98 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (21); Unit 2 Prod (Refactor) (18); Unit 4 Dev (14); Unit 1 Dev (12); Unit 5 Dev (12); Unit 3 Dev (10); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 98 of 98 records
- **Intervals:** median 93.01s (p5 0.00s / p95 2513.91s, n=97)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x45
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 98/98 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x45
data.questID  (string, 98/98 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 98/98 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 45/98 records)
    "Succeeded"  x45
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 80 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (80)
- **Intervals:** median 1.98s (p5 0.27s / p95 453.25s, n=79)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 80/80 records)
    "ChangeCanister"  x80
data.canisterType  (string, 80/80 records)
    "Clay"  x30
    "Bedrock"  x27
    "Sand"  x18
    "Gravel"  x5
data.floor  (string, 80/80 records)
    "5"  x54
    "3"  x21
    "4"  x5
data.machine  (string, 80/80 records)
    "1"  x77
    "2"  x3
data.row  (string, 80/80 records)
    "TopRow"  x53
    "BottomRow"  x27
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 40 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (40)
- **Intervals:** median 3.01s (p5 0.61s / p95 24.20s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "On"  x26
    "Off"  x14
data.floor  (string, 40/40 records)
    "4"  x21
    "3"  x8
    "2"  x7
    "1"  x4
data.machineNumber  (string, 40/40 records)
    "One"  x39
    "Two"  x1
data.machineType  (string, 40/40 records)
    "Condenser"  x21
    "Evaporator"  x12
    "VentSwitch"  x4
    "DualChamber_Evaporator"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 40/40 records)
    "3"  x18
    "2"  x16
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 37 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (25); Unit 1 Dev (9); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 3.41s (p5 1.23s / p95 42350.81s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "argumentationNodeAdd"  x23
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 37/37 records)
    "Unit 3 - Pollution Upstream"  x25
    "Unit 1 - Freshwater"  x9
    "Unit 2 – Watershed"  x3
data.nodeName  (string, 37/37 records)
    "1"  x8
    "A"  x8
    "B"  x5
    "II"  x5
    "2"  x4
    "I"  x4
    "3"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 20 records

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (2)
- **Intervals:** median 22.87s (p5 0.31s / p95 170011.96s, n=19)
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "MapCloseEvent"  x10
    "MapOpenEvent"  x10
data.featureUsed  (string, 20/20 records)
    "Map"  x20
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 164.65s (p5 0.69s / p95 261622.31s, n=11)
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

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (6); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 2.77s (p5 0.02s / p95 379440.63s, n=9)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x5
    "argumentationToolOpen"  x5
data.argumentationTitle  (string, 10/10 records)
    "Unit 5"  x6
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x2
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Evaporation Flow Diagram"  x3
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Soil Flow Rates"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 51.20s (p5 6.21s / p95 171648.86s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 2.94s (p5 1.45s / p95 14.72s, n=6)
- **`data` key-set variants:** [actionType, boxID, soilType] x4; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "soilSelected"  x4
    "cameraPlaced"  x3
data.boxID  (string, 4/7 records)
    "1"  x2
    "0"  x1
    "2"  x1
data.boxId  (string, 3/7 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 7/7 records)
    "Clay"  x6
    "Sand"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 5 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 172319.06s (p5 1173.23s / p95 346079.21s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "5"  x2
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
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
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (27x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*