# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b24

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b24
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b24.jsonl
- **Records:** 9601 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b24
- **Time span:** 2026-10-05T16:32:29.890000+00:00 .. 2026-10-16T17:10:04.431000+00:00 (264h 37m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b24\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 9601 records, 11 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 94 INFO, 0 NOT_TESTED, 102 PASS.
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
| PuzzlePieceVisibleEvent | 3147 | 32.78 | 1 | 4 | 0 | 2026-10-06T16:56:47.601000+00:00 | 2026-10-16T16:37:01.293000+00:00 | 239h 40m |
| DialogueEvent | 1984 | 20.66 | 1 | 9 | 1245 | 2026-10-05T16:33:03.602000+00:00 | 2026-10-16T17:09:53.908000+00:00 | 264h 36m |
| InputEvent | 1801 | 18.76 | 1 | 9 | 0 | 2026-10-05T16:37:52.312000+00:00 | 2026-10-16T17:10:04.431000+00:00 | 264h 32m |
| PlayerPositionEvent | 1717 | 17.88 | 1 | 9 | 0 | 2026-10-05T16:32:43.684000+00:00 | 2026-10-16T17:10:02.624000+00:00 | 264h 37m |
| argumentationNodeEvent | 312 | 3.25 | 1 | 5 | 0 | 2026-10-05T16:56:10.421000+00:00 | 2026-10-16T16:55:44.970000+00:00 | 263h 59m |
| ObjectInterEvent | 268 | 2.79 | 1 | 9 | 0 | 2026-10-05T16:39:01.258000+00:00 | 2026-10-16T17:10:04.431000+00:00 | 264h 31m |
| questEvent | 75 | 0.78 | 1 | 9 | 75 | 2026-10-05T16:33:03.578000+00:00 | 2026-10-16T17:04:52.592000+00:00 | 264h 31m |
| TopographicMapEvent | 65 | 0.68 | 1 | 3 | 0 | 2026-10-06T16:57:15.375000+00:00 | 2026-10-16T16:22:53.724000+00:00 | 239h 25m |
| Soil Key Puzzle | 38 | 0.4 | 1 | 3 | 0 | 2026-10-07T16:57:14.409000+00:00 | 2026-10-14T16:57:44.859000+00:00 | 168h 0m |
| DEBUGMenu | 28 | 0.29 | 1 | 9 | 0 | 2026-10-05T16:32:43.666000+00:00 | 2026-10-16T16:26:36.930000+00:00 | 263h 53m |
| WaterChamberEvent | 21 | 0.22 | 1 | 1 | 0 | 2026-10-16T16:35:20.698000+00:00 | 2026-10-16T16:46:06.137000+00:00 | 10m 45s |
| gameWindowFocusEvent | 20 | 0.21 | 1 | 3 | 0 | 2026-10-05T16:32:29.890000+00:00 | 2026-10-16T17:00:30.941000+00:00 | 264h 28m |
| argumentationAnswerEvent | 18 | 0.19 | 1 | 5 | 0 | 2026-10-05T16:57:08.724000+00:00 | 2026-10-16T16:55:46.621000+00:00 | 263h 58m |
| argumentationEvent | 16 | 0.17 | 1 | 5 | 0 | 2026-10-05T16:56:51.191000+00:00 | 2026-10-16T16:55:46.658000+00:00 | 263h 58m |
| soilMachine | 16 | 0.17 | 1 | 1 | 0 | 2026-10-15T16:27:54.288000+00:00 | 2026-10-15T16:35:29.218000+00:00 | 7m 34s |
| SolarStillDesignEvent | 14 | 0.15 | 1 | 1 | 0 | 2026-10-16T17:01:47.545000+00:00 | 2026-10-16T17:02:14.454000+00:00 | 26.9s |
| argumentationToolEvent | 14 | 0.15 | 1 | 4 | 0 | 2026-10-05T16:56:38.543000+00:00 | 2026-10-16T16:54:49.970000+00:00 | 263h 58m |
| gameStartEvent | 13 | 0.14 | 1 | 1 | 0 | 2026-10-05T16:32:29.891000+00:00 | 2026-10-16T16:25:59.208000+00:00 | 263h 53m |
| gameWindowUnfocusEvent | 13 | 0.14 | 1 | 5 | 0 | 2026-10-05T17:04:00.381000+00:00 | 2026-10-16T17:00:27.356000+00:00 | 263h 56m |
| DaniEvent | 6 | 0.06 | 1 | 2 | 0 | 2026-10-13T16:43:51.329000+00:00 | 2026-10-16T16:22:31.352000+00:00 | 71h 38m |
| TerasGardenBox | 6 | 0.06 | 1 | 1 | 0 | 2026-10-15T16:57:56.216000+00:00 | 2026-10-15T16:58:58.513000+00:00 | 1m 2s |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-05T17:02:15.072000+00:00 | 2026-10-16T17:10:04.408000+00:00 | 264h 7m |
| chatEvent | 4 | 0.04 | 1 | 3 | 0 | 2026-10-16T16:22:26.256000+00:00 | 2026-10-16T16:47:13.664000+00:00 | 24m 47s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87565.368s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 2.265s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.588s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.075s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.443s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.207s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 31.053s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 247.908s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84966.785s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1666.063s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 43470.2s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.726s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 14 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,C,1,II; A,C,2,II; C,3,II; C,4,II; C,D,3,II; C,D,4,3,II; C,D,4,II; D,2,II; D,4,II 
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
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [] 
  - Expected: new design, renamed value, or new coverage — review
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

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[129] _id=6ac3d33bde269131f9adf0cb ts=2026-10-05T16:41:31.5820000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[177] _id=6ac3d418de269131f9ae0177 ts=2026-10-05T16:45:12.6350000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[214] _id=6ac3d4afde269131f9ae1495 ts=2026-10-05T16:47:43.6900000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[4] _id=6ac3d11ede269131f9adc642 ts=2026-10-05T16:32:29.8910000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[514] _id=6ac3d873de269131f9ae6faa ts=2026-10-05T17:03:47.4670000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[517] _id=6ac52755de269131f9b578a3 ts=2026-10-06T16:52:36.3530000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[3] _id=6ac3d11ede269131f9adc63d ts=2026-10-05T16:32:29.8900000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[513] _id=6ac3d873de269131f9ae6fa3 ts=2026-10-05T17:03:47.4660000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[516] _id=6ac52755de269131f9b5789d ts=2026-10-06T16:52:36.3520000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[515] _id=6ac3d880de269131f9ae70af ts=2026-10-05T17:04:00.3810000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[1738] _id=6ac67417de269131f9bc8bbb ts=2026-10-06T17:05:08.786Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[3143] _id=6ac67b76de269131f9bd8dcd ts=2026-10-07T17:03:49.6120000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3146 | 0.0 | 0.075 | 274.257 | 2.377 | 433462.684 | 0.22 | 1318 | 8 |
| DialogueEvent | 1983 | 0.0 | 3.831 | 480.388 | 30.257 | 429405.649 | 0.12 | 554 | 7 |
| InputEvent | 1800 | 0.0 | 2.265 | 529.073 | 36.118 | 429672.803 | 0.11 | 33 | 9 |
| PlayerPositionEvent | 1705 | 0.0 | 10.003 | 508.263 | 10.18 | 429399.701 | 0.12 | 1 | 6 |
| argumentationNodeEvent | 311 | 0.002 | 0.899 | 3055.867 | 12.386 | 429457.622 | 0.02 | 26 | 5 |
| ObjectInterEvent | 267 | 0.0 | 12.588 | 3566.529 | 459.364 | 430597.449 | 0.02 | 3 | 11 |
| questEvent | 74 | 0.0 | 205.038 | 12869.041 | 84280.231 | 429410.569 | 0.0 | 14 | 13 |
| TopographicMapEvent | 64 | 0.021 | 8.207 | 13467.787 | 85139.14 | 431176.704 | 0.0 | 2 | 6 |
| Soil Key Puzzle | 37 | 0.114 | 2.443 | 16346.769 | 17266.31 | 518447.669 | 0.0 | 0 | 2 |
| DEBUGMenu | 27 | 9.469 | 494.909 | 35186.417 | 87176.012 | 431512.225 | 0.0 | 0 | 12 |
| WaterChamberEvent | 20 | 3.471 | 19.778 | 32.272 | 93.745 | 98.577 | 1.86 | 0 | 0 |
| gameWindowFocusEvent | 19 | 0.0 | 1666.063 | 50109.529 | 120723.116 | 431539.016 | 0.0 | 1 | 11 |
| argumentationAnswerEvent | 17 | 0.887 | 31.053 | 55901.053 | 293498.876 | 429491.292 | 0.0 | 0 | 5 |
| argumentationEvent | 15 | 0.055 | 126.427 | 63355.698 | 310380.845 | 429429.27 | 0.0 | 0 | 5 |
| soilMachine | 15 | 0.605 | 6.726 | 30.329 | 135.047 | 194.06 | 1.98 | 0 | 0 |
| SolarStillDesignEvent | 13 | 0.819 | 1.645 | 2.07 | 4.25 | 4.598 | 28.99 | 0 | 0 |
| argumentationToolEvent | 13 | 2.181 | 17.8 | 73099.341 | 327415.985 | 429481.171 | 0.0 | 0 | 4 |
| gameStartEvent | 12 | 137.763 | 84966.785 | 79167.443 | 241672.473 | 431539.016 | 0.0 | 0 | 9 |
| gameWindowUnfocusEvent | 12 | 0.0 | 43470.2 | 79182.248 | 280454.949 | 517549.614 | 0.0 | 1 | 8 |
| DaniEvent | 5 | 2.577 | 3.636 | 51584.005 | 206313.691 | 257885.769 | 0.0 | 0 | 1 |
| TerasGardenBox | 5 | 1.229 | 3.216 | 12.459 | 31.363 | 34.049 | 4.82 | 0 | 0 |
| EndOfUnit | 4 | 86624.923 | 87565.368 | 237717.334 | 598890.577 | 689113.676 | 0.0 | 0 | 4 |
| chatEvent | 3 | 2.51 | 247.908 | 495.803 | 1138.082 | 1236.99 | 0.12 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[6271] _id=6acfb1dcde269131f9d5cd31 ts=2026-10-14T16:46:19.1240000Z == 6ab9a8e69a8420a1e6b56b24.jsonl[6272] _id=6acfb1dcde269131f9d5cd32 ts=2026-10-14T16:46:19.1240000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 62 group(s), 87 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[743] _id=6ac528c2de269131f9b5caf1 ts=2026-10-06T16:58:37.1210000Z == 6ab9a8e69a8420a1e6b56b24.jsonl[746] _id=6ac528c2de269131f9b5caf9 ts=2026-10-06T16:58:37.1210000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[758] _id=6ac528c3de269131f9b5cb41 ts=2026-10-06T16:58:38.3440000Z == 6ab9a8e69a8420a1e6b56b24.jsonl[759] _id=6ac528c3de269131f9b5cb4b ts=2026-10-06T16:58:38.3440000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[756] _id=6ac528c4de269131f9b5cb70 ts=2026-10-06T16:58:41.0930000Z == 6ab9a8e69a8420a1e6b56b24.jsonl[761] _id=6ac528c4de269131f9b5cb7d ts=2026-10-06T16:58:41.0930000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[9321] _id=6ad25759de269131f9e64534 ts=2026-10-16T16:56:57.3870000Z == 6ab9a8e69a8420a1e6b56b24.jsonl[9325] _id=6ad25759de269131f9e64535 ts=2026-10-16T16:56:57.3870000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6ab9a8e69a8420a1e6b56b24.jsonl[90] _id=6ac3d2a5de269131f9ade5e7 ts=2026-10-05T16:39:01.2580000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[93] _id=6ac3d2a5de269131f9ade5ec ts=2026-10-05T16:39:01.2670000Z`; `698ms: 6ab9a8e69a8420a1e6b56b24.jsonl[9451] _id=6ad258b2de269131f9e65a7c ts=2026-10-16T17:02:42.6880000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[9466] _id=6ad258b3de269131f9e65a8a ts=2026-10-16T17:02:43.3860000Z`; `135ms: 6ab9a8e69a8420a1e6b56b24.jsonl[9466] _id=6ad258b3de269131f9e65a8a ts=2026-10-16T17:02:43.3860000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[9467] _id=6ad258b3de269131f9e65a92 ts=2026-10-16T17:02:43.5210000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 139 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `173ms: 6ab9a8e69a8420a1e6b56b24.jsonl[718] _id=6ac528bede269131f9b5ca07 ts=2026-10-06T16:58:25.1950000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[726] _id=6ac528bfde269131f9b5ca13 ts=2026-10-06T16:58:25.3680000Z`; `412ms: 6ab9a8e69a8420a1e6b56b24.jsonl[726] _id=6ac528bfde269131f9b5ca13 ts=2026-10-06T16:58:25.3680000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[727] _id=6ac528bfde269131f9b5ca1d ts=2026-10-06T16:58:25.7800000Z`; `150ms: 6ab9a8e69a8420a1e6b56b24.jsonl[727] _id=6ac528bfde269131f9b5ca1d ts=2026-10-06T16:58:25.7800000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[634] _id=6ac528bfde269131f9b5ca37 ts=2026-10-06T16:58:25.9300000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `887ms: 6ab9a8e69a8420a1e6b56b24.jsonl[9268] _id=6ad25706de269131f9e63ec5 ts=2026-10-16T16:55:34.4490000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[9269] _id=6ad25707de269131f9e63ed9 ts=2026-10-16T16:55:35.3360000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `55ms: 6ab9a8e69a8420a1e6b56b24.jsonl[5122] _id=6ace61ebde269131f9cfd3e6 ts=2026-10-13T16:52:58.0410000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[5125] _id=6ace61ebde269131f9cfd3e9 ts=2026-10-13T16:52:58.0960000Z`; `59ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8000] _id=6ad10515de269131f9de03fb ts=2026-10-15T16:53:40.2710000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[8003] _id=6ad10515de269131f9de03ff ts=2026-10-15T16:53:40.3300000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `471ms: 6ab9a8e69a8420a1e6b56b24.jsonl[4258] _id=6ac7cc8ade269131f9c4d8fe ts=2026-10-08T17:02:02.1760000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[4257] _id=6ac7cc8ade269131f9c4d908 ts=2026-10-08T17:02:02.6470000Z`; `713ms: 6ab9a8e69a8420a1e6b56b24.jsonl[5094] _id=6ace61bdde269131f9cfd122 ts=2026-10-13T16:52:13.0450000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[5095] _id=6ace61bede269131f9cfd12a ts=2026-10-13T16:52:13.7580000Z`; `507ms: 6ab9a8e69a8420a1e6b56b24.jsonl[5112] _id=6ace61e0de269131f9cfd330 ts=2026-10-13T16:52:47.4790000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[5106] _id=6ace61e0de269131f9cfd333 ts=2026-10-13T16:52:47.9860000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8434] _id=6ad24ff4de269131f9e5ceb0 ts=2026-10-16T16:25:24.3780000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[8439] _id=6ad25017de269131f9e5d0ee ts=2026-10-16T16:25:24.378Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8315] _id=6ad24e2cde269131f9e5aced ts=2026-10-16T16:17:47.7450000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[8316] _id=6ad24e9bde269131f9e5b677 ts=2026-10-16T16:17:47.745Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b24.jsonl[9549] _id=6ad258f3de269131f9e65e91 ts=2026-10-16T17:03:47.7440000Z ~ 6ab9a8e69a8420a1e6b56b24.jsonl[9555] _id=6ad258f4de269131f9e65ea1 ts=2026-10-16T17:03:47.7480000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6ab9a8e69a8420a1e6b56b24.jsonl[3165] _id=6ac7c4ddde269131f9c42934 ts=2026-10-08T16:29:16.9130000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4346] _id=6ace5a75de269131f9cf5cb6 ts=2026-10-13T16:21:09.1380000Z; 24h 20m: 6ab9a8e69a8420a1e6b56b24.jsonl[8] _id=6ac3d12bde269131f9adc8d7 ts=2026-10-05T16:32:43.6660000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[518] _id=6ac52761de269131f9b57a72 ts=2026-10-06T16:52:48.0010000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b24.jsonl[1742] _id=6ac67422de269131f9bc8c87 ts=2026-10-07T16:32:33.7180000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3160] _id=6ac7c4c2de269131f9c42786 ts=2026-10-08T16:28:50.3110000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 71h 38m 
  - Evidence: 71h 38m: 6ab9a8e69a8420a1e6b56b24.jsonl[4770] _id=6ace5fcbde269131f9cfaee4 ts=2026-10-13T16:43:54.9650000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8362] _id=6ad24f28de269131f9e5c16f ts=2026-10-16T16:22:00.7340000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b24.jsonl[4341] _id=6ac7cd2dde269131f9c4e03f ts=2026-10-08T17:04:44.7410000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4352] _id=6ace5a8bde269131f9cf5d9a ts=2026-10-13T16:21:30.3900000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b24.jsonl[511] _id=6ac3d814de269131f9ae6869 ts=2026-10-05T17:02:12.6990000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[521] _id=6ac52765de269131f9b57b27 ts=2026-10-06T16:52:52.1680000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b24.jsonl[1731] _id=6ac52a38de269131f9b60ea5 ts=2026-10-06T17:04:54.9870000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1747] _id=6ac6743dde269131f9bc8ece ts=2026-10-07T16:33:00.8750000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 554 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[7925] _id=6ad10495de269131f9ddf6ad ts=2026-10-15T16:51:32.4710000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7926] _id=6ad10495de269131f9ddf6ae ts=2026-10-15T16:51:32.4710000Z; 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8005] _id=6ad10509de269131f9de02b4 ts=2026-10-15T16:53:28.7960000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8006] _id=6ad10509de269131f9de02b5 ts=2026-10-15T16:53:28.7960000Z; 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[9210] _id=6ad256b8de269131f9e639e3 ts=2026-10-16T16:54:16.6420000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[9211] _id=6ad256b8de269131f9e639e4 ts=2026-10-16T16:54:16.6420000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 25m 
  - Evidence: 191h 25m: 6ab9a8e69a8420a1e6b56b24.jsonl[512] _id=6ac3d817de269131f9ae6896 ts=2026-10-05T17:02:15.0720000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4462] _id=6ace5bf1de269131f9cf6c98 ts=2026-10-13T16:27:28.7480000Z; 24h 20m: 6ab9a8e69a8420a1e6b56b24.jsonl[6264] _id=6acfb1c1de269131f9d5c989 ts=2026-10-14T16:45:53.1370000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8301] _id=6ad1080cde269131f9de4ded ts=2026-10-15T17:06:19.4850000Z; 24h 18m: 6ab9a8e69a8420a1e6b56b24.jsonl[4462] _id=6ace5bf1de269131f9cf6c98 ts=2026-10-13T16:27:28.7480000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[6264] _id=6acfb1c1de269131f9d5c989 ts=2026-10-14T16:45:53.1370000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a8e69a8420a1e6b56b24.jsonl[4225] _id=6ac7cc1fde269131f9c4d08b ts=2026-10-08T17:00:15.0890000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4349] _id=6ace5a89de269131f9cf5d8c ts=2026-10-13T16:21:27.8920000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b24.jsonl[485] _id=6ac3d7dede269131f9ae626a ts=2026-10-05T17:01:18.0970000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[520] _id=6ac52764de269131f9b57b0d ts=2026-10-06T16:52:50.6750000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b24.jsonl[1703] _id=6ac52a2dde269131f9b60d13 ts=2026-10-06T17:04:44.0730000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1746] _id=6ac67431de269131f9bc8dcb ts=2026-10-07T16:32:48.3600000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 33 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[3329] _id=6ac7c56bde269131f9c434a5 ts=2026-10-08T16:31:39.3460000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3330] _id=6ac7c56bde269131f9c434a6 ts=2026-10-08T16:31:39.3460000Z; 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[4628] _id=6ace5e5ade269131f9cf91e4 ts=2026-10-13T16:37:46.0560000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4632] _id=6ace5e5ade269131f9cf91e5 ts=2026-10-13T16:37:46.0560000Z; 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[6271] _id=6acfb1dcde269131f9d5cd31 ts=2026-10-14T16:46:19.1240000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[6272] _id=6acfb1dcde269131f9d5cd32 ts=2026-10-14T16:46:19.1240000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 36m 
  - Evidence: 119h 36m: 6ab9a8e69a8420a1e6b56b24.jsonl[4210] _id=6ac7cbebde269131f9c4cc16 ts=2026-10-08T16:59:23.6970000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4585] _id=6ace5df1de269131f9cf890c ts=2026-10-13T16:36:01.1460000Z; 23h 54m: 6ab9a8e69a8420a1e6b56b24.jsonl[489] _id=6ac3d7ebde269131f9ae639f ts=2026-10-05T17:01:31.3290000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[581] _id=6ac5281ade269131f9b5a07d ts=2026-10-06T16:55:53.0410000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b24.jsonl[1713] _id=6ac52a33de269131f9b60dff ts=2026-10-06T17:04:50.3400000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1767] _id=6ac67462de269131f9bc9202 ts=2026-10-07T16:33:37.6600000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.009s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[7797] _id=6ad1037ede269131f9ddd86c ts=2026-10-15T16:46:53.2410000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7799] _id=6ad1037ede269131f9ddd86d ts=2026-10-15T16:46:53.2410000Z; 1ms: 6ab9a8e69a8420a1e6b56b24.jsonl[7828] _id=6ad103bade269131f9dddcc7 ts=2026-10-15T16:47:53.7280000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7829] _id=6ad103bade269131f9dddcc8 ts=2026-10-15T16:47:53.7290000Z; 9ms: 6ab9a8e69a8420a1e6b56b24.jsonl[90] _id=6ac3d2a5de269131f9ade5e7 ts=2026-10-05T16:39:01.2580000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[93] _id=6ac3d2a5de269131f9ade5ec ts=2026-10-05T16:39:01.2670000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b24.jsonl[4342] _id=6ac7cd2bde269131f9c4e03d ts=2026-10-08T17:04:42.8910000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4348] _id=6ace5a89de269131f9cf5d8b ts=2026-10-13T16:21:22.5920000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b24.jsonl[1732] _id=6ac52a3ede269131f9b60eed ts=2026-10-06T17:05:01.5890000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1743] _id=6ac67426de269131f9bc8cd6 ts=2026-10-07T16:32:33.7540000Z; 23h 25m: 6ab9a8e69a8420a1e6b56b24.jsonl[3144] _id=6ac67b73de269131f9bd8d8c ts=2026-10-07T17:03:47.1070000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3166] _id=6ac7c4e3de269131f9c42967 ts=2026-10-08T16:29:16.9240000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[5528] _id=6ace64bdde269131f9d01263 ts=2026-10-13T17:05:00.9100000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[5605] _id=6acfab4dde269131f9d54bae ts=2026-10-13T17:05:00.91Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6ab9a8e69a8420a1e6b56b24.jsonl[3762] _id=6ac7c681de269131f9c45694 ts=2026-10-08T16:36:16.9010000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[5287] _id=6ace63b9de269131f9cff5e1 ts=2026-10-13T17:00:39.5850000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b24.jsonl[7640] _id=6ad101eede269131f9ddb66b ts=2026-10-15T16:40:12.7170000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8441] _id=6ad25044de269131f9e5d3a0 ts=2026-10-16T16:26:43.3210000Z; 23h 35m: 6ab9a8e69a8420a1e6b56b24.jsonl[6802] _id=6acfb551de269131f9d63109 ts=2026-10-14T17:01:02.2470000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7501] _id=6ad10120de269131f9dda8e8 ts=2026-10-15T16:36:46.4350000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1318 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[1004] _id=6ac5293ade269131f9b5e063 ts=2026-10-06T17:00:40.1220000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1040] _id=6ac5293bde269131f9b5e06e ts=2026-10-06T17:00:40.1220000Z; 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[1011] _id=6ac52937de269131f9b5dfb9 ts=2026-10-06T17:00:36.7980000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1025] _id=6ac52938de269131f9b5dfc3 ts=2026-10-06T17:00:36.7980000Z; 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[1014] _id=6ac52936de269131f9b5df7b ts=2026-10-06T17:00:36.2790000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1015] _id=6ac52936de269131f9b5df7f ts=2026-10-06T17:00:36.2790000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6ab9a8e69a8420a1e6b56b24.jsonl[2659] _id=6ac67a25de269131f9bd675b ts=2026-10-07T16:58:12.9560000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[5270] _id=6ace6355de269131f9cfec1b ts=2026-10-13T16:59:00.6250000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b24.jsonl[5281] _id=6ace638dde269131f9cff08c ts=2026-10-13T16:59:56.4720000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[6351] _id=6acfb469de269131f9d613d0 ts=2026-10-14T16:57:13.2810000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8e69a8420a1e6b56b24.jsonl[3938] _id=6ac7c918de269131f9c4a1ef ts=2026-10-08T16:47:20.0580000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4540] _id=6ace5d61de269131f9cf7ed1 ts=2026-10-13T16:33:36.7620000Z; 47h 43m: 6ab9a8e69a8420a1e6b56b24.jsonl[6158] _id=6acfb01dde269131f9d5a45e ts=2026-10-14T16:38:52.9250000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8368] _id=6ad24f47de269131f9e5c37e ts=2026-10-16T16:22:31.3580000Z; 23h 54m: 6ab9a8e69a8420a1e6b56b24.jsonl[2543] _id=6ac678b9de269131f9bd4849 ts=2026-10-07T16:52:09.1680000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3930] _id=6ac7c90ade269131f9c4a072 ts=2026-10-08T16:47:06.6710000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.027s shown 
  - Evidence: 21ms: 6ab9a8e69a8420a1e6b56b24.jsonl[2445] _id=6ac67764de269131f9bd1da5 ts=2026-10-07T16:46:27.7350000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[2449] _id=6ac67764de269131f9bd1da9 ts=2026-10-07T16:46:27.7560000Z; 27ms: 6ab9a8e69a8420a1e6b56b24.jsonl[2444] _id=6ac67764de269131f9bd1da1 ts=2026-10-07T16:46:27.7080000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[2445] _id=6ac67764de269131f9bd1da5 ts=2026-10-07T16:46:27.7350000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b24.jsonl[4321] _id=6ac7cd1cde269131f9c4dfdd ts=2026-10-08T17:04:27.9880000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4387] _id=6ace5acfde269131f9cf6008 ts=2026-10-13T16:22:39.2800000Z; 72h 5m: 6ab9a8e69a8420a1e6b56b24.jsonl[424] _id=6ac3d75cde269131f9ae54b1 ts=2026-10-05T16:59:07.8450000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4327] _id=6ac7cd08de269131f9c4df27 ts=2026-10-08T17:04:08.6170000Z; 47h 58m: 6ab9a8e69a8420a1e6b56b24.jsonl[5121] _id=6ace61eade269131f9cfd3dc ts=2026-10-13T16:52:58.0140000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7903] _id=6ad10476de269131f9ddf269 ts=2026-10-15T16:51:01.4000000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b24.jsonl[4334] _id=6ac7cd1cde269131f9c4dfdf ts=2026-10-08T17:04:28.0200000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4356] _id=6ace5a91de269131f9cf5dcc ts=2026-10-13T16:21:37.2900000Z; 72h 2m: 6ab9a8e69a8420a1e6b56b24.jsonl[423] _id=6ac3d75cde269131f9ae54b7 ts=2026-10-05T16:59:07.8670000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4254] _id=6ac7cc7cde269131f9c4d820 ts=2026-10-08T17:01:47.9580000Z; 47h 57m: 6ab9a8e69a8420a1e6b56b24.jsonl[5125] _id=6ace61ebde269131f9cfd3e9 ts=2026-10-13T16:52:58.0960000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7873] _id=6ad1043ede269131f9ddeb15 ts=2026-10-15T16:50:05.0720000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b24.jsonl[4325] _id=6ac7cd10de269131f9c4df56 ts=2026-10-08T17:04:16.1630000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4360] _id=6ace5aa2de269131f9cf5eab ts=2026-10-13T16:21:53.7850000Z; 72h 3m: 6ab9a8e69a8420a1e6b56b24.jsonl[417] _id=6ac3d73fde269131f9ae518d ts=2026-10-05T16:58:39.4160000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4258] _id=6ac7cc8ade269131f9c4d8fe ts=2026-10-08T17:02:02.1760000Z; 47h 57m: 6ab9a8e69a8420a1e6b56b24.jsonl[5119] _id=6ace61e8de269131f9cfd3b3 ts=2026-10-13T16:52:56.0210000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[7874] _id=6ad10442de269131f9ddeba9 ts=2026-10-15T16:50:09.0650000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 26 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6ab9a8e69a8420a1e6b56b24.jsonl[5111] _id=6ace61e0de269131f9cfd32f ts=2026-10-13T16:52:47.4770000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[5112] _id=6ace61e0de269131f9cfd330 ts=2026-10-13T16:52:47.4790000Z; 4ms: 6ab9a8e69a8420a1e6b56b24.jsonl[4271] _id=6ac7ccacde269131f9c4da8c ts=2026-10-08T17:02:36.1050000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4273] _id=6ac7ccacde269131f9c4da8e ts=2026-10-08T17:02:36.1090000Z; 6ms: 6ab9a8e69a8420a1e6b56b24.jsonl[5091] _id=6ace61bdde269131f9cfd120 ts=2026-10-13T16:52:13.0390000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[5094] _id=6ace61bdde269131f9cfd122 ts=2026-10-13T16:52:13.0450000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b24.jsonl[4309] _id=6ac7cceede269131f9c4ddec ts=2026-10-08T17:03:42.1100000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4361] _id=6ace5a97de269131f9cf5e1b ts=2026-10-13T16:21:43.2810000Z; 72h 2m: 6ab9a8e69a8420a1e6b56b24.jsonl[5080] _id=6ace61abde269131f9cfd011 ts=2026-10-13T16:51:54.9900000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[9231] _id=6ad256d7de269131f9e63b93 ts=2026-10-16T16:54:47.5180000Z; 72h 2m: 6ab9a8e69a8420a1e6b56b24.jsonl[386] _id=6ac3d758de269131f9ae545f ts=2026-10-05T16:59:04.0370000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4247] _id=6ac7cc82de269131f9c4d895 ts=2026-10-08T17:01:53.9620000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 20m 36s 
  - Evidence: 20m 36s: 6ab9a8e69a8420a1e6b56b24.jsonl[8440] _id=6ad2503cde269131f9e5d339 ts=2026-10-16T16:26:36.6740000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[9031] _id=6ad25511de269131f9e61715 ts=2026-10-16T16:47:13.6640000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a8e69a8420a1e6b56b24.jsonl[3162] _id=6ac7c4c2de269131f9c42788 ts=2026-10-08T16:28:50.4540000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4345] _id=6ace5a76de269131f9cf5cbd ts=2026-10-13T16:21:09.4700000Z; 23h 58m: 6ab9a8e69a8420a1e6b56b24.jsonl[6901] _id=6ad0fcdbde269131f9dd5743 ts=2026-10-15T16:18:34.3060000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8306] _id=6ad24e11de269131f9e5ab79 ts=2026-10-16T16:17:21.4250000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b24.jsonl[1741] _id=6ac67417de269131f9bc8bbf ts=2026-10-07T16:32:22.4380000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3162] _id=6ac7c4c2de269131f9c42788 ts=2026-10-08T16:28:50.4540000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a8e69a8420a1e6b56b24.jsonl[3161] _id=6ac7c4c2de269131f9c42787 ts=2026-10-08T16:28:50.4540000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4344] _id=6ace5a76de269131f9cf5cbc ts=2026-10-13T16:21:09.4700000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b24.jsonl[1740] _id=6ac67417de269131f9bc8bbe ts=2026-10-07T16:32:22.4380000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3161] _id=6ac7c4c2de269131f9c42787 ts=2026-10-08T16:28:50.4540000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b24.jsonl[4481] _id=6ace5c00de269131f9cf6d73 ts=2026-10-13T16:27:43.5280000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[5603] _id=6acfab4dde269131f9d54bb1 ts=2026-10-14T16:18:20.7570000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8434] _id=6ad24ff4de269131f9e5ceb0 ts=2026-10-16T16:25:24.3780000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8439] _id=6ad25017de269131f9e5d0ee ts=2026-10-16T16:25:24.378Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 45m 
  - Evidence: 143h 45m: 6ab9a8e69a8420a1e6b56b24.jsonl[4343] _id=6ac7cd32de269131f9c4e050 ts=2026-10-08T17:04:50.4920000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[6315] _id=6acfb2e0de269131f9d5f19d ts=2026-10-14T16:50:40.1060000Z; 24h 1m: 6ab9a8e69a8420a1e6b56b24.jsonl[515] _id=6ac3d880de269131f9ae70af ts=2026-10-05T17:04:00.3810000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1738] _id=6ac67417de269131f9bc8bbb ts=2026-10-06T17:05:08.786Z; 24h 1m: 6ab9a8e69a8420a1e6b56b24.jsonl[3143] _id=6ac67b76de269131f9bd8dcd ts=2026-10-07T17:03:49.6120000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4343] _id=6ac7cd32de269131f9c4e050 ts=2026-10-08T17:04:50.4920000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8315] _id=6ad24e2cde269131f9e5aced ts=2026-10-16T16:17:47.7450000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8316] _id=6ad24e9bde269131f9e5b677 ts=2026-10-16T16:17:47.745Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b24.jsonl[4339] _id=6ac7cd25de269131f9c4e027 ts=2026-10-08T17:04:37.3660000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[4350] _id=6ace5a89de269131f9cf5d8d ts=2026-10-13T16:21:27.9350000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b24.jsonl[487] _id=6ac3d7edde269131f9ae63d1 ts=2026-10-05T17:01:33.5070000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[547] _id=6ac527bede269131f9b58cc0 ts=2026-10-06T16:54:21.0510000Z; 23h 38m: 6ab9a8e69a8420a1e6b56b24.jsonl[547] _id=6ac527bede269131f9b58cc0 ts=2026-10-06T16:54:21.0510000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[1744] _id=6ac67426de269131f9bc8cd7 ts=2026-10-07T16:32:37.1370000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b24.jsonl[9321] _id=6ad25759de269131f9e64534 ts=2026-10-16T16:56:57.3870000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[9325] _id=6ad25759de269131f9e64535 ts=2026-10-16T16:56:57.3870000Z; 1ms: 6ab9a8e69a8420a1e6b56b24.jsonl[8800] _id=6ad252adde269131f9e5f79a ts=2026-10-16T16:37:00.9660000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[8801] _id=6ad252adde269131f9e5f79b ts=2026-10-16T16:37:00.9670000Z; 2ms: 6ab9a8e69a8420a1e6b56b24.jsonl[3169] _id=6ac7c4e3de269131f9c4296a ts=2026-10-08T16:29:21.1390000Z -> 6ab9a8e69a8420a1e6b56b24.jsonl[3170] _id=6ac7c4e3de269131f9c4296b ts=2026-10-08T16:29:21.1410000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[323] _id=6ac3d662de269131f9ae3c27 ts=2026-10-05T16:54:57.9480000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[433] _id=6ac3d773de269131f9ae5773 ts=2026-10-05T16:59:31.0150000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[2542] _id=6ac678b8de269131f9bd4822 ts=2026-10-07T16:52:07.8510000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 34 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[763] _id=6ac528c5de269131f9b5cb99 ts=2026-10-06T16:58:41.3430000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[739] _id=6ac528c5de269131f9b5cb9d ts=2026-10-06T16:58:41.4370000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[766] _id=6ac528c5de269131f9b5cba4 ts=2026-10-06T16:58:42.5700000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 68 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[701] _id=6ac528bbde269131f9b5c8fd ts=2026-10-06T16:58:10.5590000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[705] _id=6ac528bede269131f9b5c9c9 ts=2026-10-06T16:58:24.6890000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[724] _id=6ac528bede269131f9b5c9cf ts=2026-10-06T16:58:24.8700000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[5125] _id=6ace61ebde269131f9cfd3e9 ts=2026-10-13T16:52:58.0960000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[8003] _id=6ad10515de269131f9de03ff ts=2026-10-15T16:53:40.3300000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[8440] _id=6ad2503cde269131f9e5d339 ts=2026-10-16T16:26:36.6740000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[9031] _id=6ad25511de269131f9e61715 ts=2026-10-16T16:47:13.6640000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 196 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[775] _id=6ac528c8de269131f9b5cc35 ts=2026-10-06T16:58:45.5110000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[783] _id=6ac528c8de269131f9b5cc3d ts=2026-10-06T16:58:45.5860000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[859] _id=6ac528e8de269131f9b5d243 ts=2026-10-06T16:59:18.2820000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 486 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[664] _id=6ac528bbde269131f9b5c8bb ts=2026-10-06T16:56:48.6080000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[637] _id=6ac528bbde269131f9b5c8c6 ts=2026-10-06T16:56:48.7170000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[638] _id=6ac528bbde269131f9b5c8cc ts=2026-10-06T16:56:48.8450000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[4261] _id=6ac7cc92de269131f9c4d96d ts=2026-10-08T17:02:10.0830000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[4302] _id=6ac7ccdcde269131f9c4dd34 ts=2026-10-08T17:03:24.3100000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[4309] _id=6ac7cceede269131f9c4ddec ts=2026-10-08T17:03:42.1100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 372 start, 367 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 22 unmatched 'BecameCameraCentered' (totals: 628 open, 640 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 73 unmatched 'BecameVisible' (totals: 942 open, 937 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'argumentationToolOpen' (totals: 13 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 43 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 242 of 9600 adjacent _id pairs reverse in client time; worst 104.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b24.jsonl[671] _id=6ac528b8de269131f9b5c82b ts=2026-10-06T16:58:31.5870000Z`; `6ab9a8e69a8420a1e6b56b24.jsonl[679] _id=6ac528b8de269131f9b5c833 ts=2026-10-06T16:56:47.6010000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.89s, min -84434.66s, max -0.12s over 9601 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b24\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

No coverage-related findings.

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3147 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2193); Unit 4 Dev (450); Unit 3 Dungeon Dev (272); Unit 5 Dev - Dungeon (232)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.38s, n=3146)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3147/3147 records)
    "BecameVisible"  x942
    "BecameInvisible"  x937
    "BecameCameraUncentered"  x640
    "BecameCameraCentered"  x628
data.pieceId  (string, 3147/3147 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3147/3147 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1984 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (565); Unit 3 Dev (309); Unit 4 Dev (253); Unit 5 Dev (230); Unit 1 Dev (199); Unit 3 Dungeon Dev (162); Unit 4 Dev - Dungeon (106); Unit 4 Dev - Anderson Base (85); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1245 of 1984 records
- **Intervals:** median 3.83s (p5 0.00s / p95 30.26s, n=1983)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1245; [conversationId, dialogueEventType] x739
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1984/1984 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 1984/1984 records)
    "DialogueNodeEvent"  x1245
    "DialogueStartEvent"  x372
    "DialogueFinishEvent"  x367
data.nodeId  (number, 1245/1984 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `InputEvent` — 1801 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (473); Unit 3 Dev (334); Unit 4 Dev - Dungeon (324); Unit 4 Dev (215); Unit 3 Dungeon Dev (170); Unit 5 Dev - Dungeon (121); Unit 5 Dev (79); Unit 1 Dev (59); Unit 4 Dev - Anderson Base (26)
- **Intervals:** median 2.26s (p5 0.14s / p95 36.12s, n=1800)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1801/1801 records)
    "pressed"  x1801
data.actionType  (string, 1801/1801 records)
    "Move"  x1188
    "Interact"  x389
    "Jump"  x76
    "Hoverboard"  x72
    "Ascend"  x52
    "Map"  x12
    "Sprint"  x10
    "Pause"  x1
    "SkipCinematic"  x1
data.key  (string, 1801/1801 records, 4 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1801/1801 records)
    "Player"  x1503
    "Drone"  x298
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1717 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (508); Unit 3 Dev (251); Unit 4 Dev (216); Unit 1 Dev (177); Unit 5 Dev (133); Unit 4 Dev - Dungeon (126); Unit 3 Dungeon Dev (125); Unit 5 Dev - Dungeon (122); Unit 4 Dev - Anderson Base (59)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.18s, n=1705)
- **Fields under `data`:**

```text
data.position  (object, 1717/1717 records)
data.position.x  (number, 1717/1717 records)
    numeric range -729.762 .. 1549.85 (592 unique)
data.position.y  (number, 1717/1717 records)
    numeric range -114.468 .. 222.004 (405 unique)
data.position.z  (number, 1717/1717 records)
    numeric range -1107.79 .. 1769.86 (592 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 312 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (91); Unit 2 Prod (Refactor) (74); Unit 5 Dev (66); Unit 1 Dev (42); Unit 3 Dev (39)
- **Intervals:** median 0.90s (p5 0.03s / p95 12.39s, n=311)
- **Fields under `data`:**

```text
data.actionType  (string, 312/312 records)
    "argumentationNodeHoverEnd"  x132
    "argumentationNodeHoverStart"  x132
    "argumentationNodeAdd"  x36
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 312/312 records)
    "Unit 4 - Flooding"  x91
    "Unit 2 – Watershed"  x74
    "Unit 5"  x66
    "Unit 3 - Pollution Upstream"  x39
    "Unit 1 - Freshwater"  x27
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 312/312 records)
    "A"  x42
    "D"  x40
    "B"  x36
    "I"  x35
    "1"  x34
    "C"  x30
    "4"  x26
    "II"  x26
    "2"  x21
    "3"  x19
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 268 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (83); Unit 2 Prod (Refactor) (60); Unit 3 Dungeon Dev (34); Unit 5 Dev (27); Unit 4 Dev (20); Unit 5 Dev - Dungeon (14); Unit 3 Dev (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 12.59s (p5 0.21s / p95 459.36s, n=267)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 268/268 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 268/268 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 75 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 4 Dev - Dungeon (10); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 75 of 75 records
- **Intervals:** median 205.04s (p5 0.00s / p95 84280.23s, n=74)
- **`data` key-set variants:** [questEventType, questID, questName] x43; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 75/75 records)
    "questActiveEvent"  x43
    "questFinishEvent"  x32
data.questID  (string, 75/75 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 75/75 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/75 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 65 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (41); Unit 2 Prod (Refactor) (20); Unit 4 Dev (4)
- **Intervals:** median 8.21s (p5 1.56s / p95 85139.14s, n=64)
- **`data` key-set variants:** [actionType, featureUsed] x50; [actionType, featureUsed, location] x15
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 65/65 records)
    "MapCloseEvent"  x25
    "MapOpenEvent"  x25
    "WaypointMoveEvent"  x9
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x2
data.featureUsed  (string, 65/65 records)
    "Map"  x50
    "Waypoint"  x15
data.location  (object, 15/65 records)
data.location.x  (number, 15/65 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 15/65 records)
    numeric range -278.8 .. 113.448 (13 unique)
data.location.z  (number, 15/65 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 38 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev (10); Unit 3 Dev (8)
- **Intervals:** median 2.44s (p5 0.17s / p95 17266.31s, n=37)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x32; [Soil Key Puzzle Status, Unit] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/38 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/38 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 32/38 records)
    "RightDrag"  x19
    "LeftDrag"  x13
data.currentSoilType  (string, 32/38 records)
    "CLAY"  x8
    "CLAYSAND"  x7
    "SAND"  x6
    "CLAYROCK"  x5
    "SANDGRAVEL"  x4
    "BEDROCK"  x1
    "GRAVEL"  x1
data.isCorrectSelection  (string, 32/38 records)
    "false"  x23
    "true"  x9
data.waterLevelStatus  (string, 32/38 records)
    "TooHigh"  x16
    "Proper"  x9
    "TooLow"  x7
data.waterRetentionChange  (string, 32/38 records)
    "Increase"  x14
    "Decrease"  x9
    "NoChange"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 4 Dev (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 494.91s (p5 10.04s / p95 87176.01s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 21 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (21)
- **Intervals:** median 19.78s (p5 5.82s / p95 93.75s, n=20)
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "On"  x16
    "Off"  x5
data.floor  (string, 21/21 records)
    "3"  x8
    "4"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 21/21 records)
    "One"  x20
    "Two"  x1
data.machineType  (string, 21/21 records)
    "Condenser"  x9
    "Evaporator"  x7
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 21/21 records)
    "2"  x9
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 4 Dev (6); Unit 5 Dev (1)
- **Intervals:** median 1666.06s (p5 12.37s / p95 120723.12s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (6); Unit 4 Dev - Anderson Base (5); Unit 2 Prod (Refactor) (4); Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 31.05s (p5 7.65s / p95 293498.88s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 18/18 records)
    "Unit 5"  x6
    "Unit 4 - Flooding"  x5
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 126.43s (p5 0.06s / p95 310380.84s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 16/16 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 2 – Watershed"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 6.73s (p5 0.99s / p95 135.05s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x6
    "Gravel"  x5
    "Sand"  x3
    "Bedrock"  x2
data.floor  (string, 16/16 records)
    "3"  x7
    "5"  x5
    "4"  x4
data.machine  (string, 16/16 records)
    "1"  x15
    "2"  x1
data.row  (string, 16/16 records)
    "TopRow"  x15
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `SolarStillDesignEvent` — 14 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (14)
- **Intervals:** median 1.65s (p5 0.90s / p95 4.25s, n=13)
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
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/14 records)
    "Flat"  x1
data.featureUsed  (string, 14/14 records)
    "ExtraCovering"  x6
    "RoofStyle"  x6
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 13/14 records, 3 empty-string)
    ""  x3
    "Covered"  x3
    "Flat"  x2
    "Tilted Out"  x2
    "Cold"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 1 Dev (3); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 17.80s (p5 2.34s / p95 327415.99s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 2 – Watershed"  x7
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Waterfall Data"  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 84966.79s (p5 271.00s / p95 241672.47s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (7); Unit 2 Prod (Refactor) (3); Transition (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 43470.20s (p5 0.99s / p95 280454.95s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev (4); Unit 3 Dev (2)
- **Intervals:** median 3.64s (p5 2.59s / p95 206313.69s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 3.22s (p5 1.62s / p95 31.36s, n=5)
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
- **Intervals:** median 87565.37s (p5 86756.84s / p95 598890.58s, n=4)
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

- **Scenes:** Unit 4 Dev (2); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 247.91s (p5 27.05s / p95 1138.08s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x3
    "Open"  x1
data.chatID  (string, 4/4 records)
    "NA"  x3
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

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
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (9x); "WaypointResetEvent" (2x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*