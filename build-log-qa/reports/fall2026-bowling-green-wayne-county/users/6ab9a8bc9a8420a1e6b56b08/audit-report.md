# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b08

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b08
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b08.jsonl
- **Records:** 9770 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b08
- **Time span:** 2026-10-05T15:16:15.409000+00:00 .. 2026-10-16T15:34:39.619000+00:00 (264h 18m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b08\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 9770 records, 11 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 98 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2713 | 27.77 | 1 | 9 | 0 | 2026-10-05T15:16:44.968000+00:00 | 2026-10-16T15:34:39.619000+00:00 | 264h 17m |
| PuzzlePieceVisibleEvent | 2126 | 21.76 | 1 | 4 | 0 | 2026-10-06T15:32:50.697000+00:00 | 2026-10-16T15:08:29.289000+00:00 | 239h 35m |
| DialogueEvent | 2101 | 21.5 | 1 | 9 | 1306 | 2026-10-05T15:16:45.409000+00:00 | 2026-10-16T15:34:31.044000+00:00 | 264h 17m |
| PlayerPositionEvent | 1573 | 16.1 | 1 | 9 | 0 | 2026-10-05T15:16:25.553000+00:00 | 2026-10-16T15:34:31.410000+00:00 | 264h 18m |
| argumentationNodeEvent | 574 | 5.88 | 1 | 5 | 0 | 2026-10-05T15:38:00.049000+00:00 | 2026-10-16T15:22:42.451000+00:00 | 263h 44m |
| ObjectInterEvent | 244 | 2.5 | 1 | 9 | 0 | 2026-10-05T15:21:16.301000+00:00 | 2026-10-16T15:34:39.618000+00:00 | 264h 13m |
| questEvent | 80 | 0.82 | 1 | 9 | 80 | 2026-10-05T15:16:45.381000+00:00 | 2026-10-16T15:30:45.587000+00:00 | 264h 14m |
| TopographicMapEvent | 64 | 0.66 | 1 | 2 | 0 | 2026-10-06T15:33:21.243000+00:00 | 2026-10-14T15:20:12.087000+00:00 | 191h 46m |
| Soil Key Puzzle | 58 | 0.59 | 1 | 3 | 0 | 2026-10-07T15:35:29.987000+00:00 | 2026-10-14T15:35:47.988000+00:00 | 168h 0m |
| WaterChamberEvent | 44 | 0.45 | 1 | 1 | 0 | 2026-10-16T15:02:24.151000+00:00 | 2026-10-16T15:11:19.651000+00:00 | 8m 55s |
| DEBUGMenu | 30 | 0.31 | 1 | 9 | 0 | 2026-10-05T15:16:25.535000+00:00 | 2026-10-16T14:58:54.112000+00:00 | 263h 42m |
| argumentationAnswerEvent | 24 | 0.25 | 1 | 5 | 0 | 2026-10-05T15:39:13.302000+00:00 | 2026-10-16T15:22:47.385000+00:00 | 263h 43m |
| soilMachine | 21 | 0.21 | 1 | 1 | 0 | 2026-10-15T15:05:09.007000+00:00 | 2026-10-15T15:12:16.380000+00:00 | 7m 7s |
| argumentationToolEvent | 19 | 0.19 | 1 | 3 | 0 | 2026-10-05T15:38:49.611000+00:00 | 2026-10-16T15:17:45.956000+00:00 | 263h 38m |
| gameWindowFocusEvent | 19 | 0.19 | 1 | 6 | 0 | 2026-10-05T15:16:15.409000+00:00 | 2026-10-16T15:31:01.624000+00:00 | 264h 14m |
| TerasGardenBox | 15 | 0.15 | 1 | 1 | 0 | 2026-10-15T15:32:03.591000+00:00 | 2026-10-15T15:36:58.401000+00:00 | 4m 54s |
| argumentationEvent | 15 | 0.15 | 1 | 5 | 0 | 2026-10-05T15:38:52.462000+00:00 | 2026-10-16T15:22:47.420000+00:00 | 263h 43m |
| SolarStillDesignEvent | 14 | 0.14 | 1 | 1 | 0 | 2026-10-16T15:28:07.196000+00:00 | 2026-10-16T15:28:29.060000+00:00 | 21.9s |
| gameStartEvent | 13 | 0.13 | 1 | 1 | 0 | 2026-10-05T15:16:15.410000+00:00 | 2026-10-16T14:58:47.153000+00:00 | 263h 42m |
| gameWindowUnfocusEvent | 11 | 0.11 | 1 | 7 | 0 | 2026-10-05T15:38:15.868000+00:00 | 2026-10-16T15:31:01.568000+00:00 | 263h 52m |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-05T15:43:48.319000+00:00 | 2026-10-16T15:34:39.596000+00:00 | 263h 50m |
| chatEvent | 3 | 0.03 | 1 | 2 | 0 | 2026-10-15T15:45:54.697000+00:00 | 2026-10-16T15:12:12.691000+00:00 | 23h 26m |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-07T15:23:58.859000+00:00 | 2026-10-07T15:24:00.630000+00:00 | 1.8s |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87327.913s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.05s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.791s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.825s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.67s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 45.863s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 213.794s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.488s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 42188.997s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84133.158s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1627.716s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85749.31s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.133s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; rightShift 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 14 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 180 ft; 240 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 24 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; A,D,1,II; B,C,D,3,4,II; C,2,II; C,D,3,4,II; C,D,3,II; C,D,4,II; C,D,A,2,II; C,D,A,3,4,II; D,1,I; D,1,II; D,C,B,3,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.1x vs baseline. 
  - Observed: 574 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
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
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[130] _id=6ac3c0ebde269131f9ad1699 ts=2026-10-05T15:23:23.2910000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[221] _id=6ac3c217de269131f9ad2f89 ts=2026-10-05T15:28:23.1290000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[255] _id=6ac3c284de269131f9ad34d9 ts=2026-10-05T15:30:11.6760000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[2] _id=6ac3bf40de269131f9ace7af ts=2026-10-05T15:16:15.4100000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[642] _id=6ac3c60ade269131f9ad6a97 ts=2026-10-05T15:45:13.2660000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[693] _id=6ac51418de269131f9b465bb ts=2026-10-06T15:30:31.9380000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[1] _id=6ac3bf3fde269131f9ace7ad ts=2026-10-05T15:16:15.4090000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[437] _id=6ac3c468de269131f9ad51d5 ts=2026-10-05T15:38:16.3710000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[641] _id=6ac3c60ade269131f9ad6a91 ts=2026-10-05T15:45:13.2650000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[435] _id=6ac3c468de269131f9ad51cf ts=2026-10-05T15:38:15.8680000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[694] _id=6ac51418de269131f9b465b1 ts=2026-10-05T15:47:59.819Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[1658] _id=6ac662dbde269131f9bb99e1 ts=2026-10-06T15:47:32.578Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 3 of 64 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[776] _id=6ac514c1de269131f9b4706f ts=2026-10-06T15:33:21.2430000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[777] _id=6ac514c4de269131f9b47097 ts=2026-10-06T15:33:23.8100000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[784] _id=6ac514d5de269131f9b471b3 ts=2026-10-06T15:33:40.8770000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2712 | 0.0 | 0.913 | 350.839 | 19.663 | 429722.302 | 0.17 | 101 | 7 |
| PuzzlePieceVisibleEvent | 2125 | 0.0 | 0.05 | 405.901 | 1.779 | 433678.125 | 0.15 | 1063 | 8 |
| DialogueEvent | 2100 | 0.0 | 3.899 | 453.079 | 26.557 | 429441.508 | 0.13 | 618 | 7 |
| PlayerPositionEvent | 1559 | 9.813 | 10.003 | 556.278 | 10.13 | 429439.79 | 0.11 | 0 | 6 |
| argumentationNodeEvent | 573 | 0.005 | 0.657 | 1657.037 | 8.373 | 429465.196 | 0.04 | 52 | 5 |
| ObjectInterEvent | 243 | 0.0 | 9.807 | 3914.417 | 368.917 | 430947.62 | 0.02 | 3 | 9 |
| questEvent | 79 | 0.0 | 168.988 | 12041.015 | 83955.791 | 430779.123 | 0.0 | 13 | 11 |
| TopographicMapEvent | 63 | 0.019 | 6.825 | 10958.902 | 76448.988 | 431136.449 | 0.01 | 2 | 5 |
| Soil Key Puzzle | 57 | 0.166 | 1.791 | 10610.842 | 396.839 | 518924.484 | 0.01 | 0 | 3 |
| WaterChamberEvent | 43 | 0.205 | 5.67 | 12.453 | 44.016 | 81.374 | 4.82 | 0 | 0 |
| DEBUGMenu | 29 | 6.483 | 544.82 | 32736.158 | 86099.878 | 431022.567 | 0.0 | 0 | 14 |
| argumentationAnswerEvent | 23 | 1.314 | 45.863 | 41278.873 | 250622.008 | 429506.919 | 0.0 | 0 | 5 |
| soilMachine | 20 | 0.289 | 2.133 | 21.369 | 125.54 | 172.92 | 2.81 | 0 | 0 |
| argumentationToolEvent | 18 | 0.753 | 3.488 | 52729.797 | 323875.722 | 689578.719 | 0.0 | 0 | 2 |
| gameWindowFocusEvent | 18 | 7.152 | 1627.716 | 52849.234 | 138086.931 | 431031.963 | 0.0 | 0 | 15 |
| TerasGardenBox | 14 | 1.016 | 3.386 | 21.058 | 82.675 | 202.202 | 2.85 | 0 | 0 |
| argumentationEvent | 14 | 0.042 | 213.794 | 67816.783 | 318906.769 | 429638.684 | 0.0 | 2 | 5 |
| SolarStillDesignEvent | 13 | 0.725 | 1.618 | 1.682 | 2.489 | 2.623 | 35.68 | 0 | 0 |
| gameStartEvent | 12 | 639.55 | 84133.158 | 79112.645 | 241479.295 | 431031.963 | 0.0 | 0 | 12 |
| gameWindowUnfocusEvent | 10 | 204.348 | 85749.31 | 94996.57 | 314503.112 | 431260.184 | 0.0 | 0 | 8 |
| EndOfUnit | 4 | 85757.693 | 87327.913 | 237462.819 | 599161.159 | 689437.757 | 0.0 | 0 | 4 |
| chatEvent | 2 | 798.748 | 42188.997 | 42188.997 | 79440.221 | 83579.246 | 0.0 | 0 | 2 |
| DaniEvent | 1 | 1.771 | 1.771 | 1.771 | 1.771 | 1.771 | 33.88 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[2762] _id=6ac7b45ede269131f9c37f57 ts=2026-10-08T15:18:53.1630000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[2763] _id=6ac7b45ede269131f9c37f58 ts=2026-10-08T15:18:53.1630000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[6674] _id=6ad0eac1de269131f9dc101f ts=2026-10-15T15:01:20.4260000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[6675] _id=6ad0eac1de269131f9dc1020 ts=2026-10-15T15:01:20.4260000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[7224] _id=6ad0ed8dde269131f9dc5bde ts=2026-10-15T15:13:17.3310000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[7225] _id=6ad0ed8dde269131f9dc5bdf ts=2026-10-15T15:13:17.3310000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 88 group(s), 138 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[749] _id=6ac514a4de269131f9b46e57 ts=2026-10-06T15:32:50.6970000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[745] _id=6ac514a4de269131f9b46e5b ts=2026-10-06T15:32:50.6970000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[746] _id=6ac514a5de269131f9b46e5f ts=2026-10-06T15:32:51.2090000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[752] _id=6ac514a5de269131f9b46e67 ts=2026-10-06T15:32:51.2090000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[759] _id=6ac514a5de269131f9b46e71 ts=2026-10-06T15:32:51.8500000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[760] _id=6ac514a5de269131f9b46e73 ts=2026-10-06T15:32:51.8500000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[9497] _id=6ad24192de269131f9e52aaa ts=2026-10-16T15:24:01.8600000Z == 6ab9a8bc9a8420a1e6b56b08.jsonl[9498] _id=6ad24192de269131f9e52aab ts=2026-10-16T15:24:01.8600000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[87] _id=6ac3c06cde269131f9ad08dd ts=2026-10-05T15:21:16.3010000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[85] _id=6ac3c06dde269131f9ad08e9 ts=2026-10-05T15:21:16.3070000Z`; `989ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[260] _id=6ac3c41ede269131f9ad4c6d ts=2026-10-05T15:37:02.0640000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[290] _id=6ac3c41fde269131f9ad4c7d ts=2026-10-05T15:37:03.0530000Z`; `715ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[290] _id=6ac3c41fde269131f9ad4c7d ts=2026-10-05T15:37:03.0530000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[346] _id=6ac3c420de269131f9ad4c87 ts=2026-10-05T15:37:03.7680000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 117 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `641ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[754] _id=6ac514a5de269131f9b46e6d ts=2026-10-06T15:32:51.2090000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[759] _id=6ac514a5de269131f9b46e71 ts=2026-10-06T15:32:51.8500000Z`; `28ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[763] _id=6ac514a8de269131f9b46ea3 ts=2026-10-06T15:32:52.8530000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[764] _id=6ac514a8de269131f9b46ea9 ts=2026-10-06T15:32:52.8810000Z`; `207ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[768] _id=6ac514a8de269131f9b46eab ts=2026-10-06T15:32:52.8810000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[765] _id=6ac514a9de269131f9b46eb1 ts=2026-10-06T15:32:53.0880000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `519ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[8778] _id=6ad23d97de269131f9e4eb85 ts=2026-10-16T15:07:02.9890000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[8776] _id=6ad23d97de269131f9e4eb99 ts=2026-10-16T15:07:03.5080000Z`; `616ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[8786] _id=6ad23d9dde269131f9e4ec84 ts=2026-10-16T15:07:09.8840000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[8782] _id=6ad23d9ede269131f9e4ec96 ts=2026-10-16T15:07:10.5000000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `42ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[4794] _id=6ace5188de269131f9cf3efb ts=2026-10-13T15:43:04.1680000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[4797] _id=6ace5188de269131f9cf3efe ts=2026-10-13T15:43:04.2100000Z`; `47ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7697] _id=6ad0f0e9de269131f9dc920b ts=2026-10-15T15:27:37.0170000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[7700] _id=6ad0f0e9de269131f9dc920f ts=2026-10-15T15:27:37.0640000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 32 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `21ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[459] _id=6ac3c496de269131f9ad5507 ts=2026-10-05T15:39:01.4470000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[444] _id=6ac3c496de269131f9ad550f ts=2026-10-05T15:39:01.4680000Z`; `500ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[445] _id=6ac3c496de269131f9ad5521 ts=2026-10-05T15:39:02.4330000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[460] _id=6ac3c497de269131f9ad552f ts=2026-10-05T15:39:02.9330000Z`; `711ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[464] _id=6ac3c497de269131f9ad5525 ts=2026-10-05T15:39:02.5760000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[465] _id=6ac3c497de269131f9ad5539 ts=2026-10-05T15:39:03.2870000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `914ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[3472] _id=6ac7ba69de269131f9c41d15 ts=2026-10-08T15:44:41.1250000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[3473] _id=6ac7ba6ade269131f9c41d1d ts=2026-10-08T15:44:42.0390000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[9655] _id=6ad242dfde269131f9e53c56 ts=2026-10-16T15:29:35.4930000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[9656] _id=6ad242dfde269131f9e53c58 ts=2026-10-16T15:29:35.5000000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `514ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7076] _id=6ad0ecf1de269131f9dc4c69 ts=2026-10-15T15:10:40.9050000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[7089] _id=6ad0ecf1de269131f9dc4c7c ts=2026-10-15T15:10:41.4190000Z`; `317ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7089] _id=6ad0ecf1de269131f9dc4c7c ts=2026-10-15T15:10:41.4190000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[7090] _id=6ad0ecf1de269131f9dc4c83 ts=2026-10-15T15:10:41.7360000Z`; `289ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7090] _id=6ad0ecf1de269131f9dc4c83 ts=2026-10-15T15:10:41.7360000Z ~ 6ab9a8bc9a8420a1e6b56b08.jsonl[7083] _id=6ad0ecf2de269131f9dc4c88 ts=2026-10-15T15:10:42.0250000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2758] _id=6ac7b45bde269131f9c37f13 ts=2026-10-08T15:18:50.8700000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3521] _id=6ace4809de269131f9cf00c4 ts=2026-10-13T15:02:33.4370000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1667] _id=6ac662e5de269131f9bb9a19 ts=2026-10-07T15:19:01.3710000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2755] _id=6ac7b451de269131f9c37e57 ts=2026-10-08T15:18:41.4690000Z; 23h 47m: 6ab9a8bc9a8420a1e6b56b08.jsonl[697] _id=6ac5142bde269131f9b466f1 ts=2026-10-06T15:30:51.1620000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1659] _id=6ac662dbde269131f9bb99e3 ts=2026-10-07T15:18:50.7100000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3509] _id=6ac7ba99de269131f9c41edd ts=2026-10-08T15:45:28.3320000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3534] _id=6ace4819de269131f9cf00ce ts=2026-10-13T15:02:49.8400000Z; 23h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[686] _id=6ac3c6adde269131f9ad7851 ts=2026-10-05T15:47:56.8060000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[691] _id=6ac51444de269131f9b46893 ts=2026-10-06T15:31:16.4950000Z; 23h 32m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1651] _id=6ac5180cde269131f9b4bdb3 ts=2026-10-06T15:47:24.0010000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1685] _id=6ac6631ade269131f9bb9b6b ts=2026-10-07T15:19:54.2140000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 618 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[3506] _id=6ac7ba8ede269131f9c41e9f ts=2026-10-08T15:45:17.6760000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3507] _id=6ac7ba8ede269131f9c41ea0 ts=2026-10-08T15:45:17.6760000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[3624] _id=6ace488ade269131f9cf0360 ts=2026-10-13T15:04:42.3950000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3625] _id=6ace488ade269131f9cf0361 ts=2026-10-13T15:04:42.3950000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[3688] _id=6ace48bfde269131f9cf044c ts=2026-10-13T15:05:35.0780000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3689] _id=6ace48bfde269131f9cf044d ts=2026-10-13T15:05:35.0780000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 30m 
  - Evidence: 191h 30m: 6ab9a8bc9a8420a1e6b56b08.jsonl[638] _id=6ac3c5b4de269131f9ad6689 ts=2026-10-05T15:43:48.3190000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3758] _id=6ace4ad2de269131f9cf0ac2 ts=2026-10-13T15:14:26.0760000Z; 24h 19m: 6ab9a8bc9a8420a1e6b56b08.jsonl[5805] _id=6acf9ee8de269131f9d4a96b ts=2026-10-14T15:25:28.1360000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[8136] _id=6ad0f512de269131f9dcd702 ts=2026-10-15T15:45:21.9030000Z; 24h 11m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3758] _id=6ace4ad2de269131f9cf0ac2 ts=2026-10-13T15:14:26.0760000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[5805] _id=6acf9ee8de269131f9d4a96b ts=2026-10-14T15:25:28.1360000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3360] _id=6ac7b97dde269131f9c41237 ts=2026-10-08T15:40:45.1890000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3532] _id=6ace4818de269131f9cf00cb ts=2026-10-13T15:02:47.4910000Z; 23h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[670] _id=6ac3c680de269131f9ad74df ts=2026-10-05T15:47:11.6820000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[700] _id=6ac51437de269131f9b467a4 ts=2026-10-06T15:31:03.3640000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2709] _id=6ac66904de269131f9bc2439 ts=2026-10-07T15:45:07.3120000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2761] _id=6ac7b45ede269131f9c37f56 ts=2026-10-08T15:18:53.1610000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 101 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[2762] _id=6ac7b45ede269131f9c37f57 ts=2026-10-08T15:18:53.1630000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2763] _id=6ac7b45ede269131f9c37f58 ts=2026-10-08T15:18:53.1630000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[4459] _id=6ace4f63de269131f9cf2ac9 ts=2026-10-13T15:33:55.2480000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[4460] _id=6ace4f63de269131f9cf2aca ts=2026-10-13T15:33:55.2480000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[4853] _id=6ace51d6de269131f9cf4218 ts=2026-10-13T15:44:22.1600000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[4854] _id=6ace51d6de269131f9cf4219 ts=2026-10-13T15:44:22.1600000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3328] _id=6ac7b958de269131f9c410b3 ts=2026-10-08T15:40:08.3670000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3960] _id=6ace4cbcde269131f9cf14ac ts=2026-10-13T15:22:35.9870000Z; 23h 57m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1492] _id=6ac515c6de269131f9b48756 ts=2026-10-06T15:37:42.2470000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1944] _id=6ac666c3de269131f9bbfe2f ts=2026-10-07T15:35:29.9920000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2576] _id=6ac66835de269131f9bc17cc ts=2026-10-07T15:41:40.6260000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3173] _id=6ac7b814de269131f9c3f307 ts=2026-10-08T15:34:44.2990000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.006s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7528] _id=6ad0efdfde269131f9dc80a1 ts=2026-10-15T15:23:10.4360000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7529] _id=6ad0efdfde269131f9dc80a2 ts=2026-10-15T15:23:10.4360000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7579] _id=6ad0f013de269131f9dc8375 ts=2026-10-15T15:24:03.7160000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7580] _id=6ad0f013de269131f9dc8376 ts=2026-10-15T15:24:03.7160000Z; 6ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[87] _id=6ac3c06cde269131f9ad08dd ts=2026-10-05T15:21:16.3010000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[85] _id=6ac3c06dde269131f9ad08e9 ts=2026-10-05T15:21:16.3070000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3487] _id=6ac7ba95de269131f9c41ebe ts=2026-10-08T15:45:24.9260000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3531] _id=6ace4818de269131f9cf00ca ts=2026-10-13T15:02:44.7160000Z; 23h 42m: 6ab9a8bc9a8420a1e6b56b08.jsonl[685] _id=6ac3c6abde269131f9ad7843 ts=2026-10-05T15:47:55.4000000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[698] _id=6ac5142ede269131f9b4672d ts=2026-10-06T15:30:51.1750000Z; 23h 31m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1655] _id=6ac5180cde269131f9b4bdb9 ts=2026-10-06T15:47:24.3810000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1662] _id=6ac662eade269131f9bb9a23 ts=2026-10-07T15:19:01.4020000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 27m 
  - Evidence: 120h 27m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2873] _id=6ac7b479de269131f9c3821e ts=2026-10-08T15:19:18.4100000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[4948] _id=6ace5285de269131f9cf49f7 ts=2026-10-13T15:47:16.5350000Z; 24h 1m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1457] _id=6ac515abde269131f9b4848c ts=2026-10-06T15:37:11.8970000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2021] _id=6ac66781de269131f9bc0984 ts=2026-10-07T15:38:40.5760000Z; 23h 35m: 6ab9a8bc9a8420a1e6b56b08.jsonl[6296] _id=6acfa1eede269131f9d4d2ab ts=2026-10-14T15:38:21.1810000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7236] _id=6ad0ed96de269131f9dc5c8d ts=2026-10-15T15:13:25.4800000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1063 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[1010] _id=6ac51534de269131f9b47987 ts=2026-10-06T15:35:13.6830000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1019] _id=6ac51534de269131f9b4798b ts=2026-10-06T15:35:13.6830000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[1021] _id=6ac51552de269131f9b47c0f ts=2026-10-06T15:35:44.9400000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1124] _id=6ac51552de269131f9b47c12 ts=2026-10-06T15:35:44.9400000Z; 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[1024] _id=6ac51554de269131f9b47c37 ts=2026-10-06T15:35:45.4240000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1175] _id=6ac51554de269131f9b47c3d ts=2026-10-06T15:35:45.4240000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 8m 
  - Evidence: 144h 8m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1978] _id=6ac66729de269131f9bc055c ts=2026-10-07T15:37:13.2590000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[4928] _id=6ace5235de269131f9cf464c ts=2026-10-13T15:45:57.7430000Z; 23h 17m: 6ab9a8bc9a8420a1e6b56b08.jsonl[4936] _id=6ace525bde269131f9cf47e8 ts=2026-10-13T15:46:35.0020000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[5001] _id=6acf99d3de269131f9d44914 ts=2026-10-14T15:03:47.3820000Z; 30m 37s: 6ab9a8bc9a8420a1e6b56b08.jsonl[5012] _id=6acf99eade269131f9d44ac9 ts=2026-10-14T15:04:10.4960000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[5894] _id=6acfa118de269131f9d4c230 ts=2026-10-14T15:34:48.3920000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3034] _id=6ac7b678de269131f9c3bfd2 ts=2026-10-08T15:27:51.9720000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3825] _id=6ace4a98de269131f9cf0a14 ts=2026-10-13T15:13:28.4210000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1926] _id=6ac6666fde269131f9bbf57d ts=2026-10-07T15:34:06.6180000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3028] _id=6ac7b667de269131f9c3bc4f ts=2026-10-08T15:27:35.0200000Z; 23h 42m: 6ab9a8bc9a8420a1e6b56b08.jsonl[4527] _id=6ace4fd0de269131f9cf2e77 ts=2026-10-13T15:35:43.8450000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[5648] _id=6acf9d50de269131f9d48fbd ts=2026-10-14T15:18:39.7250000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.049s shown 
  - Evidence: 19ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[1726] _id=6ac663a5de269131f9bba3ff ts=2026-10-07T15:22:12.6900000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1730] _id=6ac663a5de269131f9bba403 ts=2026-10-07T15:22:12.7090000Z; 49ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[1725] _id=6ac663a5de269131f9bba3f8 ts=2026-10-07T15:22:12.6410000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1726] _id=6ac663a5de269131f9bba3ff ts=2026-10-07T15:22:12.6900000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3505] _id=6ac7ba8dde269131f9c41e9d ts=2026-10-08T15:45:17.6570000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3562] _id=6ace4850de269131f9cf011c ts=2026-10-13T15:03:44.5760000Z; 72h 2m: 6ab9a8bc9a8420a1e6b56b08.jsonl[533] _id=6ac3c509de269131f9ad5c31 ts=2026-10-05T15:40:56.4970000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3431] _id=6ac7ba38de269131f9c41b9e ts=2026-10-08T15:43:51.8940000Z; 47h 44m: 6ab9a8bc9a8420a1e6b56b08.jsonl[4791] _id=6ace5188de269131f9cf3ef5 ts=2026-10-13T15:43:04.1320000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7462] _id=6ad0f0cade269131f9dc9029 ts=2026-10-15T15:27:05.6440000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3382] _id=6ac7b9dade269131f9c417b5 ts=2026-10-08T15:42:18.4090000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3525] _id=6ace4821de269131f9cf00d4 ts=2026-10-13T15:02:57.0930000Z; 72h 1m: 6ab9a8bc9a8420a1e6b56b08.jsonl[534] _id=6ac3c509de269131f9ad5c33 ts=2026-10-05T15:40:56.5170000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3382] _id=6ac7b9dade269131f9c417b5 ts=2026-10-08T15:42:18.4090000Z; 47h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[4797] _id=6ace5188de269131f9cf3efe ts=2026-10-13T15:43:04.2100000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7623] _id=6ad0f091de269131f9dc8b13 ts=2026-10-15T15:26:09.1610000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.042s..0.047s shown 
  - Evidence: 42ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[4794] _id=6ace5188de269131f9cf3efb ts=2026-10-13T15:43:04.1680000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[4797] _id=6ace5188de269131f9cf3efe ts=2026-10-13T15:43:04.2100000Z; 47ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7697] _id=6ad0f0e9de269131f9dc920b ts=2026-10-15T15:27:37.0170000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7700] _id=6ad0f0e9de269131f9dc920f ts=2026-10-15T15:27:37.0640000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3504] _id=6ac7ba8bde269131f9c41e78 ts=2026-10-08T15:45:14.9830000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3547] _id=6ace4824de269131f9cf00db ts=2026-10-13T15:03:00.1790000Z; 72h 1m: 6ab9a8bc9a8420a1e6b56b08.jsonl[528] _id=6ac3c4ffde269131f9ad5bc5 ts=2026-10-05T15:40:46.4000000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3391] _id=6ac7b9ecde269131f9c41852 ts=2026-10-08T15:42:36.2780000Z; 47h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[4782] _id=6ace5182de269131f9cf3eba ts=2026-10-13T15:42:57.9510000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7626] _id=6ad0f095de269131f9dc8b81 ts=2026-10-15T15:26:13.4700000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 52 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[9317] _id=6ad2407bde269131f9e51cbf ts=2026-10-16T15:19:23.4020000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[9312] _id=6ad2407bde269131f9e51cc1 ts=2026-10-16T15:19:23.4070000Z; 7ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[3491] _id=6ac7ba81de269131f9c41e0c ts=2026-10-08T15:45:04.7790000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3397] _id=6ac7ba81de269131f9c41e0e ts=2026-10-08T15:45:04.7860000Z; 7ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[7649] _id=6ad0f0b0de269131f9dc8dac ts=2026-10-15T15:26:40.1880000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[7650] _id=6ad0f0b0de269131f9dc8dae ts=2026-10-15T15:26:40.1950000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 32m 
  - Evidence: 191h 32m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3473] _id=6ac7ba6ade269131f9c41d1d ts=2026-10-08T15:44:42.0390000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[9240] _id=6ad24014de269131f9e51840 ts=2026-10-16T15:17:40.7580000Z; 72h 2m: 6ab9a8bc9a8420a1e6b56b08.jsonl[502] _id=6ac3c4d9de269131f9ad59fb ts=2026-10-05T15:40:08.5390000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3379] _id=6ac7b9e4de269131f9c41800 ts=2026-10-08T15:42:28.4380000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 12m 
  - Evidence: 23h 12m: 6ab9a8bc9a8420a1e6b56b08.jsonl[8147] _id=6ad0f532de269131f9dcd853 ts=2026-10-15T15:45:54.6970000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[8219] _id=6ad23baede269131f9e4bde2 ts=2026-10-16T14:58:53.9430000Z; 13m 18s: 6ab9a8bc9a8420a1e6b56b08.jsonl[8219] _id=6ad23baede269131f9e4bde2 ts=2026-10-16T14:58:53.9430000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[9068] _id=6ad23eccde269131f9e507f0 ts=2026-10-16T15:12:12.6910000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2757] _id=6ac7b451de269131f9c37e59 ts=2026-10-08T15:18:41.6110000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3523] _id=6ace4809de269131f9cf00c6 ts=2026-10-13T15:02:33.5740000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1661] _id=6ac662dbde269131f9bb99e5 ts=2026-10-07T15:18:50.8620000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2757] _id=6ac7b451de269131f9c37e59 ts=2026-10-08T15:18:41.6110000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b08.jsonl[693] _id=6ac51418de269131f9b465bb ts=2026-10-06T15:30:31.9380000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1661] _id=6ac662dbde269131f9bb99e5 ts=2026-10-07T15:18:50.8620000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2756] _id=6ac7b451de269131f9c37e58 ts=2026-10-08T15:18:41.6110000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3522] _id=6ace4809de269131f9cf00c5 ts=2026-10-13T15:02:33.5740000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1660] _id=6ac662dbde269131f9bb99e4 ts=2026-10-07T15:18:50.8620000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2756] _id=6ac7b451de269131f9c37e58 ts=2026-10-08T15:18:41.6110000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b08.jsonl[692] _id=6ac51418de269131f9b465b9 ts=2026-10-06T15:30:31.9360000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[1660] _id=6ac662dbde269131f9bb99e4 ts=2026-10-07T15:18:50.8620000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8bc9a8420a1e6b56b08.jsonl[3526] _id=6ace4809de269131f9cf00c2 ts=2026-10-08T15:45:30.027Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[4391] _id=6ace4f36de269131f9cf281e ts=2026-10-13T15:33:10.2110000Z; 47h 43m: 6ab9a8bc9a8420a1e6b56b08.jsonl[6664] _id=6acfa41ede269131f9d4f654 ts=2026-10-14T15:47:41.5450000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[9677] _id=6ad24336de269131f9e54189 ts=2026-10-16T15:31:01.5680000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b08.jsonl[1658] _id=6ac662dbde269131f9bb99e1 ts=2026-10-06T15:47:32.578Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2754] _id=6ac7b451de269131f9c37e53 ts=2026-10-07T15:47:23.817Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 39m 
  - Evidence: 119h 39m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2883] _id=6ac7b55cde269131f9c39851 ts=2026-10-08T15:23:08.4140000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[3533] _id=6ace4818de269131f9cf00cc ts=2026-10-13T15:02:47.5370000Z; 23h 44m: 6ab9a8bc9a8420a1e6b56b08.jsonl[665] _id=6ac3c66bde269131f9ad7269 ts=2026-10-05T15:46:50.9690000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[696] _id=6ac5142ede269131f9b46733 ts=2026-10-06T15:30:53.3850000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b08.jsonl[2710] _id=6ac66909de269131f9bc2494 ts=2026-10-07T15:45:12.5780000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[2767] _id=6ac7b45ede269131f9c37f5c ts=2026-10-08T15:18:53.2250000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[9497] _id=6ad24192de269131f9e52aaa ts=2026-10-16T15:24:01.8600000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[9498] _id=6ad24192de269131f9e52aab ts=2026-10-16T15:24:01.8600000Z; 2ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[409] _id=6ac3c439de269131f9ad4e89 ts=2026-10-05T15:37:28.5080000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[413] _id=6ac3c439de269131f9ad4e8f ts=2026-10-05T15:37:28.5100000Z; 5ms: 6ab9a8bc9a8420a1e6b56b08.jsonl[6882] _id=6ad0ebf7de269131f9dc2f35 ts=2026-10-15T15:06:31.6700000Z -> 6ab9a8bc9a8420a1e6b56b08.jsonl[6903] _id=6ad0ebf7de269131f9dc2f37 ts=2026-10-15T15:06:31.6750000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[259] _id=6ac3c417de269131f9ad4bef ts=2026-10-05T15:36:54.9870000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[544] _id=6ac3c51fde269131f9ad5cfb ts=2026-10-05T15:41:19.1500000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[1854] _id=6ac6655dde269131f9bbd794 ts=2026-10-07T15:29:32.7970000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 24 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[940] _id=6ac51525de269131f9b47811 ts=2026-10-06T15:34:59.8760000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[930] _id=6ac51525de269131f9b47814 ts=2026-10-06T15:34:59.9410000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[941] _id=6ac51526de269131f9b4781b ts=2026-10-06T15:34:59.9960000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 75 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[754] _id=6ac514a5de269131f9b46e6d ts=2026-10-06T15:32:51.2090000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[759] _id=6ac514a5de269131f9b46e71 ts=2026-10-06T15:32:51.8500000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[760] _id=6ac514a5de269131f9b46e73 ts=2026-10-06T15:32:51.8500000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[4797] _id=6ace5188de269131f9cf3efe ts=2026-10-13T15:43:04.2100000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[7700] _id=6ad0f0e9de269131f9dc920f ts=2026-10-15T15:27:37.0640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[444] _id=6ac3c496de269131f9ad550f ts=2026-10-05T15:39:01.4680000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[8147] _id=6ad0f532de269131f9dcd853 ts=2026-10-15T15:45:54.6970000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[8219] _id=6ad23baede269131f9e4bde2 ts=2026-10-16T14:58:53.9430000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[9068] _id=6ad23eccde269131f9e507f0 ts=2026-10-16T15:12:12.6910000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[2603] _id=6ac6684ade269131f9bc18fc ts=2026-10-07T15:42:02.1160000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[5027] _id=6acf9a0cde269131f9d44c29 ts=2026-10-14T15:04:43.9230000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[6685] _id=6ad0ead8de269131f9dc1366 ts=2026-10-15T15:01:44.2320000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[650] _id=6ac3c625de269131f9ad6c29 ts=?`; `6ab9a8bc9a8420a1e6b56b08.jsonl[7876] _id=6ad0f23bde269131f9dca628 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 200 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[953] _id=6ac5152cde269131f9b478b3 ts=2026-10-06T15:35:06.9190000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[954] _id=6ac5152cde269131f9b478b9 ts=2026-10-06T15:35:06.9840000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[967] _id=6ac5152cde269131f9b478c1 ts=2026-10-06T15:35:06.9970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 227 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[745] _id=6ac514a4de269131f9b46e5b ts=2026-10-06T15:32:50.6970000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[753] _id=6ac514a6de269131f9b46e85 ts=2026-10-06T15:32:52.6710000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[755] _id=6ac514a7de269131f9b46e8b ts=2026-10-06T15:32:52.6710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 18 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[1719] _id=6ac66380de269131f9bba02c ts=2026-10-07T15:21:35.9050000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[1730] _id=6ac663a5de269131f9bba403 ts=2026-10-07T15:22:12.7090000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[1763] _id=6ac663fede269131f9bbae52 ts=2026-10-07T15:23:42.2150000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[3525] _id=6ace4821de269131f9cf00d4 ts=2026-10-13T15:02:57.0930000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 11 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[3389] _id=6ac7b9e8de269131f9c41833 ts=2026-10-08T15:42:32.2860000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[3412] _id=6ac7b9fbde269131f9c41912 ts=2026-10-08T15:42:51.4960000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[3411] _id=6ac7b9ffde269131f9c4193f ts=2026-10-08T15:42:55.7070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 401 start, 394 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 49 unmatched 'BecameCameraCentered' (totals: 469 open, 444 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 50 unmatched 'BecameVisible' (totals: 594 open, 619 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 20 open, 19 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 15 unmatched 'argumentationToolOpen' (totals: 17 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 45 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 237 of 9767 adjacent _id pairs reverse in client time; worst 89.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b08.jsonl[802] _id=6ac51501de269131f9b47531 ts=2026-10-06T15:34:24.1810000Z`; `6ab9a8bc9a8420a1e6b56b08.jsonl[814] _id=6ac51501de269131f9b47533 ts=2026-10-06T15:32:54.9020000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.39s, min -429423.87s, max -0.09s over 9768 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b08\coverage.yaml

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

### `InputEvent` — 2713 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (573); Unit 4 Dev - Dungeon (541); Unit 2 Prod (Refactor) (434); Unit 5 Dev - Dungeon (365); Unit 4 Dev (214); Unit 3 Dungeon Dev (191); Unit 1 Dev (178); Unit 5 Dev (159); Unit 4 Dev - Anderson Base (58)
- **Intervals:** median 0.91s (p5 0.09s / p95 19.66s, n=2712)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2713/2713 records)
    "pressed"  x2713
data.actionType  (string, 2713/2713 records)
    "Move"  x2027
    "Interact"  x445
    "Jump"  x145
    "Ascend"  x43
    "Hoverboard"  x35
    "Map"  x9
    "Sprint"  x6
    "Descend"  x2
    "SkipCinematic"  x1
data.key  (string, 2713/2713 records, 8 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2713/2713 records)
    "Player"  x2148
    "Drone"  x565
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2126 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1260); Unit 4 Dev (370); Unit 5 Dev - Dungeon (327); Unit 3 Dungeon Dev (169)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.78s, n=2125)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2126/2126 records)
    "BecameInvisible"  x619
    "BecameVisible"  x594
    "BecameCameraCentered"  x469
    "BecameCameraUncentered"  x444
data.pieceId  (string, 2126/2126 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2126/2126 records)
    1267 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2101 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (633); Unit 3 Dev (365); Unit 4 Dev (304); Unit 5 Dev (230); Unit 1 Dev (195); Unit 4 Dev - Dungeon (122); Unit 3 Dungeon Dev (113); Unit 4 Dev - Anderson Base (73); Unit 5 Dev - Dungeon (66)
- **eventKey:** present on 1306 of 2101 records
- **Intervals:** median 3.90s (p5 0.00s / p95 26.56s, n=2100)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1306; [conversationId, dialogueEventType] x795
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2101/2101 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2101/2101 records)
    "DialogueNodeEvent"  x1306
    "DialogueStartEvent"  x401
    "DialogueFinishEvent"  x394
data.nodeId  (number, 1306/2101 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1573 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (508); Unit 3 Dev (247); Unit 4 Dev (192); Unit 1 Dev (164); Unit 5 Dev (132); Unit 4 Dev - Dungeon (123); Unit 5 Dev - Dungeon (87); Unit 3 Dungeon Dev (77); Unit 4 Dev - Anderson Base (43)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=1559)
- **Fields under `data`:**

```text
data.position  (object, 1573/1573 records)
data.position.x  (number, 1573/1573 records)
    numeric range -653.53 .. 1556.41 (530 unique)
data.position.y  (number, 1573/1573 records)
    numeric range -114.326 .. 220.946 (404 unique)
data.position.z  (number, 1573/1573 records)
    numeric range -1034.4 .. 1984.42 (530 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 574 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (216); Unit 5 Dev (138); Unit 3 Dev (99); Unit 4 Dev - Anderson Base (61); Unit 1 Dev (60)
- **Intervals:** median 0.66s (p5 0.04s / p95 8.37s, n=573)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 574/574 records)
    "argumentationNodeHoverEnd"  x252
    "argumentationNodeHoverStart"  x251
    "argumentationNodeAdd"  x47
    "argumentationNodeRemove"  x24
data.argumentationTitle  (string, 574/574 records)
    "Unit 2 – Watershed"  x216
    "Unit 5"  x138
    "Unit 3 - Pollution Upstream"  x99
    "Unit 4 - Flooding"  x61
    "Unit 1 - Argumentation Tutorial"  x37
    "Unit 1 - Freshwater"  x23
data.nodeName  (string, 574/574 records)
    "A"  x97
    "B"  x80
    "1"  x76
    "I"  x61
    "D"  x59
    "II"  x56
    "3"  x43
    "C"  x32
    "2"  x31
    "4"  x30
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 244 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (88); Unit 2 Prod (Refactor) (37); Unit 3 Dungeon Dev (31); Unit 4 Dev (27); Unit 5 Dev - Dungeon (18); Unit 1 Dev (15); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (7)
- **Intervals:** median 9.81s (p5 0.64s / p95 368.92s, n=243)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 244/244 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 244/244 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 80 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (11); Unit 4 Dev (9); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 80 of 80 records
- **Intervals:** median 168.99s (p5 0.01s / p95 83955.79s, n=79)
- **`data` key-set variants:** [questEventType, questID, questName] x45; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 80/80 records)
    "questActiveEvent"  x45
    "questFinishEvent"  x35
data.questID  (string, 80/80 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 80/80 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/80 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 64 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (33); Unit 3 Dev (31)
- **Intervals:** median 6.83s (p5 0.53s / p95 76448.99s, n=63)
- **`data` key-set variants:** [actionType, featureUsed] x39; [actionType, featureUsed, location] x22; [actionType, featureUsed, legendName] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 64/64 records)
    "MapOpenEvent"  x20
    "MapCloseEvent"  x19
    "WaypointMoveEvent"  x13
    "WaypointSetEvent"  x7
    "Selected"  x3
    "WaypointResetEvent"  x2
data.featureUsed  (string, 64/64 records)
    "Map"  x39
    "Waypoint"  x22
    "Legend"  x3
data.legendName  (string, 3/64 records)
    "150 ft"  x1
    "180 ft"  x1
    "240 ft"  x1
data.location  (object, 22/64 records)
data.location.x  (number, 22/64 records)
    numeric range -284.264 .. 497.42 (18 unique)
data.location.y  (number, 22/64 records)
    numeric range -157.892 .. 225.921 (19 unique)
data.location.z  (number, 22/64 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 4 Dev (22); Unit 3 Dev (14)
- **Intervals:** median 1.79s (p5 0.30s / p95 396.84s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x50; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/58 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/58 records)
    "Unit 3 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 50/58 records)
    "RightDrag"  x29
    "LeftDrag"  x21
data.currentSoilType  (string, 50/58 records)
    "CLAY"  x12
    "CLAYSAND"  x12
    "CLAYROCK"  x9
    "SAND"  x9
    "SANDGRAVEL"  x4
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 50/58 records)
    "false"  x36
    "true"  x14
data.waterLevelStatus  (string, 50/58 records)
    "TooHigh"  x22
    "TooLow"  x15
    "Proper"  x13
data.waterRetentionChange  (string, 50/58 records)
    "Increase"  x23
    "NoChange"  x14
    "Decrease"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 44 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (44)
- **Intervals:** median 5.67s (p5 0.29s / p95 44.02s, n=43)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "On"  x27
    "Off"  x17
data.floor  (string, 44/44 records)
    "3"  x24
    "4"  x14
    "1"  x3
    "2"  x3
data.machineNumber  (string, 44/44 records)
    "One"  x43
    "Two"  x1
data.machineType  (string, 44/44 records)
    "Condenser"  x20
    "DualChamber_Condenser"  x11
    "Evaporator"  x9
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 44/44 records)
    "2"  x23
    "3"  x13
    "1"  x4
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 3 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 544.82s (p5 7.68s / p95 86099.88s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 24 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (10); Unit 2 Prod (Refactor) (6); Unit 1 Dev (3); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 45.86s (p5 4.97s / p95 250622.01s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "submitAnswerEvent"  x24
data.answerSubmitted  (string, 24/24 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 24/24 records)
    "Unit 5"  x10
    "Unit 2 – Watershed"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 2.13s (p5 0.32s / p95 125.54s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Bedrock"  x9
    "Clay"  x9
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 21/21 records)
    "5"  x19
    "3"  x1
    "4"  x1
data.machine  (string, 21/21 records)
    "1"  x20
    "2"  x1
data.row  (string, 21/21 records)
    "BottomRow"  x12
    "TopRow"  x9
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 19 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 5 Dev (5); Unit 1 Dev (3)
- **Intervals:** median 3.49s (p5 0.79s / p95 323875.72s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "argumentationToolOpen"  x17
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 19/19 records)
    "Unit 2 – Watershed"  x11
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 19/19 records)
    "BackingInfoPanel - Waterfall Data"  x6
    "BackingInfoPanel - Watershed Graph"  x5
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowFocusEvent` — 19 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 3 Dev (2); Transition (1); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1627.72s (p5 175.72s / p95 138086.93s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 3.39s (p5 1.16s / p95 82.68s, n=14)
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records, 8 empty-string)
    ""  x8
    "cameraPlaced"  x7
data.boxId  (string, 15/15 records)
    "1"  x6
    "2"  x5
    "0"  x4
data.soilType  (string, 15/15 records)
    "Gravel"  x6
    "Sand"  x5
    "Clay"  x2
    "None"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 213.79s (p5 0.05s / p95 318906.77s, n=14)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 14 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (14)
- **Intervals:** median 1.62s (p5 1.03s / p95 2.49s, n=13)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x13; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "optionSelected"  x13
    "DesignSubmitted"  x1
data.designSelections  (object, 1/14 records)
data.designSelections.glassRoofTemperature  (string, 1/14 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/14 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/14 records)
    "Tilted Out"  x1
data.featureUsed  (string, 14/14 records)
    "RoofStyle"  x7
    "ExtraCovering"  x5
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 13/14 records)
    "Tilted Out"  x3
    "Uncovered"  x3
    "Covered"  x2
    "Flat"  x2
    "Tilted In"  x2
    "Hot"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 84133.16s (p5 688.39s / p95 241479.30s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Transition (1); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 85749.31s (p5 375.17s / p95 314503.11s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 87327.91s (p5 85953.35s / p95 599161.16s, n=4)
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
- **Intervals:** median 42189.00s (p5 4937.77s / p95 79440.22s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1.77s (p5 1.77s / p95 1.77s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a915116:wasm-function[108544]:0x24e60da
    at wasm://wasm/0a915116:wasm-function[3309]:0x143bd9
    at wasm://wasm/0a915116:wasm-function[59793]:0x11abccc
    at wasm://wasm/0a915116:wasm-function[3347]:0x145fec
    at wasm://wasm/0a915116:wasm-function[82501]:0x170b4af
    at wasm://wasm/0a915116:wasm-function[83451]:0x171f21d
    at wasm://wasm/0a915116:wasm-function[110308]:0x259f6a8
    at invoke_iiii (blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:474038)
    at wasm://wasm/0a915116:wasm-function[83436]:0x171e8bd
    at wasm://wasm/0a915116:wasm-function[1942]:0xf58e4
    at wasm://wasm/0a915116:wasm-function[109965]:0x256667c
    at wasm://wasm/0a915116:wasm-function[106271]:0x24b7432
    at wasm://wasm/0a915116:wasm-function[84075]:0x1745541
    at wasm://wasm/0a915116:wasm-function[84074]:0x1745477
    at wasm://wasm/0a915116:wasm-function[104597]:0x23ea9bc
    at wasm://wasm/0a915116:wasm-function[104583]:0x23e6a91
    at wasm://wasm/0a915116:wasm-function[103961]:0x235b2a8
    at wasm://wasm/0a915116:wasm-function[105691]:0x245f4f0
    at wasm://wasm/0a915116:wasm-function[105691]:0x245f565
    at wasm://wasm/0a915116:wasm-function[110043]:0x256eaaf
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:23580
    at _JS_CallAsLongAsNoExceptionsSeen (blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:23594)
    at wasm://wasm/0a915116:wasm-function[110044]:0x256ebbe
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at browserIterationFunc (blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:115768)
    at callUserCallback (blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:98130)
    at Object.runIter (blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:99497)
    at Browser_mainLoop_runner (blob:https://mhs.adroit.games/e4b7147d-c2a3-4d37-944f-4c8f3e442549:9:115294)"  x1
data.type  (string, 2/2 records)
    "runtime_error"  x1
    "unhandled_rejection"  x1
data.unitId  (string, 2/2 records)
    "unit2"  x1
    "unit4"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
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
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TerasGardenBox` data.actionType: "" (8x)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "Selected" (3x); "WaypointMoveEvent" (13x); "WaypointResetEvent" (2x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (3x); "Waypoint" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (24x)
- `soilMachine` data.canisterType: "Bedrock" (9x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*