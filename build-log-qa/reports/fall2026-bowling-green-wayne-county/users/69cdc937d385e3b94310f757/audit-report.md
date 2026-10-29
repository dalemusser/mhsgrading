# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f757

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f757
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f757.jsonl
- **Records:** 2141 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f757
- **Time span:** 2026-04-15T19:10:10.239000+00:00 .. 2026-04-21T20:05:53.278000+00:00 (144h 55m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f757\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2141 records, 9 scenes.
- Findings: **0 FAIL**, **45 WARNING**, 69 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1436 | 67.07 | 1 | 9 | 988 | 2026-04-15T19:10:28.303000+00:00 | 2026-04-21T20:05:46.820000+00:00 | 144h 55m |
| PlayerPositionEvent | 399 | 18.64 | 1 | 9 | 0 | 2026-04-15T19:10:10.239000+00:00 | 2026-04-21T20:05:43.235000+00:00 | 144h 55m |
| questEvent | 70 | 3.27 | 1 | 9 | 70 | 2026-04-15T19:10:28.289000+00:00 | 2026-04-21T20:04:44.230000+00:00 | 144h 54m |
| Topographic Map Event | 62 | 2.9 | 1 | 2 | 0 | 2026-04-15T19:51:34.478000+00:00 | 2026-04-17T19:48:12.479000+00:00 | 47h 56m |
| argumentationToolEvent | 50 | 2.34 | 1 | 2 | 0 | 2026-04-21T19:17:59.545000+00:00 | 2026-04-21T19:58:45.884000+00:00 | 40m 46s |
| WaterChamberEvent | 37 | 1.73 | 1 | 1 | 0 | 2026-04-21T19:46:15.773000+00:00 | 2026-04-21T19:51:21.301000+00:00 | 5m 5s |
| TopographicMapEvent | 26 | 1.21 | 1 | 2 | 0 | 2026-04-15T19:58:35.952000+00:00 | 2026-04-17T19:19:29.911000+00:00 | 47h 20m |
| soilMachine | 18 | 0.84 | 1 | 1 | 0 | 2026-04-21T18:57:08.213000+00:00 | 2026-04-21T19:05:59.708000+00:00 | 8m 51s |
| argumentationNodeEvent | 13 | 0.61 | 1 | 2 | 0 | 2026-04-15T19:31:41.158000+00:00 | 2026-04-17T19:21:55.072000+00:00 | 47h 50m |
| argumentationEvent | 11 | 0.51 | 1 | 4 | 0 | 2026-04-15T19:31:29.474000+00:00 | 2026-04-21T19:59:35.917000+00:00 | 144h 28m |
| Soil Key Puzzle | 8 | 0.37 | 1 | 3 | 0 | 2026-04-15T19:52:09.780000+00:00 | 2026-04-17T20:02:57.414000+00:00 | 48h 10m |
| TerasGardenBox | 7 | 0.33 | 1 | 1 | 0 | 2026-04-21T19:38:18.186000+00:00 | 2026-04-21T19:39:49.926000+00:00 | 1m 31s |
| EndOfUnit | 4 | 0.19 | 1 | 4 | 0 | 2026-04-15T19:37:32.164000+00:00 | 2026-04-21T20:05:53.278000+00:00 | 144h 28m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173761.818s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.005s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 982.862s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 12.86s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.368s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.933s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 179.058s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.807s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.924s median 
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
  - Observed: 4.294s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 399 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 62 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
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
  - Observed: 13 records 
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
  - Observed: 2; 3; 4; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 5.6x vs baseline. 
  - Observed: 50 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f757.jsonl[215] _id=69dfe8357957a33870f47d31 ts=2026-04-15T19:34:13.5110000Z`; `69cdc937d385e3b94310f757.jsonl[449] _id=69dfee8f7957a33870f4965d ts=2026-04-15T20:01:19.0760000Z`; `69cdc937d385e3b94310f757.jsonl[830] _id=69e2886d1724f0c9e2f7ab34 ts=2026-04-17T19:22:20.7560000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 62 records, TopographicMapEvent: 26 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 3 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1435 | 0.0 | 2.253 | 363.567 | 35.525 | 341107.65 | 0.17 | 385 | 2 |
| PlayerPositionEvent | 385 | 29.802 | 30.005 | 1353.663 | 36.505 | 341066.992 | 0.04 | 0 | 2 |
| questEvent | 69 | 0.002 | 148.623 | 7560.231 | 879.844 | 341200.446 | 0.01 | 14 | 8 |
| Topographic Map Event | 61 | 1.05 | 10.079 | 2829.475 | 315.339 | 168980.892 | 0.02 | 0 | 2 |
| argumentationToolEvent | 49 | 0.001 | 0.924 | 49.925 | 279.991 | 1139.684 | 1.2 | 6 | 1 |
| WaterChamberEvent | 36 | 0.83 | 5.933 | 8.487 | 20.581 | 22.451 | 7.07 | 0 | 0 |
| TopographicMapEvent | 25 | 0.36 | 4.368 | 6818.158 | 862.88 | 168866.69 | 0.01 | 0 | 2 |
| soilMachine | 17 | 0.948 | 4.294 | 31.264 | 123.423 | 216.104 | 1.92 | 0 | 0 |
| argumentationNodeEvent | 12 | 0.857 | 6.807 | 14351.159 | 77477.574 | 172054.55 | 0.0 | 0 | 1 |
| argumentationEvent | 10 | 0.038 | 179.058 | 52008.644 | 267360.186 | 345346.801 | 0.0 | 1 | 4 |
| Soil Key Puzzle | 7 | 3.019 | 982.862 | 24778.233 | 118443.714 | 168264.496 | 0.0 | 0 | 4 |
| TerasGardenBox | 6 | 2.433 | 12.86 | 15.29 | 35.65 | 41.874 | 3.92 | 0 | 0 |
| EndOfUnit | 3 | 1369.144 | 173761.818 | 173367.038 | 327849.319 | 344970.152 | 0.0 | 0 | 3 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.97s, p95 36.51s, n=385) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `38ms: 69cdc937d385e3b94310f757.jsonl[833] _id=69e2886d1724f0c9e2f7ab32 ts=2026-04-17T19:22:20.7410000Z ~ 69cdc937d385e3b94310f757.jsonl[836] _id=69e2886d1724f0c9e2f7ab38 ts=2026-04-17T19:22:20.7790000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc937d385e3b94310f757.jsonl[1359] _id=69e7cd681724f0c9e2f9cdef ts=2026-04-21T19:17:59.5450000Z ~ 69cdc937d385e3b94310f757.jsonl[1360] _id=69e7cd681724f0c9e2f9cdf1 ts=2026-04-21T19:17:59.5460000Z`; `750ms: 69cdc937d385e3b94310f757.jsonl[1362] _id=69e7cda01724f0c9e2f9cf3b ts=2026-04-21T19:18:55.6980000Z ~ 69cdc937d385e3b94310f757.jsonl[1363] _id=69e7cda11724f0c9e2f9cf42 ts=2026-04-21T19:18:56.4480000Z`; `703ms: 69cdc937d385e3b94310f757.jsonl[1343] _id=69e7cda01724f0c9e2f9cf3d ts=2026-04-21T19:18:55.7840000Z ~ 69cdc937d385e3b94310f757.jsonl[1367] _id=69e7cda11724f0c9e2f9cf47 ts=2026-04-21T19:18:56.4870000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 69cdc937d385e3b94310f757.jsonl[2123] _id=69e7d7441724f0c9e2f9f8d3 ts=2026-04-21T20:00:04.0750000Z ~ 69cdc937d385e3b94310f757.jsonl[2128] _id=69e7d7451724f0c9e2f9f8d6 ts=2026-04-21T20:00:04.0790000Z`; `5ms: 69cdc937d385e3b94310f757.jsonl[2137] _id=69e7d84b1724f0c9e2f9fcab ts=2026-04-21T20:04:26.6940000Z ~ 69cdc937d385e3b94310f757.jsonl[1904] _id=69e7d84b1724f0c9e2f9fcad ts=2026-04-21T20:04:26.6990000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f757.jsonl[1175] _id=69e293651724f0c9e2f7dbd4 ts=2026-04-17T20:09:09.7350000Z -> 69cdc937d385e3b94310f757.jsonl[1188] _id=69e7c7da1724f0c9e2f9adbd ts=2026-04-21T18:54:17.3850000Z; 46h 42m: 69cdc937d385e3b94310f757.jsonl[542] _id=69dff04d7957a33870f49eeb ts=2026-04-15T20:08:45.3320000Z -> 69cdc937d385e3b94310f757.jsonl[545] _id=69e281191724f0c9e2f78ebe ts=2026-04-17T18:51:04.2220000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 385 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f757.jsonl[1706] _id=69e7d3491724f0c9e2f9ea07 ts=2026-04-21T19:43:04.1500000Z -> 69cdc937d385e3b94310f757.jsonl[1711] _id=69e7d3551724f0c9e2f9ea23 ts=2026-04-21T19:43:04.15Z; 1ms: 69cdc937d385e3b94310f757.jsonl[1452] _id=69e7d0a01724f0c9e2f9dbef ts=2026-04-21T19:31:43.6690000Z -> 69cdc937d385e3b94310f757.jsonl[1453] _id=69e7d0a01724f0c9e2f9dbf1 ts=2026-04-21T19:31:43.6700000Z; 2ms: 69cdc937d385e3b94310f757.jsonl[1567] _id=69e7d1f31724f0c9e2f9e40b ts=2026-04-21T19:37:22.3220000Z -> 69cdc937d385e3b94310f757.jsonl[1568] _id=69e7d1f31724f0c9e2f9e40f ts=2026-04-21T19:37:22.3240000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 49m 
  - Evidence: 95h 49m: 69cdc937d385e3b94310f757.jsonl[1092] _id=69e28fbe1724f0c9e2f7ce9e ts=2026-04-17T19:53:33.9820000Z -> 69cdc937d385e3b94310f757.jsonl[1705] _id=69e7d3481724f0c9e2f9ea05 ts=2026-04-21T19:43:04.1340000Z; 48h 16m: 69cdc937d385e3b94310f757.jsonl[1954] _id=69dfe8fc7957a33870f48039 ts=2026-04-15T19:37:32.1640000Z -> 69cdc937d385e3b94310f757.jsonl[1092] _id=69e28fbe1724f0c9e2f7ce9e ts=2026-04-17T19:53:33.9820000Z; 22m 49s: 69cdc937d385e3b94310f757.jsonl[1705] _id=69e7d3481724f0c9e2f9ea05 ts=2026-04-21T19:43:04.1340000Z -> 69cdc937d385e3b94310f757.jsonl[1940] _id=69e7d8a21724f0c9e2f9feb3 ts=2026-04-21T20:05:53.2780000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc937d385e3b94310f757.jsonl[2028] _id=69e293801724f0c9e2f7dc4e ts=2026-04-17T20:09:36.2710000Z -> 69cdc937d385e3b94310f757.jsonl[2029] _id=69e7c7cd1724f0c9e2f9ad89 ts=2026-04-21T18:54:03.2630000Z; 46h 42m: 69cdc937d385e3b94310f757.jsonl[535] _id=69dff0417957a33870f49e7d ts=2026-04-15T20:08:32.8270000Z -> 69cdc937d385e3b94310f757.jsonl[544] _id=69e281151724f0c9e2f78eae ts=2026-04-17T18:51:01.2220000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 46h 44m 
  - Evidence: 46h 44m: 69cdc937d385e3b94310f757.jsonl[538] _id=69dff0437957a33870f49e99 ts=2026-04-15T20:08:35.6610000Z -> 69cdc937d385e3b94310f757.jsonl[564] _id=69e2818d1724f0c9e2f7903a ts=2026-04-17T18:53:00.1570000Z; 36m 35s: 69cdc937d385e3b94310f757.jsonl[880] _id=69e289441724f0c9e2f7ae6e ts=2026-04-17T19:25:56.3160000Z -> 69cdc937d385e3b94310f757.jsonl[1117] _id=69e291d71724f0c9e2f7d3f6 ts=2026-04-17T20:02:31.5370000Z; 32m 33s: 69cdc937d385e3b94310f757.jsonl[564] _id=69e2818d1724f0c9e2f7903a ts=2026-04-17T18:53:00.1570000Z -> 69cdc937d385e3b94310f757.jsonl[870] _id=69e2892e1724f0c9e2f7ae36 ts=2026-04-17T19:25:33.8770000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 56m 
  - Evidence: 46h 56m: 69cdc937d385e3b94310f757.jsonl[527] _id=69dfefca7957a33870f49c1b ts=2026-04-15T20:06:34.6630000Z -> 69cdc937d385e3b94310f757.jsonl[625] _id=69e283df1724f0c9e2f798a4 ts=2026-04-17T19:02:55.5550000Z; 26m 19s: 69cdc937d385e3b94310f757.jsonl[794] _id=69e287cb1724f0c9e2f7a848 ts=2026-04-17T19:19:38.9710000Z -> 69cdc937d385e3b94310f757.jsonl[1981] _id=69e28df61724f0c9e2f7c264 ts=2026-04-17T19:45:58.6290000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 54m 
  - Evidence: 46h 54m: 69cdc937d385e3b94310f757.jsonl[521] _id=69dfefc67957a33870f49c09 ts=2026-04-15T20:06:30.7620000Z -> 69cdc937d385e3b94310f757.jsonl[614] _id=69e283691724f0c9e2f79740 ts=2026-04-17T19:00:57.4520000Z; 17m 17s: 69cdc937d385e3b94310f757.jsonl[617] _id=69e283751724f0c9e2f79768 ts=2026-04-17T19:01:09.6040000Z -> 69cdc937d385e3b94310f757.jsonl[786] _id=69e287831724f0c9e2f7a70a ts=2026-04-17T19:18:26.9240000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 69cdc937d385e3b94310f757.jsonl[836] _id=69e2886d1724f0c9e2f7ab38 ts=2026-04-17T19:22:20.7790000Z -> 69cdc937d385e3b94310f757.jsonl[2112] _id=69e7cd701724f0c9e2f9ce2b ts=2026-04-21T19:18:07.5800000Z; 47h 47m: 69cdc937d385e3b94310f757.jsonl[212] _id=69dfe8357957a33870f47d2d ts=2026-04-15T19:34:13.4860000Z -> 69cdc937d385e3b94310f757.jsonl[820] _id=69e288401724f0c9e2f7aa2c ts=2026-04-17T19:21:36.6980000Z; 18m 49s: 69cdc937d385e3b94310f757.jsonl[1499] _id=69e7d1981724f0c9e2f9e275 ts=2026-04-21T19:35:51.6900000Z -> 69cdc937d385e3b94310f757.jsonl[1837] _id=69e7d6011724f0c9e2f9f389 ts=2026-04-21T19:54:41.1510000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.038s..0.038s shown 
  - Evidence: 38ms: 69cdc937d385e3b94310f757.jsonl[833] _id=69e2886d1724f0c9e2f7ab32 ts=2026-04-17T19:22:20.7410000Z -> 69cdc937d385e3b94310f757.jsonl[836] _id=69e2886d1724f0c9e2f7ab38 ts=2026-04-17T19:22:20.7790000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 47m 
  - Evidence: 47h 47m: 69cdc937d385e3b94310f757.jsonl[201] _id=69dfe8307957a33870f47d19 ts=2026-04-15T19:34:08.6160000Z -> 69cdc937d385e3b94310f757.jsonl[824] _id=69e288471724f0c9e2f7aa4a ts=2026-04-17T19:21:43.1660000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 18m 59s 
  - Evidence: 18m 59s: 69cdc937d385e3b94310f757.jsonl[1498] _id=69e7d1941724f0c9e2f9e265 ts=2026-04-21T19:35:47.7430000Z -> 69cdc937d385e3b94310f757.jsonl[1836] _id=69e7d6081724f0c9e2f9f3a9 ts=2026-04-21T19:54:47.4270000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.001s..0.034s shown 
  - Evidence: 1ms: 69cdc937d385e3b94310f757.jsonl[1359] _id=69e7cd681724f0c9e2f9cdef ts=2026-04-21T19:17:59.5450000Z -> 69cdc937d385e3b94310f757.jsonl[1360] _id=69e7cd681724f0c9e2f9cdf1 ts=2026-04-21T19:17:59.5460000Z; 4ms: 69cdc937d385e3b94310f757.jsonl[1528] _id=69e7d1941724f0c9e2f9e263 ts=2026-04-21T19:35:47.7390000Z -> 69cdc937d385e3b94310f757.jsonl[1498] _id=69e7d1941724f0c9e2f9e265 ts=2026-04-21T19:35:47.7430000Z; 34ms: 69cdc937d385e3b94310f757.jsonl[1396] _id=69e7cf2e1724f0c9e2f9d4dd ts=2026-04-21T19:25:33.3070000Z -> 69cdc937d385e3b94310f757.jsonl[1397] _id=69e7cf2e1724f0c9e2f9d4df ts=2026-04-21T19:25:33.3410000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc937d385e3b94310f757.jsonl[1162] _id=69e292fd1724f0c9e2f7d973 ts=2026-04-17T20:07:25.2490000Z -> 69cdc937d385e3b94310f757.jsonl[1181] _id=69e7c7ce1724f0c9e2f9ad91 ts=2026-04-21T18:54:05.6950000Z; 46h 42m: 69cdc937d385e3b94310f757.jsonl[524] _id=69dff0347957a33870f49e41 ts=2026-04-15T20:08:19.9610000Z -> 69cdc937d385e3b94310f757.jsonl[549] _id=69e2811a1724f0c9e2f78ec2 ts=2026-04-17T18:51:05.0470000Z; 16m 59s: 69cdc937d385e3b94310f757.jsonl[1325] _id=69e7cc651724f0c9e2f9c757 ts=2026-04-21T19:13:40.8880000Z -> 69cdc937d385e3b94310f757.jsonl[1419] _id=69e7d0611724f0c9e2f9da69 ts=2026-04-21T19:30:40.8600000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f757.jsonl[139] _id=69dfe73c7957a33870f479bd ts=2026-04-15T19:30:03.1620000Z -> 69cdc937d385e3b94310f757.jsonl[154] _id=69dfe73c7957a33870f479bf ts=2026-04-15T19:30:03.1640000Z; 4ms: 69cdc937d385e3b94310f757.jsonl[2123] _id=69e7d7441724f0c9e2f9f8d3 ts=2026-04-21T20:00:04.0750000Z -> 69cdc937d385e3b94310f757.jsonl[2128] _id=69e7d7451724f0c9e2f9f8d6 ts=2026-04-21T20:00:04.0790000Z; 5ms: 69cdc937d385e3b94310f757.jsonl[2137] _id=69e7d84b1724f0c9e2f9fcab ts=2026-04-21T20:04:26.6940000Z -> 69cdc937d385e3b94310f757.jsonl[1904] _id=69e7d84b1724f0c9e2f9fcad ts=2026-04-21T20:04:26.6990000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc937d385e3b94310f757.jsonl:69cdc937d385e3b94310f757, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f757.jsonl[349] _id=69dfec6d7957a33870f48d53 ts=2026-04-15T19:52:12.7990000Z`; `69cdc937d385e3b94310f757.jsonl[880] _id=69e289441724f0c9e2f7ae6e ts=2026-04-17T19:25:56.3160000Z`; `69cdc937d385e3b94310f757.jsonl[1119] _id=69e291f11724f0c9e2f7d44e ts=2026-04-17T20:02:57.4140000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 26 record(s) match the trigger in 69cdc937d385e3b94310f757.jsonl:69cdc937d385e3b94310f757, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f757.jsonl[425] _id=69dfedec7957a33870f493c1 ts=2026-04-15T19:58:35.9520000Z`; `69cdc937d385e3b94310f757.jsonl[431] _id=69dfedf07957a33870f493cb ts=2026-04-15T19:58:40.3010000Z`; `69cdc937d385e3b94310f757.jsonl[461] _id=69dfee957957a33870f49675 ts=2026-04-15T20:01:25.4190000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f757.jsonl[645] _id=69e2843f1724f0c9e2f79a14 ts=2026-04-17T19:04:30.7140000Z`; `69cdc937d385e3b94310f757.jsonl[668] _id=69e284c71724f0c9e2f79c3e ts=2026-04-17T19:06:47.4440000Z`; `69cdc937d385e3b94310f757.jsonl[2084] _id=69e7cb8a1724f0c9e2f9c278 ts=2026-04-21T19:10:01.3270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f757.jsonl[836] _id=69e2886d1724f0c9e2f7ab38 ts=2026-04-17T19:22:20.7790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f757.jsonl[1359] _id=69e7cd681724f0c9e2f9cdef ts=2026-04-21T19:17:59.5450000Z`; `69cdc937d385e3b94310f757.jsonl[1360] _id=69e7cd681724f0c9e2f9cdf1 ts=2026-04-21T19:17:59.5460000Z`; `69cdc937d385e3b94310f757.jsonl[1528] _id=69e7d1941724f0c9e2f9e263 ts=2026-04-21T19:35:47.7390000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f757.jsonl[564] _id=69e2818d1724f0c9e2f7903a ts=2026-04-17T18:53:00.1570000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f757.jsonl[1499] _id=69e7d1981724f0c9e2f9e275 ts=2026-04-21T19:35:51.6900000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f757.jsonl[1841] _id=69e7d6141724f0c9e2f9f3db ts=2026-04-21T19:54:59.7680000Z`; `69cdc937d385e3b94310f757.jsonl[1847] _id=69e7d65e1724f0c9e2f9f561 ts=2026-04-21T19:56:13.9090000Z`; `69cdc937d385e3b94310f757.jsonl[1850] _id=69e7d65f1724f0c9e2f9f567 ts=2026-04-21T19:56:14.5800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 181 unmatched 'DialogueStartEvent' (totals: 313 start, 135 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 5 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 24 open, 26 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 41 start, 29 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.39s, min -13.30s, max -0.17s over 2141 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f757\coverage.yaml

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
  - Observed: 62 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1436 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (291); Unit 4 Dev (242); Unit 2 Prod (Refactor) (204); Unit 1 Dev (182); Unit 5 Dev (138); Unit 4 Dev - Anderson Base (134); Unit 4 Dev - Dungeon (121); Unit 3 Dungeon Dev (104); Unit 5 Dev - Dungeon (20)
- **eventKey:** present on 988 of 1436 records
- **Intervals:** median 2.25s (p5 0.01s / p95 35.52s, n=1435)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x988; [conversationId, dialogueEventType] x448
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1436/1436 records)
    numeric range 10 .. 114 (43 unique)
data.dialogueEventType  (string, 1436/1436 records)
    "DialogueNodeEvent"  x988
    "DialogueStartEvent"  x313
    "DialogueFinishEvent"  x135
data.nodeId  (number, 988/1436 records)
    numeric range 0 .. 289 (195 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 399 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (74); Unit 2 Prod (Refactor) (66); Unit 1 Dev (55); Unit 4 Dev (47); Unit 4 Dev - Anderson Base (41); Unit 3 Dungeon Dev (36); Unit 4 Dev - Dungeon (35); Unit 5 Dev (28); Unit 5 Dev - Dungeon (17)
- **Intervals:** median 30.00s (p5 29.97s / p95 36.51s, n=385)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 399/399 records)
data.position.x  (number, 399/399 records)
    numeric range -690.489 .. 1558.67 (220 unique)
data.position.y  (number, 399/399 records)
    numeric range -114.942 .. 222.004 (186 unique)
data.position.z  (number, 399/399 records)
    numeric range -1113.67 .. 1818.99 (220 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 4 Dev - Dungeon (12); Unit 3 Dev (9); Unit 2 Prod (Refactor) (8); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 148.62s (p5 0.01s / p95 879.84s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x41; [questEventType, questID, questName, questSuccessOrFailure] x29
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x41
    "questFinishEvent"  x29
data.questID  (string, 70/70 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 29/70 records)
    "Succeeded"  x29
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 62 records

- **Scenes:** Unit 3 Dev (50); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 10.08s (p5 1.92s / p95 315.34s, n=61)
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "MapCloseEvent"  x31
    "MapOpenEvent"  x31
data.featureUsed  (string, 62/62 records)
    "Map"  x62
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationToolEvent` — 50 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (34); Unit 5 Dev (16)
- **Intervals:** median 0.92s (p5 0.04s / p95 279.99s, n=49)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "argumentationToolClose"  x26
    "argumentationToolOpen"  x24
data.argumentationTitle  (string, 50/50 records)
    "Unit 4 - Flooding"  x34
    "Unit 5"  x16
data.toolName  (string, 50/50 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x24
    "BackingInfoPanel - Soil Flow Rates"  x10
    "BackingInfoPanel - Evaporation Flow Diagram"  x9
    "BackingInfoPanel - Heat Added/Released Chart"  x7
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `WaterChamberEvent` — 37 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (37)
- **Intervals:** median 5.93s (p5 0.98s / p95 20.58s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "On"  x25
    "Off"  x12
data.floor  (string, 37/37 records)
    "3"  x23
    "4"  x7
    "2"  x5
    "1"  x2
data.machineNumber  (string, 37/37 records)
    "One"  x36
    "Two"  x1
data.machineType  (string, 37/37 records)
    "Condenser"  x17
    "DualChamber_Evaporator"  x6
    "Evaporator"  x6
    "DualChamber_Condenser"  x4
    "VentSwitch"  x4
data.room  (string, 37/37 records)
    "2"  x23
    "1"  x6
    "3"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 26 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (8)
- **Intervals:** median 4.37s (p5 0.73s / p95 862.88s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "dragEnd"  x13
    "dragStart"  x13
data.featureUsed  (string, 26/26 records)
    "waypoint"  x26
data.location  (object, 26/26 records)
data.location.x  (number, 26/26 records)
    numeric range -770.79 .. 266.723 (14 unique)
data.location.y  (number, 26/26 records)
    numeric range -307.4 .. 148.992 (14 unique)
data.location.z  (number, 26/26 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 18 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (18)
- **Intervals:** median 4.29s (p5 1.07s / p95 123.42s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "ChangeCanister"  x18
data.canisterType  (string, 18/18 records)
    "Clay"  x6
    "Bedrock"  x4
    "Gravel"  x4
    "Sand"  x4
data.floor  (string, 18/18 records)
    "5"  x11
    "2"  x5
    "3"  x1
    "4"  x1
data.machine  (string, 18/18 records)
    "1"  x15
    "2"  x3
data.row  (string, 18/18 records)
    "TopRow"  x11
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 13 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (10); Unit 3 Dev (3)
- **Intervals:** median 6.81s (p5 1.89s / p95 77477.57s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationNodeAdd"  x11
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 13/13 records)
    "I"  x5
    "B"  x3
    "1"  x2
    "A"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (2)
- **Intervals:** median 179.06s (p5 19.84s / p95 267360.19s, n=10)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationSessionOpen"  x6
    "argumentationSessionClose"  x5
data.argumentationDescription  (string, 11/11 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 11/11 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 982.86s (p5 8.85s / p95 118443.71s, n=7)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Started"  x5
    "Finished"  x3
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 12.86s (p5 3.01s / p95 35.65s, n=6)
- **`data` key-set variants:** [actionType, boxId, soilType] x4; [actionType, boxID, soilType] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "cameraPlaced"  x4
    "soilSelected"  x3
data.boxID  (string, 3/7 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.boxId  (string, 4/7 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 7/7 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 173761.82s (p5 18608.41s / p95 327849.32s, n=3)
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "dragStart" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*