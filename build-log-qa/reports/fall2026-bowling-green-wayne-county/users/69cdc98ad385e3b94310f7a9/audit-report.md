# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7a9

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7a9
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7a9.jsonl
- **Records:** 1958 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7a9
- **Time span:** 2026-04-14T19:36:23.636000+00:00 .. 2026-04-22T20:04:30.784000+00:00 (192h 28m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7a9\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 1958 records, 6 scenes.
- Findings: **0 FAIL**, **43 WARNING**, 48 INFO, 2 NOT_TESTED, 39 PASS.
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
| DialogueEvent | 1298 | 66.29 | 1 | 6 | 899 | 2026-04-14T19:36:42.470000+00:00 | 2026-04-22T20:04:30.784000+00:00 | 192h 27m |
| PlayerPositionEvent | 502 | 25.64 | 1 | 6 | 0 | 2026-04-14T19:36:23.636000+00:00 | 2026-04-22T20:04:21.120000+00:00 | 192h 27m |
| questEvent | 58 | 2.96 | 1 | 6 | 58 | 2026-04-14T19:36:42.448000+00:00 | 2026-04-22T19:46:47.295000+00:00 | 192h 10m |
| Topographic Map Event | 40 | 2.04 | 1 | 3 | 0 | 2026-04-16T18:57:48.988000+00:00 | 2026-04-22T19:19:15.926000+00:00 | 144h 21m |
| TopographicMapEvent | 15 | 0.77 | 1 | 2 | 0 | 2026-04-16T19:31:02.814000+00:00 | 2026-04-20T20:08:17.481000+00:00 | 96h 37m |
| argumentationNodeEvent | 15 | 0.77 | 1 | 2 | 0 | 2026-04-14T19:58:21.227000+00:00 | 2026-04-20T19:14:47.545000+00:00 | 143h 16m |
| soilMachine | 11 | 0.56 | 1 | 1 | 0 | 2026-04-22T19:34:10.283000+00:00 | 2026-04-22T19:41:14.062000+00:00 | 7m 3s |
| argumentationEvent | 7 | 0.36 | 1 | 2 | 0 | 2026-04-14T19:58:15.554000+00:00 | 2026-04-20T19:14:49.074000+00:00 | 143h 16m |
| Soil Key Puzzle | 6 | 0.31 | 1 | 3 | 0 | 2026-04-16T19:58:21.268000+00:00 | 2026-04-22T18:58:27.537000+00:00 | 143h 0m |
| EndOfUnit | 3 | 0.15 | 1 | 2 | 0 | 2026-04-14T20:03:08.255000+00:00 | 2026-04-22T18:51:42.553000+00:00 | 190h 48m |
| crash | 3 | 0.15 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 343457.149s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.017s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 54.375s median 
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
  - Observed: 10.075s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 4.957s median 
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
  - Observed: 15.358s median 
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
  - Observed: 40 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
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
  - Observed: 15 records 
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
  - Observed: 2; 3; 4; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 26 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[742] _id=69de9cb27957a33870f3af0b ts=2026-04-14T19:59:46.0950000Z`; `69cdc98ad385e3b94310f7a9.jsonl[81] _id=69e132a71724f0c9e2f69c7c ts=2026-04-16T18:50:05.528Z`; `69cdc98ad385e3b94310f7a9.jsonl[834] _id=69e132a81724f0c9e2f69c86 ts=2026-04-16T18:50:38.592Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 40 records, TopographicMapEvent: 15 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1297 | 0.0 | 2.497 | 534.208 | 48.015 | 340941.029 | 0.11 | 325 | 4 |
| PlayerPositionEvent | 494 | 29.85 | 30.017 | 712.08 | 38.383 | 168074.152 | 0.08 | 0 | 2 |
| questEvent | 57 | 0.004 | 181.391 | 12136.927 | 35075.496 | 341079.663 | 0.0 | 7 | 9 |
| Topographic Map Event | 39 | 0.604 | 10.1 | 13325.306 | 19196.268 | 341188.404 | 0.0 | 0 | 4 |
| TopographicMapEvent | 14 | 0.25 | 10.075 | 24845.333 | 121932.971 | 346469.58 | 0.0 | 0 | 2 |
| argumentationNodeEvent | 14 | 1.387 | 4.957 | 36841.88 | 180514.768 | 515646.025 | 0.0 | 0 | 1 |
| soilMachine | 10 | 0.911 | 15.358 | 42.378 | 128.217 | 164.16 | 1.42 | 0 | 0 |
| argumentationEvent | 6 | 0.124 | 34.587 | 85965.587 | 386744.078 | 515636.704 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 5 | 25.687 | 54.375 | 102961.254 | 308911.803 | 343287.589 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 0.0 | 343457.149 | 343457.149 | 652568.583 | 686914.298 | 0.0 | 1 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[1798] _id=69e91c181724f0c9e2fa9264 ts=? == 69cdc98ad385e3b94310f7a9.jsonl[1908] _id=69e925df1724f0c9e2fab613 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.017s (p5 29.96s, p95 38.38s, n=494) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc98ad385e3b94310f7a9.jsonl[776] _id=69de9d7c7957a33870f3b227 ts=2026-04-14T20:03:08.2550000Z ~ 69cdc98ad385e3b94310f7a9.jsonl[62] _id=69de9d917957a33870f3b273 ts=2026-04-14T20:03:08.255Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `124ms: 69cdc98ad385e3b94310f7a9.jsonl[383] _id=69e67b291724f0c9e2f8d091 ts=2026-04-20T19:14:48.9500000Z ~ 69cdc98ad385e3b94310f7a9.jsonl[385] _id=69e67b291724f0c9e2f8d099 ts=2026-04-20T19:14:49.0740000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `911ms: 69cdc98ad385e3b94310f7a9.jsonl[512] _id=69e922b41724f0c9e2faa9dd ts=2026-04-22T19:34:11.9510000Z ~ 69cdc98ad385e3b94310f7a9.jsonl[1839] _id=69e922b51724f0c9e2faa9e1 ts=2026-04-22T19:34:12.8620000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc98ad385e3b94310f7a9.jsonl[1252] _id=69e141ba1724f0c9e2f712e0 ts=2026-04-16T20:08:26.1230000Z -> 69cdc98ad385e3b94310f7a9.jsonl[333] _id=69e675871724f0c9e2f8b863 ts=2026-04-20T18:50:47.1520000Z; 46h 42m: 69cdc98ad385e3b94310f7a9.jsonl[804] _id=69de9e927957a33870f3b619 ts=2026-04-14T20:07:46.1330000Z -> 69cdc98ad385e3b94310f7a9.jsonl[81] _id=69e132a71724f0c9e2f69c7c ts=2026-04-16T18:50:05.528Z; 46h 37m: 69cdc98ad385e3b94310f7a9.jsonl[1702] _id=69e688771724f0c9e2f9047d ts=2026-04-20T20:11:34.9690000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1712] _id=69e918241724f0c9e2fa8285 ts=2026-04-22T18:49:08.1380000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 325 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7a9.jsonl[490] _id=69e918bf1724f0c9e2fa846f ts=2026-04-22T18:51:42.5710000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1732] _id=69e918ce1724f0c9e2fa84ab ts=2026-04-22T18:51:42.571Z; 3ms: 69cdc98ad385e3b94310f7a9.jsonl[1654] _id=69e6875c1724f0c9e2f8ffdf ts=2026-04-20T20:06:51.7970000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1656] _id=69e6875c1724f0c9e2f8ffe1 ts=2026-04-20T20:06:51.8000000Z; 3ms: 69cdc98ad385e3b94310f7a9.jsonl[48] _id=69de9cff7957a33870f3b017 ts=2026-04-14T20:01:03.1110000Z -> 69cdc98ad385e3b94310f7a9.jsonl[49] _id=69de9cff7957a33870f3b019 ts=2026-04-14T20:01:03.1140000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 190h 48m 
  - Evidence: 190h 48m: 69cdc98ad385e3b94310f7a9.jsonl[62] _id=69de9d917957a33870f3b273 ts=2026-04-14T20:03:08.255Z -> 69cdc98ad385e3b94310f7a9.jsonl[489] _id=69e918bf1724f0c9e2fa846d ts=2026-04-22T18:51:42.5530000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7a9.jsonl[776] _id=69de9d7c7957a33870f3b227 ts=2026-04-14T20:03:08.2550000Z -> 69cdc98ad385e3b94310f7a9.jsonl[62] _id=69de9d917957a33870f3b273 ts=2026-04-14T20:03:08.255Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 46h 41m 
  - Evidence: 46h 41m: 69cdc98ad385e3b94310f7a9.jsonl[808] _id=69de9ecf7957a33870f3b6f9 ts=2026-04-14T20:08:46.7020000Z -> 69cdc98ad385e3b94310f7a9.jsonl[73] _id=69e132a71724f0c9e2f69c76 ts=2026-04-16T18:50:00.854Z; 46h 37m: 69cdc98ad385e3b94310f7a9.jsonl[1698] _id=69e6886a1724f0c9e2f90445 ts=2026-04-20T20:11:22.4130000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1710] _id=69e9180b1724f0c9e2fa8275 ts=2026-04-22T18:48:41.6950000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 69cdc98ad385e3b94310f7a9.jsonl[1193] _id=69e13f941724f0c9e2f70914 ts=2026-04-16T19:59:15.6430000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1472] _id=69e67c8b1724f0c9e2f8d71f ts=2026-04-20T19:20:43.2320000Z; 47h 36m: 69cdc98ad385e3b94310f7a9.jsonl[1476] _id=69e67ca51724f0c9e2f8d7bf ts=2026-04-20T19:21:08.9190000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1762] _id=69e91a361724f0c9e2fa8a69 ts=2026-04-22T18:57:57.5760000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc98ad385e3b94310f7a9.jsonl[1249] _id=69e141801724f0c9e2f71234 ts=2026-04-16T20:07:28.4040000Z -> 69cdc98ad385e3b94310f7a9.jsonl[351] _id=69e676451724f0c9e2f8baa1 ts=2026-04-20T18:53:56.8080000Z; 48h 23m: 69cdc98ad385e3b94310f7a9.jsonl[1290] _id=69e676bf1724f0c9e2f8bcab ts=2026-04-20T18:55:59.4380000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1195] _id=69e91f271724f0c9e2fa9eb7 ts=2026-04-22T19:19:03.0940000Z; 32m 55s: 69cdc98ad385e3b94310f7a9.jsonl[836] _id=69e132ab1724f0c9e2f69cd8 ts=2026-04-16T18:57:52.508Z -> 69cdc98ad385e3b94310f7a9.jsonl[198] _id=69e138e81724f0c9e2f6dbca ts=2026-04-16T19:30:47.9550000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 14m 
  - Evidence: 96h 14m: 69cdc98ad385e3b94310f7a9.jsonl[289] _id=69e13e481724f0c9e2f70470 ts=2026-04-16T19:53:43.8070000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1671] _id=69e687ad1724f0c9e2f90153 ts=2026-04-20T20:08:13.3870000Z; 17m 8s: 69cdc98ad385e3b94310f7a9.jsonl[199] _id=69e138f71724f0c9e2f6dbf8 ts=2026-04-16T19:31:02.8140000Z -> 69cdc98ad385e3b94310f7a9.jsonl[258] _id=69e13cfb1724f0c9e2f6ff21 ts=2026-04-16T19:48:11.4570000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 13m 
  - Evidence: 143h 13m: 69cdc98ad385e3b94310f7a9.jsonl[35] _id=69de9cb27957a33870f3af09 ts=2026-04-14T19:59:46.0450000Z -> 69cdc98ad385e3b94310f7a9.jsonl[377] _id=69e67ae71724f0c9e2f8cf73 ts=2026-04-20T19:13:42.7490000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 14m 
  - Evidence: 143h 14m: 69cdc98ad385e3b94310f7a9.jsonl[748] _id=69de9cae7957a33870f3aeff ts=2026-04-14T19:59:41.6160000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1410] _id=69e67aeb1724f0c9e2f8cf8b ts=2026-04-20T19:13:47.6410000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 44m 
  - Evidence: 94h 44m: 69cdc98ad385e3b94310f7a9.jsonl[1250] _id=69e141b51724f0c9e2f712bc ts=2026-04-16T20:08:21.0030000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1273] _id=69e6760d1724f0c9e2f8ba0d ts=2026-04-20T18:53:00.6660000Z; 46h 44m: 69cdc98ad385e3b94310f7a9.jsonl[64] _id=69de9e147957a33870f3b429 ts=2026-04-14T20:05:39.7370000Z -> 69cdc98ad385e3b94310f7a9.jsonl[80] _id=69e132a71724f0c9e2f69c7a ts=2026-04-16T18:50:03.844Z; 46h 37m: 69cdc98ad385e3b94310f7a9.jsonl[1701] _id=69e688771724f0c9e2f90475 ts=2026-04-20T20:11:34.8130000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1709] _id=69e9180e1724f0c9e2fa8279 ts=2026-04-22T18:48:45.5270000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 69cdc98ad385e3b94310f7a9.jsonl[723] _id=69de9c257957a33870f3acb1 ts=2026-04-14T19:57:25.0010000Z -> 69cdc98ad385e3b94310f7a9.jsonl[721] _id=69de9c257957a33870f3acb3 ts=2026-04-14T19:57:25.0050000Z; 5ms: 69cdc98ad385e3b94310f7a9.jsonl[521] _id=69e923a21724f0c9e2faadb7 ts=2026-04-22T19:38:10.3710000Z -> 69cdc98ad385e3b94310f7a9.jsonl[522] _id=69e923a31724f0c9e2faadb9 ts=2026-04-22T19:38:10.3760000Z; 5ms: 69cdc98ad385e3b94310f7a9.jsonl[568] _id=69e91d841724f0c9e2fa9845 ts=2026-04-22T19:12:03.9360000Z -> 69cdc98ad385e3b94310f7a9.jsonl[1] _id=69e91d841724f0c9e2fa9847 ts=2026-04-22T19:12:03.9410000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7a9.jsonl:69cdc98ad385e3b94310f7a9, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[1193] _id=69e13f941724f0c9e2f70914 ts=2026-04-16T19:59:15.6430000Z`; `69cdc98ad385e3b94310f7a9.jsonl[1476] _id=69e67ca51724f0c9e2f8d7bf ts=2026-04-20T19:21:08.9190000Z`; `69cdc98ad385e3b94310f7a9.jsonl[1760] _id=69e91a531724f0c9e2fa8af7 ts=2026-04-22T18:58:27.5370000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 15 record(s) match the trigger in 69cdc98ad385e3b94310f7a9.jsonl:69cdc98ad385e3b94310f7a9, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[199] _id=69e138f71724f0c9e2f6dbf8 ts=2026-04-16T19:31:02.8140000Z`; `69cdc98ad385e3b94310f7a9.jsonl[258] _id=69e13cfb1724f0c9e2f6ff21 ts=2026-04-16T19:48:11.4570000Z`; `69cdc98ad385e3b94310f7a9.jsonl[1126] _id=69e13cff1724f0c9e2f6ff36 ts=2026-04-16T19:48:14.6560000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[353] _id=69e6779b1724f0c9e2f8c0b7 ts=2026-04-20T18:59:38.7330000Z`; `69cdc98ad385e3b94310f7a9.jsonl[364] _id=69e678531724f0c9e2f8c3bd ts=2026-04-20T19:02:42.6980000Z`; `69cdc98ad385e3b94310f7a9.jsonl[552] _id=69e925a81724f0c9e2fab575 ts=2026-04-22T19:46:47.7220000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[385] _id=69e67b291724f0c9e2f8d099 ts=2026-04-20T19:14:49.0740000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[819] _id=69e91e7e1724f0c9e2fa9c85 ts=2026-04-22T19:16:13.9640000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `69cdc98ad385e3b94310f7a9.jsonl[492] _id=69e918c01724f0c9e2fa8471 ts=?`; `69cdc98ad385e3b94310f7a9.jsonl[1798] _id=69e91c181724f0c9e2fa9264 ts=?`; `69cdc98ad385e3b94310f7a9.jsonl[1908] _id=69e925df1724f0c9e2fab613 ts=?`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 176 unmatched 'DialogueStartEvent' (totals: 286 start, 113 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 34 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.43s, min -846.90s, max -0.24s over 1955 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7a9\coverage.yaml

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
  - Observed: 40 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
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

### `DialogueEvent` — 1298 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (500); Unit 3 Dev (286); Unit 1 Dev (178); Unit 3 Dungeon Dev (132); Unit 4 Dev - Dungeon (108); Unit 4 Dev (94)
- **eventKey:** present on 899 of 1298 records
- **Intervals:** median 2.50s (p5 0.01s / p95 48.02s, n=1297)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x899; [conversationId, dialogueEventType] x399
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1298/1298 records)
    numeric range 10 .. 107 (35 unique)
data.dialogueEventType  (string, 1298/1298 records)
    "DialogueNodeEvent"  x899
    "DialogueStartEvent"  x286
    "DialogueFinishEvent"  x113
data.nodeId  (number, 899/1298 records)
    numeric range 0 .. 286 (198 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 502 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (151); Unit 3 Dungeon Dev (82); Unit 3 Dev (78); Unit 4 Dev - Dungeon (78); Unit 4 Dev (59); Unit 1 Dev (54)
- **Intervals:** median 30.02s (p5 29.96s / p95 38.38s, n=494)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 502/502 records)
data.position.x  (number, 502/502 records)
    numeric range -666.491 .. 1438.92 (321 unique)
data.position.y  (number, 502/502 records)
    numeric range -115.127 .. 158.768 (219 unique)
data.position.z  (number, 502/502 records)
    numeric range -1137.76 .. 1864.27 (320 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 58 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 4 Dev - Dungeon (11); Unit 3 Dev (10); Unit 4 Dev (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 58 of 58 records
- **Intervals:** median 181.39s (p5 0.01s / p95 35075.50s, n=57)
- **`data` key-set variants:** [questEventType, questID, questName] x34; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 58/58 records)
    "questActiveEvent"  x34
    "questFinishEvent"  x24
data.questID  (string, 58/58 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 58/58 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/58 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 40 records

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 4 Dev - Dungeon (6); Unit 3 Dev (4)
- **Intervals:** median 10.10s (p5 0.65s / p95 19196.27s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "MapCloseEvent"  x21
    "MapOpenEvent"  x19
data.featureUsed  (string, 40/40 records)
    "Map"  x40
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 15 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 3 Dev (2)
- **Intervals:** median 10.08s (p5 0.82s / p95 121932.97s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "dragStart"  x8
    "dragEnd"  x7
data.featureUsed  (string, 15/15 records)
    "waypoint"  x15
data.location  (object, 15/15 records)
data.location.x  (number, 15/15 records)
    8 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 15/15 records)
    8 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 15/15 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 15 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (9); Unit 1 Dev (6)
- **Intervals:** median 4.96s (p5 1.42s / p95 180514.77s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationNodeAdd"  x12
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 15/15 records)
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Argumentation Tutorial"  x3
    "Unit 1 - Freshwater"  x3
data.nodeName  (string, 15/15 records)
    "A"  x6
    "B"  x3
    "I"  x3
    "1"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 15.36s (p5 1.25s / p95 128.22s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Sand"  x6
    "Gravel"  x3
    "Clay"  x2
data.floor  (string, 11/11 records)
    "5"  x6
    "3"  x4
    "4"  x1
data.machine  (string, 11/11 records)
    "1"  x7
    "2"  x4
data.row  (string, 11/11 records)
    "TopRow"  x10
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 34.59s (p5 5.42s / p95 386744.08s, n=6)
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
- **Intervals:** median 54.38s (p5 26.54s / p95 308911.80s, n=5)
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

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 343457.15s (p5 34345.71s / p95 652568.58s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x2
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Uncaught ReferenceError: onResize is not defined"  x2
    "Cannot close a closed AudioContext."  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 1 empty-string)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x2
    ""  x1
data.type  (string, 3/3 records)
    "runtime_error"  x2
    "unhandled_rejection"  x1
data.unitId  (string, 3/3 records)
    "unit4"  x2
    "unit3"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
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
- `TopographicMapEvent` data.actionType: "dragStart" (8x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*