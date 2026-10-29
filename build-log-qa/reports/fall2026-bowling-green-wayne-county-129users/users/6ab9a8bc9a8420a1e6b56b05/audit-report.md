# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b05

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b05
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b05.jsonl
- **Records:** 14526 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b05
- **Time span:** 2026-10-05T15:16:00.028000+00:00 .. 2026-10-16T15:54:37.354000+00:00 (264h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b05\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14526 records, 11 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 97 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PlayerPositionEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4941 | 34.01 | 1 | 9 | 0 | 2026-10-05T15:16:11.957000+00:00 | 2026-10-16T15:54:37.354000+00:00 | 264h 38m |
| PuzzlePieceVisibleEvent | 3038 | 20.91 | 1 | 4 | 0 | 2026-10-08T15:23:43.701000+00:00 | 2026-10-16T15:06:09.801000+00:00 | 191h 42m |
| PlayerPositionEvent | 2724 | 18.75 | 1 | 9 | 0 | 2026-10-05T15:16:08.539000+00:00 | 2026-10-16T15:54:32.676000+00:00 | 264h 38m |
| DialogueEvent | 2572 | 17.71 | 1 | 9 | 1613 | 2026-10-05T15:16:28.737000+00:00 | 2026-10-16T15:54:29.995000+00:00 | 264h 38m |
| argumentationNodeEvent | 411 | 2.83 | 1 | 5 | 0 | 2026-10-07T15:35:02.208000+00:00 | 2026-10-16T15:37:43.172000+00:00 | 216h 2m |
| ObjectInterEvent | 291 | 2.0 | 1 | 9 | 0 | 2026-10-05T15:23:54.885000+00:00 | 2026-10-16T15:54:37.353000+00:00 | 264h 30m |
| questEvent | 100 | 0.69 | 1 | 9 | 100 | 2026-10-05T15:16:28.710000+00:00 | 2026-10-16T15:48:55.549000+00:00 | 264h 32m |
| Soil Key Puzzle | 87 | 0.6 | 1 | 3 | 0 | 2026-10-08T15:32:42.697000+00:00 | 2026-10-16T02:15:28.704000+00:00 | 178h 42m |
| TopographicMapEvent | 85 | 0.59 | 1 | 2 | 0 | 2026-10-08T15:24:31.790000+00:00 | 2026-10-16T02:02:41.979000+00:00 | 178h 38m |
| DEBUGMenu | 48 | 0.33 | 1 | 9 | 0 | 2026-10-05T15:16:08.522000+00:00 | 2026-10-16T15:00:33.331000+00:00 | 263h 44m |
| gameWindowFocusEvent | 40 | 0.28 | 1 | 7 | 0 | 2026-10-05T15:16:00.028000+00:00 | 2026-10-16T15:52:04.586000+00:00 | 264h 36m |
| WaterChamberEvent | 38 | 0.26 | 1 | 1 | 0 | 2026-10-16T15:04:38.206000+00:00 | 2026-10-16T15:26:44.260000+00:00 | 22m 6s |
| gameWindowUnfocusEvent | 23 | 0.16 | 1 | 6 | 0 | 2026-10-07T15:42:27.925000+00:00 | 2026-10-16T15:52:03.396000+00:00 | 216h 9m |
| gameStartEvent | 22 | 0.15 | 1 | 1 | 0 | 2026-10-05T15:16:00.029000+00:00 | 2026-10-16T15:00:26.523000+00:00 | 263h 44m |
| argumentationAnswerEvent | 20 | 0.14 | 1 | 5 | 0 | 2026-10-07T15:35:30.526000+00:00 | 2026-10-16T15:37:48.875000+00:00 | 216h 2m |
| TerasGardenBox | 19 | 0.13 | 1 | 1 | 0 | 2026-10-16T11:29:40.489000+00:00 | 2026-10-16T11:35:14.458000+00:00 | 5m 33s |
| chatEvent | 16 | 0.11 | 1 | 3 | 0 | 2026-10-14T22:27:15.072000+00:00 | 2026-10-16T15:28:06.853000+00:00 | 41h 0m |
| argumentationEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-10-07T15:34:55.815000+00:00 | 2026-10-16T15:37:48.916000+00:00 | 216h 2m |
| soilMachine | 12 | 0.08 | 1 | 1 | 0 | 2026-10-16T02:35:43.486000+00:00 | 2026-10-16T02:53:25.754000+00:00 | 17m 42s |
| DaniEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-14T22:14:48.884000+00:00 | 2026-10-14T22:27:14.729000+00:00 | 12m 25s |
| SolarStillDesignEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-16T15:45:19.934000+00:00 | 2026-10-16T15:46:17.171000+00:00 | 57.2s |
| argumentationToolEvent | 6 | 0.04 | 1 | 3 | 0 | 2026-10-07T15:34:48.028000+00:00 | 2026-10-16T15:36:38.271000+00:00 | 216h 1m |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-07T15:42:46.357000+00:00 | 2026-10-16T15:54:37.332000+00:00 | 216h 11m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 260.751s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 67992.501s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.268s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 18.045s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.06s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.667s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 6.902s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.095s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 19.509s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 105.163s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2.106s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 12494.481s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1157.415s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 543.952s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 24.785s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.0x vs baseline. 
  - Observed: 48 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; upArrow 
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
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; B,2,II; C,2,II; C,3,4,II; C,3,II; C,D,2,II; C,D,3,4,II; C,D,3,II; C,D,A,2,II; D,2,II; D,A,2,II; II 
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
  - Observed: Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 8.0x vs baseline. 
  - Observed: 16 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-32, 10-33, 10-195, 11-12, 11-13, 11-14]; [10-38, 10-39, 10-210, 10-215, 10-216, 10-39]; [10-39, 10-210, 10-215, 10-216, 10-39]; [10-39, 10-40, 10-212, 10-39, 10-211, 10-217]; [10-6, 10-7, 10-8, 10-10, 10-9, 10-11]; [11-26, 11-25, 11-27, 11-26, 11-26, 11-27]; [11-26, 11-27, 11-27, 11-29, 11-29] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 22 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[235] _id=6ac3c19ade269131f9ad27f9 ts=2026-10-05T15:26:17.4890000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[377] _id=6ac3c343de269131f9ad3e33 ts=2026-10-05T15:33:22.5900000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[594] _id=6ac3c493de269131f9ad54d5 ts=2026-10-05T15:38:58.4660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[2] _id=6ac3bf31de269131f9ace745 ts=2026-10-05T15:16:00.0290000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[725] _id=6ac51623de269131f9b48dd1 ts=2026-10-06T15:39:15.1680000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[887] _id=6ac6625dde269131f9bb991d ts=2026-10-07T15:16:44.1390000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 40 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 40} 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1] _id=6ac3bf31de269131f9ace743 ts=2026-10-05T15:16:00.0280000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[724] _id=6ac51623de269131f9b48dcc ts=2026-10-06T15:39:15.1670000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[886] _id=6ac6625dde269131f9bb991c ts=2026-10-07T15:16:44.1390000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1411] _id=6ac66865de269131f9bc1a75 ts=2026-10-07T15:42:27.9250000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1416] _id=6ac6686bde269131f9bc1abd ts=2026-10-07T15:42:34.8670000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1475] _id=6ac7b48ede269131f9c3840f ts=2026-10-07T15:47:27.599Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 85 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1619] _id=6ac7b5b0de269131f9c3a0ce ts=2026-10-08T15:24:31.7900000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1632] _id=6ac7b5c6de269131f9c3a357 ts=2026-10-08T15:24:53.1210000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[2928] _id=6ac7b97fde269131f9c41251 ts=2026-10-08T15:40:47.0720000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4940 | 0.0 | 1.268 | 192.855 | 16.311 | 429648.29 | 0.31 | 121 | 14 |
| PuzzlePieceVisibleEvent | 3037 | 0.0 | 0.06 | 227.246 | 2.232 | 517056.949 | 0.26 | 1435 | 7 |
| PlayerPositionEvent | 2710 | 0.0 | 10.001 | 338.914 | 10.101 | 429627.185 | 0.18 | 5 | 10 |
| DialogueEvent | 2571 | 0.0 | 4.593 | 370.549 | 41.111 | 429830.387 | 0.16 | 716 | 12 |
| argumentationNodeEvent | 410 | 0.003 | 0.792 | 1896.978 | 8.891 | 606108.023 | 0.03 | 54 | 5 |
| ObjectInterEvent | 290 | 0.0 | 18.045 | 3283.595 | 669.484 | 512411.242 | 0.02 | 5 | 16 |
| questEvent | 99 | 0.0 | 239.82 | 9619.665 | 62867.961 | 429929.834 | 0.01 | 17 | 20 |
| Soil Key Puzzle | 86 | 0.149 | 1.667 | 7481.0 | 207.284 | 512408.085 | 0.01 | 0 | 4 |
| TopographicMapEvent | 84 | 0.019 | 7.095 | 7655.836 | 20375.185 | 430031.036 | 0.01 | 6 | 8 |
| DEBUGMenu | 47 | 6.97 | 260.751 | 20201.379 | 84996.943 | 431128.448 | 0.0 | 0 | 20 |
| gameWindowFocusEvent | 39 | 2.872 | 1157.415 | 24424.732 | 85323.589 | 431161.741 | 0.0 | 0 | 24 |
| WaterChamberEvent | 37 | 0.674 | 25.012 | 35.839 | 90.157 | 122.047 | 1.67 | 0 | 0 |
| gameWindowUnfocusEvent | 22 | 3.095 | 543.952 | 35371.612 | 86206.264 | 517700.11 | 0.0 | 0 | 10 |
| gameStartEvent | 21 | 111.873 | 12494.481 | 45212.69 | 87795.139 | 431161.741 | 0.0 | 0 | 19 |
| argumentationAnswerEvent | 19 | 1.495 | 19.509 | 40933.597 | 136250.548 | 606179.275 | 0.0 | 0 | 4 |
| TerasGardenBox | 18 | 1.128 | 3.665 | 18.554 | 58.735 | 149.3 | 3.23 | 0 | 0 |
| chatEvent | 15 | 0.554 | 2.106 | 9843.452 | 44937.426 | 145932.601 | 0.01 | 0 | 2 |
| argumentationEvent | 13 | 0.026 | 111.368 | 59828.7 | 292825.154 | 606095.121 | 0.0 | 2 | 4 |
| soilMachine | 11 | 4.161 | 24.785 | 96.57 | 338.784 | 455.664 | 0.62 | 0 | 0 |
| DaniEvent | 5 | 1.634 | 14.666 | 149.169 | 560.484 | 692.333 | 0.4 | 0 | 1 |
| SolarStillDesignEvent | 5 | 2.93 | 6.902 | 11.447 | 29.016 | 33.633 | 5.24 | 0 | 0 |
| argumentationToolEvent | 5 | 2.59 | 105.163 | 155542.049 | 519282.495 | 606272.56 | 0.0 | 0 | 2 |
| EndOfUnit | 4 | 15043.561 | 67992.501 | 194577.744 | 548418.508 | 627282.412 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 8 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[2598] _id=6ac7b72dde269131f9c3dc28 ts=2026-10-08T15:30:52.5360000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[2599] _id=6ac7b72dde269131f9c3dc29 ts=2026-10-08T15:30:52.5360000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[3017] _id=6ace48dbde269131f9cf04c2 ts=2026-10-13T15:06:01.5840000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[3018] _id=6ace48dbde269131f9cf04c3 ts=2026-10-13T15:06:01.5840000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[3789] _id=6acf878bde269131f9d35831 ts=2026-10-14T13:45:45.3930000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[3790] _id=6acf878bde269131f9d35832 ts=2026-10-14T13:45:45.3930000Z`
- **WARNING / Medium** `PlayerPositionEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[3907] _id=6acf8864de269131f9d36e50 ts=2026-10-14T13:49:15.8020000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[3909] _id=6acf888cde269131f9d37426 ts=2026-10-14T13:49:15.8020000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 78 group(s), 115 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1595] _id=6ac7b584de269131f9c39bfa ts=2026-10-08T15:23:46.4720000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[1596] _id=6ac7b584de269131f9c39bfc ts=2026-10-08T15:23:46.4720000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1599] _id=6ac7b586de269131f9c39c21 ts=2026-10-08T15:23:47.9580000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[1601] _id=6ac7b586de269131f9c39c29 ts=2026-10-08T15:23:47.9580000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1648] _id=6ac7b5ebde269131f9c3a7e7 ts=2026-10-08T15:25:30.0900000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[1653] _id=6ac7b5ebde269131f9c3a7f1 ts=2026-10-08T15:25:30.0900000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1420] _id=6ac668e8de269131f9bc2218 ts=? == 6ab9a8bc9a8420a1e6b56b05.jsonl[8796] _id=6ad14c5bde269131f9e1b0fb ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[14254] _id=6ad24518de269131f9e5568d ts=2026-10-16T15:39:03.6470000Z == 6ab9a8bc9a8420a1e6b56b05.jsonl[14255] _id=6ad24518de269131f9e5568e ts=2026-10-16T15:39:03.6470000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[167] _id=6ac3c10bde269131f9ad1b41 ts=2026-10-05T15:23:54.8850000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[168] _id=6ac3c10bde269131f9ad1b49 ts=2026-10-05T15:23:54.8900000Z`; `15ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[788] _id=6ac5167cde269131f9b49848 ts=2026-10-06T15:40:44.0290000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[789] _id=6ac5167cde269131f9b49854 ts=2026-10-06T15:40:44.0440000Z`; `4ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[914] _id=6ac662e3de269131f9bb9a09 ts=2026-10-07T15:18:58.2790000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[910] _id=6ac662e3de269131f9bb9a0f ts=2026-10-07T15:18:58.2830000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `796ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[3456] _id=6ace4e87de269131f9cf21f1 ts=2026-10-13T15:30:14.8940000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[3457] _id=6ace4e88de269131f9cf21f9 ts=2026-10-13T15:30:15.6900000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[7804] _id=6ad0efbbde269131f9dc7e7c ts=2026-10-15T15:22:34.8190000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[7807] _id=6ad0efbbde269131f9dc7e7f ts=2026-10-15T15:22:34.8540000Z`; `26ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12590] _id=6ad209a9de269131f9e346e1 ts=2026-10-16T11:25:28.3970000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[12593] _id=6ad209a9de269131f9e346e4 ts=2026-10-16T11:25:28.4230000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `567ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[1220] _id=6ac66729de269131f9bc0554 ts=2026-10-07T15:37:12.5290000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[1221] _id=6ac6672ade269131f9bc0563 ts=2026-10-07T15:37:13.0960000Z`; `335ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[7738] _id=6ad0ef68de269131f9dc7940 ts=2026-10-15T15:21:11.9820000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[7740] _id=6ad0ef69de269131f9dc7946 ts=2026-10-15T15:21:12.3170000Z`; `864ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[7741] _id=6ad0ef6fde269131f9dc7976 ts=2026-10-15T15:21:18.5380000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[7743] _id=6ad0ef70de269131f9dc798b ts=2026-10-15T15:21:19.4020000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[14414] _id=6ad24723de269131f9e5629c ts=2026-10-16T15:47:46.8540000Z ~ 6ab9a8bc9a8420a1e6b56b05.jsonl[14415] _id=6ad24723de269131f9e5629e ts=2026-10-16T15:47:46.8580000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1480] _id=6ac7b4afde269131f9c386ef ts=2026-10-08T15:20:14.9680000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3009] _id=6ace48c8de269131f9cf046a ts=2026-10-13T15:05:43.4160000Z; 24h 23m: 6ab9a8bc9a8420a1e6b56b05.jsonl[6] _id=6ac3bf39de269131f9ace771 ts=2026-10-05T15:16:08.5220000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[728] _id=6ac51636de269131f9b48f73 ts=2026-10-06T15:39:34.3420000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b05.jsonl[728] _id=6ac51636de269131f9b48f73 ts=2026-10-06T15:39:34.3420000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[885] _id=6ac6625dde269131f9bb991a ts=2026-10-07T15:16:43.9700000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 11m 32s 
  - Evidence: 11m 32s: 6ab9a8bc9a8420a1e6b56b05.jsonl[6608] _id=6acffedede269131f9d98ec6 ts=2026-10-14T22:14:53.0070000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7273] _id=6ad00192de269131f9d994be ts=2026-10-14T22:26:25.3400000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2998] _id=6ac7ba77de269131f9c41d9f ts=2026-10-08T15:44:54.3890000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3053] _id=6ace497dde269131f9cf074b ts=2026-10-13T15:08:44.7760000Z; 23h 52m: 6ab9a8bc9a8420a1e6b56b05.jsonl[718] _id=6ac3c68dde269131f9ad76af ts=2026-10-05T15:47:24.4040000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[729] _id=6ac5163ade269131f9b48fe3 ts=2026-10-06T15:39:36.6020000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1471] _id=6ac66980de269131f9bc2ef8 ts=2026-10-07T15:47:11.4470000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[1491] _id=6ac7b4d5de269131f9c38a7f ts=2026-10-08T15:20:52.3030000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 716 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12415] _id=6ad208f0de269131f9e34597 ts=2026-10-16T11:22:22.8680000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12444] _id=6ad208f0de269131f9e34598 ts=2026-10-16T11:22:22.8680000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12437] _id=6ad20901de269131f9e345bb ts=2026-10-16T11:22:39.6230000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12438] _id=6ad20901de269131f9e345bc ts=2026-10-16T11:22:39.6230000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12556] _id=6ad20986de269131f9e34678 ts=2026-10-16T11:24:52.7430000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12557] _id=6ad20986de269131f9e34679 ts=2026-10-16T11:24:52.7430000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 174h 14m 
  - Evidence: 174h 14m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1419] _id=6ac66877de269131f9bc1b3f ts=2026-10-07T15:42:46.3570000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[6257] _id=6acffac9de269131f9d988e2 ts=2026-10-14T21:57:28.7690000Z; 28h 12m: 6ab9a8bc9a8420a1e6b56b05.jsonl[6257] _id=6acffac9de269131f9d988e2 ts=2026-10-14T21:57:28.7690000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[10018] _id=6ad1875cde269131f9e2a81e ts=2026-10-16T02:09:31.8180000Z; 9h 34m: 6ab9a8bc9a8420a1e6b56b05.jsonl[10018] _id=6ad1875cde269131f9e2a81e ts=2026-10-16T02:09:31.8180000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[13013] _id=6ad20dfbde269131f9e34af6 ts=2026-10-16T11:43:53.7710000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b05.jsonl[3006] _id=6ac7ba8ade269131f9c41e6a ts=2026-10-08T15:45:13.2910000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3016] _id=6ace48dbde269131f9cf04c1 ts=2026-10-13T15:06:01.5810000Z; 23h 55m: 6ab9a8bc9a8420a1e6b56b05.jsonl[687] _id=6ac3c5d7de269131f9ad6819 ts=2026-10-05T15:44:22.6770000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[738] _id=6ac5164ade269131f9b49190 ts=2026-10-06T15:39:54.0400000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b05.jsonl[824] _id=6ac516fade269131f9b4a2df ts=2026-10-06T15:42:50.4120000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[892] _id=6ac6627ade269131f9bb9932 ts=2026-10-07T15:17:13.7450000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 121 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[2598] _id=6ac7b72dde269131f9c3dc28 ts=2026-10-08T15:30:52.5360000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[2599] _id=6ac7b72dde269131f9c3dc29 ts=2026-10-08T15:30:52.5360000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[3017] _id=6ace48dbde269131f9cf04c2 ts=2026-10-13T15:06:01.5840000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3018] _id=6ace48dbde269131f9cf04c3 ts=2026-10-13T15:06:01.5840000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[3018] _id=6ace48dbde269131f9cf04c3 ts=2026-10-13T15:06:01.5840000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3019] _id=6ace48dbde269131f9cf04c4 ts=2026-10-13T15:06:01.5840000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 142h 20m 
  - Evidence: 142h 20m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2763] _id=6ac7b79bde269131f9c3e8e0 ts=2026-10-08T15:32:42.7020000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3971] _id=6acf8937de269131f9d38a5e ts=2026-10-14T13:52:53.9440000Z; 23h 56m: 6ab9a8bc9a8420a1e6b56b05.jsonl[688] _id=6ac3c5dade269131f9ad6843 ts=2026-10-05T15:44:25.1010000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[788] _id=6ac5167cde269131f9b49848 ts=2026-10-06T15:40:44.0290000Z; 23h 39m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1391] _id=6ac6684ade269131f9bc18fe ts=2026-10-07T15:42:01.5950000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[1507] _id=6ac7b4f9de269131f9c38e2b ts=2026-10-08T15:21:29.1310000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12000] _id=6ad2069ede269131f9e3424c ts=2026-10-16T11:12:29.2270000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12001] _id=6ad2069ede269131f9e3424d ts=2026-10-16T11:12:29.2270000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12302] _id=6ad207e0de269131f9e34494 ts=2026-10-16T11:17:50.9130000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12303] _id=6ad207e0de269131f9e34495 ts=2026-10-16T11:17:50.9130000Z; 4ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[914] _id=6ac662e3de269131f9bb9a09 ts=2026-10-07T15:18:58.2790000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[910] _id=6ac662e3de269131f9bb9a0f ts=2026-10-07T15:18:58.2830000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b05.jsonl[3008] _id=6ac7ba95de269131f9c41ec0 ts=2026-10-08T15:45:25.1830000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3015] _id=6ace48dbde269131f9cf04c0 ts=2026-10-13T15:05:52.3680000Z; 23h 51m: 6ab9a8bc9a8420a1e6b56b05.jsonl[722] _id=6ac3c6acde269131f9ad7847 ts=2026-10-05T15:47:55.5570000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[732] _id=6ac51639de269131f9b48fc6 ts=2026-10-06T15:39:34.3680000Z; 23h 32m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1474] _id=6ac6698dde269131f9bc2ffb ts=2026-10-07T15:47:24.1980000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[1482] _id=6ac7b4b3de269131f9c38731 ts=2026-10-08T15:20:14.9880000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[10019] _id=6ad1875dde269131f9e2a822 ts=2026-10-16T02:09:32.2930000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[10024] _id=6ad18769de269131f9e2a84d ts=2026-10-16T02:09:32.293Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[3907] _id=6acf8864de269131f9d36e50 ts=2026-10-14T13:49:15.8020000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3909] _id=6acf888cde269131f9d37426 ts=2026-10-14T13:49:15.8020000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[5553] _id=6acfa0e2de269131f9d4bff0 ts=2026-10-14T15:33:53.9990000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[5559] _id=6acfa12dde269131f9d4c34a ts=2026-10-14T15:33:53.999Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2694] _id=6ac7b753de269131f9c3e0e6 ts=2026-10-08T15:31:29.3050000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[4134] _id=6acf9b12de269131f9d45f61 ts=2026-10-14T15:09:06.2540000Z; 24h 13m: 6ab9a8bc9a8420a1e6b56b05.jsonl[5286] _id=6acf9d4dde269131f9d48f90 ts=2026-10-14T15:18:35.3850000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[8043] _id=6ad0f1efde269131f9dca12d ts=2026-10-15T15:31:57.9520000Z; 8h 42m: 6ab9a8bc9a8420a1e6b56b05.jsonl[10475] _id=6ad18965de269131f9e2b26f ts=2026-10-16T02:18:11.6270000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[11641] _id=6ad203d0de269131f9e33fa0 ts=2026-10-16T11:00:30.2840000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1435 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[10043] _id=6ad188efde269131f9e2ae6d ts=2026-10-16T02:16:13.2150000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[10183] _id=6ad188efde269131f9e2ae6f ts=2026-10-16T02:16:13.2150000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[10091] _id=6ad188dbde269131f9e2add6 ts=2026-10-16T02:15:53.4430000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[10092] _id=6ad188dbde269131f9e2add8 ts=2026-10-16T02:15:53.4430000Z; 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[10112] _id=6ad188c7de269131f9e2ad5c ts=2026-10-16T02:15:33.5310000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[10113] _id=6ad188c7de269131f9e2ad5d ts=2026-10-16T02:15:33.5310000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 142h 20m 
  - Evidence: 142h 20m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2766] _id=6ac7b79ede269131f9c3e92a ts=2026-10-08T15:32:45.8540000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3970] _id=6acf8936de269131f9d38a5c ts=2026-10-14T13:52:53.9390000Z; 24h 18m: 6ab9a8bc9a8420a1e6b56b05.jsonl[4095] _id=6acf9ab0de269131f9d45798 ts=2026-10-14T15:07:27.5900000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7905] _id=6ad0f094de269131f9dc8b6a ts=2026-10-15T15:26:11.5300000Z; 10h 43m: 6ab9a8bc9a8420a1e6b56b05.jsonl[8031] _id=6ad0f1c3de269131f9dc9fa3 ts=2026-10-15T15:31:14.3820000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[10098] _id=6ad188adde269131f9e2acdf ts=2026-10-16T02:15:09.0790000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2990] _id=6ac7ba55de269131f9c41c97 ts=2026-10-08T15:44:20.8330000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3099] _id=6ace4a24de269131f9cf08f1 ts=2026-10-13T15:11:31.8690000Z; 23h 45m: 6ab9a8bc9a8420a1e6b56b05.jsonl[3667] _id=6ace5190de269131f9cf3f7c ts=2026-10-13T15:43:12.0490000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[5474] _id=6acf9f9ede269131f9d4b232 ts=2026-10-14T15:28:29.6420000Z; 16h 46m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7334] _id=6ad00237de269131f9d995fb ts=2026-10-14T22:29:10.7320000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7641] _id=6ad0ee0ede269131f9dc6340 ts=2026-10-15T15:15:25.4810000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.019s..0.023s shown 
  - Evidence: 19ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[2932] _id=6ac7b993de269131f9c413d3 ts=2026-10-08T15:41:06.2290000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[2936] _id=6ac7b993de269131f9c413d7 ts=2026-10-08T15:41:06.2480000Z; 22ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[3113] _id=6ace4a5ade269131f9cf0950 ts=2026-10-13T15:12:25.4680000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3107] _id=6ace4a5ade269131f9cf0952 ts=2026-10-13T15:12:25.4900000Z; 23ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[3326] _id=6ace4cf9de269131f9cf1676 ts=2026-10-13T15:23:36.3510000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3327] _id=6ace4cf9de269131f9cf1678 ts=2026-10-13T15:23:36.3740000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 22m 
  - Evidence: 168h 22m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1261] _id=6ac6676dde269131f9bc08b1 ts=2026-10-07T15:38:20.5500000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[6134] _id=6acfa750de269131f9d51824 ts=2026-10-14T16:01:19.8250000Z; 23h 20m: 6ab9a8bc9a8420a1e6b56b05.jsonl[6134] _id=6acfa750de269131f9d51824 ts=2026-10-14T16:01:19.8250000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7783] _id=6ad0ef94de269131f9dc7bcc ts=2026-10-15T15:21:56.0700000Z; 19h 59m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7803] _id=6ad0efbbde269131f9dc7e78 ts=2026-10-15T15:22:34.7960000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12414] _id=6ad208f0de269131f9e34595 ts=2026-10-16T11:22:22.8380000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 21m 
  - Evidence: 168h 21m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1256] _id=6ac6676dde269131f9bc08b5 ts=2026-10-07T15:38:20.5840000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[6098] _id=6acfa6fcde269131f9d5106a ts=2026-10-14T15:59:55.7050000Z; 23h 19m: 6ab9a8bc9a8420a1e6b56b05.jsonl[6137] _id=6acfa750de269131f9d51829 ts=2026-10-14T16:01:19.8540000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7726] _id=6ad0ef5bde269131f9dc786a ts=2026-10-15T15:20:58.3630000Z; 19h 57m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7807] _id=6ad0efbbde269131f9dc7e7f ts=2026-10-15T15:22:34.8540000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12353] _id=6ad2087dde269131f9e34504 ts=2026-10-16T11:20:28.0060000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.035s shown 
  - Evidence: 26ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12590] _id=6ad209a9de269131f9e346e1 ts=2026-10-16T11:25:28.3970000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12593] _id=6ad209a9de269131f9e346e4 ts=2026-10-16T11:25:28.4230000Z; 35ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[7804] _id=6ad0efbbde269131f9dc7e7c ts=2026-10-15T15:22:34.8190000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7807] _id=6ad0efbbde269131f9dc7e7f ts=2026-10-15T15:22:34.8540000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 168h 21m 
  - Evidence: 168h 21m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1259] _id=6ac66769de269131f9bc0899 ts=2026-10-07T15:38:16.5350000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[6102] _id=6acfa705de269131f9d510da ts=2026-10-14T16:00:04.5580000Z; 19h 57m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7795] _id=6ad0efb5de269131f9dc7de6 ts=2026-10-15T15:22:29.0870000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12354] _id=6ad2087ede269131f9e34509 ts=2026-10-16T11:20:29.0800000Z; 16h 53m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7296] _id=6ad001c1de269131f9d9950e ts=2026-10-14T22:27:12.0380000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[7723] _id=6ad0ef59de269131f9dc7851 ts=2026-10-15T15:20:56.9580000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 54 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12488] _id=6ad20936de269131f9e345f7 ts=2026-10-16T11:23:33.2580000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12481] _id=6ad20936de269131f9e345f9 ts=2026-10-16T11:23:33.2610000Z; 4ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12416] _id=6ad208cede269131f9e34567 ts=2026-10-16T11:21:49.1840000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12417] _id=6ad208cede269131f9e34569 ts=2026-10-16T11:21:49.1880000Z; 5ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[12409] _id=6ad208e0de269131f9e3457b ts=2026-10-16T11:22:07.5330000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[12423] _id=6ad208e1de269131f9e3457d ts=2026-10-16T11:22:07.5380000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 24m 
  - Evidence: 168h 24m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1207] _id=6ac66709de269131f9bc02f9 ts=2026-10-07T15:36:40.8870000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[6135] _id=6acfa749de269131f9d5175e ts=2026-10-14T16:01:13.4470000Z; 47h 35m: 6ab9a8bc9a8420a1e6b56b05.jsonl[6135] _id=6acfa749de269131f9d5175e ts=2026-10-14T16:01:13.4470000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[14154] _id=6ad24484de269131f9e551d3 ts=2026-10-16T15:36:35.6810000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 40h 32m 
  - Evidence: 40h 32m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7308] _id=6ad00205de269131f9d99573 ts=2026-10-14T22:28:20.4720000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[13039] _id=6ad23c11de269131f9e4c27a ts=2026-10-16T15:00:33.0730000Z; 27m 33s: 6ab9a8bc9a8420a1e6b56b05.jsonl[13039] _id=6ad23c11de269131f9e4c27a ts=2026-10-16T15:00:33.0730000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[13919] _id=6ad24287de269131f9e538a3 ts=2026-10-16T15:28:06.8530000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1478] _id=6ac7b48ede269131f9c38417 ts=2026-10-08T15:19:41.9800000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3011] _id=6ace48c8de269131f9cf0470 ts=2026-10-13T15:05:43.7210000Z; 24h 23m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2] _id=6ac3bf31de269131f9ace745 ts=2026-10-05T15:16:00.0290000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[725] _id=6ac51623de269131f9b48dd1 ts=2026-10-06T15:39:15.1680000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b05.jsonl[725] _id=6ac51623de269131f9b48dd1 ts=2026-10-06T15:39:15.1680000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[887] _id=6ac6625dde269131f9bb991d ts=2026-10-07T15:16:44.1390000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1477] _id=6ac7b48ede269131f9c38416 ts=2026-10-08T15:19:41.9800000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3010] _id=6ace48c8de269131f9cf046f ts=2026-10-13T15:05:43.7210000Z; 24h 23m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1] _id=6ac3bf31de269131f9ace743 ts=2026-10-05T15:16:00.0280000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[724] _id=6ac51623de269131f9b48dcc ts=2026-10-06T15:39:15.1670000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b05.jsonl[724] _id=6ac51623de269131f9b48dcc ts=2026-10-06T15:39:15.1670000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[886] _id=6ac6625dde269131f9bb991c ts=2026-10-07T15:16:44.1390000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 48m 
  - Evidence: 143h 48m: 6ab9a8bc9a8420a1e6b56b05.jsonl[3782] _id=6acf877ade269131f9d3562f ts=2026-10-08T15:45:34.354Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[5554] _id=6acfa0e3de269131f9d4bff8 ts=2026-10-14T15:33:54.4640000Z; 23h 58m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1475] _id=6ac7b48ede269131f9c3840f ts=2026-10-07T15:47:27.599Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3782] _id=6acf877ade269131f9d3562f ts=2026-10-08T15:45:34.354Z; 23h 31m: 6ab9a8bc9a8420a1e6b56b05.jsonl[7277] _id=6ad001acde269131f9d994e0 ts=2026-10-14T22:26:51.5550000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[8804] _id=6ad14c72de269131f9e1b1b8 ts=2026-10-15T21:58:08.4890000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a8bc9a8420a1e6b56b05.jsonl[2922] _id=6ac7b970de269131f9c411a9 ts=2026-10-08T15:40:31.9380000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[3025] _id=6ace48dbde269131f9cf04ca ts=2026-10-13T15:06:01.7720000Z; 24h 9m: 6ab9a8bc9a8420a1e6b56b05.jsonl[291] _id=6ac3c295de269131f9ad35e7 ts=2026-10-05T15:30:28.4270000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[727] _id=6ac5163ade269131f9b48fde ts=2026-10-06T15:39:36.3570000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b05.jsonl[1449] _id=6ac6693cde269131f9bc2862 ts=2026-10-07T15:46:03.8320000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[1483] _id=6ac7b4b3de269131f9c38732 ts=2026-10-08T15:20:17.4930000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[14254] _id=6ad24518de269131f9e5568d ts=2026-10-16T15:39:03.6470000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[14255] _id=6ad24518de269131f9e5568e ts=2026-10-16T15:39:03.6470000Z; 1ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[1143] _id=6ac66645de269131f9bbf098 ts=2026-10-07T15:33:24.5940000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[1144] _id=6ac66645de269131f9bbf099 ts=2026-10-07T15:33:24.5950000Z; 4ms: 6ab9a8bc9a8420a1e6b56b05.jsonl[14414] _id=6ad24723de269131f9e5629c ts=2026-10-16T15:47:46.8540000Z -> 6ab9a8bc9a8420a1e6b56b05.jsonl[14415] _id=6ad24723de269131f9e5629e ts=2026-10-16T15:47:46.8580000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1123] _id=6ac66616de269131f9bbeceb ts=2026-10-07T15:32:37.3950000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[3501] _id=6ace4f51de269131f9cf29c7 ts=2026-10-13T15:33:37.0970000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[5195] _id=6acf9d33de269131f9d48d07 ts=2026-10-14T15:18:11.2230000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[7807] _id=6ad0efbbde269131f9dc7e7f ts=2026-10-15T15:22:34.8540000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[12593] _id=6ad209a9de269131f9e346e4 ts=2026-10-16T11:25:28.4230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[13039] _id=6ad23c11de269131f9e4c27a ts=2026-10-16T15:00:33.0730000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[13919] _id=6ad24287de269131f9e538a3 ts=2026-10-16T15:28:06.8530000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[8040] _id=6ad0f1e5de269131f9dca0e5 ts=2026-10-15T15:31:48.6010000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1420] _id=6ac668e8de269131f9bc2218 ts=?`; `6ab9a8bc9a8420a1e6b56b05.jsonl[8796] _id=6ad14c5bde269131f9e1b0fb ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 72 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[4294] _id=6acf9b93de269131f9d46b66 ts=2026-10-14T15:11:13.2650000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[4308] _id=6acf9b94de269131f9d46b7e ts=2026-10-14T15:11:13.7980000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[4312] _id=6acf9b94de269131f9d46b80 ts=2026-10-14T15:11:13.7980000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 137 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[1596] _id=6ac7b584de269131f9c39bfc ts=2026-10-08T15:23:46.4720000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1653] _id=6ac7b5ebde269131f9c3a7f1 ts=2026-10-08T15:25:30.0900000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[1655] _id=6ac7b5ebde269131f9c3a7fc ts=2026-10-08T15:25:30.0900000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[4069] _id=6acf9a69de269131f9d452a4 ts=2026-10-14T15:06:17.4990000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[7641] _id=6ad0ee0ede269131f9dc6340 ts=2026-10-15T15:15:25.4810000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[9707] _id=6ad18424de269131f9e29a97 ts=2026-10-16T01:55:47.8890000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[9773] _id=6ad184e1de269131f9e29e84 ts=2026-10-16T01:58:56.3560000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 485 start, 474 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 886 open, 874 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 23 open, 22 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 5 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'questActiveEvent' (totals: 61 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 239 of 14523 adjacent _id pairs reverse in client time; worst 432151.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b05.jsonl[3781] _id=6ace52b6de269131f9cf4b07 ts=2026-10-13T15:48:06.0440000Z`; `6ab9a8bc9a8420a1e6b56b05.jsonl[3782] _id=6acf877ade269131f9d3562f ts=2026-10-08T15:45:34.354Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.00s, min -511196.14s, max -0.40s over 14524 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b05\coverage.yaml

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

### `InputEvent` — 4941 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1129); Unit 3 Dev (1095); Unit 4 Dev - Dungeon (666); Unit 1 Dev (571); Unit 3 Dungeon Dev (457); Unit 5 Dev - Dungeon (407); Unit 4 Dev - Anderson Base (333); Unit 4 Dev (169); Unit 5 Dev (114)
- **Intervals:** median 1.27s (p5 0.12s / p95 16.31s, n=4940)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4941/4941 records)
    "pressed"  x4941
data.actionType  (string, 4941/4941 records)
    "Move"  x4126
    "Interact"  x540
    "Ascend"  x97
    "Jump"  x63
    "Hoverboard"  x42
    "Sprint"  x36
    "Descend"  x31
    "Map"  x5
    "ToggleDebug"  x1
data.key  (string, 4941/4941 records, 10 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4941/4941 records)
    "Player"  x3571
    "Drone"  x1370
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3038 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1902); Unit 3 Dungeon Dev (564); Unit 4 Dev (380); Unit 5 Dev - Dungeon (192)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.23s, n=3037)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3038/3038 records)
    "BecameVisible"  x886
    "BecameInvisible"  x874
    "BecameCameraCentered"  x639
    "BecameCameraUncentered"  x639
data.pieceId  (string, 3038/3038 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3038/3038 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2724 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (859); Unit 3 Dev (400); Unit 1 Dev (396); Unit 3 Dungeon Dev (229); Unit 4 Dev - Dungeon (210); Unit 4 Dev (207); Unit 5 Dev - Dungeon (165); Unit 5 Dev (153); Unit 4 Dev - Anderson Base (105)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.10s, n=2710)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 2724/2724 records)
data.position.x  (number, 2724/2724 records)
    numeric range -693.415 .. 1586.99 (984 unique)
data.position.y  (number, 2724/2724 records)
    numeric range -9850.65 .. 222.652 (709 unique)
data.position.z  (number, 2724/2724 records)
    numeric range -1078.27 .. 1822.85 (985 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2572 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (710); Unit 3 Dev (433); Unit 1 Dev (332); Unit 4 Dev (297); Unit 3 Dungeon Dev (256); Unit 5 Dev (242); Unit 4 Dev - Dungeon (125); Unit 4 Dev - Anderson Base (103); Unit 5 Dev - Dungeon (74)
- **eventKey:** present on 1613 of 2572 records
- **Intervals:** median 4.59s (p5 0.00s / p95 41.11s, n=2571)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1613; [conversationId, dialogueEventType] x959
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2572/2572 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2572/2572 records)
    "DialogueNodeEvent"  x1613
    "DialogueStartEvent"  x485
    "DialogueFinishEvent"  x474
data.nodeId  (number, 1613/2572 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 411 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (183); Unit 3 Dev (81); Unit 5 Dev (68); Unit 1 Dev (54); Unit 2 Prod (Refactor) (25)
- **Intervals:** median 0.79s (p5 0.03s / p95 8.89s, n=410)
- **Fields under `data`:**

```text
data.actionType  (string, 411/411 records)
    "argumentationNodeHoverEnd"  x180
    "argumentationNodeHoverStart"  x180
    "argumentationNodeAdd"  x36
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 411/411 records)
    "Unit 4 - Flooding"  x183
    "Unit 3 - Pollution Upstream"  x81
    "Unit 5"  x68
    "Unit 1 - Freshwater"  x41
    "Unit 2 – Watershed"  x25
    "Unit 1 - Argumentation Tutorial"  x13
data.nodeName  (string, 411/411 records)
    "C"  x54
    "II"  x51
    "B"  x48
    "D"  x44
    "3"  x43
    "A"  x39
    "4"  x38
    "1"  x29
    "I"  x29
    "2"  x27
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 291 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (80); Unit 3 Dungeon Dev (63); Unit 2 Prod (Refactor) (54); Unit 4 Dev (31); Unit 1 Dev (20); Unit 3 Dev (13); Unit 5 Dev - Dungeon (13); Unit 4 Dev - Anderson Base (10); Unit 5 Dev (7)
- **Intervals:** median 18.05s (p5 2.42s / p95 669.48s, n=290)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 291/291 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 291/291 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 100 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 1 Dev (22); Unit 3 Dev (14); Unit 4 Dev (10); Unit 4 Dev - Dungeon (9); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 100 of 100 records
- **Intervals:** median 239.82s (p5 0.01s / p95 62867.96s, n=99)
- **`data` key-set variants:** [questEventType, questID, questName] x61; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 100/100 records)
    "questActiveEvent"  x61
    "questFinishEvent"  x39
data.questID  (string, 100/100 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 100/100 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/100 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 87 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (47); Unit 3 Dev (30); Unit 4 Dev (10)
- **Intervals:** median 1.67s (p5 0.28s / p95 207.28s, n=86)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x76; [Soil Key Puzzle Status, Unit] x11
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/87 records)
    "Started"  x6
    "Finished"  x5
data.Unit  (string, 11/87 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 76/87 records)
    "RightDrag"  x45
    "LeftDrag"  x31
data.currentSoilType  (string, 76/87 records)
    "CLAYSAND"  x16
    "SAND"  x16
    "CLAY"  x13
    "SANDGRAVEL"  x12
    "CLAYROCK"  x10
    "GRAVEL"  x6
    "BEDROCK"  x3
data.isCorrectSelection  (string, 76/87 records)
    "false"  x57
    "true"  x19
data.waterLevelStatus  (string, 76/87 records)
    "TooHigh"  x40
    "Proper"  x24
    "TooLow"  x12
data.waterRetentionChange  (string, 76/87 records)
    "Increase"  x29
    "Decrease"  x28
    "NoChange"  x19
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 85 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (53); Unit 3 Dev (32)
- **Intervals:** median 7.10s (p5 0.03s / p95 20375.19s, n=84)
- **`data` key-set variants:** [actionType, featureUsed] x45; [actionType, featureUsed, location] x38; [actionType, featureUsed, legendName] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 85/85 records)
    "WaypointMoveEvent"  x32
    "MapOpenEvent"  x23
    "MapCloseEvent"  x22
    "WaypointSetEvent"  x6
    "Selected"  x2
data.featureUsed  (string, 85/85 records)
    "Map"  x45
    "Waypoint"  x38
    "Legend"  x2
data.legendName  (string, 2/85 records)
    "0 ft"  x1
    "90 ft"  x1
data.location  (object, 38/85 records)
data.location.x  (number, 38/85 records)
    numeric range -367.212 .. 192.339 (26 unique)
data.location.y  (number, 38/85 records)
    numeric range -377.213 .. 287.781 (36 unique)
data.location.z  (number, 38/85 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 48 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (20); Unit 2 Prod (Refactor) (9); Unit 4 Dev (5); Unit 3 Dev (4); Unit 1 Dev (3); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 260.75s (p5 8.16s / p95 84996.94s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "DebugMenuStateChanged"  x48
data.isOpened  (bool, 48/48 records)
    false  x48
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 40 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 3 Dev (6); Unit 4 Dev - Dungeon (6); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Transition (1); Unit 5 Dev (1)
- **Intervals:** median 1157.41s (p5 7.04s / p95 85323.59s, n=39)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 40/40 records)
    true  x40
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 38 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (38)
- **Intervals:** median 25.01s (p5 4.38s / p95 90.16s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "On"  x24
    "Off"  x14
data.floor  (string, 38/38 records)
    "4"  x21
    "3"  x11
    "1"  x3
    "2"  x3
data.machineNumber  (string, 38/38 records)
    "One"  x37
    "Two"  x1
data.machineType  (string, 38/38 records)
    "Condenser"  x21
    "Evaporator"  x11
    "DualChamber_Condenser"  x2
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 38/38 records)
    "2"  x20
    "1"  x9
    "3"  x7
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 23 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (6); Unit 4 Dev - Dungeon (6); Unit 1 Dev (2); Transition (1); Unit 5 Dev (1)
- **Intervals:** median 543.95s (p5 7.02s / p95 86206.26s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 22 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (22)
- **Intervals:** median 12494.48s (p5 273.99s / p95 87795.14s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 20 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (8); Unit 5 Dev (6); Unit 1 Dev (3); Unit 3 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 19.51s (p5 1.79s / p95 136250.55s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "submitAnswerEvent"  x20
data.answerSubmitted  (string, 20/20 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 20/20 records)
    "Unit 4 - Flooding"  x8
    "Unit 5"  x6
    "Unit 1 - Freshwater"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TerasGardenBox` — 19 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (19)
- **Intervals:** median 3.67s (p5 1.18s / p95 58.74s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records, 11 empty-string)
    ""  x11
    "cameraPlaced"  x8
data.boxId  (string, 19/19 records)
    "0"  x8
    "1"  x7
    "2"  x4
data.soilType  (string, 19/19 records)
    "Sand"  x10
    "Gravel"  x5
    "Clay"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 16 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (14); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 2.11s (p5 0.85s / p95 44937.43s, n=15)
- **`data` key-set variants:** [actionType, chatID] x10; [actionKey, chatID] x6
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 6/16 records)
    "ScrollStop"  x6
data.actionType  (string, 10/16 records)
    "ScrollStart"  x6
    "Close"  x3
    "Open"  x1
data.chatID  (string, 16/16 records)
    "NA"  x9
    "[10-32, 10-33, 10-195, 11-12, 11-13, 11-14]"  x1
    "[10-38, 10-39, 10-210, 10-215, 10-216, 10-39]"  x1
    "[10-39, 10-210, 10-215, 10-216, 10-39]"  x1
    "[10-39, 10-40, 10-212, 10-39, 10-211, 10-217]"  x1
    "[10-6, 10-7, 10-8, 10-10, 10-9, 10-11]"  x1
    "[11-26, 11-25, 11-27, 11-26, 11-26, 11-27]"  x1
    "[11-26, 11-27, 11-27, 11-29, 11-29]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 111.37s (p5 0.03s / p95 292825.15s, n=13)
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

### `soilMachine` — 12 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (12)
- **Intervals:** median 24.79s (p5 6.94s / p95 338.78s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "ChangeCanister"  x12
data.canisterType  (string, 12/12 records)
    "Clay"  x5
    "Sand"  x3
    "Bedrock"  x2
    "Gravel"  x2
data.floor  (string, 12/12 records)
    "5"  x9
    "4"  x2
    "3"  x1
data.machine  (string, 12/12 records)
    "1"  x10
    "2"  x2
data.row  (string, 12/12 records)
    "TopRow"  x9
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (6)
- **Intervals:** median 14.67s (p5 2.13s / p95 560.48s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 6.90s (p5 2.99s / p95 29.02s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Flat"  x1
data.featureUsed  (string, 6/6 records)
    "GlassRoofTemperature"  x3
    "ExtraCovering"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records)
    "Hot"  x2
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 105.16s (p5 3.61s / p95 519282.49s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 67992.50s (p5 17956.32s / p95 548418.51s, n=4)
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

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x2
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (47 records)
- `TerasGardenBox` data.actionType: "" (11x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (32x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (38x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*