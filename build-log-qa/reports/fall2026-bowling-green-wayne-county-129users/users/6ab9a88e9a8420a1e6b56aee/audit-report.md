# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56aee

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56aee
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56aee.jsonl
- **Records:** 14819 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56aee
- **Time span:** 2026-10-06T13:15:47.432000+00:00 .. 2026-10-16T13:34:25.726000+00:00 (240h 18m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56aee\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 14819 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 93 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6654 | 44.9 | 1 | 9 | 0 | 2026-10-06T13:16:03.199000+00:00 | 2026-10-16T13:34:25.726000+00:00 | 240h 18m |
| PuzzlePieceVisibleEvent | 3337 | 22.52 | 1 | 4 | 0 | 2026-10-06T13:46:49.614000+00:00 | 2026-10-16T13:13:25.081000+00:00 | 239h 26m |
| DialogueEvent | 2212 | 14.93 | 1 | 9 | 1355 | 2026-10-06T13:16:19.746000+00:00 | 2026-10-16T13:34:20.556000+00:00 | 240h 18m |
| PlayerPositionEvent | 1552 | 10.47 | 1 | 9 | 0 | 2026-10-06T13:15:59.726000+00:00 | 2026-10-16T13:34:24.589000+00:00 | 240h 18m |
| argumentationNodeEvent | 293 | 1.98 | 1 | 5 | 0 | 2026-10-06T13:36:01.066000+00:00 | 2026-10-16T13:22:53.382000+00:00 | 239h 46m |
| ObjectInterEvent | 258 | 1.74 | 1 | 9 | 0 | 2026-10-06T13:20:23.897000+00:00 | 2026-10-16T13:34:25.726000+00:00 | 240h 14m |
| TopographicMapEvent | 117 | 0.79 | 1 | 2 | 0 | 2026-10-06T13:47:31.277000+00:00 | 2026-10-14T13:27:06.823000+00:00 | 191h 39m |
| questEvent | 85 | 0.57 | 1 | 9 | 85 | 2026-10-06T13:16:19.725000+00:00 | 2026-10-16T13:30:49.593000+00:00 | 240h 14m |
| Soil Key Puzzle | 80 | 0.54 | 1 | 3 | 0 | 2026-10-06T13:52:19.418000+00:00 | 2026-10-14T13:45:00.742000+00:00 | 191h 52m |
| WaterChamberEvent | 47 | 0.32 | 1 | 1 | 0 | 2026-10-15T13:50:20.615000+00:00 | 2026-10-16T13:15:57.553000+00:00 | 23h 25m |
| DaniEvent | 34 | 0.23 | 1 | 4 | 0 | 2026-10-06T13:59:11.786000+00:00 | 2026-10-14T14:00:06.484000+00:00 | 192h 0m |
| DEBUGMenu | 27 | 0.18 | 1 | 9 | 0 | 2026-10-06T13:15:59.703000+00:00 | 2026-10-16T13:10:59.512000+00:00 | 239h 54m |
| gameWindowFocusEvent | 21 | 0.14 | 1 | 5 | 0 | 2026-10-06T13:15:47.432000+00:00 | 2026-10-16T13:10:52.977000+00:00 | 239h 55m |
| argumentationAnswerEvent | 18 | 0.12 | 1 | 5 | 0 | 2026-10-06T13:37:10.778000+00:00 | 2026-10-16T13:22:54.364000+00:00 | 239h 45m |
| argumentationEvent | 14 | 0.09 | 1 | 5 | 0 | 2026-10-06T13:36:53.813000+00:00 | 2026-10-16T13:22:54.398000+00:00 | 239h 46m |
| gameWindowUnfocusEvent | 13 | 0.09 | 1 | 6 | 0 | 2026-10-07T13:28:08.473000+00:00 | 2026-10-15T13:59:38.692000+00:00 | 192h 31m |
| gameStartEvent | 12 | 0.08 | 1 | 1 | 0 | 2026-10-06T13:15:47.433000+00:00 | 2026-10-16T13:10:52.977000+00:00 | 239h 55m |
| argumentationToolEvent | 9 | 0.06 | 1 | 2 | 0 | 2026-10-06T13:36:50.993000+00:00 | 2026-10-13T13:42:42.064000+00:00 | 168h 5m |
| chatEvent | 9 | 0.06 | 1 | 4 | 0 | 2026-10-07T13:52:14.737000+00:00 | 2026-10-16T13:16:45.391000+00:00 | 215h 24m |
| SolarStillDesignEvent | 8 | 0.05 | 1 | 1 | 0 | 2026-10-16T13:28:17.889000+00:00 | 2026-10-16T13:28:32.075000+00:00 | 14.2s |
| soilMachine | 8 | 0.05 | 1 | 1 | 0 | 2026-10-14T13:54:36.630000+00:00 | 2026-10-15T13:18:45.617000+00:00 | 23h 24m |
| TerasGardenBox | 6 | 0.04 | 1 | 1 | 0 | 2026-10-15T13:37:50.068000+00:00 | 2026-10-15T13:38:33.215000+00:00 | 43.1s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T13:41:59.325000+00:00 | 2026-10-16T13:34:25.705000+00:00 | 239h 52m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 130415.572s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.066s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.133s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 16.131s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.481s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 175.978s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84162.48s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1001.53s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 401.203s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 34 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: rightShift; tab 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Tilted In 
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
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,D,2,II; A,D,B,2,II; A,D,C,2,II; C,2,II; C,D,3,II; D,2,II; D,4,II 
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
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 9 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [15-11, 15-12, 15-13, 15-14, 15-15]; [18-117, 18-243, 18-118, 74-0, 74-4]; [19-0, 19-1, 19-49, 19-2, 19-59, 19-50, 19-51] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[145] _id=6ac4f60cde269131f9b0511c ts=2026-10-06T13:22:19.8800000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[211] _id=6ac4f6fade269131f9b0825f ts=2026-10-06T13:26:18.4190000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[280] _id=6ac4f777de269131f9b0917b ts=2026-10-06T13:28:23.3600000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[12] _id=6ac4f484de269131f9b03532 ts=2026-10-06T13:15:47.4330000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[726] _id=6ac4fafede269131f9b1355b ts=2026-10-06T13:43:25.6940000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2275] _id=6ac64826de269131f9b8ea8f ts=2026-10-07T13:24:52.8590000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[11] _id=6ac4f483de269131f9b03530 ts=2026-10-06T13:15:47.4320000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[725] _id=6ac4fafede269131f9b13553 ts=2026-10-06T13:43:25.6920000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2274] _id=6ac64826de269131f9b8ea8e ts=2026-10-07T13:24:52.8590000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[2413] _id=6ac648e9de269131f9b918e4 ts=2026-10-07T13:28:08.4730000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2460] _id=6ac64929de269131f9b926c5 ts=2026-10-07T13:29:11.4190000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[5375] _id=6ac79ac0de269131f9c03c13 ts=2026-10-07T14:00:57.062Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6653 | 0.0 | 0.471 | 130.032 | 5.781 | 429694.474 | 0.46 | 327 | 6 |
| PuzzlePieceVisibleEvent | 3336 | 0.0 | 0.02 | 258.392 | 1.407 | 433141.733 | 0.23 | 1769 | 8 |
| DialogueEvent | 2211 | 0.0 | 3.447 | 391.262 | 23.663 | 429585.456 | 0.15 | 637 | 6 |
| PlayerPositionEvent | 1540 | 0.0 | 10.002 | 561.578 | 10.274 | 429562.042 | 0.11 | 1 | 6 |
| argumentationNodeEvent | 292 | 0.006 | 0.821 | 2956.207 | 9.182 | 431316.144 | 0.02 | 27 | 4 |
| ObjectInterEvent | 257 | 0.0 | 10.698 | 3365.143 | 345.255 | 430583.478 | 0.02 | 3 | 8 |
| TopographicMapEvent | 116 | 0.013 | 3.381 | 5948.065 | 367.019 | 430974.591 | 0.01 | 3 | 5 |
| questEvent | 84 | 0.0 | 148.911 | 10296.07 | 83674.581 | 429892.962 | 0.01 | 18 | 11 |
| Soil Key Puzzle | 79 | 0.15 | 2.066 | 8743.814 | 8628.7 | 432829.822 | 0.01 | 0 | 4 |
| WaterChamberEvent | 46 | 0.517 | 8.133 | 1833.412 | 78.865 | 83529.673 | 0.03 | 0 | 1 |
| DaniEvent | 33 | 0.005 | 3.399 | 20947.112 | 86039.746 | 431774.49 | 0.0 | 5 | 6 |
| DEBUGMenu | 26 | 6.693 | 528.74 | 33219.223 | 86323.963 | 429684.193 | 0.0 | 0 | 12 |
| gameWindowFocusEvent | 20 | 1.322 | 1001.53 | 43185.277 | 103585.125 | 429693.383 | 0.0 | 0 | 11 |
| argumentationAnswerEvent | 17 | 3.492 | 16.131 | 50773.152 | 225154.54 | 431367.85 | 0.0 | 0 | 4 |
| argumentationEvent | 13 | 0.048 | 75.488 | 66396.968 | 276648.476 | 431316.03 | 0.0 | 1 | 4 |
| gameWindowUnfocusEvent | 12 | 0.0 | 401.203 | 57757.518 | 280762.038 | 518346.08 | 0.0 | 1 | 5 |
| gameStartEvent | 11 | 101.907 | 84162.48 | 78518.686 | 258187.806 | 429693.383 | 0.0 | 0 | 10 |
| argumentationToolEvent | 8 | 0.796 | 2.481 | 75643.884 | 393307.134 | 605027.011 | 0.0 | 0 | 1 |
| chatEvent | 8 | 1.957 | 175.978 | 96933.832 | 397193.567 | 517992.84 | 0.0 | 0 | 3 |
| SolarStillDesignEvent | 7 | 1.114 | 1.642 | 2.027 | 3.694 | 4.16 | 29.61 | 0 | 0 |
| soilMachine | 7 | 10.422 | 80.668 | 12035.57 | 58691.022 | 83770.295 | 0.0 | 0 | 1 |
| TerasGardenBox | 5 | 1.222 | 4.567 | 8.629 | 19.502 | 20.656 | 6.95 | 0 | 0 |
| EndOfUnit | 4 | 85693.519 | 130415.572 | 215886.595 | 465515.177 | 517021.717 | 0.0 | 0 | 4 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 14 group(s), 31 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[2768] _id=6ac64b1fde269131f9b9a3da ts=2026-10-07T13:37:34.7230000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[2769] _id=6ac64b1fde269131f9b9a3db ts=2026-10-07T13:37:34.7230000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2826] _id=6ac64b45de269131f9b9ab6a ts=2026-10-07T13:38:11.9950000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[2827] _id=6ac64b45de269131f9b9ab6b ts=2026-10-07T13:38:11.9950000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[7863] _id=6ace372fde269131f9cee4c8 ts=2026-10-13T13:50:39.3500000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[7864] _id=6ace372fde269131f9cee4c9 ts=2026-10-13T13:50:39.3500000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 179 group(s), 293 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[874] _id=6ac4fbd4de269131f9b16344 ts=2026-10-06T13:46:58.1450000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[877] _id=6ac4fbd4de269131f9b1634f ts=2026-10-06T13:46:58.1450000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[889] _id=6ac4fbd5de269131f9b1638a ts=2026-10-06T13:46:58.8200000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[890] _id=6ac4fbd5de269131f9b16391 ts=2026-10-06T13:46:58.8200000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[882] _id=6ac4fbd6de269131f9b163ae ts=2026-10-06T13:46:59.2060000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[895] _id=6ac4fbd6de269131f9b163b5 ts=2026-10-06T13:46:59.2060000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[14547] _id=6ad22572de269131f9e38dad ts=2026-10-16T13:24:02.5500000Z == 6ab9a88e9a8420a1e6b56aee.jsonl[14548] _id=6ad22572de269131f9e38dae ts=2026-10-16T13:24:02.5500000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6ab9a88e9a8420a1e6b56aee.jsonl[96] _id=6ac4f598de269131f9b040ec ts=2026-10-06T13:20:23.8970000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[97] _id=6ac4f598de269131f9b040fb ts=2026-10-06T13:20:23.8990000Z`; `408ms: 6ab9a88e9a8420a1e6b56aee.jsonl[3756] _id=6ac64e2ade269131f9ba0241 ts=2026-10-07T13:50:33.4530000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[3769] _id=6ac64e2bde269131f9ba0257 ts=2026-10-07T13:50:33.8610000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 211 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `122ms: 6ab9a88e9a8420a1e6b56aee.jsonl[891] _id=6ac4fbd5de269131f9b1639c ts=2026-10-06T13:46:58.9540000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[876] _id=6ac4fbd5de269131f9b163a2 ts=2026-10-06T13:46:59.0760000Z`; `66ms: 6ab9a88e9a8420a1e6b56aee.jsonl[876] _id=6ac4fbd5de269131f9b163a2 ts=2026-10-06T13:46:59.0760000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[885] _id=6ac4fbd5de269131f9b163ac ts=2026-10-06T13:46:59.1420000Z`; `64ms: 6ab9a88e9a8420a1e6b56aee.jsonl[885] _id=6ac4fbd5de269131f9b163ac ts=2026-10-06T13:46:59.1420000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[882] _id=6ac4fbd6de269131f9b163ae ts=2026-10-06T13:46:59.2060000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6ab9a88e9a8420a1e6b56aee.jsonl[2206] _id=6ac4fe98de269131f9b22a64 ts=2026-10-06T13:58:48.1010000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[2208] _id=6ac4fe99de269131f9b22a9f ts=2026-10-06T13:58:48.1270000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `66ms: 6ab9a88e9a8420a1e6b56aee.jsonl[7355] _id=6ace3569de269131f9cecfea ts=2026-10-13T13:43:05.0880000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[7358] _id=6ace3569de269131f9cecfee ts=2026-10-13T13:43:05.1540000Z`; `48ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12492] _id=6ad0d647de269131f9dab3a9 ts=2026-10-15T13:33:58.5240000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[12496] _id=6ad0d647de269131f9dab3ac ts=2026-10-15T13:33:58.5720000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `395ms: 6ab9a88e9a8420a1e6b56aee.jsonl[493] _id=6ac4f958de269131f9b0e162 ts=2026-10-06T13:36:24.3270000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[498] _id=6ac4f959de269131f9b0e172 ts=2026-10-06T13:36:24.7220000Z`; `503ms: 6ab9a88e9a8420a1e6b56aee.jsonl[506] _id=6ac4f95bde269131f9b0e1eb ts=2026-10-06T13:36:26.9670000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[509] _id=6ac4f95bde269131f9b0e212 ts=2026-10-06T13:36:27.4700000Z`; `21ms: 6ab9a88e9a8420a1e6b56aee.jsonl[529] _id=6ac4f97ade269131f9b0eac0 ts=2026-10-06T13:36:57.7270000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[532] _id=6ac4f97ade269131f9b0eacc ts=2026-10-06T13:36:57.7480000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[13868] _id=6ad0dc4bde269131f9db680d ts=2026-10-15T13:59:38.6920000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[13870] _id=6ad221f7de269131f9e34e68 ts=2026-10-15T13:59:38.692Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a88e9a8420a1e6b56aee.jsonl[14721] _id=6ad226cade269131f9e3a6e7 ts=2026-10-16T13:29:46.6490000Z ~ 6ab9a88e9a8420a1e6b56aee.jsonl[14722] _id=6ad226cade269131f9e3a6eb ts=2026-10-16T13:29:46.6540000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a88e9a8420a1e6b56aee.jsonl[6194] _id=6ac7a10cde269131f9c14bca ts=2026-10-08T13:56:27.8750000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6226] _id=6ace2f80de269131f9ce9051 ts=2026-10-13T13:17:52.0680000Z; 24h 4m: 6ab9a88e9a8420a1e6b56aee.jsonl[2276] _id=6ac6482fde269131f9b8ec4a ts=2026-10-07T13:25:02.3140000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5376] _id=6ac79ac0de269131f9c03c17 ts=2026-10-08T13:29:34.9480000Z; 23h 41m: 6ab9a88e9a8420a1e6b56aee.jsonl[724] _id=6ac4fb07de269131f9b1371e ts=2026-10-06T13:43:34.7550000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2273] _id=6ac64826de269131f9b8ea8c ts=2026-10-07T13:24:52.7040000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a88e9a8420a1e6b56aee.jsonl[5996] _id=6ac79f63de269131f9c10744 ts=2026-10-08T13:49:22.9680000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7469] _id=6ace3601de269131f9ced64f ts=2026-10-13T13:45:37.4580000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aee.jsonl[4260] _id=6ac64e8fde269131f9ba0eb3 ts=2026-10-07T13:52:14.3110000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5992] _id=6ac79f61de269131f9c106d0 ts=2026-10-08T13:49:20.7750000Z; 23h 51m: 6ab9a88e9a8420a1e6b56aee.jsonl[7478] _id=6ace360ade269131f9ced6ad ts=2026-10-13T13:45:45.8300000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[9596] _id=6acf85a5de269131f9d33b56 ts=2026-10-14T13:37:41.0980000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56aee.jsonl[2227] _id=6ac4feb7de269131f9b2319c ts=2026-10-06T13:59:18.8250000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2194] _id=6ac4feb7de269131f9b231a3 ts=2026-10-06T13:59:18.8300000Z; 6ms: 6ab9a88e9a8420a1e6b56aee.jsonl[9604] _id=6acf85b7de269131f9d33c41 ts=2026-10-14T13:37:59.0110000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[9601] _id=6acf85b7de269131f9d33c48 ts=2026-10-14T13:37:59.0170000Z; 7ms: 6ab9a88e9a8420a1e6b56aee.jsonl[2261] _id=6ac4fedfde269131f9b23958 ts=2026-10-06T13:59:59.4990000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2260] _id=6ac4fedfde269131f9b2395a ts=2026-10-06T13:59:59.5060000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56aee.jsonl[6222] _id=6ac7a184de269131f9c156c3 ts=2026-10-08T13:58:26.9300000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6232] _id=6ace2f94de269131f9ce9138 ts=2026-10-13T13:18:12.3860000Z; 23h 29m: 6ab9a88e9a8420a1e6b56aee.jsonl[5372] _id=6ac6508bde269131f9ba3f5b ts=2026-10-07T14:00:42.7880000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5383] _id=6ac79acdde269131f9c03d69 ts=2026-10-08T13:29:47.5880000Z; 23h 26m: 6ab9a88e9a8420a1e6b56aee.jsonl[2211] _id=6ac4fea4de269131f9b22d32 ts=2026-10-06T13:58:59.8850000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2353] _id=6ac64863de269131f9b8f73a ts=2026-10-07T13:25:54.0920000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 637 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12365] _id=6ad0d5cade269131f9daa6fe ts=2026-10-15T13:31:53.3500000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12366] _id=6ad0d5cade269131f9daa6ff ts=2026-10-15T13:31:53.3500000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12385] _id=6ad0d5ebde269131f9daaae3 ts=2026-10-15T13:32:26.1550000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12386] _id=6ad0d5ebde269131f9daaae4 ts=2026-10-15T13:32:26.1550000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12447] _id=6ad0d61bde269131f9dab011 ts=2026-10-15T13:33:14.4380000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12448] _id=6ad0d61bde269131f9dab012 ts=2026-10-15T13:33:14.4380000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a88e9a8420a1e6b56aee.jsonl[6191] _id=6ac7a0f5de269131f9c14929 ts=2026-10-08T13:56:04.1070000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[9542] _id=6acf8492de269131f9d32941 ts=2026-10-14T13:33:05.8240000Z; 48h 14m: 6ab9a88e9a8420a1e6b56aee.jsonl[721] _id=6ac4faa7de269131f9b1276b ts=2026-10-06T13:41:59.3250000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6191] _id=6ac7a0f5de269131f9c14929 ts=2026-10-08T13:56:04.1070000Z; 24h 13m: 6ab9a88e9a8420a1e6b56aee.jsonl[9542] _id=6acf8492de269131f9d32941 ts=2026-10-14T13:33:05.8240000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12945] _id=6ad0d925de269131f9db0541 ts=2026-10-15T13:46:12.1860000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a88e9a8420a1e6b56aee.jsonl[6196] _id=6ac7a10fde269131f9c14c5c ts=2026-10-08T13:56:29.7410000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6228] _id=6ace2f8dde269131f9ce90bf ts=2026-10-13T13:18:04.2150000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aee.jsonl[5325] _id=6ac65006de269131f9ba37ae ts=2026-10-07T13:58:29.4060000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5382] _id=6ac79acdde269131f9c03d68 ts=2026-10-08T13:29:47.5480000Z; 23h 25m: 6ab9a88e9a8420a1e6b56aee.jsonl[2258] _id=6ac4fedede269131f9b23926 ts=2026-10-06T13:59:57.9760000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2278] _id=6ac64835de269131f9b8ecf3 ts=2026-10-07T13:25:07.8930000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 327 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[10011] _id=6acf8761de269131f9d3545a ts=2026-10-14T13:45:04.5620000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[10012] _id=6acf8761de269131f9d3545b ts=2026-10-14T13:45:04.5620000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[10434] _id=6acf8861de269131f9d36ddd ts=2026-10-14T13:49:21.0280000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[10435] _id=6acf8861de269131f9d36dde ts=2026-10-14T13:49:21.0280000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[10663] _id=6acf890ede269131f9d38509 ts=2026-10-14T13:52:14.0590000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[10664] _id=6acf890ede269131f9d3850a ts=2026-10-14T13:52:14.0590000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 36m 
  - Evidence: 119h 36m: 6ab9a88e9a8420a1e6b56aee.jsonl[6002] _id=6ac79f6ede269131f9c1090a ts=2026-10-08T13:49:33.3770000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6531] _id=6ace3165de269131f9cea18e ts=2026-10-13T13:25:56.8550000Z; 23h 51m: 6ab9a88e9a8420a1e6b56aee.jsonl[1997] _id=6ac4fd13de269131f9b1bb8b ts=2026-10-06T13:52:19.4230000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[3116] _id=6ac64c9fde269131f9b9e295 ts=2026-10-07T13:43:57.9250000Z; 23h 49m: 6ab9a88e9a8420a1e6b56aee.jsonl[5209] _id=6ac64f59de269131f9ba2c6c ts=2026-10-07T13:55:36.3190000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5790] _id=6ac79e4cde269131f9c0d367 ts=2026-10-08T13:44:43.3800000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12256] _id=6ad0d4ffde269131f9da94e2 ts=2026-10-15T13:28:30.1650000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12257] _id=6ad0d4ffde269131f9da94e3 ts=2026-10-15T13:28:30.1650000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12301] _id=6ad0d532de269131f9da99ec ts=2026-10-15T13:29:21.0940000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12302] _id=6ad0d532de269131f9da99ed ts=2026-10-15T13:29:21.0940000Z; 2ms: 6ab9a88e9a8420a1e6b56aee.jsonl[96] _id=6ac4f598de269131f9b040ec ts=2026-10-06T13:20:23.8970000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[97] _id=6ac4f598de269131f9b040fb ts=2026-10-06T13:20:23.8990000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56aee.jsonl[6223] _id=6ac7a190de269131f9c157b8 ts=2026-10-08T13:58:39.8600000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6227] _id=6ace2f8dde269131f9ce90be ts=2026-10-13T13:18:01.9020000Z; 23h 28m: 6ab9a88e9a8420a1e6b56aee.jsonl[5373] _id=6ac65094de269131f9ba41f5 ts=2026-10-07T14:00:51.5780000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5381] _id=6ac79acdde269131f9c03d67 ts=2026-10-08T13:29:44.6560000Z; 23h 25m: 6ab9a88e9a8420a1e6b56aee.jsonl[2257] _id=6ac4fedede269131f9b23921 ts=2026-10-06T13:59:57.7940000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2279] _id=6ac64832de269131f9b8eca0 ts=2026-10-07T13:25:02.3280000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[8316] _id=6ace3963de269131f9ceffdb ts=2026-10-13T14:00:02.8300000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[8394] _id=6acf7fbdde269131f9d2d07e ts=2026-10-13T14:00:02.83Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 19m 
  - Evidence: 120h 19m: 6ab9a88e9a8420a1e6b56aee.jsonl[5417] _id=6ac79ae3de269131f9c03fdb ts=2026-10-08T13:30:09.4770000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7634] _id=6ace36d8de269131f9cedf4a ts=2026-10-13T13:49:11.2100000Z; 23h 55m: 6ab9a88e9a8420a1e6b56aee.jsonl[1731] _id=6ac4fcd0de269131f9b1ac66 ts=2026-10-06T13:51:09.9220000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[3095] _id=6ac64d44de269131f9b9efa4 ts=2026-10-07T13:46:42.1280000Z; 23h 33m: 6ab9a88e9a8420a1e6b56aee.jsonl[10303] _id=6acf87aede269131f9d35b5d ts=2026-10-14T13:46:20.2710000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[11947] _id=6ad0d2eede269131f9da620a ts=2026-10-15T13:19:40.5280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1769 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[10026] _id=6acf8762de269131f9d3547a ts=2026-10-14T13:45:05.0630000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[10027] _id=6acf8762de269131f9d3547b ts=2026-10-14T13:45:05.0630000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[10027] _id=6acf8762de269131f9d3547b ts=2026-10-14T13:45:05.0630000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[10028] _id=6acf8763de269131f9d3547f ts=2026-10-14T13:45:05.0630000Z; 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[10040] _id=6acf8762de269131f9d35462 ts=2026-10-14T13:45:04.4970000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[10022] _id=6acf8762de269131f9d35464 ts=2026-10-14T13:45:04.4970000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 13m 
  - Evidence: 120h 13m: 6ab9a88e9a8420a1e6b56aee.jsonl[5558] _id=6ac79bc6de269131f9c062e5 ts=2026-10-08T13:33:57.4080000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7591] _id=6ace3683de269131f9cedb78 ts=2026-10-13T13:47:47.2300000Z; 23h 54m: 6ab9a88e9a8420a1e6b56aee.jsonl[7612] _id=6ace36afde269131f9cedd1e ts=2026-10-13T13:48:30.8610000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[9698] _id=6acf86eede269131f9d34b75 ts=2026-10-14T13:43:10.0420000Z; 23h 51m: 6ab9a88e9a8420a1e6b56aee.jsonl[2000] _id=6ac4fd16de269131f9b1bc1b ts=2026-10-06T13:52:22.3600000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[3117] _id=6ac64c9fde269131f9b9e293 ts=2026-10-07T13:43:57.9190000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a88e9a8420a1e6b56aee.jsonl[5653] _id=6ac79d06de269131f9c09e9e ts=2026-10-08T13:39:17.5340000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6362] _id=6ace3084de269131f9ce9a08 ts=2026-10-13T13:22:12.1250000Z; 23h 56m: 6ab9a88e9a8420a1e6b56aee.jsonl[3027] _id=6ac64c57de269131f9b9db80 ts=2026-10-07T13:42:46.5580000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5650] _id=6ac79cf9de269131f9c09c58 ts=2026-10-08T13:39:04.4730000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aee.jsonl[7429] _id=6ace35d6de269131f9ced48c ts=2026-10-13T13:44:54.5590000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[9131] _id=6acf8269de269131f9d2fcb2 ts=2026-10-14T13:23:53.4870000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.013s..0.026s shown 
  - Evidence: 13ms: 6ab9a88e9a8420a1e6b56aee.jsonl[2205] _id=6ac4fe98de269131f9b22a5e ts=2026-10-06T13:58:48.0880000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2206] _id=6ac4fe98de269131f9b22a64 ts=2026-10-06T13:58:48.1010000Z; 24ms: 6ab9a88e9a8420a1e6b56aee.jsonl[2402] _id=6ac648d4de269131f9b912a3 ts=2026-10-07T13:27:47.2540000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2401] _id=6ac648d4de269131f9b912aa ts=2026-10-07T13:27:47.2780000Z; 26ms: 6ab9a88e9a8420a1e6b56aee.jsonl[2206] _id=6ac4fe98de269131f9b22a64 ts=2026-10-06T13:58:48.1010000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2208] _id=6ac4fe99de269131f9b22a9f ts=2026-10-06T13:58:48.1270000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 12m 
  - Evidence: 23h 12m: 6ab9a88e9a8420a1e6b56aee.jsonl[13856] _id=6ad0dc2ede269131f9db6513 ts=2026-10-15T13:59:08.9130000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[13880] _id=6ad22277de269131f9e351cc ts=2026-10-16T13:11:18.5860000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a88e9a8420a1e6b56aee.jsonl[6108] _id=6ac7a027de269131f9c12a39 ts=2026-10-08T13:52:37.9610000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7310] _id=6ace352ede269131f9cecd3a ts=2026-10-13T13:42:05.8110000Z; 48h 13m: 6ab9a88e9a8420a1e6b56aee.jsonl[596] _id=6ac4fa05de269131f9b105a7 ts=2026-10-06T13:39:16.7480000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6108] _id=6ac7a027de269131f9c12a39 ts=2026-10-08T13:52:37.9610000Z; 47h 48m: 6ab9a88e9a8420a1e6b56aee.jsonl[7360] _id=6ace3569de269131f9cecfe8 ts=2026-10-13T13:43:05.0550000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12361] _id=6ad0d5cade269131f9daa6f7 ts=2026-10-15T13:31:53.3280000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56aee.jsonl[6104] _id=6ac7a027de269131f9c12a44 ts=2026-10-08T13:52:37.9840000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7262] _id=6ace34fade269131f9cecace ts=2026-10-13T13:41:14.0140000Z; 48h 12m: 6ab9a88e9a8420a1e6b56aee.jsonl[594] _id=6ac4fa05de269131f9b105af ts=2026-10-06T13:39:16.7780000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6046] _id=6ac79fe6de269131f9c11d5b ts=2026-10-08T13:51:33.5510000Z; 47h 48m: 6ab9a88e9a8420a1e6b56aee.jsonl[7358] _id=6ace3569de269131f9cecfee ts=2026-10-13T13:43:05.1540000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12287] _id=6ad0d5a3de269131f9daa37f ts=2026-10-15T13:31:14.8050000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.048s..0.048s shown 
  - Evidence: 48ms: 6ab9a88e9a8420a1e6b56aee.jsonl[12492] _id=6ad0d647de269131f9dab3a9 ts=2026-10-15T13:33:58.5240000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12496] _id=6ad0d647de269131f9dab3ac ts=2026-10-15T13:33:58.5720000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56aee.jsonl[6103] _id=6ac7a023de269131f9c12952 ts=2026-10-08T13:52:34.5030000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7260] _id=6ace34f6de269131f9ceca7b ts=2026-10-13T13:41:10.6470000Z; 48h 12m: 6ab9a88e9a8420a1e6b56aee.jsonl[593] _id=6ac4fa00de269131f9b104a6 ts=2026-10-06T13:39:11.7800000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6041] _id=6ac79fe2de269131f9c11c23 ts=2026-10-08T13:51:29.2380000Z; 47h 48m: 6ab9a88e9a8420a1e6b56aee.jsonl[7353] _id=6ace3568de269131f9cecfd4 ts=2026-10-13T13:43:03.8170000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12251] _id=6ad0d5a0de269131f9daa34a ts=2026-10-15T13:31:11.2460000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 27 interval(s) ≤ 0.006s..0.021s shown 
  - Evidence: 6ms: 6ab9a88e9a8420a1e6b56aee.jsonl[7350] _id=6ace3567de269131f9cecfcc ts=2026-10-13T13:43:02.9610000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7351] _id=6ace3567de269131f9cecfce ts=2026-10-13T13:43:02.9670000Z; 7ms: 6ab9a88e9a8420a1e6b56aee.jsonl[14489] _id=6ad2251ede269131f9e3875f ts=2026-10-16T13:22:38.1460000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[14490] _id=6ad2251ede269131f9e38761 ts=2026-10-16T13:22:38.1530000Z; 21ms: 6ab9a88e9a8420a1e6b56aee.jsonl[529] _id=6ac4f97ade269131f9b0eac0 ts=2026-10-06T13:36:57.7270000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[532] _id=6ac4f97ade269131f9b0eacc ts=2026-10-06T13:36:57.7480000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 168h 3m 
  - Evidence: 168h 3m: 6ab9a88e9a8420a1e6b56aee.jsonl[579] _id=6ac4f9e9de269131f9b0ffa8 ts=2026-10-06T13:38:49.2940000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7331] _id=6ace354cde269131f9cecec7 ts=2026-10-13T13:42:36.3050000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 53m 
  - Evidence: 143h 53m: 6ab9a88e9a8420a1e6b56aee.jsonl[4268] _id=6ac64e9dde269131f9ba10c5 ts=2026-10-07T13:52:28.4030000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[7470] _id=6ace3605de269131f9ced66c ts=2026-10-13T13:45:41.2430000Z; 48h 0m: 6ab9a88e9a8420a1e6b56aee.jsonl[7476] _id=6ace3607de269131f9ced689 ts=2026-10-13T13:45:43.2000000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[12949] _id=6ad0d93cde269131f9db07ad ts=2026-10-15T13:46:35.2590000Z; 23h 24m: 6ab9a88e9a8420a1e6b56aee.jsonl[12949] _id=6ad0d93cde269131f9db07ad ts=2026-10-15T13:46:35.2590000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[13889] _id=6ad22263de269131f9e350b0 ts=2026-10-16T13:10:59.2870000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a88e9a8420a1e6b56aee.jsonl[6193] _id=6ac7a103de269131f9c14aa0 ts=2026-10-08T13:56:18.8500000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6225] _id=6ace2f80de269131f9ce905a ts=2026-10-13T13:17:52.2330000Z; 24h 4m: 6ab9a88e9a8420a1e6b56aee.jsonl[2275] _id=6ac64826de269131f9b8ea8f ts=2026-10-07T13:24:52.8590000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5378] _id=6ac79ac0de269131f9c03c19 ts=2026-10-08T13:29:35.0880000Z; 23h 54m: 6ab9a88e9a8420a1e6b56aee.jsonl[6225] _id=6ace2f80de269131f9ce905a ts=2026-10-13T13:17:52.2330000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[8393] _id=6acf7fbdde269131f9d2d087 ts=2026-10-14T13:12:28.9270000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a88e9a8420a1e6b56aee.jsonl[6192] _id=6ac7a103de269131f9c14a9f ts=2026-10-08T13:56:18.8500000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6224] _id=6ace2f80de269131f9ce9059 ts=2026-10-13T13:17:52.2330000Z; 24h 0m: 6ab9a88e9a8420a1e6b56aee.jsonl[2459] _id=6ac6492ade269131f9b92709 ts=2026-10-07T13:29:13.5560000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5377] _id=6ac79ac0de269131f9c03c18 ts=2026-10-08T13:29:35.0880000Z; 23h 54m: 6ab9a88e9a8420a1e6b56aee.jsonl[6224] _id=6ace2f80de269131f9ce9059 ts=2026-10-13T13:17:52.2330000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[8392] _id=6acf7fbdde269131f9d2d086 ts=2026-10-14T13:12:28.9270000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6ab9a88e9a8420a1e6b56aee.jsonl[5375] _id=6ac79ac0de269131f9c03c13 ts=2026-10-07T14:00:57.062Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[8395] _id=6acf7fbdde269131f9d2d07f ts=2026-10-13T14:00:03.142Z; 23h 59m: 6ab9a88e9a8420a1e6b56aee.jsonl[11240] _id=6acf8ae5de269131f9d3cda0 ts=2026-10-14T14:00:03.5970000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[13868] _id=6ad0dc4bde269131f9db680d ts=2026-10-15T13:59:38.6920000Z; 23h 29m: 6ab9a88e9a8420a1e6b56aee.jsonl[8395] _id=6acf7fbdde269131f9d2d07f ts=2026-10-13T14:00:03.142Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[9440] _id=6acf83c0de269131f9d31942 ts=2026-10-14T13:29:36.2830000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[13868] _id=6ad0dc4bde269131f9db680d ts=2026-10-15T13:59:38.6920000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[13870] _id=6ad221f7de269131f9e34e68 ts=2026-10-15T13:59:38.692Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 24m 
  - Evidence: 119h 24m: 6ab9a88e9a8420a1e6b56aee.jsonl[6186] _id=6ac7a0efde269131f9c14879 ts=2026-10-08T13:55:58.1860000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[6269] _id=6ace3033de269131f9ce9743 ts=2026-10-13T13:20:51.1480000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aee.jsonl[5327] _id=6ac6500bde269131f9ba3802 ts=2026-10-07T13:58:34.6350000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[5385] _id=6ac79acdde269131f9c03d6b ts=2026-10-08T13:29:47.6340000Z; 23h 26m: 6ab9a88e9a8420a1e6b56aee.jsonl[2191] _id=6ac4fe7dde269131f9b2232f ts=2026-10-06T13:58:21.3130000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[2280] _id=6ac64832de269131f9b8eca1 ts=2026-10-07T13:25:04.7390000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aee.jsonl[14547] _id=6ad22572de269131f9e38dad ts=2026-10-16T13:24:02.5500000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[14548] _id=6ad22572de269131f9e38dae ts=2026-10-16T13:24:02.5500000Z; 1ms: 6ab9a88e9a8420a1e6b56aee.jsonl[14153] _id=6ad2232ade269131f9e35ec0 ts=2026-10-16T13:14:18.0800000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[14154] _id=6ad2232ade269131f9e35ec1 ts=2026-10-16T13:14:18.0810000Z; 2ms: 6ab9a88e9a8420a1e6b56aee.jsonl[482] _id=6ac4f922de269131f9b0d957 ts=2026-10-06T13:35:29.5120000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[448] _id=6ac4f922de269131f9b0d95f ts=2026-10-06T13:35:29.5140000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 16m 
  - Evidence: 23h 16m: 6ab9a88e9a8420a1e6b56aee.jsonl[10989] _id=6acf8a35de269131f9d3aa4f ts=2026-10-14T13:57:08.6360000Z -> 6ab9a88e9a8420a1e6b56aee.jsonl[11404] _id=6ad0d16fde269131f9da51c8 ts=2026-10-15T13:13:18.9310000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[419] _id=6ac4f8dede269131f9b0d063 ts=2026-10-06T13:34:22.4960000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[606] _id=6ac4fa1fde269131f9b10b39 ts=2026-10-06T13:39:43.2320000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2759] _id=6ac64b12de269131f9b9a13a ts=2026-10-07T13:37:20.8440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 40 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[1240] _id=6ac4fc4ede269131f9b18520 ts=2026-10-06T13:49:00.7890000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[1198] _id=6ac4fc4fde269131f9b18545 ts=2026-10-06T13:49:00.7920000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[0] _id=6ac4fc4fde269131f9b18555 ts=2026-10-06T13:49:01.0220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 117 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[1023] _id=6ac4fc37de269131f9b17c60 ts=2026-10-06T13:46:51.5160000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[1014] _id=6ac4fc37de269131f9b17c67 ts=2026-10-06T13:46:51.5250000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[891] _id=6ac4fbd5de269131f9b1639c ts=2026-10-06T13:46:58.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[7358] _id=6ace3569de269131f9cecfee ts=2026-10-13T13:43:05.1540000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[12496] _id=6ad0d647de269131f9dab3ac ts=2026-10-15T13:33:58.5720000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[532] _id=6ac4f97ade269131f9b0eacc ts=2026-10-06T13:36:57.7480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[12949] _id=6ad0d93cde269131f9db07ad ts=2026-10-15T13:46:35.2590000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[13889] _id=6ad22263de269131f9e350b0 ts=2026-10-16T13:10:59.2870000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[14270] _id=6ad223bdde269131f9e3695a ts=2026-10-16T13:16:45.3910000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[11268] _id=6ad0d10dde269131f9da4f57 ts=2026-10-15T13:11:40.9070000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[14150] _id=6ad2232ade269131f9e35ebd ts=2026-10-16T13:14:18.0410000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[14152] _id=6ad2232ade269131f9e35ebf ts=2026-10-16T13:14:18.0590000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[9601] _id=6acf85b7de269131f9d33c48 ts=2026-10-14T13:37:59.0170000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 232 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[1085] _id=6ac4fc53de269131f9b186da ts=2026-10-06T13:49:06.6160000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[1095] _id=6ac4fc55de269131f9b1874e ts=2026-10-06T13:49:08.1890000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[1200] _id=6ac4fc57de269131f9b1882a ts=2026-10-06T13:49:10.7140000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 414 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[877] _id=6ac4fbd4de269131f9b1634f ts=2026-10-06T13:46:58.1450000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[879] _id=6ac4fbd4de269131f9b16352 ts=2026-10-06T13:46:58.1450000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[907] _id=6ac4fbd9de269131f9b16474 ts=2026-10-06T13:47:04.1720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 41 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[2206] _id=6ac4fe98de269131f9b22a64 ts=2026-10-06T13:58:48.1010000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2208] _id=6ac4fe99de269131f9b22a9f ts=2026-10-06T13:58:48.1270000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[2249] _id=6ac4fed6de269131f9b23832 ts=2026-10-06T13:59:50.0380000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[583] _id=6ac4f9e8de269131f9b0ff6c ts=2026-10-06T13:38:48.3770000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[7330] _id=6ace354fde269131f9cecef1 ts=2026-10-13T13:42:38.8270000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[7335] _id=6ace3552de269131f9cecf13 ts=2026-10-13T13:42:42.0640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Open' (totals: 18 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 431 start, 426 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 46 unmatched 'BecameCameraCentered' (totals: 776 open, 770 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 82 unmatched 'BecameVisible' (totals: 878 open, 913 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 43 open, 41 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 7 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 46 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 595 of 14818 adjacent _id pairs reverse in client time; worst 106.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56aee.jsonl[1003] _id=6ac4fc34de269131f9b17b9d ts=2026-10-06T13:48:36.1860000Z`; `6ab9a88e9a8420a1e6b56aee.jsonl[997] _id=6ac4fc35de269131f9b17be0 ts=2026-10-06T13:46:49.6140000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.86s, min -84518.98s, max -0.09s over 14819 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56aee\coverage.yaml

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

### `InputEvent` — 6654 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1734); Unit 4 Dev - Dungeon (1198); Unit 3 Dev (1107); Unit 3 Dungeon Dev (814); Unit 5 Dev - Dungeon (808); Unit 4 Dev (510); Unit 1 Dev (270); Unit 5 Dev (169); Unit 4 Dev - Anderson Base (44)
- **Intervals:** median 0.47s (p5 0.05s / p95 5.78s, n=6653)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6654/6654 records)
    "pressed"  x6654
data.actionType  (string, 6654/6654 records)
    "Move"  x5143
    "Sprint"  x670
    "Interact"  x417
    "Jump"  x274
    "Ascend"  x50
    "Map"  x39
    "Descend"  x22
    "Hoverboard"  x22
    "Pause"  x13
    "ToggleDebug"  x4
data.key  (string, 6654/6654 records, 25 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6654/6654 records)
    "Player"  x6163
    "Drone"  x491
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3337 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2395); Unit 4 Dev (466); Unit 3 Dungeon Dev (256); Unit 5 Dev - Dungeon (220)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.41s, n=3336)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3337/3337 records)
    "BecameInvisible"  x913
    "BecameVisible"  x878
    "BecameCameraCentered"  x776
    "BecameCameraUncentered"  x770
data.pieceId  (string, 3337/3337 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3337/3337 records)
    1906 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2212 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (619); Unit 3 Dev (364); Unit 4 Dev (253); Unit 5 Dev (213); Unit 1 Dev (200); Unit 3 Dungeon Dev (199); Unit 4 Dev - Dungeon (168); Unit 4 Dev - Anderson Base (102); Unit 5 Dev - Dungeon (94)
- **eventKey:** present on 1355 of 2212 records
- **Intervals:** median 3.45s (p5 0.00s / p95 23.66s, n=2211)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1355; [conversationId, dialogueEventType] x857
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2212/2212 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2212/2212 records)
    "DialogueNodeEvent"  x1355
    "DialogueStartEvent"  x431
    "DialogueFinishEvent"  x426
data.nodeId  (number, 1355/2212 records)
    numeric range 0 .. 290 (222 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1552 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (455); Unit 3 Dev (256); Unit 4 Dev (169); Unit 1 Dev (156); Unit 4 Dev - Dungeon (128); Unit 3 Dungeon Dev (124); Unit 5 Dev - Dungeon (111); Unit 5 Dev (105); Unit 4 Dev - Anderson Base (48)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.27s, n=1540)
- **Fields under `data`:**

```text
data.position  (object, 1552/1552 records)
data.position.x  (number, 1552/1552 records)
    numeric range -687.4 .. 1556.47 (648 unique)
data.position.y  (number, 1552/1552 records)
    numeric range -114.951 .. 222.252 (470 unique)
data.position.z  (number, 1552/1552 records)
    numeric range -1039.07 .. 2003.47 (648 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 293 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (93); Unit 3 Dev (57); Unit 1 Dev (56); Unit 2 Prod (Refactor) (49); Unit 5 Dev (38)
- **Intervals:** median 0.82s (p5 0.03s / p95 9.18s, n=292)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 293/293 records)
    "argumentationNodeHoverEnd"  x125
    "argumentationNodeHoverStart"  x124
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 293/293 records)
    "Unit 4 - Flooding"  x93
    "Unit 3 - Pollution Upstream"  x57
    "Unit 2 – Watershed"  x49
    "Unit 5"  x38
    "Unit 1 - Argumentation Tutorial"  x35
    "Unit 1 - Freshwater"  x21
data.nodeName  (string, 293/293 records)
    "A"  x45
    "1"  x43
    "I"  x39
    "II"  x33
    "B"  x26
    "4"  x24
    "D"  x24
    "C"  x22
    "2"  x19
    "3"  x15
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 258 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (92); Unit 2 Prod (Refactor) (48); Unit 3 Dungeon Dev (43); Unit 4 Dev (20); Unit 5 Dev - Dungeon (18); Unit 1 Dev (11); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (6)
- **Intervals:** median 10.70s (p5 1.59s / p95 345.25s, n=257)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 258/258 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 258/258 records)
    105 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 117 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (60); Unit 3 Dev (57)
- **Intervals:** median 3.38s (p5 0.59s / p95 367.02s, n=116)
- **`data` key-set variants:** [actionType, featureUsed] x84; [actionType, featureUsed, location] x33
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 117/117 records)
    "MapOpenEvent"  x43
    "MapCloseEvent"  x41
    "WaypointMoveEvent"  x27
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x2
data.featureUsed  (string, 117/117 records)
    "Map"  x84
    "Waypoint"  x33
data.location  (object, 33/117 records)
data.location.x  (number, 33/117 records)
    numeric range -271.591 .. 106.578 (25 unique)
data.location.y  (number, 33/117 records)
    numeric range -285.829 .. 213.34 (30 unique)
data.location.z  (number, 33/117 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 85 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 4 Dev - Dungeon (15); Unit 1 Dev (12); Unit 5 Dev - Dungeon (12); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 85 of 85 records
- **Intervals:** median 148.91s (p5 0.01s / p95 83674.58s, n=84)
- **`data` key-set variants:** [questEventType, questID, questName] x46; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 85/85 records)
    "questActiveEvent"  x46
    "questFinishEvent"  x39
data.questID  (string, 85/85 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 85/85 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/85 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 80 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (51); Unit 3 Dev (16); Unit 4 Dev (13)
- **Intervals:** median 2.07s (p5 0.17s / p95 8628.70s, n=79)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x72; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/80 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/80 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 72/80 records)
    "RightDrag"  x37
    "LeftDrag"  x35
data.currentSoilType  (string, 72/80 records)
    "CLAY"  x18
    "CLAYSAND"  x14
    "CLAYROCK"  x13
    "SAND"  x11
    "SANDGRAVEL"  x8
    "BEDROCK"  x5
    "GRAVEL"  x3
data.isCorrectSelection  (string, 72/80 records)
    "false"  x55
    "true"  x17
data.waterLevelStatus  (string, 72/80 records)
    "TooHigh"  x40
    "Proper"  x31
    "TooLow"  x1
data.waterRetentionChange  (string, 72/80 records)
    "Increase"  x38
    "Decrease"  x17
    "NoChange"  x17
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 47 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (47)
- **Intervals:** median 8.13s (p5 1.11s / p95 78.87s, n=46)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "On"  x32
    "Off"  x15
data.floor  (string, 47/47 records)
    "4"  x26
    "3"  x16
    "2"  x3
    "1"  x2
data.machineNumber  (string, 47/47 records)
    "One"  x45
    "Two"  x2
data.machineType  (string, 47/47 records)
    "Condenser"  x27
    "Evaporator"  x13
    "VentSwitch"  x3
    "DualChamber_Condenser"  x2
    "DualChamber_Evaporator"  x2
data.room  (string, 47/47 records)
    "2"  x25
    "3"  x11
    "1"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DaniEvent` — 34 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 4 Dev (10); Unit 3 Dev (4); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 3.40s (p5 0.01s / p95 86039.75s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "Open"  x18
    "Close"  x16
data.toolName  (string, 34/34 records, 29 empty-string)
    ""  x29
    "Settings"  x5
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `DEBUGMenu` — 27 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 528.74s (p5 7.34s / p95 86323.96s, n=26)
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "DebugMenuStateChanged"  x27
data.isOpened  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 21 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (12); Unit 4 Dev (4); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1001.53s (p5 41.80s / p95 103585.12s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (10); Unit 3 Dev (4); Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 5 Dev (1)
- **Intervals:** median 16.13s (p5 7.79s / p95 225154.54s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    13 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x10
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 75.49s (p5 0.06s / p95 276648.48s, n=13)
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

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 401.20s (p5 2.13s / p95 280762.04s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 12 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (12)
- **Intervals:** median 84162.48s (p5 676.00s / p95 258187.81s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    true  x12
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 3 Dev (4)
- **Intervals:** median 2.48s (p5 0.84s / p95 393307.13s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x7
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 9 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 175.98s (p5 2.02s / p95 397193.57s, n=8)
- **`data` key-set variants:** [actionType, chatID] x8; [actionKey, chatID] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 1/9 records)
    "ScrollStop"  x1
data.actionType  (string, 8/9 records)
    "Close"  x5
    "Open"  x2
    "ScrollStart"  x1
data.chatID  (string, 9/9 records)
    "NA"  x6
    "[15-11, 15-12, 15-13, 15-14, 15-15]"  x1
    "[18-117, 18-243, 18-118, 74-0, 74-4]"  x1
    "[19-0, 19-1, 19-49, 19-2, 19-59, 19-50, 19-51]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 1.64s (p5 1.18s / p95 3.69s, n=7)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x7; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "optionSelected"  x7
    "DesignSubmitted"  x1
data.designSelections  (object, 1/8 records)
data.designSelections.glassRoofTemperature  (string, 1/8 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/8 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/8 records)
    "Tilted Out"  x1
data.featureUsed  (string, 8/8 records)
    "ExtraCovering"  x3
    "RoofStyle"  x3
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 7/8 records, 2 empty-string)
    ""  x2
    "Cold"  x1
    "Covered"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 80.67s (p5 14.29s / p95 58691.02s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Gravel"  x3
    "Sand"  x3
    "Clay"  x2
data.floor  (string, 8/8 records)
    "5"  x4
    "3"  x2
    "4"  x2
data.machine  (string, 8/8 records)
    "1"  x6
    "2"  x2
data.row  (string, 8/8 records)
    "TopRow"  x7
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 4.57s (p5 1.34s / p95 19.50s, n=5)
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
- **Intervals:** median 130415.57s (p5 85917.45s / p95 465515.18s, n=4)
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

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (51 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (27x); "WaypointResetEvent" (2x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (33x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*