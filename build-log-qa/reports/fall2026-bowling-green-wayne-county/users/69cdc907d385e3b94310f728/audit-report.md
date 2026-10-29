# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f728

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f728
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f728.jsonl
- **Records:** 2534 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f728
- **Time span:** 2026-04-13T17:54:38.716000+00:00 .. 2026-04-21T18:40:23.640000+00:00 (192h 45m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f728\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2534 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 66 INFO, 0 NOT_TESTED, 52 PASS.
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
| DialogueEvent | 1764 | 69.61 | 1 | 9 | 1224 | 2026-04-13T17:54:56.584000+00:00 | 2026-04-21T18:40:23.208000+00:00 | 192h 45m |
| PlayerPositionEvent | 482 | 19.02 | 1 | 9 | 0 | 2026-04-13T17:54:38.716000+00:00 | 2026-04-21T18:40:23.640000+00:00 | 192h 45m |
| Topographic Map Event | 82 | 3.24 | 1 | 2 | 0 | 2026-04-13T18:33:44.683000+00:00 | 2026-04-21T17:46:06.759000+00:00 | 191h 12m |
| questEvent | 69 | 2.72 | 1 | 9 | 69 | 2026-04-13T17:54:56.567000+00:00 | 2026-04-21T18:39:54.054000+00:00 | 192h 44m |
| argumentationToolEvent | 40 | 1.58 | 1 | 3 | 0 | 2026-04-17T18:24:52.844000+00:00 | 2026-04-21T18:38:59.847000+00:00 | 96h 14m |
| WaterChamberEvent | 31 | 1.22 | 1 | 1 | 0 | 2026-04-21T18:31:21.025000+00:00 | 2026-04-21T18:36:04.413000+00:00 | 4m 43s |
| soilMachine | 30 | 1.18 | 1 | 1 | 0 | 2026-04-21T18:01:06.886000+00:00 | 2026-04-21T18:09:44.328000+00:00 | 8m 37s |
| argumentationEvent | 10 | 0.39 | 1 | 4 | 0 | 2026-04-13T18:10:10.525000+00:00 | 2026-04-21T18:39:43.899000+00:00 | 192h 29m |
| argumentationNodeEvent | 10 | 0.39 | 1 | 2 | 0 | 2026-04-13T18:10:42.276000+00:00 | 2026-04-17T18:24:48.348000+00:00 | 96h 14m |
| Soil Key Puzzle | 8 | 0.32 | 1 | 3 | 0 | 2026-04-13T18:26:42.990000+00:00 | 2026-04-21T17:52:17.738000+00:00 | 191h 25m |
| EndOfUnit | 3 | 0.12 | 1 | 3 | 0 | 2026-04-13T18:14:20.424000+00:00 | 2026-04-21T18:27:03.520000+00:00 | 192h 12m |
| TerasGardenBox | 3 | 0.12 | 1 | 1 | 0 | 2026-04-21T18:24:54.370000+00:00 | 2026-04-21T18:25:29.254000+00:00 | 34.9s |
| crash | 2 | 0.08 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 0.849s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 345981.548s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.0s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 67.431s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 17.442s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 83 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.859s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.708s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.182s median 
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
  - Observed: 4.474s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
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
  - Observed: 82 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 10 records 
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
  - Observed: 2; 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 4.4x vs baseline. 
  - Observed: 40 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.0x vs baseline. 
  - Observed: 30 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 44 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f728.jsonl[52] _id=69dd31c67957a33870f261be ts=2026-04-13T18:11:17.9620000Z`; `69cdc907d385e3b94310f728.jsonl[180] _id=69dfd2c67957a33870f42773 ts=2026-04-15T18:02:46.2110000Z`; `69cdc907d385e3b94310f728.jsonl[1301] _id=69dfd3d27957a33870f42ea5 ts=2026-04-15T18:07:13.7640000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1763 | 0.002 | 0.849 | 393.606 | 35.963 | 334909.111 | 0.15 | 466 | 5 |
| PlayerPositionEvent | 470 | 29.928 | 30.0 | 1114.997 | 34.377 | 334921.821 | 0.05 | 0 | 3 |
| Topographic Map Event | 81 | 0.307 | 7.753 | 8498.05 | 299.635 | 343909.892 | 0.01 | 0 | 4 |
| questEvent | 68 | 0.002 | 111.712 | 10204.375 | 4245.88 | 334921.753 | 0.01 | 12 | 7 |
| argumentationToolEvent | 39 | 0.0 | 1.182 | 8883.256 | 194.641 | 345107.663 | 0.01 | 2 | 2 |
| WaterChamberEvent | 30 | 0.117 | 5.859 | 9.446 | 25.387 | 26.404 | 6.35 | 0 | 0 |
| soilMachine | 29 | 0.168 | 4.474 | 17.843 | 89.909 | 109.111 | 3.36 | 0 | 0 |
| argumentationEvent | 9 | 0.028 | 51.534 | 76997.042 | 345862.901 | 346364.155 | 0.0 | 1 | 3 |
| argumentationNodeEvent | 9 | 1.419 | 7.708 | 38494.008 | 207836.552 | 346378.187 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 7 | 2.965 | 67.431 | 98447.821 | 292312.71 | 343193.445 | 0.0 | 0 | 3 |
| EndOfUnit | 2 | 2368.554 | 345981.548 | 345981.548 | 655233.243 | 689594.542 | 0.0 | 0 | 2 |
| TerasGardenBox | 2 | 14.869 | 17.442 | 17.442 | 19.758 | 20.015 | 3.44 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `argumentationToolEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f728.jsonl[2271] _id=69e7bf161724f0c9e2f97ca9 ts=2026-04-21T18:16:53.6450000Z == 69cdc907d385e3b94310f728.jsonl[664] _id=69e7bf161724f0c9e2f97cad ts=2026-04-21T18:16:53.6450000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc907d385e3b94310f728.jsonl[457] _id=69e7ab721724f0c9e2f91511 ts=? == 69cdc907d385e3b94310f728.jsonl[1862] _id=69e7acd01724f0c9e2f919cd ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.000s (p5 29.98s, p95 34.38s, n=470) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `183ms: 69cdc907d385e3b94310f728.jsonl[826] _id=69e7c3771724f0c9e2f99ec7 ts=2026-04-21T18:35:35.1390000Z ~ 69cdc907d385e3b94310f728.jsonl[827] _id=69e7c3771724f0c9e2f99ecb ts=2026-04-21T18:35:35.3220000Z`; `664ms: 69cdc907d385e3b94310f728.jsonl[824] _id=69e7c3771724f0c9e2f99ec5 ts=2026-04-21T18:35:34.8080000Z ~ 69cdc907d385e3b94310f728.jsonl[2467] _id=69e7c3781724f0c9e2f99ed1 ts=2026-04-21T18:35:35.4720000Z`; `117ms: 69cdc907d385e3b94310f728.jsonl[2467] _id=69e7c3781724f0c9e2f99ed1 ts=2026-04-21T18:35:35.4720000Z ~ 69cdc907d385e3b94310f728.jsonl[2470] _id=69e7c3781724f0c9e2f99ed5 ts=2026-04-21T18:35:35.5890000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 69cdc907d385e3b94310f728.jsonl[1776] _id=69e27b031724f0c9e2f77e44 ts=2026-04-17T18:25:06.0870000Z ~ 69cdc907d385e3b94310f728.jsonl[409] _id=69e27b041724f0c9e2f77e4a ts=2026-04-17T18:25:06.1150000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `576ms: 69cdc907d385e3b94310f728.jsonl[671] _id=69e7bfa41724f0c9e2f98129 ts=2026-04-21T18:19:15.2160000Z ~ 69cdc907d385e3b94310f728.jsonl[672] _id=69e7bfa41724f0c9e2f9812d ts=2026-04-21T18:19:15.7920000Z`; `117ms: 69cdc907d385e3b94310f728.jsonl[672] _id=69e7bfa41724f0c9e2f9812d ts=2026-04-21T18:19:15.7920000Z ~ 69cdc907d385e3b94310f728.jsonl[674] _id=69e7bfa51724f0c9e2f98130 ts=2026-04-21T18:19:15.9090000Z`; `784ms: 69cdc907d385e3b94310f728.jsonl[2232] _id=69e7c0151724f0c9e2f98503 ts=2026-04-21T18:21:09.3020000Z ~ 69cdc907d385e3b94310f728.jsonl[2320] _id=69e7c0161724f0c9e2f9850b ts=2026-04-21T18:21:10.0860000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 69cdc907d385e3b94310f728.jsonl[2528] _id=69e7c47a1724f0c9e2f9a6e1 ts=2026-04-21T18:39:54.0500000Z ~ 69cdc907d385e3b94310f728.jsonl[843] _id=69e7c47b1724f0c9e2f9a6eb ts=2026-04-21T18:39:54.0540000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `736ms: 69cdc907d385e3b94310f728.jsonl[2164] _id=69e7bc301724f0c9e2f96871 ts=2026-04-21T18:04:31.7220000Z ~ 69cdc907d385e3b94310f728.jsonl[585] _id=69e7bc301724f0c9e2f9687e ts=2026-04-21T18:04:32.4580000Z`; `216ms: 69cdc907d385e3b94310f728.jsonl[585] _id=69e7bc301724f0c9e2f9687e ts=2026-04-21T18:04:32.4580000Z ~ 69cdc907d385e3b94310f728.jsonl[584] _id=69e7bc311724f0c9e2f96887 ts=2026-04-21T18:04:32.6740000Z`; `168ms: 69cdc907d385e3b94310f728.jsonl[584] _id=69e7bc311724f0c9e2f96887 ts=2026-04-21T18:04:32.6740000Z ~ 69cdc907d385e3b94310f728.jsonl[586] _id=69e7bc311724f0c9e2f9688b ts=2026-04-21T18:04:32.8420000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 93h 1m 
  - Evidence: 93h 1m: 69cdc907d385e3b94310f728.jsonl[1861] _id=69e291561724f0c9e2f7d1ee ts=2026-04-17T20:00:21.4150000Z -> 69cdc907d385e3b94310f728.jsonl[1863] _id=69e7ad931724f0c9e2f91eb9 ts=2026-04-21T17:02:10.5260000Z; 47h 12m: 69cdc907d385e3b94310f728.jsonl[125] _id=69dd38aa7957a33870f2915a ts=2026-04-13T18:40:42.8480000Z -> 69cdc907d385e3b94310f728.jsonl[1178] _id=69dfd08f7957a33870f415e9 ts=2026-04-15T17:53:19.5960000Z; 47h 7m: 69cdc907d385e3b94310f728.jsonl[325] _id=69dfdbb17957a33870f46672 ts=2026-04-15T18:40:49.7880000Z -> 69cdc907d385e3b94310f728.jsonl[1545] _id=69e272471724f0c9e2f74c5a ts=2026-04-17T17:47:50.4520000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 466 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f728.jsonl[1777] _id=69e27b031724f0c9e2f77e46 ts=2026-04-17T18:25:06.0950000Z -> 69cdc907d385e3b94310f728.jsonl[1775] _id=69e27b031724f0c9e2f77e48 ts=2026-04-17T18:25:06.0970000Z; 2ms: 69cdc907d385e3b94310f728.jsonl[1799] _id=69e27cae1724f0c9e2f78200 ts=2026-04-17T18:32:13.5000000Z -> 69cdc907d385e3b94310f728.jsonl[1800] _id=69e27cae1724f0c9e2f78202 ts=2026-04-17T18:32:13.5020000Z; 2ms: 69cdc907d385e3b94310f728.jsonl[421] _id=69e27b981724f0c9e2f77f14 ts=2026-04-17T18:27:35.0410000Z -> 69cdc907d385e3b94310f728.jsonl[1792] _id=69e27b991724f0c9e2f77f16 ts=2026-04-17T18:27:35.0430000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 33m 
  - Evidence: 191h 33m: 69cdc907d385e3b94310f728.jsonl[1032] _id=69dd327c7957a33870f26706 ts=2026-04-13T18:14:20.4240000Z -> 69cdc907d385e3b94310f728.jsonl[2048] _id=69e7b8371724f0c9e2f94d11 ts=2026-04-21T17:47:34.9660000Z; 39m 28s: 69cdc907d385e3b94310f728.jsonl[2048] _id=69e7b8371724f0c9e2f94d11 ts=2026-04-21T17:47:34.9660000Z -> 69cdc907d385e3b94310f728.jsonl[801] _id=69e7c1771724f0c9e2f990ed ts=2026-04-21T18:27:03.5200000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 93h 2m 
  - Evidence: 93h 2m: 69cdc907d385e3b94310f728.jsonl[1858] _id=69e291471724f0c9e2f7d1b1 ts=2026-04-17T20:00:06.8570000Z -> 69cdc907d385e3b94310f728.jsonl[1866] _id=69e7ad911724f0c9e2f91ea9 ts=2026-04-21T17:02:08.6780000Z; 47h 12m: 69cdc907d385e3b94310f728.jsonl[1175] _id=69dd38c97957a33870f291ce ts=2026-04-13T18:41:13.3860000Z -> 69cdc907d385e3b94310f728.jsonl[1177] _id=69dfd08b7957a33870f415c9 ts=2026-04-15T17:53:15.5230000Z; 1h 19m: 69cdc907d385e3b94310f728.jsonl[1853] _id=69e27e951724f0c9e2f78d14 ts=2026-04-17T18:40:20.5420000Z -> 69cdc907d385e3b94310f728.jsonl[1858] _id=69e291471724f0c9e2f7d1b1 ts=2026-04-17T20:00:06.8570000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 69cdc907d385e3b94310f728.jsonl[1798] _id=69e27ca61724f0c9e2f781d2 ts=2026-04-17T18:32:05.1880000Z -> 69cdc907d385e3b94310f728.jsonl[545] _id=69e7b93e1724f0c9e2f95315 ts=2026-04-21T17:51:58.6330000Z; 48h 13m: 69cdc907d385e3b94310f728.jsonl[1351] _id=69dfd6787957a33870f43db3 ts=2026-04-15T18:18:33.1010000Z -> 69cdc907d385e3b94310f728.jsonl[429] _id=69e27c911724f0c9e2f78155 ts=2026-04-17T18:31:44.0950000Z; 47h 50m: 69cdc907d385e3b94310f728.jsonl[89] _id=69dd35667957a33870f27aec ts=2026-04-13T18:26:45.9550000Z -> 69cdc907d385e3b94310f728.jsonl[1342] _id=69dfd6357957a33870f43bb1 ts=2026-04-15T18:17:25.6700000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 69cdc907d385e3b94310f728.jsonl[377] _id=69e2785a1724f0c9e2f7709e ts=2026-04-17T18:13:46.0140000Z -> 69cdc907d385e3b94310f728.jsonl[2013] _id=69e7b7c01724f0c9e2f9495b ts=2026-04-21T17:45:35.9060000Z; 47h 23m: 69cdc907d385e3b94310f728.jsonl[281] _id=69dfd9f37957a33870f455f7 ts=2026-04-15T18:33:23.4610000Z -> 69cdc907d385e3b94310f728.jsonl[1627] _id=69e274841724f0c9e2f75ae8 ts=2026-04-17T17:57:23.3860000Z; 47h 23m: 69cdc907d385e3b94310f728.jsonl[1160] _id=69dd37f17957a33870f28bb8 ts=2026-04-13T18:37:37.0580000Z -> 69cdc907d385e3b94310f728.jsonl[165] _id=69dfd2677957a33870f424f9 ts=2026-04-15T18:01:11.0650000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc907d385e3b94310f728.jsonl[51] _id=69dd31c67957a33870f261ba ts=2026-04-13T18:11:17.9330000Z -> 69cdc907d385e3b94310f728.jsonl[402] _id=69e27ac31724f0c9e2f77ca6 ts=2026-04-17T18:24:02.0880000Z; 95h 51m: 69cdc907d385e3b94310f728.jsonl[409] _id=69e27b041724f0c9e2f77e4a ts=2026-04-17T18:25:06.1150000Z -> 69cdc907d385e3b94310f728.jsonl[665] _id=69e7bf191724f0c9e2f97cc9 ts=2026-04-21T18:16:57.1350000Z; 21m 55s: 69cdc907d385e3b94310f728.jsonl[665] _id=69e7bf191724f0c9e2f97cc9 ts=2026-04-21T18:16:57.1350000Z -> 69cdc907d385e3b94310f728.jsonl[838] _id=69e7c43c1724f0c9e2f9a57b ts=2026-04-21T18:38:52.3650000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.028s..0.028s shown 
  - Evidence: 28ms: 69cdc907d385e3b94310f728.jsonl[1776] _id=69e27b031724f0c9e2f77e44 ts=2026-04-17T18:25:06.0870000Z -> 69cdc907d385e3b94310f728.jsonl[409] _id=69e27b041724f0c9e2f77e4a ts=2026-04-17T18:25:06.1150000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc907d385e3b94310f728.jsonl[988] _id=69dd31c47957a33870f261a6 ts=2026-04-13T18:11:16.0590000Z -> 69cdc907d385e3b94310f728.jsonl[1760] _id=69e27acf1724f0c9e2f77cfc ts=2026-04-17T18:24:14.2460000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 69cdc907d385e3b94310f728.jsonl[406] _id=69e27b021724f0c9e2f77e42 ts=2026-04-17T18:25:05.9820000Z -> 69cdc907d385e3b94310f728.jsonl[2271] _id=69e7bf161724f0c9e2f97ca9 ts=2026-04-21T18:16:53.6450000Z; 16m 57s: 69cdc907d385e3b94310f728.jsonl[2329] _id=69e7c0491724f0c9e2f986a0 ts=2026-04-21T18:22:00.6490000Z -> 69cdc907d385e3b94310f728.jsonl[840] _id=69e7c4421724f0c9e2f9a5ad ts=2026-04-21T18:38:58.1610000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.008s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f728.jsonl[2271] _id=69e7bf161724f0c9e2f97ca9 ts=2026-04-21T18:16:53.6450000Z -> 69cdc907d385e3b94310f728.jsonl[664] _id=69e7bf161724f0c9e2f97cad ts=2026-04-21T18:16:53.6450000Z; 8ms: 69cdc907d385e3b94310f728.jsonl[2289] _id=69e7bfa31724f0c9e2f9811f ts=2026-04-21T18:19:15.2080000Z -> 69cdc907d385e3b94310f728.jsonl[671] _id=69e7bfa41724f0c9e2f98129 ts=2026-04-21T18:19:15.2160000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 93h 2m 
  - Evidence: 93h 2m: 69cdc907d385e3b94310f728.jsonl[1859] _id=69e2914a1724f0c9e2f7d1c4 ts=2026-04-17T20:00:08.4640000Z -> 69cdc907d385e3b94310f728.jsonl[1865] _id=69e7ad921724f0c9e2f91eaf ts=2026-04-21T17:02:10.2170000Z; 47h 20m: 69cdc907d385e3b94310f728.jsonl[250] _id=69dfd8d47957a33870f44e71 ts=2026-04-15T18:28:36.5350000Z -> 69cdc907d385e3b94310f728.jsonl[338] _id=69e272a71724f0c9e2f74eec ts=2026-04-17T17:49:26.6830000Z; 47h 19m: 69cdc907d385e3b94310f728.jsonl[118] _id=69dd37047957a33870f28676 ts=2026-04-13T18:33:40.7850000Z -> 69cdc907d385e3b94310f728.jsonl[126] _id=69dfd08e7957a33870f415df ts=2026-04-15T17:53:18.2310000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f728.jsonl[968] _id=69dd31647957a33870f25f1a ts=2026-04-13T18:09:39.7170000Z -> 69cdc907d385e3b94310f728.jsonl[22] _id=69dd31647957a33870f25f1c ts=2026-04-13T18:09:39.7190000Z; 3ms: 69cdc907d385e3b94310f728.jsonl[2441] _id=69e7c29e1724f0c9e2f99949 ts=2026-04-21T18:31:58.4750000Z -> 69cdc907d385e3b94310f728.jsonl[812] _id=69e7c29e1724f0c9e2f9994b ts=2026-04-21T18:31:58.4780000Z; 3ms: 69cdc907d385e3b94310f728.jsonl[2448] _id=69e7c2e61724f0c9e2f99af5 ts=2026-04-21T18:33:09.8240000Z -> 69cdc907d385e3b94310f728.jsonl[820] _id=69e7c2e61724f0c9e2f99afb ts=2026-04-21T18:33:09.8270000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f728.jsonl:69cdc907d385e3b94310f728, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f728.jsonl[89] _id=69dd35667957a33870f27aec ts=2026-04-13T18:26:45.9550000Z`; `69cdc907d385e3b94310f728.jsonl[1351] _id=69dfd6787957a33870f43db3 ts=2026-04-15T18:18:33.1010000Z`; `69cdc907d385e3b94310f728.jsonl[1798] _id=69e27ca61724f0c9e2f781d2 ts=2026-04-17T18:32:05.1880000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f728.jsonl[246] _id=69dfd8e87957a33870f44f01 ts=2026-04-15T18:28:56.9160000Z`; `69cdc907d385e3b94310f728.jsonl[1587] _id=69e2739d1724f0c9e2f754fe ts=2026-04-17T17:53:32.5840000Z`; `69cdc907d385e3b94310f728.jsonl[1599] _id=69e273d21724f0c9e2f756a4 ts=2026-04-17T17:54:24.8440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f728.jsonl[409] _id=69e27b041724f0c9e2f77e4a ts=2026-04-17T18:25:06.1150000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f728.jsonl[2271] _id=69e7bf161724f0c9e2f97ca9 ts=2026-04-21T18:16:53.6450000Z`; `69cdc907d385e3b94310f728.jsonl[664] _id=69e7bf161724f0c9e2f97cad ts=2026-04-21T18:16:53.6450000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc907d385e3b94310f728.jsonl[457] _id=69e7ab721724f0c9e2f91511 ts=?`; `69cdc907d385e3b94310f728.jsonl[1862] _id=69e7acd01724f0c9e2f919cd ts=?`
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 10 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f728.jsonl[672] _id=69e7bfa41724f0c9e2f9812d ts=2026-04-21T18:19:15.7920000Z`; `69cdc907d385e3b94310f728.jsonl[674] _id=69e7bfa51724f0c9e2f98130 ts=2026-04-21T18:19:15.9090000Z`; `69cdc907d385e3b94310f728.jsonl[675] _id=69e7bfa51724f0c9e2f98139 ts=2026-04-21T18:19:17.1750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 204 unmatched 'DialogueStartEvent' (totals: 370 start, 170 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 22 open, 18 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 40 start, 29 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.35s, min -2.90s, max +0.17s over 2532 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f728\coverage.yaml

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
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=complete, Unit3=complete 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
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
  - Observed: 82 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1764 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (577); Unit 3 Dev (316); Unit 4 Dev (220); Unit 1 Dev (173); Unit 3 Dungeon Dev (136); Unit 4 Dev - Anderson Base (131); Unit 4 Dev - Dungeon (107); Unit 5 Dev (76); Unit 5 Dev - Dungeon (28)
- **eventKey:** present on 1224 of 1764 records
- **Intervals:** median 0.85s (p5 0.01s / p95 35.96s, n=1763)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1224; [conversationId, dialogueEventType] x540
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1764/1764 records)
    numeric range 8 .. 114 (47 unique)
data.dialogueEventType  (string, 1764/1764 records)
    "DialogueNodeEvent"  x1224
    "DialogueStartEvent"  x370
    "DialogueFinishEvent"  x170
data.nodeId  (number, 1224/1764 records)
    numeric range 0 .. 290 (222 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 482 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (140); Unit 3 Dev (98); Unit 3 Dungeon Dev (98); Unit 1 Dev (40); Unit 4 Dev - Dungeon (33); Unit 4 Dev (29); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (17); Unit 5 Dev (9)
- **Intervals:** median 30.00s (p5 29.98s / p95 34.38s, n=470)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 482/482 records)
data.position.x  (number, 482/482 records)
    numeric range -575.11 .. 1556.66 (250 unique)
data.position.y  (number, 482/482 records)
    numeric range -112.488 .. 217.708 (211 unique)
data.position.z  (number, 482/482 records)
    numeric range -1114.65 .. 2180.89 (250 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 82 records

- **Scenes:** Unit 3 Dev (42); Unit 2 Prod (Refactor) (40)
- **Intervals:** median 7.75s (p5 1.87s / p95 299.63s, n=81)
- **Fields under `data`:**

```text
data.actionType  (string, 82/82 records)
    "MapCloseEvent"  x41
    "MapOpenEvent"  x41
data.featureUsed  (string, 82/82 records)
    "Map"  x82
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 69 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 5 Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 69 of 69 records
- **Intervals:** median 111.71s (p5 0.00s / p95 4245.88s, n=68)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x29
- **Fields under `data`:**

```text
data.questEventType  (string, 69/69 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x29
data.questID  (string, 69/69 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 69/69 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 29/69 records)
    "Succeeded"  x29
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 40 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (36); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 1.18s (p5 0.08s / p95 194.64s, n=39)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "argumentationToolOpen"  x22
    "argumentationToolClose"  x18
data.argumentationTitle  (string, 40/40 records)
    "Unit 4 - Flooding"  x36
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
data.toolName  (string, 40/40 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x20
    "BackingInfoPanel - Soil Flow Rates"  x16
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `WaterChamberEvent` — 31 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (31)
- **Intervals:** median 5.86s (p5 0.16s / p95 25.39s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "On"  x21
    "Off"  x10
data.floor  (string, 31/31 records)
    "4"  x15
    "3"  x8
    "2"  x6
    "1"  x2
data.machineNumber  (string, 31/31 records)
    "One"  x30
    "Two"  x1
data.machineType  (string, 31/31 records)
    "Condenser"  x18
    "Evaporator"  x8
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 31/31 records)
    "2"  x12
    "3"  x12
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 30 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (30)
- **Intervals:** median 4.47s (p5 0.19s / p95 89.91s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "ChangeCanister"  x30
data.canisterType  (string, 30/30 records)
    "Bedrock"  x19
    "Clay"  x8
    "Gravel"  x3
data.floor  (string, 30/30 records)
    "5"  x28
    "3"  x1
    "4"  x1
data.machine  (string, 30/30 records)
    "1"  x29
    "2"  x1
data.row  (string, 30/30 records)
    "BottomRow"  x20
    "TopRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 51.53s (p5 1.25s / p95 345862.90s, n=9)
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

### `argumentationNodeEvent` — 10 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (3)
- **Intervals:** median 7.71s (p5 2.00s / p95 207836.55s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationNodeAdd"  x8
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Freshwater"  x7
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 10/10 records)
    "B"  x3
    "I"  x2
    "II"  x2
    "1"  x1
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 67.43s (p5 7.81s / p95 292312.71s, n=7)
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

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 345981.55s (p5 36729.85s / p95 655233.24s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 3 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (3)
- **Intervals:** median 17.44s (p5 15.13s / p95 19.76s, n=2)
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

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Unknown data format (id="")"  x2
data.phase  (string, 2/2 records)
    "compiling"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
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
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `argumentationToolEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TerasGardenBox` data.soilType: "None" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (19x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*