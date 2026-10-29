# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f732

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f732
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f732.jsonl
- **Records:** 2201 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f732
- **Time span:** 2026-04-13T17:51:19.433000+00:00 .. 2026-04-23T18:39:54.093000+00:00 (240h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f732\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 2201 records, 6 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 47 INFO, 2 NOT_TESTED, 37 PASS.
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
| DialogueEvent | 1372 | 62.34 | 1 | 6 | 948 | 2026-04-13T17:51:37.763000+00:00 | 2026-04-23T18:38:34.074000+00:00 | 240h 46m |
| PlayerPositionEvent | 661 | 30.03 | 1 | 6 | 0 | 2026-04-13T17:51:19.433000+00:00 | 2026-04-23T18:39:54.093000+00:00 | 240h 48m |
| questEvent | 70 | 3.18 | 1 | 6 | 70 | 2026-04-13T17:51:37.740000+00:00 | 2026-04-23T18:38:33.155000+00:00 | 240h 46m |
| soilMachine | 27 | 1.23 | 1 | 1 | 0 | 2026-04-23T18:10:24.687000+00:00 | 2026-04-23T18:30:53.739000+00:00 | 20m 29s |
| argumentationNodeEvent | 24 | 1.09 | 1 | 2 | 0 | 2026-04-13T18:09:34.733000+00:00 | 2026-04-17T18:07:32.963000+00:00 | 95h 57m |
| Topographic Map Event | 20 | 0.91 | 1 | 2 | 0 | 2026-04-13T18:35:06.435000+00:00 | 2026-04-21T17:52:17.401000+00:00 | 191h 17m |
| Soil Key Puzzle | 12 | 0.55 | 1 | 3 | 0 | 2026-04-13T18:28:05.381000+00:00 | 2026-04-21T18:17:02.393000+00:00 | 191h 48m |
| argumentationEvent | 7 | 0.32 | 1 | 2 | 0 | 2026-04-13T18:09:30.813000+00:00 | 2026-04-17T18:07:35.165000+00:00 | 95h 58m |
| TopographicMapEvent | 6 | 0.27 | 1 | 2 | 0 | 2026-04-13T18:35:16.506000+00:00 | 2026-04-17T17:48:15.285000+00:00 | 95h 12m |
| EndOfUnit | 2 | 0.09 | 1 | 2 | 0 | 2026-04-13T18:14:41.519000+00:00 | 2026-04-21T18:05:01.834000+00:00 | 191h 50m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 690620.315s median 
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
  - Observed: 289.681s median 
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
  - Observed: 6.225s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.841s median 
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
  - Observed: 5.972s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 12 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 20 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 24 records 
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
  - Observed: 3; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.4x vs baseline. 
  - Observed: 27 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f732.jsonl[77] _id=69dd31eb7957a33870f262d0 ts=2026-04-13T18:11:54.0970000Z`; `69cdc907d385e3b94310f732.jsonl[198] _id=69dd386b7957a33870f28fae ts=2026-04-13T18:39:38.8990000Z`; `69cdc907d385e3b94310f732.jsonl[1186] _id=69dfd1957957a33870f41e09 ts=2026-04-15T17:57:40.5300000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 20 records, TopographicMapEvent: 6 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1371 | 0.002 | 2.8 | 632.251 | 61.351 | 340230.247 | 0.09 | 345 | 6 |
| PlayerPositionEvent | 652 | 28.724 | 30.013 | 1329.041 | 32.762 | 339698.467 | 0.05 | 0 | 4 |
| questEvent | 69 | 0.002 | 143.586 | 12562.542 | 101356.184 | 341315.928 | 0.0 | 9 | 11 |
| soilMachine | 26 | 0.154 | 5.972 | 47.271 | 216.405 | 530.141 | 1.27 | 0 | 0 |
| argumentationNodeEvent | 23 | 1.214 | 6.841 | 15020.793 | 124.241 | 345131.652 | 0.0 | 0 | 1 |
| Topographic Map Event | 19 | 0.762 | 13.637 | 36243.735 | 189128.534 | 345713.997 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 11 | 3.041 | 289.681 | 62776.092 | 258936.343 | 345853.676 | 0.0 | 0 | 5 |
| argumentationEvent | 6 | 0.114 | 52.594 | 57580.725 | 258887.273 | 345104.061 | 0.0 | 0 | 1 |
| TopographicMapEvent | 5 | 0.933 | 6.225 | 68555.756 | 171687.494 | 171889.054 | 0.0 | 0 | 2 |
| EndOfUnit | 1 | 690620.315 | 690620.315 | 690620.315 | 690620.315 | 690620.315 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.013s (p5 29.95s, p95 32.76s, n=652) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `114ms: 69cdc907d385e3b94310f732.jsonl[1617] _id=69e276e71724f0c9e2f76934 ts=2026-04-17T18:07:35.0510000Z ~ 69cdc907d385e3b94310f732.jsonl[1610] _id=69e276e71724f0c9e2f76941 ts=2026-04-17T18:07:35.1650000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `856ms: 69cdc907d385e3b94310f732.jsonl[758] _id=69ea61801724f0c9e2fb1dff ts=2026-04-23T18:14:23.8700000Z ~ 69cdc907d385e3b94310f732.jsonl[2116] _id=69ea61811724f0c9e2fb1e0d ts=2026-04-23T18:14:24.7260000Z`; `744ms: 69cdc907d385e3b94310f732.jsonl[2116] _id=69ea61811724f0c9e2fb1e0d ts=2026-04-23T18:14:24.7260000Z ~ 69cdc907d385e3b94310f732.jsonl[757] _id=69ea61821724f0c9e2fb1e11 ts=2026-04-23T18:14:25.4700000Z`; `154ms: 69cdc907d385e3b94310f732.jsonl[757] _id=69ea61821724f0c9e2fb1e11 ts=2026-04-23T18:14:25.4700000Z ~ 69cdc907d385e3b94310f732.jsonl[756] _id=69ea61821724f0c9e2fb1e13 ts=2026-04-23T18:14:25.6240000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 30m 
  - Evidence: 94h 30m: 69cdc907d385e3b94310f732.jsonl[596] _id=69e27c6f1724f0c9e2f780be ts=2026-04-17T18:31:11.0180000Z -> 69cdc907d385e3b94310f732.jsonl[1735] _id=69e7ad771724f0c9e2f91dc1 ts=2026-04-21T17:01:41.2650000Z; 47h 24m: 69cdc907d385e3b94310f732.jsonl[715] _id=69e7c4751724f0c9e2f9a6cf ts=2026-04-21T18:39:48.4420000Z -> 69cdc907d385e3b94310f732.jsonl[2044] _id=69ea5f121724f0c9e2fb0975 ts=2026-04-23T18:04:01.9830000Z; 47h 6m: 69cdc907d385e3b94310f732.jsonl[1107] _id=69dd38b37957a33870f29178 ts=2026-04-13T18:40:50.2800000Z -> 69cdc907d385e3b94310f732.jsonl[1110] _id=69dfcf447957a33870f40d75 ts=2026-04-15T17:47:47.5550000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 345 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f732.jsonl[1648] _id=69e277f81724f0c9e2f76e7e ts=2026-04-17T18:12:08.7760000Z -> 69cdc907d385e3b94310f732.jsonl[1645] _id=69e277f91724f0c9e2f76e80 ts=2026-04-17T18:12:08.7780000Z; 3ms: 69cdc907d385e3b94310f732.jsonl[144] _id=69dd35c87957a33870f27d70 ts=2026-04-13T18:28:23.2930000Z -> 69cdc907d385e3b94310f732.jsonl[145] _id=69dd35c87957a33870f27d72 ts=2026-04-13T18:28:23.2960000Z; 3ms: 69cdc907d385e3b94310f732.jsonl[53] _id=69dd300c7957a33870f25688 ts=2026-04-13T18:03:55.5850000Z -> 69cdc907d385e3b94310f732.jsonl[51] _id=69dd300c7957a33870f2568a ts=2026-04-13T18:03:55.5880000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 50m 
  - Evidence: 191h 50m: 69cdc907d385e3b94310f732.jsonl[109] _id=69dd32927957a33870f26796 ts=2026-04-13T18:14:41.5190000Z -> 69cdc907d385e3b94310f732.jsonl[1942] _id=69e7bc4f1724f0c9e2f96955 ts=2026-04-21T18:05:01.8340000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc907d385e3b94310f732.jsonl[1732] _id=69e27e7e1724f0c9e2f78ce8 ts=2026-04-17T18:39:58.3230000Z -> 69cdc907d385e3b94310f732.jsonl[600] _id=69e7ad721724f0c9e2f91da5 ts=2026-04-21T17:01:36.7900000Z; 47h 23m: 69cdc907d385e3b94310f732.jsonl[714] _id=69e7c47b1724f0c9e2f9a6f1 ts=2026-04-21T18:39:53.9830000Z -> 69cdc907d385e3b94310f732.jsonl[2042] _id=69ea5f011724f0c9e2fb08cb ts=2026-04-23T18:03:44.0850000Z; 47h 7m: 69cdc907d385e3b94310f732.jsonl[1108] _id=69dd38a17957a33870f29134 ts=2026-04-13T18:40:32.5940000Z -> 69cdc907d385e3b94310f732.jsonl[200] _id=69dfcf407957a33870f40d5f ts=2026-04-15T17:47:43.4360000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 69cdc907d385e3b94310f732.jsonl[1647] _id=69e277eb1724f0c9e2f76e22 ts=2026-04-17T18:11:54.9150000Z -> 69cdc907d385e3b94310f732.jsonl[1974] _id=69e7bee91724f0c9e2f97b17 ts=2026-04-21T18:16:08.5910000Z; 47h 46m: 69cdc907d385e3b94310f732.jsonl[1037] _id=69dd35b97957a33870f27cfa ts=2026-04-13T18:28:08.4220000Z -> 69cdc907d385e3b94310f732.jsonl[325] _id=69dfd5ac7957a33870f438eb ts=2026-04-15T18:15:07.4330000Z; 46h 39m: 69cdc907d385e3b94310f732.jsonl[1316] _id=69dfd6177957a33870f43af3 ts=2026-04-15T18:16:54.9230000Z -> 69cdc907d385e3b94310f732.jsonl[405] _id=69e266361724f0c9e2f722ea ts=2026-04-17T16:56:21.6430000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 69cdc907d385e3b94310f732.jsonl[1491] _id=69e272751724f0c9e2f74dba ts=2026-04-17T17:48:36.9800000Z -> 69cdc907d385e3b94310f732.jsonl[1879] _id=69e7b8e81724f0c9e2f95161 ts=2026-04-21T17:50:30.9770000Z; 47h 42m: 69cdc907d385e3b94310f732.jsonl[301] _id=69dfd3a27957a33870f42d5b ts=2026-04-15T18:06:26.0690000Z -> 69cdc907d385e3b94310f732.jsonl[492] _id=69e272741724f0c9e2f74db6 ts=2026-04-17T17:48:36.2180000Z; 47h 23m: 69cdc907d385e3b94310f732.jsonl[197] _id=69dd386d7957a33870f28fb4 ts=2026-04-13T18:39:40.9620000Z -> 69cdc907d385e3b94310f732.jsonl[1244] _id=69dfd2db7957a33870f4280b ts=2026-04-15T18:03:06.4770000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 44m 
  - Evidence: 47h 44m: 69cdc907d385e3b94310f732.jsonl[1245] _id=69dfd2e87957a33870f4286b ts=2026-04-15T18:03:20.0060000Z -> 69cdc907d385e3b94310f732.jsonl[1509] _id=69e272591724f0c9e2f74cd6 ts=2026-04-17T17:48:09.0600000Z; 47h 28m: 69cdc907d385e3b94310f732.jsonl[178] _id=69dd37667957a33870f28874 ts=2026-04-13T18:35:17.8200000Z -> 69cdc907d385e3b94310f732.jsonl[1248] _id=69dfd2e77957a33870f4285b ts=2026-04-15T18:03:19.0730000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 69cdc907d385e3b94310f732.jsonl[87] _id=69dd31ea7957a33870f262ca ts=2026-04-13T18:11:54.0790000Z -> 69cdc907d385e3b94310f732.jsonl[530] _id=69e275fa1724f0c9e2f763b0 ts=2026-04-17T18:03:38.1400000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 69cdc907d385e3b94310f732.jsonl[953] _id=69dd31e17957a33870f26296 ts=2026-04-13T18:11:45.0200000Z -> 69cdc907d385e3b94310f732.jsonl[531] _id=69e2760c1724f0c9e2f76410 ts=2026-04-17T18:03:56.6720000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 69cdc907d385e3b94310f732.jsonl[1653] _id=69e278301724f0c9e2f76fba ts=2026-04-17T18:13:04.7470000Z -> 69cdc907d385e3b94310f732.jsonl[1737] _id=69e7ad761724f0c9e2f91dbf ts=2026-04-21T17:01:40.6750000Z; 47h 39m: 69cdc907d385e3b94310f732.jsonl[2008] _id=69e7c0d81724f0c9e2f98b77 ts=2026-04-21T18:24:23.1490000Z -> 69cdc907d385e3b94310f732.jsonl[2043] _id=69ea5f031724f0c9e2fb08e2 ts=2026-04-23T18:03:46.5720000Z; 47h 12m: 69cdc907d385e3b94310f732.jsonl[171] _id=69dd37587957a33870f28810 ts=2026-04-13T18:35:03.8510000Z -> 69cdc907d385e3b94310f732.jsonl[199] _id=69dfcf427957a33870f40d6f ts=2026-04-15T17:47:45.7930000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f732.jsonl[2077] _id=69ea60631724f0c9e2fb1449 ts=2026-04-23T18:09:38.6910000Z -> 69cdc907d385e3b94310f732.jsonl[728] _id=69ea60631724f0c9e2fb144d ts=2026-04-23T18:09:38.6930000Z; 2ms: 69cdc907d385e3b94310f732.jsonl[926] _id=69dd31227957a33870f25d5c ts=2026-04-13T18:08:33.5240000Z -> 69cdc907d385e3b94310f732.jsonl[932] _id=69dd31227957a33870f25d5e ts=2026-04-13T18:08:33.5260000Z; 5ms: 69cdc907d385e3b94310f732.jsonl[2096] _id=69ea60be1724f0c9e2fb17e7 ts=2026-04-23T18:11:10.0790000Z -> 69cdc907d385e3b94310f732.jsonl[2097] _id=69ea60bf1724f0c9e2fb17e9 ts=2026-04-23T18:11:10.0840000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f732.jsonl:69cdc907d385e3b94310f732, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f732.jsonl[1037] _id=69dd35b97957a33870f27cfa ts=2026-04-13T18:28:08.4220000Z`; `69cdc907d385e3b94310f732.jsonl[1316] _id=69dfd6177957a33870f43af3 ts=2026-04-15T18:16:54.9230000Z`; `69cdc907d385e3b94310f732.jsonl[1647] _id=69e277eb1724f0c9e2f76e22 ts=2026-04-17T18:11:54.9150000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc907d385e3b94310f732.jsonl:69cdc907d385e3b94310f732, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f732.jsonl[177] _id=69dd37657957a33870f28872 ts=2026-04-13T18:35:16.5060000Z`; `69cdc907d385e3b94310f732.jsonl[178] _id=69dd37667957a33870f28874 ts=2026-04-13T18:35:17.8200000Z`; `69cdc907d385e3b94310f732.jsonl[1248] _id=69dfd2e77957a33870f4285b ts=2026-04-15T18:03:19.0730000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f732.jsonl[383] _id=69dfd98a7957a33870f45329 ts=2026-04-15T18:31:37.1300000Z`; `69cdc907d385e3b94310f732.jsonl[1531] _id=69e273391724f0c9e2f7527c ts=2026-04-17T17:51:53.4570000Z`; `69cdc907d385e3b94310f732.jsonl[509] _id=69e273c91724f0c9e2f7565c ts=2026-04-17T17:54:17.4230000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f732.jsonl[1610] _id=69e276e71724f0c9e2f76941 ts=2026-04-17T18:07:35.1650000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f732.jsonl[2132] _id=69ea62921724f0c9e2fb281f ts=2026-04-23T18:18:57.7560000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f732.jsonl[422] _id=69e266ac1724f0c9e2f72647 ts=2026-04-17T16:58:20.2180000Z`; `69cdc907d385e3b94310f732.jsonl[429] _id=69e267ce1724f0c9e2f72eac ts=2026-04-17T17:03:09.8990000Z`; `69cdc907d385e3b94310f732.jsonl[470] _id=69e270c41724f0c9e2f74172 ts=2026-04-17T17:41:24.1190000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 166 unmatched 'DialogueStartEvent' (totals: 293 start, 131 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'Started' (totals: 8 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 43 start, 27 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.76s, min -4.59s, max -0.03s over 2201 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f732\coverage.yaml

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
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 20 records 
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

### `DialogueEvent` — 1372 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (575); Unit 3 Dev (254); Unit 1 Dev (186); Unit 4 Dev - Dungeon (156); Unit 3 Dungeon Dev (142); Unit 4 Dev (59)
- **eventKey:** present on 948 of 1372 records
- **Intervals:** median 2.80s (p5 0.01s / p95 61.35s, n=1371)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x948; [conversationId, dialogueEventType] x424
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1372/1372 records)
    numeric range 8 .. 107 (38 unique)
data.dialogueEventType  (string, 1372/1372 records)
    "DialogueNodeEvent"  x948
    "DialogueStartEvent"  x293
    "DialogueFinishEvent"  x131
data.nodeId  (number, 948/1372 records)
    numeric range 0 .. 286 (202 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 661 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (244); Unit 3 Dungeon Dev (142); Unit 4 Dev - Dungeon (96); Unit 3 Dev (89); Unit 1 Dev (47); Unit 4 Dev (43)
- **Intervals:** median 30.01s (p5 29.95s / p95 32.76s, n=652)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 661/661 records)
data.position.x  (number, 661/661 records)
    numeric range -688.529 .. 1404.72 (293 unique)
data.position.y  (number, 661/661 records)
    numeric range -112.488 .. 155.22 (227 unique)
data.position.z  (number, 661/661 records)
    numeric range -1104.33 .. 1781.72 (293 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 4 Dev - Dungeon (16); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev (5); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 143.59s (p5 0.01s / p95 101356.18s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x43; [questEventType, questID, questName, questSuccessOrFailure] x27
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x43
    "questFinishEvent"  x27
data.questID  (string, 70/70 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 27/70 records)
    "Succeeded"  x27
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 27 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (27)
- **Intervals:** median 5.97s (p5 0.77s / p95 216.41s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "ChangeCanister"  x27
data.canisterType  (string, 27/27 records)
    "Bedrock"  x10
    "Clay"  x8
    "Gravel"  x5
    "Sand"  x4
data.floor  (string, 27/27 records)
    "5"  x18
    "3"  x5
    "4"  x4
data.machine  (string, 27/27 records)
    "1"  x25
    "2"  x2
data.row  (string, 27/27 records)
    "TopRow"  x19
    "BottomRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 24 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (13); Unit 1 Dev (11)
- **Intervals:** median 6.84s (p5 1.59s / p95 124.24s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "argumentationNodeAdd"  x16
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 24/24 records)
    "Unit 3 - Pollution Upstream"  x13
    "Unit 1 - Freshwater"  x9
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 24/24 records)
    "A"  x7
    "1"  x4
    "B"  x3
    "I"  x3
    "2"  x2
    "4"  x2
    "II"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 20 records

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (10)
- **Intervals:** median 13.64s (p5 1.94s / p95 189128.53s, n=19)
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "MapCloseEvent"  x10
    "MapOpenEvent"  x10
data.featureUsed  (string, 20/20 records)
    "Map"  x20
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `Soil Key Puzzle` — 12 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 289.68s (p5 14.71s / p95 258936.34s, n=11)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/12 records)
    "Started"  x8
    "Finished"  x4
data.Unit  (string, 12/12 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 52.59s (p5 9.61s / p95 258887.27s, n=6)
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

### `TopographicMapEvent` — 6 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2)
- **Intervals:** median 6.22s (p5 1.01s / p95 171687.49s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "dragEnd"  x3
    "dragStart"  x3
data.featureUsed  (string, 6/6 records)
    "waypoint"  x6
data.location  (object, 6/6 records)
data.location.x  (number, 6/6 records)
    4 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 6/6 records)
    4 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 6/6 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 690620.31s (p5 690620.31s / p95 690620.31s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TopographicMapEvent` data.actionType: "dragStart" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (10x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*