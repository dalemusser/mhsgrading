# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f729

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f729
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f729.jsonl
- **Records:** 2422 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f729
- **Time span:** 2026-04-13T17:52:35.713000+00:00 .. 2026-04-23T18:41:41.952000+00:00 (240h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f729\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **12 event types**, 2422 records, 7 scenes.
- Findings: **0 FAIL**, **44 WARNING**, 58 INFO, 2 NOT_TESTED, 42 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1473 | 60.82 | 1 | 7 | 999 | 2026-04-13T17:52:53.820000+00:00 | 2026-04-23T18:41:41.952000+00:00 | 240h 48m |
| PlayerPositionEvent | 644 | 26.59 | 1 | 7 | 0 | 2026-04-13T17:52:35.713000+00:00 | 2026-04-23T18:41:30.257000+00:00 | 240h 48m |
| questEvent | 76 | 3.14 | 1 | 7 | 76 | 2026-04-13T17:52:53.805000+00:00 | 2026-04-23T18:40:36.046000+00:00 | 240h 47m |
| Topographic Map Event | 75 | 3.1 | 1 | 3 | 0 | 2026-04-13T18:39:08.030000+00:00 | 2026-04-21T18:25:50.629000+00:00 | 191h 46m |
| argumentationToolEvent | 60 | 2.48 | 1 | 2 | 0 | 2026-04-17T18:17:24.998000+00:00 | 2026-04-23T18:33:55.376000+00:00 | 144h 16m |
| TopographicMapEvent | 37 | 1.53 | 1 | 2 | 0 | 2026-04-13T18:39:14.674000+00:00 | 2026-04-21T18:24:48.419000+00:00 | 191h 45m |
| Soil Key Puzzle | 19 | 0.78 | 1 | 3 | 0 | 2026-04-13T18:30:34.113000+00:00 | 2026-04-23T18:02:32.616000+00:00 | 239h 31m |
| soilMachine | 19 | 0.78 | 1 | 1 | 0 | 2026-04-23T18:12:11.117000+00:00 | 2026-04-23T18:19:01.254000+00:00 | 6m 50s |
| argumentationEvent | 8 | 0.33 | 1 | 3 | 0 | 2026-04-13T18:12:36.829000+00:00 | 2026-04-23T18:32:56.188000+00:00 | 240h 20m |
| argumentationNodeEvent | 7 | 0.29 | 1 | 2 | 0 | 2026-04-13T18:12:56.024000+00:00 | 2026-04-17T18:36:22.394000+00:00 | 96h 23m |
| EndOfUnit | 2 | 0.08 | 1 | 2 | 0 | 2026-04-13T18:17:13.470000+00:00 | 2026-04-21T18:30:50.668000+00:00 | 192h 13m |
| crash | 2 | 0.08 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 692017.198s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.028s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 176.193s median 
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
  - Observed: 11.421s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 32.23s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.178s median 
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
  - Observed: 6.044s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 75 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 7 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 6.7x vs baseline. 
  - Observed: 60 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'DialogueNodeEvent:20:111' vs expected 'DialogueNodeEvent:20:33' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f729.jsonl[203] _id=69dfd3c47957a33870f42e38 ts=2026-04-15T18:06:58.9350000Z`; `69cdc907d385e3b94310f729.jsonl[458] _id=69e27dc11724f0c9e2f78842 ts=2026-04-17T18:36:48.9920000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 75 records, TopographicMapEvent: 37 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1472 | 0.0 | 3.171 | 588.946 | 50.665 | 339641.841 | 0.1 | 396 | 8 |
| PlayerPositionEvent | 632 | 29.715 | 30.028 | 1101.699 | 40.746 | 339276.784 | 0.05 | 0 | 3 |
| questEvent | 75 | 0.003 | 126.261 | 11558.163 | 52889.79 | 339383.557 | 0.01 | 7 | 11 |
| Topographic Map Event | 74 | 0.678 | 18.555 | 9329.765 | 3404.859 | 339785.044 | 0.01 | 0 | 7 |
| argumentationToolEvent | 59 | 0.002 | 1.178 | 8803.227 | 49.153 | 518170.8 | 0.01 | 7 | 2 |
| TopographicMapEvent | 36 | 0.598 | 11.421 | 19175.937 | 170969.521 | 339812.134 | 0.0 | 0 | 5 |
| Soil Key Puzzle | 18 | 2.853 | 176.193 | 47906.584 | 197729.674 | 342091.56 | 0.0 | 0 | 6 |
| soilMachine | 18 | 1.147 | 6.044 | 22.785 | 96.478 | 136.978 | 2.63 | 0 | 0 |
| argumentationEvent | 7 | 0.106 | 37.485 | 123602.766 | 466766.886 | 518167.122 | 0.0 | 0 | 2 |
| argumentationNodeEvent | 6 | 2.883 | 32.23 | 57834.395 | 260162.775 | 346864.243 | 0.0 | 0 | 1 |
| EndOfUnit | 1 | 692017.198 | 692017.198 | 692017.198 | 692017.198 | 692017.198 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.028s (p5 29.96s, p95 40.75s, n=632) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `106ms: 69cdc907d385e3b94310f729.jsonl[1667] _id=69e27dc11724f0c9e2f78840 ts=2026-04-17T18:36:48.9600000Z ~ 69cdc907d385e3b94310f729.jsonl[456] _id=69e27dc31724f0c9e2f7884c ts=2026-04-17T18:36:49.0660000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `543ms: 69cdc907d385e3b94310f729.jsonl[1623] _id=69e27c661724f0c9e2f78088 ts=2026-04-17T18:31:01.4350000Z ~ 69cdc907d385e3b94310f729.jsonl[425] _id=69e27c661724f0c9e2f78090 ts=2026-04-17T18:31:01.9780000Z`; `653ms: 69cdc907d385e3b94310f729.jsonl[1624] _id=69e27c661724f0c9e2f7808a ts=2026-04-17T18:31:01.4390000Z ~ 69cdc907d385e3b94310f729.jsonl[1625] _id=69e27c661724f0c9e2f78092 ts=2026-04-17T18:31:02.0920000Z`; `1000ms: 69cdc907d385e3b94310f729.jsonl[1625] _id=69e27c661724f0c9e2f78092 ts=2026-04-17T18:31:02.0920000Z ~ 69cdc907d385e3b94310f729.jsonl[1619] _id=69e27c671724f0c9e2f7809c ts=2026-04-17T18:31:03.0920000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 20m 
  - Evidence: 94h 20m: 69cdc907d385e3b94310f729.jsonl[469] _id=69e27e241724f0c9e2f78af2 ts=2026-04-17T18:38:27.8310000Z -> 69cdc907d385e3b94310f729.jsonl[1697] _id=69e7ace01724f0c9e2f91a1b ts=2026-04-21T16:59:09.6720000Z; 47h 19m: 69cdc907d385e3b94310f729.jsonl[2098] _id=69e7c4951724f0c9e2f9a75e ts=2026-04-21T18:40:20.3200000Z -> 69cdc907d385e3b94310f729.jsonl[2102] _id=69ea5e2b1724f0c9e2fb046f ts=2026-04-23T18:00:09.7130000Z; 47h 11m: 69cdc907d385e3b94310f729.jsonl[989] _id=69dd38b97957a33870f2918c ts=2026-04-13T18:40:56.6240000Z -> 69cdc907d385e3b94310f729.jsonl[162] _id=69dfd0527957a33870f41471 ts=2026-04-15T17:52:17.6160000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 396 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc907d385e3b94310f729.jsonl[2052] _id=69e7c25b1724f0c9e2f997a1 ts=2026-04-21T18:30:50.6840000Z -> 69cdc907d385e3b94310f729.jsonl[2053] _id=69e7c2681724f0c9e2f997fd ts=2026-04-21T18:30:50.684Z; 2ms: 69cdc907d385e3b94310f729.jsonl[691] _id=69ea67d31724f0c9e2fb4e59 ts=2026-04-23T18:41:21.6280000Z -> 69cdc907d385e3b94310f729.jsonl[2387] _id=69ea67d31724f0c9e2fb4e5b ts=2026-04-23T18:41:21.6300000Z; 3ms: 69cdc907d385e3b94310f729.jsonl[270] _id=69dfdb6d7957a33870f46465 ts=2026-04-15T18:39:40.3120000Z -> 69cdc907d385e3b94310f729.jsonl[1276] _id=69dfdb6d7957a33870f46469 ts=2026-04-15T18:39:40.3150000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 192h 13m 
  - Evidence: 192h 13m: 69cdc907d385e3b94310f729.jsonl[856] _id=69dd332a7957a33870f26be8 ts=2026-04-13T18:17:13.4700000Z -> 69cdc907d385e3b94310f729.jsonl[2048] _id=69e7c25b1724f0c9e2f9979f ts=2026-04-21T18:30:50.6680000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 14m 
  - Evidence: 94h 14m: 69cdc907d385e3b94310f729.jsonl[1686] _id=69e27e811724f0c9e2f78cee ts=2026-04-17T18:40:00.5400000Z -> 69cdc907d385e3b94310f729.jsonl[474] _id=69e7abcf1724f0c9e2f91545 ts=2026-04-21T16:54:37.3240000Z; 47h 11m: 69cdc907d385e3b94310f729.jsonl[987] _id=69dd38a27957a33870f29138 ts=2026-04-13T18:40:33.4000000Z -> 69cdc907d385e3b94310f729.jsonl[993] _id=69dfd04f7957a33870f41453 ts=2026-04-15T17:52:13.5840000Z; 46h 14m: 69cdc907d385e3b94310f729.jsonl[274] _id=69dfdb707957a33870f46485 ts=2026-04-15T18:39:43.1500000Z -> 69cdc907d385e3b94310f729.jsonl[1277] _id=69e265a71724f0c9e2f71f2e ts=2026-04-17T16:53:57.8710000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 1m 
  - Evidence: 95h 1m: 69cdc907d385e3b94310f729.jsonl[369] _id=69e274081724f0c9e2f75804 ts=2026-04-17T17:55:19.1170000Z -> 69cdc907d385e3b94310f729.jsonl[477] _id=69e7ac541724f0c9e2f91739 ts=2026-04-21T16:56:50.6770000Z; 47h 50m: 69cdc907d385e3b94310f729.jsonl[139] _id=69dd364d7957a33870f28142 ts=2026-04-13T18:30:36.9660000Z -> 69cdc907d385e3b94310f729.jsonl[233] _id=69dfd72c7957a33870f44221 ts=2026-04-15T18:21:31.0130000Z; 47h 24m: 69cdc907d385e3b94310f729.jsonl[2076] _id=69e7c3bd1724f0c9e2f9a191 ts=2026-04-21T18:36:44.7550000Z -> 69cdc907d385e3b94310f729.jsonl[2111] _id=69ea5e7c1724f0c9e2fb05e1 ts=2026-04-23T18:01:30.8910000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 23m 
  - Evidence: 94h 23m: 69cdc907d385e3b94310f729.jsonl[1621] _id=69e27cae1724f0c9e2f78204 ts=2026-04-17T18:32:14.2580000Z -> 69cdc907d385e3b94310f729.jsonl[473] _id=69e7abf81724f0c9e2f915a5 ts=2026-04-21T16:55:19.3020000Z; 47h 23m: 69cdc907d385e3b94310f729.jsonl[990] _id=69dd38bf7957a33870f291a0 ts=2026-04-13T18:41:02.4260000Z -> 69cdc907d385e3b94310f729.jsonl[1092] _id=69dfd3207957a33870f429af ts=2026-04-15T18:04:14.9030000Z; 46h 33m: 69cdc907d385e3b94310f729.jsonl[1239] _id=69dfd91a7957a33870f45051 ts=2026-04-15T18:29:45.7210000Z -> 69cdc907d385e3b94310f729.jsonl[1332] _id=69e267e31724f0c9e2f72f5a ts=2026-04-17T17:03:30.2640000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 23m 
  - Evidence: 94h 23m: 69cdc907d385e3b94310f729.jsonl[426] _id=69e27c9c1724f0c9e2f781a4 ts=2026-04-17T18:31:55.5310000Z -> 69cdc907d385e3b94310f729.jsonl[1688] _id=69e7ac011724f0c9e2f915ef ts=2026-04-21T16:55:27.6650000Z; 47h 42m: 69cdc907d385e3b94310f729.jsonl[1193] _id=69dfd6a77957a33870f43eb5 ts=2026-04-15T18:19:18.7770000Z -> 69cdc907d385e3b94310f729.jsonl[1483] _id=69e2758b1724f0c9e2f761e2 ts=2026-04-17T18:01:46.5730000Z; 47h 25m: 69cdc907d385e3b94310f729.jsonl[984] _id=69dd38537957a33870f28f0e ts=2026-04-13T18:39:14.6740000Z -> 69cdc907d385e3b94310f729.jsonl[1096] _id=69dfd3297957a33870f42a09 ts=2026-04-15T18:04:24.7700000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 69cdc907d385e3b94310f729.jsonl[456] _id=69e27dc31724f0c9e2f7884c ts=2026-04-17T18:36:49.0660000Z -> 69cdc907d385e3b94310f729.jsonl[655] _id=69ea65d91724f0c9e2fb411f ts=2026-04-23T18:32:56.1880000Z; 96h 20m: 69cdc907d385e3b94310f729.jsonl[94] _id=69dd32797957a33870f266ee ts=2026-04-13T18:14:16.7810000Z -> 69cdc907d385e3b94310f729.jsonl[437] _id=69e27d4a1724f0c9e2f78538 ts=2026-04-17T18:34:49.7830000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 21m 
  - Evidence: 96h 21m: 69cdc907d385e3b94310f729.jsonl[93] _id=69dd32767957a33870f266e0 ts=2026-04-13T18:14:13.6920000Z -> 69cdc907d385e3b94310f729.jsonl[1660] _id=69e27d661724f0c9e2f785ca ts=2026-04-17T18:35:17.9350000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 69cdc907d385e3b94310f729.jsonl[1670] _id=69e27dbb1724f0c9e2f78816 ts=2026-04-17T18:36:42.6440000Z -> 69cdc907d385e3b94310f729.jsonl[656] _id=69ea65d71724f0c9e2fb40f9 ts=2026-04-23T18:32:53.4440000Z; 13m 29s: 69cdc907d385e3b94310f729.jsonl[410] _id=69e2793b1724f0c9e2f7749a ts=2026-04-17T18:17:31.0830000Z -> 69cdc907d385e3b94310f729.jsonl[1622] _id=69e27c651724f0c9e2f7807e ts=2026-04-17T18:31:00.3450000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f729.jsonl[656] _id=69ea65d71724f0c9e2fb40f9 ts=2026-04-23T18:32:53.4440000Z -> 69cdc907d385e3b94310f729.jsonl[2351] _id=69ea65d71724f0c9e2fb40fd ts=2026-04-23T18:32:53.4460000Z; 4ms: 69cdc907d385e3b94310f729.jsonl[1623] _id=69e27c661724f0c9e2f78088 ts=2026-04-17T18:31:01.4350000Z -> 69cdc907d385e3b94310f729.jsonl[1624] _id=69e27c661724f0c9e2f7808a ts=2026-04-17T18:31:01.4390000Z; 5ms: 69cdc907d385e3b94310f729.jsonl[2363] _id=69ea66121724f0c9e2fb42f1 ts=2026-04-23T18:33:53.2400000Z -> 69cdc907d385e3b94310f729.jsonl[668] _id=69ea66131724f0c9e2fb42f3 ts=2026-04-23T18:33:53.2450000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 16m 
  - Evidence: 94h 16m: 69cdc907d385e3b94310f729.jsonl[1684] _id=69e27e191724f0c9e2f78aa0 ts=2026-04-17T18:38:16.6190000Z -> 69cdc907d385e3b94310f729.jsonl[1687] _id=69e7abd11724f0c9e2f9154d ts=2026-04-21T16:54:40.1760000Z; 47h 25m: 69cdc907d385e3b94310f729.jsonl[589] _id=69e7c32f1724f0c9e2f99cf3 ts=2026-04-21T18:34:22.3610000Z -> 69cdc907d385e3b94310f729.jsonl[2101] _id=69ea5e181724f0c9e2fb0455 ts=2026-04-23T17:59:50.8280000Z; 47h 13m: 69cdc907d385e3b94310f729.jsonl[158] _id=69dd38407957a33870f28e94 ts=2026-04-13T18:38:56.2130000Z -> 69cdc907d385e3b94310f729.jsonl[992] _id=69dfd0517957a33870f41465 ts=2026-04-15T17:52:16.2150000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.003s..0.007s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f729.jsonl[74] _id=69dd31c57957a33870f261b2 ts=2026-04-13T18:11:16.5590000Z -> 69cdc907d385e3b94310f729.jsonl[75] _id=69dd31c57957a33870f261b4 ts=2026-04-13T18:11:16.5620000Z; 6ms: 69cdc907d385e3b94310f729.jsonl[2220] _id=69ea61c61724f0c9e2fb2101 ts=2026-04-23T18:15:33.1170000Z -> 69cdc907d385e3b94310f729.jsonl[2221] _id=69ea61c61724f0c9e2fb2104 ts=2026-04-23T18:15:33.1230000Z; 7ms: 69cdc907d385e3b94310f729.jsonl[2149] _id=69ea5fc81724f0c9e2fb0f37 ts=2026-04-23T18:07:03.2640000Z -> 69cdc907d385e3b94310f729.jsonl[2150] _id=69ea5fc81724f0c9e2fb0f39 ts=2026-04-23T18:07:03.2710000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc907d385e3b94310f729.jsonl:69cdc907d385e3b94310f729, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f729.jsonl[139] _id=69dd364d7957a33870f28142 ts=2026-04-13T18:30:36.9660000Z`; `69cdc907d385e3b94310f729.jsonl[1214] _id=69dfd7da7957a33870f44649 ts=2026-04-15T18:24:25.4880000Z`; `69cdc907d385e3b94310f729.jsonl[1696] _id=69e7acda1724f0c9e2f919ef ts=2026-04-21T16:59:04.7880000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 37 record(s) match the trigger in 69cdc907d385e3b94310f729.jsonl:69cdc907d385e3b94310f729, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f729.jsonl[984] _id=69dd38537957a33870f28f0e ts=2026-04-13T18:39:14.6740000Z`; `69cdc907d385e3b94310f729.jsonl[1096] _id=69dfd3297957a33870f42a09 ts=2026-04-15T18:04:24.7700000Z`; `69cdc907d385e3b94310f729.jsonl[1094] _id=69dfd32c7957a33870f42a1b ts=2026-04-15T18:04:27.3840000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f729.jsonl[14] _id=69e276f71724f0c9e2f7699c ts=2026-04-17T18:07:51.2000000Z`; `69cdc907d385e3b94310f729.jsonl[389] _id=69e2778d1724f0c9e2f76c7c ts=2026-04-17T18:10:20.6810000Z`; `69cdc907d385e3b94310f729.jsonl[2279] _id=69ea635b1724f0c9e2fb2e21 ts=2026-04-23T18:22:18.4340000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f729.jsonl[456] _id=69e27dc31724f0c9e2f7884c ts=2026-04-17T18:36:49.0660000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc907d385e3b94310f729.jsonl[406] _id=69e279381724f0c9e2f77480 ts=2026-04-17T18:17:27.7450000Z`; `69cdc907d385e3b94310f729.jsonl[1573] _id=69e279391724f0c9e2f77484 ts=2026-04-17T18:17:28.7560000Z`; `69cdc907d385e3b94310f729.jsonl[410] _id=69e2793b1724f0c9e2f7749a ts=2026-04-17T18:17:31.0830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f729.jsonl[1700] _id=69e7acde1724f0c9e2f91a11 ts=2026-04-21T16:59:09.6490000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `69cdc907d385e3b94310f729.jsonl[582] _id=69e7c25c1724f0c9e2f997a3 ts=?`; `69cdc907d385e3b94310f729.jsonl[2281] _id=69ea63681724f0c9e2fb2e7b ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f729.jsonl[289] _id=69e2669b1724f0c9e2f725b8 ts=2026-04-17T16:58:02.7980000Z`; `69cdc907d385e3b94310f729.jsonl[300] _id=69e2674a1724f0c9e2f72a9a ts=2026-04-17T17:00:57.6220000Z`; `69cdc907d385e3b94310f729.jsonl[308] _id=69e267f51724f0c9e2f73036 ts=2026-04-17T17:03:47.7920000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `69cdc907d385e3b94310f729.jsonl[407] _id=69e279381724f0c9e2f77482 ts=2026-04-17T18:17:27.8470000Z`; `69cdc907d385e3b94310f729.jsonl[408] _id=69e2793a1724f0c9e2f7748e ts=2026-04-17T18:17:30.0070000Z`; `69cdc907d385e3b94310f729.jsonl[1622] _id=69e27c651724f0c9e2f7807e ts=2026-04-17T18:31:00.3450000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 169 unmatched 'DialogueStartEvent' (totals: 320 start, 154 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 9 unmatched 'Started' (totals: 14 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 29 open, 31 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 29 unmatched 'questActiveEvent' (totals: 52 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.05s, min -14.07s, max -0.68s over 2420 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f729\coverage.yaml

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
  - Observed: 75 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
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

### `DialogueEvent` — 1473 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (538); Unit 3 Dev (282); Unit 1 Dev (184); Unit 3 Dungeon Dev (154); Unit 4 Dev (124); Unit 4 Dev - Dungeon (98); Unit 4 Dev - Anderson Base (93)
- **eventKey:** present on 999 of 1473 records
- **Intervals:** median 3.17s (p5 0.01s / p95 50.67s, n=1472)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x999; [conversationId, dialogueEventType] x474
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1473/1473 records)
    numeric range 10 .. 114 (39 unique)
data.dialogueEventType  (string, 1473/1473 records)
    "DialogueNodeEvent"  x999
    "DialogueStartEvent"  x320
    "DialogueFinishEvent"  x154
data.nodeId  (number, 999/1473 records)
    numeric range 0 .. 289 (202 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 644 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (237); Unit 3 Dungeon Dev (154); Unit 3 Dev (99); Unit 1 Dev (50); Unit 4 Dev (43); Unit 4 Dev - Dungeon (33); Unit 4 Dev - Anderson Base (28)
- **Intervals:** median 30.03s (p5 29.96s / p95 40.75s, n=632)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 644/644 records)
data.position.x  (number, 644/644 records)
    numeric range -653.366 .. 1549.85 (324 unique)
data.position.y  (number, 644/644 records)
    numeric range -114.326 .. 163.344 (230 unique)
data.position.z  (number, 644/644 records)
    numeric range -1112.86 .. 2017.96 (324 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 4 Dev (5); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 126.26s (p5 0.01s / p95 52889.79s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x24
data.questID  (string, 76/76 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/76 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 75 records

- **Scenes:** Unit 3 Dev (38); Unit 2 Prod (Refactor) (31); Unit 3 Dungeon Dev (6)
- **Intervals:** median 18.55s (p5 1.96s / p95 3404.86s, n=74)
- **Fields under `data`:**

```text
data.actionType  (string, 75/75 records)
    "MapOpenEvent"  x38
    "MapCloseEvent"  x37
data.featureUsed  (string, 75/75 records)
    "Map"  x75
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationToolEvent` — 60 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (40); Unit 4 Dev - Anderson Base (20)
- **Intervals:** median 1.18s (p5 0.01s / p95 49.15s, n=59)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "argumentationToolClose"  x31
    "argumentationToolOpen"  x29
data.argumentationTitle  (string, 60/60 records)
    "Unit 3 - Pollution Upstream"  x40
    "Unit 4 - Flooding"  x20
data.toolName  (string, 60/60 records)
    "BackingInfoPanel - Pollution Site Data"  x24
    "BackingInfoPanel - Soil Layers and Fountain Data"  x12
    "BackingInfoPanel - "  x8
    "BackingInfoPanel - Soil Flow Rates"  x8
    "BackingInfoPanel - Watershed Image"  x8
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TopographicMapEvent` — 37 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 3 Dev (18)
- **Intervals:** median 11.42s (p5 1.98s / p95 170969.52s, n=36)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "dragStart"  x19
    "dragEnd"  x18
data.featureUsed  (string, 37/37 records)
    "waypoint"  x37
data.location  (object, 37/37 records)
data.location.x  (number, 37/37 records)
    numeric range -797.747 .. 273.46 (19 unique)
data.location.y  (number, 37/37 records)
    numeric range -307.4 .. 179.255 (20 unique)
data.location.z  (number, 37/37 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 19 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 4 Dev (4); Unit 3 Dev (2)
- **Intervals:** median 176.19s (p5 22.08s / p95 197729.67s, n=18)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 19/19 records)
    "Started"  x14
    "Finished"  x5
data.Unit  (string, 19/19 records)
    "Unit 2 Prod (Refactor)"  x13
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 6.04s (p5 1.74s / p95 96.48s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Bedrock"  x9
    "Clay"  x6
    "Gravel"  x3
    "Sand"  x1
data.floor  (string, 19/19 records)
    "5"  x15
    "4"  x3
    "3"  x1
data.machine  (string, 19/19 records)
    "1"  x18
    "2"  x1
data.row  (string, 19/19 records)
    "BottomRow"  x11
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 37.48s (p5 8.81s / p95 466766.89s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationNodeEvent` — 7 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 32.23s (p5 6.27s / p95 260162.78s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationNodeAdd"  x7
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x1
data.nodeName  (string, 7/7 records)
    "A"  x2
    "I"  x2
    "1"  x1
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 692017.20s (p5 692017.20s / p95 692017.20s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Cannot close a closed AudioContext."  x1
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit3"  x1
    "unit4"  x1
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (13 records)
- `TopographicMapEvent` data.actionType: "dragStart" (19x)
- `soilMachine` data.canisterType: "Bedrock" (9x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*