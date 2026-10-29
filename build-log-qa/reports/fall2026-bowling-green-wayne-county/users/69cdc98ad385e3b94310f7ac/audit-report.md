# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ac

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7ac
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7ac.jsonl
- **Records:** 2140 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7ac
- **Time span:** 2026-04-14T19:30:28.171000+00:00 .. 2026-04-24T20:03:40.638000+00:00 (240h 33m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ac\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2140 records, 6 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 49 INFO, 2 NOT_TESTED, 38 PASS.
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
| DialogueEvent | 1485 | 69.39 | 1 | 6 | 1000 | 2026-04-14T19:30:46.639000+00:00 | 2026-04-24T20:02:25.812000+00:00 | 240h 31m |
| PlayerPositionEvent | 490 | 22.9 | 1 | 6 | 0 | 2026-04-14T19:30:28.171000+00:00 | 2026-04-24T20:03:40.638000+00:00 | 240h 33m |
| questEvent | 54 | 2.52 | 1 | 6 | 54 | 2026-04-14T19:30:46.619000+00:00 | 2026-04-24T20:02:15.818000+00:00 | 240h 31m |
| Topographic Map Event | 32 | 1.5 | 1 | 2 | 0 | 2026-04-16T19:10:53.084000+00:00 | 2026-04-24T19:36:18.707000+00:00 | 192h 25m |
| TopographicMapEvent | 26 | 1.21 | 1 | 2 | 0 | 2026-04-16T19:11:31.340000+00:00 | 2026-04-24T19:36:16.107000+00:00 | 192h 24m |
| argumentationNodeEvent | 18 | 0.84 | 1 | 2 | 0 | 2026-04-14T19:49:56.033000+00:00 | 2026-04-22T19:34:02.864000+00:00 | 191h 44m |
| soilMachine | 16 | 0.75 | 1 | 1 | 0 | 2026-04-24T19:59:09.455000+00:00 | 2026-04-24T20:03:37.234000+00:00 | 4m 27s |
| argumentationEvent | 7 | 0.33 | 1 | 2 | 0 | 2026-04-14T19:49:49.940000+00:00 | 2026-04-22T19:34:04.185000+00:00 | 191h 44m |
| Soil Key Puzzle | 6 | 0.28 | 1 | 3 | 0 | 2026-04-14T20:08:33.975000+00:00 | 2026-04-24T19:50:04.008000+00:00 | 239h 41m |
| crash | 4 | 0.19 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.09 | 1 | 2 | 0 | 2026-04-14T19:55:56.543000+00:00 | 2026-04-24T19:42:16.953000+00:00 | 239h 46m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863180.41s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.009s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 241.853s median 
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
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.9s median 
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
  - Observed: 2.341s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 32 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
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
  - Observed: 18 records 
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
  - Observed: 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 24; 25; 36; 40; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Power Play; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[26] _id=69de9b047957a33870f3a705 ts=2026-04-14T19:52:35.3070000Z`; `69cdc98ad385e3b94310f7ac.jsonl[1243] _id=69e138cd1724f0c9e2f6db16 ts=2026-04-16T19:30:20.5510000Z`; `69cdc98ad385e3b94310f7ac.jsonl[1276] _id=69e13a591724f0c9e2f6f2d4 ts=2026-04-16T19:36:57.1010000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 32 records, TopographicMapEvent: 26 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1484 | 0.0 | 2.389 | 583.49 | 36.906 | 514935.021 | 0.1 | 408 | 4 |
| PlayerPositionEvent | 483 | 29.77 | 30.009 | 728.93 | 33.645 | 168882.114 | 0.08 | 0 | 2 |
| questEvent | 53 | 0.009 | 141.515 | 16337.532 | 68269.458 | 515315.029 | 0.0 | 7 | 8 |
| Topographic Map Event | 31 | 1.141 | 15.692 | 22345.988 | 1001.873 | 689168.999 | 0.0 | 0 | 4 |
| TopographicMapEvent | 25 | 0.295 | 3.369 | 27707.391 | 140378.023 | 514527.976 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 17 | 1.983 | 8.9 | 40602.755 | 138066.68 | 690022.282 | 0.0 | 0 | 1 |
| soilMachine | 15 | 0.833 | 2.341 | 17.852 | 101.582 | 147.515 | 3.36 | 0 | 0 |
| argumentationEvent | 6 | 0.076 | 63.089 | 115042.374 | 517525.049 | 690005.682 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 5 | 3.052 | 241.853 | 172578.007 | 586440.649 | 689861.412 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 863180.41 | 863180.41 | 863180.41 | 863180.41 | 863180.41 | 0.0 | 0 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[1451] _id=69e91f6e1724f0c9e2fa9fc3 ts=? == 69cdc98ad385e3b94310f7ac.jsonl[1988] _id=69ebc0f01724f0c9e2fbb7cb ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.009s (p5 29.96s, p95 33.64s, n=483) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `76ms: 69cdc98ad385e3b94310f7ac.jsonl[220] _id=69e922ac1724f0c9e2faa9bb ts=2026-04-22T19:34:04.1090000Z ~ 69cdc98ad385e3b94310f7ac.jsonl[218] _id=69e922ad1724f0c9e2faa9c3 ts=2026-04-22T19:34:04.1850000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 2m 
  - Evidence: 143h 2m: 69cdc98ad385e3b94310f7ac.jsonl[1403] _id=69e13d1e1724f0c9e2f6fffc ts=2026-04-16T19:48:45.7240000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1525] _id=69e918951724f0c9e2fa83dd ts=2026-04-22T18:51:00.7450000Z; 46h 54m: 69cdc98ad385e3b94310f7ac.jsonl[1898] _id=69e929f21724f0c9e2fac445 ts=2026-04-22T20:05:06.0610000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1902] _id=69ebbda41724f0c9e2fbb34f ts=2026-04-24T18:59:47.4470000Z; 46h 40m: 69cdc98ad385e3b94310f7ac.jsonl[71] _id=69de9f3d7957a33870f3b79d ts=2026-04-14T20:10:36.4760000Z -> 69cdc98ad385e3b94310f7ac.jsonl[916] _id=69e12f8e1724f0c9e2f68f54 ts=2026-04-16T18:50:53.7210000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 408 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7ac.jsonl[428] _id=69ebc7991724f0c9e2fbc315 ts=2026-04-24T19:42:16.9730000Z -> 69cdc98ad385e3b94310f7ac.jsonl[422] _id=69ebc7a81724f0c9e2fbc341 ts=2026-04-24T19:42:16.973Z; 2ms: 69cdc98ad385e3b94310f7ac.jsonl[2050] _id=69ebc4551724f0c9e2fbbd47 ts=2026-04-24T19:28:20.3830000Z -> 69cdc98ad385e3b94310f7ac.jsonl[2037] _id=69ebc4551724f0c9e2fbbd49 ts=2026-04-24T19:28:20.3850000Z; 3ms: 69cdc98ad385e3b94310f7ac.jsonl[1806] _id=69e926a41724f0c9e2fab843 ts=2026-04-22T19:50:59.6740000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1807] _id=69e926a41724f0c9e2fab845 ts=2026-04-22T19:50:59.6770000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 46m 
  - Evidence: 239h 46m: 69cdc98ad385e3b94310f7ac.jsonl[807] _id=69de9bcd7957a33870f3aa49 ts=2026-04-14T19:55:56.5430000Z -> 69cdc98ad385e3b94310f7ac.jsonl[418] _id=69ebc7991724f0c9e2fbc313 ts=2026-04-24T19:42:16.9530000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 54m 
  - Evidence: 46h 54m: 69cdc98ad385e3b94310f7ac.jsonl[1888] _id=69e929ef1724f0c9e2fac43d ts=2026-04-22T20:05:02.9540000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1906] _id=69ebbda11724f0c9e2fbb349 ts=2026-04-24T18:59:45.0680000Z; 46h 40m: 69cdc98ad385e3b94310f7ac.jsonl[64] _id=69de9f377957a33870f3b791 ts=2026-04-14T20:10:30.1290000Z -> 69cdc98ad385e3b94310f7ac.jsonl[914] _id=69e12f8a1724f0c9e2f68f4a ts=2026-04-16T18:50:49.4450000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 37m 
  - Evidence: 191h 37m: 69cdc98ad385e3b94310f7ac.jsonl[885] _id=69de9ec67957a33870f3b6dd ts=2026-04-14T20:08:37.0270000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1791] _id=69e9258b1724f0c9e2fab529 ts=2026-04-22T19:46:18.4390000Z; 47h 59m: 69cdc98ad385e3b94310f7ac.jsonl[1802] _id=69e9267d1724f0c9e2fab7bf ts=2026-04-22T19:50:20.2920000Z -> 69cdc98ad385e3b94310f7ac.jsonl[450] _id=69ebc9521724f0c9e2fbc683 ts=2026-04-24T19:49:37.8880000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 26m 
  - Evidence: 191h 26m: 69cdc98ad385e3b94310f7ac.jsonl[1444] _id=69e1412e1724f0c9e2f7101a ts=2026-04-16T20:06:06.3170000Z -> 69cdc98ad385e3b94310f7ac.jsonl[2086] _id=69ebc53f1724f0c9e2fbbf09 ts=2026-04-24T19:32:15.3160000Z; 22m 32s: 69cdc98ad385e3b94310f7ac.jsonl[1159] _id=69e136ea1724f0c9e2f6b7d4 ts=2026-04-16T19:22:17.8860000Z -> 69cdc98ad385e3b94310f7ac.jsonl[158] _id=69e13c331724f0c9e2f6fab6 ts=2026-04-16T19:44:50.3680000Z; 10m 51s: 69cdc98ad385e3b94310f7ac.jsonl[166] _id=69e13d3f1724f0c9e2f700a6 ts=2026-04-16T19:49:17.9500000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1431] _id=69e13fc91724f0c9e2f70a1a ts=2026-04-16T20:00:09.2150000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 142h 55m 
  - Evidence: 142h 55m: 69cdc98ad385e3b94310f7ac.jsonl[1433] _id=69e13fee1724f0c9e2f70ab2 ts=2026-04-16T20:00:45.2260000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1564] _id=69e919ce1724f0c9e2fa8889 ts=2026-04-22T18:56:13.2020000Z; 48h 36m: 69cdc98ad385e3b94310f7ac.jsonl[1565] _id=69e919cf1724f0c9e2fa888f ts=2026-04-22T18:56:14.8050000Z -> 69cdc98ad385e3b94310f7ac.jsonl[2083] _id=69ebc5461724f0c9e2fbbf1d ts=2026-04-24T19:32:22.1980000Z; 33m 40s: 69cdc98ad385e3b94310f7ac.jsonl[1111] _id=69e134661724f0c9e2f6a6a0 ts=2026-04-16T19:11:33.7880000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1360] _id=69e13c4b1724f0c9e2f6fb2e ts=2026-04-16T19:45:14.3300000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 40m 
  - Evidence: 191h 40m: 69cdc98ad385e3b94310f7ac.jsonl[25] _id=69de9b047957a33870f3a703 ts=2026-04-14T19:52:35.2780000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1724] _id=69e922591724f0c9e2faa89b ts=2026-04-22T19:32:40.9600000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 40m 
  - Evidence: 191h 40m: 69cdc98ad385e3b94310f7ac.jsonl[24] _id=69de9b037957a33870f3a6f7 ts=2026-04-14T19:52:33.9260000Z -> 69cdc98ad385e3b94310f7ac.jsonl[212] _id=69e922681724f0c9e2faa8cb ts=2026-04-22T19:32:56.2080000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 8m 
  - Evidence: 143h 8m: 69cdc98ad385e3b94310f7ac.jsonl[1338] _id=69e13c301724f0c9e2f6fa9e ts=2026-04-16T19:44:48.2660000Z -> 69cdc98ad385e3b94310f7ac.jsonl[1545] _id=69e919241724f0c9e2fa860d ts=2026-04-22T18:53:23.2950000Z; 47h 7m: 69cdc98ad385e3b94310f7ac.jsonl[1810] _id=69e926ec1724f0c9e2fab94b ts=2026-04-22T19:52:11.2820000Z -> 69cdc98ad385e3b94310f7ac.jsonl[241] _id=69ebbda41724f0c9e2fbb34d ts=2026-04-24T18:59:47.1000000Z; 46h 40m: 69cdc98ad385e3b94310f7ac.jsonl[67] _id=69de9f3c7957a33870f3b799 ts=2026-04-14T20:10:35.8960000Z -> 69cdc98ad385e3b94310f7ac.jsonl[915] _id=69e12f8d1724f0c9e2f68f4e ts=2026-04-16T18:50:52.0280000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.009s..0.011s shown 
  - Evidence: 9ms: 69cdc98ad385e3b94310f7ac.jsonl[521] _id=69ebcbca1724f0c9e2fbca1d ts=2026-04-24T20:00:09.5440000Z -> 69cdc98ad385e3b94310f7ac.jsonl[522] _id=69ebcbca1724f0c9e2fbca1f ts=2026-04-24T20:00:09.5530000Z; 11ms: 69cdc98ad385e3b94310f7ac.jsonl[526] _id=69ebcb4d1724f0c9e2fbc977 ts=2026-04-24T19:58:04.8750000Z -> 69cdc98ad385e3b94310f7ac.jsonl[512] _id=69ebcb4d1724f0c9e2fbc979 ts=2026-04-24T19:58:04.8860000Z; 11ms: 69cdc98ad385e3b94310f7ac.jsonl[723] _id=69de9a0b7957a33870f3a259 ts=2026-04-14T19:48:25.9180000Z -> 69cdc98ad385e3b94310f7ac.jsonl[724] _id=69de9a0b7957a33870f3a25b ts=2026-04-14T19:48:25.9290000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7ac.jsonl:69cdc98ad385e3b94310f7ac, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[885] _id=69de9ec67957a33870f3b6dd ts=2026-04-14T20:08:37.0270000Z`; `69cdc98ad385e3b94310f7ac.jsonl[1802] _id=69e9267d1724f0c9e2fab7bf ts=2026-04-22T19:50:20.2920000Z`; `69cdc98ad385e3b94310f7ac.jsonl[455] _id=69ebc96c1724f0c9e2fbc69b ts=2026-04-24T19:50:04.0080000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 26 record(s) match the trigger in 69cdc98ad385e3b94310f7ac.jsonl:69cdc98ad385e3b94310f7ac, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[1110] _id=69e134641724f0c9e2f6a690 ts=2026-04-16T19:11:31.3400000Z`; `69cdc98ad385e3b94310f7ac.jsonl[1111] _id=69e134661724f0c9e2f6a6a0 ts=2026-04-16T19:11:33.7880000Z`; `69cdc98ad385e3b94310f7ac.jsonl[1360] _id=69e13c4b1724f0c9e2f6fb2e ts=2026-04-16T19:45:14.3300000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[1601] _id=69e91af21724f0c9e2fa8d7b ts=2026-04-22T19:01:05.9170000Z`; `69cdc98ad385e3b94310f7ac.jsonl[189] _id=69e91bc31724f0c9e2fa90cb ts=2026-04-22T19:04:34.5090000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[218] _id=69e922ad1724f0c9e2faa9c3 ts=2026-04-22T19:34:04.1850000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `69cdc98ad385e3b94310f7ac.jsonl[1451] _id=69e91f6e1724f0c9e2fa9fc3 ts=?`; `69cdc98ad385e3b94310f7ac.jsonl[1988] _id=69ebc0f01724f0c9e2fbb7cb ts=?`; `69cdc98ad385e3b94310f7ac.jsonl[380] _id=69ebc65e1724f0c9e2fbc0ef ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 245 unmatched 'DialogueStartEvent' (totals: 364 start, 121 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 32 start, 22 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.81s, min -15.54s, max -0.61s over 2136 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7ac\coverage.yaml

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
  - Observed: 32 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
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

### `DialogueEvent` — 1485 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (535); Unit 3 Dev (397); Unit 3 Dungeon Dev (249); Unit 1 Dev (194); Unit 4 Dev - Dungeon (85); Unit 4 Dev (25)
- **eventKey:** present on 1000 of 1485 records
- **Intervals:** median 2.39s (p5 0.01s / p95 36.91s, n=1484)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1000; [conversationId, dialogueEventType] x485
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1485/1485 records)
    numeric range 10 .. 104 (31 unique)
data.dialogueEventType  (string, 1485/1485 records)
    "DialogueNodeEvent"  x1000
    "DialogueStartEvent"  x364
    "DialogueFinishEvent"  x121
data.nodeId  (number, 1000/1485 records)
    numeric range 0 .. 283 (197 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 490 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (170); Unit 3 Dev (145); Unit 3 Dungeon Dev (81); Unit 1 Dev (51); Unit 4 Dev - Dungeon (23); Unit 4 Dev (20)
- **Intervals:** median 30.01s (p5 29.96s / p95 33.64s, n=483)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 490/490 records)
data.position.x  (number, 490/490 records)
    numeric range -663.409 .. 1099.57 (333 unique)
data.position.y  (number, 490/490 records)
    numeric range -113.292 .. 456.842 (252 unique)
data.position.z  (number, 490/490 records)
    numeric range -1110.06 .. 2320.08 (334 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 54 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (4); Unit 4 Dev (1)
- **eventKey:** present on 54 of 54 records
- **Intervals:** median 141.51s (p5 0.01s / p95 68269.46s, n=53)
- **`data` key-set variants:** [questEventType, questID, questName] x32; [questEventType, questID, questName, questSuccessOrFailure] x22
- **Fields under `data`:**

```text
data.questEventType  (string, 54/54 records)
    "questActiveEvent"  x32
    "questFinishEvent"  x22
data.questID  (string, 54/54 records)
    20 unique values (see csv/event_unique_values.csv)
data.questName  (string, 54/54 records)
    20 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 22/54 records)
    "Succeeded"  x22
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 32 records

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (12)
- **Intervals:** median 15.69s (p5 4.22s / p95 1001.87s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "MapCloseEvent"  x16
    "MapOpenEvent"  x16
data.featureUsed  (string, 32/32 records)
    "Map"  x32
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 26 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (14); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 3.37s (p5 0.45s / p95 140378.02s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "dragEnd"  x13
    "dragStart"  x13
data.featureUsed  (string, 26/26 records)
    "waypoint"  x26
data.location  (object, 26/26 records)
data.location.x  (number, 26/26 records)
    numeric range -770.79 .. -107.728 (14 unique)
data.location.y  (number, 26/26 records)
    numeric range -307.4 .. 388.527 (14 unique)
data.location.z  (number, 26/26 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 18 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (9)
- **Intervals:** median 8.90s (p5 2.27s / p95 138066.68s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationNodeAdd"  x13
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 18/18 records)
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 18/18 records)
    "I"  x5
    "A"  x4
    "B"  x3
    "2"  x2
    "II"  x2
    "1"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 2.34s (p5 1.10s / p95 101.58s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Bedrock"  x8
    "Clay"  x3
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 16/16 records)
    "5"  x10
    "4"  x5
    "3"  x1
data.machine  (string, 16/16 records)
    "1"  x16
data.row  (string, 16/16 records)
    "TopRow"  x9
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 63.09s (p5 9.85s / p95 517525.05s, n=6)
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

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 241.85s (p5 7.67s / p95 586440.65s, n=5)
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

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "Uncaught ReferenceError: onResize is not defined"  x3
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 1 empty-string)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x2
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x1
data.type  (string, 4/4 records)
    "runtime_error"  x3
    "unhandled_rejection"  x1
data.unitId  (string, 4/4 records)
    "unit3"  x3
    "unit4"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863180.41s (p5 863180.41s / p95 863180.41s, n=1)
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
- `crash` : exact duplicate records (same timestamp, scene and data)

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)
- `soilMachine` data.canisterType: "Bedrock" (8x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*