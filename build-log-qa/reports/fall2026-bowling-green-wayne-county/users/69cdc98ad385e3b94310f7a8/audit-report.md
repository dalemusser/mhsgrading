# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7a8

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc98ad385e3b94310f7a8
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc98ad385e3b94310f7a8.jsonl
- **Records:** 2331 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc98ad385e3b94310f7a8
- **Time span:** 2026-04-14T19:25:45.898000+00:00 .. 2026-04-22T20:04:20.519000+00:00 (192h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7a8\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2331 records, 7 scenes.
- Findings: **0 FAIL**, **41 WARNING**, 54 INFO, 2 NOT_TESTED, 38 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1566 | 67.18 | 1 | 7 | 1084 | 2026-04-14T19:26:04.495000+00:00 | 2026-04-22T20:04:11.211000+00:00 | 192h 38m |
| PlayerPositionEvent | 536 | 22.99 | 1 | 7 | 0 | 2026-04-14T19:25:45.898000+00:00 | 2026-04-22T20:04:20.519000+00:00 | 192h 38m |
| Topographic Map Event | 68 | 2.92 | 1 | 2 | 0 | 2026-04-14T20:07:10.948000+00:00 | 2026-04-22T19:14:09.345000+00:00 | 191h 6m |
| questEvent | 53 | 2.27 | 1 | 7 | 53 | 2026-04-14T19:26:04.471000+00:00 | 2026-04-22T20:01:19.561000+00:00 | 192h 35m |
| argumentationNodeEvent | 35 | 1.5 | 1 | 3 | 0 | 2026-04-14T19:49:20.225000+00:00 | 2026-04-20T19:29:43.710000+00:00 | 143h 40m |
| argumentationToolEvent | 34 | 1.46 | 1 | 2 | 0 | 2026-04-16T20:05:43.723000+00:00 | 2026-04-20T19:29:27.291000+00:00 | 95h 23m |
| soilMachine | 19 | 0.82 | 1 | 1 | 0 | 2026-04-22T19:49:53.509000+00:00 | 2026-04-22T19:53:19.722000+00:00 | 3m 26s |
| argumentationEvent | 10 | 0.43 | 1 | 3 | 0 | 2026-04-14T19:49:06.010000+00:00 | 2026-04-20T19:29:50.071000+00:00 | 143h 40m |
| Soil Key Puzzle | 6 | 0.26 | 1 | 3 | 0 | 2026-04-16T19:30:46.485000+00:00 | 2026-04-22T19:26:56.861000+00:00 | 143h 56m |
| EndOfUnit | 3 | 0.13 | 1 | 3 | 0 | 2026-04-14T19:55:14.271000+00:00 | 2026-04-22T19:17:48.008000+00:00 | 191h 22m |
| crash | 1 | 0.04 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 344476.868s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.023s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 56.577s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 83 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 9.603s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.245s median 
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
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.798s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 68 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 35 records 
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
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 34 records 
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
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[573] _id=69de9ab17957a33870f3a57b ts=2026-04-14T19:51:12.9390000Z`; `69cdc98ad385e3b94310f7a8.jsonl[109] _id=69e135721724f0c9e2f6ada4 ts=2026-04-16T19:16:01.2110000Z`; `69cdc98ad385e3b94310f7a8.jsonl[1321] _id=69e677b51724f0c9e2f8c123 ts=2026-04-20T19:00:03.8540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1565 | 0.0 | 2.457 | 443.123 | 49.843 | 340855.291 | 0.14 | 393 | 4 |
| PlayerPositionEvent | 527 | 29.738 | 30.023 | 1315.408 | 34.33 | 340818.442 | 0.05 | 0 | 3 |
| Topographic Map Event | 67 | 1.057 | 11.061 | 10268.931 | 1126.327 | 341469.759 | 0.01 | 0 | 5 |
| questEvent | 52 | 0.004 | 194.133 | 13332.983 | 76672.476 | 342312.572 | 0.0 | 7 | 10 |
| argumentationNodeEvent | 34 | 0.918 | 9.603 | 15212.455 | 61869.503 | 341437.581 | 0.0 | 0 | 3 |
| argumentationToolEvent | 33 | 0.009 | 1.245 | 10406.775 | 753.928 | 341464.685 | 0.01 | 4 | 2 |
| soilMachine | 18 | 0.077 | 1.798 | 11.456 | 40.277 | 104.591 | 5.24 | 0 | 0 |
| argumentationEvent | 9 | 0.127 | 82.507 | 57471.562 | 274424.945 | 341627.914 | 0.0 | 0 | 3 |
| Soil Key Puzzle | 5 | 20.159 | 56.577 | 103634.075 | 311071.145 | 345772.614 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 173659.915 | 344476.868 | 344476.868 | 498212.127 | 515293.822 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.023s (p5 29.95s, p95 34.33s, n=527) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `127ms: 69cdc98ad385e3b94310f7a8.jsonl[275] _id=69e67eae1724f0c9e2f8e1b1 ts=2026-04-20T19:29:49.9440000Z ~ 69cdc98ad385e3b94310f7a8.jsonl[276] _id=69e67eae1724f0c9e2f8e1b9 ts=2026-04-20T19:29:50.0710000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `723ms: 69cdc98ad385e3b94310f7a8.jsonl[270] _id=69e67e941724f0c9e2f8e137 ts=2026-04-20T19:29:24.3140000Z ~ 69cdc98ad385e3b94310f7a8.jsonl[272] _id=69e67e951724f0c9e2f8e13d ts=2026-04-20T19:29:25.0370000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `887ms: 69cdc98ad385e3b94310f7a8.jsonl[2226] _id=69e926e31724f0c9e2fab91b ts=2026-04-22T19:52:03.0930000Z ~ 69cdc98ad385e3b94310f7a8.jsonl[2227] _id=69e926e41724f0c9e2fab91d ts=2026-04-22T19:52:03.9800000Z`; `894ms: 69cdc98ad385e3b94310f7a8.jsonl[2227] _id=69e926e41724f0c9e2fab91d ts=2026-04-22T19:52:03.9800000Z ~ 69cdc98ad385e3b94310f7a8.jsonl[2224] _id=69e926e51724f0c9e2fab925 ts=2026-04-22T19:52:04.8740000Z`; `77ms: 69cdc98ad385e3b94310f7a8.jsonl[2224] _id=69e926e51724f0c9e2fab925 ts=2026-04-22T19:52:04.8740000Z ~ 69cdc98ad385e3b94310f7a8.jsonl[2228] _id=69e926e51724f0c9e2fab929 ts=2026-04-22T19:52:04.9510000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc98ad385e3b94310f7a8.jsonl[179] _id=69e141951724f0c9e2f7126a ts=2026-04-16T20:07:48.8290000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1326] _id=69e6750c1724f0c9e2f8b6ff ts=2026-04-20T18:48:44.1200000Z; 46h 49m: 69cdc98ad385e3b94310f7a8.jsonl[656] _id=69de9d367957a33870f3b0e5 ts=2026-04-14T20:01:58.3260000Z -> 69cdc98ad385e3b94310f7a8.jsonl[739] _id=69e12f9d1724f0c9e2f68f7a ts=2026-04-16T18:51:08.9170000Z; 46h 40m: 69cdc98ad385e3b94310f7a8.jsonl[1925] _id=69e6881d1724f0c9e2f90335 ts=2026-04-20T20:10:04.6100000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1945] _id=69e918671724f0c9e2fa82ff ts=2026-04-22T18:50:14.3260000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 393 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc98ad385e3b94310f7a8.jsonl[237] _id=69e678801724f0c9e2f8c49d ts=2026-04-20T19:03:28.1190000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1474] _id=69e6788f1724f0c9e2f8c4cd ts=2026-04-20T19:03:28.119Z; 0ms: 69cdc98ad385e3b94310f7a8.jsonl[727] _id=69e91edc1724f0c9e2fa9db5 ts=2026-04-22T19:17:48.0430000Z -> 69cdc98ad385e3b94310f7a8.jsonl[792] _id=69e91eec1724f0c9e2fa9df9 ts=2026-04-22T19:17:48.043Z; 3ms: 69cdc98ad385e3b94310f7a8.jsonl[1740] _id=69e67fa61724f0c9e2f8e65b ts=2026-04-20T19:33:57.1220000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1737] _id=69e67fa61724f0c9e2f8e65f ts=2026-04-20T19:33:57.1250000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 8m 
  - Evidence: 143h 8m: 69cdc98ad385e3b94310f7a8.jsonl[619] _id=69de9ba27957a33870f3a9ab ts=2026-04-14T19:55:14.2710000Z -> 69cdc98ad385e3b94310f7a8.jsonl[238] _id=69e678801724f0c9e2f8c499 ts=2026-04-20T19:03:28.0930000Z; 48h 14m: 69cdc98ad385e3b94310f7a8.jsonl[238] _id=69e678801724f0c9e2f8c499 ts=2026-04-20T19:03:28.0930000Z -> 69cdc98ad385e3b94310f7a8.jsonl[737] _id=69e91edc1724f0c9e2fa9db3 ts=2026-04-22T19:17:48.0080000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 40m 
  - Evidence: 94h 40m: 69cdc98ad385e3b94310f7a8.jsonl[1305] _id=69e141a11724f0c9e2f7128a ts=2026-04-16T20:08:00.2140000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1331] _id=69e674f31724f0c9e2f8b6f5 ts=2026-04-20T18:48:18.6560000Z; 46h 41m: 69cdc98ad385e3b94310f7a8.jsonl[673] _id=69de9ee67957a33870f3b72b ts=2026-04-14T20:09:10.5840000Z -> 69cdc98ad385e3b94310f7a8.jsonl[741] _id=69e12f991724f0c9e2f68f68 ts=2026-04-16T18:51:04.2730000Z; 46h 39m: 69cdc98ad385e3b94310f7a8.jsonl[1929] _id=69e688361724f0c9e2f90371 ts=2026-04-20T20:10:30.2460000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1942] _id=69e918651724f0c9e2fa82e5 ts=2026-04-22T18:50:12.3550000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 69cdc98ad385e3b94310f7a8.jsonl[970] _id=69e1391f1724f0c9e2f6dcb2 ts=2026-04-16T19:31:42.2440000Z -> 69cdc98ad385e3b94310f7a8.jsonl[299] _id=69e67fcb1724f0c9e2f8e729 ts=2026-04-20T19:34:34.8580000Z; 47h 51m: 69cdc98ad385e3b94310f7a8.jsonl[1750] _id=69e680031724f0c9e2f8e815 ts=2026-04-20T19:35:31.4350000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1852] _id=69e920ed1724f0c9e2faa299 ts=2026-04-22T19:26:36.7020000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc98ad385e3b94310f7a8.jsonl[1240] _id=69e1405a1724f0c9e2f70c96 ts=2026-04-16T20:02:33.8140000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1376] _id=69e676381724f0c9e2f8ba7f ts=2026-04-20T18:53:43.5730000Z; 47h 57m: 69cdc98ad385e3b94310f7a8.jsonl[250] _id=69e67a131724f0c9e2f8cc41 ts=2026-04-20T19:10:10.9710000Z -> 69cdc98ad385e3b94310f7a8.jsonl[2076] _id=69e91c961724f0c9e2fa94b3 ts=2026-04-22T19:08:06.4580000Z; 47h 6m: 69cdc98ad385e3b94310f7a8.jsonl[665] _id=69de9e7c7957a33870f3b5c3 ts=2026-04-14T20:07:24.0470000Z -> 69cdc98ad385e3b94310f7a8.jsonl[873] _id=69e134dd1724f0c9e2f6a9d0 ts=2026-04-16T19:13:31.9330000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 53m 
  - Evidence: 94h 53m: 69cdc98ad385e3b94310f7a8.jsonl[1266] _id=69e140e61724f0c9e2f70e4e ts=2026-04-16T20:04:53.4000000Z -> 69cdc98ad385e3b94310f7a8.jsonl[221] _id=69e677611724f0c9e2f8bf97 ts=2026-04-20T18:58:41.3140000Z; 48h 13m: 69cdc98ad385e3b94310f7a8.jsonl[572] _id=69de9ab17957a33870f3a577 ts=2026-04-14T19:51:12.9080000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1266] _id=69e140e61724f0c9e2f70e4e ts=2026-04-16T20:04:53.4000000Z; 27m 54s: 69cdc98ad385e3b94310f7a8.jsonl[1319] _id=69e677b41724f0c9e2f8c11a ts=2026-04-20T19:00:03.8210000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1662] _id=69e67e3f1724f0c9e2f8df65 ts=2026-04-20T19:27:58.6600000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 50m 
  - Evidence: 94h 50m: 69cdc98ad385e3b94310f7a8.jsonl[1302] _id=69e141a71724f0c9e2f712a2 ts=2026-04-16T20:08:06.5510000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1424] _id=69e677641724f0c9e2f8bfab ts=2026-04-20T18:58:44.1320000Z; 48h 13m: 69cdc98ad385e3b94310f7a8.jsonl[559] _id=69de9aad7957a33870f3a563 ts=2026-04-14T19:51:08.6820000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1267] _id=69e140ea1724f0c9e2f70e66 ts=2026-04-16T20:04:57.6330000Z; 28m 11s: 69cdc98ad385e3b94310f7a8.jsonl[228] _id=69e677b21724f0c9e2f8c113 ts=2026-04-20T19:00:01.9860000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1664] _id=69e67e4d1724f0c9e2f8df9e ts=2026-04-20T19:28:13.3240000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc98ad385e3b94310f7a8.jsonl[1303] _id=69e141901724f0c9e2f7125c ts=2026-04-16T20:07:43.7770000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1426] _id=69e677691724f0c9e2f8bfbf ts=2026-04-20T18:58:48.4620000Z; 29m 15s: 69cdc98ad385e3b94310f7a8.jsonl[1400] _id=69e677921724f0c9e2f8c096 ts=2026-04-20T18:59:29.6450000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1667] _id=69e67e6d1724f0c9e2f8e045 ts=2026-04-20T19:28:45.4110000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.009s..0.020s shown 
  - Evidence: 9ms: 69cdc98ad385e3b94310f7a8.jsonl[1668] _id=69e67e731724f0c9e2f8e06b ts=2026-04-20T19:28:51.2940000Z -> 69cdc98ad385e3b94310f7a8.jsonl[266] _id=69e67e741724f0c9e2f8e06d ts=2026-04-20T19:28:51.3030000Z; 15ms: 69cdc98ad385e3b94310f7a8.jsonl[1672] _id=69e67e711724f0c9e2f8e059 ts=2026-04-20T19:28:49.0880000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1673] _id=69e67e711724f0c9e2f8e05b ts=2026-04-20T19:28:49.1030000Z; 20ms: 69cdc98ad385e3b94310f7a8.jsonl[1430] _id=69e6778e1724f0c9e2f8c06b ts=2026-04-20T18:59:26.1220000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1432] _id=69e6778e1724f0c9e2f8c06d ts=2026-04-20T18:59:26.1420000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 5m 
  - Evidence: 95h 5m: 69cdc98ad385e3b94310f7a8.jsonl[1065] _id=69e13bcc1724f0c9e2f6f8fe ts=2026-04-16T19:43:07.2630000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1325] _id=69e674f51724f0c9e2f8b6f7 ts=2026-04-20T18:48:19.8350000Z; 46h 51m: 69cdc98ad385e3b94310f7a8.jsonl[42] _id=69de9c9e7957a33870f3aeb3 ts=2026-04-14T19:59:25.8180000Z -> 69cdc98ad385e3b94310f7a8.jsonl[742] _id=69e12f9c1724f0c9e2f68f78 ts=2026-04-16T18:51:07.4220000Z; 46h 48m: 69cdc98ad385e3b94310f7a8.jsonl[1858] _id=69e6862f1724f0c9e2f8fc05 ts=2026-04-20T20:01:50.9810000Z -> 69cdc98ad385e3b94310f7a8.jsonl[1943] _id=69e918661724f0c9e2fa82fd ts=2026-04-22T18:50:13.7160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.004s..0.011s shown 
  - Evidence: 4ms: 69cdc98ad385e3b94310f7a8.jsonl[538] _id=69de99ed7957a33870f3a1bd ts=2026-04-14T19:47:56.8110000Z -> 69cdc98ad385e3b94310f7a8.jsonl[29] _id=69de99ed7957a33870f3a1bf ts=2026-04-14T19:47:56.8150000Z; 10ms: 69cdc98ad385e3b94310f7a8.jsonl[2185] _id=69e925501724f0c9e2fab419 ts=2026-04-22T19:45:20.0100000Z -> 69cdc98ad385e3b94310f7a8.jsonl[2186] _id=69e925501724f0c9e2fab41b ts=2026-04-22T19:45:20.0200000Z; 11ms: 69cdc98ad385e3b94310f7a8.jsonl[2132] _id=69e923181724f0c9e2faab67 ts=2026-04-22T19:35:52.0640000Z -> 69cdc98ad385e3b94310f7a8.jsonl[2133] _id=69e923181724f0c9e2faab69 ts=2026-04-22T19:35:52.0750000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc98ad385e3b94310f7a8.jsonl:69cdc98ad385e3b94310f7a8, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[970] _id=69e1391f1724f0c9e2f6dcb2 ts=2026-04-16T19:31:42.2440000Z`; `69cdc98ad385e3b94310f7a8.jsonl[1750] _id=69e680031724f0c9e2f8e815 ts=2026-04-20T19:35:31.4350000Z`; `69cdc98ad385e3b94310f7a8.jsonl[1874] _id=69e921011724f0c9e2faa2df ts=2026-04-22T19:26:56.8610000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[1077] _id=69e13c121724f0c9e2f6f9fa ts=2026-04-16T19:44:17.1310000Z`; `69cdc98ad385e3b94310f7a8.jsonl[1547] _id=69e67afb1724f0c9e2f8cfbd ts=2026-04-20T19:14:02.5090000Z`; `69cdc98ad385e3b94310f7a8.jsonl[1577] _id=69e67b831724f0c9e2f8d251 ts=2026-04-20T19:16:18.7430000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[276] _id=69e67eae1724f0c9e2f8e1b9 ts=2026-04-20T19:29:50.0710000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[1668] _id=69e67e731724f0c9e2f8e06b ts=2026-04-20T19:28:51.2940000Z`; `69cdc98ad385e3b94310f7a8.jsonl[271] _id=69e67e951724f0c9e2f8e13b ts=2026-04-20T19:29:24.8760000Z`; `69cdc98ad385e3b94310f7a8.jsonl[1683] _id=69e67e971724f0c9e2f8e153 ts=2026-04-20T19:29:27.2910000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[738] _id=69e91edd1724f0c9e2fa9dc3 ts=?`
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[221] _id=69e677611724f0c9e2f8bf97 ts=2026-04-20T18:58:41.3140000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc98ad385e3b94310f7a8.jsonl[270] _id=69e67e941724f0c9e2f8e137 ts=2026-04-20T19:29:24.3140000Z`; `69cdc98ad385e3b94310f7a8.jsonl[272] _id=69e67e951724f0c9e2f8e13d ts=2026-04-20T19:29:25.0370000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 170 unmatched 'DialogueStartEvent' (totals: 324 start, 158 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 17 open, 17 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 31 start, 22 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.57s, min -16.23s, max -0.31s over 2330 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc98ad385e3b94310f7a8\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=complete, Unit3=complete 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
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
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 68 records 
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

### `DialogueEvent` — 1566 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (660); Unit 3 Dev (323); Unit 3 Dungeon Dev (206); Unit 1 Dev (180); Unit 4 Dev - Dungeon (95); Unit 4 Dev (82); Unit 4 Dev - Anderson Base (20)
- **eventKey:** present on 1084 of 1566 records
- **Intervals:** median 2.46s (p5 0.01s / p95 49.84s, n=1565)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1084; [conversationId, dialogueEventType] x482
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1566/1566 records)
    numeric range 8 .. 107 (40 unique)
data.dialogueEventType  (string, 1566/1566 records)
    "DialogueNodeEvent"  x1084
    "DialogueStartEvent"  x324
    "DialogueFinishEvent"  x158
data.nodeId  (number, 1084/1566 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 536 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (202); Unit 3 Dungeon Dev (95); Unit 3 Dev (86); Unit 1 Dev (59); Unit 4 Dev - Dungeon (44); Unit 4 Dev (43); Unit 4 Dev - Anderson Base (7)
- **Intervals:** median 30.02s (p5 29.95s / p95 34.33s, n=527)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 536/536 records)
data.position.x  (number, 536/536 records)
    numeric range -738.292 .. 1439.39 (336 unique)
data.position.y  (number, 536/536 records)
    numeric range -111.052 .. 161.131 (249 unique)
data.position.z  (number, 536/536 records)
    numeric range -1108.12 .. 2210.31 (336 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 68 records

- **Scenes:** Unit 3 Dev (38); Unit 2 Prod (Refactor) (30)
- **Intervals:** median 11.06s (p5 1.47s / p95 1126.33s, n=67)
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "MapCloseEvent"  x34
    "MapOpenEvent"  x34
data.featureUsed  (string, 68/68 records)
    "Map"  x68
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 53 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 53 of 53 records
- **Intervals:** median 194.13s (p5 0.01s / p95 76672.48s, n=52)
- **`data` key-set variants:** [questEventType, questID, questName] x31; [questEventType, questID, questName, questSuccessOrFailure] x22
- **Fields under `data`:**

```text
data.questEventType  (string, 53/53 records)
    "questActiveEvent"  x31
    "questFinishEvent"  x22
data.questID  (string, 53/53 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 53/53 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 22/53 records)
    "Succeeded"  x22
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 35 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 3 Dev (7); Unit 1 Dev (5)
- **Intervals:** median 9.60s (p5 1.21s / p95 61869.50s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "argumentationNodeAdd"  x24
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 35/35 records)
    "Unit 2 – Watershed"  x23
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 35/35 records)
    "1"  x6
    "D"  x6
    "A"  x5
    "C"  x4
    "B"  x3
    "I"  x3
    "II"  x3
    "3"  x2
    "4"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationToolEvent` — 34 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (14)
- **Intervals:** median 1.25s (p5 0.02s / p95 753.93s, n=33)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "argumentationToolClose"  x17
    "argumentationToolOpen"  x17
data.argumentationTitle  (string, 34/34 records)
    "Unit 2 – Watershed"  x20
    "Unit 3 - Pollution Upstream"  x14
data.toolName  (string, 34/34 records)
    "BackingInfoPanel - Waterfall Data"  x14
    "BackingInfoPanel - Pollution Site Data"  x8
    "BackingInfoPanel - Watershed Graph"  x6
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Image"  x3
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 1.80s (p5 0.17s / p95 40.28s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Clay"  x13
    "Bedrock"  x5
    "Gravel"  x1
data.floor  (string, 19/19 records)
    "5"  x19
data.machine  (string, 19/19 records)
    "1"  x18
    "2"  x1
data.row  (string, 19/19 records)
    "BottomRow"  x15
    "TopRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3)
- **Intervals:** median 82.51s (p5 7.60s / p95 274424.95s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 56.58s (p5 27.28s / p95 311071.14s, n=5)
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

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 344476.87s (p5 190741.61s / p95 498212.13s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
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
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (2 records)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*