# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7a7

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7a7
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7a7.jsonl
- **Records:** 2599 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7a7
- **Time span:** 2026-04-14T19:38:46.062000+00:00 .. 2026-04-24T20:03:30.674000+00:00 (240h 24m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7a7\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2599 records, 4 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 54 INFO, 5 NOT_TESTED, 33 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowUnfocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1694 | 65.18 | 1 | 4 | 1175 | 2026-04-14T19:39:04.295000+00:00 | 2026-04-24T19:59:57.274000+00:00 | 240h 20m |
| PlayerPositionEvent | 598 | 23.01 | 1 | 4 | 0 | 2026-04-14T19:38:46.062000+00:00 | 2026-04-24T20:03:30.674000+00:00 | 240h 24m |
| argumentationToolEvent | 62 | 2.39 | 1 | 2 | 0 | 2026-04-20T19:37:15.980000+00:00 | 2026-04-22T19:57:34.474000+00:00 | 48h 20m |
| questEvent | 61 | 2.35 | 1 | 4 | 61 | 2026-04-14T19:39:04.253000+00:00 | 2026-04-24T19:59:28.343000+00:00 | 240h 20m |
| Topographic Map Event | 60 | 2.31 | 1 | 3 | 0 | 2026-04-16T18:55:54.428000+00:00 | 2026-04-24T19:58:27.861000+00:00 | 193h 2m |
| argumentationNodeEvent | 54 | 2.08 | 1 | 3 | 0 | 2026-04-14T20:05:09.906000+00:00 | 2026-04-22T19:59:23.456000+00:00 | 191h 54m |
| TopographicMapEvent | 38 | 1.46 | 1 | 2 | 0 | 2026-04-16T19:26:20.003000+00:00 | 2026-04-24T19:58:24.690000+00:00 | 192h 32m |
| argumentationEvent | 13 | 0.5 | 1 | 3 | 0 | 2026-04-14T20:04:43.635000+00:00 | 2026-04-22T19:59:24.748000+00:00 | 191h 54m |
| Soil Key Puzzle | 11 | 0.42 | 1 | 2 | 0 | 2026-04-16T19:15:24.343000+00:00 | 2026-04-24T19:02:26.819000+00:00 | 191h 47m |
| crash | 6 | 0.23 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.08 | 1 | 2 | 0 | 2026-04-16T19:01:44.428000+00:00 | 2026-04-20T19:44:05.256000+00:00 | 96h 42m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 348140.828s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.006s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 273.182s median 
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
  - Observed: 4.595s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.504s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.813s median 
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
  - Observed: MainMenu; Transition; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 11 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 60 records this build 
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
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 6.9x vs baseline. 
  - Observed: 62 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[520] _id=69de9e767957a33870f3b5ad ts=2026-04-14T20:07:17.7410000Z`; `69cdc98ad385e3b94310f7a7.jsonl[588] _id=69e1315f1724f0c9e2f6959e ts=2026-04-16T18:58:38.6420000Z`; `69cdc98ad385e3b94310f7a7.jsonl[827] _id=69e139691724f0c9e2f6dd86 ts=2026-04-16T19:32:57.3130000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 60 records, TopographicMapEvent: 38 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1693 | 0.0 | 2.288 | 511.077 | 46.36 | 340987.694 | 0.12 | 461 | 4 |
| PlayerPositionEvent | 593 | 29.781 | 30.006 | 1459.325 | 37.346 | 340985.944 | 0.04 | 0 | 4 |
| argumentationToolEvent | 61 | 0.007 | 0.813 | 2852.762 | 23.438 | 173817.937 | 0.02 | 4 | 1 |
| questEvent | 60 | 0.004 | 197.908 | 14420.401 | 168439.154 | 341133.495 | 0.0 | 4 | 12 |
| Topographic Map Event | 59 | 0.528 | 13.266 | 11778.872 | 18903.329 | 343427.349 | 0.01 | 0 | 6 |
| argumentationNodeEvent | 53 | 0.902 | 6.504 | 13034.973 | 67488.199 | 347863.091 | 0.0 | 0 | 3 |
| TopographicMapEvent | 37 | 0.358 | 4.595 | 18733.1 | 171531.273 | 343698.252 | 0.0 | 0 | 5 |
| argumentationEvent | 12 | 0.093 | 53.71 | 57573.426 | 252056.44 | 347820.233 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 10 | 2.971 | 273.182 | 69042.248 | 343867.403 | 345004.631 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 348140.828 | 348140.828 | 348140.828 | 348140.828 | 348140.828 | 0.0 | 0 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[1771] _id=69e686a51724f0c9e2f8fcc5 ts=? == 69cdc98ad385e3b94310f7a7.jsonl[1916] _id=69e91c951724f0c9e2fa94af ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.006s (p5 29.96s, p95 37.35s, n=593) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `93ms: 69cdc98ad385e3b94310f7a7.jsonl[2115] _id=69e9289d1724f0c9e2fabf69 ts=2026-04-22T19:59:24.6550000Z ~ 69cdc98ad385e3b94310f7a7.jsonl[271] _id=69e9289d1724f0c9e2fabf6f ts=2026-04-22T19:59:24.7480000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `851ms: 69cdc98ad385e3b94310f7a7.jsonl[1567] _id=69e680c41724f0c9e2f8eb25 ts=2026-04-20T19:38:43.6580000Z ~ 69cdc98ad385e3b94310f7a7.jsonl[1570] _id=69e680c51724f0c9e2f8eb2b ts=2026-04-20T19:38:44.5090000Z`; `931ms: 69cdc98ad385e3b94310f7a7.jsonl[1570] _id=69e680c51724f0c9e2f8eb2b ts=2026-04-20T19:38:44.5090000Z ~ 69cdc98ad385e3b94310f7a7.jsonl[1571] _id=69e680c61724f0c9e2f8eb2f ts=2026-04-20T19:38:45.4400000Z`; `869ms: 69cdc98ad385e3b94310f7a7.jsonl[1569] _id=69e680c51724f0c9e2f8eb2d ts=2026-04-20T19:38:45.3600000Z ~ 69cdc98ad385e3b94310f7a7.jsonl[196] _id=69e680c61724f0c9e2f8eb33 ts=2026-04-20T19:38:46.2290000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc98ad385e3b94310f7a7.jsonl[1033] _id=69e141bc1724f0c9e2f712ec ts=2026-04-16T20:08:27.8200000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1049] _id=69e675b91724f0c9e2f8b91f ts=2026-04-20T18:51:35.5140000Z; 46h 57m: 69cdc98ad385e3b94310f7a7.jsonl[2184] _id=69e929a41724f0c9e2fac389 ts=2026-04-22T20:03:47.6830000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2200] _id=69ebbe011724f0c9e2fbb3e5 ts=2026-04-24T19:01:21.6240000Z; 46h 47m: 69cdc98ad385e3b94310f7a7.jsonl[12] _id=69de9ed57957a33870f3b70b ts=2026-04-14T20:08:51.9390000Z -> 69cdc98ad385e3b94310f7a7.jsonl[553] _id=69e130cb1724f0c9e2f69392 ts=2026-04-16T18:56:10.6420000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 461 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7a7.jsonl[1661] _id=69e682051724f0c9e2f8f0a1 ts=2026-04-20T19:44:05.2730000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1666] _id=69e682151724f0c9e2f8f0d9 ts=2026-04-20T19:44:05.273Z; 2ms: 69cdc98ad385e3b94310f7a7.jsonl[2127] _id=69e928ba1724f0c9e2fac014 ts=2026-04-22T19:59:53.4840000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2118] _id=69e928ba1724f0c9e2fac017 ts=2026-04-22T19:59:53.4860000Z; 2ms: 69cdc98ad385e3b94310f7a7.jsonl[603] _id=69e131aa1724f0c9e2f696bc ts=2026-04-16T18:59:53.7380000Z -> 69cdc98ad385e3b94310f7a7.jsonl[599] _id=69e131aa1724f0c9e2f696be ts=2026-04-16T18:59:53.7400000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 42m 
  - Evidence: 96h 42m: 69cdc98ad385e3b94310f7a7.jsonl[626] _id=69e132181724f0c9e2f698b8 ts=2026-04-16T19:01:44.4280000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1663] _id=69e682051724f0c9e2f8f09f ts=2026-04-20T19:44:05.2560000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc98ad385e3b94310f7a7.jsonl[1034] _id=69e141bb1724f0c9e2f712e8 ts=2026-04-16T20:08:27.0940000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1048] _id=69e675b61724f0c9e2f8b915 ts=2026-04-20T18:51:33.0380000Z; 46h 52m: 69cdc98ad385e3b94310f7a7.jsonl[2185] _id=69e929c71724f0c9e2fac419 ts=2026-04-22T20:04:23.3000000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2188] _id=69ebbcf11724f0c9e2fbb2c9 ts=2026-04-24T18:56:48.6030000Z; 46h 45m: 69cdc98ad385e3b94310f7a7.jsonl[538] _id=69de9ef07957a33870f3b73b ts=2026-04-14T20:09:19.3080000Z -> 69cdc98ad385e3b94310f7a7.jsonl[548] _id=69e130801724f0c9e2f692b4 ts=2026-04-16T18:54:56.0470000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc98ad385e3b94310f7a7.jsonl[1265] _id=69e67a7e1724f0c9e2f8cdf9 ts=2026-04-20T19:11:58.0860000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2209] _id=69ebbe2a1724f0c9e2fbb447 ts=2026-04-24T19:02:02.7170000Z; 95h 7m: 69cdc98ad385e3b94310f7a7.jsonl[904] _id=69e13ca21724f0c9e2f6fd32 ts=2026-04-16T19:46:41.8100000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1064] _id=69e676701724f0c9e2f8bb41 ts=2026-04-20T18:54:39.2670000Z; 29m 42s: 69cdc98ad385e3b94310f7a7.jsonl[700] _id=69e135501724f0c9e2f6acb6 ts=2026-04-16T19:15:27.3160000Z -> 69cdc98ad385e3b94310f7a7.jsonl[897] _id=69e13c461724f0c9e2f6fb12 ts=2026-04-16T19:45:09.3970000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 69cdc98ad385e3b94310f7a7.jsonl[883] _id=69e13b9d1724f0c9e2f6f84c ts=2026-04-16T19:42:21.2990000Z -> 69cdc98ad385e3b94310f7a7.jsonl[94] _id=69e679211724f0c9e2f8c7bb ts=2026-04-20T19:06:08.6480000Z; 48h 2m: 69cdc98ad385e3b94310f7a7.jsonl[242] _id=69e926b21724f0c9e2fab86f ts=2026-04-22T19:51:14.0750000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2551] _id=69ebca641724f0c9e2fbc843 ts=2026-04-24T19:54:12.0950000Z; 47h 33m: 69cdc98ad385e3b94310f7a7.jsonl[1785] _id=69e687331724f0c9e2f8ff21 ts=2026-04-20T20:06:11.0420000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1981] _id=69e923ee1724f0c9e2faaedf ts=2026-04-22T19:39:26.0900000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 69cdc98ad385e3b94310f7a7.jsonl[851] _id=69e13a951724f0c9e2f6f3da ts=2026-04-16T19:37:56.7300000Z -> 69cdc98ad385e3b94310f7a7.jsonl[95] _id=69e679271724f0c9e2f8c7d3 ts=2026-04-20T19:06:14.9820000Z; 48h 3m: 69cdc98ad385e3b94310f7a7.jsonl[241] _id=69e926af1724f0c9e2fab861 ts=2026-04-22T19:51:10.8200000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2548] _id=69ebca671724f0c9e2fbc849 ts=2026-04-24T19:54:15.7920000Z; 47h 32m: 69cdc98ad385e3b94310f7a7.jsonl[1786] _id=69e687321724f0c9e2f8ff1f ts=2026-04-20T20:06:10.0230000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1976] _id=69e923d21724f0c9e2faae7d ts=2026-04-22T19:38:57.8710000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 37m 
  - Evidence: 96h 37m: 69cdc98ad385e3b94310f7a7.jsonl[587] _id=69e1315f1724f0c9e2f6959c ts=2026-04-16T18:58:38.6230000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1534] _id=69e6800b1724f0c9e2f8e82d ts=2026-04-20T19:35:38.8560000Z; 48h 15m: 69cdc98ad385e3b94310f7a7.jsonl[1608] _id=69e6813b1724f0c9e2f8ed59 ts=2026-04-20T19:40:43.4290000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2057] _id=69e927c41724f0c9e2fabbe3 ts=2026-04-22T19:55:47.6740000Z; 46h 49m: 69cdc98ad385e3b94310f7a7.jsonl[512] _id=69de9e767957a33870f3b5ab ts=2026-04-14T20:07:17.7210000Z -> 69cdc98ad385e3b94310f7a7.jsonl[567] _id=69e130e61724f0c9e2f6940a ts=2026-04-16T18:56:37.7800000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 37m 
  - Evidence: 96h 37m: 69cdc98ad385e3b94310f7a7.jsonl[585] _id=69e131561724f0c9e2f6957e ts=2026-04-16T18:58:30.5690000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1543] _id=69e6802e1724f0c9e2f8e8af ts=2026-04-20T19:36:13.6600000Z; 48h 16m: 69cdc98ad385e3b94310f7a7.jsonl[1604] _id=69e6813a1724f0c9e2f8ed51 ts=2026-04-20T19:40:41.7650000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2068] _id=69e928091724f0c9e2fabcf1 ts=2026-04-22T19:56:57.4390000Z; 46h 49m: 69cdc98ad385e3b94310f7a7.jsonl[518] _id=69de9e6e7957a33870f3b58f ts=2026-04-14T20:07:09.8710000Z -> 69cdc98ad385e3b94310f7a7.jsonl[564] _id=69e130e91724f0c9e2f69412 ts=2026-04-16T18:56:40.9480000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 16m 
  - Evidence: 48h 16m: 69cdc98ad385e3b94310f7a7.jsonl[1581] _id=69e680e71724f0c9e2f8ebb9 ts=2026-04-20T19:39:18.8930000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2046] _id=69e927e11724f0c9e2fabc3f ts=2026-04-22T19:56:16.8300000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.007s..0.033s shown 
  - Evidence: 7ms: 69cdc98ad385e3b94310f7a7.jsonl[2074] _id=69e9282c1724f0c9e2fabd71 ts=2026-04-22T19:57:32.2220000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2075] _id=69e9282c1724f0c9e2fabd73 ts=2026-04-22T19:57:32.2290000Z; 8ms: 69cdc98ad385e3b94310f7a7.jsonl[193] _id=69e680c91724f0c9e2f8eb3f ts=2026-04-20T19:38:48.8060000Z -> 69cdc98ad385e3b94310f7a7.jsonl[194] _id=69e680c91724f0c9e2f8eb41 ts=2026-04-20T19:38:48.8140000Z; 33ms: 69cdc98ad385e3b94310f7a7.jsonl[255] _id=69e928061724f0c9e2fabcd5 ts=2026-04-22T19:56:54.2090000Z -> 69cdc98ad385e3b94310f7a7.jsonl[256] _id=69e928061724f0c9e2fabcd7 ts=2026-04-22T19:56:54.2420000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc98ad385e3b94310f7a7.jsonl[1024] _id=69e1412a1724f0c9e2f70ff0 ts=2026-04-16T20:06:02.6320000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1052] _id=69e675ba1724f0c9e2f8b923 ts=2026-04-20T18:51:36.1270000Z; 46h 57m: 69cdc98ad385e3b94310f7a7.jsonl[1762] _id=69e6851e1724f0c9e2f8faa5 ts=2026-04-20T19:57:17.7050000Z -> 69cdc98ad385e3b94310f7a7.jsonl[1841] _id=69e9195e1724f0c9e2fa86d7 ts=2026-04-22T18:54:21.5060000Z; 46h 56m: 69cdc98ad385e3b94310f7a7.jsonl[2139] _id=69e928dc1724f0c9e2fac0b0 ts=2026-04-22T20:00:28.2060000Z -> 69cdc98ad385e3b94310f7a7.jsonl[2189] _id=69ebbcf41724f0c9e2fbb2cb ts=2026-04-24T18:56:51.7800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.013s shown 
  - Evidence: 4ms: 69cdc98ad385e3b94310f7a7.jsonl[555] _id=69e130cb1724f0c9e2f69396 ts=2026-04-16T18:56:10.6780000Z -> 69cdc98ad385e3b94310f7a7.jsonl[558] _id=69e130cb1724f0c9e2f69398 ts=2026-04-16T18:56:10.6820000Z; 8ms: 69cdc98ad385e3b94310f7a7.jsonl[482] _id=69de9d847957a33870f3b243 ts=2026-04-14T20:03:15.7020000Z -> 69cdc98ad385e3b94310f7a7.jsonl[486] _id=69de9d847957a33870f3b245 ts=2026-04-14T20:03:15.7100000Z; 13ms: 69cdc98ad385e3b94310f7a7.jsonl[405] _id=69de9a717957a33870f3a43b ts=2026-04-14T19:50:08.4680000Z -> 69cdc98ad385e3b94310f7a7.jsonl[406] _id=69de9a717957a33870f3a43d ts=2026-04-14T19:50:08.4810000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc98ad385e3b94310f7a7.jsonl:69cdc98ad385e3b94310f7a7, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[700] _id=69e135501724f0c9e2f6acb6 ts=2026-04-16T19:15:27.3160000Z`; `69cdc98ad385e3b94310f7a7.jsonl[904] _id=69e13ca21724f0c9e2f6fd32 ts=2026-04-16T19:46:41.8100000Z`; `69cdc98ad385e3b94310f7a7.jsonl[1130] _id=69e678381724f0c9e2f8c353 ts=2026-04-20T19:02:16.1890000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 38 record(s) match the trigger in 69cdc98ad385e3b94310f7a7.jsonl:69cdc98ad385e3b94310f7a7, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[782] _id=69e137dc1724f0c9e2f6c8ca ts=2026-04-16T19:26:20.0030000Z`; `69cdc98ad385e3b94310f7a7.jsonl[783] _id=69e137df1724f0c9e2f6c8e8 ts=2026-04-16T19:26:22.9200000Z`; `69cdc98ad385e3b94310f7a7.jsonl[786] _id=69e138191724f0c9e2f6cb02 ts=2026-04-16T19:27:21.2720000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[1362] _id=69e67cb81724f0c9e2f8d811 ts=2026-04-20T19:21:27.7150000Z`; `69cdc98ad385e3b94310f7a7.jsonl[1743] _id=69e684821724f0c9e2f8f883 ts=2026-04-20T19:54:42.3650000Z`; `69cdc98ad385e3b94310f7a7.jsonl[1764] _id=69e6851e1724f0c9e2f8faaf ts=2026-04-20T19:57:17.7460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[271] _id=69e9289d1724f0c9e2fabf6f ts=2026-04-22T19:59:24.7480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[2065] _id=69e928031724f0c9e2fabcbd ts=2026-04-22T19:56:50.8630000Z`; `69cdc98ad385e3b94310f7a7.jsonl[255] _id=69e928061724f0c9e2fabcd5 ts=2026-04-22T19:56:54.2090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[2216] _id=69ebbe481724f0c9e2fbb46b ts=2026-04-24T19:02:32.1180000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[1771] _id=69e686a51724f0c9e2f8fcc5 ts=?`; `69cdc98ad385e3b94310f7a7.jsonl[1916] _id=69e91c951724f0c9e2fa94af ts=?`; `69cdc98ad385e3b94310f7a7.jsonl[946] _id=69e91f1b1724f0c9e2fa9e87 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[1129] _id=69e678351724f0c9e2f8c347 ts=2026-04-20T19:02:13.2180000Z`; `69cdc98ad385e3b94310f7a7.jsonl[1263] _id=69e67a4d1724f0c9e2f8cd5b ts=2026-04-20T19:11:09.2040000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7a7.jsonl[2066] _id=69e928051724f0c9e2fabcd1 ts=2026-04-22T19:56:52.9780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 228 unmatched 'DialogueStartEvent' (totals: 372 start, 147 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 31 open, 31 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 36 start, 25 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.52s, min -48.10s, max -0.17s over 2593 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7a7\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=partial, Unit4=skipped 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 60 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 6 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `TerasGardenBox` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **NOT_TESTED / NotTested** `soilMachine` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md

## 9. Event-Type Details

### `DialogueEvent` — 1694 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (836); Unit 3 Dev (413); Unit 3 Dungeon Dev (228); Unit 1 Dev (217)
- **eventKey:** present on 1175 of 1694 records
- **Intervals:** median 2.29s (p5 0.01s / p95 46.36s, n=1693)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1175; [conversationId, dialogueEventType] x519
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1694/1694 records)
    numeric range 8 .. 103 (34 unique)
data.dialogueEventType  (string, 1694/1694 records)
    "DialogueNodeEvent"  x1175
    "DialogueStartEvent"  x372
    "DialogueFinishEvent"  x147
data.nodeId  (number, 1175/1694 records)
    numeric range 0 .. 290 (219 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 598 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (227); Unit 3 Dev (211); Unit 3 Dungeon Dev (84); Unit 1 Dev (76)
- **Intervals:** median 30.01s (p5 29.96s / p95 37.35s, n=593)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 598/598 records)
data.position.x  (number, 598/598 records)
    numeric range -592.033 .. 1429.15 (265 unique)
data.position.y  (number, 598/598 records)
    numeric range -115.127 .. 155.843 (193 unique)
data.position.z  (number, 598/598 records)
    numeric range -1136.42 .. 1869.41 (264 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationToolEvent` — 62 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (28)
- **Intervals:** median 0.81s (p5 0.04s / p95 23.44s, n=61)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "argumentationToolClose"  x31
    "argumentationToolOpen"  x31
data.argumentationTitle  (string, 62/62 records)
    "Unit 2 – Watershed"  x34
    "Unit 3 - Pollution Upstream"  x28
data.toolName  (string, 62/62 records)
    "BackingInfoPanel - Pollution Site Data"  x24
    "BackingInfoPanel - Waterfall Data"  x24
    "BackingInfoPanel - Watershed Graph"  x10
    "BackingInfoPanel - "  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `questEvent` — 61 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 1 Dev (17); Unit 3 Dev (15); Unit 3 Dungeon Dev (6)
- **eventKey:** present on 61 of 61 records
- **Intervals:** median 197.91s (p5 0.01s / p95 168439.15s, n=60)
- **`data` key-set variants:** [questEventType, questID, questName] x36; [questEventType, questID, questName, questSuccessOrFailure] x25
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 61/61 records)
    "questActiveEvent"  x36
    "questFinishEvent"  x25
data.questID  (string, 61/61 records)
    16 unique values (see csv/event_unique_values.csv)
data.questName  (string, 61/61 records)
    16 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 25/61 records)
    "Succeeded"  x25
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 60 records

- **Scenes:** Unit 3 Dev (30); Unit 2 Prod (Refactor) (28); Unit 1 Dev (2)
- **Intervals:** median 13.27s (p5 0.83s / p95 18903.33s, n=59)
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "MapCloseEvent"  x30
    "MapOpenEvent"  x30
data.featureUsed  (string, 60/60 records)
    "Map"  x60
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 54 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 3 Dev (15); Unit 1 Dev (12)
- **Intervals:** median 6.50s (p5 1.26s / p95 67488.20s, n=53)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "argumentationNodeAdd"  x35
    "argumentationNodeRemove"  x19
data.argumentationTitle  (string, 54/54 records)
    "Unit 2 – Watershed"  x27
    "Unit 3 - Pollution Upstream"  x15
    "Unit 1 - Freshwater"  x8
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 54/54 records)
    "1"  x13
    "II"  x9
    "I"  x8
    "A"  x7
    "B"  x4
    "D"  x4
    "2"  x2
    "3"  x2
    "4"  x2
    "C"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 38 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (14)
- **Intervals:** median 4.59s (p5 1.11s / p95 171531.27s, n=37)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "dragEnd"  x19
    "dragStart"  x19
data.featureUsed  (string, 38/38 records)
    "waypoint"  x38
data.location  (object, 38/38 records)
data.location.x  (number, 38/38 records)
    numeric range -800.585 .. 427.043 (20 unique)
data.location.y  (number, 38/38 records)
    numeric range -325.845 .. 172.014 (19 unique)
data.location.z  (number, 38/38 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 53.71s (p5 13.25s / p95 252056.44s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 11 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (2)
- **Intervals:** median 273.18s (p5 2.97s / p95 343867.40s, n=10)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/11 records)
    "Started"  x6
    "Finished"  x5
data.Unit  (string, 11/11 records)
    "Unit 2 Prod (Refactor)"  x9
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "Uncaught ReferenceError: onResize is not defined"  x5
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 1 empty-string)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x5
    ""  x1
data.type  (string, 6/6 records)
    "runtime_error"  x5
    "unhandled_rejection"  x1
data.unitId  (string, 6/6 records)
    "unit3"  x6
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 348140.83s (p5 348140.83s / p95 348140.83s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "2"  x1
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
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `crash` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (9 records)
- `TopographicMapEvent` data.actionType: "dragStart" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (19x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*