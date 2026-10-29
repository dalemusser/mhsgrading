# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae9

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae9
- **Game version string(s) in log:** 2.8.1, 2.8.4, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae9.jsonl
- **Records:** 11687 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae9
- **Time span:** 2026-10-06T13:22:31.213000+00:00 .. 2026-10-16T16:53:20.585000+00:00 (243h 30m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae9\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 11687 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 95 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3168 | 27.11 | 1 | 9 | 0 | 2026-10-06T13:22:45.092000+00:00 | 2026-10-16T16:53:20.585000+00:00 | 243h 30m |
| PuzzlePieceVisibleEvent | 3064 | 26.22 | 1 | 4 | 0 | 2026-10-07T13:27:21.571000+00:00 | 2026-10-16T14:35:26.683000+00:00 | 217h 8m |
| DialogueEvent | 2273 | 19.45 | 1 | 9 | 1413 | 2026-10-06T13:23:01.537000+00:00 | 2026-10-16T16:53:16.233000+00:00 | 243h 30m |
| PlayerPositionEvent | 1857 | 15.89 | 1 | 9 | 0 | 2026-10-06T13:22:41.358000+00:00 | 2026-10-16T16:53:13.912000+00:00 | 243h 30m |
| ObjectInterEvent | 397 | 3.4 | 1 | 9 | 0 | 2026-10-06T13:26:45.710000+00:00 | 2026-10-16T16:53:20.585000+00:00 | 243h 26m |
| argumentationNodeEvent | 395 | 3.38 | 1 | 5 | 0 | 2026-10-06T13:50:06.401000+00:00 | 2026-10-16T16:06:20.650000+00:00 | 242h 16m |
| questEvent | 99 | 0.85 | 1 | 9 | 99 | 2026-10-06T13:23:01.511000+00:00 | 2026-10-16T16:49:52.069000+00:00 | 243h 26m |
| Soil Key Puzzle | 68 | 0.58 | 1 | 3 | 0 | 2026-10-08T13:40:15.839000+00:00 | 2026-10-15T13:47:00.522000+00:00 | 168h 6m |
| TopographicMapEvent | 52 | 0.44 | 1 | 2 | 0 | 2026-10-07T13:27:45.782000+00:00 | 2026-10-15T13:32:52.296000+00:00 | 192h 5m |
| soilMachine | 48 | 0.41 | 1 | 1 | 0 | 2026-10-15T16:06:20.420000+00:00 | 2026-10-16T13:26:34.150000+00:00 | 21h 20m |
| WaterChamberEvent | 45 | 0.39 | 1 | 1 | 0 | 2026-10-16T13:59:06.501000+00:00 | 2026-10-16T15:57:59.973000+00:00 | 1h 58m |
| DEBUGMenu | 42 | 0.36 | 1 | 9 | 0 | 2026-10-06T13:22:41.340000+00:00 | 2026-10-16T16:42:20.660000+00:00 | 243h 19m |
| DaniEvent | 42 | 0.36 | 1 | 3 | 0 | 2026-10-07T13:50:00.808000+00:00 | 2026-10-15T13:57:23.466000+00:00 | 192h 7m |
| argumentationAnswerEvent | 29 | 0.25 | 1 | 5 | 0 | 2026-10-06T13:51:24.597000+00:00 | 2026-10-16T16:06:25.134000+00:00 | 242h 15m |
| gameWindowFocusEvent | 25 | 0.21 | 1 | 3 | 0 | 2026-10-06T13:22:31.213000+00:00 | 2026-10-16T16:42:20.814000+00:00 | 243h 19m |
| gameStartEvent | 20 | 0.17 | 1 | 1 | 0 | 2026-10-06T13:22:31.214000+00:00 | 2026-10-16T16:42:20.814000+00:00 | 243h 19m |
| argumentationEvent | 14 | 0.12 | 1 | 5 | 0 | 2026-10-06T13:51:07.214000+00:00 | 2026-10-16T16:06:25.165000+00:00 | 242h 15m |
| chatEvent | 10 | 0.09 | 1 | 4 | 0 | 2026-10-07T13:51:07.941000+00:00 | 2026-10-16T16:42:32.364000+00:00 | 218h 51m |
| SolarStillDesignEvent | 9 | 0.08 | 1 | 1 | 0 | 2026-10-16T16:46:52.332000+00:00 | 2026-10-16T16:47:22.454000+00:00 | 30.1s |
| gameWindowUnfocusEvent | 8 | 0.07 | 1 | 2 | 0 | 2026-10-07T13:45:14.387000+00:00 | 2026-10-16T14:47:43.680000+00:00 | 217h 2m |
| TerasGardenBox | 7 | 0.06 | 1 | 1 | 0 | 2026-10-16T13:46:18.947000+00:00 | 2026-10-16T13:47:03.955000+00:00 | 45.0s |
| argumentationToolEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-10-06T13:51:04.914000+00:00 | 2026-10-14T13:27:32.240000+00:00 | 191h 36m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T13:55:36.969000+00:00 | 2026-10-16T16:53:20.566000+00:00 | 242h 57m |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87019.359s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.315s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.054s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.898s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.758s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.088s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2169.24s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1892.059s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85733.805s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.707s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.5x vs baseline. 
  - Observed: 42 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 42 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E To Pick Up 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.8x vs baseline. 
  - Observed: 29 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,B,1,I; B,1,II; B,2,II; B,A,1,II; C,1,II; C,2,II; C,3,4,II; C,3,II; C,4,II; C,D,3,II; C,D,A,2,II; D,1,II; D,2,II; D,B,2,II; D,C,2,II 
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
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 10 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-217, 10-218, 11-224, 11-226, 11-24]; [21-12, 21-92, 21-15, 18-231, 28-192] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 9.6x vs baseline. 
  - Observed: 48 records 
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
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[479] _id=6ac4f9e6de269131f9b0fedf ts=2026-10-06T13:38:45.4960000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[552] _id=6ac4fac0de269131f9b12b6b ts=2026-10-06T13:42:23.8810000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[582] _id=6ac4fb21de269131f9b13f22 ts=2026-10-06T13:44:01.4480000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[1] _id=6ac4f617de269131f9b05396 ts=2026-10-06T13:22:31.2140000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[389] _id=6ac4f88fde269131f9b0c66f ts=2026-10-06T13:33:03.3340000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[802] _id=6ac4fe2ede269131f9b20a90 ts=2026-10-06T13:57:02.2160000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[0] _id=6ac4f617de269131f9b0538e ts=2026-10-06T13:22:31.2130000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[390] _id=6ac4f88fde269131f9b0c66a ts=2026-10-06T13:33:03.3330000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[800] _id=6ac4fe2ede269131f9b20a85 ts=2026-10-06T13:57:02.2150000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[2478] _id=6ac64cebde269131f9b9e8b4 ts=2026-10-07T13:45:14.3870000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[2758] _id=6ac6501dde269131f9ba3958 ts=2026-10-07T13:58:51.9830000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[3870] _id=6ac7a0cdde269131f9c14495 ts=2026-10-08T13:55:24.7630000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3167 | 0.0 | 1.315 | 276.803 | 21.137 | 429544.963 | 0.22 | 72 | 12 |
| PuzzlePieceVisibleEvent | 3063 | 0.0 | 0.054 | 255.202 | 1.902 | 429563.332 | 0.24 | 1490 | 7 |
| DialogueEvent | 2272 | 0.0 | 3.415 | 385.834 | 26.021 | 429447.103 | 0.16 | 659 | 12 |
| PlayerPositionEvent | 1843 | 0.0 | 10.001 | 473.403 | 10.204 | 429443.492 | 0.13 | 1 | 10 |
| ObjectInterEvent | 396 | 0.0 | 7.973 | 2213.118 | 247.461 | 516646.744 | 0.03 | 3 | 10 |
| argumentationNodeEvent | 394 | 0.0 | 0.589 | 2213.64 | 11.2 | 602909.425 | 0.03 | 43 | 5 |
| questEvent | 98 | 0.0 | 162.074 | 8942.965 | 76834.414 | 429517.926 | 0.01 | 19 | 15 |
| Soil Key Puzzle | 67 | 0.15 | 1.227 | 9032.906 | 14.48 | 603301.241 | 0.01 | 0 | 2 |
| TopographicMapEvent | 51 | 0.02 | 5.898 | 13558.951 | 85404.958 | 431537.936 | 0.0 | 2 | 5 |
| soilMachine | 47 | 0.157 | 3.707 | 1634.335 | 150.297 | 75788.003 | 0.04 | 0 | 1 |
| WaterChamberEvent | 44 | 1.27 | 13.777 | 162.124 | 84.94 | 4119.308 | 0.37 | 0 | 2 |
| DEBUGMenu | 41 | 6.156 | 503.815 | 21365.349 | 85391.0 | 429557.985 | 0.0 | 0 | 19 |
| DaniEvent | 41 | 0.005 | 3.431 | 16869.333 | 84713.13 | 517625.852 | 0.0 | 2 | 4 |
| argumentationAnswerEvent | 28 | 1.339 | 20.758 | 31146.448 | 114759.064 | 689719.682 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 24 | 68.164 | 1892.059 | 36499.567 | 84732.226 | 429567.496 | 0.0 | 0 | 20 |
| gameStartEvent | 19 | 168.635 | 2634.768 | 46104.716 | 120511.522 | 429567.496 | 0.0 | 0 | 17 |
| argumentationEvent | 13 | 0.036 | 110.58 | 67085.996 | 379005.076 | 689671.872 | 0.0 | 2 | 4 |
| chatEvent | 9 | 2.305 | 2169.24 | 87542.714 | 432035.193 | 604515.575 | 0.0 | 0 | 6 |
| SolarStillDesignEvent | 8 | 1.132 | 2.522 | 3.765 | 9.973 | 13.234 | 15.94 | 0 | 0 |
| gameWindowUnfocusEvent | 7 | 21.041 | 85733.805 | 111621.328 | 354727.578 | 430441.428 | 0.0 | 0 | 5 |
| TerasGardenBox | 6 | 0.903 | 2.315 | 7.501 | 21.007 | 22.919 | 8.0 | 0 | 0 |
| argumentationToolEvent | 5 | 2.219 | 3.088 | 137957.465 | 551820.026 | 689773.719 | 0.0 | 0 | 1 |
| EndOfUnit | 4 | 10718.176 | 87019.359 | 218665.899 | 599515.913 | 689906.704 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 11 group(s), 25 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[2485] _id=6ac64d12de269131f9b9ebaa ts=2026-10-07T13:45:52.0560000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[2486] _id=6ac64d12de269131f9b9ebab ts=2026-10-07T13:45:52.0560000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[3878] _id=6ac7a0fbde269131f9c149be ts=2026-10-08T13:56:09.7500000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[3879] _id=6ac7a0fbde269131f9c149bf ts=2026-10-08T13:56:09.7500000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[4007] _id=6ace2efbde269131f9ce8da7 ts=2026-10-13T13:15:37.3980000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[4008] _id=6ace2efbde269131f9ce8da8 ts=2026-10-13T13:15:37.3980000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 44 group(s), 77 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[1017] _id=6ac64903de269131f9b91e0c ts=2026-10-07T13:28:33.1050000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[1016] _id=6ac64903de269131f9b91e11 ts=2026-10-07T13:28:33.1050000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[1027] _id=6ac64906de269131f9b91ef6 ts=2026-10-07T13:28:35.9920000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[1025] _id=6ac64906de269131f9b91efa ts=2026-10-07T13:28:35.9920000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[1010] _id=6ac6490ede269131f9b920f4 ts=2026-10-07T13:28:44.0190000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[1011] _id=6ac6490ede269131f9b920f5 ts=2026-10-07T13:28:44.0190000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[862] _id=6ac4fe4cde269131f9b2148e ts=? == 6ab9a88e9a8420a1e6b56ae9.jsonl[2492] _id=6ac64d12de269131f9b9ebb5 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[11408] _id=6ad24bc6de269131f9e59946 ts=2026-10-16T16:07:33.6500000Z == 6ab9a88e9a8420a1e6b56ae9.jsonl[11409] _id=6ad24bc6de269131f9e59947 ts=2026-10-16T16:07:33.6500000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 76 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `530ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[71] _id=6ac4f71ade269131f9b086a7 ts=2026-10-06T13:26:50.3930000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[73] _id=6ac4f71bde269131f9b086b3 ts=2026-10-06T13:26:50.9230000Z`; `444ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[73] _id=6ac4f71bde269131f9b086b3 ts=2026-10-06T13:26:50.9230000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[84] _id=6ac4f71bde269131f9b086bb ts=2026-10-06T13:26:51.3670000Z`; `441ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[85] _id=6ac4f71ede269131f9b086e3 ts=2026-10-06T13:26:53.7670000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[97] _id=6ac4f71ede269131f9b086f3 ts=2026-10-06T13:26:54.2080000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `43ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[5589] _id=6acf8982de269131f9d3963a ts=2026-10-14T13:54:10.0540000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[5592] _id=6acf8982de269131f9d3963d ts=2026-10-14T13:54:10.0970000Z`; `36ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[9744] _id=6ad229b7de269131f9e3de8f ts=2026-10-16T13:42:14.4140000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[9747] _id=6ad229b7de269131f9e3de92 ts=2026-10-16T13:42:14.4500000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 28 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `61ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[700] _id=6ac4fcd5de269131f9b1ada7 ts=2026-10-06T13:51:17.0040000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[702] _id=6ac4fcd5de269131f9b1adaa ts=2026-10-06T13:51:17.0650000Z`; `38ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[712] _id=6ac4fcd7de269131f9b1adfb ts=2026-10-06T13:51:18.4420000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[679] _id=6ac4fcd7de269131f9b1ae04 ts=2026-10-06T13:51:18.4800000Z`; `498ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2778] _id=6ac6500cde269131f9ba381a ts=2026-10-07T13:58:35.3100000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[2769] _id=6ac6500cde269131f9ba3826 ts=2026-10-07T13:58:35.8080000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[11475] _id=6ad253fcde269131f9e6090c ts=2026-10-16T16:42:35.7500000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[11476] _id=6ad253fcde269131f9e6090d ts=2026-10-16T16:42:35.7560000Z`; `5ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[11590] _id=6ad25567de269131f9e61e35 ts=2026-10-16T16:48:38.5890000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[11591] _id=6ad25567de269131f9e61e3b ts=2026-10-16T16:48:38.5940000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `486ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[8333] _id=6ad0fab6de269131f9dd489e ts=2026-10-15T16:09:26.3030000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[8334] _id=6ad0fab7de269131f9dd48ba ts=2026-10-15T16:09:26.7890000Z`; `364ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[8334] _id=6ad0fab7de269131f9dd48ba ts=2026-10-15T16:09:26.7890000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[8339] _id=6ad0fab7de269131f9dd48c3 ts=2026-10-15T16:09:27.1530000Z`; `293ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[8339] _id=6ad0fab7de269131f9dd48c3 ts=2026-10-15T16:09:27.1530000Z ~ 6ab9a88e9a8420a1e6b56ae9.jsonl[8343] _id=6ad0fab7de269131f9dd48d3 ts=2026-10-15T16:09:27.4460000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3874] _id=6ac7a0f5de269131f9c14935 ts=2026-10-08T13:56:04.5540000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3994] _id=6ace2eebde269131f9ce8d49 ts=2026-10-13T13:15:22.5390000Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae9.jsonl[4004] _id=6ace2ef6de269131f9ce8d8e ts=2026-10-13T13:15:33.7870000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4324] _id=6acf7f86de269131f9d2cf95 ts=2026-10-14T13:11:34.3550000Z; 23h 43m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2482] _id=6ac64d0cde269131f9b9eb3a ts=2026-10-07T13:45:47.4810000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2795] _id=6ac79a9bde269131f9c037d9 ts=2026-10-08T13:28:58.4810000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 47m 
  - Evidence: 143h 47m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2829] _id=6ac79b04de269131f9c04464 ts=2026-10-08T13:30:43.8030000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4467] _id=6acf80fede269131f9d2e049 ts=2026-10-14T13:17:49.6550000Z; 24h 10m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5313] _id=6acf87b2de269131f9d35ba3 ts=2026-10-14T13:46:25.5690000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[7906] _id=6ad0dbc1de269131f9db5773 ts=2026-10-15T13:57:20.5890000Z; 23h 31m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2786] _id=6ac65019de269131f9ba3905 ts=2026-10-07T13:58:48.4700000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2828] _id=6ac79b02de269131f9c0441c ts=2026-10-08T13:30:41.6000000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2779] _id=6ac65018de269131f9ba38f3 ts=2026-10-07T13:58:47.4460000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2780] _id=6ac65018de269131f9ba38f7 ts=2026-10-07T13:58:47.4510000Z; 7ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2785] _id=6ac65014de269131f9ba38b3 ts=2026-10-07T13:58:43.5520000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2784] _id=6ac65014de269131f9ba38b5 ts=2026-10-07T13:58:43.5590000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3976] _id=6ac7a173de269131f9c1559a ts=2026-10-08T13:58:10.3200000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4009] _id=6ace2efbde269131f9ce8da9 ts=2026-10-13T13:15:37.4230000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2677] _id=6ac64f89de269131f9ba2ed1 ts=2026-10-07T13:56:24.5370000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2800] _id=6ac79aabde269131f9c039ad ts=2026-10-08T13:29:13.5530000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae9.jsonl[899] _id=6ac4febede269131f9b232f7 ts=2026-10-06T13:59:26.1210000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[915] _id=6ac64856de269131f9b8f489 ts=2026-10-07T13:25:40.9250000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 659 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[11299] _id=6ad24b36de269131f9e58fca ts=2026-10-16T16:05:08.8860000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[11300] _id=6ad24b36de269131f9e58fcb ts=2026-10-16T16:05:08.8860000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[11346] _id=6ad24b72de269131f9e593ae ts=2026-10-16T16:06:09.0390000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[11347] _id=6ad24b72de269131f9e593af ts=2026-10-16T16:06:09.0390000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[5522] _id=6acf8934de269131f9d38a0c ts=2026-10-14T13:52:52.0170000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5523] _id=6acf8934de269131f9d38a0d ts=2026-10-14T13:52:52.0170000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 38m 
  - Evidence: 191h 38m: 6ab9a88e9a8420a1e6b56ae9.jsonl[854] _id=6ac4fdd9de269131f9b1f1e3 ts=2026-10-06T13:55:36.9690000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4999] _id=6acf84ccde269131f9d32d60 ts=2026-10-14T13:34:03.6730000Z; 24h 15m: 6ab9a88e9a8420a1e6b56ae9.jsonl[6742] _id=6ad0d79dde269131f9dad18c ts=2026-10-15T13:39:40.9590000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10070] _id=6ad22ca3de269131f9e42df9 ts=2026-10-16T13:54:42.3900000Z; 24h 5m: 6ab9a88e9a8420a1e6b56ae9.jsonl[4999] _id=6acf84ccde269131f9d32d60 ts=2026-10-14T13:34:03.6730000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[6742] _id=6ad0d79dde269131f9dad18c ts=2026-10-15T13:39:40.9590000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3945] _id=6ac7a111de269131f9c14c91 ts=2026-10-08T13:56:32.4320000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4006] _id=6ace2efbde269131f9ce8da6 ts=2026-10-13T13:15:37.3950000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2764] _id=6ac65005de269131f9ba379a ts=2026-10-07T13:58:28.5460000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2799] _id=6ac79aabde269131f9c039ac ts=2026-10-08T13:29:13.5100000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae9.jsonl[890] _id=6ac4feb1de269131f9b23012 ts=2026-10-06T13:59:12.5620000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[906] _id=6ac64846de269131f9b8f16a ts=2026-10-07T13:25:25.4670000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 72 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[10389] _id=6ad23536de269131f9e47c49 ts=2026-10-16T14:31:16.9860000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10390] _id=6ad23536de269131f9e47c4a ts=2026-10-16T14:31:16.9860000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2485] _id=6ac64d12de269131f9b9ebaa ts=2026-10-07T13:45:52.0560000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2486] _id=6ac64d12de269131f9b9ebab ts=2026-10-07T13:45:52.0560000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2486] _id=6ac64d12de269131f9b9ebab ts=2026-10-07T13:45:52.0560000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2487] _id=6ac64d12de269131f9b9ebac ts=2026-10-07T13:45:52.0560000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3674] _id=6ac79eacde269131f9c0e5ff ts=2026-10-08T13:46:19.2510000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4436] _id=6acf80d2de269131f9d2ddd8 ts=2026-10-14T13:17:05.9950000Z; 24h 4m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2279] _id=6ac64aa4de269131f9b98b4e ts=2026-10-07T13:35:31.5090000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3010] _id=6ac79d40de269131f9c0a876 ts=2026-10-08T13:40:15.8430000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5154] _id=6acf8688de269131f9d345c2 ts=2026-10-14T13:41:27.8030000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5951] _id=6ad0d220de269131f9da5823 ts=2026-10-15T13:16:16.2430000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.007s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[9434] _id=6ad2283cde269131f9e3c079 ts=2026-10-16T13:35:55.8200000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9435] _id=6ad2283cde269131f9e3c07a ts=2026-10-16T13:35:55.8200000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[9493] _id=6ad2287cde269131f9e3c5fc ts=2026-10-16T13:36:59.6670000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9494] _id=6ad2287cde269131f9e3c5fd ts=2026-10-16T13:36:59.6670000Z; 7ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[461] _id=6ac4f972de269131f9b0e8a0 ts=2026-10-06T13:36:50.0320000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[459] _id=6ac4f972de269131f9b0e8a8 ts=2026-10-06T13:36:50.0390000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3975] _id=6ac7a173de269131f9c15596 ts=2026-10-08T13:58:10.3060000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4005] _id=6ace2efbde269131f9ce8da5 ts=2026-10-13T13:15:33.7980000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2794] _id=6ac79a9bde269131f9c037d3 ts=2026-10-07T13:59:46.051Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2798] _id=6ac79aabde269131f9c039ab ts=2026-10-08T13:29:09.0120000Z; 23h 25m: 6ab9a88e9a8420a1e6b56ae9.jsonl[896] _id=6ac4febbde269131f9b23274 ts=2026-10-06T13:59:23.1280000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[904] _id=6ac64841de269131f9b8efce ts=2026-10-07T13:25:17.2560000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2793] _id=6ac65053de269131f9ba3c67 ts=2026-10-07T13:59:46.0510000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2794] _id=6ac79a9bde269131f9c037d3 ts=2026-10-07T13:59:46.051Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3944] _id=6ac7a10fde269131f9c14c44 ts=2026-10-08T13:56:27.1240000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3989] _id=6ace2f07de269131f9ce8ddd ts=2026-10-13T13:15:50.4560000Z; 48h 1m: 6ab9a88e9a8420a1e6b56ae9.jsonl[4073] _id=6ace2f13de269131f9ce8e87 ts=2026-10-13T13:15:59.9930000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5994] _id=6ad0d281de269131f9da5b37 ts=2026-10-15T13:17:51.6000000Z; 24h 6m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2206] _id=6ac64a82de269131f9b98553 ts=2026-10-07T13:34:56.5770000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3060] _id=6ac79d9cde269131f9c0b8e4 ts=2026-10-08T13:41:47.0830000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1490 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[1000] _id=6ac64902de269131f9b91ddc ts=2026-10-07T13:28:33.1050000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[985] _id=6ac64902de269131f9b91ded ts=2026-10-07T13:28:33.1050000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[1001] _id=6ac6490ede269131f9b920bf ts=2026-10-07T13:28:43.8670000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[1002] _id=6ac6490ede269131f9b920c0 ts=2026-10-07T13:28:43.8670000Z; 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[10052] _id=6ad22d4cde269131f9e43e47 ts=2026-10-16T13:57:30.6520000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10149] _id=6ad22d4cde269131f9e43e49 ts=2026-10-16T13:57:30.6520000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 35m 
  - Evidence: 167h 35m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3036] _id=6ac79d7bde269131f9c0b30e ts=2026-10-08T13:41:14.9960000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5950] _id=6ad0d220de269131f9da5821 ts=2026-10-15T13:16:16.2370000Z; 28m 32s: 6ab9a88e9a8420a1e6b56ae9.jsonl[5956] _id=6ad0d23bde269131f9da58f4 ts=2026-10-15T13:16:42.9730000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[6818] _id=6ad0d8ebde269131f9daff05 ts=2026-10-15T13:45:15.0780000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2868] _id=6ac79bbcde269131f9c060ef ts=2026-10-08T13:33:47.8340000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4256] _id=6ace316ede269131f9cea1e7 ts=2026-10-13T13:26:05.7700000Z; 24h 10m: 6ab9a88e9a8420a1e6b56ae9.jsonl[4262] _id=6ace3180de269131f9cea286 ts=2026-10-13T13:26:24.2230000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5049] _id=6acf858ade269131f9d33a60 ts=2026-10-14T13:37:14.3730000Z; 23h 53m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5099] _id=6acf860ede269131f9d33fde ts=2026-10-14T13:39:26.3010000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[6594] _id=6ad0d5ffde269131f9daacec ts=2026-10-15T13:32:46.9890000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.039s shown 
  - Evidence: 20ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2425] _id=6ac64c61de269131f9b9dcc9 ts=2026-10-07T13:42:56.2720000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2429] _id=6ac64c61de269131f9b9dccd ts=2026-10-07T13:42:56.2920000Z; 39ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2430] _id=6ac64c61de269131f9b9dcbf ts=2026-10-07T13:42:56.2330000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2425] _id=6ac64c61de269131f9b9dcc9 ts=2026-10-07T13:42:56.2720000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 1h 8m 
  - Evidence: 1h 8m: 6ab9a88e9a8420a1e6b56ae9.jsonl[10861] _id=6ad23839de269131f9e495e4 ts=2026-10-16T14:44:08.9440000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10935] _id=6ad24851de269131f9e564d8 ts=2026-10-16T15:52:48.2520000Z; 35m 7s: 6ab9a88e9a8420a1e6b56ae9.jsonl[10377] _id=6ad22dabde269131f9e447a1 ts=2026-10-16T13:59:06.5010000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10558] _id=6ad235e5de269131f9e4806c ts=2026-10-16T14:34:13.5170000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 35m 
  - Evidence: 191h 35m: 6ab9a88e9a8420a1e6b56ae9.jsonl[757] _id=6ac4fd26de269131f9b1bfa9 ts=2026-10-06T13:52:37.6650000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4824] _id=6acf835dde269131f9d31227 ts=2026-10-14T13:27:57.3470000Z; 47h 45m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5587] _id=6acf8982de269131f9d39634 ts=2026-10-14T13:54:10.0330000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9599] _id=6ad2292ade269131f9e3d3cf ts=2026-10-16T13:39:53.7270000Z; 2h 22m: 6ab9a88e9a8420a1e6b56ae9.jsonl[9753] _id=6ad229b7de269131f9e3de8b ts=2026-10-16T13:42:14.3970000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[11285] _id=6ad24b26de269131f9e58ea7 ts=2026-10-16T16:04:53.4340000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 34m 
  - Evidence: 191h 34m: 6ab9a88e9a8420a1e6b56ae9.jsonl[754] _id=6ac4fd26de269131f9b1bfb1 ts=2026-10-06T13:52:37.6870000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4798] _id=6acf832ede269131f9d30f0b ts=2026-10-14T13:27:09.5590000Z; 47h 44m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5592] _id=6acf8982de269131f9d3963d ts=2026-10-14T13:54:10.0970000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9559] _id=6ad228f8de269131f9e3cff2 ts=2026-10-16T13:39:03.9750000Z; 2h 22m: 6ab9a88e9a8420a1e6b56ae9.jsonl[9747] _id=6ad229b7de269131f9e3de92 ts=2026-10-16T13:42:14.4500000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[11270] _id=6ad24b18de269131f9e58da0 ts=2026-10-16T16:04:39.5750000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.036s..0.043s shown 
  - Evidence: 36ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[9744] _id=6ad229b7de269131f9e3de8f ts=2026-10-16T13:42:14.4140000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9747] _id=6ad229b7de269131f9e3de92 ts=2026-10-16T13:42:14.4500000Z; 43ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[5589] _id=6acf8982de269131f9d3963a ts=2026-10-14T13:54:10.0540000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5592] _id=6acf8982de269131f9d3963d ts=2026-10-14T13:54:10.0970000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 28m 
  - Evidence: 167h 28m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2783] _id=6ac6500fde269131f9ba3850 ts=2026-10-07T13:58:38.1640000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4799] _id=6acf832cde269131f9d30ef6 ts=2026-10-14T13:27:07.5890000Z; 47h 44m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5582] _id=6acf897cde269131f9d394f2 ts=2026-10-14T13:54:04.0120000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9558] _id=6ad228f6de269131f9e3cfba ts=2026-10-16T13:39:01.3970000Z; 24h 6m: 6ab9a88e9a8420a1e6b56ae9.jsonl[751] _id=6ac4fd1ede269131f9b1bdd1 ts=2026-10-06T13:52:29.7430000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2774] _id=6ac6500ade269131f9ba37f3 ts=2026-10-07T13:58:33.5100000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 43 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[2770] _id=6ac6500cde269131f9ba382a ts=2026-10-07T13:58:35.8390000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2771] _id=6ac6500cde269131f9ba382b ts=2026-10-07T13:58:35.8390000Z; 3ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[4913] _id=6acf83cede269131f9d31a0a ts=2026-10-14T13:29:50.5020000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4906] _id=6acf83cfde269131f9d31a0e ts=2026-10-14T13:29:50.5050000Z; 4ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[9750] _id=6ad229b3de269131f9e3de4b ts=2026-10-16T13:42:11.2450000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[9737] _id=6ad229b4de269131f9e3de4f ts=2026-10-16T13:42:11.2490000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 36m 
  - Evidence: 191h 36m: 6ab9a88e9a8420a1e6b56ae9.jsonl[690] _id=6ac4fccbde269131f9b1ab19 ts=2026-10-06T13:51:07.1330000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4808] _id=6acf8339de269131f9d30fe8 ts=2026-10-14T13:27:20.8520000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 167h 55m 
  - Evidence: 167h 55m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2578] _id=6ac64e4fde269131f9ba06e7 ts=2026-10-07T13:51:10.2460000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5314] _id=6acf87b2de269131f9d35ba7 ts=2026-10-14T13:46:25.8210000Z; 48h 8m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5241] _id=6acf87b5de269131f9d35bce ts=2026-10-14T13:46:28.6070000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10072] _id=6ad22cb7de269131f9e4303e ts=2026-10-16T13:55:03.2280000Z; 1h 7m: 6ab9a88e9a8420a1e6b56ae9.jsonl[10889] _id=6ad23872de269131f9e4986f ts=2026-10-16T14:45:05.8570000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10924] _id=6ad24839de269131f9e5648b ts=2026-10-16T15:52:24.1350000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3873] _id=6ac7a0ecde269131f9c14823 ts=2026-10-08T13:55:55.2230000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3996] _id=6ace2eebde269131f9ce8d50 ts=2026-10-13T13:15:22.7190000Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3996] _id=6ace2eebde269131f9ce8d50 ts=2026-10-13T13:15:22.7190000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4326] _id=6acf7f87de269131f9d2cf98 ts=2026-10-14T13:11:34.6880000Z; 23h 43m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2481] _id=6ac64d04de269131f9b9ea94 ts=2026-10-07T13:45:38.9960000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2797] _id=6ac79a9bde269131f9c037db ts=2026-10-08T13:28:58.6110000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3872] _id=6ac7a0ecde269131f9c14822 ts=2026-10-08T13:55:55.2230000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3995] _id=6ace2eebde269131f9ce8d4f ts=2026-10-13T13:15:22.7190000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae9.jsonl[5002] _id=6acf84dade269131f9d32e54 ts=2026-10-14T13:34:17.9640000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[5723] _id=6ad0cff3de269131f9da4d6a ts=2026-10-15T13:06:58.9890000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2792] _id=6ac65042de269131f9ba3b88 ts=2026-10-07T13:59:29.5750000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2796] _id=6ac79a9bde269131f9c037da ts=2026-10-08T13:28:58.6100000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 34m 
  - Evidence: 119h 34m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3870] _id=6ac7a0cdde269131f9c14495 ts=2026-10-08T13:55:24.7630000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4290] _id=6ace3237de269131f9ceaa16 ts=2026-10-13T13:29:26.1910000Z; 49h 27m: 6ab9a88e9a8420a1e6b56ae9.jsonl[4476] _id=6acf811cde269131f9d2e1de ts=2026-10-14T13:18:19.9960000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[10897] _id=6ad238aade269131f9e49b70 ts=2026-10-16T14:46:01.9250000Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2758] _id=6ac6501dde269131f9ba3958 ts=2026-10-07T13:58:51.9830000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[3870] _id=6ac7a0cdde269131f9c14495 ts=2026-10-08T13:55:24.7630000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a88e9a8420a1e6b56ae9.jsonl[3948] _id=6ac7a12cde269131f9c14f4a ts=2026-10-08T13:56:59.5780000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4011] _id=6ace2efbde269131f9ce8dab ts=2026-10-13T13:15:37.5040000Z; 23h 52m: 6ab9a88e9a8420a1e6b56ae9.jsonl[4144] _id=6ace2ff2de269131f9ce9572 ts=2026-10-13T13:19:45.5450000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[4336] _id=6acf7f98de269131f9d2cfce ts=2026-10-14T13:11:51.4110000Z; 23h 43m: 6ab9a88e9a8420a1e6b56ae9.jsonl[2489] _id=6ac64d12de269131f9b9ebae ts=2026-10-07T13:45:52.0780000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[2802] _id=6ac79aabde269131f9c039af ts=2026-10-08T13:29:13.7160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[11408] _id=6ad24bc6de269131f9e59946 ts=2026-10-16T16:07:33.6500000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[11409] _id=6ad24bc6de269131f9e59947 ts=2026-10-16T16:07:33.6500000Z; 1ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[11014] _id=6ad248f1de269131f9e56986 ts=2026-10-16T15:55:28.3480000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[11015] _id=6ad248f1de269131f9e56987 ts=2026-10-16T15:55:28.3490000Z; 3ms: 6ab9a88e9a8420a1e6b56ae9.jsonl[663] _id=6ac4fc75de269131f9b190f9 ts=2026-10-06T13:49:40.4600000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[661] _id=6ac4fc75de269131f9b19105 ts=2026-10-06T13:49:40.4630000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21h 3m 
  - Evidence: 21h 3m: 6ab9a88e9a8420a1e6b56ae9.jsonl[8367] _id=6ad0facdde269131f9dd4bea ts=2026-10-15T16:09:49.2330000Z -> 6ab9a88e9a8420a1e6b56ae9.jsonl[8556] _id=6ad222d9de269131f9e3580e ts=2026-10-16T13:12:57.2360000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[654] _id=6ac4fc5bde269131f9b189c3 ts=2026-10-06T13:49:15.3220000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[765] _id=6ac4fd3ade269131f9b1c53c ts=2026-10-06T13:52:58.3410000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[2542] _id=6ac64dbede269131f9b9f833 ts=2026-10-07T13:48:45.1090000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[5592] _id=6acf8982de269131f9d3963d ts=2026-10-14T13:54:10.0970000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[9747] _id=6ad229b7de269131f9e3de92 ts=2026-10-16T13:42:14.4500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[702] _id=6ac4fcd5de269131f9b1adaa ts=2026-10-06T13:51:17.0650000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[679] _id=6ac4fcd7de269131f9b1ae04 ts=2026-10-06T13:51:18.4800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[10072] _id=6ad22cb7de269131f9e4303e ts=2026-10-16T13:55:03.2280000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[10384] _id=6ad23530de269131f9e47c3e ts=2026-10-16T14:31:12.4680000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[10889] _id=6ad23872de269131f9e4986f ts=2026-10-16T14:45:05.8570000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[5983] _id=6ad0d27ade269131f9da5ae7 ts=2026-10-15T13:17:45.9800000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[8492] _id=6ad22276de269131f9e351c4 ts=2026-10-16T13:11:17.9180000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[11013] _id=6ad248f1de269131f9e56985 ts=2026-10-16T15:55:28.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[862] _id=6ac4fe4cde269131f9b2148e ts=?`; `6ab9a88e9a8420a1e6b56ae9.jsonl[2492] _id=6ac64d12de269131f9b9ebb5 ts=?`; `6ab9a88e9a8420a1e6b56ae9.jsonl[3877] _id=6ac7a0fbde269131f9c149c4 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 36 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[3332] _id=6ac79e5fde269131f9c0d6b5 ts=2026-10-08T13:45:00.3110000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[3336] _id=6ac79e5fde269131f9c0d6b9 ts=2026-10-08T13:45:00.4480000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[3399] _id=6ac79e6dde269131f9c0d95f ts=2026-10-08T13:45:15.5570000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 85 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[1016] _id=6ac64903de269131f9b91e11 ts=2026-10-07T13:28:33.1050000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[984] _id=6ac64903de269131f9b91e1b ts=2026-10-07T13:28:33.1050000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[1018] _id=6ac64903de269131f9b91e29 ts=2026-10-07T13:28:33.1050000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[4812] _id=6acf833ede269131f9d31036 ts=2026-10-14T13:27:26.1060000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[4813] _id=6acf8341de269131f9d31055 ts=2026-10-14T13:27:29.1520000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[4814] _id=6acf8344de269131f9d3108d ts=2026-10-14T13:27:32.2400000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 436 start, 424 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 894 open, 882 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 5 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 57 start, 42 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 255 of 11682 adjacent _id pairs reverse in client time; worst 96.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae9.jsonl[1048] _id=6ac6491bde269131f9b9239f ts=2026-10-07T13:28:58.1910000Z`; `6ab9a88e9a8420a1e6b56ae9.jsonl[1046] _id=6ac6491cde269131f9b923cb ts=2026-10-07T13:27:21.5710000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.70s, min -84553.70s, max -0.31s over 11683 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae9\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3168 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (793); Unit 4 Dev - Dungeon (750); Unit 3 Dev (483); Unit 5 Dev - Dungeon (300); Unit 1 Dev (271); Unit 3 Dungeon Dev (207); Unit 4 Dev (172); Unit 4 Dev - Anderson Base (127); Unit 5 Dev (65)
- **Intervals:** median 1.31s (p5 0.12s / p95 21.14s, n=3167)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3168/3168 records)
    "pressed"  x3168
data.actionType  (string, 3168/3168 records)
    "Move"  x2150
    "Interact"  x634
    "Jump"  x241
    "Hoverboard"  x56
    "Sprint"  x43
    "Ascend"  x32
    "Pause"  x7
    "Map"  x3
    "Descend"  x1
    "SkipCinematic"  x1
data.key  (string, 3168/3168 records, 24 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3168/3168 records)
    "Player"  x2640
    "Drone"  x528
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3064 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1762); Unit 4 Dev (816); Unit 5 Dev - Dungeon (366); Unit 3 Dungeon Dev (120)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.90s, n=3063)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3064/3064 records)
    "BecameVisible"  x894
    "BecameInvisible"  x882
    "BecameCameraCentered"  x644
    "BecameCameraUncentered"  x644
data.pieceId  (string, 3064/3064 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3064/3064 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2273 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (694); Unit 3 Dev (309); Unit 5 Dev (276); Unit 4 Dev (256); Unit 1 Dev (216); Unit 4 Dev - Dungeon (168); Unit 3 Dungeon Dev (130); Unit 5 Dev - Dungeon (121); Unit 4 Dev - Anderson Base (103)
- **eventKey:** present on 1413 of 2273 records
- **Intervals:** median 3.41s (p5 0.00s / p95 26.02s, n=2272)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1413; [conversationId, dialogueEventType] x860
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2273/2273 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2273/2273 records)
    "DialogueNodeEvent"  x1413
    "DialogueStartEvent"  x436
    "DialogueFinishEvent"  x424
data.nodeId  (number, 1413/2273 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1857 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (598); Unit 3 Dev (233); Unit 4 Dev - Dungeon (229); Unit 1 Dev (196); Unit 4 Dev (177); Unit 5 Dev - Dungeon (146); Unit 5 Dev (142); Unit 3 Dungeon Dev (82); Unit 4 Dev - Anderson Base (54)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.20s, n=1843)
- **Fields under `data`:**

```text
data.position  (object, 1857/1857 records)
data.position.x  (number, 1857/1857 records)
    numeric range -692.002 .. 1598.69 (735 unique)
data.position.y  (number, 1857/1857 records)
    numeric range -116.835 .. 222.404 (518 unique)
data.position.z  (number, 1857/1857 records)
    numeric range -1122.18 .. 1929.47 (735 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 397 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (149); Unit 1 Dev (97); Unit 2 Prod (Refactor) (48); Unit 3 Dungeon Dev (33); Unit 4 Dev (22); Unit 5 Dev - Dungeon (21); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (7)
- **Intervals:** median 7.97s (p5 0.18s / p95 247.46s, n=396)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 397/397 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 397/397 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 395 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (129); Unit 2 Prod (Refactor) (87); Unit 3 Dev (71); Unit 5 Dev (66); Unit 1 Dev (42)
- **Intervals:** median 0.59s (p5 0.03s / p95 11.20s, n=394)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 395/395 records)
    "argumentationNodeHoverEnd"  x167
    "argumentationNodeHoverStart"  x165
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x22
data.argumentationTitle  (string, 395/395 records)
    "Unit 4 - Flooding"  x129
    "Unit 2 – Watershed"  x87
    "Unit 3 - Pollution Upstream"  x71
    "Unit 5"  x66
    "Unit 1 - Argumentation Tutorial"  x25
    "Unit 1 - Freshwater"  x17
data.nodeName  (string, 395/395 records)
    "A"  x57
    "I"  x55
    "C"  x48
    "B"  x46
    "D"  x42
    "1"  x35
    "II"  x31
    "3"  x27
    "4"  x26
    "2"  x21
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 99 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 4 Dev - Dungeon (18); Unit 1 Dev (14); Unit 5 Dev - Dungeon (13); Unit 3 Dev (12); Unit 5 Dev (9); Unit 4 Dev (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 99 of 99 records
- **Intervals:** median 162.07s (p5 0.01s / p95 76834.41s, n=98)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x42
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 99/99 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x42
data.questID  (string, 99/99 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 99/99 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 42/99 records)
    "Succeeded"  x42
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 68 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (42); Unit 2 Prod (Refactor) (20); Unit 3 Dev (6)
- **Intervals:** median 1.23s (p5 0.15s / p95 14.48s, n=67)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x62; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/68 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/68 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 62/68 records)
    "RightDrag"  x34
    "LeftDrag"  x28
data.currentSoilType  (string, 62/68 records)
    "CLAYSAND"  x14
    "CLAY"  x12
    "SAND"  x12
    "CLAYROCK"  x10
    "SANDGRAVEL"  x7
    "BEDROCK"  x4
    "GRAVEL"  x3
data.isCorrectSelection  (string, 62/68 records)
    "false"  x46
    "true"  x16
data.waterLevelStatus  (string, 62/68 records)
    "Proper"  x24
    "TooHigh"  x23
    "TooLow"  x15
data.waterRetentionChange  (string, 62/68 records)
    "Increase"  x27
    "Decrease"  x19
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 52 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (39); Unit 3 Dev (13)
- **Intervals:** median 5.90s (p5 1.10s / p95 85404.96s, n=51)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, location] x12
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x5
data.featureUsed  (string, 52/52 records)
    "Map"  x40
    "Waypoint"  x12
data.location  (object, 12/52 records)
data.location.x  (number, 12/52 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 12/52 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 12/52 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 48 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (48)
- **Intervals:** median 3.71s (p5 0.31s / p95 150.30s, n=47)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "ChangeCanister"  x48
data.canisterType  (string, 48/48 records)
    "Gravel"  x18
    "Clay"  x12
    "Bedrock"  x10
    "Sand"  x8
data.floor  (string, 48/48 records)
    "4"  x22
    "5"  x19
    "3"  x7
data.machine  (string, 48/48 records)
    "1"  x47
    "2"  x1
data.row  (string, 48/48 records)
    "TopRow"  x40
    "BottomRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 45 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (45)
- **Intervals:** median 13.78s (p5 1.87s / p95 84.94s, n=44)
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "On"  x32
    "Off"  x13
data.floor  (string, 45/45 records)
    "3"  x21
    "4"  x18
    "1"  x3
    "2"  x3
data.machineNumber  (string, 45/45 records)
    "One"  x43
    "Two"  x2
data.machineType  (string, 45/45 records)
    "Condenser"  x20
    "Evaporator"  x10
    "DualChamber_Evaporator"  x7
    "DualChamber_Condenser"  x4
    "VentSwitch"  x4
data.room  (string, 45/45 records)
    "2"  x22
    "3"  x12
    "1"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 42 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (7); Unit 3 Dev (4); Unit 4 Dev - Dungeon (4); Unit 4 Dev (3); Unit 5 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 503.81s (p5 6.87s / p95 85391.00s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "DebugMenuStateChanged"  x42
data.isOpened  (bool, 42/42 records)
    false  x42
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 42 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (6); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 3.43s (p5 0.83s / p95 84713.13s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "Close"  x21
    "Open"  x21
data.toolName  (string, 42/42 records, 40 empty-string)
    ""  x40
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationAnswerEvent` — 29 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (9); Unit 2 Prod (Refactor) (6); Unit 5 Dev (6); Unit 3 Dev (5); Unit 1 Dev (3)
- **Intervals:** median 20.76s (p5 3.38s / p95 114759.06s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "submitAnswerEvent"  x29
data.answerSubmitted  (string, 29/29 records)
    20 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 29/29 records)
    "Unit 4 - Flooding"  x9
    "Unit 2 – Watershed"  x6
    "Unit 5"  x6
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 2 Prod (Refactor) (3); Unit 5 Dev (2)
- **Intervals:** median 1892.06s (p5 205.38s / p95 84732.23s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 2634.77s (p5 412.47s / p95 120511.52s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 110.58s (p5 0.04s / p95 379005.08s, n=13)
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

### `chatEvent` — 10 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (3); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 2169.24s (p5 2.50s / p95 432035.19s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "Close"  x8
    "Open"  x2
data.chatID  (string, 10/10 records)
    "NA"  x8
    "[10-217, 10-218, 11-224, 11-226, 11-24]"  x1
    "[21-12, 21-92, 21-15, 18-231, 28-192]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `SolarStillDesignEvent` — 9 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (9)
- **Intervals:** median 2.52s (p5 1.20s / p95 9.97s, n=8)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x8; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "optionSelected"  x8
    "DesignSubmitted"  x1
data.designSelections  (object, 1/9 records)
data.designSelections.glassRoofTemperature  (string, 1/9 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/9 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/9 records)
    "Tilted Out"  x1
data.featureUsed  (string, 9/9 records)
    "ExtraCovering"  x4
    "RoofStyle"  x3
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 8/9 records, 2 empty-string)
    ""  x2
    "Tilted Out"  x2
    "Uncovered"  x2
    "Cold"  x1
    "Covered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 5 Dev (3)
- **Intervals:** median 85733.80s (p5 38.94s / p95 354727.58s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 2.31s (p5 1.00s / p95 21.01s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x3
data.boxId  (string, 7/7 records)
    "2"  x3
    "0"  x2
    "1"  x2
data.soilType  (string, 7/7 records)
    "Gravel"  x3
    "Clay"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 1 Dev (2)
- **Intervals:** median 3.09s (p5 2.38s / p95 551820.03s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 87019.36s (p5 22121.04s / p95 599515.91s, n=4)
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

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x4
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 4 empty-string)
    ""  x4
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x3
    "unit5"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (22x)
- `soilMachine` data.canisterType: "Bedrock" (10x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*