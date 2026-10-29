# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77b
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f77b.jsonl
- **Records:** 2940 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f77b
- **Time span:** 2026-04-14T13:51:09.642000+00:00 .. 2026-04-28T14:32:37.838000+00:00 (336h 41m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 2940 records, 7 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 46 INFO, 2 NOT_TESTED, 37 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2100 | 71.43 | 1 | 7 | 1471 | 2026-04-14T13:51:28.452000+00:00 | 2026-04-28T14:32:37.838000+00:00 | 336h 41m |
| PlayerPositionEvent | 592 | 20.14 | 1 | 7 | 0 | 2026-04-14T13:51:09.642000+00:00 | 2026-04-28T14:32:36.052000+00:00 | 336h 41m |
| questEvent | 94 | 3.2 | 1 | 7 | 94 | 2026-04-14T13:51:28.432000+00:00 | 2026-04-28T14:32:37.653000+00:00 | 336h 41m |
| Topographic Map Event | 42 | 1.43 | 1 | 2 | 0 | 2026-04-16T13:45:06.616000+00:00 | 2026-04-24T14:33:25.496000+00:00 | 192h 48m |
| argumentationNodeEvent | 40 | 1.36 | 1 | 3 | 0 | 2026-04-14T14:10:17.316000+00:00 | 2026-04-22T13:33:56.280000+00:00 | 191h 23m |
| Soil Key Puzzle | 19 | 0.65 | 1 | 3 | 0 | 2026-04-14T14:26:22.484000+00:00 | 2026-04-28T14:14:51.929000+00:00 | 335h 48m |
| argumentationEvent | 17 | 0.58 | 1 | 3 | 0 | 2026-04-14T14:10:09.093000+00:00 | 2026-04-22T13:33:58.428000+00:00 | 191h 23m |
| TopographicMapEvent | 16 | 0.54 | 1 | 2 | 0 | 2026-04-16T13:49:48.363000+00:00 | 2026-04-24T14:32:24.471000+00:00 | 192h 42m |
| soilMachine | 16 | 0.54 | 1 | 1 | 0 | 2026-04-28T14:22:27.961000+00:00 | 2026-04-28T14:26:44.541000+00:00 | 4m 16s |
| EndOfUnit | 4 | 0.14 | 1 | 3 | 0 | 2026-04-14T14:15:02.266000+00:00 | 2026-04-28T14:09:45.748000+00:00 | 335h 54m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 515164.728s median 
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
  - Observed: 240.416s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.146s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.654s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
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
  - Observed: 3.377s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 42 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
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
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 40 records 
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
  - Observed: 2; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 12 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[754] _id=69de4b3b7957a33870f34a73 ts=2026-04-14T14:12:10.8320000Z`; `69cdc965d385e3b94310f77b.jsonl[89] _id=69e0e8817957a33870f510b9 ts=2026-04-16T13:47:44.6810000Z`; `69cdc965d385e3b94310f77b.jsonl[118] _id=69e0f07e7957a33870f53f9d ts=2026-04-16T14:21:50.0940000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 42 records, TopographicMapEvent: 16 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2099 | 0.0 | 2.069 | 577.451 | 33.189 | 343996.015 | 0.1 | 523 | 5 |
| PlayerPositionEvent | 577 | 0.0 | 30.01 | 2099.528 | 33.936 | 343995.329 | 0.03 | 1 | 5 |
| questEvent | 93 | 0.005 | 136.264 | 13033.002 | 68130.333 | 344030.01 | 0.0 | 11 | 11 |
| Topographic Map Event | 41 | 0.691 | 15.965 | 16929.241 | 171529.017 | 343271.164 | 0.0 | 0 | 7 |
| argumentationNodeEvent | 39 | 1.093 | 8.654 | 17667.153 | 170857.376 | 341154.636 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 18 | 2.98 | 240.416 | 67161.636 | 343223.081 | 346067.83 | 0.0 | 0 | 6 |
| argumentationEvent | 16 | 0.103 | 43.438 | 43064.333 | 215748.441 | 341106.477 | 0.0 | 0 | 4 |
| TopographicMapEvent | 15 | 0.589 | 6.146 | 46250.407 | 225899.551 | 344279.583 | 0.0 | 0 | 4 |
| soilMachine | 15 | 1.457 | 3.377 | 17.105 | 76.97 | 93.801 | 3.51 | 0 | 0 |
| EndOfUnit | 3 | 3369.197 | 515164.728 | 403094.494 | 673191.074 | 690749.557 | 0.0 | 0 | 3 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.010s (p5 29.96s, p95 33.94s, n=577) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `103ms: 69cdc965d385e3b94310f77b.jsonl[2165] _id=69e8ce461724f0c9e2fa23eb ts=2026-04-22T13:33:58.3250000Z ~ 69cdc965d385e3b94310f77b.jsonl[337] _id=69e8ce471724f0c9e2fa23f5 ts=2026-04-22T13:33:58.4280000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f77b.jsonl[457] _id=69eb7f8a1724f0c9e2fba341 ts=2026-04-24T14:34:49.6710000Z -> 69cdc965d385e3b94310f77b.jsonl[458] _id=69f0bf461724f0c9e2fca99b ts=2026-04-28T14:08:05.6860000Z; 94h 43m: 69cdc965d385e3b94310f77b.jsonl[1359] _id=69e0f36a7957a33870f5579d ts=2026-04-16T14:34:18.0350000Z -> 69cdc965d385e3b94310f77b.jsonl[1372] _id=69e627721724f0c9e2f84a79 ts=2026-04-20T13:17:38.2980000Z; 47h 49m: 69cdc965d385e3b94310f77b.jsonl[2433] _id=69e8d6ce1724f0c9e2fa5c11 ts=2026-04-22T14:10:22.6340000Z -> 69cdc965d385e3b94310f77b.jsonl[376] _id=69eb77741724f0c9e2fb7955 ts=2026-04-24T14:00:17.4600000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 523 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77b.jsonl[313] _id=69e6356c1724f0c9e2f89b87 ts=2026-04-20T14:17:16.2100000Z -> 69cdc965d385e3b94310f77b.jsonl[1971] _id=69e635991724f0c9e2f89cdf ts=2026-04-20T14:17:16.21Z; 0ms: 69cdc965d385e3b94310f77b.jsonl[472] _id=69f0bfaa1724f0c9e2fcaa3b ts=2026-04-28T14:09:45.7650000Z -> 69cdc965d385e3b94310f77b.jsonl[467] _id=69f0bfb91724f0c9e2fcaa45 ts=2026-04-28T14:09:45.765Z; 3ms: 69cdc965d385e3b94310f77b.jsonl[1674] _id=69e62e431724f0c9e2f87233 ts=2026-04-20T13:46:42.7670000Z -> 69cdc965d385e3b94310f77b.jsonl[1676] _id=69e62e431724f0c9e2f87237 ts=2026-04-20T13:46:42.7700000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 52m 
  - Evidence: 191h 52m: 69cdc965d385e3b94310f77b.jsonl[1969] _id=69e6356c1724f0c9e2f89b85 ts=2026-04-20T14:17:16.1910000Z -> 69cdc965d385e3b94310f77b.jsonl[2801] _id=69f0bfaa1724f0c9e2fcaa39 ts=2026-04-28T14:09:45.7480000Z; 143h 6m: 69cdc965d385e3b94310f77b.jsonl[793] _id=69de4be67957a33870f34f83 ts=2026-04-14T14:15:02.2660000Z -> 69cdc965d385e3b94310f77b.jsonl[1436] _id=69e628431724f0c9e2f84e3d ts=2026-04-20T13:21:06.9940000Z; 56m 9s: 69cdc965d385e3b94310f77b.jsonl[1436] _id=69e628431724f0c9e2f84e3d ts=2026-04-20T13:21:06.9940000Z -> 69cdc965d385e3b94310f77b.jsonl[1969] _id=69e6356c1724f0c9e2f89b85 ts=2026-04-20T14:17:16.1910000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f77b.jsonl[2771] _id=69eb7f771724f0c9e2fba2c1 ts=2026-04-24T14:34:30.0890000Z -> 69cdc965d385e3b94310f77b.jsonl[2778] _id=69f0bf321724f0c9e2fca993 ts=2026-04-28T14:07:45.4180000Z; 94h 41m: 69cdc965d385e3b94310f77b.jsonl[1363] _id=69e0f3a97957a33870f558d9 ts=2026-04-16T14:35:20.9550000Z -> 69cdc965d385e3b94310f77b.jsonl[1364] _id=69e627481724f0c9e2f84a61 ts=2026-04-20T13:16:55.3310000Z; 47h 28m: 69cdc965d385e3b94310f77b.jsonl[373] _id=69e8db2d1724f0c9e2fa7483 ts=2026-04-22T14:29:01.5030000Z -> 69cdc965d385e3b94310f77b.jsonl[2480] _id=69eb76d51724f0c9e2fb76c9 ts=2026-04-24T13:57:39.4730000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77b.jsonl[1122] _id=69e0ed197957a33870f52bab ts=2026-04-16T14:07:20.9670000Z -> 69cdc965d385e3b94310f77b.jsonl[1125] _id=69e0ed2e7957a33870f52c31 ts=2026-04-16T14:07:20.967Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 7m 
  - Evidence: 96h 7m: 69cdc965d385e3b94310f77b.jsonl[2547] _id=69eb78f31724f0c9e2fb81bf ts=2026-04-24T14:06:42.5780000Z -> 69cdc965d385e3b94310f77b.jsonl[2819] _id=69f0c0c71724f0c9e2fcaad1 ts=2026-04-28T14:14:30.4080000Z; 95h 12m: 69cdc965d385e3b94310f77b.jsonl[112] _id=69e0eed17957a33870f53793 ts=2026-04-16T14:14:40.4650000Z -> 69cdc965d385e3b94310f77b.jsonl[1476] _id=69e629911724f0c9e2f85443 ts=2026-04-20T13:26:41.5310000Z; 48h 16m: 69cdc965d385e3b94310f77b.jsonl[2257] _id=69e8d0751724f0c9e2fa350f ts=2026-04-22T13:43:16.9900000Z -> 69cdc965d385e3b94310f77b.jsonl[2488] _id=69eb77531724f0c9e2fb78c1 ts=2026-04-24T13:59:46.8690000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 69cdc965d385e3b94310f77b.jsonl[1135] _id=69e0ed707957a33870f52e19 ts=2026-04-16T14:08:48.0520000Z -> 69cdc965d385e3b94310f77b.jsonl[1482] _id=69e62a581724f0c9e2f85956 ts=2026-04-20T13:29:59.2160000Z; 47h 47m: 69cdc965d385e3b94310f77b.jsonl[2015] _id=69e637371724f0c9e2f8a881 ts=2026-04-20T14:24:55.0450000Z -> 69cdc965d385e3b94310f77b.jsonl[2437] _id=69e8d7361724f0c9e2fa5fa0 ts=2026-04-22T14:12:06.4490000Z; 47h 38m: 69cdc965d385e3b94310f77b.jsonl[2462] _id=69e8d9021724f0c9e2fa68dd ts=2026-04-22T14:19:46.3270000Z -> 69cdc965d385e3b94310f77b.jsonl[2482] _id=69eb770c1724f0c9e2fb776f ts=2026-04-24T13:58:35.3440000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 69cdc965d385e3b94310f77b.jsonl[95] _id=69e0e9887957a33870f5178b ts=2026-04-16T13:52:08.6000000Z -> 69cdc965d385e3b94310f77b.jsonl[1532] _id=69e62a601724f0c9e2f8597b ts=2026-04-20T13:30:08.1830000Z; 48h 39m: 69cdc965d385e3b94310f77b.jsonl[1560] _id=69e62afc1724f0c9e2f85d6f ts=2026-04-20T13:32:44.6270000Z -> 69cdc965d385e3b94310f77b.jsonl[372] _id=69e8d73a1724f0c9e2fa5fbb ts=2026-04-22T14:12:09.8780000Z; 47h 42m: 69cdc965d385e3b94310f77b.jsonl[2456] _id=69e8d8e11724f0c9e2fa6825 ts=2026-04-22T14:19:12.9490000Z -> 69cdc965d385e3b94310f77b.jsonl[2499] _id=69eb77b91724f0c9e2fb7b07 ts=2026-04-24T14:01:28.7910000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc965d385e3b94310f77b.jsonl[136] _id=69e0f30f7957a33870f5537b ts=2026-04-16T14:32:47.3030000Z -> 69cdc965d385e3b94310f77b.jsonl[156] _id=69e627821724f0c9e2f84a97 ts=2026-04-20T13:17:53.7800000Z; 48h 19m: 69cdc965d385e3b94310f77b.jsonl[753] _id=69de4b3b7957a33870f34a71 ts=2026-04-14T14:12:10.8050000Z -> 69cdc965d385e3b94310f77b.jsonl[1311] _id=69e0f2c57957a33870f550cf ts=2026-04-16T14:31:33.2340000Z; 47h 21m: 69cdc965d385e3b94310f77b.jsonl[1841] _id=69e633fd1724f0c9e2f89311 ts=2026-04-20T14:11:09.3070000Z -> 69cdc965d385e3b94310f77b.jsonl[331] _id=69e8cdf81724f0c9e2fa213b ts=2026-04-22T13:32:39.7770000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc965d385e3b94310f77b.jsonl[1332] _id=69e0f3007957a33870f55305 ts=2026-04-16T14:32:32.2060000Z -> 69cdc965d385e3b94310f77b.jsonl[1384] _id=69e627a31724f0c9e2f84b15 ts=2026-04-20T13:18:26.8420000Z; 48h 20m: 69cdc965d385e3b94310f77b.jsonl[750] _id=69de4b2d7957a33870f34a1d ts=2026-04-14T14:11:56.8540000Z -> 69cdc965d385e3b94310f77b.jsonl[1321] _id=69e0f2df7957a33870f551ff ts=2026-04-16T14:31:59.1270000Z; 47h 21m: 69cdc965d385e3b94310f77b.jsonl[1809] _id=69e633f51724f0c9e2f892f7 ts=2026-04-20T14:11:01.7590000Z -> 69cdc965d385e3b94310f77b.jsonl[2147] _id=69e8ce011724f0c9e2fa21ad ts=2026-04-22T13:32:49.7020000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f77b.jsonl[449] _id=69eb7f571724f0c9e2fba221 ts=2026-04-24T14:33:58.1700000Z -> 69cdc965d385e3b94310f77b.jsonl[2779] _id=69f0bf351724f0c9e2fca995 ts=2026-04-28T14:07:48.1800000Z; 94h 43m: 69cdc965d385e3b94310f77b.jsonl[1340] _id=69e0f3277957a33870f55453 ts=2026-04-16T14:33:11.2170000Z -> 69cdc965d385e3b94310f77b.jsonl[1365] _id=69e6274b1724f0c9e2f84a63 ts=2026-04-20T13:16:58.2290000Z; 47h 30m: 69cdc965d385e3b94310f77b.jsonl[2476] _id=69e8dad31724f0c9e2fa7225 ts=2026-04-22T14:27:31.1580000Z -> 69cdc965d385e3b94310f77b.jsonl[2479] _id=69eb76d81724f0c9e2fb76cf ts=2026-04-24T13:57:43.0460000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 69cdc965d385e3b94310f77b.jsonl[1297] _id=69e0f2ba7957a33870f55057 ts=2026-04-16T14:31:22.2180000Z -> 69cdc965d385e3b94310f77b.jsonl[131] _id=69e0f2ba7957a33870f55059 ts=2026-04-16T14:31:22.2230000Z; 5ms: 69cdc965d385e3b94310f77b.jsonl[1371] _id=69e627721724f0c9e2f84a7d ts=2026-04-20T13:17:38.3290000Z -> 69cdc965d385e3b94310f77b.jsonl[152] _id=69e627731724f0c9e2f84a7f ts=2026-04-20T13:17:38.3340000Z; 5ms: 69cdc965d385e3b94310f77b.jsonl[722] _id=69de4a7e7957a33870f3459b ts=2026-04-14T14:09:01.5040000Z -> 69cdc965d385e3b94310f77b.jsonl[721] _id=69de4a7e7957a33870f3459d ts=2026-04-14T14:09:01.5090000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 8 record(s) match the trigger in 69cdc965d385e3b94310f77b.jsonl:69cdc965d385e3b94310f77b, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[874] _id=69de4e927957a33870f36158 ts=2026-04-14T14:26:25.5360000Z`; `69cdc965d385e3b94310f77b.jsonl[67] _id=69e0e6fa7957a33870f50681 ts=2026-04-16T13:41:14.0070000Z`; `69cdc965d385e3b94310f77b.jsonl[184] _id=69e629941724f0c9e2f8544f ts=2026-04-20T13:26:44.5110000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 16 record(s) match the trigger in 69cdc965d385e3b94310f77b.jsonl:69cdc965d385e3b94310f77b, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[1050] _id=69e0e8fc7957a33870f5140b ts=2026-04-16T13:49:48.3630000Z`; `69cdc965d385e3b94310f77b.jsonl[1051] _id=69e0e9027957a33870f5142d ts=2026-04-16T13:49:54.5090000Z`; `69cdc965d385e3b94310f77b.jsonl[1066] _id=69e0e9867957a33870f51773 ts=2026-04-16T13:52:06.1530000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[1701] _id=69e62ec81724f0c9e2f87565 ts=2026-04-20T13:48:55.4600000Z`; `69cdc965d385e3b94310f77b.jsonl[323] _id=69e6380d1724f0c9e2f8ad5f ts=2026-04-20T14:28:29.6420000Z`; `69cdc965d385e3b94310f77b.jsonl[2069] _id=69e8cb491724f0c9e2fa112b ts=2026-04-22T13:21:12.7130000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[337] _id=69e8ce471724f0c9e2fa23f5 ts=2026-04-22T13:33:58.4280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[2517] _id=69eb783a1724f0c9e2fb7e2b ts=2026-04-24T14:03:38.0660000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f77b.jsonl[105] _id=69e0edda7957a33870f53119 ts=2026-04-16T14:10:34.1610000Z`; `69cdc965d385e3b94310f77b.jsonl[112] _id=69e0eed17957a33870f53793 ts=2026-04-16T14:14:40.4650000Z`; `69cdc965d385e3b94310f77b.jsonl[1476] _id=69e629911724f0c9e2f85443 ts=2026-04-20T13:26:41.5310000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 215 unmatched 'DialogueStartEvent' (totals: 420 start, 209 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Started' (totals: 11 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 57 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.36s, min -44.90s, max -0.09s over 2940 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 42 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `DialogueEvent` — 2100 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (840); Unit 3 Dev (421); Unit 1 Dev (420); Unit 3 Dungeon Dev (243); Unit 4 Dev - Dungeon (90); Unit 4 Dev (84); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 1471 of 2100 records
- **Intervals:** median 2.07s (p5 0.01s / p95 33.19s, n=2099)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1471; [conversationId, dialogueEventType] x629
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2100/2100 records)
    numeric range 8 .. 107 (38 unique)
data.dialogueEventType  (string, 2100/2100 records)
    "DialogueNodeEvent"  x1471
    "DialogueStartEvent"  x420
    "DialogueFinishEvent"  x209
data.nodeId  (number, 1471/2100 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 592 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (214); Unit 3 Dev (162); Unit 1 Dev (86); Unit 3 Dungeon Dev (84); Unit 4 Dev (23); Unit 4 Dev - Dungeon (22); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 30.01s (p5 29.96s / p95 33.94s, n=577)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 592/592 records)
data.position.x  (number, 592/592 records)
    numeric range -714.47 .. 1443.96 (318 unique)
data.position.y  (number, 592/592 records)
    numeric range -3578.95 .. 171.569 (263 unique)
data.position.z  (number, 592/592 records)
    numeric range -1110.85 .. 2175.3 (316 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 94 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (29); Unit 2 Prod (Refactor) (26); Unit 3 Dev (20); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (5); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 94 of 94 records
- **Intervals:** median 136.26s (p5 0.01s / p95 68130.33s, n=93)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 94/94 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x37
data.questID  (string, 94/94 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 94/94 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/94 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 42 records

- **Scenes:** Unit 3 Dev (26); Unit 2 Prod (Refactor) (16)
- **Intervals:** median 15.96s (p5 1.34s / p95 171529.02s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "MapCloseEvent"  x21
    "MapOpenEvent"  x21
data.featureUsed  (string, 42/42 records)
    "Map"  x42
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 40 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (14); Unit 3 Dev (7)
- **Intervals:** median 8.65s (p5 1.84s / p95 170857.38s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "argumentationNodeAdd"  x29
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 40/40 records)
    "Unit 2 – Watershed"  x19
    "Unit 1 - Freshwater"  x11
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 40/40 records)
    "A"  x9
    "1"  x7
    "I"  x7
    "B"  x5
    "D"  x4
    "II"  x3
    "3"  x2
    "C"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 19 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 3 Dev (6); Unit 4 Dev (2)
- **Intervals:** median 240.42s (p5 2.99s / p95 343223.08s, n=18)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 19/19 records)
    "Started"  x11
    "Finished"  x8
data.Unit  (string, 19/19 records)
    "Unit 2 Prod (Refactor)"  x11
    "Unit 3 Dev"  x6
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (12); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 43.44s (p5 0.90s / p95 215748.44s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 17/17 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x6
    "Unit 1 - Does the planet WAT-247 have freshwater"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 1 - Argumentation Tutorial"  x6
    "Unit 1 - Freshwater"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TopographicMapEvent` — 16 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (8)
- **Intervals:** median 6.15s (p5 1.24s / p95 225899.55s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "dragEnd"  x8
    "dragStart"  x8
data.featureUsed  (string, 16/16 records)
    "waypoint"  x16
data.location  (object, 16/16 records)
data.location.x  (number, 16/16 records)
    9 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 16/16 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 16/16 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 3.38s (p5 1.49s / p95 76.97s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x7
    "Bedrock"  x4
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 16/16 records)
    "5"  x10
    "4"  x5
    "3"  x1
data.machine  (string, 16/16 records)
    "1"  x15
    "2"  x1
data.row  (string, 16/16 records)
    "BottomRow"  x8
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 515164.73s (p5 54548.75s / p95 673191.07s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x2
    "2"  x1
    "3"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (11 records)
- `TopographicMapEvent` data.actionType: "dragStart" (8x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*