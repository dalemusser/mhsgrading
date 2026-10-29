# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f783

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f783
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f783.jsonl
- **Records:** 2673 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f783
- **Time span:** 2026-04-14T13:44:18.496000+00:00 .. 2026-04-24T14:08:01.902000+00:00 (240h 23m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f783\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 2673 records, 9 scenes.
- Findings: **0 FAIL**, **45 WARNING**, 67 INFO, 0 NOT_TESTED, 55 PASS.
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
| DialogueEvent | 1977 | 73.96 | 1 | 9 | 1409 | 2026-04-14T13:44:36.549000+00:00 | 2026-04-24T14:07:59.972000+00:00 | 240h 23m |
| PlayerPositionEvent | 417 | 15.6 | 1 | 9 | 0 | 2026-04-14T13:44:18.496000+00:00 | 2026-04-24T14:08:01.902000+00:00 | 240h 23m |
| questEvent | 82 | 3.07 | 1 | 9 | 82 | 2026-04-14T13:44:36.533000+00:00 | 2026-04-24T14:07:56.166000+00:00 | 240h 23m |
| soilMachine | 49 | 1.83 | 1 | 1 | 0 | 2026-04-22T13:45:25.642000+00:00 | 2026-04-22T13:54:01.030000+00:00 | 8m 35s |
| Topographic Map Event | 38 | 1.42 | 1 | 2 | 0 | 2026-04-14T14:20:38.351000+00:00 | 2026-04-22T13:28:04.901000+00:00 | 191h 7m |
| WaterChamberEvent | 37 | 1.38 | 1 | 1 | 0 | 2026-04-22T14:16:59.189000+00:00 | 2026-04-22T14:24:03.432000+00:00 | 7m 4s |
| argumentationNodeEvent | 17 | 0.64 | 1 | 3 | 0 | 2026-04-14T14:02:00.413000+00:00 | 2026-04-21T23:20:31.935000+00:00 | 177h 18m |
| argumentationToolEvent | 16 | 0.6 | 1 | 3 | 0 | 2026-04-16T14:22:29.436000+00:00 | 2026-04-22T14:06:03.129000+00:00 | 143h 43m |
| argumentationEvent | 12 | 0.45 | 1 | 5 | 0 | 2026-04-14T14:01:45.451000+00:00 | 2026-04-22T14:27:05.543000+00:00 | 192h 25m |
| Soil Key Puzzle | 11 | 0.41 | 1 | 3 | 0 | 2026-04-14T14:15:03.962000+00:00 | 2026-04-22T13:37:22.608000+00:00 | 191h 22m |
| TopographicMapEvent | 9 | 0.34 | 1 | 1 | 0 | 2026-04-14T14:20:48.497000+00:00 | 2026-04-16T13:48:36.218000+00:00 | 47h 27m |
| EndOfUnit | 5 | 0.19 | 1 | 5 | 0 | 2026-04-14T14:06:49.964000+00:00 | 2026-04-24T14:03:32.418000+00:00 | 239h 56m |
| TerasGardenBox | 3 | 0.11 | 1 | 1 | 0 | 2026-04-22T14:09:49.341000+00:00 | 2026-04-22T14:10:12.200000+00:00 | 22.9s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.505s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173110.28s median 
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
  - Observed: 96.625s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 11.43s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 54.527s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.266s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 148.893s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 20.86s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.932s median 
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
  - Observed: 2.787s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 417 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 11 records 
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
  - Observed: 38 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 9 records 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` — record volume changed 9.8x vs baseline. 
  - Observed: 49 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 69 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f783.jsonl[906] _id=69de49407957a33870f33c89 ts=2026-04-14T14:03:43.7000000Z`; `69cdc965d385e3b94310f783.jsonl[1069] _id=69de4d0f7957a33870f35807 ts=2026-04-14T14:19:57.9690000Z`; `69cdc965d385e3b94310f783.jsonl[1110] _id=69de4dce7957a33870f35ceb ts=2026-04-14T14:23:09.4010000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 38 records, TopographicMapEvent: 9 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1976 | 0.0 | 1.505 | 437.957 | 25.885 | 462861.054 | 0.14 | 478 | 5 |
| PlayerPositionEvent | 405 | 0.0 | 30.005 | 2136.086 | 36.003 | 462789.136 | 0.03 | 1 | 4 |
| questEvent | 81 | 0.003 | 108.757 | 10683.946 | 1304.882 | 463193.574 | 0.01 | 16 | 7 |
| soilMachine | 48 | 0.117 | 2.787 | 10.737 | 68.747 | 107.531 | 5.59 | 0 | 0 |
| Topographic Map Event | 37 | 0.13 | 14.142 | 18595.853 | 34579.462 | 515644.018 | 0.0 | 0 | 4 |
| WaterChamberEvent | 36 | 0.152 | 4.266 | 11.785 | 49.688 | 97.66 | 5.09 | 0 | 0 |
| argumentationNodeEvent | 16 | 1.272 | 20.86 | 39894.47 | 246433.724 | 464066.386 | 0.0 | 0 | 2 |
| argumentationToolEvent | 15 | 0.002 | 1.932 | 34494.246 | 176334.776 | 464215.616 | 0.0 | 1 | 2 |
| argumentationEvent | 11 | 0.136 | 148.893 | 62974.554 | 318948.708 | 464049.161 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 10 | 2.969 | 96.625 | 68893.865 | 333279.71 | 466383.366 | 0.0 | 0 | 4 |
| TopographicMapEvent | 8 | 1.338 | 54.527 | 21358.465 | 110888.753 | 170527.969 | 0.0 | 0 | 1 |
| EndOfUnit | 4 | 2541.843 | 173110.28 | 215950.614 | 463877.008 | 515040.051 | 0.0 | 0 | 4 |
| TerasGardenBox | 2 | 10.244 | 11.43 | 11.43 | 12.496 | 12.615 | 5.25 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.96s, p95 36.00s, n=405) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `165ms: 69cdc965d385e3b94310f783.jsonl[1261] _id=69e0e7f77957a33870f50d79 ts=2026-04-16T13:45:27.1250000Z ~ 69cdc965d385e3b94310f783.jsonl[1257] _id=69e0e7f87957a33870f50d83 ts=2026-04-16T13:45:27.2900000Z`; `130ms: 69cdc965d385e3b94310f783.jsonl[1257] _id=69e0e7f87957a33870f50d83 ts=2026-04-16T13:45:27.2900000Z ~ 69cdc965d385e3b94310f783.jsonl[1260] _id=69e0e7f87957a33870f50d87 ts=2026-04-16T13:45:27.4200000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `730ms: 69cdc965d385e3b94310f783.jsonl[685] _id=69e8d8a81724f0c9e2fa66eb ts=2026-04-22T14:18:15.0540000Z ~ 69cdc965d385e3b94310f783.jsonl[686] _id=69e8d8a81724f0c9e2fa66f1 ts=2026-04-22T14:18:15.7840000Z`; `378ms: 69cdc965d385e3b94310f783.jsonl[2417] _id=69e8d8a81724f0c9e2fa66ed ts=2026-04-22T14:18:15.5580000Z ~ 69cdc965d385e3b94310f783.jsonl[2436] _id=69e8d8a81724f0c9e2fa66f3 ts=2026-04-22T14:18:15.9360000Z`; `382ms: 69cdc965d385e3b94310f783.jsonl[686] _id=69e8d8a81724f0c9e2fa66f1 ts=2026-04-22T14:18:15.7840000Z ~ 69cdc965d385e3b94310f783.jsonl[2437] _id=69e8d8a81724f0c9e2fa66f5 ts=2026-04-22T14:18:16.1660000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `136ms: 69cdc965d385e3b94310f783.jsonl[1732] _id=69e806481724f0c9e2fa03d9 ts=2026-04-21T23:20:39.2320000Z ~ 69cdc965d385e3b94310f783.jsonl[1733] _id=69e806481724f0c9e2fa03df ts=2026-04-21T23:20:39.3680000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc965d385e3b94310f783.jsonl[594] _id=69e8d4e21724f0c9e2fa4d29 ts=2026-04-22T14:02:09.3330000Z ~ 69cdc965d385e3b94310f783.jsonl[595] _id=69e8d4e21724f0c9e2fa4d2b ts=2026-04-22T14:02:09.3350000Z`; `802ms: 69cdc965d385e3b94310f783.jsonl[2260] _id=69e8d5c41724f0c9e2fa544b ts=2026-04-22T14:05:55.8870000Z ~ 69cdc965d385e3b94310f783.jsonl[606] _id=69e8d5c51724f0c9e2fa5453 ts=2026-04-22T14:05:56.6890000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 69cdc965d385e3b94310f783.jsonl[2536] _id=69e8dadc1724f0c9e2fa724d ts=2026-04-22T14:27:39.6450000Z ~ 69cdc965d385e3b94310f783.jsonl[2537] _id=69e8dadc1724f0c9e2fa724f ts=2026-04-22T14:27:39.6540000Z`; `4ms: 69cdc965d385e3b94310f783.jsonl[2564] _id=69eb76b81724f0c9e2fb7693 ts=2026-04-24T13:57:10.5690000Z ~ 69cdc965d385e3b94310f783.jsonl[711] _id=69eb76b81724f0c9e2fb7695 ts=2026-04-24T13:57:10.5730000Z`; `5ms: 69cdc965d385e3b94310f783.jsonl[2600] _id=69eb77ee1724f0c9e2fb7c3d ts=2026-04-24T14:02:21.9610000Z ~ 69cdc965d385e3b94310f783.jsonl[2606] _id=69eb77ee1724f0c9e2fb7c3f ts=2026-04-24T14:02:21.9660000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `626ms: 69cdc965d385e3b94310f783.jsonl[2053] _id=69e8d0f71724f0c9e2fa3803 ts=2026-04-22T13:45:26.8460000Z ~ 69cdc965d385e3b94310f783.jsonl[2056] _id=69e8d0f81724f0c9e2fa3807 ts=2026-04-22T13:45:27.4720000Z`; `284ms: 69cdc965d385e3b94310f783.jsonl[2056] _id=69e8d0f81724f0c9e2fa3807 ts=2026-04-22T13:45:27.4720000Z ~ 69cdc965d385e3b94310f783.jsonl[2054] _id=69e8d0f81724f0c9e2fa380b ts=2026-04-22T13:45:27.7560000Z`; `117ms: 69cdc965d385e3b94310f783.jsonl[2054] _id=69e8d0f81724f0c9e2fa380b ts=2026-04-22T13:45:27.7560000Z ~ 69cdc965d385e3b94310f783.jsonl[2058] _id=69e8d0f81724f0c9e2fa380f ts=2026-04-22T13:45:27.8730000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 128h 34m 
  - Evidence: 128h 34m: 69cdc965d385e3b94310f783.jsonl[1702] _id=69e0f3aa7957a33870f558df ts=2026-04-16T14:35:21.8540000Z -> 69cdc965d385e3b94310f783.jsonl[1708] _id=69e803b71724f0c9e2fa02d1 ts=2026-04-21T23:09:42.9080000Z; 47h 29m: 69cdc965d385e3b94310f783.jsonl[2557] _id=69e8db051724f0c9e2fa739f ts=2026-04-22T14:28:21.0330000Z -> 69cdc965d385e3b94310f783.jsonl[712] _id=69eb76c91724f0c9e2fb76a5 ts=2026-04-24T13:57:29.6730000Z; 47h 2m: 69cdc965d385e3b94310f783.jsonl[1133] _id=69de4fc27957a33870f36a98 ts=2026-04-14T14:31:28.9790000Z -> 69cdc965d385e3b94310f783.jsonl[1135] _id=69e0e54b7957a33870f4f9eb ts=2026-04-16T13:34:02.9040000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 478 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f783.jsonl[1625] _id=69e0f17b7957a33870f5459b ts=2026-04-16T14:26:03.0770000Z -> 69cdc965d385e3b94310f783.jsonl[1627] _id=69e0f18f7957a33870f54657 ts=2026-04-16T14:26:03.077Z; 0ms: 69cdc965d385e3b94310f783.jsonl[1937] _id=69e8cd5b1724f0c9e2fa1d03 ts=2026-04-22T13:30:03.1350000Z -> 69cdc965d385e3b94310f783.jsonl[1941] _id=69e8cd691724f0c9e2fa1d61 ts=2026-04-22T13:30:03.135Z; 0ms: 69cdc965d385e3b94310f783.jsonl[2388] _id=69e8d7491724f0c9e2fa6031 ts=2026-04-22T14:12:24.9780000Z -> 69cdc965d385e3b94310f783.jsonl[2392] _id=69e8d7581724f0c9e2fa608b ts=2026-04-22T14:12:24.978Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 4m 
  - Evidence: 143h 4m: 69cdc965d385e3b94310f783.jsonl[1626] _id=69e0f17b7957a33870f54595 ts=2026-04-16T14:26:03.0590000Z -> 69cdc965d385e3b94310f783.jsonl[493] _id=69e8cd5b1724f0c9e2fa1d01 ts=2026-04-22T13:30:03.1100000Z; 48h 19m: 69cdc965d385e3b94310f783.jsonl[950] _id=69de49fa7957a33870f341f3 ts=2026-04-14T14:06:49.9640000Z -> 69cdc965d385e3b94310f783.jsonl[1626] _id=69e0f17b7957a33870f54595 ts=2026-04-16T14:26:03.0590000Z; 47h 51m: 69cdc965d385e3b94310f783.jsonl[2391] _id=69e8d7491724f0c9e2fa602f ts=2026-04-22T14:12:24.9530000Z -> 69cdc965d385e3b94310f783.jsonl[755] _id=69eb78341724f0c9e2fb7e03 ts=2026-04-24T14:03:32.4180000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 128h 33m 
  - Evidence: 128h 33m: 69cdc965d385e3b94310f783.jsonl[283] _id=69e0f39a7957a33870f558a7 ts=2026-04-16T14:35:06.0570000Z -> 69cdc965d385e3b94310f783.jsonl[1709] _id=69e803601724f0c9e2fa02c1 ts=2026-04-21T23:08:15.1930000Z; 47h 26m: 69cdc965d385e3b94310f783.jsonl[2561] _id=69e8db7b1724f0c9e2fa7505 ts=2026-04-22T14:30:19.1560000Z -> 69cdc965d385e3b94310f783.jsonl[2565] _id=69eb76b41724f0c9e2fb768f ts=2026-04-24T13:57:07.7400000Z; 47h 2m: 69cdc965d385e3b94310f783.jsonl[133] _id=69de4fad7957a33870f36a1a ts=2026-04-14T14:31:08.8800000Z -> 69cdc965d385e3b94310f783.jsonl[134] _id=69e0e52b7957a33870f4f9bf ts=2026-04-16T13:33:28.1610000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f783.jsonl[422] _id=69e8089d1724f0c9e2fa04cd ts=2026-04-21T23:28:15.2860000Z -> 69cdc965d385e3b94310f783.jsonl[1765] _id=69e8c9df1724f0c9e2fa0a11 ts=2026-04-21T23:28:15.286Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 129h 33m 
  - Evidence: 129h 33m: 69cdc965d385e3b94310f783.jsonl[1321] _id=69e0e9927957a33870f517f5 ts=2026-04-16T13:52:17.9420000Z -> 69cdc965d385e3b94310f783.jsonl[1754] _id=69e808891724f0c9e2fa04a5 ts=2026-04-21T23:25:21.3080000Z; 47h 23m: 69cdc965d385e3b94310f783.jsonl[1017] _id=69de4beb7957a33870f34fa9 ts=2026-04-14T14:15:06.9930000Z -> 69cdc965d385e3b94310f783.jsonl[1179] _id=69e0e6507957a33870f50225 ts=2026-04-16T13:38:24.4560000Z; 14h 8m: 69cdc965d385e3b94310f783.jsonl[1756] _id=69e808981724f0c9e2fa04ad ts=2026-04-21T23:26:06.7540000Z -> 69cdc965d385e3b94310f783.jsonl[1952] _id=69e8ce791724f0c9e2fa2551 ts=2026-04-22T13:34:48.3300000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 14m 
  - Evidence: 143h 14m: 69cdc965d385e3b94310f783.jsonl[1453] _id=69e0ee3a7957a33870f53385 ts=2026-04-16T14:12:09.6800000Z -> 69cdc965d385e3b94310f783.jsonl[1878] _id=69e8cc761724f0c9e2fa1791 ts=2026-04-22T13:26:13.6980000Z; 47h 11m: 69cdc965d385e3b94310f783.jsonl[1130] _id=69de4fa87957a33870f369f0 ts=2026-04-14T14:31:04.0290000Z -> 69cdc965d385e3b94310f783.jsonl[1238] _id=69e0e7577957a33870f509a3 ts=2026-04-16T13:42:47.2340000Z; 12m 28s: 69cdc965d385e3b94310f783.jsonl[1308] _id=69e0e8be7957a33870f51291 ts=2026-04-16T13:48:45.9160000Z -> 69cdc965d385e3b94310f783.jsonl[1355] _id=69e0ebaa7957a33870f52473 ts=2026-04-16T14:01:14.4420000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 22m 
  - Evidence: 47h 22m: 69cdc965d385e3b94310f783.jsonl[1086] _id=69de4d417957a33870f359a5 ts=2026-04-14T14:20:48.4970000Z -> 69cdc965d385e3b94310f783.jsonl[1240] _id=69e0e7607957a33870f509d3 ts=2026-04-16T13:42:56.4660000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 128h 54m 
  - Evidence: 128h 54m: 69cdc965d385e3b94310f783.jsonl[1579] _id=69e0f0ed7957a33870f541db ts=2026-04-16T14:23:40.8270000Z -> 69cdc965d385e3b94310f783.jsonl[363] _id=69e8059e1724f0c9e2fa03ad ts=2026-04-21T23:17:49.9880000Z; 48h 17m: 69cdc965d385e3b94310f783.jsonl[905] _id=69de49407957a33870f33c85 ts=2026-04-14T14:03:43.6800000Z -> 69cdc965d385e3b94310f783.jsonl[1558] _id=69e0f0587957a33870f53ee7 ts=2026-04-16T14:21:11.9340000Z; 14h 41m: 69cdc965d385e3b94310f783.jsonl[1733] _id=69e806481724f0c9e2fa03df ts=2026-04-21T23:20:39.3680000Z -> 69cdc965d385e3b94310f783.jsonl[2221] _id=69e8d4e71724f0c9e2fa4d4d ts=2026-04-22T14:02:15.0310000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 128h 54m 
  - Evidence: 128h 54m: 69cdc965d385e3b94310f783.jsonl[1583] _id=69e0f0e77957a33870f541c9 ts=2026-04-16T14:23:34.8820000Z -> 69cdc965d385e3b94310f783.jsonl[366] _id=69e805aa1724f0c9e2fa03b5 ts=2026-04-21T23:18:01.2680000Z; 48h 18m: 69cdc965d385e3b94310f783.jsonl[902] _id=69de49327957a33870f33c1b ts=2026-04-14T14:03:29.5490000Z -> 69cdc965d385e3b94310f783.jsonl[1560] _id=69e0f0737957a33870f53f57 ts=2026-04-16T14:21:39.0530000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 128h 56m 
  - Evidence: 128h 56m: 69cdc965d385e3b94310f783.jsonl[1570] _id=69e0f0a67957a33870f5405d ts=2026-04-16T14:22:30.6180000Z -> 69cdc965d385e3b94310f783.jsonl[355] _id=69e805ff1724f0c9e2fa03c1 ts=2026-04-21T23:19:26.2340000Z; 14h 42m: 69cdc965d385e3b94310f783.jsonl[357] _id=69e806041724f0c9e2fa03c9 ts=2026-04-21T23:19:32.0600000Z -> 69cdc965d385e3b94310f783.jsonl[594] _id=69e8d4e21724f0c9e2fa4d29 ts=2026-04-22T14:02:09.3330000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f783.jsonl[594] _id=69e8d4e21724f0c9e2fa4d29 ts=2026-04-22T14:02:09.3330000Z -> 69cdc965d385e3b94310f783.jsonl[595] _id=69e8d4e21724f0c9e2fa4d2b ts=2026-04-22T14:02:09.3350000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 128h 39m 
  - Evidence: 128h 39m: 69cdc965d385e3b94310f783.jsonl[1647] _id=69e0f2087957a33870f54a23 ts=2026-04-16T14:28:24.4960000Z -> 69cdc965d385e3b94310f783.jsonl[1710] _id=69e803631724f0c9e2fa02c3 ts=2026-04-21T23:08:18.0700000Z; 47h 29m: 69cdc965d385e3b94310f783.jsonl[2537] _id=69e8dadc1724f0c9e2fa724f ts=2026-04-22T14:27:39.6540000Z -> 69cdc965d385e3b94310f783.jsonl[2564] _id=69eb76b81724f0c9e2fb7693 ts=2026-04-24T13:57:10.5690000Z; 47h 13m: 69cdc965d385e3b94310f783.jsonl[1078] _id=69de4d347957a33870f358fb ts=2026-04-14T14:20:36.0410000Z -> 69cdc965d385e3b94310f783.jsonl[1141] _id=69e0e5667957a33870f4fb0b ts=2026-04-16T13:34:29.8870000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f783.jsonl[871] _id=69de48a77957a33870f337d9 ts=2026-04-14T14:01:10.2510000Z -> 69cdc965d385e3b94310f783.jsonl[873] _id=69de48a77957a33870f337db ts=2026-04-14T14:01:10.2540000Z; 4ms: 69cdc965d385e3b94310f783.jsonl[2564] _id=69eb76b81724f0c9e2fb7693 ts=2026-04-24T13:57:10.5690000Z -> 69cdc965d385e3b94310f783.jsonl[711] _id=69eb76b81724f0c9e2fb7695 ts=2026-04-24T13:57:10.5730000Z; 5ms: 69cdc965d385e3b94310f783.jsonl[2600] _id=69eb77ee1724f0c9e2fb7c3d ts=2026-04-24T14:02:21.9610000Z -> 69cdc965d385e3b94310f783.jsonl[2606] _id=69eb77ee1724f0c9e2fb7c3f ts=2026-04-24T14:02:21.9660000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc965d385e3b94310f783.jsonl:69cdc965d385e3b94310f783, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1017] _id=69de4beb7957a33870f34fa9 ts=2026-04-14T14:15:06.9930000Z`; `69cdc965d385e3b94310f783.jsonl[1178] _id=69e0e6537957a33870f50239 ts=2026-04-16T13:38:27.4250000Z`; `69cdc965d385e3b94310f783.jsonl[1321] _id=69e0e9927957a33870f517f5 ts=2026-04-16T13:52:17.9420000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 9 record(s) match the trigger in 69cdc965d385e3b94310f783.jsonl:69cdc965d385e3b94310f783, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1086] _id=69de4d417957a33870f359a5 ts=2026-04-14T14:20:48.4970000Z`; `69cdc965d385e3b94310f783.jsonl[1240] _id=69e0e7607957a33870f509d3 ts=2026-04-16T13:42:56.4660000Z`; `69cdc965d385e3b94310f783.jsonl[1201] _id=69e0e7627957a33870f509d7 ts=2026-04-16T13:42:57.8040000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1439] _id=69e0ede87957a33870f531a5 ts=2026-04-16T14:10:47.9070000Z`; `69cdc965d385e3b94310f783.jsonl[302] _id=69e803dd1724f0c9e2fa0301 ts=2026-04-21T23:10:20.8280000Z`; `69cdc965d385e3b94310f783.jsonl[1753] _id=69e808761724f0c9e2fa04a3 ts=2026-04-21T23:25:13.5220000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Finished' preceded by 'Started' per Unit 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1754] _id=69e808891724f0c9e2fa04a5 ts=2026-04-21T23:25:21.3080000Z`; `69cdc965d385e3b94310f783.jsonl[1756] _id=69e808981724f0c9e2fa04ad ts=2026-04-21T23:26:06.7540000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1733] _id=69e806481724f0c9e2fa03df ts=2026-04-21T23:20:39.3680000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f783.jsonl[356] _id=69e806001724f0c9e2fa03c3 ts=2026-04-21T23:19:27.9310000Z`; `69cdc965d385e3b94310f783.jsonl[594] _id=69e8d4e21724f0c9e2fa4d29 ts=2026-04-22T14:02:09.3330000Z`; `69cdc965d385e3b94310f783.jsonl[595] _id=69e8d4e21724f0c9e2fa4d2b ts=2026-04-22T14:02:09.3350000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1372] _id=69e0ec707957a33870f527b7 ts=2026-04-16T14:04:31.3310000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f783.jsonl[1981] _id=69e8ceff1724f0c9e2fa28b3 ts=2026-04-22T13:37:03.0570000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 194 unmatched 'DialogueStartEvent' (totals: 379 start, 189 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 7 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 47 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 1 of 2672 adjacent _id pairs reverse in client time; worst 28.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `69cdc965d385e3b94310f783.jsonl[422] _id=69e8089d1724f0c9e2fa04cd ts=2026-04-21T23:28:15.2860000Z`; `69cdc965d385e3b94310f783.jsonl[1764] _id=69e8c9df1724f0c9e2fa0a0f ts=2026-04-21T23:27:46.621Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.65s, min -49644.95s, max -0.22s over 2673 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f783\coverage.yaml

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
  - Observed: 38 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1977 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (644); Unit 3 Dev (301); Unit 5 Dev (232); Unit 4 Dev (228); Unit 1 Dev (204); Unit 4 Dev - Anderson Base (132); Unit 3 Dungeon Dev (111); Unit 4 Dev - Dungeon (90); Unit 5 Dev - Dungeon (35)
- **eventKey:** present on 1409 of 1977 records
- **Intervals:** median 1.50s (p5 0.01s / p95 25.89s, n=1976)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1409; [conversationId, dialogueEventType] x568
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1977/1977 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 1977/1977 records)
    "DialogueNodeEvent"  x1409
    "DialogueStartEvent"  x379
    "DialogueFinishEvent"  x189
data.nodeId  (number, 1409/1977 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 417 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (139); Unit 3 Dev (63); Unit 1 Dev (45); Unit 4 Dev (35); Unit 5 Dev (33); Unit 3 Dungeon Dev (30); Unit 4 Dev - Dungeon (30); Unit 5 Dev - Dungeon (23); Unit 4 Dev - Anderson Base (19)
- **Intervals:** median 30.00s (p5 29.96s / p95 36.00s, n=405)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 417/417 records)
data.position.x  (number, 417/417 records)
    numeric range -696.453 .. 1557.89 (265 unique)
data.position.y  (number, 417/417 records)
    numeric range -114.672 .. 222.404 (217 unique)
data.position.z  (number, 417/417 records)
    numeric range -1108.48 .. 2029.46 (265 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 5 Dev (13); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 108.76s (p5 0.01s / p95 1304.88s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x35
data.questID  (string, 82/82 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/82 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 49 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (49)
- **Intervals:** median 2.79s (p5 0.32s / p95 68.75s, n=48)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "ChangeCanister"  x49
data.canisterType  (string, 49/49 records)
    "Clay"  x21
    "Bedrock"  x15
    "Sand"  x9
    "Gravel"  x4
data.floor  (string, 49/49 records)
    "5"  x35
    "3"  x11
    "4"  x3
data.machine  (string, 49/49 records)
    "1"  x48
    "2"  x1
data.row  (string, 49/49 records)
    "TopRow"  x26
    "BottomRow"  x23
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Topographic Map Event` — 38 records

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (14)
- **Intervals:** median 14.14s (p5 1.21s / p95 34579.46s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x18
data.featureUsed  (string, 38/38 records)
    "Map"  x38
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 37 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (37)
- **Intervals:** median 4.27s (p5 0.21s / p95 49.69s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "On"  x24
    "Off"  x13
data.floor  (string, 37/37 records)
    "2"  x15
    "4"  x9
    "3"  x8
    "1"  x5
data.machineNumber  (string, 37/37 records)
    "One"  x36
    "Two"  x1
data.machineType  (string, 37/37 records)
    "Condenser"  x26
    "Evaporator"  x6
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 37/37 records)
    "1"  x16
    "3"  x11
    "2"  x8
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationNodeEvent` — 17 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (7); Unit 3 Dev (3)
- **Intervals:** median 20.86s (p5 1.31s / p95 246433.72s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 17/17 records)
    "Unit 2 – Watershed"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 17/17 records)
    "A"  x5
    "I"  x4
    "1"  x3
    "D"  x2
    "5"  x1
    "B"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (10); Unit 3 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.93s (p5 0.04s / p95 176334.78s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolClose"  x9
    "argumentationToolOpen"  x7
data.argumentationTitle  (string, 16/16 records)
    "Unit 4 - Flooding"  x10
    "Unit 3 - Pollution Upstream"  x4
    "Unit 2 – Watershed"  x2
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 148.89s (p5 11.43s / p95 318948.71s, n=11)
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

### `Soil Key Puzzle` — 11 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev (3); Unit 3 Dev (2)
- **Intervals:** median 96.62s (p5 3.00s / p95 333279.71s, n=10)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/11 records)
    "Finished"  x6
    "Started"  x5
data.Unit  (string, 11/11 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 4 Dev"  x3
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 9 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (9)
- **Intervals:** median 54.53s (p5 1.42s / p95 110888.75s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "dragStart"  x5
    "dragEnd"  x4
data.featureUsed  (string, 9/9 records)
    "waypoint"  x9
data.location  (object, 9/9 records)
data.location.x  (number, 9/9 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 9/9 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 9/9 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 173110.28s (p5 28000.69s / p95 463877.01s, n=4)
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
- **Intervals:** median 11.43s (p5 10.36s / p95 12.50s, n=2)
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "dragStart" (5x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (15x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*