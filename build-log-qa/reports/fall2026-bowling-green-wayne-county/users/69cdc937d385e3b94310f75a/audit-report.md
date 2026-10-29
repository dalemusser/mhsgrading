# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75a
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f75a.jsonl
- **Records:** 1781 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f75a
- **Time span:** 2026-04-15T19:40:55.325000+00:00 .. 2026-04-23T20:10:34.353000+00:00 (192h 29m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1781 records, 4 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 55 INFO, 5 NOT_TESTED, 33 PASS.
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
| DialogueEvent | 1171 | 65.75 | 1 | 4 | 824 | 2026-04-15T19:41:13.325000+00:00 | 2026-04-23T20:10:34.353000+00:00 | 192h 29m |
| PlayerPositionEvent | 418 | 23.47 | 1 | 4 | 0 | 2026-04-15T19:40:55.325000+00:00 | 2026-04-23T20:10:16.989000+00:00 | 192h 29m |
| Topographic Map Event | 76 | 4.27 | 1 | 3 | 0 | 2026-04-15T19:43:04.809000+00:00 | 2026-04-21T19:49:31.534000+00:00 | 144h 6m |
| questEvent | 48 | 2.7 | 1 | 4 | 48 | 2026-04-15T19:41:13.302000+00:00 | 2026-04-23T20:10:00.280000+00:00 | 192h 28m |
| argumentationNodeEvent | 26 | 1.46 | 1 | 2 | 0 | 2026-04-17T19:15:51.482000+00:00 | 2026-04-21T19:57:13.537000+00:00 | 96h 41m |
| TopographicMapEvent | 20 | 1.12 | 1 | 2 | 0 | 2026-04-15T20:05:24.507000+00:00 | 2026-04-21T19:07:18.593000+00:00 | 143h 1m |
| Soil Key Puzzle | 7 | 0.39 | 1 | 2 | 0 | 2026-04-17T19:37:59.826000+00:00 | 2026-04-23T19:38:31.662000+00:00 | 144h 0m |
| argumentationEvent | 7 | 0.39 | 1 | 2 | 0 | 2026-04-17T19:15:43.517000+00:00 | 2026-04-21T19:57:17.320000+00:00 | 96h 41m |
| argumentationToolEvent | 4 | 0.22 | 1 | 1 | 0 | 2026-04-21T19:56:44.388000+00:00 | 2026-04-21T19:56:50.060000+00:00 | 5.7s |
| EndOfUnit | 2 | 0.11 | 1 | 1 | 0 | 2026-04-17T19:20:29.661000+00:00 | 2026-04-17T19:20:29.661000+00:00 | 0.0s |
| crash | 2 | 0.11 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.054s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 165.043s median 
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
  - Observed: 6.686s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 6.525s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.941s median 
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
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 418 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 7 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 76 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 26 records 
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
  - Observed: 2; 4; C; D 
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
  - Observed: 2 records this build 
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
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[944] _id=69e2874e1724f0c9e2f7a63a ts=2026-04-17T19:17:34.6050000Z`; `69cdc937d385e3b94310f75a.jsonl[1132] _id=69e28dea1724f0c9e2f7c1e4 ts=2026-04-17T19:45:46.5810000Z`; `69cdc937d385e3b94310f75a.jsonl[1366] _id=69e7ca851724f0c9e2f9bc5b ts=2026-04-21T19:05:40.5990000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 76 records, TopographicMapEvent: 20 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1170 | 0.002 | 2.232 | 592.274 | 56.341 | 255363.144 | 0.1 | 296 | 5 |
| PlayerPositionEvent | 413 | 29.872 | 30.054 | 1677.533 | 44.885 | 255349.957 | 0.04 | 0 | 4 |
| Topographic Map Event | 75 | 0.264 | 8.244 | 6917.156 | 1213.391 | 341669.698 | 0.01 | 0 | 5 |
| questEvent | 47 | 0.005 | 183.496 | 14743.127 | 143258.244 | 255541.017 | 0.0 | 3 | 9 |
| argumentationNodeEvent | 25 | 0.862 | 6.525 | 13923.282 | 50.533 | 347818.328 | 0.0 | 0 | 1 |
| TopographicMapEvent | 19 | 0.673 | 6.686 | 27100.741 | 187524.775 | 342904.509 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 6 | 3.055 | 165.043 | 86405.306 | 301719.387 | 344408.338 | 0.0 | 0 | 2 |
| argumentationEvent | 6 | 0.169 | 40.531 | 58015.634 | 260886.798 | 347782.308 | 0.0 | 0 | 1 |
| argumentationToolEvent | 3 | 0.106 | 1.941 | 1.891 | 3.457 | 3.625 | 31.73 | 0 | 0 |
| EndOfUnit | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 1 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[385] _id=69e7c9311724f0c9e2f9b4b1 ts=? == 69cdc937d385e3b94310f75a.jsonl[444] _id=69e7cef61724f0c9e2f9d3bf ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.054s (p5 29.95s, p95 44.88s, n=413) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc937d385e3b94310f75a.jsonl[989] _id=69e287fd1724f0c9e2f7a932 ts=2026-04-17T19:20:29.6610000Z ~ 69cdc937d385e3b94310f75a.jsonl[990] _id=69e288161724f0c9e2f7a99a ts=2026-04-17T19:20:29.661Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `169ms: 69cdc937d385e3b94310f75a.jsonl[553] _id=69e7d69e1724f0c9e2f9f645 ts=2026-04-21T19:57:17.1510000Z ~ 69cdc937d385e3b94310f75a.jsonl[558] _id=69e7d69f1724f0c9e2f9f64b ts=2026-04-21T19:57:17.3200000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 70h 56m 
  - Evidence: 70h 56m: 69cdc937d385e3b94310f75a.jsonl[377] _id=69e3e20f1724f0c9e2f848ca ts=2026-04-18T19:57:03.5050000Z -> 69cdc937d385e3b94310f75a.jsonl[1249] _id=69e7c7931724f0c9e2f9ac95 ts=2026-04-21T18:53:06.6490000Z; 47h 28m: 69cdc937d385e3b94310f75a.jsonl[1679] _id=69e7d88b1724f0c9e2f9fe21 ts=2026-04-21T20:05:29.8080000Z -> 69cdc937d385e3b94310f75a.jsonl[1685] _id=69ea74451724f0c9e2fb5535 ts=2026-04-23T19:34:29.5820000Z; 46h 44m: 69cdc937d385e3b94310f75a.jsonl[23] _id=69dfeffc7957a33870f49cfb ts=2026-04-15T20:07:23.5600000Z -> 69cdc937d385e3b94310f75a.jsonl[24] _id=69e281391724f0c9e2f78f12 ts=2026-04-17T18:51:36.3970000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 296 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f75a.jsonl[1297] _id=69e7c94d1724f0c9e2f9b51b ts=2026-04-21T19:00:28.0830000Z -> 69cdc937d385e3b94310f75a.jsonl[1298] _id=69e7c94d1724f0c9e2f9b51f ts=2026-04-21T19:00:28.0850000Z; 3ms: 69cdc937d385e3b94310f75a.jsonl[546] _id=69e7d6831724f0c9e2f9f5df ts=2026-04-21T19:56:50.2340000Z -> 69cdc937d385e3b94310f75a.jsonl[539] _id=69e7d6831724f0c9e2f9f5e1 ts=2026-04-21T19:56:50.2370000Z; 4ms: 69cdc937d385e3b94310f75a.jsonl[112] _id=69e287981724f0c9e2f7a768 ts=2026-04-17T19:18:47.8060000Z -> 69cdc937d385e3b94310f75a.jsonl[113] _id=69e287981724f0c9e2f7a76a ts=2026-04-17T19:18:47.8100000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75a.jsonl[989] _id=69e287fd1724f0c9e2f7a932 ts=2026-04-17T19:20:29.6610000Z -> 69cdc937d385e3b94310f75a.jsonl[990] _id=69e288161724f0c9e2f7a99a ts=2026-04-17T19:20:29.661Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 70h 55m 
  - Evidence: 70h 55m: 69cdc937d385e3b94310f75a.jsonl[374] _id=69e3e2181724f0c9e2f848cc ts=2026-04-18T19:57:12.6350000Z -> 69cdc937d385e3b94310f75a.jsonl[1251] _id=69e7c78f1724f0c9e2f9ac7f ts=2026-04-21T18:53:02.5920000Z; 47h 28m: 69cdc937d385e3b94310f75a.jsonl[1680] _id=69e7d88b1724f0c9e2f9fe29 ts=2026-04-21T20:05:29.8150000Z -> 69cdc937d385e3b94310f75a.jsonl[1681] _id=69ea743e1724f0c9e2fb552f ts=2026-04-23T19:34:22.0680000Z; 46h 43m: 69cdc937d385e3b94310f75a.jsonl[794] _id=69dff00b7957a33870f49d31 ts=2026-04-15T20:07:38.6410000Z -> 69cdc937d385e3b94310f75a.jsonl[803] _id=69e281281724f0c9e2f78eec ts=2026-04-17T18:51:19.7710000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 69cdc937d385e3b94310f75a.jsonl[144] _id=69e28c1b1724f0c9e2f7b8ae ts=2026-04-17T19:38:02.8810000Z -> 69cdc937d385e3b94310f75a.jsonl[1440] _id=69e7cd741724f0c9e2f9ce43 ts=2026-04-21T19:18:11.2190000Z; 48h 14m: 69cdc937d385e3b94310f75a.jsonl[1468] _id=69e7cebe1724f0c9e2f9d2e3 ts=2026-04-21T19:23:41.3060000Z -> 69cdc937d385e3b94310f75a.jsonl[1696] _id=69ea75121724f0c9e2fb5675 ts=2026-04-23T19:37:53.8390000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 54m 
  - Evidence: 94h 54m: 69cdc937d385e3b94310f75a.jsonl[1245] _id=69e2937a1724f0c9e2f7dc3a ts=2026-04-17T20:09:30.8520000Z -> 69cdc937d385e3b94310f75a.jsonl[1339] _id=69e7ca211724f0c9e2f9b9d6 ts=2026-04-21T19:04:00.5500000Z; 47h 35m: 69cdc937d385e3b94310f75a.jsonl[5] _id=69dfeb727957a33870f489a9 ts=2026-04-15T19:48:01.4710000Z -> 69cdc937d385e3b94310f75a.jsonl[921] _id=69e2889c1724f0c9e2f7ac3a ts=2026-04-17T19:23:08.4590000Z; 25m 34s: 69cdc937d385e3b94310f75a.jsonl[1422] _id=69e7cc471724f0c9e2f9c623 ts=2026-04-21T19:13:10.1050000Z -> 69cdc937d385e3b94310f75a.jsonl[1551] _id=69e7d2451724f0c9e2f9e5a9 ts=2026-04-21T19:38:44.7310000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 69cdc937d385e3b94310f75a.jsonl[1155] _id=69e28eaa1724f0c9e2f7c8d4 ts=2026-04-17T19:48:58.3970000Z -> 69cdc937d385e3b94310f75a.jsonl[1344] _id=69e7ca231724f0c9e2f9b9e7 ts=2026-04-21T19:04:02.9060000Z; 47h 17m: 69cdc937d385e3b94310f75a.jsonl[19] _id=69dfef8e7957a33870f49b1f ts=2026-04-15T20:05:33.7540000Z -> 69cdc937d385e3b94310f75a.jsonl[1003] _id=69e288a21724f0c9e2f7ac5a ts=2026-04-17T19:23:14.1140000Z; 20m 15s: 69cdc937d385e3b94310f75a.jsonl[1011] _id=69e288a91724f0c9e2f7ac80 ts=2026-04-17T19:23:20.9610000Z -> 69cdc937d385e3b94310f75a.jsonl[1102] _id=69e28d691724f0c9e2f7bdfa ts=2026-04-17T19:43:36.8740000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 36m 
  - Evidence: 96h 36m: 69cdc937d385e3b94310f75a.jsonl[943] _id=69e2874e1724f0c9e2f7a638 ts=2026-04-17T19:17:34.5740000Z -> 69cdc937d385e3b94310f75a.jsonl[1641] _id=69e7d5d51724f0c9e2f9f2eb ts=2026-04-21T19:53:56.8820000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 36m 
  - Evidence: 96h 36m: 69cdc937d385e3b94310f75a.jsonl[111] _id=69e2873d1724f0c9e2f7a5ee ts=2026-04-17T19:17:16.9090000Z -> 69cdc937d385e3b94310f75a.jsonl[1643] _id=69e7d5e81724f0c9e2f9f327 ts=2026-04-21T19:54:15.2370000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 70h 59m 
  - Evidence: 70h 59m: 69cdc937d385e3b94310f75a.jsonl[311] _id=69e3e15d1724f0c9e2f84884 ts=2026-04-18T19:54:04.2280000Z -> 69cdc937d385e3b94310f75a.jsonl[1248] _id=69e7c7921724f0c9e2f9ac8d ts=2026-04-21T18:53:05.2450000Z; 47h 35m: 69cdc937d385e3b94310f75a.jsonl[1665] _id=69e7d6f31724f0c9e2f9f785 ts=2026-04-21T19:58:42.3330000Z -> 69cdc937d385e3b94310f75a.jsonl[1683] _id=69ea74411724f0c9e2fb5533 ts=2026-04-23T19:34:25.3530000Z; 46h 45m: 69cdc937d385e3b94310f75a.jsonl[780] _id=69dfefc17957a33870f49bea ts=2026-04-15T20:06:24.8440000Z -> 69cdc937d385e3b94310f75a.jsonl[801] _id=69e281391724f0c9e2f78f10 ts=2026-04-17T18:51:36.3840000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.005s..0.012s shown 
  - Evidence: 5ms: 69cdc937d385e3b94310f75a.jsonl[925] _id=69e286b21724f0c9e2f7a3a2 ts=2026-04-17T19:14:57.6070000Z -> 69cdc937d385e3b94310f75a.jsonl[97] _id=69e286b21724f0c9e2f7a3a4 ts=2026-04-17T19:14:57.6120000Z; 12ms: 69cdc937d385e3b94310f75a.jsonl[843] _id=69e283c11724f0c9e2f7984c ts=2026-04-17T19:02:25.4240000Z -> 69cdc937d385e3b94310f75a.jsonl[79] _id=69e283c11724f0c9e2f7984e ts=2026-04-17T19:02:25.4360000Z; 12ms: 69cdc937d385e3b94310f75a.jsonl[863] _id=69e284a71724f0c9e2f79bc4 ts=2026-04-17T19:06:15.6120000Z -> 69cdc937d385e3b94310f75a.jsonl[864] _id=69e284a81724f0c9e2f79bc6 ts=2026-04-17T19:06:15.6240000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc937d385e3b94310f75a.jsonl:69cdc937d385e3b94310f75a, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[144] _id=69e28c1b1724f0c9e2f7b8ae ts=2026-04-17T19:38:02.8810000Z`; `69cdc937d385e3b94310f75a.jsonl[1448] _id=69e7cdb21724f0c9e2f9cf97 ts=2026-04-21T19:19:13.5430000Z`; `69cdc937d385e3b94310f75a.jsonl[1699] _id=69ea75371724f0c9e2fb56dd ts=2026-04-23T19:38:31.6620000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 20 record(s) match the trigger in 69cdc937d385e3b94310f75a.jsonl:69cdc937d385e3b94310f75a, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[775] _id=69dfef857957a33870f49af1 ts=2026-04-15T20:05:24.5070000Z`; `69cdc937d385e3b94310f75a.jsonl[776] _id=69dfef857957a33870f49af3 ts=2026-04-15T20:05:25.1800000Z`; `69cdc937d385e3b94310f75a.jsonl[777] _id=69dfef877957a33870f49b03 ts=2026-04-15T20:05:27.0990000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[1525] _id=69e7d15d1724f0c9e2f9e0f9 ts=2026-04-21T19:34:52.3350000Z`; `69cdc937d385e3b94310f75a.jsonl[1542] _id=69e7d1ca1724f0c9e2f9e35b ts=2026-04-21T19:36:39.9620000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[558] _id=69e7d69f1724f0c9e2f9f64b ts=2026-04-21T19:57:17.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[545] _id=69e7d6821724f0c9e2f9f5dd ts=2026-04-21T19:56:50.0600000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[1687] _id=69ea74611724f0c9e2fb5553 ts=2026-04-23T19:34:57.4620000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc937d385e3b94310f75a.jsonl[385] _id=69e7c9311724f0c9e2f9b4b1 ts=?`; `69cdc937d385e3b94310f75a.jsonl[444] _id=69e7cef61724f0c9e2f9d3bf ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 167 unmatched 'DialogueStartEvent' (totals: 256 start, 91 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 32 start, 16 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.56s, min -24.77s, max -0.13s over 1779 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75a\coverage.yaml

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
  - Observed: 76 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `DialogueEvent` — 1171 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (573); Unit 1 Dev (261); Unit 3 Dev (235); Unit 3 Dungeon Dev (102)
- **eventKey:** present on 824 of 1171 records
- **Intervals:** median 2.23s (p5 0.01s / p95 56.34s, n=1170)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x824; [conversationId, dialogueEventType] x347
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1171/1171 records)
    numeric range 10 .. 101 (25 unique)
data.dialogueEventType  (string, 1171/1171 records)
    "DialogueNodeEvent"  x824
    "DialogueStartEvent"  x256
    "DialogueFinishEvent"  x91
data.nodeId  (number, 824/1171 records)
    numeric range 0 .. 289 (174 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 418 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (172); Unit 1 Dev (99); Unit 3 Dev (86); Unit 3 Dungeon Dev (61)
- **Intervals:** median 30.05s (p5 29.95s / p95 44.88s, n=413)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 418/418 records)
data.position.x  (number, 418/418 records)
    numeric range -666.157 .. 1601.18 (263 unique)
data.position.y  (number, 418/418 records)
    numeric range -115.126 .. 155.307 (165 unique)
data.position.z  (number, 418/418 records)
    numeric range -1194.03 .. 1814.95 (264 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 76 records

- **Scenes:** Unit 3 Dev (42); Unit 2 Prod (Refactor) (22); Unit 1 Dev (12)
- **Intervals:** median 8.24s (p5 1.45s / p95 1213.39s, n=75)
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapCloseEvent"  x38
    "MapOpenEvent"  x38
data.featureUsed  (string, 76/76 records)
    "Map"  x76
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 48 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 1 Dev (18); Unit 3 Dev (7); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 48 of 48 records
- **Intervals:** median 183.50s (p5 1.11s / p95 143258.24s, n=47)
- **`data` key-set variants:** [questEventType, questID, questName] x32; [questEventType, questID, questName, questSuccessOrFailure] x16
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 48/48 records)
    "questActiveEvent"  x32
    "questFinishEvent"  x16
data.questID  (string, 48/48 records)
    13 unique values (see csv/event_unique_values.csv)
data.questName  (string, 48/48 records)
    13 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 16/48 records)
    "Succeeded"  x16
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 26 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (19); Unit 1 Dev (7)
- **Intervals:** median 6.53s (p5 0.96s / p95 50.53s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "argumentationNodeAdd"  x17
    "argumentationNodeRemove"  x9
data.argumentationTitle  (string, 26/26 records)
    "Unit 3 - Pollution Upstream"  x19
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 26/26 records)
    "I"  x8
    "1"  x6
    "II"  x4
    "B"  x3
    "3"  x2
    "A"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 20 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (6)
- **Intervals:** median 6.69s (p5 1.22s / p95 187524.77s, n=19)
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

### `Soil Key Puzzle` — 7 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (2)
- **Intervals:** median 165.04s (p5 11.75s / p95 301719.39s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 7/7 records)
    "Started"  x4
    "Finished"  x3
data.Unit  (string, 7/7 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 40.53s (p5 7.63s / p95 260886.80s, n=6)
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

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 1.94s (p5 0.29s / p95 3.46s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 0.00s (p5 0.00s / p95 0.00s, n=1)
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x2
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Uncaught ReferenceError: onResize is not defined"  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit2:831:9)"  x2
data.type  (string, 2/2 records)
    "runtime_error"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x2
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (5 records)
- `TopographicMapEvent` data.actionType: "dragStart" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (9x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*