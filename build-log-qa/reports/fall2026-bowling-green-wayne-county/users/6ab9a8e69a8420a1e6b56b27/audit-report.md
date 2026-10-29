# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b27

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b27
- **Game version string(s) in log:** 2.9.1, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b27.jsonl
- **Records:** 13115 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b27
- **Time span:** 2026-10-07T16:44:37.521000+00:00 .. 2026-10-19T16:16:31.002000+00:00 (287h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b27\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 13115 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 104 INFO, 0 NOT_TESTED, 94 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3662 | 27.92 | 1 | 9 | 0 | 2026-10-07T16:45:04.614000+00:00 | 2026-10-19T16:16:06.368000+00:00 | 287h 31m |
| PuzzlePieceVisibleEvent | 3228 | 24.61 | 1 | 4 | 0 | 2026-10-08T16:57:22.445000+00:00 | 2026-10-16T16:53:06.834000+00:00 | 191h 55m |
| DialogueEvent | 2327 | 17.74 | 1 | 9 | 1444 | 2026-10-07T16:45:05.779000+00:00 | 2026-10-19T16:16:20.158000+00:00 | 287h 31m |
| PlayerPositionEvent | 2120 | 16.16 | 1 | 9 | 0 | 2026-10-07T16:44:45.916000+00:00 | 2026-10-19T16:16:31.002000+00:00 | 287h 31m |
| argumentationNodeEvent | 741 | 5.65 | 1 | 5 | 0 | 2026-10-08T16:45:41.953000+00:00 | 2026-10-19T16:13:30.401000+00:00 | 263h 27m |
| ObjectInterEvent | 379 | 2.89 | 1 | 9 | 0 | 2026-10-07T16:49:47.817000+00:00 | 2026-10-19T16:09:30.643000+00:00 | 287h 19m |
| Soil Key Puzzle | 119 | 0.91 | 1 | 3 | 0 | 2026-10-13T16:21:32.808000+00:00 | 2026-10-16T16:04:29.293000+00:00 | 71h 42m |
| questEvent | 94 | 0.72 | 1 | 9 | 94 | 2026-10-07T16:45:05.758000+00:00 | 2026-10-19T16:16:00.717000+00:00 | 287h 30m |
| TopographicMapEvent | 90 | 0.69 | 1 | 4 | 0 | 2026-10-08T16:29:31.374000+00:00 | 2026-10-15T17:01:02.521000+00:00 | 168h 31m |
| argumentationAnswerEvent | 84 | 0.64 | 1 | 5 | 0 | 2026-10-08T16:45:53.772000+00:00 | 2026-10-19T16:13:32.155000+00:00 | 263h 27m |
| soilMachine | 68 | 0.52 | 1 | 1 | 0 | 2026-10-15T16:31:01.411000+00:00 | 2026-10-15T17:01:51.811000+00:00 | 30m 50s |
| WaterChamberEvent | 54 | 0.41 | 1 | 1 | 0 | 2026-10-16T16:51:43.857000+00:00 | 2026-10-19T16:03:10.402000+00:00 | 71h 11m |
| DEBUGMenu | 43 | 0.33 | 1 | 9 | 0 | 2026-10-07T16:44:37.521000+00:00 | 2026-10-19T16:15:48.799000+00:00 | 287h 31m |
| gameWindowFocusEvent | 22 | 0.17 | 1 | 3 | 0 | 2026-10-07T16:44:37.867000+00:00 | 2026-10-19T16:15:48.938000+00:00 | 287h 31m |
| gameStartEvent | 19 | 0.14 | 1 | 1 | 0 | 2026-10-07T16:44:37.867000+00:00 | 2026-10-19T16:15:48.938000+00:00 | 287h 31m |
| argumentationEvent | 15 | 0.11 | 1 | 5 | 0 | 2026-10-08T16:45:36.866000+00:00 | 2026-10-19T16:13:32.191000+00:00 | 263h 27m |
| TerasGardenBox | 11 | 0.08 | 1 | 1 | 0 | 2026-10-16T16:38:36.008000+00:00 | 2026-10-16T16:39:18.594000+00:00 | 42.6s |
| gameWindowUnfocusEvent | 11 | 0.08 | 1 | 5 | 0 | 2026-10-07T17:03:38.056000+00:00 | 2026-10-15T17:05:13.899000+00:00 | 192h 1m |
| argumentationToolEvent | 9 | 0.07 | 1 | 2 | 0 | 2026-10-08T16:47:11.780000+00:00 | 2026-10-14T16:47:47.511000+00:00 | 144h 0m |
| DaniEvent | 8 | 0.06 | 1 | 2 | 0 | 2026-10-14T16:33:55.179000+00:00 | 2026-10-15T17:01:28.488000+00:00 | 24h 27m |
| chatEvent | 6 | 0.05 | 1 | 3 | 0 | 2026-10-14T16:33:57.829000+00:00 | 2026-10-19T16:15:58.117000+00:00 | 119h 42m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-08T16:50:06.904000+00:00 | 2026-10-16T16:46:06.579000+00:00 | 191h 55m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 140233.387s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.223s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.063s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.44s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.826s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 5.93s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 138.966s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.52s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1817.37s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 16492.693s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.887s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.1x vs baseline. 
  - Observed: 119 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 16.8x vs baseline. 
  - Observed: 84 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,4,II; A,B,2,II; A,B,D,2,II; A,C,2,II; A,C,B,2,II; A,D,C,2,II; B,1,II; B,2,II; B,C,2,II; B,D,2,II; C,1,II; C,2,II; C,3,II; C,4,II; C,A,2,II; C,B,2,II; C,D,3,II; C,D,4,3,II; D,1,II; D,2,II; D,3,II; D,4,II; D,A,B,2,II; D,B,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.3x vs baseline. 
  - Observed: 741 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [23-36, 23-38, 23-39, 23-41, 23-42] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 13.6x vs baseline. 
  - Observed: 68 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[3] _id=6ac676f6de269131f9bd0b1a ts=2026-10-07T16:44:37.8670000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[294] _id=6ac7c4e1de269131f9c42959 ts=2026-10-08T16:29:21.4890000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[311] _id=6ac7c50fde269131f9c42c11 ts=2026-10-08T16:30:07.2670000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[2] _id=6ac676f6de269131f9bd0b19 ts=2026-10-07T16:44:37.8670000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[293] _id=6ac7c4e1de269131f9c42958 ts=2026-10-08T16:29:21.4890000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[308] _id=6ac7c4fcde269131f9c42b01 ts=2026-10-08T16:29:48.0050000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[291] _id=6ac7c4e1de269131f9c42953 ts=2026-10-07T17:03:38.056Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[307] _id=6ac7c4fade269131f9c42ae0 ts=2026-10-08T16:29:46.2620000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[309] _id=6ac7c4fcde269131f9c42b14 ts=2026-10-08T16:29:48.7440000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 17 of 90 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[304] _id=6ac7c4ecde269131f9c42a1e ts=2026-10-08T16:29:31.3740000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[306] _id=6ac7c4edde269131f9c42a27 ts=2026-10-08T16:29:33.7800000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[303] _id=6ac7c4f1de269131f9c42a50 ts=2026-10-08T16:29:37.1100000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3661 | 0.0 | 1.152 | 282.727 | 19.648 | 429459.286 | 0.21 | 68 | 9 |
| PuzzlePieceVisibleEvent | 3227 | 0.0 | 0.063 | 214.114 | 2.347 | 429634.967 | 0.28 | 1489 | 10 |
| DialogueEvent | 2326 | 0.0 | 3.659 | 445.002 | 30.562 | 429563.545 | 0.13 | 674 | 9 |
| PlayerPositionEvent | 2108 | 9.791 | 10.001 | 490.899 | 10.119 | 429457.215 | 0.12 | 0 | 8 |
| argumentationNodeEvent | 740 | 0.0 | 0.504 | 1281.714 | 8.359 | 518390.52 | 0.05 | 70 | 4 |
| ObjectInterEvent | 378 | 0.0 | 12.223 | 2736.463 | 298.63 | 429603.28 | 0.02 | 6 | 14 |
| Soil Key Puzzle | 118 | 0.006 | 0.766 | 2187.936 | 247.0 | 136749.117 | 0.03 | 5 | 6 |
| questEvent | 93 | 0.0 | 163.653 | 11129.623 | 63410.508 | 430065.073 | 0.01 | 19 | 17 |
| TopographicMapEvent | 89 | 0.023 | 3.826 | 6816.754 | 1739.558 | 429965.936 | 0.01 | 2 | 7 |
| argumentationAnswerEvent | 83 | 0.055 | 5.93 | 11427.209 | 379.039 | 518392.896 | 0.01 | 0 | 4 |
| soilMachine | 67 | 0.115 | 3.887 | 27.618 | 147.966 | 339.406 | 2.17 | 0 | 0 |
| WaterChamberEvent | 53 | 1.518 | 10.947 | 4835.595 | 70.01 | 255182.022 | 0.01 | 0 | 1 |
| DEBUGMenu | 42 | 6.544 | 510.803 | 24644.554 | 85326.292 | 430133.184 | 0.0 | 0 | 19 |
| gameWindowFocusEvent | 21 | 19.262 | 1817.37 | 49289.099 | 256260.546 | 430142.656 | 0.0 | 0 | 16 |
| gameStartEvent | 18 | 45.778 | 2297.38 | 57503.948 | 282342.862 | 430142.656 | 0.0 | 0 | 16 |
| argumentationEvent | 14 | 0.037 | 138.966 | 67748.238 | 348980.499 | 518374.294 | 0.0 | 1 | 5 |
| TerasGardenBox | 10 | 0.157 | 1.44 | 4.259 | 16.382 | 19.01 | 14.09 | 0 | 0 |
| gameWindowUnfocusEvent | 10 | 2.482 | 16492.693 | 69129.584 | 275620.769 | 432100.139 | 0.0 | 0 | 8 |
| argumentationToolEvent | 8 | 0.073 | 0.52 | 64804.466 | 336981.448 | 518432.451 | 0.0 | 0 | 1 |
| DaniEvent | 7 | 2.243 | 6.278 | 12579.044 | 60906.374 | 86241.603 | 0.0 | 0 | 2 |
| chatEvent | 5 | 4.885 | 710.566 | 86184.058 | 239716.091 | 256258.444 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 32144.788 | 140233.387 | 230319.892 | 480746.689 | 518581.5 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 7 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[297] _id=6ac7c4ecde269131f9c42a19 ts=2026-10-08T16:29:31.3710000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[298] _id=6ac7c4ecde269131f9c42a1a ts=2026-10-08T16:29:31.3710000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[2656] _id=6ace5fb5de269131f9cfad67 ts=2026-10-13T16:43:32.2210000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[2657] _id=6ace5fb5de269131f9cfad68 ts=2026-10-13T16:43:32.2210000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[5200] _id=6acfb169de269131f9d5c0ea ts=2026-10-14T16:44:25.3680000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[5201] _id=6acfb169de269131f9d5c0eb ts=2026-10-14T16:44:25.3680000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 75 group(s), 121 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[1715] _id=6ace5b2ede269131f9cf6357 ts=2026-10-13T16:24:13.6550000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[1717] _id=6ace5b2ede269131f9cf635e ts=2026-10-13T16:24:13.6550000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[1719] _id=6ace5b30de269131f9cf636a ts=2026-10-13T16:24:15.2860000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[1723] _id=6ace5b30de269131f9cf636c ts=2026-10-13T16:24:15.2860000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[1724] _id=6ace5b30de269131f9cf636d ts=2026-10-13T16:24:15.4100000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[1725] _id=6ace5b30de269131f9cf636e ts=2026-10-13T16:24:15.4100000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[13085] _id=6ad641fede269131f9e9a97c ts=2026-10-19T16:14:53.5410000Z == 6ab9a8e69a8420a1e6b56b27.jsonl[13086] _id=6ad641fede269131f9e9a97d ts=2026-10-19T16:14:53.5410000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 40 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b27.jsonl[56] _id=6ac6782cde269131f9bd35b8 ts=2026-10-07T16:49:47.8170000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[57] _id=6ac6782cde269131f9bd35c4 ts=2026-10-07T16:49:47.8210000Z`; `11ms: 6ab9a8e69a8420a1e6b56b27.jsonl[324] _id=6ac7c53ede269131f9c43043 ts=2026-10-08T16:30:54.6810000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[325] _id=6ac7c53fde269131f9c43050 ts=2026-10-08T16:30:54.6920000Z`; `863ms: 6ab9a8e69a8420a1e6b56b27.jsonl[770] _id=6ac7cabdde269131f9c4b851 ts=2026-10-08T16:54:20.8500000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[772] _id=6ac7cabdde269131f9c4b863 ts=2026-10-08T16:54:21.7130000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `309ms: 6ab9a8e69a8420a1e6b56b27.jsonl[11673] _id=6ad25327de269131f9e5fdec ts=2026-10-16T16:39:02.9470000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[11659] _id=6ad25327de269131f9e5fdf2 ts=2026-10-16T16:39:03.2560000Z`; `157ms: 6ab9a8e69a8420a1e6b56b27.jsonl[11659] _id=6ad25327de269131f9e5fdf2 ts=2026-10-16T16:39:03.2560000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[11660] _id=6ad25327de269131f9e5fdf6 ts=2026-10-16T16:39:03.4130000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `264ms: 6ab9a8e69a8420a1e6b56b27.jsonl[2658] _id=6ace5fa4de269131f9cfac1d ts=2026-10-13T16:43:15.6240000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[2659] _id=6ace5fa4de269131f9cfac23 ts=2026-10-13T16:43:15.8880000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 27 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `946ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10783] _id=6ad24f20de269131f9e5c0d1 ts=2026-10-16T16:21:52.2510000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[10791] _id=6ad24f21de269131f9e5c0e4 ts=2026-10-16T16:21:53.1970000Z`; `122ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10839] _id=6ad24f5bde269131f9e5c497 ts=2026-10-16T16:22:51.4730000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[10865] _id=6ad24f5cde269131f9e5c49b ts=2026-10-16T16:22:51.5950000Z`; `831ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10888] _id=6ad24f75de269131f9e5c628 ts=2026-10-16T16:23:16.9780000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[10886] _id=6ad24f76de269131f9e5c63a ts=2026-10-16T16:23:17.8090000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6ab9a8e69a8420a1e6b56b27.jsonl[6123] _id=6acfdeebde269131f9d93d9f ts=2026-10-14T19:58:34.1670000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[6126] _id=6acfdeebde269131f9d93da2 ts=2026-10-14T19:58:34.2040000Z`; `57ms: 6ab9a8e69a8420a1e6b56b27.jsonl[11540] _id=6ad2522ede269131f9e5f016 ts=2026-10-16T16:34:53.9340000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[11543] _id=6ad2522ede269131f9e5f01e ts=2026-10-16T16:34:53.9910000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 40 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `748ms: 6ab9a8e69a8420a1e6b56b27.jsonl[5275] _id=6acfb20ade269131f9d5d218 ts=2026-10-14T16:47:06.2170000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[5278] _id=6acfb20bde269131f9d5d22e ts=2026-10-14T16:47:06.9650000Z`; `253ms: 6ab9a8e69a8420a1e6b56b27.jsonl[5292] _id=6acfb224de269131f9d5d54c ts=2026-10-14T16:47:31.8740000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[5296] _id=6acfb224de269131f9d5d555 ts=2026-10-14T16:47:32.1270000Z`; `469ms: 6ab9a8e69a8420a1e6b56b27.jsonl[5294] _id=6acfb224de269131f9d5d54e ts=2026-10-14T16:47:31.9420000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[5295] _id=6acfb224de269131f9d5d55e ts=2026-10-14T16:47:32.4110000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `650ms: 6ab9a8e69a8420a1e6b56b27.jsonl[599] _id=6ac7c910de269131f9c4a0f0 ts=2026-10-08T16:47:11.7800000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[606] _id=6ac7c910de269131f9c4a0fe ts=2026-10-08T16:47:12.4300000Z`; `649ms: 6ab9a8e69a8420a1e6b56b27.jsonl[606] _id=6ac7c910de269131f9c4a0fe ts=2026-10-08T16:47:12.4300000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[603] _id=6ac7c911de269131f9c4a10b ts=2026-10-08T16:47:13.0790000Z`; `661ms: 6ab9a8e69a8420a1e6b56b27.jsonl[604] _id=6ac7c911de269131f9c4a107 ts=2026-10-08T16:47:12.9440000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[602] _id=6ac7c911de269131f9c4a117 ts=2026-10-08T16:47:13.6050000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8e69a8420a1e6b56b27.jsonl[13100] _id=6ad64242de269131f9e9aa26 ts=2026-10-19T16:16:00.7100000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[13101] _id=6ad64242de269131f9e9aa27 ts=2026-10-19T16:16:00.7170000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `203ms: 6ab9a8e69a8420a1e6b56b27.jsonl[9040] _id=6ad101efde269131f9ddb676 ts=2026-10-15T16:40:14.4450000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[9041] _id=6ad101efde269131f9ddb67d ts=2026-10-15T16:40:14.6480000Z`; `115ms: 6ab9a8e69a8420a1e6b56b27.jsonl[9041] _id=6ad101efde269131f9ddb67d ts=2026-10-15T16:40:14.6480000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[9031] _id=6ad101efde269131f9ddb681 ts=2026-10-15T16:40:14.7630000Z`; `129ms: 6ab9a8e69a8420a1e6b56b27.jsonl[9031] _id=6ad101efde269131f9ddb681 ts=2026-10-15T16:40:14.7630000Z ~ 6ab9a8e69a8420a1e6b56b27.jsonl[9034] _id=6ad101efde269131f9ddb685 ts=2026-10-15T16:40:14.8920000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 28m 
  - Evidence: 119h 28m: 6ab9a8e69a8420a1e6b56b27.jsonl[714] _id=6ac7ca1dde269131f9c4b032 ts=2026-10-08T16:51:41.1070000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1653] _id=6ace5a53de269131f9cf5baa ts=2026-10-13T16:20:34.2910000Z; 71h 10m: 6ab9a8e69a8420a1e6b56b27.jsonl[11834] _id=6ad254e8de269131f9e61470 ts=2026-10-16T16:46:29.6460000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12652] _id=6ad63de2de269131f9e98a4a ts=2026-10-19T15:57:21.1020000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b27.jsonl[4] _id=6ac676fede269131f9bd0c4d ts=2026-10-07T16:44:45.8920000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[292] _id=6ac7c4e1de269131f9c42957 ts=2026-10-08T16:29:21.3340000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 57m 
  - Evidence: 23h 57m: 6ab9a8e69a8420a1e6b56b27.jsonl[4849] _id=6acfaef5de269131f9d58c46 ts=2026-10-14T16:33:57.4220000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[8745] _id=6ad0ffd7de269131f9dd94cf ts=2026-10-15T16:31:19.0250000Z; 29m 50s: 6ab9a8e69a8420a1e6b56b27.jsonl[8746] _id=6ad0ffddde269131f9dd9530 ts=2026-10-15T16:31:25.3030000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[9975] _id=6ad106dcde269131f9de34cd ts=2026-10-15T17:01:16.1410000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8e69a8420a1e6b56b27.jsonl[1494] _id=6ac7cc84de269131f9c4d8b3 ts=2026-10-08T17:01:56.2330000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1667] _id=6ace5a80de269131f9cf5d27 ts=2026-10-13T16:21:19.7780000Z; 70h 57m: 6ab9a8e69a8420a1e6b56b27.jsonl[12548] _id=6ad2582cde269131f9e653ef ts=2026-10-16T17:00:28.4020000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12660] _id=6ad63df5de269131f9e98ac4 ts=2026-10-19T15:57:40.1360000Z; 23h 26m: 6ab9a8e69a8420a1e6b56b27.jsonl[289] _id=6ac67b66de269131f9bd8b92 ts=2026-10-07T17:03:33.5320000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[319] _id=6ac7c526de269131f9c42df8 ts=2026-10-08T16:30:29.8820000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 674 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10589] _id=6ad24d7cde269131f9e5a8cc ts=2026-10-16T16:14:52.4020000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10590] _id=6ad24d7cde269131f9e5a8cd ts=2026-10-16T16:14:52.4020000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10773] _id=6ad24f16de269131f9e5c00a ts=2026-10-16T16:21:42.1090000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10774] _id=6ad24f16de269131f9e5c00b ts=2026-10-16T16:21:42.1090000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10841] _id=6ad24f4cde269131f9e5c3c2 ts=2026-10-16T16:22:35.3760000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10842] _id=6ad24f4cde269131f9e5c3c3 ts=2026-10-16T16:22:35.3760000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 3m 
  - Evidence: 144h 3m: 6ab9a8e69a8420a1e6b56b27.jsonl[708] _id=6ac7c9bfde269131f9c4aca9 ts=2026-10-08T16:50:06.9040000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[5432] _id=6acfb374de269131f9d6008c ts=2026-10-14T16:53:08.4040000Z; 38h 57m: 6ab9a8e69a8420a1e6b56b27.jsonl[7570] _id=6ad03105de269131f9da1f43 ts=2026-10-15T01:48:53.1920000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[11830] _id=6ad254cfde269131f9e61390 ts=2026-10-16T16:46:06.5790000Z; 8h 55m: 6ab9a8e69a8420a1e6b56b27.jsonl[5432] _id=6acfb374de269131f9d6008c ts=2026-10-14T16:53:08.4040000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[7570] _id=6ad03105de269131f9da1f43 ts=2026-10-15T01:48:53.1920000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b27.jsonl[1634] _id=6ac7ccd8de269131f9c4dcd8 ts=2026-10-08T17:03:19.7500000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1658] _id=6ace5a6cde269131f9cf5c49 ts=2026-10-13T16:20:59.0360000Z; 70h 52m: 6ab9a8e69a8420a1e6b56b27.jsonl[12531] _id=6ad25941de269131f9e661c2 ts=2026-10-16T17:05:04.7710000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12667] _id=6ad63e00de269131f9e98b18 ts=2026-10-19T15:57:51.5620000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b27.jsonl[255] _id=6ac67aadde269131f9bd76f1 ts=2026-10-07T17:00:29.3770000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[296] _id=6ac7c4ecde269131f9c42a18 ts=2026-10-08T16:29:31.3680000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 68 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10001] _id=6ad1070ade269131f9de3913 ts=2026-10-15T17:02:02.0050000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10002] _id=6ad1070ade269131f9de3914 ts=2026-10-15T17:02:02.0050000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10006] _id=6ad1070ade269131f9de391b ts=2026-10-15T17:02:02.1590000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10007] _id=6ad1070ade269131f9de391c ts=2026-10-15T17:02:02.1590000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10011] _id=6ad1070bde269131f9de3922 ts=2026-10-15T17:02:02.4140000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10012] _id=6ad1070bde269131f9de3923 ts=2026-10-15T17:02:02.4140000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b27.jsonl[1638] _id=6ac7ccd4de269131f9c4dcb3 ts=2026-10-08T17:03:16.2790000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1687] _id=6ace5af8de269131f9cf61c1 ts=2026-10-13T16:23:19.5590000Z; 70h 59m: 6ab9a8e69a8420a1e6b56b27.jsonl[12452] _id=6ad257dade269131f9e64dc2 ts=2026-10-16T16:59:05.8010000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12679] _id=6ad63e22de269131f9e98c31 ts=2026-10-19T15:58:24.9790000Z; 23h 30m: 6ab9a8e69a8420a1e6b56b27.jsonl[260] _id=6ac67ac0de269131f9bd7946 ts=2026-10-07T17:00:47.7090000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[324] _id=6ac7c53ede269131f9c43043 ts=2026-10-08T16:30:54.6810000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10432] _id=6ad24bb8de269131f9e5985e ts=2026-10-16T16:07:19.9100000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10433] _id=6ad24bb8de269131f9e5985f ts=2026-10-16T16:07:19.9100000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10477] _id=6ad24c0ade269131f9e59d3d ts=2026-10-16T16:08:41.5250000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10478] _id=6ad24c0ade269131f9e59d3e ts=2026-10-16T16:08:41.5250000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10662] _id=6ad24e50de269131f9e5b00b ts=2026-10-16T16:18:24.1260000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10663] _id=6ad24e50de269131f9e5b00c ts=2026-10-16T16:18:24.1260000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b27.jsonl[1640] _id=6ac7ccd5de269131f9c4dcc1 ts=2026-10-08T17:03:17.0750000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1657] _id=6ace5a6cde269131f9cf5c48 ts=2026-10-13T16:20:54.2900000Z; 70h 52m: 6ab9a8e69a8420a1e6b56b27.jsonl[12539] _id=6ad25955de269131f9e661e2 ts=2026-10-16T17:05:25.0760000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12658] _id=6ad63deede269131f9e98a8d ts=2026-10-19T15:57:28.0170000Z; 23h 25m: 6ab9a8e69a8420a1e6b56b27.jsonl[288] _id=6ac67b63de269131f9bd8b23 ts=2026-10-07T17:03:30.9170000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[295] _id=6ac7c4ecde269131f9c42a17 ts=2026-10-08T16:29:29.6100000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b27.jsonl[1647] _id=6ac7ccd8de269131f9c4dcf6 ts=2026-10-08T17:03:19.4680000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1702] _id=6ace5b1bde269131f9cf62ba ts=2026-10-13T16:23:54.4350000Z; 22h 54m: 6ab9a8e69a8420a1e6b56b27.jsonl[10094] _id=6ad10781de269131f9de4488 ts=2026-10-15T17:03:59.3690000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10133] _id=6ad249bbde269131f9e5760d ts=2026-10-16T15:58:50.6280000Z; 22h 53m: 6ab9a8e69a8420a1e6b56b27.jsonl[3078] _id=6ace648ede269131f9d01077 ts=2026-10-13T17:04:12.4960000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[3170] _id=6acfa674de269131f9d506f1 ts=2026-10-14T15:57:38.9200000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1489 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[1003] _id=6ac7cbf3de269131f9c4ccc7 ts=2026-10-08T16:57:36.4730000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1004] _id=6ac7cbf3de269131f9c4ccc9 ts=2026-10-08T16:57:36.4730000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[1004] _id=6ac7cbf3de269131f9c4ccc9 ts=2026-10-08T16:57:36.4730000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1005] _id=6ac7cbf3de269131f9c4cccb ts=2026-10-08T16:57:36.4730000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10050] _id=6ad1076fde269131f9de424e ts=2026-10-15T17:03:42.7230000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10052] _id=6ad10770de269131f9de425a ts=2026-10-15T17:03:42.7230000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 37h 59m 
  - Evidence: 37h 59m: 6ab9a8e69a8420a1e6b56b27.jsonl[8052] _id=6ad034dfde269131f9da3167 ts=2026-10-15T02:05:19.1350000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10330] _id=6ad24b0cde269131f9e58cf4 ts=2026-10-16T16:04:28.2520000Z; 22h 53m: 6ab9a8e69a8420a1e6b56b27.jsonl[3016] _id=6ace645bde269131f9d00a7d ts=2026-10-13T17:03:22.6490000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[3131] _id=6acfa633de269131f9d5043f ts=2026-10-14T15:56:35.4360000Z; 5h 58m: 6ab9a8e69a8420a1e6b56b27.jsonl[6228] _id=6acfdfa4de269131f9d947fa ts=2026-10-14T20:01:39.7030000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[7668] _id=6ad033b6de269131f9da2a05 ts=2026-10-15T02:00:21.6380000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.006s..0.008s shown 
  - Evidence: 6ms: 6ab9a8e69a8420a1e6b56b27.jsonl[6205] _id=6acfdf8ede269131f9d94663 ts=2026-10-14T20:01:17.4060000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[6208] _id=6acfdf8ede269131f9d94667 ts=2026-10-14T20:01:17.4120000Z; 6ms: 6ab9a8e69a8420a1e6b56b27.jsonl[7716] _id=6ad033f7de269131f9da2c85 ts=2026-10-15T02:01:26.2970000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[7717] _id=6ad033f7de269131f9da2c88 ts=2026-10-15T02:01:26.3030000Z; 8ms: 6ab9a8e69a8420a1e6b56b27.jsonl[3022] _id=6ace6458de269131f9d009e7 ts=2026-10-13T17:03:19.4160000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[3023] _id=6ace6458de269131f9d009eb ts=2026-10-13T17:03:19.4240000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a8e69a8420a1e6b56b27.jsonl[936] _id=6ac7cbc9de269131f9c4ca41 ts=2026-10-08T16:58:48.8780000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1733] _id=6ace5b57de269131f9cf64a8 ts=2026-10-13T16:24:54.8140000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b27.jsonl[2938] _id=6ace638fde269131f9cff0fd ts=2026-10-13T16:59:58.8900000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[4692] _id=6acfad63de269131f9d571ac ts=2026-10-14T16:27:15.4750000Z; 15h 17m: 6ab9a8e69a8420a1e6b56b27.jsonl[7455] _id=6ad02fb6de269131f9da1a6b ts=2026-10-15T01:43:18.0580000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[9966] _id=6ad106cede269131f9de3388 ts=2026-10-15T17:01:02.0830000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.031s shown 
  - Evidence: 23ms: 6ab9a8e69a8420a1e6b56b27.jsonl[2564] _id=6ace5e5cde269131f9cf920b ts=2026-10-13T16:37:47.1310000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[2568] _id=6ace5e5cde269131f9cf920f ts=2026-10-13T16:37:47.1540000Z; 31ms: 6ab9a8e69a8420a1e6b56b27.jsonl[2563] _id=6ace5e5bde269131f9cf9209 ts=2026-10-13T16:37:47.1000000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[2564] _id=6ace5e5cde269131f9cf920b ts=2026-10-13T16:37:47.1310000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 70h 53m 
  - Evidence: 70h 53m: 6ab9a8e69a8420a1e6b56b27.jsonl[12535] _id=6ad25935de269131f9e66169 ts=2026-10-16T17:04:52.7650000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12670] _id=6ad63e03de269131f9e98b38 ts=2026-10-19T15:57:54.7870000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6ab9a8e69a8420a1e6b56b27.jsonl[612] _id=6ac7c919de269131f9c4a223 ts=2026-10-08T16:47:21.7150000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[5281] _id=6acfb212de269131f9d5d30d ts=2026-10-14T16:47:14.6110000Z; 71h 38m: 6ab9a8e69a8420a1e6b56b27.jsonl[11539] _id=6ad2522ede269131f9e5f014 ts=2026-10-16T16:34:53.9070000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12984] _id=6ad6418fde269131f9e9a7cc ts=2026-10-19T16:13:02.2750000Z; 44h 16m: 6ab9a8e69a8420a1e6b56b27.jsonl[6128] _id=6acfdeebde269131f9d93d9b ts=2026-10-14T19:58:34.1390000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10595] _id=6ad24d7cde269131f9e5a8ca ts=2026-10-16T16:14:52.3830000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6ab9a8e69a8420a1e6b56b27.jsonl[613] _id=6ac7c919de269131f9c4a225 ts=2026-10-08T16:47:21.7470000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[5269] _id=6acfb200de269131f9d5d0c6 ts=2026-10-14T16:46:56.0410000Z; 71h 36m: 6ab9a8e69a8420a1e6b56b27.jsonl[11543] _id=6ad2522ede269131f9e5f01e ts=2026-10-16T16:34:53.9910000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12975] _id=6ad64117de269131f9e9a690 ts=2026-10-19T16:11:02.4460000Z; 44h 15m: 6ab9a8e69a8420a1e6b56b27.jsonl[6126] _id=6acfdeebde269131f9d93da2 ts=2026-10-14T19:58:34.2040000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10539] _id=6ad24d49de269131f9e5a859 ts=2026-10-16T16:14:00.8990000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.037s..0.037s shown 
  - Evidence: 37ms: 6ab9a8e69a8420a1e6b56b27.jsonl[6123] _id=6acfdeebde269131f9d93d9f ts=2026-10-14T19:58:34.1670000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[6126] _id=6acfdeebde269131f9d93da2 ts=2026-10-14T19:58:34.2040000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6ab9a8e69a8420a1e6b56b27.jsonl[598] _id=6ac7c90ede269131f9c4a0c4 ts=2026-10-08T16:47:09.8770000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[5267] _id=6acfb204de269131f9d5d160 ts=2026-10-14T16:47:00.3970000Z; 71h 36m: 6ab9a8e69a8420a1e6b56b27.jsonl[11535] _id=6ad25229de269131f9e5efdc ts=2026-10-16T16:34:49.4270000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12949] _id=6ad64115de269131f9e9a682 ts=2026-10-19T16:11:00.5240000Z; 44h 15m: 6ab9a8e69a8420a1e6b56b27.jsonl[6121] _id=6acfdee7de269131f9d93d72 ts=2026-10-14T19:58:30.8180000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10537] _id=6ad24d47de269131f9e5a855 ts=2026-10-16T16:13:58.9430000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 70 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10577] _id=6ad24d84de269131f9e5a8e0 ts=2026-10-16T16:14:59.9370000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10606] _id=6ad24dc3de269131f9e5a962 ts=2026-10-16T16:14:59.937Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10599] _id=6ad24d84de269131f9e5a8de ts=2026-10-16T16:14:59.8220000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10605] _id=6ad24dc3de269131f9e5a961 ts=2026-10-16T16:14:59.822Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[10764] _id=6ad24f0fde269131f9e5bf59 ts=2026-10-16T16:21:35.4910000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[10765] _id=6ad24f0fde269131f9e5bf5a ts=2026-10-16T16:21:35.4910000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6ab9a8e69a8420a1e6b56b27.jsonl[607] _id=6ac7c912de269131f9c4a131 ts=2026-10-08T16:47:14.6930000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[5301] _id=6acfb233de269131f9d5d69e ts=2026-10-14T16:47:47.1440000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 71h 10m 
  - Evidence: 71h 10m: 6ab9a8e69a8420a1e6b56b27.jsonl[11836] _id=6ad254e5de269131f9e6144f ts=2026-10-16T16:46:29.3920000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12655] _id=6ad63de8de269131f9e98a72 ts=2026-10-19T15:57:27.8360000Z; 48h 12m: 6ab9a8e69a8420a1e6b56b27.jsonl[4859] _id=6acfaefade269131f9d58c92 ts=2026-10-14T16:34:02.7140000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[11836] _id=6ad254e5de269131f9e6144f ts=2026-10-16T16:46:29.3920000Z; 11m 50s: 6ab9a8e69a8420a1e6b56b27.jsonl[12819] _id=6ad63f78de269131f9e9981a ts=2026-10-19T16:04:07.5510000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[13093] _id=6ad6423fde269131f9e9aa1e ts=2026-10-19T16:15:58.1170000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a8e69a8420a1e6b56b27.jsonl[712] _id=6ac7ca14de269131f9c4afcd ts=2026-10-08T16:51:31.9370000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1655] _id=6ace5a53de269131f9cf5bac ts=2026-10-13T16:20:34.5930000Z; 71h 11m: 6ab9a8e69a8420a1e6b56b27.jsonl[11816] _id=6ad254ddde269131f9e613f5 ts=2026-10-16T16:46:20.8850000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12654] _id=6ad63de2de269131f9e98a4d ts=2026-10-19T15:57:21.4310000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b27.jsonl[3] _id=6ac676f6de269131f9bd0b1a ts=2026-10-07T16:44:37.8670000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[294] _id=6ac7c4e1de269131f9c42959 ts=2026-10-08T16:29:21.4890000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a8e69a8420a1e6b56b27.jsonl[711] _id=6ac7ca14de269131f9c4afcc ts=2026-10-08T16:51:31.9370000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1654] _id=6ace5a53de269131f9cf5bab ts=2026-10-13T16:20:34.5930000Z; 71h 11m: 6ab9a8e69a8420a1e6b56b27.jsonl[11815] _id=6ad254ddde269131f9e613f4 ts=2026-10-16T16:46:20.8850000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12653] _id=6ad63de2de269131f9e98a4c ts=2026-10-19T15:57:21.4310000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b27.jsonl[2] _id=6ac676f6de269131f9bd0b19 ts=2026-10-07T16:44:37.8670000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[293] _id=6ac7c4e1de269131f9c42958 ts=2026-10-08T16:29:21.4890000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a8e69a8420a1e6b56b27.jsonl[1652] _id=6ace5a53de269131f9cf5ba8 ts=2026-10-08T17:03:21.871Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[3097] _id=6acfa5c3de269131f9d4ff80 ts=2026-10-13T17:05:02.01Z; 23h 26m: 6ab9a8e69a8420a1e6b56b27.jsonl[291] _id=6ac7c4e1de269131f9c42953 ts=2026-10-07T17:03:38.056Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[307] _id=6ac7c4fade269131f9c42ae0 ts=2026-10-08T16:29:46.2620000Z; 23h 6m: 6ab9a8e69a8420a1e6b56b27.jsonl[3097] _id=6acfa5c3de269131f9d4ff80 ts=2026-10-13T17:05:02.01Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[4481] _id=6acfaaf8de269131f9d549df ts=2026-10-14T16:11:11.669Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a8e69a8420a1e6b56b27.jsonl[741] _id=6ac7ca7ade269131f9c4b41d ts=2026-10-08T16:53:13.9950000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[1659] _id=6ace5a6cde269131f9cf5c4a ts=2026-10-13T16:20:59.0680000Z; 70h 58m: 6ab9a8e69a8420a1e6b56b27.jsonl[12501] _id=6ad257e9de269131f9e64ede ts=2026-10-16T16:59:20.7290000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12659] _id=6ad63deede269131f9e98a8e ts=2026-10-19T15:57:33.0020000Z; 23h 34m: 6ab9a8e69a8420a1e6b56b27.jsonl[182] _id=6ac67976de269131f9bd568d ts=2026-10-07T16:55:18.0790000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[305] _id=6ac7c4ecde269131f9c42a1f ts=2026-10-08T16:29:31.4230000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[12753] _id=6ad63ec7de269131f9e9917b ts=2026-10-19T16:01:10.0940000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[12754] _id=6ad63ec7de269131f9e9917c ts=2026-10-19T16:01:10.0940000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[13085] _id=6ad641fede269131f9e9a97c ts=2026-10-19T16:14:53.5410000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[13086] _id=6ad641fede269131f9e9a97d ts=2026-10-19T16:14:53.5410000Z; 0ms: 6ab9a8e69a8420a1e6b56b27.jsonl[533] _id=6ac7c866de269131f9c48f19 ts=2026-10-08T16:44:22.6380000Z -> 6ab9a8e69a8420a1e6b56b27.jsonl[534] _id=6ac7c866de269131f9c48f1a ts=2026-10-08T16:44:22.6380000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[527] _id=6ac7c853de269131f9c48d04 ts=2026-10-08T16:44:03.7180000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[623] _id=6ac7c92bde269131f9c4a3b9 ts=2026-10-08T16:47:39.3000000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[2662] _id=6ace5fadde269131f9cfacd7 ts=2026-10-13T16:43:24.8320000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[6126] _id=6acfdeebde269131f9d93da2 ts=2026-10-14T19:58:34.2040000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[11836] _id=6ad254e5de269131f9e6144f ts=2026-10-16T16:46:29.3920000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[12655] _id=6ad63de8de269131f9e98a72 ts=2026-10-19T15:57:27.8360000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[12819] _id=6ad63f78de269131f9e9981a ts=2026-10-19T16:04:07.5510000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[8274] _id=6ad0360cde269131f9da352e ts=2026-10-15T02:10:19.3360000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[8474] _id=6ad0fd6dde269131f9dd60b9 ts=2026-10-15T16:21:01.2900000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[12751] _id=6ad63ec7de269131f9e99176 ts=2026-10-19T16:01:10.0610000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[1650] _id=6ace5a6cde269131f9cf5c44 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 70 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[1999] _id=6ace5ba7de269131f9cf6926 ts=2026-10-13T16:26:13.9900000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[1990] _id=6ace5ba9de269131f9cf6943 ts=2026-10-13T16:26:15.6730000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[2055] _id=6ace5bcede269131f9cf6acb ts=2026-10-13T16:26:52.4770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 211 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[1801] _id=6ace5b90de269131f9cf670c ts=2026-10-13T16:23:55.5540000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[1808] _id=6ace5b91de269131f9cf6734 ts=2026-10-13T16:23:58.3080000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[1717] _id=6ace5b2ede269131f9cf635e ts=2026-10-13T16:24:13.6550000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 20 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[828] _id=6ac7cb0ede269131f9c4bd7c ts=2026-10-08T16:55:42.5300000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[900] _id=6ac7cb93de269131f9c4c607 ts=2026-10-08T16:57:55.6960000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[1733] _id=6ace5b57de269131f9cf64a8 ts=2026-10-13T16:24:54.8140000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[10742] _id=6ad24ef7de269131f9e5bd4f ts=2026-10-16T16:21:10.8040000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[10605] _id=6ad24dc3de269131f9e5a961 ts=2026-10-16T16:14:59.822Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[606] _id=6ac7c910de269131f9c4a0fe ts=2026-10-08T16:47:12.4300000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[603] _id=6ac7c911de269131f9c4a10b ts=2026-10-08T16:47:13.0790000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[605] _id=6ac7c911de269131f9c4a119 ts=2026-10-08T16:47:13.6780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'DialogueStartEvent' (totals: 447 start, 436 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'BecameCameraCentered' (totals: 630 open, 629 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 17 unmatched 'BecameVisible' (totals: 993 open, 976 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 21 open, 20 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 6 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'questActiveEvent' (totals: 57 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 256 of 13113 adjacent _id pairs reverse in client time; worst 124.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b27.jsonl[963] _id=6ac7cbefde269131f9c4cc4f ts=2026-10-08T16:59:27.2250000Z`; `6ab9a8e69a8420a1e6b56b27.jsonl[952] _id=6ac7cbf0de269131f9c4cc57 ts=2026-10-08T16:57:22.4450000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.62s, min -429433.22s, max -0.14s over 13114 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b27\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3662 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1256); Unit 2 Prod (Refactor) (876); Unit 3 Dungeon Dev (408); Unit 3 Dev (359); Unit 5 Dev - Dungeon (319); Unit 4 Dev (160); Unit 4 Dev - Anderson Base (115); Unit 1 Dev (109); Unit 5 Dev (60)
- **Intervals:** median 1.15s (p5 0.14s / p95 19.65s, n=3661)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3662/3662 records)
    "pressed"  x3662
data.actionType  (string, 3662/3662 records)
    "Move"  x2804
    "Interact"  x520
    "Jump"  x133
    "Ascend"  x75
    "Hoverboard"  x67
    "Sprint"  x45
    "Map"  x12
    "Pause"  x4
    "SkipCinematic"  x2
data.key  (string, 3662/3662 records, 2 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3662/3662 records)
    "Player"  x3006
    "Drone"  x656
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3228 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2224); Unit 4 Dev (396); Unit 5 Dev - Dungeon (326); Unit 3 Dungeon Dev (282)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.35s, n=3227)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3228/3228 records)
    "BecameVisible"  x993
    "BecameInvisible"  x976
    "BecameCameraCentered"  x630
    "BecameCameraUncentered"  x629
data.pieceId  (string, 3228/3228 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3228/3228 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2327 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (712); Unit 3 Dev (317); Unit 1 Dev (277); Unit 4 Dev (275); Unit 4 Dev - Anderson Base (253); Unit 3 Dungeon Dev (188); Unit 5 Dev (110); Unit 4 Dev - Dungeon (101); Unit 5 Dev - Dungeon (94)
- **eventKey:** present on 1444 of 2327 records
- **Intervals:** median 3.66s (p5 0.00s / p95 30.56s, n=2326)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1444; [conversationId, dialogueEventType] x883
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2327/2327 records)
    numeric range 8 .. 117 (53 unique)
data.dialogueEventType  (string, 2327/2327 records)
    "DialogueNodeEvent"  x1444
    "DialogueStartEvent"  x447
    "DialogueFinishEvent"  x436
data.nodeId  (number, 1444/2327 records)
    numeric range 0 .. 290 (222 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2120 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (625); Unit 4 Dev - Dungeon (303); Unit 1 Dev (233); Unit 3 Dev (210); Unit 4 Dev (193); Unit 4 Dev - Anderson Base (176); Unit 3 Dungeon Dev (157); Unit 5 Dev - Dungeon (153); Unit 5 Dev (70)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=2108)
- **Fields under `data`:**

```text
data.position  (object, 2120/2120 records)
data.position.x  (number, 2120/2120 records)
    numeric range -693.109 .. 1549.88 (829 unique)
data.position.y  (number, 2120/2120 records)
    numeric range -29029.6 .. 222.005 (544 unique)
data.position.z  (number, 2120/2120 records)
    numeric range -1035.33 .. 2095.94 (830 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 741 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (573); Unit 3 Dev (57); Unit 2 Prod (Refactor) (51); Unit 5 Dev (38); Unit 1 Dev (22)
- **Intervals:** median 0.50s (p5 0.03s / p95 8.36s, n=740)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 741/741 records)
    "argumentationNodeHoverEnd"  x301
    "argumentationNodeHoverStart"  x301
    "argumentationNodeAdd"  x81
    "argumentationNodeRemove"  x58
data.argumentationTitle  (string, 741/741 records)
    "Unit 4 - Flooding"  x573
    "Unit 3 - Pollution Upstream"  x57
    "Unit 2 – Watershed"  x51
    "Unit 5"  x38
    "Unit 1 - Argumentation Tutorial"  x11
    "Unit 1 - Freshwater"  x11
data.nodeName  (string, 741/741 records)
    "B"  x122
    "A"  x105
    "D"  x95
    "C"  x86
    "2"  x79
    "1"  x61
    "II"  x58
    "3"  x47
    "4"  x44
    "I"  x39
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 379 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (164); Unit 2 Prod (Refactor) (67); Unit 3 Dungeon Dev (59); Unit 5 Dev - Dungeon (23); Unit 4 Dev - Anderson Base (18); Unit 4 Dev (17); Unit 1 Dev (15); Unit 3 Dev (12); Unit 5 Dev (4)
- **Intervals:** median 12.22s (p5 0.21s / p95 298.63s, n=378)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 379/379 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 379/379 records)
    105 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 119 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (49); Unit 4 Dev (46); Unit 3 Dev (24)
- **Intervals:** median 0.77s (p5 0.12s / p95 247.00s, n=118)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x111; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/119 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/119 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 111/119 records)
    "RightDrag"  x60
    "LeftDrag"  x51
data.currentSoilType  (string, 111/119 records)
    "CLAYSAND"  x25
    "CLAY"  x23
    "SAND"  x23
    "CLAYROCK"  x15
    "SANDGRAVEL"  x14
    "BEDROCK"  x6
    "GRAVEL"  x5
data.isCorrectSelection  (string, 111/119 records)
    "false"  x84
    "true"  x27
data.waterLevelStatus  (string, 111/119 records)
    "Proper"  x65
    "TooHigh"  x32
    "TooLow"  x14
data.waterRetentionChange  (string, 111/119 records)
    "Increase"  x48
    "Decrease"  x36
    "NoChange"  x27
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 94 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (18); Unit 3 Dev (12); Unit 5 Dev - Dungeon (12); Unit 4 Dev (11); Unit 4 Dev - Dungeon (10); Unit 5 Dev (6); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 94 of 94 records
- **Intervals:** median 163.65s (p5 0.00s / p95 63410.51s, n=93)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 94/94 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x37
data.questID  (string, 94/94 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 94/94 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/94 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 90 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (66); Unit 3 Dev (19); Unit 1 Dev (3); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 3.83s (p5 0.53s / p95 1739.56s, n=89)
- **`data` key-set variants:** [actionType, featureUsed] x41; [actionType, featureUsed, location] x32; [actionType, featureUsed, legendName] x17
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 90/90 records)
    "WaypointMoveEvent"  x27
    "MapOpenEvent"  x21
    "MapCloseEvent"  x20
    "Selected"  x16
    "WaypointSetEvent"  x5
    "Unselected"  x1
data.featureUsed  (string, 90/90 records)
    "Map"  x41
    "Waypoint"  x32
    "Legend"  x17
data.legendName  (string, 17/90 records)
    13 unique values (see csv/event_unique_values.csv)
data.location  (object, 32/90 records)
data.location.x  (number, 32/90 records)
    numeric range -391.657 .. 200.774 (30 unique)
data.location.y  (number, 32/90 records)
    numeric range -288.025 .. 300.434 (30 unique)
data.location.z  (number, 32/90 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 84 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (75); Unit 1 Dev (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 5.93s (p5 0.12s / p95 379.04s, n=83)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 84/84 records)
    "submitAnswerEvent"  x84
data.answerSubmitted  (string, 84/84 records)
    28 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 84/84 records)
    "Unit 4 - Flooding"  x75
    "Unit 1 - Freshwater"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 68 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (68)
- **Intervals:** median 3.89s (p5 0.13s / p95 147.97s, n=67)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "ChangeCanister"  x68
data.canisterType  (string, 68/68 records)
    "Clay"  x41
    "Bedrock"  x23
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 68/68 records)
    "5"  x66
    "3"  x1
    "4"  x1
data.machine  (string, 68/68 records)
    "1"  x66
    "2"  x2
data.row  (string, 68/68 records)
    "BottomRow"  x52
    "TopRow"  x16
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 54 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (54)
- **Intervals:** median 10.95s (p5 2.10s / p95 70.01s, n=53)
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "On"  x37
    "Off"  x17
data.floor  (string, 54/54 records)
    "4"  x33
    "3"  x16
    "2"  x3
    "1"  x2
data.machineNumber  (string, 54/54 records)
    "One"  x52
    "Two"  x2
data.machineType  (string, 54/54 records)
    "Condenser"  x25
    "Evaporator"  x19
    "DualChamber_Condenser"  x4
    "VentSwitch"  x4
    "DualChamber_Evaporator"  x2
data.room  (string, 54/54 records)
    "3"  x26
    "2"  x17
    "1"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 43 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (5); Unit 4 Dev (5); Unit 1 Dev (3); Unit 3 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 510.80s (p5 8.27s / p95 85326.29s, n=42)
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "DebugMenuStateChanged"  x43
data.isOpened  (bool, 43/43 records)
    false  x43
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 22 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 3 Dev (2); Unit 1 Dev (1)
- **Intervals:** median 1817.37s (p5 26.52s / p95 256260.55s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 2297.38s (p5 421.16s / p95 282342.86s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 138.97s (p5 0.05s / p95 348980.50s, n=14)
- **Open findings:** 3 — see sections 5-8
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

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 1.44s (p5 0.23s / p95 16.38s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 6 empty-string)
    ""  x6
    "cameraPlaced"  x5
data.boxId  (string, 11/11 records)
    "0"  x5
    "1"  x4
    "2"  x2
data.soilType  (string, 11/11 records)
    "Clay"  x5
    "Sand"  x5
    "Gravel"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 16492.69s (p5 8.98s / p95 275620.77s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 0.52s (p5 0.09s / p95 336981.45s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x6
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Freshwater"  x7
    "Unit 2 – Watershed"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Waterfall Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev - Dungeon (6); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 6.28s (p5 2.25s / p95 60906.37s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 8 empty-string)
    ""  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 710.57s (p5 83.85s / p95 239716.09s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x5
    "Open"  x1
data.chatID  (string, 6/6 records)
    "NA"  x5
    "[23-36, 23-38, 23-39, 23-41, 23-42]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 140233.39s (p5 42953.65s / p95 480746.69s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

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
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (49 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TopographicMapEvent` data.actionType: "Selected" (16x); "Unselected" (1x); "WaypointMoveEvent" (27x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (17x); "Waypoint" (32x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (58x)
- `soilMachine` data.canisterType: "Bedrock" (23x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*