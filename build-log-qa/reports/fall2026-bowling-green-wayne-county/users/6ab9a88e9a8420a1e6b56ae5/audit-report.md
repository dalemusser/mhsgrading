# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae5

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae5
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae5.jsonl
- **Records:** 9349 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae5
- **Time span:** 2026-10-06T13:14:27.433000+00:00 .. 2026-10-16T13:26:55.782000+00:00 (240h 12m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae5\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 9349 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 92 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2368 | 25.33 | 1 | 9 | 0 | 2026-10-06T13:14:41.223000+00:00 | 2026-10-16T13:26:55.782000+00:00 | 240h 12m |
| PuzzlePieceVisibleEvent | 2130 | 22.78 | 1 | 4 | 0 | 2026-10-06T13:47:19.206000+00:00 | 2026-10-15T13:42:02.140000+00:00 | 215h 54m |
| DialogueEvent | 2127 | 22.75 | 1 | 9 | 1321 | 2026-10-06T13:14:57.836000+00:00 | 2026-10-16T13:26:51.471000+00:00 | 240h 11m |
| PlayerPositionEvent | 1710 | 18.29 | 1 | 9 | 0 | 2026-10-06T13:14:37.556000+00:00 | 2026-10-16T13:26:52.359000+00:00 | 240h 12m |
| argumentationNodeEvent | 310 | 3.32 | 1 | 5 | 0 | 2026-10-06T13:35:52.439000+00:00 | 2026-10-16T13:15:20.774000+00:00 | 239h 39m |
| ObjectInterEvent | 256 | 2.74 | 1 | 9 | 0 | 2026-10-06T13:19:41.669000+00:00 | 2026-10-16T13:26:55.782000+00:00 | 240h 7m |
| Soil Key Puzzle | 126 | 1.35 | 1 | 3 | 0 | 2026-10-06T13:54:12.583000+00:00 | 2026-10-14T13:21:32.223000+00:00 | 191h 27m |
| questEvent | 79 | 0.85 | 1 | 9 | 79 | 2026-10-06T13:14:57.810000+00:00 | 2026-10-16T13:23:30.541000+00:00 | 240h 8m |
| TopographicMapEvent | 57 | 0.61 | 1 | 2 | 0 | 2026-10-06T13:47:54.875000+00:00 | 2026-10-14T02:49:52.388000+00:00 | 181h 1m |
| DEBUGMenu | 29 | 0.31 | 1 | 9 | 0 | 2026-10-06T13:14:37.544000+00:00 | 2026-10-16T13:10:46.123000+00:00 | 239h 56m |
| WaterChamberEvent | 24 | 0.26 | 1 | 1 | 0 | 2026-10-15T13:40:45.051000+00:00 | 2026-10-15T13:51:31.467000+00:00 | 10m 46s |
| argumentationAnswerEvent | 18 | 0.19 | 1 | 5 | 0 | 2026-10-06T13:37:06.580000+00:00 | 2026-10-16T13:15:31.395000+00:00 | 239h 38m |
| argumentationEvent | 18 | 0.19 | 1 | 5 | 0 | 2026-10-06T13:36:46.291000+00:00 | 2026-10-16T13:15:31.445000+00:00 | 239h 38m |
| gameWindowFocusEvent | 16 | 0.17 | 1 | 3 | 0 | 2026-10-06T13:14:27.433000+00:00 | 2026-10-16T13:10:46.273000+00:00 | 239h 56m |
| argumentationToolEvent | 14 | 0.15 | 1 | 3 | 0 | 2026-10-06T13:36:43.541000+00:00 | 2026-10-13T13:36:15.330000+00:00 | 167h 59m |
| gameStartEvent | 14 | 0.15 | 1 | 1 | 0 | 2026-10-06T13:14:27.435000+00:00 | 2026-10-16T13:10:46.273000+00:00 | 239h 56m |
| soilMachine | 14 | 0.15 | 1 | 1 | 0 | 2026-10-14T13:36:33.841000+00:00 | 2026-10-14T13:47:40.038000+00:00 | 11m 6s |
| SolarStillDesignEvent | 12 | 0.13 | 1 | 1 | 0 | 2026-10-16T13:20:48.234000+00:00 | 2026-10-16T13:21:11.009000+00:00 | 22.8s |
| TerasGardenBox | 8 | 0.09 | 1 | 1 | 0 | 2026-10-15T13:25:06.731000+00:00 | 2026-10-15T13:26:17.178000+00:00 | 1m 10s |
| gameWindowUnfocusEvent | 6 | 0.06 | 1 | 4 | 0 | 2026-10-06T13:18:15.762000+00:00 | 2026-10-13T16:11:02.566000+00:00 | 170h 52m |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-06T13:42:30.803000+00:00 | 2026-10-16T13:26:55.767000+00:00 | 239h 44m |
| DaniEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-13T16:10:15.636000+00:00 | 2026-10-14T02:47:49.444000+00:00 | 10h 37m |
| chatEvent | 4 | 0.04 | 1 | 2 | 0 | 2026-10-15T13:35:12.683000+00:00 | 2026-10-16T13:10:55.366000+00:00 | 23h 35m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 108685.363s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.554s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 17.143s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.077s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.958s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 9.12s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 28.992s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.824s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 39199.802s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 37730.56s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 44155.227s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 23.234s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.3x vs baseline. 
  - Observed: 126 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 12 records 
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
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,C,2,II; A,C,B,2,II; A,D,1,II; B,5,I; C,2,II; C,A,2,II; C,D,2,II; C,D,3,4,II; C,D,3,II; C,D,4,II 
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
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[144] _id=6ac4f5ddde269131f9b047c5 ts=2026-10-06T13:21:32.5780000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[171] _id=6ac4f6bdde269131f9b079e0 ts=2026-10-06T13:25:16.0000000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[253] _id=6ac4f790de269131f9b096ac ts=2026-10-06T13:28:46.9460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[6] _id=6ac4f434de269131f9b02f42 ts=2026-10-06T13:14:27.4350000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[576] _id=6ac4fb22de269131f9b13f53 ts=2026-10-06T13:44:01.3030000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[1596] _id=6ac64838de269131f9b8edba ts=2026-10-07T13:25:11.4570000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[7] _id=6ac4f434de269131f9b02f3c ts=2026-10-06T13:14:27.4330000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[58] _id=6ac4f51ade269131f9b03a17 ts=2026-10-06T13:18:17.1650000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[572] _id=6ac4fb22de269131f9b13f42 ts=2026-10-06T13:44:01.3020000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[60] _id=6ac4f518de269131f9b03a05 ts=2026-10-06T13:18:15.7620000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[1593] _id=6ac64838de269131f9b8edae ts=2026-10-06T13:59:40.814Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[2837] _id=6ac79a80de269131f9c035ed ts=2026-10-07T13:59:46.601Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2367 | 0.0 | 1.554 | 365.329 | 24.572 | 386110.938 | 0.16 | 36 | 9 |
| PuzzlePieceVisibleEvent | 2129 | 0.0 | 0.077 | 365.093 | 2.75 | 432828.797 | 0.16 | 874 | 7 |
| DialogueEvent | 2126 | 0.0 | 3.532 | 406.733 | 26.294 | 385540.064 | 0.15 | 606 | 9 |
| PlayerPositionEvent | 1698 | 9.79 | 10.001 | 461.647 | 10.117 | 385526.788 | 0.13 | 0 | 7 |
| argumentationNodeEvent | 309 | 0.006 | 0.833 | 2792.131 | 10.195 | 385639.396 | 0.02 | 28 | 6 |
| ObjectInterEvent | 255 | 0.0 | 17.143 | 3389.938 | 406.832 | 429910.292 | 0.02 | 5 | 9 |
| Soil Key Puzzle | 125 | 0.001 | 0.454 | 5513.917 | 11.125 | 517985.918 | 0.01 | 9 | 3 |
| questEvent | 78 | 0.0 | 202.88 | 11083.497 | 83464.603 | 385601.798 | 0.01 | 13 | 14 |
| TopographicMapEvent | 56 | 0.017 | 9.12 | 11637.813 | 49974.135 | 430357.9 | 0.01 | 2 | 5 |
| DEBUGMenu | 28 | 8.841 | 686.199 | 30848.878 | 86124.073 | 387306.609 | 0.0 | 0 | 14 |
| WaterChamberEvent | 23 | 2.48 | 13.346 | 28.105 | 76.72 | 95.917 | 2.13 | 0 | 0 |
| argumentationAnswerEvent | 17 | 2.975 | 28.992 | 50747.342 | 216296.937 | 385753.374 | 0.0 | 0 | 6 |
| argumentationEvent | 17 | 0.034 | 97.576 | 50748.538 | 216207.335 | 385624.033 | 0.0 | 1 | 6 |
| gameWindowFocusEvent | 15 | 76.086 | 37730.56 | 57585.256 | 176819.222 | 387330.598 | 0.0 | 0 | 12 |
| argumentationToolEvent | 13 | 0.976 | 4.824 | 46520.907 | 258673.083 | 385642.984 | 0.0 | 0 | 3 |
| gameStartEvent | 13 | 76.086 | 39199.802 | 66444.526 | 206892.276 | 387330.598 | 0.0 | 0 | 11 |
| soilMachine | 13 | 1.139 | 23.234 | 51.246 | 168.777 | 199.003 | 1.17 | 0 | 0 |
| SolarStillDesignEvent | 11 | 0.838 | 1.623 | 2.07 | 4.241 | 4.273 | 28.98 | 0 | 0 |
| TerasGardenBox | 7 | 1.251 | 1.958 | 10.064 | 32.563 | 37.866 | 5.96 | 0 | 0 |
| gameWindowUnfocusEvent | 5 | 2485.052 | 44155.227 | 123033.361 | 395234.569 | 472441.765 | 0.0 | 0 | 5 |
| EndOfUnit | 4 | 85932.014 | 108685.363 | 215766.241 | 494511.053 | 559762.225 | 0.0 | 0 | 4 |
| DaniEvent | 3 | 1.916 | 1.926 | 12751.269 | 34425.162 | 38249.966 | 0.0 | 0 | 1 |
| chatEvent | 3 | 76.208 | 1039.62 | 28314.228 | 75548.131 | 83826.855 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 47 group(s), 64 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[760] _id=6ac4fc4ede269131f9b184fe ts=2026-10-06T13:48:53.3160000Z == 6ab9a88e9a8420a1e6b56ae5.jsonl[761] _id=6ac4fc4ede269131f9b18509 ts=2026-10-06T13:48:53.3160000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[850] _id=6ac4fc78de269131f9b191d9 ts=2026-10-06T13:49:43.3100000Z == 6ab9a88e9a8420a1e6b56ae5.jsonl[847] _id=6ac4fc78de269131f9b191eb ts=2026-10-06T13:49:43.3100000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[853] _id=6ac4fc7ade269131f9b1927c ts=2026-10-06T13:49:43.8630000Z == 6ab9a88e9a8420a1e6b56ae5.jsonl[802] _id=6ac4fc7ade269131f9b19289 ts=2026-10-06T13:49:43.8630000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[9135] _id=6ad223b9de269131f9e3692a ts=2026-10-16T13:16:40.5790000Z == 6ab9a88e9a8420a1e6b56ae5.jsonl[9136] _id=6ad223b9de269131f9e3692b ts=2026-10-16T13:16:40.5790000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[108] _id=6ac4f56ede269131f9b03e6c ts=2026-10-06T13:19:41.6690000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[107] _id=6ac4f56ede269131f9b03e70 ts=2026-10-06T13:19:41.6740000Z`; `574ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[8287] _id=6ad0d7a0de269131f9dad1e6 ts=2026-10-15T13:39:44.4610000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[8260] _id=6ad0d7a1de269131f9dad1f9 ts=2026-10-15T13:39:45.0350000Z`; `203ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[8260] _id=6ad0d7a1de269131f9dad1f9 ts=2026-10-15T13:39:45.0350000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[8291] _id=6ad0d7a1de269131f9dad20b ts=2026-10-15T13:39:45.2380000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 112 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `91ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[714] _id=6ac4fc4ade269131f9b183ba ts=2026-10-06T13:48:39.4450000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[725] _id=6ac4fc4ade269131f9b183c0 ts=2026-10-06T13:48:39.5360000Z`; `96ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[759] _id=6ac4fc4cde269131f9b18498 ts=2026-10-06T13:48:40.6670000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[702] _id=6ac4fc4cde269131f9b184a6 ts=2026-10-06T13:48:40.7630000Z`; `89ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[690] _id=6ac4fc4dde269131f9b184cf ts=2026-10-06T13:48:53.1620000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[703] _id=6ac4fc4dde269131f9b184db ts=2026-10-06T13:48:53.2510000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `301ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4617] _id=6ace352ade269131f9cecce4 ts=2026-10-13T13:42:01.6330000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[4616] _id=6ace352bde269131f9ceccec ts=2026-10-13T13:42:01.9340000Z`; `478ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4618] _id=6ace352ade269131f9cecce8 ts=2026-10-13T13:42:01.7790000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[4620] _id=6ace352bde269131f9ceccf0 ts=2026-10-13T13:42:02.2570000Z`; `324ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4616] _id=6ace352bde269131f9ceccec ts=2026-10-13T13:42:01.9340000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[4621] _id=6ace352bde269131f9ceccf1 ts=2026-10-13T13:42:02.2580000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `51ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4512] _id=6ace33ecde269131f9ceba5f ts=2026-10-13T13:36:43.9300000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[4496] _id=6ace33ecde269131f9ceba67 ts=2026-10-13T13:36:43.9810000Z`; `34ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7739] _id=6ad0d346de269131f9da6718 ts=2026-10-15T13:21:10.6270000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[7736] _id=6ad0d346de269131f9da6720 ts=2026-10-15T13:21:10.6610000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `24ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[385] _id=6ac4f975de269131f9b0e96a ts=2026-10-06T13:36:52.6950000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[386] _id=6ac4f975de269131f9b0e976 ts=2026-10-06T13:36:52.7190000Z`; `730ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[3761] _id=6acd83ffde269131f9ce85c3 ts=2026-10-13T01:06:06.8270000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[3754] _id=6acd8400de269131f9ce85c9 ts=2026-10-13T01:06:07.5570000Z`; `242ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[3764] _id=6acd841ade269131f9ce85ff ts=2026-10-13T01:06:33.2480000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[3765] _id=6acd841ade269131f9ce8603 ts=2026-10-13T01:06:33.4900000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[9260] _id=6ad22513de269131f9e386ca ts=2026-10-16T13:22:26.8580000Z ~ 6ab9a88e9a8420a1e6b56ae5.jsonl[9259] _id=6ad22513de269131f9e386ce ts=2026-10-16T13:22:26.8630000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 107h 35m 
  - Evidence: 107h 35m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2838] _id=6ac79a98de269131f9c03769 ts=2026-10-08T13:28:55.3570000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3707] _id=6acd8383de269131f9ce84d8 ts=2026-10-13T01:04:01.9660000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1597] _id=6ac64843de269131f9b8f061 ts=2026-10-07T13:25:22.4260000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2834] _id=6ac79a80de269131f9c035ef ts=2026-10-08T13:28:31.3880000Z; 23h 41m: 6ab9a88e9a8420a1e6b56ae5.jsonl[577] _id=6ac4fb2bde269131f9b141b3 ts=2026-10-06T13:44:10.6160000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1594] _id=6ac64838de269131f9b8edb8 ts=2026-10-07T13:25:11.3230000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 10h 37m 
  - Evidence: 10h 37m: 6ab9a88e9a8420a1e6b56ae5.jsonl[5694] _id=6ace57eade269131f9cf5895 ts=2026-10-13T16:10:17.5520000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[5722] _id=6aceed53de269131f9d2aed7 ts=2026-10-14T02:47:47.5180000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 107h 5m 
  - Evidence: 107h 5m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3705] _id=6ac7a18ede269131f9c15781 ts=2026-10-08T13:58:37.7390000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3714] _id=6acd8392de269131f9ce84ec ts=2026-10-13T01:04:17.8030000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2828] _id=6ac65050de269131f9ba3c40 ts=2026-10-07T13:59:43.4180000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2841] _id=6ac79a9ade269131f9c037b9 ts=2026-10-08T13:28:57.5480000Z; 23h 28m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1582] _id=6ac4fe89de269131f9b22640 ts=2026-10-06T13:58:32.3380000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1613] _id=6ac6488ede269131f9b9016c ts=2026-10-07T13:26:37.4310000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 606 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[3784] _id=6acd841ede269131f9ce8611 ts=2026-10-13T01:06:36.8630000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3785] _id=6acd841ede269131f9ce8612 ts=2026-10-13T01:06:36.8630000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7673] _id=6ad0d2e9de269131f9da61d6 ts=2026-10-15T13:19:37.2410000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7674] _id=6ad0d2e9de269131f9da61d7 ts=2026-10-15T13:19:37.2410000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[8900] _id=6ad0dc61de269131f9db6a05 ts=2026-10-15T14:00:00.9710000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[8902] _id=6ad2220ade269131f9e34ea4 ts=2026-10-15T14:00:00.971Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 155h 29m 
  - Evidence: 155h 29m: 6ab9a88e9a8420a1e6b56ae5.jsonl[569] _id=6ac4fac7de269131f9b12c26 ts=2026-10-06T13:42:30.8030000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3889] _id=6acd855ade269131f9ce87d1 ts=2026-10-13T01:11:53.0280000Z; 34h 39m: 6ab9a88e9a8420a1e6b56ae5.jsonl[5857] _id=6aceef21de269131f9d2b154 ts=2026-10-14T02:55:29.3390000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[8056] _id=6ad0d673de269131f9dab776 ts=2026-10-15T13:34:43.7530000Z; 25h 43m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3889] _id=6acd855ade269131f9ce87d1 ts=2026-10-13T01:11:53.0280000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[5857] _id=6aceef21de269131f9d2b154 ts=2026-10-14T02:55:29.3390000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 107h 15m 
  - Evidence: 107h 15m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3617] _id=6ac7a0a3de269131f9c14021 ts=2026-10-08T13:54:43.1270000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3848] _id=6acd84e3de269131f9ce873c ts=2026-10-13T01:09:54.0650000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2772] _id=6ac64f94de269131f9ba2f52 ts=2026-10-07T13:56:34.9900000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2840] _id=6ac79a9ade269131f9c037b8 ts=2026-10-08T13:28:57.5220000Z; 23h 25m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1506] _id=6ac4fecade269131f9b235b9 ts=2026-10-06T13:59:37.3580000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1600] _id=6ac6484ade269131f9b8f22c ts=2026-10-07T13:25:29.4020000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 36 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[3201] _id=6ac79e45de269131f9c0d255 ts=2026-10-08T13:44:37.1860000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3202] _id=6ac79e45de269131f9c0d256 ts=2026-10-08T13:44:37.1860000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4285] _id=6ace3210de269131f9cea807 ts=2026-10-13T13:28:47.4390000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4286] _id=6ace3210de269131f9cea808 ts=2026-10-13T13:28:47.4390000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[5346] _id=6ace5518de269131f9cf4efd ts=2026-10-13T15:58:15.9510000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[5347] _id=6ace5518de269131f9cf4efe ts=2026-10-13T15:58:15.9510000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3598] _id=6ac7a07dde269131f9c13b46 ts=2026-10-08T13:54:04.0150000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3969] _id=6ace2fd3de269131f9ce9473 ts=2026-10-13T13:19:14.3070000Z; 23h 55m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2457] _id=6ac64e9ede269131f9ba1111 ts=2026-10-07T13:52:29.6180000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3343] _id=6ac79efbde269131f9c0f2fa ts=2026-10-08T13:47:38.5270000Z; 23h 51m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1511] _id=6ac4fd85de269131f9b1d896 ts=2026-10-06T13:54:12.5890000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2042] _id=6ac64d1cde269131f9b9ec78 ts=2026-10-07T13:46:03.3030000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7291] _id=6acf8a2ede269131f9d3a94f ts=2026-10-14T13:57:01.6850000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7292] _id=6acf8a2ede269131f9d3a950 ts=2026-10-14T13:57:01.6850000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7358] _id=6acf8a7ede269131f9d3b7b6 ts=2026-10-14T13:58:21.0760000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7359] _id=6acf8a7ede269131f9d3b7b7 ts=2026-10-14T13:58:21.0760000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7479] _id=6ad0d193de269131f9da5312 ts=2026-10-15T13:13:54.8230000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7480] _id=6ad0d193de269131f9da5313 ts=2026-10-15T13:13:54.8230000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 107h 5m 
  - Evidence: 107h 5m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3706] _id=6ac7a196de269131f9c15822 ts=2026-10-08T13:58:46.2600000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3711] _id=6acd8391de269131f9ce84e7 ts=2026-10-13T01:04:13.0480000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2826] _id=6ac6504bde269131f9ba3bed ts=2026-10-07T13:59:38.2140000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2839] _id=6ac79a9ade269131f9c037b7 ts=2026-10-08T13:28:55.3720000Z; 23h 25m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1591] _id=6ac4fec6de269131f9b234cc ts=2026-10-06T13:59:33.7820000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1598] _id=6ac64846de269131f9b8f156 ts=2026-10-07T13:25:22.4500000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 13m 
  - Evidence: 120h 13m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2921] _id=6ac79ab4de269131f9c03ad2 ts=2026-10-08T13:29:22.6820000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4686] _id=6ace3571de269131f9ced02c ts=2026-10-13T13:43:11.4790000Z; 23h 55m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1491] _id=6ac4fd54de269131f9b1cc50 ts=2026-10-06T13:53:20.9960000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2132] _id=6ac64dddde269131f9b9fa66 ts=2026-10-07T13:49:15.8660000Z; 23h 43m: 6ab9a88e9a8420a1e6b56ae5.jsonl[7146] _id=6acf88d9de269131f9d37f0e ts=2026-10-14T13:51:19.6200000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[8069] _id=6ad0d698de269131f9daba65 ts=2026-10-15T13:35:19.2520000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 874 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[1000] _id=6ac4fc95de269131f9b19b29 ts=2026-10-06T13:50:10.7100000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[957] _id=6ac4fc95de269131f9b19b2e ts=2026-10-06T13:50:10.7100000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[1017] _id=6ac4fcd2de269131f9b1ad0d ts=2026-10-06T13:51:13.0410000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1019] _id=6ac4fcd2de269131f9b1ad11 ts=2026-10-06T13:51:13.0410000Z; 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[1060] _id=6ac4fca3de269131f9b19fb8 ts=2026-10-06T13:50:25.8070000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1062] _id=6ac4fca3de269131f9b19fc6 ts=2026-10-06T13:50:25.8070000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 53m 
  - Evidence: 143h 53m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2117] _id=6ac64db1de269131f9b9f76d ts=2026-10-07T13:48:32.6000000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4607] _id=6ace3513de269131f9cecbfe ts=2026-10-13T13:41:38.5180000Z; 23h 51m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1513] _id=6ac4fd88de269131f9b1d972 ts=2026-10-06T13:54:15.5710000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2043] _id=6ac64d1cde269131f9b9ec70 ts=2026-10-07T13:46:03.2980000Z; 23h 38m: 6ab9a88e9a8420a1e6b56ae5.jsonl[4666] _id=6ace3548de269131f9cece74 ts=2026-10-13T13:42:31.5520000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[5927] _id=6acf81cbde269131f9d2ed0f ts=2026-10-14T13:21:14.1790000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4620] _id=6ace352bde269131f9ceccf0 ts=2026-10-13T13:42:02.2570000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4621] _id=6ace352bde269131f9ceccf1 ts=2026-10-13T13:42:02.2580000Z; 1ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4621] _id=6ace352bde269131f9ceccf1 ts=2026-10-13T13:42:02.2580000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4622] _id=6ace352bde269131f9ceccf2 ts=2026-10-13T13:42:02.2590000Z; 1ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[4623] _id=6ace352bde269131f9ceccf6 ts=2026-10-13T13:42:02.5570000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4624] _id=6ace352bde269131f9ceccf7 ts=2026-10-13T13:42:02.5580000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3279] _id=6ac79eaade269131f9c0e572 ts=2026-10-08T13:46:17.6010000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3962] _id=6ace2fc0de269131f9ce9396 ts=2026-10-13T13:18:55.5010000Z; 23h 53m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2023] _id=6ac64cedde269131f9b9e8dc ts=2026-10-07T13:45:16.2850000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3098] _id=6ac79cd4de269131f9c0959a ts=2026-10-08T13:38:27.4280000Z; 23h 39m: 6ab9a88e9a8420a1e6b56ae5.jsonl[666] _id=6ac4fc1dde269131f9b1741e ts=2026-10-06T13:48:12.1120000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1647] _id=6ac648e6de269131f9b9182a ts=2026-10-07T13:28:05.4150000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.017s..0.020s shown 
  - Evidence: 17ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[1651] _id=6ac648f4de269131f9b91b09 ts=2026-10-07T13:28:19.5570000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1652] _id=6ac648f4de269131f9b91b17 ts=2026-10-07T13:28:19.5740000Z; 20ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[1652] _id=6ac648f4de269131f9b91b17 ts=2026-10-07T13:28:19.5740000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1656] _id=6ac648f4de269131f9b91b1b ts=2026-10-07T13:28:19.5940000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 107h 9m 
  - Evidence: 107h 9m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3683] _id=6ac7a144de269131f9c15190 ts=2026-10-08T13:57:23.4550000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3795] _id=6acd841dde269131f9ce860f ts=2026-10-13T01:06:36.8290000Z; 48h 18m: 6ab9a88e9a8420a1e6b56ae5.jsonl[448] _id=6ac4f9d7de269131f9b0fcf3 ts=2026-10-06T13:38:30.6270000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3683] _id=6ac7a144de269131f9c15190 ts=2026-10-08T13:57:23.4550000Z; 47h 42m: 6ab9a88e9a8420a1e6b56ae5.jsonl[4511] _id=6ace33ecde269131f9ceba5d ts=2026-10-13T13:36:43.8970000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7663] _id=6ad0d2ccde269131f9da6040 ts=2026-10-15T13:19:08.2320000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 107h 7m 
  - Evidence: 107h 7m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3684] _id=6ac7a144de269131f9c15198 ts=2026-10-08T13:57:23.4780000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3717] _id=6acd839cde269131f9ce8504 ts=2026-10-13T01:04:27.5110000Z; 48h 17m: 6ab9a88e9a8420a1e6b56ae5.jsonl[453] _id=6ac4f9d7de269131f9b0fcf5 ts=2026-10-06T13:38:30.6490000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3640] _id=6ac7a0f4de269131f9c14916 ts=2026-10-08T13:56:03.8100000Z; 47h 41m: 6ab9a88e9a8420a1e6b56ae5.jsonl[4496] _id=6ace33ecde269131f9ceba67 ts=2026-10-13T13:36:43.9810000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7624] _id=6ad0d28ede269131f9da5c24 ts=2026-10-15T13:18:05.9710000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.034s..0.034s shown 
  - Evidence: 34ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7739] _id=6ad0d346de269131f9da6718 ts=2026-10-15T13:21:10.6270000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7736] _id=6ad0d346de269131f9da6720 ts=2026-10-15T13:21:10.6610000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 107h 7m 
  - Evidence: 107h 7m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3680] _id=6ac7a137de269131f9c15062 ts=2026-10-08T13:57:11.1500000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3718] _id=6acd839fde269131f9ce8511 ts=2026-10-13T01:04:30.5460000Z; 48h 17m: 6ab9a88e9a8420a1e6b56ae5.jsonl[452] _id=6ac4f9d5de269131f9b0fca7 ts=2026-10-06T13:38:28.2680000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3643] _id=6ac7a0fade269131f9c14997 ts=2026-10-08T13:56:09.9390000Z; 47h 41m: 6ab9a88e9a8420a1e6b56ae5.jsonl[4504] _id=6ace33ebde269131f9ceba4f ts=2026-10-13T13:36:42.1250000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7623] _id=6ad0d28cde269131f9da5c11 ts=2026-10-15T13:18:04.5340000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 28 interval(s) ≤ 0.006s..0.022s shown 
  - Evidence: 6ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[9064] _id=6ad22358de269131f9e3620f ts=2026-10-16T13:15:03.2820000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[9062] _id=6ad22358de269131f9e36211 ts=2026-10-16T13:15:03.2880000Z; 21ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7623] _id=6ad0d28cde269131f9da5c11 ts=2026-10-15T13:18:04.5340000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7621] _id=6ad0d28cde269131f9da5c15 ts=2026-10-15T13:18:04.5550000Z; 22ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[7712] _id=6ad0d32dde269131f9da6559 ts=2026-10-15T13:20:45.5400000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7715] _id=6ad0d32dde269131f9da655d ts=2026-10-15T13:20:45.5620000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 107h 7m 
  - Evidence: 107h 7m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3682] _id=6ac7a13ede269131f9c150f2 ts=2026-10-08T13:57:17.5580000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3726] _id=6acd83a9de269131f9ce8526 ts=2026-10-13T01:04:40.5420000Z; 48h 20m: 6ab9a88e9a8420a1e6b56ae5.jsonl[383] _id=6ac4f96fde269131f9b0e7d1 ts=2026-10-06T13:36:46.2510000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3679] _id=6ac7a139de269131f9c15088 ts=2026-10-08T13:57:12.7340000Z; 12h 30m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3729] _id=6acd83cbde269131f9ce8540 ts=2026-10-13T01:05:14.5470000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4459] _id=6ace33a0de269131f9ceb628 ts=2026-10-13T13:35:27.1310000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 17m 
  - Evidence: 23h 17m: 6ab9a88e9a8420a1e6b56ae5.jsonl[8703] _id=6ad0daa0de269131f9db341e ts=2026-10-15T13:52:32.3030000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[8909] _id=6ad22214de269131f9e34efa ts=2026-10-16T13:09:39.1580000Z; 17m 19s: 6ab9a88e9a8420a1e6b56ae5.jsonl[8059] _id=6ad0d690de269131f9dab9e2 ts=2026-10-15T13:35:12.6830000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[8703] _id=6ad0daa0de269131f9db341e ts=2026-10-15T13:52:32.3030000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 107h 35m 
  - Evidence: 107h 35m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2836] _id=6ac79a80de269131f9c035f1 ts=2026-10-08T13:28:31.5180000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3709] _id=6acd8383de269131f9ce84db ts=2026-10-13T01:04:02.1160000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1596] _id=6ac64838de269131f9b8edba ts=2026-10-07T13:25:11.4570000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2836] _id=6ac79a80de269131f9c035f1 ts=2026-10-08T13:28:31.5180000Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae5.jsonl[5866] _id=6acf808ede269131f9d2da39 ts=2026-10-14T13:15:57.3680000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7405] _id=6ad0d123de269131f9da4fb2 ts=2026-10-15T13:12:02.8890000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 107h 35m 
  - Evidence: 107h 35m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2835] _id=6ac79a80de269131f9c035f0 ts=2026-10-08T13:28:31.5180000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3708] _id=6acd8383de269131f9ce84da ts=2026-10-13T01:04:02.1160000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1595] _id=6ac64838de269131f9b8edb9 ts=2026-10-07T13:25:11.4570000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2835] _id=6ac79a80de269131f9c035f0 ts=2026-10-08T13:28:31.5180000Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae5.jsonl[5865] _id=6acf808ede269131f9d2da38 ts=2026-10-14T13:15:57.3680000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[7404] _id=6ad0d123de269131f9da4fb1 ts=2026-10-15T13:12:02.8890000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 131h 14m 
  - Evidence: 131h 14m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2837] _id=6ac79a80de269131f9c035ed ts=2026-10-07T13:59:46.601Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3894] _id=6acd85cdde269131f9ce8841 ts=2026-10-13T01:13:48.3660000Z; 24h 0m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1593] _id=6ac64838de269131f9b8edae ts=2026-10-06T13:59:40.814Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2837] _id=6ac79a80de269131f9c035ed ts=2026-10-07T13:59:46.601Z; 12h 15m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3894] _id=6acd85cdde269131f9ce8841 ts=2026-10-13T01:13:48.3660000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[4368] _id=6ace3248de269131f9ceaabd ts=2026-10-13T13:29:43.5930000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 107h 6m 
  - Evidence: 107h 6m: 6ab9a88e9a8420a1e6b56ae5.jsonl[3689] _id=6ac7a14ede269131f9c1526c ts=2026-10-08T13:57:33.9020000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[3712] _id=6acd8391de269131f9ce84e8 ts=2026-10-13T01:04:15.7000000Z; 23h 31m: 6ab9a88e9a8420a1e6b56ae5.jsonl[2777] _id=6ac64fb0de269131f9ba311d ts=2026-10-07T13:57:03.2250000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[2848] _id=6ac79a9ade269131f9c037bb ts=2026-10-08T13:28:57.6170000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae5.jsonl[1579] _id=6ac4fe84de269131f9b2251b ts=2026-10-06T13:58:27.8910000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[1599] _id=6ac64846de269131f9b8f157 ts=2026-10-07T13:25:25.0220000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[9135] _id=6ad223b9de269131f9e3692a ts=2026-10-16T13:16:40.5790000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[9136] _id=6ad223b9de269131f9e3692b ts=2026-10-16T13:16:40.5790000Z; 2ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[353] _id=6ac4f91cde269131f9b0d851 ts=2026-10-06T13:35:22.7860000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[354] _id=6ac4f91cde269131f9b0d85d ts=2026-10-06T13:35:22.7880000Z; 2ms: 6ab9a88e9a8420a1e6b56ae5.jsonl[8451] _id=6ad0d84ade269131f9daeac7 ts=2026-10-15T13:42:34.5720000Z -> 6ab9a88e9a8420a1e6b56ae5.jsonl[8452] _id=6ad0d84ade269131f9daeac8 ts=2026-10-15T13:42:34.5740000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[335] _id=6ac4f8fade269131f9b0d3e1 ts=2026-10-06T13:34:49.0890000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[373] _id=6ac4f9ecde269131f9b10067 ts=2026-10-06T13:38:51.8770000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[1781] _id=6ac64a75de269131f9b9830c ts=2026-10-07T13:34:44.0450000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 25 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[671] _id=6ac4fc51de269131f9b185d2 ts=2026-10-06T13:49:02.2920000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[669] _id=6ac4fc51de269131f9b185e3 ts=2026-10-06T13:49:02.8060000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[677] _id=6ac4fc51de269131f9b185f7 ts=2026-10-06T13:49:03.3470000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 61 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[733] _id=6ac4fc4ade269131f9b183d4 ts=2026-10-06T13:48:39.6290000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[738] _id=6ac4fc4ade269131f9b183e8 ts=2026-10-06T13:48:39.8080000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[730] _id=6ac4fc4bde269131f9b1842c ts=2026-10-06T13:48:40.4370000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[4496] _id=6ace33ecde269131f9ceba67 ts=2026-10-13T13:36:43.9810000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[7736] _id=6ad0d346de269131f9da6720 ts=2026-10-15T13:21:10.6610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[386] _id=6ac4f975de269131f9b0e976 ts=2026-10-06T13:36:52.7190000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[8059] _id=6ad0d690de269131f9dab9e2 ts=2026-10-15T13:35:12.6830000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[8703] _id=6ad0daa0de269131f9db341e ts=2026-10-15T13:52:32.3030000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[8909] _id=6ad22214de269131f9e34efa ts=2026-10-16T13:09:39.1580000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 79 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[964] _id=6ac4fc8ede269131f9b19856 ts=2026-10-06T13:50:02.4530000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[953] _id=6ac4fc8ede269131f9b19868 ts=2026-10-06T13:50:02.7310000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[1039] _id=6ac4fc9cde269131f9b19dac ts=2026-10-06T13:50:18.6980000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 196 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[725] _id=6ac4fc4ade269131f9b183c0 ts=2026-10-06T13:48:39.5360000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[729] _id=6ac4fc4bde269131f9b18426 ts=2026-10-06T13:48:40.4370000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[702] _id=6ac4fc4cde269131f9b184a6 ts=2026-10-06T13:48:40.7630000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[3726] _id=6acd83a9de269131f9ce8526 ts=2026-10-13T01:04:40.5420000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[3730] _id=6acd83bdde269131f9ce8532 ts=2026-10-13T01:05:00.7390000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[3729] _id=6acd83cbde269131f9ce8540 ts=2026-10-13T01:05:14.5470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 406 start, 400 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameCameraCentered' (totals: 437 open, 450 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 34 unmatched 'BecameVisible' (totals: 608 open, 635 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'argumentationToolOpen' (totals: 13 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 45 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 184 of 9348 adjacent _id pairs reverse in client time; worst 95.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae5.jsonl[715] _id=6ac4fc48de269131f9b18290 ts=2026-10-06T13:48:54.9070000Z`; `6ab9a88e9a8420a1e6b56ae5.jsonl[716] _id=6ac4fc48de269131f9b182ec ts=2026-10-06T13:47:19.3060000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.92s, min -84525.52s, max -0.19s over 9349 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae5\coverage.yaml

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

### `InputEvent` — 2368 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (719); Unit 3 Dev (313); Unit 3 Dungeon Dev (296); Unit 4 Dev - Dungeon (264); Unit 4 Dev - Anderson Base (202); Unit 5 Dev - Dungeon (198); Unit 4 Dev (133); Unit 1 Dev (130); Unit 5 Dev (113)
- **Intervals:** median 1.55s (p5 0.16s / p95 24.57s, n=2367)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2368/2368 records)
    "pressed"  x2368
data.actionType  (string, 2368/2368 records)
    "Move"  x1735
    "Interact"  x428
    "Ascend"  x96
    "Hoverboard"  x44
    "Jump"  x29
    "Sprint"  x27
    "Map"  x7
    "SkipCinematic"  x1
    "ToggleDebug"  x1
data.key  (string, 2368/2368 records, 7 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2368/2368 records)
    "Player"  x1647
    "Drone"  x721
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2130 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1244); Unit 4 Dev (436); Unit 3 Dungeon Dev (232); Unit 5 Dev - Dungeon (218)
- **Intervals:** median 0.08s (p5 0.00s / p95 2.75s, n=2129)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2130/2130 records)
    "BecameInvisible"  x635
    "BecameVisible"  x608
    "BecameCameraUncentered"  x450
    "BecameCameraCentered"  x437
data.pieceId  (string, 2130/2130 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2130/2130 records)
    1457 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2127 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (591); Unit 3 Dev (312); Unit 5 Dev (265); Unit 4 Dev (249); Unit 1 Dev (203); Unit 3 Dungeon Dev (188); Unit 4 Dev - Anderson Base (137); Unit 4 Dev - Dungeon (110); Unit 5 Dev - Dungeon (72)
- **eventKey:** present on 1321 of 2127 records
- **Intervals:** median 3.53s (p5 0.00s / p95 26.29s, n=2126)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1321; [conversationId, dialogueEventType] x806
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2127/2127 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2127/2127 records)
    "DialogueNodeEvent"  x1321
    "DialogueStartEvent"  x406
    "DialogueFinishEvent"  x400
data.nodeId  (number, 1321/2127 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1710 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (515); Unit 3 Dev (220); Unit 3 Dungeon Dev (169); Unit 4 Dev (168); Unit 1 Dev (167); Unit 4 Dev - Dungeon (142); Unit 5 Dev (140); Unit 5 Dev - Dungeon (103); Unit 4 Dev - Anderson Base (86)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=1698)
- **Fields under `data`:**

```text
data.position  (object, 1710/1710 records)
data.position.x  (number, 1710/1710 records)
    numeric range -681.999 .. 1555.17 (616 unique)
data.position.y  (number, 1710/1710 records)
    numeric range -114.326 .. 222.005 (447 unique)
data.position.z  (number, 1710/1710 records)
    numeric range -1148.5 .. 1800.6 (616 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 310 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (82); Unit 5 Dev (76); Unit 4 Dev - Anderson Base (69); Unit 3 Dev (51); Unit 1 Dev (32)
- **Intervals:** median 0.83s (p5 0.03s / p95 10.20s, n=309)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 310/310 records)
    "argumentationNodeHoverEnd"  x134
    "argumentationNodeHoverStart"  x133
    "argumentationNodeAdd"  x35
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 310/310 records)
    "Unit 2 – Watershed"  x82
    "Unit 5"  x76
    "Unit 4 - Flooding"  x69
    "Unit 3 - Pollution Upstream"  x51
    "Unit 1 - Freshwater"  x17
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 310/310 records)
    "I"  x45
    "A"  x42
    "D"  x41
    "B"  x38
    "1"  x34
    "II"  x27
    "C"  x23
    "3"  x18
    "2"  x17
    "4"  x16
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 256 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (80); Unit 3 Dungeon Dev (48); Unit 2 Prod (Refactor) (33); Unit 4 Dev (22); Unit 5 Dev - Dungeon (19); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (13); Unit 5 Dev (13); Unit 1 Dev (10)
- **Intervals:** median 17.14s (p5 2.17s / p95 406.83s, n=255)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 256/256 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 256/256 records)
    105 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 126 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (64); Unit 3 Dev (52); Unit 4 Dev (10)
- **Intervals:** median 0.45s (p5 0.01s / p95 11.12s, n=125)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x118; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/126 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/126 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 118/126 records)
    "RightDrag"  x62
    "LeftDrag"  x56
data.currentSoilType  (string, 118/126 records)
    "CLAYSAND"  x27
    "SAND"  x27
    "CLAY"  x21
    "SANDGRAVEL"  x17
    "CLAYROCK"  x15
    "GRAVEL"  x7
    "BEDROCK"  x4
data.isCorrectSelection  (string, 118/126 records)
    "false"  x95
    "true"  x23
data.waterLevelStatus  (string, 118/126 records)
    "Proper"  x61
    "TooHigh"  x31
    "TooLow"  x26
data.waterRetentionChange  (string, 118/126 records)
    "Decrease"  x53
    "Increase"  x42
    "NoChange"  x23
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 79 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (12); Unit 3 Dev (10); Unit 5 Dev (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 79 of 79 records
- **Intervals:** median 202.88s (p5 0.01s / p95 83464.60s, n=78)
- **`data` key-set variants:** [questEventType, questID, questName] x45; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 79/79 records)
    "questActiveEvent"  x45
    "questFinishEvent"  x34
data.questID  (string, 79/79 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 79/79 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/79 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 57 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (29); Unit 2 Prod (Refactor) (28)
- **Intervals:** median 9.12s (p5 1.62s / p95 49974.13s, n=56)
- **`data` key-set variants:** [actionType, featureUsed] x38; [actionType, featureUsed, location] x19
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 57/57 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
    "WaypointMoveEvent"  x13
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x1
data.featureUsed  (string, 57/57 records)
    "Map"  x38
    "Waypoint"  x19
data.location  (object, 19/57 records)
data.location.x  (number, 19/57 records)
    numeric range -326.441 .. 3.94725 (14 unique)
data.location.y  (number, 19/57 records)
    numeric range -257.711 .. 124.696 (18 unique)
data.location.z  (number, 19/57 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (12); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 4 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 686.20s (p5 9.41s / p95 86124.07s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 24 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (24)
- **Intervals:** median 13.35s (p5 3.70s / p95 76.72s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "On"  x17
    "Off"  x7
data.floor  (string, 24/24 records)
    "4"  x11
    "3"  x7
    "2"  x4
    "1"  x2
data.machineNumber  (string, 24/24 records)
    "One"  x23
    "Two"  x1
data.machineType  (string, 24/24 records)
    "Condenser"  x15
    "Evaporator"  x6
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 24/24 records)
    "3"  x10
    "2"  x7
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 5 Dev (5); Unit 2 Prod (Refactor) (3); Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 28.99s (p5 6.84s / p95 216296.94s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x6
    "Unit 5"  x5
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (4); Unit 5 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 97.58s (p5 0.05s / p95 216207.34s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 18/18 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x4
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 18/18 records)
    "Unit 2 – Watershed"  x4
    "Unit 5"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowFocusEvent` — 16 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 37730.56s (p5 183.64s / p95 176819.22s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (7); Unit 2 Prod (Refactor) (5); Unit 1 Dev (2)
- **Intervals:** median 4.82s (p5 1.06s / p95 258673.08s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x7
    "Unit 2 – Watershed"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - Waterfall Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 39199.80s (p5 379.95s / p95 206892.28s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 14 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (14)
- **Intervals:** median 23.23s (p5 1.31s / p95 168.78s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "ChangeCanister"  x14
data.canisterType  (string, 14/14 records)
    "Gravel"  x5
    "Clay"  x4
    "Sand"  x3
    "Bedrock"  x2
data.floor  (string, 14/14 records)
    "4"  x9
    "5"  x4
    "3"  x1
data.machine  (string, 14/14 records)
    "1"  x12
    "2"  x2
data.row  (string, 14/14 records)
    "TopRow"  x13
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `SolarStillDesignEvent` — 12 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (12)
- **Intervals:** median 1.62s (p5 1.07s / p95 4.24s, n=11)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x11; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "optionSelected"  x11
    "DesignSubmitted"  x1
data.designSelections  (object, 1/12 records)
data.designSelections.glassRoofTemperature  (string, 1/12 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/12 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/12 records)
    "Tilted Out"  x1
data.featureUsed  (string, 12/12 records)
    "RoofStyle"  x7
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 11/12 records, 2 empty-string)
    "Tilted Out"  x3
    ""  x2
    "Uncovered"  x2
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 1.96s (p5 1.29s / p95 32.56s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x3
data.boxId  (string, 8/8 records)
    "0"  x4
    "1"  x2
    "2"  x2
data.soilType  (string, 8/8 records)
    "Clay"  x3
    "Sand"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 6 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); MainMenu (1); Unit 1 Dev (1)
- **Intervals:** median 44155.23s (p5 3923.84s / p95 395234.57s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    false  x6
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 108685.36s (p5 86934.66s / p95 494511.05s, n=4)
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

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 1.93s (p5 1.92s / p95 34425.16s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1039.62s (p5 172.55s / p95 75548.13s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (64 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (13x); "WaypointResetEvent" (1x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*