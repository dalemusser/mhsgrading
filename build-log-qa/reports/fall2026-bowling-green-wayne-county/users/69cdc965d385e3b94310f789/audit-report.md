# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f789

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f789
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f789.jsonl
- **Records:** 1604 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f789
- **Time span:** 2026-04-14T14:25:52.700000+00:00 .. 2026-04-28T14:25:29.088000+00:00 (335h 59m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f789\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1604 records, 6 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 53 INFO, 2 NOT_TESTED, 38 PASS.
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
| DialogueEvent | 1103 | 68.77 | 1 | 6 | 776 | 2026-04-14T14:26:11.346000+00:00 | 2026-04-28T14:16:03.375000+00:00 | 335h 49m |
| PlayerPositionEvent | 355 | 22.13 | 1 | 6 | 0 | 2026-04-14T14:25:52.700000+00:00 | 2026-04-28T14:25:29.088000+00:00 | 335h 59m |
| questEvent | 50 | 3.12 | 1 | 6 | 50 | 2026-04-14T14:26:11.332000+00:00 | 2026-04-28T14:13:21.252000+00:00 | 335h 47m |
| Topographic Map Event | 36 | 2.24 | 1 | 2 | 0 | 2026-04-16T13:55:19.058000+00:00 | 2026-04-22T14:27:16.397000+00:00 | 144h 31m |
| argumentationNodeEvent | 24 | 1.5 | 1 | 2 | 0 | 2026-04-16T13:46:15.064000+00:00 | 2026-04-22T14:03:22.035000+00:00 | 144h 17m |
| soilMachine | 11 | 0.69 | 1 | 1 | 0 | 2026-04-24T14:30:39.337000+00:00 | 2026-04-28T14:16:45.312000+00:00 | 95h 46m |
| Soil Key Puzzle | 8 | 0.5 | 1 | 3 | 0 | 2026-04-16T14:04:24.424000+00:00 | 2026-04-24T14:14:58.020000+00:00 | 192h 10m |
| argumentationEvent | 7 | 0.44 | 1 | 2 | 0 | 2026-04-16T13:45:58.304000+00:00 | 2026-04-22T14:03:23.504000+00:00 | 144h 17m |
| TopographicMapEvent | 4 | 0.25 | 1 | 2 | 0 | 2026-04-16T14:09:19.698000+00:00 | 2026-04-22T14:06:48.577000+00:00 | 143h 57m |
| crash | 4 | 0.25 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.12 | 1 | 2 | 0 | 2026-04-16T13:51:42.837000+00:00 | 2026-04-24T14:00:46.829000+00:00 | 192h 9m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.353s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 691743.992s median 
  - Expected: 2855.05s in 09-23-26 
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
  - Observed: 76.66s median 
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
  - Observed: 9.604s median 
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
  - Observed: 17.842s median 
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
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 355 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 8 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 36 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 4 records 
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
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 36; 40; 41; 43; 44; 45; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 13 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f789.jsonl[710] _id=69e0e88e7957a33870f5113b ts=2026-04-16T13:47:58.2540000Z`; `69cdc965d385e3b94310f789.jsonl[886] _id=69e0ed837957a33870f52e95 ts=2026-04-16T14:09:06.8600000Z`; `69cdc965d385e3b94310f789.jsonl[140] _id=69e0ee867957a33870f535db ts=2026-04-16T14:13:26.2830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 36 records, TopographicMapEvent: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1102 | 0.002 | 1.353 | 1097.089 | 46.564 | 514364.641 | 0.05 | 265 | 5 |
| PlayerPositionEvent | 348 | 27.76 | 30.008 | 1997.362 | 34.802 | 344038.947 | 0.03 | 0 | 3 |
| questEvent | 49 | 0.002 | 135.665 | 24669.998 | 170481.007 | 514454.265 | 0.0 | 8 | 7 |
| Topographic Map Event | 35 | 0.702 | 10.766 | 14866.21 | 934.356 | 516231.477 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 23 | 1.058 | 9.604 | 22583.781 | 49.239 | 519139.037 | 0.0 | 0 | 1 |
| soilMachine | 10 | 1.868 | 17.842 | 34476.597 | 189436.488 | 344263.191 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 7 | 3.002 | 76.66 | 98833.371 | 414855.703 | 518698.091 | 0.0 | 0 | 2 |
| argumentationEvent | 6 | 0.133 | 58.061 | 86574.2 | 389395.277 | 519127.984 | 0.0 | 0 | 1 |
| TopographicMapEvent | 3 | 3.209 | 3.492 | 172749.626 | 466418.309 | 518242.178 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 691743.992 | 691743.992 | 691743.992 | 691743.992 | 691743.992 | 0.0 | 0 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc965d385e3b94310f789.jsonl[1010] _id=69e8cc5c1724f0c9e2fa1711 ts=? == 69cdc965d385e3b94310f789.jsonl[1027] _id=69e8cd681724f0c9e2fa1d51 ts=?`; `69cdc965d385e3b94310f789.jsonl[1523] _id=69eb7baa1724f0c9e2fb8f7f ts=? == 69cdc965d385e3b94310f789.jsonl[477] _id=69f0bfa41724f0c9e2fcaa31 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.95s, p95 34.80s, n=348) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `133ms: 69cdc965d385e3b94310f789.jsonl[1205] _id=69e8d52b1724f0c9e2fa4f87 ts=2026-04-22T14:03:23.3710000Z ~ 69cdc965d385e3b94310f789.jsonl[311] _id=69e8d52b1724f0c9e2fa4f8d ts=2026-04-22T14:03:23.5040000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 142h 52m 
  - Evidence: 142h 52m: 69cdc965d385e3b94310f789.jsonl[984] _id=69e0f22d7957a33870f54b93 ts=2026-04-16T14:29:00.7980000Z -> 69cdc965d385e3b94310f789.jsonl[166] _id=69e8cb691724f0c9e2fa11e1 ts=2026-04-22T13:21:45.4390000Z; 95h 34m: 69cdc965d385e3b94310f789.jsonl[1593] _id=69eb7f551724f0c9e2fba211 ts=2026-04-24T14:33:57.2720000Z -> 69cdc965d385e3b94310f789.jsonl[469] _id=69f0bf6f1724f0c9e2fca9bf ts=2026-04-28T14:08:45.9930000Z; 47h 31m: 69cdc965d385e3b94310f789.jsonl[1407] _id=69e8db141724f0c9e2fa740d ts=2026-04-22T14:28:36.2530000Z -> 69cdc965d385e3b94310f789.jsonl[1416] _id=69eb775c1724f0c9e2fb78db ts=2026-04-24T13:59:55.9140000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 265 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f789.jsonl[1351] _id=69e8da171724f0c9e2fa6d9f ts=2026-04-22T14:24:22.5920000Z -> 69cdc965d385e3b94310f789.jsonl[1352] _id=69e8da171724f0c9e2fa6da1 ts=2026-04-22T14:24:22.5940000Z; 2ms: 69cdc965d385e3b94310f789.jsonl[728] _id=69e0e8cd7957a33870f51309 ts=2026-04-16T13:49:01.6180000Z -> 69cdc965d385e3b94310f789.jsonl[86] _id=69e0e8cd7957a33870f5130b ts=2026-04-16T13:49:01.6200000Z; 3ms: 69cdc965d385e3b94310f789.jsonl[118] _id=69e0ed6b7957a33870f52de5 ts=2026-04-16T14:08:41.6590000Z -> 69cdc965d385e3b94310f789.jsonl[873] _id=69e0ed6b7957a33870f52de9 ts=2026-04-16T14:08:41.6620000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 192h 9m 
  - Evidence: 192h 9m: 69cdc965d385e3b94310f789.jsonl[752] _id=69e0e96e7957a33870f516d1 ts=2026-04-16T13:51:42.8370000Z -> 69cdc965d385e3b94310f789.jsonl[1429] _id=69eb778f1724f0c9e2fb7a17 ts=2026-04-24T14:00:46.8290000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f789.jsonl[1601] _id=69eb7f811724f0c9e2fba313 ts=2026-04-24T14:34:40.7790000Z -> 69cdc965d385e3b94310f789.jsonl[467] _id=69f0bf681724f0c9e2fca9b1 ts=2026-04-28T14:08:39.7260000Z; 47h 30m: 69cdc965d385e3b94310f789.jsonl[1406] _id=69e8db0a1724f0c9e2fa73cb ts=2026-04-22T14:28:26.5870000Z -> 69cdc965d385e3b94310f789.jsonl[1409] _id=69eb77091724f0c9e2fb7769 ts=2026-04-24T13:58:32.6370000Z; 47h 3m: 69cdc965d385e3b94310f789.jsonl[570] _id=69de4fc37957a33870f36aa2 ts=2026-04-14T14:31:31.4790000Z -> 69cdc965d385e3b94310f789.jsonl[573] _id=69e0e58a7957a33870f4fd6f ts=2026-04-16T13:35:05.8950000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 4m 
  - Evidence: 144h 4m: 69cdc965d385e3b94310f789.jsonl[834] _id=69e0ec6b7957a33870f52793 ts=2026-04-16T14:04:27.4260000Z -> 69cdc965d385e3b94310f789.jsonl[1260] _id=69e8d6951724f0c9e2fa5a35 ts=2026-04-22T14:09:25.5170000Z; 47h 55m: 69cdc965d385e3b94310f789.jsonl[1261] _id=69e8d6a61724f0c9e2fa5aa1 ts=2026-04-22T14:09:42.0670000Z -> 69cdc965d385e3b94310f789.jsonl[1451] _id=69eb78b31724f0c9e2fb8101 ts=2026-04-24T14:05:38.8630000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 23m 
  - Evidence: 143h 23m: 69cdc965d385e3b94310f789.jsonl[935] _id=69e0ef417957a33870f539f1 ts=2026-04-16T14:16:33.2920000Z -> 69cdc965d385e3b94310f789.jsonl[1087] _id=69e8cfc81724f0c9e2fa2f49 ts=2026-04-22T13:40:24.7690000Z; 20m 22s: 69cdc965d385e3b94310f789.jsonl[1243] _id=69e8d5fa1724f0c9e2fa558f ts=2026-04-22T14:06:50.1820000Z -> 69cdc965d385e3b94310f789.jsonl[1384] _id=69e8dac01724f0c9e2fa71cd ts=2026-04-22T14:27:12.8010000Z; 13m 30s: 69cdc965d385e3b94310f789.jsonl[260] _id=69e8d2c41724f0c9e2fa4239 ts=2026-04-22T13:53:08.6010000Z -> 69cdc965d385e3b94310f789.jsonl[339] _id=69e8d5ef1724f0c9e2fa5551 ts=2026-04-22T14:06:39.4160000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 69cdc965d385e3b94310f789.jsonl[125] _id=69e0ed927957a33870f52f09 ts=2026-04-16T14:09:22.9070000Z -> 69cdc965d385e3b94310f789.jsonl[1244] _id=69e8d5f51724f0c9e2fa557b ts=2026-04-22T14:06:45.0850000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 69cdc965d385e3b94310f789.jsonl[709] _id=69e0e88e7957a33870f51137 ts=2026-04-16T13:47:58.2300000Z -> 69cdc965d385e3b94310f789.jsonl[1184] _id=69e8d4661724f0c9e2fa49d7 ts=2026-04-22T14:00:06.2140000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 69cdc965d385e3b94310f789.jsonl[707] _id=69e0e8897957a33870f510f9 ts=2026-04-16T13:47:53.0020000Z -> 69cdc965d385e3b94310f789.jsonl[1187] _id=69e8d46c1724f0c9e2fa49fd ts=2026-04-22T14:00:12.0390000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 142h 54m 
  - Evidence: 142h 54m: 69cdc965d385e3b94310f789.jsonl[981] _id=69e0f22c7957a33870f54b7d ts=2026-04-16T14:29:00.1450000Z -> 69cdc965d385e3b94310f789.jsonl[171] _id=69e8cbc21724f0c9e2fa13af ts=2026-04-22T13:23:14.4100000Z; 95h 34m: 69cdc965d385e3b94310f789.jsonl[1591] _id=69eb7f4c1724f0c9e2fba1db ts=2026-04-24T14:33:47.9090000Z -> 69cdc965d385e3b94310f789.jsonl[468] _id=69f0bf6f1724f0c9e2fca9bd ts=2026-04-28T14:08:45.4880000Z; 47h 30m: 69cdc965d385e3b94310f789.jsonl[390] _id=69e8dae11724f0c9e2fa727f ts=2026-04-22T14:27:45.8110000Z -> 69cdc965d385e3b94310f789.jsonl[1410] _id=69eb770d1724f0c9e2fb7771 ts=2026-04-24T13:58:36.1800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f789.jsonl[682] _id=69e0e8077957a33870f50dbb ts=2026-04-16T13:45:43.6450000Z -> 69cdc965d385e3b94310f789.jsonl[63] _id=69e0e8087957a33870f50dbd ts=2026-04-16T13:45:43.6470000Z; 4ms: 69cdc965d385e3b94310f789.jsonl[15] _id=69e0e6d67957a33870f50573 ts=2026-04-16T13:40:38.7580000Z -> 69cdc965d385e3b94310f789.jsonl[16] _id=69e0e6d67957a33870f50575 ts=2026-04-16T13:40:38.7620000Z; 6ms: 69cdc965d385e3b94310f789.jsonl[33] _id=69e0e6467957a33870f50201 ts=2026-04-16T13:38:14.1360000Z -> 69cdc965d385e3b94310f789.jsonl[34] _id=69e0e6467957a33870f50203 ts=2026-04-16T13:38:14.1420000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 69cdc965d385e3b94310f789.jsonl[1600] _id=69eb7f771724f0c9e2fba2c7 ts=2026-04-24T14:34:31.6780000Z -> 69cdc965d385e3b94310f789.jsonl[490] _id=69f0c03f1724f0c9e2fcaa75 ts=2026-04-28T14:12:14.8690000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc965d385e3b94310f789.jsonl:69cdc965d385e3b94310f789, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f789.jsonl[834] _id=69e0ec6b7957a33870f52793 ts=2026-04-16T14:04:27.4260000Z`; `69cdc965d385e3b94310f789.jsonl[1261] _id=69e8d6a61724f0c9e2fa5aa1 ts=2026-04-22T14:09:42.0670000Z`; `69cdc965d385e3b94310f789.jsonl[1447] _id=69eb78ff1724f0c9e2fb81e7 ts=2026-04-24T14:06:55.5230000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc965d385e3b94310f789.jsonl:69cdc965d385e3b94310f789, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f789.jsonl[889] _id=69e0ed8f7957a33870f52ef0 ts=2026-04-16T14:09:19.6980000Z`; `69cdc965d385e3b94310f789.jsonl[125] _id=69e0ed927957a33870f52f09 ts=2026-04-16T14:09:22.9070000Z`; `69cdc965d385e3b94310f789.jsonl[1244] _id=69e8d5f51724f0c9e2fa557b ts=2026-04-22T14:06:45.0850000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f789.jsonl[204] _id=69e8cdb71724f0c9e2fa1f83 ts=2026-04-22T13:31:34.8330000Z`; `69cdc965d385e3b94310f789.jsonl[217] _id=69e8ce0a1724f0c9e2fa220f ts=2026-04-22T13:32:57.4170000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f789.jsonl[311] _id=69e8d52b1724f0c9e2fa4f8d ts=2026-04-22T14:03:23.5040000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f789.jsonl[9] _id=69de4f027957a33870f363fa ts=2026-04-14T14:28:18.1420000Z`; `69cdc965d385e3b94310f789.jsonl[465] _id=69f0bf741724f0c9e2fca9c9 ts=2026-04-28T14:08:52.3090000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `69cdc965d385e3b94310f789.jsonl[1010] _id=69e8cc5c1724f0c9e2fa1711 ts=?`; `69cdc965d385e3b94310f789.jsonl[1027] _id=69e8cd681724f0c9e2fa1d51 ts=?`; `69cdc965d385e3b94310f789.jsonl[1523] _id=69eb7baa1724f0c9e2fb8f7f ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 141 unmatched 'DialogueStartEvent' (totals: 233 start, 94 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 31 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.22s, min -11.55s, max +0.02s over 1600 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f789\coverage.yaml

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
  - Observed: 36 records 
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

### `DialogueEvent` — 1103 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (432); Unit 1 Dev (234); Unit 2 Prod (Refactor) (206); Unit 4 Dev - Dungeon (105); Unit 3 Dungeon Dev (76); Unit 4 Dev (50)
- **eventKey:** present on 776 of 1103 records
- **Intervals:** median 1.35s (p5 0.01s / p95 46.56s, n=1102)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x776; [conversationId, dialogueEventType] x327
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1103/1103 records)
    numeric range 10 .. 104 (32 unique)
data.dialogueEventType  (string, 1103/1103 records)
    "DialogueNodeEvent"  x776
    "DialogueStartEvent"  x233
    "DialogueFinishEvent"  x94
data.nodeId  (number, 776/1103 records)
    numeric range 0 .. 283 (192 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 355 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (107); Unit 2 Prod (Refactor) (73); Unit 4 Dev - Dungeon (69); Unit 1 Dev (45); Unit 4 Dev (33); Unit 3 Dungeon Dev (28)
- **Intervals:** median 30.01s (p5 29.95s / p95 34.80s, n=348)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 355/355 records)
data.position.x  (number, 355/355 records)
    numeric range -573.884 .. 1313.09 (209 unique)
data.position.y  (number, 355/355 records)
    numeric range -2.31117e+06 .. 159.233 (179 unique)
data.position.z  (number, 355/355 records)
    numeric range -1113.68 .. 1739.98 (211 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 50 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (15); Unit 3 Dev (11); Unit 4 Dev - Dungeon (11); Unit 2 Prod (Refactor) (9); Unit 3 Dungeon Dev (2); Unit 4 Dev (2)
- **eventKey:** present on 50 of 50 records
- **Intervals:** median 135.66s (p5 0.01s / p95 170481.01s, n=49)
- **`data` key-set variants:** [questEventType, questID, questName] x31; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 50/50 records)
    "questActiveEvent"  x31
    "questFinishEvent"  x19
data.questID  (string, 50/50 records)
    20 unique values (see csv/event_unique_values.csv)
data.questName  (string, 50/50 records)
    20 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 19/50 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 36 records

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (12)
- **Intervals:** median 10.77s (p5 0.92s / p95 934.36s, n=35)
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
data.featureUsed  (string, 36/36 records)
    "Map"  x36
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 24 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (13); Unit 1 Dev (11)
- **Intervals:** median 9.60s (p5 1.08s / p95 49.24s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x9
data.argumentationTitle  (string, 24/24 records)
    "Unit 3 - Pollution Upstream"  x13
    "Unit 1 - Freshwater"  x11
data.nodeName  (string, 24/24 records)
    "1"  x5
    "A"  x5
    "II"  x4
    "B"  x3
    "2"  x2
    "3"  x2
    "I"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 17.84s (p5 1.87s / p95 189436.49s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Gravel"  x6
    "Clay"  x2
    "Sand"  x2
    "Bedrock"  x1
data.floor  (string, 11/11 records)
    "4"  x9
    "3"  x2
data.machine  (string, 11/11 records)
    "1"  x11
data.row  (string, 11/11 records)
    "TopRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 8 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (4); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 76.66s (p5 7.07s / p95 414855.70s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/8 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/8 records)
    "Unit 4 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 58.06s (p5 1.05s / p95 389395.28s, n=6)
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

### `TopographicMapEvent` — 4 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 3.49s (p5 3.24s / p95 466418.31s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "dragEnd"  x2
    "dragStart"  x2
data.featureUsed  (string, 4/4 records)
    "waypoint"  x4
data.location  (object, 4/4 records)
data.location.x  (number, 4/4 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 4/4 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 4/4 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "Uncaught ReferenceError: onResize is not defined"  x4
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x2
data.type  (string, 4/4 records)
    "runtime_error"  x4
data.unitId  (string, 4/4 records)
    "unit3"  x2
    "unit4"  x2
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 691743.99s (p5 691743.99s / p95 691743.99s, n=1)
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
- `TopographicMapEvent` data.actionType: "dragStart" (2x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (9x)
- `soilMachine` data.canisterType: "Bedrock" (1x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*