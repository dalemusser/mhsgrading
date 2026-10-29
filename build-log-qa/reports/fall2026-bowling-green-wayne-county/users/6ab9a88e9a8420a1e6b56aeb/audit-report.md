# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56aeb

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56aeb
- **Game version string(s) in log:** 2.8.4, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56aeb.jsonl
- **Records:** 11442 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56aeb
- **Time span:** 2026-10-06T13:39:37.666000+00:00 .. 2026-10-16T13:49:26.715000+00:00 (240h 9m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56aeb\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 11442 records, 11 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 97 INFO, 0 NOT_TESTED, 102 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PlayerPositionEvent | 3570 | 31.2 | 1 | 9 | 0 | 2026-10-06T13:48:22.420000+00:00 | 2026-10-16T13:49:25.298000+00:00 | 240h 1m |
| DialogueEvent | 2273 | 19.87 | 1 | 9 | 1442 | 2026-10-06T13:48:42.387000+00:00 | 2026-10-16T13:49:22.649000+00:00 | 240h 0m |
| InputEvent | 2269 | 19.83 | 1 | 9 | 0 | 2026-10-06T13:48:25.915000+00:00 | 2026-10-16T13:49:26.715000+00:00 | 240h 1m |
| PuzzlePieceVisibleEvent | 2213 | 19.34 | 1 | 4 | 0 | 2026-10-07T13:55:28.125000+00:00 | 2026-10-16T13:18:01.583000+00:00 | 215h 22m |
| argumentationNodeEvent | 376 | 3.29 | 1 | 5 | 0 | 2026-10-07T13:45:20.685000+00:00 | 2026-10-16T13:37:35.705000+00:00 | 215h 52m |
| ObjectInterEvent | 294 | 2.57 | 1 | 9 | 0 | 2026-10-06T13:54:48.676000+00:00 | 2026-10-16T13:49:26.715000+00:00 | 239h 54m |
| questEvent | 84 | 0.73 | 1 | 9 | 84 | 2026-10-06T13:48:42.363000+00:00 | 2026-10-16T13:45:47.025000+00:00 | 239h 57m |
| TopographicMapEvent | 74 | 0.65 | 1 | 2 | 0 | 2026-10-07T13:56:16.791000+00:00 | 2026-10-15T13:40:51.670000+00:00 | 191h 44m |
| Soil Key Puzzle | 64 | 0.56 | 1 | 3 | 0 | 2026-10-13T13:31:45.257000+00:00 | 2026-10-15T13:51:55.548000+00:00 | 48h 20m |
| DEBUGMenu | 39 | 0.34 | 1 | 9 | 0 | 2026-10-06T13:48:22.400000+00:00 | 2026-10-16T13:10:48.201000+00:00 | 239h 22m |
| gameWindowFocusEvent | 29 | 0.25 | 1 | 5 | 0 | 2026-10-06T13:39:37.666000+00:00 | 2026-10-16T13:10:41.648000+00:00 | 239h 31m |
| argumentationAnswerEvent | 28 | 0.24 | 1 | 5 | 0 | 2026-10-07T13:45:43.834000+00:00 | 2026-10-16T13:37:37.228000+00:00 | 215h 51m |
| WaterChamberEvent | 26 | 0.23 | 1 | 1 | 0 | 2026-10-16T13:16:22.401000+00:00 | 2026-10-16T13:27:58.011000+00:00 | 11m 35s |
| gameStartEvent | 19 | 0.17 | 1 | 1 | 0 | 2026-10-06T13:39:37.668000+00:00 | 2026-10-16T13:10:41.648000+00:00 | 239h 31m |
| gameWindowUnfocusEvent | 19 | 0.17 | 1 | 8 | 0 | 2026-10-06T13:39:48.295000+00:00 | 2026-10-16T04:43:32.156000+00:00 | 231h 3m |
| argumentationEvent | 14 | 0.12 | 1 | 5 | 0 | 2026-10-07T13:45:08.882000+00:00 | 2026-10-16T13:37:37.263000+00:00 | 215h 52m |
| DaniEvent | 12 | 0.1 | 1 | 2 | 0 | 2026-10-13T13:20:47.879000+00:00 | 2026-10-14T13:50:30.232000+00:00 | 24h 29m |
| TerasGardenBox | 12 | 0.1 | 1 | 1 | 0 | 2026-10-16T04:30:40.974000+00:00 | 2026-10-16T05:21:43.765000+00:00 | 51m 2s |
| soilMachine | 7 | 0.06 | 1 | 1 | 0 | 2026-10-16T03:21:30.165000+00:00 | 2026-10-16T03:35:39.993000+00:00 | 14m 9s |
| SolarStillDesignEvent | 6 | 0.05 | 1 | 1 | 0 | 2026-10-16T13:43:06.278000+00:00 | 2026-10-16T13:43:31.392000+00:00 | 25.1s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-07T13:50:23.404000+00:00 | 2026-10-16T13:49:26.699000+00:00 | 215h 59m |
| chatEvent | 4 | 0.03 | 1 | 3 | 0 | 2026-10-14T13:50:17.567000+00:00 | 2026-10-16T13:29:01.986000+00:00 | 47h 38m |
| argumentationToolEvent | 3 | 0.03 | 1 | 2 | 0 | 2026-10-07T13:45:04.426000+00:00 | 2026-10-14T13:28:48.181000+00:00 | 167h 43m |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 382.158s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 71898.012s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 2.087s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 13.295s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.052s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.278s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 22.538s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.102s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.179s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 301911.878s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1014.396s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1094.179s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 39 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
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
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.6x vs baseline. 
  - Observed: 28 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 2,II; A,1,; A,2,II; A,3,II; A,4,II; A,D,C,2,II; B,2,II; B,5,I; C,2,II; C,3,II; C,4,II; C,D,3,II; D,2,II; D,A,2,II; D,B,2,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [11-26, 11-25, 11-26, 11-27, 11-27] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[1] _id=6ac4fa1ade269131f9b10a36 ts=2026-10-06T13:39:37.6680000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[4] _id=6ac4fbd8de269131f9b16430 ts=2026-10-06T13:47:03.4130000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[325] _id=6ac64832de269131f9b8ec91 ts=2026-10-07T13:25:04.8740000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 29 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 29} 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[0] _id=6ac4fa1ade269131f9b10a2e ts=2026-10-06T13:39:37.6660000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[3] _id=6ac4fbd8de269131f9b1642e ts=2026-10-06T13:47:03.4110000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[324] _id=6ac64832de269131f9b8ec90 ts=2026-10-07T13:25:04.8740000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[2] _id=6ac4fa25de269131f9b10ca9 ts=2026-10-06T13:39:48.2950000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[322] _id=6ac64832de269131f9b8ec8a ts=2026-10-06T13:59:42.173Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[1472] _id=6ac79ac7de269131f9c03cca ts=2026-10-07T13:59:46.028Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PlayerPositionEvent | 3558 | 9.801 | 10.001 | 235.011 | 10.075 | 429408.38 | 0.26 | 0 | 8 |
| DialogueEvent | 2272 | 0.0 | 4.069 | 380.299 | 33.167 | 429574.257 | 0.16 | 644 | 10 |
| InputEvent | 2268 | 0.0 | 2.087 | 380.979 | 39.972 | 429450.868 | 0.16 | 28 | 12 |
| PuzzlePieceVisibleEvent | 2212 | 0.0 | 0.052 | 350.521 | 2.294 | 431978.798 | 0.17 | 1101 | 6 |
| argumentationNodeEvent | 375 | 0.019 | 0.497 | 2072.36 | 10.093 | 603639.454 | 0.03 | 30 | 4 |
| ObjectInterEvent | 293 | 0.0 | 13.295 | 2947.707 | 550.701 | 431745.366 | 0.02 | 4 | 14 |
| questEvent | 83 | 0.0 | 220.807 | 10407.526 | 54800.759 | 430187.855 | 0.01 | 15 | 16 |
| TopographicMapEvent | 73 | 0.027 | 10.102 | 9455.82 | 31316.669 | 429727.996 | 0.01 | 2 | 9 |
| Soil Key Puzzle | 63 | 0.159 | 2.278 | 2762.068 | 20.813 | 171943.435 | 0.02 | 0 | 2 |
| DEBUGMenu | 38 | 6.713 | 382.158 | 22677.521 | 85119.297 | 430355.905 | 0.0 | 0 | 17 |
| gameWindowFocusEvent | 28 | 11.889 | 1014.396 | 30795.142 | 85303.743 | 430365.946 | 0.0 | 0 | 17 |
| argumentationAnswerEvent | 27 | 3.445 | 15.179 | 28781.978 | 106438.633 | 603683.878 | 0.0 | 0 | 4 |
| WaterChamberEvent | 25 | 0.007 | 16.764 | 27.824 | 77.308 | 94.313 | 2.16 | 1 | 0 |
| gameStartEvent | 18 | 42.737 | 3934.49 | 47903.554 | 137164.81 | 430365.945 | 0.0 | 0 | 14 |
| gameWindowUnfocusEvent | 18 | 23.295 | 1094.179 | 46212.437 | 137887.526 | 429628.331 | 0.0 | 0 | 11 |
| argumentationEvent | 13 | 0.035 | 86.758 | 59780.645 | 324107.035 | 603643.926 | 0.0 | 2 | 4 |
| DaniEvent | 11 | 0.876 | 4.013 | 8016.578 | 42112.717 | 55565.938 | 0.01 | 0 | 4 |
| TerasGardenBox | 11 | 1.512 | 22.538 | 278.436 | 1459.157 | 2455.79 | 0.22 | 0 | 1 |
| soilMachine | 6 | 7.517 | 94.266 | 141.638 | 352.857 | 417.855 | 0.42 | 0 | 0 |
| SolarStillDesignEvent | 5 | 0.236 | 3.438 | 5.023 | 9.917 | 10.087 | 11.95 | 0 | 0 |
| EndOfUnit | 4 | 29981.903 | 71898.012 | 194385.824 | 526278.906 | 603765.367 | 0.0 | 0 | 4 |
| chatEvent | 3 | 4.587 | 1094.08 | 57174.806 | 153492.585 | 170425.752 | 0.0 | 0 | 2 |
| argumentationToolEvent | 2 | 4.395 | 301911.878 | 301911.878 | 573628.612 | 603819.36 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[5562] _id=6acf7fd6de269131f9d2d258 ts=2026-10-14T13:12:53.3320000Z == 6ab9a88e9a8420a1e6b56aeb.jsonl[5563] _id=6acf7fd6de269131f9d2d259 ts=2026-10-14T13:12:53.3320000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[9954] _id=6ad1aa19de269131f9e33716 ts=2026-10-16T04:37:43.7040000Z == 6ab9a88e9a8420a1e6b56aeb.jsonl[9955] _id=6ad1aa19de269131f9e33717 ts=2026-10-16T04:37:43.7040000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 35 group(s), 63 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[2710] _id=6ace3389de269131f9ceb499 ts=2026-10-13T13:35:03.5380000Z == 6ab9a88e9a8420a1e6b56aeb.jsonl[2711] _id=6ace3389de269131f9ceb49d ts=2026-10-13T13:35:03.5380000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[2718] _id=6ace3389de269131f9ceb4a4 ts=2026-10-13T13:35:03.8030000Z == 6ab9a88e9a8420a1e6b56aeb.jsonl[2719] _id=6ace3389de269131f9ceb4a6 ts=2026-10-13T13:35:03.8030000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[2724] _id=6ace338bde269131f9ceb4d3 ts=2026-10-13T13:35:04.4170000Z == 6ab9a88e9a8420a1e6b56aeb.jsonl[2725] _id=6ace338bde269131f9ceb4d4 ts=2026-10-13T13:35:04.4170000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 34 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `467ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[163] _id=6ac4fdafde269131f9b1e473 ts=2026-10-06T13:54:54.4600000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[164] _id=6ac4fdafde269131f9b1e493 ts=2026-10-06T13:54:54.9270000Z`; `138ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[164] _id=6ac4fdafde269131f9b1e493 ts=2026-10-06T13:54:54.9270000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[169] _id=6ac4fdb0de269131f9b1e4a8 ts=2026-10-06T13:54:55.0650000Z`; `264ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[169] _id=6ac4fdb0de269131f9b1e4a8 ts=2026-10-06T13:54:55.0650000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[170] _id=6ac4fdb0de269131f9b1e4ba ts=2026-10-06T13:54:55.3290000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `38ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[6862] _id=6acf8a61de269131f9d3b121 ts=2026-10-14T13:57:52.4880000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[6865] _id=6acf8a61de269131f9d3b124 ts=2026-10-14T13:57:52.5260000Z`; `35ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[9746] _id=6ad1a6a6de269131f9e335a2 ts=2026-10-16T04:23:02.2420000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[9749] _id=6ad1a6a6de269131f9e335a5 ts=2026-10-16T04:23:02.2770000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 26 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `899ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[703] _id=6ac64d66de269131f9b9f1cc ts=2026-10-07T13:47:16.9840000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[704] _id=6ac64d67de269131f9b9f1e2 ts=2026-10-07T13:47:17.8830000Z`; `821ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[714] _id=6ac64d6fde269131f9b9f2b5 ts=2026-10-07T13:47:26.6900000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[711] _id=6ac64d70de269131f9b9f2c3 ts=2026-10-07T13:47:27.5110000Z`; `427ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[6766] _id=6acf89ecde269131f9d3a02a ts=2026-10-14T13:55:56.2350000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[6768] _id=6acf89edde269131f9d3a03a ts=2026-10-14T13:55:56.6620000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11218] _id=6ad228ecde269131f9e3cedd ts=2026-10-16T13:38:51.8630000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[11219] _id=6ad228ecde269131f9e3cede ts=2026-10-16T13:38:51.8640000Z`; `5ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11350] _id=6ad22a4dde269131f9e3ea9c ts=2026-10-16T13:44:45.0610000Z ~ 6ab9a88e9a8420a1e6b56aeb.jsonl[11351] _id=6ad22a4dde269131f9e3ea9e ts=2026-10-16T13:44:45.0660000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2092] _id=6ac79de2de269131f9c0c48b ts=2026-10-08T13:42:57.2330000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2403] _id=6ace2ef5de269131f9ce8d8a ts=2026-10-13T13:15:33.1380000Z; 23h 43m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6087] _id=6acf84abde269131f9d32aea ts=2026-10-14T13:33:31.0010000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6921] _id=6ad0d252de269131f9da5998 ts=2026-10-15T13:17:05.6620000Z; 23h 37m: 6ab9a88e9a8420a1e6b56aeb.jsonl[810] _id=6ac64e7cde269131f9ba0bd7 ts=2026-10-07T13:51:55.1530000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1469] _id=6ac79ac7de269131f9c03cd4 ts=2026-10-08T13:29:42.3270000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 15h 26m 
  - Evidence: 15h 26m: 6ab9a88e9a8420a1e6b56aeb.jsonl[3700] _id=6ace38c6de269131f9cefa97 ts=2026-10-13T13:57:26.3250000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[3947] _id=6acf11d4de269131f9d2ba5e ts=2026-10-14T05:23:32.2630000Z; 7h 57m: 6ab9a88e9a8420a1e6b56aeb.jsonl[3940] _id=6acf11d5de269131f9d2ba60 ts=2026-10-14T05:23:33.3540000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5762] _id=6acf81c9de269131f9d2eced ts=2026-10-14T13:21:12.8510000Z; 36m 33s: 6ab9a88e9a8420a1e6b56aeb.jsonl[2545] _id=6ace3034de269131f9ce974d ts=2026-10-13T13:20:51.8920000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[3702] _id=6ace38c5de269131f9cefa8b ts=2026-10-13T13:57:25.4490000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2346] _id=6ac7a100de269131f9c14a45 ts=2026-10-08T13:56:15.9370000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2400] _id=6ace2f08de269131f9ce8dea ts=2026-10-13T13:15:50.1940000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1434] _id=6ac65041de269131f9ba3b65 ts=2026-10-07T13:59:28.0040000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1487] _id=6ac79af6de269131f9c0428f ts=2026-10-08T13:30:29.6880000Z; 23h 26m: 6ab9a88e9a8420a1e6b56aeb.jsonl[121] _id=6ac4fecade269131f9b235d8 ts=2026-10-06T13:59:37.8980000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[339] _id=6ac64860de269131f9b8f67b ts=2026-10-07T13:25:51.2810000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 644 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11135] _id=6ad22881de269131f9e3c677 ts=2026-10-16T13:37:04.9330000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11136] _id=6ad22881de269131f9e3c678 ts=2026-10-16T13:37:04.9330000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11154] _id=6ad22890de269131f9e3c78f ts=2026-10-16T13:37:20.3500000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11155] _id=6ad22890de269131f9e3c790 ts=2026-10-16T13:37:20.3500000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[2108] _id=6ac79dc4de269131f9c0c03b ts=2026-10-08T13:42:27.9390000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2109] _id=6ac79dd7de269131f9c0c320 ts=2026-10-08T13:42:27.939Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 42m 
  - Evidence: 167h 42m: 6ab9a88e9a8420a1e6b56aeb.jsonl[805] _id=6ac64e20de269131f9ba0154 ts=2026-10-07T13:50:23.4040000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6083] _id=6acf8495de269131f9d3297a ts=2026-10-14T13:33:08.7710000Z; 24h 13m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6083] _id=6acf8495de269131f9d3297a ts=2026-10-14T13:33:08.7710000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[7702] _id=6ad0d92ade269131f9db05ee ts=2026-10-15T13:46:17.7330000Z; 15h 43m: 6ab9a88e9a8420a1e6b56aeb.jsonl[7702] _id=6ad0d92ade269131f9db05ee ts=2026-10-15T13:46:17.7330000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[10259] _id=6ad1b649de269131f9e33997 ts=2026-10-16T05:29:44.7960000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2394] _id=6ac7a186de269131f9c15701 ts=2026-10-08T13:58:29.7340000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2414] _id=6ace2f11de269131f9ce8e42 ts=2026-10-13T13:16:00.6020000Z; 23h 30m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1440] _id=6ac65037de269131f9ba3af7 ts=2026-10-07T13:59:18.3690000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1477] _id=6ac79adbde269131f9c03eda ts=2026-10-08T13:30:01.3240000Z; 23h 25m: 6ab9a88e9a8420a1e6b56aeb.jsonl[316] _id=6ac4fec1de269131f9b23380 ts=2026-10-06T13:59:28.5840000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[326] _id=6ac64844de269131f9b8f0a8 ts=2026-10-07T13:25:23.3210000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 28 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[3704] _id=6ace38c6de269131f9cefa9b ts=2026-10-13T13:57:26.3320000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[3705] _id=6ace38c6de269131f9cefa9c ts=2026-10-13T13:57:26.3320000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[5562] _id=6acf7fd6de269131f9d2d258 ts=2026-10-14T13:12:53.3320000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5563] _id=6acf7fd6de269131f9d2d259 ts=2026-10-14T13:12:53.3320000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[5563] _id=6acf7fd6de269131f9d2d259 ts=2026-10-14T13:12:53.3320000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5564] _id=6acf7fd6de269131f9d2d25a ts=2026-10-14T13:12:53.3320000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1990] _id=6ac79c40de269131f9c07b03 ts=2026-10-08T13:35:59.9000000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2639] _id=6ace32c1de269131f9ceae82 ts=2026-10-13T13:31:45.2660000Z; 23h 33m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6321] _id=6acf87afde269131f9d35b5f ts=2026-10-14T13:46:22.5610000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6976] _id=6ad0d309de269131f9da63ae ts=2026-10-15T13:20:08.5020000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1423] _id=6ac6503ade269131f9ba3b2e ts=2026-10-07T13:59:21.7130000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1504] _id=6ac79b1dde269131f9c04742 ts=2026-10-08T13:31:08.7130000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[9282] _id=6ad1a29ade269131f9e329f0 ts=2026-10-16T04:05:45.4740000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[9283] _id=6ad1a29ade269131f9e329f1 ts=2026-10-16T04:05:45.4740000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[9348] _id=6ad1a33dde269131f9e32e45 ts=2026-10-16T04:08:28.4650000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[9349] _id=6ad1a33dde269131f9e32e46 ts=2026-10-16T04:08:28.4650000Z; 5ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[352] _id=6ac6488bde269131f9b90048 ts=2026-10-07T13:26:34.0220000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[353] _id=6ac6488bde269131f9b90065 ts=2026-10-07T13:26:34.0270000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2397] _id=6ac7a1a4de269131f9c15910 ts=2026-10-08T13:58:59.2720000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2399] _id=6ace2f08de269131f9ce8de9 ts=2026-10-13T13:15:47.6520000Z; 23h 30m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1467] _id=6ac6504bde269131f9ba3bef ts=2026-10-07T13:59:38.4540000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1476] _id=6ac79adbde269131f9c03ed9 ts=2026-10-08T13:29:58.4740000Z; 23h 25m: 6ab9a88e9a8420a1e6b56aeb.jsonl[227] _id=6ac4fecade269131f9b235bd ts=2026-10-06T13:59:37.4600000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[319] _id=6ac6483dde269131f9b8eecf ts=2026-10-07T13:25:14.3600000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1976] _id=6ac79c1ede269131f9c0743b ts=2026-10-08T13:35:24.7190000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2717] _id=6ace3388de269131f9ceb495 ts=2026-10-13T13:35:03.5170000Z; 47h 39m: 6ab9a88e9a8420a1e6b56aeb.jsonl[3434] _id=6ace354fde269131f9ceceff ts=2026-10-13T13:42:37.5400000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[7022] _id=6ad0d381de269131f9da6cc5 ts=2026-10-15T13:22:07.2750000Z; 23h 32m: 6ab9a88e9a8420a1e6b56aeb.jsonl[1462] _id=6ac65048de269131f9ba3bbb ts=2026-10-07T13:59:33.9510000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1558] _id=6ac79b92de269131f9c05b45 ts=2026-10-08T13:31:41.3520000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1101 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[1000] _id=6ac64fc0de269131f9ba328e ts=2026-10-07T13:55:49.8320000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1001] _id=6ac64fc0de269131f9ba328f ts=2026-10-07T13:55:49.8320000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[1001] _id=6ac64fc0de269131f9ba328f ts=2026-10-07T13:55:49.8320000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[995] _id=6ac64fc0de269131f9ba3293 ts=2026-10-07T13:55:49.8320000Z; 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[1003] _id=6ac64fc1de269131f9ba32a6 ts=2026-10-07T13:55:51.0050000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1004] _id=6ac64fc1de269131f9ba32a7 ts=2026-10-07T13:55:51.0050000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 45m 
  - Evidence: 47h 45m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2693] _id=6ace3361de269131f9ceb341 ts=2026-10-13T13:34:25.0620000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6978] _id=6ad0d309de269131f9da63a7 ts=2026-10-15T13:20:08.4970000Z; 30m 6s: 6ab9a88e9a8420a1e6b56aeb.jsonl[7002] _id=6ad0d357de269131f9da68b2 ts=2026-10-15T13:21:26.9030000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[7766] _id=6ad0da66de269131f9db2ce3 ts=2026-10-15T13:51:33.5520000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 40m 55s 
  - Evidence: 40m 55s: 6ab9a88e9a8420a1e6b56aeb.jsonl[10027] _id=6ad1aaa4de269131f9e3379e ts=2026-10-16T04:40:03.2290000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[10097] _id=6ad1b43bde269131f9e33833 ts=2026-10-16T05:20:59.0190000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2349] _id=6ac7a102de269131f9c14a6b ts=2026-10-08T13:56:17.7380000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2476] _id=6ace2fa2de269131f9ce91cf ts=2026-10-13T13:18:25.7340000Z; 23h 46m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6637] _id=6acf88eede269131f9d3813b ts=2026-10-14T13:51:41.6300000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[7542] _id=6ad0d73ade269131f9dac670 ts=2026-10-15T13:38:01.2670000Z; 23h 35m: 6ab9a88e9a8420a1e6b56aeb.jsonl[911] _id=6ac64f95de269131f9ba2f62 ts=2026-10-07T13:56:36.2980000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1525] _id=6ac79b52de269131f9c04cdc ts=2026-10-08T13:32:01.2390000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.040s shown 
  - Evidence: 27ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[2182] _id=6ac79eb5de269131f9c0e799 ts=2026-10-08T13:46:28.5570000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2187] _id=6ac79eb5de269131f9c0e79d ts=2026-10-08T13:46:28.5840000Z; 40ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[2183] _id=6ac79eb5de269131f9c0e791 ts=2026-10-08T13:46:28.5170000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2182] _id=6ac79eb5de269131f9c0e799 ts=2026-10-08T13:46:28.5570000Z
- **INFO / Info** `WaterChamberEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[10757] _id=6ad224d5de269131f9e38270 ts=2026-10-16T13:21:25.0200000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[10759] _id=6ad224d5de269131f9e38280 ts=2026-10-16T13:21:25.0270000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 41m 
  - Evidence: 167h 41m: 6ab9a88e9a8420a1e6b56aeb.jsonl[719] _id=6ac64d74de269131f9b9f317 ts=2026-10-07T13:47:31.5390000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5992] _id=6acf8397de269131f9d316c5 ts=2026-10-14T13:28:55.4170000Z; 38h 16m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6861] _id=6acf8a60de269131f9d3b11b ts=2026-10-14T13:57:52.4640000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[9461] _id=6ad1a4b1de269131f9e33205 ts=2026-10-16T04:14:40.7950000Z; 9h 14m: 6ab9a88e9a8420a1e6b56aeb.jsonl[9758] _id=6ad1a6a6de269131f9e335a0 ts=2026-10-16T04:23:02.2260000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11131] _id=6ad22881de269131f9e3c66e ts=2026-10-16T13:37:04.8970000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 40m 
  - Evidence: 167h 40m: 6ab9a88e9a8420a1e6b56aeb.jsonl[720] _id=6ac64d74de269131f9b9f31f ts=2026-10-07T13:47:31.5590000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5970] _id=6acf836fde269131f9d31318 ts=2026-10-14T13:28:15.4850000Z; 38h 15m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6865] _id=6acf8a61de269131f9d3b124 ts=2026-10-14T13:57:52.5260000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[9420] _id=6ad1a476de269131f9e33175 ts=2026-10-16T04:13:41.6330000Z; 9h 13m: 6ab9a88e9a8420a1e6b56aeb.jsonl[9749] _id=6ad1a6a6de269131f9e335a5 ts=2026-10-16T04:23:02.2770000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11084] _id=6ad2284ade269131f9e3c1b9 ts=2026-10-16T13:36:10.5050000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.035s..0.038s shown 
  - Evidence: 35ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[9746] _id=6ad1a6a6de269131f9e335a2 ts=2026-10-16T04:23:02.2420000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[9749] _id=6ad1a6a6de269131f9e335a5 ts=2026-10-16T04:23:02.2770000Z; 38ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[6862] _id=6acf8a61de269131f9d3b121 ts=2026-10-14T13:57:52.4880000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6865] _id=6acf8a61de269131f9d3b124 ts=2026-10-14T13:57:52.5260000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 40m 
  - Evidence: 167h 40m: 6ab9a88e9a8420a1e6b56aeb.jsonl[716] _id=6ac64d72de269131f9b9f2e1 ts=2026-10-07T13:47:28.5810000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5964] _id=6acf8368de269131f9d312a4 ts=2026-10-14T13:28:08.0350000Z; 38h 15m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6854] _id=6acf8a5bde269131f9d3b032 ts=2026-10-14T13:57:47.0670000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[9424] _id=6ad1a478de269131f9e3317e ts=2026-10-16T04:13:43.9840000Z; 9h 13m: 6ab9a88e9a8420a1e6b56aeb.jsonl[9745] _id=6ad1a6a4de269131f9e3359e ts=2026-10-16T04:22:59.8590000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11083] _id=6ad2284cde269131f9e3c1ce ts=2026-10-16T13:36:11.8960000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 30 interval(s) ≤ 0.019s..0.023s shown 
  - Evidence: 19ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[662] _id=6ac64cf5de269131f9b9e95a ts=2026-10-07T13:45:23.9350000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[663] _id=6ac64cf5de269131f9b9e95b ts=2026-10-07T13:45:23.9540000Z; 21ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11110] _id=6ad22870de269131f9e3c4d1 ts=2026-10-16T13:36:47.9540000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11111] _id=6ad22870de269131f9e3c4d7 ts=2026-10-16T13:36:47.9750000Z; 23ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11112] _id=6ad22871de269131f9e3c4e6 ts=2026-10-16T13:36:48.7220000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11113] _id=6ad22871de269131f9e3c4e8 ts=2026-10-16T13:36:48.7450000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 43m 
  - Evidence: 167h 43m: 6ab9a88e9a8420a1e6b56aeb.jsonl[650] _id=6ac64ce5de269131f9b9e84b ts=2026-10-07T13:45:08.8210000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[5994] _id=6acf8390de269131f9d31650 ts=2026-10-14T13:28:48.1810000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 20m 
  - Evidence: 47h 20m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6526] _id=6acf889ede269131f9d3769a ts=2026-10-14T13:50:22.1540000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[10293] _id=6ad22258de269131f9e35022 ts=2026-10-16T13:10:47.9060000Z; 18m 14s: 6ab9a88e9a8420a1e6b56aeb.jsonl[10293] _id=6ad22258de269131f9e35022 ts=2026-10-16T13:10:47.9060000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[10947] _id=6ad2269ede269131f9e3a3f2 ts=2026-10-16T13:29:01.9860000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2112] _id=6ac79dd8de269131f9c0c335 ts=2026-10-08T13:42:47.3440000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2405] _id=6ace2ef5de269131f9ce8d8c ts=2026-10-13T13:15:33.2890000Z; 23h 43m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6085] _id=6acf84a2de269131f9d32a5f ts=2026-10-14T13:33:22.3620000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6923] _id=6ad0d252de269131f9da599a ts=2026-10-15T13:17:05.7950000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aeb.jsonl[4] _id=6ac4fbd8de269131f9b16430 ts=2026-10-06T13:47:03.4130000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[325] _id=6ac64832de269131f9b8ec91 ts=2026-10-07T13:25:04.8740000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2111] _id=6ac79dd8de269131f9c0c334 ts=2026-10-08T13:42:47.3430000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2404] _id=6ace2ef5de269131f9ce8d8b ts=2026-10-13T13:15:33.2890000Z; 23h 43m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6084] _id=6acf84a2de269131f9d32a5e ts=2026-10-14T13:33:22.3620000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[6922] _id=6ad0d252de269131f9da5999 ts=2026-10-15T13:17:05.7950000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aeb.jsonl[3] _id=6ac4fbd8de269131f9b1642e ts=2026-10-06T13:47:03.4110000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[324] _id=6ac64832de269131f9b8ec90 ts=2026-10-07T13:25:04.8740000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2406] _id=6ace2ef5de269131f9ce8d88 ts=2026-10-08T13:59:03.555Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2501] _id=6ace2fe4de269131f9ce9512 ts=2026-10-13T13:19:31.8860000Z; 24h 0m: 6ab9a88e9a8420a1e6b56aeb.jsonl[322] _id=6ac64832de269131f9b8ec8a ts=2026-10-06T13:59:42.173Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1472] _id=6ac79ac7de269131f9c03cca ts=2026-10-07T13:59:46.028Z; 23h 59m: 6ab9a88e9a8420a1e6b56aeb.jsonl[6920] _id=6ad0d252de269131f9da5994 ts=2026-10-14T14:00:05.24Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[8209] _id=6ad1940bde269131f9e2d5c3 ts=2026-10-15T13:59:51.253Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a88e9a8420a1e6b56aeb.jsonl[2173] _id=6ac79e9bde269131f9c0e240 ts=2026-10-08T13:46:02.5000000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[2402] _id=6ace2f08de269131f9ce8dec ts=2026-10-13T13:15:50.3550000Z; 23h 36m: 6ab9a88e9a8420a1e6b56aeb.jsonl[837] _id=6ac64edade269131f9ba1a80 ts=2026-10-07T13:53:29.7580000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[1478] _id=6ac79adbde269131f9c03edb ts=2026-10-08T13:30:01.3660000Z; 23h 26m: 6ab9a88e9a8420a1e6b56aeb.jsonl[299] _id=6ac4fe93de269131f9b228ee ts=2026-10-06T13:58:42.4310000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[320] _id=6ac6483dde269131f9b8eed0 ts=2026-10-07T13:25:15.9540000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[634] _id=6ac64c9ade269131f9b9e22c ts=2026-10-07T13:43:52.9770000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[635] _id=6ac64c9ade269131f9b9e22d ts=2026-10-07T13:43:52.9770000Z; 1ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11218] _id=6ad228ecde269131f9e3cedd ts=2026-10-16T13:38:51.8630000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11219] _id=6ad228ecde269131f9e3cede ts=2026-10-16T13:38:51.8640000Z; 5ms: 6ab9a88e9a8420a1e6b56aeb.jsonl[11350] _id=6ad22a4dde269131f9e3ea9c ts=2026-10-16T13:44:45.0610000Z -> 6ab9a88e9a8420a1e6b56aeb.jsonl[11351] _id=6ad22a4dde269131f9e3ea9e ts=2026-10-16T13:44:45.0660000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[620] _id=6ac64c7cde269131f9b9df91 ts=2026-10-07T13:43:23.2620000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[728] _id=6ac64d88de269131f9b9f484 ts=2026-10-07T13:47:51.3340000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[2268] _id=6ac79ffdde269131f9c121d9 ts=2026-10-08T13:51:56.2820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[6865] _id=6acf8a61de269131f9d3b124 ts=2026-10-14T13:57:52.5260000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[9749] _id=6ad1a6a6de269131f9e335a5 ts=2026-10-16T04:23:02.2770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[10293] _id=6ad22258de269131f9e35022 ts=2026-10-16T13:10:47.9060000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[10947] _id=6ad2269ede269131f9e3a3f2 ts=2026-10-16T13:29:01.9860000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[7011] _id=6ad0d37bde269131f9da6c15 ts=2026-10-15T13:22:02.3530000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[2116] _id=6ac79de8de269131f9c0c568 ts=?`; `6ab9a88e9a8420a1e6b56aeb.jsonl[9735] _id=6ad1a8afde269131f9e336fe ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 47 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[1720] _id=6ac79bc5de269131f9c062b6 ts=2026-10-08T13:33:56.6440000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[1777] _id=6ac79bddde269131f9c0674f ts=2026-10-08T13:34:19.8840000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[2851] _id=6ace3426de269131f9cebde2 ts=2026-10-13T13:37:41.2600000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 92 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[1557] _id=6ac79b93de269131f9c05b5f ts=2026-10-08T13:31:41.9080000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[1565] _id=6ac79b93de269131f9c05b66 ts=2026-10-08T13:31:41.9080000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[1570] _id=6ac79b94de269131f9c05b7c ts=2026-10-08T13:32:55.8740000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 18 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[5736] _id=6acf81bfde269131f9d2ec1e ts=2026-10-14T13:21:02.8980000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[5813] _id=6acf822cde269131f9d2f591 ts=2026-10-14T13:22:51.6320000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[5879] _id=6acf8296de269131f9d301a9 ts=2026-10-14T13:24:37.7290000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 419 start, 412 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'BecameCameraCentered' (totals: 393 open, 392 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 14 unmatched 'BecameVisible' (totals: 721 open, 707 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 29 open, 28 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 50 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 151 of 11439 adjacent _id pairs reverse in client time; worst 107.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56aeb.jsonl[986] _id=6ac64fbfde269131f9ba326e ts=2026-10-07T13:57:18.4960000Z`; `6ab9a88e9a8420a1e6b56aeb.jsonl[987] _id=6ac64fbfde269131f9ba326f ts=2026-10-07T13:55:30.7350000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.66s, min -429390.10s, max -0.30s over 11440 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56aeb\coverage.yaml

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

### `PlayerPositionEvent` — 3570 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (2103); Unit 4 Dev (336); Unit 3 Dev (240); Unit 4 Dev - Dungeon (225); Unit 1 Dev (219); Unit 4 Dev - Anderson Base (133); Unit 5 Dev (120); Unit 5 Dev - Dungeon (109); Unit 3 Dungeon Dev (85)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.08s, n=3558)
- **Fields under `data`:**

```text
data.position  (object, 3570/3570 records)
data.position.x  (number, 3570/3570 records)
    numeric range -680.626 .. 1553.41 (693 unique)
data.position.y  (number, 3570/3570 records)
    numeric range -115.085 .. 222.252 (483 unique)
data.position.z  (number, 3570/3570 records)
    numeric range -1129.03 .. 2073.6 (692 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2273 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (706); Unit 4 Dev (330); Unit 3 Dev (321); Unit 1 Dev (235); Unit 5 Dev (222); Unit 4 Dev - Anderson Base (140); Unit 4 Dev - Dungeon (134); Unit 3 Dungeon Dev (116); Unit 5 Dev - Dungeon (69)
- **eventKey:** present on 1442 of 2273 records
- **Intervals:** median 4.07s (p5 0.00s / p95 33.17s, n=2272)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1442; [conversationId, dialogueEventType] x831
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2273/2273 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2273/2273 records)
    "DialogueNodeEvent"  x1442
    "DialogueStartEvent"  x419
    "DialogueFinishEvent"  x412
data.nodeId  (number, 1442/2273 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `InputEvent` — 2269 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (810); Unit 3 Dev (408); Unit 4 Dev - Dungeon (257); Unit 1 Dev (237); Unit 5 Dev - Dungeon (164); Unit 4 Dev (143); Unit 3 Dungeon Dev (108); Unit 4 Dev - Anderson Base (87); Unit 5 Dev (55)
- **Intervals:** median 2.09s (p5 0.19s / p95 39.97s, n=2268)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2269/2269 records)
    "pressed"  x2269
data.actionType  (string, 2269/2269 records)
    "Move"  x1726
    "Interact"  x387
    "Ascend"  x88
    "Hoverboard"  x24
    "Sprint"  x18
    "Jump"  x17
    "Map"  x7
    "Pause"  x2
data.key  (string, 2269/2269 records, 19 empty-string)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2269/2269 records)
    "Player"  x1515
    "Drone"  x754
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2213 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1439); Unit 4 Dev (370); Unit 5 Dev - Dungeon (266); Unit 3 Dungeon Dev (138)
- **Intervals:** median 0.05s (p5 0.00s / p95 2.29s, n=2212)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2213/2213 records)
    "BecameVisible"  x721
    "BecameInvisible"  x707
    "BecameCameraCentered"  x393
    "BecameCameraUncentered"  x392
data.pieceId  (string, 2213/2213 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2213/2213 records)
    1419 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `argumentationNodeEvent` — 376 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (185); Unit 3 Dev (71); Unit 5 Dev (64); Unit 1 Dev (33); Unit 2 Prod (Refactor) (23)
- **Intervals:** median 0.50s (p5 0.04s / p95 10.09s, n=375)
- **Fields under `data`:**

```text
data.actionType  (string, 376/376 records)
    "argumentationNodeHoverEnd"  x156
    "argumentationNodeHoverStart"  x156
    "argumentationNodeAdd"  x42
    "argumentationNodeRemove"  x22
data.argumentationTitle  (string, 376/376 records)
    "Unit 4 - Flooding"  x185
    "Unit 3 - Pollution Upstream"  x71
    "Unit 5"  x64
    "Unit 2 – Watershed"  x23
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 376/376 records)
    "1"  x49
    "A"  x45
    "C"  x42
    "II"  x41
    "B"  x38
    "I"  x36
    "3"  x35
    "2"  x33
    "D"  x28
    "4"  x24
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 294 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (77); Unit 2 Prod (Refactor) (54); Unit 1 Dev (47); Unit 4 Dev (36); Unit 3 Dungeon Dev (28); Unit 5 Dev - Dungeon (17); Unit 5 Dev (14); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 13.29s (p5 0.21s / p95 550.70s, n=293)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 294/294 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 294/294 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (15); Unit 4 Dev - Dungeon (12); Unit 3 Dev (11); Unit 4 Dev (10); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 220.81s (p5 0.01s / p95 54800.76s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x34
data.questID  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/84 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 74 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (39); Unit 2 Prod (Refactor) (35)
- **Intervals:** median 10.10s (p5 1.46s / p95 31316.67s, n=73)
- **`data` key-set variants:** [actionType, featureUsed] x57; [actionType, featureUsed, location] x17
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 74/74 records)
    "MapOpenEvent"  x29
    "MapCloseEvent"  x28
    "WaypointMoveEvent"  x11
    "WaypointSetEvent"  x6
data.featureUsed  (string, 74/74 records)
    "Map"  x57
    "Waypoint"  x17
data.location  (object, 17/74 records)
data.location.x  (number, 17/74 records)
    numeric range -318.005 .. 248.575 (17 unique)
data.location.y  (number, 17/74 records)
    numeric range -304.106 .. 224.515 (17 unique)
data.location.z  (number, 17/74 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 64 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (40); Unit 3 Dev (16); Unit 4 Dev (8)
- **Intervals:** median 2.28s (p5 0.32s / p95 20.81s, n=63)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/64 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/64 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 58/64 records)
    "RightDrag"  x32
    "LeftDrag"  x26
data.currentSoilType  (string, 58/64 records)
    "CLAY"  x13
    "CLAYSAND"  x12
    "SAND"  x11
    "CLAYROCK"  x10
    "SANDGRAVEL"  x7
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 58/64 records)
    "false"  x43
    "true"  x15
data.waterLevelStatus  (string, 58/64 records)
    "TooHigh"  x22
    "Proper"  x21
    "TooLow"  x15
data.waterRetentionChange  (string, 58/64 records)
    "Increase"  x27
    "Decrease"  x16
    "NoChange"  x15
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 39 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (7); Unit 4 Dev (5); Unit 3 Dev (3); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 382.16s (p5 8.54s / p95 85119.30s, n=38)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "DebugMenuStateChanged"  x39
data.isOpened  (bool, 39/39 records)
    false  x39
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 29 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 4 Dev (6); Unit 2 Prod (Refactor) (2); Transition (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1014.40s (p5 14.18s / p95 85303.74s, n=28)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 29/29 records)
    true  x29
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 28 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (19); Unit 3 Dev (3); Unit 5 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 15.18s (p5 6.14s / p95 106438.63s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "submitAnswerEvent"  x28
data.answerSubmitted  (string, 28/28 records)
    19 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 28/28 records)
    "Unit 4 - Flooding"  x19
    "Unit 3 - Pollution Upstream"  x3
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 26 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (26)
- **Intervals:** median 16.76s (p5 1.27s / p95 77.31s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "On"  x19
    "Off"  x7
data.floor  (string, 26/26 records)
    "3"  x16
    "4"  x5
    "2"  x3
    "1"  x2
data.machineNumber  (string, 26/26 records)
    "One"  x25
    "Two"  x1
data.machineType  (string, 26/26 records)
    "Condenser"  x13
    "DualChamber_Condenser"  x4
    "Evaporator"  x4
    "DualChamber_Evaporator"  x3
    "VentSwitch"  x2
data.room  (string, 26/26 records)
    "2"  x14
    "1"  x6
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 3934.49s (p5 223.66s / p95 137164.81s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (7); Unit 2 Prod (Refactor) (6); MainMenu (1); Transition (1); Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1094.18s (p5 30.68s / p95 137887.53s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 86.76s (p5 0.04s / p95 324107.03s, n=13)
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

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (4)
- **Intervals:** median 4.01s (p5 0.89s / p95 42112.72s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 12 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (12)
- **Intervals:** median 22.54s (p5 1.83s / p95 1459.16s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records, 3 empty-string)
    "cameraPlaced"  x9
    ""  x3
data.boxId  (string, 12/12 records)
    "0"  x4
    "1"  x4
    "2"  x4
data.soilType  (string, 12/12 records)
    "None"  x6
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 7 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (7)
- **Intervals:** median 94.27s (p5 25.15s / p95 352.86s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "ChangeCanister"  x7
data.canisterType  (string, 7/7 records)
    "Clay"  x3
    "Gravel"  x3
    "Sand"  x1
data.floor  (string, 7/7 records)
    "4"  x3
    "5"  x3
    "3"  x1
data.machine  (string, 7/7 records)
    "1"  x6
    "2"  x1
data.row  (string, 7/7 records)
    "TopRow"  x6
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 3.44s (p5 0.61s / p95 9.92s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted In"  x1
data.featureUsed  (string, 6/6 records)
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records, 1 empty-string)
    ""  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 71898.01s (p5 33975.68s / p95 526278.91s, n=4)
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

- **Scenes:** Unit 3 Dev (2); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1094.08s (p5 113.54s / p95 153492.58s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x3
    "Open"  x1
data.chatID  (string, 4/4 records)
    "NA"  x3
    "[11-26, 11-25, 11-26, 11-27, 11-27]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 301911.88s (p5 30195.14s / p95 573628.61s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationToolOpen"  x2
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 3/3 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x1
data.toolName  (string, 3/3 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
    at invoke_iiii (blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:474038)
    at wasm://wasm/0a915116:wasm-function[83436]:0x171e8bd
    at wasm://wasm/0a915116:wasm-function[1942]:0xf58e4
    at wasm://wasm/0a915116:wasm-function[109965]:0x256667c
    at wasm://wasm/0a915116:wasm-function[106271]:0x24b7432
    at wasm://wasm/0a915116:wasm-function[84075]:0x1745541
    at wasm://wasm/0a915116:wasm-function[84074]:0x1745477
    at wasm://wasm/0a915116:wasm-function[104583]:0x23e6a91
    at wasm://wasm/0a915116:wasm-function[103961]:0x235b2a8
    at wasm://wasm/0a915116:wasm-function[105691]:0x245f4f0
    at wasm://wasm/0a915116:wasm-function[105691]:0x245f565
    at wasm://wasm/0a915116:wasm-function[110043]:0x256eaaf
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:23580
    at _JS_CallAsLongAsNoExceptionsSeen (blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:23594)
    at wasm://wasm/0a915116:wasm-function[110044]:0x256ebbe
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at browserIterationFunc (blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:115768)
    at callUserCallback (blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:98130)
    at Object.runIter (blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:99497)
    at Browser_mainLoop_runner (blob:https://mhs.adroit.games/aee8914f-801a-408e-998e-b97214faa5cf:9:115294)"  x1
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
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (40 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TerasGardenBox` data.soilType: "None" (6x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (11x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (22x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*