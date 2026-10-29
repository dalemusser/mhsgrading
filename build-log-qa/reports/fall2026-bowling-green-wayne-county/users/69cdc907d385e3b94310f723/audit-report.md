# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f723

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc907d385e3b94310f723
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc907d385e3b94310f723.jsonl
- **Records:** 2316 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc907d385e3b94310f723
- **Time span:** 2026-04-13T17:54:42.823000+00:00 .. 2026-04-21T18:41:01.010000+00:00 (192h 46m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f723\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2316 records, 6 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 52 INFO, 2 NOT_TESTED, 44 PASS.
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
| DialogueEvent | 1569 | 67.75 | 1 | 6 | 1112 | 2026-04-13T17:55:01.029000+00:00 | 2026-04-21T18:41:01.010000+00:00 | 192h 45m |
| PlayerPositionEvent | 559 | 24.14 | 1 | 6 | 0 | 2026-04-13T17:54:42.823000+00:00 | 2026-04-21T18:40:51.144000+00:00 | 192h 46m |
| questEvent | 60 | 2.59 | 1 | 6 | 60 | 2026-04-13T17:55:00.993000+00:00 | 2026-04-21T18:41:00.068000+00:00 | 192h 45m |
| argumentationNodeEvent | 36 | 1.55 | 1 | 3 | 0 | 2026-04-13T18:14:09.132000+00:00 | 2026-04-21T17:40:12.307000+00:00 | 191h 26m |
| Topographic Map Event | 32 | 1.38 | 1 | 2 | 0 | 2026-04-15T18:35:06.085000+00:00 | 2026-04-21T18:08:04.939000+00:00 | 143h 32m |
| TopographicMapEvent | 32 | 1.38 | 1 | 2 | 0 | 2026-04-15T18:39:47.632000+00:00 | 2026-04-21T18:08:03.133000+00:00 | 143h 28m |
| Soil Key Puzzle | 10 | 0.43 | 1 | 3 | 0 | 2026-04-13T18:38:55.993000+00:00 | 2026-04-21T18:17:00.129000+00:00 | 191h 38m |
| argumentationEvent | 9 | 0.39 | 1 | 3 | 0 | 2026-04-13T18:13:59.442000+00:00 | 2026-04-21T17:40:14.659000+00:00 | 191h 26m |
| argumentationToolEvent | 4 | 0.17 | 1 | 1 | 0 | 2026-04-21T17:38:57.717000+00:00 | 2026-04-21T17:39:08.137000+00:00 | 10.4s |
| EndOfUnit | 3 | 0.13 | 1 | 3 | 0 | 2026-04-13T18:19:01.964000+00:00 | 2026-04-21T18:11:45.073000+00:00 | 191h 52m |
| soilMachine | 2 | 0.09 | 1 | 1 | 0 | 2026-04-21T18:34:39.292000+00:00 | 2026-04-21T18:39:28.287000+00:00 | 4m 48s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 345381.554s median 
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
  - Observed: 123.909s median 
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
  - Observed: 8.68s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.665s median 
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
  - Observed: 288.995s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 10 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 32 records this build 
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
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 36 records 
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
  - Observed: 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
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
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc907d385e3b94310f723.jsonl[533] _id=69dd32e87957a33870f26a38 ts=2026-04-13T18:16:07.1160000Z`; `69cdc907d385e3b94310f723.jsonl[937] _id=69dfdb707957a33870f46487 ts=2026-04-15T18:39:43.8030000Z`; `69cdc907d385e3b94310f723.jsonl[1166] _id=69e2708d1724f0c9e2f7400e ts=2026-04-17T17:40:28.2830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 32 records, TopographicMapEvent: 32 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1568 | 0.002 | 2.066 | 442.577 | 40.656 | 339513.164 | 0.14 | 381 | 5 |
| PlayerPositionEvent | 552 | 29.778 | 30.008 | 1256.764 | 33.122 | 339323.415 | 0.05 | 0 | 3 |
| questEvent | 59 | 0.003 | 157.267 | 11762.018 | 19010.18 | 339602.396 | 0.01 | 7 | 8 |
| argumentationNodeEvent | 35 | 1.036 | 8.68 | 19690.376 | 102969.718 | 345699.287 | 0.0 | 0 | 2 |
| Topographic Map Event | 31 | 2.934 | 15.945 | 16670.286 | 84568.09 | 345645.508 | 0.0 | 0 | 4 |
| TopographicMapEvent | 31 | 0.348 | 2.998 | 16661.145 | 84576.351 | 345600.46 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 9 | 2.978 | 123.909 | 76653.793 | 343107.987 | 345329.727 | 0.0 | 0 | 4 |
| argumentationEvent | 8 | 0.082 | 69.182 | 86146.902 | 344790.873 | 345687.042 | 0.0 | 0 | 2 |
| argumentationToolEvent | 3 | 0.128 | 2.665 | 3.473 | 7.131 | 7.627 | 17.27 | 0 | 0 |
| EndOfUnit | 2 | 345030.257 | 345381.554 | 345381.554 | 345697.722 | 345732.852 | 0.0 | 0 | 2 |
| soilMachine | 1 | 288.995 | 288.995 | 288.995 | 288.995 | 288.995 | 0.21 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.95s, p95 33.12s, n=552) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `82ms: 69cdc907d385e3b94310f723.jsonl[250] _id=69e7b67f1724f0c9e2f940d9 ts=2026-04-21T17:40:14.5770000Z ~ 69cdc907d385e3b94310f723.jsonl[249] _id=69e7b67f1724f0c9e2f940e3 ts=2026-04-21T17:40:14.6590000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 18m 
  - Evidence: 94h 18m: 69cdc907d385e3b94310f723.jsonl[1641] _id=69e27df11724f0c9e2f78972 ts=2026-04-17T18:37:36.5020000Z -> 69cdc907d385e3b94310f723.jsonl[1652] _id=69e7ac2a1724f0c9e2f91665 ts=2026-04-21T16:56:09.6660000Z; 47h 32m: 69cdc907d385e3b94310f723.jsonl[40] _id=69dd38d67957a33870f29204 ts=2026-04-13T18:41:25.6690000Z -> 69cdc907d385e3b94310f723.jsonl[41] _id=69dfd55f7957a33870f43753 ts=2026-04-15T18:13:51.4120000Z; 46h 15m: 69cdc907d385e3b94310f723.jsonl[947] _id=69dfdba77957a33870f4660d ts=2026-04-15T18:40:38.9870000Z -> 69cdc907d385e3b94310f723.jsonl[955] _id=69e2661a1724f0c9e2f721ba ts=2026-04-17T16:55:54.0550000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 381 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 69cdc907d385e3b94310f723.jsonl[1319] _id=69e274cb1724f0c9e2f75cb6 ts=2026-04-17T17:58:34.9860000Z -> 69cdc907d385e3b94310f723.jsonl[1318] _id=69e274cc1724f0c9e2f75cbd ts=2026-04-17T17:58:34.9880000Z; 3ms: 69cdc907d385e3b94310f723.jsonl[1016] _id=69e267961724f0c9e2f72cc2 ts=2026-04-17T17:02:13.6120000Z -> 69cdc907d385e3b94310f723.jsonl[1017] _id=69e267961724f0c9e2f72cc6 ts=2026-04-17T17:02:13.6150000Z; 3ms: 69cdc907d385e3b94310f723.jsonl[123] _id=69e268311724f0c9e2f732a2 ts=2026-04-17T17:04:48.5020000Z -> 69cdc907d385e3b94310f723.jsonl[1055] _id=69e268321724f0c9e2f732ad ts=2026-04-17T17:04:48.5050000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 69cdc907d385e3b94310f723.jsonl[577] _id=69dd33967957a33870f26f10 ts=2026-04-13T18:19:01.9640000Z -> 69cdc907d385e3b94310f723.jsonl[1556] _id=69e27a1b1724f0c9e2f779a0 ts=2026-04-17T18:21:14.8160000Z; 95h 50m: 69cdc907d385e3b94310f723.jsonl[1556] _id=69e27a1b1724f0c9e2f779a0 ts=2026-04-17T18:21:14.8160000Z -> 69cdc907d385e3b94310f723.jsonl[2131] _id=69e7bde11724f0c9e2f973fd ts=2026-04-21T18:11:45.0730000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 15m 
  - Evidence: 94h 15m: 69cdc907d385e3b94310f723.jsonl[1648] _id=69e27e701724f0c9e2f78c9e ts=2026-04-17T18:39:44.0640000Z -> 69cdc907d385e3b94310f723.jsonl[1650] _id=69e7abed1724f0c9e2f9158d ts=2026-04-21T16:55:07.4790000Z; 47h 32m: 69cdc907d385e3b94310f723.jsonl[701] _id=69dd38ca7957a33870f291d2 ts=2026-04-13T18:41:13.3170000Z -> 69cdc907d385e3b94310f723.jsonl[703] _id=69dfd55c7957a33870f4373d ts=2026-04-15T18:13:47.2490000Z; 46h 9m: 69cdc907d385e3b94310f723.jsonl[100] _id=69dfdced7957a33870f4670b ts=2026-04-15T18:46:04.8880000Z -> 69cdc907d385e3b94310f723.jsonl[954] _id=69e265fd1724f0c9e2f72089 ts=2026-04-17T16:55:23.9800000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 69cdc907d385e3b94310f723.jsonl[1250] _id=69e272931724f0c9e2f74e50 ts=2026-04-17T17:49:06.8360000Z -> 69cdc907d385e3b94310f723.jsonl[1916] _id=69e7b7851724f0c9e2f947b3 ts=2026-04-21T17:44:36.5630000Z; 94h 22m: 69cdc907d385e3b94310f723.jsonl[677] _id=69dd38437957a33870f28eae ts=2026-04-13T18:38:58.9710000Z -> 69cdc907d385e3b94310f723.jsonl[1013] _id=69e267831724f0c9e2f72c6e ts=2026-04-17T17:01:54.3490000Z; 46m 24s: 69cdc907d385e3b94310f723.jsonl[1012] _id=69e267861724f0c9e2f72c7a ts=2026-04-17T17:01:57.3800000Z -> 69cdc907d385e3b94310f723.jsonl[1197] _id=69e272661724f0c9e2f74d64 ts=2026-04-17T17:48:21.5190000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 69cdc907d385e3b94310f723.jsonl[1370] _id=69e2762a1724f0c9e2f764da ts=2026-04-17T18:04:25.5170000Z -> 69cdc907d385e3b94310f723.jsonl[2048] _id=69e7bc571724f0c9e2f96985 ts=2026-04-21T18:05:11.0250000Z; 46h 24m: 69cdc907d385e3b94310f723.jsonl[95] _id=69dfdbaf7957a33870f46659 ts=2026-04-15T18:40:46.4110000Z -> 69cdc907d385e3b94310f723.jsonl[1070] _id=69e2684b1724f0c9e2f73356 ts=2026-04-17T17:05:14.4330000Z; 34m 28s: 69cdc907d385e3b94310f723.jsonl[1084] _id=69e268781724f0c9e2f73495 ts=2026-04-17T17:06:00.1110000Z -> 69cdc907d385e3b94310f723.jsonl[1173] _id=69e2708d1724f0c9e2f7400c ts=2026-04-17T17:40:28.2690000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 69cdc907d385e3b94310f723.jsonl[170] _id=69e276281724f0c9e2f764ca ts=2026-04-17T18:04:23.4410000Z -> 69cdc907d385e3b94310f723.jsonl[2052] _id=69e7bc281724f0c9e2f96835 ts=2026-04-21T18:04:23.9010000Z; 46h 24m: 69cdc907d385e3b94310f723.jsonl[94] _id=69dfdbae7957a33870f46651 ts=2026-04-15T18:40:46.3330000Z -> 69cdc907d385e3b94310f723.jsonl[1071] _id=69e268541724f0c9e2f73392 ts=2026-04-17T17:05:23.5590000Z; 34m 35s: 69cdc907d385e3b94310f723.jsonl[1083] _id=69e268751724f0c9e2f73482 ts=2026-04-17T17:05:56.7500000Z -> 69cdc907d385e3b94310f723.jsonl[1169] _id=69e270911724f0c9e2f74018 ts=2026-04-17T17:40:32.2260000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 69cdc907d385e3b94310f723.jsonl[529] _id=69dd32e77957a33870f26a32 ts=2026-04-13T18:16:07.0930000Z -> 69cdc907d385e3b94310f723.jsonl[179] _id=69e2793e1724f0c9e2f774a8 ts=2026-04-17T18:17:34.1350000Z; 95h 18m: 69cdc907d385e3b94310f723.jsonl[1510] _id=69e279891724f0c9e2f7767c ts=2026-04-17T18:18:49.1990000Z -> 69cdc907d385e3b94310f723.jsonl[1821] _id=69e7b5e01724f0c9e2f93c61 ts=2026-04-21T17:37:35.7590000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 69cdc907d385e3b94310f723.jsonl[532] _id=69dd32e47957a33870f26a22 ts=2026-04-13T18:16:03.6470000Z -> 69cdc907d385e3b94310f723.jsonl[1504] _id=69e279471724f0c9e2f774e6 ts=2026-04-17T18:17:42.9340000Z; 95h 19m: 69cdc907d385e3b94310f723.jsonl[1509] _id=69e279851724f0c9e2f77661 ts=2026-04-17T18:18:44.7310000Z -> 69cdc907d385e3b94310f723.jsonl[1812] _id=69e7b5f01724f0c9e2f93cd7 ts=2026-04-21T17:37:51.4010000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 94h 20m 
  - Evidence: 94h 20m: 69cdc907d385e3b94310f723.jsonl[214] _id=69e27d5d1724f0c9e2f78594 ts=2026-04-17T18:35:08.7410000Z -> 69cdc907d385e3b94310f723.jsonl[1651] _id=69e7abf11724f0c9e2f9159d ts=2026-04-21T16:55:11.1370000Z; 47h 34m: 69cdc907d385e3b94310f723.jsonl[681] _id=69dd38617957a33870f28f60 ts=2026-04-13T18:39:29.0760000Z -> 69cdc907d385e3b94310f723.jsonl[704] _id=69dfd55e7957a33870f4374b ts=2026-04-15T18:13:49.9270000Z; 46h 21m: 69cdc907d385e3b94310f723.jsonl[79] _id=69dfda587957a33870f45ae5 ts=2026-04-15T18:35:04.4930000Z -> 69cdc907d385e3b94310f723.jsonl[964] _id=69e2663d1724f0c9e2f72332 ts=2026-04-17T16:56:28.5150000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.003s..0.009s shown 
  - Evidence: 3ms: 69cdc907d385e3b94310f723.jsonl[485] _id=69dd322d7957a33870f264c0 ts=2026-04-13T18:13:00.1170000Z -> 69cdc907d385e3b94310f723.jsonl[480] _id=69dd322d7957a33870f264c6 ts=2026-04-13T18:13:00.1200000Z; 6ms: 69cdc907d385e3b94310f723.jsonl[389] _id=69dd2f527957a33870f2525e ts=2026-04-13T18:00:49.3420000Z -> 69cdc907d385e3b94310f723.jsonl[390] _id=69dd2f527957a33870f25262 ts=2026-04-13T18:00:49.3480000Z; 9ms: 69cdc907d385e3b94310f723.jsonl[320] _id=69e7c24d1724f0c9e2f99739 ts=2026-04-21T18:30:36.4430000Z -> 69cdc907d385e3b94310f723.jsonl[2256] _id=69e7c24d1724f0c9e2f99743 ts=2026-04-21T18:30:36.4520000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc907d385e3b94310f723.jsonl:69cdc907d385e3b94310f723, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc907d385e3b94310f723.jsonl[677] _id=69dd38437957a33870f28eae ts=2026-04-13T18:38:58.9710000Z`; `69cdc907d385e3b94310f723.jsonl[1012] _id=69e267861724f0c9e2f72c7a ts=2026-04-17T17:01:57.3800000Z`; `69cdc907d385e3b94310f723.jsonl[1250] _id=69e272931724f0c9e2f74e50 ts=2026-04-17T17:49:06.8360000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 32 record(s) match the trigger in 69cdc907d385e3b94310f723.jsonl:69cdc907d385e3b94310f723, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc907d385e3b94310f723.jsonl[925] _id=69dfdb737957a33870f464a7 ts=2026-04-15T18:39:47.6320000Z`; `69cdc907d385e3b94310f723.jsonl[938] _id=69dfdb777957a33870f464cf ts=2026-04-15T18:39:50.9540000Z`; `69cdc907d385e3b94310f723.jsonl[93] _id=69dfdbae7957a33870f4664b ts=2026-04-15T18:40:45.9210000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc907d385e3b94310f723.jsonl[162] _id=69e275fa1724f0c9e2f763ae ts=2026-04-17T18:03:37.3530000Z`; `69cdc907d385e3b94310f723.jsonl[208] _id=69e27cff1724f0c9e2f783e0 ts=2026-04-17T18:33:34.6080000Z`; `69cdc907d385e3b94310f723.jsonl[216] _id=69e27d5d1724f0c9e2f78598 ts=2026-04-17T18:35:08.8120000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc907d385e3b94310f723.jsonl[249] _id=69e7b67f1724f0c9e2f940e3 ts=2026-04-21T17:40:14.6590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc907d385e3b94310f723.jsonl[2271] _id=69e7c2d41724f0c9e2f99a8d ts=2026-04-21T18:32:51.5210000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 182 unmatched 'DialogueStartEvent' (totals: 318 start, 139 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 33 start, 27 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.78s, min -6.39s, max -0.14s over 2316 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc907d385e3b94310f723\coverage.yaml

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
  - Observed: 32 records 
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

### `DialogueEvent` — 1569 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (796); Unit 3 Dev (377); Unit 1 Dev (184); Unit 4 Dev - Dungeon (102); Unit 3 Dungeon Dev (85); Unit 4 Dev (25)
- **eventKey:** present on 1112 of 1569 records
- **Intervals:** median 2.07s (p5 0.01s / p95 40.66s, n=1568)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1112; [conversationId, dialogueEventType] x457
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1569/1569 records)
    numeric range 8 .. 104 (38 unique)
data.dialogueEventType  (string, 1569/1569 records)
    "DialogueNodeEvent"  x1112
    "DialogueStartEvent"  x318
    "DialogueFinishEvent"  x139
data.nodeId  (number, 1112/1569 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 559 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (277); Unit 3 Dev (143); Unit 1 Dev (49); Unit 4 Dev - Dungeon (39); Unit 3 Dungeon Dev (32); Unit 4 Dev (19)
- **Intervals:** median 30.01s (p5 29.95s / p95 33.12s, n=552)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 559/559 records)
data.position.x  (number, 559/559 records)
    numeric range -696.267 .. 1529.32 (276 unique)
data.position.y  (number, 559/559 records)
    numeric range -113.185 .. 158.002 (190 unique)
data.position.z  (number, 559/559 records)
    numeric range -1110.34 .. 1917.03 (276 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 60 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev - Dungeon (11); Unit 3 Dungeon Dev (2); Unit 4 Dev (1)
- **eventKey:** present on 60 of 60 records
- **Intervals:** median 157.27s (p5 0.01s / p95 19010.18s, n=59)
- **`data` key-set variants:** [questEventType, questID, questName] x33; [questEventType, questID, questName, questSuccessOrFailure] x27
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 60/60 records)
    "questActiveEvent"  x33
    "questFinishEvent"  x27
data.questID  (string, 60/60 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 60/60 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 27/60 records)
    "Succeeded"  x27
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 36 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (18); Unit 3 Dev (13); Unit 2 Prod (Refactor) (5)
- **Intervals:** median 8.68s (p5 1.47s / p95 102969.72s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "argumentationNodeAdd"  x23
    "argumentationNodeRemove"  x13
data.argumentationTitle  (string, 36/36 records)
    "Unit 3 - Pollution Upstream"  x13
    "Unit 1 - Freshwater"  x11
    "Unit 1 - Argumentation Tutorial"  x7
    "Unit 2 – Watershed"  x5
data.nodeName  (string, 36/36 records)
    "1"  x11
    "B"  x7
    "A"  x6
    "I"  x4
    "II"  x3
    "2"  x2
    "3"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Topographic Map Event` — 32 records

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (12)
- **Intervals:** median 15.95s (p5 5.42s / p95 84568.09s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "MapCloseEvent"  x16
    "MapOpenEvent"  x16
data.featureUsed  (string, 32/32 records)
    "Map"  x32
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 32 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (8)
- **Intervals:** median 3.00s (p5 0.43s / p95 84576.35s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "dragEnd"  x16
    "dragStart"  x16
data.featureUsed  (string, 32/32 records)
    "waypoint"  x32
data.location  (object, 32/32 records)
data.location.x  (number, 32/32 records)
    numeric range -800.544 .. 128.903 (17 unique)
data.location.y  (number, 32/32 records)
    numeric range -308.817 .. 126.153 (17 unique)
data.location.z  (number, 32/32 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 10 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 123.91s (p5 3.00s / p95 343107.99s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/10 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/10 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 69.18s (p5 5.43s / p95 344790.87s, n=8)
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

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 2.67s (p5 0.38s / p95 7.13s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Pollution Site Data"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 345381.55s (p5 345065.39s / p95 345697.72s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `soilMachine` — 2 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (2)
- **Intervals:** median 289.00s (p5 289.00s / p95 289.00s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "ChangeCanister"  x2
data.canisterType  (string, 2/2 records)
    "Gravel"  x1
    "Sand"  x1
data.floor  (string, 2/2 records)
    "3"  x1
    "4"  x1
data.machine  (string, 2/2 records)
    "1"  x2
data.row  (string, 2/2 records)
    "TopRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (16x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (13x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*