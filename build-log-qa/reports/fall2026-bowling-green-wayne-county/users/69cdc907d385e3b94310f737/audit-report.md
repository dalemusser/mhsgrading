# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f737

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f737
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f737.jsonl
- **Records:** 2251 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f737
- **Time span:** 2026-04-13T17:56:35.721000+00:00 .. 2026-04-23T18:39:52.904000+00:00 (240h 43m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f737\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2251 records, 5 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 54 INFO, 2 NOT_TESTED, 35 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1454 | 64.59 | 1 | 5 | 1008 | 2026-04-13T17:56:53.888000+00:00 | 2026-04-23T18:39:45.852000+00:00 | 240h 42m |
| PlayerPositionEvent | 639 | 28.39 | 1 | 5 | 0 | 2026-04-13T17:56:35.721000+00:00 | 2026-04-23T18:39:52.904000+00:00 | 240h 43m |
| questEvent | 51 | 2.27 | 1 | 5 | 51 | 2026-04-13T17:56:53.874000+00:00 | 2026-04-23T18:38:47.432000+00:00 | 240h 41m |
| argumentationNodeEvent | 33 | 1.47 | 1 | 3 | 0 | 2026-04-13T18:17:58.959000+00:00 | 2026-04-21T17:43:19.586000+00:00 | 191h 25m |
| Topographic Map Event | 23 | 1.02 | 1 | 2 | 0 | 2026-04-15T18:00:37.724000+00:00 | 2026-04-23T18:27:24.395000+00:00 | 192h 26m |
| TopographicMapEvent | 20 | 0.89 | 1 | 2 | 0 | 2026-04-15T18:01:11.396000+00:00 | 2026-04-23T18:27:22.307000+00:00 | 192h 26m |
| argumentationToolEvent | 10 | 0.44 | 1 | 1 | 0 | 2026-04-21T17:41:30.168000+00:00 | 2026-04-21T17:41:58.716000+00:00 | 28.5s |
| argumentationEvent | 9 | 0.4 | 1 | 3 | 0 | 2026-04-13T18:15:56.910000+00:00 | 2026-04-21T17:43:21.058000+00:00 | 191h 27m |
| Soil Key Puzzle | 8 | 0.36 | 1 | 2 | 0 | 2026-04-13T18:38:32.106000+00:00 | 2026-04-21T17:52:16.625000+00:00 | 191h 13m |
| EndOfUnit | 3 | 0.13 | 1 | 3 | 0 | 2026-04-13T18:21:55.325000+00:00 | 2026-04-23T18:32:52.535000+00:00 | 240h 10m |
| crash | 1 | 0.04 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 432328.605s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.003s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 225.409s median 
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
  - Observed: 6.85s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 143.004s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.732s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.65s median 
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
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 23 records this build 
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
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 33 records 
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
  - Observed: D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f737.jsonl[376] _id=69dd33737957a33870f26e0c ts=2026-04-13T18:18:27.5140000Z`; `69cdc907d385e3b94310f737.jsonl[57] _id=69dfd37c7957a33870f42c4f ts=2026-04-15T18:05:47.5710000Z`; `69cdc907d385e3b94310f737.jsonl[99] _id=69e271fd1724f0c9e2f74a6c ts=2026-04-17T17:46:36.1720000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 23 records, TopographicMapEvent: 20 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1453 | 0.002 | 2.921 | 596.402 | 46.787 | 339406.166 | 0.1 | 387 | 8 |
| PlayerPositionEvent | 633 | 0.0 | 30.003 | 1367.713 | 30.876 | 339353.961 | 0.04 | 1 | 4 |
| questEvent | 50 | 0.002 | 193.519 | 17330.271 | 168347.233 | 339669.85 | 0.0 | 3 | 14 |
| argumentationNodeEvent | 32 | 0.373 | 7.732 | 21535.02 | 154622.411 | 345211.717 | 0.0 | 0 | 2 |
| Topographic Map Event | 22 | 3.654 | 20.212 | 31491.212 | 164162.988 | 517545.137 | 0.0 | 0 | 3 |
| TopographicMapEvent | 19 | 0.514 | 6.85 | 36461.627 | 208907.502 | 517547.422 | 0.0 | 0 | 2 |
| argumentationToolEvent | 9 | 0.083 | 1.65 | 3.172 | 11.639 | 15.987 | 18.92 | 0 | 0 |
| argumentationEvent | 8 | 0.088 | 143.004 | 86155.518 | 344583.63 | 345177.638 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 7 | 2.812 | 225.409 | 98346.36 | 412765.678 | 516730.054 | 0.0 | 0 | 3 |
| EndOfUnit | 2 | 343713.038 | 432328.605 | 432328.605 | 512082.615 | 520944.172 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.003s (p5 29.96s, p95 30.88s, n=633) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `88ms: 69cdc907d385e3b94310f737.jsonl[1715] _id=69e7b7391724f0c9e2f945db ts=2026-04-21T17:43:20.9700000Z ~ 69cdc907d385e3b94310f737.jsonl[1714] _id=69e7b7391724f0c9e2f945eb ts=2026-04-21T17:43:21.0580000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `884ms: 69cdc907d385e3b94310f737.jsonl[1694] _id=69e7b6e41724f0c9e2f9439f ts=2026-04-21T17:41:56.1820000Z ~ 69cdc907d385e3b94310f737.jsonl[1697] _id=69e7b6e51724f0c9e2f943af ts=2026-04-21T17:41:57.0660000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f737.jsonl[1485] _id=69e27e701724f0c9e2f78c9c ts=2026-04-17T18:39:43.1650000Z -> 69cdc907d385e3b94310f737.jsonl[1493] _id=69e7ac3d1724f0c9e2f916d3 ts=2026-04-21T16:56:29.3310000Z; 47h 21m: 69cdc907d385e3b94310f737.jsonl[1984] _id=69e7c47f1724f0c9e2f9a709 ts=2026-04-21T18:39:59.4490000Z -> 69cdc907d385e3b94310f737.jsonl[1986] _id=69ea5e901724f0c9e2fb062b ts=2026-04-23T18:01:51.8360000Z; 47h 3m: 69cdc907d385e3b94310f737.jsonl[32] _id=69dd38e67957a33870f2922c ts=2026-04-13T18:41:41.6180000Z -> 69cdc907d385e3b94310f737.jsonl[542] _id=69dfcea07957a33870f40b7f ts=2026-04-15T17:45:03.5320000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 387 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f737.jsonl[12] _id=69dd33bd7957a33870f27026 ts=2026-04-13T18:19:41.1560000Z -> 69cdc907d385e3b94310f737.jsonl[16] _id=69dd33bd7957a33870f2702a ts=2026-04-13T18:19:41.1580000Z; 3ms: 69cdc907d385e3b94310f737.jsonl[15] _id=69dd33c17957a33870f27048 ts=2026-04-13T18:19:44.9130000Z -> 69cdc907d385e3b94310f737.jsonl[372] _id=69dd33c17957a33870f27052 ts=2026-04-13T18:19:44.9160000Z; 3ms: 69cdc907d385e3b94310f737.jsonl[1773] _id=69e7ba4b1724f0c9e2f95981 ts=2026-04-21T17:56:27.0030000Z -> 69cdc907d385e3b94310f737.jsonl[1774] _id=69e7ba4b1724f0c9e2f95985 ts=2026-04-21T17:56:27.0060000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 42m 
  - Evidence: 144h 42m: 69cdc907d385e3b94310f737.jsonl[1291] _id=69e272e51724f0c9e2f75076 ts=2026-04-17T17:50:28.3630000Z -> 69cdc907d385e3b94310f737.jsonl[2208] _id=69ea65d41724f0c9e2fb40cf ts=2026-04-23T18:32:52.5350000Z; 95h 28m: 69cdc907d385e3b94310f737.jsonl[413] _id=69dd34437957a33870f27384 ts=2026-04-13T18:21:55.3250000Z -> 69cdc907d385e3b94310f737.jsonl[1291] _id=69e272e51724f0c9e2f75076 ts=2026-04-17T17:50:28.3630000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f737.jsonl[1483] _id=69e27e5e1724f0c9e2f78c58 ts=2026-04-17T18:39:25.6140000Z -> 69cdc907d385e3b94310f737.jsonl[1489] _id=69e7abf81724f0c9e2f915a3 ts=2026-04-21T16:55:19.5750000Z; 47h 21m: 69cdc907d385e3b94310f737.jsonl[1985] _id=69e7c4951724f0c9e2f9a762 ts=2026-04-21T18:40:21.5010000Z -> 69cdc907d385e3b94310f737.jsonl[1987] _id=69ea5e8e1724f0c9e2fb0623 ts=2026-04-23T18:01:50.3000000Z; 47h 3m: 69cdc907d385e3b94310f737.jsonl[535] _id=69dd38e87957a33870f2922e ts=2026-04-13T18:41:43.9460000Z -> 69cdc907d385e3b94310f737.jsonl[537] _id=69dfce9c7957a33870f40b78 ts=2026-04-15T17:44:59.6960000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f737.jsonl[1328] _id=69e2753f1724f0c9e2f76012 ts=2026-04-17T18:00:30.7650000Z -> 69cdc907d385e3b94310f737.jsonl[1329] _id=69e275a91724f0c9e2f76256 ts=2026-04-17T18:00:30.765Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 32m 
  - Evidence: 143h 32m: 69cdc907d385e3b94310f737.jsonl[788] _id=69dfd5f57957a33870f43a3d ts=2026-04-15T18:16:21.1620000Z -> 69cdc907d385e3b94310f737.jsonl[1761] _id=69e7b86f1724f0c9e2f94e9b ts=2026-04-21T17:48:31.2160000Z; 47h 16m: 69cdc907d385e3b94310f737.jsonl[494] _id=69dd382b7957a33870f28dde ts=2026-04-13T18:38:35.2670000Z -> 69cdc907d385e3b94310f737.jsonl[605] _id=69dfd0f17957a33870f41971 ts=2026-04-15T17:54:57.4000000Z; 17m 51s: 69cdc907d385e3b94310f737.jsonl[603] _id=69dfd0f47957a33870f41987 ts=2026-04-15T17:55:00.2120000Z -> 69cdc907d385e3b94310f737.jsonl[773] _id=69dfd5247957a33870f43611 ts=2026-04-15T18:12:51.3700000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 45m 
  - Evidence: 143h 45m: 69cdc907d385e3b94310f737.jsonl[1482] _id=69e27e7c1724f0c9e2f78cd6 ts=2026-04-17T18:39:55.1030000Z -> 69cdc907d385e3b94310f737.jsonl[2156] _id=69ea64241724f0c9e2fb334b ts=2026-04-23T18:25:40.2400000Z; 47h 58m: 69cdc907d385e3b94310f737.jsonl[997] _id=69dfdb697957a33870f46449 ts=2026-04-15T18:39:36.9990000Z -> 69cdc907d385e3b94310f737.jsonl[1464] _id=69e27e0a1724f0c9e2f78a40 ts=2026-04-17T18:38:01.8430000Z; 31m 7s: 69cdc907d385e3b94310f737.jsonl[732] _id=69dfd40e7957a33870f43023 ts=2026-04-15T18:08:13.7800000Z -> 69cdc907d385e3b94310f737.jsonl[995] _id=69dfdb597957a33870f463cb ts=2026-04-15T18:39:21.4970000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 45m 
  - Evidence: 143h 45m: 69cdc907d385e3b94310f737.jsonl[1486] _id=69e27e821724f0c9e2f78cf0 ts=2026-04-17T18:40:01.6820000Z -> 69cdc907d385e3b94310f737.jsonl[2152] _id=69ea642d1724f0c9e2fb336b ts=2026-04-23T18:25:49.1040000Z; 48h 30m: 69cdc907d385e3b94310f737.jsonl[738] _id=69dfd40e7957a33870f4301f ts=2026-04-15T18:08:13.6990000Z -> 69cdc907d385e3b94310f737.jsonl[1473] _id=69e27e241724f0c9e2f78af7 ts=2026-04-17T18:38:27.8770000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 69cdc907d385e3b94310f737.jsonl[1243] _id=69e271fd1724f0c9e2f74a66 ts=2026-04-17T17:46:36.1450000Z -> 69cdc907d385e3b94310f737.jsonl[138] _id=69e7b6561724f0c9e2f93fb7 ts=2026-04-21T17:39:33.7830000Z; 95h 24m: 69cdc907d385e3b94310f737.jsonl[374] _id=69dd33737957a33870f26e06 ts=2026-04-13T18:18:27.4910000Z -> 69cdc907d385e3b94310f737.jsonl[96] _id=69e2712c1724f0c9e2f74446 ts=2026-04-17T17:43:07.9640000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 69cdc907d385e3b94310f737.jsonl[1241] _id=69e271f91724f0c9e2f74a5c ts=2026-04-17T17:46:32.7570000Z -> 69cdc907d385e3b94310f737.jsonl[1674] _id=69e7b6741724f0c9e2f94097 ts=2026-04-21T17:40:04.4740000Z; 95h 25m: 69cdc907d385e3b94310f737.jsonl[375] _id=69dd336e7957a33870f26dd6 ts=2026-04-13T18:18:21.9620000Z -> 69cdc907d385e3b94310f737.jsonl[1210] _id=69e2713d1724f0c9e2f744ae ts=2026-04-17T17:43:24.6180000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc907d385e3b94310f737.jsonl[1450] _id=69e27d251724f0c9e2f78486 ts=2026-04-17T18:34:12.2740000Z -> 69cdc907d385e3b94310f737.jsonl[1487] _id=69e7abfa1724f0c9e2f915ab ts=2026-04-21T16:55:22.1240000Z; 47h 24m: 69cdc907d385e3b94310f737.jsonl[1972] _id=69e7c3e11724f0c9e2f9a2c9 ts=2026-04-21T18:37:21.4510000Z -> 69cdc907d385e3b94310f737.jsonl[1988] _id=69ea5e901724f0c9e2fb0629 ts=2026-04-23T18:01:51.5900000Z; 47h 3m: 69cdc907d385e3b94310f737.jsonl[527] _id=69dd38e57957a33870f29228 ts=2026-04-13T18:41:41.0630000Z -> 69cdc907d385e3b94310f737.jsonl[541] _id=69dfce9f7957a33870f40b7d ts=2026-04-15T17:45:01.9340000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.008s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f737.jsonl[341] _id=69dd327f7957a33870f2671e ts=2026-04-13T18:14:23.1120000Z -> 69cdc907d385e3b94310f737.jsonl[5] _id=69dd327f7957a33870f26720 ts=2026-04-13T18:14:23.1140000Z; 5ms: 69cdc907d385e3b94310f737.jsonl[274] _id=69dd30ae7957a33870f25a2e ts=2026-04-13T18:06:38.4630000Z -> 69cdc907d385e3b94310f737.jsonl[275] _id=69dd30ae7957a33870f25a32 ts=2026-04-13T18:06:38.4680000Z; 8ms: 69cdc907d385e3b94310f737.jsonl[227] _id=69dd2fbd7957a33870f254c4 ts=2026-04-13T18:02:37.7380000Z -> 69cdc907d385e3b94310f737.jsonl[233] _id=69dd2fbd7957a33870f254c6 ts=2026-04-13T18:02:37.7460000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f737.jsonl:69cdc907d385e3b94310f737, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f737.jsonl[494] _id=69dd382b7957a33870f28dde ts=2026-04-13T18:38:35.2670000Z`; `69cdc907d385e3b94310f737.jsonl[603] _id=69dfd0f47957a33870f41987 ts=2026-04-15T17:55:00.2120000Z`; `69cdc907d385e3b94310f737.jsonl[788] _id=69dfd5f57957a33870f43a3d ts=2026-04-15T18:16:21.1620000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 20 record(s) match the trigger in 69cdc907d385e3b94310f737.jsonl:69cdc907d385e3b94310f737, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f737.jsonl[676] _id=69dfd2677957a33870f424fb ts=2026-04-15T18:01:11.3960000Z`; `69cdc907d385e3b94310f737.jsonl[675] _id=69dfd2687957a33870f42503 ts=2026-04-15T18:01:11.9100000Z`; `69cdc907d385e3b94310f737.jsonl[680] _id=69dfd26f7957a33870f42535 ts=2026-04-15T18:01:18.7600000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f737.jsonl[913] _id=69dfd9e57957a33870f4557f ts=2026-04-15T18:33:09.0120000Z`; `69cdc907d385e3b94310f737.jsonl[1423] _id=69e27c711724f0c9e2f780ce ts=2026-04-17T18:31:12.8880000Z`; `69cdc907d385e3b94310f737.jsonl[1454] _id=69e27d251724f0c9e2f7848a ts=2026-04-17T18:34:12.3190000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f737.jsonl[1714] _id=69e7b7391724f0c9e2f945eb ts=2026-04-21T17:43:21.0580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f737.jsonl[2232] _id=69ea66561724f0c9e2fb44d1 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 197 unmatched 'DialogueStartEvent' (totals: 320 start, 126 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 32 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.45s, min -106.42s, max -0.14s over 2250 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f737\coverage.yaml

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
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 23 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
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

### `DialogueEvent` — 1454 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (661); Unit 3 Dev (376); Unit 3 Dungeon Dev (225); Unit 1 Dev (184); Unit 4 Dev (8)
- **eventKey:** present on 1008 of 1454 records
- **Intervals:** median 2.92s (p5 0.01s / p95 46.79s, n=1453)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1008; [conversationId, dialogueEventType] x446
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1454/1454 records)
    numeric range 8 .. 104 (36 unique)
data.dialogueEventType  (string, 1454/1454 records)
    "DialogueNodeEvent"  x1008
    "DialogueStartEvent"  x320
    "DialogueFinishEvent"  x126
data.nodeId  (number, 1008/1454 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 639 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (249); Unit 3 Dev (213); Unit 3 Dungeon Dev (117); Unit 1 Dev (51); Unit 4 Dev (9)
- **Intervals:** median 30.00s (p5 29.96s / p95 30.88s, n=633)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 639/639 records)
data.position.x  (number, 639/639 records)
    numeric range -696.056 .. 2338.54 (256 unique)
data.position.y  (number, 639/639 records)
    numeric range -115.127 .. 155.365 (176 unique)
data.position.z  (number, 639/639 records)
    numeric range -1112.22 .. 1815.39 (256 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 51 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (15); Unit 1 Dev (12); Unit 3 Dungeon Dev (5); Unit 4 Dev (1)
- **eventKey:** present on 51 of 51 records
- **Intervals:** median 193.52s (p5 1.89s / p95 168347.23s, n=50)
- **`data` key-set variants:** [questEventType, questID, questName] x32; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 51/51 records)
    "questActiveEvent"  x32
    "questFinishEvent"  x19
data.questID  (string, 51/51 records)
    18 unique values (see csv/event_unique_values.csv)
data.questName  (string, 51/51 records)
    18 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/51 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 33 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (19); Unit 2 Prod (Refactor) (11); Unit 1 Dev (3)
- **Intervals:** median 7.73s (p5 1.72s / p95 154622.41s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "argumentationNodeAdd"  x21
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 33/33 records)
    "Unit 3 - Pollution Upstream"  x19
    "Unit 2 – Watershed"  x11
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 33/33 records)
    "B"  x7
    "A"  x6
    "C"  x4
    "I"  x4
    "II"  x3
    "1"  x2
    "2"  x2
    "3"  x2
    "4"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 23 records

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (11)
- **Intervals:** median 20.21s (p5 6.03s / p95 164162.99s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "MapOpenEvent"  x12
    "MapCloseEvent"  x11
data.featureUsed  (string, 23/23 records)
    "Map"  x23
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 20 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (10)
- **Intervals:** median 6.85s (p5 1.87s / p95 208907.50s, n=19)
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
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 20/20 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 20/20 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (10)
- **Intervals:** median 1.65s (p5 0.09s / p95 11.64s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x5
    "argumentationToolOpen"  x5
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x10
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Pollution Site Data"  x10
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 143.00s (p5 11.64s / p95 344583.63s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2)
- **Intervals:** median 225.41s (p5 2.92s / p95 412765.68s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 432328.60s (p5 352574.59s / p95 512082.62s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x1
data.type  (string, 1/1 records)
    "runtime_error"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*