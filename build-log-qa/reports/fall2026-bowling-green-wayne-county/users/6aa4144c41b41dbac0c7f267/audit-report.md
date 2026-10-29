# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f267

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f267
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f267.jsonl
- **Records:** 14259 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f267
- **Time span:** 2026-09-23T18:15:36.431000+00:00 .. 2026-10-07T15:34:36.443000+00:00 (333h 19m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f267\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14259 records, 11 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 102 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4719 | 33.09 | 1 | 9 | 0 | 2026-09-23T18:15:51.929000+00:00 | 2026-10-07T15:34:36.443000+00:00 | 333h 18m |
| PuzzlePieceVisibleEvent | 3981 | 27.92 | 1 | 4 | 0 | 2026-09-25T18:22:32.268000+00:00 | 2026-10-07T14:56:56.006000+00:00 | 284h 34m |
| PlayerPositionEvent | 2556 | 17.93 | 1 | 9 | 0 | 2026-09-23T18:15:47.083000+00:00 | 2026-10-07T15:34:32.360000+00:00 | 333h 18m |
| DialogueEvent | 1897 | 13.3 | 1 | 9 | 1121 | 2026-09-23T18:16:08.636000+00:00 | 2026-10-07T15:34:22.373000+00:00 | 333h 18m |
| ObjectInterEvent | 457 | 3.2 | 1 | 9 | 0 | 2026-09-23T18:20:43.530000+00:00 | 2026-10-07T15:34:36.443000+00:00 | 333h 13m |
| argumentationNodeEvent | 136 | 0.95 | 1 | 4 | 0 | 2026-09-29T18:48:49.713000+00:00 | 2026-10-07T15:14:45.112000+00:00 | 188h 25m |
| questEvent | 93 | 0.65 | 1 | 9 | 93 | 2026-09-23T18:16:08.615000+00:00 | 2026-10-07T15:29:54.218000+00:00 | 333h 13m |
| Soil Key Puzzle | 86 | 0.6 | 1 | 3 | 0 | 2026-09-28T18:38:29.860000+00:00 | 2026-10-01T14:52:32.832000+00:00 | 68h 14m |
| TopographicMapEvent | 67 | 0.47 | 1 | 2 | 0 | 2026-09-25T18:26:36.415000+00:00 | 2026-09-30T19:21:04.140000+00:00 | 120h 54m |
| soilMachine | 52 | 0.36 | 1 | 1 | 0 | 2026-10-05T18:21:47.086000+00:00 | 2026-10-06T18:24:37.714000+00:00 | 24h 2m |
| gameWindowFocusEvent | 47 | 0.33 | 1 | 9 | 0 | 2026-09-23T18:15:36.431000+00:00 | 2026-10-07T15:31:15.839000+00:00 | 333h 15m |
| DEBUGMenu | 33 | 0.23 | 1 | 9 | 0 | 2026-09-23T18:15:47.076000+00:00 | 2026-10-07T15:21:28.751000+00:00 | 333h 5m |
| WaterChamberEvent | 31 | 0.22 | 1 | 1 | 0 | 2026-10-07T14:48:28.539000+00:00 | 2026-10-07T15:05:50.136000+00:00 | 17m 21s |
| gameWindowUnfocusEvent | 26 | 0.18 | 1 | 8 | 0 | 2026-09-23T18:32:50.561000+00:00 | 2026-10-07T15:31:13.844000+00:00 | 332h 58m |
| gameStartEvent | 24 | 0.17 | 1 | 1 | 0 | 2026-09-23T18:15:36.432000+00:00 | 2026-10-07T15:21:29.245000+00:00 | 333h 5m |
| argumentationAnswerEvent | 11 | 0.08 | 1 | 4 | 0 | 2026-09-30T12:32:40.990000+00:00 | 2026-10-07T15:14:46.808000+00:00 | 170h 42m |
| argumentationEvent | 11 | 0.08 | 1 | 4 | 0 | 2026-09-30T12:32:08.372000+00:00 | 2026-10-07T15:14:46.879000+00:00 | 170h 42m |
| DaniEvent | 8 | 0.06 | 1 | 1 | 0 | 2026-09-30T12:41:31.091000+00:00 | 2026-09-30T19:21:05.902000+00:00 | 6h 39m |
| TerasGardenBox | 7 | 0.05 | 1 | 1 | 0 | 2026-10-06T18:52:28.519000+00:00 | 2026-10-06T18:54:03.790000+00:00 | 1m 35s |
| SolarStillDesignEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-07T15:26:39.151000+00:00 | 2026-10-07T15:26:44.688000+00:00 | 5.5s |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-07T14:43:43.945000+00:00 | 2026-10-07T15:21:45.850000+00:00 | 38m 1s |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-30T19:27:41.911000+00:00 | 2026-10-07T15:34:36.425000+00:00 | 164h 6m |
| argumentationToolEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-09-30T18:27:39.444000+00:00 | 2026-09-30T18:27:39.444000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 590814.514s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 0.905s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 10.742s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 23.261s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 7477.675s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 703.382s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2210.533s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.468s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 2; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Press [E/Action button] to enter escape pod  
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Topography Piece 1; Topography Piece 2; Topography Piece 3; Topography Piece 4; Topography Piece 5; Topography Piece 6; Topography Slot 1; Topography Slot 2; Topography Slot 3; Topography Slot 5; Topography Slot 6 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 180 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,I; A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,C,D,2,I; C,D,3,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 1 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 24 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 34; 54; 56 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; What Was That?; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 10.4x vs baseline. 
  - Observed: 52 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 126 mismatch(es); e.g. 'DialogueNodeEvent:30:96' vs expected 'DialogueNodeEvent:30:33' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[374] _id=6abaad0a485cab4c956f7647 ts=2026-09-23T18:43:31.949Z`; `6aa4144c41b41dbac0c7f267.jsonl[383] _id=6abaad0a485cab4c956f7653 ts=2026-09-23T18:43:36.756Z`; `6aa4144c41b41dbac0c7f267.jsonl[850] _id=6abaad4f485cab4c956f8080 ts=2026-09-24T18:11:25.452Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[1001] _id=6abaad62485cab4c956f82aa ts=2026-09-25T18:23:44.257Z`; `6aa4144c41b41dbac0c7f267.jsonl[2130] _id=6abaadd7485cab4c956f9553 ts=2026-09-25T18:35:16.099Z`; `6aa4144c41b41dbac0c7f267.jsonl[2219] _id=6abaaddc485cab4c956f9651 ts=2026-09-25T18:40:10.694Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[51] _id=6ab41748485cab4c954f369a ts=2026-09-23T18:15:36.4320000Z`; `6aa4144c41b41dbac0c7f267.jsonl[560] _id=6abaad2a485cab4c956f7a65 ts=2026-09-24T17:45:08.975Z`; `6aa4144c41b41dbac0c7f267.jsonl[702] _id=6abaad3d485cab4c956f7d79 ts=2026-09-24T17:51:33.793Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 47 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 47} 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[50] _id=6ab41748485cab4c954f3698 ts=2026-09-23T18:15:36.4310000Z`; `6aa4144c41b41dbac0c7f267.jsonl[316] _id=6ab41b55485cab4c954f55d6 ts=2026-09-23T18:32:53.7860000Z`; `6aa4144c41b41dbac0c7f267.jsonl[353] _id=6ab41bcb485cab4c954f59c6 ts=2026-09-23T18:34:51.8300000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[315] _id=6ab41b52485cab4c954f55c0 ts=2026-09-23T18:32:50.5610000Z`; `6aa4144c41b41dbac0c7f267.jsonl[355] _id=6ab41bcb485cab4c954f59c4 ts=2026-09-23T18:34:51.7580000Z`; `6aa4144c41b41dbac0c7f267.jsonl[375] _id=6abaad05485cab4c956f75ff ts=2026-09-23T18:34:53.167Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 14 of 67 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[1083] _id=6abaad6a485cab4c956f83cd ts=2026-09-25T18:26:36.415Z`; `6aa4144c41b41dbac0c7f267.jsonl[1094] _id=6abaad6a485cab4c956f83d1 ts=2026-09-25T18:26:38.106Z`; `6aa4144c41b41dbac0c7f267.jsonl[1107] _id=6abaad6a485cab4c956f83d7 ts=2026-09-25T18:26:43.716Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4718 | 0.0 | 1.006 | 254.329 | 17.085 | 355994.695 | 0.24 | 253 | 15 |
| PuzzlePieceVisibleEvent | 3980 | 0.0 | 0.029 | 257.403 | 1.507 | 444514.167 | 0.23 | 2467 | 7 |
| PlayerPositionEvent | 2543 | 0.0 | 9.999 | 404.454 | 10.035 | 355955.336 | 0.15 | 1 | 11 |
| DialogueEvent | 1896 | 0.0 | 4.861 | 632.855 | 55.243 | 356005.821 | 0.09 | 532 | 14 |
| ObjectInterEvent | 456 | 0.001 | 7.494 | 2630.774 | 417.589 | 356529.131 | 0.02 | 4 | 19 |
| argumentationNodeEvent | 135 | 0.018 | 0.29 | 5024.855 | 19.72 | 519250.648 | 0.01 | 35 | 4 |
| questEvent | 92 | 0.0 | 267.24 | 13039.409 | 77260.637 | 356068.964 | 0.0 | 19 | 22 |
| Soil Key Puzzle | 85 | 0.062 | 0.7 | 2889.917 | 31.691 | 172525.444 | 0.02 | 0 | 3 |
| TopographicMapEvent | 66 | 0.125 | 3.117 | 6594.966 | 6425.174 | 257294.255 | 0.01 | 0 | 8 |
| soilMachine | 51 | 0.205 | 2.468 | 1697.463 | 342.725 | 84894.45 | 0.04 | 0 | 1 |
| gameWindowFocusEvent | 46 | 1.433 | 703.382 | 26081.291 | 86528.396 | 356041.923 | 0.0 | 0 | 23 |
| DEBUGMenu | 32 | 5.284 | 1198.788 | 37473.177 | 164014.74 | 357060.586 | 0.0 | 0 | 21 |
| WaterChamberEvent | 30 | 0.679 | 15.277 | 34.72 | 137.624 | 238.781 | 1.73 | 0 | 0 |
| gameWindowUnfocusEvent | 25 | 1.409 | 2210.533 | 47948.131 | 294974.185 | 357911.376 | 0.0 | 0 | 13 |
| gameStartEvent | 23 | 190.387 | 7477.675 | 52137.079 | 241164.225 | 357565.33 | 0.0 | 0 | 17 |
| argumentationAnswerEvent | 10 | 0.641 | 23.261 | 61452.582 | 318817.952 | 519388.099 | 0.0 | 0 | 3 |
| argumentationEvent | 10 | 0.031 | 71.548 | 61455.851 | 318686.314 | 519192.163 | 0.0 | 2 | 3 |
| DaniEvent | 7 | 1.754 | 2.817 | 3424.973 | 10629.51 | 11365.585 | 0.02 | 0 | 3 |
| TerasGardenBox | 6 | 1.297 | 10.742 | 15.879 | 38.83 | 42.11 | 3.78 | 0 | 0 |
| SolarStillDesignEvent | 5 | 0.755 | 0.905 | 1.107 | 1.768 | 1.92 | 54.18 | 0 | 0 |
| chatEvent | 3 | 339.741 | 906.325 | 760.635 | 1022.888 | 1035.839 | 0.08 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 590814.514 | 590814.514 | 590814.514 | 590814.514 | 590814.514 | 0.0 | 0 | 1 |
| argumentationToolEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 9 group(s), 37 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[6383] _id=6abd56ce485cab4c9591d102 ts=2026-09-30T18:37:01.9520000Z == 6aa4144c41b41dbac0c7f267.jsonl[6384] _id=6abd56ce485cab4c9591d107 ts=2026-09-30T18:37:01.9520000Z`; `6aa4144c41b41dbac0c7f267.jsonl[9486] _id=6abe74ed485cab4c95a98178 ts=2026-10-01T14:57:49.5030000Z == 6aa4144c41b41dbac0c7f267.jsonl[9478] _id=6abe74ed485cab4c95a9817c ts=2026-10-01T14:57:49.5030000Z`; `6aa4144c41b41dbac0c7f267.jsonl[9479] _id=6abe74ed485cab4c95a9817f ts=2026-10-01T14:57:49.5040000Z == 6aa4144c41b41dbac0c7f267.jsonl[9482] _id=6abe74ed485cab4c95a98182 ts=2026-10-01T14:57:49.5040000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 206 group(s), 324 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[932] _id=6abaad5a485cab4c956f81b9 ts=2026-09-25T18:22:32.268Z == 6aa4144c41b41dbac0c7f267.jsonl[933] _id=6abaad5b485cab4c956f81bd ts=2026-09-25T18:22:32.268Z`; `6aa4144c41b41dbac0c7f267.jsonl[867] _id=6abaad5b485cab4c956f81cd ts=2026-09-25T18:22:32.276Z == 6aa4144c41b41dbac0c7f267.jsonl[868] _id=6abaad5b485cab4c956f81d1 ts=2026-09-25T18:22:32.276Z`; `6aa4144c41b41dbac0c7f267.jsonl[935] _id=6abaad5b485cab4c956f81d3 ts=2026-09-25T18:22:32.347Z == 6aa4144c41b41dbac0c7f267.jsonl[972] _id=6abaad5c485cab4c956f81d7 ts=2026-09-25T18:22:32.347Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[13982] _id=6ac66394de269131f9bba20b ts=2026-10-07T15:21:55.5150000Z == 6aa4144c41b41dbac0c7f267.jsonl[13983] _id=6ac66394de269131f9bba20c ts=2026-10-07T15:21:55.5150000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 96 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `278ms: 6aa4144c41b41dbac0c7f267.jsonl[0] _id=6ab4187e485cab4c954f3d78 ts=2026-09-23T18:20:46.1580000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[2] _id=6ab4187e485cab4c954f3d80 ts=2026-09-23T18:20:46.4360000Z`; `241ms: 6aa4144c41b41dbac0c7f267.jsonl[2] _id=6ab4187e485cab4c954f3d80 ts=2026-09-23T18:20:46.4360000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[4] _id=6ab4187e485cab4c954f3d86 ts=2026-09-23T18:20:46.6770000Z`; `228ms: 6aa4144c41b41dbac0c7f267.jsonl[4] _id=6ab4187e485cab4c954f3d86 ts=2026-09-23T18:20:46.6770000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[6] _id=6ab4187e485cab4c954f3d8c ts=2026-09-23T18:20:46.9050000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 900 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4144c41b41dbac0c7f267.jsonl[934] _id=6abaad5b485cab4c956f81cb ts=2026-09-25T18:22:32.268Z ~ 6aa4144c41b41dbac0c7f267.jsonl[867] _id=6abaad5b485cab4c956f81cd ts=2026-09-25T18:22:32.276Z`; `71ms: 6aa4144c41b41dbac0c7f267.jsonl[868] _id=6abaad5b485cab4c956f81d1 ts=2026-09-25T18:22:32.276Z ~ 6aa4144c41b41dbac0c7f267.jsonl[935] _id=6abaad5b485cab4c956f81d3 ts=2026-09-25T18:22:32.347Z`; `174ms: 6aa4144c41b41dbac0c7f267.jsonl[973] _id=6abaad5c485cab4c956f81e3 ts=2026-09-25T18:22:32.347Z ~ 6aa4144c41b41dbac0c7f267.jsonl[962] _id=6abaad5c485cab4c956f81e5 ts=2026-09-25T18:22:32.521Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `195ms: 6aa4144c41b41dbac0c7f267.jsonl[8399] _id=6abe7386485cab4c95a97098 ts=2026-10-01T14:51:50.4430000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[8398] _id=6abe7386485cab4c95a9709c ts=2026-10-01T14:51:50.6380000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `267ms: 6aa4144c41b41dbac0c7f267.jsonl[2271] _id=6abaade2485cab4c956f975f ts=2026-09-25T18:43:55.458Z ~ 6aa4144c41b41dbac0c7f267.jsonl[2279] _id=6abaade3485cab4c956f9778 ts=2026-09-25T18:43:55.725Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `641ms: 6aa4144c41b41dbac0c7f267.jsonl[12012] _id=6ac541eade269131f9b6d8c9 ts=2026-10-06T18:46:02.6960000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[12010] _id=6ac541ebde269131f9b6d8eb ts=2026-10-06T18:46:03.3370000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6aa4144c41b41dbac0c7f267.jsonl[6153] _id=6abd54e0485cab4c959187a9 ts=2026-09-30T18:28:48.1100000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[6158] _id=6abd54e0485cab4c959187b7 ts=2026-09-30T18:28:48.1470000Z`; `31ms: 6aa4144c41b41dbac0c7f267.jsonl[12040] _id=6ac5421ade269131f9b6dfe3 ts=2026-10-06T18:46:50.1650000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[12042] _id=6ac5421ade269131f9b6dfed ts=2026-10-06T18:46:50.1960000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 23 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `580ms: 6aa4144c41b41dbac0c7f267.jsonl[3918] _id=6abc0811485cab4c9584cacd ts=2026-09-29T18:48:49.7130000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[3915] _id=6abc0812485cab4c9584cad7 ts=2026-09-29T18:48:50.2930000Z`; `409ms: 6aa4144c41b41dbac0c7f267.jsonl[3997] _id=6abd019a485cab4c9586583d ts=2026-09-30T12:33:31.4700000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[3993] _id=6abd019a485cab4c95865841 ts=2026-09-30T12:33:31.8790000Z`; `406ms: 6aa4144c41b41dbac0c7f267.jsonl[3998] _id=6abd019a485cab4c9586583f ts=2026-09-30T12:33:31.5160000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[3994] _id=6abd019a485cab4c95865843 ts=2026-09-30T12:33:31.9220000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6aa4144c41b41dbac0c7f267.jsonl[13946] _id=6ac66230de269131f9bb98ec ts=2026-10-07T15:16:00.1080000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[13947] _id=6ac66230de269131f9bb98ed ts=2026-10-07T15:16:00.1090000Z`; `3ms: 6aa4144c41b41dbac0c7f267.jsonl[14118] _id=6ac664f9de269131f9bbcde2 ts=2026-10-07T15:27:53.4380000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[14119] _id=6ac664f9de269131f9bbcde4 ts=2026-10-07T15:27:53.4410000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `709ms: 6aa4144c41b41dbac0c7f267.jsonl[10120] _id=6ac3eabcde269131f9aeebc7 ts=2026-10-05T18:21:48.5860000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[10106] _id=6ac3eabdde269131f9aeebdd ts=2026-10-05T18:21:49.2950000Z`; `647ms: 6aa4144c41b41dbac0c7f267.jsonl[10106] _id=6ac3eabdde269131f9aeebdd ts=2026-10-05T18:21:49.2950000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[10125] _id=6ac3eabdde269131f9aeebe9 ts=2026-10-05T18:21:49.9420000Z`; `444ms: 6aa4144c41b41dbac0c7f267.jsonl[10134] _id=6ac3eac5de269131f9aeec63 ts=2026-10-05T18:21:57.1150000Z ~ 6aa4144c41b41dbac0c7f267.jsonl[10141] _id=6ac3eac5de269131f9aeec73 ts=2026-10-05T18:21:57.5590000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 99h 11m 
  - Evidence: 99h 11m: 6aa4144c41b41dbac0c7f267.jsonl[9484] _id=6abe74eb485cab4c95a98166 ts=2026-10-01T14:57:47.9580000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9948] _id=6ac3e7b0de269131f9aebd3a ts=2026-10-05T18:08:48.5440000Z; 71h 45m: 6aa4144c41b41dbac0c7f267.jsonl[987] _id=6abaad60485cab4c956f825b ts=2026-09-25T18:23:04.234Z -> 6aa4144c41b41dbac0c7f267.jsonl[2281] _id=6abaade3485cab4c956f9797 ts=2026-09-28T18:08:18.8190000Z; 24h 7m: 6aa4144c41b41dbac0c7f267.jsonl[771] _id=6abaad45485cab4c956f7ec3 ts=2026-09-24T18:09:55.412Z -> 6aa4144c41b41dbac0c7f267.jsonl[843] _id=6abaad50485cab4c956f80a9 ts=2026-09-25T18:17:35.734Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 3h 9m 
  - Evidence: 3h 9m: 6aa4144c41b41dbac0c7f267.jsonl[4931] _id=6abd264f485cab4c958bc921 ts=2026-09-30T15:10:07.8850000Z -> 6aa4144c41b41dbac0c7f267.jsonl[5807] _id=6abd52b5485cab4c95912a81 ts=2026-09-30T18:19:33.4700000Z; 2h 28m: 6aa4144c41b41dbac0c7f267.jsonl[4088] _id=6abd037d485cab4c95866399 ts=2026-09-30T12:41:33.0680000Z -> 6aa4144c41b41dbac0c7f267.jsonl[4926] _id=6abd264d485cab4c958bc8b7 ts=2026-09-30T15:10:05.0680000Z; 1h 1m: 6aa4144c41b41dbac0c7f267.jsonl[5810] _id=6abd52b7485cab4c95912acb ts=2026-09-30T18:19:35.2880000Z -> 6aa4144c41b41dbac0c7f267.jsonl[7434] _id=6abd6120485cab4c959293fc ts=2026-09-30T19:21:04.1480000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 98h 53m 
  - Evidence: 98h 53m: 6aa4144c41b41dbac0c7f267.jsonl[9939] _id=6abe7910485cab4c95a9ff0c ts=2026-10-01T15:15:28.0980000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9947] _id=6ac3e7b6de269131f9aebd93 ts=2026-10-05T18:08:53.9190000Z; 71h 26m: 6aa4144c41b41dbac0c7f267.jsonl[2273] _id=6abaade3485cab4c956f9773 ts=2026-09-25T18:43:55.665Z -> 6aa4144c41b41dbac0c7f267.jsonl[2249] _id=6abaade8485cab4c956f9853 ts=2026-09-28T18:10:11.9530000Z; 24h 6m: 6aa4144c41b41dbac0c7f267.jsonl[854] _id=6abaad50485cab4c956f8097 ts=2026-09-24T18:11:39.72Z -> 6aa4144c41b41dbac0c7f267.jsonl[844] _id=6abaad51485cab4c956f80b3 ts=2026-09-25T18:17:40.614Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 532 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f267.jsonl[13958] _id=6ac66228de269131f9bb98b6 ts=2026-10-07T15:15:51.9940000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13959] _id=6ac66228de269131f9bb98b7 ts=2026-10-07T15:15:51.9940000Z; 1ms: 6aa4144c41b41dbac0c7f267.jsonl[11978] _id=6ac541bcde269131f9b6d2bb ts=2026-10-06T18:45:16.1980000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11993] _id=6ac541bcde269131f9b6d2bf ts=2026-10-06T18:45:16.1990000Z; 1ms: 6aa4144c41b41dbac0c7f267.jsonl[13732] _id=6ac65feede269131f9bb7c47 ts=2026-10-07T15:06:22.4930000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13733] _id=6ac65feede269131f9bb7c48 ts=2026-10-07T15:06:22.4940000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 164h 6m 
  - Evidence: 164h 6m: 6aa4144c41b41dbac0c7f267.jsonl[7531] _id=6abd62ad485cab4c9593c6b9 ts=2026-09-30T19:27:41.9110000Z -> 6aa4144c41b41dbac0c7f267.jsonl[14258] _id=6ac6668cde269131f9bbf8af ts=2026-10-07T15:34:36.4250000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 98h 53m 
  - Evidence: 98h 53m: 6aa4144c41b41dbac0c7f267.jsonl[9925] _id=6abe791b485cab4c95aa005e ts=2026-10-01T15:15:39.0420000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9952] _id=6ac3e7b6de269131f9aebd8b ts=2026-10-05T18:08:53.7370000Z; 71h 26m: 6aa4144c41b41dbac0c7f267.jsonl[2198] _id=6abaadde485cab4c956f96a9 ts=2026-09-25T18:41:51.681Z -> 6aa4144c41b41dbac0c7f267.jsonl[2276] _id=6abaade3485cab4c956f979b ts=2026-09-28T18:08:24.9330000Z; 24h 6m: 6aa4144c41b41dbac0c7f267.jsonl[840] _id=6abaad4f485cab4c956f8072 ts=2026-09-24T18:11:17.299Z -> 6aa4144c41b41dbac0c7f267.jsonl[858] _id=6abaad51485cab4c956f80af ts=2026-09-25T18:17:39.157Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 253 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f267.jsonl[12253] _id=6ac6596cde269131f9baf8ca ts=2026-10-07T14:38:29.5370000Z -> 6aa4144c41b41dbac0c7f267.jsonl[12254] _id=6ac6596cde269131f9baf8cb ts=2026-10-07T14:38:29.5370000Z; 0ms: 6aa4144c41b41dbac0c7f267.jsonl[12254] _id=6ac6596cde269131f9baf8cb ts=2026-10-07T14:38:29.5370000Z -> 6aa4144c41b41dbac0c7f267.jsonl[12255] _id=6ac6596cde269131f9baf8cc ts=2026-10-07T14:38:29.5370000Z; 0ms: 6aa4144c41b41dbac0c7f267.jsonl[12255] _id=6ac6596cde269131f9baf8cc ts=2026-10-07T14:38:29.5370000Z -> 6aa4144c41b41dbac0c7f267.jsonl[12256] _id=6ac6596cde269131f9baf8cd ts=2026-10-07T14:38:29.5370000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 99h 2m 
  - Evidence: 99h 2m: 6aa4144c41b41dbac0c7f267.jsonl[9930] _id=6abe7901485cab4c95a9fd04 ts=2026-10-01T15:15:13.1750000Z -> 6aa4144c41b41dbac0c7f267.jsonl[10017] _id=6ac3e9b2de269131f9aed8e9 ts=2026-10-05T18:17:22.3060000Z; 72h 3m: 6aa4144c41b41dbac0c7f267.jsonl[1976] _id=6abaadd5485cab4c956f950d ts=2026-09-25T18:34:30.202Z -> 6aa4144c41b41dbac0c7f267.jsonl[2709] _id=6abab425485cab4c95703120 ts=2026-09-28T18:38:29.8670000Z; 24h 9m: 6aa4144c41b41dbac0c7f267.jsonl[841] _id=6abaad4f485cab4c956f8075 ts=2026-09-24T18:11:25.418Z -> 6aa4144c41b41dbac0c7f267.jsonl[896] _id=6abaad56485cab4c956f8147 ts=2026-09-25T18:20:25.894Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f267.jsonl[11850] _id=6ac54047de269131f9b6a80f ts=2026-10-06T18:39:03.3900000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11858] _id=6ac54047de269131f9b6a814 ts=2026-10-06T18:39:03.3910000Z; 2ms: 6aa4144c41b41dbac0c7f267.jsonl[11815] _id=6ac53ff5de269131f9b69da3 ts=2026-10-06T18:37:41.3280000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11813] _id=6ac53ff5de269131f9b69da5 ts=2026-10-06T18:37:41.3300000Z; 4ms: 6aa4144c41b41dbac0c7f267.jsonl[3615] _id=6abc0244485cab4c9584653b ts=2026-09-29T18:24:04.1820000Z -> 6aa4144c41b41dbac0c7f267.jsonl[3630] _id=6abc0244485cab4c9584653d ts=2026-09-29T18:24:04.1860000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 98h 52m 
  - Evidence: 98h 52m: 6aa4144c41b41dbac0c7f267.jsonl[9942] _id=6abe793d485cab4c95aa08e8 ts=2026-10-01T15:16:13.2150000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9944] _id=6ac3e7b6de269131f9aebd89 ts=2026-10-05T18:08:48.5510000Z; 71h 24m: 6aa4144c41b41dbac0c7f267.jsonl[2269] _id=6abaade3485cab4c956f9781 ts=2026-09-25T18:44:10.066Z -> 6aa4144c41b41dbac0c7f267.jsonl[2282] _id=6abaade3485cab4c956f9799 ts=2026-09-28T18:08:18.8900000Z; 23h 18m: 6aa4144c41b41dbac0c7f267.jsonl[10927] _id=6ac3f20ede269131f9af6805 ts=2026-10-05T18:53:02.5560000Z -> 6aa4144c41b41dbac0c7f267.jsonl[10942] _id=6ac539bfde269131f9b62c35 ts=2026-10-06T18:11:11.5470000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f267.jsonl[12508] _id=6ac65a7bde269131f9bb07e4 ts=2026-10-07T14:43:07.4200000Z -> 6aa4144c41b41dbac0c7f267.jsonl[12518] _id=6ac65a9ade269131f9bb0a15 ts=2026-10-07T14:43:07.42Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 123h 28m 
  - Evidence: 123h 28m: 6aa4144c41b41dbac0c7f267.jsonl[9465] _id=6abe74c5485cab4c95a9801e ts=2026-10-01T14:57:07.3950000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11417] _id=6ac53d26de269131f9b660a1 ts=2026-10-06T18:25:41.5620000Z; 72h 5m: 6aa4144c41b41dbac0c7f267.jsonl[2123] _id=6abaadd5485cab4c956f94ed ts=2026-09-25T18:33:57.461Z -> 6aa4144c41b41dbac0c7f267.jsonl[2726] _id=6abab45c485cab4c957036e2 ts=2026-09-28T18:39:24.5790000Z; 47h 49m: 6aa4144c41b41dbac0c7f267.jsonl[3420] _id=6abab64d485cab4c9570683a ts=2026-09-28T18:47:40.2590000Z -> 6aa4144c41b41dbac0c7f267.jsonl[6367] _id=6abd56c9485cab4c9591d02f ts=2026-09-30T18:36:56.6790000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2467 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f267.jsonl[1065] _id=6abaad70485cab4c956f8461 ts=2026-09-25T18:28:01.302Z -> 6aa4144c41b41dbac0c7f267.jsonl[1066] _id=6abaad70485cab4c956f8463 ts=2026-09-25T18:28:01.302Z; 0ms: 6aa4144c41b41dbac0c7f267.jsonl[1066] _id=6abaad70485cab4c956f8463 ts=2026-09-25T18:28:01.302Z -> 6aa4144c41b41dbac0c7f267.jsonl[1141] _id=6abaad70485cab4c956f8465 ts=2026-09-25T18:28:01.302Z; 0ms: 6aa4144c41b41dbac0c7f267.jsonl[1099] _id=6abaad6d485cab4c956f8419 ts=2026-09-25T18:28:00.515Z -> 6aa4144c41b41dbac0c7f267.jsonl[1117] _id=6abaad6d485cab4c956f841b ts=2026-09-25T18:28:00.515Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 55m 
  - Evidence: 47h 55m: 6aa4144c41b41dbac0c7f267.jsonl[2720] _id=6abab43b485cab4c957033a3 ts=2026-09-28T18:38:51.5560000Z -> 6aa4144c41b41dbac0c7f267.jsonl[4199] _id=6abd5629485cab4c9591b681 ts=2026-09-30T18:34:17.0000000Z; 18h 11m: 6aa4144c41b41dbac0c7f267.jsonl[6333] _id=6abd569e485cab4c9591c771 ts=2026-09-30T18:36:14.8330000Z -> 6aa4144c41b41dbac0c7f267.jsonl[7730] _id=6abe5671485cab4c95a3e912 ts=2026-10-01T12:47:46.8960000Z; 2h 2m: 6aa4144c41b41dbac0c7f267.jsonl[7765] _id=6abe56b5485cab4c95a3ee53 ts=2026-10-01T12:48:54.9860000Z -> 6aa4144c41b41dbac0c7f267.jsonl[8390] _id=6abe7382485cab4c95a9708a ts=2026-10-01T14:51:46.2010000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 71h 28m 
  - Evidence: 71h 28m: 6aa4144c41b41dbac0c7f267.jsonl[2279] _id=6abaade3485cab4c956f9778 ts=2026-09-25T18:43:55.725Z -> 6aa4144c41b41dbac0c7f267.jsonl[2353] _id=6abaadfa485cab4c956f9a45 ts=2026-09-28T18:12:09.9800000Z; 42h 6m: 6aa4144c41b41dbac0c7f267.jsonl[2635] _id=6abab351485cab4c95701ff4 ts=2026-09-28T18:34:57.3450000Z -> 6aa4144c41b41dbac0c7f267.jsonl[4078] _id=6abd036f485cab4c9586631b ts=2026-09-30T12:41:19.4150000Z; 3h 9m: 6aa4144c41b41dbac0c7f267.jsonl[4929] _id=6abd264d485cab4c958bc8b1 ts=2026-09-30T15:10:05.0590000Z -> 6aa4144c41b41dbac0c7f267.jsonl[5804] _id=6abd52ab485cab4c95912933 ts=2026-09-30T18:19:23.8200000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 16m 
  - Evidence: 144h 16m: 6aa4144c41b41dbac0c7f267.jsonl[6154] _id=6abd54e0485cab4c959187a3 ts=2026-09-30T18:28:48.0750000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11995] _id=6ac541bcde269131f9b6d2b9 ts=2026-10-06T18:45:16.1740000Z; 20h 27m: 6aa4144c41b41dbac0c7f267.jsonl[12048] _id=6ac5421ade269131f9b6dfdf ts=2026-10-06T18:46:50.1470000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13913] _id=6ac661e6de269131f9bb9740 ts=2026-10-07T15:14:46.8080000Z; 5h 55m: 6aa4144c41b41dbac0c7f267.jsonl[3974] _id=6abd0167485cab4c95865773 ts=2026-09-30T12:32:40.9900000Z -> 6aa4144c41b41dbac0c7f267.jsonl[6103] _id=6abd54cb485cab4c959183e8 ts=2026-09-30T18:28:27.1620000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 13m 
  - Evidence: 144h 13m: 6aa4144c41b41dbac0c7f267.jsonl[6158] _id=6abd54e0485cab4c959187b7 ts=2026-09-30T18:28:48.1470000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11931] _id=6ac540f8de269131f9b6bc10 ts=2026-10-06T18:42:00.3100000Z; 20h 27m: 6aa4144c41b41dbac0c7f267.jsonl[12042] _id=6ac5421ade269131f9b6dfed ts=2026-10-06T18:46:50.1960000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13892] _id=6ac661b1de269131f9bb9635 ts=2026-10-07T15:13:53.8050000Z; 5h 53m: 6aa4144c41b41dbac0c7f267.jsonl[3991] _id=6abd0191485cab4c95865813 ts=2026-09-30T12:33:22.3590000Z -> 6aa4144c41b41dbac0c7f267.jsonl[6086] _id=6abd5486485cab4c95917929 ts=2026-09-30T18:27:18.0870000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.037s shown 
  - Evidence: 31ms: 6aa4144c41b41dbac0c7f267.jsonl[12040] _id=6ac5421ade269131f9b6dfe3 ts=2026-10-06T18:46:50.1650000Z -> 6aa4144c41b41dbac0c7f267.jsonl[12042] _id=6ac5421ade269131f9b6dfed ts=2026-10-06T18:46:50.1960000Z; 37ms: 6aa4144c41b41dbac0c7f267.jsonl[6153] _id=6abd54e0485cab4c959187a9 ts=2026-09-30T18:28:48.1100000Z -> 6aa4144c41b41dbac0c7f267.jsonl[6158] _id=6abd54e0485cab4c959187b7 ts=2026-09-30T18:28:48.1470000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 14m 
  - Evidence: 144h 14m: 6aa4144c41b41dbac0c7f267.jsonl[6150] _id=6abd54dc485cab4c959186cb ts=2026-09-30T18:28:44.1360000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11941] _id=6ac5412ede269131f9b6c2d3 ts=2026-10-06T18:42:54.7840000Z; 20h 27m: 6aa4144c41b41dbac0c7f267.jsonl[12047] _id=6ac54219de269131f9b6dfc5 ts=2026-10-06T18:46:49.1480000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13901] _id=6ac661dade269131f9bb96fc ts=2026-10-07T15:14:34.4760000Z; 17h 44m: 6aa4144c41b41dbac0c7f267.jsonl[3919] _id=6abc0813485cab4c9584cae7 ts=2026-09-29T18:48:51.6360000Z -> 6aa4144c41b41dbac0c7f267.jsonl[3970] _id=6abd0196485cab4c95865829 ts=2026-09-30T12:33:28.1960000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 35 interval(s) ≤ 0.018s..0.022s shown 
  - Evidence: 18ms: 6aa4144c41b41dbac0c7f267.jsonl[11976] _id=6ac541b4de269131f9b6d1ef ts=2026-10-06T18:45:08.7930000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11980] _id=6ac541b4de269131f9b6d1f3 ts=2026-10-06T18:45:08.8110000Z; 21ms: 6aa4144c41b41dbac0c7f267.jsonl[6091] _id=6abd5494485cab4c95917ad9 ts=2026-09-30T18:27:32.1380000Z -> 6aa4144c41b41dbac0c7f267.jsonl[6093] _id=6abd5494485cab4c95917ade ts=2026-09-30T18:27:32.1590000Z; 22ms: 6aa4144c41b41dbac0c7f267.jsonl[12045] _id=6ac54219de269131f9b6dfc1 ts=2026-10-06T18:46:49.1260000Z -> 6aa4144c41b41dbac0c7f267.jsonl[12047] _id=6ac54219de269131f9b6dfc5 ts=2026-10-06T18:46:49.1480000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 17m 15s 
  - Evidence: 17m 15s: 6aa4144c41b41dbac0c7f267.jsonl[13098] _id=6ac65bf3de269131f9bb20b6 ts=2026-10-07T14:49:23.6860000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13742] _id=6ac65fffde269131f9bb7da2 ts=2026-10-07T15:06:39.5250000Z; 15m 6s: 6aa4144c41b41dbac0c7f267.jsonl[13742] _id=6ac65fffde269131f9bb7da2 ts=2026-10-07T15:06:39.5250000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13971] _id=6ac66389de269131f9bba100 ts=2026-10-07T15:21:45.8500000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 99h 19m 
  - Evidence: 99h 19m: 6aa4144c41b41dbac0c7f267.jsonl[8301] _id=6abe72ed485cab4c95a9620e ts=2026-10-01T14:49:17.4660000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9950] _id=6ac3e7abde269131f9aebce5 ts=2026-10-05T18:08:42.7960000Z; 71h 45m: 6aa4144c41b41dbac0c7f267.jsonl[959] _id=6abaad60485cab4c956f8259 ts=2026-09-25T18:22:57.688Z -> 6aa4144c41b41dbac0c7f267.jsonl[2288] _id=6abaade3485cab4c956f978d ts=2026-09-28T18:08:06.4910000Z; 24h 7m: 6aa4144c41b41dbac0c7f267.jsonl[744] _id=6abaad45485cab4c956f7ebd ts=2026-09-24T18:09:46.173Z -> 6aa4144c41b41dbac0c7f267.jsonl[842] _id=6abaad50485cab4c956f80a5 ts=2026-09-25T18:17:29.201Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 98h 54m 
  - Evidence: 98h 54m: 6aa4144c41b41dbac0c7f267.jsonl[9920] _id=6abe78e0485cab4c95a9f89c ts=2026-10-01T15:14:40.8720000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9949] _id=6ac3e7aade269131f9aebce3 ts=2026-10-05T18:08:42.7950000Z; 71h 45m: 6aa4144c41b41dbac0c7f267.jsonl[958] _id=6abaad60485cab4c956f8257 ts=2026-09-25T18:22:57.671Z -> 6aa4144c41b41dbac0c7f267.jsonl[2280] _id=6abaade3485cab4c956f978b ts=2026-09-28T18:08:06.3970000Z; 24h 7m: 6aa4144c41b41dbac0c7f267.jsonl[765] _id=6abaad45485cab4c956f7eb7 ts=2026-09-24T18:09:46.148Z -> 6aa4144c41b41dbac0c7f267.jsonl[855] _id=6abaad50485cab4c956f809f ts=2026-09-25T18:17:29.169Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 99h 25m 
  - Evidence: 99h 25m: 6aa4144c41b41dbac0c7f267.jsonl[9943] _id=6abe7942485cab4c95aa09a3 ts=2026-10-01T15:16:18.0420000Z -> 6aa4144c41b41dbac0c7f267.jsonl[10561] _id=6ac3ef59de269131f9af44db ts=2026-10-05T18:41:29.4180000Z; 96h 16m: 6aa4144c41b41dbac0c7f267.jsonl[691] _id=6abaad3d485cab4c956f7d7b ts=2026-09-24T17:51:47.583Z -> 6aa4144c41b41dbac0c7f267.jsonl[2289] _id=6abaade3485cab4c956f9791 ts=2026-09-28T18:08:10.8780000Z; 24h 35m: 6aa4144c41b41dbac0c7f267.jsonl[2289] _id=6abaade3485cab4c956f9791 ts=2026-09-28T18:08:10.8780000Z -> 6aa4144c41b41dbac0c7f267.jsonl[3840] _id=6abc06e4485cab4c9584b7e9 ts=2026-09-29T18:43:48.6250000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 98h 54m 
  - Evidence: 98h 54m: 6aa4144c41b41dbac0c7f267.jsonl[9910] _id=6abe78d0485cab4c95a9f67c ts=2026-10-01T15:14:24.8100000Z -> 6aa4144c41b41dbac0c7f267.jsonl[9953] _id=6ac3e7b6de269131f9aebd91 ts=2026-10-05T18:08:53.7740000Z; 71h 25m: 6aa4144c41b41dbac0c7f267.jsonl[2263] _id=6abaade1485cab4c956f9731 ts=2026-09-25T18:43:37.403Z -> 6aa4144c41b41dbac0c7f267.jsonl[2145] _id=6abaade6485cab4c956f981f ts=2026-09-28T18:09:30.2930000Z; 47h 35m: 6aa4144c41b41dbac0c7f267.jsonl[382] _id=6abaad0a485cab4c956f764d ts=2026-09-23T18:43:36.702Z -> 6aa4144c41b41dbac0c7f267.jsonl[876] _id=6abaad53485cab4c956f80f5 ts=2026-09-25T18:19:11.137Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f267.jsonl[13982] _id=6ac66394de269131f9bba20b ts=2026-10-07T15:21:55.5150000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13983] _id=6ac66394de269131f9bba20c ts=2026-10-07T15:21:55.5150000Z; 1ms: 6aa4144c41b41dbac0c7f267.jsonl[13416] _id=6ac65d3bde269131f9bb3a45 ts=2026-10-07T14:54:50.9160000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13417] _id=6ac65d3bde269131f9bb3a46 ts=2026-10-07T14:54:50.9170000Z; 1ms: 6aa4144c41b41dbac0c7f267.jsonl[13946] _id=6ac66230de269131f9bb98ec ts=2026-10-07T15:16:00.1080000Z -> 6aa4144c41b41dbac0c7f267.jsonl[13947] _id=6ac66230de269131f9bb98ed ts=2026-10-07T15:16:00.1090000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 34m 
  - Evidence: 23h 34m: 6aa4144c41b41dbac0c7f267.jsonl[10734] _id=6ac3f05ade269131f9af5c01 ts=2026-10-05T18:45:46.3470000Z -> 6aa4144c41b41dbac0c7f267.jsonl[11229] _id=6ac53bf8de269131f9b64aef ts=2026-10-06T18:20:40.7970000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[2633] _id=6abab34f485cab4c95701fd5 ts=2026-09-28T18:34:55.2640000Z`; `6aa4144c41b41dbac0c7f267.jsonl[3196] _id=6abab61a485cab4c95705ea3 ts=2026-09-28T18:46:49.9990000Z`; `6aa4144c41b41dbac0c7f267.jsonl[4445] _id=6abd22fa485cab4c958b9245 ts=2026-09-30T14:55:54.5660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 910 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[1093] _id=6abaad73485cab4c956f84d1 ts=2026-09-25T18:26:13.918Z`; `6aa4144c41b41dbac0c7f267.jsonl[1147] _id=6abaad73485cab4c956f84d9 ts=2026-09-25T18:26:14.005Z`; `6aa4144c41b41dbac0c7f267.jsonl[1148] _id=6abaad73485cab4c956f84df ts=2026-09-25T18:26:14.173Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 189 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[932] _id=6abaad5a485cab4c956f81b9 ts=2026-09-25T18:22:32.268Z`; `6aa4144c41b41dbac0c7f267.jsonl[933] _id=6abaad5b485cab4c956f81bd ts=2026-09-25T18:22:32.268Z`; `6aa4144c41b41dbac0c7f267.jsonl[866] _id=6abaad5b485cab4c956f81c9 ts=2026-09-25T18:22:32.268Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[6158] _id=6abd54e0485cab4c959187b7 ts=2026-09-30T18:28:48.1470000Z`; `6aa4144c41b41dbac0c7f267.jsonl[12042] _id=6ac5421ade269131f9b6dfed ts=2026-10-06T18:46:50.1960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[11969] _id=6ac541afde269131f9b6d0fd ts=2026-10-06T18:45:02.4820000Z`; `6aa4144c41b41dbac0c7f267.jsonl[11965] _id=6ac541afde269131f9b6d112 ts=2026-10-06T18:45:02.7160000Z`; `6aa4144c41b41dbac0c7f267.jsonl[12045] _id=6ac54219de269131f9b6dfc1 ts=2026-10-06T18:46:49.1260000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[12523] _id=6ac65a9fde269131f9bb0a43 ts=2026-10-07T14:43:43.9450000Z`; `6aa4144c41b41dbac0c7f267.jsonl[13098] _id=6ac65bf3de269131f9bb20b6 ts=2026-10-07T14:49:23.6860000Z`; `6aa4144c41b41dbac0c7f267.jsonl[13742] _id=6ac65fffde269131f9bb7da2 ts=2026-10-07T15:06:39.5250000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[157] _id=6ab41925485cab4c954f4456 ts=2026-09-23T18:23:33.7610000Z`; `6aa4144c41b41dbac0c7f267.jsonl[2130] _id=6abaadd7485cab4c956f9553 ts=2026-09-25T18:35:16.099Z`; `6aa4144c41b41dbac0c7f267.jsonl[2261] _id=6abaade1485cab4c956f9723 ts=2026-09-25T18:43:08.912Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[446] _id=6abaad19485cab4c956f77e7 ts=?`; `6aa4144c41b41dbac0c7f267.jsonl[3929] _id=6abd0098485cab4c95865387 ts=?`; `6aa4144c41b41dbac0c7f267.jsonl[8308] _id=6abe72fd485cab4c95a96424 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 442 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[2820] _id=6abab4eb485cab4c95704855 ts=2026-09-28T18:41:46.1540000Z`; `6aa4144c41b41dbac0c7f267.jsonl[2821] _id=6abab4eb485cab4c95704859 ts=2026-09-28T18:41:46.1920000Z`; `6aa4144c41b41dbac0c7f267.jsonl[2861] _id=6abab4ed485cab4c95704893 ts=2026-09-28T18:41:48.1580000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 366 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[2739] _id=6abab45d485cab4c957036f1 ts=2026-09-28T18:39:24.8030000Z`; `6aa4144c41b41dbac0c7f267.jsonl[2741] _id=6abab45e485cab4c95703725 ts=2026-09-28T18:39:24.8950000Z`; `6aa4144c41b41dbac0c7f267.jsonl[2772] _id=6abab493485cab4c95703efb ts=2026-09-28T18:40:18.6350000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[1111] _id=6abaad6b485cab4c956f83e7 ts=2026-09-25T18:26:56.951Z`; `6aa4144c41b41dbac0c7f267.jsonl[2270] _id=6abaade2485cab4c956f9753 ts=2026-09-25T18:43:52.824Z`; `6aa4144c41b41dbac0c7f267.jsonl[2271] _id=6abaade2485cab4c956f975f ts=2026-09-25T18:43:55.458Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[11974] _id=6ac541afde269131f9b6d124 ts=2026-10-06T18:45:02.9990000Z`; `6aa4144c41b41dbac0c7f267.jsonl[11975] _id=6ac541afde269131f9b6d127 ts=2026-10-06T18:45:03.2340000Z`; `6aa4144c41b41dbac0c7f267.jsonl[11973] _id=6ac541b0de269131f9b6d12b ts=2026-10-06T18:45:03.7180000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 392 start, 384 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 101 unmatched 'BecameCameraCentered' (totals: 739 open, 1548 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 59 unmatched 'BecameVisible' (totals: 782 open, 912 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'MapOpenEvent' (totals: 17 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationNodeHoverStart' (totals: 60 open, 60 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 31 unmatched 'questActiveEvent' (totals: 58 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 283 of 14254 adjacent _id pairs reverse in client time; worst 130.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f267.jsonl[1146] _id=6abaad73485cab4c956f84ca ts=2026-09-25T18:28:23.957Z`; `6aa4144c41b41dbac0c7f267.jsonl[1093] _id=6abaad73485cab4c956f84d1 ts=2026-09-25T18:26:13.918Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -430393.44s, max +3.81s over 14255 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f267\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4719 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1461); Unit 4 Dev - Dungeon (999); Unit 1 Dev (658); Unit 4 Dev (525); Unit 3 Dungeon Dev (340); Unit 2 Prod (Refactor) (327); Unit 5 Dev - Dungeon (242); Unit 5 Dev (86); Unit 4 Dev - Anderson Base (81)
- **Intervals:** median 1.01s (p5 0.04s / p95 17.09s, n=4718)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4719/4719 records)
    "pressed"  x4719
data.actionType  (string, 4719/4719 records)
    "Move"  x2882
    "Interact"  x985
    "Jump"  x610
    "Hoverboard"  x99
    "Sprint"  x74
    "Ascend"  x58
    "Map"  x6
    "Descend"  x4
    "Pause"  x1
data.key  (string, 4719/4719 records, 4 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4719/4719 records)
    "Player"  x3538
    "Drone"  x1181
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3981 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 4 Dev (1566); Unit 2 Prod (Refactor) (1455); Unit 5 Dev - Dungeon (686); Unit 3 Dungeon Dev (274)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.51s, n=3980)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3981/3981 records)
    "BecameCameraUncentered"  x1548
    "BecameInvisible"  x912
    "BecameVisible"  x782
    "BecameCameraCentered"  x739
data.pieceId  (string, 3981/3981 records)
    29 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3981/3981 records)
    1806 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2556 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (487); Unit 4 Dev - Dungeon (460); Unit 1 Dev (430); Unit 2 Prod (Refactor) (380); Unit 4 Dev (269); Unit 3 Dungeon Dev (190); Unit 5 Dev - Dungeon (134); Unit 5 Dev (132); Unit 4 Dev - Anderson Base (74)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.04s, n=2543)
- **Fields under `data`:**

```text
data.position  (object, 2556/2556 records)
data.position.x  (number, 2556/2556 records)
    numeric range -681.335 .. 1553.23 (786 unique)
data.position.y  (number, 2556/2556 records)
    numeric range -113.891 .. 222.405 (608 unique)
data.position.z  (number, 2556/2556 records)
    numeric range -1038.51 .. 1789.16 (785 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1897 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (418); Unit 2 Prod (Refactor) (318); Unit 5 Dev (246); Unit 4 Dev (237); Unit 1 Dev (187); Unit 4 Dev - Dungeon (180); Unit 3 Dungeon Dev (132); Unit 5 Dev - Dungeon (94); Unit 4 Dev - Anderson Base (85)
- **eventKey:** present on 1121 of 1897 records
- **Intervals:** median 4.86s (p5 0.00s / p95 55.24s, n=1896)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1121; [conversationId, dialogueEventType] x776
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1897/1897 records)
    numeric range 10 .. 118 (44 unique)
data.dialogueEventType  (string, 1897/1897 records)
    "DialogueNodeEvent"  x1121
    "DialogueStartEvent"  x392
    "DialogueFinishEvent"  x384
data.nodeId  (number, 1121/1897 records)
    numeric range 0 .. 279 (203 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 457 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (197); Unit 1 Dev (77); Unit 3 Dungeon Dev (51); Unit 2 Prod (Refactor) (41); Unit 4 Dev (30); Unit 5 Dev - Dungeon (26); Unit 3 Dev (16); Unit 5 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 7.49s (p5 0.20s / p95 417.59s, n=456)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 457/457 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 457/457 records)
    82 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 136 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (57); Unit 3 Dev (49); Unit 1 Dev (16); Unit 5 Dev (14)
- **Intervals:** median 0.29s (p5 0.03s / p95 19.72s, n=135)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 136/136 records)
    "argumentationNodeHoverEnd"  x60
    "argumentationNodeHoverStart"  x60
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 136/136 records)
    "Unit 4 - Flooding"  x57
    "Unit 3 - Pollution Upstream"  x49
    "Unit 5"  x14
    "Unit 1 - Freshwater"  x10
    "Unit 1 - Argumentation Tutorial"  x6
data.nodeName  (string, 136/136 records)
    "I"  x39
    "4"  x18
    "A"  x18
    "2"  x10
    "II"  x10
    "3"  x9
    "C"  x8
    "D"  x8
    "B"  x6
    "1"  x5
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 93 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (20); Unit 1 Dev (18); Unit 3 Dev (13); Unit 2 Prod (Refactor) (12); Unit 4 Dev (9); Unit 5 Dev (9); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 93 of 93 records
- **Intervals:** median 267.24s (p5 0.00s / p95 77260.64s, n=92)
- **`data` key-set variants:** [questEventType, questID, questName] x58; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 93/93 records)
    "questActiveEvent"  x58
    "questFinishEvent"  x35
data.questID  (string, 93/93 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 93/93 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/93 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 86 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (66); Unit 3 Dev (12); Unit 2 Prod (Refactor) (8)
- **Intervals:** median 0.70s (p5 0.18s / p95 31.69s, n=85)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x78; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/86 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/86 records)
    "Unit 4 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
data.actionType  (string, 78/86 records)
    "RightDrag"  x42
    "LeftDrag"  x36
data.currentSoilType  (string, 78/86 records)
    "CLAY"  x17
    "CLAYSAND"  x16
    "SAND"  x15
    "CLAYROCK"  x12
    "SANDGRAVEL"  x11
    "GRAVEL"  x4
    "BEDROCK"  x3
data.isCorrectSelection  (string, 78/86 records)
    "false"  x60
    "true"  x18
data.waterLevelStatus  (string, 78/86 records)
    "Proper"  x39
    "TooLow"  x27
    "TooHigh"  x12
data.waterRetentionChange  (string, 78/86 records)
    "Decrease"  x30
    "Increase"  x30
    "NoChange"  x18
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 67 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (34); Unit 2 Prod (Refactor) (33)
- **Intervals:** median 3.12s (p5 0.49s / p95 6425.17s, n=66)
- **`data` key-set variants:** [actionType, featureUsed] x29; [actionType, featureUsed, location] x24; [actionType, featureUsed, legendName] x14
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 67/67 records)
    "WaypointMoveEvent"  x18
    "MapOpenEvent"  x17
    "Selected"  x13
    "MapCloseEvent"  x12
    "WaypointSetEvent"  x6
    "Unselected"  x1
data.featureUsed  (string, 67/67 records)
    "Map"  x29
    "Waypoint"  x24
    "Legend"  x14
data.legendName  (string, 14/67 records)
    "Water"  x3
    "240 ft"  x2
    "270 ft"  x2
    "0 ft"  x1
    "180 ft"  x1
    "30 ft"  x1
    "300 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
    "90 ft"  x1
data.location  (object, 24/67 records)
data.location.x  (number, 24/67 records)
    numeric range -560.09 .. 165.91 (24 unique)
data.location.y  (number, 24/67 records)
    numeric range -321.5 .. 236.5 (23 unique)
data.location.z  (number, 24/67 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 52 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (52)
- **Intervals:** median 2.47s (p5 0.25s / p95 342.72s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "ChangeCanister"  x52
data.canisterType  (string, 52/52 records)
    "Clay"  x17
    "Bedrock"  x16
    "Sand"  x14
    "Gravel"  x5
data.floor  (string, 52/52 records)
    "5"  x28
    "3"  x19
    "4"  x5
data.machine  (string, 52/52 records)
    "1"  x51
    "2"  x1
data.row  (string, 52/52 records)
    "TopRow"  x41
    "BottomRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 47 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (24); Unit 1 Dev (7); Unit 3 Dev (4); Unit 4 Dev - Dungeon (3); Unit 5 Dev (3); Transition (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 703.38s (p5 7.45s / p95 86528.40s, n=46)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 47/47 records)
    true  x47
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 33 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 1 Dev (7); Unit 4 Dev (6); MainMenu (4); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 4 Dev - Dungeon (4); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1198.79s (p5 8.18s / p95 164014.74s, n=32)
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "DebugMenuStateChanged"  x33
data.isOpened  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 31 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (31)
- **Intervals:** median 15.28s (p5 0.74s / p95 137.62s, n=30)
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "On"  x21
    "Off"  x10
data.floor  (string, 31/31 records)
    "4"  x15
    "3"  x7
    "2"  x5
    "1"  x4
data.machineNumber  (string, 31/31 records)
    "One"  x30
    "Two"  x1
data.machineType  (string, 31/31 records)
    "Condenser"  x20
    "Evaporator"  x7
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
    "DualChamber_Evaporator"  x1
data.room  (string, 31/31 records)
    "2"  x12
    "3"  x9
    "1"  x8
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 26 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (5); Unit 4 Dev - Dungeon (4); Transition (3); Unit 5 Dev (3); Unit 4 Dev (2); Unit 3 Dungeon Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 2210.53s (p5 8.83s / p95 294974.19s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 24 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (24)
- **Intervals:** median 7477.68s (p5 324.12s / p95 241164.23s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 11 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (7); Unit 3 Dev (2); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 23.26s (p5 2.56s / p95 318817.95s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "submitAnswerEvent"  x11
data.answerSubmitted  (string, 11/11 records, 1 empty-string)
    "A,C,D,2,I"  x6
    ""  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "C,D,3,II"  x1
    "I"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 4 - Flooding"  x7
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 71.55s (p5 0.03s / p95 318686.31s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 11/11 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (8)
- **Intervals:** median 2.82s (p5 1.77s / p95 10629.51s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 8 empty-string)
    ""  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 10.74s (p5 1.32s / p95 38.83s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 3 empty-string)
    "cameraPlaced"  x4
    ""  x3
data.boxId  (string, 7/7 records)
    "0"  x3
    "1"  x2
    "2"  x2
data.soilType  (string, 7/7 records)
    "Clay"  x5
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 0.91s (p5 0.76s / p95 1.77s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted Out"  x1
data.featureUsed  (string, 6/6 records)
    "ExtraCovering"  x2
    "RoofStyle"  x2
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records)
    "Cold"  x1
    "Covered"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 906.33s (p5 396.40s / p95 1022.89s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x1
    "The root document of this element is not valid for pointer lock."  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x1
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit1"  x1
    "unit2"  x1
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 590814.51s (p5 590814.51s / p95 590814.51s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 1 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 1/1 records)
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 1/1 records)
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (8 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (13x); "Unselected" (1x); "WaypointMoveEvent" (18x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (14x); "Waypoint" (24x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (16x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*