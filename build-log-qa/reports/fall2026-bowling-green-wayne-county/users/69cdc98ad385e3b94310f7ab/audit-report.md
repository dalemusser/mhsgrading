# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ab

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ab
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7ab.jsonl
- **Records:** 3577 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7ab
- **Time span:** 2026-04-14T19:31:41.165000+00:00 .. 2026-04-24T18:56:51.623000+00:00 (239h 25m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ab\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 3577 records, 9 scenes.
- Findings: **0 FAIL**, **45 WARNING**, 65 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 2539 | 70.98 | 1 | 9 | 1775 | 2026-04-14T19:32:09.375000+00:00 | 2026-04-24T18:56:02.732000+00:00 | 239h 23m |
| PlayerPositionEvent | 632 | 17.67 | 1 | 9 | 0 | 2026-04-14T19:31:41.165000+00:00 | 2026-04-24T18:56:37.084000+00:00 | 239h 24m |
| WaterChamberEvent | 130 | 3.63 | 1 | 1 | 0 | 2026-04-22T19:35:19.187000+00:00 | 2026-04-22T19:51:26.262000+00:00 | 16m 7s |
| questEvent | 91 | 2.54 | 1 | 9 | 91 | 2026-04-14T19:32:09.331000+00:00 | 2026-04-24T18:55:08.969000+00:00 | 239h 22m |
| Topographic Map Event | 44 | 1.23 | 1 | 2 | 0 | 2026-04-14T20:06:37.785000+00:00 | 2026-04-20T19:27:41.513000+00:00 | 143h 21m |
| soilMachine | 42 | 1.17 | 1 | 1 | 0 | 2026-04-20T19:49:42.314000+00:00 | 2026-04-20T19:56:54.476000+00:00 | 7m 12s |
| argumentationNodeEvent | 41 | 1.15 | 1 | 3 | 0 | 2026-04-14T19:55:42.269000+00:00 | 2026-04-17T16:38:54.212000+00:00 | 68h 43m |
| argumentationToolEvent | 18 | 0.5 | 1 | 2 | 0 | 2026-04-22T18:52:50.977000+00:00 | 2026-04-22T19:58:07.775000+00:00 | 1h 5m |
| argumentationEvent | 13 | 0.36 | 1 | 5 | 0 | 2026-04-14T19:54:39.907000+00:00 | 2026-04-22T19:58:07.939000+00:00 | 192h 3m |
| TopographicMapEvent | 8 | 0.22 | 1 | 2 | 0 | 2026-04-16T19:13:12.489000+00:00 | 2026-04-20T19:23:40.981000+00:00 | 96h 10m |
| EndOfUnit | 7 | 0.2 | 1 | 5 | 0 | 2026-04-14T20:01:36.534000+00:00 | 2026-04-24T18:56:51.623000+00:00 | 238h 55m |
| Soil Key Puzzle | 6 | 0.17 | 1 | 3 | 0 | 2026-04-16T19:23:36.178000+00:00 | 2026-04-20T19:34:33.246000+00:00 | 96h 10m |
| TerasGardenBox | 6 | 0.17 | 1 | 1 | 0 | 2026-04-22T19:27:58.945000+00:00 | 2026-04-22T19:28:20.974000+00:00 | 22.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.299s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 169424.671s median 
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
  - Observed: 184.342s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 0.218s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.461s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 2.1s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 497.316s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.12s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.43s median 
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
  - Observed: 1.004s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
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
  - Observed: 44 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
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
- **INFO / Info** `WaterChamberEvent` — record volume changed 6.5x vs baseline. 
  - Observed: 130 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 41 records 
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
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `soilMachine` — record volume changed 8.4x vs baseline. 
  - Observed: 42 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 60 mismatch(es); e.g. 'DialogueNodeEvent:31:70' vs expected 'DialogueNodeEvent:31:71' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[163] _id=69de9b817957a33870f3a931 ts=2026-04-14T19:54:41.4220000Z`; `69cdc98ad385e3b94310f7ab.jsonl[164] _id=69de9b827957a33870f3a933 ts=2026-04-14T19:54:41.5520000Z`; `69cdc98ad385e3b94310f7ab.jsonl[169] _id=69de9b827957a33870f3a939 ts=2026-04-14T19:54:41.9120000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 44 records, TopographicMapEvent: 8 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2538 | 0.0 | 1.299 | 339.572 | 28.719 | 267288.77 | 0.18 | 625 | 8 |
| PlayerPositionEvent | 620 | 22.58 | 30.013 | 1389.22 | 40.519 | 267288.817 | 0.04 | 0 | 8 |
| WaterChamberEvent | 129 | 0.004 | 2.1 | 7.497 | 30.784 | 56.697 | 8.0 | 6 | 0 |
| questEvent | 90 | 0.002 | 109.166 | 9575.329 | 37767.916 | 267335.287 | 0.01 | 18 | 15 |
| Topographic Map Event | 43 | 0.188 | 11.328 | 12001.482 | 53622.415 | 270221.818 | 0.0 | 0 | 6 |
| soilMachine | 41 | 0.004 | 1.004 | 10.541 | 69.681 | 112.811 | 5.69 | 1 | 0 |
| argumentationNodeEvent | 40 | 0.69 | 6.12 | 6184.799 | 1276.161 | 229983.35 | 0.01 | 0 | 2 |
| argumentationToolEvent | 17 | 0.001 | 1.43 | 230.4 | 1282.271 | 2584.478 | 0.26 | 4 | 2 |
| argumentationEvent | 12 | 0.115 | 497.316 | 57617.336 | 324502.885 | 440032.267 | 0.0 | 0 | 6 |
| TopographicMapEvent | 7 | 1.145 | 4.461 | 49461.213 | 242152.391 | 345720.519 | 0.0 | 0 | 1 |
| EndOfUnit | 6 | 1886.089 | 169424.671 | 143352.515 | 272377.677 | 286471.521 | 0.0 | 0 | 6 |
| Soil Key Puzzle | 5 | 17.503 | 184.342 | 69251.414 | 275598.273 | 343989.16 | 0.0 | 0 | 2 |
| TerasGardenBox | 5 | 0.118 | 0.218 | 4.406 | 11.35 | 11.753 | 13.62 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.013s (p5 29.97s, p95 40.52s, n=620) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `218ms: 69cdc98ad385e3b94310f7ab.jsonl[2247] _id=69e9213f1724f0c9e2faa401 ts=2026-04-22T19:27:58.9450000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2251] _id=69e921401724f0c9e2faa408 ts=2026-04-22T19:27:59.1630000Z`; `204ms: 69cdc98ad385e3b94310f7ab.jsonl[2258] _id=69e921551724f0c9e2faa463 ts=2026-04-22T19:28:20.6520000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[3494] _id=69e921551724f0c9e2faa465 ts=2026-04-22T19:28:20.8560000Z`; `118ms: 69cdc98ad385e3b94310f7ab.jsonl[3494] _id=69e921551724f0c9e2faa465 ts=2026-04-22T19:28:20.8560000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2259] _id=69e921561724f0c9e2faa467 ts=2026-04-22T19:28:20.9740000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 35 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `430ms: 69cdc98ad385e3b94310f7ab.jsonl[2585] _id=69e9230a1724f0c9e2faab21 ts=2026-04-22T19:35:37.2040000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2574] _id=69e9230a1724f0c9e2faab25 ts=2026-04-22T19:35:37.6340000Z`; `940ms: 69cdc98ad385e3b94310f7ab.jsonl[2575] _id=69e9230b1724f0c9e2faab29 ts=2026-04-22T19:35:38.8390000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2587] _id=69e9230c1724f0c9e2faab2d ts=2026-04-22T19:35:39.7790000Z`; `267ms: 69cdc98ad385e3b94310f7ab.jsonl[2587] _id=69e9230c1724f0c9e2faab2d ts=2026-04-22T19:35:39.7790000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2588] _id=69e9230d1724f0c9e2faab31 ts=2026-04-22T19:35:40.0460000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `115ms: 69cdc98ad385e3b94310f7ab.jsonl[3457] _id=69e262241724f0c9e2f71dfc ts=2026-04-17T16:39:00.3090000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[3454] _id=69e262251724f0c9e2f71e02 ts=2026-04-17T16:39:00.4240000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc98ad385e3b94310f7ab.jsonl[3525] _id=69e919041724f0c9e2fa858d ts=2026-04-22T18:52:50.9770000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2356] _id=69e919041724f0c9e2fa858f ts=2026-04-22T18:52:50.9780000Z`; `2ms: 69cdc98ad385e3b94310f7ab.jsonl[340] _id=69e91e341724f0c9e2fa9b59 ts=2026-04-22T19:14:58.8700000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[333] _id=69e91e341724f0c9e2fa9b5b ts=2026-04-22T19:14:58.8720000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 69cdc98ad385e3b94310f7ab.jsonl[2874] _id=69e9285d1724f0c9e2fabe37 ts=2026-04-22T19:58:20.6400000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2875] _id=69e9285e1724f0c9e2fabe39 ts=2026-04-22T19:58:20.6520000Z`; `8ms: 69cdc98ad385e3b94310f7ab.jsonl[2925] _id=69e929051724f0c9e2fac141 ts=2026-04-22T20:01:08.5630000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2918] _id=69e929051724f0c9e2fac143 ts=2026-04-22T20:01:08.5710000Z`; `4ms: 69cdc98ad385e3b94310f7ab.jsonl[2987] _id=69e929af1724f0c9e2fac3ab ts=2026-04-22T20:03:56.2010000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2985] _id=69e929af1724f0c9e2fac3ad ts=2026-04-22T20:03:56.2050000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 20 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `832ms: 69cdc98ad385e3b94310f7ab.jsonl[2047] _id=69e684391724f0c9e2f8f781 ts=2026-04-20T19:53:28.4640000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2051] _id=69e6843a1724f0c9e2f8f783 ts=2026-04-20T19:53:29.2960000Z`; `209ms: 69cdc98ad385e3b94310f7ab.jsonl[2051] _id=69e6843a1724f0c9e2f8f783 ts=2026-04-20T19:53:29.2960000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2052] _id=69e6843a1724f0c9e2f8f787 ts=2026-04-20T19:53:29.5050000Z`; `192ms: 69cdc98ad385e3b94310f7ab.jsonl[2052] _id=69e6843a1724f0c9e2f8f787 ts=2026-04-20T19:53:29.5050000Z ~ 69cdc98ad385e3b94310f7ab.jsonl[2034] _id=69e6843a1724f0c9e2f8f789 ts=2026-04-20T19:53:29.6970000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 74h 14m 
  - Evidence: 74h 14m: 69cdc98ad385e3b94310f7ab.jsonl[3473] _id=69e262a51724f0c9e2f71e92 ts=2026-04-17T16:41:08.5810000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1572] _id=69e676be1724f0c9e2f8bc9b ts=2026-04-20T18:55:57.3510000Z; 46h 40m: 69cdc98ad385e3b94310f7ab.jsonl[2244] _id=69e688141724f0c9e2f90315 ts=2026-04-20T20:09:55.3990000Z -> 69cdc98ad385e3b94310f7ab.jsonl[3512] _id=69e9186c1724f0c9e2fa831f ts=2026-04-22T18:50:18.8330000Z; 46h 39m: 69cdc98ad385e3b94310f7ab.jsonl[312] _id=69de9ee67957a33870f3b729 ts=2026-04-14T20:09:09.8710000Z -> 69cdc98ad385e3b94310f7ab.jsonl[3286] _id=69e12f131724f0c9e2f68f14 ts=2026-04-16T18:48:49.9480000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 625 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7ab.jsonl[1232] _id=69e21ff11724f0c9e2f719dc ts=2026-04-17T11:56:32.7730000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1203] _id=69e220401724f0c9e2f719de ts=2026-04-17T11:56:32.773Z; 2ms: 69cdc98ad385e3b94310f7ab.jsonl[3415] _id=69e25fdc1724f0c9e2f71cca ts=2026-04-17T16:29:15.7030000Z -> 69cdc98ad385e3b94310f7ab.jsonl[3421] _id=69e25fdc1724f0c9e2f71ccc ts=2026-04-17T16:29:15.7050000Z; 2ms: 69cdc98ad385e3b94310f7ab.jsonl[923] _id=69e91f2a1724f0c9e2fa9ec3 ts=2026-04-22T19:19:05.3380000Z -> 69cdc98ad385e3b94310f7ab.jsonl[924] _id=69e91f2a1724f0c9e2fa9ec5 ts=2026-04-22T19:19:05.3400000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 79h 34m 
  - Evidence: 79h 34m: 69cdc98ad385e3b94310f7ab.jsonl[1231] _id=69e21ff01724f0c9e2f719da ts=2026-04-17T11:56:32.6770000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1860] _id=69e67ef91724f0c9e2f8e2e3 ts=2026-04-20T19:31:04.1980000Z; 63h 54m: 69cdc98ad385e3b94310f7ab.jsonl[229] _id=69de9d207957a33870f3b085 ts=2026-04-14T20:01:36.5340000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1231] _id=69e21ff01724f0c9e2f719da ts=2026-04-17T11:56:32.6770000Z; 48h 1m: 69cdc98ad385e3b94310f7ab.jsonl[1860] _id=69e67ef91724f0c9e2f8e2e3 ts=2026-04-20T19:31:04.1980000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2557] _id=69e922381724f0c9e2faa813 ts=2026-04-22T19:32:07.5890000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 74h 14m 
  - Evidence: 74h 14m: 69cdc98ad385e3b94310f7ab.jsonl[3474] _id=69e2628e1724f0c9e2f71e88 ts=2026-04-17T16:40:45.7580000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1567] _id=69e676a81724f0c9e2f8bc3b ts=2026-04-20T18:55:34.5750000Z; 46h 39m: 69cdc98ad385e3b94310f7ab.jsonl[2246] _id=69e688411724f0c9e2f90395 ts=2026-04-20T20:10:40.0460000Z -> 69cdc98ad385e3b94310f7ab.jsonl[3511] _id=69e918671724f0c9e2fa8303 ts=2026-04-22T18:50:14.0420000Z; 46h 39m: 69cdc98ad385e3b94310f7ab.jsonl[308] _id=69de9eea7957a33870f3b72f ts=2026-04-14T20:09:14.3080000Z -> 69cdc98ad385e3b94310f7ab.jsonl[394] _id=69e12f081724f0c9e2f68f10 ts=2026-04-16T18:48:38.6780000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc98ad385e3b94310f7ab.jsonl[3316] _id=69e137f11724f0c9e2f6c964 ts=2026-04-16T19:26:40.5200000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1605] _id=69e677a61724f0c9e2f8c0e9 ts=2026-04-20T18:59:49.6800000Z; 33m 54s: 69cdc98ad385e3b94310f7ab.jsonl[1608] _id=69e677c61724f0c9e2f8c173 ts=2026-04-20T19:00:21.0200000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1881] _id=69e67fb81724f0c9e2f8e6bd ts=2026-04-20T19:34:15.7430000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 75h 3m 
  - Evidence: 75h 3m: 69cdc98ad385e3b94310f7ab.jsonl[1457] _id=69e25da11724f0c9e2f71c1c ts=2026-04-17T16:19:45.4090000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1760] _id=69e67d301724f0c9e2f8dac7 ts=2026-04-20T19:23:27.2270000Z; 46h 51m: 69cdc98ad385e3b94310f7ab.jsonl[279] _id=69de9e527957a33870f3b523 ts=2026-04-14T20:06:41.9710000Z -> 69cdc98ad385e3b94310f7ab.jsonl[442] _id=69e1314b1724f0c9e2f69558 ts=2026-04-16T18:58:19.2320000Z; 16h 4m: 69cdc98ad385e3b94310f7ab.jsonl[883] _id=69e13efd1724f0c9e2f706c0 ts=2026-04-16T19:56:44.8390000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1274] _id=69e2210c1724f0c9e2f71a2e ts=2026-04-17T12:01:16.3890000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 69cdc98ad385e3b94310f7ab.jsonl[646] _id=69e136c01724f0c9e2f6b6b0 ts=2026-04-16T19:21:35.8200000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1759] _id=69e67d391724f0c9e2f8daf3 ts=2026-04-20T19:23:36.3390000Z
- **INFO / Info** `WaterChamberEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.004s..0.009s shown 
  - Evidence: 4ms: 69cdc98ad385e3b94310f7ab.jsonl[2602] _id=69e923231724f0c9e2faabaf ts=2026-04-22T19:36:02.1580000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2608] _id=69e923231724f0c9e2faabb1 ts=2026-04-22T19:36:02.1620000Z; 8ms: 69cdc98ad385e3b94310f7ab.jsonl[2606] _id=69e923211724f0c9e2faaba1 ts=2026-04-22T19:36:01.0060000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2600] _id=69e923221724f0c9e2faaba5 ts=2026-04-22T19:36:01.0140000Z; 9ms: 69cdc98ad385e3b94310f7ab.jsonl[2614] _id=69e9234b1724f0c9e2faac55 ts=2026-04-22T19:36:42.7990000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2620] _id=69e9234c1724f0c9e2faac57 ts=2026-04-22T19:36:42.8080000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 122h 13m 
  - Evidence: 122h 13m: 69cdc98ad385e3b94310f7ab.jsonl[3454] _id=69e262251724f0c9e2f71e02 ts=2026-04-17T16:39:00.4240000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2352] _id=69e919051724f0c9e2fa8593 ts=2026-04-22T18:52:52.6910000Z; 63h 52m: 69cdc98ad385e3b94310f7ab.jsonl[183] _id=69de9c557957a33870f3ad69 ts=2026-04-14T19:58:13.1330000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1123] _id=69e21eb01724f0c9e2f7191a ts=2026-04-17T11:51:11.9780000Z; 4h 31m: 69cdc98ad385e3b94310f7ab.jsonl[1130] _id=69e21f511724f0c9e2f7196c ts=2026-04-17T11:53:53.6020000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1474] _id=69e25efe1724f0c9e2f71c8e ts=2026-04-17T16:25:33.8650000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 63h 53m 
  - Evidence: 63h 53m: 69cdc98ad385e3b94310f7ab.jsonl[190] _id=69de9c537957a33870f3ad5f ts=2026-04-14T19:58:11.2410000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1131] _id=69e21eb21724f0c9e2f71920 ts=2026-04-17T11:51:14.5910000Z; 4h 35m: 69cdc98ad385e3b94310f7ab.jsonl[1152] _id=69e21f501724f0c9e2f7196a ts=2026-04-17T11:53:52.4640000Z -> 69cdc98ad385e3b94310f7ab.jsonl[3413] _id=69e25fd41724f0c9e2f71cbc ts=2026-04-17T16:29:07.9410000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 43m 4s 
  - Evidence: 43m 4s: 69cdc98ad385e3b94310f7ab.jsonl[333] _id=69e91e341724f0c9e2fa9b5b ts=2026-04-22T19:14:58.8720000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2861] _id=69e9284c1724f0c9e2fabde3 ts=2026-04-22T19:58:03.3500000Z; 15m 56s: 69cdc98ad385e3b94310f7ab.jsonl[2422] _id=69e91a771724f0c9e2fa8b7d ts=2026-04-22T18:59:02.1510000Z -> 69cdc98ad385e3b94310f7ab.jsonl[340] _id=69e91e341724f0c9e2fa9b59 ts=2026-04-22T19:14:58.8700000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.001s..0.030s shown 
  - Evidence: 1ms: 69cdc98ad385e3b94310f7ab.jsonl[3525] _id=69e919041724f0c9e2fa858d ts=2026-04-22T18:52:50.9770000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2356] _id=69e919041724f0c9e2fa858f ts=2026-04-22T18:52:50.9780000Z; 2ms: 69cdc98ad385e3b94310f7ab.jsonl[340] _id=69e91e341724f0c9e2fa9b59 ts=2026-04-22T19:14:58.8700000Z -> 69cdc98ad385e3b94310f7ab.jsonl[333] _id=69e91e341724f0c9e2fa9b5b ts=2026-04-22T19:14:58.8720000Z; 30ms: 69cdc98ad385e3b94310f7ab.jsonl[2421] _id=69e91a751724f0c9e2fa8b73 ts=2026-04-22T18:59:00.2200000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2428] _id=69e91a751724f0c9e2fa8b75 ts=2026-04-22T18:59:00.2500000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 74h 15m 
  - Evidence: 74h 15m: 69cdc98ad385e3b94310f7ab.jsonl[3467] _id=69e262661724f0c9e2f71e4a ts=2026-04-17T16:40:06.0220000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1571] _id=69e676b01724f0c9e2f8bc55 ts=2026-04-20T18:55:41.3090000Z; 46h 44m: 69cdc98ad385e3b94310f7ab.jsonl[262] _id=69de9dd37957a33870f3b349 ts=2026-04-14T20:04:35.5480000Z -> 69cdc98ad385e3b94310f7ab.jsonl[3285] _id=69e12f111724f0c9e2f68f12 ts=2026-04-16T18:48:47.5300000Z; 46h 41m: 69cdc98ad385e3b94310f7ab.jsonl[2234] _id=69e687e71724f0c9e2f90243 ts=2026-04-20T20:09:10.5710000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2319] _id=69e9186b1724f0c9e2fa831a ts=2026-04-22T18:50:17.4710000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 69cdc98ad385e3b94310f7ab.jsonl[152] _id=69de9b427957a33870f3a81b ts=2026-04-14T19:53:38.4360000Z -> 69cdc98ad385e3b94310f7ab.jsonl[153] _id=69de9b427957a33870f3a81d ts=2026-04-14T19:53:38.4380000Z; 4ms: 69cdc98ad385e3b94310f7ab.jsonl[2987] _id=69e929af1724f0c9e2fac3ab ts=2026-04-22T20:03:56.2010000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2985] _id=69e929af1724f0c9e2fac3ad ts=2026-04-22T20:03:56.2050000Z; 5ms: 69cdc98ad385e3b94310f7ab.jsonl[1977] _id=69e682c31724f0c9e2f8f389 ts=2026-04-20T19:47:13.7710000Z -> 69cdc98ad385e3b94310f7ab.jsonl[1978] _id=69e682c31724f0c9e2f8f38b ts=2026-04-20T19:47:13.7760000Z
- **INFO / Info** `soilMachine` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.004s..0.004s shown 
  - Evidence: 4ms: 69cdc98ad385e3b94310f7ab.jsonl[2065] _id=69e6844d1724f0c9e2f8f7d1 ts=2026-04-20T19:53:48.2770000Z -> 69cdc98ad385e3b94310f7ab.jsonl[2066] _id=69e6844e1724f0c9e2f8f7d5 ts=2026-04-20T19:53:48.2810000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7ab.jsonl:69cdc98ad385e3b94310f7ab, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[3316] _id=69e137f11724f0c9e2f6c964 ts=2026-04-16T19:26:40.5200000Z`; `69cdc98ad385e3b94310f7ab.jsonl[1608] _id=69e677c61724f0c9e2f8c173 ts=2026-04-20T19:00:21.0200000Z`; `69cdc98ad385e3b94310f7ab.jsonl[1883] _id=69e67fca1724f0c9e2f8e723 ts=2026-04-20T19:34:33.2460000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 8 record(s) match the trigger in 69cdc98ad385e3b94310f7ab.jsonl:69cdc98ad385e3b94310f7ab, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[575] _id=69e134c91724f0c9e2f6a944 ts=2026-04-16T19:13:12.4890000Z`; `69cdc98ad385e3b94310f7ab.jsonl[578] _id=69e134ca1724f0c9e2f6a94c ts=2026-04-16T19:13:13.6340000Z`; `69cdc98ad385e3b94310f7ab.jsonl[3305] _id=69e136b71724f0c9e2f6b64e ts=2026-04-16T19:21:27.0580000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[741] _id=69e13b711724f0c9e2f6f77e ts=2026-04-16T19:41:34.5660000Z`; `69cdc98ad385e3b94310f7ab.jsonl[1308] _id=69e221b61724f0c9e2f71a62 ts=2026-04-17T12:04:05.8560000Z`; `69cdc98ad385e3b94310f7ab.jsonl[1178] _id=69e227cd1724f0c9e2f71a9a ts=2026-04-17T12:30:03.9590000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[3454] _id=69e262251724f0c9e2f71e02 ts=2026-04-17T16:39:00.4240000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[3525] _id=69e919041724f0c9e2fa858d ts=2026-04-22T18:52:50.9770000Z`; `69cdc98ad385e3b94310f7ab.jsonl[2356] _id=69e919041724f0c9e2fa858f ts=2026-04-22T18:52:50.9780000Z`; `69cdc98ad385e3b94310f7ab.jsonl[340] _id=69e91e341724f0c9e2fa9b59 ts=2026-04-22T19:14:58.8700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[3346] _id=69e139d01724f0c9e2f6e814 ts=2026-04-16T19:34:37.9280000Z`; `69cdc98ad385e3b94310f7ab.jsonl[1769] _id=69e67da31724f0c9e2f8dcc9 ts=2026-04-20T19:25:22.5110000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[343] _id=69e91e3e1724f0c9e2fa9b7d ts=2026-04-22T19:15:09.9170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7ab.jsonl[2866] _id=69e9284f1724f0c9e2fabdf5 ts=2026-04-22T19:58:06.8690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 216 unmatched 'DialogueStartEvent' (totals: 488 start, 276 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 7 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 8 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 53 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.00s, min -80.04s, max -0.15s over 3577 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ab\coverage.yaml

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
  - Observed: 44 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2539 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (696); Unit 3 Dev (433); Unit 5 Dev (399); Unit 4 Dev - Anderson Base (381); Unit 4 Dev (236); Unit 1 Dev (194); Unit 4 Dev - Dungeon (90); Unit 3 Dungeon Dev (76); Unit 5 Dev - Dungeon (34)
- **eventKey:** present on 1775 of 2539 records
- **Intervals:** median 1.30s (p5 0.01s / p95 28.72s, n=2538)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1775; [conversationId, dialogueEventType] x764
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2539/2539 records)
    numeric range 8 .. 114 (50 unique)
data.dialogueEventType  (string, 2539/2539 records)
    "DialogueNodeEvent"  x1775
    "DialogueStartEvent"  x488
    "DialogueFinishEvent"  x276
data.nodeId  (number, 1775/2539 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 632 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (192); Unit 3 Dev (120); Unit 4 Dev - Anderson Base (74); Unit 1 Dev (59); Unit 4 Dev - Dungeon (41); Unit 3 Dungeon Dev (39); Unit 5 Dev (36); Unit 5 Dev - Dungeon (36); Unit 4 Dev (35)
- **Intervals:** median 30.01s (p5 29.97s / p95 40.52s, n=620)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 632/632 records)
data.position.x  (number, 632/632 records)
    numeric range -666.621 .. 1644.89 (346 unique)
data.position.y  (number, 632/632 records)
    numeric range -112.489 .. 225.704 (270 unique)
data.position.z  (number, 632/632 records)
    numeric range -1141.47 .. 2286.97 (346 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `WaterChamberEvent` — 130 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (130)
- **Intervals:** median 2.10s (p5 0.07s / p95 30.78s, n=129)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 130/130 records)
    "On"  x68
    "Off"  x62
data.floor  (string, 130/130 records)
    "4"  x79
    "1"  x26
    "2"  x13
    "3"  x12
data.machineNumber  (string, 130/130 records)
    "One"  x129
    "Two"  x1
data.machineType  (string, 130/130 records)
    "Condenser"  x81
    "Evaporator"  x42
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 130/130 records)
    "3"  x62
    "2"  x46
    "1"  x18
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `questEvent` — 91 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 5 Dev (19); Unit 3 Dev (16); Unit 2 Prod (Refactor) (13); Unit 1 Dev (12); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 91 of 91 records
- **Intervals:** median 109.17s (p5 0.01s / p95 37767.92s, n=90)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 91/91 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x38
data.questID  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/91 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 44 records

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (22)
- **Intervals:** median 11.33s (p5 0.85s / p95 53622.41s, n=43)
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "MapCloseEvent"  x22
    "MapOpenEvent"  x22
data.featureUsed  (string, 44/44 records)
    "Map"  x44
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 42 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (42)
- **Intervals:** median 1.00s (p5 0.18s / p95 69.68s, n=41)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "ChangeCanister"  x42
data.canisterType  (string, 42/42 records)
    "Bedrock"  x29
    "Clay"  x6
    "Sand"  x4
    "Gravel"  x3
data.floor  (string, 42/42 records)
    "5"  x40
    "3"  x1
    "4"  x1
data.machine  (string, 42/42 records)
    "1"  x37
    "2"  x5
data.row  (string, 42/42 records)
    "BottomRow"  x34
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 41 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (13); Unit 3 Dev (11)
- **Intervals:** median 6.12s (p5 1.02s / p95 1276.16s, n=40)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "argumentationNodeAdd"  x25
    "argumentationNodeRemove"  x16
data.argumentationTitle  (string, 41/41 records)
    "Unit 2 – Watershed"  x17
    "Unit 1 - Freshwater"  x13
    "Unit 3 - Pollution Upstream"  x11
data.nodeName  (string, 41/41 records)
    "A"  x10
    "B"  x9
    "1"  x6
    "I"  x6
    "II"  x5
    "C"  x2
    "D"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 18 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (14); Unit 5 Dev (4)
- **Intervals:** median 1.43s (p5 0.00s / p95 1282.27s, n=17)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationToolClose"  x10
    "argumentationToolOpen"  x8
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x14
    "Unit 5"  x4
data.toolName  (string, 18/18 records)
    "BackingInfoPanel - Soil Layers and Fountain Data"  x8
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Evaporation Flow Diagram"  x3
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (2)
- **Intervals:** median 497.32s (p5 1.21s / p95 324502.88s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionOpen"  x7
    "argumentationSessionClose"  x6
data.argumentationDescription  (string, 13/13 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 4 - Flooding"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TopographicMapEvent` — 8 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2)
- **Intervals:** median 4.46s (p5 1.27s / p95 242152.39s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "dragEnd"  x4
    "dragStart"  x4
data.featureUsed  (string, 8/8 records)
    "waypoint"  x8
data.location  (object, 8/8 records)
data.location.x  (number, 8/8 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 8/8 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 8/8 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `EndOfUnit` — 7 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 5 Dev (3); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 169424.67s (p5 2117.57s / p95 272377.68s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 7/7 records)
    "5"  x3
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 184.34s (p5 20.27s / p95 275598.27s, n=5)
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

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 0.22s (p5 0.14s / p95 11.35s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x6
data.boxId  (string, 6/6 records)
    "2"  x3
    "0"  x2
    "1"  x1
data.soilType  (string, 6/6 records)
    "None"  x6
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

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
- `TerasGardenBox` data.soilType: "None" (6x)
- `TopographicMapEvent` data.actionType: "dragStart" (4x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (16x)
- `soilMachine` data.canisterType: "Bedrock" (29x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*