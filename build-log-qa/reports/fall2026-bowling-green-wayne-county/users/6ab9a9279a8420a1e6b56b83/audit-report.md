# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b83

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b83
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b83.jsonl
- **Records:** 13148 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b83
- **Time span:** 2026-10-06T18:52:03.937000+00:00 .. 2026-10-19T16:11:00.851000+00:00 (309h 18m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b83\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 13148 records, 11 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 103 INFO, 0 NOT_TESTED, 93 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3802 | 28.92 | 1 | 4 | 0 | 2026-10-08T18:53:31.564000+00:00 | 2026-10-16T18:40:26.769000+00:00 | 191h 46m |
| InputEvent | 3192 | 24.28 | 1 | 8 | 0 | 2026-10-06T18:57:52.970000+00:00 | 2026-10-19T16:11:00.851000+00:00 | 309h 13m |
| PlayerPositionEvent | 2889 | 21.97 | 1 | 9 | 0 | 2026-10-06T18:53:38.965000+00:00 | 2026-10-19T16:10:54.079000+00:00 | 309h 17m |
| DialogueEvent | 2065 | 15.71 | 1 | 9 | 1259 | 2026-10-06T18:53:58.921000+00:00 | 2026-10-19T16:10:42.355000+00:00 | 309h 16m |
| argumentationNodeEvent | 409 | 3.11 | 1 | 4 | 0 | 2026-10-07T19:07:58.853000+00:00 | 2026-10-16T02:06:08.201000+00:00 | 198h 58m |
| ObjectInterEvent | 367 | 2.79 | 1 | 8 | 0 | 2026-10-06T19:01:35.429000+00:00 | 2026-10-19T16:10:15.285000+00:00 | 309h 8m |
| TopographicMapEvent | 83 | 0.63 | 1 | 4 | 0 | 2026-10-06T19:15:25.808000+00:00 | 2026-10-15T23:30:09.542000+00:00 | 220h 14m |
| questEvent | 78 | 0.59 | 1 | 8 | 78 | 2026-10-06T18:53:58.896000+00:00 | 2026-10-19T16:09:23.719000+00:00 | 309h 15m |
| Soil Key Puzzle | 37 | 0.28 | 1 | 3 | 0 | 2026-10-08T19:10:16.541000+00:00 | 2026-10-15T23:45:52.408000+00:00 | 172h 35m |
| DEBUGMenu | 36 | 0.27 | 1 | 9 | 0 | 2026-10-06T18:53:38.951000+00:00 | 2026-10-19T16:09:21.539000+00:00 | 309h 15m |
| WaterChamberEvent | 32 | 0.24 | 1 | 1 | 0 | 2026-10-16T18:38:33.691000+00:00 | 2026-10-19T16:11:00.844000+00:00 | 69h 32m |
| argumentationAnswerEvent | 31 | 0.24 | 1 | 4 | 0 | 2026-10-07T19:10:50.614000+00:00 | 2026-10-16T02:06:15.906000+00:00 | 198h 55m |
| gameWindowFocusEvent | 29 | 0.22 | 1 | 8 | 0 | 2026-10-06T18:52:03.937000+00:00 | 2026-10-19T16:08:36.684000+00:00 | 309h 16m |
| DaniEvent | 23 | 0.17 | 1 | 5 | 0 | 2026-10-06T19:15:01.019000+00:00 | 2026-10-16T00:20:36.249000+00:00 | 221h 5m |
| gameStartEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-10-06T18:52:03.938000+00:00 | 2026-10-19T16:08:36.684000+00:00 | 309h 16m |
| gameWindowUnfocusEvent | 15 | 0.11 | 1 | 7 | 0 | 2026-10-06T19:15:02.214000+00:00 | 2026-10-16T01:03:04.180000+00:00 | 221h 48m |
| argumentationEvent | 12 | 0.09 | 1 | 4 | 0 | 2026-10-07T19:07:32.028000+00:00 | 2026-10-16T02:06:15.977000+00:00 | 198h 58m |
| soilMachine | 9 | 0.07 | 1 | 1 | 0 | 2026-10-16T00:23:40.251000+00:00 | 2026-10-16T00:42:07.448000+00:00 | 18m 27s |
| TerasGardenBox | 8 | 0.06 | 1 | 1 | 0 | 2026-10-16T02:11:39.842000+00:00 | 2026-10-16T02:14:32.604000+00:00 | 2m 52s |
| chatEvent | 7 | 0.05 | 1 | 4 | 0 | 2026-10-15T19:10:43.916000+00:00 | 2026-10-19T16:09:21.349000+00:00 | 92h 58m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-07T19:14:13.963000+00:00 | 2026-10-16T02:26:11.370000+00:00 | 199h 11m |
| argumentationToolEvent | 3 | 0.02 | 1 | 1 | 0 | 2026-10-14T19:10:10.714000+00:00 | 2026-10-14T19:10:12.268000+00:00 | 1.6s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 160618.748s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 2.257s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 13.634s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.071s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 3.433s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 17.114s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.123s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 27.177s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.777s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 8413.341s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 55931.398s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1334.537s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 642.786s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.0x vs baseline. 
  - Observed: 36 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 23 records this build 
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
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK; GRAVEL 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Aryn's Room; Teleporter Room; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 31 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 2,II; A,2,II; B,2,II; C,1,II; C,2,I; C,2,II; C,3,II; C,4,II; C,B,2,II; C,D,A,2,II; D,1,II; D,2,II; D,C,2,II; II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 7 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [73-208, 73-209, 73-210, 73-211, 73-212]; [79-119, 79-120, 79-121, 79-123, 79-124] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[6] _id=6ac54354de269131f9b703f5 ts=2026-10-06T18:52:03.9380000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[411] _id=6ac692d3de269131f9bdf159 ts=2026-10-07T18:43:30.1430000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[939] _id=6ac69a6bde269131f9bf1a04 ts=2026-10-07T19:15:54.8960000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 29 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 29} 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[5] _id=6ac54354de269131f9b703f1 ts=2026-10-06T18:52:03.9370000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[392] _id=6ac548bcde269131f9b7869d ts=2026-10-06T19:15:07.2340000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[410] _id=6ac692d3de269131f9bdf158 ts=2026-10-07T18:43:30.1430000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[361] _id=6ac548b7de269131f9b785e3 ts=2026-10-06T19:15:02.2140000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[408] _id=6ac692d3de269131f9bdf14a ts=2026-10-06T19:17:36.682Z`; `6ab9a9279a8420a1e6b56b83.jsonl[3227] _id=6ace7f91de269131f9d13925 ts=2026-10-09T16:11:02.582Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 4 of 83 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[397] _id=6ac548cede269131f9b78957 ts=2026-10-06T19:15:25.8080000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[400] _id=6ac5493cde269131f9b79a07 ts=2026-10-06T19:17:16.0120000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[401] _id=6ac54941de269131f9b79ae1 ts=2026-10-06T19:17:21.0690000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3801 | 0.0 | 0.071 | 181.64 | 2.698 | 381970.462 | 0.33 | 1614 | 8 |
| InputEvent | 3191 | 0.0 | 2.257 | 348.852 | 27.347 | 355744.75 | 0.17 | 35 | 13 |
| PlayerPositionEvent | 2876 | 9.767 | 10.003 | 260.808 | 10.094 | 355727.29 | 0.23 | 0 | 7 |
| DialogueEvent | 2064 | 0.0 | 4.341 | 539.44 | 50.871 | 355914.148 | 0.11 | 587 | 11 |
| argumentationNodeEvent | 408 | 0.004 | 0.651 | 1755.611 | 15.993 | 546231.418 | 0.03 | 16 | 4 |
| ObjectInterEvent | 366 | 0.0 | 13.634 | 3040.765 | 422.247 | 381778.067 | 0.02 | 5 | 13 |
| TopographicMapEvent | 82 | 0.02 | 7.123 | 9669.314 | 56411.753 | 356540.114 | 0.01 | 4 | 8 |
| questEvent | 77 | 0.001 | 226.948 | 14458.764 | 84475.985 | 355745.324 | 0.0 | 12 | 19 |
| Soil Key Puzzle | 36 | 0.904 | 3.433 | 17259.33 | 67287.863 | 457157.793 | 0.0 | 0 | 4 |
| DEBUGMenu | 35 | 8.846 | 727.149 | 31809.788 | 135874.139 | 356424.592 | 0.0 | 0 | 18 |
| WaterChamberEvent | 31 | 2.933 | 28.696 | 8075.715 | 142.632 | 249153.631 | 0.01 | 0 | 1 |
| argumentationAnswerEvent | 30 | 3.197 | 27.177 | 23870.843 | 85551.371 | 546297.187 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 28 | 82.697 | 1334.537 | 39764.027 | 192794.198 | 356436.753 | 0.0 | 0 | 18 |
| DaniEvent | 22 | 0.001 | 4.037 | 36178.874 | 172612.207 | 432342.962 | 0.0 | 4 | 5 |
| gameStartEvent | 15 | 1693.219 | 55931.398 | 74226.183 | 282287.862 | 356436.752 | 0.0 | 0 | 15 |
| gameWindowUnfocusEvent | 14 | 11.231 | 642.786 | 57034.426 | 294547.485 | 380981.858 | 0.0 | 0 | 7 |
| argumentationEvent | 11 | 0.037 | 90.007 | 65120.359 | 326864.821 | 546207.195 | 0.0 | 1 | 4 |
| soilMachine | 8 | 4.349 | 111.808 | 138.4 | 306.055 | 325.298 | 0.43 | 0 | 0 |
| TerasGardenBox | 7 | 8.979 | 17.114 | 24.68 | 52.52 | 57.4 | 2.43 | 0 | 0 |
| chatEvent | 6 | 16.598 | 8413.341 | 55786.239 | 203994.064 | 249061.873 | 0.0 | 0 | 4 |
| EndOfUnit | 3 | 10101.104 | 160618.748 | 239039.136 | 507819.674 | 546397.555 | 0.0 | 0 | 3 |
| argumentationToolEvent | 2 | 0.525 | 0.777 | 0.777 | 1.004 | 1.029 | 77.22 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 8 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[10649] _id=6ad174a8de269131f9e24cf0 ts=2026-10-16T00:49:43.1820000Z == 6ab9a9279a8420a1e6b56b83.jsonl[10650] _id=6ad174a8de269131f9e24cf1 ts=2026-10-16T00:49:43.1820000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[10656] _id=6ad174a8de269131f9e24cf7 ts=2026-10-16T00:49:43.1850000Z == 6ab9a9279a8420a1e6b56b83.jsonl[10657] _id=6ad174a8de269131f9e24cf8 ts=2026-10-16T00:49:43.1850000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[10661] _id=6ad174a8de269131f9e24cfc ts=2026-10-16T00:49:43.8630000Z == 6ab9a9279a8420a1e6b56b83.jsonl[10662] _id=6ad174a8de269131f9e24cfd ts=2026-10-16T00:49:43.8630000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 47 group(s), 75 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[1122] _id=6ac7e7a0de269131f9c5cfbe ts=2026-10-08T18:57:34.7420000Z == 6ab9a9279a8420a1e6b56b83.jsonl[1120] _id=6ac7e7a0de269131f9c5cfca ts=2026-10-08T18:57:34.7420000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[1125] _id=6ac7e7a0de269131f9c5cfcb ts=2026-10-08T18:57:34.8180000Z == 6ab9a9279a8420a1e6b56b83.jsonl[1126] _id=6ac7e7a0de269131f9c5cfd3 ts=2026-10-08T18:57:34.8180000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[1142] _id=6ac7e7a2de269131f9c5d063 ts=2026-10-08T18:57:35.8440000Z == 6ab9a9279a8420a1e6b56b83.jsonl[1136] _id=6ac7e7a2de269131f9c5d06b ts=2026-10-08T18:57:35.8440000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 78 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b83.jsonl[132] _id=6ac54590de269131f9b72c3f ts=2026-10-06T19:01:35.4290000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[130] _id=6ac54590de269131f9b72c43 ts=2026-10-06T19:01:35.4340000Z`; `4ms: 6ab9a9279a8420a1e6b56b83.jsonl[461] _id=6ac6936fde269131f9be04a9 ts=2026-10-07T18:46:06.9630000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[462] _id=6ac69370de269131f9be04b7 ts=2026-10-07T18:46:06.9670000Z`; `802ms: 6ab9a9279a8420a1e6b56b83.jsonl[1023] _id=6ac7e67cde269131f9c5a5fe ts=2026-10-08T18:52:44.5920000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[1025] _id=6ac7e67dde269131f9c5a616 ts=2026-10-08T18:52:45.3940000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `51ms: 6ab9a9279a8420a1e6b56b83.jsonl[6667] _id=6acfd438de269131f9d84cc9 ts=2026-10-14T19:12:55.5780000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[6672] _id=6acfd438de269131f9d84ccc ts=2026-10-14T19:12:55.6290000Z`; `37ms: 6ab9a9279a8420a1e6b56b83.jsonl[11896] _id=6ad18698de269131f9e2a5dd ts=2026-10-16T02:06:15.9400000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[11901] _id=6ad18698de269131f9e2a5e0 ts=2026-10-16T02:06:15.9770000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 24 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `729ms: 6ab9a9279a8420a1e6b56b83.jsonl[5863] _id=6aceef29de269131f9d2b164 ts=2026-10-14T02:55:36.3480000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[5874] _id=6aceef29de269131f9d2b167 ts=2026-10-14T02:55:37.0770000Z`; `820ms: 6ab9a9279a8420a1e6b56b83.jsonl[5866] _id=6aceef2cde269131f9d2b16b ts=2026-10-14T02:55:39.3170000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[5875] _id=6aceef2dde269131f9d2b16f ts=2026-10-14T02:55:40.1370000Z`; `356ms: 6ab9a9279a8420a1e6b56b83.jsonl[11087] _id=6ad17841de269131f9e26199 ts=2026-10-16T01:05:04.9890000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[11089] _id=6ad17841de269131f9e2619d ts=2026-10-16T01:05:05.3450000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `525ms: 6ab9a9279a8420a1e6b56b83.jsonl[6618] _id=6acfd393de269131f9d8308c ts=2026-10-14T19:10:10.7140000Z ~ 6ab9a9279a8420a1e6b56b83.jsonl[6619] _id=6acfd394de269131f9d830b2 ts=2026-10-14T19:10:11.2390000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 99h 0m 
  - Evidence: 99h 0m: 6ab9a9279a8420a1e6b56b83.jsonl[2460] _id=6ac90f49de269131f9ca6f5d ts=2026-10-09T15:59:04.3110000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3228] _id=6ace7f91de269131f9d1392c ts=2026-10-13T18:59:28.9030000Z; 69h 34m: 6ab9a9279a8420a1e6b56b83.jsonl[12327] _id=6ad26e09de269131f9e70905 ts=2026-10-16T18:33:41.6880000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13105] _id=6ad64085de269131f9e9a0f4 ts=2026-10-19T16:08:36.5310000Z; 24h 5m: 6ab9a9279a8420a1e6b56b83.jsonl[5955] _id=6acfcb11de269131f9d71ad4 ts=2026-10-14T18:33:52.9900000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6768] _id=6ad11df0de269131f9df0c6a ts=2026-10-15T18:39:43.9700000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 5m 
  - Evidence: 120h 5m: 6ab9a9279a8420a1e6b56b83.jsonl[1735] _id=6ac7e910de269131f9c6086b ts=2026-10-08T19:03:44.0390000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3383] _id=6ace81e7de269131f9d171d4 ts=2026-10-13T19:09:27.0010000Z; 47h 57m: 6ab9a9279a8420a1e6b56b83.jsonl[3426] _id=6ace82d0de269131f9d19c55 ts=2026-10-13T19:13:20.4020000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[7623] _id=6ad12530de269131f9e00ec2 ts=2026-10-15T19:10:40.3220000Z; 47h 48m: 6ab9a9279a8420a1e6b56b83.jsonl[396] _id=6ac548cede269131f9b78951 ts=2026-10-06T19:15:25.7970000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[1730] _id=6ac7e903de269131f9c60697 ts=2026-10-08T19:03:31.4470000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b83.jsonl[3429] _id=6ace82cbde269131f9d19b56 ts=2026-10-13T19:13:15.3480000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3430] _id=6ace82cbde269131f9d19b57 ts=2026-10-13T19:13:15.3490000Z; 7ms: 6ab9a9279a8420a1e6b56b83.jsonl[3427] _id=6ace82c8de269131f9d19a8a ts=2026-10-13T19:13:11.5080000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3402] _id=6ace82c8de269131f9d19a8c ts=2026-10-13T19:13:11.5150000Z; 8ms: 6ab9a9279a8420a1e6b56b83.jsonl[1723] _id=6ac7e907de269131f9c60733 ts=2026-10-08T19:03:35.2260000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[1731] _id=6ac7e907de269131f9c60737 ts=2026-10-08T19:03:35.2340000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 98h 51m 
  - Evidence: 98h 51m: 6ab9a9279a8420a1e6b56b83.jsonl[3203] _id=6ac91209de269131f9ca7d7e ts=2026-10-09T16:10:48.3030000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3277] _id=6ace8052de269131f9d14543 ts=2026-10-13T19:02:42.4510000Z; 69h 10m: 6ab9a9279a8420a1e6b56b83.jsonl[13102] _id=6ad27407de269131f9e7863b ts=2026-10-16T18:59:18.3720000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13116] _id=6ad640bbde269131f9e9a2ad ts=2026-10-19T16:09:31.0070000Z; 23h 40m: 6ab9a9279a8420a1e6b56b83.jsonl[177] _id=6ac5464bde269131f9b73f17 ts=2026-10-06T19:04:42.6030000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[444] _id=6ac69335de269131f9bdfccc ts=2026-10-07T18:45:08.6410000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 587 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10633] _id=6ad1745cde269131f9e24be7 ts=2026-10-16T00:48:20.0970000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10643] _id=6ad1749bde269131f9e24cae ts=2026-10-16T00:48:20.097Z; 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[11120] _id=6ad17873de269131f9e262a7 ts=2026-10-16T01:05:55.3680000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11121] _id=6ad17873de269131f9e262a8 ts=2026-10-16T01:05:55.3680000Z; 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[11135] _id=6ad17896de269131f9e26348 ts=2026-10-16T01:06:29.5430000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11136] _id=6ad17896de269131f9e26349 ts=2026-10-16T01:06:29.5430000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 151h 46m 
  - Evidence: 151h 46m: 6ab9a9279a8420a1e6b56b83.jsonl[937] _id=6ac69a06de269131f9bf10e4 ts=2026-10-07T19:14:13.9630000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[5947] _id=6acef064de269131f9d2b210 ts=2026-10-14T03:00:51.5180000Z; 44h 36m: 6ab9a9279a8420a1e6b56b83.jsonl[5947] _id=6acef064de269131f9d2b210 ts=2026-10-14T03:00:51.5180000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[8786] _id=6ad163cede269131f9e20b6f ts=2026-10-15T23:37:50.2660000Z; 2h 48m: 6ab9a9279a8420a1e6b56b83.jsonl[8786] _id=6ad163cede269131f9e20b6f ts=2026-10-15T23:37:50.2660000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[12320] _id=6ad18b43de269131f9e2b971 ts=2026-10-16T02:26:11.3700000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 98h 49m 
  - Evidence: 98h 49m: 6ab9a9279a8420a1e6b56b83.jsonl[3222] _id=6ac9120ede269131f9ca7d8a ts=2026-10-09T16:10:53.1510000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3234] _id=6ace7faede269131f9d13a57 ts=2026-10-13T18:59:57.9010000Z; 69h 12m: 6ab9a9279a8420a1e6b56b83.jsonl[13078] _id=6ad2739bde269131f9e77f64 ts=2026-10-16T18:57:30.2730000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13115] _id=6ad640c7de269131f9e9a315 ts=2026-10-19T16:09:42.0290000Z; 23h 33m: 6ab9a9279a8420a1e6b56b83.jsonl[953] _id=6ac69a97de269131f9bf1e63 ts=2026-10-07T19:16:38.5150000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[973] _id=6ac7e5dfde269131f9c59093 ts=2026-10-08T18:50:07.0290000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 35 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10649] _id=6ad174a8de269131f9e24cf0 ts=2026-10-16T00:49:43.1820000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10650] _id=6ad174a8de269131f9e24cf1 ts=2026-10-16T00:49:43.1820000Z; 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10650] _id=6ad174a8de269131f9e24cf1 ts=2026-10-16T00:49:43.1820000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10651] _id=6ad174a8de269131f9e24cf2 ts=2026-10-16T00:49:43.1820000Z; 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10651] _id=6ad174a8de269131f9e24cf2 ts=2026-10-16T00:49:43.1820000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10652] _id=6ad174a8de269131f9e24cf3 ts=2026-10-16T00:49:43.1820000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 106h 2m 
  - Evidence: 106h 2m: 6ab9a9279a8420a1e6b56b83.jsonl[3154] _id=6ac91110de269131f9ca7a36 ts=2026-10-09T16:06:39.3010000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3979] _id=6acee462de269131f9d29bf0 ts=2026-10-14T02:09:37.3680000Z; 69h 19m: 6ab9a9279a8420a1e6b56b83.jsonl[12949] _id=6ad2720ede269131f9e76128 ts=2026-10-16T18:50:53.4290000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13131] _id=6ad640e8de269131f9e9a49f ts=2026-10-19T16:10:15.2850000Z; 23h 39m: 6ab9a9279a8420a1e6b56b83.jsonl[917] _id=6ac699dbde269131f9bf0c69 ts=2026-10-07T19:13:30.8760000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[1013] _id=6ac7e67ade269131f9c5a596 ts=2026-10-08T18:52:42.1850000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10956] _id=6ad1773ade269131f9e25d0b ts=2026-10-16T01:00:41.4660000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10957] _id=6ad1773ade269131f9e25d0c ts=2026-10-16T01:00:41.4660000Z; 1ms: 6ab9a9279a8420a1e6b56b83.jsonl[11015] _id=6ad17796de269131f9e25f07 ts=2026-10-16T01:02:14.0470000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11016] _id=6ad17796de269131f9e25f08 ts=2026-10-16T01:02:14.0480000Z; 4ms: 6ab9a9279a8420a1e6b56b83.jsonl[461] _id=6ac6936fde269131f9be04a9 ts=2026-10-07T18:46:06.9630000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[462] _id=6ac69370de269131f9be04b7 ts=2026-10-07T18:46:06.9670000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 98h 48m 
  - Evidence: 98h 48m: 6ab9a9279a8420a1e6b56b83.jsonl[3226] _id=6ac91211de269131f9ca7d8e ts=2026-10-09T16:10:56.9830000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3232] _id=6ace7fa6de269131f9d13a0e ts=2026-10-13T18:59:44.2730000Z; 23h 32m: 6ab9a9279a8420a1e6b56b83.jsonl[962] _id=6ac69abdde269131f9bf20a2 ts=2026-10-07T19:17:16.8750000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[969] _id=6ac7e5cede269131f9c58edd ts=2026-10-08T18:49:46.3900000Z; 23h 26m: 6ab9a9279a8420a1e6b56b83.jsonl[403] _id=6ac54948de269131f9b79b9b ts=2026-10-06T19:17:28.2120000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[415] _id=6ac692ecde269131f9bdf43a ts=2026-10-07T18:43:52.9710000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 106h 6m 
  - Evidence: 106h 6m: 6ab9a9279a8420a1e6b56b83.jsonl[3139] _id=6ac910eade269131f9ca79c7 ts=2026-10-09T16:06:00.3520000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[4031] _id=6acee4fcde269131f9d29c98 ts=2026-10-14T02:12:10.8140000Z; 40h 21m: 6ab9a9279a8420a1e6b56b83.jsonl[5165] _id=6acee762de269131f9d2a5af ts=2026-10-14T02:22:24.1240000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6846] _id=6ad11ee2de269131f9df2bc5 ts=2026-10-15T18:43:44.6750000Z; 20h 52m: 6ab9a9279a8420a1e6b56b83.jsonl[2353] _id=6ac7ea5ade269131f9c64cf6 ts=2026-10-08T19:09:12.5740000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[2549] _id=6ac91029de269131f9ca7448 ts=2026-10-09T16:01:37.0660000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1614 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10436] _id=6ad1732cde269131f9e246b5 ts=2026-10-16T00:43:23.3000000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10465] _id=6ad1732cde269131f9e246b7 ts=2026-10-16T00:43:23.3000000Z; 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10440] _id=6ad17331de269131f9e246cd ts=2026-10-16T00:43:27.9970000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10441] _id=6ad17331de269131f9e246ce ts=2026-10-16T00:43:27.9970000Z; 0ms: 6ab9a9279a8420a1e6b56b83.jsonl[10441] _id=6ad17331de269131f9e246ce ts=2026-10-16T00:43:27.9970000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[10442] _id=6ad17331de269131f9e246d0 ts=2026-10-16T00:43:27.9970000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 126h 59m 
  - Evidence: 126h 59m: 6ab9a9279a8420a1e6b56b83.jsonl[2378] _id=6ac7ea9bde269131f9c655a3 ts=2026-10-08T19:10:19.5690000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3972] _id=6acee462de269131f9d29bee ts=2026-10-14T02:09:37.3620000Z; 23h 24m: 6ab9a9279a8420a1e6b56b83.jsonl[6765] _id=6acfd56bde269131f9d8863a ts=2026-10-14T19:18:02.5290000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6820] _id=6ad11e89de269131f9df1d21 ts=2026-10-15T18:42:17.3080000Z; 17h 7m: 6ab9a9279a8420a1e6b56b83.jsonl[3990] _id=6acee48ede269131f9d29c20 ts=2026-10-14T02:10:21.7310000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6757] _id=6acfd54ede269131f9d88309 ts=2026-10-14T19:17:33.9550000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 99h 2m 
  - Evidence: 99h 2m: 6ab9a9279a8420a1e6b56b83.jsonl[2531] _id=6ac91003de269131f9ca7426 ts=2026-10-09T16:02:10.8450000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3312] _id=6ace80bfde269131f9d15001 ts=2026-10-13T19:04:30.9590000Z; 47h 40m: 6ab9a9279a8420a1e6b56b83.jsonl[401] _id=6ac54941de269131f9b79ae1 ts=2026-10-06T19:17:21.0690000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[1159] _id=6ac7e7b9de269131f9c5d439 ts=2026-10-08T18:58:01.2750000Z; 24h 26m: 6ab9a9279a8420a1e6b56b83.jsonl[6066] _id=6acfcd00de269131f9d75f0a ts=2026-10-14T18:42:07.7190000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[7505] _id=6ad124c8de269131f9dffde5 ts=2026-10-15T19:08:56.1710000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.020s..0.037s shown 
  - Evidence: 20ms: 6ab9a9279a8420a1e6b56b83.jsonl[3639] _id=6acedf82de269131f9d29805 ts=2026-10-14T01:48:49.2560000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3643] _id=6acedf82de269131f9d29809 ts=2026-10-14T01:48:49.2760000Z; 22ms: 6ab9a9279a8420a1e6b56b83.jsonl[3315] _id=6ace80cfde269131f9d150f5 ts=2026-10-13T19:04:46.9090000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3319] _id=6ace80cfde269131f9d150f9 ts=2026-10-13T19:04:46.9310000Z; 37ms: 6ab9a9279a8420a1e6b56b83.jsonl[3638] _id=6acedf82de269131f9d29803 ts=2026-10-14T01:48:49.2190000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3639] _id=6acedf82de269131f9d29805 ts=2026-10-14T01:48:49.2560000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 69h 12m 
  - Evidence: 69h 12m: 6ab9a9279a8420a1e6b56b83.jsonl[13074] _id=6ad27388de269131f9e77e4c ts=2026-10-16T18:57:11.9650000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13124] _id=6ad640cade269131f9e9a349 ts=2026-10-19T16:09:45.5960000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 151h 44m 
  - Evidence: 151h 44m: 6ab9a9279a8420a1e6b56b83.jsonl[843] _id=6ac6993bde269131f9beffaf ts=2026-10-07T19:10:50.6140000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[5830] _id=6aceef34de269131f9d2b177 ts=2026-10-14T02:55:47.8010000Z; 29h 52m: 6ab9a9279a8420a1e6b56b83.jsonl[6669] _id=6acfd438de269131f9d84cc4 ts=2026-10-14T19:12:55.5490000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11119] _id=6ad17873de269131f9e262a5 ts=2026-10-16T01:05:55.3380000Z; 16h 17m: 6ab9a9279a8420a1e6b56b83.jsonl[5830] _id=6aceef34de269131f9d2b177 ts=2026-10-14T02:55:47.8010000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6669] _id=6acfd438de269131f9d84cc4 ts=2026-10-14T19:12:55.5490000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 151h 43m 
  - Evidence: 151h 43m: 6ab9a9279a8420a1e6b56b83.jsonl[844] _id=6ac6993bde269131f9beffb1 ts=2026-10-07T19:10:50.6440000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[5837] _id=6aceeedade269131f9d2b0ef ts=2026-10-14T02:54:17.8390000Z; 29h 52m: 6ab9a9279a8420a1e6b56b83.jsonl[6672] _id=6acfd438de269131f9d84ccc ts=2026-10-14T19:12:55.6290000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11083] _id=6ad1783ade269131f9e26172 ts=2026-10-16T01:04:58.0770000Z; 16h 13m: 6ab9a9279a8420a1e6b56b83.jsonl[5877] _id=6aceef34de269131f9d2b179 ts=2026-10-14T02:55:47.8460000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6600] _id=6acfd36ade269131f9d829d8 ts=2026-10-14T19:09:30.4150000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.037s..0.037s shown 
  - Evidence: 37ms: 6ab9a9279a8420a1e6b56b83.jsonl[11896] _id=6ad18698de269131f9e2a5dd ts=2026-10-16T02:06:15.9400000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11901] _id=6ad18698de269131f9e2a5e0 ts=2026-10-16T02:06:15.9770000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 151h 43m 
  - Evidence: 151h 43m: 6ab9a9279a8420a1e6b56b83.jsonl[836] _id=6ac69935de269131f9beff58 ts=2026-10-07T19:10:45.0050000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[5822] _id=6aceeeedde269131f9d2b0fe ts=2026-10-14T02:54:36.4230000Z; 29h 51m: 6ab9a9279a8420a1e6b56b83.jsonl[6665] _id=6acfd435de269131f9d84c4d ts=2026-10-14T19:12:52.8370000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11076] _id=6ad17835de269131f9e26164 ts=2026-10-16T01:04:52.8310000Z; 16h 13m: 6ab9a9279a8420a1e6b56b83.jsonl[5829] _id=6aceef2ede269131f9d2b173 ts=2026-10-14T02:55:41.5090000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6603] _id=6acfd36ede269131f9d82a89 ts=2026-10-14T19:09:33.6990000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b83.jsonl[11551] _id=6ad18428de269131f9e29aa8 ts=2026-10-16T01:55:51.6420000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11552] _id=6ad18428de269131f9e29aaa ts=2026-10-16T01:55:51.6460000Z; 4ms: 6ab9a9279a8420a1e6b56b83.jsonl[5855] _id=6aceef11de269131f9d2b136 ts=2026-10-14T02:55:12.8690000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[5856] _id=6aceef11de269131f9d2b138 ts=2026-10-14T02:55:12.8730000Z; 5ms: 6ab9a9279a8420a1e6b56b83.jsonl[11108] _id=6ad1785dde269131f9e2623e ts=2026-10-16T01:05:33.3370000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[11112] _id=6ad1785dde269131f9e26240 ts=2026-10-16T01:05:33.3420000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 69h 11m 
  - Evidence: 69h 11m: 6ab9a9279a8420a1e6b56b83.jsonl[13093] _id=6ad273ccde269131f9e78388 ts=2026-10-16T18:58:19.4760000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13111] _id=6ad640b2de269131f9e9a233 ts=2026-10-19T16:09:21.3490000Z; 19h 6m: 6ab9a9279a8420a1e6b56b83.jsonl[8606] _id=6ad1614fde269131f9e20321 ts=2026-10-15T23:27:10.8200000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[12325] _id=6ad26e06de269131f9e708b1 ts=2026-10-16T18:33:41.4570000Z; 4h 15m: 6ab9a9279a8420a1e6b56b83.jsonl[7627] _id=6ad1254ade269131f9e01288 ts=2026-10-15T19:11:05.5600000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[8605] _id=6ad1613ede269131f9e202f3 ts=2026-10-15T23:26:54.2220000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 99h 0m 
  - Evidence: 99h 0m: 6ab9a9279a8420a1e6b56b83.jsonl[2457] _id=6ac90f3dde269131f9ca6ee0 ts=2026-10-09T15:58:52.4590000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3230] _id=6ace7f91de269131f9d1392e ts=2026-10-13T18:59:29.2110000Z; 69h 35m: 6ab9a9279a8420a1e6b56b83.jsonl[12323] _id=6ad26df8de269131f9e70732 ts=2026-10-16T18:33:26.9180000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13109] _id=6ad64085de269131f9e9a0f9 ts=2026-10-19T16:08:36.6840000Z; 24h 6m: 6ab9a9279a8420a1e6b56b83.jsonl[5954] _id=6acfcaf6de269131f9d718fc ts=2026-10-14T18:33:25.6420000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6767] _id=6ad11df0de269131f9df0c6f ts=2026-10-15T18:39:44.1240000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 99h 0m 
  - Evidence: 99h 0m: 6ab9a9279a8420a1e6b56b83.jsonl[2456] _id=6ac90f3dde269131f9ca6edf ts=2026-10-09T15:58:52.4580000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3229] _id=6ace7f91de269131f9d1392d ts=2026-10-13T18:59:29.2110000Z; 69h 35m: 6ab9a9279a8420a1e6b56b83.jsonl[12322] _id=6ad26df8de269131f9e70731 ts=2026-10-16T18:33:26.9180000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13108] _id=6ad64085de269131f9e9a0f8 ts=2026-10-19T16:08:36.6840000Z; 23h 46m: 6ab9a9279a8420a1e6b56b83.jsonl[6202] _id=6acfcf88de269131f9d7aaef ts=2026-10-14T18:52:55.9820000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[6766] _id=6ad11df0de269131f9df0c6e ts=2026-10-15T18:39:44.1240000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 105h 49m 
  - Evidence: 105h 49m: 6ab9a9279a8420a1e6b56b83.jsonl[3227] _id=6ace7f91de269131f9d13925 ts=2026-10-09T16:11:02.582Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3792] _id=6acee24dde269131f9d29964 ts=2026-10-14T02:00:44.4400000Z; 68h 53m: 6ab9a9279a8420a1e6b56b83.jsonl[408] _id=6ac692d3de269131f9bdf14a ts=2026-10-06T19:17:36.682Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3227] _id=6ace7f91de269131f9d13925 ts=2026-10-09T16:11:02.582Z; 28h 46m: 6ab9a9279a8420a1e6b56b83.jsonl[6195] _id=6acfcf5ade269131f9d7a60b ts=2026-10-14T18:52:10.0770000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[8790] _id=6ad163f4de269131f9e20bfd ts=2026-10-15T23:38:28.0940000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 98h 49m 
  - Evidence: 98h 49m: 6ab9a9279a8420a1e6b56b83.jsonl[3224] _id=6ac91204de269131f9ca7d70 ts=2026-10-09T16:10:44.0090000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[3233] _id=6ace7fa6de269131f9d13a0f ts=2026-10-13T18:59:49.3330000Z; 69h 18m: 6ab9a9279a8420a1e6b56b83.jsonl[12957] _id=6ad2721ede269131f9e76247 ts=2026-10-16T18:51:09.1950000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[13114] _id=6ad640b5de269131f9e9a25a ts=2026-10-19T16:09:23.7190000Z; 23h 40m: 6ab9a9279a8420a1e6b56b83.jsonl[153] _id=6ac545fdde269131f9b73537 ts=2026-10-06T19:03:24.9730000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[417] _id=6ac692ecde269131f9bdf43c ts=2026-10-07T18:43:54.7860000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b83.jsonl[765] _id=6ac697eade269131f9bede6a ts=2026-10-07T19:05:13.6810000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[766] _id=6ac697eade269131f9bede6b ts=2026-10-07T19:05:13.6820000Z; 6ms: 6ab9a9279a8420a1e6b56b83.jsonl[12772] _id=6ad26fcfde269131f9e736dc ts=2026-10-16T18:41:18.9320000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[12773] _id=6ad26fd0de269131f9e736e2 ts=2026-10-16T18:41:18.9380000Z; 6ms: 6ab9a9279a8420a1e6b56b83.jsonl[12822] _id=6ad27073de269131f9e7416f ts=2026-10-16T18:44:02.1590000Z -> 6ab9a9279a8420a1e6b56b83.jsonl[12823] _id=6ad27073de269131f9e7417d ts=2026-10-16T18:44:02.1650000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[737] _id=6ac697a4de269131f9bed033 ts=2026-10-07T19:04:03.3260000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[852] _id=6ac69952de269131f9bf01a1 ts=2026-10-07T19:11:13.8260000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[5145] _id=6acee75bde269131f9d2a57b ts=2026-10-14T02:22:18.3520000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[6672] _id=6acfd438de269131f9d84ccc ts=2026-10-14T19:12:55.6290000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[11901] _id=6ad18698de269131f9e2a5e0 ts=2026-10-16T02:06:15.9770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[12325] _id=6ad26e06de269131f9e708b1 ts=2026-10-16T18:33:41.4570000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[13093] _id=6ad273ccde269131f9e78388 ts=2026-10-16T18:58:19.4760000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[13111] _id=6ad640b2de269131f9e9a233 ts=2026-10-19T16:09:21.3490000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[5102] _id=6acee6c8de269131f9d2a4e7 ts=2026-10-14T02:19:51.6650000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[6842] _id=6ad11edbde269131f9df2a47 ts=2026-10-15T18:43:39.4360000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[9994] _id=6ad16e20de269131f9e231cd ts=2026-10-16T00:21:52.1620000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[948] _id=6ac69a8ede269131f9bf1d89 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 88 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[4154] _id=6acee58dde269131f9d29dd0 ts=2026-10-14T02:14:35.3940000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[4168] _id=6acee58ede269131f9d29dd2 ts=2026-10-14T02:14:35.3940000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[4171] _id=6acee58fde269131f9d29dd9 ts=2026-10-14T02:14:35.6930000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 291 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[1120] _id=6ac7e7a0de269131f9c5cfca ts=2026-10-08T18:57:34.7420000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[1125] _id=6ac7e7a0de269131f9c5cfcb ts=2026-10-08T18:57:34.8180000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[1126] _id=6ac7e7a0de269131f9c5cfd3 ts=2026-10-08T18:57:34.8180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[6820] _id=6ad11e89de269131f9df1d21 ts=2026-10-15T18:42:17.3080000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[6619] _id=6acfd394de269131f9d830b2 ts=2026-10-14T19:10:11.2390000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[6620] _id=6acfd394de269131f9d830f0 ts=2026-10-14T19:10:12.2680000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 12 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 407 start, 399 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 24 unmatched 'BecameVisible' (totals: 1165 open, 1141 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 3 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 44 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 255 of 13146 adjacent _id pairs reverse in client time; worst 419.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b83.jsonl[1263] _id=6ac7e84fde269131f9c5e847 ts=2026-10-08T19:00:30.6210000Z`; `6ab9a9279a8420a1e6b56b83.jsonl[1269] _id=6ac7e84fde269131f9c5e855 ts=2026-10-08T18:53:31.5640000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.86s, min -355706.87s, max -0.32s over 13147 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b83\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 3802 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2430); Unit 4 Dev (694); Unit 3 Dungeon Dev (378); Unit 5 Dev - Dungeon (300)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.70s, n=3801)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3802/3802 records)
    "BecameVisible"  x1165
    "BecameInvisible"  x1141
    "BecameCameraCentered"  x748
    "BecameCameraUncentered"  x748
data.pieceId  (string, 3802/3802 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3802/3802 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3192 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (902); Unit 3 Dungeon Dev (626); Unit 4 Dev - Dungeon (450); Unit 3 Dev (343); Unit 1 Dev (342); Unit 4 Dev (222); Unit 5 Dev - Dungeon (207); Unit 4 Dev - Anderson Base (100)
- **Intervals:** median 2.26s (p5 0.16s / p95 27.35s, n=3191)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3192/3192 records)
    "pressed"  x3192
data.actionType  (string, 3192/3192 records)
    "Move"  x2250
    "Interact"  x604
    "Ascend"  x89
    "Hoverboard"  x84
    "Sprint"  x78
    "Jump"  x59
    "Map"  x21
    "Pause"  x5
    "SkipCinematic"  x2
data.key  (string, 3192/3192 records, 11 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3192/3192 records)
    "Player"  x2680
    "Drone"  x512
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2889 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (772); Unit 4 Dev - Anderson Base (414); Unit 3 Dev (365); Unit 3 Dungeon Dev (339); Unit 1 Dev (313); Unit 4 Dev - Dungeon (262); Unit 4 Dev (260); Unit 5 Dev - Dungeon (157); Unit 5 Dev (7)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.09s, n=2876)
- **Fields under `data`:**

```text
data.position  (object, 2889/2889 records)
data.position.x  (number, 2889/2889 records)
    numeric range -683.155 .. 1550.74 (1090 unique)
data.position.y  (number, 2889/2889 records)
    numeric range -115.128 .. 222.252 (639 unique)
data.position.z  (number, 2889/2889 records)
    numeric range -1088.59 .. 2135.05 (1091 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2065 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (657); Unit 3 Dev (320); Unit 4 Dev (300); Unit 1 Dev (211); Unit 3 Dungeon Dev (204); Unit 4 Dev - Anderson Base (163); Unit 4 Dev - Dungeon (119); Unit 5 Dev - Dungeon (87); Unit 5 Dev (4)
- **eventKey:** present on 1259 of 2065 records
- **Intervals:** median 4.34s (p5 0.00s / p95 50.87s, n=2064)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1259; [conversationId, dialogueEventType] x806
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2065/2065 records)
    numeric range 8 .. 116 (50 unique)
data.dialogueEventType  (string, 2065/2065 records)
    "DialogueNodeEvent"  x1259
    "DialogueStartEvent"  x407
    "DialogueFinishEvent"  x399
data.nodeId  (number, 1259/2065 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 409 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (323); Unit 3 Dev (35); Unit 2 Prod (Refactor) (33); Unit 1 Dev (18)
- **Intervals:** median 0.65s (p5 0.05s / p95 15.99s, n=408)
- **Fields under `data`:**

```text
data.actionType  (string, 409/409 records)
    "argumentationNodeHoverEnd"  x172
    "argumentationNodeHoverStart"  x172
    "argumentationNodeAdd"  x40
    "argumentationNodeRemove"  x25
data.argumentationTitle  (string, 409/409 records)
    "Unit 4 - Flooding"  x323
    "Unit 3 - Pollution Upstream"  x35
    "Unit 2 – Watershed"  x33
    "Unit 1 - Freshwater"  x15
    "Unit 1 - Argumentation Tutorial"  x3
data.nodeName  (string, 409/409 records)
    "A"  x52
    "C"  x51
    "B"  x50
    "1"  x49
    "2"  x45
    "II"  x40
    "D"  x35
    "4"  x30
    "I"  x28
    "3"  x26
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 367 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (120); Unit 2 Prod (Refactor) (95); Unit 4 Dev - Dungeon (76); Unit 4 Dev (27); Unit 1 Dev (14); Unit 5 Dev - Dungeon (14); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 13.63s (p5 0.16s / p95 422.25s, n=366)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 367/367 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 367/367 records)
    102 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 83 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (49); Unit 3 Dev (23); Unit 3 Dungeon Dev (6); Unit 1 Dev (5)
- **Intervals:** median 7.12s (p5 0.22s / p95 56411.75s, n=82)
- **`data` key-set variants:** [actionType, featureUsed] x50; [actionType, featureUsed, location] x29; [actionType, featureUsed, legendName] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 83/83 records)
    "MapCloseEvent"  x25
    "MapOpenEvent"  x25
    "WaypointMoveEvent"  x22
    "WaypointSetEvent"  x6
    "Selected"  x4
    "WaypointResetEvent"  x1
data.featureUsed  (string, 83/83 records)
    "Map"  x50
    "Waypoint"  x29
    "Legend"  x4
data.legendName  (string, 4/83 records)
    "0 ft"  x1
    "Aryn's Room"  x1
    "Teleporter Room"  x1
    "Water"  x1
data.location  (object, 29/83 records)
data.location.x  (number, 29/83 records)
    numeric range -340.5 .. 459.136 (24 unique)
data.location.y  (number, 29/83 records)
    numeric range -304.106 .. 141.567 (28 unique)
data.location.z  (number, 29/83 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 78 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (15); Unit 3 Dev (11); Unit 4 Dev (11); Unit 4 Dev - Dungeon (11); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 78 of 78 records
- **Intervals:** median 226.95s (p5 0.01s / p95 84475.99s, n=77)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 78/78 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x34
data.questID  (string, 78/78 records)
    31 unique values (see csv/event_unique_values.csv)
data.questName  (string, 78/78 records)
    31 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/78 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 37 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (15); Unit 2 Prod (Refactor) (14); Unit 4 Dev (8)
- **Intervals:** median 3.43s (p5 0.97s / p95 67287.86s, n=36)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x28; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/37 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/37 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x3
    "Unit 4 Dev"  x2
data.actionType  (string, 28/37 records)
    "RightDrag"  x18
    "LeftDrag"  x10
data.currentSoilType  (string, 28/37 records)
    "CLAY"  x9
    "CLAYSAND"  x7
    "CLAYROCK"  x5
    "SAND"  x5
    "SANDGRAVEL"  x2
data.isCorrectSelection  (string, 28/37 records)
    "false"  x16
    "true"  x12
data.waterLevelStatus  (string, 28/37 records)
    "TooHigh"  x16
    "Proper"  x7
    "TooLow"  x5
data.waterRetentionChange  (string, 28/37 records)
    "NoChange"  x12
    "Increase"  x10
    "Decrease"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 36 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 3 Dev (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 727.15s (p5 9.90s / p95 135874.14s, n=35)
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "DebugMenuStateChanged"  x36
data.isOpened  (bool, 36/36 records)
    false  x36
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 32 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (32)
- **Intervals:** median 28.70s (p5 5.85s / p95 142.63s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "On"  x23
    "Off"  x9
data.floor  (string, 32/32 records)
    "3"  x14
    "4"  x13
    "2"  x3
    "1"  x2
data.machineNumber  (string, 32/32 records)
    "One"  x31
    "Two"  x1
data.machineType  (string, 32/32 records)
    "Condenser"  x17
    "Evaporator"  x8
    "VentSwitch"  x3
    "DualChamber_Condenser"  x2
    "DualChamber_Evaporator"  x2
data.room  (string, 32/32 records)
    "2"  x14
    "3"  x10
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 31 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (28); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 27.18s (p5 5.07s / p95 85551.37s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "submitAnswerEvent"  x31
data.answerSubmitted  (string, 31/31 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 31/31 records)
    "Unit 4 - Flooding"  x28
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 29 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 4 Dev - Dungeon (4); Unit 4 Dev (3); Unit 4 Dev - Anderson Base (2); Transition (1); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 1334.54s (p5 120.49s / p95 192794.20s, n=28)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 29/29 records)
    true  x29
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 23 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 1 Dev (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 4.04s (p5 0.01s / p95 172612.21s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "Open"  x12
    "Close"  x11
data.toolName  (string, 23/23 records, 19 empty-string)
    ""  x19
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 55931.40s (p5 1869.29s / p95 282287.86s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev - Dungeon (4); Unit 4 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Anderson Base (2); Transition (1); Unit 3 Dev (1)
- **Intervals:** median 642.79s (p5 104.34s / p95 294547.49s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 90.01s (p5 0.04s / p95 326864.82s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 9 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (9)
- **Intervals:** median 111.81s (p5 5.21s / p95 306.05s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "ChangeCanister"  x9
data.canisterType  (string, 9/9 records)
    "Clay"  x3
    "Gravel"  x3
    "Sand"  x2
    "Bedrock"  x1
data.floor  (string, 9/9 records)
    "4"  x4
    "5"  x4
    "3"  x1
data.machine  (string, 9/9 records)
    "1"  x7
    "2"  x2
data.row  (string, 9/9 records)
    "TopRow"  x8
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 17.11s (p5 9.31s / p95 52.52s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 3 empty-string)
    "cameraPlaced"  x5
    ""  x3
data.boxId  (string, 8/8 records)
    "0"  x3
    "1"  x3
    "2"  x2
data.soilType  (string, 8/8 records)
    "Gravel"  x4
    "None"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 7 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 8413.34s (p5 17.86s / p95 203994.06s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "Close"  x5
    "Open"  x2
data.chatID  (string, 7/7 records)
    "NA"  x5
    "[73-208, 73-209, 73-210, 73-211, 73-212]"  x1
    "[79-119, 79-120, 79-121, 79-123, 79-124]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 160618.75s (p5 25152.87s / p95 507819.67s, n=3)
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

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (3)
- **Intervals:** median 0.78s (p5 0.55s / p95 1.00s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationToolOpen"  x3
data.argumentationTitle  (string, 3/3 records)
    "Unit 3 - Pollution Upstream"  x3
data.toolName  (string, 3/3 records)
    "BackingInfoPanel - Pollution Site Data"  x3
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (14 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "WaypointMoveEvent" (22x); "WaypointResetEvent" (1x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (4x); "Waypoint" (29x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (25x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*