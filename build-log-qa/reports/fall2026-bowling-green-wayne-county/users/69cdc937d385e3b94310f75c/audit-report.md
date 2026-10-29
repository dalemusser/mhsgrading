# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75c
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f75c.jsonl
- **Records:** 2200 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f75c
- **Time span:** 2026-04-13T19:34:40.468000+00:00 .. 2026-04-21T20:06:14.313000+00:00 (192h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2200 records, 9 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 67 INFO, 0 NOT_TESTED, 55 PASS.
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
| DialogueEvent | 1486 | 67.55 | 1 | 9 | 1049 | 2026-04-13T19:34:58.687000+00:00 | 2026-04-21T20:06:03.212000+00:00 | 192h 31m |
| PlayerPositionEvent | 450 | 20.45 | 1 | 9 | 0 | 2026-04-13T19:34:40.468000+00:00 | 2026-04-21T20:05:50.194000+00:00 | 192h 31m |
| questEvent | 72 | 3.27 | 1 | 9 | 72 | 2026-04-13T19:34:58.672000+00:00 | 2026-04-21T20:05:15.781000+00:00 | 192h 30m |
| Topographic Map Event | 58 | 2.64 | 1 | 2 | 0 | 2026-04-15T19:19:56.115000+00:00 | 2026-04-17T20:03:12.672000+00:00 | 48h 43m |
| TopographicMapEvent | 36 | 1.64 | 1 | 2 | 0 | 2026-04-15T19:39:29.260000+00:00 | 2026-04-17T19:51:19.103000+00:00 | 48h 11m |
| WaterChamberEvent | 33 | 1.5 | 1 | 1 | 0 | 2026-04-21T19:46:41.279000+00:00 | 2026-04-21T19:52:49.651000+00:00 | 6m 8s |
| argumentationNodeEvent | 17 | 0.77 | 1 | 2 | 0 | 2026-04-15T19:12:30.683000+00:00 | 2026-04-17T19:28:09.604000+00:00 | 48h 15m |
| soilMachine | 13 | 0.59 | 1 | 1 | 0 | 2026-04-21T19:11:21.169000+00:00 | 2026-04-21T19:17:28.470000+00:00 | 6m 7s |
| TerasGardenBox | 10 | 0.45 | 1 | 1 | 0 | 2026-04-21T19:33:29.723000+00:00 | 2026-04-21T19:34:21.581000+00:00 | 51.9s |
| argumentationEvent | 10 | 0.45 | 1 | 4 | 0 | 2026-04-15T19:12:24.883000+00:00 | 2026-04-21T19:59:11.208000+00:00 | 144h 46m |
| Soil Key Puzzle | 9 | 0.41 | 1 | 3 | 0 | 2026-04-15T19:29:18.609000+00:00 | 2026-04-21T18:59:00.996000+00:00 | 143h 29m |
| EndOfUnit | 4 | 0.18 | 1 | 4 | 0 | 2026-04-15T19:18:46.074000+00:00 | 2026-04-21T20:06:14.313000+00:00 | 144h 47m |
| argumentationToolEvent | 2 | 0.09 | 1 | 1 | 0 | 2026-04-21T19:27:48.425000+00:00 | 2026-04-21T19:27:48.427000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 175619.926s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.002s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 820.892s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.531s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.67s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.197s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.573s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.002s median 
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
  - Observed: 15.732s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 9 records 
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
  - Observed: 58 records this build 
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
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 17 records 
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
  - Observed: 2; 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationToolOpen 
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
  - Observed: BackingInfoPanel - Soil Flow Rates 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[520] _id=69dfe3e27957a33870f46bb7 ts=2026-04-15T19:15:46.4840000Z`; `69cdc937d385e3b94310f75c.jsonl[753] _id=69dfea1d7957a33870f484ac ts=2026-04-15T19:42:20.9680000Z`; `69cdc937d385e3b94310f75c.jsonl[1188] _id=69e289d31724f0c9e2f7b094 ts=2026-04-17T19:28:18.9080000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:28' vs expected 'questActiveEvent:32' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[473] _id=69dfe2967957a33870f4677d ts=2026-04-15T19:10:13.5880000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 58 records, TopographicMapEvent: 36 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 7 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1485 | 0.0 | 2.497 | 466.71 | 34.903 | 341259.373 | 0.13 | 374 | 4 |
| PlayerPositionEvent | 438 | 26.826 | 30.002 | 1581.367 | 40.903 | 341046.892 | 0.04 | 0 | 3 |
| questEvent | 71 | 0.001 | 121.976 | 9760.804 | 1130.847 | 341480.423 | 0.01 | 15 | 8 |
| Topographic Map Event | 57 | 2.084 | 16.724 | 3077.133 | 672.397 | 170110.384 | 0.02 | 0 | 4 |
| TopographicMapEvent | 35 | 0.871 | 4.67 | 4957.424 | 826.34 | 170058.08 | 0.01 | 0 | 2 |
| WaterChamberEvent | 32 | 0.893 | 6.197 | 11.512 | 35.007 | 47.759 | 5.21 | 0 | 0 |
| argumentationNodeEvent | 16 | 1.2 | 5.573 | 10858.683 | 43483.967 | 173493.883 | 0.01 | 0 | 1 |
| soilMachine | 12 | 1.264 | 15.732 | 30.608 | 88.779 | 118.458 | 1.96 | 0 | 0 |
| TerasGardenBox | 9 | 0.702 | 1.531 | 5.762 | 20.65 | 22.462 | 10.41 | 0 | 0 |
| argumentationEvent | 9 | 0.046 | 89.01 | 57911.814 | 276734.701 | 345575.654 | 0.0 | 1 | 3 |
| Soil Key Puzzle | 8 | 3.001 | 820.892 | 64572.798 | 282530.049 | 343453.515 | 0.0 | 0 | 4 |
| EndOfUnit | 3 | 1409.117 | 175619.926 | 173749.413 | 327359.269 | 344219.196 | 0.0 | 0 | 3 |
| argumentationToolEvent | 1 | 0.002 | 0.002 | 0.002 | 0.002 | 0.002 | 30000.0 | 1 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.002s (p5 29.96s, p95 40.90s, n=438) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `46ms: 69cdc937d385e3b94310f75c.jsonl[1186] _id=69e289d31724f0c9e2f7b092 ts=2026-04-17T19:28:18.8910000Z ~ 69cdc937d385e3b94310f75c.jsonl[1179] _id=69e289d41724f0c9e2f7b09e ts=2026-04-17T19:28:18.9370000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc937d385e3b94310f75c.jsonl[237] _id=69e7cfb51724f0c9e2f9d72b ts=2026-04-21T19:27:48.4250000Z ~ 69cdc937d385e3b94310f75c.jsonl[238] _id=69e7cfb51724f0c9e2f9d72d ts=2026-04-21T19:27:48.4270000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc937d385e3b94310f75c.jsonl[473] _id=69dfe2967957a33870f4677d ts=2026-04-15T19:10:13.5880000Z ~ 69cdc937d385e3b94310f75c.jsonl[474] _id=69dfe2967957a33870f4677f ts=2026-04-15T19:10:13.5890000Z`; `11ms: 69cdc937d385e3b94310f75c.jsonl[2116] _id=69e7d7581724f0c9e2f9f951 ts=2026-04-21T20:00:24.0260000Z ~ 69cdc937d385e3b94310f75c.jsonl[2117] _id=69e7d7591724f0c9e2f9f953 ts=2026-04-21T20:00:24.0370000Z`; `15ms: 69cdc937d385e3b94310f75c.jsonl[2158] _id=69e7d84e1724f0c9e2f9fccb ts=2026-04-21T20:04:29.5940000Z ~ 69cdc937d385e3b94310f75c.jsonl[2136] _id=69e7d84e1724f0c9e2f9fccd ts=2026-04-21T20:04:29.6090000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 47m 
  - Evidence: 94h 47m: 69cdc937d385e3b94310f75c.jsonl[1475] _id=69e292c51724f0c9e2f7d846 ts=2026-04-17T20:06:28.0240000Z -> 69cdc937d385e3b94310f75c.jsonl[1485] _id=69e7c7d01724f0c9e2f9ad95 ts=2026-04-21T18:54:07.3970000Z; 47h 0m: 69cdc937d385e3b94310f75c.jsonl[469] _id=69dd4da97957a33870f2bcb5 ts=2026-04-13T20:10:16.6350000Z -> 69cdc937d385e3b94310f75c.jsonl[475] _id=69dfe2c47957a33870f467f5 ts=2026-04-15T19:11:00.2490000Z; 46h 47m: 69cdc937d385e3b94310f75c.jsonl[106] _id=69dff0a87957a33870f49f75 ts=2026-04-15T20:10:16.0880000Z -> 69cdc937d385e3b94310f75c.jsonl[962] _id=69e282b01724f0c9e2f79442 ts=2026-04-17T18:57:50.6280000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 374 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75c.jsonl[1469] _id=69e2929a1724f0c9e2f7d7ac ts=2026-04-17T20:05:46.0160000Z -> 69cdc937d385e3b94310f75c.jsonl[1471] _id=69e292a91724f0c9e2f7d7f4 ts=2026-04-17T20:05:46.016Z; 2ms: 69cdc937d385e3b94310f75c.jsonl[1234] _id=69e28ae91724f0c9e2f7b3ec ts=2026-04-17T19:32:56.1780000Z -> 69cdc937d385e3b94310f75c.jsonl[1240] _id=69e28ae91724f0c9e2f7b3ee ts=2026-04-17T19:32:56.1800000Z; 2ms: 69cdc937d385e3b94310f75c.jsonl[1359] _id=69e28ea11724f0c9e2f7c890 ts=2026-04-17T19:48:48.1120000Z -> 69cdc937d385e3b94310f75c.jsonl[1357] _id=69e28ea11724f0c9e2f7c892 ts=2026-04-17T19:48:48.1140000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 69cdc937d385e3b94310f75c.jsonl[1421] _id=69e2929a1724f0c9e2f7d7aa ts=2026-04-17T20:05:46.0000000Z -> 69cdc937d385e3b94310f75c.jsonl[1952] _id=69e7d3351724f0c9e2f9e9bf ts=2026-04-21T19:42:45.1960000Z; 48h 46m: 69cdc937d385e3b94310f75c.jsonl[568] _id=69dfe4967957a33870f46e27 ts=2026-04-15T19:18:46.0740000Z -> 69cdc937d385e3b94310f75c.jsonl[1421] _id=69e2929a1724f0c9e2f7d7aa ts=2026-04-17T20:05:46.0000000Z; 23m 29s: 69cdc937d385e3b94310f75c.jsonl[1952] _id=69e7d3351724f0c9e2f9e9bf ts=2026-04-21T19:42:45.1960000Z -> 69cdc937d385e3b94310f75c.jsonl[291] _id=69e7d8b71724f0c9e2f9fed3 ts=2026-04-21T20:06:14.3130000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f75c.jsonl[1482] _id=69e293881724f0c9e2f7dc6a ts=2026-04-17T20:09:43.3830000Z -> 69cdc937d385e3b94310f75c.jsonl[1487] _id=69e7c7bf1724f0c9e2f9ad59 ts=2026-04-21T18:53:50.2750000Z; 46h 59m: 69cdc937d385e3b94310f75c.jsonl[470] _id=69dd4daa7957a33870f2bcb7 ts=2026-04-13T20:10:18.5960000Z -> 69cdc937d385e3b94310f75c.jsonl[472] _id=69dfe2957957a33870f46777 ts=2026-04-15T19:10:12.8580000Z; 46h 47m: 69cdc937d385e3b94310f75c.jsonl[101] _id=69dff0907957a33870f49f61 ts=2026-04-15T20:09:51.9470000Z -> 69cdc937d385e3b94310f75c.jsonl[961] _id=69e282ae1724f0c9e2f7943e ts=2026-04-17T18:57:48.2920000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 69cdc937d385e3b94310f75c.jsonl[1253] _id=69e28b431724f0c9e2f7b526 ts=2026-04-17T19:34:26.2400000Z -> 69cdc937d385e3b94310f75c.jsonl[1511] _id=69e7c8e01724f0c9e2f9b3b5 ts=2026-04-21T18:58:39.7550000Z; 47h 3m: 69cdc937d385e3b94310f75c.jsonl[866] _id=69dfed7b7957a33870f491b7 ts=2026-04-15T19:56:43.3940000Z -> 69cdc937d385e3b94310f75c.jsonl[977] _id=69e283271724f0c9e2f7961a ts=2026-04-17T18:59:49.8640000Z; 34m 13s: 69cdc937d385e3b94310f75c.jsonl[977] _id=69e283271724f0c9e2f7961a ts=2026-04-17T18:59:49.8640000Z -> 69cdc937d385e3b94310f75c.jsonl[1251] _id=69e28b2c1724f0c9e2f7b4bc ts=2026-04-17T19:34:03.4370000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 15m 
  - Evidence: 47h 15m: 69cdc937d385e3b94310f75c.jsonl[85] _id=69dfec9e7957a33870f48ddf ts=2026-04-15T19:53:01.9910000Z -> 69cdc937d385e3b94310f75c.jsonl[1022] _id=69e2851d1724f0c9e2f79dc0 ts=2026-04-17T19:08:12.3750000Z; 27m 55s: 69cdc937d385e3b94310f75c.jsonl[1075] _id=69e2889c1724f0c9e2f7ac3c ts=2026-04-17T19:23:07.8920000Z -> 69cdc937d385e3b94310f75c.jsonl[1384] _id=69e28f281724f0c9e2f7cb6c ts=2026-04-17T19:51:03.5900000Z; 14m 57s: 69cdc937d385e3b94310f75c.jsonl[575] _id=69dfe4e87957a33870f46f85 ts=2026-04-15T19:20:08.3920000Z -> 69cdc937d385e3b94310f75c.jsonl[695] _id=69dfe86a7957a33870f47e07 ts=2026-04-15T19:35:06.2490000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 14m 
  - Evidence: 47h 14m: 69cdc937d385e3b94310f75c.jsonl[844] _id=69dfec9b7957a33870f48dcf ts=2026-04-15T19:52:59.2550000Z -> 69cdc937d385e3b94310f75c.jsonl[1010] _id=69e284e61724f0c9e2f79cd2 ts=2026-04-17T19:07:17.3350000Z; 38m 34s: 69cdc937d385e3b94310f75c.jsonl[1059] _id=69e2862b1724f0c9e2f7a1c4 ts=2026-04-17T19:12:42.9200000Z -> 69cdc937d385e3b94310f75c.jsonl[1385] _id=69e28f351724f0c9e2f7cba0 ts=2026-04-17T19:51:17.0520000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 59m 
  - Evidence: 95h 59m: 69cdc937d385e3b94310f75c.jsonl[1179] _id=69e289d41724f0c9e2f7b09e ts=2026-04-17T19:28:18.9370000Z -> 69cdc937d385e3b94310f75c.jsonl[1780] _id=69e7cfbb1724f0c9e2f9d743 ts=2026-04-21T19:27:54.5910000Z; 48h 11m: 69cdc937d385e3b94310f75c.jsonl[512] _id=69dfe3e27957a33870f46bb3 ts=2026-04-15T19:15:46.4690000Z -> 69cdc937d385e3b94310f75c.jsonl[1152] _id=69e289841724f0c9e2f7af76 ts=2026-04-17T19:26:59.7410000Z; 28m 57s: 69cdc937d385e3b94310f75c.jsonl[1780] _id=69e7cfbb1724f0c9e2f9d743 ts=2026-04-21T19:27:54.5910000Z -> 69cdc937d385e3b94310f75c.jsonl[2096] _id=69e7d6841724f0c9e2f9f5e7 ts=2026-04-21T19:56:52.0770000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.046s..0.046s shown 
  - Evidence: 46ms: 69cdc937d385e3b94310f75c.jsonl[1186] _id=69e289d31724f0c9e2f7b092 ts=2026-04-17T19:28:18.8910000Z -> 69cdc937d385e3b94310f75c.jsonl[1179] _id=69e289d41724f0c9e2f7b09e ts=2026-04-17T19:28:18.9370000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 11m 
  - Evidence: 48h 11m: 69cdc937d385e3b94310f75c.jsonl[518] _id=69dfe3dc7957a33870f46b9b ts=2026-04-15T19:15:40.5580000Z -> 69cdc937d385e3b94310f75c.jsonl[1176] _id=69e289931724f0c9e2f7afac ts=2026-04-17T19:27:14.4410000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f75c.jsonl[237] _id=69e7cfb51724f0c9e2f9d72b ts=2026-04-21T19:27:48.4250000Z -> 69cdc937d385e3b94310f75c.jsonl[238] _id=69e7cfb51724f0c9e2f9d72d ts=2026-04-21T19:27:48.4270000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc937d385e3b94310f75c.jsonl[1470] _id=69e292941724f0c9e2f7d784 ts=2026-04-17T20:05:39.5180000Z -> 69cdc937d385e3b94310f75c.jsonl[1497] _id=69e7c87c1724f0c9e2f9b073 ts=2026-04-21T18:56:59.9410000Z; 47h 1m: 69cdc937d385e3b94310f75c.jsonl[37] _id=69dd4d507957a33870f2bbe9 ts=2026-04-13T20:08:47.8220000Z -> 69cdc937d385e3b94310f75c.jsonl[473] _id=69dfe2967957a33870f4677d ts=2026-04-15T19:10:13.5880000Z; 46h 50m: 69cdc937d385e3b94310f75c.jsonl[932] _id=69dff0017957a33870f49d0b ts=2026-04-15T20:07:29.3330000Z -> 69cdc937d385e3b94310f75c.jsonl[964] _id=69e282b11724f0c9e2f79448 ts=2026-04-17T18:57:51.2920000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 69cdc937d385e3b94310f75c.jsonl[473] _id=69dfe2967957a33870f4677d ts=2026-04-15T19:10:13.5880000Z -> 69cdc937d385e3b94310f75c.jsonl[474] _id=69dfe2967957a33870f4677f ts=2026-04-15T19:10:13.5890000Z; 2ms: 69cdc937d385e3b94310f75c.jsonl[477] _id=69dfe2c47957a33870f467f9 ts=2026-04-15T19:11:00.2710000Z -> 69cdc937d385e3b94310f75c.jsonl[479] _id=69dfe2c47957a33870f467fd ts=2026-04-15T19:11:00.2730000Z; 3ms: 69cdc937d385e3b94310f75c.jsonl[465] _id=69dd4d507957a33870f2bbe5 ts=2026-04-13T20:08:47.8190000Z -> 69cdc937d385e3b94310f75c.jsonl[37] _id=69dd4d507957a33870f2bbe9 ts=2026-04-13T20:08:47.8220000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc937d385e3b94310f75c.jsonl:69cdc937d385e3b94310f75c, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[64] _id=69dfe7117957a33870f47925 ts=2026-04-15T19:29:21.6100000Z`; `69cdc937d385e3b94310f75c.jsonl[866] _id=69dfed7b7957a33870f491b7 ts=2026-04-15T19:56:43.3940000Z`; `69cdc937d385e3b94310f75c.jsonl[1253] _id=69e28b431724f0c9e2f7b526 ts=2026-04-17T19:34:26.2400000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 36 record(s) match the trigger in 69cdc937d385e3b94310f75c.jsonl:69cdc937d385e3b94310f75c, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[726] _id=69dfe9717957a33870f48221 ts=2026-04-15T19:39:29.2600000Z`; `69cdc937d385e3b94310f75c.jsonl[729] _id=69dfe9797957a33870f48239 ts=2026-04-15T19:39:37.3560000Z`; `69cdc937d385e3b94310f75c.jsonl[758] _id=69dfea367957a33870f484ed ts=2026-04-15T19:42:46.0710000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[34] _id=69dd4d297957a33870f2bb5d ts=2026-04-13T20:08:08.6230000Z`; `69cdc937d385e3b94310f75c.jsonl[1047] _id=69e2866b1724f0c9e2f7a2a2 ts=2026-04-17T19:13:46.9870000Z`; `69cdc937d385e3b94310f75c.jsonl[120] _id=69e286fb1724f0c9e2f7a4e2 ts=2026-04-17T19:16:10.0530000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[1179] _id=69e289d41724f0c9e2f7b09e ts=2026-04-17T19:28:18.9370000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[237] _id=69e7cfb51724f0c9e2f9d72b ts=2026-04-21T19:27:48.4250000Z`; `69cdc937d385e3b94310f75c.jsonl[238] _id=69e7cfb51724f0c9e2f9d72d ts=2026-04-21T19:27:48.4270000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc937d385e3b94310f75c.jsonl[384] _id=69dd4a8d7957a33870f2b189 ts=2026-04-13T19:57:01.1680000Z`; `69cdc937d385e3b94310f75c.jsonl[1405] _id=69e28fce1724f0c9e2f7ceec ts=2026-04-17T19:53:49.9560000Z`; `69cdc937d385e3b94310f75c.jsonl[1410] _id=69e291151724f0c9e2f7d114 ts=2026-04-17T19:59:16.3060000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 163 unmatched 'DialogueStartEvent' (totals: 298 start, 139 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 41 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.77s, min -15.61s, max -0.20s over 2200 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75c\coverage.yaml

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
  - Observed: 58 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1486 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (324); Unit 2 Prod (Refactor) (298); Unit 4 Dev (226); Unit 1 Dev (196); Unit 5 Dev (145); Unit 3 Dungeon Dev (91); Unit 4 Dev - Anderson Base (90); Unit 4 Dev - Dungeon (90); Unit 5 Dev - Dungeon (26)
- **eventKey:** present on 1049 of 1486 records
- **Intervals:** median 2.50s (p5 0.01s / p95 34.90s, n=1485)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1049; [conversationId, dialogueEventType] x437
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1486/1486 records)
    numeric range 10 .. 114 (45 unique)
data.dialogueEventType  (string, 1486/1486 records)
    "DialogueNodeEvent"  x1049
    "DialogueStartEvent"  x298
    "DialogueFinishEvent"  x139
data.nodeId  (number, 1049/1486 records)
    numeric range 0 .. 289 (206 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 450 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (103); Unit 1 Dev (87); Unit 3 Dev (81); Unit 4 Dev (62); Unit 3 Dungeon Dev (29); Unit 4 Dev - Dungeon (27); Unit 5 Dev (26); Unit 5 Dev - Dungeon (20); Unit 4 Dev - Anderson Base (15)
- **Intervals:** median 30.00s (p5 29.96s / p95 40.90s, n=438)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 450/450 records)
data.position.x  (number, 450/450 records)
    numeric range -692.336 .. 1559.04 (260 unique)
data.position.y  (number, 450/450 records)
    numeric range -114.326 .. 217.861 (234 unique)
data.position.z  (number, 450/450 records)
    numeric range -1111.1 .. 2017.51 (260 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 72 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (14); Unit 3 Dev (12); Unit 2 Prod (Refactor) (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 72 of 72 records
- **Intervals:** median 121.98s (p5 0.01s / p95 1130.85s, n=71)
- **`data` key-set variants:** [questEventType, questID, questName] x41; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 72/72 records)
    "questActiveEvent"  x41
    "questFinishEvent"  x31
data.questID  (string, 72/72 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 72/72 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/72 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 58 records

- **Scenes:** Unit 3 Dev (32); Unit 2 Prod (Refactor) (26)
- **Intervals:** median 16.72s (p5 2.52s / p95 672.40s, n=57)
- **Fields under `data`:**

```text
data.actionType  (string, 58/58 records)
    "MapCloseEvent"  x29
    "MapOpenEvent"  x29
data.featureUsed  (string, 58/58 records)
    "Map"  x58
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 36 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 3 Dev (10)
- **Intervals:** median 4.67s (p5 1.64s / p95 826.34s, n=35)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "dragEnd"  x18
    "dragStart"  x18
data.featureUsed  (string, 36/36 records)
    "waypoint"  x36
data.location  (object, 36/36 records)
data.location.x  (number, 36/36 records)
    numeric range -772.607 .. 152.047 (19 unique)
data.location.y  (number, 36/36 records)
    numeric range -311.033 .. 238.286 (19 unique)
data.location.z  (number, 36/36 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 33 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (33)
- **Intervals:** median 6.20s (p5 1.01s / p95 35.01s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "On"  x22
    "Off"  x11
data.floor  (string, 33/33 records)
    "4"  x19
    "3"  x6
    "1"  x5
    "2"  x3
data.machineNumber  (string, 33/33 records)
    "One"  x32
    "Two"  x1
data.machineType  (string, 33/33 records)
    "Condenser"  x20
    "Evaporator"  x6
    "VentSwitch"  x6
    "DualChamber_Condenser"  x1
data.room  (string, 33/33 records)
    "3"  x17
    "2"  x10
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 17 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (10); Unit 3 Dev (7)
- **Intervals:** median 5.57s (p5 1.55s / p95 43483.97s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationNodeAdd"  x13
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 17/17 records)
    "Unit 1 - Freshwater"  x7
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 17/17 records)
    "I"  x5
    "A"  x4
    "5"  x3
    "1"  x2
    "II"  x2
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 13 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (13)
- **Intervals:** median 15.73s (p5 1.53s / p95 88.78s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "ChangeCanister"  x13
data.canisterType  (string, 13/13 records)
    "Bedrock"  x6
    "Clay"  x4
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 13/13 records)
    "5"  x11
    "3"  x1
    "4"  x1
data.machine  (string, 13/13 records)
    "1"  x12
    "2"  x1
data.row  (string, 13/13 records)
    "BottomRow"  x7
    "TopRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 1.53s (p5 0.84s / p95 20.65s, n=9)
- **`data` key-set variants:** [actionType, boxID, soilType] x7; [actionType, boxId, soilType] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "soilSelected"  x7
    "cameraPlaced"  x3
data.boxID  (string, 7/10 records)
    "1"  x4
    "2"  x3
data.boxId  (string, 3/10 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 10/10 records)
    "Gravel"  x4
    "Sand"  x4
    "Clay"  x1
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 89.01s (p5 20.84s / p95 276734.70s, n=9)
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

### `Soil Key Puzzle` — 9 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 820.89s (p5 9.38s / p95 282530.05s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/9 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/9 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 175619.93s (p5 18830.20s / p95 327359.27s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 0.00s (p5 0.00s / p95 0.00s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 4 - Flooding"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Soil Flow Rates"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (5 records)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "dragStart" (18x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*