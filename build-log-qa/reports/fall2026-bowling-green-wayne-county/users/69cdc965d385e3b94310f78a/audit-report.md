# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f78a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f78a
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f78a.jsonl
- **Records:** 2715 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f78a
- **Time span:** 2026-04-14T13:44:08.111000+00:00 .. 2026-04-24T14:35:57.526000+00:00 (240h 51m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f78a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 2715 records, 7 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 45 INFO, 0 NOT_TESTED, 41 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1892 | 69.69 | 1 | 7 | 1301 | 2026-04-14T13:44:26.313000+00:00 | 2026-04-24T14:35:57.526000+00:00 | 240h 51m |
| PlayerPositionEvent | 551 | 20.29 | 1 | 7 | 0 | 2026-04-14T13:44:08.111000+00:00 | 2026-04-24T14:35:41.608000+00:00 | 240h 51m |
| questEvent | 100 | 3.68 | 1 | 7 | 100 | 2026-04-14T13:44:26.287000+00:00 | 2026-04-24T14:35:46.628000+00:00 | 240h 51m |
| Topographic Map Event | 46 | 1.69 | 1 | 3 | 0 | 2026-04-16T13:41:57.006000+00:00 | 2026-04-24T14:16:26.123000+00:00 | 192h 34m |
| argumentationNodeEvent | 37 | 1.36 | 1 | 2 | 0 | 2026-04-14T14:05:37.249000+00:00 | 2026-04-20T14:15:58.295000+00:00 | 144h 10m |
| WaterChamberEvent | 36 | 1.33 | 1 | 1 | 0 | 2026-04-24T14:31:54.978000+00:00 | 2026-04-24T14:35:36.301000+00:00 | 3m 41s |
| soilMachine | 23 | 0.85 | 1 | 1 | 0 | 2026-04-22T14:05:20.322000+00:00 | 2026-04-22T14:24:27.004000+00:00 | 19m 6s |
| Soil Key Puzzle | 15 | 0.55 | 1 | 3 | 0 | 2026-04-14T14:26:32.683000+00:00 | 2026-04-24T14:03:53.518000+00:00 | 239h 37m |
| argumentationEvent | 11 | 0.41 | 1 | 2 | 0 | 2026-04-14T14:05:13.888000+00:00 | 2026-04-20T14:15:59.454000+00:00 | 144h 10m |
| EndOfUnit | 4 | 0.15 | 1 | 2 | 0 | 2026-04-14T14:11:19.155000+00:00 | 2026-04-22T13:43:30.022000+00:00 | 191h 32m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.782s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173030.426s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.005s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 146.115s median 
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
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 3.834s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 28.425s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.147s median 
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
  - Observed: 5.552s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 46 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `WaterChamberEvent` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 37 records 
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
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 41; 44; 45; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.6x vs baseline. 
  - Observed: 23 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 21 mismatch(es); e.g. 'DialogueNodeEvent:31:72' vs expected 'DialogueNodeEvent:31:73' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[16] _id=69de499d7957a33870f33f1f ts=2026-04-14T14:05:17.2420000Z`; `69cdc965d385e3b94310f78a.jsonl[18] _id=69de499e7957a33870f33f29 ts=2026-04-14T14:05:17.4400000Z`; `69cdc965d385e3b94310f78a.jsonl[20] _id=69de49eb7957a33870f3416d ts=2026-04-14T14:06:35.5300000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'questActiveEvent:40' vs expected 'questActiveEvent:36' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[2542] _id=69eb76c51724f0c9e2fb769d ts=2026-04-24T13:57:25.0380000Z`; `69cdc965d385e3b94310f78a.jsonl[2548] _id=69eb771b1724f0c9e2fb77bf ts=2026-04-24T13:58:51.3330000Z`; `69cdc965d385e3b94310f78a.jsonl[2612] _id=69eb7ba61724f0c9e2fb8f73 ts=2026-04-24T14:18:13.7730000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1891 | 0.002 | 1.782 | 458.536 | 40.922 | 341632.421 | 0.13 | 479 | 5 |
| PlayerPositionEvent | 536 | 0.817 | 30.005 | 661.158 | 36.722 | 169278.026 | 0.09 | 0 | 2 |
| questEvent | 99 | 0.001 | 104.962 | 8758.387 | 1271.445 | 341654.099 | 0.01 | 20 | 9 |
| Topographic Map Event | 45 | 0.327 | 15.913 | 15405.98 | 136292.43 | 345605.014 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 36 | 1.336 | 5.147 | 14417.251 | 562.263 | 516605.847 | 0.0 | 0 | 2 |
| WaterChamberEvent | 35 | 0.151 | 3.834 | 6.324 | 19.75 | 22.628 | 9.49 | 0 | 0 |
| soilMachine | 22 | 0.234 | 5.552 | 52.122 | 161.456 | 617.799 | 1.15 | 0 | 1 |
| Soil Key Puzzle | 14 | 2.999 | 146.115 | 61617.203 | 233498.376 | 345013.554 | 0.0 | 0 | 6 |
| argumentationEvent | 10 | 0.067 | 28.425 | 51904.557 | 285029.495 | 516567.975 | 0.0 | 0 | 2 |
| EndOfUnit | 3 | 0.0 | 173030.426 | 229843.622 | 482153.439 | 516500.441 | 0.0 | 1 | 2 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.005s (p5 29.96s, p95 36.72s, n=536) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 69cdc965d385e3b94310f78a.jsonl[1440] _id=69e62c9c1724f0c9e2f86a69 ts=2026-04-20T13:39:39.5960000Z ~ 69cdc965d385e3b94310f78a.jsonl[1441] _id=69e62cad1724f0c9e2f86ad9 ts=2026-04-20T13:39:39.596Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `704ms: 69cdc965d385e3b94310f78a.jsonl[2631] _id=69eb7f121724f0c9e2fba02f ts=2026-04-24T14:32:49.6760000Z ~ 69cdc965d385e3b94310f78a.jsonl[2632] _id=69eb7f121724f0c9e2fba035 ts=2026-04-24T14:32:50.3800000Z`; `557ms: 69cdc965d385e3b94310f78a.jsonl[2664] _id=69eb7f121724f0c9e2fba031 ts=2026-04-24T14:32:50.0840000Z ~ 69cdc965d385e3b94310f78a.jsonl[2681] _id=69eb7f131724f0c9e2fba039 ts=2026-04-24T14:32:50.6410000Z`; `412ms: 69cdc965d385e3b94310f78a.jsonl[2632] _id=69eb7f121724f0c9e2fba035 ts=2026-04-24T14:32:50.3800000Z ~ 69cdc965d385e3b94310f78a.jsonl[2682] _id=69eb7f131724f0c9e2fba03d ts=2026-04-24T14:32:50.7920000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `67ms: 69cdc965d385e3b94310f78a.jsonl[220] _id=69e6351f1724f0c9e2f89973 ts=2026-04-20T14:15:59.3870000Z ~ 69cdc965d385e3b94310f78a.jsonl[223] _id=69e635201724f0c9e2f8997d ts=2026-04-20T14:15:59.4540000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc965d385e3b94310f78a.jsonl[2542] _id=69eb76c51724f0c9e2fb769d ts=2026-04-24T13:57:25.0380000Z ~ 69cdc965d385e3b94310f78a.jsonl[2540] _id=69eb76c51724f0c9e2fb769f ts=2026-04-24T13:57:25.0400000Z`; `1ms: 69cdc965d385e3b94310f78a.jsonl[2548] _id=69eb771b1724f0c9e2fb77bf ts=2026-04-24T13:58:51.3330000Z ~ 69cdc965d385e3b94310f78a.jsonl[2549] _id=69eb771c1724f0c9e2fb77c1 ts=2026-04-24T13:58:51.3340000Z`; `1ms: 69cdc965d385e3b94310f78a.jsonl[2612] _id=69eb7ba61724f0c9e2fb8f73 ts=2026-04-24T14:18:13.7730000Z ~ 69cdc965d385e3b94310f78a.jsonl[2613] _id=69eb7ba61724f0c9e2fb8f75 ts=2026-04-24T14:18:13.7740000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `690ms: 69cdc965d385e3b94310f78a.jsonl[2311] _id=69e8d5dd1724f0c9e2fa54ef ts=2026-04-22T14:06:20.4050000Z ~ 69cdc965d385e3b94310f78a.jsonl[2312] _id=69e8d5dd1724f0c9e2fa54f9 ts=2026-04-22T14:06:21.0950000Z`; `700ms: 69cdc965d385e3b94310f78a.jsonl[2312] _id=69e8d5dd1724f0c9e2fa54f9 ts=2026-04-22T14:06:21.0950000Z ~ 69cdc965d385e3b94310f78a.jsonl[2313] _id=69e8d5de1724f0c9e2fa5503 ts=2026-04-22T14:06:21.7950000Z`; `282ms: 69cdc965d385e3b94310f78a.jsonl[2313] _id=69e8d5de1724f0c9e2fa5503 ts=2026-04-22T14:06:21.7950000Z ~ 69cdc965d385e3b94310f78a.jsonl[2314] _id=69e8d5de1724f0c9e2fa5505 ts=2026-04-22T14:06:22.0770000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 53m 
  - Evidence: 94h 53m: 69cdc965d385e3b94310f78a.jsonl[103] _id=69e0f2e97957a33870f55261 ts=2026-04-16T14:32:08.2660000Z -> 69cdc965d385e3b94310f78a.jsonl[1239] _id=69e629691724f0c9e2f85367 ts=2026-04-20T13:26:00.6870000Z; 47h 28m: 69cdc965d385e3b94310f78a.jsonl[2528] _id=69e8db1a1724f0c9e2fa743d ts=2026-04-22T14:28:41.9040000Z -> 69cdc965d385e3b94310f78a.jsonl[2541] _id=69eb76c61724f0c9e2fb76a1 ts=2026-04-24T13:57:26.0620000Z; 47h 4m: 69cdc965d385e3b94310f78a.jsonl[838] _id=69de4f237957a33870f364e6 ts=2026-04-14T14:28:51.1370000Z -> 69cdc965d385e3b94310f78a.jsonl[852] _id=69e0e5287957a33870f4f9bb ts=2026-04-16T13:33:27.1310000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 479 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc965d385e3b94310f78a.jsonl[48] _id=69e0e5467957a33870f4f9db ts=2026-04-16T13:33:57.3100000Z -> 69cdc965d385e3b94310f78a.jsonl[49] _id=69e0e5467957a33870f4f9dd ts=2026-04-16T13:33:57.3120000Z; 3ms: 69cdc965d385e3b94310f78a.jsonl[1160] _id=69e0f0ef7957a33870f541f3 ts=2026-04-16T14:23:42.7190000Z -> 69cdc965d385e3b94310f78a.jsonl[1161] _id=69e0f0f07957a33870f541f7 ts=2026-04-16T14:23:42.7220000Z; 3ms: 69cdc965d385e3b94310f78a.jsonl[1169] _id=69e0f1197957a33870f542de ts=2026-04-16T14:24:24.0690000Z -> 69cdc965d385e3b94310f78a.jsonl[1165] _id=69e0f1197957a33870f542e1 ts=2026-04-16T14:24:24.0720000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 28m 
  - Evidence: 143h 28m: 69cdc965d385e3b94310f78a.jsonl[691] _id=69de4b077957a33870f34967 ts=2026-04-14T14:11:19.1550000Z -> 69cdc965d385e3b94310f78a.jsonl[1440] _id=69e62c9c1724f0c9e2f86a69 ts=2026-04-20T13:39:39.5960000Z; 48h 3m: 69cdc965d385e3b94310f78a.jsonl[1441] _id=69e62cad1724f0c9e2f86ad9 ts=2026-04-20T13:39:39.596Z -> 69cdc965d385e3b94310f78a.jsonl[2154] _id=69e8d0821724f0c9e2fa3565 ts=2026-04-22T13:43:30.0220000Z
- **INFO / Info** `EndOfUnit` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f78a.jsonl[1440] _id=69e62c9c1724f0c9e2f86a69 ts=2026-04-20T13:39:39.5960000Z -> 69cdc965d385e3b94310f78a.jsonl[1441] _id=69e62cad1724f0c9e2f86ad9 ts=2026-04-20T13:39:39.596Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 1m 
  - Evidence: 47h 1m: 69cdc965d385e3b94310f78a.jsonl[851] _id=69de4fe57957a33870f36adc ts=2026-04-14T14:32:05.4080000Z -> 69cdc965d385e3b94310f78a.jsonl[46] _id=69e0e5257957a33870f4f9b3 ts=2026-04-16T13:33:23.4340000Z; 46h 40m: 69cdc965d385e3b94310f78a.jsonl[1894] _id=69e639c41724f0c9e2f8b5ab ts=2026-04-20T14:35:48.1580000Z -> 69cdc965d385e3b94310f78a.jsonl[1897] _id=69e8ca351724f0c9e2fa0bb5 ts=2026-04-22T13:16:36.3080000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc965d385e3b94310f78a.jsonl[1215] _id=69e0f2e27957a33870f5521a ts=2026-04-16T14:32:01.2580000Z -> 69cdc965d385e3b94310f78a.jsonl[1813] _id=69e636971724f0c9e2f8a375 ts=2026-04-20T14:22:14.8120000Z; 48h 10m: 69cdc965d385e3b94310f78a.jsonl[2193] _id=69e8d29d1724f0c9e2fa41b5 ts=2026-04-22T13:52:28.7720000Z -> 69cdc965d385e3b94310f78a.jsonl[2558] _id=69eb78281724f0c9e2fb7dab ts=2026-04-24T14:03:20.5130000Z; 47h 28m: 69cdc965d385e3b94310f78a.jsonl[1815] _id=69e636b51724f0c9e2f8a42d ts=2026-04-20T14:22:45.5360000Z -> 69cdc965d385e3b94310f78a.jsonl[2187] _id=69e8d2701724f0c9e2fa4143 ts=2026-04-22T13:51:43.4700000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 69cdc965d385e3b94310f78a.jsonl[1002] _id=69e0e8de7957a33870f51377 ts=2026-04-16T13:49:17.7860000Z -> 69cdc965d385e3b94310f78a.jsonl[1479] _id=69e62ee31724f0c9e2f87621 ts=2026-04-20T13:49:22.8000000Z; 48h 35m: 69cdc965d385e3b94310f78a.jsonl[2105] _id=69e8cff11724f0c9e2fa3071 ts=2026-04-22T13:41:05.0310000Z -> 69cdc965d385e3b94310f78a.jsonl[2605] _id=69eb7b331724f0c9e2fb8d07 ts=2026-04-24T14:16:18.6910000Z; 47h 16m: 69cdc965d385e3b94310f78a.jsonl[1816] _id=69e636be1724f0c9e2f8a4a1 ts=2026-04-20T14:22:54.1760000Z -> 69cdc965d385e3b94310f78a.jsonl[341] _id=69e8cf7d1724f0c9e2fa2c73 ts=2026-04-22T13:39:09.1650000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 29m 
  - Evidence: 143h 29m: 69cdc965d385e3b94310f78a.jsonl[641] _id=69de49eb7957a33870f3416b ts=2026-04-14T14:06:35.4980000Z -> 69cdc965d385e3b94310f78a.jsonl[154] _id=69e62bc41724f0c9e2f86395 ts=2026-04-20T13:36:03.4730000Z; 33m 58s: 69cdc965d385e3b94310f78a.jsonl[1402] _id=69e62bfd1724f0c9e2f864f7 ts=2026-04-20T13:37:01.4410000Z -> 69cdc965d385e3b94310f78a.jsonl[1656] _id=69e633f31724f0c9e2f892e9 ts=2026-04-20T14:10:59.4610000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 69cdc965d385e3b94310f78a.jsonl[640] _id=69de49ea7957a33870f34161 ts=2026-04-14T14:06:34.0260000Z -> 69cdc965d385e3b94310f78a.jsonl[1398] _id=69e62be81724f0c9e2f8645b ts=2026-04-20T13:36:39.8730000Z; 35m 28s: 69cdc965d385e3b94310f78a.jsonl[1401] _id=69e62bfb1724f0c9e2f864e9 ts=2026-04-20T13:36:58.9960000Z -> 69cdc965d385e3b94310f78a.jsonl[1665] _id=69e6344b1724f0c9e2f8943b ts=2026-04-20T14:12:27.1660000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 54m 
  - Evidence: 94h 54m: 69cdc965d385e3b94310f78a.jsonl[1209] _id=69e0f2d37957a33870f55193 ts=2026-04-16T14:31:46.5560000Z -> 69cdc965d385e3b94310f78a.jsonl[1238] _id=69e629691724f0c9e2f85361 ts=2026-04-20T13:26:00.6550000Z; 47h 28m: 69cdc965d385e3b94310f78a.jsonl[2536] _id=69e8db131724f0c9e2fa7403 ts=2026-04-22T14:28:34.7800000Z -> 69cdc965d385e3b94310f78a.jsonl[2542] _id=69eb76c51724f0c9e2fb769d ts=2026-04-24T13:57:25.0380000Z; 47h 4m: 69cdc965d385e3b94310f78a.jsonl[844] _id=69de4f227957a33870f364e0 ts=2026-04-14T14:28:50.8030000Z -> 69cdc965d385e3b94310f78a.jsonl[47] _id=69e0e5277957a33870f4f9b5 ts=2026-04-16T13:33:25.8460000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 20 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 69cdc965d385e3b94310f78a.jsonl[2548] _id=69eb771b1724f0c9e2fb77bf ts=2026-04-24T13:58:51.3330000Z -> 69cdc965d385e3b94310f78a.jsonl[2549] _id=69eb771c1724f0c9e2fb77c1 ts=2026-04-24T13:58:51.3340000Z; 1ms: 69cdc965d385e3b94310f78a.jsonl[2612] _id=69eb7ba61724f0c9e2fb8f73 ts=2026-04-24T14:18:13.7730000Z -> 69cdc965d385e3b94310f78a.jsonl[2613] _id=69eb7ba61724f0c9e2fb8f75 ts=2026-04-24T14:18:13.7740000Z; 2ms: 69cdc965d385e3b94310f78a.jsonl[2542] _id=69eb76c51724f0c9e2fb769d ts=2026-04-24T13:57:25.0380000Z -> 69cdc965d385e3b94310f78a.jsonl[2540] _id=69eb76c51724f0c9e2fb769f ts=2026-04-24T13:57:25.0400000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 10m 17s 
  - Evidence: 10m 17s: 69cdc965d385e3b94310f78a.jsonl[2345] _id=69e8d6ee1724f0c9e2fa5cf9 ts=2026-04-22T14:10:53.4230000Z -> 69cdc965d385e3b94310f78a.jsonl[2384] _id=69e8d9571724f0c9e2fa6a4f ts=2026-04-22T14:21:11.2220000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc965d385e3b94310f78a.jsonl:69cdc965d385e3b94310f78a, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[813] _id=69de4e9b7957a33870f36186 ts=2026-04-14T14:26:35.6820000Z`; `69cdc965d385e3b94310f78a.jsonl[889] _id=69e0e6427957a33870f501e9 ts=2026-04-16T13:38:09.8360000Z`; `69cdc965d385e3b94310f78a.jsonl[1071] _id=69e0ed0e7957a33870f52b69 ts=2026-04-16T14:07:09.0250000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[1511] _id=69e62fca1724f0c9e2f87b0d ts=2026-04-20T13:53:13.8990000Z`; `69cdc965d385e3b94310f78a.jsonl[190] _id=69e630411724f0c9e2f87d83 ts=2026-04-20T13:55:11.2510000Z`; `69cdc965d385e3b94310f78a.jsonl[2391] _id=69e8d7b21724f0c9e2fa6297 ts=2026-04-22T14:14:09.9830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[223] _id=69e635201724f0c9e2f8997d ts=2026-04-20T14:15:59.4540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[494] _id=69de46597957a33870f32c37 ts=2026-04-14T13:51:21.2850000Z`; `69cdc965d385e3b94310f78a.jsonl[2424] _id=69e8d8931724f0c9e2fa667b ts=2026-04-22T14:17:54.5200000Z`; `69cdc965d385e3b94310f78a.jsonl[2515] _id=69e8dabd1724f0c9e2fa71af ts=2026-04-22T14:27:08.4450000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f78a.jsonl[100] _id=69e0f2477957a33870f54c93 ts=2026-04-16T14:29:26.2570000Z`; `69cdc965d385e3b94310f78a.jsonl[1215] _id=69e0f2e27957a33870f5521a ts=2026-04-16T14:32:01.2580000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 220 unmatched 'DialogueStartEvent' (totals: 404 start, 187 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Started' (totals: 9 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'questActiveEvent' (totals: 60 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.62s, min -17.81s, max -0.05s over 2715 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f78a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
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
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 46 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 1892 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (451); Unit 2 Prod (Refactor) (411); Unit 1 Dev (408); Unit 3 Dungeon Dev (236); Unit 4 Dev - Dungeon (193); Unit 4 Dev (163); Unit 5 Dev - Dungeon (30)
- **eventKey:** present on 1301 of 1892 records
- **Intervals:** median 1.78s (p5 0.01s / p95 40.92s, n=1891)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1301; [conversationId, dialogueEventType] x591
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1892/1892 records)
    numeric range 10 .. 107 (38 unique)
data.dialogueEventType  (string, 1892/1892 records)
    "DialogueNodeEvent"  x1301
    "DialogueStartEvent"  x404
    "DialogueFinishEvent"  x187
data.nodeId  (number, 1301/1892 records)
    numeric range 0 .. 286 (202 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 551 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (155); Unit 1 Dev (93); Unit 4 Dev (93); Unit 3 Dev (82); Unit 3 Dungeon Dev (65); Unit 4 Dev - Dungeon (47); Unit 5 Dev - Dungeon (16)
- **Intervals:** median 30.00s (p5 29.96s / p95 36.72s, n=536)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 551/551 records)
data.position.x  (number, 551/551 records)
    numeric range -694.133 .. 1556.9 (386 unique)
data.position.y  (number, 551/551 records)
    numeric range -111.173 .. 163.768 (304 unique)
data.position.z  (number, 551/551 records)
    numeric range -1108.48 .. 1918.92 (387 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 100 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 4 Dev (19); Unit 4 Dev - Dungeon (19); Unit 2 Prod (Refactor) (18); Unit 3 Dev (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4)
- **eventKey:** present on 100 of 100 records
- **Intervals:** median 104.96s (p5 0.01s / p95 1271.44s, n=99)
- **`data` key-set variants:** [questEventType, questID, questName] x60; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 100/100 records)
    "questActiveEvent"  x60
    "questFinishEvent"  x40
data.questID  (string, 100/100 records)
    27 unique values (see csv/event_unique_values.csv)
data.questName  (string, 100/100 records)
    27 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/100 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 46 records

- **Scenes:** Unit 3 Dev (26); Unit 2 Prod (Refactor) (18); Unit 4 Dev (2)
- **Intervals:** median 15.91s (p5 1.72s / p95 136292.43s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "MapCloseEvent"  x23
    "MapOpenEvent"  x23
data.featureUsed  (string, 46/46 records)
    "Map"  x46
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 37 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (25); Unit 1 Dev (12)
- **Intervals:** median 5.15s (p5 1.68s / p95 562.26s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "argumentationNodeAdd"  x23
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 37/37 records)
    "Unit 3 - Pollution Upstream"  x25
    "Unit 1 - Freshwater"  x12
data.nodeName  (string, 37/37 records)
    "A"  x11
    "B"  x8
    "1"  x6
    "I"  x3
    "2"  x2
    "3"  x2
    "4"  x2
    "II"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `WaterChamberEvent` — 36 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (36)
- **Intervals:** median 3.83s (p5 0.26s / p95 19.75s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "On"  x21
    "Off"  x15
data.floor  (string, 36/36 records)
    "3"  x22
    "2"  x9
    "1"  x5
data.machineNumber  (string, 36/36 records)
    "One"  x35
    "Two"  x1
data.machineType  (string, 36/36 records)
    "Condenser"  x20
    "Evaporator"  x6
    "VentSwitch"  x5
    "DualChamber_Evaporator"  x4
    "DualChamber_Condenser"  x1
data.room  (string, 36/36 records)
    "1"  x19
    "2"  x13
    "3"  x2
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 23 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (23)
- **Intervals:** median 5.55s (p5 0.28s / p95 161.46s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "ChangeCanister"  x23
data.canisterType  (string, 23/23 records)
    "Clay"  x11
    "Gravel"  x5
    "Sand"  x4
    "Bedrock"  x3
data.floor  (string, 23/23 records)
    "4"  x13
    "5"  x7
    "3"  x3
data.machine  (string, 23/23 records)
    "1"  x21
    "2"  x2
data.row  (string, 23/23 records)
    "TopRow"  x23
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 15 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 4 Dev (4); Unit 3 Dev (2)
- **Intervals:** median 146.11s (p5 3.05s / p95 233498.38s, n=14)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 15/15 records)
    "Started"  x9
    "Finished"  x6
data.Unit  (string, 15/15 records)
    "Unit 2 Prod (Refactor)"  x9
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3)
- **Intervals:** median 28.43s (p5 0.54s / p95 285029.50s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 11/11 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
data.argumentationTitle  (string, 11/11 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (1)
- **Intervals:** median 173030.43s (p5 17303.04s / p95 482153.44s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x3
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
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (9 records)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*