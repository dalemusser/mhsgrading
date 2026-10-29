# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f722

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f722
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f722.jsonl
- **Records:** 2990 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f722
- **Time span:** 2026-04-13T17:50:59.625000+00:00 .. 2026-04-23T18:40:44.845000+00:00 (240h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f722\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 2990 records, 9 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 71 INFO, 0 NOT_TESTED, 57 PASS.
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
| DialogueEvent | 2024 | 67.69 | 1 | 9 | 1394 | 2026-04-13T17:51:17.793000+00:00 | 2026-04-23T18:40:44.845000+00:00 | 240h 49m |
| PlayerPositionEvent | 672 | 22.47 | 1 | 9 | 0 | 2026-04-13T17:50:59.625000+00:00 | 2026-04-23T18:40:34.309000+00:00 | 240h 49m |
| questEvent | 76 | 2.54 | 1 | 9 | 76 | 2026-04-13T17:51:17.777000+00:00 | 2026-04-23T18:37:28.994000+00:00 | 240h 46m |
| Topographic Map Event | 40 | 1.34 | 1 | 2 | 0 | 2026-04-15T18:00:56.188000+00:00 | 2026-04-21T17:46:03.248000+00:00 | 143h 45m |
| WaterChamberEvent | 39 | 1.3 | 1 | 1 | 0 | 2026-04-23T18:24:25.582000+00:00 | 2026-04-23T18:36:12.057000+00:00 | 11m 46s |
| argumentationToolEvent | 38 | 1.27 | 1 | 3 | 0 | 2026-04-17T17:05:50.229000+00:00 | 2026-04-23T18:02:46.803000+00:00 | 144h 56m |
| TopographicMapEvent | 28 | 0.94 | 1 | 2 | 0 | 2026-04-15T18:03:19.861000+00:00 | 2026-04-21T17:42:37.373000+00:00 | 143h 39m |
| soilMachine | 26 | 0.87 | 1 | 1 | 0 | 2026-04-21T18:02:55.675000+00:00 | 2026-04-21T18:10:29.586000+00:00 | 7m 33s |
| argumentationEvent | 12 | 0.4 | 1 | 5 | 0 | 2026-04-13T18:07:45.453000+00:00 | 2026-04-23T18:40:44.831000+00:00 | 240h 32m |
| argumentationNodeEvent | 11 | 0.37 | 1 | 3 | 0 | 2026-04-13T18:08:08.400000+00:00 | 2026-04-17T17:59:07.844000+00:00 | 95h 50m |
| Soil Key Puzzle | 10 | 0.33 | 1 | 3 | 0 | 2026-04-13T18:28:32.205000+00:00 | 2026-04-21T17:53:14.706000+00:00 | 191h 24m |
| TerasGardenBox | 5 | 0.17 | 1 | 1 | 0 | 2026-04-23T18:09:10.062000+00:00 | 2026-04-23T18:10:05.150000+00:00 | 55.1s |
| crash | 5 | 0.17 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 4 | 0.13 | 1 | 4 | 0 | 2026-04-13T18:11:27.874000+00:00 | 2026-04-23T18:15:46.485000+00:00 | 240h 4m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.252s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 343853.865s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.013s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 59.339s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 13.774s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.743s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 9.907s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.114s median 
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
  - Observed: 5.268s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
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
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineNumber` — baseline categorical value(s) not seen this build. 
  - Observed: Two 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
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
  - Observed: 2; 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 38 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
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
  - Observed: 51 mismatch(es); e.g. 'DialogueNodeEvent:35:35' vs expected 'DialogueNodeEvent:35:37' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f722.jsonl[32] _id=69dd30297957a33870f2573a ts=2026-04-13T18:04:24.2120000Z`; `69cdc907d385e3b94310f722.jsonl[33] _id=69dd30297957a33870f2573c ts=2026-04-13T18:04:24.5660000Z`; `69cdc907d385e3b94310f722.jsonl[781] _id=69dd30f27957a33870f25c20 ts=2026-04-13T18:07:45.9270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 28 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 2 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2023 | 0.0 | 1.252 | 428.555 | 39.717 | 339316.985 | 0.14 | 535 | 9 |
| PlayerPositionEvent | 658 | 29.779 | 30.013 | 1204.558 | 38.182 | 339320.721 | 0.05 | 0 | 5 |
| questEvent | 75 | 0.002 | 170.994 | 11556.95 | 80290.48 | 339566.315 | 0.01 | 11 | 14 |
| Topographic Map Event | 39 | 1.317 | 12.518 | 13269.412 | 18284.941 | 344938.574 | 0.0 | 0 | 3 |
| WaterChamberEvent | 38 | 0.116 | 12.217 | 18.591 | 51.18 | 68.678 | 3.23 | 0 | 0 |
| argumentationToolEvent | 37 | 0.001 | 2.114 | 14103.151 | 36786.597 | 346967.549 | 0.0 | 5 | 3 |
| TopographicMapEvent | 27 | 0.698 | 3.743 | 19153.982 | 120207.354 | 344946.599 | 0.0 | 0 | 2 |
| soilMachine | 25 | 0.767 | 5.268 | 18.156 | 75.639 | 109.269 | 3.3 | 0 | 0 |
| argumentationEvent | 11 | 0.104 | 60.001 | 78725.398 | 344379.517 | 346945.098 | 0.0 | 0 | 5 |
| argumentationNodeEvent | 10 | 2.883 | 9.907 | 34505.944 | 189426.04 | 341840.028 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 9 | 3.004 | 59.339 | 76564.722 | 275768.673 | 345030.232 | 0.0 | 0 | 4 |
| TerasGardenBox | 4 | 1.419 | 13.774 | 13.772 | 25.77 | 26.12 | 4.36 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 3 | 174468.551 | 343853.865 | 288086.204 | 345727.962 | 345936.195 | 0.0 | 0 | 3 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f722.jsonl[2364] _id=69e7bdbe1724f0c9e2f97317 ts=? == 69cdc907d385e3b94310f722.jsonl[2592] _id=69e8e41e1724f0c9e2fa75cb ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.013s (p5 29.97s, p95 38.18s, n=658) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `302ms: 69cdc907d385e3b94310f722.jsonl[627] _id=69ea65d31724f0c9e2fb40b3 ts=2026-04-23T18:31:56.6360000Z ~ 69cdc907d385e3b94310f722.jsonl[628] _id=69ea65d41724f0c9e2fb40c1 ts=2026-04-23T18:31:56.9380000Z`; `116ms: 69cdc907d385e3b94310f722.jsonl[628] _id=69ea65d41724f0c9e2fb40c1 ts=2026-04-23T18:31:56.9380000Z ~ 69cdc907d385e3b94310f722.jsonl[629] _id=69ea65d41724f0c9e2fb40c7 ts=2026-04-23T18:31:57.0540000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `104ms: 69cdc907d385e3b94310f722.jsonl[1752] _id=69e274f51724f0c9e2f75df6 ts=2026-04-17T17:59:16.9710000Z ~ 69cdc907d385e3b94310f722.jsonl[1789] _id=69e274f51724f0c9e2f75e06 ts=2026-04-17T17:59:17.0750000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc907d385e3b94310f722.jsonl[481] _id=69e7c02b1724f0c9e2f98599 ts=2026-04-21T18:21:30.8290000Z ~ 69cdc907d385e3b94310f722.jsonl[2465] _id=69e7c02b1724f0c9e2f9859e ts=2026-04-21T18:21:30.8310000Z`; `850ms: 69cdc907d385e3b94310f722.jsonl[2512] _id=69e7c1631724f0c9e2f9902b ts=2026-04-21T18:26:43.0330000Z ~ 69cdc907d385e3b94310f722.jsonl[503] _id=69e7c1641724f0c9e2f9902f ts=2026-04-21T18:26:43.8830000Z`; `895ms: 69cdc907d385e3b94310f722.jsonl[2511] _id=69e7c1631724f0c9e2f9902d ts=2026-04-21T18:26:43.0420000Z ~ 69cdc907d385e3b94310f722.jsonl[499] _id=69e7c1641724f0c9e2f99033 ts=2026-04-21T18:26:43.9370000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `885ms: 69cdc907d385e3b94310f722.jsonl[2317] _id=69e7bc331724f0c9e2f9689b ts=2026-04-21T18:04:35.4790000Z ~ 69cdc907d385e3b94310f722.jsonl[2322] _id=69e7bc341724f0c9e2f9689d ts=2026-04-21T18:04:36.3640000Z`; `916ms: 69cdc907d385e3b94310f722.jsonl[2350] _id=69e7bd511724f0c9e2f97031 ts=2026-04-21T18:09:21.1910000Z ~ 69cdc907d385e3b94310f722.jsonl[2354] _id=69e7bd521724f0c9e2f97033 ts=2026-04-21T18:09:22.1070000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f722.jsonl[336] _id=69e27e881724f0c9e2f78cfe ts=2026-04-17T18:40:07.4660000Z -> 69cdc907d385e3b94310f722.jsonl[342] _id=69e7abfd1724f0c9e2f915cf ts=2026-04-21T16:55:24.4510000Z; 47h 8m: 69cdc907d385e3b94310f722.jsonl[996] _id=69dd38a17957a33870f29130 ts=2026-04-13T18:40:32.1140000Z -> 69cdc907d385e3b94310f722.jsonl[1000] _id=69dfcf9a7957a33870f40f69 ts=2026-04-15T17:49:14.1840000Z; 46h 15m: 69cdc907d385e3b94310f722.jsonl[216] _id=69dfdb907957a33870f46561 ts=2026-04-15T18:40:16.2000000Z -> 69cdc907d385e3b94310f722.jsonl[1384] _id=69e2661e1724f0c9e2f721d4 ts=2026-04-17T16:55:57.3320000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 535 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f722.jsonl[273] _id=69e270fe1724f0c9e2f7432e ts=2026-04-17T17:42:21.7550000Z -> 69cdc907d385e3b94310f722.jsonl[1632] _id=69e271171724f0c9e2f743d8 ts=2026-04-17T17:42:21.755Z; 0ms: 69cdc907d385e3b94310f722.jsonl[2837] _id=69ea61d21724f0c9e2fb2183 ts=2026-04-23T18:15:46.4990000Z -> 69cdc907d385e3b94310f722.jsonl[2839] _id=69ea62541724f0c9e2fb25e3 ts=2026-04-23T18:15:46.499Z; 1ms: 69cdc907d385e3b94310f722.jsonl[1503] _id=69e268781724f0c9e2f73494 ts=2026-04-17T17:06:00.1980000Z -> 69cdc907d385e3b94310f722.jsonl[1506] _id=69e268791724f0c9e2f7349a ts=2026-04-17T17:06:00.1990000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 5m 
  - Evidence: 96h 5m: 69cdc907d385e3b94310f722.jsonl[272] _id=69e270fe1724f0c9e2f7432c ts=2026-04-17T17:42:21.7390000Z -> 69cdc907d385e3b94310f722.jsonl[2192] _id=69e7b84e1724f0c9e2f94d9b ts=2026-04-21T17:47:57.9340000Z; 95h 30m: 69cdc907d385e3b94310f722.jsonl[830] _id=69dd31d07957a33870f26214 ts=2026-04-13T18:11:27.8740000Z -> 69cdc907d385e3b94310f722.jsonl[272] _id=69e270fe1724f0c9e2f7432c ts=2026-04-17T17:42:21.7390000Z; 48h 27m: 69cdc907d385e3b94310f722.jsonl[2192] _id=69e7b84e1724f0c9e2f94d9b ts=2026-04-21T17:47:57.9340000Z -> 69cdc907d385e3b94310f722.jsonl[2836] _id=69ea61d21724f0c9e2fb2181 ts=2026-04-23T18:15:46.4850000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f722.jsonl[1971] _id=69e27e831724f0c9e2f78cf2 ts=2026-04-17T18:40:02.5780000Z -> 69cdc907d385e3b94310f722.jsonl[343] _id=69e7abfb1724f0c9e2f915b1 ts=2026-04-21T16:55:23.2990000Z; 47h 8m: 69cdc907d385e3b94310f722.jsonl[997] _id=69dd38be7957a33870f2919e ts=2026-04-13T18:41:02.5360000Z -> 69cdc907d385e3b94310f722.jsonl[999] _id=69dfcf977957a33870f40f63 ts=2026-04-15T17:49:10.3580000Z; 46h 14m: 69cdc907d385e3b94310f722.jsonl[1377] _id=69dfdbb97957a33870f46697 ts=2026-04-15T18:40:56.8210000Z -> 69cdc907d385e3b94310f722.jsonl[1378] _id=69e2660a1724f0c9e2f7211e ts=2026-04-17T16:55:37.3230000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc907d385e3b94310f722.jsonl[321] _id=69e275ab1724f0c9e2f7626c ts=2026-04-17T18:02:18.9230000Z -> 69cdc907d385e3b94310f722.jsonl[2224] _id=69e7b9711724f0c9e2f95407 ts=2026-04-21T17:52:49.1550000Z; 47h 44m: 69cdc907d385e3b94310f722.jsonl[1227] _id=69dfd6277957a33870f43b4d ts=2026-04-15T18:17:10.7850000Z -> 69cdc907d385e3b94310f722.jsonl[320] _id=69e2758b1724f0c9e2f761e4 ts=2026-04-17T18:01:47.1190000Z; 47h 27m: 69cdc907d385e3b94310f722.jsonl[921] _id=69dd35d37957a33870f27dbe ts=2026-04-13T18:28:35.4310000Z -> 69cdc907d385e3b94310f722.jsonl[1050] _id=69dfd1277957a33870f41b19 ts=2026-04-15T17:55:50.6180000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 69cdc907d385e3b94310f722.jsonl[1710] _id=69e2737c1724f0c9e2f7542e ts=2026-04-17T17:53:00.0500000Z -> 69cdc907d385e3b94310f722.jsonl[2139] _id=69e7b6e61724f0c9e2f943bb ts=2026-04-21T17:41:58.6240000Z; 47h 12m: 69cdc907d385e3b94310f722.jsonl[1374] _id=69dfdb8d7957a33870f46547 ts=2026-04-15T18:40:12.9180000Z -> 69cdc907d385e3b94310f722.jsonl[1689] _id=69e273721724f0c9e2f753f6 ts=2026-04-17T17:52:50.0420000Z; 23m 52s: 69cdc907d385e3b94310f722.jsonl[1218] _id=69dfd5e47957a33870f439f9 ts=2026-04-15T18:16:03.5290000Z -> 69cdc907d385e3b94310f722.jsonl[1371] _id=69dfdb7c7957a33870f46501 ts=2026-04-15T18:39:56.0050000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 49m 
  - Evidence: 95h 49m: 69cdc907d385e3b94310f722.jsonl[285] _id=69e273791724f0c9e2f7541f ts=2026-04-17T17:52:56.6560000Z -> 69cdc907d385e3b94310f722.jsonl[2135] _id=69e7b6eb1724f0c9e2f943e5 ts=2026-04-21T17:42:03.2550000Z; 47h 40m: 69cdc907d385e3b94310f722.jsonl[1200] _id=69dfd4ef7957a33870f4350f ts=2026-04-15T18:11:58.6100000Z -> 69cdc907d385e3b94310f722.jsonl[291] _id=69e273771724f0c9e2f75412 ts=2026-04-17T17:52:55.1060000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 22m 
  - Evidence: 96h 22m: 69cdc907d385e3b94310f722.jsonl[1789] _id=69e274f51724f0c9e2f75e06 ts=2026-04-17T17:59:17.0750000Z -> 69cdc907d385e3b94310f722.jsonl[482] _id=69e7c0361724f0c9e2f985f7 ts=2026-04-21T18:21:42.1730000Z; 94h 56m: 69cdc907d385e3b94310f722.jsonl[55] _id=69dd311c7957a33870f25d34 ts=2026-04-13T18:08:28.3630000Z -> 69cdc907d385e3b94310f722.jsonl[1498] _id=69e268531724f0c9e2f7338a ts=2026-04-17T17:05:22.2990000Z; 47h 41m: 69cdc907d385e3b94310f722.jsonl[482] _id=69e7c0361724f0c9e2f985f7 ts=2026-04-21T18:21:42.1730000Z -> 69cdc907d385e3b94310f722.jsonl[583] _id=69ea5ec81724f0c9e2fb074d ts=2026-04-23T18:02:48.0230000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 57m 
  - Evidence: 94h 57m: 69cdc907d385e3b94310f722.jsonl[793] _id=69dd31177957a33870f25d0e ts=2026-04-13T18:08:22.6390000Z -> 69cdc907d385e3b94310f722.jsonl[1499] _id=69e268671724f0c9e2f73436 ts=2026-04-17T17:05:42.6670000Z; 52m 22s: 69cdc907d385e3b94310f722.jsonl[248] _id=69e2688d1724f0c9e2f7353a ts=2026-04-17T17:06:21.1170000Z -> 69cdc907d385e3b94310f722.jsonl[1780] _id=69e274d41724f0c9e2f75d00 ts=2026-04-17T17:58:43.3940000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 22m 
  - Evidence: 96h 22m: 69cdc907d385e3b94310f722.jsonl[1775] _id=69e274d31724f0c9e2f75cfc ts=2026-04-17T17:58:43.2800000Z -> 69cdc907d385e3b94310f722.jsonl[481] _id=69e7c02b1724f0c9e2f98599 ts=2026-04-21T18:21:30.8290000Z; 47h 35m: 69cdc907d385e3b94310f722.jsonl[498] _id=69e7c1681724f0c9e2f9904f ts=2026-04-21T18:26:48.4350000Z -> 69cdc907d385e3b94310f722.jsonl[2651] _id=69ea5ec71724f0c9e2fb0749 ts=2026-04-23T18:02:46.8020000Z; 52m 23s: 69cdc907d385e3b94310f722.jsonl[243] _id=69e268841724f0c9e2f734ea ts=2026-04-17T17:06:12.2020000Z -> 69cdc907d385e3b94310f722.jsonl[1777] _id=69e274cc1724f0c9e2f75cc2 ts=2026-04-17T17:58:35.8570000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.007s shown 
  - Evidence: 1ms: 69cdc907d385e3b94310f722.jsonl[2651] _id=69ea5ec71724f0c9e2fb0749 ts=2026-04-23T18:02:46.8020000Z -> 69cdc907d385e3b94310f722.jsonl[582] _id=69ea5ec71724f0c9e2fb074b ts=2026-04-23T18:02:46.8030000Z; 2ms: 69cdc907d385e3b94310f722.jsonl[481] _id=69e7c02b1724f0c9e2f98599 ts=2026-04-21T18:21:30.8290000Z -> 69cdc907d385e3b94310f722.jsonl[2465] _id=69e7c02b1724f0c9e2f9859e ts=2026-04-21T18:21:30.8310000Z; 7ms: 69cdc907d385e3b94310f722.jsonl[500] _id=69e7c1651724f0c9e2f99035 ts=2026-04-21T18:26:44.8020000Z -> 69cdc907d385e3b94310f722.jsonl[502] _id=69e7c1651724f0c9e2f99038 ts=2026-04-21T18:26:44.8090000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 19m 
  - Evidence: 94h 19m: 69cdc907d385e3b94310f722.jsonl[1940] _id=69e27d8f1724f0c9e2f786da ts=2026-04-17T18:35:57.8120000Z -> 69cdc907d385e3b94310f722.jsonl[1973] _id=69e7abfd1724f0c9e2f915cb ts=2026-04-21T16:55:24.1270000Z; 47h 13m: 69cdc907d385e3b94310f722.jsonl[956] _id=69dd376f7957a33870f288a4 ts=2026-04-13T18:35:26.4410000Z -> 69cdc907d385e3b94310f722.jsonl[998] _id=69dfcf997957a33870f40f67 ts=2026-04-15T17:49:12.5530000Z; 46h 21m: 69cdc907d385e3b94310f722.jsonl[1326] _id=69dfda2c7957a33870f457e9 ts=2026-04-15T18:34:18.3020000Z -> 69cdc907d385e3b94310f722.jsonl[1379] _id=69e2660d1724f0c9e2f7213a ts=2026-04-17T16:55:40.5110000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f722.jsonl[2881] _id=69ea64441724f0c9e2fb3417 ts=2026-04-23T18:25:34.5140000Z -> 69cdc907d385e3b94310f722.jsonl[2882] _id=69ea64571724f0c9e2fb34a3 ts=2026-04-23T18:25:34.5160000Z; 2ms: 69cdc907d385e3b94310f722.jsonl[771] _id=69dd30c37957a33870f25aaa ts=2026-04-13T18:06:59.1460000Z -> 69cdc907d385e3b94310f722.jsonl[773] _id=69dd30c37957a33870f25aac ts=2026-04-13T18:06:59.1480000Z; 4ms: 69cdc907d385e3b94310f722.jsonl[618] _id=69ea647e1724f0c9e2fb35c1 ts=2026-04-23T18:26:50.0480000Z -> 69cdc907d385e3b94310f722.jsonl[2888] _id=69ea648c1724f0c9e2fb3631 ts=2026-04-23T18:26:50.0520000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc907d385e3b94310f722.jsonl:69cdc907d385e3b94310f722, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f722.jsonl[921] _id=69dd35d37957a33870f27dbe ts=2026-04-13T18:28:35.4310000Z`; `69cdc907d385e3b94310f722.jsonl[1051] _id=69dfd12a7957a33870f41b3d ts=2026-04-15T17:55:53.6220000Z`; `69cdc907d385e3b94310f722.jsonl[1227] _id=69dfd6277957a33870f43b4d ts=2026-04-15T18:17:10.7850000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 28 record(s) match the trigger in 69cdc907d385e3b94310f722.jsonl:69cdc907d385e3b94310f722, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f722.jsonl[1116] _id=69dfd2e87957a33870f4286f ts=2026-04-15T18:03:19.8610000Z`; `69cdc907d385e3b94310f722.jsonl[131] _id=69dfd2eb7957a33870f42883 ts=2026-04-15T18:03:22.7420000Z`; `69cdc907d385e3b94310f722.jsonl[132] _id=69dfd2f47957a33870f428c2 ts=2026-04-15T18:03:31.6100000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f722.jsonl[198] _id=69dfda2f7957a33870f4582f ts=2026-04-15T18:34:20.2970000Z`; `69cdc907d385e3b94310f722.jsonl[282] _id=69e272e71724f0c9e2f75083 ts=2026-04-17T17:50:30.4130000Z`; `69cdc907d385e3b94310f722.jsonl[1699] _id=69e2731e1724f0c9e2f751da ts=2026-04-17T17:51:25.3610000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f722.jsonl[1789] _id=69e274f51724f0c9e2f75e06 ts=2026-04-17T17:59:17.0750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f722.jsonl[1778] _id=69e274ce1724f0c9e2f75cd6 ts=2026-04-17T17:58:38.0130000Z`; `69cdc907d385e3b94310f722.jsonl[481] _id=69e7c02b1724f0c9e2f98599 ts=2026-04-21T18:21:30.8290000Z`; `69cdc907d385e3b94310f722.jsonl[2465] _id=69e7c02b1724f0c9e2f9859e ts=2026-04-21T18:21:30.8310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `69cdc907d385e3b94310f722.jsonl[2002] _id=69e7acff1724f0c9e2f91acf ts=?`; `69cdc907d385e3b94310f722.jsonl[2364] _id=69e7bdbe1724f0c9e2f97317 ts=?`; `69cdc907d385e3b94310f722.jsonl[2592] _id=69e8e41e1724f0c9e2fa75cb ts=?`
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f722.jsonl[583] _id=69ea5ec81724f0c9e2fb074d ts=2026-04-23T18:02:48.0230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 236 unmatched 'DialogueStartEvent' (totals: 431 start, 199 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationSessionOpen' (totals: 7 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 17 open, 21 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 46 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.59s, min -130.01s, max -0.18s over 2985 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f722\coverage.yaml

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
  - Observed: 40 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2024 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (669); Unit 4 Dev - Anderson Base (267); Unit 3 Dev (258); Unit 4 Dev (251); Unit 3 Dungeon Dev (200); Unit 1 Dev (198); Unit 4 Dev - Dungeon (90); Unit 5 Dev - Dungeon (46); Unit 5 Dev (45)
- **eventKey:** present on 1394 of 2024 records
- **Intervals:** median 1.25s (p5 0.01s / p95 39.72s, n=2023)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1394; [conversationId, dialogueEventType] x630
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2024/2024 records)
    numeric range 8 .. 114 (48 unique)
data.dialogueEventType  (string, 2024/2024 records)
    "DialogueNodeEvent"  x1394
    "DialogueStartEvent"  x431
    "DialogueFinishEvent"  x199
data.nodeId  (number, 1394/2024 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 672 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (249); Unit 3 Dungeon Dev (135); Unit 4 Dev - Anderson Base (66); Unit 4 Dev (54); Unit 3 Dev (53); Unit 1 Dev (41); Unit 5 Dev - Dungeon (36); Unit 4 Dev - Dungeon (29); Unit 5 Dev (9)
- **Intervals:** median 30.01s (p5 29.97s / p95 38.18s, n=658)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 672/672 records)
data.position.x  (number, 672/672 records)
    numeric range -733.114 .. 1621.39 (331 unique)
data.position.y  (number, 672/672 records)
    numeric range -115.127 .. 220.34 (249 unique)
data.position.z  (number, 672/672 records)
    numeric range -1107.06 .. 2125.34 (331 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 3 Dev (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (6); Unit 4 Dev - Anderson Base (6); Unit 5 Dev (1)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 170.99s (p5 0.01s / p95 80290.48s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x46; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x46
    "questFinishEvent"  x30
data.questID  (string, 76/76 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/76 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (18)
- **Intervals:** median 12.52s (p5 1.94s / p95 18284.94s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 39 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (39)
- **Intervals:** median 12.22s (p5 1.19s / p95 51.18s, n=38)
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "On"  x29
    "Off"  x10
data.floor  (string, 39/39 records)
    "3"  x31
    "4"  x6
    "1"  x2
data.machineNumber  (string, 39/39 records)
    "One"  x39
data.machineType  (string, 39/39 records)
    "Condenser"  x25
    "DualChamber_Evaporator"  x5
    "VentSwitch"  x5
    "Evaporator"  x3
    "DualChamber_Condenser"  x1
data.room  (string, 39/39 records)
    "2"  x14
    "1"  x12
    "4"  x10
    "3"  x3
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 38 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (22); Unit 2 Prod (Refactor) (12); Unit 3 Dev (4)
- **Intervals:** median 2.11s (p5 0.01s / p95 36786.60s, n=37)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "argumentationToolClose"  x21
    "argumentationToolOpen"  x17
data.argumentationTitle  (string, 38/38 records)
    "Unit 4 - Flooding"  x22
    "Unit 2 – Watershed"  x12
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 38/38 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x14
    "BackingInfoPanel - Soil Flow Rates"  x8
    "BackingInfoPanel - Waterfall Data"  x8
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TopographicMapEvent` — 28 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (6)
- **Intervals:** median 3.74s (p5 1.61s / p95 120207.35s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "dragEnd"  x14
    "dragStart"  x14
data.featureUsed  (string, 28/28 records)
    "waypoint"  x28
data.location  (object, 28/28 records)
data.location.x  (number, 28/28 records)
    numeric range -869.203 .. 211.939 (15 unique)
data.location.y  (number, 28/28 records)
    numeric range -318.647 .. 329.476 (15 unique)
data.location.z  (number, 28/28 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 5.27s (p5 0.89s / p95 75.64s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Bedrock"  x13
    "Clay"  x6
    "Gravel"  x4
    "Sand"  x3
data.floor  (string, 26/26 records)
    "5"  x13
    "4"  x12
    "3"  x1
data.machine  (string, 26/26 records)
    "1"  x25
    "2"  x1
data.row  (string, 26/26 records)
    "TopRow"  x20
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (1)
- **Intervals:** median 60.00s (p5 0.46s / p95 344379.52s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionOpen"  x7
    "argumentationSessionClose"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x2
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationNodeEvent` — 11 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 1 Dev (3); Unit 3 Dev (3)
- **Intervals:** median 9.91s (p5 3.81s / p95 189426.04s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 2 – Watershed"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 11/11 records)
    "I"  x4
    "1"  x2
    "A"  x2
    "5"  x1
    "B"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 59.34s (p5 3.09s / p95 275768.67s, n=9)
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

### `TerasGardenBox` — 5 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (5)
- **Intervals:** median 13.77s (p5 1.77s / p95 25.77s, n=4)
- **`data` key-set variants:** [actionType, boxId, soilType] x3; [actionType, boxID, soilType] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "cameraPlaced"  x3
    "soilSelected"  x2
data.boxID  (string, 2/5 records)
    "1"  x2
data.boxId  (string, 3/5 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 5/5 records)
    "Gravel"  x2
    "None"  x2
    "Sand"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "Uncaught ReferenceError: onResize is not defined"  x5
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x4
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 5/5 records)
    "runtime_error"  x5
data.unitId  (string, 5/5 records)
    "unit4"  x4
    "unit3"  x1
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 343853.86s (p5 191407.08s / p95 345727.96s, n=3)
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "dragStart" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)
- `soilMachine` data.canisterType: "Bedrock" (13x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*