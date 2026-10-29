# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f721

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f721
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f721.jsonl
- **Records:** 1770 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f721
- **Time span:** 2026-04-13T18:00:40.341000+00:00 .. 2026-04-23T18:41:05.806000+00:00 (240h 40m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f721\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **9 event types**, 1770 records, 6 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 42 INFO, 2 NOT_TESTED, 29 PASS.
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
| DialogueEvent | 981 | 55.42 | 1 | 6 | 653 | 2026-04-13T18:00:58.437000+00:00 | 2026-04-23T18:39:41.635000+00:00 | 240h 38m |
| PlayerPositionEvent | 617 | 34.86 | 1 | 6 | 0 | 2026-04-13T18:00:40.341000+00:00 | 2026-04-23T18:41:05.806000+00:00 | 240h 40m |
| Topographic Map Event | 52 | 2.94 | 1 | 2 | 0 | 2026-04-15T18:06:11.683000+00:00 | 2026-04-21T18:04:10.855000+00:00 | 143h 57m |
| TopographicMapEvent | 50 | 2.82 | 1 | 2 | 0 | 2026-04-15T18:06:20.924000+00:00 | 2026-04-21T17:48:44.245000+00:00 | 143h 42m |
| questEvent | 40 | 2.26 | 1 | 6 | 40 | 2026-04-13T18:00:58.418000+00:00 | 2026-04-23T18:39:23.642000+00:00 | 240h 38m |
| argumentationNodeEvent | 16 | 0.9 | 1 | 2 | 0 | 2026-04-13T18:22:25.443000+00:00 | 2026-04-21T18:09:48.222000+00:00 | 191h 47m |
| argumentationEvent | 7 | 0.4 | 1 | 2 | 0 | 2026-04-13T18:22:19.753000+00:00 | 2026-04-21T18:09:49.983000+00:00 | 191h 47m |
| Soil Key Puzzle | 6 | 0.34 | 1 | 3 | 0 | 2026-04-17T17:45:33.632000+00:00 | 2026-04-23T18:28:30.158000+00:00 | 144h 42m |
| EndOfUnit | 1 | 0.06 | 1 | 1 | 0 | 2026-04-13T18:28:40.056000+00:00 | 2026-04-13T18:28:40.056000+00:00 | 0.0s |

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
  - Observed: 30.019s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 409.564s median 
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
  - Observed: 7.308s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.763s median 
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
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 52 records this build 
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
  - Observed: 16 records 
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
  - Observed: 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 25; 36; 40; 41; 43; 44; 45; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'DialogueNodeEvent:20:111' vs expected 'DialogueNodeEvent:20:33' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f721.jsonl[529] _id=69dfd5387957a33870f43683 ts=2026-04-15T18:13:11.9140000Z`; `69cdc907d385e3b94310f721.jsonl[1102] _id=69e7bd6f1724f0c9e2f970e9 ts=2026-04-21T18:09:49.9050000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 52 records, TopographicMapEvent: 50 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 980 | 0.002 | 3.79 | 884.003 | 72.016 | 339674.047 | 0.07 | 275 | 7 |
| PlayerPositionEvent | 611 | 7.311 | 30.019 | 1417.493 | 35.85 | 339566.787 | 0.04 | 0 | 4 |
| Topographic Map Event | 51 | 3.247 | 25.416 | 10162.337 | 3315.126 | 341158.784 | 0.01 | 0 | 5 |
| TopographicMapEvent | 49 | 0.268 | 7.308 | 10558.027 | 450.101 | 348295.29 | 0.01 | 0 | 2 |
| questEvent | 39 | 0.003 | 256.155 | 22212.954 | 170242.803 | 340065.237 | 0.0 | 5 | 9 |
| argumentationNodeEvent | 15 | 1.663 | 5.763 | 46029.519 | 207130.138 | 690187.485 | 0.0 | 0 | 1 |
| argumentationEvent | 6 | 0.107 | 58.604 | 115075.038 | 517659.338 | 690167.312 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 5 | 52.206 | 409.564 | 104195.305 | 312340.719 | 347096.742 | 0.0 | 0 | 2 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.019s (p5 29.96s, p95 35.85s, n=611) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `107ms: 69cdc907d385e3b94310f721.jsonl[1598] _id=69e7bd6f1724f0c9e2f970e7 ts=2026-04-21T18:09:49.8760000Z ~ 69cdc907d385e3b94310f721.jsonl[1103] _id=69e7bd6f1724f0c9e2f970ef ts=2026-04-21T18:09:49.9830000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 21m 
  - Evidence: 94h 21m: 69cdc907d385e3b94310f721.jsonl[908] _id=69e27e4b1724f0c9e2f78bee ts=2026-04-17T18:39:06.7400000Z -> 69cdc907d385e3b94310f721.jsonl[915] _id=69e7ad261724f0c9e2f91bd3 ts=2026-04-21T17:00:20.7870000Z; 47h 22m: 69cdc907d385e3b94310f721.jsonl[1676] _id=69e7c42a1724f0c9e2f9a4db ts=2026-04-21T18:38:33.0450000Z -> 69cdc907d385e3b94310f721.jsonl[1273] _id=69ea5e561724f0c9e2fb052f ts=2026-04-23T18:00:53.1300000Z; 47h 7m: 69cdc907d385e3b94310f721.jsonl[102] _id=69dd388c7957a33870f29096 ts=2026-04-13T18:40:11.9740000Z -> 69cdc907d385e3b94310f721.jsonl[345] _id=69dfcf277957a33870f40cd9 ts=2026-04-15T17:47:18.4510000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 275 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f721.jsonl[1275] _id=69ea5e621724f0c9e2fb056f ts=2026-04-23T18:01:05.3310000Z -> 69cdc907d385e3b94310f721.jsonl[1684] _id=69ea5e621724f0c9e2fb0571 ts=2026-04-23T18:01:05.3330000Z; 3ms: 69cdc907d385e3b94310f721.jsonl[1184] _id=69e7bfaf1724f0c9e2f98183 ts=2026-04-21T18:19:25.9390000Z -> 69cdc907d385e3b94310f721.jsonl[1185] _id=69e7bfaf1724f0c9e2f98185 ts=2026-04-21T18:19:25.9420000Z; 3ms: 69cdc907d385e3b94310f721.jsonl[238] _id=69dd352f7957a33870f27956 ts=2026-04-13T18:25:50.8870000Z -> 69cdc907d385e3b94310f721.jsonl[239] _id=69dd352f7957a33870f27958 ts=2026-04-13T18:25:50.8900000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 19m 
  - Evidence: 94h 19m: 69cdc907d385e3b94310f721.jsonl[910] _id=69e27e841724f0c9e2f78cf4 ts=2026-04-17T18:40:04.2260000Z -> 69cdc907d385e3b94310f721.jsonl[912] _id=69e7acf41724f0c9e2f91a8d ts=2026-04-21T16:59:31.0130000Z; 47h 20m: 69cdc907d385e3b94310f721.jsonl[1270] _id=69e7c47b1724f0c9e2f9a6f5 ts=2026-04-21T18:39:54.4930000Z -> 69cdc907d385e3b94310f721.jsonl[1271] _id=69ea5e541724f0c9e2fb0527 ts=2026-04-23T18:00:51.5760000Z; 47h 6m: 69cdc907d385e3b94310f721.jsonl[342] _id=69dd38b87957a33870f29186 ts=2026-04-13T18:40:56.1830000Z -> 69cdc907d385e3b94310f721.jsonl[343] _id=69dfcf237957a33870f40ccd ts=2026-04-15T17:47:14.3610000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 24m 
  - Evidence: 96h 24m: 69cdc907d385e3b94310f721.jsonl[771] _id=69e273581724f0c9e2f75350 ts=2026-04-17T17:52:23.1960000Z -> 69cdc907d385e3b94310f721.jsonl[1622] _id=69e7bf311724f0c9e2f97d81 ts=2026-04-21T18:17:19.9380000Z; 48h 8m: 69cdc907d385e3b94310f721.jsonl[1178] _id=69e7bf961724f0c9e2f980c3 ts=2026-04-21T18:19:01.3270000Z -> 69cdc907d385e3b94310f721.jsonl[1352] _id=69ea649a1724f0c9e2fb3693 ts=2026-04-23T18:27:37.9520000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc907d385e3b94310f721.jsonl[836] _id=69e2798c1724f0c9e2f77690 ts=2026-04-17T18:18:52.8850000Z -> 69cdc907d385e3b94310f721.jsonl[947] _id=69e7ae351724f0c9e2f923e3 ts=2026-04-21T17:04:51.6690000Z; 46h 18m: 69cdc907d385e3b94310f721.jsonl[645] _id=69dfdacc7957a33870f45fc9 ts=2026-04-15T18:37:00.2310000Z -> 69cdc907d385e3b94310f721.jsonl[671] _id=69e2661e1724f0c9e2f721e2 ts=2026-04-17T16:55:58.6950000Z; 1h 13m: 69cdc907d385e3b94310f721.jsonl[692] _id=69e267f51724f0c9e2f7303c ts=2026-04-17T17:03:49.4290000Z -> 69cdc907d385e3b94310f721.jsonl[828] _id=69e279441724f0c9e2f774be ts=2026-04-17T18:17:40.3400000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 44m 
  - Evidence: 96h 44m: 69cdc907d385e3b94310f721.jsonl[688] _id=69e267f11724f0c9e2f7300a ts=2026-04-17T17:03:45.6090000Z -> 69cdc907d385e3b94310f721.jsonl[1561] _id=69e7b87a1724f0c9e2f94ed9 ts=2026-04-21T17:48:40.8990000Z; 46h 19m: 69cdc907d385e3b94310f721.jsonl[656] _id=69dfdac97957a33870f45fb7 ts=2026-04-15T18:36:57.4770000Z -> 69cdc907d385e3b94310f721.jsonl[1459] _id=69e266241724f0c9e2f7221c ts=2026-04-17T16:56:04.8230000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 69cdc907d385e3b94310f721.jsonl[216] _id=69dd34ef7957a33870f2778a ts=2026-04-13T18:24:47.1480000Z -> 69cdc907d385e3b94310f721.jsonl[1593] _id=69e7bce71724f0c9e2f96dad ts=2026-04-21T18:07:34.4600000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 43m 
  - Evidence: 191h 43m: 69cdc907d385e3b94310f721.jsonl[214] _id=69dd34eb7957a33870f2776a ts=2026-04-13T18:24:42.3780000Z -> 69cdc907d385e3b94310f721.jsonl[1594] _id=69e7bcf71724f0c9e2f96e11 ts=2026-04-21T18:07:49.8630000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 27m 
  - Evidence: 94h 27m: 69cdc907d385e3b94310f721.jsonl[832] _id=69e27c941724f0c9e2f78170 ts=2026-04-17T18:31:48.4750000Z -> 69cdc907d385e3b94310f721.jsonl[913] _id=69e7acf71724f0c9e2f91a99 ts=2026-04-21T16:59:33.7120000Z; 47h 28m: 69cdc907d385e3b94310f721.jsonl[1239] _id=69e7c2b31724f0c9e2f999b7 ts=2026-04-21T18:32:17.8870000Z -> 69cdc907d385e3b94310f721.jsonl[1682] _id=69ea5e551724f0c9e2fb052b ts=2026-04-23T18:00:52.8750000Z; 47h 16m: 69cdc907d385e3b94310f721.jsonl[283] _id=69dd366d7957a33870f2820c ts=2026-04-13T18:31:08.8000000Z -> 69cdc907d385e3b94310f721.jsonl[344] _id=69dfcf257957a33870f40cd5 ts=2026-04-15T17:47:16.9160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.003s..0.008s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f721.jsonl[176] _id=69dd34057957a33870f271d4 ts=2026-04-13T18:20:52.0680000Z -> 69cdc907d385e3b94310f721.jsonl[173] _id=69dd34057957a33870f271d6 ts=2026-04-13T18:20:52.0710000Z; 7ms: 69cdc907d385e3b94310f721.jsonl[81] _id=69dd31ae7957a33870f26114 ts=2026-04-13T18:10:53.9010000Z -> 69cdc907d385e3b94310f721.jsonl[88] _id=69dd31ae7957a33870f26118 ts=2026-04-13T18:10:53.9080000Z; 8ms: 69cdc907d385e3b94310f721.jsonl[1392] _id=69ea66511724f0c9e2fb44af ts=2026-04-23T18:34:57.2260000Z -> 69cdc907d385e3b94310f721.jsonl[1393] _id=69ea66511724f0c9e2fb44b1 ts=2026-04-23T18:34:57.2340000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 2 record(s) match the trigger in 69cdc907d385e3b94310f721.jsonl:69cdc907d385e3b94310f721, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f721.jsonl[1178] _id=69e7bf961724f0c9e2f980c3 ts=2026-04-21T18:19:01.3270000Z`; `69cdc907d385e3b94310f721.jsonl[1355] _id=69ea64ce1724f0c9e2fb3851 ts=2026-04-23T18:28:30.1580000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 50 record(s) match the trigger in 69cdc907d385e3b94310f721.jsonl:69cdc907d385e3b94310f721, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f721.jsonl[468] _id=69dfd39d7957a33870f42d37 ts=2026-04-15T18:06:20.9240000Z`; `69cdc907d385e3b94310f721.jsonl[469] _id=69dfd39d7957a33870f42d3f ts=2026-04-15T18:06:21.3720000Z`; `69cdc907d385e3b94310f721.jsonl[473] _id=69dfd3a77957a33870f42d83 ts=2026-04-15T18:06:30.4540000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f721.jsonl[866] _id=69e27aef1724f0c9e2f77db6 ts=2026-04-17T18:24:46.9900000Z`; `69cdc907d385e3b94310f721.jsonl[834] _id=69e27c951724f0c9e2f78176 ts=2026-04-17T18:31:48.5540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f721.jsonl[1103] _id=69e7bd6f1724f0c9e2f970ef ts=2026-04-21T18:09:49.9830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f721.jsonl[771] _id=69e273581724f0c9e2f75350 ts=2026-04-17T17:52:23.1960000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 146 unmatched 'DialogueStartEvent' (totals: 236 start, 92 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 4 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 27 start, 13 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.71s, min -7.19s, max -0.02s over 1770 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f721\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=partial, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=partial, Unit4=partial, Unit5=skipped 
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
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 52 records 
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

### `DialogueEvent` — 981 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (272); Unit 2 Prod (Refactor) (270); Unit 1 Dev (190); Unit 3 Dungeon Dev (173); Unit 4 Dev - Dungeon (51); Unit 4 Dev (25)
- **eventKey:** present on 653 of 981 records
- **Intervals:** median 3.79s (p5 0.01s / p95 72.02s, n=980)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x653; [conversationId, dialogueEventType] x328
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 981/981 records)
    numeric range 10 .. 102 (29 unique)
data.dialogueEventType  (string, 981/981 records)
    "DialogueNodeEvent"  x653
    "DialogueStartEvent"  x236
    "DialogueFinishEvent"  x92
data.nodeId  (number, 653/981 records)
    numeric range 0 .. 289 (157 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 617 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (226); Unit 3 Dev (214); Unit 3 Dungeon Dev (82); Unit 1 Dev (56); Unit 4 Dev - Dungeon (21); Unit 4 Dev (18)
- **Intervals:** median 30.02s (p5 29.96s / p95 35.85s, n=611)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 617/617 records)
data.position.x  (number, 617/617 records)
    numeric range -704.879 .. 1539.35 (269 unique)
data.position.y  (number, 617/617 records)
    numeric range -113.231 .. 157.922 (205 unique)
data.position.z  (number, 617/617 records)
    numeric range -1114.64 .. 2028.56 (269 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 52 records

- **Scenes:** Unit 2 Prod (Refactor) (38); Unit 3 Dev (14)
- **Intervals:** median 25.42s (p5 3.93s / p95 3315.13s, n=51)
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "MapCloseEvent"  x26
    "MapOpenEvent"  x26
data.featureUsed  (string, 52/52 records)
    "Map"  x52
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 50 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (48); Unit 3 Dev (2)
- **Intervals:** median 7.31s (p5 0.53s / p95 450.10s, n=49)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "dragEnd"  x25
    "dragStart"  x25
data.featureUsed  (string, 50/50 records)
    "waypoint"  x50
data.location  (object, 50/50 records)
data.location.x  (number, 50/50 records)
    numeric range -770.79 .. 287.983 (26 unique)
data.location.y  (number, 50/50 records)
    numeric range -307.4 .. 202.852 (26 unique)
data.location.z  (number, 50/50 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 40 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (12); Unit 2 Prod (Refactor) (11); Unit 3 Dev (8); Unit 4 Dev - Dungeon (5); Unit 3 Dungeon Dev (3); Unit 4 Dev (1)
- **eventKey:** present on 40 of 40 records
- **Intervals:** median 256.15s (p5 0.01s / p95 170242.80s, n=39)
- **`data` key-set variants:** [questEventType, questID, questName] x27; [questEventType, questID, questName, questSuccessOrFailure] x13
- **Fields under `data`:**

```text
data.questEventType  (string, 40/40 records)
    "questActiveEvent"  x27
    "questFinishEvent"  x13
data.questID  (string, 40/40 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 40/40 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 13/40 records)
    "Succeeded"  x13
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 16 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (9); Unit 1 Dev (7)
- **Intervals:** median 5.76s (p5 2.00s / p95 207130.14s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationNodeAdd"  x12
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 16/16 records)
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 16/16 records)
    "3"  x4
    "I"  x3
    "2"  x2
    "A"  x2
    "II"  x2
    "1"  x1
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 58.60s (p5 7.63s / p95 517659.34s, n=6)
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
- **Intervals:** median 409.56s (p5 62.04s / p95 312340.72s, n=5)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/6 records)
    "Started"  x4
    "Finished"  x2
data.Unit  (string, 6/6 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `TopographicMapEvent` data.actionType: "dragStart" (25x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*