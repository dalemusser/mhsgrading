# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f71f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f71f
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f71f.jsonl
- **Records:** 1815 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f71f
- **Time span:** 2026-04-14T16:23:17.068000+00:00 .. 2026-04-23T18:40:38.941000+00:00 (218h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f71f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **9 event types**, 1815 records, 4 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 44 INFO, 5 NOT_TESTED, 30 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1290 | 71.07 | 1 | 4 | 928 | 2026-04-14T16:23:35.121000+00:00 | 2026-04-23T18:40:38.941000+00:00 | 218h 17m |
| PlayerPositionEvent | 399 | 21.98 | 1 | 4 | 0 | 2026-04-14T16:23:17.068000+00:00 | 2026-04-23T18:40:30.525000+00:00 | 218h 17m |
| questEvent | 44 | 2.42 | 1 | 4 | 44 | 2026-04-14T16:23:35.106000+00:00 | 2026-04-23T18:39:47.763000+00:00 | 218h 16m |
| Topographic Map Event | 28 | 1.54 | 1 | 1 | 0 | 2026-04-15T18:09:16.988000+00:00 | 2026-04-17T18:01:03.808000+00:00 | 47h 51m |
| TopographicMapEvent | 18 | 0.99 | 1 | 2 | 0 | 2026-04-15T18:30:31.483000+00:00 | 2026-04-23T18:16:23.078000+00:00 | 191h 45m |
| argumentationNodeEvent | 17 | 0.94 | 1 | 3 | 0 | 2026-04-15T18:03:11.981000+00:00 | 2026-04-23T18:21:18.262000+00:00 | 192h 18m |
| argumentationEvent | 9 | 0.5 | 1 | 3 | 0 | 2026-04-15T18:03:05.591000+00:00 | 2026-04-23T18:21:19.808000+00:00 | 192h 18m |
| Soil Key Puzzle | 8 | 0.44 | 1 | 2 | 0 | 2026-04-15T18:17:49.515000+00:00 | 2026-04-23T18:27:40.230000+00:00 | 192h 9m |
| EndOfUnit | 2 | 0.11 | 1 | 2 | 0 | 2026-04-15T18:08:05.927000+00:00 | 2026-04-17T18:23:13.863000+00:00 | 48h 15m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173707.936s median 
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
  - Observed: 63.63s median 
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
  - Observed: 11.865s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 14.31s median 
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
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 399 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 28 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 17 records 
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
  - Observed: 2; 4; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 15 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f71f.jsonl[102] _id=69dfd3637957a33870f42ba5 ts=2026-04-15T18:05:22.8480000Z`; `69cdc907d385e3b94310f71f.jsonl[771] _id=69dfd91d7957a33870f4506f ts=2026-04-15T18:29:49.1010000Z`; `69cdc907d385e3b94310f71f.jsonl[928] _id=69e2673c1724f0c9e2f72a2e ts=2026-04-17T17:00:43.5350000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 28 records, TopographicMapEvent: 18 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1289 | 0.0 | 2.274 | 609.638 | 34.747 | 516094.058 | 0.1 | 320 | 4 |
| PlayerPositionEvent | 394 | 10.06 | 30.006 | 1994.125 | 34.544 | 516055.421 | 0.03 | 0 | 3 |
| questEvent | 43 | 0.003 | 191.262 | 18273.783 | 82058.53 | 516093.445 | 0.0 | 4 | 10 |
| Topographic Map Event | 27 | 1.932 | 20.353 | 6381.734 | 2496.052 | 167048.682 | 0.01 | 0 | 2 |
| TopographicMapEvent | 17 | 0.494 | 11.865 | 40608.917 | 238192.304 | 522691.171 | 0.0 | 0 | 2 |
| argumentationNodeEvent | 16 | 1.618 | 14.31 | 43267.893 | 259803.013 | 518445.638 | 0.0 | 0 | 2 |
| argumentationEvent | 8 | 0.099 | 59.374 | 86536.777 | 397726.987 | 518422.141 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 7 | 2.986 | 63.63 | 98827.245 | 415131.258 | 521022.091 | 0.0 | 0 | 3 |
| EndOfUnit | 1 | 173707.936 | 173707.936 | 173707.936 | 173707.936 | 173707.936 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.006s (p5 29.96s, p95 34.54s, n=394) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `99ms: 69cdc907d385e3b94310f71f.jsonl[1665] _id=69ea63201724f0c9e2fb2c45 ts=2026-04-23T18:21:19.7090000Z ~ 69cdc907d385e3b94310f71f.jsonl[1667] _id=69ea63201724f0c9e2fb2c4f ts=2026-04-23T18:21:19.8080000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 69cdc907d385e3b94310f71f.jsonl[1515] _id=69e27e731724f0c9e2f78cb0 ts=2026-04-17T18:39:46.9460000Z -> 69cdc907d385e3b94310f71f.jsonl[1520] _id=69ea5e711724f0c9e2fb05a5 ts=2026-04-23T18:01:21.0040000Z; 46h 14m: 69cdc907d385e3b94310f71f.jsonl[149] _id=69dfdbc27957a33870f466cf ts=2026-04-15T18:41:05.9830000Z -> 69cdc907d385e3b94310f71f.jsonl[153] _id=69e265fb1724f0c9e2f72076 ts=2026-04-17T16:55:15.9410000Z; 25h 15m: 69cdc907d385e3b94310f71f.jsonl[399] _id=69de6bad7957a33870f37b19 ts=2026-04-14T16:30:37.8040000Z -> 69cdc907d385e3b94310f71f.jsonl[409] _id=69dfced47957a33870f40bb1 ts=2026-04-15T17:45:56.0960000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 320 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f71f.jsonl[294] _id=69e27a921724f0c9e2f77bae ts=2026-04-17T18:23:13.8870000Z -> 69cdc907d385e3b94310f71f.jsonl[1434] _id=69e27aa71724f0c9e2f77c08 ts=2026-04-17T18:23:13.887Z; 3ms: 69cdc907d385e3b94310f71f.jsonl[109] _id=69dfd3797957a33870f42c41 ts=2026-04-15T18:05:45.2530000Z -> 69cdc907d385e3b94310f71f.jsonl[107] _id=69dfd3797957a33870f42c43 ts=2026-04-15T18:05:45.2560000Z; 3ms: 69cdc907d385e3b94310f71f.jsonl[1127] _id=69e272d91724f0c9e2f7501e ts=2026-04-17T17:50:16.7230000Z -> 69cdc907d385e3b94310f71f.jsonl[1126] _id=69e272d91724f0c9e2f75020 ts=2026-04-17T17:50:16.7260000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 15m 
  - Evidence: 48h 15m: 69cdc907d385e3b94310f71f.jsonl[597] _id=69dfd4067957a33870f42fed ts=2026-04-15T18:08:05.9270000Z -> 69cdc907d385e3b94310f71f.jsonl[1429] _id=69e27a921724f0c9e2f77bac ts=2026-04-17T18:23:13.8630000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 20m 
  - Evidence: 143h 20m: 69cdc907d385e3b94310f71f.jsonl[1516] _id=69e27e711724f0c9e2f78ca4 ts=2026-04-17T18:39:45.2540000Z -> 69cdc907d385e3b94310f71f.jsonl[1517] _id=69ea5e4a1724f0c9e2fb04f1 ts=2026-04-23T18:00:40.6750000Z; 46h 13m: 69cdc907d385e3b94310f71f.jsonl[150] _id=69dfdbc87957a33870f466d5 ts=2026-04-15T18:41:12.0020000Z -> 69cdc907d385e3b94310f71f.jsonl[852] _id=69e265fb1724f0c9e2f72070 ts=2026-04-17T16:54:46.3130000Z; 25h 14m: 69cdc907d385e3b94310f71f.jsonl[400] _id=69de6bb97957a33870f37b1b ts=2026-04-14T16:30:49.2590000Z -> 69cdc907d385e3b94310f71f.jsonl[403] _id=69dfce977957a33870f40b6b ts=2026-04-15T17:44:54.6860000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 43m 
  - Evidence: 144h 43m: 69cdc907d385e3b94310f71f.jsonl[1066] _id=69e271361724f0c9e2f74482 ts=2026-04-17T17:43:18.0270000Z -> 69cdc907d385e3b94310f71f.jsonl[1695] _id=69ea64741724f0c9e2fb3573 ts=2026-04-23T18:27:00.1180000Z; 46h 40m: 69cdc907d385e3b94310f71f.jsonl[663] _id=69dfd6507957a33870f43c69 ts=2026-04-15T18:17:52.5010000Z -> 69cdc907d385e3b94310f71f.jsonl[892] _id=69e266c51724f0c9e2f726e4 ts=2026-04-17T16:58:45.1500000Z; 43m 26s: 69cdc907d385e3b94310f71f.jsonl[896] _id=69e266c81724f0c9e2f726ea ts=2026-04-17T16:58:48.1890000Z -> 69cdc907d385e3b94310f71f.jsonl[226] _id=69e270f71724f0c9e2f742e4 ts=2026-04-17T17:42:14.3970000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 24m 
  - Evidence: 46h 24m: 69cdc907d385e3b94310f71f.jsonl[818] _id=69dfdac57957a33870f45f9b ts=2026-04-15T18:36:53.6070000Z -> 69cdc907d385e3b94310f71f.jsonl[189] _id=69e2674f1724f0c9e2f72ad6 ts=2026-04-17T17:01:02.2890000Z; 55m 59s: 69cdc907d385e3b94310f71f.jsonl[976] _id=69e268321724f0c9e2f732a8 ts=2026-04-17T17:04:49.9190000Z -> 69cdc907d385e3b94310f71f.jsonl[1242] _id=69e275511724f0c9e2f76072 ts=2026-04-17T18:00:49.0270000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 145h 11m 
  - Evidence: 145h 11m: 69cdc907d385e3b94310f71f.jsonl[975] _id=69e268321724f0c9e2f732a6 ts=2026-04-17T17:04:49.7760000Z -> 69cdc907d385e3b94310f71f.jsonl[1616] _id=69ea61f51724f0c9e2fb22b9 ts=2026-04-23T18:16:20.9470000Z; 46h 24m: 69cdc907d385e3b94310f71f.jsonl[817] _id=69dfdac07957a33870f45f73 ts=2026-04-15T18:36:48.6050000Z -> 69cdc907d385e3b94310f71f.jsonl[937] _id=69e2675c1724f0c9e2f72b4a ts=2026-04-17T17:01:16.1920000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 69cdc907d385e3b94310f71f.jsonl[1394] _id=69e279a71724f0c9e2f7773a ts=2026-04-17T18:19:19.5060000Z -> 69cdc907d385e3b94310f71f.jsonl[333] _id=69ea62be1724f0c9e2fb294f ts=2026-04-23T18:19:41.6470000Z; 48h 12m: 69cdc907d385e3b94310f71f.jsonl[101] _id=69dfd3627957a33870f42ba1 ts=2026-04-15T18:05:22.8190000Z -> 69cdc907d385e3b94310f71f.jsonl[1355] _id=69e2796d1724f0c9e2f775ee ts=2026-04-17T18:18:21.6640000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 69cdc907d385e3b94310f71f.jsonl[1389] _id=69e2799c1724f0c9e2f776ec ts=2026-04-17T18:19:08.6400000Z -> 69cdc907d385e3b94310f71f.jsonl[1647] _id=69ea62cb1724f0c9e2fb299f ts=2026-04-23T18:19:54.2780000Z; 48h 13m: 69cdc907d385e3b94310f71f.jsonl[560] _id=69dfd3617957a33870f42b91 ts=2026-04-15T18:05:21.0020000Z -> 69cdc907d385e3b94310f71f.jsonl[1377] _id=69e279761724f0c9e2f7761e ts=2026-04-17T18:18:29.8070000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 69cdc907d385e3b94310f71f.jsonl[1514] _id=69e27e4e1724f0c9e2f78bf8 ts=2026-04-17T18:39:10.0860000Z -> 69cdc907d385e3b94310f71f.jsonl[1518] _id=69ea5e4c1724f0c9e2fb0501 ts=2026-04-23T18:00:43.5310000Z; 46h 14m: 69cdc907d385e3b94310f71f.jsonl[845] _id=69dfdbc17957a33870f466c9 ts=2026-04-15T18:41:05.3240000Z -> 69cdc907d385e3b94310f71f.jsonl[857] _id=69e266001724f0c9e2f720aa ts=2026-04-17T16:55:27.8700000Z; 25h 15m: 69cdc907d385e3b94310f71f.jsonl[65] _id=69de6b817957a33870f37afb ts=2026-04-14T16:29:53.6080000Z -> 69cdc907d385e3b94310f71f.jsonl[404] _id=69dfce987957a33870f40b6f ts=2026-04-15T17:44:55.6760000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.003s..0.007s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f71f.jsonl[93] _id=69dfd2647957a33870f424d9 ts=2026-04-15T18:01:07.9790000Z -> 69cdc907d385e3b94310f71f.jsonl[529] _id=69dfd2647957a33870f424dd ts=2026-04-15T18:01:07.9820000Z; 6ms: 69cdc907d385e3b94310f71f.jsonl[440] _id=69dfcfda7957a33870f41141 ts=2026-04-15T17:50:18.4860000Z -> 69cdc907d385e3b94310f71f.jsonl[441] _id=69dfcfda7957a33870f41145 ts=2026-04-15T17:50:18.4920000Z; 7ms: 69cdc907d385e3b94310f71f.jsonl[51] _id=69de6b817957a33870f37af9 ts=2026-04-14T16:29:53.6010000Z -> 69cdc907d385e3b94310f71f.jsonl[65] _id=69de6b817957a33870f37afb ts=2026-04-14T16:29:53.6080000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc907d385e3b94310f71f.jsonl:69cdc907d385e3b94310f71f, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f71f.jsonl[663] _id=69dfd6507957a33870f43c69 ts=2026-04-15T18:17:52.5010000Z`; `69cdc907d385e3b94310f71f.jsonl[896] _id=69e266c81724f0c9e2f726ea ts=2026-04-17T16:58:48.1890000Z`; `69cdc907d385e3b94310f71f.jsonl[1066] _id=69e271361724f0c9e2f74482 ts=2026-04-17T17:43:18.0270000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 18 record(s) match the trigger in 69cdc907d385e3b94310f71f.jsonl:69cdc907d385e3b94310f71f, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f71f.jsonl[775] _id=69dfd9477957a33870f4516b ts=2026-04-15T18:30:31.4830000Z`; `69cdc907d385e3b94310f71f.jsonl[778] _id=69dfd9537957a33870f451cf ts=2026-04-15T18:30:43.3480000Z`; `69cdc907d385e3b94310f71f.jsonl[798] _id=69dfd9ed7957a33870f455c3 ts=2026-04-15T18:33:17.3860000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f71f.jsonl[1170] _id=69e273e81724f0c9e2f7571b ts=2026-04-17T17:54:48.4090000Z`; `69cdc907d385e3b94310f71f.jsonl[1495] _id=69e27dcc1724f0c9e2f78892 ts=2026-04-17T18:36:59.9310000Z`; `69cdc907d385e3b94310f71f.jsonl[1513] _id=69e27e4e1724f0c9e2f78bfc ts=2026-04-17T18:39:10.1580000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f71f.jsonl[1667] _id=69ea63201724f0c9e2fb2c4f ts=2026-04-23T18:21:19.8080000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 149 unmatched 'DialogueStartEvent' (totals: 254 start, 108 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 6 unmatched 'questActiveEvent' (totals: 25 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.34s, min -72.31s, max -0.10s over 1815 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f71f\coverage.yaml

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
  - Observed: 28 records 
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

### `DialogueEvent` — 1290 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (710); Unit 3 Dev (245); Unit 1 Dev (244); Unit 3 Dungeon Dev (91)
- **eventKey:** present on 928 of 1290 records
- **Intervals:** median 2.27s (p5 0.01s / p95 34.75s, n=1289)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x928; [conversationId, dialogueEventType] x362
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1290/1290 records)
    numeric range 8 .. 103 (34 unique)
data.dialogueEventType  (string, 1290/1290 records)
    "DialogueNodeEvent"  x928
    "DialogueStartEvent"  x254
    "DialogueFinishEvent"  x108
data.nodeId  (number, 928/1290 records)
    numeric range 0 .. 290 (208 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 399 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (234); Unit 3 Dev (78); Unit 1 Dev (63); Unit 3 Dungeon Dev (24)
- **Intervals:** median 30.01s (p5 29.96s / p95 34.54s, n=394)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 399/399 records)
data.position.x  (number, 399/399 records)
    numeric range -558.38 .. 1508.82 (155 unique)
data.position.y  (number, 399/399 records)
    numeric range -112.338 .. 163.875 (137 unique)
data.position.z  (number, 399/399 records)
    numeric range -1107.01 .. 1805.27 (155 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 44 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (15); Unit 3 Dev (8); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 44 of 44 records
- **Intervals:** median 191.26s (p5 0.01s / p95 82058.53s, n=43)
- **`data` key-set variants:** [questEventType, questID, questName] x25; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Fields under `data`:**

```text
data.questEventType  (string, 44/44 records)
    "questActiveEvent"  x25
    "questFinishEvent"  x19
data.questID  (string, 44/44 records)
    15 unique values (see csv/event_unique_values.csv)
data.questName  (string, 44/44 records)
    15 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/44 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 28 records

- **Scenes:** Unit 2 Prod (Refactor) (28)
- **Intervals:** median 20.35s (p5 3.13s / p95 2496.05s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "MapCloseEvent"  x14
    "MapOpenEvent"  x14
data.featureUsed  (string, 28/28 records)
    "Map"  x28
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 18 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (2)
- **Intervals:** median 11.87s (p5 0.52s / p95 238192.30s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "dragEnd"  x9
    "dragStart"  x9
data.featureUsed  (string, 18/18 records)
    "waypoint"  x18
data.location  (object, 18/18 records)
data.location.x  (number, 18/18 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 18/18 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 18/18 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 17 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (7); Unit 1 Dev (5); Unit 2 Prod (Refactor) (5)
- **Intervals:** median 14.31s (p5 2.44s / p95 259803.01s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 17/17 records)
    "Unit 3 - Pollution Upstream"  x7
    "Unit 2 – Watershed"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 17/17 records)
    "1"  x3
    "A"  x3
    "B"  x3
    "3"  x2
    "D"  x2
    "I"  x2
    "5"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 59.37s (p5 9.21s / p95 397726.99s, n=8)
- **Open findings:** 1 — see sections 5-8
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
- **Intervals:** median 63.63s (p5 3.00s / p95 415131.26s, n=7)
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

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 173707.94s (p5 173707.94s / p95 173707.94s, n=1)
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
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (9x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*