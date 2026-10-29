# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba4

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba4
- **Game version string(s) in log:** 2.8.4, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba4.jsonl
- **Records:** 14823 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba4
- **Time span:** 2026-10-06T20:00:19.543000+00:00 .. 2026-10-19T16:16:34.456000+00:00 (308h 16m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba4\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 14823 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 101 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4513 | 30.45 | 1 | 9 | 0 | 2026-10-06T20:00:33.100000+00:00 | 2026-10-19T16:16:27.002000+00:00 | 308h 15m |
| PuzzlePieceVisibleEvent | 3153 | 21.27 | 1 | 4 | 0 | 2026-10-08T20:10:36.795000+00:00 | 2026-10-16T16:00:47.001000+00:00 | 187h 50m |
| DialogueEvent | 2641 | 17.82 | 1 | 9 | 1620 | 2026-10-06T20:00:49.332000+00:00 | 2026-10-19T16:16:34.052000+00:00 | 308h 15m |
| PlayerPositionEvent | 2551 | 17.21 | 1 | 9 | 0 | 2026-10-06T20:00:29.439000+00:00 | 2026-10-19T16:16:34.456000+00:00 | 308h 16m |
| argumentationNodeEvent | 863 | 5.82 | 1 | 5 | 0 | 2026-10-07T20:04:01.654000+00:00 | 2026-10-19T16:14:01.466000+00:00 | 284h 9m |
| ObjectInterEvent | 367 | 2.48 | 1 | 9 | 0 | 2026-10-06T20:05:54.841000+00:00 | 2026-10-19T16:07:03.823000+00:00 | 308h 1m |
| argumentationAnswerEvent | 156 | 1.05 | 1 | 5 | 0 | 2026-10-07T20:05:16.613000+00:00 | 2026-10-19T16:14:04.898000+00:00 | 284h 8m |
| TopographicMapEvent | 124 | 0.84 | 1 | 4 | 0 | 2026-10-13T13:55:16.995000+00:00 | 2026-10-16T02:11:24.804000+00:00 | 60h 16m |
| questEvent | 98 | 0.66 | 1 | 9 | 98 | 2026-10-06T20:00:49.299000+00:00 | 2026-10-19T16:15:14.787000+00:00 | 308h 14m |
| DEBUGMenu | 55 | 0.37 | 1 | 9 | 0 | 2026-10-06T20:00:19.543000+00:00 | 2026-10-19T15:55:14.521000+00:00 | 307h 54m |
| Soil Key Puzzle | 52 | 0.35 | 1 | 3 | 0 | 2026-10-13T19:51:20.964000+00:00 | 2026-10-15T19:37:11.658000+00:00 | 47h 45m |
| WaterChamberEvent | 52 | 0.35 | 1 | 1 | 0 | 2026-10-16T15:58:43.548000+00:00 | 2026-10-19T16:01:04.055000+00:00 | 72h 2m |
| gameWindowFocusEvent | 35 | 0.24 | 1 | 7 | 0 | 2026-10-06T20:00:19.882000+00:00 | 2026-10-19T15:55:06.797000+00:00 | 307h 54m |
| DaniEvent | 32 | 0.22 | 1 | 4 | 0 | 2026-10-08T19:40:56.021000+00:00 | 2026-10-15T20:05:25.229000+00:00 | 168h 24m |
| gameStartEvent | 25 | 0.17 | 1 | 1 | 0 | 2026-10-06T20:00:19.882000+00:00 | 2026-10-19T15:55:06.797000+00:00 | 307h 54m |
| gameWindowUnfocusEvent | 21 | 0.14 | 1 | 8 | 0 | 2026-10-07T19:44:47.689000+00:00 | 2026-10-16T20:11:51.256000+00:00 | 216h 27m |
| argumentationEvent | 19 | 0.13 | 1 | 5 | 0 | 2026-10-07T20:05:03.771000+00:00 | 2026-10-19T16:14:04.927000+00:00 | 284h 9m |
| soilMachine | 19 | 0.13 | 1 | 1 | 0 | 2026-10-15T19:52:28.609000+00:00 | 2026-10-15T20:09:09.942000+00:00 | 16m 41s |
| TerasGardenBox | 18 | 0.12 | 1 | 1 | 0 | 2026-10-16T03:13:36.458000+00:00 | 2026-10-16T03:15:39.759000+00:00 | 2m 3s |
| argumentationToolEvent | 12 | 0.08 | 1 | 4 | 0 | 2026-10-07T20:05:00.413000+00:00 | 2026-10-19T16:13:06.317000+00:00 | 284h 8m |
| chatEvent | 12 | 0.08 | 1 | 4 | 0 | 2026-10-08T19:43:38.540000+00:00 | 2026-10-19T16:02:21.831000+00:00 | 260h 18m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-08T20:04:22.923000+00:00 | 2026-10-16T03:26:51.374000+00:00 | 175h 22m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 95046.505s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.05s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.238s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 1.033s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 48.378s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 7701.525s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8638.056s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1941.81s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2539.759s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.196s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.6x vs baseline. 
  - Observed: 55 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 32 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
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
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 31.2x vs baseline. 
  - Observed: 156 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,4,I; A,B,2,II; A,B,C,3,4,II; A,C,2,II; A,C,3,4,II; A,C,3,II; A,C,4,II; A,C,B,3,4,II; A,D,2,II; B,1,II; B,2,I; B,2,II; B,3,II; B,4,II; B,A,2,II; B,C,2,II; B,C,3,4,II; B,C,D,2,II; B,C,D,3,4,II; B,C,D,3,II; C,2,II; C,A,2,II; C,A,3,4,II; C,B,2,II; C,B,3,4,II; C,D,2,II; C,D,3,4,II; C,D,3,II; C,D,A,2,II; C,D,B,3,4,II; D,2,II; D,B,C,2,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 863 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 6.0x vs baseline. 
  - Observed: 12 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [11-31, 11-25, 11-230, 11-230, 11-26]; [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 25 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments 
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

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[5] _id=6ac55354de269131f9b7ff26 ts=2026-10-06T20:00:19.8820000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[197] _id=6ac6a0e6de269131f9bf2edc ts=2026-10-07T19:43:33.5560000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[700] _id=6ac7f17fde269131f9c6b093 ts=2026-10-08T19:39:42.7130000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 35 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 35} 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[4] _id=6ac55354de269131f9b7ff25 ts=2026-10-06T20:00:19.8820000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[196] _id=6ac6a0e6de269131f9bf2edb ts=2026-10-07T19:43:33.5560000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[241] _id=6ac6a132de269131f9bf35b6 ts=2026-10-07T19:44:49.9980000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[240] _id=6ac6a130de269131f9bf3573 ts=2026-10-07T19:44:47.6890000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[697] _id=6ac7f17ede269131f9c6b08d ts=2026-10-07T20:10:34.459Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1462] _id=6ace3725de269131f9cee42e ts=2026-10-08T20:10:59.605Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 124 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[1598] _id=6ace3845de269131f9cef371 ts=2026-10-13T13:55:16.9950000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1544] _id=6ace384fde269131f9cef442 ts=2026-10-13T13:55:27.1560000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1545] _id=6ace3850de269131f9cef450 ts=2026-10-13T13:55:27.8970000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4512 | 0.0 | 0.765 | 245.956 | 17.442 | 409227.633 | 0.24 | 236 | 20 |
| PuzzlePieceVisibleEvent | 3152 | 0.0 | 0.05 | 214.534 | 1.68 | 409408.127 | 0.28 | 1581 | 11 |
| DialogueEvent | 2640 | 0.0 | 4.21 | 420.358 | 33.158 | 409229.494 | 0.14 | 765 | 17 |
| PlayerPositionEvent | 2539 | 9.788 | 10.002 | 436.534 | 10.133 | 409191.995 | 0.14 | 0 | 14 |
| argumentationNodeEvent | 862 | 0.007 | 0.509 | 1186.775 | 15.55 | 506225.383 | 0.05 | 67 | 6 |
| ObjectInterEvent | 366 | 0.0 | 8.892 | 3029.697 | 482.707 | 409403.807 | 0.02 | 7 | 17 |
| argumentationAnswerEvent | 155 | 0.139 | 1.033 | 6599.537 | 206.63 | 506315.978 | 0.01 | 0 | 6 |
| TopographicMapEvent | 123 | 0.026 | 6.238 | 1763.966 | 1812.353 | 73504.606 | 0.03 | 2 | 12 |
| questEvent | 97 | 0.0 | 206.317 | 11439.85 | 68730.659 | 409374.251 | 0.01 | 19 | 22 |
| DEBUGMenu | 54 | 6.912 | 400.277 | 20527.685 | 85655.783 | 409470.277 | 0.0 | 0 | 25 |
| Soil Key Puzzle | 51 | 0.158 | 1.511 | 3371.582 | 1693.156 | 85341.424 | 0.02 | 0 | 3 |
| WaterChamberEvent | 51 | 0.932 | 12.499 | 5085.108 | 96.808 | 243853.502 | 0.01 | 0 | 2 |
| gameWindowFocusEvent | 34 | 64.25 | 1941.81 | 32602.556 | 141288.492 | 409480.165 | 0.0 | 0 | 24 |
| DaniEvent | 31 | 0.006 | 2.257 | 19557.071 | 79210.055 | 433324.436 | 0.0 | 4 | 4 |
| gameStartEvent | 24 | 83.457 | 8638.056 | 46186.955 | 220244.63 | 409480.164 | 0.0 | 0 | 21 |
| gameWindowUnfocusEvent | 20 | 0.0 | 2539.759 | 38961.178 | 102584.636 | 409614.936 | 0.0 | 3 | 12 |
| argumentationEvent | 18 | 0.026 | 91.434 | 56830.064 | 336020.544 | 506221.352 | 0.0 | 1 | 6 |
| soilMachine | 18 | 0.832 | 4.196 | 55.63 | 216.535 | 359.9 | 1.08 | 0 | 0 |
| TerasGardenBox | 17 | 0.68 | 2.061 | 7.253 | 24.522 | 29.818 | 8.27 | 0 | 0 |
| argumentationToolEvent | 11 | 1.52 | 48.378 | 92989.628 | 462700.148 | 506317.502 | 0.0 | 0 | 4 |
| chatEvent | 11 | 1.372 | 7701.525 | 85193.026 | 376317.353 | 508735.59 | 0.0 | 0 | 6 |
| EndOfUnit | 3 | 29679.03 | 95046.505 | 210449.484 | 465465.275 | 506622.916 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 12 group(s), 16 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[4898] _id=6acfa5e7de269131f9d500f6 ts=2026-10-14T15:55:18.0550000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[4899] _id=6acfa5e7de269131f9d500f7 ts=2026-10-14T15:55:18.0550000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[4900] _id=6acfa5e7de269131f9d500f8 ts=2026-10-14T15:55:18.0560000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[4901] _id=6acfa5e7de269131f9d500f9 ts=2026-10-14T15:55:18.0560000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[4903] _id=6acfa5e7de269131f9d500fb ts=2026-10-14T15:55:18.0570000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[4904] _id=6acfa5e7de269131f9d500fc ts=2026-10-14T15:55:18.0570000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 54 group(s), 89 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[1552] _id=6ace380dde269131f9cef046 ts=2026-10-13T13:54:18.8100000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[1558] _id=6ace380dde269131f9cef04b ts=2026-10-13T13:54:18.8100000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1559] _id=6ace380dde269131f9cef04d ts=2026-10-13T13:54:18.9880000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[1555] _id=6ace380dde269131f9cef053 ts=2026-10-13T13:54:18.9880000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1573] _id=6ace381fde269131f9cef157 ts=2026-10-13T13:54:37.8670000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[1574] _id=6ace3820de269131f9cef16d ts=2026-10-13T13:54:37.8670000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[14776] _id=6ad64213de269131f9e9a9d8 ts=2026-10-19T16:15:14.7870000Z == 6ab9a9439a8420a1e6b56ba4.jsonl[14777] _id=6ad64213de269131f9e9a9d9 ts=2026-10-19T16:15:14.7870000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 59 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba4.jsonl[134] _id=6ac554a3de269131f9b82ffa ts=2026-10-06T20:05:54.8410000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[135] _id=6ac554a3de269131f9b83000 ts=2026-10-06T20:05:54.8460000Z`; `5ms: 6ab9a9439a8420a1e6b56ba4.jsonl[249] _id=6ac6a141de269131f9bf376b ts=2026-10-07T19:45:05.2950000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[250] _id=6ac6a141de269131f9bf3771 ts=2026-10-07T19:45:05.3000000Z`; `447ms: 6ab9a9439a8420a1e6b56ba4.jsonl[762] _id=6ac7f20bde269131f9c6bd07 ts=2026-10-08T19:42:03.2030000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[764] _id=6ac7f20bde269131f9c6bd19 ts=2026-10-08T19:42:03.6500000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `849ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12896] _id=6ad196dade269131f9e2e45b ts=2026-10-16T03:15:37.5180000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[12898] _id=6ad196dade269131f9e2e461 ts=2026-10-16T03:15:38.3670000Z`; `680ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12898] _id=6ad196dade269131f9e2e461 ts=2026-10-16T03:15:38.3670000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[12889] _id=6ad196dbde269131f9e2e467 ts=2026-10-16T03:15:39.0470000Z`; `712ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12889] _id=6ad196dbde269131f9e2e467 ts=2026-10-16T03:15:39.0470000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[12891] _id=6ad196dcde269131f9e2e46d ts=2026-10-16T03:15:39.7590000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `634ms: 6ab9a9439a8420a1e6b56ba4.jsonl[1606] _id=6ace3875de269131f9cef688 ts=2026-10-13T13:56:04.4840000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[1609] _id=6ace3875de269131f9cef695 ts=2026-10-13T13:56:05.1180000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 75 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `185ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11700] _id=6ad18af2de269131f9e2b846 ts=2026-10-16T02:24:49.9550000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[11714] _id=6ad18af2de269131f9e2b84d ts=2026-10-16T02:24:50.1400000Z`; `877ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12038] _id=6ad18cd3de269131f9e2bd6b ts=2026-10-16T02:32:50.7300000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[12039] _id=6ad18cd4de269131f9e2bd6f ts=2026-10-16T02:32:51.6070000Z`; `881ms: 6ab9a9439a8420a1e6b56ba4.jsonl[14544] _id=6ad640ebde269131f9e9a4c9 ts=2026-10-19T16:10:19.1350000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[14543] _id=6ad640ecde269131f9e9a4cf ts=2026-10-19T16:10:20.0160000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `52ms: 6ab9a9439a8420a1e6b56ba4.jsonl[7204] _id=6acfdccdde269131f9d9193b ts=2026-10-14T19:49:32.6450000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[7200] _id=6acfdccdde269131f9d9193f ts=2026-10-14T19:49:32.6970000Z`; `26ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12693] _id=6ad19538de269131f9e2de2c ts=2026-10-16T03:08:40.0800000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[12705] _id=6ad19538de269131f9e2de2f ts=2026-10-16T03:08:40.1060000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 56 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `796ms: 6ab9a9439a8420a1e6b56ba4.jsonl[523] _id=6ac6a5b2de269131f9bf73c3 ts=2026-10-07T20:04:01.6540000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[522] _id=6ac6a5b3de269131f9bf73e4 ts=2026-10-07T20:04:02.4500000Z`; `451ms: 6ab9a9439a8420a1e6b56ba4.jsonl[592] _id=6ac6a663de269131f9bf811c ts=2026-10-07T20:06:58.8100000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[591] _id=6ac6a663de269131f9bf812f ts=2026-10-07T20:06:59.2610000Z`; `984ms: 6ab9a9439a8420a1e6b56ba4.jsonl[590] _id=6ac6a663de269131f9bf811e ts=2026-10-07T20:06:58.8760000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[593] _id=6ac6a664de269131f9bf813c ts=2026-10-07T20:06:59.8600000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[3184] _id=6ace904ade269131f9d2543a ts=2026-10-13T20:10:49.6300000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[3185] _id=6ace925ede269131f9d254b8 ts=2026-10-13T20:10:49.63Z`; `0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[7957] _id=6acfdf77de269131f9d944fc ts=2026-10-14T20:00:54.7420000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[8001] _id=6acfdf88de269131f9d945e9 ts=2026-10-14T20:00:54.742Z`; `0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[14053] _id=6ad28507de269131f9e80441 ts=2026-10-16T20:11:51.2560000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[14060] _id=6ad63d5bde269131f9e987b3 ts=2026-10-16T20:11:51.256Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `841ms: 6ab9a9439a8420a1e6b56ba4.jsonl[10509] _id=6ad12fb7de269131f9e0e398 ts=2026-10-15T19:55:35.4290000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[10539] _id=6ad12fb8de269131f9e0e3a8 ts=2026-10-15T19:55:36.2700000Z`; `832ms: 6ab9a9439a8420a1e6b56ba4.jsonl[10539] _id=6ad12fb8de269131f9e0e3a8 ts=2026-10-15T19:55:36.2700000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[10541] _id=6ad12fb9de269131f9e0e3b5 ts=2026-10-15T19:55:37.1020000Z`; `856ms: 6ab9a9439a8420a1e6b56ba4.jsonl[10832] _id=6ad13162de269131f9e10005 ts=2026-10-15T20:02:41.9220000Z ~ 6ab9a9439a8420a1e6b56ba4.jsonl[10834] _id=6ad13163de269131f9e10012 ts=2026-10-15T20:02:42.7780000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 113h 44m 
  - Evidence: 113h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[1327] _id=6ac7f7a7de269131f9c731d7 ts=2026-10-08T20:05:58.7430000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1463] _id=6ace3726de269131f9cee430 ts=2026-10-13T13:50:29.0200000Z; 67h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[14026] _id=6ad284aade269131f9e8013e ts=2026-10-16T20:10:15.3710000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14055] _id=6ad63d5bde269131f9e987b5 ts=2026-10-19T15:55:06.6650000Z; 23h 56m: 6ab9a9439a8420a1e6b56ba4.jsonl[199] _id=6ac6a0eede269131f9bf2fa7 ts=2026-10-07T19:43:42.0030000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[698] _id=6ac7f17fde269131f9c6b091 ts=2026-10-08T19:39:42.5640000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 22m 
  - Evidence: 120h 22m: 6ab9a9439a8420a1e6b56ba4.jsonl[862] _id=6ac7f288de269131f9c6c555 ts=2026-10-08T19:44:08.5500000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[3087] _id=6ace8f35de269131f9d24cea ts=2026-10-13T20:06:12.9860000Z; 23h 6m: 6ab9a9439a8420a1e6b56ba4.jsonl[6006] _id=6acfb5b8de269131f9d63c3a ts=2026-10-14T17:02:48.7140000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9146] _id=6ad0faaade269131f9dd4765 ts=2026-10-15T16:09:13.9630000Z; 20h 53m: 6ab9a9439a8420a1e6b56ba4.jsonl[3149] _id=6ace8fd4de269131f9d2524c ts=2026-10-13T20:08:51.8580000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[6002] _id=6acfb5b6de269131f9d63c0c ts=2026-10-14T17:02:46.7200000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.006s..0.008s shown 
  - Evidence: 6ms: 6ab9a9439a8420a1e6b56ba4.jsonl[855] _id=6ac7f281de269131f9c6c4ed ts=2026-10-08T19:44:01.5880000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[856] _id=6ac7f282de269131f9c6c4f0 ts=2026-10-08T19:44:01.5940000Z; 8ms: 6ab9a9439a8420a1e6b56ba4.jsonl[853] _id=6ac7f27ade269131f9c6c496 ts=2026-10-08T19:43:54.4480000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[849] _id=6ac7f27ade269131f9c6c498 ts=2026-10-08T19:43:54.4560000Z; 8ms: 6ab9a9439a8420a1e6b56ba4.jsonl[9147] _id=6ad0faabde269131f9dd477b ts=2026-10-15T16:09:15.0650000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9149] _id=6ad0faabde269131f9dd4781 ts=2026-10-15T16:09:15.0730000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 113h 40m 
  - Evidence: 113h 40m: 6ab9a9439a8420a1e6b56ba4.jsonl[1459] _id=6ac7f8cade269131f9c746f3 ts=2026-10-08T20:10:50.4320000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1477] _id=6ace3758de269131f9cee6c0 ts=2026-10-13T13:51:19.9260000Z; 67h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[14040] _id=6ad284d7de269131f9e802f9 ts=2026-10-16T20:11:02.9260000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14054] _id=6ad63d6cde269131f9e987e4 ts=2026-10-19T15:55:24.0170000Z; 23h 34m: 6ab9a9439a8420a1e6b56ba4.jsonl[142] _id=6ac55585de269131f9b84c92 ts=2026-10-06T20:09:41.5690000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[223] _id=6ac6a109de269131f9bf31f2 ts=2026-10-07T19:44:09.1250000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 765 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11629] _id=6ad18aa7de269131f9e2b6c5 ts=2026-10-16T02:23:34.6810000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11630] _id=6ad18aa7de269131f9e2b6c6 ts=2026-10-16T02:23:34.6810000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11659] _id=6ad18accde269131f9e2b783 ts=2026-10-16T02:24:11.6000000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11660] _id=6ad18accde269131f9e2b784 ts=2026-10-16T02:24:11.6000000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11701] _id=6ad18af2de269131f9e2b848 ts=2026-10-16T02:24:49.9730000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11702] _id=6ad18af2de269131f9e2b849 ts=2026-10-16T02:24:49.9730000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 140h 43m 
  - Evidence: 140h 43m: 6ab9a9439a8420a1e6b56ba4.jsonl[1317] _id=6ac7f747de269131f9c72a45 ts=2026-10-08T20:04:22.9230000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[5621] _id=6acfb246de269131f9d5d8b4 ts=2026-10-14T16:48:05.8390000Z; 26h 24m: 6ab9a9439a8420a1e6b56ba4.jsonl[5621] _id=6acfb246de269131f9d5d8b4 ts=2026-10-14T16:48:05.8390000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9347] _id=6ad1258cde269131f9e01b9a ts=2026-10-15T19:12:12.3440000Z; 8h 14m: 6ab9a9439a8420a1e6b56ba4.jsonl[9347] _id=6ad1258cde269131f9e01b9a ts=2026-10-15T19:12:12.3440000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[13092] _id=6ad1997bde269131f9e2f48b ts=2026-10-16T03:26:51.3740000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 113h 40m 
  - Evidence: 113h 40m: 6ab9a9439a8420a1e6b56ba4.jsonl[1454] _id=6ac7f8b8de269131f9c7461f ts=2026-10-08T20:10:32.4830000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1471] _id=6ace3744de269131f9cee5a3 ts=2026-10-13T13:51:00.1160000Z; 67h 43m: 6ab9a9439a8420a1e6b56ba4.jsonl[14030] _id=6ad284f7de269131f9e80413 ts=2026-10-16T20:11:35.1420000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14069] _id=6ad63d74de269131f9e98800 ts=2026-10-19T15:55:31.8450000Z; 23h 35m: 6ab9a9439a8420a1e6b56ba4.jsonl[179] _id=6ac55537de269131f9b8434b ts=2026-10-06T20:08:22.9910000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[201] _id=6ac6a0f1de269131f9bf2fe0 ts=2026-10-07T19:43:43.6920000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 236 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11245] _id=6ad187dade269131f9e2aa08 ts=2026-10-16T02:11:37.4100000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11246] _id=6ad187dade269131f9e2aa09 ts=2026-10-16T02:11:37.4100000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11246] _id=6ad187dade269131f9e2aa09 ts=2026-10-16T02:11:37.4100000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11247] _id=6ad187dade269131f9e2aa0a ts=2026-10-16T02:11:37.4100000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11291] _id=6ad18898de269131f9e2ac9b ts=2026-10-16T02:14:47.8010000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11292] _id=6ad18898de269131f9e2ac9c ts=2026-10-16T02:14:47.8010000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 113h 43m 
  - Evidence: 113h 43m: 6ab9a9439a8420a1e6b56ba4.jsonl[1432] _id=6ac7f881de269131f9c7431c ts=2026-10-08T20:09:37.5920000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1515] _id=6ace37bede269131f9ceec79 ts=2026-10-13T13:53:01.3990000Z; 67h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[14029] _id=6ad284f5de269131f9e80409 ts=2026-10-16T20:11:33.0220000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14075] _id=6ad63d8cde269131f9e9887b ts=2026-10-19T15:55:55.9450000Z; 23h 36m: 6ab9a9439a8420a1e6b56ba4.jsonl[181] _id=6ac55539de269131f9b8436f ts=2026-10-06T20:08:25.6390000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[249] _id=6ac6a141de269131f9bf376b ts=2026-10-07T19:45:05.2950000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11536] _id=6ad189cbde269131f9e2b41a ts=2026-10-16T02:19:54.9270000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11537] _id=6ad189cbde269131f9e2b41b ts=2026-10-16T02:19:54.9270000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12574] _id=6ad19437de269131f9e2d6e0 ts=2026-10-16T03:04:22.5250000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[12575] _id=6ad19437de269131f9e2d6e1 ts=2026-10-16T03:04:22.5250000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12604] _id=6ad19477de269131f9e2d8e9 ts=2026-10-16T03:05:26.9800000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[12605] _id=6ad19477de269131f9e2d8ea ts=2026-10-16T03:05:26.9800000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 113h 39m 
  - Evidence: 113h 39m: 6ab9a9439a8420a1e6b56ba4.jsonl[1460] _id=6ac7f8ccde269131f9c74701 ts=2026-10-08T20:10:51.8850000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1467] _id=6ace3737de269131f9cee53a ts=2026-10-13T13:50:43.8800000Z; 67h 43m: 6ab9a9439a8420a1e6b56ba4.jsonl[14041] _id=6ad28504de269131f9e80437 ts=2026-10-16T20:11:47.9410000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14062] _id=6ad63d66de269131f9e987d0 ts=2026-10-19T15:55:14.5340000Z; 23h 33m: 6ab9a9439a8420a1e6b56ba4.jsonl[195] _id=6ac55592de269131f9b84dd4 ts=2026-10-06T20:09:53.8110000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[200] _id=6ac6a0f1de269131f9bf2fdf ts=2026-10-07T19:43:42.0150000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 113h 43m 
  - Evidence: 113h 43m: 6ab9a9439a8420a1e6b56ba4.jsonl[1444] _id=6ac7f8cbde269131f9c746f5 ts=2026-10-08T20:10:50.3160000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1550] _id=6ace380cde269131f9cef031 ts=2026-10-13T13:54:18.4430000Z; 22h 57m: 6ab9a9439a8420a1e6b56ba4.jsonl[4563] _id=6ace9b41de269131f9d266bf ts=2026-10-13T20:57:36.2310000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[7510] _id=6acfde14de269131f9d930d9 ts=2026-10-14T19:54:59.2770000Z; 19h 51m: 6ab9a9439a8420a1e6b56ba4.jsonl[8220] _id=6acfdff9de269131f9d94d75 ts=2026-10-14T20:03:01.9510000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[8514] _id=6ad0f727de269131f9dceabf ts=2026-10-15T15:54:13.2260000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1581 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[10000] _id=6ad12bf3de269131f9e0a332 ts=2026-10-15T19:39:30.8590000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[10001] _id=6ad12bf3de269131f9e0a334 ts=2026-10-15T19:39:30.8590000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[10001] _id=6ad12bf3de269131f9e0a334 ts=2026-10-15T19:39:30.8590000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9998] _id=6ad12bf3de269131f9e0a33a ts=2026-10-15T19:39:30.8590000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[10003] _id=6ad12bf5de269131f9e0a383 ts=2026-10-15T19:39:31.6110000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[10004] _id=6ad12bf5de269131f9e0a389 ts=2026-10-15T19:39:31.6110000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 23h 42m 
  - Evidence: 23h 42m: 6ab9a9439a8420a1e6b56ba4.jsonl[7484] _id=6acfddebde269131f9d92eeb ts=2026-10-14T19:54:18.4570000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9455] _id=6ad12b48de269131f9e08d27 ts=2026-10-15T19:36:39.8810000Z; 23h 4m: 6ab9a9439a8420a1e6b56ba4.jsonl[3501] _id=6ace992cde269131f9d25d42 ts=2026-10-13T20:48:44.5860000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[7466] _id=6acfddc7de269131f9d92c8f ts=2026-10-14T19:53:42.8980000Z; 56m 2s: 6ab9a9439a8420a1e6b56ba4.jsonl[2752] _id=6ace8bbcde269131f9d22d5a ts=2026-10-13T19:51:24.0390000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[3474] _id=6ace98dede269131f9d25ce0 ts=2026-10-13T20:47:26.0660000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 20h 25m 
  - Evidence: 20h 25m: 6ab9a9439a8420a1e6b56ba4.jsonl[7009] _id=6acfdb4bde269131f9d9068c ts=2026-10-14T19:43:07.0120000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9120] _id=6ad0fa6cde269131f9dd412d ts=2026-10-15T16:08:11.6180000Z; 19h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[4773] _id=6ace9db4de269131f9d26ba5 ts=2026-10-13T21:08:03.8030000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[5692] _id=6acfb369de269131f9d5ff79 ts=2026-10-14T16:52:57.4910000Z; 6h 5m: 6ab9a9439a8420a1e6b56ba4.jsonl[10933] _id=6ad13207de269131f9e10b03 ts=2026-10-15T20:05:27.6400000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11237] _id=6ad187cade269131f9e2a9cf ts=2026-10-16T02:11:21.8380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.036s shown 
  - Evidence: 26ms: 6ab9a9439a8420a1e6b56ba4.jsonl[2895] _id=6ace8d52de269131f9d23c8d ts=2026-10-13T19:58:09.5440000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[2899] _id=6ace8d52de269131f9d23c91 ts=2026-10-13T19:58:09.5700000Z; 36ms: 6ab9a9439a8420a1e6b56ba4.jsonl[2909] _id=6ace8d52de269131f9d23c8b ts=2026-10-13T19:58:09.5080000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[2895] _id=6ace8d52de269131f9d23c8d ts=2026-10-13T19:58:09.5440000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 67h 44m 
  - Evidence: 67h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[14049] _id=6ad284eade269131f9e803cb ts=2026-10-16T20:11:22.5550000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14073] _id=6ad63d78de269131f9e9880a ts=2026-10-19T15:55:36.0570000Z; 4h 0m: 6ab9a9439a8420a1e6b56ba4.jsonl[14005] _id=6ad24c7fde269131f9e5a5ee ts=2026-10-16T16:10:39.3330000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14045] _id=6ad284dede269131f9e8032b ts=2026-10-16T20:11:10.0560000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 140h 38m 
  - Evidence: 140h 38m: 6ab9a9439a8420a1e6b56ba4.jsonl[1233] _id=6ac7f6a4de269131f9c71a91 ts=2026-10-08T20:01:39.6810000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[5475] _id=6acfb06fde269131f9d5ad91 ts=2026-10-14T16:40:15.6590000Z; 85h 1m: 6ab9a9439a8420a1e6b56ba4.jsonl[12702] _id=6ad19538de269131f9e2de2a ts=2026-10-16T03:08:40.0630000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14490] _id=6ad640c8de269131f9e9a329 ts=2026-10-19T16:09:43.4750000Z; 30h 33m: 6ab9a9439a8420a1e6b56ba4.jsonl[7199] _id=6acfdccdde269131f9d91939 ts=2026-10-14T19:49:32.6230000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11611] _id=6ad18a9bde269131f9e2b68a ts=2026-10-16T02:23:22.8570000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 140h 37m 
  - Evidence: 140h 37m: 6ab9a9439a8420a1e6b56ba4.jsonl[1227] _id=6ac7f6a4de269131f9c71a94 ts=2026-10-08T20:01:39.7090000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[5400] _id=6acfb011de269131f9d5a2a1 ts=2026-10-14T16:38:41.0610000Z; 84h 59m: 6ab9a9439a8420a1e6b56ba4.jsonl[12705] _id=6ad19538de269131f9e2de2f ts=2026-10-16T03:08:40.1060000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14464] _id=6ad64079de269131f9e9a0c0 ts=2026-10-19T16:08:25.2130000Z; 30h 33m: 6ab9a9439a8420a1e6b56ba4.jsonl[7200] _id=6acfdccdde269131f9d9193f ts=2026-10-14T19:49:32.6970000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11601] _id=6ad18a8cde269131f9e2b655 ts=2026-10-16T02:23:08.2660000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.026s..0.026s shown 
  - Evidence: 26ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12693] _id=6ad19538de269131f9e2de2c ts=2026-10-16T03:08:40.0800000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[12705] _id=6ad19538de269131f9e2de2f ts=2026-10-16T03:08:40.1060000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 140h 37m 
  - Evidence: 140h 37m: 6ab9a9439a8420a1e6b56ba4.jsonl[1230] _id=6ac7f6a2de269131f9c71a76 ts=2026-10-08T20:01:38.4220000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[5404] _id=6acfb014de269131f9d5a311 ts=2026-10-14T16:38:43.8050000Z; 84h 59m: 6ab9a9439a8420a1e6b56ba4.jsonl[12700] _id=6ad19534de269131f9e2de1c ts=2026-10-16T03:08:36.1180000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14469] _id=6ad64084de269131f9e9a0ec ts=2026-10-19T16:08:35.4640000Z; 30h 33m: 6ab9a9439a8420a1e6b56ba4.jsonl[7198] _id=6acfdcccde269131f9d91933 ts=2026-10-14T19:49:31.5940000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11599] _id=6ad18a88de269131f9e2b645 ts=2026-10-16T02:23:04.0270000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 67 interval(s) ≤ 0.007s..0.017s shown 
  - Evidence: 7ms: 6ab9a9439a8420a1e6b56ba4.jsonl[11837] _id=6ad18b9cde269131f9e2ba64 ts=2026-10-16T02:27:39.5580000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[11826] _id=6ad18b9cde269131f9e2ba68 ts=2026-10-16T02:27:39.5650000Z; 7ms: 6ab9a9439a8420a1e6b56ba4.jsonl[12296] _id=6ad1904fde269131f9e2c941 ts=2026-10-16T02:47:43.1350000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[12294] _id=6ad1904fde269131f9e2c943 ts=2026-10-16T02:47:43.1420000Z; 17ms: 6ab9a9439a8420a1e6b56ba4.jsonl[1150] _id=6ac7f64fde269131f9c70e94 ts=2026-10-08T20:00:14.9360000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1151] _id=6ac7f64fde269131f9c70e95 ts=2026-10-08T20:00:14.9530000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 140h 38m 
  - Evidence: 140h 38m: 6ab9a9439a8420a1e6b56ba4.jsonl[1156] _id=6ac7f649de269131f9c70d68 ts=2026-10-08T20:00:09.3710000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[5407] _id=6acfb017de269131f9d5a373 ts=2026-10-14T16:38:46.8730000Z; 116h 24m: 6ab9a9439a8420a1e6b56ba4.jsonl[7140] _id=6acfdc88de269131f9d91513 ts=2026-10-14T19:48:23.5230000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14706] _id=6ad64193de269131f9e9a7e7 ts=2026-10-19T16:13:06.3170000Z; 23h 52m: 6ab9a9439a8420a1e6b56ba4.jsonl[573] _id=6ac6a698de269131f9bf86e8 ts=2026-10-07T20:07:51.6700000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1152] _id=6ac7f647de269131f9c70d1b ts=2026-10-08T20:00:07.4680000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 141h 18m 
  - Evidence: 141h 18m: 6ab9a9439a8420a1e6b56ba4.jsonl[851] _id=6ac7f279de269131f9c6c485 ts=2026-10-08T19:43:53.3650000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[6003] _id=6acfb5b9de269131f9d63c5d ts=2026-10-14T17:02:48.9550000Z; 67h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[14025] _id=6ad284a7de269131f9e8010d ts=2026-10-16T20:10:15.1790000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14059] _id=6ad63d63de269131f9e987cd ts=2026-10-19T15:55:14.2960000Z; 34h 24m: 6ab9a9439a8420a1e6b56ba4.jsonl[6007] _id=6acfb5bbde269131f9d63cc9 ts=2026-10-14T17:02:51.6070000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[13100] _id=6ad19999de269131f9e2f591 ts=2026-10-16T03:27:21.0950000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 113h 44m 
  - Evidence: 113h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[1322] _id=6ac7f79dde269131f9c7312f ts=2026-10-08T20:05:49.0040000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1465] _id=6ace3726de269131f9cee432 ts=2026-10-13T13:50:29.1680000Z; 67h 45m: 6ab9a9439a8420a1e6b56ba4.jsonl[14019] _id=6ad2849ade269131f9e80085 ts=2026-10-16T20:10:01.7900000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14057] _id=6ad63d5bde269131f9e987b7 ts=2026-10-19T15:55:06.7970000Z; 23h 56m: 6ab9a9439a8420a1e6b56ba4.jsonl[197] _id=6ac6a0e6de269131f9bf2edc ts=2026-10-07T19:43:33.5560000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[700] _id=6ac7f17fde269131f9c6b093 ts=2026-10-08T19:39:42.7130000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 113h 44m 
  - Evidence: 113h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[1321] _id=6ac7f79dde269131f9c7312e ts=2026-10-08T20:05:49.0030000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1464] _id=6ace3726de269131f9cee431 ts=2026-10-13T13:50:29.1680000Z; 67h 43m: 6ab9a9439a8420a1e6b56ba4.jsonl[14052] _id=6ad28508de269131f9e80447 ts=2026-10-16T20:11:51.8610000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14056] _id=6ad63d5bde269131f9e987b6 ts=2026-10-19T15:55:06.7970000Z; 23h 54m: 6ab9a9439a8420a1e6b56ba4.jsonl[241] _id=6ac6a132de269131f9bf35b6 ts=2026-10-07T19:44:49.9980000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[699] _id=6ac7f17fde269131f9c6b092 ts=2026-10-08T19:39:42.7130000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 113h 46m 
  - Evidence: 113h 46m: 6ab9a9439a8420a1e6b56ba4.jsonl[1462] _id=6ace3725de269131f9cee42e ts=2026-10-08T20:10:59.605Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1646] _id=6ace896cde269131f9d2118f ts=2026-10-13T13:57:54.541Z; 24h 0m: 6ab9a9439a8420a1e6b56ba4.jsonl[697] _id=6ac7f17ede269131f9c6b08d ts=2026-10-07T20:10:34.459Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1462] _id=6ace3725de269131f9cee42e ts=2026-10-08T20:10:59.605Z; 20h 3m: 6ab9a9439a8420a1e6b56ba4.jsonl[8001] _id=6acfdf88de269131f9d945e9 ts=2026-10-14T20:00:54.742Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[9007] _id=6ad0f99dde269131f9dd28b5 ts=2026-10-15T16:04:45.0550000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[14053] _id=6ad28507de269131f9e80441 ts=2026-10-16T20:11:51.2560000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14060] _id=6ad63d5bde269131f9e987b3 ts=2026-10-16T20:11:51.256Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[3184] _id=6ace904ade269131f9d2543a ts=2026-10-13T20:10:49.6300000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[3185] _id=6ace925ede269131f9d254b8 ts=2026-10-13T20:10:49.63Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[7957] _id=6acfdf77de269131f9d944fc ts=2026-10-14T20:00:54.7420000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[8001] _id=6acfdf88de269131f9d945e9 ts=2026-10-14T20:00:54.742Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 113h 42m 
  - Evidence: 113h 42m: 6ab9a9439a8420a1e6b56ba4.jsonl[1377] _id=6ac7f818de269131f9c73bf3 ts=2026-10-08T20:07:51.8580000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1468] _id=6ace3737de269131f9cee53b ts=2026-10-13T13:50:46.1090000Z; 67h 44m: 6ab9a9439a8420a1e6b56ba4.jsonl[14028] _id=6ad284aade269131f9e80140 ts=2026-10-16T20:10:17.8040000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14063] _id=6ad63d66de269131f9e987d1 ts=2026-10-19T15:55:16.8460000Z; 23h 36m: 6ab9a9439a8420a1e6b56ba4.jsonl[157] _id=6ac554fede269131f9b83b95 ts=2026-10-06T20:07:25.8310000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[207] _id=6ac6a0f1de269131f9bf2fe2 ts=2026-10-07T19:43:44.2060000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[1122] _id=6ac7f5fcde269131f9c70370 ts=2026-10-08T19:58:52.1050000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[1123] _id=6ac7f5fcde269131f9c70371 ts=2026-10-08T19:58:52.1050000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[14197] _id=6ad63e29de269131f9e98c8a ts=2026-10-19T15:58:32.2410000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14198] _id=6ad63e29de269131f9e98c8b ts=2026-10-19T15:58:32.2410000Z; 0ms: 6ab9a9439a8420a1e6b56ba4.jsonl[14776] _id=6ad64213de269131f9e9a9d8 ts=2026-10-19T16:15:14.7870000Z -> 6ab9a9439a8420a1e6b56ba4.jsonl[14777] _id=6ad64213de269131f9e9a9d9 ts=2026-10-19T16:15:14.7870000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[501] _id=6ac6a56bde269131f9bf701d ts=2026-10-07T20:02:51.5780000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1103] _id=6ac7f5d9de269131f9c70143 ts=2026-10-08T19:58:17.5390000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1190] _id=6ac7f6b6de269131f9c71c74 ts=2026-10-08T20:01:57.9820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[7200] _id=6acfdccdde269131f9d9193f ts=2026-10-14T19:49:32.6970000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[13100] _id=6ad19999de269131f9e2f591 ts=2026-10-16T03:27:21.0950000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[13163] _id=6ad22a6ede269131f9e3edd1 ts=2026-10-16T13:45:17.3500000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[13218] _id=6ad24883de269131f9e565ad ts=2026-10-16T15:53:38.8750000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[918] _id=6ac7f2f7de269131f9c6cc35 ts=2026-10-08T19:45:59.2080000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[14196] _id=6ad63e29de269131f9e98c89 ts=2026-10-19T15:58:32.2210000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[12513] _id=6ad193dede269131f9e2d564 ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 12 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[775] _id=6ac7f212de269131f9c6be0d ts=2026-10-08T19:42:10.2500000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[844] _id=6ac7f268de269131f9c6c37d ts=2026-10-08T19:43:36.0730000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[848] _id=6ac7f276de269131f9c6c457 ts=2026-10-08T19:43:49.7320000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 130 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[3693] _id=6ace9a12de269131f9d25f80 ts=2026-10-13T20:52:32.5150000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[3694] _id=6ace9a12de269131f9d25f88 ts=2026-10-13T20:52:32.6870000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[3696] _id=6ace9a13de269131f9d25f91 ts=2026-10-13T20:52:32.7050000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 127 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[1552] _id=6ace380dde269131f9cef046 ts=2026-10-13T13:54:18.8100000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1558] _id=6ace380dde269131f9cef04b ts=2026-10-13T13:54:18.8100000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1569] _id=6ace381bde269131f9cef11a ts=2026-10-13T13:54:34.9990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[12652] _id=6ad194f2de269131f9e2dc83 ts=2026-10-16T03:07:30.1760000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[7106] _id=6acfdc57de269131f9d912bc ts=2026-10-14T19:47:35.1450000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[7140] _id=6acfdc88de269131f9d91513 ts=2026-10-14T19:48:23.5230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Open' (totals: 17 open, 15 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 516 start, 505 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'BecameCameraCentered' (totals: 703 open, 699 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 13 unmatched 'BecameVisible' (totals: 882 open, 869 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 10 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 59 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 410 of 14821 adjacent _id pairs reverse in client time; worst 78.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba4.jsonl[1779] _id=6ace8aabde269131f9d21c44 ts=2026-10-13T19:46:50.8120000Z`; `6ab9a9439a8420a1e6b56ba4.jsonl[1780] _id=6ace8aacde269131f9d21c4a ts=2026-10-13T19:45:32.6920000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.64s, min -409170.34s, max -0.17s over 14822 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba4\coverage.yaml

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

### `InputEvent` — 4513 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1238); Unit 2 Prod (Refactor) (873); Unit 4 Dev - Dungeon (556); Unit 3 Dungeon Dev (554); Unit 5 Dev - Dungeon (459); Unit 1 Dev (322); Unit 4 Dev - Anderson Base (238); Unit 4 Dev (219); Unit 5 Dev (54)
- **Intervals:** median 0.77s (p5 0.05s / p95 17.44s, n=4512)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4513/4513 records)
    "pressed"  x4513
data.actionType  (string, 4513/4513 records)
    "Move"  x3575
    "Interact"  x561
    "Jump"  x140
    "Ascend"  x69
    "Sprint"  x42
    "Descend"  x38
    "Pause"  x35
    "Hoverboard"  x34
    "Map"  x18
    "SkipCinematic"  x1
data.key  (string, 4513/4513 records, 21 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4513/4513 records)
    "Player"  x3144
    "Drone"  x1369
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3153 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1719); Unit 4 Dev (530); Unit 3 Dungeon Dev (526); Unit 5 Dev - Dungeon (378)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.68s, n=3152)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3153/3153 records)
    "BecameVisible"  x882
    "BecameInvisible"  x869
    "BecameCameraCentered"  x703
    "BecameCameraUncentered"  x699
data.pieceId  (string, 3153/3153 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3153/3153 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2641 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (710); Unit 3 Dev (412); Unit 1 Dev (378); Unit 4 Dev - Anderson Base (281); Unit 4 Dev (267); Unit 3 Dungeon Dev (249); Unit 5 Dev (126); Unit 4 Dev - Dungeon (109); Unit 5 Dev - Dungeon (109)
- **eventKey:** present on 1620 of 2641 records
- **Intervals:** median 4.21s (p5 0.00s / p95 33.16s, n=2640)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1620; [conversationId, dialogueEventType] x1021
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2641/2641 records)
    numeric range 8 .. 117 (54 unique)
data.dialogueEventType  (string, 2641/2641 records)
    "DialogueNodeEvent"  x1620
    "DialogueStartEvent"  x516
    "DialogueFinishEvent"  x505
data.nodeId  (number, 1620/2641 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2551 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (720); Unit 1 Dev (356); Unit 3 Dev (326); Unit 4 Dev - Anderson Base (309); Unit 4 Dev (240); Unit 3 Dungeon Dev (176); Unit 4 Dev - Dungeon (172); Unit 5 Dev - Dungeon (166); Unit 5 Dev (86)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.13s, n=2539)
- **Fields under `data`:**

```text
data.position  (object, 2551/2551 records)
data.position.x  (number, 2551/2551 records)
    numeric range -787.159 .. 1557.07 (792 unique)
data.position.y  (number, 2551/2551 records)
    numeric range -115.127 .. 222.252 (533 unique)
data.position.z  (number, 2551/2551 records)
    numeric range -1036.12 .. 2175.72 (794 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 863 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (515); Unit 5 Dev (122); Unit 1 Dev (104); Unit 3 Dev (63); Unit 2 Prod (Refactor) (59)
- **Intervals:** median 0.51s (p5 0.04s / p95 15.55s, n=862)
- **Fields under `data`:**

```text
data.actionType  (string, 863/863 records)
    "argumentationNodeHoverEnd"  x345
    "argumentationNodeHoverStart"  x345
    "argumentationNodeAdd"  x101
    "argumentationNodeRemove"  x72
data.argumentationTitle  (string, 863/863 records)
    "Unit 4 - Flooding"  x515
    "Unit 5"  x122
    "Unit 1 - Freshwater"  x64
    "Unit 3 - Pollution Upstream"  x63
    "Unit 2 – Watershed"  x59
    "Unit 1 - Argumentation Tutorial"  x40
data.nodeName  (string, 863/863 records)
    "B"  x154
    "A"  x131
    "C"  x124
    "D"  x102
    "II"  x88
    "I"  x69
    "2"  x54
    "4"  x54
    "1"  x43
    "3"  x37
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 367 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (80); Unit 2 Prod (Refactor) (76); Unit 1 Dev (65); Unit 3 Dungeon Dev (55); Unit 4 Dev (30); Unit 5 Dev - Dungeon (24); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (14); Unit 5 Dev (5)
- **Intervals:** median 8.89s (p5 0.18s / p95 482.71s, n=366)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 367/367 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 367/367 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationAnswerEvent` — 156 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (94); Unit 4 Dev - Anderson Base (51); Unit 3 Dev (5); Unit 1 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.03s (p5 0.16s / p95 206.63s, n=155)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 156/156 records)
    "submitAnswerEvent"  x156
data.answerSubmitted  (string, 156/156 records)
    39 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 156/156 records)
    "Unit 5"  x94
    "Unit 4 - Flooding"  x51
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 124 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (68); Unit 3 Dev (50); Unit 4 Dev (4); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 6.24s (p5 0.75s / p95 1812.35s, n=123)
- **`data` key-set variants:** [actionType, featureUsed] x88; [actionType, featureUsed, location] x34; [actionType, featureUsed, legendName] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 124/124 records)
    "MapCloseEvent"  x44
    "MapOpenEvent"  x44
    "WaypointMoveEvent"  x29
    "WaypointSetEvent"  x5
    "Selected"  x2
data.featureUsed  (string, 124/124 records)
    "Map"  x88
    "Waypoint"  x34
    "Legend"  x2
data.legendName  (string, 2/124 records)
    "0 ft"  x1
    "90 ft"  x1
data.location  (object, 34/124 records)
data.location.x  (number, 34/124 records)
    numeric range -441.725 .. -1.67646 (26 unique)
data.location.y  (number, 34/124 records)
    numeric range -132.585 .. 301.84 (30 unique)
data.location.z  (number, 34/124 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 98 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 2 Prod (Refactor) (17); Unit 5 Dev - Dungeon (15); Unit 3 Dev (13); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (4); Unit 5 Dev (4); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 98 of 98 records
- **Intervals:** median 206.32s (p5 0.01s / p95 68730.66s, n=97)
- **`data` key-set variants:** [questEventType, questID, questName] x59; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 98/98 records)
    "questActiveEvent"  x59
    "questFinishEvent"  x39
data.questID  (string, 98/98 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 98/98 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/98 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 55 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (25); Unit 2 Prod (Refactor) (6); Unit 1 Dev (5); Unit 5 Dev - Dungeon (5); Unit 3 Dev (4); Unit 4 Dev (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 400.28s (p5 7.84s / p95 85655.78s, n=54)
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "DebugMenuStateChanged"  x55
data.isOpened  (bool, 55/55 records)
    false  x55
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `Soil Key Puzzle` — 52 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 3 Dev (14); Unit 4 Dev (12)
- **Intervals:** median 1.51s (p5 0.19s / p95 1693.16s, n=51)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/52 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/52 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 44/52 records)
    "RightDrag"  x25
    "LeftDrag"  x19
data.currentSoilType  (string, 44/52 records)
    "CLAY"  x10
    "CLAYSAND"  x9
    "SAND"  x8
    "CLAYROCK"  x7
    "SANDGRAVEL"  x6
    "GRAVEL"  x3
    "BEDROCK"  x1
data.isCorrectSelection  (string, 44/52 records)
    "false"  x33
    "true"  x11
data.waterLevelStatus  (string, 44/52 records)
    "TooHigh"  x19
    "Proper"  x14
    "TooLow"  x11
data.waterRetentionChange  (string, 44/52 records)
    "Increase"  x19
    "Decrease"  x14
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 52 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (52)
- **Intervals:** median 12.50s (p5 1.92s / p95 96.81s, n=51)
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "On"  x36
    "Off"  x16
data.floor  (string, 52/52 records)
    "4"  x22
    "3"  x21
    "1"  x5
    "2"  x4
data.machineNumber  (string, 52/52 records)
    "One"  x50
    "Two"  x2
data.machineType  (string, 52/52 records)
    "Condenser"  x26
    "Evaporator"  x14
    "VentSwitch"  x5
    "DualChamber_Evaporator"  x4
    "DualChamber_Condenser"  x3
data.room  (string, 52/52 records)
    "3"  x20
    "2"  x16
    "1"  x10
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 35 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (26); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1941.81s (p5 81.00s / p95 141288.49s, n=34)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 35/35 records)
    true  x35
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 32 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (16); Unit 3 Dev (10); Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.26s (p5 0.01s / p95 79210.06s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "Open"  x17
    "Close"  x15
data.toolName  (string, 32/32 records, 28 empty-string)
    ""  x28
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 25 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (25)
- **Intervals:** median 8638.06s (p5 162.40s / p95 220244.63s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 21 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (3); Unit 3 Dungeon Dev (3); Unit 5 Dev - Dungeon (3); Unit 1 Dev (2); MainMenu (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2539.76s (p5 0.00s / p95 102584.64s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    false  x21
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 19 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 91.43s (p5 0.05s / p95 336020.54s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x9
data.argumentationDescription  (string, 19/19 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 19/19 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 4.20s (p5 0.84s / p95 216.53s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Bedrock"  x6
    "Clay"  x5
    "Sand"  x5
    "Gravel"  x3
data.floor  (string, 19/19 records)
    "4"  x9
    "5"  x9
    "3"  x1
data.machine  (string, 19/19 records)
    "1"  x15
    "2"  x4
data.row  (string, 19/19 records)
    "TopRow"  x18
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 18 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (18)
- **Intervals:** median 2.06s (p5 0.71s / p95 24.52s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records, 8 empty-string)
    "cameraPlaced"  x10
    ""  x8
data.boxId  (string, 18/18 records)
    "0"  x7
    "2"  x6
    "1"  x5
data.soilType  (string, 18/18 records)
    "Gravel"  x9
    "Sand"  x7
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 3 Dev (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (1)
- **Intervals:** median 48.38s (p5 1.71s / p95 462700.15s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x10
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x4
    "Unit 2 – Watershed"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 5"  x1
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 12 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (5); Unit 1 Dev (4); Unit 3 Dev (2); Unit 5 Dev (1)
- **Intervals:** median 7701.52s (p5 1.82s / p95 376317.35s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x9
    "Open"  x3
data.chatID  (string, 12/12 records)
    "NA"  x9
    "[]"  x2
    "[11-31, 11-25, 11-230, 11-230, 11-26]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 95046.51s (p5 36215.78s / p95 465465.27s, n=3)
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
    "Permissions check failed"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "TypeError: Permissions check failed"  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
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
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (26 records)
- `TerasGardenBox` data.actionType: "" (8x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (29x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (34x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (72x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*