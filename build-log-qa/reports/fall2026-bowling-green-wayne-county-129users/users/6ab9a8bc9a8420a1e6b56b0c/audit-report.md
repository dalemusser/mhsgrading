# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b0c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b0c
- **Game version string(s) in log:** 2.8.4, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b0c.jsonl
- **Records:** 13529 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b0c
- **Time span:** 2026-10-05T15:16:03.767000+00:00 .. 2026-10-18T17:28:09.663000+00:00 (314h 12m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b0c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13529 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 100 INFO, 0 NOT_TESTED, 102 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3804 | 28.12 | 1 | 4 | 0 | 2026-10-08T15:21:40.105000+00:00 | 2026-10-16T15:34:58.908000+00:00 | 192h 13m |
| InputEvent | 3387 | 25.04 | 1 | 9 | 0 | 2026-10-05T15:22:14.205000+00:00 | 2026-10-18T17:28:09.663000+00:00 | 314h 5m |
| PlayerPositionEvent | 2626 | 19.41 | 1 | 9 | 0 | 2026-10-05T15:16:16.073000+00:00 | 2026-10-18T17:28:01.258000+00:00 | 314h 11m |
| DialogueEvent | 2414 | 17.84 | 1 | 9 | 1500 | 2026-10-05T15:16:33.897000+00:00 | 2026-10-18T17:28:01.646000+00:00 | 314h 11m |
| argumentationNodeEvent | 433 | 3.2 | 1 | 5 | 0 | 2026-10-07T15:35:03.911000+00:00 | 2026-10-18T17:13:24.062000+00:00 | 265h 38m |
| ObjectInterEvent | 286 | 2.11 | 1 | 9 | 0 | 2026-10-05T15:36:06.506000+00:00 | 2026-10-18T17:28:09.663000+00:00 | 313h 52m |
| questEvent | 111 | 0.82 | 1 | 9 | 111 | 2026-10-05T15:16:33.875000+00:00 | 2026-10-18T17:23:48.112000+00:00 | 314h 7m |
| WaterChamberEvent | 108 | 0.8 | 1 | 1 | 0 | 2026-10-16T15:33:08.879000+00:00 | 2026-10-18T17:05:33.526000+00:00 | 49h 32m |
| TopographicMapEvent | 72 | 0.53 | 1 | 2 | 0 | 2026-10-08T15:22:10.258000+00:00 | 2026-10-15T01:47:36.267000+00:00 | 154h 25m |
| Soil Key Puzzle | 58 | 0.43 | 1 | 3 | 0 | 2026-10-13T15:37:35.123000+00:00 | 2026-10-15T15:15:28.624000+00:00 | 47h 37m |
| DEBUGMenu | 45 | 0.33 | 1 | 9 | 0 | 2026-10-05T15:16:16.065000+00:00 | 2026-10-18T17:00:41.190000+00:00 | 313h 44m |
| argumentationAnswerEvent | 38 | 0.28 | 1 | 5 | 0 | 2026-10-07T15:35:19.574000+00:00 | 2026-10-18T17:13:25.239000+00:00 | 265h 38m |
| gameStartEvent | 21 | 0.16 | 1 | 1 | 0 | 2026-10-05T15:16:03.768000+00:00 | 2026-10-18T17:00:35.829000+00:00 | 313h 44m |
| gameWindowFocusEvent | 21 | 0.16 | 1 | 1 | 0 | 2026-10-05T15:16:03.767000+00:00 | 2026-10-18T17:00:35.829000+00:00 | 313h 44m |
| TerasGardenBox | 19 | 0.14 | 1 | 1 | 0 | 2026-10-16T15:12:52.422000+00:00 | 2026-10-16T15:20:19.622000+00:00 | 7m 27s |
| chatEvent | 17 | 0.13 | 1 | 4 | 0 | 2026-10-13T15:27:01.727000+00:00 | 2026-10-18T17:06:29.789000+00:00 | 121h 39m |
| argumentationEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-10-07T15:34:56.284000+00:00 | 2026-10-18T17:13:25.264000+00:00 | 265h 38m |
| DaniEvent | 12 | 0.09 | 1 | 2 | 0 | 2026-10-13T15:26:57.829000+00:00 | 2026-10-15T01:46:18.784000+00:00 | 34h 19m |
| soilMachine | 12 | 0.09 | 1 | 1 | 0 | 2026-10-15T15:32:37.002000+00:00 | 2026-10-15T15:42:27.601000+00:00 | 9m 50s |
| argumentationToolEvent | 10 | 0.07 | 1 | 3 | 0 | 2026-10-07T15:34:53.124000+00:00 | 2026-10-15T00:39:04.568000+00:00 | 177h 4m |
| gameWindowUnfocusEvent | 8 | 0.06 | 1 | 4 | 0 | 2026-10-05T15:33:48.597000+00:00 | 2026-10-16T18:24:03.149000+00:00 | 266h 50m |
| SolarStillDesignEvent | 7 | 0.05 | 1 | 1 | 0 | 2026-10-18T17:20:47.292000+00:00 | 2026-10-18T17:21:05.529000+00:00 | 18.2s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-07T15:41:17.075000+00:00 | 2026-10-18T17:28:09.648000+00:00 | 265h 46m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 157572.507s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.834s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 20.517s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.045s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.929s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 10.219s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 134.249s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 7.99s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6913.568s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 6913.567s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86381.852s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 8.451s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.8x vs baseline. 
  - Observed: 45 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; press; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 5.4x vs baseline. 
  - Observed: 108 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.6x vs baseline. 
  - Observed: 38 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,4,I; A,D,1,I; B,2,II; B,A,2,II; B,C,D,2,II; C,2,II; C,D,2,II; C,D,3,II; C,D,A,2,II; C,D,B,2,II; D,1,I; D,1,II; D,2,II; D,C,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 433 records 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 8.5x vs baseline. 
  - Observed: 17 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [19-0, 19-1, 19-49, 19-2, 19-59, 19-50, 19-51]; [28-194, 28-194, 28-194, 28-194, 28-194]; [73-200, 73-204, 73-208, 73-209, 73-210, 73-211, 73-212]; [73-208, 73-209, 73-210, 73-211, 73-212]; [83-10, 83-11, 73-200, 73-204, 73-208, 73-209] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[540] _id=6ac3c47fde269131f9ad535d ts=2026-10-05T15:38:39.0180000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[677] _id=6ac3c610de269131f9ad6ae9 ts=2026-10-05T15:45:19.9670000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[885] _id=6ac5179cde269131f9b4b1e3 ts=2026-10-06T15:45:31.2610000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[1] _id=6ac3bf34de269131f9ace755 ts=2026-10-05T15:16:03.7680000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[456] _id=6ac3c392de269131f9ad42e5 ts=2026-10-05T15:34:41.3320000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[733] _id=6ac515ecde269131f9b48a69 ts=2026-10-06T15:38:19.2810000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[0] _id=6ac3bf34de269131f9ace753 ts=2026-10-05T15:16:03.7670000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[455] _id=6ac3c392de269131f9ad42e3 ts=2026-10-05T15:34:41.3320000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[734] _id=6ac515ecde269131f9b48a67 ts=2026-10-06T15:38:19.2800000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[454] _id=6ac3c35dde269131f9ad4011 ts=2026-10-05T15:33:48.5970000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[732] _id=6ac515ecde269131f9b48a5f ts=2026-10-05T15:48:02.449Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[915] _id=6ac662bbde269131f9bb9986 ts=2026-10-06T15:47:44.301Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 72 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[1594] _id=6ac7b523de269131f9c392c8 ts=2026-10-08T15:22:10.2580000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[1607] _id=6ac7b53bde269131f9c3954e ts=2026-10-08T15:22:34.4080000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[3806] _id=6ac7ba8bde269131f9c41e7d ts=2026-10-08T15:45:14.2500000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3803 | 0.0 | 0.045 | 181.961 | 2.244 | 431216.344 | 0.33 | 2034 | 9 |
| InputEvent | 3386 | 0.0 | 1.834 | 333.95 | 25.492 | 429685.55 | 0.18 | 101 | 15 |
| PlayerPositionEvent | 2614 | 9.785 | 10.0 | 414.399 | 10.033 | 429570.64 | 0.14 | 0 | 12 |
| DialogueEvent | 2413 | 0.0 | 4.001 | 468.748 | 37.24 | 429670.503 | 0.13 | 702 | 15 |
| argumentationNodeEvent | 432 | 0.014 | 0.483 | 2213.658 | 7.154 | 635527.728 | 0.03 | 91 | 4 |
| ObjectInterEvent | 285 | 0.0 | 20.517 | 3964.643 | 1266.224 | 432222.727 | 0.02 | 7 | 16 |
| questEvent | 110 | 0.0 | 174.278 | 10280.311 | 82342.208 | 429599.78 | 0.01 | 30 | 20 |
| WaterChamberEvent | 107 | 0.124 | 10.987 | 1666.772 | 64.528 | 167840.058 | 0.04 | 0 | 3 |
| TopographicMapEvent | 71 | 0.011 | 6.929 | 7829.944 | 4131.747 | 429761.76 | 0.01 | 4 | 7 |
| Soil Key Puzzle | 57 | 0.167 | 1.1 | 3008.307 | 15.832 | 119132.679 | 0.02 | 0 | 2 |
| DEBUGMenu | 44 | 4.039 | 565.138 | 25669.662 | 86934.189 | 431116.531 | 0.0 | 0 | 21 |
| argumentationAnswerEvent | 37 | 0.234 | 10.219 | 25845.559 | 146784.461 | 635583.161 | 0.0 | 0 | 4 |
| gameStartEvent | 20 | 90.144 | 6913.568 | 56473.603 | 181464.063 | 431123.909 | 0.0 | 0 | 19 |
| gameWindowFocusEvent | 20 | 90.144 | 6913.567 | 56473.603 | 181464.064 | 431123.909 | 0.0 | 0 | 19 |
| TerasGardenBox | 18 | 0.899 | 3.591 | 24.844 | 70.655 | 288.67 | 2.42 | 0 | 0 |
| chatEvent | 16 | 0.342 | 7.99 | 27373.004 | 143883.396 | 168243.024 | 0.0 | 0 | 5 |
| argumentationEvent | 13 | 0.023 | 134.249 | 73562.229 | 362334.569 | 635506.569 | 0.0 | 2 | 4 |
| DaniEvent | 11 | 1.73 | 4.563 | 11232.814 | 59182.059 | 86156.409 | 0.01 | 0 | 3 |
| soilMachine | 11 | 0.182 | 8.451 | 53.691 | 167.364 | 168.183 | 1.12 | 0 | 0 |
| argumentationToolEvent | 9 | 0.258 | 24.632 | 70827.938 | 382012.097 | 635589.171 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 7 | 853.852 | 86381.852 | 137230.65 | 404796.599 | 518444.739 | 0.0 | 0 | 7 |
| SolarStillDesignEvent | 6 | 1.083 | 1.801 | 3.04 | 6.275 | 6.567 | 19.74 | 0 | 0 |
| EndOfUnit | 4 | 5966.632 | 157572.507 | 239203.143 | 567343.772 | 635700.928 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 9 group(s), 36 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[3824] _id=6ace489fde269131f9cf03a4 ts=2026-10-13T15:05:01.2360000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[3825] _id=6ace489fde269131f9cf03a5 ts=2026-10-13T15:05:01.2360000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[3826] _id=6ace489fde269131f9cf03a6 ts=2026-10-13T15:05:01.2370000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[3827] _id=6ace489fde269131f9cf03a7 ts=2026-10-13T15:05:01.2370000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[3828] _id=6ace489fde269131f9cf03a8 ts=2026-10-13T15:05:01.2380000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[3829] _id=6ace489fde269131f9cf03a9 ts=2026-10-13T15:05:01.2380000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 44 group(s), 59 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[1579] _id=6ac7b50ade269131f9c39004 ts=2026-10-08T15:21:44.9520000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[1580] _id=6ac7b50ade269131f9c39008 ts=2026-10-08T15:21:44.9520000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[1578] _id=6ac7b50ade269131f9c3900c ts=2026-10-08T15:21:44.9720000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[1583] _id=6ac7b50ade269131f9c39013 ts=2026-10-08T15:21:44.9720000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[1644] _id=6ac7b57dde269131f9c39b2b ts=2026-10-08T15:23:39.5730000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[1637] _id=6ac7b57dde269131f9c39b32 ts=2026-10-08T15:23:39.5730000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[13274] _id=6ad4fe7bde269131f9e8b4c7 ts=2026-10-18T17:14:34.6870000Z == 6ab9a8bc9a8420a1e6b56b0c.jsonl[13275] _id=6ad4fe7bde269131f9e8b4c8 ts=2026-10-18T17:14:34.6870000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[486] _id=6ac3c3e7de269131f9ad4845 ts=2026-10-05T15:36:06.5060000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[488] _id=6ac3c3e7de269131f9ad484b ts=2026-10-05T15:36:06.5130000Z`; `4ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[847] _id=6ac51714de269131f9b4a5b1 ts=2026-10-06T15:43:15.2670000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[845] _id=6ac51714de269131f9b4a5b4 ts=2026-10-06T15:43:15.2710000Z`; `4ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[931] _id=6ac662f0de269131f9bb9a44 ts=2026-10-07T15:19:11.4760000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[932] _id=6ac662f0de269131f9bb9a46 ts=2026-10-07T15:19:11.4800000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `434ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12341] _id=6ad2453ade269131f9e5577b ts=2026-10-16T15:39:37.9640000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[12295] _id=6ad2453ade269131f9e55785 ts=2026-10-16T15:39:38.3980000Z`; `365ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12293] _id=6ad2453ade269131f9e55781 ts=2026-10-16T15:39:38.1820000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[12343] _id=6ad2453ade269131f9e5578a ts=2026-10-16T15:39:38.5470000Z`; `336ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12373] _id=6ad24560de269131f9e558b3 ts=2026-10-16T15:40:16.0120000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[12375] _id=6ad24560de269131f9e558bc ts=2026-10-16T15:40:16.3480000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `966ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[6801] _id=6ad019edde269131f9d9bb03 ts=2026-10-15T00:10:20.5340000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[6802] _id=6ad019eede269131f9d9bb05 ts=2026-10-15T00:10:21.5000000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `46ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7653] _id=6ad020e8de269131f9d9d3e1 ts=2026-10-15T00:40:07.5890000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[7656] _id=6ad020e8de269131f9d9d3e4 ts=2026-10-15T00:40:07.6350000Z`; `23ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11470] _id=6ad23e10de269131f9e4f82f ts=2026-10-16T15:09:03.7520000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[11477] _id=6ad23e10de269131f9e4f832 ts=2026-10-16T15:09:03.7750000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 35 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `382ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1241] _id=6ac666f6de269131f9bc0148 ts=2026-10-07T15:36:21.5750000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[1242] _id=6ac666f6de269131f9bc014c ts=2026-10-07T15:36:21.9570000Z`; `600ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1235] _id=6ac666f9de269131f9bc0166 ts=2026-10-07T15:36:24.2570000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[1237] _id=6ac666f9de269131f9bc0173 ts=2026-10-07T15:36:24.8570000Z`; `384ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[6741] _id=6ad019a7de269131f9d9ba43 ts=2026-10-15T00:09:11.0500000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[6742] _id=6ad019a7de269131f9d9ba47 ts=2026-10-15T00:09:11.4340000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `258ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[6799] _id=6ad019eade269131f9d9bafb ts=2026-10-15T00:10:17.9440000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[6800] _id=6ad019eade269131f9d9bafd ts=2026-10-15T00:10:18.2020000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12653] _id=6ad24c77de269131f9e5a53e ts=2026-10-16T16:10:30.7640000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[12667] _id=6ad269b0de269131f9e6fafb ts=2026-10-16T16:10:30.764Z`; `0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12663] _id=6ad24c78de269131f9e5a546 ts=2026-10-16T16:10:30.7780000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[12668] _id=6ad269b0de269131f9e6fafc ts=2026-10-16T16:10:30.778Z`; `0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12664] _id=6ad24c78de269131f9e5a547 ts=2026-10-16T16:10:30.7880000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[12669] _id=6ad269b0de269131f9e6fafd ts=2026-10-16T16:10:30.788Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `268ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10281] _id=6ad0f326de269131f9dcb9bc ts=2026-10-15T15:37:09.9640000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[10286] _id=6ad0f326de269131f9dcb9c5 ts=2026-10-15T15:37:10.2320000Z`; `182ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10286] _id=6ad0f326de269131f9dcb9c5 ts=2026-10-15T15:37:10.2320000Z ~ 6ab9a8bc9a8420a1e6b56b0c.jsonl[10287] _id=6ad0f326de269131f9dcb9d0 ts=2026-10-15T15:37:10.4140000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1506] _id=6ac7b489de269131f9c38374 ts=2026-10-08T15:19:36.3210000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3819] _id=6ace4895de269131f9cf0381 ts=2026-10-13T15:04:52.8520000Z; 46h 43m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12678] _id=6ad26a08de269131f9e6fbfe ts=2026-10-16T18:16:38.2310000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12878] _id=6ad4fb34de269131f9e8b1bd ts=2026-10-18T17:00:35.7770000Z; 24h 9m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3818] _id=6ace489cde269131f9cf0396 ts=2026-10-13T15:04:59.7860000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[4814] _id=6acf9c6ade269131f9d47d21 ts=2026-10-14T15:14:49.5850000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 23h 55m 
  - Evidence: 23h 55m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[4183] _id=6ace4dc6de269131f9cf1cef ts=2026-10-13T15:27:01.5600000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[5523] _id=6acf9e52de269131f9d4a0b8 ts=2026-10-14T15:22:57.9690000Z; 8h 56m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[5527] _id=6acf9e56de269131f9d4a0e8 ts=2026-10-14T15:23:02.5320000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[7029] _id=6ad01c26de269131f9d9be18 ts=2026-10-15T00:19:50.2410000Z; 1h 25m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7032] _id=6ad01c36de269131f9d9be20 ts=2026-10-15T00:20:05.6860000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[9047] _id=6ad03046de269131f9da1c96 ts=2026-10-15T01:45:41.7230000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3813] _id=6ac7ba98de269131f9c41ed4 ts=2026-10-08T15:45:27.0150000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3866] _id=6ace48fede269131f9cf053c ts=2026-10-13T15:06:37.5180000Z; 46h 38m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12822] _id=6ad26b52de269131f9e700a7 ts=2026-10-16T18:22:10.2690000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12872] _id=6ad4fb41de269131f9e8b1cd ts=2026-10-18T17:00:49.3670000Z; 23h 51m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[707] _id=6ac3c670de269131f9ad72fb ts=2026-10-05T15:46:55.9980000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[740] _id=6ac515f4de269131f9b48ab7 ts=2026-10-06T15:38:27.8160000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 702 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11332] _id=6ad23da3de269131f9e4ed47 ts=2026-10-16T15:07:15.0220000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11333] _id=6ad23da3de269131f9e4ed48 ts=2026-10-16T15:07:15.0220000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11389] _id=6ad23dd4de269131f9e4f209 ts=2026-10-16T15:08:04.3350000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11390] _id=6ad23dd4de269131f9e4f20a ts=2026-10-16T15:08:04.3350000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11423] _id=6ad23deede269131f9e4f4a8 ts=2026-10-16T15:08:30.0530000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11424] _id=6ad23deede269131f9e4f4a9 ts=2026-10-16T15:08:30.0530000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 176h 35m 
  - Evidence: 176h 35m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1393] _id=6ac6681ede269131f9bc1519 ts=2026-10-07T15:41:17.0750000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6963] _id=6ad01b52de269131f9d9bd2d ts=2026-10-15T00:16:18.0030000Z; 49h 59m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11899] _id=6ad24297de269131f9e5391f ts=2026-10-16T15:28:23.0940000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[13526] _id=6ad501a9de269131f9e8b7b6 ts=2026-10-18T17:28:09.6480000Z; 37h 32m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[9226] _id=6ad032a1de269131f9da23ce ts=2026-10-15T01:55:44.6350000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11899] _id=6ad24297de269131f9e5391f ts=2026-10-16T15:28:23.0940000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3768] _id=6ac7ba28de269131f9c41b0f ts=2026-10-08T15:43:35.6850000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3823] _id=6ace489fde269131f9cf03a3 ts=2026-10-13T15:05:01.2350000Z; 46h 36m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12861] _id=6ad26bbcde269131f9e701de ts=2026-10-16T18:23:55.5990000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12867] _id=6ad4fb3ade269131f9e8b1c5 ts=2026-10-18T17:00:42.2210000Z; 23h 51m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[723] _id=6ac3c695de269131f9ad772f ts=2026-10-05T15:47:32.5550000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[742] _id=6ac51602de269131f9b48bc2 ts=2026-10-06T15:38:41.4200000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 101 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12867] _id=6ad4fb3ade269131f9e8b1c5 ts=2026-10-18T17:00:42.2210000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12868] _id=6ad4fb3ade269131f9e8b1c6 ts=2026-10-18T17:00:42.2210000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12868] _id=6ad4fb3ade269131f9e8b1c6 ts=2026-10-18T17:00:42.2210000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12869] _id=6ad4fb3ade269131f9e8b1c7 ts=2026-10-18T17:00:42.2210000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12869] _id=6ad4fb3ade269131f9e8b1c7 ts=2026-10-18T17:00:42.2210000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12870] _id=6ad4fb3ade269131f9e8b1c8 ts=2026-10-18T17:00:42.2210000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 120h 3m 
  - Evidence: 120h 3m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3614] _id=6ac7b7e1de269131f9c3ef14 ts=2026-10-08T15:33:52.4000000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[4351] _id=6ace5040de269131f9cf327b ts=2026-10-13T15:37:35.1270000Z; 46h 40m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12790] _id=6ad26b08de269131f9e6ffa3 ts=2026-10-16T18:20:55.8150000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12891] _id=6ad4fb62de269131f9e8b1ec ts=2026-10-18T17:01:22.6740000Z; 23h 55m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[676] _id=6ac3c610de269131f9ad6ae5 ts=2026-10-05T15:45:19.9560000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[768] _id=6ac51675de269131f9b49721 ts=2026-10-06T15:40:37.1700000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10960] _id=6ad106d2de269131f9de33de ts=2026-10-15T17:01:05.2560000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[10961] _id=6ad106d2de269131f9de33df ts=2026-10-15T17:01:05.2560000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11155] _id=6ad23c91de269131f9e4cd87 ts=2026-10-16T15:02:40.8410000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11156] _id=6ad23c91de269131f9e4cd88 ts=2026-10-16T15:02:40.8410000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11201] _id=6ad23cd2de269131f9e4d20f ts=2026-10-16T15:03:46.0510000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11202] _id=6ad23cd2de269131f9e4d210 ts=2026-10-16T15:03:46.0510000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3808] _id=6ac7ba9ade269131f9c41eeb ts=2026-10-08T15:45:29.1540000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3822] _id=6ace489fde269131f9cf03a2 ts=2026-10-13T15:04:59.7940000Z; 46h 36m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12862] _id=6ad26bbfde269131f9e701e0 ts=2026-10-16T18:23:59.3340000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12866] _id=6ad4fb3ade269131f9e8b1c4 ts=2026-10-18T17:00:41.1960000Z; 23h 50m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[729] _id=6ac3c6afde269131f9ad7863 ts=2026-10-05T15:47:58.7560000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[735] _id=6ac515f4de269131f9b48ab1 ts=2026-10-06T15:38:27.0340000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3575] _id=6ac7b7c1de269131f9c3eca2 ts=2026-10-08T15:33:19.5690000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[4086] _id=6ace4c31de269131f9cf109e ts=2026-10-13T15:20:15.9130000Z; 23h 27m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[4790] _id=6ace52aede269131f9cf4ae4 ts=2026-10-13T15:47:56.6780000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[4818] _id=6acf9c78de269131f9d47e33 ts=2026-10-14T15:15:03.2840000Z; 22h 34m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10695] _id=6ad10545de269131f9de0a53 ts=2026-10-15T16:54:27.1170000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11919] _id=6ad242c1de269131f9e53adc ts=2026-10-16T15:29:04.0970000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2034 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10484] _id=6ad0f4b4de269131f9dcd202 ts=2026-10-15T15:43:47.1700000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[10490] _id=6ad0f4b4de269131f9dcd206 ts=2026-10-15T15:43:47.1700000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10487] _id=6ad0f4b3de269131f9dcd1e5 ts=2026-10-15T15:43:46.3010000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[10488] _id=6ad0f4b3de269131f9dcd1e7 ts=2026-10-15T15:43:46.3010000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[10489] _id=6ad0f4b3de269131f9dcd1ea ts=2026-10-15T15:43:46.4020000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[10480] _id=6ad0f4b3de269131f9dcd1f5 ts=2026-10-15T15:43:46.4020000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 33h 5m 
  - Evidence: 33h 5m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[4392] _id=6ace50b7de269131f9cf379d ts=2026-10-13T15:39:34.7210000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[7776] _id=6ad02213de269131f9d9d90f ts=2026-10-15T00:45:07.4000000Z; 14h 29m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7790] _id=6ad02242de269131f9d9d9c6 ts=2026-10-15T00:45:53.8810000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[9309] _id=6ad0edfede269131f9dc629d ts=2026-10-15T15:15:10.0400000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3814] _id=6ac7ba98de269131f9c41ed5 ts=2026-10-08T15:45:27.0190000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3904] _id=6ace4959de269131f9cf06e7 ts=2026-10-13T15:08:08.7790000Z; 23h 46m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[4338] _id=6ace5005de269131f9cf305e ts=2026-10-13T15:36:36.3460000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[5522] _id=6acf9e4dde269131f9d4a079 ts=2026-10-14T15:22:52.7360000Z; 7h 48m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[5807] _id=6acfa0d6de269131f9d4bf89 ts=2026-10-14T15:33:42.5490000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6280] _id=6ad00e9fde269131f9d9a461 ts=2026-10-14T23:22:07.3990000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.011s..0.026s shown 
  - Evidence: 11ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3906] _id=6ace4966de269131f9cf0701 ts=2026-10-13T15:08:21.8380000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3907] _id=6ace4966de269131f9cf0702 ts=2026-10-13T15:08:21.8490000Z; 12ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3907] _id=6ace4966de269131f9cf0702 ts=2026-10-13T15:08:21.8490000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3911] _id=6ace4966de269131f9cf0706 ts=2026-10-13T15:08:21.8610000Z; 26ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3810] _id=6ac7ba98de269131f9c41ed1 ts=2026-10-08T15:45:26.9930000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3814] _id=6ac7ba98de269131f9c41ed5 ts=2026-10-08T15:45:27.0190000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 46h 37m 
  - Evidence: 46h 37m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12856] _id=6ad26badde269131f9e701d6 ts=2026-10-16T18:23:41.3170000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12887] _id=6ad4fb4dde269131f9e8b1dc ts=2026-10-18T17:01:01.3750000Z; 2h 6m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12650] _id=6ad24c61de269131f9e5a3d2 ts=2026-10-16T16:10:07.9710000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12691] _id=6ad26a1cde269131f9e6fc6c ts=2026-10-16T18:17:00.4340000Z; 18m 42s: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12562] _id=6ad24748de269131f9e5632f ts=2026-10-16T15:48:24.2630000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12580] _id=6ad24babde269131f9e59748 ts=2026-10-16T16:07:06.6360000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 176h 33m 
  - Evidence: 176h 33m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1275] _id=6ac66726de269131f9bc04dd ts=2026-10-07T15:37:09.9400000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6789] _id=6ad019e5de269131f9d9baf5 ts=2026-10-15T00:10:13.1010000Z; 50h 4m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11469] _id=6ad23e0fde269131f9e4f829 ts=2026-10-16T15:09:03.7390000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[13176] _id=6ad4fe28de269131f9e8b454 ts=2026-10-18T17:13:12.6400000Z; 38h 26m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7660] _id=6ad020e8de269131f9d9d3df ts=2026-10-15T00:40:07.5710000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11324] _id=6ad23d9ade269131f9e4ebeb ts=2026-10-16T15:07:05.9220000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 176h 31m 
  - Evidence: 176h 31m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1269] _id=6ac66726de269131f9bc04e8 ts=2026-10-07T15:37:09.9590000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6719] _id=6ad01999de269131f9d9ba1a ts=2026-10-15T00:08:56.5280000Z; 50h 3m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11477] _id=6ad23e10de269131f9e4f832 ts=2026-10-16T15:09:03.7750000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12967] _id=6ad4fe0bde269131f9e8b411 ts=2026-10-18T17:12:43.6770000Z; 38h 26m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7656] _id=6ad020e8de269131f9d9d3e4 ts=2026-10-15T00:40:07.6350000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11265] _id=6ad23d6bde269131f9e4e4ce ts=2026-10-16T15:06:19.3590000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.046s shown 
  - Evidence: 23ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11470] _id=6ad23e10de269131f9e4f82f ts=2026-10-16T15:09:03.7520000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11477] _id=6ad23e10de269131f9e4f832 ts=2026-10-16T15:09:03.7750000Z; 46ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7653] _id=6ad020e8de269131f9d9d3e1 ts=2026-10-15T00:40:07.5890000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[7656] _id=6ad020e8de269131f9d9d3e4 ts=2026-10-15T00:40:07.6350000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 176h 32m 
  - Evidence: 176h 32m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1267] _id=6ac66717de269131f9bc03ec ts=2026-10-07T15:36:54.2410000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6738] _id=6ad0199ede269131f9d9ba27 ts=2026-10-15T00:09:01.9690000Z; 50h 3m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11419] _id=6ad23e0dde269131f9e4f7df ts=2026-10-16T15:09:00.7620000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12968] _id=6ad4fe0dde269131f9e8b416 ts=2026-10-18T17:12:45.0940000Z; 38h 26m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7651] _id=6ad020e5de269131f9d9d3c7 ts=2026-10-15T00:40:05.2900000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11263] _id=6ad23d68de269131f9e4e452 ts=2026-10-16T15:06:15.9390000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 91 interval(s) ≤ 0.014s..0.017s shown 
  - Evidence: 14ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[7531] _id=6ad02066de269131f9d9cd88 ts=2026-10-15T00:37:57.7370000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[7532] _id=6ad02066de269131f9d9cd89 ts=2026-10-15T00:37:57.7510000Z; 17ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11279] _id=6ad23d73de269131f9e4e5e8 ts=2026-10-16T15:06:26.8390000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11277] _id=6ad23d73de269131f9e4e5ea ts=2026-10-16T15:06:26.8560000Z; 17ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[11298] _id=6ad23d88de269131f9e4e995 ts=2026-10-16T15:06:48.6230000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11299] _id=6ad23d89de269131f9e4e9c8 ts=2026-10-16T15:06:48.6400000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 176h 33m 
  - Evidence: 176h 33m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1274] _id=6ac66725de269131f9bc04c9 ts=2026-10-07T15:37:08.7730000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6799] _id=6ad019eade269131f9d9bafb ts=2026-10-15T00:10:17.9440000Z; 27m 26s: 6ab9a8bc9a8420a1e6b56b0c.jsonl[6800] _id=6ad019eade269131f9d9bafd ts=2026-10-15T00:10:18.2020000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[7517] _id=6ad02059de269131f9d9cd20 ts=2026-10-15T00:37:44.6890000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 46h 44m 
  - Evidence: 46h 44m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12684] _id=6ad26a06de269131f9e6fbfc ts=2026-10-16T18:16:38.0810000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12864] _id=6ad4fb39de269131f9e8b1c1 ts=2026-10-18T17:00:41.1050000Z; 37h 42m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[9062] _id=6ad03068de269131f9da1d0c ts=2026-10-15T01:46:15.4060000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[11908] _id=6ad242bbde269131f9e53ab6 ts=2026-10-16T15:28:58.9260000Z; 34h 18m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[4190] _id=6ace4dd4de269131f9cf1d4d ts=2026-10-13T15:27:14.9970000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[9048] _id=6ad0304ade269131f9da1ca2 ts=2026-10-15T01:45:45.7940000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1504] _id=6ac7b482de269131f9c382e4 ts=2026-10-08T15:19:29.0000000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3821] _id=6ace4896de269131f9cf0384 ts=2026-10-13T15:04:52.9090000Z; 46h 45m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12673] _id=6ad269b0de269131f9e6fb02 ts=2026-10-16T18:15:11.7580000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12880] _id=6ad4fb34de269131f9e8b1bf ts=2026-10-18T17:00:35.8290000Z; 24h 9m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3821] _id=6ace4896de269131f9cf0384 ts=2026-10-13T15:04:52.9090000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[4813] _id=6acf9c6ade269131f9d47d27 ts=2026-10-14T15:14:49.6850000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1503] _id=6ac7b482de269131f9c382e3 ts=2026-10-08T15:19:29.0000000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3820] _id=6ace4896de269131f9cf0383 ts=2026-10-13T15:04:52.9090000Z; 46h 45m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12672] _id=6ad269b0de269131f9e6fb01 ts=2026-10-16T18:15:11.7570000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12879] _id=6ad4fb34de269131f9e8b1be ts=2026-10-18T17:00:35.8290000Z; 24h 9m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3820] _id=6ace4896de269131f9cf0383 ts=2026-10-13T15:04:52.9090000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[4812] _id=6acf9c6ade269131f9d47d26 ts=2026-10-14T15:14:49.6850000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[1505] _id=6ac7b482de269131f9c382dc ts=2026-10-07T15:47:23.294Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[6071] _id=6ad00c98de269131f9d9a1dd ts=2026-10-13T15:48:08.033Z; 38h 46m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[8390] _id=6ad02b6ede269131f9da03fa ts=2026-10-15T01:01:34.505Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12564] _id=6ad24b8cde269131f9e594f9 ts=2026-10-16T15:48:32.112Z; 33h 13m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[6071] _id=6ad00c98de269131f9d9a1dd ts=2026-10-13T15:48:08.033Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[8390] _id=6ad02b6ede269131f9da03fa ts=2026-10-15T01:01:34.505Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[3802] _id=6ac7ba7ede269131f9c41df9 ts=2026-10-08T15:45:01.5040000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[3830] _id=6ace489fde269131f9cf03aa ts=2026-10-13T15:05:01.2840000Z; 46h 39m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12805] _id=6ad26b18de269131f9e6fffe ts=2026-10-16T18:21:11.9900000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12871] _id=6ad4fb3ade269131f9e8b1c9 ts=2026-10-18T17:00:42.3320000Z; 23h 56m: 6ab9a8bc9a8420a1e6b56b0c.jsonl[575] _id=6ac3c546de269131f9ad5ea1 ts=2026-10-05T15:41:57.9170000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[739] _id=6ac515f4de269131f9b48ab3 ts=2026-10-06T15:38:27.6250000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 30 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12653] _id=6ad24c77de269131f9e5a53e ts=2026-10-16T16:10:30.7640000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12667] _id=6ad269b0de269131f9e6fafb ts=2026-10-16T16:10:30.764Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12663] _id=6ad24c78de269131f9e5a546 ts=2026-10-16T16:10:30.7780000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12668] _id=6ad269b0de269131f9e6fafc ts=2026-10-16T16:10:30.778Z; 0ms: 6ab9a8bc9a8420a1e6b56b0c.jsonl[12664] _id=6ad24c78de269131f9e5a547 ts=2026-10-16T16:10:30.7880000Z -> 6ab9a8bc9a8420a1e6b56b0c.jsonl[12669] _id=6ad269b0de269131f9e6fafd ts=2026-10-16T16:10:30.788Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[1167] _id=6ac66629de269131f9bbee63 ts=2026-10-07T15:32:56.2620000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[5443] _id=6acf9e0fde269131f9d49cd4 ts=2026-10-14T15:21:51.4390000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[5736] _id=6acfa012de269131f9d4b6eb ts=2026-10-14T15:30:25.9660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[7656] _id=6ad020e8de269131f9d9d3e4 ts=2026-10-15T00:40:07.6350000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[11477] _id=6ad23e10de269131f9e4f832 ts=2026-10-16T15:09:03.7750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[11908] _id=6ad242bbde269131f9e53ab6 ts=2026-10-16T15:28:58.9260000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[12568] _id=6ad24b93de269131f9e59562 ts=2026-10-16T16:06:42.4340000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[12684] _id=6ad26a06de269131f9e6fbfc ts=2026-10-16T18:16:38.0810000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[12653] _id=6ad24c77de269131f9e5a53e ts=2026-10-16T16:10:30.7640000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[12667] _id=6ad269b0de269131f9e6fafb ts=2026-10-16T16:10:30.764Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[12663] _id=6ad24c78de269131f9e5a546 ts=2026-10-16T16:10:30.7780000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[11086] _id=6ad23c23de269131f9e4c391 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 69 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[4565] _id=6ace5249de269131f9cf471e ts=2026-10-13T15:46:15.2990000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[4561] _id=6ace5249de269131f9cf4722 ts=2026-10-13T15:46:15.2990000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[4562] _id=6ace5249de269131f9cf4724 ts=2026-10-13T15:46:15.2990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 142 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[1579] _id=6ac7b50ade269131f9c39004 ts=2026-10-08T15:21:44.9520000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[1580] _id=6ac7b50ade269131f9c39008 ts=2026-10-08T15:21:44.9520000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[1578] _id=6ac7b50ade269131f9c3900c ts=2026-10-08T15:21:44.9720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 20 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[3904] _id=6ace4959de269131f9cf06e7 ts=2026-10-13T15:08:08.7790000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[3911] _id=6ace4966de269131f9cf0706 ts=2026-10-13T15:08:21.8610000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[3815] _id=6ace49cbde269131f9cf0811 ts=2026-10-13T15:10:02.0950000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[1268] _id=6ac66724de269131f9bc04bd ts=2026-10-07T15:37:07.9560000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[6800] _id=6ad019eade269131f9d9bafd ts=2026-10-15T00:10:18.2020000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[7593] _id=6ad020a9de269131f9d9d122 ts=2026-10-15T00:39:04.5680000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 462 start, 452 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 1212 open, 1200 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 23 open, 22 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 8 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'questActiveEvent' (totals: 63 start, 48 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 214 of 13527 adjacent _id pairs reverse in client time; worst 86386.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b0c.jsonl[6067] _id=6acfa42ade269131f9d4f6d0 ts=2026-10-14T15:47:54.1000000Z`; `6ab9a8bc9a8420a1e6b56b0c.jsonl[6071] _id=6ad00c98de269131f9d9a1dd ts=2026-10-13T15:48:08.033Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.75s, min -167793.01s, max -0.19s over 13528 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b0c\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 3804 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2710); Unit 4 Dev (640); Unit 3 Dungeon Dev (232); Unit 5 Dev - Dungeon (222)
- **Intervals:** median 0.04s (p5 0.00s / p95 2.24s, n=3803)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3804/3804 records)
    "BecameVisible"  x1212
    "BecameInvisible"  x1200
    "BecameCameraCentered"  x696
    "BecameCameraUncentered"  x696
data.pieceId  (string, 3804/3804 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3804/3804 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3387 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (840); Unit 1 Dev (627); Unit 3 Dungeon Dev (448); Unit 5 Dev - Dungeon (378); Unit 3 Dev (369); Unit 4 Dev - Dungeon (268); Unit 4 Dev - Anderson Base (223); Unit 4 Dev (148); Unit 5 Dev (86)
- **Intervals:** median 1.83s (p5 0.15s / p95 25.49s, n=3386)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3387/3387 records)
    "pressed"  x3387
data.actionType  (string, 3387/3387 records)
    "Move"  x2646
    "Interact"  x486
    "Jump"  x121
    "Ascend"  x52
    "Hoverboard"  x37
    "Sprint"  x24
    "Map"  x12
    "Descend"  x4
    "SkipCinematic"  x2
    "ToggleDebug"  x2
    "Pause"  x1
data.key  (string, 3387/3387 records, 10 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3387/3387 records)
    "Player"  x2750
    "Drone"  x637
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2626 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (986); Unit 1 Dev (377); Unit 3 Dev (253); Unit 4 Dev (239); Unit 5 Dev - Dungeon (221); Unit 3 Dungeon Dev (189); Unit 4 Dev - Dungeon (144); Unit 5 Dev (127); Unit 4 Dev - Anderson Base (90)
- **Intervals:** median 10.00s (p5 9.97s / p95 10.03s, n=2614)
- **Fields under `data`:**

```text
data.position  (object, 2626/2626 records)
data.position.x  (number, 2626/2626 records)
    numeric range -704.456 .. 1556.82 (969 unique)
data.position.y  (number, 2626/2626 records)
    numeric range -114.326 .. 222.252 (673 unique)
data.position.z  (number, 2626/2626 records)
    numeric range -1129.31 .. 2344.51 (970 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2414 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (721); Unit 4 Dev (327); Unit 3 Dev (307); Unit 1 Dev (281); Unit 5 Dev (220); Unit 3 Dungeon Dev (186); Unit 4 Dev - Anderson Base (141); Unit 5 Dev - Dungeon (126); Unit 4 Dev - Dungeon (105)
- **eventKey:** present on 1500 of 2414 records
- **Intervals:** median 4.00s (p5 0.00s / p95 37.24s, n=2413)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1500; [conversationId, dialogueEventType] x914
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2414/2414 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2414/2414 records)
    "DialogueNodeEvent"  x1500
    "DialogueStartEvent"  x462
    "DialogueFinishEvent"  x452
data.nodeId  (number, 1500/2414 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 433 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (137); Unit 3 Dev (119); Unit 2 Prod (Refactor) (103); Unit 5 Dev (38); Unit 1 Dev (36)
- **Intervals:** median 0.48s (p5 0.02s / p95 7.15s, n=432)
- **Fields under `data`:**

```text
data.actionType  (string, 433/433 records)
    "argumentationNodeHoverEnd"  x186
    "argumentationNodeHoverStart"  x186
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x20
data.argumentationTitle  (string, 433/433 records)
    "Unit 4 - Flooding"  x137
    "Unit 3 - Pollution Upstream"  x119
    "Unit 2 – Watershed"  x103
    "Unit 5"  x38
    "Unit 1 - Freshwater"  x21
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 433/433 records)
    "B"  x64
    "A"  x61
    "I"  x43
    "C"  x42
    "1"  x41
    "II"  x41
    "D"  x40
    "2"  x35
    "4"  x30
    "3"  x23
    "5"  x13
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 286 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (61); Unit 2 Prod (Refactor) (59); Unit 3 Dungeon Dev (59); Unit 4 Dev (30); Unit 5 Dev - Dungeon (22); Unit 1 Dev (19); Unit 4 Dev - Anderson Base (17); Unit 3 Dev (11); Unit 5 Dev (8)
- **Intervals:** median 20.52s (p5 2.35s / p95 1266.22s, n=285)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 286/286 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 286/286 records)
    103 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 111 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 5 Dev - Dungeon (26); Unit 1 Dev (22); Unit 2 Prod (Refactor) (20); Unit 4 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 111 of 111 records
- **Intervals:** median 174.28s (p5 0.00s / p95 82342.21s, n=110)
- **`data` key-set variants:** [questEventType, questID, questName] x63; [questEventType, questID, questName, questSuccessOrFailure] x48
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 111/111 records)
    "questActiveEvent"  x63
    "questFinishEvent"  x48
data.questID  (string, 111/111 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 111/111 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 48/111 records)
    "Succeeded"  x48
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 108 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (108)
- **Intervals:** median 10.99s (p5 0.16s / p95 64.53s, n=107)
- **Fields under `data`:**

```text
data.actionType  (string, 108/108 records)
    "On"  x64
    "Off"  x44
data.floor  (string, 108/108 records)
    "3"  x60
    "4"  x40
    "1"  x5
    "2"  x3
data.machineNumber  (string, 108/108 records)
    "One"  x104
    "Two"  x4
data.machineType  (string, 108/108 records)
    "Condenser"  x58
    "Evaporator"  x22
    "DualChamber_Evaporator"  x18
    "VentSwitch"  x6
    "DualChamber_Condenser"  x4
data.room  (string, 108/108 records)
    "2"  x59
    "3"  x25
    "1"  x16
    "4"  x8
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 72 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (45); Unit 3 Dev (27)
- **Intervals:** median 6.93s (p5 0.16s / p95 4131.75s, n=71)
- **`data` key-set variants:** [actionType, featureUsed] x45; [actionType, featureUsed, location] x25; [actionType, featureUsed, legendName] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 72/72 records)
    "MapOpenEvent"  x23
    "MapCloseEvent"  x22
    "WaypointMoveEvent"  x19
    "WaypointSetEvent"  x5
    "Selected"  x2
    "WaypointResetEvent"  x1
data.featureUsed  (string, 72/72 records)
    "Map"  x45
    "Waypoint"  x25
    "Legend"  x2
data.legendName  (string, 2/72 records)
    "0 ft"  x1
    "90 ft"  x1
data.location  (object, 25/72 records)
data.location.x  (number, 25/72 records)
    numeric range -374.242 .. 175.468 (22 unique)
data.location.y  (number, 25/72 records)
    numeric range -283.017 .. 311.681 (21 unique)
data.location.z  (number, 25/72 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 3 Dev (16); Unit 4 Dev (10)
- **Intervals:** median 1.10s (p5 0.30s / p95 15.83s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/58 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/58 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/58 records)
    "RightDrag"  x29
    "LeftDrag"  x23
data.currentSoilType  (string, 52/58 records)
    "CLAYROCK"  x12
    "CLAY"  x11
    "CLAYSAND"  x10
    "SAND"  x8
    "BEDROCK"  x6
    "SANDGRAVEL"  x4
    "GRAVEL"  x1
data.isCorrectSelection  (string, 52/58 records)
    "false"  x41
    "true"  x11
data.waterLevelStatus  (string, 52/58 records)
    "TooHigh"  x37
    "Proper"  x11
    "TooLow"  x4
data.waterRetentionChange  (string, 52/58 records)
    "Increase"  x32
    "NoChange"  x11
    "Decrease"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 45 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (6); Unit 1 Dev (5); Unit 4 Dev (5); Unit 5 Dev - Dungeon (4); Unit 3 Dungeon Dev (3); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 565.14s (p5 6.01s / p95 86934.19s, n=44)
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "DebugMenuStateChanged"  x45
data.isOpened  (bool, 45/45 records)
    false  x45
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 38 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (15); Unit 2 Prod (Refactor) (12); Unit 3 Dev (6); Unit 1 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 10.22s (p5 1.30s / p95 146784.46s, n=37)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "submitAnswerEvent"  x38
data.answerSubmitted  (string, 38/38 records)
    20 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 38/38 records)
    "Unit 4 - Flooding"  x15
    "Unit 2 – Watershed"  x12
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 6913.57s (p5 637.28s / p95 181464.06s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowFocusEvent` — 21 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21)
- **Intervals:** median 6913.57s (p5 637.28s / p95 181464.06s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TerasGardenBox` — 19 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (19)
- **Intervals:** median 3.59s (p5 1.39s / p95 70.66s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records, 12 empty-string)
    ""  x12
    "cameraPlaced"  x7
data.boxId  (string, 19/19 records)
    "0"  x11
    "1"  x4
    "2"  x4
data.soilType  (string, 19/19 records)
    "Clay"  x7
    "Sand"  x7
    "Gravel"  x4
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 17 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (8); Unit 2 Prod (Refactor) (4); Unit 5 Dev - Dungeon (4); Unit 5 Dev (1)
- **Intervals:** median 7.99s (p5 0.79s / p95 143883.40s, n=16)
- **`data` key-set variants:** [actionType, chatID] x13; [actionKey, chatID] x4
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 4/17 records)
    "ScrollStop"  x4
data.actionType  (string, 13/17 records)
    "Close"  x7
    "ScrollStart"  x4
    "Open"  x2
data.chatID  (string, 17/17 records)
    "NA"  x11
    "[83-10, 83-11, 73-200, 73-204, 73-208, 73-209]"  x2
    "[19-0, 19-1, 19-49, 19-2, 19-59, 19-50, 19-51]"  x1
    "[28-194, 28-194, 28-194, 28-194, 28-194]"  x1
    "[73-200, 73-204, 73-208, 73-209, 73-210, 73-211, 73-212]"  x1
    "[73-208, 73-209, 73-210, 73-211, 73-212]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 134.25s (p5 0.04s / p95 362334.57s, n=13)
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

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (8); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 4.56s (p5 2.55s / p95 59182.06s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `soilMachine` — 12 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (12)
- **Intervals:** median 8.45s (p5 0.23s / p95 167.36s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "ChangeCanister"  x12
data.canisterType  (string, 12/12 records)
    "Sand"  x6
    "Clay"  x3
    "Gravel"  x3
data.floor  (string, 12/12 records)
    "4"  x8
    "5"  x3
    "3"  x1
data.machine  (string, 12/12 records)
    "1"  x11
    "2"  x1
data.row  (string, 12/12 records)
    "TopRow"  x11
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 24.63s (p5 0.48s / p95 382012.10s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolOpen"  x8
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 86381.85s (p5 3397.01s / p95 404796.60s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `SolarStillDesignEvent` — 7 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (7)
- **Intervals:** median 1.80s (p5 1.21s / p95 6.28s, n=6)
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
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/7 records)
    "Flat"  x1
data.featureUsed  (string, 7/7 records)
    "ExtraCovering"  x3
    "RoofStyle"  x2
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 6/7 records)
    "Covered"  x2
    "Cold"  x1
    "Flat"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 157572.51s (p5 25345.41s / p95 567343.77s, n=4)
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
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (32 records)
- `TerasGardenBox` data.actionType: "" (12x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (19x); "WaypointResetEvent" (1x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (25x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (20x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*