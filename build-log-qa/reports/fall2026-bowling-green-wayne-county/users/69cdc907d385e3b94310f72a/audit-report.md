# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72a
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f72a.jsonl
- **Records:** 2809 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f72a
- **Time span:** 2026-04-13T18:04:30.489000+00:00 .. 2026-04-23T18:41:19.290000+00:00 (240h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2809 records, 6 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 55 INFO, 2 NOT_TESTED, 34 PASS.
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
| DialogueEvent | 1952 | 69.49 | 1 | 6 | 1377 | 2026-04-13T18:04:49.223000+00:00 | 2026-04-23T18:41:19.290000+00:00 | 240h 36m |
| PlayerPositionEvent | 574 | 20.43 | 1 | 6 | 0 | 2026-04-13T18:04:30.489000+00:00 | 2026-04-23T18:41:13.471000+00:00 | 240h 36m |
| argumentationNodeEvent | 111 | 3.95 | 1 | 3 | 0 | 2026-04-13T18:21:31.199000+00:00 | 2026-04-21T18:07:43.695000+00:00 | 191h 46m |
| Topographic Map Event | 66 | 2.35 | 1 | 2 | 0 | 2026-04-15T17:58:26.069000+00:00 | 2026-04-21T18:05:06.243000+00:00 | 144h 6m |
| questEvent | 61 | 2.17 | 1 | 5 | 61 | 2026-04-13T18:04:49.190000+00:00 | 2026-04-23T18:38:27.793000+00:00 | 240h 33m |
| argumentationEvent | 14 | 0.5 | 1 | 3 | 0 | 2026-04-13T18:20:40.555000+00:00 | 2026-04-21T18:07:45.996000+00:00 | 191h 47m |
| TopographicMapEvent | 13 | 0.46 | 1 | 2 | 0 | 2026-04-15T17:58:41.866000+00:00 | 2026-04-21T18:02:49.704000+00:00 | 144h 4m |
| Soil Key Puzzle | 8 | 0.28 | 1 | 3 | 0 | 2026-04-13T18:36:03.180000+00:00 | 2026-04-23T18:39:51.321000+00:00 | 240h 3m |
| EndOfUnit | 6 | 0.21 | 1 | 3 | 0 | 2026-04-13T18:25:37.722000+00:00 | 2026-04-23T18:34:58.903000+00:00 | 240h 9m |
| argumentationToolEvent | 2 | 0.07 | 1 | 1 | 0 | 2026-04-17T18:38:22.964000+00:00 | 2026-04-17T18:38:28.290000+00:00 | 5.3s |
| crash | 2 | 0.07 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.399s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173619.175s median 
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
  - Observed: 47.176s median 
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
  - Observed: 28.292s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 2.04s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 5.326s median 
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
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
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
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 66 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
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
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
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
  - Observed: 11 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[568] _id=69dd347b7957a33870f274d4 ts=2026-04-13T18:22:50.7510000Z`; `69cdc907d385e3b94310f72a.jsonl[776] _id=69dfcfae7957a33870f41021 ts=2026-04-15T17:49:33.5650000Z`; `69cdc907d385e3b94310f72a.jsonl[837] _id=69dfd2257957a33870f422aa ts=2026-04-15T18:00:02.2550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[1205] _id=69e265a81724f0c9e2f71f30 ts=2026-04-17T16:53:59.1250000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 66 records, TopographicMapEvent: 13 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1951 | 0.0 | 1.399 | 443.972 | 27.773 | 339274.101 | 0.14 | 498 | 9 |
| PlayerPositionEvent | 565 | 29.699 | 30.01 | 1532.256 | 42.436 | 339240.395 | 0.04 | 0 | 5 |
| argumentationNodeEvent | 110 | 0.829 | 2.04 | 6276.114 | 12.652 | 339805.713 | 0.01 | 0 | 4 |
| Topographic Map Event | 65 | 0.209 | 14.447 | 7981.541 | 2422.125 | 341918.737 | 0.01 | 0 | 5 |
| questEvent | 60 | 0.001 | 124.395 | 14433.643 | 166563.287 | 342141.475 | 0.0 | 7 | 12 |
| argumentationEvent | 13 | 0.1 | 33.529 | 53109.649 | 240132.622 | 339946.652 | 0.0 | 0 | 4 |
| TopographicMapEvent | 12 | 1.704 | 28.292 | 43220.653 | 249918.718 | 348357.331 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 7 | 2.987 | 47.176 | 123461.163 | 345861.699 | 347351.951 | 0.0 | 0 | 3 |
| EndOfUnit | 5 | 0.0 | 173619.175 | 172912.236 | 446981.57 | 514655.282 | 0.0 | 2 | 3 |
| argumentationToolEvent | 1 | 5.326 | 5.326 | 5.326 | 5.326 | 5.326 | 11.27 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.010s (p5 29.96s, p95 42.44s, n=565) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc907d385e3b94310f72a.jsonl[620] _id=69dd35217957a33870f278de ts=2026-04-13T18:25:37.7220000Z ~ 69cdc907d385e3b94310f72a.jsonl[621] _id=69dd35357957a33870f27970 ts=2026-04-13T18:25:37.722Z`; `0ms: 69cdc907d385e3b94310f72a.jsonl[1182] _id=69dfdb557957a33870f4638d ts=2026-04-15T18:39:16.8970000Z ~ 69cdc907d385e3b94310f72a.jsonl[1179] _id=69dfdb677957a33870f46423 ts=2026-04-15T18:39:16.897Z`
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `438ms: 69cdc907d385e3b94310f72a.jsonl[1676] _id=69e274fd1724f0c9e2f75e44 ts=2026-04-17T17:59:25.3910000Z ~ 69cdc907d385e3b94310f72a.jsonl[1678] _id=69e274fe1724f0c9e2f75e48 ts=2026-04-17T17:59:25.8290000Z`; `731ms: 69cdc907d385e3b94310f72a.jsonl[1677] _id=69e274fe1724f0c9e2f75e46 ts=2026-04-17T17:59:25.6000000Z ~ 69cdc907d385e3b94310f72a.jsonl[1679] _id=69e274fe1724f0c9e2f75e4e ts=2026-04-17T17:59:26.3310000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `100ms: 69cdc907d385e3b94310f72a.jsonl[312] _id=69e7bcf21724f0c9e2f96deb ts=2026-04-21T18:07:45.8960000Z ~ 69cdc907d385e3b94310f72a.jsonl[2343] _id=69e7bcf21724f0c9e2f96df1 ts=2026-04-21T18:07:45.9960000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc907d385e3b94310f72a.jsonl[1205] _id=69e265a81724f0c9e2f71f30 ts=2026-04-17T16:53:59.1250000Z ~ 69cdc907d385e3b94310f72a.jsonl[1204] _id=69e265a81724f0c9e2f71f34 ts=2026-04-17T16:53:59.1260000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 14m 
  - Evidence: 94h 14m: 69cdc907d385e3b94310f72a.jsonl[1861] _id=69e27e671724f0c9e2f78c7c ts=2026-04-17T18:39:35.4210000Z -> 69cdc907d385e3b94310f72a.jsonl[1882] _id=69e7abb11724f0c9e2f91517 ts=2026-04-21T16:54:09.5220000Z; 47h 22m: 69cdc907d385e3b94310f72a.jsonl[2515] _id=69e7c41b1724f0c9e2f9a463 ts=2026-04-21T18:38:18.7590000Z -> 69cdc907d385e3b94310f72a.jsonl[2522] _id=69ea5e3f1724f0c9e2fb04b9 ts=2026-04-23T18:00:30.2550000Z; 47h 8m: 69cdc907d385e3b94310f72a.jsonl[623] _id=69dd38467957a33870f28ec0 ts=2026-04-13T18:39:02.1520000Z -> 69cdc907d385e3b94310f72a.jsonl[753] _id=69dfcf4d7957a33870f40dc1 ts=2026-04-15T17:47:57.3330000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 498 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72a.jsonl[2083] _id=69e7b5b41724f0c9e2f939d9 ts=2026-04-21T17:36:52.1950000Z -> 69cdc907d385e3b94310f72a.jsonl[2085] _id=69e7b5c31724f0c9e2f93ab9 ts=2026-04-21T17:36:52.195Z; 2ms: 69cdc907d385e3b94310f72a.jsonl[602] _id=69dd34d87957a33870f276ee ts=2026-04-13T18:24:24.4270000Z -> 69cdc907d385e3b94310f72a.jsonl[604] _id=69dd34d87957a33870f276f0 ts=2026-04-13T18:24:24.4290000Z; 3ms: 69cdc907d385e3b94310f72a.jsonl[1148] _id=69dfdb0b7957a33870f4614d ts=2026-04-15T18:38:02.8160000Z -> 69cdc907d385e3b94310f72a.jsonl[1166] _id=69dfdb0b7957a33870f46151 ts=2026-04-15T18:38:02.8190000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 142h 57m 
  - Evidence: 142h 57m: 69cdc907d385e3b94310f72a.jsonl[1179] _id=69dfdb677957a33870f46423 ts=2026-04-15T18:39:16.897Z -> 69cdc907d385e3b94310f72a.jsonl[2082] _id=69e7b5b41724f0c9e2f939d5 ts=2026-04-21T17:36:52.1790000Z; 48h 58m: 69cdc907d385e3b94310f72a.jsonl[2082] _id=69e7b5b41724f0c9e2f939d5 ts=2026-04-21T17:36:52.1790000Z -> 69cdc907d385e3b94310f72a.jsonl[2762] _id=69ea66531724f0c9e2fb44bb ts=2026-04-23T18:34:58.9030000Z; 48h 13m: 69cdc907d385e3b94310f72a.jsonl[621] _id=69dd35357957a33870f27970 ts=2026-04-13T18:25:37.722Z -> 69cdc907d385e3b94310f72a.jsonl[1182] _id=69dfdb557957a33870f4638d ts=2026-04-15T18:39:16.8970000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72a.jsonl[1182] _id=69dfdb557957a33870f4638d ts=2026-04-15T18:39:16.8970000Z -> 69cdc907d385e3b94310f72a.jsonl[1179] _id=69dfdb677957a33870f46423 ts=2026-04-15T18:39:16.897Z; 0ms: 69cdc907d385e3b94310f72a.jsonl[620] _id=69dd35217957a33870f278de ts=2026-04-13T18:25:37.7220000Z -> 69cdc907d385e3b94310f72a.jsonl[621] _id=69dd35357957a33870f27970 ts=2026-04-13T18:25:37.722Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 14m 
  - Evidence: 94h 14m: 69cdc907d385e3b94310f72a.jsonl[1865] _id=69e27e781724f0c9e2f78cc4 ts=2026-04-17T18:39:51.7960000Z -> 69cdc907d385e3b94310f72a.jsonl[1877] _id=69e7aba11724f0c9e2f91513 ts=2026-04-21T16:53:52.1910000Z; 47h 20m: 69cdc907d385e3b94310f72a.jsonl[2520] _id=69e7c47c1724f0c9e2f9a6fb ts=2026-04-21T18:39:55.9620000Z -> 69cdc907d385e3b94310f72a.jsonl[2525] _id=69ea5e3d1724f0c9e2fb04b1 ts=2026-04-23T18:00:28.3230000Z; 47h 7m: 69cdc907d385e3b94310f72a.jsonl[746] _id=69dd38b37957a33870f2917a ts=2026-04-13T18:40:50.9700000Z -> 69cdc907d385e3b94310f72a.jsonl[750] _id=69dfcf497957a33870f40d9d ts=2026-04-15T17:47:53.2370000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 29m 
  - Evidence: 96h 29m: 69cdc907d385e3b94310f72a.jsonl[1469] _id=69e2712a1724f0c9e2f74438 ts=2026-04-17T17:43:06.2070000Z -> 69cdc907d385e3b94310f72a.jsonl[2380] _id=69e7be021724f0c9e2f974d9 ts=2026-04-21T18:12:18.1580000Z; 95h 6m: 69cdc907d385e3b94310f72a.jsonl[703] _id=69dd37967957a33870f289a2 ts=2026-04-13T18:36:06.1670000Z -> 69cdc907d385e3b94310f72a.jsonl[1464] _id=69e271071724f0c9e2f74366 ts=2026-04-17T17:42:30.6100000Z; 48h 26m: 69cdc907d385e3b94310f72a.jsonl[2382] _id=69e7be311724f0c9e2f975ed ts=2026-04-21T18:13:05.3340000Z -> 69cdc907d385e3b94310f72a.jsonl[2793] _id=69ea67621724f0c9e2fb4c1f ts=2026-04-23T18:39:29.5450000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 58m 
  - Evidence: 94h 58m: 69cdc907d385e3b94310f72a.jsonl[1687] _id=69e275671724f0c9e2f760fc ts=2026-04-17T18:01:10.7280000Z -> 69cdc907d385e3b94310f72a.jsonl[1931] _id=69e7ad051724f0c9e2f91b07 ts=2026-04-21T16:59:49.4650000Z; 46h 38m: 69cdc907d385e3b94310f72a.jsonl[989] _id=69dfd7787957a33870f443cb ts=2026-04-15T18:22:48.2090000Z -> 69cdc907d385e3b94310f72a.jsonl[1310] _id=69e2676f1724f0c9e2f72be2 ts=2026-04-17T17:01:34.5100000Z; 52m 35s: 69cdc907d385e3b94310f72a.jsonl[1932] _id=69e7ad0a1724f0c9e2f91b23 ts=2026-04-21T16:59:53.8700000Z -> 69cdc907d385e3b94310f72a.jsonl[2199] _id=69e7b95e1724f0c9e2f953a9 ts=2026-04-21T17:52:29.7370000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 45m 
  - Evidence: 96h 45m: 69cdc907d385e3b94310f72a.jsonl[1379] _id=69e268a41724f0c9e2f735fa ts=2026-04-17T17:06:44.0630000Z -> 69cdc907d385e3b94310f72a.jsonl[2201] _id=69e7b9691724f0c9e2f953e7 ts=2026-04-21T17:52:41.3940000Z; 47h 2m: 69cdc907d385e3b94310f72a.jsonl[863] _id=69dfd1d27957a33870f41fe3 ts=2026-04-15T17:58:41.8660000Z -> 69cdc907d385e3b94310f72a.jsonl[1311] _id=69e267741724f0c9e2f72c11 ts=2026-04-17T17:01:39.9000000Z; 10m 4s: 69cdc907d385e3b94310f72a.jsonl[2202] _id=69e7b96b1724f0c9e2f953eb ts=2026-04-21T17:52:43.0980000Z -> 69cdc907d385e3b94310f72a.jsonl[2264] _id=69e7bbc81724f0c9e2f96553 ts=2026-04-21T18:02:47.8230000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 25m 
  - Evidence: 94h 25m: 69cdc907d385e3b94310f72a.jsonl[1794] _id=69e27dd41724f0c9e2f788ba ts=2026-04-17T18:37:07.9770000Z -> 69cdc907d385e3b94310f72a.jsonl[1990] _id=69e7adbf1724f0c9e2f92065 ts=2026-04-21T17:02:54.6290000Z; 48h 13m: 69cdc907d385e3b94310f72a.jsonl[572] _id=69dd347a7957a33870f274d1 ts=2026-04-13T18:22:50.7250000Z -> 69cdc907d385e3b94310f72a.jsonl[64] _id=69dfda907957a33870f45e0b ts=2026-04-15T18:36:00.6600000Z; 48h 0m: 69cdc907d385e3b94310f72a.jsonl[108] _id=69dfdaaf7957a33870f45ef3 ts=2026-04-15T18:36:31.2170000Z -> 69cdc907d385e3b94310f72a.jsonl[1794] _id=69e27dd41724f0c9e2f788ba ts=2026-04-17T18:37:07.9770000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 23m 
  - Evidence: 94h 23m: 69cdc907d385e3b94310f72a.jsonl[236] _id=69e27e641724f0c9e2f78c6e ts=2026-04-17T18:39:31.7430000Z -> 69cdc907d385e3b94310f72a.jsonl[1992] _id=69e7adc11724f0c9e2f92075 ts=2026-04-21T17:02:57.4560000Z; 48h 13m: 69cdc907d385e3b94310f72a.jsonl[570] _id=69dd34797957a33870f274c0 ts=2026-04-13T18:22:49.0320000Z -> 69cdc907d385e3b94310f72a.jsonl[1132] _id=69dfda9c7957a33870f45e65 ts=2026-04-15T18:36:12.6550000Z; 48h 0m: 69cdc907d385e3b94310f72a.jsonl[1137] _id=69dfdaab7957a33870f45edb ts=2026-04-15T18:36:27.2610000Z -> 69cdc907d385e3b94310f72a.jsonl[1797] _id=69e27dd61724f0c9e2f788cc ts=2026-04-17T18:37:10.2340000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 2m 
  - Evidence: 95h 2m: 69cdc907d385e3b94310f72a.jsonl[1570] _id=69e273261724f0c9e2f7521c ts=2026-04-17T17:51:34.0510000Z -> 69cdc907d385e3b94310f72a.jsonl[1874] _id=69e7aba41724f0c9e2f91515 ts=2026-04-21T16:53:55.5260000Z; 47h 28m: 69cdc907d385e3b94310f72a.jsonl[2473] _id=69e7c2961724f0c9e2f99915 ts=2026-04-21T18:31:49.9020000Z -> 69cdc907d385e3b94310f72a.jsonl[2521] _id=69ea5e3e1724f0c9e2fb04b7 ts=2026-04-23T18:00:29.7760000Z; 47h 8m: 69cdc907d385e3b94310f72a.jsonl[742] _id=69dd38457957a33870f28ebc ts=2026-04-13T18:39:01.1720000Z -> 69cdc907d385e3b94310f72a.jsonl[752] _id=69dfcf4c7957a33870f40dbb ts=2026-04-15T17:47:55.7570000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 69cdc907d385e3b94310f72a.jsonl[1205] _id=69e265a81724f0c9e2f71f30 ts=2026-04-17T16:53:59.1250000Z -> 69cdc907d385e3b94310f72a.jsonl[1204] _id=69e265a81724f0c9e2f71f34 ts=2026-04-17T16:53:59.1260000Z; 3ms: 69cdc907d385e3b94310f72a.jsonl[1130] _id=69dfda8c7957a33870f45ddb ts=2026-04-15T18:35:55.7400000Z -> 69cdc907d385e3b94310f72a.jsonl[1128] _id=69dfda8c7957a33870f45ddf ts=2026-04-15T18:35:55.7430000Z; 4ms: 69cdc907d385e3b94310f72a.jsonl[519] _id=69dd33d67957a33870f270ae ts=2026-04-13T18:20:05.5190000Z -> 69cdc907d385e3b94310f72a.jsonl[522] _id=69dd33d67957a33870f270b0 ts=2026-04-13T18:20:05.5230000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f72a.jsonl:69cdc907d385e3b94310f72a, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[703] _id=69dd37967957a33870f289a2 ts=2026-04-13T18:36:06.1670000Z`; `69cdc907d385e3b94310f72a.jsonl[1469] _id=69e2712a1724f0c9e2f74438 ts=2026-04-17T17:43:06.2070000Z`; `69cdc907d385e3b94310f72a.jsonl[2382] _id=69e7be311724f0c9e2f975ed ts=2026-04-21T18:13:05.3340000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 13 record(s) match the trigger in 69cdc907d385e3b94310f72a.jsonl:69cdc907d385e3b94310f72a, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[863] _id=69dfd1d27957a33870f41fe3 ts=2026-04-15T17:58:41.8660000Z`; `69cdc907d385e3b94310f72a.jsonl[1311] _id=69e267741724f0c9e2f72c11 ts=2026-04-17T17:01:39.9000000Z`; `69cdc907d385e3b94310f72a.jsonl[1313] _id=69e267761724f0c9e2f72c28 ts=2026-04-17T17:01:42.0860000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[1574] _id=69e2733b1724f0c9e2f75295 ts=2026-04-17T17:51:55.4290000Z`; `69cdc907d385e3b94310f72a.jsonl[2126] _id=69e7b7d41724f0c9e2f94a03 ts=2026-04-21T17:45:56.5620000Z`; `69cdc907d385e3b94310f72a.jsonl[2149] _id=69e7b80a1724f0c9e2f94bc1 ts=2026-04-21T17:46:49.8280000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[2343] _id=69e7bcf21724f0c9e2f96df1 ts=2026-04-21T18:07:45.9960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[2077] _id=69e7b5b51724f0c9e2f939f7 ts=?`; `69cdc907d385e3b94310f72a.jsonl[364] _id=69ea66551724f0c9e2fb44c7 ts=?`
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f72a.jsonl[1990] _id=69e7adbf1724f0c9e2f92065 ts=2026-04-21T17:02:54.6290000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 226 unmatched 'DialogueStartEvent' (totals: 399 start, 176 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 35 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.42s, min -20.06s, max -0.12s over 2807 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72a\coverage.yaml

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
  - Observed: 66 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `DialogueEvent` — 1952 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (975); Unit 1 Dev (404); Unit 3 Dev (351); Unit 3 Dungeon Dev (195); Unit 4 Dev (21); Unit 4 Dev - Dungeon (6)
- **eventKey:** present on 1377 of 1952 records
- **Intervals:** median 1.40s (p5 0.01s / p95 27.77s, n=1951)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1377; [conversationId, dialogueEventType] x575
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1952/1952 records)
    numeric range 8 .. 104 (36 unique)
data.dialogueEventType  (string, 1952/1952 records)
    "DialogueNodeEvent"  x1377
    "DialogueStartEvent"  x399
    "DialogueFinishEvent"  x176
data.nodeId  (number, 1377/1952 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 574 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (310); Unit 3 Dungeon Dev (104); Unit 3 Dev (82); Unit 1 Dev (65); Unit 4 Dev (12); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 30.01s (p5 29.96s / p95 42.44s, n=565)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 574/574 records)
data.position.x  (number, 574/574 records)
    numeric range -722.347 .. 3017.67 (283 unique)
data.position.y  (number, 574/574 records)
    numeric range -334700 .. 471.489 (208 unique)
data.position.z  (number, 574/574 records)
    numeric range -1118.21 .. 2194.28 (283 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 111 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (82); Unit 1 Dev (24); Unit 3 Dev (5)
- **Intervals:** median 2.04s (p5 0.96s / p95 12.65s, n=110)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 111/111 records)
    "argumentationNodeAdd"  x63
    "argumentationNodeRemove"  x48
data.argumentationTitle  (string, 111/111 records)
    "Unit 2 – Watershed"  x82
    "Unit 1 - Freshwater"  x24
    "Unit 3 - Pollution Upstream"  x5
data.nodeName  (string, 111/111 records)
    "B"  x29
    "A"  x18
    "C"  x18
    "D"  x16
    "1"  x12
    "I"  x9
    "II"  x8
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 66 records

- **Scenes:** Unit 2 Prod (Refactor) (60); Unit 3 Dev (6)
- **Intervals:** median 14.45s (p5 0.54s / p95 2422.13s, n=65)
- **Fields under `data`:**

```text
data.actionType  (string, 66/66 records)
    "MapCloseEvent"  x33
    "MapOpenEvent"  x33
data.featureUsed  (string, 66/66 records)
    "Map"  x66
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 61 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 2 Prod (Refactor) (22); Unit 3 Dev (9); Unit 3 Dungeon Dev (5); Unit 4 Dev (1)
- **eventKey:** present on 61 of 61 records
- **Intervals:** median 124.39s (p5 0.01s / p95 166563.29s, n=60)
- **`data` key-set variants:** [questEventType, questID, questName] x35; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 61/61 records)
    "questActiveEvent"  x35
    "questFinishEvent"  x26
data.questID  (string, 61/61 records)
    18 unique values (see csv/event_unique_values.csv)
data.questName  (string, 61/61 records)
    18 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/61 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3)
- **Intervals:** median 33.53s (p5 1.22s / p95 240132.62s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 14/14 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TopographicMapEvent` — 13 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (4)
- **Intervals:** median 28.29s (p5 1.80s / p95 249918.72s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "dragStart"  x7
    "dragEnd"  x6
data.featureUsed  (string, 13/13 records)
    "waypoint"  x13
data.location  (object, 13/13 records)
data.location.x  (number, 13/13 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 13/13 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 13/13 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 47.18s (p5 8.62s / p95 345861.70s, n=7)
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

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 173619.17s (p5 0.00s / p95 446981.57s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "1"  x4
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 5.33s (p5 5.33s / p95 5.33s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 2 – Watershed"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Cannot close a closed AudioContext."  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x1
    "unit3"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (4 records)
- `TopographicMapEvent` data.actionType: "dragStart" (7x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (48x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*