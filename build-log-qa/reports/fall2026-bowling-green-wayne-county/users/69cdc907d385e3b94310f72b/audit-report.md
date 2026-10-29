# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72b
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f72b.jsonl
- **Records:** 1517 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f72b
- **Time span:** 2026-04-13T18:06:03.529000+00:00 .. 2026-04-23T18:40:35.317000+00:00 (240h 34m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1517 records, 6 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 54 INFO, 2 NOT_TESTED, 33 PASS.
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
| DialogueEvent | 959 | 63.22 | 1 | 6 | 666 | 2026-04-13T18:06:21.853000+00:00 | 2026-04-23T18:39:30.212000+00:00 | 240h 33m |
| PlayerPositionEvent | 395 | 26.04 | 1 | 6 | 0 | 2026-04-13T18:06:03.529000+00:00 | 2026-04-23T18:40:35.317000+00:00 | 240h 34m |
| questEvent | 41 | 2.7 | 1 | 6 | 41 | 2026-04-13T18:06:21.839000+00:00 | 2026-04-23T18:38:29.929000+00:00 | 240h 32m |
| Topographic Map Event | 32 | 2.11 | 1 | 2 | 0 | 2026-04-15T18:09:59.360000+00:00 | 2026-04-23T18:25:03.011000+00:00 | 192h 15m |
| TopographicMapEvent | 30 | 1.98 | 1 | 2 | 0 | 2026-04-15T18:12:27.657000+00:00 | 2026-04-23T18:20:47.307000+00:00 | 192h 8m |
| argumentationToolEvent | 22 | 1.45 | 1 | 1 | 0 | 2026-04-21T18:05:58.641000+00:00 | 2026-04-21T18:11:04.754000+00:00 | 5m 6s |
| argumentationNodeEvent | 19 | 1.25 | 1 | 2 | 0 | 2026-04-13T18:30:59.039000+00:00 | 2026-04-21T18:13:53.776000+00:00 | 191h 42m |
| Soil Key Puzzle | 9 | 0.59 | 1 | 3 | 0 | 2026-04-15T18:30:08.020000+00:00 | 2026-04-23T18:32:50.697000+00:00 | 192h 2m |
| argumentationEvent | 7 | 0.46 | 1 | 2 | 0 | 2026-04-13T18:30:46.090000+00:00 | 2026-04-21T18:13:56.249000+00:00 | 191h 43m |
| EndOfUnit | 2 | 0.13 | 1 | 2 | 0 | 2026-04-13T18:36:31.980000+00:00 | 2026-04-23T18:27:14.169000+00:00 | 239h 50m |
| crash | 1 | 0.07 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863442.189s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.007s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2401.7s median 
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
  - Observed: 3.78s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 13.318s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.613s median 
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
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 395 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 9 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 32 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 19 records 
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
  - Observed: 2; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 36; 40; 41; 43; 44; 45; 48; 49; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[280] _id=69dd36d97957a33870f2854c ts=2026-04-13T18:32:57.1310000Z`; `69cdc907d385e3b94310f72b.jsonl[12] _id=69dfd5b07957a33870f438fb ts=2026-04-15T18:15:11.3640000Z`; `69cdc907d385e3b94310f72b.jsonl[1044] _id=69e7be641724f0c9e2f97741 ts=2026-04-21T18:13:56.2010000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 32 records, TopographicMapEvent: 30 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 958 | 0.0 | 3.253 | 903.954 | 63.138 | 345411.78 | 0.07 | 253 | 5 |
| PlayerPositionEvent | 388 | 29.844 | 30.007 | 2226.722 | 33.43 | 345331.829 | 0.03 | 0 | 4 |
| questEvent | 40 | 0.003 | 234.964 | 21648.202 | 169742.177 | 345447.18 | 0.0 | 4 | 11 |
| Topographic Map Event | 31 | 1.361 | 20.928 | 22325.924 | 170898.78 | 348852.978 | 0.0 | 0 | 3 |
| TopographicMapEvent | 29 | 0.444 | 3.78 | 23851.712 | 104897.934 | 515958.901 | 0.0 | 0 | 2 |
| argumentationToolEvent | 21 | 0.015 | 0.613 | 14.577 | 52.999 | 217.356 | 4.12 | 4 | 0 |
| argumentationNodeEvent | 18 | 1.412 | 13.318 | 38343.041 | 103599.491 | 689476.835 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 8 | 25.605 | 2401.7 | 86420.335 | 285377.393 | 345555.447 | 0.0 | 0 | 4 |
| argumentationEvent | 6 | 0.072 | 52.672 | 115031.693 | 517201.193 | 689372.854 | 0.0 | 0 | 2 |
| EndOfUnit | 1 | 863442.189 | 863442.189 | 863442.189 | 863442.189 | 863442.189 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.007s (p5 29.96s, p95 33.43s, n=388) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `72ms: 69cdc907d385e3b94310f72b.jsonl[1047] _id=69e7be641724f0c9e2f9773d ts=2026-04-21T18:13:56.1770000Z ~ 69cdc907d385e3b94310f72b.jsonl[30] _id=69e7be651724f0c9e2f97747 ts=2026-04-21T18:13:56.2490000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `673ms: 69cdc907d385e3b94310f72b.jsonl[1014] _id=69e7bd7a1724f0c9e2f97147 ts=2026-04-21T18:10:01.9520000Z ~ 69cdc907d385e3b94310f72b.jsonl[1015] _id=69e7bd7b1724f0c9e2f97151 ts=2026-04-21T18:10:02.6250000Z`; `628ms: 69cdc907d385e3b94310f72b.jsonl[1018] _id=69e7bd7a1724f0c9e2f97149 ts=2026-04-21T18:10:02.0120000Z ~ 69cdc907d385e3b94310f72b.jsonl[1019] _id=69e7bd7b1724f0c9e2f97153 ts=2026-04-21T18:10:02.6400000Z`; `392ms: 69cdc907d385e3b94310f72b.jsonl[1015] _id=69e7bd7b1724f0c9e2f97151 ts=2026-04-21T18:10:02.6250000Z ~ 69cdc907d385e3b94310f72b.jsonl[1020] _id=69e7bd7b1724f0c9e2f97155 ts=2026-04-21T18:10:03.0170000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 69cdc907d385e3b94310f72b.jsonl[755] _id=69e2682a1724f0c9e2f7325c ts=2026-04-17T17:04:41.8190000Z -> 69cdc907d385e3b94310f72b.jsonl[760] _id=69e7ad701724f0c9e2f91d9b ts=2026-04-21T17:01:33.5990000Z; 47h 22m: 69cdc907d385e3b94310f72b.jsonl[1189] _id=69e7c45d1724f0c9e2f9a659 ts=2026-04-21T18:39:24.3950000Z -> 69cdc907d385e3b94310f72b.jsonl[1198] _id=69ea5e841724f0c9e2fb0605 ts=2026-04-23T18:01:38.3870000Z; 47h 7m: 69cdc907d385e3b94310f72b.jsonl[345] _id=69dd38a07957a33870f29124 ts=2026-04-13T18:40:31.7510000Z -> 69cdc907d385e3b94310f72b.jsonl[350] _id=69dfcf447957a33870f40d7b ts=2026-04-15T17:47:48.3880000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 253 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f72b.jsonl[58] _id=69ea64821724f0c9e2fb35e3 ts=2026-04-23T18:27:14.1790000Z -> 69cdc907d385e3b94310f72b.jsonl[1425] _id=69ea64931724f0c9e2fb3665 ts=2026-04-23T18:27:14.179Z; 2ms: 69cdc907d385e3b94310f72b.jsonl[5] _id=69dd37227957a33870f28704 ts=2026-04-13T18:34:10.0800000Z -> 69cdc907d385e3b94310f72b.jsonl[303] _id=69dd37227957a33870f28706 ts=2026-04-13T18:34:10.0820000Z; 3ms: 69cdc907d385e3b94310f72b.jsonl[1298] _id=69ea61a91724f0c9e2fb1fc5 ts=2026-04-23T18:15:04.9420000Z -> 69cdc907d385e3b94310f72b.jsonl[1299] _id=69ea61a91724f0c9e2fb1fc7 ts=2026-04-23T18:15:04.9450000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 50m 
  - Evidence: 239h 50m: 69cdc907d385e3b94310f72b.jsonl[333] _id=69dd37b07957a33870f28a28 ts=2026-04-13T18:36:31.9800000Z -> 69cdc907d385e3b94310f72b.jsonl[1423] _id=69ea64821724f0c9e2fb35e1 ts=2026-04-23T18:27:14.1690000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 69cdc907d385e3b94310f72b.jsonl[758] _id=69e268771724f0c9e2f7348c ts=2026-04-17T17:05:58.8610000Z -> 69cdc907d385e3b94310f72b.jsonl[759] _id=69e7ad6b1724f0c9e2f91d83 ts=2026-04-21T17:01:30.6900000Z; 47h 21m: 69cdc907d385e3b94310f72b.jsonl[1193] _id=69e7c48f1724f0c9e2f9a737 ts=2026-04-21T18:40:15.0990000Z -> 69cdc907d385e3b94310f72b.jsonl[1195] _id=69ea5e821724f0c9e2fb05fd ts=2026-04-23T18:01:36.7990000Z; 47h 6m: 69cdc907d385e3b94310f72b.jsonl[347] _id=69dd38ad7957a33870f29168 ts=2026-04-13T18:40:45.5530000Z -> 69cdc907d385e3b94310f72b.jsonl[348] _id=69dfcf407957a33870f40d61 ts=2026-04-15T17:47:43.1370000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 59m 
  - Evidence: 95h 59m: 69cdc907d385e3b94310f72b.jsonl[747] _id=69e2680c1724f0c9e2f73120 ts=2026-04-17T17:04:12.1790000Z -> 69cdc907d385e3b94310f72b.jsonl[778] _id=69e7ade01724f0c9e2f92183 ts=2026-04-21T17:03:27.6260000Z; 48h 13m: 69cdc907d385e3b94310f72b.jsonl[1095] _id=69e7bf871724f0c9e2f9806f ts=2026-04-21T18:18:46.9430000Z -> 69cdc907d385e3b94310f72b.jsonl[1452] _id=69ea65b91724f0c9e2fb3ffb ts=2026-04-23T18:32:25.0920000Z; 46h 26m: 69cdc907d385e3b94310f72b.jsonl[662] _id=69dfd9b17957a33870f45405 ts=2026-04-15T18:32:17.4790000Z -> 69cdc907d385e3b94310f72b.jsonl[724] _id=69e266d21724f0c9e2f72748 ts=2026-04-17T16:58:57.6190000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 54m 
  - Evidence: 96h 54m: 69cdc907d385e3b94310f72b.jsonl[706] _id=69e266811724f0c9e2f7250b ts=2026-04-17T16:57:37.4750000Z -> 69cdc907d385e3b94310f72b.jsonl[889] _id=69e7b9371724f0c9e2f952f3 ts=2026-04-21T17:51:50.4530000Z; 48h 25m: 69cdc907d385e3b94310f72b.jsonl[890] _id=69e7b9381724f0c9e2f952f9 ts=2026-04-21T17:51:52.1860000Z -> 69cdc907d385e3b94310f72b.jsonl[1332] _id=69ea623f1724f0c9e2fb2537 ts=2026-04-23T18:17:34.8560000Z; 46h 30m: 69cdc907d385e3b94310f72b.jsonl[639] _id=69dfd85b7957a33870f44a09 ts=2026-04-15T18:26:35.2690000Z -> 69cdc907d385e3b94310f72b.jsonl[712] _id=69e2667a1724f0c9e2f724de ts=2026-04-17T16:57:30.1590000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 19m 
  - Evidence: 143h 19m: 69cdc907d385e3b94310f72b.jsonl[641] _id=69dfd85b7957a33870f44a05 ts=2026-04-15T18:26:34.8360000Z -> 69cdc907d385e3b94310f72b.jsonl[842] _id=69e7b7d21724f0c9e2f949e1 ts=2026-04-21T17:45:53.7370000Z; 48h 31m: 69cdc907d385e3b94310f72b.jsonl[843] _id=69e7b7d51724f0c9e2f94a07 ts=2026-04-21T17:45:56.5950000Z -> 69cdc907d385e3b94310f72b.jsonl[1326] _id=69ea621f1724f0c9e2fb2431 ts=2026-04-23T18:17:03.2240000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 29m 
  - Evidence: 191h 29m: 69cdc907d385e3b94310f72b.jsonl[2] _id=69dd36d97957a33870f2854a ts=2026-04-13T18:32:57.1130000Z -> 69cdc907d385e3b94310f72b.jsonl[982] _id=69e7bbb61724f0c9e2f964dd ts=2026-04-21T18:02:29.9670000Z; 11m 26s: 69cdc907d385e3b94310f72b.jsonl[982] _id=69e7bbb61724f0c9e2f964dd ts=2026-04-21T18:02:29.9670000Z -> 69cdc907d385e3b94310f72b.jsonl[1047] _id=69e7be641724f0c9e2f9773d ts=2026-04-21T18:13:56.1770000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 31m 
  - Evidence: 191h 31m: 69cdc907d385e3b94310f72b.jsonl[284] _id=69dd36d47957a33870f28530 ts=2026-04-13T18:32:51.8570000Z -> 69cdc907d385e3b94310f72b.jsonl[987] _id=69e7bc191724f0c9e2f967a7 ts=2026-04-21T18:04:08.6920000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.015s..0.041s shown 
  - Evidence: 15ms: 69cdc907d385e3b94310f72b.jsonl[1015] _id=69e7bd7b1724f0c9e2f97151 ts=2026-04-21T18:10:02.6250000Z -> 69cdc907d385e3b94310f72b.jsonl[1019] _id=69e7bd7b1724f0c9e2f97153 ts=2026-04-21T18:10:02.6400000Z; 34ms: 69cdc907d385e3b94310f72b.jsonl[1026] _id=69e7bdb51724f0c9e2f972dd ts=2026-04-21T18:11:01.0500000Z -> 69cdc907d385e3b94310f72b.jsonl[1027] _id=69e7bdb51724f0c9e2f972e1 ts=2026-04-21T18:11:01.0840000Z; 41ms: 69cdc907d385e3b94310f72b.jsonl[1000] _id=69e7bc941724f0c9e2f96b0b ts=2026-04-21T18:06:12.2990000Z -> 69cdc907d385e3b94310f72b.jsonl[1002] _id=69e7bc951724f0c9e2f96b0d ts=2026-04-21T18:06:12.3400000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 69cdc907d385e3b94310f72b.jsonl[744] _id=69e268071724f0c9e2f730d8 ts=2026-04-17T17:04:07.6040000Z -> 69cdc907d385e3b94310f72b.jsonl[764] _id=69e7ad701724f0c9e2f91da1 ts=2026-04-21T17:01:34.7840000Z; 47h 42m: 69cdc907d385e3b94310f72b.jsonl[1100] _id=69e7bfb81724f0c9e2f981f8 ts=2026-04-21T18:19:35.8700000Z -> 69cdc907d385e3b94310f72b.jsonl[1197] _id=69ea5e831724f0c9e2fb0603 ts=2026-04-23T18:01:38.1470000Z; 47h 7m: 69cdc907d385e3b94310f72b.jsonl[346] _id=69dd389c7957a33870f2910c ts=2026-04-13T18:40:27.6940000Z -> 69cdc907d385e3b94310f72b.jsonl[349] _id=69dfcf427957a33870f40d6d ts=2026-04-15T17:47:45.6550000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.003s..0.009s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f72b.jsonl[247] _id=69dd36037957a33870f27efe ts=2026-04-13T18:29:22.9480000Z -> 69cdc907d385e3b94310f72b.jsonl[248] _id=69dd36037957a33870f27f00 ts=2026-04-13T18:29:22.9510000Z; 6ms: 69cdc907d385e3b94310f72b.jsonl[1504] _id=69ea67261724f0c9e2fb4a8d ts=2026-04-23T18:38:29.9230000Z -> 69cdc907d385e3b94310f72b.jsonl[1505] _id=69ea67261724f0c9e2fb4a8f ts=2026-04-23T18:38:29.9290000Z; 9ms: 69cdc907d385e3b94310f72b.jsonl[121] _id=69dd32457957a33870f2656a ts=2026-04-13T18:13:25.2430000Z -> 69cdc907d385e3b94310f72b.jsonl[120] _id=69dd32457957a33870f2656c ts=2026-04-13T18:13:25.2520000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc907d385e3b94310f72b.jsonl:69cdc907d385e3b94310f72b, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[662] _id=69dfd9b17957a33870f45405 ts=2026-04-15T18:32:17.4790000Z`; `69cdc907d385e3b94310f72b.jsonl[1095] _id=69e7bf871724f0c9e2f9806f ts=2026-04-21T18:18:46.9430000Z`; `69cdc907d385e3b94310f72b.jsonl[1455] _id=69ea65d31724f0c9e2fb40a9 ts=2026-04-23T18:32:50.6970000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 30 record(s) match the trigger in 69cdc907d385e3b94310f72b.jsonl:69cdc907d385e3b94310f72b, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[522] _id=69dfd50c7957a33870f4358d ts=2026-04-15T18:12:27.6570000Z`; `69cdc907d385e3b94310f72b.jsonl[523] _id=69dfd50c7957a33870f43593 ts=2026-04-15T18:12:28.1010000Z`; `69cdc907d385e3b94310f72b.jsonl[517] _id=69dfd5137957a33870f435bb ts=2026-04-15T18:12:35.1860000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[871] _id=69e7b8b11724f0c9e2f95064 ts=2026-04-21T17:49:36.3900000Z`; `69cdc907d385e3b94310f72b.jsonl[884] _id=69e7b90b1724f0c9e2f9520d ts=2026-04-21T17:51:06.4880000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[30] _id=69e7be651724f0c9e2f97747 ts=2026-04-21T18:13:56.2490000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[997] _id=69e7bc971724f0c9e2f96b2b ts=2026-04-21T18:06:14.6850000Z`; `69cdc907d385e3b94310f72b.jsonl[1021] _id=69e7bd801724f0c9e2f97173 ts=2026-04-21T18:10:07.9310000Z`; `69cdc907d385e3b94310f72b.jsonl[1026] _id=69e7bdb51724f0c9e2f972dd ts=2026-04-21T18:11:01.0500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[57] _id=69ea64831724f0c9e2fb35e9 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[747] _id=69e2680c1724f0c9e2f73120 ts=2026-04-17T17:04:12.1790000Z`; `69cdc907d385e3b94310f72b.jsonl[778] _id=69e7ade01724f0c9e2f92183 ts=2026-04-21T17:03:27.6260000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f72b.jsonl[27] _id=69e7bd7e1724f0c9e2f97163 ts=2026-04-21T18:10:06.2850000Z`; `69cdc907d385e3b94310f72b.jsonl[1013] _id=69e7bd801724f0c9e2f9717c ts=2026-04-21T18:10:08.0510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 125 unmatched 'DialogueStartEvent' (totals: 208 start, 85 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Started' (totals: 6 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 11 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 27 start, 14 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.61s, min -17.04s, max -0.26s over 1516 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=partial 
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
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 32 records 
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

### `DialogueEvent` — 959 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (296); Unit 2 Prod (Refactor) (275); Unit 1 Dev (196); Unit 3 Dungeon Dev (133); Unit 4 Dev - Dungeon (34); Unit 4 Dev (25)
- **eventKey:** present on 666 of 959 records
- **Intervals:** median 3.25s (p5 0.01s / p95 63.14s, n=958)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x666; [conversationId, dialogueEventType] x293
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 959/959 records)
    numeric range 10 .. 104 (33 unique)
data.dialogueEventType  (string, 959/959 records)
    "DialogueNodeEvent"  x666
    "DialogueStartEvent"  x208
    "DialogueFinishEvent"  x85
data.nodeId  (number, 666/959 records)
    numeric range 0 .. 289 (205 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 395 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (131); Unit 3 Dev (106); Unit 3 Dungeon Dev (70); Unit 1 Dev (61); Unit 4 Dev (16); Unit 4 Dev - Dungeon (11)
- **Intervals:** median 30.01s (p5 29.96s / p95 33.43s, n=388)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 395/395 records)
data.position.x  (number, 395/395 records)
    numeric range -691.582 .. 1584.71 (222 unique)
data.position.y  (number, 395/395 records)
    numeric range -114.686 .. 155.733 (175 unique)
data.position.z  (number, 395/395 records)
    numeric range -1107.51 .. 1796.68 (222 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 41 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (12); Unit 3 Dev (9); Unit 3 Dungeon Dev (3); Unit 4 Dev - Dungeon (3); Unit 4 Dev (1)
- **eventKey:** present on 41 of 41 records
- **Intervals:** median 234.96s (p5 0.01s / p95 169742.18s, n=40)
- **`data` key-set variants:** [questEventType, questID, questName] x27; [questEventType, questID, questName, questSuccessOrFailure] x14
- **Fields under `data`:**

```text
data.questEventType  (string, 41/41 records)
    "questActiveEvent"  x27
    "questFinishEvent"  x14
data.questID  (string, 41/41 records)
    18 unique values (see csv/event_unique_values.csv)
data.questName  (string, 41/41 records)
    18 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 14/41 records)
    "Succeeded"  x14
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 32 records

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (16)
- **Intervals:** median 20.93s (p5 1.68s / p95 170898.78s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "MapCloseEvent"  x16
    "MapOpenEvent"  x16
data.featureUsed  (string, 32/32 records)
    "Map"  x32
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 30 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (10)
- **Intervals:** median 3.78s (p5 0.57s / p95 104897.93s, n=29)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "dragEnd"  x15
    "dragStart"  x15
data.featureUsed  (string, 30/30 records)
    "waypoint"  x30
data.location  (object, 30/30 records)
data.location.x  (number, 30/30 records)
    numeric range -792.051 .. 58.3696 (16 unique)
data.location.y  (number, 30/30 records)
    numeric range -315.904 .. 124.897 (16 unique)
data.location.z  (number, 30/30 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationToolEvent` — 22 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (22)
- **Intervals:** median 0.61s (p5 0.03s / p95 53.00s, n=21)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "argumentationToolClose"  x11
    "argumentationToolOpen"  x11
data.argumentationTitle  (string, 22/22 records)
    "Unit 3 - Pollution Upstream"  x22
data.toolName  (string, 22/22 records)
    "BackingInfoPanel - Pollution Site Data"  x16
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Image"  x3
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationNodeEvent` — 19 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (13); Unit 1 Dev (6)
- **Intervals:** median 13.32s (p5 1.83s / p95 103599.49s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 19/19 records)
    "Unit 3 - Pollution Upstream"  x13
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 19/19 records)
    "I"  x5
    "1"  x4
    "3"  x2
    "4"  x2
    "A"  x2
    "II"  x2
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 9 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 2401.70s (p5 27.31s / p95 285377.39s, n=8)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/9 records)
    "Started"  x6
    "Finished"  x3
data.Unit  (string, 9/9 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 52.67s (p5 6.47s / p95 517201.19s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863442.19s (p5 863442.19s / p95 863442.19s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
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
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit3"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (5 records)
- `TopographicMapEvent` data.actionType: "dragStart" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*