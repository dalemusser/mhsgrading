# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f784

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f784
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f784.jsonl
- **Records:** 2754 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f784
- **Time span:** 2026-04-14T13:54:30.582000+00:00 .. 2026-04-24T14:08:04.234000+00:00 (240h 13m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f784\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2754 records, 9 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 60 INFO, 0 NOT_TESTED, 56 PASS.
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
| DialogueEvent | 1960 | 71.17 | 1 | 9 | 1387 | 2026-04-14T13:54:49.153000+00:00 | 2026-04-24T14:07:31.100000+00:00 | 240h 12m |
| PlayerPositionEvent | 486 | 17.65 | 1 | 9 | 0 | 2026-04-14T13:54:30.582000+00:00 | 2026-04-24T14:08:04.234000+00:00 | 240h 13m |
| questEvent | 79 | 2.87 | 1 | 9 | 79 | 2026-04-14T13:54:49.123000+00:00 | 2026-04-24T14:04:20.170000+00:00 | 240h 9m |
| Topographic Map Event | 76 | 2.76 | 1 | 2 | 0 | 2026-04-16T13:55:13.500000+00:00 | 2026-04-22T13:30:39.101000+00:00 | 143h 35m |
| WaterChamberEvent | 45 | 1.63 | 1 | 1 | 0 | 2026-04-22T14:17:04.023000+00:00 | 2026-04-22T14:22:53.582000+00:00 | 5m 49s |
| argumentationNodeEvent | 27 | 0.98 | 1 | 3 | 0 | 2026-04-14T14:13:24.129000+00:00 | 2026-04-20T14:05:52.762000+00:00 | 143h 52m |
| argumentationToolEvent | 26 | 0.94 | 1 | 3 | 0 | 2026-04-20T13:33:39.156000+00:00 | 2026-04-22T14:06:12.125000+00:00 | 48h 32m |
| TopographicMapEvent | 20 | 0.73 | 1 | 1 | 0 | 2026-04-16T13:56:23.006000+00:00 | 2026-04-16T14:13:54.843000+00:00 | 17m 31s |
| argumentationEvent | 12 | 0.44 | 1 | 5 | 0 | 2026-04-14T14:13:14.983000+00:00 | 2026-04-22T14:27:30.326000+00:00 | 192h 14m |
| soilMachine | 9 | 0.33 | 1 | 1 | 0 | 2026-04-22T13:49:09.332000+00:00 | 2026-04-22T13:57:44.439000+00:00 | 8m 35s |
| Soil Key Puzzle | 6 | 0.22 | 1 | 3 | 0 | 2026-04-16T14:16:26.582000+00:00 | 2026-04-22T13:38:16.370000+00:00 | 143h 21m |
| EndOfUnit | 5 | 0.18 | 1 | 5 | 0 | 2026-04-14T14:22:40.214000+00:00 | 2026-04-24T14:04:12.556000+00:00 | 239h 41m |
| TerasGardenBox | 3 | 0.11 | 1 | 1 | 0 | 2026-04-22T14:09:56.262000+00:00 | 2026-04-22T14:10:44.327000+00:00 | 48.1s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.737s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172393.203s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.01s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 118.484s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 24.032s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.731s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.741s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.632s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.449s median 
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
  - Observed: 19.212s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
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
  - Observed: 76 records this build 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 27 records 
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
  - Observed: 2; 3; 4; D 
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
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 19 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f784.jsonl[613] _id=69de4be37957a33870f34f6b ts=2026-04-14T14:14:58.9120000Z`; `69cdc965d385e3b94310f784.jsonl[38] _id=69e0e5ec7957a33870f50019 ts=2026-04-16T13:36:43.5110000Z`; `69cdc965d385e3b94310f784.jsonl[65] _id=69e0e9d37957a33870f519c3 ts=2026-04-16T13:53:22.0540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 76 records, TopographicMapEvent: 20 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1959 | 0.0 | 1.737 | 441.43 | 30.661 | 341087.747 | 0.14 | 483 | 4 |
| PlayerPositionEvent | 474 | 18.767 | 30.01 | 1823.795 | 42.666 | 341034.243 | 0.03 | 0 | 4 |
| questEvent | 78 | 0.002 | 112.275 | 11084.244 | 26525.558 | 341408.549 | 0.01 | 15 | 7 |
| Topographic Map Event | 75 | 2.339 | 12.061 | 6892.341 | 179.26 | 342545.068 | 0.01 | 0 | 3 |
| WaterChamberEvent | 44 | 0.099 | 4.741 | 7.945 | 25.602 | 72.106 | 7.55 | 0 | 0 |
| argumentationNodeEvent | 26 | 1.083 | 6.632 | 19921.101 | 1344.808 | 515876.44 | 0.0 | 0 | 2 |
| argumentationToolEvent | 25 | 0.002 | 7.449 | 6990.119 | 1415.522 | 172809.549 | 0.01 | 3 | 2 |
| TopographicMapEvent | 19 | 0.218 | 6.731 | 55.36 | 255.044 | 277.464 | 1.08 | 0 | 0 |
| argumentationEvent | 11 | 0.155 | 105.833 | 62914.122 | 344318.673 | 515841.392 | 0.0 | 0 | 4 |
| soilMachine | 8 | 1.313 | 19.212 | 64.388 | 240.092 | 326.746 | 0.93 | 0 | 0 |
| Soil Key Puzzle | 5 | 21.118 | 118.484 | 103221.958 | 310217.275 | 345046.707 | 0.0 | 0 | 2 |
| EndOfUnit | 4 | 2371.412 | 172393.203 | 215723.086 | 464249.462 | 515734.525 | 0.0 | 0 | 4 |
| TerasGardenBox | 2 | 18.039 | 24.032 | 24.032 | 29.427 | 30.026 | 2.5 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.010s (p5 29.96s, p95 42.67s, n=474) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `661ms: 69cdc965d385e3b94310f784.jsonl[365] _id=69e8d9141724f0c9e2fa694b ts=2026-04-22T14:20:04.4100000Z ~ 69cdc965d385e3b94310f784.jsonl[2546] _id=69e8d9151724f0c9e2fa6957 ts=2026-04-22T14:20:05.0710000Z`; `417ms: 69cdc965d385e3b94310f784.jsonl[2410] _id=69e8d9151724f0c9e2fa6953 ts=2026-04-22T14:20:04.8330000Z ~ 69cdc965d385e3b94310f784.jsonl[2547] _id=69e8d9151724f0c9e2fa695b ts=2026-04-22T14:20:05.2500000Z`; `875ms: 69cdc965d385e3b94310f784.jsonl[2543] _id=69e8d9201724f0c9e2fa6983 ts=2026-04-22T14:20:15.6140000Z ~ 69cdc965d385e3b94310f784.jsonl[2545] _id=69e8d9211724f0c9e2fa6987 ts=2026-04-22T14:20:16.4890000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `155ms: 69cdc965d385e3b94310f784.jsonl[1725] _id=69e632c61724f0c9e2f88be3 ts=2026-04-20T14:05:57.2030000Z ~ 69cdc965d385e3b94310f784.jsonl[1730] _id=69e632c61724f0c9e2f88bef ts=2026-04-20T14:05:57.3580000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc965d385e3b94310f784.jsonl[2328] _id=69e8d5be1724f0c9e2fa5411 ts=2026-04-22T14:05:49.5090000Z ~ 69cdc965d385e3b94310f784.jsonl[2333] _id=69e8d5be1724f0c9e2fa5413 ts=2026-04-22T14:05:49.5110000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 69cdc965d385e3b94310f784.jsonl[2629] _id=69e8dade1724f0c9e2fa7265 ts=2026-04-22T14:27:42.3150000Z ~ 69cdc965d385e3b94310f784.jsonl[2627] _id=69e8dadf1724f0c9e2fa726b ts=2026-04-22T14:27:42.3240000Z`; `9ms: 69cdc965d385e3b94310f784.jsonl[2658] _id=69eb77031724f0c9e2fb7751 ts=2026-04-24T13:58:25.6110000Z ~ 69cdc965d385e3b94310f784.jsonl[2655] _id=69eb77041724f0c9e2fb7759 ts=2026-04-24T13:58:25.6200000Z`; `4ms: 69cdc965d385e3b94310f784.jsonl[2689] _id=69eb78181724f0c9e2fb7d27 ts=2026-04-24T14:03:03.4090000Z ~ 69cdc965d385e3b94310f784.jsonl[2690] _id=69eb78181724f0c9e2fb7d29 ts=2026-04-24T14:03:03.4130000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc965d385e3b94310f784.jsonl[1265] _id=69e0f3957957a33870f5588f ts=2026-04-16T14:35:00.3590000Z -> 69cdc965d385e3b94310f784.jsonl[1272] _id=69e627f51724f0c9e2f84cc9 ts=2026-04-20T13:19:48.1060000Z; 47h 30m: 69cdc965d385e3b94310f784.jsonl[2651] _id=69e8db061724f0c9e2fa73a3 ts=2026-04-22T14:28:21.6550000Z -> 69cdc965d385e3b94310f784.jsonl[2656] _id=69eb770d1724f0c9e2fb7779 ts=2026-04-24T13:58:36.6900000Z; 47h 4m: 69cdc965d385e3b94310f784.jsonl[719] _id=69de4f597957a33870f36754 ts=2026-04-14T14:29:43.8020000Z -> 69cdc965d385e3b94310f784.jsonl[725] _id=69e0e55d7957a33870f4fa95 ts=2026-04-16T13:34:21.0880000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 483 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f784.jsonl[2482] _id=69e8d75f1724f0c9e2fa60cb ts=2026-04-22T14:12:46.9380000Z -> 69cdc965d385e3b94310f784.jsonl[2486] _id=69e8d78c1724f0c9e2fa61d3 ts=2026-04-22T14:12:46.938Z; 0ms: 69cdc965d385e3b94310f784.jsonl[278] _id=69e8ce1c1724f0c9e2fa2293 ts=2026-04-22T13:33:15.5260000Z -> 69cdc965d385e3b94310f784.jsonl[2056] _id=69e8ce2a1724f0c9e2fa22ff ts=2026-04-22T13:33:15.526Z; 2ms: 69cdc965d385e3b94310f784.jsonl[1888] _id=69e8ca8f1724f0c9e2fa0d65 ts=2026-04-22T13:18:06.5180000Z -> 69cdc965d385e3b94310f784.jsonl[1889] _id=69e8ca8f1724f0c9e2fa0d67 ts=2026-04-22T13:18:06.5200000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 15m 
  - Evidence: 143h 15m: 69cdc965d385e3b94310f784.jsonl[669] _id=69de4db17957a33870f35c43 ts=2026-04-14T14:22:40.2140000Z -> 69cdc965d385e3b94310f784.jsonl[1481] _id=69e62c471724f0c9e2f86759 ts=2026-04-20T13:38:14.7390000Z; 47h 55m: 69cdc965d385e3b94310f784.jsonl[1481] _id=69e62c471724f0c9e2f86759 ts=2026-04-20T13:38:14.7390000Z -> 69cdc965d385e3b94310f784.jsonl[2054] _id=69e8ce1c1724f0c9e2fa228f ts=2026-04-22T13:33:15.5090000Z; 47h 51m: 69cdc965d385e3b94310f784.jsonl[2476] _id=69e8d75f1724f0c9e2fa60c9 ts=2026-04-22T14:12:46.9210000Z -> 69cdc965d385e3b94310f784.jsonl[2728] _id=69eb785d1724f0c9e2fb7f33 ts=2026-04-24T14:04:12.5560000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f784.jsonl[1267] _id=69e0f3b07957a33870f558f1 ts=2026-04-16T14:35:27.6550000Z -> 69cdc965d385e3b94310f784.jsonl[1269] _id=69e627db1724f0c9e2f84c25 ts=2026-04-20T13:19:21.8980000Z; 47h 28m: 69cdc965d385e3b94310f784.jsonl[2654] _id=69e8db7c1724f0c9e2fa7509 ts=2026-04-22T14:30:20.4520000Z -> 69cdc965d385e3b94310f784.jsonl[387] _id=69eb76ff1724f0c9e2fb7743 ts=2026-04-24T13:58:22.3790000Z; 47h 2m: 69cdc965d385e3b94310f784.jsonl[34] _id=69de4fbe7957a33870f36a84 ts=2026-04-14T14:31:25.4290000Z -> 69cdc965d385e3b94310f784.jsonl[723] _id=69e0e55a7957a33870f4fa61 ts=2026-04-16T13:34:16.9290000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc965d385e3b94310f784.jsonl[1070] _id=69e0efb17957a33870f53c13 ts=2026-04-16T14:18:25.0660000Z -> 69cdc965d385e3b94310f784.jsonl[1771] _id=69e633881724f0c9e2f89055 ts=2026-04-20T14:09:11.7730000Z; 47h 28m: 69cdc965d385e3b94310f784.jsonl[1757] _id=69e633a01724f0c9e2f890cd ts=2026-04-20T14:09:35.7050000Z -> 69cdc965d385e3b94310f784.jsonl[2074] _id=69e8cf331724f0c9e2fa29ff ts=2026-04-22T13:37:55.2520000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 9m 
  - Evidence: 95h 9m: 69cdc965d385e3b94310f784.jsonl[1219] _id=69e0f2e57957a33870f55239 ts=2026-04-16T14:32:05.1680000Z -> 69cdc965d385e3b94310f784.jsonl[1504] _id=69e62cf71724f0c9e2f86c87 ts=2026-04-20T13:41:10.2360000Z; 47h 45m: 69cdc965d385e3b94310f784.jsonl[1531] _id=69e62d7e1724f0c9e2f86ef1 ts=2026-04-20T13:43:25.3570000Z -> 69cdc965d385e3b94310f784.jsonl[1990] _id=69e8cd091724f0c9e2fa1b2f ts=2026-04-22T13:28:41.1960000Z; 10m 58s: 69cdc965d385e3b94310f784.jsonl[1090] _id=69e0f0477957a33870f53e97 ts=2026-04-16T14:20:54.4380000Z -> 69cdc965d385e3b94310f784.jsonl[133] _id=69e0f2d97957a33870f551d9 ts=2026-04-16T14:31:53.1070000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 17m 
  - Evidence: 143h 17m: 69cdc965d385e3b94310f784.jsonl[605] _id=69de4be37957a33870f34f67 ts=2026-04-14T14:14:58.8810000Z -> 69cdc965d385e3b94310f784.jsonl[1378] _id=69e62ae51724f0c9e2f85ca3 ts=2026-04-20T13:32:20.2730000Z; 47h 59m: 69cdc965d385e3b94310f784.jsonl[1730] _id=69e632c61724f0c9e2f88bef ts=2026-04-20T14:05:57.3580000Z -> 69cdc965d385e3b94310f784.jsonl[2330] _id=69e8d5c11724f0c9e2fa542b ts=2026-04-22T14:05:53.3120000Z; 29m 14s: 69cdc965d385e3b94310f784.jsonl[1420] _id=69e62b811724f0c9e2f861bf ts=2026-04-20T13:34:56.8060000Z -> 69cdc965d385e3b94310f784.jsonl[199] _id=69e6325c1724f0c9e2f88989 ts=2026-04-20T14:04:11.3700000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 17m 
  - Evidence: 143h 17m: 69cdc965d385e3b94310f784.jsonl[612] _id=69de4bdf7957a33870f34f5b ts=2026-04-14T14:14:54.7760000Z -> 69cdc965d385e3b94310f784.jsonl[1385] _id=69e62b041724f0c9e2f85da7 ts=2026-04-20T13:32:51.2160000Z; 29m 35s: 69cdc965d385e3b94310f784.jsonl[1422] _id=69e62b801724f0c9e2f861b2 ts=2026-04-20T13:34:55.1300000Z -> 69cdc965d385e3b94310f784.jsonl[1714] _id=69e6326f1724f0c9e2f88a01 ts=2026-04-20T14:04:30.5980000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 48h 0m 
  - Evidence: 48h 0m: 69cdc965d385e3b94310f784.jsonl[1710] _id=69e632b41724f0c9e2f88b77 ts=2026-04-20T14:05:39.9600000Z -> 69cdc965d385e3b94310f784.jsonl[2328] _id=69e8d5be1724f0c9e2fa5411 ts=2026-04-22T14:05:49.5090000Z; 29m 19s: 69cdc965d385e3b94310f784.jsonl[1418] _id=69e62b7e1724f0c9e2f861a5 ts=2026-04-20T13:34:53.5280000Z -> 69cdc965d385e3b94310f784.jsonl[1709] _id=69e6325e1724f0c9e2f88997 ts=2026-04-20T14:04:13.2590000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.024s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f784.jsonl[2328] _id=69e8d5be1724f0c9e2fa5411 ts=2026-04-22T14:05:49.5090000Z -> 69cdc965d385e3b94310f784.jsonl[2333] _id=69e8d5be1724f0c9e2fa5413 ts=2026-04-22T14:05:49.5110000Z; 8ms: 69cdc965d385e3b94310f784.jsonl[1713] _id=69e632681724f0c9e2f889cb ts=2026-04-20T14:04:23.0520000Z -> 69cdc965d385e3b94310f784.jsonl[198] _id=69e632681724f0c9e2f889cd ts=2026-04-20T14:04:23.0600000Z; 24ms: 69cdc965d385e3b94310f784.jsonl[1404] _id=69e62b361724f0c9e2f85f45 ts=2026-04-20T13:33:41.9790000Z -> 69cdc965d385e3b94310f784.jsonl[1405] _id=69e62b371724f0c9e2f85f47 ts=2026-04-20T13:33:42.0030000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 50m 
  - Evidence: 94h 50m: 69cdc965d385e3b94310f784.jsonl[1170] _id=69e0f23c7957a33870f54c13 ts=2026-04-16T14:29:16.1810000Z -> 69cdc965d385e3b94310f784.jsonl[1268] _id=69e627de1724f0c9e2f84c2f ts=2026-04-20T13:19:24.7300000Z; 47h 30m: 69cdc965d385e3b94310f784.jsonl[2627] _id=69e8dadf1724f0c9e2fa726b ts=2026-04-22T14:27:42.3240000Z -> 69cdc965d385e3b94310f784.jsonl[2658] _id=69eb77031724f0c9e2fb7751 ts=2026-04-24T13:58:25.6110000Z; 47h 9m: 69cdc965d385e3b94310f784.jsonl[681] _id=69de4e167957a33870f35eb0 ts=2026-04-14T14:24:22.0290000Z -> 69cdc965d385e3b94310f784.jsonl[724] _id=69e0e55c7957a33870f4fa8d ts=2026-04-16T13:34:19.6400000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f784.jsonl[2727] _id=69eb78651724f0c9e2fb7f6d ts=2026-04-24T14:04:20.1680000Z -> 69cdc965d385e3b94310f784.jsonl[2671] _id=69eb78651724f0c9e2fb7f71 ts=2026-04-24T14:04:20.1700000Z; 3ms: 69cdc965d385e3b94310f784.jsonl[573] _id=69de4b617957a33870f34b8f ts=2026-04-14T14:12:48.0350000Z -> 69cdc965d385e3b94310f784.jsonl[571] _id=69de4b617957a33870f34b91 ts=2026-04-14T14:12:48.0380000Z; 4ms: 69cdc965d385e3b94310f784.jsonl[2689] _id=69eb78181724f0c9e2fb7d27 ts=2026-04-24T14:03:03.4090000Z -> 69cdc965d385e3b94310f784.jsonl[2690] _id=69eb78181724f0c9e2fb7d29 ts=2026-04-24T14:03:03.4130000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc965d385e3b94310f784.jsonl:69cdc965d385e3b94310f784, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f784.jsonl[1070] _id=69e0efb17957a33870f53c13 ts=2026-04-16T14:18:25.0660000Z`; `69cdc965d385e3b94310f784.jsonl[1757] _id=69e633a01724f0c9e2f890cd ts=2026-04-20T14:09:35.7050000Z`; `69cdc965d385e3b94310f784.jsonl[2076] _id=69e8cf481724f0c9e2fa2a7b ts=2026-04-22T13:38:16.3700000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 20 record(s) match the trigger in 69cdc965d385e3b94310f784.jsonl:69cdc965d385e3b94310f784, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f784.jsonl[914] _id=69e0ea877957a33870f51ebb ts=2026-04-16T13:56:23.0060000Z`; `69cdc965d385e3b94310f784.jsonl[915] _id=69e0ea8a7957a33870f51ed1 ts=2026-04-16T13:56:25.9350000Z`; `69cdc965d385e3b94310f784.jsonl[921] _id=69e0eab07957a33870f51f9d ts=2026-04-16T13:57:03.5970000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f784.jsonl[1185] _id=69e0f2577957a33870f54cff ts=2026-04-16T14:29:42.5670000Z`; `69cdc965d385e3b94310f784.jsonl[1552] _id=69e62e1b1724f0c9e2f87197 ts=2026-04-20T13:46:02.7180000Z`; `69cdc965d385e3b94310f784.jsonl[1567] _id=69e62e5c1724f0c9e2f872fb ts=2026-04-20T13:47:07.9680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f784.jsonl[1730] _id=69e632c61724f0c9e2f88bef ts=2026-04-20T14:05:57.3580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f784.jsonl[1713] _id=69e632681724f0c9e2f889cb ts=2026-04-20T14:04:23.0520000Z`; `69cdc965d385e3b94310f784.jsonl[2328] _id=69e8d5be1724f0c9e2fa5411 ts=2026-04-22T14:05:49.5090000Z`; `69cdc965d385e3b94310f784.jsonl[2333] _id=69e8d5be1724f0c9e2fa5413 ts=2026-04-22T14:05:49.5110000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 200 unmatched 'DialogueStartEvent' (totals: 384 start, 189 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 12 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 47 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.85s, min -45.37s, max -0.50s over 2754 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f784\coverage.yaml

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
  - Observed: 76 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1960 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (676); Unit 3 Dev (341); Unit 4 Dev (226); Unit 5 Dev (200); Unit 1 Dev (178); Unit 3 Dungeon Dev (150); Unit 4 Dev - Dungeon (92); Unit 4 Dev - Anderson Base (67); Unit 5 Dev - Dungeon (30)
- **eventKey:** present on 1387 of 1960 records
- **Intervals:** median 1.74s (p5 0.01s / p95 30.66s, n=1959)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1387; [conversationId, dialogueEventType] x573
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1960/1960 records)
    numeric range 8 .. 114 (50 unique)
data.dialogueEventType  (string, 1960/1960 records)
    "DialogueNodeEvent"  x1387
    "DialogueStartEvent"  x384
    "DialogueFinishEvent"  x189
data.nodeId  (number, 1387/1960 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 486 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (161); Unit 3 Dev (73); Unit 3 Dungeon Dev (64); Unit 1 Dev (56); Unit 4 Dev - Dungeon (34); Unit 5 Dev (34); Unit 4 Dev (33); Unit 5 Dev - Dungeon (19); Unit 4 Dev - Anderson Base (12)
- **Intervals:** median 30.01s (p5 29.96s / p95 42.67s, n=474)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 486/486 records)
data.position.x  (number, 486/486 records)
    numeric range -690.33 .. 1591.97 (300 unique)
data.position.y  (number, 486/486 records)
    numeric range -114.326 .. 217.859 (240 unique)
data.position.z  (number, 486/486 records)
    numeric range -1109.4 .. 2119.55 (300 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 79 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 5 Dev (11); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 79 of 79 records
- **Intervals:** median 112.28s (p5 0.01s / p95 26525.56s, n=78)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Fields under `data`:**

```text
data.questEventType  (string, 79/79 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x32
data.questID  (string, 79/79 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 79/79 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/79 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 76 records

- **Scenes:** Unit 2 Prod (Refactor) (56); Unit 3 Dev (20)
- **Intervals:** median 12.06s (p5 2.53s / p95 179.26s, n=75)
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapCloseEvent"  x38
    "MapOpenEvent"  x38
data.featureUsed  (string, 76/76 records)
    "Map"  x76
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 45 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (45)
- **Intervals:** median 4.74s (p5 0.20s / p95 25.60s, n=44)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "On"  x29
    "Off"  x16
data.floor  (string, 45/45 records)
    "3"  x28
    "4"  x10
    "1"  x4
    "2"  x3
data.machineNumber  (string, 45/45 records)
    "One"  x44
    "Two"  x1
data.machineType  (string, 45/45 records)
    "Condenser"  x29
    "Evaporator"  x7
    "VentSwitch"  x4
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
data.room  (string, 45/45 records)
    "2"  x26
    "3"  x11
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 27 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (9); Unit 3 Dev (5)
- **Intervals:** median 6.63s (p5 1.54s / p95 1344.81s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "argumentationNodeAdd"  x19
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 27/27 records)
    "Unit 2 – Watershed"  x13
    "Unit 1 - Freshwater"  x7
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 27/27 records)
    "I"  x8
    "1"  x7
    "A"  x3
    "B"  x3
    "II"  x3
    "C"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 26 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (8); Unit 4 Dev - Anderson Base (6)
- **Intervals:** median 7.45s (p5 0.01s / p95 1415.52s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "argumentationToolClose"  x14
    "argumentationToolOpen"  x12
data.argumentationTitle  (string, 26/26 records)
    "Unit 2 – Watershed"  x12
    "Unit 3 - Pollution Upstream"  x8
    "Unit 4 - Flooding"  x6
data.toolName  (string, 26/26 records)
    "BackingInfoPanel - Waterfall Data"  x8
    "BackingInfoPanel - Pollution Site Data"  x6
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TopographicMapEvent` — 20 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (20)
- **Intervals:** median 6.73s (p5 1.59s / p95 255.04s, n=19)
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
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 20/20 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 20/20 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 105.83s (p5 9.49s / p95 344318.67s, n=11)
- **Open findings:** 1 — see sections 5-8
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

### `soilMachine` — 9 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (9)
- **Intervals:** median 19.21s (p5 2.27s / p95 240.09s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "ChangeCanister"  x9
data.canisterType  (string, 9/9 records)
    "Clay"  x3
    "Sand"  x3
    "Gravel"  x2
    "Bedrock"  x1
data.floor  (string, 9/9 records)
    "5"  x6
    "4"  x3
data.machine  (string, 9/9 records)
    "1"  x7
    "2"  x2
data.row  (string, 9/9 records)
    "TopRow"  x7
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 118.48s (p5 21.68s / p95 310217.27s, n=5)
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 172393.20s (p5 27858.55s / p95 464249.46s, n=4)
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

### `TerasGardenBox` — 3 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (3)
- **Intervals:** median 24.03s (p5 18.64s / p95 29.43s, n=2)
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
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "dragStart" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*