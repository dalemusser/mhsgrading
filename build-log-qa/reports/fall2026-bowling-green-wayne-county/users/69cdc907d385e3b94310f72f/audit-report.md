# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f72f
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f72f.jsonl
- **Records:** 1789 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f72f
- **Time span:** 2026-04-13T17:58:47.420000+00:00 .. 2026-04-23T18:41:09.762000+00:00 (240h 42m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1789 records, 4 scenes.
- Findings: **0 FAIL**, **40 WARNING**, 54 INFO, 5 NOT_TESTED, 33 PASS.
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
| DialogueEvent | 1196 | 66.85 | 1 | 4 | 833 | 2026-04-13T17:59:05.917000+00:00 | 2026-04-23T18:39:47.157000+00:00 | 240h 40m |
| PlayerPositionEvent | 452 | 25.27 | 1 | 4 | 0 | 2026-04-13T17:58:47.420000+00:00 | 2026-04-23T18:41:09.762000+00:00 | 240h 42m |
| questEvent | 49 | 2.74 | 1 | 4 | 49 | 2026-04-13T17:59:05.900000+00:00 | 2026-04-23T18:33:37.349000+00:00 | 240h 34m |
| Topographic Map Event | 36 | 2.01 | 1 | 1 | 0 | 2026-04-13T18:36:07.411000+00:00 | 2026-04-17T18:23:13.065000+00:00 | 95h 47m |
| TopographicMapEvent | 14 | 0.78 | 1 | 1 | 0 | 2026-04-15T18:07:41.718000+00:00 | 2026-04-17T18:05:24.101000+00:00 | 47h 57m |
| argumentationNodeEvent | 14 | 0.78 | 1 | 2 | 0 | 2026-04-13T18:18:03.523000+00:00 | 2026-04-23T18:28:03.445000+00:00 | 240h 9m |
| argumentationToolEvent | 12 | 0.67 | 1 | 1 | 0 | 2026-04-23T18:25:50.125000+00:00 | 2026-04-23T18:27:26.128000+00:00 | 1m 36s |
| argumentationEvent | 7 | 0.39 | 1 | 2 | 0 | 2026-04-13T18:17:05.571000+00:00 | 2026-04-23T18:28:05.231000+00:00 | 240h 10m |
| Soil Key Puzzle | 5 | 0.28 | 1 | 2 | 0 | 2026-04-17T18:19:53.242000+00:00 | 2026-04-23T18:32:53.653000+00:00 | 144h 13m |
| crash | 3 | 0.17 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 1 | 0.06 | 1 | 1 | 0 | 2026-04-13T18:30:11.505000+00:00 | 2026-04-13T18:30:11.505000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.276s median 
  - Expected: 3.7s in 09-23-26 
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
  - Observed: 89107.541s median 
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
  - Observed: 7.64s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 11.253s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.231s median 
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
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 36 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 14 records 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 14 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; C; D 
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
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 18 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[344] _id=69dd33797957a33870f26e44 ts=2026-04-13T18:18:32.5130000Z`; `69cdc907d385e3b94310f72f.jsonl[684] _id=69dfd6667957a33870f43cf9 ts=2026-04-15T18:18:13.1860000Z`; `69cdc907d385e3b94310f72f.jsonl[40] _id=69dfd6667957a33870f43cfb ts=2026-04-15T18:18:13.3880000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 36 records, TopographicMapEvent: 14 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1195 | 0.001 | 1.276 | 725.055 | 63.688 | 339685.65 | 0.08 | 320 | 8 |
| PlayerPositionEvent | 448 | 29.788 | 30.007 | 1929.025 | 52.472 | 339353.931 | 0.03 | 0 | 7 |
| questEvent | 48 | 0.005 | 151.924 | 18043.155 | 168616.583 | 339474.877 | 0.0 | 3 | 14 |
| Topographic Map Event | 35 | 2.043 | 22.897 | 9852.162 | 51751.901 | 171364.299 | 0.01 | 0 | 3 |
| TopographicMapEvent | 13 | 0.617 | 7.64 | 13281.722 | 68911.78 | 171582.41 | 0.0 | 0 | 1 |
| argumentationNodeEvent | 13 | 1.284 | 11.253 | 66507.686 | 345796.762 | 864416.98 | 0.0 | 0 | 1 |
| argumentationToolEvent | 11 | 0.034 | 2.231 | 8.728 | 40.045 | 70.617 | 6.87 | 2 | 0 |
| argumentationEvent | 6 | 0.072 | 41.21 | 144109.943 | 648345.62 | 864404.908 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 4 | 38.567 | 89107.541 | 129795.103 | 316512.906 | 340926.763 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.007s (p5 29.96s, p95 52.47s, n=448) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `72ms: 69cdc907d385e3b94310f72f.jsonl[1684] _id=69ea64b51724f0c9e2fb3745 ts=2026-04-23T18:28:05.1590000Z ~ 69cdc907d385e3b94310f72f.jsonl[147] _id=69ea64b61724f0c9e2fb374b ts=2026-04-23T18:28:05.2310000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc907d385e3b94310f72f.jsonl[1262] _id=69e27e801724f0c9e2f78cec ts=2026-04-17T18:40:00.4850000Z -> 69cdc907d385e3b94310f72f.jsonl[1278] _id=69e7ad661724f0c9e2f91d55 ts=2026-04-21T17:01:26.1350000Z; 47h 45m: 69cdc907d385e3b94310f72f.jsonl[1483] _id=69e7bf821724f0c9e2f9805b ts=2026-04-21T18:18:41.7030000Z -> 69cdc907d385e3b94310f72f.jsonl[1513] _id=69ea5f0e1724f0c9e2fb0937 ts=2026-04-23T18:03:58.0720000Z; 47h 6m: 69cdc907d385e3b94310f72f.jsonl[453] _id=69dd38657957a33870f28f82 ts=2026-04-13T18:39:33.1520000Z -> 69cdc907d385e3b94310f72f.jsonl[458] _id=69dfcef17957a33870f40bf9 ts=2026-04-15T17:46:24.4160000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 320 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 69cdc907d385e3b94310f72f.jsonl[20] _id=69dd33c97957a33870f2706e ts=2026-04-13T18:19:51.8810000Z -> 69cdc907d385e3b94310f72f.jsonl[364] _id=69dd33ca7957a33870f27076 ts=2026-04-13T18:19:51.8820000Z; 2ms: 69cdc907d385e3b94310f72f.jsonl[369] _id=69dd35dd7957a33870f27dfc ts=2026-04-13T18:28:44.7470000Z -> 69cdc907d385e3b94310f72f.jsonl[21] _id=69dd35dd7957a33870f27dfe ts=2026-04-13T18:28:44.7490000Z; 3ms: 69cdc907d385e3b94310f72f.jsonl[1243] _id=69e27e191724f0c9e2f78a9a ts=2026-04-17T18:38:16.1810000Z -> 69cdc907d385e3b94310f72f.jsonl[92] _id=69e27e191724f0c9e2f78a9c ts=2026-04-17T18:38:16.1840000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f72f.jsonl[1259] _id=69e27e761724f0c9e2f78cb6 ts=2026-04-17T18:39:49.7660000Z -> 69cdc907d385e3b94310f72f.jsonl[1265] _id=69e7ac111724f0c9e2f9162d ts=2026-04-21T16:55:43.6970000Z; 47h 26m: 69cdc907d385e3b94310f72f.jsonl[1508] _id=69e7c3a71724f0c9e2f9a07d ts=2026-04-21T18:36:22.5700000Z -> 69cdc907d385e3b94310f72f.jsonl[1509] _id=69ea5ed81724f0c9e2fb07c9 ts=2026-04-23T18:03:02.2700000Z; 47h 5m: 69cdc907d385e3b94310f72f.jsonl[456] _id=69dd389e7957a33870f29118 ts=2026-04-13T18:40:29.6680000Z -> 69cdc907d385e3b94310f72f.jsonl[462] _id=69dfceed7957a33870f40beb ts=2026-04-15T17:46:20.2410000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc907d385e3b94310f72f.jsonl[1154] _id=69e279f91724f0c9e2f778d6 ts=2026-04-17T18:20:40.6060000Z -> 69cdc907d385e3b94310f72f.jsonl[1288] _id=69e7adb81724f0c9e2f9201d ts=2026-04-21T17:02:47.3690000Z; 49h 29m: 69cdc907d385e3b94310f72f.jsonl[1288] _id=69e7adb81724f0c9e2f9201d ts=2026-04-21T17:02:47.3690000Z -> 69cdc907d385e3b94310f72f.jsonl[1728] _id=69ea65af1724f0c9e2fb3f85 ts=2026-04-23T18:32:15.0860000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 36m 
  - Evidence: 47h 36m: 69cdc907d385e3b94310f72f.jsonl[632] _id=69dfd42d7957a33870f430e8 ts=2026-04-15T18:08:44.4390000Z -> 69cdc907d385e3b94310f72f.jsonl[952] _id=69e271911724f0c9e2f74778 ts=2026-04-17T17:44:48.7380000Z; 47h 21m: 69cdc907d385e3b94310f72f.jsonl[457] _id=69dd38a77957a33870f2914c ts=2026-04-13T18:40:39.0800000Z -> 69cdc907d385e3b94310f72f.jsonl[36] _id=69dfd2937957a33870f42647 ts=2026-04-15T18:01:54.0920000Z; 14m 30s: 69cdc907d385e3b94310f72f.jsonl[1086] _id=69e277271724f0c9e2f76a6c ts=2026-04-17T18:08:39.3830000Z -> 69cdc907d385e3b94310f72f.jsonl[1181] _id=69e27a8e1724f0c9e2f77b86 ts=2026-04-17T18:23:09.9510000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 39m 
  - Evidence: 47h 39m: 69cdc907d385e3b94310f72f.jsonl[39] _id=69dfd42b7957a33870f430cf ts=2026-04-15T18:08:42.3760000Z -> 69cdc907d385e3b94310f72f.jsonl[995] _id=69e272691724f0c9e2f74d74 ts=2026-04-17T17:48:24.7860000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 240h 6m 
  - Evidence: 240h 6m: 69cdc907d385e3b94310f72f.jsonl[343] _id=69dd33797957a33870f26e42 ts=2026-04-13T18:18:32.4940000Z -> 69cdc907d385e3b94310f72f.jsonl[1641] _id=69ea640e1724f0c9e2fb3289 ts=2026-04-23T18:25:17.4020000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 240h 6m 
  - Evidence: 240h 6m: 69cdc907d385e3b94310f72f.jsonl[16] _id=69dd33727957a33870f26df8 ts=2026-04-13T18:18:25.8240000Z -> 69cdc907d385e3b94310f72f.jsonl[1657] _id=69ea64131724f0c9e2fb32b3 ts=2026-04-23T18:25:22.8040000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.034s..0.048s shown 
  - Evidence: 34ms: 69cdc907d385e3b94310f72f.jsonl[1660] _id=69ea64301724f0c9e2fb3381 ts=2026-04-23T18:25:52.1550000Z -> 69cdc907d385e3b94310f72f.jsonl[1663] _id=69ea64301724f0c9e2fb3383 ts=2026-04-23T18:25:52.1890000Z; 48ms: 69cdc907d385e3b94310f72f.jsonl[1668] _id=69ea64431724f0c9e2fb3409 ts=2026-04-23T18:26:10.8030000Z -> 69cdc907d385e3b94310f72f.jsonl[1671] _id=69ea64431724f0c9e2fb340b ts=2026-04-23T18:26:10.8510000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 17m 
  - Evidence: 94h 17m: 69cdc907d385e3b94310f72f.jsonl[1239] _id=69e27e001724f0c9e2f789e0 ts=2026-04-17T18:37:52.3290000Z -> 69cdc907d385e3b94310f72f.jsonl[1263] _id=69e7ac141724f0c9e2f91634 ts=2026-04-21T16:55:47.2060000Z; 47h 46m: 69cdc907d385e3b94310f72f.jsonl[1469] _id=69e7befa1724f0c9e2f97b95 ts=2026-04-21T18:16:25.4820000Z -> 69cdc907d385e3b94310f72f.jsonl[1510] _id=69ea5eda1724f0c9e2fb07d5 ts=2026-04-23T18:03:05.5720000Z; 47h 8m: 69cdc907d385e3b94310f72f.jsonl[432] _id=69dd38077957a33870f28c9a ts=2026-04-13T18:37:58.0580000Z -> 69cdc907d385e3b94310f72f.jsonl[460] _id=69dfcef07957a33870f40bf7 ts=2026-04-15T17:46:22.7330000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.005s..0.010s shown 
  - Evidence: 5ms: 69cdc907d385e3b94310f72f.jsonl[301] _id=69dd32f67957a33870f26a84 ts=2026-04-13T18:16:21.9180000Z -> 69cdc907d385e3b94310f72f.jsonl[302] _id=69dd32f67957a33870f26a86 ts=2026-04-13T18:16:21.9230000Z; 7ms: 69cdc907d385e3b94310f72f.jsonl[241] _id=69dd315f7957a33870f25ee8 ts=2026-04-13T18:09:34.6390000Z -> 69cdc907d385e3b94310f72f.jsonl[242] _id=69dd315f7957a33870f25eea ts=2026-04-13T18:09:34.6460000Z; 10ms: 69cdc907d385e3b94310f72f.jsonl[210] _id=69dd30167957a33870f256ba ts=2026-04-13T18:04:05.6920000Z -> 69cdc907d385e3b94310f72f.jsonl[211] _id=69dd30167957a33870f256bc ts=2026-04-13T18:04:05.7020000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 2 record(s) match the trigger in 69cdc907d385e3b94310f72f.jsonl:69cdc907d385e3b94310f72f, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[1154] _id=69e279f91724f0c9e2f778d6 ts=2026-04-17T18:20:40.6060000Z`; `69cdc907d385e3b94310f72f.jsonl[1731] _id=69ea65d61724f0c9e2fb40e9 ts=2026-04-23T18:32:53.6530000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 14 record(s) match the trigger in 69cdc907d385e3b94310f72f.jsonl:69cdc907d385e3b94310f72f, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[621] _id=69dfd3ee7957a33870f42f69 ts=2026-04-15T18:07:41.7180000Z`; `69cdc907d385e3b94310f72f.jsonl[620] _id=69dfd3ef7957a33870f42f75 ts=2026-04-15T18:07:42.5330000Z`; `69cdc907d385e3b94310f72f.jsonl[38] _id=69dfd3f67957a33870f42f99 ts=2026-04-15T18:07:50.1730000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[1347] _id=69e7b98f1724f0c9e2f95495 ts=2026-04-21T17:53:18.5940000Z`; `69cdc907d385e3b94310f72f.jsonl[1376] _id=69e7b9eb1724f0c9e2f956dd ts=2026-04-21T17:54:50.8090000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[147] _id=69ea64b61724f0c9e2fb374b ts=2026-04-23T18:28:05.2310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[1665] _id=69ea64321724f0c9e2fb339b ts=2026-04-23T18:25:53.9700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `69cdc907d385e3b94310f72f.jsonl[1276] _id=69e7ad4a1724f0c9e2f91ccf ts=?`; `69cdc907d385e3b94310f72f.jsonl[1500] _id=69e7c2c71724f0c9e2f99a29 ts=?`; `69cdc907d385e3b94310f72f.jsonl[1560] _id=69ea60f11724f0c9e2fb1965 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 187 unmatched 'DialogueStartEvent' (totals: 274 start, 89 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 3 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 31 start, 18 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.67s, min -7.58s, max -0.41s over 1786 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f72f\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=partial, Unit4=skipped 
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
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 36 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
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

### `DialogueEvent` — 1196 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (667); Unit 3 Dev (298); Unit 1 Dev (190); Unit 3 Dungeon Dev (41)
- **eventKey:** present on 833 of 1196 records
- **Intervals:** median 1.28s (p5 0.01s / p95 63.69s, n=1195)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x833; [conversationId, dialogueEventType] x363
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1196/1196 records)
    numeric range 10 .. 84 (27 unique)
data.dialogueEventType  (string, 1196/1196 records)
    "DialogueNodeEvent"  x833
    "DialogueStartEvent"  x274
    "DialogueFinishEvent"  x89
data.nodeId  (number, 833/1196 records)
    numeric range 0 .. 286 (160 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 452 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (237); Unit 3 Dev (152); Unit 1 Dev (46); Unit 3 Dungeon Dev (17)
- **Intervals:** median 30.01s (p5 29.96s / p95 52.47s, n=448)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 452/452 records)
data.position.x  (number, 452/452 records)
    numeric range -674.132 .. 1401.43 (290 unique)
data.position.y  (number, 452/452 records)
    numeric range -115.12 .. 206.23 (214 unique)
data.position.z  (number, 452/452 records)
    numeric range -1143.98 .. 2134.13 (290 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 49 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (14); Unit 1 Dev (12); Unit 3 Dungeon Dev (1)
- **eventKey:** present on 49 of 49 records
- **Intervals:** median 151.92s (p5 0.54s / p95 168616.58s, n=48)
- **`data` key-set variants:** [questEventType, questID, questName] x31; [questEventType, questID, questName, questSuccessOrFailure] x18
- **Fields under `data`:**

```text
data.questEventType  (string, 49/49 records)
    "questActiveEvent"  x31
    "questFinishEvent"  x18
data.questID  (string, 49/49 records)
    13 unique values (see csv/event_unique_values.csv)
data.questName  (string, 49/49 records)
    13 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 18/49 records)
    "Succeeded"  x18
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 36 records

- **Scenes:** Unit 2 Prod (Refactor) (36)
- **Intervals:** median 22.90s (p5 2.85s / p95 51751.90s, n=35)
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
data.featureUsed  (string, 36/36 records)
    "Map"  x36
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 14 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (14)
- **Intervals:** median 7.64s (p5 0.74s / p95 68911.78s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "dragEnd"  x7
    "dragStart"  x7
data.featureUsed  (string, 14/14 records)
    "waypoint"  x14
data.location  (object, 14/14 records)
data.location.x  (number, 14/14 records)
    8 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 14/14 records)
    8 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 14/14 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 14 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (3)
- **Intervals:** median 11.25s (p5 1.70s / p95 345796.76s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 14/14 records)
    "A"  x3
    "B"  x3
    "2"  x2
    "I"  x2
    "II"  x2
    "1"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (12)
- **Intervals:** median 2.23s (p5 0.04s / p95 40.05s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x6
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x12
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - Pollution Site Data"  x10
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 41.21s (p5 1.18s / p95 648345.62s, n=6)
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

### `Soil Key Puzzle` — 5 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2)
- **Intervals:** median 89107.54s (p5 39.89s / p95 316512.91s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 5/5 records)
    "Started"  x3
    "Finished"  x2
data.Unit  (string, 5/5 records)
    "Unit 2 Prod (Refactor)"  x3
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x2
    "runtime_error"  x1
data.unitId  (string, 3/3 records)
    "unit3"  x2
    "unit2"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

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
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now
- `DialogueEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (3 records)
- `TopographicMapEvent` data.actionType: "dragStart" (7x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*