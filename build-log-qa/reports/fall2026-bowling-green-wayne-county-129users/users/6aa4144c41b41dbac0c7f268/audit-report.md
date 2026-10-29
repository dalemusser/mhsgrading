# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f268

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f268
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f268.jsonl
- **Records:** 12156 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f268
- **Time span:** 2026-09-23T18:19:03.270000+00:00 .. 2026-10-07T18:50:02.897000+00:00 (336h 30m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f268\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 12156 records, 11 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 94 INFO, 0 NOT_TESTED, 89 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4267 | 35.1 | 1 | 9 | 0 | 2026-09-23T18:24:37.874000+00:00 | 2026-10-07T18:49:57.239000+00:00 | 336h 25m |
| PuzzlePieceVisibleEvent | 3126 | 25.72 | 1 | 4 | 0 | 2026-09-24T18:11:50.134000+00:00 | 2026-10-07T14:57:59.794000+00:00 | 308h 46m |
| DialogueEvent | 1864 | 15.33 | 1 | 9 | 1136 | 2026-09-23T18:19:34.408000+00:00 | 2026-10-07T18:50:01.090000+00:00 | 336h 30m |
| PlayerPositionEvent | 1788 | 14.71 | 1 | 9 | 0 | 2026-09-23T18:19:12.737000+00:00 | 2026-10-07T18:50:00.066000+00:00 | 336h 30m |
| argumentationNodeEvent | 391 | 3.22 | 1 | 4 | 0 | 2026-09-24T17:58:34.046000+00:00 | 2026-10-07T18:47:33.940000+00:00 | 312h 48m |
| ObjectInterEvent | 314 | 2.58 | 1 | 9 | 0 | 2026-09-23T18:26:16.823000+00:00 | 2026-10-07T18:44:33.422000+00:00 | 336h 18m |
| questEvent | 76 | 0.63 | 1 | 9 | 76 | 2026-09-23T18:19:34.386000+00:00 | 2026-10-07T18:48:42.301000+00:00 | 336h 29m |
| TopographicMapEvent | 54 | 0.44 | 1 | 2 | 0 | 2026-09-24T18:12:21.974000+00:00 | 2026-10-05T18:19:28.406000+00:00 | 264h 7m |
| gameWindowFocusEvent | 42 | 0.35 | 1 | 9 | 0 | 2026-09-23T18:19:03.270000+00:00 | 2026-10-07T18:49:55.850000+00:00 | 336h 30m |
| Soil Key Puzzle | 36 | 0.3 | 1 | 2 | 0 | 2026-09-30T18:34:50.362000+00:00 | 2026-10-05T18:36:21.415000+00:00 | 120h 1m |
| gameWindowUnfocusEvent | 33 | 0.27 | 1 | 8 | 0 | 2026-09-23T18:21:00.897000+00:00 | 2026-10-07T18:50:02.897000+00:00 | 336h 29m |
| WaterChamberEvent | 32 | 0.26 | 1 | 1 | 0 | 2026-10-07T14:56:57.793000+00:00 | 2026-10-07T15:07:43.957000+00:00 | 10m 46s |
| argumentationAnswerEvent | 31 | 0.26 | 1 | 4 | 0 | 2026-09-24T18:01:52.929000+00:00 | 2026-10-07T18:47:36.395000+00:00 | 312h 45m |
| soilMachine | 27 | 0.22 | 1 | 1 | 0 | 2026-10-06T18:17:21.564000+00:00 | 2026-10-06T18:30:34.165000+00:00 | 13m 12s |
| DEBUGMenu | 24 | 0.2 | 1 | 9 | 0 | 2026-09-23T18:19:12.725000+00:00 | 2026-10-07T18:42:31.364000+00:00 | 336h 23m |
| gameStartEvent | 16 | 0.13 | 1 | 1 | 0 | 2026-09-23T18:19:03.271000+00:00 | 2026-10-07T18:42:31.484000+00:00 | 336h 23m |
| argumentationEvent | 12 | 0.1 | 1 | 4 | 0 | 2026-09-24T17:59:46.223000+00:00 | 2026-10-07T18:47:36.429000+00:00 | 312h 47m |
| TerasGardenBox | 11 | 0.09 | 1 | 1 | 0 | 2026-10-07T14:41:55.731000+00:00 | 2026-10-07T14:43:09.235000+00:00 | 1m 13s |
| argumentationToolEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-09-24T17:59:42.148000+00:00 | 2026-09-30T18:25:33.575000+00:00 | 144h 25m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-24T18:05:46.697000+00:00 | 2026-10-07T14:52:20.762000+00:00 | 308h 46m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-07T14:52:54.162000+00:00 | 2026-10-07T18:42:38.828000+00:00 | 3h 49m |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 555797.032s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.761s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 9.087s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 128.544s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 6892.333s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 73930.596s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 377.671s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 756.904s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.94s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to Insert 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 Prod (Refactor) 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointMoveEvent; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 300 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 31 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,3,I; A,5,II; A,C,2,II; B,A,1,I; B,D,C,2,II; C,2,II; C,A,2,II; C,B,2,II; D,2,II; D,3,II; D,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 24; 25; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; Investigate the Temple; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.4x vs baseline. 
  - Observed: 27 records 
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
  - Observed: 29 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[170] _id=6ab41a4b485cab4c954f4ed2 ts=2026-09-23T18:28:27.3030000Z`; `6aa4144c41b41dbac0c7f268.jsonl[263] _id=6ab41b66485cab4c954f567c ts=2026-09-23T18:33:09.9670000Z`; `6aa4144c41b41dbac0c7f268.jsonl[294] _id=6ab41c4b485cab4c954f5db3 ts=2026-09-23T18:36:59.5090000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[16] _id=6ab41817485cab4c954f3aac ts=2026-09-23T18:19:03.2710000Z`; `6aa4144c41b41dbac0c7f268.jsonl[456] _id=6ab560be485cab4c955379d9 ts=2026-09-24T17:41:18.2790000Z`; `6aa4144c41b41dbac0c7f268.jsonl[930] _id=6ab566ce485cab4c95540f6c ts=2026-09-24T18:07:10.1720000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 42 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 42} 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[15] _id=6ab41817485cab4c954f3aaa ts=2026-09-23T18:19:03.2700000Z`; `6aa4144c41b41dbac0c7f268.jsonl[27] _id=6ab4189e485cab4c954f3efd ts=2026-09-23T18:21:18.4240000Z`; `6aa4144c41b41dbac0c7f268.jsonl[41] _id=6ab418f0485cab4c954f41f6 ts=2026-09-23T18:22:40.1260000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 33 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 33} 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[24] _id=6ab4188c485cab4c954f3e2e ts=2026-09-23T18:21:00.8970000Z`; `6aa4144c41b41dbac0c7f268.jsonl[37] _id=6ab418ef485cab4c954f41f4 ts=2026-09-23T18:22:40.0100000Z`; `6aa4144c41b41dbac0c7f268.jsonl[188] _id=6ab41a91485cab4c954f5060 ts=2026-09-23T18:29:37.7800000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 19 of 54 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1085] _id=6ab56805485cab4c95542276 ts=2026-09-24T18:12:21.9740000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1096] _id=6ab56834485cab4c9554242c ts=2026-09-24T18:13:08.9310000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1202] _id=6ab6b8cc485cab4c955db035 ts=2026-09-25T18:09:17.4750000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4266 | 0.0 | 0.847 | 283.9 | 12.171 | 355880.069 | 0.21 | 122 | 9 |
| PuzzlePieceVisibleEvent | 3125 | 0.0 | 0.029 | 355.702 | 1.349 | 433012.2 | 0.17 | 1876 | 7 |
| DialogueEvent | 1863 | 0.0 | 4.233 | 650.256 | 36.04 | 355954.102 | 0.09 | 520 | 9 |
| PlayerPositionEvent | 1774 | 9.829 | 10.0 | 586.618 | 10.019 | 355863.942 | 0.1 | 0 | 8 |
| argumentationNodeEvent | 390 | 0.005 | 0.38 | 2887.538 | 6.1 | 519808.624 | 0.02 | 76 | 3 |
| ObjectInterEvent | 313 | 0.001 | 8.341 | 3868.04 | 332.71 | 355986.975 | 0.02 | 4 | 10 |
| questEvent | 75 | 0.0 | 212.566 | 16151.306 | 84738.611 | 356293.774 | 0.0 | 15 | 13 |
| TopographicMapEvent | 53 | 0.417 | 2.634 | 17940.121 | 35152.598 | 604800.392 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 41 | 5.512 | 377.671 | 29547.624 | 171761.999 | 356309.6 | 0.0 | 0 | 16 |
| Soil Key Puzzle | 35 | 0.311 | 1.005 | 12345.459 | 11.849 | 432016.502 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 32 | 4.93 | 756.904 | 37854.438 | 210272.992 | 357041.719 | 0.0 | 0 | 16 |
| WaterChamberEvent | 31 | 0.862 | 8.761 | 20.844 | 65.556 | 84.127 | 2.88 | 0 | 0 |
| argumentationAnswerEvent | 30 | 0.42 | 9.087 | 37531.449 | 324549.013 | 519835.865 | 0.0 | 0 | 3 |
| soilMachine | 26 | 0.581 | 2.94 | 30.485 | 115.137 | 253.638 | 1.97 | 0 | 0 |
| DEBUGMenu | 23 | 4.798 | 1504.587 | 52652.115 | 250366.795 | 356294.638 | 0.0 | 0 | 16 |
| gameStartEvent | 15 | 161.473 | 73930.596 | 80733.881 | 288217.862 | 356309.6 | 0.0 | 0 | 12 |
| argumentationEvent | 11 | 0.026 | 68.057 | 102370.019 | 519590.84 | 519788.428 | 0.0 | 2 | 3 |
| TerasGardenBox | 10 | 0.735 | 3.394 | 7.35 | 21.556 | 26.756 | 8.16 | 0 | 0 |
| argumentationToolEvent | 3 | 4.044 | 128.544 | 173317.142 | 467849.809 | 519818.839 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 159762.908 | 555797.032 | 555797.032 | 912227.745 | 951831.157 | 0.0 | 0 | 2 |
| chatEvent | 2 | 948.372 | 6892.333 | 6892.333 | 12241.898 | 12836.294 | 0.01 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 11 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[10304] _id=6ac5406ede269131f9b6ad7d ts=2026-10-06T18:39:42.2320000Z == 6aa4144c41b41dbac0c7f268.jsonl[10301] _id=6ac5406ede269131f9b6ad7f ts=2026-10-06T18:39:42.2320000Z`; `6aa4144c41b41dbac0c7f268.jsonl[10821] _id=6ac6596dde269131f9baf8ec ts=2026-10-07T14:38:35.3740000Z == 6aa4144c41b41dbac0c7f268.jsonl[10822] _id=6ac6596dde269131f9baf8ed ts=2026-10-07T14:38:35.3740000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 128 group(s), 173 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1051] _id=6ab567e8485cab4c95542140 ts=2026-09-24T18:11:50.6500000Z == 6aa4144c41b41dbac0c7f268.jsonl[1064] _id=6ab567e8485cab4c95542142 ts=2026-09-24T18:11:50.6500000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1067] _id=6ab567e9485cab4c95542150 ts=2026-09-24T18:11:51.2670000Z == 6aa4144c41b41dbac0c7f268.jsonl[951] _id=6ab567e9485cab4c95542152 ts=2026-09-24T18:11:51.2670000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1076] _id=6ab567e9485cab4c9554215c ts=2026-09-24T18:11:51.2990000Z == 6aa4144c41b41dbac0c7f268.jsonl[1070] _id=6ab567e9485cab4c9554215e ts=2026-09-24T18:11:51.2990000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[12117] _id=6ac6940ade269131f9be1c89 ts=2026-10-07T18:48:42.3010000Z == 6aa4144c41b41dbac0c7f268.jsonl[12118] _id=6ac6940ade269131f9be1c8a ts=2026-10-07T18:48:42.3010000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4144c41b41dbac0c7f268.jsonl[122] _id=6ab419c8485cab4c954f4a9c ts=2026-09-23T18:26:16.8230000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[123] _id=6ab419c8485cab4c954f4a9e ts=2026-09-23T18:26:16.8280000Z`; `708ms: 6aa4144c41b41dbac0c7f268.jsonl[343] _id=6ab41c66485cab4c954f5eb7 ts=2026-09-23T18:37:26.4310000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[344] _id=6ab41c67485cab4c954f5ebd ts=2026-09-23T18:37:27.1390000Z`; `554ms: 6aa4144c41b41dbac0c7f268.jsonl[344] _id=6ab41c67485cab4c954f5ebd ts=2026-09-23T18:37:27.1390000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[345] _id=6ab41c67485cab4c954f5ec9 ts=2026-09-23T18:37:27.6930000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 485 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa4144c41b41dbac0c7f268.jsonl[1061] _id=6ab567e7485cab4c9554212e ts=2026-09-24T18:11:50.5700000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[1049] _id=6ab567e7485cab4c95542132 ts=2026-09-24T18:11:50.5870000Z`; `7ms: 6aa4144c41b41dbac0c7f268.jsonl[1074] _id=6ab567e9485cab4c9554214e ts=2026-09-24T18:11:51.2600000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[1067] _id=6ab567e9485cab4c95542150 ts=2026-09-24T18:11:51.2670000Z`; `17ms: 6aa4144c41b41dbac0c7f268.jsonl[1077] _id=6ab567e9485cab4c95542162 ts=2026-09-24T18:11:51.3300000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[1071] _id=6ab567e9485cab4c95542164 ts=2026-09-24T18:11:51.3470000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `735ms: 6aa4144c41b41dbac0c7f268.jsonl[10915] _id=6ac65a4ade269131f9bb050f ts=2026-10-07T14:42:18.6990000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[10916] _id=6ac65a4bde269131f9bb0515 ts=2026-10-07T14:42:19.4340000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `606ms: 6aa4144c41b41dbac0c7f268.jsonl[10668] _id=6ac5422dde269131f9b6e1fb ts=2026-10-06T18:47:09.4700000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[10673] _id=6ac5422ede269131f9b6e20e ts=2026-10-06T18:47:10.0760000Z`; `800ms: 6aa4144c41b41dbac0c7f268.jsonl[10673] _id=6ac5422ede269131f9b6e20e ts=2026-10-06T18:47:10.0760000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[10674] _id=6ac5422ede269131f9b6e21f ts=2026-10-06T18:47:10.8760000Z`; `910ms: 6aa4144c41b41dbac0c7f268.jsonl[10733] _id=6ac54265de269131f9b6e9eb ts=2026-10-06T18:48:05.5480000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[10729] _id=6ac54266de269131f9b6ea03 ts=2026-10-06T18:48:06.4580000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6aa4144c41b41dbac0c7f268.jsonl[6568] _id=6abd54bc485cab4c95918183 ts=2026-09-30T18:28:12.4970000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[6569] _id=6abd54bc485cab4c95918193 ts=2026-09-30T18:28:12.5270000Z`; `26ms: 6aa4144c41b41dbac0c7f268.jsonl[10734] _id=6ac54269de269131f9b6ea4e ts=2026-10-06T18:48:09.2520000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[10736] _id=6ac54269de269131f9b6ea60 ts=2026-10-06T18:48:09.2780000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 57 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `509ms: 6aa4144c41b41dbac0c7f268.jsonl[6387] _id=6abd5426485cab4c95916ab9 ts=2026-09-30T18:25:42.3690000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[6389] _id=6abd5426485cab4c95916ad3 ts=2026-09-30T18:25:42.8780000Z`; `444ms: 6aa4144c41b41dbac0c7f268.jsonl[6388] _id=6abd5426485cab4c95916abf ts=2026-09-30T18:25:42.5220000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[6390] _id=6abd5426485cab4c95916ad9 ts=2026-09-30T18:25:42.9660000Z`; `431ms: 6aa4144c41b41dbac0c7f268.jsonl[6395] _id=6abd542a485cab4c95916b3f ts=2026-09-30T18:25:46.0640000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[6396] _id=6abd542a485cab4c95916b5b ts=2026-09-30T18:25:46.4950000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `899ms: 6aa4144c41b41dbac0c7f268.jsonl[9398] _id=6ac53b32de269131f9b63f7d ts=2026-10-06T18:17:22.2480000Z ~ 6aa4144c41b41dbac0c7f268.jsonl[9227] _id=6ac53b33de269131f9b63f89 ts=2026-10-06T18:17:23.1470000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 98h 58m 
  - Evidence: 98h 58m: 6aa4144c41b41dbac0c7f268.jsonl[6995] _id=6abe7786485cab4c95a9c92c ts=2026-10-01T15:08:54.7580000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7476] _id=6ac3e74dde269131f9aeb62d ts=2026-10-05T18:07:09.3960000Z; 71h 57m: 6aa4144c41b41dbac0c7f268.jsonl[1112] _id=6ab6b83a485cab4c955da5f5 ts=2026-09-25T18:06:37.1100000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3738] _id=6abaac0c485cab4c956f6775 ts=2026-09-28T18:03:56.9680000Z; 47h 51m: 6aa4144c41b41dbac0c7f268.jsonl[3996] _id=6abaae26485cab4c956f9ee7 ts=2026-09-28T18:12:54.9810000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5690] _id=6abd4f3c485cab4c9590d681 ts=2026-09-30T18:04:44.2070000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 98h 52m 
  - Evidence: 98h 52m: 6aa4144c41b41dbac0c7f268.jsonl[7354] _id=6abe78fa485cab4c95a9fbe8 ts=2026-10-01T15:15:05.9830000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7553] _id=6ac3e76cde269131f9aeb84f ts=2026-10-05T18:07:40.0850000Z; 71h 21m: 6aa4144c41b41dbac0c7f268.jsonl[3718] _id=6ab6c09c485cab4c955e6701 ts=2026-09-25T18:42:36.1500000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3731] _id=6abaac14485cab4c956f679a ts=2026-09-28T18:04:03.5950000Z; 47h 16m: 6aa4144c41b41dbac0c7f268.jsonl[5677] _id=6abab658485cab4c95706b28 ts=2026-09-28T18:47:52.4260000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5695] _id=6abd4f3e485cab4c9590d695 ts=2026-09-30T18:04:46.1920000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 520 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10560] _id=6ac541c6de269131f9b6d3a5 ts=2026-10-06T18:45:26.4870000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10557] _id=6ac541c6de269131f9b6d3a7 ts=2026-10-06T18:45:26.4870000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[11774] _id=6ac6606ade269131f9bb852d ts=2026-10-07T15:08:26.2780000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11775] _id=6ac6606ade269131f9bb852e ts=2026-10-07T15:08:26.2780000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[12036] _id=6ac693bdde269131f9be0fc2 ts=2026-10-07T18:47:25.5500000Z -> 6aa4144c41b41dbac0c7f268.jsonl[12037] _id=6ac693bdde269131f9be0fc3 ts=2026-10-07T18:47:25.5500000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 264h 23m 
  - Evidence: 264h 23m: 6aa4144c41b41dbac0c7f268.jsonl[927] _id=6ab5667a485cab4c955406c0 ts=2026-09-24T18:05:46.6970000Z -> 6aa4144c41b41dbac0c7f268.jsonl[8179] _id=6ac3ec91de269131f9af0d91 ts=2026-10-05T18:29:37.8540000Z; 44h 22m: 6aa4144c41b41dbac0c7f268.jsonl[8179] _id=6ac3ec91de269131f9af0d91 ts=2026-10-05T18:29:37.8540000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11117] _id=6ac65ca4de269131f9bb2f97 ts=2026-10-07T14:52:20.7620000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 98h 51m 
  - Evidence: 98h 51m: 6aa4144c41b41dbac0c7f268.jsonl[7466] _id=6abe7932485cab4c95aa05c8 ts=2026-10-01T15:16:02.6660000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7493] _id=6ac3e75ade269131f9aeb6c1 ts=2026-10-05T18:07:22.7350000Z; 71h 21m: 6aa4144c41b41dbac0c7f268.jsonl[3726] _id=6ab6c0b3485cab4c955e6773 ts=2026-09-25T18:42:59.4220000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3742] _id=6abaac20485cab4c956f6811 ts=2026-09-28T18:04:16.1110000Z; 47h 25m: 6aa4144c41b41dbac0c7f268.jsonl[5640] _id=6abab5bf485cab4c95705799 ts=2026-09-28T18:45:19.2740000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5718] _id=6abd50ac485cab4c9590eccb ts=2026-09-30T18:10:52.9910000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 122 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10304] _id=6ac5406ede269131f9b6ad7d ts=2026-10-06T18:39:42.2320000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10301] _id=6ac5406ede269131f9b6ad7f ts=2026-10-06T18:39:42.2320000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10821] _id=6ac6596dde269131f9baf8ec ts=2026-10-07T14:38:35.3740000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10822] _id=6ac6596dde269131f9baf8ed ts=2026-10-07T14:38:35.3740000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10822] _id=6ac6596dde269131f9baf8ed ts=2026-10-07T14:38:35.3740000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10824] _id=6ac6596dde269131f9baf8ee ts=2026-10-07T14:38:35.3740000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 98h 53m 
  - Evidence: 98h 53m: 6aa4144c41b41dbac0c7f268.jsonl[7338] _id=6abe78d0485cab4c95a9f674 ts=2026-10-01T15:14:24.6780000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7526] _id=6ac3e763de269131f9aeb751 ts=2026-10-05T18:07:31.6530000Z; 71h 59m: 6aa4144c41b41dbac0c7f268.jsonl[3264] _id=6ab6bb66485cab4c955e09fd ts=2026-09-25T18:20:22.4750000Z -> 6aa4144c41b41dbac0c7f268.jsonl[4070] _id=6abaafb1485cab4c956fd217 ts=2026-09-28T18:19:29.1720000Z; 47h 45m: 6aa4144c41b41dbac0c7f268.jsonl[4292] _id=6abab1a6485cab4c9570022d ts=2026-09-28T18:27:50.7150000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5849] _id=6abd5156485cab4c9590febf ts=2026-09-30T18:13:42.0190000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f268.jsonl[10362] _id=6ac540c6de269131f9b6b70b ts=2026-10-06T18:41:10.5270000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10370] _id=6ac540c6de269131f9b6b711 ts=2026-10-06T18:41:10.5280000Z; 2ms: 6aa4144c41b41dbac0c7f268.jsonl[10431] _id=6ac5410fde269131f9b6befd ts=2026-10-06T18:42:23.2910000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10432] _id=6ac5410fde269131f9b6bf01 ts=2026-10-06T18:42:23.2930000Z; 4ms: 6aa4144c41b41dbac0c7f268.jsonl[484] _id=6ab56129485cab4c95537f2d ts=2026-09-24T17:43:05.1960000Z -> 6aa4144c41b41dbac0c7f268.jsonl[485] _id=6ab56129485cab4c95537f31 ts=2026-09-24T17:43:05.2000000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 98h 51m 
  - Evidence: 98h 51m: 6aa4144c41b41dbac0c7f268.jsonl[7468] _id=6abe7935485cab4c95aa06b2 ts=2026-10-01T15:16:05.4630000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7477] _id=6ac3e751de269131f9aeb66d ts=2026-10-05T18:07:09.4050000Z; 71h 20m: 6aa4144c41b41dbac0c7f268.jsonl[3729] _id=6ab6c0cf485cab4c955e6836 ts=2026-09-25T18:43:28.0090000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3739] _id=6abaac14485cab4c956f6795 ts=2026-09-28T18:03:56.9770000Z; 23h 52m: 6aa4144c41b41dbac0c7f268.jsonl[1105] _id=6ab5685e485cab4c955424e4 ts=2026-09-24T18:13:51.0570000Z -> 6aa4144c41b41dbac0c7f268.jsonl[1117] _id=6ab6b83a485cab4c955da5f7 ts=2026-09-25T18:06:37.1150000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 16m 
  - Evidence: 120h 16m: 6aa4144c41b41dbac0c7f268.jsonl[3250] _id=6ab6bb4a485cab4c955e0533 ts=2026-09-25T18:19:53.1490000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6815] _id=6abd56be485cab4c9591cdc9 ts=2026-09-30T18:36:45.3490000Z; 98h 51m: 6aa4144c41b41dbac0c7f268.jsonl[7451] _id=6abe7928485cab4c95aa03c8 ts=2026-10-01T15:15:49.6320000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7475] _id=6ac3e752de269131f9aeb68a ts=2026-10-05T18:07:11.6430000Z; 23h 56m: 6aa4144c41b41dbac0c7f268.jsonl[1080] _id=6ab567ea485cab4c9554216e ts=2026-09-24T18:11:51.4210000Z -> 6aa4144c41b41dbac0c7f268.jsonl[1435] _id=6ab6b942485cab4c955dbb0d ts=2026-09-25T18:08:42.1840000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1876 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10006] _id=6ac53e85de269131f9b6764f ts=2026-10-06T18:31:32.6090000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10007] _id=6ac53e85de269131f9b67651 ts=2026-10-06T18:31:32.6090000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10062] _id=6ac53e88de269131f9b67685 ts=2026-10-06T18:31:35.9240000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10075] _id=6ac53e88de269131f9b67689 ts=2026-10-06T18:31:35.9240000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[10066] _id=6ac53e85de269131f9b67649 ts=2026-10-06T18:31:32.6090000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10006] _id=6ac53e85de269131f9b6764f ts=2026-10-06T18:31:32.6090000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6aa4144c41b41dbac0c7f268.jsonl[6793] _id=6abd5669485cab4c9591bf51 ts=2026-09-30T18:35:21.5530000Z -> 6aa4144c41b41dbac0c7f268.jsonl[8274] _id=6ac3edfade269131f9af257b ts=2026-10-05T18:35:38.0550000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 0m 
  - Evidence: 168h 0m: 6aa4144c41b41dbac0c7f268.jsonl[4040] _id=6abaafaa485cab4c956fd1d1 ts=2026-09-28T18:19:21.9910000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7970] _id=6ac3ea2ade269131f9aedfff ts=2026-10-05T18:19:22.3830000Z; 71h 40m: 6aa4144c41b41dbac0c7f268.jsonl[3660] _id=6ab6bfbe485cab4c955e5c2d ts=2026-09-25T18:38:54.9120000Z -> 6aa4144c41b41dbac0c7f268.jsonl[4078] _id=6abaaf97485cab4c956fcf4f ts=2026-09-28T18:19:03.6830000Z; 23h 56m: 6aa4144c41b41dbac0c7f268.jsonl[1096] _id=6ab56834485cab4c9554242c ts=2026-09-24T18:13:08.9310000Z -> 6aa4144c41b41dbac0c7f268.jsonl[1202] _id=6ab6b8cc485cab4c955db035 ts=2026-09-25T18:09:17.4750000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4144c41b41dbac0c7f268.jsonl[809] _id=6ab565a6485cab4c9553ea5e ts=2026-09-24T18:02:14.1560000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6452] _id=6abd5442485cab4c95916eff ts=2026-09-30T18:26:10.0210000Z; 144h 17m: 6aa4144c41b41dbac0c7f268.jsonl[6565] _id=6abd54bc485cab4c95918181 ts=2026-09-30T18:28:12.4710000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10556] _id=6ac541c6de269131f9b6d3a3 ts=2026-10-06T18:45:26.4500000Z; 23h 59m: 6aa4144c41b41dbac0c7f268.jsonl[10731] _id=6ac54269de269131f9b6ea49 ts=2026-10-06T18:48:09.2310000Z -> 6aa4144c41b41dbac0c7f268.jsonl[12058] _id=6ac693bdde269131f9be0fbe ts=2026-10-07T18:47:25.5080000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4144c41b41dbac0c7f268.jsonl[810] _id=6ab565a6485cab4c9553ea62 ts=2026-09-24T18:02:14.1770000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6376] _id=6abd5412485cab4c95916935 ts=2026-09-30T18:25:22.6050000Z; 144h 16m: 6aa4144c41b41dbac0c7f268.jsonl[6569] _id=6abd54bc485cab4c95918193 ts=2026-09-30T18:28:12.5270000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10506] _id=6ac5419dde269131f9b6cf21 ts=2026-10-06T18:44:45.7790000Z; 23h 58m: 6aa4144c41b41dbac0c7f268.jsonl[10736] _id=6ac54269de269131f9b6ea60 ts=2026-10-06T18:48:09.2780000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11997] _id=6ac69384de269131f9be072c ts=2026-10-07T18:46:28.3720000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.030s shown 
  - Evidence: 26ms: 6aa4144c41b41dbac0c7f268.jsonl[10734] _id=6ac54269de269131f9b6ea4e ts=2026-10-06T18:48:09.2520000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10736] _id=6ac54269de269131f9b6ea60 ts=2026-10-06T18:48:09.2780000Z; 30ms: 6aa4144c41b41dbac0c7f268.jsonl[6568] _id=6abd54bc485cab4c95918183 ts=2026-09-30T18:28:12.4970000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6569] _id=6abd54bc485cab4c95918193 ts=2026-09-30T18:28:12.5270000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4144c41b41dbac0c7f268.jsonl[804] _id=6ab565a3485cab4c9553ea25 ts=2026-09-24T18:02:11.5390000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6438] _id=6abd5424485cab4c95916a75 ts=2026-09-30T18:25:40.1630000Z; 144h 16m: 6aa4144c41b41dbac0c7f268.jsonl[6561] _id=6abd54b8485cab4c959180d6 ts=2026-09-30T18:28:08.4890000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10486] _id=6ac54191de269131f9b6cdb7 ts=2026-10-06T18:44:33.5540000Z; 23h 58m: 6aa4144c41b41dbac0c7f268.jsonl[10725] _id=6ac54252de269131f9b6e7a5 ts=2026-10-06T18:47:46.5570000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11992] _id=6ac69381de269131f9be06c4 ts=2026-10-07T18:46:25.6670000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 76 interval(s) ≤ 0.005s..0.020s shown 
  - Evidence: 5ms: 6aa4144c41b41dbac0c7f268.jsonl[6490] _id=6abd547c485cab4c959177ab ts=2026-09-30T18:27:08.5810000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6491] _id=6abd547c485cab4c959177af ts=2026-09-30T18:27:08.5860000Z; 20ms: 6aa4144c41b41dbac0c7f268.jsonl[10502] _id=6ac54197de269131f9b6ce89 ts=2026-10-06T18:44:39.3670000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10471] _id=6ac54198de269131f9b6cea3 ts=2026-10-06T18:44:39.3870000Z; 20ms: 6aa4144c41b41dbac0c7f268.jsonl[10574] _id=6ac541e6de269131f9b6d804 ts=2026-10-06T18:45:58.4670000Z -> 6aa4144c41b41dbac0c7f268.jsonl[10585] _id=6ac541e6de269131f9b6d808 ts=2026-10-06T18:45:58.4870000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4144c41b41dbac0c7f268.jsonl[786] _id=6ab56592485cab4c9553e80f ts=2026-09-24T18:01:54.7360000Z -> 6aa4144c41b41dbac0c7f268.jsonl[6380] _id=6abd541d485cab4c959169f5 ts=2026-09-30T18:25:33.5750000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 3h 33m 
  - Evidence: 3h 33m: 6aa4144c41b41dbac0c7f268.jsonl[11783] _id=6ac6607ade269131f9bb8611 ts=2026-10-07T15:08:42.5340000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11889] _id=6ac6929ede269131f9bdec24 ts=2026-10-07T18:42:38.8280000Z; 15m 48s: 6aa4144c41b41dbac0c7f268.jsonl[11127] _id=6ac65cc6de269131f9bb3275 ts=2026-10-07T14:52:54.1620000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11783] _id=6ac6607ade269131f9bb8611 ts=2026-10-07T15:08:42.5340000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 98h 58m 
  - Evidence: 98h 58m: 6aa4144c41b41dbac0c7f268.jsonl[6991] _id=6abe7770485cab4c95a9c4ee ts=2026-10-01T15:08:32.5440000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7474] _id=6ac3e746de269131f9aeb5df ts=2026-10-05T18:07:02.1440000Z; 71h 57m: 6aa4144c41b41dbac0c7f268.jsonl[1116] _id=6ab6b83a485cab4c955da5f3 ts=2026-09-25T18:06:31.1060000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3735] _id=6abaac03485cab4c956f6767 ts=2026-09-28T18:03:46.7940000Z; 47h 51m: 6aa4144c41b41dbac0c7f268.jsonl[3994] _id=6abaae1e485cab4c956f9e06 ts=2026-09-28T18:12:45.9370000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5689] _id=6abd4f36485cab4c9590d65d ts=2026-09-30T18:04:37.9380000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 98h 58m 
  - Evidence: 98h 58m: 6aa4144c41b41dbac0c7f268.jsonl[6985] _id=6abe7770485cab4c95a9c4e0 ts=2026-10-01T15:08:32.5430000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7473] _id=6ac3e746de269131f9aeb5dd ts=2026-10-05T18:07:02.1430000Z; 71h 20m: 6aa4144c41b41dbac0c7f268.jsonl[3730] _id=6ab6c0d5485cab4c955e6855 ts=2026-09-25T18:43:34.0350000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3737] _id=6abaac02485cab4c956f6765 ts=2026-09-28T18:03:46.7910000Z; 47h 42m: 6aa4144c41b41dbac0c7f268.jsonl[4129] _id=6abab043485cab4c956fe2b1 ts=2026-09-28T18:21:55.9380000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5687] _id=6abd4f36485cab4c9590d65b ts=2026-09-30T18:04:37.9370000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 99h 10m 
  - Evidence: 99h 10m: 6aa4144c41b41dbac0c7f268.jsonl[7469] _id=6abe793a485cab4c95aa084e ts=2026-10-01T15:16:10.5960000Z -> 6aa4144c41b41dbac0c7f268.jsonl[8130] _id=6ac3ebecde269131f9aeff41 ts=2026-10-05T18:26:52.3150000Z; 71h 28m: 6aa4144c41b41dbac0c7f268.jsonl[3728] _id=6ab6c0d3485cab4c955e6843 ts=2026-09-25T18:43:31.5990000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3990] _id=6abaadfb485cab4c956f9a5d ts=2026-09-28T18:12:11.4250000Z; 47h 43m: 6aa4144c41b41dbac0c7f268.jsonl[4128] _id=6abab043485cab4c956fe2af ts=2026-09-28T18:21:55.8610000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5693] _id=6abd4f47485cab4c9590d70d ts=2026-09-30T18:04:55.9880000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 98h 58m 
  - Evidence: 98h 58m: 6aa4144c41b41dbac0c7f268.jsonl[7001] _id=6abe778b485cab4c95a9ca5a ts=2026-10-01T15:08:59.4570000Z -> 6aa4144c41b41dbac0c7f268.jsonl[7478] _id=6ac3e751de269131f9aeb673 ts=2026-10-05T18:07:13.2310000Z; 71h 35m: 6aa4144c41b41dbac0c7f268.jsonl[3429] _id=6ab6bd58485cab4c955e4157 ts=2026-09-25T18:28:40.8280000Z -> 6aa4144c41b41dbac0c7f268.jsonl[3732] _id=6abaac14485cab4c956f67a2 ts=2026-09-28T18:04:03.6320000Z; 47h 42m: 6aa4144c41b41dbac0c7f268.jsonl[4218] _id=6abab17f485cab4c956ffef3 ts=2026-09-28T18:27:11.9330000Z -> 6aa4144c41b41dbac0c7f268.jsonl[5701] _id=6abd506a485cab4c9590e849 ts=2026-09-30T18:09:46.2710000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f268.jsonl[11497] _id=6ac65e1dde269131f9bb502c ts=2026-10-07T14:58:37.7970000Z -> 6aa4144c41b41dbac0c7f268.jsonl[11498] _id=6ac65e1dde269131f9bb502d ts=2026-10-07T14:58:37.7970000Z; 0ms: 6aa4144c41b41dbac0c7f268.jsonl[12117] _id=6ac6940ade269131f9be1c89 ts=2026-10-07T18:48:42.3010000Z -> 6aa4144c41b41dbac0c7f268.jsonl[12118] _id=6ac6940ade269131f9be1c8a ts=2026-10-07T18:48:42.3010000Z; 1ms: 6aa4144c41b41dbac0c7f268.jsonl[728] _id=6ab564aa485cab4c9553c961 ts=2026-09-24T17:58:02.3350000Z -> 6aa4144c41b41dbac0c7f268.jsonl[725] _id=6ab564aa485cab4c9553c966 ts=2026-09-24T17:58:02.3360000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[711] _id=6ab56491485cab4c9553c728 ts=2026-09-24T17:57:38.0060000Z`; `6aa4144c41b41dbac0c7f268.jsonl[818] _id=6ab565bd485cab4c9553ee88 ts=2026-09-24T18:02:37.2420000Z`; `6aa4144c41b41dbac0c7f268.jsonl[4167] _id=6abab0c1485cab4c956ff25f ts=2026-09-28T18:24:01.5220000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 90 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1598] _id=6ab6b958485cab4c955dbdc7 ts=2026-09-25T18:11:35.6120000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1568] _id=6ab6b958485cab4c955dbdd1 ts=2026-09-25T18:11:35.6330000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1665] _id=6ab6b965485cab4c955dbf67 ts=2026-09-25T18:11:49.4110000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 238 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1070] _id=6ab567e9485cab4c9554215e ts=2026-09-24T18:11:51.2990000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1071] _id=6ab567e9485cab4c95542164 ts=2026-09-24T18:11:51.3470000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1078] _id=6ab567ea485cab4c95542166 ts=2026-09-24T18:11:51.3720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[6569] _id=6abd54bc485cab4c95918193 ts=2026-09-30T18:28:12.5270000Z`; `6aa4144c41b41dbac0c7f268.jsonl[10736] _id=6ac54269de269131f9b6ea60 ts=2026-10-06T18:48:09.2780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[6491] _id=6abd547c485cab4c959177af ts=2026-09-30T18:27:08.5860000Z`; `6aa4144c41b41dbac0c7f268.jsonl[6492] _id=6abd547c485cab4c959177b3 ts=2026-09-30T18:27:08.6070000Z`; `6aa4144c41b41dbac0c7f268.jsonl[10477] _id=6ac54191de269131f9b6cdc7 ts=2026-10-06T18:44:33.6790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[11127] _id=6ac65cc6de269131f9bb3275 ts=2026-10-07T14:52:54.1620000Z`; `6aa4144c41b41dbac0c7f268.jsonl[11783] _id=6ac6607ade269131f9bb8611 ts=2026-10-07T15:08:42.5340000Z`; `6aa4144c41b41dbac0c7f268.jsonl[11889] _id=6ac6929ede269131f9bdec24 ts=2026-10-07T18:42:38.8280000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[3736] _id=6abaac13485cab4c956f678b ts=?`; `6aa4144c41b41dbac0c7f268.jsonl[5696] _id=6abd5021485cab4c9590e425 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 419 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1596] _id=6ab6b95a485cab4c955dbe3f ts=2026-09-25T18:11:38.8380000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1721] _id=6ab6b973485cab4c955dc0bf ts=2026-09-25T18:12:03.9310000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1734] _id=6ab6b976485cab4c955dc0e9 ts=2026-09-25T18:12:06.0490000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 575 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1059] _id=6ab567e7485cab4c95542124 ts=2026-09-24T18:11:50.4280000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1060] _id=6ab567e7485cab4c9554212a ts=2026-09-24T18:11:50.4930000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1048] _id=6ab567e7485cab4c9554212c ts=2026-09-24T18:11:50.5380000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 19 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[10479] _id=6ac54193de269131f9b6cded ts=2026-10-06T18:44:35.0520000Z`; `6aa4144c41b41dbac0c7f268.jsonl[10495] _id=6ac54194de269131f9b6ce10 ts=2026-10-06T18:44:36.2280000Z`; `6aa4144c41b41dbac0c7f268.jsonl[10491] _id=6ac54194de269131f9b6ce1d ts=2026-10-06T18:44:36.6090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'DialogueStartEvent' (totals: 368 start, 360 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 167 unmatched 'BecameCameraCentered' (totals: 649 open, 572 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 133 unmatched 'BecameVisible' (totals: 900 open, 1005 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 174 open, 180 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 47 start, 29 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 250 of 12153 adjacent _id pairs reverse in client time; worst 152.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f268.jsonl[1464] _id=6ab6b946485cab4c955dbba1 ts=2026-09-25T18:11:18.0840000Z`; `6aa4144c41b41dbac0c7f268.jsonl[1465] _id=6ab6b946485cab4c955dbba5 ts=2026-09-25T18:08:45.1430000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -153.11s, max +1.00s over 12154 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f268\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4267 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1969); Unit 4 Dev - Dungeon (702); Unit 2 Prod (Refactor) (578); Unit 3 Dungeon Dev (284); Unit 1 Dev (235); Unit 4 Dev (181); Unit 5 Dev - Dungeon (173); Unit 4 Dev - Anderson Base (84); Unit 5 Dev (61)
- **Intervals:** median 0.85s (p5 0.09s / p95 12.17s, n=4266)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4267/4267 records)
    "pressed"  x4267
data.actionType  (string, 4267/4267 records)
    "Move"  x2899
    "Interact"  x877
    "Sprint"  x158
    "Ascend"  x152
    "Jump"  x114
    "Hoverboard"  x39
    "Map"  x20
    "Descend"  x6
    "SkipCinematic"  x2
data.key  (string, 4267/4267 records)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4267/4267 records)
    "Player"  x2511
    "Drone"  x1756
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3126 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1786); Unit 4 Dev (568); Unit 3 Dungeon Dev (500); Unit 5 Dev - Dungeon (272)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.35s, n=3125)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3126/3126 records)
    "BecameInvisible"  x1005
    "BecameVisible"  x900
    "BecameCameraCentered"  x649
    "BecameCameraUncentered"  x572
data.pieceId  (string, 3126/3126 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3126/3126 records)
    1956 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1864 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (482); Unit 1 Dev (287); Unit 4 Dev (263); Unit 2 Prod (Refactor) (254); Unit 5 Dev (143); Unit 3 Dungeon Dev (140); Unit 4 Dev - Dungeon (122); Unit 4 Dev - Anderson Base (98); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1136 of 1864 records
- **Intervals:** median 4.23s (p5 0.00s / p95 36.04s, n=1863)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1136; [conversationId, dialogueEventType] x728
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1864/1864 records)
    numeric range 10 .. 117 (48 unique)
data.dialogueEventType  (string, 1864/1864 records)
    "DialogueNodeEvent"  x1136
    "DialogueStartEvent"  x368
    "DialogueFinishEvent"  x360
data.nodeId  (number, 1136/1864 records)
    numeric range 0 .. 289 (200 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1788 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (442); Unit 1 Dev (308); Unit 2 Prod (Refactor) (303); Unit 4 Dev (207); Unit 4 Dev - Dungeon (185); Unit 3 Dungeon Dev (115); Unit 5 Dev - Dungeon (95); Unit 5 Dev (77); Unit 4 Dev - Anderson Base (56)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.02s, n=1774)
- **Fields under `data`:**

```text
data.position  (object, 1788/1788 records)
data.position.x  (number, 1788/1788 records)
    numeric range -686.069 .. 1575.64 (622 unique)
data.position.y  (number, 1788/1788 records)
    numeric range -112.476 .. 221.836 (458 unique)
data.position.z  (number, 1788/1788 records)
    numeric range -1182.29 .. 1974.07 (624 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 391 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (183); Unit 3 Dev (117); Unit 5 Dev (66); Unit 1 Dev (25)
- **Intervals:** median 0.38s (p5 0.03s / p95 6.10s, n=390)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 391/391 records)
    "argumentationNodeHoverEnd"  x180
    "argumentationNodeHoverStart"  x174
    "argumentationNodeAdd"  x26
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 391/391 records)
    "Unit 4 - Flooding"  x183
    "Unit 3 - Pollution Upstream"  x117
    "Unit 5"  x66
    "Unit 1 - Freshwater"  x17
    "Unit 1 - Argumentation Tutorial"  x8
data.nodeName  (string, 391/391 records)
    "A"  x53
    "D"  x47
    "I"  x42
    "B"  x40
    "2"  x37
    "II"  x36
    "C"  x33
    "3"  x31
    "4"  x30
    "1"  x29
    "5"  x13
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 314 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (125); Unit 2 Prod (Refactor) (60); Unit 3 Dungeon Dev (46); Unit 1 Dev (26); Unit 4 Dev (20); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (8); Unit 5 Dev - Dungeon (8)
- **Intervals:** median 8.34s (p5 0.86s / p95 332.71s, n=313)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 314/314 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 314/314 records)
    88 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 3 Dev (12); Unit 4 Dev - Dungeon (12); Unit 4 Dev (9); Unit 2 Prod (Refactor) (8); Unit 5 Dev - Dungeon (7); Unit 5 Dev (5); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 212.57s (p5 0.00s / p95 84738.61s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x29
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x29
data.questID  (string, 76/76 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 29/76 records)
    "Succeeded"  x29
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 54 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (50); Unit 3 Dev (4)
- **Intervals:** median 2.63s (p5 0.53s / p95 35152.60s, n=53)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, legendName] x19; [actionType, featureUsed, location] x1
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "Selected"  x19
    "MapCloseEvent"  x17
    "MapOpenEvent"  x17
    "WaypointSetEvent"  x1
data.featureUsed  (string, 54/54 records)
    "Map"  x34
    "Legend"  x19
    "Waypoint"  x1
data.legendName  (string, 19/54 records)
    "180 ft"  x5
    "270 ft"  x5
    "150 ft"  x3
    "210 ft"  x2
    "240 ft"  x2
    "300 ft"  x1
    "90 ft"  x1
data.location  (object, 1/54 records)
data.location.x  (number, 1/54 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 1/54 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 1/54 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 42 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 1 Dev (7); Unit 2 Prod (Refactor) (6); Unit 3 Dev (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (2); Transition (1); Unit 3 Dungeon Dev (1); Unit 5 Dev (1)
- **Intervals:** median 377.67s (p5 10.77s / p95 171762.00s, n=41)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 42/42 records)
    true  x42
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 36 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (18); Unit 4 Dev (18)
- **Intervals:** median 1.00s (p5 0.45s / p95 11.85s, n=35)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x32; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/36 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/36 records)
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 32/36 records)
    "RightDrag"  x17
    "LeftDrag"  x15
data.currentSoilType  (string, 32/36 records)
    "CLAYSAND"  x8
    "CLAY"  x7
    "SAND"  x6
    "CLAYROCK"  x4
    "SANDGRAVEL"  x4
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 32/36 records)
    "false"  x23
    "true"  x9
data.waterLevelStatus  (string, 32/36 records)
    "TooHigh"  x13
    "Proper"  x11
    "TooLow"  x8
data.waterRetentionChange  (string, 32/36 records)
    "Decrease"  x16
    "NoChange"  x9
    "Increase"  x7
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowUnfocusEvent` — 33 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (8); Unit 4 Dev (5); Unit 3 Dev (4); Unit 5 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Transition (1)
- **Intervals:** median 756.90s (p5 8.09s / p95 210272.99s, n=32)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `WaterChamberEvent` — 32 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (32)
- **Intervals:** median 8.76s (p5 0.87s / p95 65.56s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "On"  x22
    "Off"  x10
data.floor  (string, 32/32 records)
    "3"  x20
    "4"  x7
    "2"  x3
    "1"  x2
data.machineNumber  (string, 32/32 records)
    "One"  x31
    "Two"  x1
data.machineType  (string, 32/32 records)
    "Condenser"  x11
    "DualChamber_Condenser"  x9
    "Evaporator"  x6
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x2
data.room  (string, 32/32 records)
    "2"  x20
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 31 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (21); Unit 3 Dev (5); Unit 1 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 9.09s (p5 0.69s / p95 324549.01s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "submitAnswerEvent"  x31
data.answerSubmitted  (string, 31/31 records, 2 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 31/31 records)
    "Unit 4 - Flooding"  x21
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 27 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (27)
- **Intervals:** median 2.94s (p5 0.72s / p95 115.14s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "ChangeCanister"  x27
data.canisterType  (string, 27/27 records)
    "Clay"  x13
    "Bedrock"  x7
    "Gravel"  x4
    "Sand"  x3
data.floor  (string, 27/27 records)
    "5"  x19
    "4"  x8
data.machine  (string, 27/27 records)
    "1"  x26
    "2"  x1
data.row  (string, 27/27 records)
    "TopRow"  x16
    "BottomRow"  x11
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 24 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); MainMenu (3); Unit 3 Dev (3); Unit 3 Dungeon Dev (3); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1504.59s (p5 24.11s / p95 250366.79s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "DebugMenuStateChanged"  x24
data.isOpened  (bool, 24/24 records)
    false  x24
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 73930.60s (p5 255.39s / p95 288217.86s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 68.06s (p5 0.03s / p95 519590.84s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 3.39s (p5 0.95s / p95 21.56s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x4
data.boxId  (string, 11/11 records)
    "0"  x7
    "1"  x2
    "2"  x2
data.soilType  (string, 11/11 records)
    "Gravel"  x4
    "Clay"  x3
    "Sand"  x3
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (1)
- **Intervals:** median 128.54s (p5 16.49s / p95 467849.81s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 555797.03s (p5 199366.32s / p95 912227.74s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 6892.33s (p5 1542.77s / p95 12241.90s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "No launch progress after 95 s: loading assets"  x1
data.phase  (string, 2/2 records)
    "compiling"  x1
    "running"  x1
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "load_stalled"  x1
    "unhandled_rejection"  x1
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
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `TerasGardenBox` data.actionType: "" (7x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (19x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Legend" (19x); "Waypoint" (1x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (7x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*