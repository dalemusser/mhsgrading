# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b29

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b29
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b29.jsonl
- **Records:** 10583 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b29
- **Time span:** 2026-10-05T16:32:22.404000+00:00 .. 2026-10-16T16:53:42.818000+00:00 (264h 21m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b29\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 10583 records, 10 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 94 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3203 | 30.27 | 1 | 4 | 0 | 2026-10-06T16:54:26.938000+00:00 | 2026-10-16T16:28:20.700000+00:00 | 239h 33m |
| InputEvent | 2401 | 22.69 | 1 | 9 | 0 | 2026-10-05T16:32:55.894000+00:00 | 2026-10-16T16:53:42.818000+00:00 | 264h 20m |
| DialogueEvent | 2189 | 20.68 | 1 | 9 | 1357 | 2026-10-05T16:32:57.067000+00:00 | 2026-10-16T16:53:34.850000+00:00 | 264h 20m |
| PlayerPositionEvent | 1867 | 17.64 | 1 | 9 | 0 | 2026-10-05T16:32:37.031000+00:00 | 2026-10-16T16:53:39.796000+00:00 | 264h 21m |
| ObjectInterEvent | 273 | 2.58 | 1 | 9 | 0 | 2026-10-05T16:37:25.199000+00:00 | 2026-10-16T16:53:42.817000+00:00 | 264h 16m |
| argumentationNodeEvent | 262 | 2.48 | 1 | 5 | 0 | 2026-10-05T16:55:19.988000+00:00 | 2026-10-16T16:39:24.374000+00:00 | 263h 44m |
| questEvent | 78 | 0.74 | 1 | 9 | 78 | 2026-10-05T16:32:57.046000+00:00 | 2026-10-16T16:49:52.454000+00:00 | 264h 16m |
| Soil Key Puzzle | 74 | 0.7 | 1 | 3 | 0 | 2026-10-07T17:00:44.218000+00:00 | 2026-10-15T16:19:35.151000+00:00 | 191h 18m |
| TopographicMapEvent | 49 | 0.46 | 1 | 2 | 0 | 2026-10-06T16:55:06.808000+00:00 | 2026-10-14T16:50:01.969000+00:00 | 191h 54m |
| DEBUGMenu | 29 | 0.27 | 1 | 9 | 0 | 2026-10-05T16:32:37.018000+00:00 | 2026-10-16T16:16:23.783000+00:00 | 263h 43m |
| gameWindowFocusEvent | 20 | 0.19 | 1 | 3 | 0 | 2026-10-05T16:32:22.404000+00:00 | 2026-10-16T16:16:17.458000+00:00 | 263h 43m |
| WaterChamberEvent | 19 | 0.18 | 1 | 1 | 0 | 2026-10-16T16:20:26.573000+00:00 | 2026-10-16T16:31:24.351000+00:00 | 10m 57s |
| soilMachine | 16 | 0.15 | 1 | 1 | 0 | 2026-10-15T16:38:27.002000+00:00 | 2026-10-15T16:47:35.958000+00:00 | 9m 8s |
| argumentationAnswerEvent | 15 | 0.14 | 1 | 5 | 0 | 2026-10-05T16:55:41.070000+00:00 | 2026-10-16T16:39:25.709000+00:00 | 263h 43m |
| argumentationEvent | 15 | 0.14 | 1 | 5 | 0 | 2026-10-05T16:55:06.334000+00:00 | 2026-10-16T16:39:25.741000+00:00 | 263h 44m |
| argumentationToolEvent | 15 | 0.14 | 1 | 3 | 0 | 2026-10-05T16:55:06.269000+00:00 | 2026-10-14T16:27:17.802000+00:00 | 215h 32m |
| SolarStillDesignEvent | 14 | 0.13 | 1 | 1 | 0 | 2026-10-16T16:45:33.956000+00:00 | 2026-10-16T16:46:31.313000+00:00 | 57.4s |
| gameStartEvent | 13 | 0.12 | 1 | 1 | 0 | 2026-10-05T16:32:22.406000+00:00 | 2026-10-16T16:16:17.458000+00:00 | 263h 43m |
| gameWindowUnfocusEvent | 13 | 0.12 | 1 | 6 | 0 | 2026-10-05T17:04:40.216000+00:00 | 2026-10-16T02:46:35.319000+00:00 | 249h 41m |
| TerasGardenBox | 7 | 0.07 | 1 | 1 | 0 | 2026-10-16T02:21:28.093000+00:00 | 2026-10-16T02:35:26.454000+00:00 | 13m 58s |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-05T17:00:34.035000+00:00 | 2026-10-16T16:53:42.786000+00:00 | 263h 53m |
| chatEvent | 3 | 0.03 | 1 | 2 | 0 | 2026-10-16T02:45:32.599000+00:00 | 2026-10-16T16:32:21.034000+00:00 | 13h 46m |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-13T17:01:53.971000+00:00 | 2026-10-13T17:01:58.645000+00:00 | 4.7s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 104410.72s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.591s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 14.578s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.067s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.013s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 14.341s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 29.699s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 0.96s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 24804.217s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 66322.904s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2095.976s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 60419.302s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.168s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 14 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,II; A,B,2,II; A,C,2,II; B,2,II; C,2,II; C,A,2,II; C,D,3,II; C,D,4,II; D,2,II; D,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[135] _id=6ac3d2c0de269131f9ade813 ts=2026-10-05T16:39:28.0000000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[205] _id=6ac3d3c2de269131f9adfa20 ts=2026-10-05T16:43:45.8430000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[255] _id=6ac3d495de269131f9ae11c5 ts=2026-10-05T16:47:16.9970000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[12] _id=6ac3d116de269131f9adc53b ts=2026-10-05T16:32:22.4060000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[556] _id=6ac3d80ade269131f9ae677f ts=2026-10-05T17:02:02.2740000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[578] _id=6ac526ecde269131f9b56ae6 ts=2026-10-06T16:50:51.5800000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[11] _id=6ac3d116de269131f9adc537 ts=2026-10-05T16:32:22.4040000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[555] _id=6ac3d80ade269131f9ae677b ts=2026-10-05T17:02:02.2720000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[577] _id=6ac526ebde269131f9b56adf ts=2026-10-06T16:50:51.5780000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[579] _id=6ac526ebde269131f9b56ac9 ts=2026-10-05T17:04:40.216Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[2190] _id=6ac673f2de269131f9bc898e ts=2026-10-06T17:04:28.637Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[3234] _id=6ac7c4abde269131f9c425fb ts=2026-10-07T17:04:35.43Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3202 | 0.0 | 0.067 | 269.342 | 2.069 | 517894.822 | 0.22 | 1376 | 7 |
| InputEvent | 2400 | 0.0 | 1.591 | 396.52 | 27.142 | 429624.724 | 0.15 | 72 | 10 |
| DialogueEvent | 2188 | 0.0 | 3.844 | 434.935 | 29.259 | 429586.898 | 0.14 | 627 | 9 |
| PlayerPositionEvent | 1855 | 9.793 | 10.001 | 512.803 | 10.124 | 429540.321 | 0.12 | 0 | 8 |
| ObjectInterEvent | 272 | 0.0 | 14.578 | 3497.712 | 485.707 | 430065.486 | 0.02 | 5 | 13 |
| argumentationNodeEvent | 261 | 0.004 | 0.96 | 3637.718 | 13.379 | 690102.097 | 0.02 | 27 | 5 |
| questEvent | 77 | 0.0 | 205.783 | 12356.044 | 83985.463 | 430702.06 | 0.0 | 13 | 14 |
| Soil Key Puzzle | 73 | 0.008 | 2.013 | 9434.67 | 22.059 | 518305.304 | 0.01 | 1 | 3 |
| TopographicMapEvent | 48 | 0.018 | 14.341 | 14393.649 | 85417.611 | 431981.215 | 0.0 | 2 | 5 |
| DEBUGMenu | 28 | 6.484 | 719.908 | 33908.099 | 86028.107 | 431364.97 | 0.0 | 0 | 15 |
| gameWindowFocusEvent | 19 | 4.099 | 2095.976 | 49970.266 | 120723.248 | 431425.189 | 0.0 | 0 | 12 |
| WaterChamberEvent | 18 | 6.252 | 28.366 | 36.543 | 104.692 | 122.952 | 1.64 | 0 | 0 |
| soilMachine | 15 | 0.631 | 5.168 | 36.597 | 145.56 | 202.639 | 1.64 | 0 | 0 |
| argumentationAnswerEvent | 14 | 10.193 | 29.699 | 67816.046 | 299080.472 | 690164.728 | 0.0 | 0 | 5 |
| argumentationEvent | 14 | 0.045 | 94.978 | 67818.529 | 298974.677 | 690050.56 | 0.0 | 1 | 5 |
| argumentationToolEvent | 14 | 0.976 | 8.623 | 55423.681 | 297207.402 | 690116.378 | 0.0 | 0 | 2 |
| SolarStillDesignEvent | 13 | 1.139 | 3.482 | 4.412 | 9.684 | 10.444 | 13.6 | 0 | 0 |
| gameStartEvent | 12 | 1570.053 | 66322.904 | 79119.588 | 241551.78 | 431425.189 | 0.0 | 0 | 12 |
| gameWindowUnfocusEvent | 12 | 5.905 | 60419.302 | 74909.592 | 240897.629 | 429392.076 | 0.0 | 0 | 8 |
| TerasGardenBox | 6 | 1.886 | 4.955 | 139.727 | 607.561 | 802.836 | 0.43 | 0 | 1 |
| EndOfUnit | 4 | 50918.243 | 104410.72 | 237497.188 | 604983.236 | 690249.069 | 0.0 | 0 | 4 |
| chatEvent | 2 | 957.441 | 24804.217 | 24804.217 | 46266.316 | 48650.994 | 0.0 | 0 | 2 |
| DaniEvent | 1 | 4.674 | 4.674 | 4.674 | 4.674 | 4.674 | 12.84 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[4331] _id=6ac7cbf2de269131f9c4cc9d ts=2026-10-08T16:59:29.9970000Z == 6ab9a8e69a8420a1e6b56b29.jsonl[4339] _id=6ac7cbf2de269131f9c4cc9e ts=2026-10-08T16:59:29.9970000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 75 group(s), 104 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[639] _id=6ac527c4de269131f9b58e25 ts=2026-10-06T16:54:28.0020000Z == 6ab9a8e69a8420a1e6b56b29.jsonl[644] _id=6ac527c4de269131f9b58e2b ts=2026-10-06T16:54:28.0020000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[647] _id=6ac527cfde269131f9b590d9 ts=2026-10-06T16:54:38.7350000Z == 6ab9a8e69a8420a1e6b56b29.jsonl[648] _id=6ac527d0de269131f9b590e4 ts=2026-10-06T16:54:38.7350000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[650] _id=6ac527d1de269131f9b59131 ts=2026-10-06T16:54:39.9340000Z == 6ab9a8e69a8420a1e6b56b29.jsonl[654] _id=6ac527d1de269131f9b59137 ts=2026-10-06T16:54:39.9340000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[10191] _id=6ad25385de269131f9e60255 ts=2026-10-16T16:40:36.1480000Z == 6ab9a8e69a8420a1e6b56b29.jsonl[10192] _id=6ad25385de269131f9e60256 ts=2026-10-16T16:40:36.1480000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8e69a8420a1e6b56b29.jsonl[94] _id=6ac3d245de269131f9addd09 ts=2026-10-05T16:37:25.1990000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[97] _id=6ac3d245de269131f9addd0d ts=2026-10-05T16:37:25.2040000Z`; `634ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8052] _id=6ad10191de269131f9ddb0fe ts=2026-10-15T16:38:40.9920000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[8042] _id=6ad10192de269131f9ddb10d ts=2026-10-15T16:38:41.6260000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 196 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `88ms: 6ab9a8e69a8420a1e6b56b29.jsonl[703] _id=6ac52820de269131f9b5a25f ts=2026-10-06T16:55:58.5790000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[713] _id=6ac52820de269131f9b5a266 ts=2026-10-06T16:55:58.6670000Z`; `25ms: 6ab9a8e69a8420a1e6b56b29.jsonl[713] _id=6ac52820de269131f9b5a266 ts=2026-10-06T16:55:58.6670000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[715] _id=6ac52821de269131f9b5a275 ts=2026-10-06T16:55:58.6920000Z`; `19ms: 6ab9a8e69a8420a1e6b56b29.jsonl[717] _id=6ac52823de269131f9b5a31f ts=2026-10-06T16:56:00.3890000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[723] _id=6ac52824de269131f9b5a331 ts=2026-10-06T16:56:00.4080000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6ab9a8e69a8420a1e6b56b29.jsonl[6072] _id=6acfad8ede269131f9d57526 ts=2026-10-14T16:27:57.2790000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[6075] _id=6acfad8ede269131f9d57529 ts=2026-10-14T16:27:57.3240000Z`; `58ms: 6ab9a8e69a8420a1e6b56b29.jsonl[9113] _id=6ad18934de269131f9e2b0dc ts=2026-10-16T02:17:23.4170000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[9116] _id=6ad18934de269131f9e2b0e0 ts=2026-10-16T02:17:23.4750000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `845ms: 6ab9a8e69a8420a1e6b56b29.jsonl[387] _id=6ac3d679de269131f9ae3ec5 ts=2026-10-05T16:55:20.8090000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[390] _id=6ac3d679de269131f9ae3edb ts=2026-10-05T16:55:21.6540000Z`; `546ms: 6ab9a8e69a8420a1e6b56b29.jsonl[391] _id=6ac3d67ade269131f9ae3ee0 ts=2026-10-05T16:55:21.6660000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[392] _id=6ac3d67ade269131f9ae3ee9 ts=2026-10-05T16:55:22.2120000Z`; `33ms: 6ab9a8e69a8420a1e6b56b29.jsonl[396] _id=6ac3d67cde269131f9ae3f0f ts=2026-10-05T16:55:23.7120000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[395] _id=6ac3d67cde269131f9ae3f1b ts=2026-10-05T16:55:23.7450000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8e69a8420a1e6b56b29.jsonl[10452] _id=6ad2553dde269131f9e61ad6 ts=2026-10-16T16:47:57.0190000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[10453] _id=6ad2553dde269131f9e61ada ts=2026-10-16T16:47:57.0240000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `631ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8048] _id=6ad10191de269131f9ddb0fc ts=2026-10-15T16:38:40.9890000Z ~ 6ab9a8e69a8420a1e6b56b29.jsonl[8049] _id=6ad10191de269131f9ddb109 ts=2026-10-15T16:38:41.6200000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a8e69a8420a1e6b56b29.jsonl[3243] _id=6ac7c4e7de269131f9c429d7 ts=2026-10-08T16:29:26.8960000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4512] _id=6ace59ecde269131f9cf590f ts=2026-10-13T16:18:51.8660000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b29.jsonl[2194] _id=6ac673fbde269131f9bc8a28 ts=2026-10-07T16:31:55.7960000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3235] _id=6ac7c4abde269131f9c425fd ts=2026-10-08T16:28:26.6620000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b29.jsonl[364] _id=6ac3d81ade269131f9ae68de ts=2026-10-05T17:02:17.7260000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[580] _id=6ac526f7de269131f9b56ca0 ts=2026-10-06T16:51:03.5670000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8e69a8420a1e6b56b29.jsonl[4489] _id=6ac7ccf2de269131f9c4de28 ts=2026-10-08T17:03:46.2500000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4523] _id=6ace5b06de269131f9cf622f ts=2026-10-13T16:23:33.1480000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b29.jsonl[573] _id=6ac3d886de269131f9ae714f ts=2026-10-05T17:04:06.6150000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[591] _id=6ac52715de269131f9b57116 ts=2026-10-06T16:51:33.0290000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b29.jsonl[2180] _id=6ac52a16de269131f9b60ae3 ts=2026-10-06T17:04:22.1970000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[2205] _id=6ac67422de269131f9bc8c7c ts=2026-10-07T16:32:33.6720000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 627 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[10249] _id=6ad2532fde269131f9e5fe4a ts=2026-10-16T16:39:10.4920000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[10250] _id=6ad2532fde269131f9e5fe4b ts=2026-10-16T16:39:10.4920000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8756] _id=6ad1077ade269131f9de438f ts=2026-10-15T17:03:53.3160000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8757] _id=6ad1077ade269131f9de4390 ts=2026-10-15T17:03:53.3160000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8862] _id=6ad10785de269131f9de450a ts=2026-10-15T17:04:05.4000000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8863] _id=6ad10785de269131f9de450b ts=2026-10-15T17:04:05.4000000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 44m 
  - Evidence: 191h 44m: 6ab9a8e69a8420a1e6b56b29.jsonl[548] _id=6ac3d7b2de269131f9ae5e0d ts=2026-10-05T17:00:34.0350000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[5085] _id=6ace5ffbde269131f9cfb183 ts=2026-10-13T16:44:43.1040000Z; 33h 50m: 6ab9a8e69a8420a1e6b56b29.jsonl[6874] _id=6acfb3dfde269131f9d60918 ts=2026-10-14T16:54:54.3610000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[9509] _id=6ad18fb1de269131f9e2c5ca ts=2026-10-16T02:45:04.5430000Z; 24h 10m: 6ab9a8e69a8420a1e6b56b29.jsonl[5085] _id=6ace5ffbde269131f9cfb183 ts=2026-10-13T16:44:43.1040000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6874] _id=6acfb3dfde269131f9d60918 ts=2026-10-14T16:54:54.3610000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b29.jsonl[4491] _id=6ac7cd20de269131f9c4e00b ts=2026-10-08T17:04:31.8880000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4536] _id=6ace5b59de269131f9cf64b4 ts=2026-10-13T16:24:56.6120000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b29.jsonl[572] _id=6ac3d887de269131f9ae715f ts=2026-10-05T17:04:06.9040000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[582] _id=6ac526fbde269131f9b56d2f ts=2026-10-06T16:51:05.5170000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b29.jsonl[2152] _id=6ac52a0dde269131f9b608c4 ts=2026-10-06T17:04:12.8400000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[2199] _id=6ac6740dde269131f9bc8b1a ts=2026-10-07T16:32:13.3260000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 72 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[4331] _id=6ac7cbf2de269131f9c4cc9d ts=2026-10-08T16:59:29.9970000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4339] _id=6ac7cbf2de269131f9c4cc9e ts=2026-10-08T16:59:29.9970000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[5893] _id=6acfac1fde269131f9d55981 ts=2026-10-14T16:21:49.9200000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[5894] _id=6acfac1fde269131f9d55982 ts=2026-10-14T16:21:49.9200000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[5907] _id=6acfac24de269131f9d55a03 ts=2026-10-14T16:21:55.2740000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[5908] _id=6acfac24de269131f9d55a04 ts=2026-10-14T16:21:55.2740000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a8e69a8420a1e6b56b29.jsonl[4468] _id=6ac7ccdede269131f9c4dd44 ts=2026-10-08T17:03:25.4640000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4663] _id=6ace5ccfde269131f9cf7785 ts=2026-10-13T16:31:10.9500000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b29.jsonl[520] _id=6ac3d786de269131f9ae59a3 ts=2026-10-05T16:59:50.2900000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[608] _id=6ac5274fde269131f9b577ff ts=2026-10-06T16:52:31.8320000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b29.jsonl[3164] _id=6ac67abcde269131f9bd78f0 ts=2026-10-07T17:00:44.2220000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3292] _id=6ac7c595de269131f9c438a1 ts=2026-10-08T16:32:21.1000000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8651] _id=6ad105f7de269131f9de1d5e ts=2026-10-15T16:57:26.5460000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8652] _id=6ad105f7de269131f9de1d5f ts=2026-10-15T16:57:26.5460000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8704] _id=6ad10637de269131f9de2333 ts=2026-10-15T16:58:30.9860000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8710] _id=6ad10637de269131f9de2334 ts=2026-10-15T16:58:30.9860000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[8970] _id=6ad1880cde269131f9e2aacc ts=2026-10-16T02:12:27.3910000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8971] _id=6ad1880cde269131f9e2aacd ts=2026-10-16T02:12:27.3910000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8e69a8420a1e6b56b29.jsonl[4511] _id=6ac7cd1ede269131f9c4dfeb ts=2026-10-08T17:04:30.2210000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4519] _id=6ace5b06de269131f9cf622e ts=2026-10-13T16:23:30.5420000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b29.jsonl[576] _id=6ac3d89ede269131f9ae72fb ts=2026-10-05T17:04:30.6440000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[581] _id=6ac526fbde269131f9b56d1f ts=2026-10-06T16:51:03.5770000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b29.jsonl[2182] _id=6ac52a1ade269131f9b60b63 ts=2026-10-06T17:04:26.4750000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[2195] _id=6ac673ffde269131f9bc8a50 ts=2026-10-07T16:31:55.8170000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 51m 
  - Evidence: 143h 51m: 6ab9a8e69a8420a1e6b56b29.jsonl[4000] _id=6ac7c7aede269131f9c47e5a ts=2026-10-08T16:41:16.3780000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6219] _id=6acfaeb5de269131f9d58759 ts=2026-10-14T16:32:51.2000000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b29.jsonl[2733] _id=6ac67531de269131f9bcb3b7 ts=2026-10-07T16:37:03.2570000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3323] _id=6ac7c5e0de269131f9c44289 ts=2026-10-08T16:33:34.9980000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b29.jsonl[6364] _id=6acfaf28de269131f9d5902b ts=2026-10-14T16:34:45.9170000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[7013] _id=6ad0fd1cde269131f9dd5a95 ts=2026-10-15T16:19:39.6300000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1376 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[1029] _id=6ac52896de269131f9b5c069 ts=2026-10-06T16:57:57.9410000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[1030] _id=6ac52896de269131f9b5c06f ts=2026-10-06T16:57:57.9410000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[1030] _id=6ac52896de269131f9b5c06f ts=2026-10-06T16:57:57.9410000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[1059] _id=6ac52896de269131f9b5c076 ts=2026-10-06T16:57:57.9410000Z; 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[1031] _id=6ac52898de269131f9b5c0ba ts=2026-10-06T16:57:58.5080000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[1066] _id=6ac52898de269131f9b5c0d3 ts=2026-10-06T16:57:58.5080000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 58m 
  - Evidence: 143h 58m: 6ab9a8e69a8420a1e6b56b29.jsonl[3302] _id=6ac7c5b8de269131f9c43d72 ts=2026-10-08T16:32:55.5360000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6182] _id=6acfae59de269131f9d581ca ts=2026-10-14T16:31:20.8400000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b29.jsonl[6201] _id=6acfae8bde269131f9d58516 ts=2026-10-14T16:32:10.6880000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6988] _id=6ad0fd03de269131f9dd58dd ts=2026-10-15T16:19:14.8270000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b29.jsonl[3205] _id=6ac67b48de269131f9bd87ff ts=2026-10-07T17:03:04.1080000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3290] _id=6ac7c595de269131f9c4389b ts=2026-10-08T16:32:21.0940000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.008s..0.008s shown 
  - Evidence: 8ms: 6ab9a8e69a8420a1e6b56b29.jsonl[6994] _id=6ad0fd0ede269131f9dd5972 ts=2026-10-15T16:19:25.8040000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6983] _id=6ad0fd0ede269131f9dd5975 ts=2026-10-15T16:19:25.8120000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 13m 22s 
  - Evidence: 13m 22s: 6ab9a8e69a8420a1e6b56b29.jsonl[9235] _id=6ad18a32de269131f9e2b575 ts=2026-10-16T02:21:38.0030000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[9335] _id=6ad18d55de269131f9e2bedd ts=2026-10-16T02:35:00.8390000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6ab9a8e69a8420a1e6b56b29.jsonl[4181] _id=6ac7ca38de269131f9c4b138 ts=2026-10-08T16:52:07.9070000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[5205] _id=6ace61a5de269131f9cfcfbe ts=2026-10-13T16:51:49.1220000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b29.jsonl[3060] _id=6ac6797ede269131f9bd5739 ts=2026-10-07T16:55:26.0660000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4176] _id=6ac7ca29de269131f9c4b0a1 ts=2026-10-08T16:51:52.8090000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b29.jsonl[5467] _id=6ace63dbde269131f9cff9bc ts=2026-10-13T17:01:14.5580000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6726] _id=6acfb227de269131f9d5d59e ts=2026-10-14T16:47:34.1380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.018s..0.036s shown 
  - Evidence: 18ms: 6ab9a8e69a8420a1e6b56b29.jsonl[2893] _id=6ac6770ede269131f9bd0f63 ts=2026-10-07T16:45:02.2030000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[2897] _id=6ac6770ede269131f9bd0f67 ts=2026-10-07T16:45:02.2210000Z; 36ms: 6ab9a8e69a8420a1e6b56b29.jsonl[2892] _id=6ac6770ede269131f9bd0f51 ts=2026-10-07T16:45:02.1670000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[2893] _id=6ac6770ede269131f9bd0f63 ts=2026-10-07T16:45:02.2030000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 6ab9a8e69a8420a1e6b56b29.jsonl[446] _id=6ac3d705de269131f9ae4c85 ts=2026-10-05T16:57:41.5910000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[5003] _id=6ace5efbde269131f9cf9e2c ts=2026-10-13T16:40:26.3190000Z; 24h 34m: 6ab9a8e69a8420a1e6b56b29.jsonl[6071] _id=6acfad8ede269131f9d57524 ts=2026-10-14T16:27:57.2620000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8823] _id=6ad1073ede269131f9de3de6 ts=2026-10-15T17:02:53.9040000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b29.jsonl[5003] _id=6ace5efbde269131f9cf9e2c ts=2026-10-13T16:40:26.3190000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6071] _id=6acfad8ede269131f9d57524 ts=2026-10-14T16:27:57.2620000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 40m 
  - Evidence: 191h 40m: 6ab9a8e69a8420a1e6b56b29.jsonl[448] _id=6ac3d706de269131f9ae4c8b ts=2026-10-05T16:57:41.6190000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4945] _id=6ace5e88de269131f9cf95a7 ts=2026-10-13T16:38:32.1790000Z; 24h 33m: 6ab9a8e69a8420a1e6b56b29.jsonl[6075] _id=6acfad8ede269131f9d57529 ts=2026-10-14T16:27:57.3240000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8785] _id=6ad106d9de269131f9de346d ts=2026-10-15T17:01:12.6790000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b29.jsonl[5004] _id=6ace5efbde269131f9cf9e30 ts=2026-10-13T16:40:26.3460000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6008] _id=6acfad1ade269131f9d56cc4 ts=2026-10-14T16:26:01.1150000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.045s..0.045s shown 
  - Evidence: 45ms: 6ab9a8e69a8420a1e6b56b29.jsonl[6072] _id=6acfad8ede269131f9d57526 ts=2026-10-14T16:27:57.2790000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6075] _id=6acfad8ede269131f9d57529 ts=2026-10-14T16:27:57.3240000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 41m 
  - Evidence: 191h 41m: 6ab9a8e69a8420a1e6b56b29.jsonl[445] _id=6ac3d700de269131f9ae4c09 ts=2026-10-05T16:57:36.5560000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4957] _id=6ace5eb7de269131f9cf990a ts=2026-10-13T16:39:18.6530000Z; 24h 33m: 6ab9a8e69a8420a1e6b56b29.jsonl[6068] _id=6acfad8cde269131f9d574fc ts=2026-10-14T16:27:55.5790000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8780] _id=6ad106ddde269131f9de34d5 ts=2026-10-15T17:01:16.9390000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b29.jsonl[4999] _id=6ace5ef1de269131f9cf9d4e ts=2026-10-13T16:40:16.5660000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6001] _id=6acfad15de269131f9d56c80 ts=2026-10-14T16:25:56.3160000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 27 interval(s) ≤ 0.004s..0.012s shown 
  - Evidence: 4ms: 6ab9a8e69a8420a1e6b56b29.jsonl[426] _id=6ac3d6d4de269131f9ae4727 ts=2026-10-05T16:56:51.9060000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[425] _id=6ac3d6d4de269131f9ae472b ts=2026-10-05T16:56:51.9100000Z; 7ms: 6ab9a8e69a8420a1e6b56b29.jsonl[9082] _id=6ad188f7de269131f9e2aeae ts=2026-10-16T02:16:22.6320000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[9080] _id=6ad188f7de269131f9e2aeb0 ts=2026-10-16T02:16:22.6390000Z; 12ms: 6ab9a8e69a8420a1e6b56b29.jsonl[390] _id=6ac3d679de269131f9ae3edb ts=2026-10-05T16:55:21.6540000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[391] _id=6ac3d67ade269131f9ae3ee0 ts=2026-10-05T16:55:21.6660000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 41m 
  - Evidence: 191h 41m: 6ab9a8e69a8420a1e6b56b29.jsonl[337] _id=6ac3d6cfde269131f9ae46dd ts=2026-10-05T16:56:47.5750000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4946] _id=6ace5e94de269131f9cf9652 ts=2026-10-13T16:38:43.9530000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b29.jsonl[4956] _id=6ace5eb5de269131f9cf98df ts=2026-10-13T16:39:16.6370000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[6032] _id=6acfad3ede269131f9d56ef9 ts=2026-10-14T16:26:37.6670000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 13h 30m 
  - Evidence: 13h 30m: 6ab9a8e69a8420a1e6b56b29.jsonl[9514] _id=6ad18fcdde269131f9e2c619 ts=2026-10-16T02:45:32.5990000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[9554] _id=6ad24dd8de269131f9e5a9b4 ts=2026-10-16T16:16:23.5930000Z; 15m 57s: 6ab9a8e69a8420a1e6b56b29.jsonl[9554] _id=6ad24dd8de269131f9e5a9b4 ts=2026-10-16T16:16:23.5930000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[10085] _id=6ad25195de269131f9e5e80d ts=2026-10-16T16:32:21.0340000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a8e69a8420a1e6b56b29.jsonl[3237] _id=6ac7c4abde269131f9c425ff ts=2026-10-08T16:28:26.8090000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4515] _id=6ace59ecde269131f9cf5911 ts=2026-10-13T16:18:51.9980000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b29.jsonl[2193] _id=6ac673f2de269131f9bc899e ts=2026-10-07T16:31:46.0000000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3237] _id=6ac7c4abde269131f9c425ff ts=2026-10-08T16:28:26.8090000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b29.jsonl[556] _id=6ac3d80ade269131f9ae677f ts=2026-10-05T17:02:02.2740000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[578] _id=6ac526ecde269131f9b56ae6 ts=2026-10-06T16:50:51.5800000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a8e69a8420a1e6b56b29.jsonl[3236] _id=6ac7c4abde269131f9c425fe ts=2026-10-08T16:28:26.8090000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4514] _id=6ace59ecde269131f9cf5910 ts=2026-10-13T16:18:51.9980000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b29.jsonl[2192] _id=6ac673f2de269131f9bc899d ts=2026-10-07T16:31:45.9990000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3236] _id=6ac7c4abde269131f9c425fe ts=2026-10-08T16:28:26.8090000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b29.jsonl[555] _id=6ac3d80ade269131f9ae677b ts=2026-10-05T17:02:02.2720000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[577] _id=6ac526ebde269131f9b56adf ts=2026-10-06T16:50:51.5780000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b29.jsonl[4513] _id=6ace59ecde269131f9cf590d ts=2026-10-08T17:04:35.46Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4517] _id=6ace5a74de269131f9cf5caa ts=2026-10-13T16:21:07.5360000Z; 24h 4m: 6ab9a8e69a8420a1e6b56b29.jsonl[6907] _id=6acfb523de269131f9d629b9 ts=2026-10-14T17:00:17.9720000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[8906] _id=6ad18797de269131f9e2a926 ts=2026-10-15T17:04:52.872Z; 24h 0m: 6ab9a8e69a8420a1e6b56b29.jsonl[2190] _id=6ac673f2de269131f9bc898e ts=2026-10-06T17:04:28.637Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[3234] _id=6ac7c4abde269131f9c425fb ts=2026-10-07T17:04:35.43Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6ab9a8e69a8420a1e6b56b29.jsonl[4069] _id=6ac7c897de269131f9c495b1 ts=2026-10-08T16:45:11.1610000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[4525] _id=6ace5b06de269131f9cf6231 ts=2026-10-13T16:23:33.2210000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b29.jsonl[567] _id=6ac3d87fde269131f9ae7097 ts=2026-10-05T17:03:58.8520000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[583] _id=6ac526fbde269131f9b56d3d ts=2026-10-06T16:51:05.5480000Z; 23h 40m: 6ab9a8e69a8420a1e6b56b29.jsonl[583] _id=6ac526fbde269131f9b56d3d ts=2026-10-06T16:51:05.5480000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[2196] _id=6ac673ffde269131f9bc8a51 ts=2026-10-07T16:31:58.4230000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b29.jsonl[10191] _id=6ad25385de269131f9e60255 ts=2026-10-16T16:40:36.1480000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[10192] _id=6ad25385de269131f9e60256 ts=2026-10-16T16:40:36.1480000Z; 3ms: 6ab9a8e69a8420a1e6b56b29.jsonl[356] _id=6ac3d620de269131f9ae3259 ts=2026-10-05T16:53:51.3780000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[359] _id=6ac3d620de269131f9ae3265 ts=2026-10-05T16:53:51.3810000Z; 4ms: 6ab9a8e69a8420a1e6b56b29.jsonl[115] _id=6ac3d291de269131f9ade46d ts=2026-10-05T16:38:41.2770000Z -> 6ab9a8e69a8420a1e6b56b29.jsonl[118] _id=6ac3d291de269131f9ade471 ts=2026-10-05T16:38:41.2810000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[345] _id=6ac3d5fede269131f9ae2f39 ts=2026-10-05T16:53:18.2970000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[456] _id=6ac3d720de269131f9ae4ea9 ts=2026-10-05T16:58:08.0100000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[3000] _id=6ac678a8de269131f9bd45ba ts=2026-10-07T16:51:52.4170000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 24 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[845] _id=6ac5283dde269131f9b5a995 ts=2026-10-06T16:56:27.4020000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[859] _id=6ac5283dde269131f9b5a99f ts=2026-10-06T16:56:27.4580000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[896] _id=6ac52852de269131f9b5af47 ts=2026-10-06T16:56:49.5130000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 93 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[640] _id=6ac527c4de269131f9b58e2f ts=2026-10-06T16:54:28.0020000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[645] _id=6ac527c4de269131f9b58e37 ts=2026-10-06T16:54:28.0020000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[715] _id=6ac52821de269131f9b5a275 ts=2026-10-06T16:55:58.6920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[6075] _id=6acfad8ede269131f9d57529 ts=2026-10-14T16:27:57.3240000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[395] _id=6ac3d67cde269131f9ae3f1b ts=2026-10-05T16:55:23.7450000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[9514] _id=6ad18fcdde269131f9e2c619 ts=2026-10-16T02:45:32.5990000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[9554] _id=6ad24dd8de269131f9e5a9b4 ts=2026-10-16T16:16:23.5930000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[10085] _id=6ad25195de269131f9e5e80d ts=2026-10-16T16:32:21.0340000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[7738] _id=6ad0fed2de269131f9dd7f39 ts=2026-10-15T16:26:58.1730000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[533] _id=6ac3d82cde269131f9ae6a09 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 230 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[1093] _id=6ac5289ede269131f9b5c24b ts=2026-10-06T16:58:04.8780000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[1133] _id=6ac528afde269131f9b5c5bf ts=2026-10-06T16:58:22.6790000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[1138] _id=6ac528b0de269131f9b5c60f ts=2026-10-06T16:58:23.0420000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 600 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[642] _id=6ac527c4de269131f9b58e15 ts=2026-10-06T16:54:27.6770000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[648] _id=6ac527d0de269131f9b590e4 ts=2026-10-06T16:54:38.7350000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[680] _id=6ac5281dde269131f9b5a155 ts=2026-10-06T16:55:56.2410000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[9067] _id=6ad188e8de269131f9e2ae40 ts=2026-10-16T02:16:07.6280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[398] _id=6ac3d682de269131f9ae3f95 ts=2026-10-05T16:55:29.9800000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[401] _id=6ac3d688de269131f9ae4005 ts=2026-10-05T16:55:35.7780000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[429] _id=6ac3d6d2de269131f9ae46fd ts=2026-10-05T16:56:49.8460000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[419] _id=6ac3d6cade269131f9ae4655 ts=2026-10-05T16:56:42.4150000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[4949] _id=6ace5ea3de269131f9cf978a ts=2026-10-13T16:38:58.5180000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[4951] _id=6ace5eaade269131f9cf982c ts=2026-10-13T16:39:05.9890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 419 start, 413 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 45 unmatched 'BecameCameraCentered' (totals: 626 open, 605 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 89 unmatched 'BecameVisible' (totals: 984 open, 988 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 114 open, 114 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'argumentationToolOpen' (totals: 13 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 46 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 246 of 10581 adjacent _id pairs reverse in client time; worst 106.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b29.jsonl[765] _id=6ac5282dde269131f9b5a572 ts=2026-10-06T16:56:12.8930000Z`; `6ab9a8e69a8420a1e6b56b29.jsonl[779] _id=6ac5282ede269131f9b5a5af ts=2026-10-06T16:54:26.9380000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.77s, min -429257.18s, max -0.14s over 10582 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b29\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3203 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2225); Unit 4 Dev (638); Unit 5 Dev - Dungeon (210); Unit 3 Dungeon Dev (130)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.07s, n=3202)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3203/3203 records)
    "BecameInvisible"  x988
    "BecameVisible"  x984
    "BecameCameraCentered"  x626
    "BecameCameraUncentered"  x605
data.pieceId  (string, 3203/3203 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3203/3203 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2401 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (799); Unit 3 Dev (533); Unit 4 Dev - Dungeon (313); Unit 4 Dev - Anderson Base (165); Unit 4 Dev (161); Unit 3 Dungeon Dev (139); Unit 5 Dev - Dungeon (138); Unit 1 Dev (86); Unit 5 Dev (67)
- **Intervals:** median 1.59s (p5 0.10s / p95 27.14s, n=2400)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2401/2401 records)
    "pressed"  x2401
data.actionType  (string, 2401/2401 records)
    "Move"  x1955
    "Interact"  x311
    "Sprint"  x36
    "Ascend"  x26
    "Descend"  x23
    "Hoverboard"  x20
    "Jump"  x20
    "Map"  x10
data.key  (string, 2401/2401 records, 3 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2401/2401 records)
    "Player"  x1497
    "Drone"  x904
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2189 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (680); Unit 3 Dev (380); Unit 4 Dev (255); Unit 5 Dev (247); Unit 1 Dev (203); Unit 4 Dev - Anderson Base (161); Unit 3 Dungeon Dev (106); Unit 4 Dev - Dungeon (82); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1357 of 2189 records
- **Intervals:** median 3.84s (p5 0.00s / p95 29.26s, n=2188)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1357; [conversationId, dialogueEventType] x832
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2189/2189 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2189/2189 records)
    "DialogueNodeEvent"  x1357
    "DialogueStartEvent"  x419
    "DialogueFinishEvent"  x413
data.nodeId  (number, 1357/2189 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1867 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (619); Unit 4 Dev (272); Unit 3 Dev (255); Unit 1 Dev (167); Unit 4 Dev - Dungeon (148); Unit 5 Dev (121); Unit 5 Dev - Dungeon (104); Unit 4 Dev - Anderson Base (101); Unit 3 Dungeon Dev (80)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=1855)
- **Fields under `data`:**

```text
data.position  (object, 1867/1867 records)
data.position.x  (number, 1867/1867 records)
    numeric range -699.442 .. 1556.04 (627 unique)
data.position.y  (number, 1867/1867 records)
    numeric range -115.127 .. 222.008 (440 unique)
data.position.z  (number, 1867/1867 records)
    numeric range -1036.39 .. 2075.24 (627 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 273 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (92); Unit 2 Prod (Refactor) (72); Unit 3 Dungeon Dev (25); Unit 4 Dev (22); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (12); Unit 1 Dev (11); Unit 5 Dev - Dungeon (11); Unit 5 Dev (10)
- **Intervals:** median 14.58s (p5 1.96s / p95 485.71s, n=272)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 273/273 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 273/273 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 262 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (105); Unit 3 Dev (53); Unit 2 Prod (Refactor) (39); Unit 1 Dev (35); Unit 5 Dev (30)
- **Intervals:** median 0.96s (p5 0.04s / p95 13.38s, n=261)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 262/262 records)
    "argumentationNodeHoverEnd"  x114
    "argumentationNodeHoverStart"  x114
    "argumentationNodeAdd"  x28
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 262/262 records)
    "Unit 4 - Flooding"  x105
    "Unit 3 - Pollution Upstream"  x53
    "Unit 2 – Watershed"  x39
    "Unit 5"  x30
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x16
data.nodeName  (string, 262/262 records)
    "A"  x40
    "B"  x36
    "I"  x35
    "II"  x32
    "1"  x26
    "C"  x25
    "3"  x19
    "4"  x18
    "D"  x18
    "2"  x10
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 78 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev (9); Unit 4 Dev - Dungeon (8); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 78 of 78 records
- **Intervals:** median 205.78s (p5 0.00s / p95 83985.46s, n=77)
- **`data` key-set variants:** [questEventType, questID, questName] x46; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 78/78 records)
    "questActiveEvent"  x46
    "questFinishEvent"  x32
data.questID  (string, 78/78 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 78/78 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/78 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 74 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (40); Unit 3 Dev (20); Unit 4 Dev (14)
- **Intervals:** median 2.01s (p5 0.15s / p95 22.06s, n=73)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x66; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/74 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/74 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 66/74 records)
    "RightDrag"  x38
    "LeftDrag"  x28
data.currentSoilType  (string, 66/74 records)
    "SAND"  x14
    "CLAYSAND"  x13
    "CLAY"  x12
    "CLAYROCK"  x11
    "SANDGRAVEL"  x9
    "BEDROCK"  x4
    "GRAVEL"  x3
data.isCorrectSelection  (string, 66/74 records)
    "false"  x49
    "true"  x17
data.waterLevelStatus  (string, 66/74 records)
    "TooHigh"  x26
    "Proper"  x22
    "TooLow"  x18
data.waterRetentionChange  (string, 66/74 records)
    "Increase"  x29
    "Decrease"  x20
    "NoChange"  x17
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 49 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (21)
- **Intervals:** median 14.34s (p5 1.24s / p95 85417.61s, n=48)
- **`data` key-set variants:** [actionType, featureUsed] x38; [actionType, featureUsed, location] x11
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
    "WaypointMoveEvent"  x8
    "WaypointSetEvent"  x3
data.featureUsed  (string, 49/49 records)
    "Map"  x38
    "Waypoint"  x11
data.location  (object, 11/49 records)
data.location.x  (number, 11/49 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 11/49 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 11/49 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 719.91s (p5 6.76s / p95 86028.11s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 4 Dev (3); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 2095.98s (p5 5.62s / p95 120723.25s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 19 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (19)
- **Intervals:** median 28.37s (p5 7.22s / p95 104.69s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "On"  x15
    "Off"  x4
data.floor  (string, 19/19 records)
    "3"  x9
    "4"  x5
    "2"  x3
    "1"  x2
data.machineNumber  (string, 19/19 records)
    "One"  x17
    "Two"  x2
data.machineType  (string, 19/19 records)
    "Condenser"  x12
    "Evaporator"  x4
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 19/19 records)
    "2"  x6
    "4"  x5
    "1"  x4
    "3"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 5.17s (p5 0.77s / p95 145.56s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x8
    "Bedrock"  x4
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 16/16 records)
    "5"  x10
    "4"  x6
data.machine  (string, 16/16 records)
    "1"  x15
    "2"  x1
data.row  (string, 16/16 records)
    "TopRow"  x11
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 15 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (9); Unit 1 Dev (2); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 29.70s (p5 10.42s / p95 299080.47s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "submitAnswerEvent"  x15
data.answerSubmitted  (string, 15/15 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 15/15 records)
    "Unit 4 - Flooding"  x9
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 94.98s (p5 0.05s / p95 298974.68s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 15 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5)
- **Intervals:** median 8.62s (p5 1.70s / p95 297207.40s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 15/15 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Graph"  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Waterfall Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `SolarStillDesignEvent` — 14 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (14)
- **Intervals:** median 3.48s (p5 1.30s / p95 9.68s, n=13)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x13; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "optionSelected"  x13
    "DesignSubmitted"  x1
data.designSelections  (object, 1/14 records)
data.designSelections.glassRoofTemperature  (string, 1/14 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/14 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/14 records)
    "Tilted In"  x1
data.featureUsed  (string, 14/14 records)
    "GlassRoofTemperature"  x6
    "RoofStyle"  x5
    "ExtraCovering"  x2
    "Submit"  x1
data.selectedOption  (string, 13/14 records, 1 empty-string)
    "Cold"  x3
    "Hot"  x3
    "Tilted In"  x3
    ""  x1
    "Covered"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 66322.90s (p5 1685.45s / p95 241551.78s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); MainMenu (3); Unit 4 Dev (3); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 60419.30s (p5 9.29s / p95 240897.63s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 4.96s (p5 1.91s / p95 607.56s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x3
data.boxId  (string, 7/7 records)
    "0"  x3
    "1"  x2
    "2"  x2
data.soilType  (string, 7/7 records)
    "Clay"  x3
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 104410.72s (p5 56332.20s / p95 604983.24s, n=4)
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

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 24804.22s (p5 3342.12s / p95 46266.32s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 4.67s (p5 4.67s / p95 4.67s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit2"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationNodeEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (40 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (8x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (11x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*