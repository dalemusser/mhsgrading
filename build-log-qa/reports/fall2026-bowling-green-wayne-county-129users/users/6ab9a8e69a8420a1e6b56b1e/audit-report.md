# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b1e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b1e
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b1e.jsonl
- **Records:** 10124 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b1e
- **Time span:** 2026-10-05T16:31:59.368000+00:00 .. 2026-10-16T16:49:05.715000+00:00 (264h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b1e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 10124 records, 10 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 99 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2755 | 27.21 | 1 | 9 | 0 | 2026-10-05T16:35:44.463000+00:00 | 2026-10-16T16:49:05.715000+00:00 | 264h 13m |
| PuzzlePieceVisibleEvent | 2479 | 24.49 | 1 | 4 | 0 | 2026-10-06T16:41:23.733000+00:00 | 2026-10-16T16:20:23.935000+00:00 | 239h 39m |
| DialogueEvent | 2080 | 20.55 | 1 | 9 | 1279 | 2026-10-05T16:32:30.730000+00:00 | 2026-10-16T16:48:47.554000+00:00 | 264h 16m |
| PlayerPositionEvent | 1830 | 18.08 | 1 | 9 | 0 | 2026-10-05T16:32:10.820000+00:00 | 2026-10-16T16:49:04.425000+00:00 | 264h 16m |
| ObjectInterEvent | 254 | 2.51 | 1 | 9 | 0 | 2026-10-05T16:38:56.017000+00:00 | 2026-10-16T16:49:05.715000+00:00 | 264h 10m |
| argumentationNodeEvent | 213 | 2.1 | 1 | 5 | 0 | 2026-10-05T16:56:01.389000+00:00 | 2026-10-16T16:36:37.570000+00:00 | 263h 40m |
| Soil Key Puzzle | 136 | 1.34 | 1 | 3 | 0 | 2026-10-07T16:55:00.712000+00:00 | 2026-10-15T16:50:20.045000+00:00 | 191h 55m |
| TopographicMapEvent | 128 | 1.26 | 1 | 2 | 0 | 2026-10-06T16:41:51.009000+00:00 | 2026-10-14T16:36:12.228000+00:00 | 191h 54m |
| questEvent | 79 | 0.78 | 1 | 9 | 79 | 2026-10-05T16:32:30.706000+00:00 | 2026-10-16T16:45:07.898000+00:00 | 264h 12m |
| DEBUGMenu | 31 | 0.31 | 1 | 9 | 0 | 2026-10-05T16:32:10.810000+00:00 | 2026-10-16T16:15:51.550000+00:00 | 263h 43m |
| WaterChamberEvent | 24 | 0.24 | 1 | 1 | 0 | 2026-10-16T16:19:40.521000+00:00 | 2026-10-16T16:28:50.922000+00:00 | 9m 10s |
| gameWindowFocusEvent | 16 | 0.16 | 1 | 3 | 0 | 2026-10-05T16:31:59.368000+00:00 | 2026-10-16T16:15:40.302000+00:00 | 263h 43m |
| soilMachine | 15 | 0.15 | 1 | 1 | 0 | 2026-10-15T16:18:53.380000+00:00 | 2026-10-15T16:28:12.663000+00:00 | 9m 19s |
| argumentationEvent | 14 | 0.14 | 1 | 5 | 0 | 2026-10-05T16:55:55.943000+00:00 | 2026-10-16T16:36:38.854000+00:00 | 263h 40m |
| gameStartEvent | 14 | 0.14 | 1 | 1 | 0 | 2026-10-05T16:31:59.369000+00:00 | 2026-10-16T16:15:40.302000+00:00 | 263h 43m |
| argumentationToolEvent | 13 | 0.13 | 1 | 3 | 0 | 2026-10-05T16:55:53.654000+00:00 | 2026-10-13T16:47:18.661000+00:00 | 191h 51m |
| argumentationAnswerEvent | 9 | 0.09 | 1 | 5 | 0 | 2026-10-05T16:56:13.358000+00:00 | 2026-10-16T16:36:38.825000+00:00 | 263h 40m |
| DaniEvent | 8 | 0.08 | 1 | 2 | 0 | 2026-10-07T16:42:26.880000+00:00 | 2026-10-13T16:35:43.014000+00:00 | 143h 53m |
| SolarStillDesignEvent | 7 | 0.07 | 1 | 1 | 0 | 2026-10-16T16:42:20.256000+00:00 | 2026-10-16T16:42:43.039000+00:00 | 22.8s |
| TerasGardenBox | 6 | 0.06 | 1 | 1 | 0 | 2026-10-15T16:50:38.822000+00:00 | 2026-10-15T16:51:29.454000+00:00 | 50.6s |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-05T17:00:24.953000+00:00 | 2026-10-16T16:49:05.688000+00:00 | 263h 48m |
| chatEvent | 4 | 0.04 | 1 | 2 | 0 | 2026-10-15T17:00:00.862000+00:00 | 2026-10-16T16:29:49.391000+00:00 | 23h 29m |
| gameWindowUnfocusEvent | 3 | 0.03 | 1 | 3 | 0 | 2026-10-05T17:04:39.218000+00:00 | 2026-10-15T17:02:32.735000+00:00 | 239h 57m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 158617.411s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.633s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 15.801s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.093s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 3.715s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.936s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.445s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 42985.172s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84876.106s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 83450.907s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 431936.758s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 14.97s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.6x vs baseline. 
  - Observed: 136 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: C,2,II; C,D,3,II; C,D,A,2,II; D,C,2,II 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 3 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[184] _id=6ac3d317de269131f9adee27 ts=2026-10-05T16:40:54.2640000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[239] _id=6ac3d407de269131f9ae000d ts=2026-10-05T16:44:54.0840000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[290] _id=6ac3d498de269131f9ae121d ts=2026-10-05T16:47:19.9610000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[8] _id=6ac3d100de269131f9adc1b5 ts=2026-10-05T16:31:59.3690000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[582] _id=6ac3d807de269131f9ae6735 ts=2026-10-05T17:01:58.1210000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[611] _id=6ac52440de269131f9b521e5 ts=2026-10-06T16:39:27.5790000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[7] _id=6ac3d100de269131f9adc1b3 ts=2026-10-05T16:31:59.3680000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[581] _id=6ac3d807de269131f9ae6729 ts=2026-10-05T17:01:58.1190000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[610] _id=6ac52440de269131f9b521e1 ts=2026-10-06T16:39:27.5780000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 3 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 3} 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[604] _id=6ac3d8a8de269131f9ae738f ts=2026-10-05T17:04:39.2180000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[7006] _id=6acfb177de269131f9d5c20f ts=2026-10-14T16:44:38.1490000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[9038] _id=6ad10729de269131f9de3c05 ts=2026-10-15T17:02:32.7350000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2754 | 0.0 | 1.633 | 345.389 | 22.186 | 287089.472 | 0.17 | 59 | 8 |
| PuzzlePieceVisibleEvent | 2478 | 0.0 | 0.093 | 348.16 | 3.091 | 433006.109 | 0.17 | 945 | 9 |
| DialogueEvent | 2079 | 0.0 | 3.762 | 457.613 | 31.831 | 287124.714 | 0.13 | 590 | 8 |
| PlayerPositionEvent | 1818 | 9.719 | 10.001 | 523.169 | 10.226 | 287084.511 | 0.11 | 0 | 8 |
| ObjectInterEvent | 253 | 0.0 | 15.801 | 3758.932 | 448.334 | 288136.152 | 0.02 | 3 | 10 |
| argumentationNodeEvent | 212 | 0.016 | 0.601 | 4477.529 | 8.551 | 431106.987 | 0.01 | 22 | 4 |
| Soil Key Puzzle | 135 | 0.001 | 1.073 | 5117.921 | 11.875 | 517961.923 | 0.01 | 3 | 4 |
| TopographicMapEvent | 127 | 0.027 | 8.445 | 5439.852 | 587.983 | 288065.337 | 0.01 | 2 | 7 |
| questEvent | 78 | 0.0 | 209.541 | 12194.323 | 84722.515 | 287188.336 | 0.0 | 14 | 14 |
| DEBUGMenu | 30 | 7.168 | 663.01 | 31647.358 | 116875.416 | 289261.982 | 0.0 | 0 | 16 |
| WaterChamberEvent | 23 | 0.165 | 16.946 | 23.93 | 70.756 | 76.242 | 2.51 | 0 | 0 |
| gameWindowFocusEvent | 15 | 135.055 | 83450.907 | 63294.729 | 186138.195 | 289272.411 | 0.0 | 0 | 11 |
| soilMachine | 14 | 3.244 | 14.97 | 39.949 | 150.734 | 190.351 | 1.5 | 0 | 0 |
| argumentationEvent | 13 | 0.045 | 85.554 | 73018.685 | 328002.731 | 431115.441 | 0.0 | 2 | 4 |
| gameStartEvent | 13 | 135.055 | 84876.106 | 73032.379 | 200871.654 | 289272.411 | 0.0 | 0 | 11 |
| argumentationToolEvent | 12 | 2.202 | 19.856 | 57557.084 | 336630.911 | 431141.235 | 0.0 | 0 | 2 |
| argumentationAnswerEvent | 8 | 35.363 | 42985.172 | 118653.183 | 371055.257 | 431200.994 | 0.0 | 0 | 4 |
| DaniEvent | 7 | 0.007 | 3.082 | 73999.448 | 362587.356 | 517978.354 | 0.0 | 2 | 1 |
| SolarStillDesignEvent | 6 | 1.141 | 3.715 | 3.797 | 6.705 | 7.023 | 15.8 | 0 | 0 |
| TerasGardenBox | 5 | 0.821 | 1.936 | 10.126 | 24.445 | 25.219 | 5.93 | 0 | 0 |
| EndOfUnit | 4 | 85776.099 | 158617.411 | 237430.184 | 499163.175 | 546709.813 | 0.0 | 0 | 4 |
| chatEvent | 3 | 138.688 | 838.051 | 28196.176 | 75334.416 | 83611.79 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 2 | 87474.586 | 431936.758 | 431936.758 | 741952.714 | 776398.931 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[2941] _id=6ac7c482de269131f9c424e2 ts=2026-10-08T16:27:44.7220000Z == 6ab9a8e69a8420a1e6b56b1e.jsonl[2942] _id=6ac7c482de269131f9c424e3 ts=2026-10-08T16:27:44.7220000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[6981] _id=6acfb0bbde269131f9d5b1f9 ts=2026-10-14T16:41:30.0810000Z == 6ab9a8e69a8420a1e6b56b1e.jsonl[6982] _id=6acfb0bbde269131f9d5b1fa ts=2026-10-14T16:41:30.0810000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 71 group(s), 101 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[605] _id=6ac524b5de269131f9b526ed ts=2026-10-06T16:41:23.7330000Z == 6ab9a8e69a8420a1e6b56b1e.jsonl[659] _id=6ac524b5de269131f9b526f7 ts=2026-10-06T16:41:23.7330000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[661] _id=6ac524b5de269131f9b526fd ts=2026-10-06T16:41:23.9000000Z == 6ab9a8e69a8420a1e6b56b1e.jsonl[639] _id=6ac524b5de269131f9b526ff ts=2026-10-06T16:41:23.9000000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[642] _id=6ac524b6de269131f9b52709 ts=2026-10-06T16:41:24.0770000Z == 6ab9a8e69a8420a1e6b56b1e.jsonl[648] _id=6ac524b6de269131f9b5270f ts=2026-10-06T16:41:24.0770000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[9888] _id=6ad252dbde269131f9e5fa28 ts=2026-10-16T16:37:46.9490000Z == 6ab9a8e69a8420a1e6b56b1e.jsonl[9889] _id=6ad252dbde269131f9e5fa29 ts=2026-10-16T16:37:46.9490000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[136] _id=6ac3d2a0de269131f9ade589 ts=2026-10-05T16:38:56.0170000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[137] _id=6ac3d2a1de269131f9ade58d ts=2026-10-05T16:38:56.0240000Z`; `214ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[6582] _id=6acface7de269131f9d568b6 ts=2026-10-14T16:25:11.2450000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[6587] _id=6acface8de269131f9d568c8 ts=2026-10-14T16:25:11.4590000Z`; `164ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[6587] _id=6acface8de269131f9d568c8 ts=2026-10-14T16:25:11.4590000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[6592] _id=6acface8de269131f9d568d0 ts=2026-10-14T16:25:11.6230000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 100 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `93ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[773] _id=6ac52519de269131f9b52d23 ts=2026-10-06T16:42:48.9140000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[774] _id=6ac52519de269131f9b52d2b ts=2026-10-06T16:42:49.0070000Z`; `111ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[776] _id=6ac52519de269131f9b52d31 ts=2026-10-06T16:42:57.1870000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[766] _id=6ac52519de269131f9b52d33 ts=2026-10-06T16:42:57.2980000Z`; `107ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[766] _id=6ac52519de269131f9b52d33 ts=2026-10-06T16:42:57.2980000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[757] _id=6ac52519de269131f9b52d37 ts=2026-10-06T16:42:57.4050000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `818ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[2412] _id=6ac67a0ede269131f9bd64d6 ts=2026-10-07T16:57:49.9590000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[2414] _id=6ac67a0fde269131f9bd64f9 ts=2026-10-07T16:57:50.7770000Z`; `370ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[2374] _id=6ac67a0fde269131f9bd64f3 ts=2026-10-07T16:57:50.6210000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[2415] _id=6ac67a0fde269131f9bd6501 ts=2026-10-07T16:57:50.9910000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[1733] _id=6ac528b1de269131f9b5c674 ts=2026-10-06T16:58:25.3380000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[1731] _id=6ac528b2de269131f9b5c69d ts=2026-10-06T16:58:25.3650000Z`; `544ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[4271] _id=6acc30b5de269131f9cb7dcc ts=2026-10-12T00:58:28.5120000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[4280] _id=6acc30b5de269131f9cb7dce ts=2026-10-12T00:58:29.0560000Z`; `918ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[5128] _id=6ace5de3de269131f9cf87f3 ts=2026-10-13T16:35:47.1770000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[5130] _id=6ace5de4de269131f9cf8805 ts=2026-10-13T16:35:48.0950000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `355ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[9524] _id=6ad24fc8de269131f9e5cc24 ts=2026-10-16T16:24:39.6370000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[9527] _id=6ad24fc8de269131f9e5cc2f ts=2026-10-16T16:24:39.9920000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[5647] _id=6ace60a3de269131f9cfbcf0 ts=2026-10-13T16:47:31.0420000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[5650] _id=6ace60a3de269131f9cfbcf3 ts=2026-10-13T16:47:31.0870000Z`; `50ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[8654] _id=6ad10363de269131f9ddd6b5 ts=2026-10-15T16:46:26.8340000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[8657] _id=6ad10363de269131f9ddd6b8 ts=2026-10-15T16:46:26.8840000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[432] _id=6ac3d6a3de269131f9ae42bf ts=2026-10-05T16:56:01.6440000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[391] _id=6ac3d6a3de269131f9ae42c6 ts=2026-10-05T16:56:01.6630000Z`; `51ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[439] _id=6ac3d6a6de269131f9ae430f ts=2026-10-05T16:56:05.0580000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[433] _id=6ac3d6a6de269131f9ae4316 ts=2026-10-05T16:56:05.1090000Z`; `16ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[436] _id=6ac3d6a7de269131f9ae4332 ts=2026-10-05T16:56:06.0970000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[437] _id=6ac3d6a7de269131f9ae4339 ts=2026-10-05T16:56:06.1130000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[9782] _id=6ad25456de269131f9e60d6c ts=2026-10-16T16:44:06.0630000Z ~ 6ab9a8e69a8420a1e6b56b1e.jsonl[9780] _id=6ad25456de269131f9e60d6e ts=2026-10-16T16:44:06.0740000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 80h 21m 
  - Evidence: 80h 21m: 6ab9a8e69a8420a1e6b56b1e.jsonl[2920] _id=6ac7c47ede269131f9c424c6 ts=2026-10-08T16:27:42.3140000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4125] _id=6acc2e6dde269131f9cb79d4 ts=2026-10-12T00:48:44.2960000Z; 39h 25m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4201] _id=6acc2f67de269131f9cb7c2e ts=2026-10-12T00:52:55.1250000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4400] _id=6ace59bfde269131f9cf58d8 ts=2026-10-13T16:18:06.7910000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b1e.jsonl[1828] _id=6ac67371de269131f9bc80df ts=2026-10-07T16:29:36.3340000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[2924] _id=6ac7c474de269131f9c424a5 ts=2026-10-08T16:27:31.8880000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 52m 
  - Evidence: 143h 52m: 6ab9a8e69a8420a1e6b56b1e.jsonl[2053] _id=6ac67677de269131f9bcf4aa ts=2026-10-07T16:42:30.2400000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5118] _id=6ace5dd1de269131f9cf8624 ts=2026-10-13T16:35:28.5940000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.007s..0.009s shown 
  - Evidence: 7ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[5123] _id=6ace5ddcde269131f9cf8736 ts=2026-10-13T16:35:40.0440000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5125] _id=6ace5ddcde269131f9cf8739 ts=2026-10-13T16:35:40.0510000Z; 9ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[5120] _id=6ace5dd4de269131f9cf8662 ts=2026-10-13T16:35:31.6760000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4763] _id=6ace5dd4de269131f9cf8666 ts=2026-10-13T16:35:31.6850000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 79h 45m 
  - Evidence: 79h 45m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4122] _id=6ac7cd09de269131f9c4df32 ts=2026-10-08T17:04:09.0860000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4142] _id=6acc2e9ede269131f9cb7a5f ts=2026-10-12T00:49:33.8000000Z; 39h 15m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4394] _id=6acc320fde269131f9cb80c9 ts=2026-10-12T01:04:15.1200000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4421] _id=6ace5a04de269131f9cf5994 ts=2026-10-13T16:19:15.3490000Z; 23h 35m: 6ab9a8e69a8420a1e6b56b1e.jsonl[599] _id=6ac3d886de269131f9ae7143 ts=2026-10-05T17:04:05.5660000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[613] _id=6ac52465de269131f9b52375 ts=2026-10-06T16:40:04.6890000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 590 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[4045] _id=6ac7cc1fde269131f9c4d080 ts=2026-10-08T17:00:14.6870000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4046] _id=6ac7cc1fde269131f9c4d081 ts=2026-10-08T17:00:14.6870000Z; 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[8601] _id=6ad10295de269131f9ddc565 ts=2026-10-15T16:43:00.4760000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8602] _id=6ad10295de269131f9ddc566 ts=2026-10-15T16:43:00.4760000Z; 1ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[10000] _id=6ad25441de269131f9e60c57 ts=2026-10-16T16:43:44.9370000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[10001] _id=6ad25441de269131f9e60c58 ts=2026-10-16T16:43:44.9380000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 151h 51m 
  - Evidence: 151h 51m: 6ab9a8e69a8420a1e6b56b1e.jsonl[578] _id=6ac3d7a9de269131f9ae5d4f ts=2026-10-05T17:00:24.9530000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4190] _id=6acc2f3fde269131f9cb7c19 ts=2026-10-12T00:52:14.7660000Z; 63h 48m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4190] _id=6acc2f3fde269131f9cb7c19 ts=2026-10-12T00:52:14.7660000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[6975] _id=6acfb0a3de269131f9d5b073 ts=2026-10-14T16:41:06.9950000Z; 24h 18m: 6ab9a8e69a8420a1e6b56b1e.jsonl[6975] _id=6acfb0a3de269131f9d5b073 ts=2026-10-14T16:41:06.9950000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8954] _id=6ad10672de269131f9de2ab8 ts=2026-10-15T16:59:29.5890000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 79h 44m 
  - Evidence: 79h 44m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4123] _id=6ac7cd09de269131f9c4df34 ts=2026-10-08T17:04:09.2860000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4131] _id=6acc2e7cde269131f9cb7a02 ts=2026-10-12T00:48:58.7580000Z; 39h 15m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4384] _id=6acc31f1de269131f9cb8095 ts=2026-10-12T01:03:45.2450000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4410] _id=6ace59e6de269131f9cf58f8 ts=2026-10-13T16:18:45.6630000Z; 23h 36m: 6ab9a8e69a8420a1e6b56b1e.jsonl[561] _id=6ac3d844de269131f9ae6c00 ts=2026-10-05T17:02:59.1300000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[608] _id=6ac5244ede269131f9b52267 ts=2026-10-06T16:39:40.9520000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 59 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[2941] _id=6ac7c482de269131f9c424e2 ts=2026-10-08T16:27:44.7220000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[2942] _id=6ac7c482de269131f9c424e3 ts=2026-10-08T16:27:44.7220000Z; 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[4788] _id=6ace5c7ede269131f9cf7336 ts=2026-10-13T16:29:49.2530000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4789] _id=6ace5c7ede269131f9cf7337 ts=2026-10-13T16:29:49.2530000Z; 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[4923] _id=6ace5d25de269131f9cf7bed ts=2026-10-13T16:32:36.6660000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4924] _id=6ace5d25de269131f9cf7bee ts=2026-10-13T16:32:36.6660000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 80h 2m 
  - Evidence: 80h 2m: 6ab9a8e69a8420a1e6b56b1e.jsonl[3947] _id=6ac7cb35de269131f9c4c0b0 ts=2026-10-08T16:56:21.2280000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4284] _id=6acc30bede269131f9cb7dde ts=2026-10-12T00:58:37.3800000Z; 39h 17m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4381] _id=6acc31d3de269131f9cb804c ts=2026-10-12T01:03:14.7010000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4454] _id=6ace5a6dde269131f9cf5c50 ts=2026-10-13T16:21:00.5320000Z; 24h 6m: 6ab9a8e69a8420a1e6b56b1e.jsonl[1570] _id=6ac52659de269131f9b558c3 ts=2026-10-06T16:48:24.9920000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[2295] _id=6ac67965de269131f9bd5536 ts=2026-10-07T16:55:00.7190000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.007s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[8458] _id=6ad1018ede269131f9ddb0ba ts=2026-10-15T16:38:37.3570000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8459] _id=6ad1018ede269131f9ddb0bb ts=2026-10-15T16:38:37.3570000Z; 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[8507] _id=6ad101dcde269131f9ddb525 ts=2026-10-15T16:39:55.9510000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8508] _id=6ad101dcde269131f9ddb526 ts=2026-10-15T16:39:55.9510000Z; 7ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[136] _id=6ac3d2a0de269131f9ade589 ts=2026-10-05T16:38:56.0170000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[137] _id=6ac3d2a1de269131f9ade58d ts=2026-10-05T16:38:56.0240000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 79h 44m 
  - Evidence: 79h 44m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4124] _id=6ac7cd0cde269131f9c4df3c ts=2026-10-08T17:04:11.8430000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4130] _id=6acc2e7cde269131f9cb7a01 ts=2026-10-12T00:48:56.3540000Z; 39h 13m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4399] _id=6acc321bde269131f9cb80db ts=2026-10-12T01:04:27.0020000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4401] _id=6ace59d4de269131f9cf58e4 ts=2026-10-13T16:18:21.2760000Z; 23h 35m: 6ab9a8e69a8420a1e6b56b1e.jsonl[603] _id=6ac3d89fde269131f9ae72ff ts=2026-10-05T17:04:30.3220000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[607] _id=6ac5244ede269131f9b52265 ts=2026-10-06T16:39:38.7700000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 16m 
  - Evidence: 120h 16m: 6ab9a8e69a8420a1e6b56b1e.jsonl[3458] _id=6ac7c632de269131f9c44b9f ts=2026-10-08T16:34:57.0250000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5766] _id=6ace61a1de269131f9cfcf67 ts=2026-10-13T16:51:43.1340000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b1e.jsonl[1548] _id=6ac52639de269131f9b552db ts=2026-10-06T16:47:50.4250000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[1891] _id=6ac67468de269131f9bc92a2 ts=2026-10-07T16:33:42.9910000Z; 23h 36m: 6ab9a8e69a8420a1e6b56b1e.jsonl[7463] _id=6acfb345de269131f9d5fc35 ts=2026-10-14T16:52:20.0950000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8155] _id=6ad0ff58de269131f9dd8bb6 ts=2026-10-15T16:29:11.2380000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 945 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[1010] _id=6ac5256bde269131f9b534e5 ts=2026-10-06T16:44:24.7030000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[1036] _id=6ac5256cde269131f9b534ed ts=2026-10-06T16:44:24.7030000Z; 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[1018] _id=6ac52569de269131f9b53489 ts=2026-10-06T16:44:23.7800000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[1030] _id=6ac52569de269131f9b5348f ts=2026-10-06T16:44:23.7800000Z; 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[1020] _id=6ac5256ade269131f9b53495 ts=2026-10-06T16:44:23.8490000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[1031] _id=6ac5256ade269131f9b53499 ts=2026-10-06T16:44:23.8490000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 52m 
  - Evidence: 143h 52m: 6ab9a8e69a8420a1e6b56b1e.jsonl[2418] _id=6ac67a11de269131f9bd6529 ts=2026-10-07T16:57:52.4250000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5737] _id=6ace615bde269131f9cfcaf7 ts=2026-10-13T16:50:34.3480000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b1e.jsonl[5743] _id=6ace6175de269131f9cfccce ts=2026-10-13T16:51:00.2890000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[7059] _id=6acfb25ede269131f9d5dd09 ts=2026-10-14T16:48:29.8170000Z; 23h 40m: 6ab9a8e69a8420a1e6b56b1e.jsonl[7085] _id=6acfb290de269131f9d5e4e9 ts=2026-10-14T16:49:19.8650000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8210] _id=6ad0ff97de269131f9dd9105 ts=2026-10-15T16:30:14.7870000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[2321] _id=6ac6798fde269131f9bd587f ts=2026-10-07T16:55:41.9810000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[2322] _id=6ac6798fde269131f9bd5880 ts=2026-10-07T16:55:41.9820000Z; 5ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[7048] _id=6acfb263de269131f9d5dddf ts=2026-10-14T16:48:34.9740000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[7049] _id=6acfb263de269131f9d5ddf1 ts=2026-10-14T16:48:34.9790000Z; 8ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[2319] _id=6ac6798ede269131f9bd586b ts=2026-10-07T16:55:41.6890000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[2320] _id=6ac6798ede269131f9bd5877 ts=2026-10-07T16:55:41.6970000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 80h 1m 
  - Evidence: 80h 1m: 6ab9a8e69a8420a1e6b56b1e.jsonl[3921] _id=6ac7cb5dde269131f9c4c2bb ts=2026-10-08T16:57:01.3790000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4276] _id=6acc309fde269131f9cb7dac ts=2026-10-12T00:58:06.7160000Z; 39h 23m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4272] _id=6acc30b9de269131f9cb7dd6 ts=2026-10-12T00:58:33.0500000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4505] _id=6ace5a9fde269131f9cf5e8b ts=2026-10-13T16:21:51.1270000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b1e.jsonl[2245] _id=6ac67898de269131f9bd434a ts=2026-10-07T16:51:35.4280000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[3627] _id=6ac7c85dde269131f9c48e0b ts=2026-10-08T16:44:13.7490000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.028s shown 
  - Evidence: 27ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[1733] _id=6ac528b1de269131f9b5c674 ts=2026-10-06T16:58:25.3380000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[1731] _id=6ac528b2de269131f9b5c69d ts=2026-10-06T16:58:25.3650000Z; 28ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[1732] _id=6ac528b1de269131f9b5c66d ts=2026-10-06T16:58:25.3100000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[1733] _id=6ac528b1de269131f9b5c674 ts=2026-10-06T16:58:25.3380000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4063] _id=6ac7cc42de269131f9c4d3f0 ts=2026-10-08T17:00:50.0240000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5645] _id=6ace60a3de269131f9cfbcea ts=2026-10-13T16:47:31.0180000Z; 72h 2m: 6ab9a8e69a8420a1e6b56b1e.jsonl[484] _id=6ac3d703de269131f9ae4c4b ts=2026-10-05T16:57:38.6310000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4048] _id=6ac7cc1ede269131f9c4d079 ts=2026-10-08T17:00:14.6610000Z; 47h 55m: 6ab9a8e69a8420a1e6b56b1e.jsonl[5645] _id=6ace60a3de269131f9cfbcea ts=2026-10-13T16:47:31.0180000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8591] _id=6ad10295de269131f9ddc55f ts=2026-10-15T16:43:00.4550000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4066] _id=6ac7cc42de269131f9c4d3f2 ts=2026-10-08T17:00:50.0470000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5597] _id=6ace604ede269131f9cfb621 ts=2026-10-13T16:46:05.4880000Z; 72h 1m: 6ab9a8e69a8420a1e6b56b1e.jsonl[485] _id=6ac3d703de269131f9ae4c4d ts=2026-10-05T16:57:38.6650000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[3989] _id=6ac7cbbfde269131f9c4c95a ts=2026-10-08T16:58:39.5900000Z; 47h 54m: 6ab9a8e69a8420a1e6b56b1e.jsonl[5650] _id=6ace60a3de269131f9cfbcf3 ts=2026-10-13T16:47:31.0870000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8562] _id=6ad10266de269131f9ddc0ed ts=2026-10-15T16:42:14.2050000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.045s..0.050s shown 
  - Evidence: 45ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[5647] _id=6ace60a3de269131f9cfbcf0 ts=2026-10-13T16:47:31.0420000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5650] _id=6ace60a3de269131f9cfbcf3 ts=2026-10-13T16:47:31.0870000Z; 50ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[8654] _id=6ad10363de269131f9ddd6b5 ts=2026-10-15T16:46:26.8340000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8657] _id=6ad10363de269131f9ddd6b8 ts=2026-10-15T16:46:26.8840000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4062] _id=6ac7cc40de269131f9c4d3de ts=2026-10-08T17:00:48.5130000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5589] _id=6ace6044de269131f9cfb5a6 ts=2026-10-13T16:45:55.5000000Z; 72h 1m: 6ab9a8e69a8420a1e6b56b1e.jsonl[486] _id=6ac3d701de269131f9ae4c15 ts=2026-10-05T16:57:36.3330000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[3993] _id=6ac7cbc8de269131f9c4ca1f ts=2026-10-08T16:58:47.9600000Z; 47h 54m: 6ab9a8e69a8420a1e6b56b1e.jsonl[5644] _id=6ace609ade269131f9cfbc5e ts=2026-10-13T16:47:21.8340000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[8563] _id=6ad10268de269131f9ddc10f ts=2026-10-15T16:42:15.9100000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.016s..0.022s shown 
  - Evidence: 16ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[436] _id=6ac3d6a7de269131f9ae4332 ts=2026-10-05T16:56:06.0970000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[437] _id=6ac3d6a7de269131f9ae4339 ts=2026-10-05T16:56:06.1130000Z; 19ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[432] _id=6ac3d6a3de269131f9ae42bf ts=2026-10-05T16:56:01.6440000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[391] _id=6ac3d6a3de269131f9ae42c6 ts=2026-10-05T16:56:01.6630000Z; 22ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[5592] _id=6ace6047de269131f9cfb5c6 ts=2026-10-13T16:45:58.4610000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5593] _id=6ace6047de269131f9cfb5c8 ts=2026-10-13T16:45:58.4830000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4054] _id=6ac7cc32de269131f9c4d21e ts=2026-10-08T17:00:34.5150000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[5606] _id=6ace6058de269131f9cfb70f ts=2026-10-13T16:46:15.7500000Z; 72h 1m: 6ab9a8e69a8420a1e6b56b1e.jsonl[462] _id=6ac3d6ecde269131f9ae4a21 ts=2026-10-05T16:57:15.8130000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[3997] _id=6ac7cbd4de269131f9c4cad3 ts=2026-10-08T16:59:00.0950000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 13m 
  - Evidence: 23h 13m: 6ab9a8e69a8420a1e6b56b1e.jsonl[8959] _id=6ad10691de269131f9de2e0b ts=2026-10-15T17:00:00.8620000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[9108] _id=6ad24d2dde269131f9e5a7f1 ts=2026-10-16T16:13:32.6520000Z; 13m 58s: 6ab9a8e69a8420a1e6b56b1e.jsonl[9155] _id=6ad24db7de269131f9e5a938 ts=2026-10-16T16:15:51.3400000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[9660] _id=6ad250fdde269131f9e5dfca ts=2026-10-16T16:29:49.3910000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 80h 21m 
  - Evidence: 80h 21m: 6ab9a8e69a8420a1e6b56b1e.jsonl[2926] _id=6ac7c474de269131f9c424a8 ts=2026-10-08T16:27:32.0400000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4127] _id=6acc2e6dde269131f9cb79d7 ts=2026-10-12T00:48:44.4510000Z; 39h 25m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4193] _id=6acc2f4dde269131f9cb7c22 ts=2026-10-12T00:52:29.3410000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4405] _id=6ace59c0de269131f9cf58db ts=2026-10-13T16:18:07.1570000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4405] _id=6ace59c0de269131f9cf58db ts=2026-10-13T16:18:07.1570000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[6277] _id=6acfab1ede269131f9d54a7f ts=2026-10-14T16:17:34.0050000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 80h 21m 
  - Evidence: 80h 21m: 6ab9a8e69a8420a1e6b56b1e.jsonl[2925] _id=6ac7c474de269131f9c424a7 ts=2026-10-08T16:27:32.0400000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4126] _id=6acc2e6dde269131f9cb79d6 ts=2026-10-12T00:48:44.4510000Z; 39h 25m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4192] _id=6acc2f4dde269131f9cb7c21 ts=2026-10-12T00:52:29.3410000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4404] _id=6ace59c0de269131f9cf58da ts=2026-10-13T16:18:07.1570000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4404] _id=6ace59c0de269131f9cf58da ts=2026-10-13T16:18:07.1570000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[6276] _id=6acfab1ede269131f9d54a7e ts=2026-10-14T16:17:34.0050000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 39m 
  - Evidence: 215h 39m: 6ab9a8e69a8420a1e6b56b1e.jsonl[604] _id=6ac3d8a8de269131f9ae738f ts=2026-10-05T17:04:39.2180000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[7006] _id=6acfb177de269131f9d5c20f ts=2026-10-14T16:44:38.1490000Z; 24h 17m: 6ab9a8e69a8420a1e6b56b1e.jsonl[7006] _id=6acfb177de269131f9d5c20f ts=2026-10-14T16:44:38.1490000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[9038] _id=6ad10729de269131f9de3c05 ts=2026-10-15T17:02:32.7350000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 79h 46m 
  - Evidence: 79h 46m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4087] _id=6ac7cca6de269131f9c4da5c ts=2026-10-08T17:02:30.4610000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4132] _id=6acc2e7cde269131f9cb7a03 ts=2026-10-12T00:48:58.7970000Z; 39h 22m: 6ab9a8e69a8420a1e6b56b1e.jsonl[4232] _id=6acc3008de269131f9cb7cd8 ts=2026-10-12T00:55:35.8730000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[4402] _id=6ace59d4de269131f9cf58e5 ts=2026-10-13T16:18:25.7630000Z; 23h 35m: 6ab9a8e69a8420a1e6b56b1e.jsonl[600] _id=6ac3d886de269131f9ae713f ts=2026-10-05T17:04:05.4640000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[615] _id=6ac5244ede269131f9b5226b ts=2026-10-06T16:39:40.9990000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[9888] _id=6ad252dbde269131f9e5fa28 ts=2026-10-16T16:37:46.9490000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[9889] _id=6ad252dbde269131f9e5fa29 ts=2026-10-16T16:37:46.9490000Z; 2ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[406] _id=6ac3d652de269131f9ae3aaf ts=2026-10-05T16:54:41.4780000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[404] _id=6ac3d652de269131f9ae3ab2 ts=2026-10-05T16:54:41.4800000Z; 3ms: 6ab9a8e69a8420a1e6b56b1e.jsonl[2943] _id=6ac7c482de269131f9c424e4 ts=2026-10-08T16:27:44.7600000Z -> 6ab9a8e69a8420a1e6b56b1e.jsonl[2944] _id=6ac7c482de269131f9c424e5 ts=2026-10-08T16:27:44.7630000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[397] _id=6ac3d639de269131f9ae35e9 ts=2026-10-05T16:54:16.1390000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[476] _id=6ac3d718de269131f9ae4e17 ts=2026-10-05T16:57:59.2880000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[3422] _id=6ac7c60cde269131f9c44851 ts=2026-10-08T16:34:20.7160000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 20 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[919] _id=6ac52547de269131f9b53165 ts=2026-10-06T16:43:50.4220000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[728] _id=6ac52558de269131f9b53312 ts=2026-10-06T16:44:07.1130000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[995] _id=6ac5255ede269131f9b533b5 ts=2026-10-06T16:44:10.9580000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 54 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[731] _id=6ac52515de269131f9b52c8d ts=2026-10-06T16:41:30.9130000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[722] _id=6ac52515de269131f9b52c92 ts=2026-10-06T16:41:30.9810000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[735] _id=6ac52516de269131f9b52ccb ts=2026-10-06T16:42:45.8500000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[5650] _id=6ace60a3de269131f9cfbcf3 ts=2026-10-13T16:47:31.0870000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[8657] _id=6ad10363de269131f9ddd6b8 ts=2026-10-15T16:46:26.8840000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[391] _id=6ac3d6a3de269131f9ae42c6 ts=2026-10-05T16:56:01.6630000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[433] _id=6ac3d6a6de269131f9ae4316 ts=2026-10-05T16:56:05.1090000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[437] _id=6ac3d6a7de269131f9ae4339 ts=2026-10-05T16:56:06.1130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[8959] _id=6ad10691de269131f9de2e0b ts=2026-10-15T17:00:00.8620000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[9108] _id=6ad24d2dde269131f9e5a7f1 ts=2026-10-16T16:13:32.6520000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[9155] _id=6ad24db7de269131f9e5a938 ts=2026-10-16T16:15:51.3400000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[7825] _id=6ad0fc4fde269131f9dd54af ts=2026-10-15T16:16:14.4920000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[13] _id=6ac3d11dde269131f9adc62f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 139 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[888] _id=6ac52543de269131f9b5308d ts=2026-10-06T16:43:45.1880000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[889] _id=6ac52543de269131f9b53095 ts=2026-10-06T16:43:45.3940000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[890] _id=6ac52543de269131f9b5309b ts=2026-10-06T16:43:45.7660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 313 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[659] _id=6ac524b5de269131f9b526f7 ts=2026-10-06T16:41:23.7330000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[661] _id=6ac524b5de269131f9b526fd ts=2026-10-06T16:41:23.9000000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[639] _id=6ac524b5de269131f9b526ff ts=2026-10-06T16:41:23.9000000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 46 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[1733] _id=6ac528b1de269131f9b5c674 ts=2026-10-06T16:58:25.3380000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[1731] _id=6ac528b2de269131f9b5c69d ts=2026-10-06T16:58:25.3650000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[1789] _id=6ac52973de269131f9b5ecd3 ts=2026-10-06T17:01:38.8910000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[4051] _id=6ac7cc2bde269131f9c4d15b ts=2026-10-08T17:00:26.7710000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[4053] _id=6ac7cc2fde269131f9c4d1c7 ts=2026-10-08T17:00:30.9310000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[4054] _id=6ac7cc32de269131f9c4d21e ts=2026-10-08T17:00:34.5150000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 404 start, 397 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 27 unmatched 'BecameCameraCentered' (totals: 520 open, 513 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 48 unmatched 'BecameVisible' (totals: 720 open, 726 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 48 open, 45 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'argumentationToolOpen' (totals: 12 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 47 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 179 of 10122 adjacent _id pairs reverse in client time; worst 92.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b1e.jsonl[717] _id=6ac52513de269131f9b52c49 ts=2026-10-06T16:42:58.6100000Z`; `6ab9a8e69a8420a1e6b56b1e.jsonl[718] _id=6ac52514de269131f9b52c65 ts=2026-10-06T16:41:26.4160000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.76s, min -94.39s, max -0.23s over 10123 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b1e\coverage.yaml

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

### `InputEvent` — 2755 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (952); Unit 2 Prod (Refactor) (640); Unit 3 Dungeon Dev (319); Unit 4 Dev - Dungeon (304); Unit 5 Dev - Dungeon (146); Unit 1 Dev (125); Unit 4 Dev (117); Unit 4 Dev - Anderson Base (84); Unit 5 Dev (68)
- **Intervals:** median 1.63s (p5 0.13s / p95 22.19s, n=2754)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2755/2755 records)
    "pressed"  x2755
data.actionType  (string, 2755/2755 records)
    "Move"  x1965
    "Interact"  x480
    "Jump"  x135
    "Hoverboard"  x87
    "Ascend"  x32
    "Sprint"  x29
    "Descend"  x20
    "Map"  x6
    "ToggleDebug"  x1
data.key  (string, 2755/2755 records, 36 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2755/2755 records)
    "Player"  x1727
    "Drone"  x1028
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2479 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1542); Unit 4 Dev (380); Unit 5 Dev - Dungeon (303); Unit 3 Dungeon Dev (254)
- **Intervals:** median 0.09s (p5 0.00s / p95 3.09s, n=2478)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2479/2479 records)
    "BecameInvisible"  x726
    "BecameVisible"  x720
    "BecameCameraCentered"  x520
    "BecameCameraUncentered"  x513
data.pieceId  (string, 2479/2479 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2479/2479 records)
    1752 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2080 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (582); Unit 3 Dev (369); Unit 4 Dev (253); Unit 5 Dev (217); Unit 1 Dev (198); Unit 3 Dungeon Dev (195); Unit 4 Dev - Dungeon (114); Unit 4 Dev - Anderson Base (78); Unit 5 Dev - Dungeon (74)
- **eventKey:** present on 1279 of 2080 records
- **Intervals:** median 3.76s (p5 0.01s / p95 31.83s, n=2079)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1279; [conversationId, dialogueEventType] x801
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2080/2080 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2080/2080 records)
    "DialogueNodeEvent"  x1279
    "DialogueStartEvent"  x404
    "DialogueFinishEvent"  x397
data.nodeId  (number, 1279/2080 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1830 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (589); Unit 3 Dev (304); Unit 4 Dev (175); Unit 1 Dev (169); Unit 3 Dungeon Dev (151); Unit 4 Dev - Dungeon (147); Unit 5 Dev - Dungeon (117); Unit 5 Dev (112); Unit 4 Dev - Anderson Base (66)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.23s, n=1818)
- **Fields under `data`:**

```text
data.position  (object, 1830/1830 records)
data.position.x  (number, 1830/1830 records)
    numeric range -698.795 .. 1555.14 (704 unique)
data.position.y  (number, 1830/1830 records)
    numeric range -115.03 .. 222.005 (518 unique)
data.position.z  (number, 1830/1830 records)
    numeric range -1045.13 .. 2067.43 (704 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 254 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (80); Unit 3 Dungeon Dev (62); Unit 2 Prod (Refactor) (39); Unit 4 Dev (20); Unit 5 Dev - Dungeon (12); Unit 3 Dev (11); Unit 5 Dev (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 15.80s (p5 1.86s / p95 448.33s, n=253)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 254/254 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 254/254 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 213 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (59); Unit 3 Dev (43); Unit 2 Prod (Refactor) (41); Unit 5 Dev (40); Unit 1 Dev (30)
- **Intervals:** median 0.60s (p5 0.03s / p95 8.55s, n=212)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 213/213 records)
    "argumentationNodeHoverEnd"  x96
    "argumentationNodeHoverStart"  x93
    "argumentationNodeAdd"  x21
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 213/213 records)
    "Unit 4 - Flooding"  x59
    "Unit 3 - Pollution Upstream"  x43
    "Unit 2 – Watershed"  x41
    "Unit 5"  x40
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x11
data.nodeName  (string, 213/213 records)
    "I"  x37
    "II"  x31
    "A"  x29
    "C"  x26
    "1"  x21
    "B"  x14
    "D"  x14
    "2"  x13
    "4"  x12
    "5"  x9
    "3"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 136 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (100); Unit 4 Dev (30); Unit 3 Dev (6)
- **Intervals:** median 1.07s (p5 0.16s / p95 11.87s, n=135)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x130; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/136 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/136 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 130/136 records)
    "RightDrag"  x70
    "LeftDrag"  x60
data.currentSoilType  (string, 130/136 records)
    "SAND"  x27
    "CLAY"  x24
    "CLAYSAND"  x23
    "SANDGRAVEL"  x22
    "CLAYROCK"  x19
    "GRAVEL"  x10
    "BEDROCK"  x5
data.isCorrectSelection  (string, 130/136 records)
    "false"  x103
    "true"  x27
data.waterLevelStatus  (string, 130/136 records)
    "Proper"  x59
    "TooHigh"  x53
    "TooLow"  x18
data.waterRetentionChange  (string, 130/136 records)
    "Increase"  x63
    "Decrease"  x40
    "NoChange"  x27
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 128 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (74); Unit 2 Prod (Refactor) (54)
- **Intervals:** median 8.45s (p5 1.16s / p95 587.98s, n=127)
- **`data` key-set variants:** [actionType, featureUsed] x93; [actionType, featureUsed, location] x35
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 128/128 records)
    "MapOpenEvent"  x48
    "MapCloseEvent"  x45
    "WaypointMoveEvent"  x28
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x2
data.featureUsed  (string, 128/128 records)
    "Map"  x93
    "Waypoint"  x35
data.location  (object, 35/128 records)
data.location.x  (number, 35/128 records)
    numeric range -347.529 .. 546.594 (30 unique)
data.location.y  (number, 35/128 records)
    numeric range -308.399 .. 307.464 (31 unique)
data.location.z  (number, 35/128 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 79 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 4 Dev - Dungeon (11); Unit 3 Dev (10); Unit 5 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 79 of 79 records
- **Intervals:** median 209.54s (p5 0.01s / p95 84722.51s, n=78)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 79/79 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x32
data.questID  (string, 79/79 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 79/79 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/79 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 31 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (5); Unit 3 Dev (3); Unit 4 Dev (3); Unit 5 Dev - Dungeon (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 663.01s (p5 7.38s / p95 116875.42s, n=30)
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "DebugMenuStateChanged"  x31
data.isOpened  (bool, 31/31 records)
    false  x31
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 24 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (24)
- **Intervals:** median 16.95s (p5 0.59s / p95 70.76s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "On"  x18
    "Off"  x6
data.floor  (string, 24/24 records)
    "3"  x14
    "4"  x5
    "2"  x3
    "1"  x2
data.machineNumber  (string, 24/24 records)
    "One"  x23
    "Two"  x1
data.machineType  (string, 24/24 records)
    "Condenser"  x11
    "DualChamber_Condenser"  x5
    "Evaporator"  x4
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 24/24 records)
    "2"  x12
    "1"  x6
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 16 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 4 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 83450.91s (p5 152.79s / p95 186138.19s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 15 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (15)
- **Intervals:** median 14.97s (p5 3.41s / p95 150.73s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "ChangeCanister"  x15
data.canisterType  (string, 15/15 records)
    "Clay"  x5
    "Gravel"  x4
    "Bedrock"  x3
    "Sand"  x3
data.floor  (string, 15/15 records)
    "5"  x9
    "4"  x5
    "3"  x1
data.machine  (string, 15/15 records)
    "1"  x13
    "2"  x2
data.row  (string, 15/15 records)
    "TopRow"  x11
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 85.55s (p5 0.05s / p95 328002.73s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 84876.11s (p5 188.96s / p95 200871.65s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 1 Dev (3)
- **Intervals:** median 19.86s (p5 2.89s / p95 336630.91s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x12
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 13/13 records)
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - Waterfall Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationAnswerEvent` — 9 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 42985.17s (p5 39.80s / p95 371055.26s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "submitAnswerEvent"  x9
data.answerSubmitted  (string, 9/9 records)
    "A,1,I"  x3
    "A,1,II"  x1
    "A,5,I"  x1
    "C,2,II"  x1
    "C,D,3,II"  x1
    "C,D,A,2,II"  x1
    "D,C,2,II"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 4 - Flooding"  x3
    "Unit 2 – Watershed"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (6); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 3.08s (p5 0.01s / p95 362587.36s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 6 empty-string)
    ""  x6
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 7 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (7)
- **Intervals:** median 3.72s (p5 1.22s / p95 6.71s, n=6)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x6; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "optionSelected"  x6
    "DesignSubmitted"  x1
data.designSelections  (object, 1/7 records)
data.designSelections.glassRoofTemperature  (string, 1/7 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/7 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/7 records)
    "Tilted In"  x1
data.featureUsed  (string, 7/7 records)
    "RoofStyle"  x3
    "GlassRoofTemperature"  x2
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 6/7 records, 1 empty-string)
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.94s (p5 0.92s / p95 24.44s, n=5)
- **Open findings:** 1 — see sections 5-8
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 158617.41s (p5 86035.07s / p95 499163.18s, n=4)
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

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 5 Dev (1)
- **Intervals:** median 838.05s (p5 208.62s / p95 75334.42s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `gameWindowUnfocusEvent` — 3 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (1); Unit 4 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 431936.76s (p5 121920.80s / p95 741952.71s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 3/3 records)
    false  x3
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

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
    "unit1"  x1
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
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (100 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (28x); "WaypointResetEvent" (2x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (35x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*