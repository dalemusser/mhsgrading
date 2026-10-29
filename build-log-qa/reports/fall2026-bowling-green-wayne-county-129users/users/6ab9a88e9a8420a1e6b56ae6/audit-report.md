# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae6

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae6
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae6.jsonl
- **Records:** 12943 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae6
- **Time span:** 2026-10-06T13:18:32.091000+00:00 .. 2026-10-16T13:39:23.262000+00:00 (240h 20m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae6\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 12943 records, 11 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 86 INFO, 0 NOT_TESTED, 96 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5114 | 39.51 | 1 | 9 | 0 | 2026-10-06T13:23:38.419000+00:00 | 2026-10-16T13:39:23.262000+00:00 | 240h 15m |
| PuzzlePieceVisibleEvent | 2282 | 17.63 | 1 | 4 | 0 | 2026-10-07T13:27:09.806000+00:00 | 2026-10-15T21:02:02.935000+00:00 | 199h 34m |
| DialogueEvent | 2219 | 17.14 | 1 | 9 | 1376 | 2026-10-06T13:19:18.675000+00:00 | 2026-10-16T13:39:14.082000+00:00 | 240h 19m |
| PlayerPositionEvent | 2021 | 15.61 | 1 | 9 | 0 | 2026-10-06T13:18:58.679000+00:00 | 2026-10-16T13:39:20.712000+00:00 | 240h 20m |
| argumentationNodeEvent | 426 | 3.29 | 1 | 5 | 0 | 2026-10-06T13:45:02.702000+00:00 | 2026-10-16T13:25:03.027000+00:00 | 239h 40m |
| ObjectInterEvent | 330 | 2.55 | 1 | 9 | 0 | 2026-10-06T13:25:23.555000+00:00 | 2026-10-16T13:39:23.262000+00:00 | 240h 13m |
| TopographicMapEvent | 85 | 0.66 | 1 | 2 | 0 | 2026-10-06T13:58:11.485000+00:00 | 2026-10-14T13:31:48.050000+00:00 | 191h 33m |
| questEvent | 85 | 0.66 | 1 | 9 | 85 | 2026-10-06T13:19:18.652000+00:00 | 2026-10-16T13:35:35.314000+00:00 | 240h 16m |
| soilMachine | 68 | 0.53 | 1 | 1 | 0 | 2026-10-15T13:16:02.941000+00:00 | 2026-10-15T13:29:48.595000+00:00 | 13m 45s |
| Soil Key Puzzle | 62 | 0.48 | 1 | 3 | 0 | 2026-10-07T13:35:12.046000+00:00 | 2026-10-14T13:48:51.139000+00:00 | 168h 13m |
| WaterChamberEvent | 52 | 0.4 | 1 | 1 | 0 | 2026-10-15T21:01:04.339000+00:00 | 2026-10-16T13:16:12.010000+00:00 | 16h 15m |
| DEBUGMenu | 38 | 0.29 | 1 | 9 | 0 | 2026-10-06T13:18:58.662000+00:00 | 2026-10-16T13:10:57.543000+00:00 | 239h 51m |
| argumentationAnswerEvent | 37 | 0.29 | 1 | 5 | 0 | 2026-10-06T13:45:20.776000+00:00 | 2026-10-16T13:25:04.286000+00:00 | 239h 39m |
| TerasGardenBox | 20 | 0.15 | 1 | 1 | 0 | 2026-10-15T16:05:29.273000+00:00 | 2026-10-15T20:47:43.487000+00:00 | 4h 42m |
| gameWindowFocusEvent | 19 | 0.15 | 1 | 3 | 0 | 2026-10-06T13:18:32.091000+00:00 | 2026-10-16T13:10:47.057000+00:00 | 239h 52m |
| SolarStillDesignEvent | 18 | 0.14 | 1 | 1 | 0 | 2026-10-16T13:31:50.733000+00:00 | 2026-10-16T13:32:17.569000+00:00 | 26.8s |
| gameStartEvent | 17 | 0.13 | 1 | 1 | 0 | 2026-10-06T13:18:32.093000+00:00 | 2026-10-16T13:10:47.057000+00:00 | 239h 52m |
| argumentationToolEvent | 16 | 0.12 | 1 | 2 | 0 | 2026-10-06T13:44:57.178000+00:00 | 2026-10-13T13:48:32.854000+00:00 | 168h 3m |
| argumentationEvent | 14 | 0.11 | 1 | 5 | 0 | 2026-10-06T13:44:57.266000+00:00 | 2026-10-16T13:25:04.314000+00:00 | 239h 40m |
| gameWindowUnfocusEvent | 12 | 0.09 | 1 | 5 | 0 | 2026-10-06T13:59:34.449000+00:00 | 2026-10-15T21:12:52.328000+00:00 | 223h 13m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T13:51:42.728000+00:00 | 2026-10-16T13:39:23.234000+00:00 | 239h 47m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-15T20:57:30.675000+00:00 | 2026-10-16T13:17:01.618000+00:00 | 16h 19m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 164057.532s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.06s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.944s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.702s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 17.803s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.975s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 29385.471s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 13599.218s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 6619.062s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 7861.353s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.868s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 38 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 18 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.4x vs baseline. 
  - Observed: 37 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,I; A,2,II; A,3,II; A,4,II; B,2,I; B,2,II; B,A,2,I; C,2,II; D,2,I; D,2,II; D,3,II; D,C,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 426 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 13.6x vs baseline. 
  - Observed: 68 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[157] _id=6ac4f74ade269131f9b08c4e ts=2026-10-06T13:27:37.8950000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[210] _id=6ac4f861de269131f9b0c058 ts=2026-10-06T13:32:16.5050000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[264] _id=6ac4f947de269131f9b0de98 ts=2026-10-06T13:36:06.8670000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[1] _id=6ac4f528de269131f9b03ad3 ts=2026-10-06T13:18:32.0930000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[694] _id=6ac4fd42de269131f9b1c742 ts=2026-10-06T13:53:05.8570000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[827] _id=6ac6483dde269131f9b8eeb9 ts=2026-10-07T13:25:16.0440000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[2] _id=6ac4f528de269131f9b03acf ts=2026-10-06T13:18:32.0910000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[695] _id=6ac4fd42de269131f9b1c737 ts=2026-10-06T13:53:05.8560000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[826] _id=6ac6483dde269131f9b8eeb8 ts=2026-10-07T13:25:16.0440000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[828] _id=6ac6483dde269131f9b8eea1 ts=2026-10-06T13:59:34.449Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[2429] _id=6ac64c7ade269131f9b9df62 ts=2026-10-07T13:43:22.0510000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[2938] _id=6ac79a7ade269131f9c03580 ts=2026-10-07T13:59:46.518Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5113 | 0.0 | 0.534 | 169.166 | 10.07 | 387608.735 | 0.35 | 288 | 13 |
| PuzzlePieceVisibleEvent | 2281 | 0.0 | 0.06 | 314.99 | 2.041 | 432784.959 | 0.19 | 1068 | 7 |
| DialogueEvent | 2218 | 0.0 | 4.146 | 390.079 | 31.116 | 387595.478 | 0.15 | 671 | 11 |
| PlayerPositionEvent | 2009 | 9.731 | 10.0 | 237.465 | 10.116 | 84533.479 | 0.25 | 0 | 9 |
| argumentationNodeEvent | 425 | 0.005 | 0.83 | 2030.118 | 12.064 | 389410.179 | 0.03 | 29 | 4 |
| ObjectInterEvent | 329 | 0.0 | 9.004 | 2628.692 | 387.968 | 388919.131 | 0.02 | 3 | 13 |
| TopographicMapEvent | 84 | 0.019 | 3.47 | 8209.721 | 825.525 | 430624.129 | 0.01 | 2 | 5 |
| questEvent | 84 | 0.0 | 204.863 | 10297.341 | 79661.454 | 388107.986 | 0.01 | 17 | 18 |
| soilMachine | 67 | 0.171 | 2.868 | 12.323 | 53.3 | 145.378 | 4.87 | 0 | 0 |
| Soil Key Puzzle | 61 | 0.146 | 1.944 | 9928.182 | 1278.563 | 433251.364 | 0.01 | 0 | 4 |
| WaterChamberEvent | 51 | 0.683 | 8.702 | 1147.209 | 62.677 | 57565.188 | 0.05 | 0 | 1 |
| DEBUGMenu | 37 | 6.877 | 522.903 | 23338.348 | 85093.311 | 390311.872 | 0.0 | 0 | 18 |
| argumentationAnswerEvent | 36 | 0.632 | 17.803 | 23966.209 | 183357.258 | 389469.763 | 0.0 | 0 | 4 |
| TerasGardenBox | 19 | 0.708 | 2.587 | 891.274 | 1721.101 | 16774.461 | 0.07 | 0 | 1 |
| gameWindowFocusEvent | 18 | 80.304 | 6619.062 | 47974.165 | 131271.427 | 390340.663 | 0.0 | 0 | 15 |
| SolarStillDesignEvent | 17 | 0.767 | 1.142 | 1.579 | 3.807 | 5.301 | 38.01 | 0 | 0 |
| gameStartEvent | 16 | 83.151 | 13599.218 | 53970.935 | 162527.728 | 390340.663 | 0.0 | 0 | 14 |
| argumentationToolEvent | 15 | 1.11 | 1.975 | 40334.378 | 181532.157 | 604803.365 | 0.0 | 0 | 1 |
| argumentationEvent | 13 | 0.047 | 88.06 | 66369.773 | 284907.051 | 389412.226 | 0.0 | 1 | 5 |
| gameWindowUnfocusEvent | 11 | 142.216 | 7861.353 | 73054.353 | 299879.513 | 426966.392 | 0.0 | 0 | 9 |
| EndOfUnit | 4 | 60166.898 | 164057.532 | 215815.127 | 436037.628 | 474978.544 | 0.0 | 0 | 4 |
| chatEvent | 2 | 364.222 | 29385.471 | 29385.471 | 55504.596 | 58406.721 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 6 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[2881] _id=6ac64fddde269131f9ba34ae ts=2026-10-07T13:57:48.6000000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[2882] _id=6ac64fddde269131f9ba34af ts=2026-10-07T13:57:48.6000000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[2947] _id=6ac79a8bde269131f9c036b1 ts=2026-10-08T13:28:42.2630000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[2948] _id=6ac79a8bde269131f9c036b2 ts=2026-10-08T13:28:42.2630000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[2949] _id=6ac79a8bde269131f9c036b3 ts=2026-10-08T13:28:42.2640000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[2950] _id=6ac79a8bde269131f9c036b4 ts=2026-10-08T13:28:42.2640000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 33 group(s), 56 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[880] _id=6ac648b0de269131f9b908e0 ts=2026-10-07T13:27:11.4220000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[878] _id=6ac648b0de269131f9b908f5 ts=2026-10-07T13:27:11.4220000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[885] _id=6ac648b2de269131f9b9094d ts=2026-10-07T13:27:11.6310000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[883] _id=6ac648b2de269131f9b9095a ts=2026-10-07T13:27:11.6310000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[887] _id=6ac648b2de269131f9b90969 ts=2026-10-07T13:27:11.9390000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[888] _id=6ac648b2de269131f9b90978 ts=2026-10-07T13:27:11.9390000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[12599] _id=6ad22605de269131f9e397fa ts=2026-10-16T13:26:28.6240000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[12600] _id=6ad22605de269131f9e397fb ts=2026-10-16T13:26:28.6240000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[12781] _id=6ad227b3de269131f9e3b772 ts=2026-10-16T13:33:38.5740000Z == 6ab9a88e9a8420a1e6b56ae6.jsonl[12782] _id=6ad227b3de269131f9e3b774 ts=2026-10-16T13:33:38.5740000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[104] _id=6ac4f6c4de269131f9b07a90 ts=2026-10-06T13:25:23.5550000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[105] _id=6ac4f6c4de269131f9b07a94 ts=2026-10-06T13:25:23.5600000Z`; `913ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[6319] _id=6acf7fc9de269131f9d2d130 ts=2026-10-14T13:12:40.9470000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[6322] _id=6acf7fcade269131f9d2d141 ts=2026-10-14T13:12:41.8600000Z`; `165ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[8651] _id=6ad0d380de269131f9da6caf ts=2026-10-15T13:22:07.9090000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[8654] _id=6ad0d380de269131f9da6cb5 ts=2026-10-15T13:22:08.0740000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `244ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[926] _id=6ac648d2de269131f9b9123a ts=2026-10-07T13:27:45.8040000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[928] _id=6ac648d2de269131f9b91245 ts=2026-10-07T13:27:46.0480000Z`; `649ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[5080] _id=6ace347bde269131f9cec309 ts=2026-10-13T13:39:06.7650000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[5081] _id=6ace347cde269131f9cec312 ts=2026-10-13T13:39:07.4140000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `632ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[530] _id=6ac4fbeede269131f9b168e8 ts=2026-10-06T13:47:25.9700000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[529] _id=6ac4fbefde269131f9b16918 ts=2026-10-06T13:47:26.6020000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `47ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[5549] _id=6ace36bbde269131f9ceddbb ts=2026-10-13T13:48:42.9860000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[5547] _id=6ace36bbde269131f9ceddc1 ts=2026-10-13T13:48:43.0330000Z`; `53ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[10225] _id=6ad0db5ede269131f9db4ce0 ts=2026-10-15T13:55:41.8300000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[10222] _id=6ad0db5ede269131f9db4ce8 ts=2026-10-15T13:55:41.8830000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `64ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[465] _id=6ac4fb5fde269131f9b14b07 ts=2026-10-06T13:45:03.2670000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[466] _id=6ac4fb60de269131f9b14b0a ts=2026-10-06T13:45:03.3310000Z`; `798ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[472] _id=6ac4fb63de269131f9b14bba ts=2026-10-06T13:45:06.8540000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[461] _id=6ac4fb64de269131f9b14bea ts=2026-10-06T13:45:07.6520000Z`; `22ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[477] _id=6ac4fb64de269131f9b14c04 ts=2026-10-06T13:45:07.9820000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[473] _id=6ac4fb64de269131f9b14c0a ts=2026-10-06T13:45:08.0040000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `171ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[8650] _id=6ad0d380de269131f9da6ca5 ts=2026-10-15T13:22:07.9030000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[8653] _id=6ad0d380de269131f9da6cb4 ts=2026-10-15T13:22:08.0740000Z`; `188ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[8653] _id=6ad0d380de269131f9da6cb4 ts=2026-10-15T13:22:08.0740000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[8656] _id=6ad0d380de269131f9da6cbe ts=2026-10-15T13:22:08.2620000Z`; `601ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[8695] _id=6ad0d3a3de269131f9da70a8 ts=2026-10-15T13:22:43.0910000Z ~ 6ab9a88e9a8420a1e6b56ae6.jsonl[8702] _id=6ad0d3a4de269131f9da70d0 ts=2026-10-15T13:22:43.6920000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 108h 25m 
  - Evidence: 108h 25m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3977] _id=6ac83b88de269131f9c78df9 ts=2026-10-09T00:55:35.7790000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4653] _id=6ace3030de269131f9ce972a ts=2026-10-13T13:20:47.6510000Z; 24h 2m: 6ab9a88e9a8420a1e6b56ae6.jsonl[829] _id=6ac64847de269131f9b8f1ab ts=2026-10-07T13:25:26.7860000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2939] _id=6ac79a7ade269131f9c03586 ts=2026-10-08T13:28:25.9710000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae6.jsonl[697] _id=6ac4fd4ade269131f9b1c9d8 ts=2026-10-06T13:53:14.0630000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[825] _id=6ac6483dde269131f9b8eeb7 ts=2026-10-07T13:25:15.9060000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 107h 39m 
  - Evidence: 107h 39m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4651] _id=6ac8463bde269131f9c7aed3 ts=2026-10-09T01:41:15.2100000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4660] _id=6ace3047de269131f9ce97f0 ts=2026-10-13T13:21:10.6880000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2919] _id=6ac65013de269131f9ba38a6 ts=2026-10-07T13:58:42.3440000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2951] _id=6ac79a8bde269131f9c036b5 ts=2026-10-08T13:28:42.3110000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae6.jsonl[820] _id=6ac4fea6de269131f9b22db0 ts=2026-10-06T13:59:01.4600000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[847] _id=6ac64868de269131f9b8f80f ts=2026-10-07T13:25:59.6050000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 671 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[10002] _id=6ad0da1dde269131f9db25f0 ts=2026-10-15T13:50:20.7320000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10006] _id=6ad0da1dde269131f9db25f1 ts=2026-10-15T13:50:20.7320000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[10102] _id=6ad0dabcde269131f9db384e ts=2026-10-15T13:52:59.8720000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10103] _id=6ad0dabcde269131f9db384f ts=2026-10-15T13:52:59.8720000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[10137] _id=6ad0db24de269131f9db454e ts=2026-10-15T13:54:43.5790000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10138] _id=6ad0db24de269131f9db454f ts=2026-10-15T13:54:43.5790000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 131h 56m 
  - Evidence: 131h 56m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4652] _id=6ac8463bde269131f9c7aed1 ts=2026-10-09T01:41:15.1660000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[7286] _id=6acf859ede269131f9d33b1e ts=2026-10-14T13:37:33.7100000Z; 59h 49m: 6ab9a88e9a8420a1e6b56ae6.jsonl[690] _id=6ac4fcefde269131f9b1b33b ts=2026-10-06T13:51:42.7280000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4652] _id=6ac8463bde269131f9c7aed1 ts=2026-10-09T01:41:15.1660000Z; 31h 19m: 6ab9a88e9a8420a1e6b56ae6.jsonl[7286] _id=6acf859ede269131f9d33b1e ts=2026-10-14T13:37:33.7100000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10901] _id=6ad13e04de269131f9e1438b ts=2026-10-15T20:56:36.3360000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 107h 40m 
  - Evidence: 107h 40m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4645] _id=6ac84625de269131f9c7aeb8 ts=2026-10-09T01:40:53.3660000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4658] _id=6ace303fde269131f9ce97a2 ts=2026-10-13T13:21:02.1010000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2928] _id=6ac6501ade269131f9ba3923 ts=2026-10-07T13:58:49.8310000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2944] _id=6ac79a8bde269131f9c036ae ts=2026-10-08T13:28:42.2550000Z; 23h 27m: 6ab9a88e9a8420a1e6b56ae6.jsonl[801] _id=6ac4fe56de269131f9b2179e ts=2026-10-06T13:57:42.4490000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[836] _id=6ac6484bde269131f9b8f249 ts=2026-10-07T13:25:29.8420000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 288 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[10431] _id=6ad0fa11de269131f9dd35f3 ts=2026-10-15T16:06:41.1560000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10432] _id=6ad0fa11de269131f9dd35f4 ts=2026-10-15T16:06:41.1560000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[11206] _id=6ad13f4bde269131f9e14f18 ts=2026-10-15T21:02:03.4920000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[11207] _id=6ad13f4bde269131f9e14f19 ts=2026-10-15T21:02:03.4920000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[11363] _id=6ad13fdcde269131f9e1533a ts=2026-10-15T21:04:28.3770000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[11364] _id=6ad13fdcde269131f9e1533b ts=2026-10-15T21:04:28.3770000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 108h 1m 
  - Evidence: 108h 1m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4430] _id=6ac84383de269131f9c7aaaa ts=2026-10-09T01:29:38.9570000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4792] _id=6ace32bade269131f9ceae40 ts=2026-10-13T13:31:38.0880000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2839] _id=6ac64f92de269131f9ba2f4c ts=2026-10-07T13:56:33.6070000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[3011] _id=6ac79b1fde269131f9c04781 ts=2026-10-08T13:31:11.6080000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae6.jsonl[780] _id=6ac4fe2ade269131f9b20954 ts=2026-10-06T13:56:57.6260000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[860] _id=6ac6488cde269131f9b900cc ts=2026-10-07T13:26:36.0110000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[9707] _id=6ad0d7e8de269131f9dad926 ts=2026-10-15T13:40:56.1410000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9708] _id=6ad0d7e8de269131f9dad927 ts=2026-10-15T13:40:56.1410000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[9760] _id=6ad0d830de269131f9dae526 ts=2026-10-15T13:42:07.5520000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9761] _id=6ad0d830de269131f9dae528 ts=2026-10-15T13:42:07.5520000Z; 5ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[104] _id=6ac4f6c4de269131f9b07a90 ts=2026-10-06T13:25:23.5550000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[105] _id=6ac4f6c4de269131f9b07a94 ts=2026-10-06T13:25:23.5600000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 23h 28m 
  - Evidence: 23h 28m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2936] _id=6ac65052de269131f9ba3c5b ts=2026-10-07T13:59:45.9370000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2943] _id=6ac79a8bde269131f9c036ad ts=2026-10-08T13:28:39.4160000Z; 23h 25m: 6ab9a88e9a8420a1e6b56ae6.jsonl[824] _id=6ac4febfde269131f9b23316 ts=2026-10-06T13:59:27.1680000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[835] _id=6ac6484bde269131f9b8f248 ts=2026-10-07T13:25:26.8190000Z; 23h 11m: 6ab9a88e9a8420a1e6b56ae6.jsonl[6211] _id=6ace3962de269131f9ceffd5 ts=2026-10-13T14:00:01.3240000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[6231] _id=6acf7f99de269131f9d2cfd0 ts=2026-10-14T13:11:51.9280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 13m 
  - Evidence: 120h 13m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3590] _id=6ac79d7cde269131f9c0b335 ts=2026-10-08T13:41:15.0100000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5802] _id=6ace380dde269131f9cef05a ts=2026-10-13T13:54:19.9690000Z; 23h 39m: 6ab9a88e9a8420a1e6b56ae6.jsonl[7757] _id=6acf88c8de269131f9d37cda ts=2026-10-14T13:51:02.2560000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9346] _id=6ad0d592de269131f9daa23f ts=2026-10-15T13:30:56.4970000Z; 23h 36m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2930] _id=6ac6501dde269131f9ba3961 ts=2026-10-07T13:58:52.8440000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[3092] _id=6ac79c07de269131f9c06f08 ts=2026-10-08T13:35:03.0990000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1068 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[1002] _id=6ac6490fde269131f9b92138 ts=2026-10-07T13:28:42.1730000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[984] _id=6ac6490fde269131f9b9213a ts=2026-10-07T13:28:42.1730000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[1004] _id=6ac6490fde269131f9b9214e ts=2026-10-07T13:28:42.7510000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[1007] _id=6ac6490fde269131f9b92156 ts=2026-10-07T13:28:42.7510000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[1005] _id=6ac64910de269131f9b9215c ts=2026-10-07T13:28:42.7510000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[1008] _id=6ac64910de269131f9b92162 ts=2026-10-07T13:28:42.7510000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 20m 
  - Evidence: 120h 20m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3024] _id=6ac79b5ede269131f9c04f08 ts=2026-10-08T13:32:13.3460000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5754] _id=6ace37c1de269131f9ceecb5 ts=2026-10-13T13:53:04.7100000Z; 23h 54m: 6ab9a88e9a8420a1e6b56ae6.jsonl[5778] _id=6ace37e5de269131f9ceee88 ts=2026-10-13T13:53:40.3220000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[7387] _id=6acf881cde269131f9d364a7 ts=2026-10-14T13:48:12.0580000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2851] _id=6ac64facde269131f9ba30b4 ts=2026-10-07T13:56:59.7810000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[3010] _id=6ac79b1fde269131f9c0477d ts=2026-10-08T13:31:11.6020000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 4h 39m 
  - Evidence: 4h 39m: 6ab9a88e9a8420a1e6b56ae6.jsonl[10450] _id=6ad0fa20de269131f9dd37d6 ts=2026-10-15T16:06:55.9840000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10595] _id=6ad13ba6de269131f9e1353f ts=2026-10-15T20:46:30.4450000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 37m 
  - Evidence: 119h 37m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3827] _id=6ac7a02dde269131f9c12b5f ts=2026-10-08T13:52:44.7770000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4745] _id=6ace324dde269131f9ceaade ts=2026-10-13T13:29:48.9060000Z; 23h 57m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2782] _id=6ac64f32de269131f9ba2916 ts=2026-10-07T13:54:58.0890000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[3815] _id=6ac7a00ade269131f9c124a2 ts=2026-10-08T13:52:09.9860000Z; 23h 47m: 6ab9a88e9a8420a1e6b56ae6.jsonl[5234] _id=6ace34fdde269131f9cecafd ts=2026-10-13T13:41:17.0380000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[7046] _id=6acf83a3de269131f9d317bc ts=2026-10-14T13:29:07.2060000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.042s shown 
  - Evidence: 19ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[2400] _id=6ac64c5ade269131f9b9dbc8 ts=2026-10-07T13:42:49.2100000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2404] _id=6ac64c5ade269131f9b9dbcc ts=2026-10-07T13:42:49.2290000Z; 42ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[2398] _id=6ac64c59de269131f9b9dbbd ts=2026-10-07T13:42:49.1680000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2400] _id=6ac64c5ade269131f9b9dbc8 ts=2026-10-07T13:42:49.2100000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 15h 59m 
  - Evidence: 15h 59m: 6ab9a88e9a8420a1e6b56ae6.jsonl[11825] _id=6ad14199de269131f9e16c20 ts=2026-10-15T21:11:53.5990000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[11870] _id=6ad22277de269131f9e351d0 ts=2026-10-16T13:11:18.7870000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 108h 11m 
  - Evidence: 108h 11m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4543] _id=6ac844f2de269131f9c7accb ts=2026-10-09T01:35:45.7080000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5480] _id=6ace3650de269131f9ced9c1 ts=2026-10-13T13:46:55.4710000Z; 59h 48m: 6ab9a88e9a8420a1e6b56ae6.jsonl[537] _id=6ac4fbf4de269131f9b16a02 ts=2026-10-06T13:47:31.5420000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4543] _id=6ac844f2de269131f9c7accb ts=2026-10-09T01:35:45.7080000Z; 47h 58m: 6ab9a88e9a8420a1e6b56ae6.jsonl[5546] _id=6ace36bbde269131f9ceddb9 ts=2026-10-13T13:48:42.9720000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9868] _id=6ad0d963de269131f9db0bd8 ts=2026-10-15T13:47:14.5940000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 108h 10m 
  - Evidence: 108h 10m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4534] _id=6ac844f2de269131f9c7accd ts=2026-10-09T01:35:45.7370000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5433] _id=6ace3616de269131f9ced75e ts=2026-10-13T13:45:57.9630000Z; 59h 47m: 6ab9a88e9a8420a1e6b56ae6.jsonl[536] _id=6ac4fbf4de269131f9b16a09 ts=2026-10-06T13:47:31.5650000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4500] _id=6ac844b9de269131f9c7ac5f ts=2026-10-09T01:34:48.4990000Z; 47h 55m: 6ab9a88e9a8420a1e6b56ae6.jsonl[5547] _id=6ace36bbde269131f9ceddc1 ts=2026-10-13T13:48:43.0330000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9807] _id=6ad0d8bede269131f9daf7ca ts=2026-10-15T13:44:29.4770000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.047s..0.047s shown 
  - Evidence: 47ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[5549] _id=6ace36bbde269131f9ceddbb ts=2026-10-13T13:48:42.9860000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5547] _id=6ace36bbde269131f9ceddc1 ts=2026-10-13T13:48:43.0330000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 108h 10m 
  - Evidence: 108h 10m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4542] _id=6ac844f0de269131f9c7acc7 ts=2026-10-09T01:35:43.4450000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5432] _id=6ace3612de269131f9ced72d ts=2026-10-13T13:45:53.6240000Z; 59h 47m: 6ab9a88e9a8420a1e6b56ae6.jsonl[516] _id=6ac4fbeade269131f9b16834 ts=2026-10-06T13:47:22.4330000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4489] _id=6ac844b3de269131f9c7ac55 ts=2026-10-09T01:34:43.3690000Z; 47h 55m: 6ab9a88e9a8420a1e6b56ae6.jsonl[5453] _id=6ace36b6de269131f9cedd97 ts=2026-10-13T13:48:37.5200000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9810] _id=6ad0d8c5de269131f9daf8d7 ts=2026-10-15T13:44:37.1910000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 29 interval(s) ≤ 0.005s..0.022s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[9958] _id=6ad0d9e9de269131f9db1e3c ts=2026-10-15T13:49:29.1940000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9957] _id=6ad0d9e9de269131f9db1e43 ts=2026-10-15T13:49:29.1990000Z; 8ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[9818] _id=6ad0d8cfde269131f9dafa61 ts=2026-10-15T13:44:46.7580000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[9817] _id=6ad0d8cfde269131f9dafa66 ts=2026-10-15T13:44:46.7660000Z; 22ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[477] _id=6ac4fb64de269131f9b14c04 ts=2026-10-06T13:45:07.9820000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[473] _id=6ac4fb64de269131f9b14c0a ts=2026-10-06T13:45:08.0040000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 168h 0m 
  - Evidence: 168h 0m: 6ab9a88e9a8420a1e6b56ae6.jsonl[501] _id=6ac4fbe6de269131f9b1671f ts=2026-10-06T13:47:18.1080000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[5501] _id=6ace366ade269131f9cedaba ts=2026-10-13T13:47:21.4730000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16h 13m 
  - Evidence: 16h 13m: 6ab9a88e9a8420a1e6b56ae6.jsonl[10914] _id=6ad13e3ade269131f9e1469f ts=2026-10-15T20:57:30.6750000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[11879] _id=6ad22262de269131f9e3509e ts=2026-10-16T13:10:57.3960000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 108h 25m 
  - Evidence: 108h 25m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3974] _id=6ac83b6bde269131f9c78dcd ts=2026-10-09T00:55:07.3110000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4655] _id=6ace3030de269131f9ce972f ts=2026-10-13T13:20:47.9740000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae6.jsonl[827] _id=6ac6483dde269131f9b8eeb9 ts=2026-10-07T13:25:16.0440000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2941] _id=6ac79a7ade269131f9c03588 ts=2026-10-08T13:28:26.1270000Z; 23h 45m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4696] _id=6ace315ede269131f9cea14b ts=2026-10-13T13:25:49.2530000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[6229] _id=6acf7f8fde269131f9d2cfb1 ts=2026-10-14T13:11:42.5800000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 108h 25m 
  - Evidence: 108h 25m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3973] _id=6ac83b6bde269131f9c78dcc ts=2026-10-09T00:55:07.3110000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4654] _id=6ace3030de269131f9ce972e ts=2026-10-13T13:20:47.9740000Z; 23h 45m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4695] _id=6ace315ede269131f9cea14a ts=2026-10-13T13:25:49.2530000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[6228] _id=6acf7f8fde269131f9d2cfb0 ts=2026-10-14T13:11:42.5800000Z; 23h 45m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2430] _id=6ac64c7dde269131f9b9df9c ts=2026-10-07T13:43:24.0610000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2940] _id=6ac79a7ade269131f9c03587 ts=2026-10-08T13:28:26.1270000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 118h 36m 
  - Evidence: 118h 36m: 6ab9a88e9a8420a1e6b56ae6.jsonl[3963] _id=6ac7ac8fde269131f9c24d0f ts=2026-10-08T14:45:34.9920000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4670] _id=6ace3066de269131f9ce9922 ts=2026-10-13T13:21:41.3840000Z; 47h 59m: 6ab9a88e9a8420a1e6b56ae6.jsonl[6226] _id=6acf7f8fde269131f9d2cfad ts=2026-10-13T14:00:09.217Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[10323] _id=6ad0f96ede269131f9dd23a5 ts=2026-10-15T14:00:01.85Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2938] _id=6ac79a7ade269131f9c03580 ts=2026-10-07T13:59:46.518Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[3888] _id=6ac7a0ecde269131f9c14825 ts=2026-10-08T13:55:55.7360000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 107h 48m 
  - Evidence: 107h 48m: 6ab9a88e9a8420a1e6b56ae6.jsonl[4642] _id=6ac84631de269131f9c7aec7 ts=2026-10-09T01:41:04.8830000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[4740] _id=6ace323dde269131f9ceaa61 ts=2026-10-13T13:29:32.8690000Z; 23h 46m: 6ab9a88e9a8420a1e6b56ae6.jsonl[2391] _id=6ac64c47de269131f9b9d943 ts=2026-10-07T13:42:30.3220000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[2953] _id=6ac79a8bde269131f9c036b7 ts=2026-10-08T13:28:42.3970000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae6.jsonl[729] _id=6ac4fdaade269131f9b1e32d ts=2026-10-06T13:54:50.0660000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[838] _id=6ac6484bde269131f9b8f24b ts=2026-10-07T13:25:29.8800000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[12599] _id=6ad22605de269131f9e397fa ts=2026-10-16T13:26:28.6240000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[12600] _id=6ad22605de269131f9e397fb ts=2026-10-16T13:26:28.6240000Z; 0ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[12781] _id=6ad227b3de269131f9e3b772 ts=2026-10-16T13:33:38.5740000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[12782] _id=6ad227b3de269131f9e3b774 ts=2026-10-16T13:33:38.5740000Z; 1ms: 6ab9a88e9a8420a1e6b56ae6.jsonl[11271] _id=6ad13f78de269131f9e15060 ts=2026-10-15T21:02:47.7610000Z -> 6ab9a88e9a8420a1e6b56ae6.jsonl[11272] _id=6ad13f78de269131f9e15061 ts=2026-10-15T21:02:47.7620000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[412] _id=6ac4faebde269131f9b131a9 ts=2026-10-06T13:43:07.1200000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[545] _id=6ac4fc13de269131f9b1715e ts=2026-10-06T13:48:02.9410000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[3578] _id=6ac79d77de269131f9c0b273 ts=2026-10-08T13:41:10.8820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[5547] _id=6ace36bbde269131f9ceddc1 ts=2026-10-13T13:48:43.0330000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[10222] _id=6ad0db5ede269131f9db4ce8 ts=2026-10-15T13:55:41.8830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[466] _id=6ac4fb60de269131f9b14b0a ts=2026-10-06T13:45:03.3310000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[473] _id=6ac4fb64de269131f9b14c0a ts=2026-10-06T13:45:08.0040000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[10914] _id=6ad13e3ade269131f9e1469f ts=2026-10-15T20:57:30.6750000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[11879] _id=6ad22262de269131f9e3509e ts=2026-10-16T13:10:57.3960000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[12230] _id=6ad223cede269131f9e36a52 ts=2026-10-16T13:17:01.6180000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[8082] _id=6ad0d10ede269131f9da4f5b ts=2026-10-15T13:11:41.3060000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[12103] _id=6ad22334de269131f9e35f97 ts=2026-10-16T13:14:27.9100000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[12104] _id=6ad22334de269131f9e35f99 ts=2026-10-16T13:14:27.9270000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 21 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[3247] _id=6ac79c88de269131f9c0867c ts=2026-10-08T13:37:09.1060000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[3267] _id=6ac79c88de269131f9c08684 ts=2026-10-08T13:37:09.1060000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[3269] _id=6ac79c88de269131f9c08688 ts=2026-10-08T13:37:09.1060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 64 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[878] _id=6ac648b0de269131f9b908f5 ts=2026-10-07T13:27:11.4220000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[881] _id=6ac648b1de269131f9b90931 ts=2026-10-07T13:27:11.5510000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[885] _id=6ac648b2de269131f9b9094d ts=2026-10-07T13:27:11.6310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[495] _id=6ac4fbe3de269131f9b1668d ts=2026-10-06T13:47:15.4270000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[5500] _id=6ace366bde269131f9cedaca ts=2026-10-13T13:47:22.6480000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[5503] _id=6ace366cde269131f9cedad6 ts=2026-10-13T13:47:24.1100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 DEBUGMenu record in 'Unit 3 Dev' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[4693] _id=6ace3116de269131f9ce9e85 ts=2026-10-13T13:24:38.2030000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 428 start, 415 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 677 open, 665 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'argumentationToolOpen' (totals: 14 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 49 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 309 of 12942 adjacent _id pairs reverse in client time; worst 93.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae6.jsonl[992] _id=6ac6490cde269131f9b9203a ts=2026-10-07T13:28:43.4560000Z`; `6ab9a88e9a8420a1e6b56ae6.jsonl[991] _id=6ac6490dde269131f9b9206b ts=2026-10-07T13:27:09.8060000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.72s, min -84519.77s, max -0.08s over 12943 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae6\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md

## 9. Event-Type Details

### `InputEvent` — 5114 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1066); Unit 2 Prod (Refactor) (1020); Unit 5 Dev - Dungeon (820); Unit 3 Dev (703); Unit 3 Dungeon Dev (503); Unit 4 Dev (476); Unit 5 Dev (258); Unit 1 Dev (212); Unit 4 Dev - Anderson Base (56)
- **Intervals:** median 0.53s (p5 0.04s / p95 10.07s, n=5113)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5114/5114 records)
    "pressed"  x5114
data.actionType  (string, 5114/5114 records)
    "Move"  x4383
    "Interact"  x547
    "Jump"  x79
    "Hoverboard"  x45
    "Ascend"  x24
    "Descend"  x21
    "Map"  x11
    "Sprint"  x4
data.key  (string, 5114/5114 records, 4 empty-string)
    14 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5114/5114 records)
    "Player"  x4582
    "Drone"  x532
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2282 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1390); Unit 3 Dungeon Dev (378); Unit 4 Dev (326); Unit 5 Dev - Dungeon (188)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.04s, n=2281)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2282/2282 records)
    "BecameVisible"  x677
    "BecameInvisible"  x665
    "BecameCameraCentered"  x470
    "BecameCameraUncentered"  x470
data.pieceId  (string, 2282/2282 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2282/2282 records)
    1495 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2219 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (644); Unit 4 Dev (336); Unit 3 Dev (290); Unit 5 Dev (247); Unit 1 Dev (210); Unit 3 Dungeon Dev (155); Unit 4 Dev - Anderson Base (134); Unit 5 Dev - Dungeon (104); Unit 4 Dev - Dungeon (99)
- **eventKey:** present on 1376 of 2219 records
- **Intervals:** median 4.15s (p5 0.00s / p95 31.12s, n=2218)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1376; [conversationId, dialogueEventType] x843
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2219/2219 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2219/2219 records)
    "DialogueNodeEvent"  x1376
    "DialogueStartEvent"  x428
    "DialogueFinishEvent"  x415
data.nodeId  (number, 1376/2219 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2021 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (696); Unit 3 Dev (245); Unit 4 Dev (231); Unit 1 Dev (196); Unit 4 Dev - Dungeon (166); Unit 5 Dev (128); Unit 5 Dev - Dungeon (128); Unit 3 Dungeon Dev (123); Unit 4 Dev - Anderson Base (108)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=2009)
- **Fields under `data`:**

```text
data.position  (object, 2021/2021 records)
data.position.x  (number, 2021/2021 records)
    numeric range -720.167 .. 1558.71 (687 unique)
data.position.y  (number, 2021/2021 records)
    numeric range -114.748 .. 222.252 (477 unique)
data.position.z  (number, 2021/2021 records)
    numeric range -1174.4 .. 2020.57 (687 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 426 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (261); Unit 3 Dev (71); Unit 5 Dev (34); Unit 1 Dev (31); Unit 2 Prod (Refactor) (29)
- **Intervals:** median 0.83s (p5 0.04s / p95 12.06s, n=425)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 426/426 records)
    "argumentationNodeHoverEnd"  x181
    "argumentationNodeHoverStart"  x179
    "argumentationNodeAdd"  x42
    "argumentationNodeRemove"  x24
data.argumentationTitle  (string, 426/426 records)
    "Unit 4 - Flooding"  x261
    "Unit 3 - Pollution Upstream"  x71
    "Unit 5"  x34
    "Unit 2 – Watershed"  x29
    "Unit 1 - Freshwater"  x21
    "Unit 1 - Argumentation Tutorial"  x10
data.nodeName  (string, 426/426 records)
    "B"  x74
    "A"  x56
    "C"  x54
    "D"  x44
    "I"  x37
    "2"  x33
    "II"  x33
    "1"  x31
    "3"  x27
    "4"  x26
    "5"  x11
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 330 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (140); Unit 2 Prod (Refactor) (57); Unit 3 Dungeon Dev (42); Unit 4 Dev (27); Unit 5 Dev - Dungeon (18); Unit 5 Dev (16); Unit 3 Dev (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 9.00s (p5 0.68s / p95 387.97s, n=329)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 330/330 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 330/330 records)
    110 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 85 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (52); Unit 3 Dev (33)
- **Intervals:** median 3.47s (p5 0.64s / p95 825.53s, n=84)
- **`data` key-set variants:** [actionType, featureUsed, location] x47; [actionType, featureUsed] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 85/85 records)
    "WaypointMoveEvent"  x42
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
    "WaypointSetEvent"  x5
data.featureUsed  (string, 85/85 records)
    "Waypoint"  x47
    "Map"  x38
data.location  (object, 47/85 records)
data.location.x  (number, 47/85 records)
    numeric range -226.622 .. 244.357 (38 unique)
data.location.y  (number, 47/85 records)
    numeric range -339.253 .. 214.758 (37 unique)
data.location.z  (number, 47/85 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 85 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 4 Dev (12); Unit 5 Dev - Dungeon (12); Unit 4 Dev - Dungeon (11); Unit 3 Dev (9); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 85 of 85 records
- **Intervals:** median 204.86s (p5 0.01s / p95 79661.45s, n=84)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 85/85 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x36
data.questID  (string, 85/85 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 85/85 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/85 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 68 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (68)
- **Intervals:** median 2.87s (p5 0.35s / p95 53.30s, n=67)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "ChangeCanister"  x68
data.canisterType  (string, 68/68 records)
    "Clay"  x34
    "Bedrock"  x29
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 68/68 records)
    "5"  x62
    "3"  x3
    "4"  x3
data.machine  (string, 68/68 records)
    "1"  x67
    "2"  x1
data.row  (string, 68/68 records)
    "TopRow"  x39
    "BottomRow"  x29
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 62 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (22); Unit 4 Dev (16)
- **Intervals:** median 1.94s (p5 0.22s / p95 1278.56s, n=61)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/62 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/62 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/62 records)
    "RightDrag"  x31
    "LeftDrag"  x21
data.currentSoilType  (string, 52/62 records)
    "SAND"  x12
    "CLAY"  x10
    "CLAYSAND"  x10
    "CLAYROCK"  x8
    "SANDGRAVEL"  x8
    "GRAVEL"  x3
    "BEDROCK"  x1
data.isCorrectSelection  (string, 52/62 records)
    "false"  x38
    "true"  x14
data.waterLevelStatus  (string, 52/62 records)
    "TooHigh"  x23
    "Proper"  x18
    "TooLow"  x11
data.waterRetentionChange  (string, 52/62 records)
    "Decrease"  x21
    "Increase"  x17
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 52 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (52)
- **Intervals:** median 8.70s (p5 0.95s / p95 62.68s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "On"  x34
    "Off"  x18
data.floor  (string, 52/52 records)
    "4"  x27
    "3"  x15
    "2"  x8
    "1"  x2
data.machineNumber  (string, 52/52 records)
    "One"  x50
    "Two"  x2
data.machineType  (string, 52/52 records)
    "Condenser"  x26
    "Evaporator"  x18
    "VentSwitch"  x4
    "DualChamber_Condenser"  x2
    "DualChamber_Evaporator"  x2
data.room  (string, 52/52 records)
    "2"  x18
    "3"  x18
    "1"  x12
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 38 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (6); Unit 4 Dev (5); Unit 3 Dev (4); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 522.90s (p5 9.13s / p95 85093.31s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "DebugMenuStateChanged"  x38
data.isOpened  (bool, 38/38 records)
    false  x38
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 37 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (21); Unit 3 Dev (7); Unit 1 Dev (6); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 17.80s (p5 1.60s / p95 183357.26s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "submitAnswerEvent"  x37
data.answerSubmitted  (string, 37/37 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 37/37 records)
    "Unit 4 - Flooding"  x21
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TerasGardenBox` — 20 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (20)
- **Intervals:** median 2.59s (p5 0.90s / p95 1721.10s, n=19)
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records, 13 empty-string)
    ""  x13
    "cameraPlaced"  x7
data.boxId  (string, 20/20 records)
    "0"  x10
    "1"  x5
    "2"  x5
data.soilType  (string, 20/20 records)
    "Gravel"  x8
    "Sand"  x7
    "Clay"  x5
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowFocusEvent` — 19 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 6619.06s (p5 82.72s / p95 131271.43s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `SolarStillDesignEvent` — 18 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (18)
- **Intervals:** median 1.14s (p5 0.83s / p95 3.81s, n=17)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x17; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "optionSelected"  x17
    "DesignSubmitted"  x1
data.designSelections  (object, 1/18 records)
data.designSelections.glassRoofTemperature  (string, 1/18 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/18 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/18 records)
    "Tilted Out"  x1
data.featureUsed  (string, 18/18 records)
    "RoofStyle"  x9
    "ExtraCovering"  x5
    "GlassRoofTemperature"  x3
    "Submit"  x1
data.selectedOption  (string, 17/18 records, 7 empty-string)
    ""  x7
    "Tilted Out"  x3
    "Covered"  x2
    "Cold"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 13599.22s (p5 184.38s / p95 162527.73s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (5)
- **Intervals:** median 1.98s (p5 1.16s / p95 181532.16s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolOpen"  x14
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - Pollution Site Data"  x11
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 88.06s (p5 0.05s / p95 284907.05s, n=13)
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

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2); Unit 4 Dev (2); Transition (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 7861.35s (p5 146.01s / p95 299879.51s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 164057.53s (p5 68053.26s / p95 436037.63s, n=4)
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

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 29385.47s (p5 3266.35s / p95 55504.60s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (24 records)
- `TerasGardenBox` data.actionType: "" (13x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (42x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (47x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (24x)
- `soilMachine` data.canisterType: "Bedrock" (29x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*