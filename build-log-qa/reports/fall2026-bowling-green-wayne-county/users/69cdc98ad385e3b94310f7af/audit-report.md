# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7af

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7af
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7af.jsonl
- **Records:** 2525 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7af
- **Time span:** 2026-04-14T19:24:47.986000+00:00 .. 2026-04-22T19:14:19.013000+00:00 (191h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7af\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2525 records, 9 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 57 INFO, 0 NOT_TESTED, 58 PASS.
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
| DialogueEvent | 1757 | 69.58 | 1 | 9 | 1240 | 2026-04-14T19:25:06.314000+00:00 | 2026-04-22T19:14:13.331000+00:00 | 191h 49m |
| PlayerPositionEvent | 449 | 17.78 | 1 | 9 | 0 | 2026-04-14T19:24:47.986000+00:00 | 2026-04-22T19:14:18.730000+00:00 | 191h 49m |
| questEvent | 78 | 3.09 | 1 | 9 | 78 | 2026-04-14T19:25:06.299000+00:00 | 2026-04-22T19:10:45.749000+00:00 | 191h 45m |
| Topographic Map Event | 58 | 2.3 | 1 | 2 | 0 | 2026-04-16T18:58:30.232000+00:00 | 2026-04-20T19:18:32.749000+00:00 | 96h 20m |
| WaterChamberEvent | 47 | 1.86 | 1 | 1 | 0 | 2026-04-22T18:51:11.543000+00:00 | 2026-04-22T18:56:30.215000+00:00 | 5m 18s |
| TopographicMapEvent | 34 | 1.35 | 1 | 2 | 0 | 2026-04-16T18:59:11.245000+00:00 | 2026-04-20T19:18:31.384000+00:00 | 96h 19m |
| argumentationNodeEvent | 25 | 0.99 | 1 | 3 | 0 | 2026-04-14T19:48:36.442000+00:00 | 2026-04-20T18:57:14.950000+00:00 | 143h 8m |
| argumentationToolEvent | 20 | 0.79 | 1 | 3 | 0 | 2026-04-16T19:47:37.992000+00:00 | 2026-04-20T19:58:24.571000+00:00 | 96h 10m |
| soilMachine | 19 | 0.75 | 1 | 1 | 0 | 2026-04-20T19:39:46.820000+00:00 | 2026-04-20T19:45:26.036000+00:00 | 5m 39s |
| argumentationEvent | 12 | 0.48 | 1 | 5 | 0 | 2026-04-14T19:48:21.539000+00:00 | 2026-04-22T19:04:25.038000+00:00 | 191h 16m |
| TerasGardenBox | 11 | 0.44 | 1 | 1 | 0 | 2026-04-20T20:08:36.715000+00:00 | 2026-04-20T20:09:32.347000+00:00 | 55.6s |
| Soil Key Puzzle | 10 | 0.4 | 1 | 3 | 0 | 2026-04-14T20:04:40.133000+00:00 | 2026-04-20T19:29:51.736000+00:00 | 143h 25m |
| EndOfUnit | 5 | 0.2 | 1 | 5 | 0 | 2026-04-14T19:53:05.838000+00:00 | 2026-04-22T19:14:19.013000+00:00 | 191h 21m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 170999.796s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.012s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 146.182s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.778s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.048s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 140.665s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.244s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.125s median 
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
  - Observed: 3.223s median 
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
  - Observed: 2; 3; 4; C 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[762] _id=69de9a847957a33870f3a49b ts=2026-04-14T19:50:27.9110000Z`; `69cdc98ad385e3b94310f7af.jsonl[117] _id=69e133331724f0c9e2f69f9c ts=2026-04-16T19:06:25.9510000Z`; `69cdc98ad385e3b94310f7af.jsonl[176] _id=69e13d111724f0c9e2f6ff98 ts=2026-04-16T19:48:33.0110000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 58 records, TopographicMapEvent: 34 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 8 records, data.boxId: 3 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1756 | 0.0 | 2.542 | 393.25 | 29.383 | 340858.372 | 0.15 | 424 | 3 |
| PlayerPositionEvent | 437 | 29.787 | 30.012 | 1195.928 | 34.783 | 340849.783 | 0.05 | 0 | 2 |
| questEvent | 77 | 0.003 | 117.696 | 8965.447 | 1088.757 | 341260.902 | 0.01 | 14 | 7 |
| Topographic Map Event | 57 | 0.134 | 11.676 | 6084.255 | 604.054 | 341830.422 | 0.01 | 0 | 3 |
| WaterChamberEvent | 46 | 0.789 | 4.048 | 6.928 | 20.782 | 33.0 | 8.66 | 0 | 0 |
| TopographicMapEvent | 33 | 0.499 | 3.778 | 10507.883 | 1140.205 | 343338.765 | 0.01 | 0 | 2 |
| argumentationNodeEvent | 24 | 1.233 | 8.244 | 21471.605 | 146690.127 | 342453.489 | 0.0 | 0 | 2 |
| argumentationToolEvent | 19 | 0.003 | 1.125 | 18223.504 | 37509.65 | 342529.176 | 0.0 | 2 | 2 |
| soilMachine | 18 | 0.817 | 3.223 | 18.845 | 84.87 | 103.668 | 3.18 | 0 | 0 |
| argumentationEvent | 11 | 0.105 | 140.665 | 62596.682 | 257492.495 | 342440.548 | 0.0 | 0 | 4 |
| TerasGardenBox | 10 | 1.329 | 2.541 | 5.563 | 18.586 | 18.724 | 10.79 | 0 | 0 |
| Soil Key Puzzle | 9 | 3.02 | 146.182 | 57367.956 | 274165.971 | 344516.36 | 0.0 | 0 | 4 |
| EndOfUnit | 4 | 2982.663 | 170999.796 | 172218.294 | 318213.445 | 343890.919 | 0.0 | 0 | 4 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.012s (p5 29.95s, p95 34.78s, n=437) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `560ms: 69cdc98ad385e3b94310f7af.jsonl[1774] _id=69e677de1724f0c9e2f8c1cf ts=2026-04-20T19:00:45.2640000Z ~ 69cdc98ad385e3b94310f7af.jsonl[1775] _id=69e677de1724f0c9e2f8c1d9 ts=2026-04-20T19:00:45.8240000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `105ms: 69cdc98ad385e3b94310f7af.jsonl[222] _id=69e6770e1724f0c9e2f8be23 ts=2026-04-20T18:57:17.3240000Z ~ 69cdc98ad385e3b94310f7af.jsonl[229] _id=69e6770e1724f0c9e2f8be2b ts=2026-04-20T18:57:17.4290000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `950ms: 69cdc98ad385e3b94310f7af.jsonl[1746] _id=69e676e61724f0c9e2f8bd65 ts=2026-04-20T18:56:37.4270000Z ~ 69cdc98ad385e3b94310f7af.jsonl[1747] _id=69e676e71724f0c9e2f8bd6b ts=2026-04-20T18:56:38.3770000Z`; `3ms: 69cdc98ad385e3b94310f7af.jsonl[431] _id=69e685091724f0c9e2f8fa49 ts=2026-04-20T19:56:56.9690000Z ~ 69cdc98ad385e3b94310f7af.jsonl[2158] _id=69e685091724f0c9e2f8fa4b ts=2026-04-20T19:56:56.9720000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `13ms: 69cdc98ad385e3b94310f7af.jsonl[2471] _id=69e91bcf1724f0c9e2fa9101 ts=2026-04-22T19:04:47.1160000Z ~ 69cdc98ad385e3b94310f7af.jsonl[2464] _id=69e91bd01724f0c9e2fa9103 ts=2026-04-22T19:04:47.1290000Z`; `13ms: 69cdc98ad385e3b94310f7af.jsonl[2514] _id=69e91cfd1724f0c9e2fa9659 ts=2026-04-22T19:09:49.1560000Z ~ 69cdc98ad385e3b94310f7af.jsonl[2507] _id=69e91cfe1724f0c9e2fa965d ts=2026-04-22T19:09:49.1690000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `817ms: 69cdc98ad385e3b94310f7af.jsonl[383] _id=69e681f21724f0c9e2f8f041 ts=2026-04-20T19:43:45.6450000Z ~ 69cdc98ad385e3b94310f7af.jsonl[384] _id=69e681f31724f0c9e2f8f043 ts=2026-04-20T19:43:46.4620000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc98ad385e3b94310f7af.jsonl[1653] _id=69e141a91724f0c9e2f712a8 ts=2026-04-16T20:08:08.4620000Z -> 69cdc98ad385e3b94310f7af.jsonl[1678] _id=69e675281724f0c9e2f8b729 ts=2026-04-20T18:49:06.8340000Z; 46h 43m: 69cdc98ad385e3b94310f7af.jsonl[53] _id=69de9e857957a33870f3b5f5 ts=2026-04-14T20:07:33.6560000Z -> 69cdc98ad385e3b94310f7af.jsonl[939] _id=69e12f9b1724f0c9e2f68f70 ts=2026-04-16T18:51:06.6670000Z; 46h 34m: 69cdc98ad385e3b94310f7af.jsonl[2309] _id=69e688bf1724f0c9e2f904f3 ts=2026-04-20T20:12:47.2140000Z -> 69cdc98ad385e3b94310f7af.jsonl[2321] _id=69e917d31724f0c9e2fa823d ts=2026-04-22T18:47:46.9690000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 424 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7af.jsonl[1522] _id=69e13dc61724f0c9e2f702ac ts=2026-04-16T19:51:33.6150000Z -> 69cdc98ad385e3b94310f7af.jsonl[1528] _id=69e13dd51724f0c9e2f702da ts=2026-04-16T19:51:33.615Z; 3ms: 69cdc98ad385e3b94310f7af.jsonl[1230] _id=69e138561724f0c9e2f6d5e4 ts=2026-04-16T19:28:21.3390000Z -> 69cdc98ad385e3b94310f7af.jsonl[1228] _id=69e138561724f0c9e2f6d5f2 ts=2026-04-16T19:28:21.3420000Z; 3ms: 69cdc98ad385e3b94310f7af.jsonl[1241] _id=69e1387f1724f0c9e2f6d8fa ts=2026-04-16T19:29:02.7570000Z -> 69cdc98ad385e3b94310f7af.jsonl[1242] _id=69e1387f1724f0c9e2f6d8fc ts=2026-04-16T19:29:02.7600000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 69cdc98ad385e3b94310f7af.jsonl[1520] _id=69e13dc61724f0c9e2f702aa ts=2026-04-16T19:51:33.6000000Z -> 69cdc98ad385e3b94310f7af.jsonl[1666] _id=69e67d191724f0c9e2f8da3b ts=2026-04-20T19:23:04.5190000Z; 47h 58m: 69cdc98ad385e3b94310f7af.jsonl[809] _id=69de9b227957a33870f3a7b7 ts=2026-04-14T19:53:05.8380000Z -> 69cdc98ad385e3b94310f7af.jsonl[1520] _id=69e13dc61724f0c9e2f702aa ts=2026-04-16T19:51:33.6000000Z; 47h 1m: 69cdc98ad385e3b94310f7af.jsonl[2308] _id=69e688bf1724f0c9e2f904f1 ts=2026-04-20T20:12:47.1820000Z -> 69cdc98ad385e3b94310f7af.jsonl[934] _id=69e91e0b1724f0c9e2fa9abb ts=2026-04-22T19:14:19.0130000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc98ad385e3b94310f7af.jsonl[1661] _id=69e141ba1724f0c9e2f712de ts=2026-04-16T20:08:25.4600000Z -> 69cdc98ad385e3b94310f7af.jsonl[1673] _id=69e6752c1724f0c9e2f8b733 ts=2026-04-20T18:49:15.2430000Z; 46h 41m: 69cdc98ad385e3b94310f7af.jsonl[922] _id=69de9ef87957a33870f3b74b ts=2026-04-14T20:09:27.9680000Z -> 69cdc98ad385e3b94310f7af.jsonl[945] _id=69e12f971724f0c9e2f68f62 ts=2026-04-16T18:51:01.6480000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 41m 
  - Evidence: 95h 41m: 69cdc98ad385e3b94310f7af.jsonl[1162] _id=69e136b41724f0c9e2f6b642 ts=2026-04-16T19:21:23.9910000Z -> 69cdc98ad385e3b94310f7af.jsonl[1780] _id=69e678791724f0c9e2f8c46f ts=2026-04-20T19:03:20.3510000Z; 46h 50m: 69cdc98ad385e3b94310f7af.jsonl[888] _id=69de9ddb7957a33870f3b36b ts=2026-04-14T20:04:43.1530000Z -> 69cdc98ad385e3b94310f7af.jsonl[987] _id=69e1309c1724f0c9e2f692fa ts=2026-04-16T18:55:23.5400000Z; 24m 42s: 69cdc98ad385e3b94310f7af.jsonl[1791] _id=69e678bf1724f0c9e2f8c587 ts=2026-04-20T19:04:30.3700000Z -> 69cdc98ad385e3b94310f7af.jsonl[1965] _id=69e67e8a1724f0c9e2f8e0f7 ts=2026-04-20T19:29:13.3140000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 57m 
  - Evidence: 94h 57m: 69cdc98ad385e3b94310f7af.jsonl[1615] _id=69e140721724f0c9e2f70ce4 ts=2026-04-16T20:02:57.6210000Z -> 69cdc98ad385e3b94310f7af.jsonl[1767] _id=69e677b81724f0c9e2f8c131 ts=2026-04-20T19:00:08.0430000Z; 20m 50s: 69cdc98ad385e3b94310f7af.jsonl[1321] _id=69e139de1724f0c9e2f6eaf6 ts=2026-04-16T19:34:53.9190000Z -> 69cdc98ad385e3b94310f7af.jsonl[1558] _id=69e13ec11724f0c9e2f705f0 ts=2026-04-16T19:55:44.4000000Z; 15m 46s: 69cdc98ad385e3b94310f7af.jsonl[1773] _id=69e677e61724f0c9e2f8c203 ts=2026-04-20T19:00:53.5790000Z -> 69cdc98ad385e3b94310f7af.jsonl[1878] _id=69e67b981724f0c9e2f8d2a7 ts=2026-04-20T19:16:40.2630000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 69cdc98ad385e3b94310f7af.jsonl[1548] _id=69e13e711724f0c9e2f704f8 ts=2026-04-16T19:54:25.0520000Z -> 69cdc98ad385e3b94310f7af.jsonl[1886] _id=69e67b9c1724f0c9e2f8d2b5 ts=2026-04-20T19:16:43.8170000Z; 36m 8s: 69cdc98ad385e3b94310f7af.jsonl[1125] _id=69e135f51724f0c9e2f6b19c ts=2026-04-16T19:18:12.4450000Z -> 69cdc98ad385e3b94310f7af.jsonl[1544] _id=69e13e6d1724f0c9e2f704ec ts=2026-04-16T19:54:21.2960000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 7m 
  - Evidence: 95h 7m: 69cdc98ad385e3b94310f7af.jsonl[1481] _id=69e13d111724f0c9e2f6ff94 ts=2026-04-16T19:48:32.9830000Z -> 69cdc98ad385e3b94310f7af.jsonl[218] _id=69e676ba1724f0c9e2f8bc83 ts=2026-04-20T18:55:53.5310000Z; 47h 55m: 69cdc98ad385e3b94310f7af.jsonl[761] _id=69de9a847957a33870f3a497 ts=2026-04-14T19:50:27.8770000Z -> 69cdc98ad385e3b94310f7af.jsonl[1440] _id=69e13c841724f0c9e2f6fca4 ts=2026-04-16T19:46:12.3180000Z; 47h 4m: 69cdc98ad385e3b94310f7af.jsonl[2156] _id=69e6850d1724f0c9e2f8fa5c ts=2026-04-20T19:57:00.7370000Z -> 69cdc98ad385e3b94310f7af.jsonl[2440] _id=69e91b151724f0c9e2fa8e2f ts=2026-04-22T19:01:40.9250000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 7m 
  - Evidence: 95h 7m: 69cdc98ad385e3b94310f7af.jsonl[1480] _id=69e13d101724f0c9e2f6ff8e ts=2026-04-16T19:48:31.6980000Z -> 69cdc98ad385e3b94310f7af.jsonl[1740] _id=69e676c51724f0c9e2f8bcd3 ts=2026-04-20T18:56:05.1870000Z; 47h 56m: 69cdc98ad385e3b94310f7af.jsonl[764] _id=69de9a7c7957a33870f3a46f ts=2026-04-14T19:50:19.6670000Z -> 69cdc98ad385e3b94310f7af.jsonl[1446] _id=69e13c8f1724f0c9e2f6fcde ts=2026-04-16T19:46:23.1200000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 8m 
  - Evidence: 95h 8m: 69cdc98ad385e3b94310f7af.jsonl[1470] _id=69e13cdf1724f0c9e2f6fe74 ts=2026-04-16T19:47:43.2910000Z -> 69cdc98ad385e3b94310f7af.jsonl[1743] _id=69e676e11724f0c9e2f8bd55 ts=2026-04-20T18:56:32.4670000Z; 1h 0m: 69cdc98ad385e3b94310f7af.jsonl[1747] _id=69e676e71724f0c9e2f8bd6b ts=2026-04-20T18:56:38.3770000Z -> 69cdc98ad385e3b94310f7af.jsonl[431] _id=69e685091724f0c9e2f8fa49 ts=2026-04-20T19:56:56.9690000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.010s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7af.jsonl[431] _id=69e685091724f0c9e2f8fa49 ts=2026-04-20T19:56:56.9690000Z -> 69cdc98ad385e3b94310f7af.jsonl[2158] _id=69e685091724f0c9e2f8fa4b ts=2026-04-20T19:56:56.9720000Z; 10ms: 69cdc98ad385e3b94310f7af.jsonl[2165] _id=69e685601724f0c9e2f8fbb3 ts=2026-04-20T19:58:23.4360000Z -> 69cdc98ad385e3b94310f7af.jsonl[2162] _id=69e685601724f0c9e2f8fbb5 ts=2026-04-20T19:58:23.4460000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 47m 
  - Evidence: 94h 47m: 69cdc98ad385e3b94310f7af.jsonl[1604] _id=69e140161724f0c9e2f70b62 ts=2026-04-16T20:01:25.8340000Z -> 69cdc98ad385e3b94310f7af.jsonl[1677] _id=69e675241724f0c9e2f8b725 ts=2026-04-20T18:49:06.7360000Z; 46h 43m: 69cdc98ad385e3b94310f7af.jsonl[915] _id=69de9e837957a33870f3b5e5 ts=2026-04-14T20:07:31.4710000Z -> 69cdc98ad385e3b94310f7af.jsonl[938] _id=69e12f9a1724f0c9e2f68f6a ts=2026-04-16T18:51:04.9830000Z; 46h 34m: 69cdc98ad385e3b94310f7af.jsonl[2307] _id=69e688be1724f0c9e2f904eb ts=2026-04-20T20:12:45.6840000Z -> 69cdc98ad385e3b94310f7af.jsonl[2314] _id=69e917c71724f0c9e2fa8237 ts=2026-04-22T18:47:33.8240000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.003s..0.008s shown 
  - Evidence: 3ms: 69cdc98ad385e3b94310f7af.jsonl[734] _id=69de99c27957a33870f3a0e7 ts=2026-04-14T19:47:14.1140000Z -> 69cdc98ad385e3b94310f7af.jsonl[14] _id=69de99c27957a33870f3a0e9 ts=2026-04-14T19:47:14.1170000Z; 7ms: 69cdc98ad385e3b94310f7af.jsonl[2342] _id=69e918c91724f0c9e2fa849d ts=2026-04-22T18:51:52.4260000Z -> 69cdc98ad385e3b94310f7af.jsonl[2340] _id=69e918c91724f0c9e2fa849f ts=2026-04-22T18:51:52.4330000Z; 8ms: 69cdc98ad385e3b94310f7af.jsonl[519] _id=69e919621724f0c9e2fa86e5 ts=2026-04-22T18:54:25.2880000Z -> 69cdc98ad385e3b94310f7af.jsonl[2371] _id=69e919621724f0c9e2fa86e7 ts=2026-04-22T18:54:25.2960000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc98ad385e3b94310f7af.jsonl:69cdc98ad385e3b94310f7af, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[888] _id=69de9ddb7957a33870f3b36b ts=2026-04-14T20:04:43.1530000Z`; `69cdc98ad385e3b94310f7af.jsonl[60] _id=69e1309f1724f0c9e2f6930a ts=2026-04-16T18:55:26.5840000Z`; `69cdc98ad385e3b94310f7af.jsonl[1162] _id=69e136b41724f0c9e2f6b642 ts=2026-04-16T19:21:23.9910000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 34 record(s) match the trigger in 69cdc98ad385e3b94310f7af.jsonl:69cdc98ad385e3b94310f7af, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[1019] _id=69e131801724f0c9e2f69622 ts=2026-04-16T18:59:11.2450000Z`; `69cdc98ad385e3b94310f7af.jsonl[1020] _id=69e131801724f0c9e2f69624 ts=2026-04-16T18:59:11.7440000Z`; `69cdc98ad385e3b94310f7af.jsonl[1021] _id=69e131891724f0c9e2f69640 ts=2026-04-16T18:59:20.5520000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[154] _id=69e139501724f0c9e2f6dd34 ts=2026-04-16T19:32:32.0330000Z`; `69cdc98ad385e3b94310f7af.jsonl[1585] _id=69e13f981724f0c9e2f70924 ts=2026-04-16T19:59:19.6730000Z`; `69cdc98ad385e3b94310f7af.jsonl[1605] _id=69e140161724f0c9e2f70b66 ts=2026-04-16T20:01:25.8940000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[229] _id=69e6770e1724f0c9e2f8be2b ts=2026-04-20T18:57:17.4290000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[1744] _id=69e676e21724f0c9e2f8bd57 ts=2026-04-20T18:56:34.0010000Z`; `69cdc98ad385e3b94310f7af.jsonl[1742] _id=69e676e31724f0c9e2f8bd5d ts=2026-04-20T18:56:35.0360000Z`; `69cdc98ad385e3b94310f7af.jsonl[431] _id=69e685091724f0c9e2f8fa49 ts=2026-04-20T19:56:56.9690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7af.jsonl[220] _id=69e676e21724f0c9e2f8bd5b ts=2026-04-20T18:56:34.0770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 175 unmatched 'DialogueStartEvent' (totals: 344 start, 173 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 9 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 44 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.71s, min -16.19s, max -0.33s over 2525 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7af\coverage.yaml

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
  - Observed: 58 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1757 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (607); Unit 3 Dev (311); Unit 4 Dev (217); Unit 1 Dev (172); Unit 5 Dev (172); Unit 4 Dev - Dungeon (90); Unit 4 Dev - Anderson Base (88); Unit 3 Dungeon Dev (77); Unit 5 Dev - Dungeon (23)
- **eventKey:** present on 1240 of 1757 records
- **Intervals:** median 2.54s (p5 0.01s / p95 29.38s, n=1756)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1240; [conversationId, dialogueEventType] x517
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1757/1757 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 1757/1757 records)
    "DialogueNodeEvent"  x1240
    "DialogueStartEvent"  x344
    "DialogueFinishEvent"  x173
data.nodeId  (number, 1240/1757 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 449 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (144); Unit 3 Dev (79); Unit 1 Dev (57); Unit 4 Dev (46); Unit 5 Dev (35); Unit 4 Dev - Dungeon (27); Unit 3 Dungeon Dev (21); Unit 4 Dev - Anderson Base (21); Unit 5 Dev - Dungeon (19)
- **Intervals:** median 30.01s (p5 29.95s / p95 34.78s, n=437)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 449/449 records)
data.position.x  (number, 449/449 records)
    numeric range -699.376 .. 1557.21 (234 unique)
data.position.y  (number, 449/449 records)
    numeric range -113.845 .. 222.252 (210 unique)
data.position.z  (number, 449/449 records)
    numeric range -1105.01 .. 2023.4 (234 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 78 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (16); Unit 2 Prod (Refactor) (15); Unit 1 Dev (12); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 78 of 78 records
- **Intervals:** median 117.70s (p5 0.01s / p95 1088.76s, n=77)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Fields under `data`:**

```text
data.questEventType  (string, 78/78 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x34
data.questID  (string, 78/78 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 78/78 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/78 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 58 records

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (24)
- **Intervals:** median 11.68s (p5 0.57s / p95 604.05s, n=57)
- **Fields under `data`:**

```text
data.actionType  (string, 58/58 records)
    "MapCloseEvent"  x29
    "MapOpenEvent"  x29
data.featureUsed  (string, 58/58 records)
    "Map"  x58
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 47 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (47)
- **Intervals:** median 4.05s (p5 1.07s / p95 20.78s, n=46)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "On"  x29
    "Off"  x18
data.floor  (string, 47/47 records)
    "3"  x22
    "4"  x19
    "1"  x3
    "2"  x3
data.machineNumber  (string, 47/47 records)
    "One"  x46
    "Two"  x1
data.machineType  (string, 47/47 records)
    "Condenser"  x26
    "DualChamber_Condenser"  x9
    "Evaporator"  x8
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 47/47 records)
    "2"  x24
    "3"  x15
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 34 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (10)
- **Intervals:** median 3.78s (p5 0.76s / p95 1140.20s, n=33)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "dragEnd"  x17
    "dragStart"  x17
data.featureUsed  (string, 34/34 records)
    "waypoint"  x34
data.location  (object, 34/34 records)
data.location.x  (number, 34/34 records)
    numeric range -770.79 .. 134.614 (18 unique)
data.location.y  (number, 34/34 records)
    numeric range -307.4 .. 141.084 (18 unique)
data.location.z  (number, 34/34 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 25 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (5); Unit 3 Dev (3)
- **Intervals:** median 8.24s (p5 1.40s / p95 146690.13s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 25/25 records)
    "Unit 2 – Watershed"  x17
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 25/25 records)
    "I"  x6
    "1"  x5
    "D"  x4
    "A"  x3
    "B"  x3
    "II"  x3
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (8); Unit 2 Prod (Refactor) (6); Unit 4 Dev - Anderson Base (6)
- **Intervals:** median 1.12s (p5 0.01s / p95 37509.65s, n=19)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolClose"  x11
    "argumentationToolOpen"  x9
data.argumentationTitle  (string, 20/20 records)
    "Unit 3 - Pollution Upstream"  x8
    "Unit 2 – Watershed"  x6
    "Unit 4 - Flooding"  x6
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - Waterfall Data"  x4
    "BackingInfoPanel - "  x2
    "BackingInfoPanel - Soil Flow Rates"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 3.22s (p5 0.82s / p95 84.87s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Bedrock"  x9
    "Clay"  x5
    "Sand"  x3
    "Gravel"  x2
data.floor  (string, 19/19 records)
    "5"  x15
    "3"  x3
    "4"  x1
data.machine  (string, 19/19 records)
    "1"  x18
    "2"  x1
data.row  (string, 19/19 records)
    "TopRow"  x12
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 140.66s (p5 16.47s / p95 257492.49s, n=11)
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

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 2.54s (p5 1.41s / p95 18.59s, n=10)
- **`data` key-set variants:** [actionType, boxID, soilType] x8; [actionType, boxId, soilType] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "soilSelected"  x8
    "cameraPlaced"  x3
data.boxID  (string, 8/11 records)
    "0"  x3
    "1"  x3
    "2"  x2
data.boxId  (string, 3/11 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 11/11 records)
    "Sand"  x5
    "Clay"  x4
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 146.18s (p5 3.03s / p95 274165.97s, n=9)
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 170999.80s (p5 27929.04s / p95 318213.45s, n=4)
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
- `TopographicMapEvent` data.actionType: "dragStart" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)
- `soilMachine` data.canisterType: "Bedrock" (9x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*