# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba1

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba1
- **Game version string(s) in log:** 2.9.0, 2.9.1, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba1.jsonl
- **Records:** 8987 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba1
- **Time span:** 2026-10-06T19:35:58.945000+00:00 .. 2026-10-18T16:34:51.085000+00:00 (284h 58m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba1\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 8987 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 90 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2175 | 24.2 | 1 | 9 | 1359 | 2026-10-06T19:36:31.171000+00:00 | 2026-10-18T16:34:45.757000+00:00 | 284h 58m |
| PuzzlePieceVisibleEvent | 2113 | 23.51 | 1 | 4 | 0 | 2026-10-07T19:49:21.355000+00:00 | 2026-10-18T16:03:01.883000+00:00 | 260h 13m |
| PlayerPositionEvent | 1870 | 20.81 | 1 | 9 | 0 | 2026-10-06T19:36:10.415000+00:00 | 2026-10-18T16:34:41.718000+00:00 | 284h 58m |
| InputEvent | 1794 | 19.96 | 1 | 9 | 0 | 2026-10-06T19:40:05.796000+00:00 | 2026-10-18T16:34:51.085000+00:00 | 284h 54m |
| argumentationNodeEvent | 465 | 5.17 | 1 | 5 | 0 | 2026-10-06T20:00:59.780000+00:00 | 2026-10-18T16:21:39.871000+00:00 | 284h 20m |
| ObjectInterEvent | 216 | 2.4 | 1 | 9 | 0 | 2026-10-06T19:42:49.402000+00:00 | 2026-10-18T16:34:51.085000+00:00 | 284h 52m |
| questEvent | 81 | 0.9 | 1 | 9 | 81 | 2026-10-06T19:36:31.141000+00:00 | 2026-10-18T16:30:27.175000+00:00 | 284h 53m |
| Soil Key Puzzle | 58 | 0.65 | 1 | 3 | 0 | 2026-10-08T19:56:39.548000+00:00 | 2026-10-15T19:34:34.154000+00:00 | 167h 37m |
| TopographicMapEvent | 49 | 0.55 | 1 | 2 | 0 | 2026-10-07T19:50:17.649000+00:00 | 2026-10-14T20:48:13.270000+00:00 | 168h 57m |
| DEBUGMenu | 41 | 0.46 | 1 | 9 | 0 | 2026-10-06T19:35:58.945000+00:00 | 2026-10-18T15:53:34.797000+00:00 | 284h 17m |
| argumentationAnswerEvent | 23 | 0.26 | 1 | 5 | 0 | 2026-10-06T20:01:21.987000+00:00 | 2026-10-18T16:21:43.700000+00:00 | 284h 20m |
| WaterChamberEvent | 20 | 0.22 | 1 | 1 | 0 | 2026-10-18T16:01:52.080000+00:00 | 2026-10-18T16:13:43.728000+00:00 | 11m 51s |
| argumentationEvent | 19 | 0.21 | 1 | 5 | 0 | 2026-10-06T20:00:54.752000+00:00 | 2026-10-18T16:21:43.739000+00:00 | 284h 20m |
| gameStartEvent | 17 | 0.19 | 1 | 1 | 0 | 2026-10-06T19:35:59.337000+00:00 | 2026-10-18T15:53:26.929000+00:00 | 284h 17m |
| gameWindowFocusEvent | 17 | 0.19 | 1 | 1 | 0 | 2026-10-06T19:35:59.337000+00:00 | 2026-10-18T15:53:26.928000+00:00 | 284h 17m |
| TerasGardenBox | 6 | 0.07 | 1 | 1 | 0 | 2026-10-18T15:40:01.136000+00:00 | 2026-10-18T15:41:02.808000+00:00 | 1m 1s |
| gameWindowUnfocusEvent | 6 | 0.07 | 1 | 3 | 0 | 2026-10-06T20:10:43.148000+00:00 | 2026-10-15T20:12:18.567000+00:00 | 216h 1m |
| EndOfUnit | 5 | 0.06 | 1 | 5 | 0 | 2026-10-06T20:08:02.743000+00:00 | 2026-10-18T16:34:51.059000+00:00 | 284h 26m |
| SolarStillDesignEvent | 5 | 0.06 | 1 | 1 | 0 | 2026-10-18T16:27:48.472000+00:00 | 2026-10-18T16:28:03.473000+00:00 | 15.0s |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T20:00:54.706000+00:00 | 2026-10-06T20:01:01.562000+00:00 | 6.9s |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-18T15:53:34.564000+00:00 | 2026-10-18T16:14:47.797000+00:00 | 21m 13s |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |
| soilMachine | 1 | 0.01 | 1 | 1 | 0 | 2026-10-15T19:57:26.711000+00:00 | 2026-10-15T19:57:26.711000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 389.606s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 208392.028s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 2.325s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 20.116s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.073s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 15.805s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 30.376s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 6.856s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 9791.953s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 9791.953s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86387.295s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.4x vs baseline. 
  - Observed: 41 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Sprint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: s 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Switch Canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointMoveEvent; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.6x vs baseline. 
  - Observed: 23 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,II; A,B,C,2,II; A,B,D,2,II; A,C,2,II; A,C,4,II; B,2,II; B,5,I; C,2,II; C,3,II; C,A,2,II; C,B,A,2,II; C,D,3,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 465 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[6] _id=6ac54d9fde269131f9b7a6d6 ts=2026-10-06T19:35:59.3370000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[619] _id=6ac55583de269131f9b84c6c ts=2026-10-06T20:09:39.4290000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[634] _id=6ac69f2dde269131f9bf21da ts=2026-10-07T19:36:12.3160000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[5] _id=6ac54d9fde269131f9b7a6d5 ts=2026-10-06T19:35:59.3370000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[618] _id=6ac55583de269131f9b84c6b ts=2026-10-06T20:09:39.4290000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[633] _id=6ac69f2dde269131f9bf21d9 ts=2026-10-07T19:36:12.3160000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[631] _id=6ac555c4de269131f9b85235 ts=2026-10-06T20:10:43.1480000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[635] _id=6ac6a13bde269131f9bf36ce ts=2026-10-07T19:44:58.7080000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[3020] _id=6ace872dde269131f9d1f785 ts=2026-10-13T19:31:56.4930000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2174 | 0.0 | 3.841 | 471.893 | 31.856 | 429811.741 | 0.13 | 632 | 9 |
| PuzzlePieceVisibleEvent | 2112 | 0.0 | 0.073 | 443.57 | 2.982 | 429780.535 | 0.14 | 887 | 6 |
| PlayerPositionEvent | 1856 | 9.81 | 10.002 | 424.929 | 10.129 | 429478.397 | 0.14 | 0 | 7 |
| InputEvent | 1793 | 0.0 | 2.325 | 572.05 | 32.419 | 429758.504 | 0.1 | 13 | 10 |
| argumentationNodeEvent | 464 | 0.005 | 0.923 | 2206.121 | 10.616 | 604592.081 | 0.03 | 38 | 7 |
| ObjectInterEvent | 215 | 0.0 | 20.116 | 4769.868 | 668.932 | 430041.361 | 0.01 | 9 | 12 |
| questEvent | 80 | 0.0 | 228.53 | 12820.45 | 83759.13 | 429513.651 | 0.0 | 13 | 13 |
| Soil Key Puzzle | 57 | 0.305 | 1.292 | 10587.274 | 15.118 | 517893.419 | 0.01 | 0 | 2 |
| TopographicMapEvent | 48 | 0.022 | 15.805 | 12672.409 | 56299.836 | 431337.494 | 0.0 | 2 | 5 |
| DEBUGMenu | 40 | 7.429 | 389.606 | 25586.396 | 88966.181 | 431364.859 | 0.0 | 0 | 16 |
| argumentationAnswerEvent | 22 | 2.861 | 30.376 | 46528.26 | 152867.722 | 604690.266 | 0.0 | 0 | 7 |
| WaterChamberEvent | 19 | 4.103 | 26.41 | 37.455 | 83.959 | 117.695 | 1.6 | 0 | 0 |
| argumentationEvent | 18 | 0.03 | 103.655 | 56869.388 | 223488.56 | 604585.117 | 0.0 | 3 | 7 |
| gameStartEvent | 16 | 255.33 | 9791.953 | 63965.475 | 224990.358 | 431381.856 | 0.0 | 0 | 12 |
| gameWindowFocusEvent | 16 | 255.33 | 9791.953 | 63965.474 | 224990.358 | 431381.856 | 0.0 | 0 | 12 |
| TerasGardenBox | 5 | 1.828 | 2.488 | 12.334 | 28.231 | 28.684 | 4.86 | 0 | 0 |
| gameWindowUnfocusEvent | 5 | 2362.326 | 86387.295 | 155539.084 | 431388.719 | 517617.785 | 0.0 | 0 | 5 |
| EndOfUnit | 4 | 2503.46 | 208392.028 | 256002.079 | 563136.457 | 604720.801 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 4 | 2.333 | 3.283 | 3.75 | 5.705 | 6.102 | 16.0 | 0 | 0 |
| argumentationToolEvent | 1 | 6.856 | 6.856 | 6.856 | 6.856 | 6.856 | 8.75 | 0 | 0 |
| chatEvent | 1 | 1273.233 | 1273.233 | 1273.233 | 1273.233 | 1273.233 | 0.05 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| soilMachine | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[6818] _id=6ad24a28de269131f9e57d6e ts=2026-10-16T16:00:39.1460000Z == 6ab9a9439a8420a1e6b56ba1.jsonl[6819] _id=6ad24a28de269131f9e57d6f ts=2026-10-16T16:00:39.1460000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 35 group(s), 52 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[822] _id=6ac6a2b9de269131f9bf4b84 ts=2026-10-07T19:51:19.7520000Z == 6ab9a9439a8420a1e6b56ba1.jsonl[823] _id=6ac6a2b9de269131f9bf4b88 ts=2026-10-07T19:51:19.7520000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[854] _id=6ac6a2bfde269131f9bf4be0 ts=2026-10-07T19:51:24.1630000Z == 6ab9a9439a8420a1e6b56ba1.jsonl[855] _id=6ac6a2bfde269131f9bf4be4 ts=2026-10-07T19:51:24.1630000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[858] _id=6ac6a2bfde269131f9bf4bee ts=2026-10-07T19:51:24.2840000Z == 6ab9a9439a8420a1e6b56ba1.jsonl[861] _id=6ac6a2c0de269131f9bf4bf6 ts=2026-10-07T19:51:24.2840000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[8778] _id=6ad4f25fde269131f9e8b01f ts=2026-10-18T16:22:54.8570000Z == 6ab9a9439a8420a1e6b56ba1.jsonl[8779] _id=6ad4f25fde269131f9e8b020 ts=2026-10-18T16:22:54.8570000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9439a8420a1e6b56ba1.jsonl[139] _id=6ac54f39de269131f9b7b009 ts=2026-10-06T19:42:49.4020000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[134] _id=6ac54f3ade269131f9b7b00e ts=2026-10-06T19:42:49.4060000Z`; `832ms: 6ab9a9439a8420a1e6b56ba1.jsonl[721] _id=6ac6a126de269131f9bf3466 ts=2026-10-07T19:44:38.1080000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[722] _id=6ac6a127de269131f9bf3483 ts=2026-10-07T19:44:38.9400000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6ab9a9439a8420a1e6b56ba1.jsonl[4365] _id=6acfdbbdde269131f9d90cac ts=2026-10-14T19:45:00.9950000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[4368] _id=6acfdbbdde269131f9d90caf ts=2026-10-14T19:45:01.0250000Z`; `34ms: 6ab9a9439a8420a1e6b56ba1.jsonl[7417] _id=6ad284c9de269131f9e802ac ts=2026-10-16T20:10:49.0930000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[7420] _id=6ad284c9de269131f9e802af ts=2026-10-16T20:10:49.1270000Z`; `39ms: 6ab9a9439a8420a1e6b56ba1.jsonl[7614] _id=6ad4e741de269131f9e8a80b ts=2026-10-18T15:35:29.1320000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[7617] _id=6ad4e741de269131f9e8a80e ts=2026-10-18T15:35:29.1710000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1000ms: 6ab9a9439a8420a1e6b56ba1.jsonl[3689] _id=6ace8dfbde269131f9d241d0 ts=2026-10-13T20:00:58.5560000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[3696] _id=6ace8dfcde269131f9d241d8 ts=2026-10-13T20:00:59.5560000Z`; `945ms: 6ab9a9439a8420a1e6b56ba1.jsonl[3706] _id=6ace8e0fde269131f9d24232 ts=2026-10-13T20:01:18.4530000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[3708] _id=6ace8e10de269131f9d2423a ts=2026-10-13T20:01:19.3980000Z`; `996ms: 6ab9a9439a8420a1e6b56ba1.jsonl[3720] _id=6ace8e3bde269131f9d24324 ts=2026-10-13T20:02:02.9970000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[3731] _id=6ace8e3cde269131f9d2432e ts=2026-10-13T20:02:03.9930000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba1.jsonl[8896] _id=6ad4f3dade269131f9e8b103 ts=2026-10-18T16:29:13.3530000Z ~ 6ab9a9439a8420a1e6b56ba1.jsonl[8889] _id=6ad4f3dade269131f9e8b105 ts=2026-10-18T16:29:13.3580000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a9439a8420a1e6b56ba1.jsonl[1669] _id=6ac7f15dde269131f9c6ae06 ts=2026-10-08T19:39:09.2220000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2636] _id=6ace8662de269131f9d1ec97 ts=2026-10-13T19:28:34.0810000Z; 43h 16m: 6ab9a9439a8420a1e6b56ba1.jsonl[7425] _id=6ad284fcde269131f9e80427 ts=2026-10-16T20:11:40.3110000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7473] _id=6ad4e58bde269131f9e8a697 ts=2026-10-18T15:28:10.5620000Z; 23h 44m: 6ab9a9439a8420a1e6b56ba1.jsonl[968] _id=6ac6a384de269131f9bf5311 ts=2026-10-07T19:54:43.2830000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1666] _id=6ac7f14cde269131f9c6acfb ts=2026-10-08T19:38:52.4080000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a9439a8420a1e6b56ba1.jsonl[2623] _id=6ac7f8dbde269131f9c74766 ts=2026-10-08T20:11:07.4240000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3126] _id=6ace87d0de269131f9d1fe7e ts=2026-10-13T19:34:39.1650000Z; 43h 15m: 6ab9a9439a8420a1e6b56ba1.jsonl[7472] _id=6ad28539de269131f9e804a1 ts=2026-10-16T20:12:41.3620000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7505] _id=6ad4e595de269131f9e8a6a1 ts=2026-10-18T15:28:21.2330000Z; 23h 34m: 6ab9a9439a8420a1e6b56ba1.jsonl[1621] _id=6ac6a659de269131f9bf8021 ts=2026-10-07T20:06:48.2060000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1692] _id=6ac7f1c8de269131f9c6b5e0 ts=2026-10-08T19:40:56.5870000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 632 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6950] _id=6ad24b4ade269131f9e5911d ts=2026-10-16T16:05:29.4990000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6951] _id=6ad24b4ade269131f9e5911e ts=2026-10-16T16:05:29.4990000Z; 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6963] _id=6ad24b57de269131f9e591d8 ts=2026-10-16T16:05:42.1860000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6964] _id=6ad24b57de269131f9e591d9 ts=2026-10-16T16:05:42.1860000Z; 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6983] _id=6ad24b75de269131f9e593e6 ts=2026-10-16T16:06:12.1190000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6984] _id=6ad24b75de269131f9e593e7 ts=2026-10-16T16:06:12.1190000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 58m 
  - Evidence: 167h 58m: 6ab9a9439a8420a1e6b56ba1.jsonl[617] _id=6ac55523de269131f9b8412b ts=2026-10-06T20:08:02.7430000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3820] _id=6ace8f54de269131f9d24e30 ts=2026-10-13T20:06:43.5440000Z; 90h 58m: 6ab9a9439a8420a1e6b56ba1.jsonl[5444] _id=6acfec20de269131f9d96a8c ts=2026-10-14T20:54:55.7590000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7994] _id=6ad4eb64de269131f9e8aa5b ts=2026-10-18T15:53:07.5990000Z; 24h 48m: 6ab9a9439a8420a1e6b56ba1.jsonl[3820] _id=6ace8f54de269131f9d24e30 ts=2026-10-13T20:06:43.5440000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[5444] _id=6acfec20de269131f9d96a8c ts=2026-10-14T20:54:55.7590000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9439a8420a1e6b56ba1.jsonl[2551] _id=6ac7f7d2de269131f9c735fb ts=2026-10-08T20:06:42.4350000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2661] _id=6ace8691de269131f9d1ef64 ts=2026-10-13T19:29:20.9390000Z; 43h 21m: 6ab9a9439a8420a1e6b56ba1.jsonl[7327] _id=6ad28429de269131f9e7fd58 ts=2026-10-16T20:08:08.7360000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7509] _id=6ad4e5c5de269131f9e8a6b1 ts=2026-10-18T15:29:09.1130000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba1.jsonl[622] _id=6ac55590de269131f9b84d9f ts=2026-10-06T20:09:50.3490000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[645] _id=6ac6a042de269131f9bf26c7 ts=2026-10-07T19:40:47.6440000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6818] _id=6ad24a28de269131f9e57d6e ts=2026-10-16T16:00:39.1460000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6819] _id=6ad24a28de269131f9e57d6f ts=2026-10-16T16:00:39.1460000Z; 3ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6812] _id=6ad24a28de269131f9e57d6b ts=2026-10-16T16:00:39.0730000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6813] _id=6ad24a28de269131f9e57d6d ts=2026-10-16T16:00:39.0760000Z; 4ms: 6ab9a9439a8420a1e6b56ba1.jsonl[3426] _id=6ace8bb1de269131f9d22d1f ts=2026-10-13T19:51:12.5800000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3427] _id=6ace8bb1de269131f9d22d21 ts=2026-10-13T19:51:12.5840000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a9439a8420a1e6b56ba1.jsonl[2342] _id=6ac7f6dfde269131f9c720ea ts=2026-10-08T20:02:39.1590000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2763] _id=6ace86b9de269131f9d1f185 ts=2026-10-13T19:30:00.5200000Z; 43h 21m: 6ab9a9439a8420a1e6b56ba1.jsonl[7322] _id=6ad2842ade269131f9e7fd5f ts=2026-10-16T20:08:09.9950000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7524] _id=6ad4e5e6de269131f9e8a6d4 ts=2026-10-18T15:29:41.6130000Z; 23h 54m: 6ab9a9439a8420a1e6b56ba1.jsonl[1285] _id=6ac6a53fde269131f9bf6d41 ts=2026-10-07T20:02:06.6340000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1998] _id=6ac7f577de269131f9c6fa12 ts=2026-10-08T19:56:39.5580000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6561] _id=6ad13298de269131f9e115fb ts=2026-10-15T20:07:52.1770000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6562] _id=6ad13298de269131f9e115fc ts=2026-10-15T20:07:52.1770000Z; 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6611] _id=6ad132f1de269131f9e11c85 ts=2026-10-15T20:09:21.0990000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6612] _id=6ad132f1de269131f9e11c86 ts=2026-10-15T20:09:21.0990000Z; 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6787] _id=6ad24a06de269131f9e57b56 ts=2026-10-16T16:00:01.6510000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6788] _id=6ad24a06de269131f9e57b57 ts=2026-10-16T16:00:01.6510000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a9439a8420a1e6b56ba1.jsonl[2621] _id=6ac7f8dbde269131f9c74764 ts=2026-10-08T20:11:06.8270000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2638] _id=6ace8687de269131f9d1ee91 ts=2026-10-13T19:29:05.2240000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba1.jsonl[630] _id=6ac555c1de269131f9b85209 ts=2026-10-06T20:10:40.7260000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[644] _id=6ac6a042de269131f9bf26c6 ts=2026-10-07T19:40:43.1350000Z; 23h 29m: 6ab9a9439a8420a1e6b56ba1.jsonl[1662] _id=6ac6a700de269131f9bf8aae ts=2026-10-07T20:09:36.0630000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1670] _id=6ac7f161de269131f9c6ae56 ts=2026-10-08T19:39:09.2360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a9439a8420a1e6b56ba1.jsonl[2533] _id=6ac7f7b2de269131f9c732e5 ts=2026-10-08T20:06:09.8650000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2628] _id=6ace8688de269131f9d1ee94 ts=2026-10-13T19:29:10.4000000Z; 67h 52m: 6ab9a9439a8420a1e6b56ba1.jsonl[6391] _id=6ad13113de269131f9e0fc40 ts=2026-10-15T20:01:21.7580000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[8005] _id=6ad4eb86de269131f9e8aa6a ts=2026-10-18T15:53:41.1380000Z; 24h 17m: 6ab9a9439a8420a1e6b56ba1.jsonl[3107] _id=6ace87a5de269131f9d1fca5 ts=2026-10-13T19:33:55.8380000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[4525] _id=6acfdd23de269131f9d91eb3 ts=2026-10-14T19:50:57.9390000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 887 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[1050] _id=6ac6a444de269131f9bf5c2f ts=2026-10-07T19:57:39.5840000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1051] _id=6ac6a444de269131f9bf5c31 ts=2026-10-07T19:57:39.5840000Z; 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[1055] _id=6ac6a443de269131f9bf5c10 ts=2026-10-07T19:57:39.0360000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1064] _id=6ac6a443de269131f9bf5c18 ts=2026-10-07T19:57:39.0360000Z; 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[1059] _id=6ac6a445de269131f9bf5c4a ts=2026-10-07T19:57:40.4250000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1077] _id=6ac6a445de269131f9bf5c4c ts=2026-10-07T19:57:40.4250000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 51m 
  - Evidence: 143h 51m: 6ab9a9439a8420a1e6b56ba1.jsonl[2022] _id=6ac7f5c3de269131f9c6ff38 ts=2026-10-08T19:57:55.2260000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[4472] _id=6acfdcc9de269131f9d918fb ts=2026-10-14T19:49:28.6450000Z; 23h 43m: 6ab9a9439a8420a1e6b56ba1.jsonl[4500] _id=6acfdcefde269131f9d91bff ts=2026-10-14T19:50:06.8930000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[5536] _id=6ad12aa7de269131f9e08078 ts=2026-10-15T19:33:59.6030000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9439a8420a1e6b56ba1.jsonl[1953] _id=6ac7f51ade269131f9c6f44f ts=2026-10-08T19:55:06.7750000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3284] _id=6ace8a05de269131f9d21696 ts=2026-10-13T19:44:04.2690000Z; 23h 45m: 6ab9a9439a8420a1e6b56ba1.jsonl[1019] _id=6ac6a418de269131f9bf5a4e ts=2026-10-07T19:57:11.8380000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1728] _id=6ac7f221de269131f9c6bf7c ts=2026-10-08T19:42:25.6250000Z; 23h 42m: 6ab9a9439a8420a1e6b56ba1.jsonl[3289] _id=6ace8a14de269131f9d21736 ts=2026-10-13T19:44:19.3340000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3875] _id=6acfd76bde269131f9d8a99a ts=2026-10-14T19:26:34.7930000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.029s shown 
  - Evidence: 22ms: 6ab9a9439a8420a1e6b56ba1.jsonl[1733] _id=6ac7f231de269131f9c6c05e ts=2026-10-08T19:42:41.7140000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1737] _id=6ac7f231de269131f9c6c062 ts=2026-10-08T19:42:41.7360000Z; 29ms: 6ab9a9439a8420a1e6b56ba1.jsonl[1732] _id=6ac7f231de269131f9c6c05c ts=2026-10-08T19:42:41.6850000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1733] _id=6ac7f231de269131f9c6c05e ts=2026-10-08T19:42:41.7140000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 167h 58m 
  - Evidence: 167h 58m: 6ab9a9439a8420a1e6b56ba1.jsonl[503] _id=6ac5544ede269131f9b82414 ts=2026-10-06T20:04:30.0480000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3673] _id=6ace8e61de269131f9d2448b ts=2026-10-13T20:02:40.3140000Z; 43h 24m: 6ab9a9439a8420a1e6b56ba1.jsonl[7416] _id=6ad284c9de269131f9e802a8 ts=2026-10-16T20:10:49.0760000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7685] _id=6ad4e741de269131f9e8a809 ts=2026-10-18T15:35:29.1150000Z; 24h 27m: 6ab9a9439a8420a1e6b56ba1.jsonl[4334] _id=6acfdbbdde269131f9d90ca6 ts=2026-10-14T19:45:00.9800000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6712] _id=6ad1339ede269131f9e1213d ts=2026-10-15T20:12:14.6780000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 167h 56m 
  - Evidence: 167h 56m: 6ab9a9439a8420a1e6b56ba1.jsonl[504] _id=6ac5544ede269131f9b8241a ts=2026-10-06T20:04:30.0770000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3693] _id=6ace8df7de269131f9d241c1 ts=2026-10-13T20:00:55.1940000Z; 43h 23m: 6ab9a9439a8420a1e6b56ba1.jsonl[7420] _id=6ad284c9de269131f9e802af ts=2026-10-16T20:10:49.1270000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7654] _id=6ad4e716de269131f9e8a7c2 ts=2026-10-18T15:34:45.3540000Z; 24h 26m: 6ab9a9439a8420a1e6b56ba1.jsonl[4368] _id=6acfdbbdde269131f9d90caf ts=2026-10-14T19:45:01.0250000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6676] _id=6ad13370de269131f9e120a2 ts=2026-10-15T20:11:28.6510000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.030s..0.039s shown 
  - Evidence: 30ms: 6ab9a9439a8420a1e6b56ba1.jsonl[4365] _id=6acfdbbdde269131f9d90cac ts=2026-10-14T19:45:00.9950000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[4368] _id=6acfdbbdde269131f9d90caf ts=2026-10-14T19:45:01.0250000Z; 34ms: 6ab9a9439a8420a1e6b56ba1.jsonl[7417] _id=6ad284c9de269131f9e802ac ts=2026-10-16T20:10:49.0930000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7420] _id=6ad284c9de269131f9e802af ts=2026-10-16T20:10:49.1270000Z; 39ms: 6ab9a9439a8420a1e6b56ba1.jsonl[7614] _id=6ad4e741de269131f9e8a80b ts=2026-10-18T15:35:29.1320000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7617] _id=6ad4e741de269131f9e8a80e ts=2026-10-18T15:35:29.1710000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 167h 56m 
  - Evidence: 167h 56m: 6ab9a9439a8420a1e6b56ba1.jsonl[501] _id=6ac5544bde269131f9b82377 ts=2026-10-06T20:04:26.4750000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3689] _id=6ace8dfbde269131f9d241d0 ts=2026-10-13T20:00:58.5560000Z; 43h 23m: 6ab9a9439a8420a1e6b56ba1.jsonl[7415] _id=6ad284c8de269131f9e80299 ts=2026-10-16T20:10:47.7290000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7639] _id=6ad4e70ede269131f9e8a7b8 ts=2026-10-18T15:34:37.6900000Z; 24h 26m: 6ab9a9439a8420a1e6b56ba1.jsonl[4363] _id=6acfdbbbde269131f9d90c95 ts=2026-10-14T19:44:59.3540000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6675] _id=6ad1336dde269131f9e1208d ts=2026-10-15T20:11:25.2140000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.005s..0.014s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6923] _id=6ad24b25de269131f9e58e7e ts=2026-10-16T16:04:52.5390000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6924] _id=6ad24b25de269131f9e58e88 ts=2026-10-16T16:04:52.5440000Z; 5ms: 6ab9a9439a8420a1e6b56ba1.jsonl[8695] _id=6ad4f1fdde269131f9e8af98 ts=2026-10-18T16:21:16.4860000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[8711] _id=6ad4f1fdde269131f9e8af9a ts=2026-10-18T16:21:16.4910000Z; 14ms: 6ab9a9439a8420a1e6b56ba1.jsonl[6928] _id=6ad24b2bde269131f9e58f17 ts=2026-10-16T16:04:58.6650000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6929] _id=6ad24b2bde269131f9e58f18 ts=2026-10-16T16:04:58.6790000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21m 13s 
  - Evidence: 21m 13s: 6ab9a9439a8420a1e6b56ba1.jsonl[7986] _id=6ad4eb7fde269131f9e8aa64 ts=2026-10-18T15:53:34.5640000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[8552] _id=6ad4f078de269131f9e8ae7f ts=2026-10-18T16:14:47.7970000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a9439a8420a1e6b56ba1.jsonl[1668] _id=6ac7f14cde269131f9c6ad02 ts=2026-10-08T19:38:52.5640000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2635] _id=6ace8663de269131f9d1ec9c ts=2026-10-13T19:28:34.4200000Z; 43h 23m: 6ab9a9439a8420a1e6b56ba1.jsonl[7183] _id=6ad28369de269131f9e7fa56 ts=2026-10-16T20:04:57.5290000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7481] _id=6ad4e58bde269131f9e8a69a ts=2026-10-18T15:28:10.7210000Z; 23h 44m: 6ab9a9439a8420a1e6b56ba1.jsonl[965] _id=6ac6a36ede269131f9bf5257 ts=2026-10-07T19:54:21.8560000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1668] _id=6ac7f14cde269131f9c6ad02 ts=2026-10-08T19:38:52.5640000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a9439a8420a1e6b56ba1.jsonl[1667] _id=6ac7f14cde269131f9c6ad01 ts=2026-10-08T19:38:52.5640000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2634] _id=6ace8663de269131f9d1ec9b ts=2026-10-13T19:28:34.4200000Z; 43h 23m: 6ab9a9439a8420a1e6b56ba1.jsonl[7182] _id=6ad28369de269131f9e7fa55 ts=2026-10-16T20:04:57.5290000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7480] _id=6ad4e58bde269131f9e8a699 ts=2026-10-18T15:28:10.7210000Z; 23h 44m: 6ab9a9439a8420a1e6b56ba1.jsonl[964] _id=6ac6a36ede269131f9bf5256 ts=2026-10-07T19:54:21.8560000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[1667] _id=6ac7f14cde269131f9c6ad01 ts=2026-10-08T19:38:52.5640000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 46m 
  - Evidence: 143h 46m: 6ab9a9439a8420a1e6b56ba1.jsonl[635] _id=6ac6a13bde269131f9bf36ce ts=2026-10-07T19:44:58.7080000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[3020] _id=6ace872dde269131f9d1f785 ts=2026-10-13T19:31:56.4930000Z; 24h 1m: 6ab9a9439a8420a1e6b56ba1.jsonl[3865] _id=6acfd746de269131f9d8a63c ts=2026-10-13T20:11:18.819Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[5303] _id=6acfe9dcde269131f9d96870 ts=2026-10-14T20:12:31.272Z; 23h 59m: 6ab9a9439a8420a1e6b56ba1.jsonl[5303] _id=6acfe9dcde269131f9d96870 ts=2026-10-14T20:12:31.272Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[6721] _id=6ad24980de269131f9e5720b ts=2026-10-15T20:12:18.567Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a9439a8420a1e6b56ba1.jsonl[2619] _id=6ac7f8bcde269131f9c74649 ts=2026-10-08T20:10:36.7580000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[2627] _id=6ace8687de269131f9d1ee92 ts=2026-10-13T19:29:10.4090000Z; 43h 17m: 6ab9a9439a8420a1e6b56ba1.jsonl[7428] _id=6ad284e0de269131f9e80335 ts=2026-10-16T20:11:11.8730000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[7476] _id=6ad4e595de269131f9e8a69f ts=2026-10-18T15:28:20.0660000Z; 23h 35m: 6ab9a9439a8420a1e6b56ba1.jsonl[594] _id=6ac554fade269131f9b83aef ts=2026-10-06T20:07:21.8200000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[673] _id=6ac6a0c1de269131f9bf2c6b ts=2026-10-07T19:42:56.3910000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba1.jsonl[8778] _id=6ad4f25fde269131f9e8b01f ts=2026-10-18T16:22:54.8570000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[8779] _id=6ad4f25fde269131f9e8b020 ts=2026-10-18T16:22:54.8570000Z; 1ms: 6ab9a9439a8420a1e6b56ba1.jsonl[414] _id=6ac55325de269131f9b7f932 ts=2026-10-06T19:59:32.6640000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[416] _id=6ac55325de269131f9b7f933 ts=2026-10-06T19:59:32.6650000Z; 5ms: 6ab9a9439a8420a1e6b56ba1.jsonl[8896] _id=6ad4f3dade269131f9e8b103 ts=2026-10-18T16:29:13.3530000Z -> 6ab9a9439a8420a1e6b56ba1.jsonl[8889] _id=6ad4f3dade269131f9e8b105 ts=2026-10-18T16:29:13.3580000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[394] _id=6ac552fdde269131f9b7f10d ts=2026-10-06T19:58:52.8090000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[513] _id=6ac55466de269131f9b82851 ts=2026-10-06T20:04:54.2580000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[1826] _id=6ac7f385de269131f9c6d902 ts=2026-10-08T19:48:20.8660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[959] _id=6ac6a36ede269131f9bf5250 ts=2026-10-07T19:52:04.905Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[960] _id=6ac6a36ede269131f9bf5251 ts=2026-10-07T19:52:04.922Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[961] _id=6ac6a36ede269131f9bf5252 ts=2026-10-07T19:52:04.959Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[4368] _id=6acfdbbdde269131f9d90caf ts=2026-10-14T19:45:01.0250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[7986] _id=6ad4eb7fde269131f9e8aa64 ts=2026-10-18T15:53:34.5640000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[8552] _id=6ad4f078de269131f9e8ae7f ts=2026-10-18T16:14:47.7970000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[9] _id=6ac54db8de269131f9b7a736 ts=?`; `6ab9a9439a8420a1e6b56ba1.jsonl[2625] _id=6ace8687de269131f9d1ee8d ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 51 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[2267] _id=6ac7f6c9de269131f9c71eb5 ts=2026-10-08T20:02:16.7380000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[2269] _id=6ac7f6c9de269131f9c71ec0 ts=2026-10-08T20:02:16.8260000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[2281] _id=6ac7f6cdde269131f9c71f2f ts=2026-10-08T20:02:20.3870000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 161 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[823] _id=6ac6a2b9de269131f9bf4b88 ts=2026-10-07T19:51:19.7520000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[827] _id=6ac6a2b9de269131f9bf4b8a ts=2026-10-07T19:51:19.7520000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[824] _id=6ac6a2bade269131f9bf4b90 ts=2026-10-07T19:51:19.7520000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[6877] _id=6ad24acfde269131f9e5888e ts=2026-10-16T16:03:26.4140000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[7353] _id=6ad28483de269131f9e7ff79 ts=2026-10-16T20:09:39.1770000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[7654] _id=6ad4e716de269131f9e8a7c2 ts=2026-10-18T15:34:45.3540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 DEBUGMenu record in 'Unit 2 Prod (Refactor)' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[637] _id=6ac69f43de269131f9bf2210 ts=2026-10-07T19:36:33.7600000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 412 start, 404 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 21 unmatched 'BecameVisible' (totals: 638 open, 621 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 48 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 131 of 8984 adjacent _id pairs reverse in client time; worst 148.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba1.jsonl[882] _id=6ac6a2d7de269131f9bf4ca8 ts=2026-10-07T19:51:49.9800000Z`; `6ab9a9439a8420a1e6b56ba1.jsonl[883] _id=6ac6a2d7de269131f9bf4cac ts=2026-10-07T19:49:21.3550000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.72s, min -83679.86s, max -0.16s over 8985 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba1\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2175 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (614); Unit 4 Dev - Anderson Base (298); Unit 3 Dev (290); Unit 4 Dev (277); Unit 5 Dev (214); Unit 1 Dev (196); Unit 3 Dungeon Dev (115); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (72)
- **eventKey:** present on 1359 of 2175 records
- **Intervals:** median 3.84s (p5 0.00s / p95 31.86s, n=2174)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1359; [conversationId, dialogueEventType] x816
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2175/2175 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2175/2175 records)
    "DialogueNodeEvent"  x1359
    "DialogueStartEvent"  x412
    "DialogueFinishEvent"  x404
data.nodeId  (number, 1359/2175 records)
    numeric range 0 .. 290 (220 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PuzzlePieceVisibleEvent` — 2113 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1325); Unit 3 Dungeon Dev (294); Unit 4 Dev (272); Unit 5 Dev - Dungeon (222)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.98s, n=2112)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2113/2113 records)
    "BecameVisible"  x638
    "BecameInvisible"  x621
    "BecameCameraCentered"  x427
    "BecameCameraUncentered"  x427
data.pieceId  (string, 2113/2113 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2113/2113 records)
    1568 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1870 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (551); Unit 3 Dev (255); Unit 4 Dev (212); Unit 4 Dev - Anderson Base (205); Unit 1 Dev (191); Unit 5 Dev - Dungeon (127); Unit 4 Dev - Dungeon (117); Unit 5 Dev (117); Unit 3 Dungeon Dev (95)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=1856)
- **Fields under `data`:**

```text
data.position  (object, 1870/1870 records)
data.position.x  (number, 1870/1870 records)
    numeric range -689.474 .. 1554.76 (595 unique)
data.position.y  (number, 1870/1870 records)
    numeric range -114.326 .. 222.252 (433 unique)
data.position.z  (number, 1870/1870 records)
    numeric range -1118.03 .. 1970.98 (596 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `InputEvent` — 1794 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (521); Unit 3 Dev (281); Unit 4 Dev - Anderson Base (276); Unit 4 Dev - Dungeon (168); Unit 1 Dev (167); Unit 3 Dungeon Dev (121); Unit 4 Dev (111); Unit 5 Dev - Dungeon (104); Unit 5 Dev (45)
- **Intervals:** median 2.33s (p5 0.25s / p95 32.42s, n=1793)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1794/1794 records)
    "pressed"  x1794
data.actionType  (string, 1794/1794 records)
    "Move"  x1388
    "Interact"  x216
    "Ascend"  x54
    "Jump"  x50
    "Descend"  x44
    "Hoverboard"  x31
    "Map"  x9
    "ToggleDebug"  x2
data.key  (string, 1794/1794 records, 12 empty-string)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1794/1794 records)
    "Player"  x1225
    "Drone"  x569
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `argumentationNodeEvent` — 465 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (300); Unit 2 Prod (Refactor) (51); Unit 3 Dev (51); Unit 5 Dev (36); Unit 1 Dev (27)
- **Intervals:** median 0.92s (p5 0.04s / p95 10.62s, n=464)
- **Fields under `data`:**

```text
data.actionType  (string, 465/465 records)
    "argumentationNodeHoverEnd"  x204
    "argumentationNodeHoverStart"  x204
    "argumentationNodeAdd"  x45
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 465/465 records)
    "Unit 4 - Flooding"  x300
    "Unit 2 – Watershed"  x51
    "Unit 3 - Pollution Upstream"  x51
    "Unit 5"  x36
    "Unit 1 - Freshwater"  x17
    "Unit 1 - Argumentation Tutorial"  x10
data.nodeName  (string, 465/465 records)
    "A"  x88
    "B"  x69
    "C"  x58
    "D"  x42
    "1"  x37
    "I"  x37
    "2"  x36
    "4"  x36
    "II"  x32
    "3"  x23
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 216 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (56); Unit 2 Prod (Refactor) (39); Unit 4 Dev - Anderson Base (36); Unit 3 Dungeon Dev (27); Unit 4 Dev (19); Unit 3 Dev (14); Unit 1 Dev (10); Unit 5 Dev - Dungeon (9); Unit 5 Dev (6)
- **Intervals:** median 20.12s (p5 1.81s / p95 668.93s, n=215)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 216/216 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 216/216 records)
    97 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (6); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 228.53s (p5 0.01s / p95 83759.13s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x48; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x48
    "questFinishEvent"  x33
data.questID  (string, 81/81 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/81 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (24); Unit 2 Prod (Refactor) (20); Unit 4 Dev (14)
- **Intervals:** median 1.29s (p5 0.43s / p95 15.12s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/58 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/58 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/58 records)
    "RightDrag"  x29
    "LeftDrag"  x23
data.currentSoilType  (string, 52/58 records)
    "CLAYSAND"  x13
    "CLAY"  x12
    "SAND"  x10
    "CLAYROCK"  x8
    "SANDGRAVEL"  x5
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 52/58 records)
    "false"  x37
    "true"  x15
data.waterLevelStatus  (string, 52/58 records)
    "Proper"  x28
    "TooHigh"  x18
    "TooLow"  x6
data.waterRetentionChange  (string, 52/58 records)
    "Increase"  x19
    "Decrease"  x18
    "NoChange"  x15
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 49 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (26); Unit 2 Prod (Refactor) (23)
- **Intervals:** median 15.81s (p5 2.35s / p95 56299.84s, n=48)
- **`data` key-set variants:** [actionType, featureUsed] x48; [actionType, featureUsed, location] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "MapCloseEvent"  x24
    "MapOpenEvent"  x24
    "WaypointSetEvent"  x1
data.featureUsed  (string, 49/49 records)
    "Map"  x48
    "Waypoint"  x1
data.location  (object, 1/49 records)
data.location.x  (number, 1/49 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 1/49 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 1/49 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 41 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (8); Unit 3 Dev (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 389.61s (p5 8.16s / p95 88966.18s, n=40)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "DebugMenuStateChanged"  x41
data.isOpened  (bool, 41/41 records)
    false  x41
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 23 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (15); Unit 5 Dev (3); Unit 1 Dev (2); Unit 3 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 30.38s (p5 5.24s / p95 152867.72s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "submitAnswerEvent"  x23
data.answerSubmitted  (string, 23/23 records)
    18 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 23/23 records)
    "Unit 4 - Flooding"  x15
    "Unit 5"  x3
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 20 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (20)
- **Intervals:** median 26.41s (p5 6.28s / p95 83.96s, n=19)
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "On"  x16
    "Off"  x4
data.floor  (string, 20/20 records)
    "4"  x9
    "3"  x6
    "2"  x3
    "1"  x2
data.machineNumber  (string, 20/20 records)
    "One"  x19
    "Two"  x1
data.machineType  (string, 20/20 records)
    "Condenser"  x11
    "Evaporator"  x6
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 20/20 records)
    "3"  x8
    "2"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationEvent` — 19 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (8); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 103.66s (p5 0.03s / p95 223488.56s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x9
data.argumentationDescription  (string, 19/19 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x8
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 19/19 records)
    "Unit 4 - Flooding"  x8
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 9791.95s (p5 275.87s / p95 224990.36s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowFocusEvent` — 17 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (17)
- **Intervals:** median 9791.95s (p5 275.87s / p95 224990.36s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.49s (p5 1.91s / p95 28.23s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 6 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 86387.29s (p5 18860.97s / p95 431388.72s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    false  x6
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 208392.03s (p5 15521.77s / p95 563136.46s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `SolarStillDesignEvent` — 5 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (5)
- **Intervals:** median 3.28s (p5 2.45s / p95 5.71s, n=4)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x4; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "optionSelected"  x4
    "DesignSubmitted"  x1
data.designSelections  (object, 1/5 records)
data.designSelections.glassRoofTemperature  (string, 1/5 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/5 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/5 records)
    "Tilted Out"  x1
data.featureUsed  (string, 5/5 records)
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 4/5 records)
    "Cold"  x1
    "Covered"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 6.86s (p5 6.86s / p95 6.86s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1273.23s (p5 1273.23s / p95 1273.23s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Permissions check failed"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit1"  x1
    "unit2"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

### `soilMachine` — 1 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "ChangeCanister"  x1
data.canisterType  (string, 1/1 records)
    "Gravel"  x1
data.floor  (string, 1/1 records)
    "5"  x1
data.machine  (string, 1/1 records)
    "2"  x1
data.row  (string, 1/1 records)
    "TopRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (1x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*