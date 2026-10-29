# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba3

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba3
- **Game version string(s) in log:** 2.8.4, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba3.jsonl
- **Records:** 17202 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba3
- **Time span:** 2026-10-05T20:06:22.304000+00:00 .. 2026-10-16T14:08:15.102000+00:00 (258h 1m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba3\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 17202 records, 11 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 103 INFO, 0 NOT_TESTED, 102 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 6062 | 35.24 | 1 | 4 | 0 | 2026-10-06T19:58:51.419000+00:00 | 2026-10-16T00:18:00.262000+00:00 | 220h 19m |
| InputEvent | 3842 | 22.33 | 1 | 9 | 0 | 2026-10-05T20:06:37.816000+00:00 | 2026-10-16T14:08:15.102000+00:00 | 258h 1m |
| PlayerPositionEvent | 3043 | 17.69 | 1 | 9 | 0 | 2026-10-05T20:06:34.300000+00:00 | 2026-10-16T14:08:11.451000+00:00 | 258h 1m |
| DialogueEvent | 2463 | 14.32 | 1 | 9 | 1490 | 2026-10-05T20:06:54.293000+00:00 | 2026-10-16T14:07:13.795000+00:00 | 258h 0m |
| argumentationNodeEvent | 866 | 5.03 | 1 | 5 | 0 | 2026-10-06T19:47:01.944000+00:00 | 2026-10-16T13:49:09.528000+00:00 | 234h 2m |
| ObjectInterEvent | 347 | 2.02 | 1 | 9 | 0 | 2026-10-06T19:26:43.901000+00:00 | 2026-10-16T14:08:15.102000+00:00 | 234h 41m |
| argumentationAnswerEvent | 86 | 0.5 | 1 | 5 | 0 | 2026-10-06T19:47:14.577000+00:00 | 2026-10-16T13:49:11.041000+00:00 | 234h 1m |
| Soil Key Puzzle | 82 | 0.48 | 1 | 3 | 0 | 2026-10-07T19:51:11.185000+00:00 | 2026-10-15T19:27:26.194000+00:00 | 191h 36m |
| questEvent | 82 | 0.48 | 1 | 9 | 82 | 2026-10-05T20:06:54.263000+00:00 | 2026-10-16T13:58:42.561000+00:00 | 257h 51m |
| TopographicMapEvent | 64 | 0.37 | 1 | 3 | 0 | 2026-10-06T19:59:16.870000+00:00 | 2026-10-14T20:06:18.008000+00:00 | 192h 7m |
| DEBUGMenu | 50 | 0.29 | 1 | 9 | 0 | 2026-10-05T20:06:34.289000+00:00 | 2026-10-16T13:43:05.318000+00:00 | 257h 36m |
| WaterChamberEvent | 44 | 0.26 | 1 | 1 | 0 | 2026-10-16T00:05:46.643000+00:00 | 2026-10-16T00:25:31.394000+00:00 | 19m 44s |
| gameWindowFocusEvent | 39 | 0.23 | 1 | 6 | 0 | 2026-10-05T20:06:22.304000+00:00 | 2026-10-16T14:00:36.393000+00:00 | 257h 54m |
| gameStartEvent | 24 | 0.14 | 1 | 1 | 0 | 2026-10-05T20:06:22.305000+00:00 | 2026-10-16T13:43:05.646000+00:00 | 257h 36m |
| TerasGardenBox | 23 | 0.13 | 1 | 1 | 0 | 2026-10-15T21:47:14.369000+00:00 | 2026-10-15T21:57:36.071000+00:00 | 10m 21s |
| gameWindowUnfocusEvent | 23 | 0.13 | 1 | 7 | 0 | 2026-10-05T20:09:51.998000+00:00 | 2026-10-16T14:00:32.661000+00:00 | 257h 50m |
| argumentationEvent | 14 | 0.08 | 1 | 5 | 0 | 2026-10-06T19:46:56.712000+00:00 | 2026-10-16T13:49:11.080000+00:00 | 234h 2m |
| argumentationToolEvent | 14 | 0.08 | 1 | 3 | 0 | 2026-10-06T19:46:56.676000+00:00 | 2026-10-13T19:56:59.561000+00:00 | 168h 10m |
| SolarStillDesignEvent | 10 | 0.06 | 1 | 1 | 0 | 2026-10-16T13:55:37.085000+00:00 | 2026-10-16T13:56:04.857000+00:00 | 27.8s |
| soilMachine | 10 | 0.06 | 1 | 1 | 0 | 2026-10-15T19:40:27.607000+00:00 | 2026-10-15T19:52:52.395000+00:00 | 12m 24s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T19:51:50.919000+00:00 | 2026-10-16T14:08:15.090000+00:00 | 234h 16m |
| chatEvent | 5 | 0.03 | 1 | 2 | 0 | 2026-10-15T22:12:41.046000+00:00 | 2026-10-16T13:43:14.785000+00:00 | 15h 30m |
| DaniEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-10T12:11:41.278000+00:00 | 2026-10-10T12:11:47.781000+00:00 | 6.5s |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 131.248s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 208274.404s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.374s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.05s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.601s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.771s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.495s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 195.298s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 4010.669s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1066.218s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1802.037s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 11.787s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.2x vs baseline. 
  - Observed: 50 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
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
  - Observed: Cold; Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 240 ft; 30 ft; 300 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 17.2x vs baseline. 
  - Observed: 86 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,I; A,2,II; A,3,I; A,B,2,I; A,B,2,II; A,C,1,II; A,C,2,II; A,C,3,II; A,D,2,II; A,D,C,2,II; B,1,II; B,2,II; B,3,I; B,C,1,I; B,D,2,II; C,1,I; C,1,II; C,A,2,II; C,A,4,II; C,B,1,I; C,B,2,II; C,D,2,II; C,D,3,II; C,D,4,II; D,1,I; D,1,II; D,2,I; D,2,II; D,3,I; D,3,II; D,A,2,II; D,B,1,II; D,B,2,II; D,C,2,I; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 866 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 24 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[2] _id=6ac4033ede269131f9af90a9 ts=2026-10-05T20:06:22.3050000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[88] _id=6ac54aeede269131f9b79d5e ts=2026-10-06T19:24:29.0790000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[739] _id=6ac551adde269131f9b7c7ea ts=2026-10-06T19:53:16.9110000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 39 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 39} 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[0] _id=6ac4033ede269131f9af90a4 ts=2026-10-05T20:06:22.3040000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[57] _id=6ac40411de269131f9af955f ts=2026-10-05T20:09:53.7780000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[87] _id=6ac54aeede269131f9b79d5d ts=2026-10-06T19:24:29.0790000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[55] _id=6ac40410de269131f9af954b ts=2026-10-05T20:09:51.9980000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[99] _id=6ac54aeede269131f9b79d5a ts=2026-10-05T20:11:22.429Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[486] _id=6ac54efede269131f9b7ae42 ts=2026-10-06T19:41:49.6380000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 4 of 64 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[860] _id=6ac55315de269131f9b7f6f3 ts=2026-10-06T19:59:16.8700000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[863] _id=6ac55319de269131f9b7f783 ts=2026-10-06T19:59:20.7010000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[866] _id=6ac5531cde269131f9b7f801 ts=2026-10-06T19:59:23.4380000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 6061 | 0.0 | 0.05 | 130.861 | 1.326 | 285325.929 | 0.46 | 3042 | 10 |
| InputEvent | 3841 | 0.0 | 1.374 | 241.837 | 21.209 | 281565.605 | 0.25 | 142 | 14 |
| PlayerPositionEvent | 3031 | 9.752 | 10.001 | 213.379 | 10.092 | 195854.863 | 0.28 | 0 | 9 |
| DialogueEvent | 2462 | 0.0 | 4.912 | 377.262 | 42.13 | 281542.464 | 0.16 | 736 | 12 |
| argumentationNodeEvent | 865 | 0.0 | 0.62 | 974.02 | 13.531 | 321435.629 | 0.06 | 72 | 6 |
| ObjectInterEvent | 346 | 0.0 | 9.308 | 2441.882 | 496.257 | 283027.913 | 0.02 | 5 | 16 |
| argumentationAnswerEvent | 85 | 0.173 | 20.495 | 9911.958 | 1223.709 | 321452.052 | 0.01 | 0 | 6 |
| Soil Key Puzzle | 81 | 0.151 | 1.601 | 8515.741 | 39.842 | 288248.647 | 0.01 | 0 | 4 |
| questEvent | 81 | 0.0 | 227.795 | 11460.596 | 83973.457 | 281687.261 | 0.01 | 14 | 21 |
| TopographicMapEvent | 63 | 0.012 | 4.771 | 10978.113 | 79918.368 | 285018.857 | 0.01 | 3 | 9 |
| DEBUGMenu | 49 | 4.753 | 131.248 | 18926.348 | 84880.211 | 288451.714 | 0.0 | 0 | 20 |
| WaterChamberEvent | 43 | 2.236 | 16.946 | 27.552 | 99.566 | 160.314 | 2.18 | 0 | 0 |
| gameWindowFocusEvent | 38 | 6.677 | 1066.218 | 24433.002 | 102543.896 | 282741.389 | 0.0 | 0 | 23 |
| gameStartEvent | 23 | 41.773 | 2001.704 | 40321.884 | 184908.072 | 288460.881 | 0.0 | 0 | 17 |
| TerasGardenBox | 22 | 0.912 | 2.362 | 28.259 | 49.529 | 428.466 | 2.12 | 0 | 0 |
| gameWindowUnfocusEvent | 22 | 3.111 | 1802.037 | 42192.757 | 191584.242 | 285218.867 | 0.0 | 0 | 14 |
| argumentationEvent | 13 | 0.042 | 195.298 | 64810.336 | 298552.92 | 321414.83 | 0.0 | 2 | 5 |
| argumentationToolEvent | 13 | 0.136 | 11.383 | 46569.453 | 298714.021 | 321491.633 | 0.0 | 0 | 2 |
| SolarStillDesignEvent | 9 | 0.005 | 1.363 | 3.086 | 9.855 | 12.912 | 19.44 | 1 | 0 |
| soilMachine | 9 | 3.841 | 11.787 | 82.754 | 306.598 | 364.535 | 0.73 | 0 | 0 |
| EndOfUnit | 4 | 57357.741 | 208274.404 | 210846.043 | 362348.681 | 369477.622 | 0.0 | 0 | 4 |
| chatEvent | 4 | 460.068 | 4010.669 | 13958.435 | 41223.249 | 47352.332 | 0.0 | 0 | 3 |
| DaniEvent | 1 | 6.503 | 6.503 | 6.503 | 6.503 | 6.503 | 9.23 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 12 group(s), 30 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[286] _id=6ac54d24de269131f9b7a4ac ts=2026-10-06T19:33:55.5540000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[287] _id=6ac54d24de269131f9b7a4ad ts=2026-10-06T19:33:55.5540000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[743] _id=6ac551bbde269131f9b7c841 ts=2026-10-06T19:53:29.7990000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[744] _id=6ac551bbde269131f9b7c842 ts=2026-10-06T19:53:29.7990000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[748] _id=6ac551bbde269131f9b7c845 ts=2026-10-06T19:53:29.8000000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[749] _id=6ac551bbde269131f9b7c846 ts=2026-10-06T19:53:29.8000000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 93 group(s), 155 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[848] _id=6ac552fdde269131f9b7f11c ts=2026-10-06T19:58:51.4190000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[849] _id=6ac552fdde269131f9b7f126 ts=2026-10-06T19:58:51.4190000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[841] _id=6ac552fdde269131f9b7f137 ts=2026-10-06T19:58:51.5900000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[843] _id=6ac552fede269131f9b7f140 ts=2026-10-06T19:58:51.5900000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[912] _id=6ac5536cde269131f9b802a1 ts=2026-10-06T20:00:42.4320000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[907] _id=6ac5536cde269131f9b802a5 ts=2026-10-06T20:00:42.4320000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[16890] _id=6ad22b9dde269131f9e41018 ts=2026-10-16T13:50:21.5080000Z == 6ab9a9439a8420a1e6b56ba3.jsonl[16891] _id=6ad22b9dde269131f9e41019 ts=2026-10-16T13:50:21.5080000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba3.jsonl[155] _id=6ac54b74de269131f9b79e7b ts=2026-10-06T19:26:43.9010000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[149] _id=6ac54b74de269131f9b79e7d ts=2026-10-06T19:26:43.9060000Z`; `622ms: 6ab9a9439a8420a1e6b56ba3.jsonl[1137] _id=6ac55422de269131f9b81bb5 ts=2026-10-06T20:03:46.0620000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[1139] _id=6ac55423de269131f9b81bcb ts=2026-10-06T20:03:46.6840000Z`; `546ms: 6ab9a9439a8420a1e6b56ba3.jsonl[1145] _id=6ac55425de269131f9b81c00 ts=2026-10-06T20:03:48.2630000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[1143] _id=6ac55425de269131f9b81c13 ts=2026-10-06T20:03:48.8090000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `912ms: 6ab9a9439a8420a1e6b56ba3.jsonl[14678] _id=6ad149e8de269131f9e1a18d ts=2026-10-15T21:47:19.2370000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[14680] _id=6ad149e9de269131f9e1a18f ts=2026-10-15T21:47:20.1490000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `277ms: 6ab9a9439a8420a1e6b56ba3.jsonl[2564] _id=6ac6a04ade269131f9bf2700 ts=2026-10-07T19:40:58.1590000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[2549] _id=6ac6a04bde269131f9bf2702 ts=2026-10-07T19:40:58.4360000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `400ms: 6ab9a9439a8420a1e6b56ba3.jsonl[629] _id=6ac5508bde269131f9b7b980 ts=2026-10-06T19:48:26.3440000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[627] _id=6ac5508bde269131f9b7b986 ts=2026-10-06T19:48:26.7440000Z`; `948ms: 6ab9a9439a8420a1e6b56ba3.jsonl[7773] _id=6aca3856de269131f9cb3b35 ts=2026-10-10T13:06:29.8970000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[7761] _id=6aca3857de269131f9cb3b3c ts=2026-10-10T13:06:30.8450000Z`; `880ms: 6ab9a9439a8420a1e6b56ba3.jsonl[7802] _id=6aca388ede269131f9cb3b64 ts=2026-10-10T13:07:25.9830000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[7787] _id=6aca388fde269131f9cb3b66 ts=2026-10-10T13:07:26.8630000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6ab9a9439a8420a1e6b56ba3.jsonl[8929] _id=6ace8d1bde269131f9d23a94 ts=2026-10-13T19:57:14.8270000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[8932] _id=6ace8d1bde269131f9d23a97 ts=2026-10-13T19:57:14.8720000Z`; `42ms: 6ab9a9439a8420a1e6b56ba3.jsonl[14547] _id=6ad14882de269131f9e19309 ts=2026-10-15T21:41:21.3600000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[14550] _id=6ad14882de269131f9e1930c ts=2026-10-15T21:41:21.4020000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 45 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `821ms: 6ab9a9439a8420a1e6b56ba3.jsonl[572] _id=6ac55039de269131f9b7b6e4 ts=2026-10-06T19:47:04.3920000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[584] _id=6ac5503ade269131f9b7b6f1 ts=2026-10-06T19:47:05.2130000Z`; `142ms: 6ab9a9439a8420a1e6b56ba3.jsonl[606] _id=6ac55085de269131f9b7b93b ts=2026-10-06T19:48:21.0490000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[607] _id=6ac55086de269131f9b7b941 ts=2026-10-06T19:48:21.1910000Z`; `219ms: 6ab9a9439a8420a1e6b56ba3.jsonl[602] _id=6ac55085de269131f9b7b93d ts=2026-10-06T19:48:21.0770000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[618] _id=6ac55086de269131f9b7b947 ts=2026-10-06T19:48:21.2960000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `566ms: 6ab9a9439a8420a1e6b56ba3.jsonl[594] _id=6ac5507dde269131f9b7b8dd ts=2026-10-06T19:48:12.7430000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[609] _id=6ac5507ede269131f9b7b8e7 ts=2026-10-06T19:48:13.3090000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba3.jsonl[17058] _id=6ad22d45de269131f9e43d96 ts=2026-10-16T13:57:25.5310000Z ~ 6ab9a9439a8420a1e6b56ba3.jsonl[17059] _id=6ad22d45de269131f9e43d98 ts=2026-10-16T13:57:25.5360000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 80h 7m 
  - Evidence: 80h 7m: 6ab9a9439a8420a1e6b56ba3.jsonl[4958] _id=6aca1fe0de269131f9cb2603 ts=2026-10-10T11:22:07.9330000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8111] _id=6ace86a4de269131f9d1f0a0 ts=2026-10-13T19:29:39.6470000Z; 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4682] _id=6ac6a677de269131f9bf8300 ts=2026-10-07T20:07:18.6060000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4704] _id=6ac9a39ede269131f9cb246a ts=2026-10-10T02:31:57.5680000Z; 23h 42m: 6ab9a9439a8420a1e6b56ba3.jsonl[740] _id=6ac551b8de269131f9b7c82d ts=2026-10-06T19:53:27.4680000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2462] _id=6ac69f28de269131f9bf21d1 ts=2026-10-07T19:36:07.2250000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 78h 12m 
  - Evidence: 78h 12m: 6ab9a9439a8420a1e6b56ba3.jsonl[8110] _id=6aca3af7de269131f9cb3dce ts=2026-10-10T13:17:42.3170000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8139] _id=6ace86bdde269131f9d1f1ad ts=2026-10-13T19:30:04.7810000Z; 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4696] _id=6ac6a69dde269131f9bf8799 ts=2026-10-07T20:07:56.6940000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4701] _id=6ac9a3c6de269131f9cb2487 ts=2026-10-10T02:32:37.9700000Z; 23h 28m: 6ab9a9439a8420a1e6b56ba3.jsonl[2446] _id=6ac555a5de269131f9b84fdf ts=2026-10-06T20:10:12.6700000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2507] _id=6ac69fe0de269131f9bf2418 ts=2026-10-07T19:39:11.4120000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 736 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13442] _id=6ad13e2cde269131f9e144cc ts=2026-10-15T20:30:39.3270000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13443] _id=6ad13e2cde269131f9e144cd ts=2026-10-15T20:30:39.3270000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13449] _id=6ad13e2cde269131f9e144d4 ts=2026-10-15T20:30:52.9540000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13450] _id=6ad13e2cde269131f9e144d5 ts=2026-10-15T20:30:52.9540000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13472] _id=6ad13e2cde269131f9e144eb ts=2026-10-15T20:31:17.4230000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13473] _id=6ad13e2cde269131f9e144ec ts=2026-10-15T20:31:17.4230000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 102h 37m 
  - Evidence: 102h 37m: 6ab9a9439a8420a1e6b56ba3.jsonl[8107] _id=6aca3af6de269131f9cb3dcc ts=2026-10-10T13:17:42.2660000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[10681] _id=6acfde3cde269131f9d93336 ts=2026-10-14T19:55:39.8880000Z; 89h 25m: 6ab9a9439a8420a1e6b56ba3.jsonl[736] _id=6ac55157de269131f9b7c2eb ts=2026-10-06T19:51:50.9190000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8107] _id=6aca3af6de269131f9cb3dcc ts=2026-10-10T13:17:42.2660000Z; 26h 16m: 6ab9a9439a8420a1e6b56ba3.jsonl[10681] _id=6acfde3cde269131f9d93336 ts=2026-10-14T19:55:39.8880000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[15278] _id=6ad14fc2de269131f9e1ccbc ts=2026-10-15T22:12:17.3490000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 78h 12m 
  - Evidence: 78h 12m: 6ab9a9439a8420a1e6b56ba3.jsonl[8093] _id=6aca3ad7de269131f9cb3db5 ts=2026-10-10T13:17:11.0120000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8116] _id=6ace86b5de269131f9d1f133 ts=2026-10-13T19:29:56.6170000Z; 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4692] _id=6ac6a688de269131f9bf8539 ts=2026-10-07T20:07:35.8910000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4721] _id=6ac9a3aede269131f9cb2472 ts=2026-10-10T02:32:13.1240000Z; 23h 26m: 6ab9a9439a8420a1e6b56ba3.jsonl[2434] _id=6ac55590de269131f9b84db2 ts=2026-10-06T20:09:51.7880000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2466] _id=6ac69f3cde269131f9bf2202 ts=2026-10-07T19:36:27.2160000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 142 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[10438] _id=6acfdb91de269131f9d90a19 ts=2026-10-14T19:44:16.3400000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[10439] _id=6acfdb91de269131f9d90a1a ts=2026-10-14T19:44:16.3400000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[11116] _id=6acfe197de269131f9d9629e ts=2026-10-14T20:09:58.6820000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[11117] _id=6acfe197de269131f9d9629f ts=2026-10-14T20:09:58.6820000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[11313] _id=6ad12893de269131f9e0556e ts=2026-10-15T19:25:05.7450000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[11314] _id=6ad12893de269131f9e0556f ts=2026-10-15T19:25:05.7450000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 78h 37m 
  - Evidence: 78h 37m: 6ab9a9439a8420a1e6b56ba3.jsonl[7680] _id=6aca372dde269131f9cb3a84 ts=2026-10-10T13:01:32.5880000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8255] _id=6ace88c0de269131f9d2089a ts=2026-10-13T19:38:40.5010000Z; 64h 2m: 6ab9a9439a8420a1e6b56ba3.jsonl[4409] _id=6ac6a2afde269131f9bf4b1d ts=2026-10-07T19:51:11.1890000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[5419] _id=6aca274ede269131f9cb29a6 ts=2026-10-10T11:53:50.1300000Z; 23h 29m: 6ab9a9439a8420a1e6b56ba3.jsonl[2438] _id=6ac5559cde269131f9b84ef6 ts=2026-10-06T20:10:03.6400000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2458] _id=6ac6a007de269131f9bf24fa ts=2026-10-07T19:39:51.2320000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13186] _id=6ad13267de269131f9e1122f ts=2026-10-15T20:07:03.1310000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13187] _id=6ad13267de269131f9e11230 ts=2026-10-15T20:07:03.1310000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13227] _id=6ad132d9de269131f9e11b23 ts=2026-10-15T20:08:56.7060000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13228] _id=6ad132d9de269131f9e11b24 ts=2026-10-15T20:08:56.7060000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13296] _id=6ad13e2cde269131f9e14476 ts=2026-10-15T20:25:44.7220000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13360] _id=6ad13e2cde269131f9e14477 ts=2026-10-15T20:25:44.7220000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 54h 24m 
  - Evidence: 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4694] _id=6ac6a69ade269131f9bf8734 ts=2026-10-07T20:07:53.6710000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4720] _id=6ac9a3aede269131f9cb2471 ts=2026-10-10T02:32:08.5340000Z; 23h 26m: 6ab9a9439a8420a1e6b56ba3.jsonl[2447] _id=6ac555adde269131f9b85099 ts=2026-10-06T20:10:20.9540000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2465] _id=6ac69f3cde269131f9bf2201 ts=2026-10-07T19:36:24.7390000Z; 23h 13m: 6ab9a9439a8420a1e6b56ba3.jsonl[76] _id=6ac40466de269131f9af9721 ts=2026-10-05T20:11:18.2690000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[92] _id=6ac54afade269131f9b79d71 ts=2026-10-06T19:24:39.9270000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 79h 15m 
  - Evidence: 79h 15m: 6ab9a9439a8420a1e6b56ba3.jsonl[7498] _id=6aca3416de269131f9cb390b ts=2026-10-10T12:48:21.7640000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[9145] _id=6ace8ea5de269131f9d246bd ts=2026-10-13T20:03:47.6930000Z; 64h 8m: 6ab9a9439a8420a1e6b56ba3.jsonl[4392] _id=6ac6a272de269131f9bf48b5 ts=2026-10-07T19:50:08.6920000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[5516] _id=6aca2887de269131f9cb2a6b ts=2026-10-10T11:59:02.6090000Z; 23h 31m: 6ab9a9439a8420a1e6b56ba3.jsonl[2432] _id=6ac5557bde269131f9b84bad ts=2026-10-06T20:09:27.0960000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2544] _id=6ac6a031de269131f9bf2665 ts=2026-10-07T19:40:32.8590000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3042 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[1002] _id=6ac553b4de269131f9b80b35 ts=2026-10-06T20:00:42.4980000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[1003] _id=6ac553b4de269131f9b80b39 ts=2026-10-06T20:00:42.4980000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[1004] _id=6ac553b4de269131f9b80b3f ts=2026-10-06T20:00:45.5280000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[988] _id=6ac553b4de269131f9b80b45 ts=2026-10-06T20:00:45.5280000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[1005] _id=6ac553b4de269131f9b80b47 ts=2026-10-06T20:00:45.6930000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[989] _id=6ac553b4de269131f9b80b49 ts=2026-10-06T20:00:45.6930000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 80h 4m 
  - Evidence: 80h 4m: 6ab9a9439a8420a1e6b56ba3.jsonl[5489] _id=6aca2841de269131f9cb2a36 ts=2026-10-10T11:57:53.0720000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[9090] _id=6ace8e39de269131f9d24316 ts=2026-10-13T20:02:01.7190000Z; 64h 2m: 6ab9a9439a8420a1e6b56ba3.jsonl[4417] _id=6ac6a2b2de269131f9bf4b35 ts=2026-10-07T19:51:14.1850000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[5404] _id=6aca274ede269131f9cb29a4 ts=2026-10-10T11:53:50.1250000Z; 24h 4m: 6ab9a9439a8420a1e6b56ba3.jsonl[9119] _id=6ace8e72de269131f9d2451f ts=2026-10-13T20:02:57.9480000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[10755] _id=6acfe117de269131f9d95ba2 ts=2026-10-14T20:07:50.5140000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56ba3.jsonl[16979] _id=6ad22ce8de269131f9e43566 ts=2026-10-16T13:55:52.8160000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[16987] _id=6ad22ce9de269131f9e43568 ts=2026-10-16T13:55:52.8210000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 79h 10m 
  - Evidence: 79h 10m: 6ab9a9439a8420a1e6b56ba3.jsonl[7186] _id=6aca2f55de269131f9cb369b ts=2026-10-10T12:28:04.4870000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8253] _id=6ace88afde269131f9d207e6 ts=2026-10-13T19:38:23.3440000Z; 54h 28m: 6ab9a9439a8420a1e6b56ba3.jsonl[4671] _id=6ac6a62dde269131f9bf7b9b ts=2026-10-07T20:06:04.9840000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4759] _id=6ac9a450de269131f9cb24c5 ts=2026-10-10T02:34:55.8250000Z; 24h 7m: 6ab9a9439a8420a1e6b56ba3.jsonl[8258] _id=6ace88bbde269131f9d20868 ts=2026-10-13T19:38:35.4290000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[10487] _id=6acfdc0cde269131f9d90faf ts=2026-10-14T19:46:19.1440000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.012s..0.041s shown 
  - Evidence: 12ms: 6ab9a9439a8420a1e6b56ba3.jsonl[5383] _id=6aca26e6de269131f9cb2973 ts=2026-10-10T11:52:06.3210000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[5384] _id=6aca26e6de269131f9cb2974 ts=2026-10-10T11:52:06.3330000Z; 16ms: 6ab9a9439a8420a1e6b56ba3.jsonl[4559] _id=6ac6a4c0de269131f9bf6320 ts=2026-10-07T19:59:59.5700000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4563] _id=6ac6a4c0de269131f9bf6324 ts=2026-10-07T19:59:59.5860000Z; 41ms: 6ab9a9439a8420a1e6b56ba3.jsonl[4554] _id=6ac6a4c0de269131f9bf631b ts=2026-10-07T19:59:59.5290000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4559] _id=6ac6a4c0de269131f9bf6320 ts=2026-10-07T19:59:59.5700000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 89h 17m 
  - Evidence: 89h 17m: 6ab9a9439a8420a1e6b56ba3.jsonl[631] _id=6ac55091de269131f9b7b9b3 ts=2026-10-06T19:48:32.3950000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[7757] _id=6aca383dde269131f9cb3b25 ts=2026-10-10T13:06:04.4470000Z; 78h 43m: 6ab9a9439a8420a1e6b56ba3.jsonl[8013] _id=6aca39a8de269131f9cb3d12 ts=2026-10-10T13:12:07.8470000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8854] _id=6ace8cc4de269131f9d23773 ts=2026-10-13T19:55:48.2480000Z; 48h 33m: 6ab9a9439a8420a1e6b56ba3.jsonl[8928] _id=6ace8d1bde269131f9d23a92 ts=2026-10-13T19:57:14.7910000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13441] _id=6ad13e2cde269131f9e144cb ts=2026-10-15T20:30:39.3040000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 89h 16m 
  - Evidence: 89h 16m: 6ab9a9439a8420a1e6b56ba3.jsonl[632] _id=6ac55091de269131f9b7b9bc ts=2026-10-06T19:48:32.4240000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[7739] _id=6aca3817de269131f9cb3af6 ts=2026-10-10T13:05:27.2540000Z; 78h 41m: 6ab9a9439a8420a1e6b56ba3.jsonl[8024] _id=6aca39a8de269131f9cb3d14 ts=2026-10-10T13:12:07.8830000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8776] _id=6ace8c57de269131f9d2333b ts=2026-10-13T19:53:59.5290000Z; 48h 32m: 6ab9a9439a8420a1e6b56ba3.jsonl[8932] _id=6ace8d1bde269131f9d23a97 ts=2026-10-13T19:57:14.8720000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13411] _id=6ad13e2cde269131f9e144ad ts=2026-10-15T20:29:55.4510000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.042s..0.045s shown 
  - Evidence: 42ms: 6ab9a9439a8420a1e6b56ba3.jsonl[14547] _id=6ad14882de269131f9e19309 ts=2026-10-15T21:41:21.3600000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[14550] _id=6ad14882de269131f9e1930c ts=2026-10-15T21:41:21.4020000Z; 45ms: 6ab9a9439a8420a1e6b56ba3.jsonl[8929] _id=6ace8d1bde269131f9d23a94 ts=2026-10-13T19:57:14.8270000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8932] _id=6ace8d1bde269131f9d23a97 ts=2026-10-13T19:57:14.8720000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 89h 17m 
  - Evidence: 89h 17m: 6ab9a9439a8420a1e6b56ba3.jsonl[625] _id=6ac55088de269131f9b7b966 ts=2026-10-06T19:48:23.3860000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[7741] _id=6aca3823de269131f9cb3afd ts=2026-10-10T13:05:39.0150000Z; 78h 42m: 6ab9a9439a8420a1e6b56ba3.jsonl[8012] _id=6aca399cde269131f9cb3d0e ts=2026-10-10T13:11:55.9990000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8785] _id=6ace8c5fde269131f9d23375 ts=2026-10-13T19:54:06.8580000Z; 48h 32m: 6ab9a9439a8420a1e6b56ba3.jsonl[8923] _id=6ace8d16de269131f9d23a6d ts=2026-10-13T19:57:10.6410000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13415] _id=6ad13e2cde269131f9e144b1 ts=2026-10-15T20:30:03.3520000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 72 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13455] _id=6ad13e2cde269131f9e144da ts=2026-10-15T20:31:00.0000000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13456] _id=6ad13e2cde269131f9e144db ts=2026-10-15T20:31:00.0000000Z; 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[574] _id=6ac5503ade269131f9b7b6f0 ts=2026-10-06T19:47:05.2130000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[584] _id=6ac5503ade269131f9b7b6f1 ts=2026-10-06T19:47:05.2130000Z; 1ms: 6ab9a9439a8420a1e6b56ba3.jsonl[13416] _id=6ad13e2cde269131f9e144b2 ts=2026-10-15T20:30:03.4750000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[13417] _id=6ad13e2cde269131f9e144b3 ts=2026-10-15T20:30:03.4760000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 89h 18m 
  - Evidence: 89h 18m: 6ab9a9439a8420a1e6b56ba3.jsonl[612] _id=6ac55081de269131f9b7b912 ts=2026-10-06T19:48:17.1240000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[7772] _id=6aca3855de269131f9cb3b33 ts=2026-10-10T13:06:28.7570000Z; 78h 45m: 6ab9a9439a8420a1e6b56ba3.jsonl[7983] _id=6aca395bde269131f9cb3ccc ts=2026-10-10T13:10:50.9450000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8880] _id=6ace8ce4de269131f9d23899 ts=2026-10-13T19:56:19.8910000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 13h 9m 
  - Evidence: 13h 9m: 6ab9a9439a8420a1e6b56ba3.jsonl[16569] _id=6ad170fbde269131f9e23e0f ts=2026-10-16T00:34:02.4530000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[16618] _id=6ad229f3de269131f9e3e300 ts=2026-10-16T13:43:14.7850000Z; 1h 48m: 6ab9a9439a8420a1e6b56ba3.jsonl[15284] _id=6ad14fd9de269131f9e1ccef ts=2026-10-15T22:12:41.0460000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[15324] _id=6ad16935de269131f9e21d1b ts=2026-10-16T00:00:52.8230000Z; 25m 29s: 6ab9a9439a8420a1e6b56ba3.jsonl[15324] _id=6ad16935de269131f9e21d1b ts=2026-10-16T00:00:52.8230000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[16419] _id=6ad16f2fde269131f9e23612 ts=2026-10-16T00:26:22.3850000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 80h 7m 
  - Evidence: 80h 7m: 6ab9a9439a8420a1e6b56ba3.jsonl[4957] _id=6aca1fd7de269131f9cb2601 ts=2026-10-10T11:21:59.1060000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8113] _id=6ace86a4de269131f9d1f0a6 ts=2026-10-13T19:29:39.9870000Z; 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4680] _id=6ac6a66cde269131f9bf81cb ts=2026-10-07T20:07:07.7530000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4719] _id=6ac9a39ede269131f9cb246d ts=2026-10-10T02:31:57.7150000Z; 23h 54m: 6ab9a9439a8420a1e6b56ba3.jsonl[8113] _id=6ace86a4de269131f9d1f0a6 ts=2026-10-13T19:29:39.9870000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[9563] _id=6acfd6dcde269131f9d89f21 ts=2026-10-14T19:24:11.0480000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 78h 32m 
  - Evidence: 78h 32m: 6ab9a9439a8420a1e6b56ba3.jsonl[7590] _id=6aca362fde269131f9cb39d0 ts=2026-10-10T12:57:18.5980000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8112] _id=6ace86a4de269131f9d1f0a5 ts=2026-10-13T19:29:39.9870000Z; 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4679] _id=6ac6a66cde269131f9bf81ca ts=2026-10-07T20:07:07.7530000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4718] _id=6ac9a39ede269131f9cb246c ts=2026-10-10T02:31:57.7150000Z; 23h 54m: 6ab9a9439a8420a1e6b56ba3.jsonl[8112] _id=6ace86a4de269131f9d1f0a5 ts=2026-10-13T19:29:39.9870000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[9562] _id=6acfd6dcde269131f9d89f20 ts=2026-10-14T19:24:11.0480000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 79h 13m 
  - Evidence: 79h 13m: 6ab9a9439a8420a1e6b56ba3.jsonl[7582] _id=6aca362dde269131f9cb39ce ts=2026-10-10T12:57:17.0810000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[9554] _id=6ace9050de269131f9d25456 ts=2026-10-13T20:10:55.9480000Z; 54h 45m: 6ab9a9439a8420a1e6b56ba3.jsonl[4677] _id=6ac6a652de269131f9bf7f8c ts=2026-10-07T20:06:41.8510000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4905] _id=6ac9a84ede269131f9cb25d5 ts=2026-10-10T02:51:58.6050000Z; 24h 1m: 6ab9a9439a8420a1e6b56ba3.jsonl[9554] _id=6ace9050de269131f9d25456 ts=2026-10-13T20:10:55.9480000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[11299] _id=6ad12884de269131f9e054cf ts=2026-10-14T20:12:02.463Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 78h 14m 
  - Evidence: 78h 14m: 6ab9a9439a8420a1e6b56ba3.jsonl[8097] _id=6aca3aeede269131f9cb3dc4 ts=2026-10-10T13:17:34.1390000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[8164] _id=6ace8745de269131f9d1f845 ts=2026-10-13T19:32:21.4000000Z; 54h 24m: 6ab9a9439a8420a1e6b56ba3.jsonl[4687] _id=6ac6a67dde269131f9bf83d0 ts=2026-10-07T20:07:23.2100000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[4727] _id=6ac9a3aede269131f9cb2478 ts=2026-10-10T02:32:13.3300000Z; 23h 40m: 6ab9a9439a8420a1e6b56ba3.jsonl[787] _id=6ac5523ede269131f9b7d2d3 ts=2026-10-06T19:55:41.4340000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[2468] _id=6ac69f3cde269131f9bf2204 ts=2026-10-07T19:36:27.2500000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba3.jsonl[16890] _id=6ad22b9dde269131f9e41018 ts=2026-10-16T13:50:21.5080000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[16891] _id=6ad22b9dde269131f9e41019 ts=2026-10-16T13:50:21.5080000Z; 1ms: 6ab9a9439a8420a1e6b56ba3.jsonl[538] _id=6ac54fd5de269131f9b7b3e9 ts=2026-10-06T19:45:24.4100000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[542] _id=6ac54fd5de269131f9b7b3ea ts=2026-10-06T19:45:24.4110000Z; 2ms: 6ab9a9439a8420a1e6b56ba3.jsonl[15919] _id=6ad16af2de269131f9e22561 ts=2026-10-16T00:08:17.3050000Z -> 6ab9a9439a8420a1e6b56ba3.jsonl[15920] _id=6ad16af2de269131f9e22562 ts=2026-10-16T00:08:17.3070000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[523] _id=6ac54f96de269131f9b7b267 ts=2026-10-06T19:44:21.6620000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[641] _id=6ac550b7de269131f9b7ba9c ts=2026-10-06T19:49:10.9560000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[4670] _id=6ac6a62cde269131f9bf7b7a ts=2026-10-07T20:06:03.8720000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[8932] _id=6ace8d1bde269131f9d23a97 ts=2026-10-13T19:57:14.8720000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[14550] _id=6ad14882de269131f9e1930c ts=2026-10-15T21:41:21.4020000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[15284] _id=6ad14fd9de269131f9e1ccef ts=2026-10-15T22:12:41.0460000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[15324] _id=6ad16935de269131f9e21d1b ts=2026-10-16T00:00:52.8230000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[16419] _id=6ad16f2fde269131f9e23612 ts=2026-10-16T00:26:22.3850000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[6863] _id=6aca2a99de269131f9cb3440 ts=2026-10-10T12:07:53.1310000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[12213] _id=6ad12b85de269131f9e095b5 ts=2026-10-15T19:37:41.3920000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[12475] _id=6ad12d32de269131f9e0b7de ts=2026-10-15T19:44:49.8990000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[4684] _id=6ac6a67cde269131f9bf83c9 ts=?`; `6ab9a9439a8420a1e6b56ba3.jsonl[16571] _id=6ad17102de269131f9e23e25 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 168 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[5721] _id=6aca2959de269131f9cb2bf7 ts=2026-10-10T12:02:30.7610000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[5722] _id=6aca2959de269131f9cb2bf9 ts=2026-10-10T12:02:30.7610000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[5725] _id=6aca2959de269131f9cb2bfd ts=2026-10-10T12:02:30.8470000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 839 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[849] _id=6ac552fdde269131f9b7f126 ts=2026-10-06T19:58:51.4190000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[850] _id=6ac552fdde269131f9b7f12a ts=2026-10-06T19:58:51.4190000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[907] _id=6ac5536cde269131f9b802a5 ts=2026-10-06T20:00:42.4320000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[609] _id=6ac5507ede269131f9b7b8e7 ts=2026-10-06T19:48:13.3090000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[611] _id=6ac55080de269131f9b7b905 ts=2026-10-06T19:48:15.8370000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[7788] _id=6aca3894de269131f9cb3b70 ts=2026-10-10T13:07:31.3280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 491 start, 482 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 9 unmatched 'BecameCameraCentered' (totals: 1124 open, 1115 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 39 unmatched 'BecameVisible' (totals: 1931 open, 1892 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 11 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 50 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 534 of 17199 adjacent _id pairs reverse in client time; worst 179.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba3.jsonl[960] _id=6ac553b0de269131f9b80a89 ts=2026-10-06T20:01:51.5490000Z`; `6ab9a9439a8420a1e6b56ba3.jsonl[959] _id=6ac553b1de269131f9b80a99 ts=2026-10-06T19:58:52.4560000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.88s, min -84344.67s, max -0.10s over 17200 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba3\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 6062 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (4038); Unit 4 Dev (1065); Unit 5 Dev - Dungeon (495); Unit 3 Dungeon Dev (464)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.33s, n=6061)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6062/6062 records)
    "BecameVisible"  x1931
    "BecameInvisible"  x1892
    "BecameCameraCentered"  x1124
    "BecameCameraUncentered"  x1115
data.pieceId  (string, 6062/6062 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 6062/6062 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3842 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1017); Unit 4 Dev (488); Unit 3 Dev (479); Unit 4 Dev - Dungeon (454); Unit 3 Dungeon Dev (446); Unit 5 Dev - Dungeon (355); Unit 1 Dev (262); Unit 5 Dev (230); Unit 4 Dev - Anderson Base (111)
- **Intervals:** median 1.37s (p5 0.10s / p95 21.21s, n=3841)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3842/3842 records)
    "pressed"  x3842
data.actionType  (string, 3842/3842 records)
    "Move"  x2807
    "Interact"  x532
    "Jump"  x330
    "Ascend"  x59
    "Hoverboard"  x58
    "Sprint"  x24
    "Descend"  x20
    "Pause"  x6
    "Map"  x4
    "SkipCinematic"  x2
data.key  (string, 3842/3842 records, 4 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3842/3842 records)
    "Player"  x3322
    "Drone"  x520
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 3043 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1101); Unit 4 Dev - Anderson Base (524); Unit 4 Dev (322); Unit 3 Dev (269); Unit 1 Dev (192); Unit 5 Dev (190); Unit 3 Dungeon Dev (160); Unit 5 Dev - Dungeon (154); Unit 4 Dev - Dungeon (131)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.09s, n=3031)
- **Fields under `data`:**

```text
data.position  (object, 3043/3043 records)
data.position.x  (number, 3043/3043 records)
    numeric range -685.194 .. 1557.67 (889 unique)
data.position.y  (number, 3043/3043 records)
    numeric range -115.126 .. 223.093 (606 unique)
data.position.z  (number, 3043/3043 records)
    numeric range -1042.64 .. 2129.67 (889 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2463 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (736); Unit 3 Dev (344); Unit 4 Dev (331); Unit 4 Dev - Anderson Base (275); Unit 5 Dev (242); Unit 1 Dev (195); Unit 3 Dungeon Dev (168); Unit 4 Dev - Dungeon (103); Unit 5 Dev - Dungeon (69)
- **eventKey:** present on 1490 of 2463 records
- **Intervals:** median 4.91s (p5 0.00s / p95 42.13s, n=2462)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1490; [conversationId, dialogueEventType] x973
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2463/2463 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2463/2463 records)
    "DialogueNodeEvent"  x1490
    "DialogueStartEvent"  x491
    "DialogueFinishEvent"  x482
data.nodeId  (number, 1490/2463 records)
    numeric range 0 .. 290 (235 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 866 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (497); Unit 2 Prod (Refactor) (169); Unit 3 Dev (99); Unit 5 Dev (66); Unit 1 Dev (35)
- **Intervals:** median 0.62s (p5 0.03s / p95 13.53s, n=865)
- **Fields under `data`:**

```text
data.actionType  (string, 866/866 records)
    "argumentationNodeHoverEnd"  x360
    "argumentationNodeHoverStart"  x360
    "argumentationNodeAdd"  x83
    "argumentationNodeRemove"  x63
data.argumentationTitle  (string, 866/866 records)
    "Unit 4 - Flooding"  x497
    "Unit 2 – Watershed"  x169
    "Unit 3 - Pollution Upstream"  x99
    "Unit 5"  x66
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x16
data.nodeName  (string, 866/866 records)
    "A"  x143
    "B"  x118
    "I"  x108
    "II"  x99
    "D"  x90
    "C"  x88
    "3"  x61
    "1"  x59
    "2"  x45
    "4"  x40
    "5"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 347 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (129); Unit 4 Dev - Dungeon (80); Unit 3 Dungeon Dev (50); Unit 4 Dev (29); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (11); Unit 5 Dev (11); Unit 1 Dev (10); Unit 5 Dev - Dungeon (9)
- **Intervals:** median 9.31s (p5 1.98s / p95 496.26s, n=346)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 347/347 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 347/347 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationAnswerEvent` — 86 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (51); Unit 2 Prod (Refactor) (21); Unit 1 Dev (6); Unit 3 Dev (5); Unit 5 Dev (3)
- **Intervals:** median 20.50s (p5 0.27s / p95 1223.71s, n=85)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 86/86 records)
    "submitAnswerEvent"  x86
data.answerSubmitted  (string, 86/86 records)
    39 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 86/86 records)
    "Unit 4 - Flooding"  x51
    "Unit 2 – Watershed"  x21
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `Soil Key Puzzle` — 82 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (46); Unit 3 Dev (26); Unit 4 Dev (10)
- **Intervals:** median 1.60s (p5 0.16s / p95 39.84s, n=81)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x72; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/82 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/82 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 72/82 records)
    "RightDrag"  x39
    "LeftDrag"  x33
data.currentSoilType  (string, 72/82 records)
    "CLAYSAND"  x15
    "CLAY"  x14
    "SAND"  x13
    "CLAYROCK"  x11
    "SANDGRAVEL"  x10
    "GRAVEL"  x5
    "BEDROCK"  x4
data.isCorrectSelection  (string, 72/82 records)
    "false"  x53
    "true"  x19
data.waterLevelStatus  (string, 72/82 records)
    "TooHigh"  x33
    "TooLow"  x24
    "Proper"  x15
data.waterRetentionChange  (string, 72/82 records)
    "Increase"  x29
    "Decrease"  x24
    "NoChange"  x19
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 1 Dev (13); Unit 4 Dev (11); Unit 4 Dev - Dungeon (10); Unit 3 Dev (9); Unit 5 Dev (9); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 227.79s (p5 0.01s / p95 83973.46s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x32
data.questID  (string, 82/82 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/82 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 64 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (43); Unit 3 Dev (19); Unit 4 Dev (2)
- **Intervals:** median 4.77s (p5 0.29s / p95 79918.37s, n=63)
- **`data` key-set variants:** [actionType, featureUsed] x36; [actionType, featureUsed, location] x24; [actionType, featureUsed, legendName] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 64/64 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
    "WaypointMoveEvent"  x16
    "WaypointSetEvent"  x7
    "Selected"  x4
    "WaypointResetEvent"  x1
data.featureUsed  (string, 64/64 records)
    "Map"  x36
    "Waypoint"  x24
    "Legend"  x4
data.legendName  (string, 4/64 records)
    "150 ft"  x1
    "240 ft"  x1
    "30 ft"  x1
    "300 ft"  x1
data.location  (object, 24/64 records)
data.location.x  (number, 24/64 records)
    numeric range -348.935 .. 533.974 (21 unique)
data.location.y  (number, 24/64 records)
    numeric range -146.644 .. 350.91 (20 unique)
data.location.z  (number, 24/64 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 50 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (23); Unit 2 Prod (Refactor) (7); Unit 4 Dev (5); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3); Unit 1 Dev (2); Unit 3 Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 131.25s (p5 6.55s / p95 84880.21s, n=49)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "DebugMenuStateChanged"  x50
data.isOpened  (bool, 50/50 records)
    false  x50
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 44 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (44)
- **Intervals:** median 16.95s (p5 2.79s / p95 99.57s, n=43)
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "On"  x26
    "Off"  x18
data.floor  (string, 44/44 records)
    "3"  x24
    "4"  x14
    "2"  x4
    "1"  x2
data.machineNumber  (string, 44/44 records)
    "One"  x40
    "Two"  x4
data.machineType  (string, 44/44 records)
    "Condenser"  x19
    "DualChamber_Condenser"  x13
    "Evaporator"  x8
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 44/44 records)
    "2"  x20
    "3"  x13
    "1"  x6
    "4"  x5
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 39 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (24); Unit 2 Prod (Refactor) (9); Unit 1 Dev (2); Unit 4 Dev (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1066.22s (p5 18.21s / p95 102543.90s, n=38)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 39/39 records)
    true  x39
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 24 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (24)
- **Intervals:** median 2001.70s (p5 57.66s / p95 184908.07s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 23 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (23)
- **Intervals:** median 2.36s (p5 1.23s / p95 49.53s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records, 16 empty-string)
    ""  x16
    "cameraPlaced"  x7
data.boxId  (string, 23/23 records)
    "0"  x12
    "1"  x7
    "2"  x4
data.soilType  (string, 23/23 records)
    "Clay"  x15
    "Gravel"  x4
    "Sand"  x3
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 23 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 4 Dev (4); Unit 1 Dev (3); Transition (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1802.04s (p5 6.64s / p95 191584.24s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 195.30s (p5 0.04s / p95 298552.92s, n=13)
- **Open findings:** 2 — see sections 5-8
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

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3)
- **Intervals:** median 11.38s (p5 0.39s / p95 298714.02s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x11
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Freshwater"  x5
    "Unit 2 – Watershed"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Watershed Graph"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `SolarStillDesignEvent` — 10 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (10)
- **Intervals:** median 1.36s (p5 0.24s / p95 9.85s, n=9)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x9; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "optionSelected"  x9
    "DesignSubmitted"  x1
data.designSelections  (object, 1/10 records)
data.designSelections.glassRoofTemperature  (string, 1/10 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/10 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/10 records)
    "Tilted In"  x1
data.featureUsed  (string, 10/10 records)
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x3
    "RoofStyle"  x3
    "Submit"  x1
data.selectedOption  (string, 9/10 records, 3 empty-string)
    ""  x3
    "Hot"  x2
    "Tilted In"  x2
    "Covered"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `soilMachine` — 10 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (10)
- **Intervals:** median 11.79s (p5 4.12s / p95 306.60s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "ChangeCanister"  x10
data.canisterType  (string, 10/10 records)
    "Gravel"  x4
    "Sand"  x3
    "Clay"  x2
    "Bedrock"  x1
data.floor  (string, 10/10 records)
    "2"  x7
    "3"  x1
    "4"  x1
    "5"  x1
data.machine  (string, 10/10 records)
    "1"  x9
    "2"  x1
data.row  (string, 10/10 records)
    "TopRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 208274.40s (p5 62943.70s / p95 362348.68s, n=4)
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

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 4010.67s (p5 620.49s / p95 41223.25s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x5
data.chatID  (string, 5/5 records)
    "NA"  x5
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 6.50s (p5 6.50s / p95 6.50s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "not granted"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "TypeError: not granted"  x1
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x1
    "unit5"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (46 records)
- `TerasGardenBox` data.actionType: "" (16x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "WaypointMoveEvent" (16x); "WaypointResetEvent" (1x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (4x); "Waypoint" (24x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (63x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*