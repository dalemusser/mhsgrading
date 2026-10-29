# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f778

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f778
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f778.jsonl
- **Records:** 2340 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f778
- **Time span:** 2026-04-14T13:50:32.721000+00:00 .. 2026-04-22T14:29:03.147000+00:00 (192h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f778\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 2340 records, 6 scenes.
- Findings: **0 FAIL**, **40 WARNING**, 48 INFO, 2 NOT_TESTED, 37 PASS.
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
| DialogueEvent | 1699 | 72.61 | 1 | 6 | 1272 | 2026-04-14T13:50:51.092000+00:00 | 2026-04-22T14:28:43.150000+00:00 | 192h 37m |
| PlayerPositionEvent | 454 | 19.4 | 1 | 6 | 0 | 2026-04-14T13:50:32.721000+00:00 | 2026-04-22T14:29:03.147000+00:00 | 192h 38m |
| questEvent | 82 | 3.5 | 1 | 6 | 82 | 2026-04-14T13:50:51.067000+00:00 | 2026-04-22T14:25:02.613000+00:00 | 192h 34m |
| Topographic Map Event | 40 | 1.71 | 1 | 2 | 0 | 2026-04-14T14:10:13.517000+00:00 | 2026-04-20T14:23:35.247000+00:00 | 144h 13m |
| TopographicMapEvent | 24 | 1.03 | 1 | 1 | 0 | 2026-04-16T13:49:59.972000+00:00 | 2026-04-20T14:20:55.925000+00:00 | 96h 30m |
| Soil Key Puzzle | 22 | 0.94 | 1 | 2 | 0 | 2026-04-14T14:24:39.758000+00:00 | 2026-04-22T13:47:21.439000+00:00 | 191h 22m |
| argumentationNodeEvent | 10 | 0.43 | 1 | 1 | 0 | 2026-04-14T14:03:58.444000+00:00 | 2026-04-14T14:07:05.824000+00:00 | 3m 7s |
| argumentationEvent | 4 | 0.17 | 1 | 1 | 0 | 2026-04-14T14:03:44.525000+00:00 | 2026-04-14T14:07:16.437000+00:00 | 3m 31s |
| soilMachine | 4 | 0.17 | 1 | 1 | 0 | 2026-04-22T14:11:28.791000+00:00 | 2026-04-22T14:14:50.274000+00:00 | 3m 21s |
| EndOfUnit | 1 | 0.04 | 1 | 1 | 0 | 2026-04-14T14:11:05.239000+00:00 | 2026-04-14T14:11:05.239000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 0.653s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.008s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 212.771s median 
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
  - Observed: 5.526s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 16.001s median 
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
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 3 Dungeon Dev; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
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
- **INFO / Info** `argumentationEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 4 records 
  - Expected: 14 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
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
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 41; 43; 44; 45; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 69 mismatch(es); e.g. 'DialogueNodeEvent:37:0' vs expected 'DialogueNodeEvent:37:64' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f778.jsonl[90] _id=69de491b7957a33870f33b5d ts=2026-04-14T14:03:06.4240000Z`; `69cdc965d385e3b94310f778.jsonl[126] _id=69de4a157957a33870f342b9 ts=2026-04-14T14:07:16.4880000Z`; `69cdc965d385e3b94310f778.jsonl[1510] _id=69de4fb87957a33870f36a62 ts=2026-04-14T14:31:19.5470000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:25' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc965d385e3b94310f778.jsonl[2092] _id=69e8c9461724f0c9e2fa096d ts=2026-04-22T13:12:36.4180000Z`; `69cdc965d385e3b94310f778.jsonl[953] _id=69e8c9cb1724f0c9e2fa09cf ts=2026-04-22T13:14:49.3230000Z`; `69cdc965d385e3b94310f778.jsonl[2109] _id=69e8ca651724f0c9e2fa0c93 ts=2026-04-22T13:17:23.5870000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 24 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1698 | 0.003 | 0.653 | 408.405 | 32.446 | 341013.682 | 0.15 | 353 | 6 |
| PlayerPositionEvent | 446 | 29.78 | 30.008 | 1553.091 | 39.69 | 340933.497 | 0.04 | 0 | 3 |
| questEvent | 81 | 0.002 | 119.692 | 8558.661 | 860.357 | 341526.059 | 0.01 | 13 | 8 |
| Topographic Map Event | 39 | 2.335 | 34.298 | 13312.865 | 19419.926 | 341464.092 | 0.0 | 0 | 5 |
| TopographicMapEvent | 23 | 0.392 | 5.526 | 15106.781 | 2448.043 | 343326.324 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 21 | 2.983 | 212.771 | 32807.699 | 170495.462 | 342419.223 | 0.0 | 0 | 6 |
| argumentationNodeEvent | 9 | 1.002 | 16.001 | 20.82 | 58.525 | 61.823 | 2.88 | 0 | 0 |
| argumentationEvent | 3 | 32.989 | 52.17 | 70.637 | 119.295 | 126.753 | 0.85 | 0 | 0 |
| soilMachine | 3 | 6.751 | 64.938 | 67.161 | 123.308 | 129.794 | 0.89 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.96s, p95 39.69s, n=446) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 69cdc965d385e3b94310f778.jsonl[2092] _id=69e8c9461724f0c9e2fa096d ts=2026-04-22T13:12:36.4180000Z ~ 69cdc965d385e3b94310f778.jsonl[2090] _id=69e8c9461724f0c9e2fa096f ts=2026-04-22T13:12:36.4210000Z`; `9ms: 69cdc965d385e3b94310f778.jsonl[953] _id=69e8c9cb1724f0c9e2fa09cf ts=2026-04-22T13:14:49.3230000Z ~ 69cdc965d385e3b94310f778.jsonl[2101] _id=69e8c9cb1724f0c9e2fa09d1 ts=2026-04-22T13:14:49.3320000Z`; `8ms: 69cdc965d385e3b94310f778.jsonl[2109] _id=69e8ca651724f0c9e2fa0c93 ts=2026-04-22T13:17:23.5870000Z ~ 69cdc965d385e3b94310f778.jsonl[965] _id=69e8ca651724f0c9e2fa0c95 ts=2026-04-22T13:17:23.5950000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc965d385e3b94310f778.jsonl[507] _id=69e0f3857957a33870f55834 ts=2026-04-16T14:34:44.2290000Z -> 69cdc965d385e3b94310f778.jsonl[1773] _id=69e6279a1724f0c9e2f84ae3 ts=2026-04-20T13:18:17.9110000Z; 47h 2m: 69cdc965d385e3b94310f778.jsonl[1513] _id=69de4fd37957a33870f36ad0 ts=2026-04-14T14:31:46.7150000Z -> 69cdc965d385e3b94310f778.jsonl[222] _id=69e0e55a7957a33870f4fa59 ts=2026-04-16T13:34:17.3940000Z; 46h 37m: 69cdc965d385e3b94310f778.jsonl[924] _id=69e6399a1724f0c9e2f8b54f ts=2026-04-20T14:35:05.5670000Z -> 69cdc965d385e3b94310f778.jsonl[2088] _id=69e8c9461724f0c9e2fa0969 ts=2026-04-22T13:12:35.3140000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 353 interval(s) ≤ 0.003s..0.004s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f778.jsonl[1377] _id=69de4a607957a33870f344b5 ts=2026-04-14T14:08:31.4390000Z -> 69cdc965d385e3b94310f778.jsonl[72] _id=69de4a607957a33870f344b7 ts=2026-04-14T14:08:31.4420000Z; 4ms: 69cdc965d385e3b94310f778.jsonl[1387] _id=69de4ad27957a33870f347f3 ts=2026-04-14T14:10:25.2540000Z -> 69cdc965d385e3b94310f778.jsonl[1401] _id=69de4ad27957a33870f347f5 ts=2026-04-14T14:10:25.2580000Z; 4ms: 69cdc965d385e3b94310f778.jsonl[141] _id=69de4a647957a33870f344cf ts=2026-04-14T14:08:35.2400000Z -> 69cdc965d385e3b94310f778.jsonl[142] _id=69de4a647957a33870f344d1 ts=2026-04-14T14:08:35.2440000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc965d385e3b94310f778.jsonl[1768] _id=69e0f3b17957a33870f558fd ts=2026-04-16T14:35:28.8180000Z -> 69cdc965d385e3b94310f778.jsonl[1771] _id=69e627791724f0c9e2f84a89 ts=2026-04-20T13:17:42.3150000Z; 47h 1m: 69cdc965d385e3b94310f778.jsonl[214] _id=69de4fcf7957a33870f36ac0 ts=2026-04-14T14:31:42.7850000Z -> 69cdc965d385e3b94310f778.jsonl[220] _id=69e0e5387957a33870f4f9c3 ts=2026-04-16T13:33:41.1650000Z; 46h 37m: 69cdc965d385e3b94310f778.jsonl[935] _id=69e6399e1724f0c9e2f8b563 ts=2026-04-20T14:35:09.8360000Z -> 69cdc965d385e3b94310f778.jsonl[2087] _id=69e8c9421724f0c9e2fa0967 ts=2026-04-22T13:12:32.7870000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 6m 
  - Evidence: 95h 6m: 69cdc965d385e3b94310f778.jsonl[1648] _id=69e0ef017957a33870f53873 ts=2026-04-16T14:15:28.7570000Z -> 69cdc965d385e3b94310f778.jsonl[1791] _id=69e628941724f0c9e2f84f95 ts=2026-04-20T13:22:27.9800000Z; 47h 21m: 69cdc965d385e3b94310f778.jsonl[1480] _id=69de4e2c7957a33870f35f3b ts=2026-04-14T14:24:42.7410000Z -> 69cdc965d385e3b94310f778.jsonl[1540] _id=69e0e82b7957a33870f50e81 ts=2026-04-16T13:46:18.2030000Z; 46h 47m: 69cdc965d385e3b94310f778.jsonl[2064] _id=69e637a01724f0c9e2f8aaf1 ts=2026-04-20T14:26:39.5000000Z -> 69cdc965d385e3b94310f778.jsonl[950] _id=69e8c9a41724f0c9e2fa09a3 ts=2026-04-22T13:14:11.3870000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc965d385e3b94310f778.jsonl[1745] _id=69e0f3157957a33870f553b7 ts=2026-04-16T14:32:52.9740000Z -> 69cdc965d385e3b94310f778.jsonl[580] _id=69e628ed1724f0c9e2f85153 ts=2026-04-20T13:23:57.0660000Z; 47h 18m: 69cdc965d385e3b94310f778.jsonl[218] _id=69de4fd47957a33870f36ad2 ts=2026-04-14T14:31:46.7740000Z -> 69cdc965d385e3b94310f778.jsonl[302] _id=69e0e8ff7957a33870f5141f ts=2026-04-16T13:49:50.0980000Z; 44m 17s: 69cdc965d385e3b94310f778.jsonl[706] _id=69e62be11724f0c9e2f86431 ts=2026-04-20T13:36:32.7340000Z -> 69cdc965d385e3b94310f778.jsonl[835] _id=69e636431724f0c9e2f8a139 ts=2026-04-20T14:20:50.0600000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 69cdc965d385e3b94310f778.jsonl[1634] _id=69e0ede37957a33870f53167 ts=2026-04-16T14:10:42.2030000Z -> 69cdc965d385e3b94310f778.jsonl[602] _id=69e62b001724f0c9e2f85d91 ts=2026-04-20T13:32:48.5270000Z; 44m 26s: 69cdc965d385e3b94310f778.jsonl[708] _id=69e62bdd1724f0c9e2f86413 ts=2026-04-20T13:36:28.7640000Z -> 69cdc965d385e3b94310f778.jsonl[2031] _id=69e636481724f0c9e2f8a14f ts=2026-04-20T14:20:55.5330000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc965d385e3b94310f778.jsonl[1715] _id=69e0f18b7957a33870f54632 ts=2026-04-16T14:26:18.5160000Z -> 69cdc965d385e3b94310f778.jsonl[510] _id=69e627a11724f0c9e2f84b07 ts=2026-04-20T13:18:24.5750000Z; 47h 2m: 69cdc965d385e3b94310f778.jsonl[215] _id=69de4fd27957a33870f36ac6 ts=2026-04-14T14:31:45.7460000Z -> 69cdc965d385e3b94310f778.jsonl[226] _id=69e0e5657957a33870f4faf1 ts=2026-04-16T13:34:28.0830000Z; 46h 37m: 69cdc965d385e3b94310f778.jsonl[937] _id=69e639931724f0c9e2f8b4ff ts=2026-04-20T14:34:58.8570000Z -> 69cdc965d385e3b94310f778.jsonl[2092] _id=69e8c9461724f0c9e2fa096d ts=2026-04-22T13:12:36.4180000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f778.jsonl[2148] _id=69e8cd5d1724f0c9e2fa1d0f ts=2026-04-22T13:30:04.0730000Z -> 69cdc965d385e3b94310f778.jsonl[1048] _id=69e8cd5e1724f0c9e2fa1d15 ts=2026-04-22T13:30:04.0750000Z; 2ms: 69cdc965d385e3b94310f778.jsonl[95] _id=69de493b7957a33870f33c5d ts=2026-04-14T14:03:37.4300000Z -> 69cdc965d385e3b94310f778.jsonl[97] _id=69de493b7957a33870f33c5f ts=2026-04-14T14:03:37.4320000Z; 3ms: 69cdc965d385e3b94310f778.jsonl[2092] _id=69e8c9461724f0c9e2fa096d ts=2026-04-22T13:12:36.4180000Z -> 69cdc965d385e3b94310f778.jsonl[2090] _id=69e8c9461724f0c9e2fa096f ts=2026-04-22T13:12:36.4210000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 8 record(s) match the trigger in 69cdc965d385e3b94310f778.jsonl:69cdc965d385e3b94310f778, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f778.jsonl[1480] _id=69de4e2c7957a33870f35f3b ts=2026-04-14T14:24:42.7410000Z`; `69cdc965d385e3b94310f778.jsonl[1541] _id=69e0e82e7957a33870f50e85 ts=2026-04-16T13:46:21.1990000Z`; `69cdc965d385e3b94310f778.jsonl[1648] _id=69e0ef017957a33870f53873 ts=2026-04-16T14:15:28.7570000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 24 record(s) match the trigger in 69cdc965d385e3b94310f778.jsonl:69cdc965d385e3b94310f778, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f778.jsonl[312] _id=69e0e9087957a33870f51449 ts=2026-04-16T13:49:59.9720000Z`; `69cdc965d385e3b94310f778.jsonl[313] _id=69e0e90b7957a33870f51453 ts=2026-04-16T13:50:02.7390000Z`; `69cdc965d385e3b94310f778.jsonl[1593] _id=69e0e9b47957a33870f518f7 ts=2026-04-16T13:52:52.0780000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f778.jsonl[1723] _id=69e0f1b57957a33870f5478f ts=2026-04-16T14:26:59.9360000Z`; `69cdc965d385e3b94310f778.jsonl[1188] _id=69e8d8681724f0c9e2fa659b ts=2026-04-22T14:17:11.7390000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f778.jsonl[962] _id=69e8ca0a1724f0c9e2fa0b0b ts=2026-04-22T13:15:52.4570000Z`; `69cdc965d385e3b94310f778.jsonl[1023] _id=69e8cb301724f0c9e2fa1097 ts=2026-04-22T13:20:47.7280000Z`; `69cdc965d385e3b94310f778.jsonl[1029] _id=69e8cbba1724f0c9e2fa136b ts=2026-04-22T13:23:05.4970000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 129 unmatched 'DialogueStartEvent' (totals: 277 start, 150 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'Started' (totals: 14 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 36 unmatched 'questActiveEvent' (totals: 59 start, 23 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.83s, min -3.46s, max -0.25s over 2340 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f778\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=partial, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 40 records 
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

### `DialogueEvent` — 1699 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (1179); Unit 1 Dev (211); Unit 4 Dev (103); Unit 4 Dev - Anderson Base (96); Unit 4 Dev - Dungeon (90); Unit 3 Dev (20)
- **eventKey:** present on 1272 of 1699 records
- **Intervals:** median 0.65s (p5 0.01s / p95 32.45s, n=1698)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1272; [conversationId, dialogueEventType] x427
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1699/1699 records)
    numeric range 8 .. 107 (28 unique)
data.dialogueEventType  (string, 1699/1699 records)
    "DialogueNodeEvent"  x1272
    "DialogueStartEvent"  x277
    "DialogueFinishEvent"  x150
data.nodeId  (number, 1272/1699 records)
    numeric range 0 .. 290 (163 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 454 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (285); Unit 1 Dev (41); Unit 4 Dev (39); Unit 3 Dev (36); Unit 4 Dev - Dungeon (36); Unit 4 Dev - Anderson Base (17)
- **Intervals:** median 30.01s (p5 29.96s / p95 39.69s, n=446)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 454/454 records)
data.position.x  (number, 454/454 records)
    numeric range -105.92 .. 1620.98 (302 unique)
data.position.y  (number, 454/454 records)
    numeric range -114.913 .. 166.214 (230 unique)
data.position.z  (number, 454/454 records)
    numeric range -721.288 .. 1981.39 (302 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (48); Unit 1 Dev (12); Unit 4 Dev - Dungeon (9); Unit 3 Dev (7); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 119.69s (p5 0.00s / p95 860.36s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x59; [questEventType, questID, questName, questSuccessOrFailure] x23
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x59
    "questFinishEvent"  x23
data.questID  (string, 82/82 records)
    20 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    20 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 23/82 records)
    "Succeeded"  x23
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 2 Prod (Refactor) (38); Unit 1 Dev (2)
- **Intervals:** median 34.30s (p5 2.40s / p95 19419.93s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapOpenEvent"  x21
    "MapCloseEvent"  x19
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 24 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24)
- **Intervals:** median 5.53s (p5 0.82s / p95 2448.04s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "dragEnd"  x12
    "dragStart"  x12
data.featureUsed  (string, 24/24 records)
    "waypoint"  x24
data.location  (object, 24/24 records)
data.location.x  (number, 24/24 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 24/24 records)
    numeric range -307.4 .. 253.989 (13 unique)
data.location.z  (number, 24/24 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 22 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev (2)
- **Intervals:** median 212.77s (p5 3.00s / p95 170495.46s, n=21)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 22/22 records)
    "Started"  x14
    "Finished"  x8
data.Unit  (string, 22/22 records)
    "Unit 2 Prod (Refactor)"  x20
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 10 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (10)
- **Intervals:** median 16.00s (p5 1.09s / p95 58.53s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationNodeAdd"  x8
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 10/10 records)
    "A"  x3
    "B"  x3
    "1"  x2
    "I"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 52.17s (p5 34.91s / p95 119.29s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationSessionClose"  x2
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 4/4 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 4 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (4)
- **Intervals:** median 64.94s (p5 12.57s / p95 123.31s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "ChangeCanister"  x4
data.canisterType  (string, 4/4 records)
    "Bedrock"  x2
    "Gravel"  x1
    "Sand"  x1
data.floor  (string, 4/4 records)
    "5"  x3
    "4"  x1
data.machine  (string, 4/4 records)
    "1"  x3
    "2"  x1
data.row  (string, 4/4 records)
    "BottomRow"  x2
    "TopRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "1"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TopographicMapEvent` data.actionType: "dragStart" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (2x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*