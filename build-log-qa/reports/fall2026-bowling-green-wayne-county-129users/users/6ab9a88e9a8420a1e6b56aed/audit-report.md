# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56aed

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56aed
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56aed.jsonl
- **Records:** 14320 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56aed
- **Time span:** 2026-10-06T13:18:24.965000+00:00 .. 2026-10-16T13:52:54.457000+00:00 (240h 34m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56aed\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 14320 records, 11 scenes.
- Findings: **0 FAIL**, **29 WARNING**, 97 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6460 | 45.11 | 1 | 9 | 0 | 2026-10-06T13:19:09.776000+00:00 | 2026-10-16T13:52:54.457000+00:00 | 240h 33m |
| PuzzlePieceVisibleEvent | 2660 | 18.58 | 1 | 4 | 0 | 2026-10-06T13:46:40.962000+00:00 | 2026-10-16T13:24:28.310000+00:00 | 239h 37m |
| DialogueEvent | 2270 | 15.85 | 1 | 9 | 1391 | 2026-10-06T13:19:11.404000+00:00 | 2026-10-16T13:52:51.061000+00:00 | 240h 33m |
| PlayerPositionEvent | 1582 | 11.05 | 1 | 9 | 0 | 2026-10-06T13:18:51.206000+00:00 | 2026-10-16T13:52:54.386000+00:00 | 240h 34m |
| argumentationNodeEvent | 434 | 3.03 | 1 | 5 | 0 | 2026-10-06T13:36:42.557000+00:00 | 2026-10-16T13:41:10.850000+00:00 | 240h 4m |
| ObjectInterEvent | 311 | 2.17 | 1 | 9 | 0 | 2026-10-06T13:23:20.618000+00:00 | 2026-10-16T13:52:54.457000+00:00 | 240h 29m |
| TopographicMapEvent | 161 | 1.12 | 1 | 4 | 0 | 2026-10-06T13:31:11.370000+00:00 | 2026-10-15T13:43:30.467000+00:00 | 216h 12m |
| Soil Key Puzzle | 117 | 0.82 | 1 | 3 | 0 | 2026-10-06T13:47:55.153000+00:00 | 2026-10-16T13:14:14.310000+00:00 | 239h 26m |
| questEvent | 77 | 0.54 | 1 | 9 | 77 | 2026-10-06T13:19:11.382000+00:00 | 2026-10-16T13:48:50.337000+00:00 | 240h 29m |
| DaniEvent | 42 | 0.29 | 1 | 4 | 0 | 2026-10-06T13:31:14.060000+00:00 | 2026-10-15T13:28:51.890000+00:00 | 215h 57m |
| WaterChamberEvent | 29 | 0.2 | 1 | 1 | 0 | 2026-10-16T13:24:39.857000+00:00 | 2026-10-16T13:33:33.366000+00:00 | 8m 53s |
| DEBUGMenu | 28 | 0.2 | 1 | 9 | 0 | 2026-10-06T13:18:51.193000+00:00 | 2026-10-16T13:19:50.924000+00:00 | 240h 0m |
| gameWindowFocusEvent | 25 | 0.17 | 1 | 7 | 0 | 2026-10-06T13:18:24.965000+00:00 | 2026-10-16T13:42:58.620000+00:00 | 240h 24m |
| argumentationAnswerEvent | 22 | 0.15 | 1 | 5 | 0 | 2026-10-06T13:39:09.490000+00:00 | 2026-10-16T13:41:12.599000+00:00 | 240h 2m |
| soilMachine | 18 | 0.13 | 1 | 1 | 0 | 2026-10-15T13:34:24.915000+00:00 | 2026-10-15T13:40:26.682000+00:00 | 6m 1s |
| gameWindowUnfocusEvent | 15 | 0.1 | 1 | 7 | 0 | 2026-10-06T13:18:46.608000+00:00 | 2026-10-16T13:42:56.027000+00:00 | 240h 24m |
| TerasGardenBox | 14 | 0.1 | 1 | 1 | 0 | 2026-10-16T13:11:53.572000+00:00 | 2026-10-16T13:13:12.123000+00:00 | 1m 18s |
| argumentationEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-10-06T13:37:29.844000+00:00 | 2026-10-16T13:41:12.633000+00:00 | 240h 3m |
| argumentationToolEvent | 13 | 0.09 | 1 | 3 | 0 | 2026-10-06T13:39:06.795000+00:00 | 2026-10-14T13:40:23.205000+00:00 | 192h 1m |
| gameStartEvent | 12 | 0.08 | 1 | 1 | 0 | 2026-10-06T13:18:24.966000+00:00 | 2026-10-16T13:19:42.666000+00:00 | 240h 1m |
| SolarStillDesignEvent | 7 | 0.05 | 1 | 1 | 0 | 2026-10-16T13:46:26.257000+00:00 | 2026-10-16T13:46:41.708000+00:00 | 15.5s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T13:41:46.304000+00:00 | 2026-10-16T13:52:54.445000+00:00 | 240h 11m |
| chatEvent | 4 | 0.03 | 1 | 3 | 0 | 2026-10-07T13:27:52.758000+00:00 | 2026-10-16T13:34:22.152000+00:00 | 216h 6m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 128496.207s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.716s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 30.995s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 230.215s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 76806.936s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 813.07s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1339.265s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.107s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 42 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.1x vs baseline. 
  - Observed: 117 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.4x vs baseline. 
  - Observed: 22 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; B,1,I; B,2,II; B,3,I; C,1,II; C,2,II; C,4,II; C,D,3,II; C,D,4,3,II; C,D,A,2,II; D,1,II; D,2,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 434 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [19-48, 19-58, 19-46, 19-60, 19-61] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
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
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[155] _id=6ac4f6a9de269131f9b07737 ts=2026-10-06T13:24:56.6770000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[218] _id=6ac4f779de269131f9b091cb ts=2026-10-06T13:28:25.1510000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[308] _id=6ac4f802de269131f9b0b2f8 ts=2026-10-06T13:30:41.8120000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[3] _id=6ac4f521de269131f9b03a8f ts=2026-10-06T13:18:24.9660000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[770] _id=6ac4faeede269131f9b13233 ts=2026-10-06T13:43:09.4020000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[2131] _id=6ac647ecde269131f9b8df98 ts=2026-10-07T13:23:55.5170000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[2] _id=6ac4f521de269131f9b03a8b ts=2026-10-06T13:18:24.9650000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[6] _id=6ac4f538de269131f9b03b8b ts=2026-10-06T13:18:47.4740000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[769] _id=6ac4faedde269131f9b13226 ts=2026-10-06T13:43:09.4010000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[4] _id=6ac4f537de269131f9b03b7b ts=2026-10-06T13:18:46.6080000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[2128] _id=6ac647ecde269131f9b8df92 ts=2026-10-06T14:00:01.261Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[2273] _id=6ac648bbde269131f9b90c10 ts=2026-10-07T13:27:22.3170000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 161 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[349] _id=6ac4f820de269131f9b0b7aa ts=2026-10-06T13:31:11.3700000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[351] _id=6ac4f822de269131f9b0b832 ts=2026-10-06T13:31:14.0480000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[818] _id=6ac4fbdbde269131f9b164c8 ts=2026-10-06T13:47:06.4430000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6459 | 0.0 | 0.515 | 134.08 | 5.961 | 429543.1 | 0.45 | 349 | 9 |
| PuzzlePieceVisibleEvent | 2659 | 0.0 | 0.02 | 324.433 | 1.22 | 518821.831 | 0.18 | 1421 | 7 |
| DialogueEvent | 2269 | 0.0 | 3.124 | 381.675 | 26.455 | 430039.03 | 0.16 | 667 | 7 |
| PlayerPositionEvent | 1570 | 9.753 | 10.002 | 503.235 | 10.691 | 429521.314 | 0.12 | 0 | 6 |
| argumentationNodeEvent | 433 | 0.004 | 0.817 | 1996.001 | 11.722 | 519602.268 | 0.03 | 38 | 5 |
| ObjectInterEvent | 310 | 0.0 | 6.742 | 2792.819 | 253.995 | 431002.096 | 0.02 | 3 | 8 |
| TopographicMapEvent | 160 | 0.023 | 3.716 | 4864.619 | 259.534 | 516198.334 | 0.01 | 4 | 7 |
| Soil Key Puzzle | 116 | 0.005 | 0.938 | 7430.855 | 29.834 | 604495.704 | 0.01 | 3 | 4 |
| questEvent | 76 | 0.0 | 160.853 | 11391.828 | 83534.532 | 430522.49 | 0.01 | 13 | 10 |
| DaniEvent | 41 | 0.006 | 1.951 | 18962.386 | 86189.671 | 517546.436 | 0.0 | 8 | 5 |
| WaterChamberEvent | 28 | 0.807 | 11.117 | 19.054 | 56.387 | 76.225 | 3.15 | 0 | 0 |
| DEBUGMenu | 27 | 8.423 | 535.376 | 32002.212 | 86628.269 | 430735.752 | 0.0 | 0 | 12 |
| gameWindowFocusEvent | 24 | 7.355 | 813.07 | 36061.402 | 86759.466 | 430748.844 | 0.0 | 0 | 12 |
| argumentationAnswerEvent | 21 | 0.566 | 30.995 | 41148.719 | 87037.274 | 605478.242 | 0.0 | 0 | 4 |
| soilMachine | 17 | 1.89 | 4.107 | 21.28 | 72.923 | 158.458 | 2.82 | 0 | 0 |
| gameWindowUnfocusEvent | 14 | 16.305 | 1339.265 | 61817.816 | 261970.724 | 429500.223 | 0.0 | 0 | 8 |
| TerasGardenBox | 13 | 0.693 | 2.376 | 6.042 | 20.358 | 24.973 | 9.93 | 0 | 0 |
| argumentationEvent | 13 | 0.042 | 230.215 | 66478.676 | 294323.835 | 605335.157 | 0.0 | 1 | 4 |
| argumentationToolEvent | 12 | 0.542 | 21.997 | 57606.368 | 319521.065 | 605417.81 | 0.0 | 0 | 2 |
| gameStartEvent | 11 | 82.138 | 76806.936 | 78552.518 | 258992.111 | 430748.844 | 0.0 | 0 | 9 |
| SolarStillDesignEvent | 6 | 1.156 | 1.831 | 2.575 | 4.954 | 5.397 | 23.3 | 0 | 0 |
| EndOfUnit | 4 | 2009.159 | 128496.207 | 216167.035 | 539177.02 | 605666.567 | 0.0 | 0 | 4 |
| chatEvent | 3 | 0.876 | 871.432 | 259329.798 | 699492.521 | 777117.086 | 0.0 | 0 | 2 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 9 group(s), 20 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[5664] _id=6acf7f8cde269131f9d2cf9d ts=2026-10-14T13:11:38.4680000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[5665] _id=6acf7f8cde269131f9d2cf9e ts=2026-10-14T13:11:38.4680000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[5669] _id=6acf7f8cde269131f9d2cfa2 ts=2026-10-14T13:11:38.4690000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[5670] _id=6acf7f8cde269131f9d2cfa3 ts=2026-10-14T13:11:38.4690000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[9389] _id=6acfa860de269131f9d52cfb ts=2026-10-14T16:05:51.1510000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[9390] _id=6acfa860de269131f9d52cfc ts=2026-10-14T16:05:51.1510000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 113 group(s), 181 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[930] _id=6ac4fbc3de269131f9b15f0d ts=2026-10-06T13:46:41.1330000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[936] _id=6ac4fbc3de269131f9b15f16 ts=2026-10-06T13:46:41.1330000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[908] _id=6ac4fbc5de269131f9b15fc4 ts=2026-10-06T13:46:41.9970000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[924] _id=6ac4fbc5de269131f9b15fce ts=2026-10-06T13:46:41.9970000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[948] _id=6ac4fbc6de269131f9b15fdc ts=2026-10-06T13:46:42.0630000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[939] _id=6ac4fbc6de269131f9b15fff ts=2026-10-06T13:46:42.0630000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[14062] _id=6ad229bbde269131f9e3df1f ts=2026-10-16T13:42:19.3220000Z == 6ab9a88e9a8420a1e6b56aed.jsonl[14063] _id=6ad229bbde269131f9e3df20 ts=2026-10-16T13:42:19.3220000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a88e9a8420a1e6b56aed.jsonl[107] _id=6ac4f649de269131f9b060d3 ts=2026-10-06T13:23:20.6180000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[108] _id=6ac4f649de269131f9b060e4 ts=2026-10-06T13:23:20.6250000Z`; `358ms: 6ab9a88e9a8420a1e6b56aed.jsonl[865] _id=6ac4fb94de269131f9b155f4 ts=2026-10-06T13:45:55.5990000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[877] _id=6ac4fb94de269131f9b1560c ts=2026-10-06T13:45:55.9570000Z`; `243ms: 6ab9a88e9a8420a1e6b56aed.jsonl[877] _id=6ac4fb94de269131f9b1560c ts=2026-10-06T13:45:55.9570000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[878] _id=6ac4fb95de269131f9b1561c ts=2026-10-06T13:45:56.2000000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 185 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `171ms: 6ab9a88e9a8420a1e6b56aed.jsonl[922] _id=6ac4fbc2de269131f9b15f03 ts=2026-10-06T13:46:40.9620000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[930] _id=6ac4fbc3de269131f9b15f0d ts=2026-10-06T13:46:41.1330000Z`; `10ms: 6ab9a88e9a8420a1e6b56aed.jsonl[942] _id=6ac4fbc3de269131f9b15f40 ts=2026-10-06T13:46:41.1330000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[937] _id=6ac4fbc3de269131f9b15f50 ts=2026-10-06T13:46:41.1430000Z`; `113ms: 6ab9a88e9a8420a1e6b56aed.jsonl[938] _id=6ac4fbc4de269131f9b15fa2 ts=2026-10-06T13:46:41.8100000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[947] _id=6ac4fbc5de269131f9b15fae ts=2026-10-06T13:46:41.9230000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `693ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12545] _id=6ad222e0de269131f9e3587d ts=2026-10-16T13:13:03.7560000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[12549] _id=6ad222e0de269131f9e35889 ts=2026-10-16T13:13:04.4490000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6ab9a88e9a8420a1e6b56aed.jsonl[2122] _id=6ac4fed9de269131f9b23894 ts=2026-10-06T13:59:53.1010000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[2126] _id=6ac4fedade269131f9b238a8 ts=2026-10-06T13:59:53.1270000Z`; `286ms: 6ab9a88e9a8420a1e6b56aed.jsonl[2534] _id=6ac649b4de269131f9b94ada ts=2026-10-07T13:31:31.2240000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[2535] _id=6ac649b4de269131f9b94ae5 ts=2026-10-07T13:31:31.5100000Z`; `521ms: 6ab9a88e9a8420a1e6b56aed.jsonl[6140] _id=6acf823cde269131f9d2f74f ts=2026-10-14T13:23:07.8680000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[6147] _id=6acf823cde269131f9d2f75b ts=2026-10-14T13:23:08.3890000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `566ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12078] _id=6ad0da87de269131f9db3092 ts=2026-10-15T13:52:07.2480000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[12080] _id=6ad0da88de269131f9db30ad ts=2026-10-15T13:52:07.8140000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `77ms: 6ab9a88e9a8420a1e6b56aed.jsonl[7025] _id=6acf868ade269131f9d345e3 ts=2026-10-14T13:41:29.9950000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[7028] _id=6acf868ade269131f9d345e9 ts=2026-10-14T13:41:30.0720000Z`; `42ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12224] _id=6ad0db62de269131f9db4d34 ts=2026-10-15T13:55:45.6080000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[12228] _id=6ad0db62de269131f9db4d3a ts=2026-10-15T13:55:45.6500000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `442ms: 6ab9a88e9a8420a1e6b56aed.jsonl[553] _id=6ac4f975de269131f9b0e953 ts=2026-10-06T13:36:53.0060000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[546] _id=6ac4f976de269131f9b0e97a ts=2026-10-06T13:36:53.4480000Z`; `564ms: 6ab9a88e9a8420a1e6b56aed.jsonl[547] _id=6ac4f975de269131f9b0e95a ts=2026-10-06T13:36:53.0830000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[555] _id=6ac4f976de269131f9b0e98f ts=2026-10-06T13:36:53.6470000Z`; `32ms: 6ab9a88e9a8420a1e6b56aed.jsonl[588] _id=6ac4f9a9de269131f9b0f806 ts=2026-10-06T13:37:44.3660000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[584] _id=6ac4f9a9de269131f9b0f80c ts=2026-10-06T13:37:44.3980000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `542ms: 6ab9a88e9a8420a1e6b56aed.jsonl[6909] _id=6acf85b8de269131f9d33c4f ts=2026-10-14T13:37:59.7070000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[6907] _id=6acf85b8de269131f9d33c56 ts=2026-10-14T13:38:00.2490000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a88e9a8420a1e6b56aed.jsonl[14218] _id=6ad22b06de269131f9e3fcf8 ts=2026-10-16T13:47:50.1800000Z ~ 6ab9a88e9a8420a1e6b56aed.jsonl[14213] _id=6ad22b06de269131f9e3fcfa ts=2026-10-16T13:47:50.1830000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6ab9a88e9a8420a1e6b56aed.jsonl[4486] _id=6ac79cbcde269131f9c09103 ts=2026-10-08T13:38:03.8250000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4979] _id=6ace2f4cde269131f9ce8f49 ts=2026-10-13T13:16:59.5770000Z; 24h 13m: 6ab9a88e9a8420a1e6b56aed.jsonl[2132] _id=6ac647f7de269131f9b8e1b2 ts=2026-10-07T13:24:06.2050000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4475] _id=6ac79cafde269131f9c08e58 ts=2026-10-08T13:37:50.7300000Z; 23h 40m: 6ab9a88e9a8420a1e6b56aed.jsonl[771] _id=6ac4faf6de269131f9b133db ts=2026-10-06T13:43:18.3640000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2129] _id=6ac647ecde269131f9b8df96 ts=2026-10-07T13:23:55.3680000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 45m 
  - Evidence: 143h 45m: 6ab9a88e9a8420a1e6b56aed.jsonl[2546] _id=6ac649cdde269131f9b95129 ts=2026-10-07T13:31:56.7840000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4991] _id=6ace2f77de269131f9ce9006 ts=2026-10-13T13:17:43.2200000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aed.jsonl[6570] _id=6acf83ebde269131f9d31bac ts=2026-10-14T13:30:19.4380000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10668] _id=6ad0d4f3de269131f9da938b ts=2026-10-15T13:28:18.4030000Z; 23h 56m: 6ab9a88e9a8420a1e6b56aed.jsonl[360] _id=6ac4f827de269131f9b0b910 ts=2026-10-06T13:31:19.0990000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2302] _id=6ac648d5de269131f9b912de ts=2026-10-07T13:27:48.7700000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.006s..0.008s shown 
  - Evidence: 6ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10683] _id=6ad0d512de269131f9da96ab ts=2026-10-15T13:28:49.7160000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10685] _id=6ad0d512de269131f9da96b1 ts=2026-10-15T13:28:49.7220000Z; 7ms: 6ab9a88e9a8420a1e6b56aed.jsonl[358] _id=6ac4f826de269131f9b0b8c8 ts=2026-10-06T13:31:17.5510000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[355] _id=6ac4f826de269131f9b0b8d0 ts=2026-10-06T13:31:17.5580000Z; 8ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10676] _id=6ad0d4fade269131f9da944e ts=2026-10-15T13:28:25.5390000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10677] _id=6ad0d4fade269131f9da9450 ts=2026-10-15T13:28:25.5470000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a88e9a8420a1e6b56aed.jsonl[4971] _id=6ac7a180de269131f9c1567a ts=2026-10-08T13:58:23.4040000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5008] _id=6ace3156de269131f9cea113 ts=2026-10-13T13:25:42.4340000Z; 23h 39m: 6ab9a88e9a8420a1e6b56aed.jsonl[4471] _id=6ac65051de269131f9ba3c44 ts=2026-10-07T13:59:44.3470000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4597] _id=6ac79ce9de269131f9c0998b ts=2026-10-08T13:38:48.0430000Z; 23h 25m: 6ab9a88e9a8420a1e6b56aed.jsonl[2124] _id=6ac4fedade269131f9b238a4 ts=2026-10-06T13:59:53.1220000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2135] _id=6ac6483dde269131f9b8eedc ts=2026-10-07T13:25:16.8410000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 667 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12072] _id=6ad0da87de269131f9db3096 ts=2026-10-15T13:52:07.2720000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12073] _id=6ad0da87de269131f9db3097 ts=2026-10-15T13:52:07.2720000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12111] _id=6ad0dabfde269131f9db38ca ts=2026-10-15T13:53:03.1120000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12112] _id=6ad0dabfde269131f9db38cb ts=2026-10-15T13:53:03.1120000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12152] _id=6ad0dafdde269131f9db4099 ts=2026-10-15T13:54:04.4000000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12153] _id=6ad0dafdde269131f9db409a ts=2026-10-15T13:54:04.4000000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 14m 
  - Evidence: 168h 14m: 6ab9a88e9a8420a1e6b56aed.jsonl[765] _id=6ac4fa9ade269131f9b12584 ts=2026-10-06T13:41:46.3040000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5632] _id=6ace387dde269131f9cef6e5 ts=2026-10-13T13:56:12.8710000Z; 45h 6m: 6ab9a88e9a8420a1e6b56aed.jsonl[9639] _id=6acfa9fbde269131f9d5482a ts=2026-10-14T16:12:42.3670000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12738] _id=6ad2245dde269131f9e37713 ts=2026-10-16T13:19:25.2860000Z; 26h 16m: 6ab9a88e9a8420a1e6b56aed.jsonl[5632] _id=6ace387dde269131f9cef6e5 ts=2026-10-13T13:56:12.8710000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[9639] _id=6acfa9fbde269131f9d5482a ts=2026-10-14T16:12:42.3670000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56aed.jsonl[4968] _id=6ac7a183de269131f9c156a6 ts=2026-10-08T13:58:25.9810000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4985] _id=6ace2f69de269131f9ce8fc1 ts=2026-10-13T13:17:29.0810000Z; 23h 40m: 6ab9a88e9a8420a1e6b56aed.jsonl[4422] _id=6ac64fbade269131f9ba31d9 ts=2026-10-07T13:57:13.5090000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4479] _id=6ac79cc0de269131f9c09195 ts=2026-10-08T13:38:06.8050000Z; 23h 25m: 6ab9a88e9a8420a1e6b56aed.jsonl[2105] _id=6ac4fe9cde269131f9b22b5a ts=2026-10-06T13:58:52.3840000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2137] _id=6ac647fbde269131f9b8e28c ts=2026-10-07T13:24:09.7560000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 349 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10075] _id=6ad0d369de269131f9da6a28 ts=2026-10-15T13:21:44.6330000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10114] _id=6ad0d369de269131f9da6a29 ts=2026-10-15T13:21:44.6330000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10615] _id=6ad0d4cfde269131f9da8f7e ts=2026-10-15T13:27:42.8560000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10616] _id=6ad0d4cfde269131f9da8f7f ts=2026-10-15T13:27:42.8560000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[11051] _id=6ad0d65ade269131f9dab55a ts=2026-10-15T13:34:17.8880000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[11052] _id=6ad0d65ade269131f9dab55b ts=2026-10-15T13:34:17.8880000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a88e9a8420a1e6b56aed.jsonl[4964] _id=6ac7a16ade269131f9c154f1 ts=2026-10-08T13:58:00.9010000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5134] _id=6ace3503de269131f9cecb54 ts=2026-10-13T13:41:22.9970000Z; 24h 1m: 6ab9a88e9a8420a1e6b56aed.jsonl[3818] _id=6ac64f0bde269131f9ba2477 ts=2026-10-07T13:54:18.2690000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4890] _id=6ac7a0d5de269131f9c1458c ts=2026-10-08T13:55:32.0850000Z; 23h 55m: 6ab9a88e9a8420a1e6b56aed.jsonl[1862] _id=6ac4fd1ede269131f9b1be03 ts=2026-10-06T13:52:30.3310000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[3215] _id=6ac64da4de269131f9b9f6bd ts=2026-10-07T13:48:19.5650000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.007s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[11951] _id=6ad0d9acde269131f9db156c ts=2026-10-15T13:48:27.3470000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[11952] _id=6ad0d9acde269131f9db156d ts=2026-10-15T13:48:27.3470000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[11991] _id=6ad0d9e3de269131f9db1d12 ts=2026-10-15T13:49:22.6820000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[11992] _id=6ad0d9e3de269131f9db1d13 ts=2026-10-15T13:49:22.6820000Z; 7ms: 6ab9a88e9a8420a1e6b56aed.jsonl[107] _id=6ac4f649de269131f9b060d3 ts=2026-10-06T13:23:20.6180000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[108] _id=6ac4f649de269131f9b060e4 ts=2026-10-06T13:23:20.6250000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a88e9a8420a1e6b56aed.jsonl[4977] _id=6ac7a18ede269131f9c15790 ts=2026-10-08T13:58:37.9060000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4987] _id=6ace2f64de269131f9ce8fae ts=2026-10-13T13:17:19.2200000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aed.jsonl[4472] _id=6ac65055de269131f9ba3c73 ts=2026-10-07T13:59:48.2890000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4478] _id=6ac79cc0de269131f9c09194 ts=2026-10-08T13:38:03.8490000Z; 23h 24m: 6ab9a88e9a8420a1e6b56aed.jsonl[2120] _id=6ac4fed8de269131f9b23868 ts=2026-10-06T13:59:51.5880000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2136] _id=6ac647fbde269131f9b8e28b ts=2026-10-07T13:24:06.2200000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 144h 7m 
  - Evidence: 144h 7m: 6ab9a88e9a8420a1e6b56aed.jsonl[4550] _id=6ac79ccdde269131f9c09436 ts=2026-10-08T13:38:19.2450000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[7262] _id=6acf8772de269131f9d3557c ts=2026-10-14T13:45:21.0760000Z; 23h 59m: 6ab9a88e9a8420a1e6b56aed.jsonl[1704] _id=6ac4fccbde269131f9b1ab07 ts=2026-10-06T13:51:04.7100000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[3341] _id=6ac64e31de269131f9ba0331 ts=2026-10-07T13:50:40.0640000Z; 23h 41m: 6ab9a88e9a8420a1e6b56aed.jsonl[4368] _id=6ac64fa4de269131f9ba300c ts=2026-10-07T13:56:50.7550000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4474] _id=6ac79cc1de269131f9c091af ts=2026-10-08T13:38:07.7190000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1421 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10000] _id=6ad0d35fde269131f9da694b ts=2026-10-15T13:21:33.9180000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[9763] _id=6ad0d35fde269131f9da694f ts=2026-10-15T13:21:33.9180000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10002] _id=6ad0d360de269131f9da695c ts=2026-10-15T13:21:33.9690000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10003] _id=6ad0d360de269131f9da695d ts=2026-10-15T13:21:33.9690000Z; 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[10004] _id=6ad0d360de269131f9da695f ts=2026-10-15T13:21:33.9830000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[10049] _id=6ad0d360de269131f9da6961 ts=2026-10-15T13:21:33.9830000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 54m 
  - Evidence: 167h 54m: 6ab9a88e9a8420a1e6b56aed.jsonl[3280] _id=6ac64de2de269131f9b9fb03 ts=2026-10-07T13:49:22.0160000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[7219] _id=6acf8732de269131f9d350b4 ts=2026-10-14T13:44:17.7200000Z; 23h 54m: 6ab9a88e9a8420a1e6b56aed.jsonl[1938] _id=6ac4fd85de269131f9b1d87a ts=2026-10-06T13:54:12.7150000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[3220] _id=6ac64da4de269131f9b9f6ba ts=2026-10-07T13:48:19.5600000Z; 23h 53m: 6ab9a88e9a8420a1e6b56aed.jsonl[9830] _id=6ad0d328de269131f9da6524 ts=2026-10-15T13:20:39.7180000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12599] _id=6ad22325de269131f9e35e73 ts=2026-10-16T13:14:13.3710000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.005s..0.027s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56aed.jsonl[3262] _id=6ac64ddade269131f9b9fa10 ts=2026-10-07T13:49:13.1490000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[3265] _id=6ac64ddade269131f9b9fa14 ts=2026-10-07T13:49:13.1540000Z; 9ms: 6ab9a88e9a8420a1e6b56aed.jsonl[9813] _id=6ad0d317de269131f9da6462 ts=2026-10-15T13:20:22.5010000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[9811] _id=6ad0d317de269131f9da646b ts=2026-10-15T13:20:22.5100000Z; 27ms: 6ab9a88e9a8420a1e6b56aed.jsonl[9801] _id=6ad0d30fde269131f9da63f2 ts=2026-10-15T13:20:14.5520000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[9796] _id=6ad0d30fde269131f9da63f4 ts=2026-10-15T13:20:14.5790000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 23m 
  - Evidence: 143h 23m: 6ab9a88e9a8420a1e6b56aed.jsonl[4774] _id=6ac79fa5de269131f9c111b5 ts=2026-10-08T13:50:27.8210000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5694] _id=6acf800ade269131f9d2d552 ts=2026-10-14T13:13:46.1550000Z; 24h 3m: 6ab9a88e9a8420a1e6b56aed.jsonl[3004] _id=6ac64d50de269131f9b9f055 ts=2026-10-07T13:46:55.5390000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4783] _id=6ac79f98de269131f9c10f4f ts=2026-10-08T13:50:15.6160000Z; 23h 26m: 6ab9a88e9a8420a1e6b56aed.jsonl[2126] _id=6ac4fedade269131f9b238a8 ts=2026-10-06T13:59:53.1270000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2240] _id=6ac64890de269131f9b901d5 ts=2026-10-07T13:26:39.7070000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.023s..0.044s shown 
  - Evidence: 23ms: 6ab9a88e9a8420a1e6b56aed.jsonl[2243] _id=6ac64899de269131f9b90373 ts=2026-10-07T13:26:48.1190000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2248] _id=6ac64899de269131f9b90377 ts=2026-10-07T13:26:48.1420000Z; 26ms: 6ab9a88e9a8420a1e6b56aed.jsonl[2122] _id=6ac4fed9de269131f9b23894 ts=2026-10-06T13:59:53.1010000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2126] _id=6ac4fedade269131f9b238a8 ts=2026-10-06T13:59:53.1270000Z; 44ms: 6ab9a88e9a8420a1e6b56aed.jsonl[2246] _id=6ac64899de269131f9b9036c ts=2026-10-07T13:26:48.0750000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2243] _id=6ac64899de269131f9b90373 ts=2026-10-07T13:26:48.1190000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 11m 
  - Evidence: 168h 11m: 6ab9a88e9a8420a1e6b56aed.jsonl[617] _id=6ac4f9fede269131f9b10413 ts=2026-10-06T13:39:09.4900000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5441] _id=6ace3724de269131f9cee410 ts=2026-10-13T13:50:27.7320000Z; 24h 10m: 6ab9a88e9a8420a1e6b56aed.jsonl[7024] _id=6acf868ade269131f9d345df ts=2026-10-14T13:41:29.9740000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12078] _id=6ad0da87de269131f9db3092 ts=2026-10-15T13:52:07.2480000Z; 23h 46m: 6ab9a88e9a8420a1e6b56aed.jsonl[5539] _id=6ace37aade269131f9ceebbe ts=2026-10-13T13:52:42.4550000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[6965] _id=6acf8612de269131f9d34012 ts=2026-10-14T13:39:30.2000000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 8m 
  - Evidence: 168h 8m: 6ab9a88e9a8420a1e6b56aed.jsonl[616] _id=6ac4f9fede269131f9b1041d ts=2026-10-06T13:39:09.5100000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5367] _id=6ace3694de269131f9cedbe2 ts=2026-10-13T13:48:04.6670000Z; 24h 9m: 6ab9a88e9a8420a1e6b56aed.jsonl[7028] _id=6acf868ade269131f9d345e9 ts=2026-10-14T13:41:30.0720000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12032] _id=6ad0da51de269131f9db2ac3 ts=2026-10-15T13:51:13.0260000Z; 23h 44m: 6ab9a88e9a8420a1e6b56aed.jsonl[5540] _id=6ace37aade269131f9ceebc0 ts=2026-10-13T13:52:42.4810000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[6889] _id=6acf85a4de269131f9d33b46 ts=2026-10-14T13:37:39.7800000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.042s..0.042s shown 
  - Evidence: 42ms: 6ab9a88e9a8420a1e6b56aed.jsonl[12224] _id=6ad0db62de269131f9db4d34 ts=2026-10-15T13:55:45.6080000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12228] _id=6ad0db62de269131f9db4d3a ts=2026-10-15T13:55:45.6500000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 20m 
  - Evidence: 144h 20m: 6ab9a88e9a8420a1e6b56aed.jsonl[2314] _id=6ac648e5de269131f9b917b6 ts=2026-10-07T13:28:04.2580000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5372] _id=6ace3696de269131f9cedbf3 ts=2026-10-13T13:48:06.5260000Z; 24h 10m: 6ab9a88e9a8420a1e6b56aed.jsonl[7019] _id=6acf866ade269131f9d34488 ts=2026-10-14T13:40:57.5540000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12031] _id=6ad0da4fde269131f9db2a94 ts=2026-10-15T13:51:11.2530000Z; 23h 48m: 6ab9a88e9a8420a1e6b56aed.jsonl[607] _id=6ac4f9f9de269131f9b102fb ts=2026-10-06T13:39:04.5390000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2311] _id=6ac648dede269131f9b91548 ts=2026-10-07T13:27:57.4370000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.004s..0.004s shown 
  - Evidence: 4ms: 6ab9a88e9a8420a1e6b56aed.jsonl[6957] _id=6acf860bde269131f9d33fbf ts=2026-10-14T13:39:23.5150000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[6951] _id=6acf860bde269131f9d33fc1 ts=2026-10-14T13:39:23.5190000Z; 4ms: 6ab9a88e9a8420a1e6b56aed.jsonl[6984] _id=6acf862bde269131f9d34159 ts=2026-10-14T13:39:55.4450000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[6983] _id=6acf862bde269131f9d3415b ts=2026-10-14T13:39:55.4490000Z; 4ms: 6ab9a88e9a8420a1e6b56aed.jsonl[7010] _id=6acf8661de269131f9d3442a ts=2026-10-14T13:40:48.6930000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[7012] _id=6acf8661de269131f9d3442e ts=2026-10-14T13:40:48.6970000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 10m 
  - Evidence: 168h 10m: 6ab9a88e9a8420a1e6b56aed.jsonl[610] _id=6ac4f9fbde269131f9b10381 ts=2026-10-06T13:39:06.7950000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[5407] _id=6ace36e4de269131f9cee01d ts=2026-10-13T13:49:24.6050000Z; 23h 46m: 6ab9a88e9a8420a1e6b56aed.jsonl[5485] _id=6ace374ede269131f9cee61f ts=2026-10-13T13:51:09.9260000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[6904] _id=6acf85b3de269131f9d33c11 ts=2026-10-14T13:37:55.4730000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 51m 
  - Evidence: 215h 51m: 6ab9a88e9a8420a1e6b56aed.jsonl[2306] _id=6ac648dade269131f9b91425 ts=2026-10-07T13:27:53.6340000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12743] _id=6ad22476de269131f9e37976 ts=2026-10-16T13:19:50.7200000Z; 14m 31s: 6ab9a88e9a8420a1e6b56aed.jsonl[12743] _id=6ad22476de269131f9e37976 ts=2026-10-16T13:19:50.7200000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[13751] _id=6ad227dede269131f9e3baa2 ts=2026-10-16T13:34:22.1520000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 39m 
  - Evidence: 119h 39m: 6ab9a88e9a8420a1e6b56aed.jsonl[4477] _id=6ac79cb0de269131f9c08e6a ts=2026-10-08T13:37:50.8940000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4981] _id=6ace2f4cde269131f9ce8f4b ts=2026-10-13T13:16:59.7380000Z; 24h 13m: 6ab9a88e9a8420a1e6b56aed.jsonl[2131] _id=6ac647ecde269131f9b8df98 ts=2026-10-07T13:23:55.5170000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4477] _id=6ac79cb0de269131f9c08e6a ts=2026-10-08T13:37:50.8940000Z; 23h 55m: 6ab9a88e9a8420a1e6b56aed.jsonl[9641] _id=6ad0d198de269131f9da5354 ts=2026-10-15T13:14:00.1390000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[12368] _id=6ad221fede269131f9e34e81 ts=2026-10-16T13:09:17.7630000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 39m 
  - Evidence: 119h 39m: 6ab9a88e9a8420a1e6b56aed.jsonl[4476] _id=6ac79cb0de269131f9c08e69 ts=2026-10-08T13:37:50.8940000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4980] _id=6ace2f4cde269131f9ce8f4a ts=2026-10-13T13:16:59.7380000Z; 24h 10m: 6ab9a88e9a8420a1e6b56aed.jsonl[2280] _id=6ac648bdde269131f9b90c97 ts=2026-10-07T13:27:24.3660000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4476] _id=6ac79cb0de269131f9c08e69 ts=2026-10-08T13:37:50.8940000Z; 23h 40m: 6ab9a88e9a8420a1e6b56aed.jsonl[769] _id=6ac4faedde269131f9b13226 ts=2026-10-06T13:43:09.4010000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2130] _id=6ac647ecde269131f9b8df97 ts=2026-10-07T13:23:55.5170000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a88e9a8420a1e6b56aed.jsonl[4978] _id=6ace2f4bde269131f9ce8f47 ts=2026-10-08T13:58:42.547Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4982] _id=6ace2f4fde269131f9ce8f53 ts=2026-10-13T13:17:02.7700000Z; 47h 42m: 6ab9a88e9a8420a1e6b56aed.jsonl[5650] _id=6ace38c5de269131f9cefa89 ts=2026-10-13T13:57:25.2240000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[11511] _id=6ad0d7b8de269131f9dad468 ts=2026-10-15T13:40:07.7560000Z; 24h 31m: 6ab9a88e9a8420a1e6b56aed.jsonl[2273] _id=6ac648bbde269131f9b90c10 ts=2026-10-07T13:27:22.3170000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4978] _id=6ace2f4bde269131f9ce8f47 ts=2026-10-08T13:58:42.547Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 35m 
  - Evidence: 119h 35m: 6ab9a88e9a8420a1e6b56aed.jsonl[4649] _id=6ac79daade269131f9c0bbed ts=2026-10-08T13:42:01.6590000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4988] _id=6ace2f64de269131f9ce8faf ts=2026-10-13T13:17:24.1490000Z; 23h 40m: 6ab9a88e9a8420a1e6b56aed.jsonl[4424] _id=6ac64fc0de269131f9ba3283 ts=2026-10-07T13:57:19.3960000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[4481] _id=6ac79cc0de269131f9c09197 ts=2026-10-08T13:38:06.8690000Z; 23h 24m: 6ab9a88e9a8420a1e6b56aed.jsonl[2116] _id=6ac4fec7de269131f9b23528 ts=2026-10-06T13:59:35.2800000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[2139] _id=6ac647fbde269131f9b8e28e ts=2026-10-07T13:24:09.8160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aed.jsonl[14062] _id=6ad229bbde269131f9e3df1f ts=2026-10-16T13:42:19.3220000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[14063] _id=6ad229bbde269131f9e3df20 ts=2026-10-16T13:42:19.3220000Z; 1ms: 6ab9a88e9a8420a1e6b56aed.jsonl[13604] _id=6ad22736de269131f9e3aea9 ts=2026-10-16T13:31:34.3060000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[13605] _id=6ad22736de269131f9e3aeaa ts=2026-10-16T13:31:34.3070000Z; 3ms: 6ab9a88e9a8420a1e6b56aed.jsonl[14218] _id=6ad22b06de269131f9e3fcf8 ts=2026-10-16T13:47:50.1800000Z -> 6ab9a88e9a8420a1e6b56aed.jsonl[14213] _id=6ad22b06de269131f9e3fcfa ts=2026-10-16T13:47:50.1830000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[461] _id=6ac4f92fde269131f9b0daeb ts=2026-10-06T13:35:42.8060000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[621] _id=6ac4fa0dde269131f9b10739 ts=2026-10-06T13:39:24.8310000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[2750] _id=6ac64b84de269131f9b9b97f ts=2026-10-07T13:39:16.0240000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 39 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[1092] _id=6ac4fc32de269131f9b17ace ts=2026-10-06T13:48:32.6640000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1207] _id=6ac4fc49de269131f9b182f8 ts=2026-10-06T13:48:53.9750000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1208] _id=6ac4fc49de269131f9b1830a ts=2026-10-06T13:48:55.0370000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 105 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[922] _id=6ac4fbc2de269131f9b15f03 ts=2026-10-06T13:46:40.9620000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[930] _id=6ac4fbc3de269131f9b15f0d ts=2026-10-06T13:46:41.1330000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[936] _id=6ac4fbc3de269131f9b15f16 ts=2026-10-06T13:46:41.1330000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[7028] _id=6acf868ade269131f9d345e9 ts=2026-10-14T13:41:30.0720000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[12228] _id=6ad0db62de269131f9db4d3a ts=2026-10-15T13:55:45.6500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[584] _id=6ac4f9a9de269131f9b0f80c ts=2026-10-06T13:37:44.3980000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[593] _id=6ac4f9acde269131f9b0f879 ts=2026-10-06T13:37:47.5910000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[12743] _id=6ad22476de269131f9e37976 ts=2026-10-16T13:19:50.7200000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[13751] _id=6ad227dede269131f9e3baa2 ts=2026-10-16T13:34:22.1520000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 132 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[1163] _id=6ac4fc41de269131f9b18014 ts=2026-10-06T13:48:47.3720000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1137] _id=6ac4fc44de269131f9b18141 ts=2026-10-06T13:48:51.3190000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1148] _id=6ac4fc45de269131f9b18166 ts=2026-10-06T13:48:51.5070000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 230 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[1002] _id=6ac4fc18de269131f9b172a4 ts=2026-10-06T13:48:06.1610000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1003] _id=6ac4fc18de269131f9b172a9 ts=2026-10-06T13:48:06.1610000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1004] _id=6ac4fc18de269131f9b172c7 ts=2026-10-06T13:48:06.1610000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 43 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[2122] _id=6ac4fed9de269131f9b23894 ts=2026-10-06T13:59:53.1010000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[2126] _id=6ac4fedade269131f9b238a8 ts=2026-10-06T13:59:53.1270000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[2240] _id=6ac64890de269131f9b901d5 ts=2026-10-07T13:26:39.7070000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[5417] _id=6ace36fede269131f9cee1e3 ts=2026-10-13T13:49:50.2730000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[5485] _id=6ace374ede269131f9cee61f ts=2026-10-13T13:51:09.9260000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[6909] _id=6acf85b8de269131f9d33c4f ts=2026-10-14T13:37:59.7070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 443 start, 436 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 35 unmatched 'BecameCameraCentered' (totals: 615 open, 619 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 33 unmatched 'BecameVisible' (totals: 677 open, 749 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 46 open, 43 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 13 unmatched 'argumentationToolOpen' (totals: 13 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 44 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 415 of 14319 adjacent _id pairs reverse in client time; worst 11.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56aed.jsonl[987] _id=6ac4fc26de269131f9b176e1 ts=2026-10-06T13:48:21.5210000Z`; `6ab9a88e9a8420a1e6b56aed.jsonl[1029] _id=6ac4fc26de269131f9b176ed ts=2026-10-06T13:48:10.0590000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.61s, min -429497.40s, max -0.24s over 14320 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56aed\coverage.yaml

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

### `InputEvent` — 6460 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1645); Unit 3 Dungeon Dev (1327); Unit 3 Dev (1068); Unit 4 Dev - Dungeon (887); Unit 4 Dev (512); Unit 5 Dev - Dungeon (465); Unit 1 Dev (347); Unit 5 Dev (163); Unit 4 Dev - Anderson Base (46)
- **Intervals:** median 0.52s (p5 0.04s / p95 5.96s, n=6459)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6460/6460 records)
    "pressed"  x6460
data.actionType  (string, 6460/6460 records)
    "Move"  x5094
    "Jump"  x629
    "Interact"  x595
    "Ascend"  x61
    "Hoverboard"  x51
    "Sprint"  x11
    "Pause"  x8
    "Map"  x7
    "SkipCinematic"  x4
data.key  (string, 6460/6460 records, 40 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6460/6460 records)
    "Player"  x5624
    "Drone"  x836
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2660 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1554); Unit 4 Dev (456); Unit 5 Dev - Dungeon (328); Unit 3 Dungeon Dev (322)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.22s, n=2659)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2660/2660 records)
    "BecameInvisible"  x749
    "BecameVisible"  x677
    "BecameCameraUncentered"  x619
    "BecameCameraCentered"  x615
data.pieceId  (string, 2660/2660 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2660/2660 records)
    1462 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2270 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (712); Unit 3 Dev (375); Unit 4 Dev (282); Unit 5 Dev (218); Unit 3 Dungeon Dev (208); Unit 1 Dev (196); Unit 4 Dev - Anderson Base (101); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (79)
- **eventKey:** present on 1391 of 2270 records
- **Intervals:** median 3.12s (p5 0.00s / p95 26.46s, n=2269)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1391; [conversationId, dialogueEventType] x879
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2270/2270 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2270/2270 records)
    "DialogueNodeEvent"  x1391
    "DialogueStartEvent"  x443
    "DialogueFinishEvent"  x436
data.nodeId  (number, 1391/2270 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1582 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (546); Unit 3 Dev (230); Unit 4 Dev (165); Unit 3 Dungeon Dev (148); Unit 1 Dev (137); Unit 5 Dev (109); Unit 4 Dev - Dungeon (104); Unit 5 Dev - Dungeon (87); Unit 4 Dev - Anderson Base (56)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.69s, n=1570)
- **Fields under `data`:**

```text
data.position  (object, 1582/1582 records)
data.position.x  (number, 1582/1582 records)
    numeric range -694.084 .. 1556.52 (621 unique)
data.position.y  (number, 1582/1582 records)
    numeric range -112.49 .. 222.245 (485 unique)
data.position.z  (number, 1582/1582 records)
    numeric range -1038.9 .. 1924.63 (623 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 434 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (131); Unit 4 Dev - Anderson Base (119); Unit 3 Dev (97); Unit 5 Dev (46); Unit 1 Dev (41)
- **Intervals:** median 0.82s (p5 0.03s / p95 11.72s, n=433)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 434/434 records)
    "argumentationNodeHoverEnd"  x195
    "argumentationNodeHoverStart"  x193
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 434/434 records)
    "Unit 2 – Watershed"  x131
    "Unit 4 - Flooding"  x119
    "Unit 3 - Pollution Upstream"  x97
    "Unit 5"  x46
    "Unit 1 - Argumentation Tutorial"  x26
    "Unit 1 - Freshwater"  x15
data.nodeName  (string, 434/434 records)
    "B"  x72
    "A"  x55
    "I"  x52
    "1"  x49
    "C"  x44
    "D"  x40
    "3"  x33
    "II"  x33
    "4"  x24
    "2"  x17
    "5"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 311 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (101); Unit 3 Dungeon Dev (65); Unit 2 Prod (Refactor) (57); Unit 4 Dev (25); Unit 5 Dev - Dungeon (19); Unit 3 Dev (13); Unit 5 Dev (12); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 6.74s (p5 0.61s / p95 254.00s, n=310)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 311/311 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 311/311 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 161 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (93); Unit 2 Prod (Refactor) (64); Unit 1 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 3.72s (p5 0.80s / p95 259.53s, n=160)
- **`data` key-set variants:** [actionType, featureUsed] x89; [actionType, featureUsed, location] x71; [actionType, featureUsed, legendName] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 161/161 records)
    "WaypointMoveEvent"  x64
    "MapOpenEvent"  x46
    "MapCloseEvent"  x43
    "WaypointSetEvent"  x7
    "Selected"  x1
data.featureUsed  (string, 161/161 records)
    "Map"  x89
    "Waypoint"  x71
    "Legend"  x1
data.legendName  (string, 1/161 records)
    "360 ft"  x1
data.location  (object, 71/161 records)
data.location.x  (number, 71/161 records)
    numeric range -355.965 .. 556.469 (59 unique)
data.location.y  (number, 71/161 records)
    numeric range -328.006 .. 332.77 (66 unique)
data.location.z  (number, 71/161 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 117 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (75); Unit 4 Dev (30); Unit 3 Dev (12)
- **Intervals:** median 0.94s (p5 0.15s / p95 29.83s, n=116)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x109; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/117 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/117 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 109/117 records)
    "RightDrag"  x57
    "LeftDrag"  x52
data.currentSoilType  (string, 109/117 records)
    "CLAYSAND"  x23
    "CLAY"  x21
    "SAND"  x21
    "SANDGRAVEL"  x16
    "CLAYROCK"  x15
    "GRAVEL"  x7
    "BEDROCK"  x6
data.isCorrectSelection  (string, 109/117 records)
    "false"  x83
    "true"  x26
data.waterLevelStatus  (string, 109/117 records)
    "Proper"  x48
    "TooHigh"  x46
    "TooLow"  x15
data.waterRetentionChange  (string, 109/117 records)
    "Increase"  x43
    "Decrease"  x40
    "NoChange"  x26
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 77 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 4 Dev (10); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 77 of 77 records
- **Intervals:** median 160.85s (p5 0.00s / p95 83534.53s, n=76)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 77/77 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x33
data.questID  (string, 77/77 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 77/77 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/77 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DaniEvent` — 42 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev - Dungeon (10); Unit 1 Dev (6); Unit 3 Dev (6)
- **Intervals:** median 1.95s (p5 0.01s / p95 86189.67s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "Close"  x21
    "Open"  x21
data.toolName  (string, 42/42 records, 34 empty-string)
    ""  x34
    "Settings"  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `WaterChamberEvent` — 29 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (29)
- **Intervals:** median 11.12s (p5 1.28s / p95 56.39s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "On"  x20
    "Off"  x9
data.floor  (string, 29/29 records)
    "3"  x13
    "4"  x11
    "2"  x3
    "1"  x2
data.machineNumber  (string, 29/29 records)
    "One"  x28
    "Two"  x1
data.machineType  (string, 29/29 records)
    "Condenser"  x16
    "Evaporator"  x6
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 29/29 records)
    "2"  x12
    "3"  x10
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 4 Dev (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 3 Dungeon Dev (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 535.38s (p5 8.99s / p95 86628.27s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (7); Transition (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 813.07s (p5 14.50s / p95 86759.47s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 22 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (10); Unit 2 Prod (Refactor) (6); Unit 3 Dev (3); Unit 5 Dev (2); Unit 1 Dev (1)
- **Intervals:** median 31.00s (p5 1.29s / p95 87037.27s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "submitAnswerEvent"  x22
data.answerSubmitted  (string, 22/22 records)
    16 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 22/22 records)
    "Unit 4 - Flooding"  x10
    "Unit 2 – Watershed"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 18 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (18)
- **Intervals:** median 4.11s (p5 1.90s / p95 72.92s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "ChangeCanister"  x18
data.canisterType  (string, 18/18 records)
    "Clay"  x11
    "Bedrock"  x5
    "Gravel"  x1
    "Sand"  x1
data.floor  (string, 18/18 records)
    "5"  x16
    "4"  x2
data.machine  (string, 18/18 records)
    "1"  x17
    "2"  x1
data.row  (string, 18/18 records)
    "BottomRow"  x10
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); MainMenu (1); Transition (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 1339.26s (p5 17.12s / p95 261970.72s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 14 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (14)
- **Intervals:** median 2.38s (p5 0.81s / p95 20.36s, n=13)
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x7
data.boxId  (string, 14/14 records)
    "0"  x8
    "1"  x4
    "2"  x2
data.soilType  (string, 14/14 records)
    "Gravel"  x8
    "Clay"  x3
    "Sand"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 230.22s (p5 0.06s / p95 294323.84s, n=13)
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

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (8); Unit 2 Prod (Refactor) (4); Unit 1 Dev (1)
- **Intervals:** median 22.00s (p5 1.39s / p95 319521.07s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x13
data.argumentationTitle  (string, 13/13 records)
    "Unit 3 - Pollution Upstream"  x8
    "Unit 2 – Watershed"  x4
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - Pollution Site Data"  x7
    "BackingInfoPanel - Waterfall Data"  x3
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 12 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (12)
- **Intervals:** median 76806.94s (p5 312.45s / p95 258992.11s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    true  x12
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 7 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (7)
- **Intervals:** median 1.83s (p5 1.27s / p95 4.95s, n=6)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x6; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "optionSelected"  x6
    "DesignSubmitted"  x1
data.designSelections  (object, 1/7 records)
data.designSelections.glassRoofTemperature  (string, 1/7 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/7 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/7 records)
    "Tilted In"  x1
data.featureUsed  (string, 7/7 records)
    "RoofStyle"  x3
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 6/7 records)
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 128496.21s (p5 15896.21s / p95 539177.02s, n=4)
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

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 871.43s (p5 87.93s / p95 699492.52s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x3
    "Open"  x1
data.chatID  (string, 4/4 records)
    "NA"  x3
    "[19-48, 19-58, 19-46, 19-60, 19-61]"  x1
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
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (75 records)
- `TerasGardenBox` data.actionType: "" (7x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (64x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (71x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*