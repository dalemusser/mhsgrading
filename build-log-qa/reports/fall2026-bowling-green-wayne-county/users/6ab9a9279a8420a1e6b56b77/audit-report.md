# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b77

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b77
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b77.jsonl
- **Records:** 14969 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b77
- **Time span:** 2026-10-06T18:36:50.100000+00:00 .. 2026-10-16T21:15:00.200000+00:00 (242h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b77\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14969 records, 11 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 92 INFO, 0 NOT_TESTED, 102 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5556 | 37.12 | 1 | 9 | 0 | 2026-10-06T18:37:05.810000+00:00 | 2026-10-16T21:15:00.200000+00:00 | 242h 37m |
| PuzzlePieceVisibleEvent | 3260 | 21.78 | 1 | 4 | 0 | 2026-10-08T18:53:10.154000+00:00 | 2026-10-16T18:44:21.569000+00:00 | 191h 51m |
| PlayerPositionEvent | 2785 | 18.61 | 1 | 9 | 0 | 2026-10-06T18:37:02.308000+00:00 | 2026-10-16T21:14:53.775000+00:00 | 242h 37m |
| DialogueEvent | 2178 | 14.55 | 1 | 9 | 1400 | 2026-10-06T18:37:22.353000+00:00 | 2026-10-16T21:14:41.682000+00:00 | 242h 37m |
| ObjectInterEvent | 376 | 2.51 | 1 | 9 | 0 | 2026-10-06T18:42:57.146000+00:00 | 2026-10-16T21:15:00.199000+00:00 | 242h 32m |
| argumentationNodeEvent | 283 | 1.89 | 1 | 5 | 0 | 2026-10-07T19:08:29.293000+00:00 | 2026-10-16T20:56:06.817000+00:00 | 217h 47m |
| TopographicMapEvent | 121 | 0.81 | 1 | 4 | 0 | 2026-10-08T18:53:39.318000+00:00 | 2026-10-15T01:13:06.462000+00:00 | 150h 19m |
| Soil Key Puzzle | 102 | 0.68 | 1 | 3 | 0 | 2026-10-08T19:01:35.645000+00:00 | 2026-10-15T00:27:09.561000+00:00 | 149h 25m |
| questEvent | 81 | 0.54 | 1 | 9 | 81 | 2026-10-06T18:37:22.326000+00:00 | 2026-10-16T21:08:57.774000+00:00 | 242h 31m |
| WaterChamberEvent | 57 | 0.38 | 1 | 1 | 0 | 2026-10-16T18:38:26.236000+00:00 | 2026-10-16T18:54:04.447000+00:00 | 15m 38s |
| DEBUGMenu | 28 | 0.19 | 1 | 9 | 0 | 2026-10-06T18:37:02.290000+00:00 | 2026-10-16T20:45:55.872000+00:00 | 242h 8m |
| gameWindowFocusEvent | 22 | 0.15 | 1 | 7 | 0 | 2026-10-06T18:36:50.100000+00:00 | 2026-10-16T20:45:56.006000+00:00 | 242h 9m |
| soilMachine | 16 | 0.11 | 1 | 1 | 0 | 2026-10-15T01:13:33.313000+00:00 | 2026-10-15T01:28:14.564000+00:00 | 14m 41s |
| argumentationAnswerEvent | 15 | 0.1 | 1 | 5 | 0 | 2026-10-07T19:08:52.822000+00:00 | 2026-10-16T20:56:07.868000+00:00 | 217h 47m |
| argumentationEvent | 14 | 0.09 | 1 | 5 | 0 | 2026-10-07T19:08:24.039000+00:00 | 2026-10-16T20:56:07.899000+00:00 | 217h 47m |
| gameWindowUnfocusEvent | 14 | 0.09 | 1 | 9 | 0 | 2026-10-06T19:17:44.451000+00:00 | 2026-10-16T18:59:27.131000+00:00 | 239h 41m |
| gameStartEvent | 12 | 0.08 | 1 | 1 | 0 | 2026-10-06T18:36:50.102000+00:00 | 2026-10-16T20:45:56.006000+00:00 | 242h 9m |
| argumentationToolEvent | 11 | 0.07 | 1 | 4 | 0 | 2026-10-07T19:08:19.103000+00:00 | 2026-10-16T20:55:22.025000+00:00 | 217h 47m |
| DaniEvent | 10 | 0.07 | 1 | 3 | 0 | 2026-10-11T00:08:32.539000+00:00 | 2026-10-15T01:01:08.202000+00:00 | 96h 52m |
| SolarStillDesignEvent | 8 | 0.05 | 1 | 1 | 0 | 2026-10-16T21:03:29.364000+00:00 | 2026-10-16T21:04:14.064000+00:00 | 44.7s |
| chatEvent | 7 | 0.05 | 1 | 4 | 0 | 2026-10-14T18:43:30.195000+00:00 | 2026-10-16T20:46:13.368000+00:00 | 50h 2m |
| TerasGardenBox | 6 | 0.04 | 1 | 1 | 0 | 2026-10-15T01:50:33.304000+00:00 | 2026-10-15T01:52:41.340000+00:00 | 2m 8s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-07T19:13:35.041000+00:00 | 2026-10-16T21:15:00.179000+00:00 | 218h 1m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 218680.193s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.403s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.065s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 20.642s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.829s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.707s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 55.866s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.119s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3980.236s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84816.132s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2547.872s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 4839.984s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.766s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 10 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 330 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 15 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; A,II; C,D,2,II; C,D,3,II; C,D,4,2,II; C,D,4,II; C,D,A,2,II; D,C,3,4,II 
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
  - Observed: Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 7 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [79-71, 79-74, 79-75, 79-76, 79-108]; [91-61, 91-56, 91-57, 91-59, 91-61] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 14 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[458] _id=6ac5441bde269131f9b71263 ts=2026-10-06T18:55:23.4590000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[497] _id=6ac54551de269131f9b726d5 ts=2026-10-06T19:00:33.5900000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[581] _id=6ac54650de269131f9b73fd3 ts=2026-10-06T19:04:47.9610000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[6] _id=6ac53fc2de269131f9b69841 ts=2026-10-06T18:36:50.1020000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[747] _id=6ac692f3de269131f9bdf4e0 ts=2026-10-07T18:44:02.0210000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1306] _id=6ac69a41de269131f9bf159f ts=2026-10-07T19:15:12.3590000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[5] _id=6ac53fc2de269131f9b6983f ts=2026-10-06T18:36:50.1000000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[746] _id=6ac692f3de269131f9bdf4df ts=2026-10-07T18:44:02.0210000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1305] _id=6ac69a41de269131f9bf159e ts=2026-10-07T19:15:12.3590000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[744] _id=6ac692f3de269131f9bdf4da ts=2026-10-06T19:17:44.451Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1340] _id=6ac7e591de269131f9c58a2a ts=2026-10-07T19:17:32.272Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1341] _id=6ac7e5a1de269131f9c58b4d ts=2026-10-08T18:49:03.3340000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 22 of 121 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[1467] _id=6ac7e6b4de269131f9c5abff ts=2026-10-08T18:53:39.3180000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1465] _id=6ac7e6b7de269131f9c5ac61 ts=2026-10-08T18:53:42.3700000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1472] _id=6ac7e6bbde269131f9c5acdc ts=2026-10-08T18:53:46.3080000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5555 | 0.0 | 1.153 | 157.241 | 13.155 | 234769.339 | 0.38 | 98 | 11 |
| PuzzlePieceVisibleEvent | 3259 | 0.0 | 0.065 | 211.927 | 2.449 | 237958.996 | 0.28 | 1496 | 8 |
| PlayerPositionEvent | 2773 | 9.736 | 10.002 | 177.202 | 10.086 | 187640.913 | 0.34 | 0 | 6 |
| DialogueEvent | 2177 | 0.0 | 4.684 | 401.212 | 47.652 | 234554.044 | 0.15 | 603 | 12 |
| ObjectInterEvent | 375 | 0.0 | 12.403 | 2328.328 | 376.278 | 235526.934 | 0.03 | 5 | 15 |
| argumentationNodeEvent | 282 | 0.003 | 0.79 | 2780.346 | 9.976 | 281399.3 | 0.02 | 37 | 4 |
| TopographicMapEvent | 120 | 0.019 | 3.829 | 4509.726 | 1315.541 | 237049.771 | 0.01 | 4 | 9 |
| Soil Key Puzzle | 101 | 0.12 | 0.494 | 5326.078 | 18.737 | 240315.238 | 0.01 | 0 | 3 |
| questEvent | 80 | 0.0 | 254.707 | 10913.693 | 84769.791 | 234732.882 | 0.01 | 15 | 19 |
| WaterChamberEvent | 56 | 0.095 | 6.707 | 16.754 | 71.457 | 90.159 | 3.58 | 0 | 0 |
| DEBUGMenu | 27 | 7.848 | 836.88 | 32286.429 | 176574.949 | 241546.269 | 0.0 | 0 | 14 |
| gameWindowFocusEvent | 21 | 4.674 | 2547.872 | 41511.71 | 189351.682 | 236673.619 | 0.0 | 0 | 14 |
| soilMachine | 15 | 0.337 | 6.766 | 58.75 | 202.09 | 223.166 | 1.02 | 0 | 0 |
| argumentationAnswerEvent | 14 | 3.796 | 55.866 | 56002.503 | 252239.396 | 281492.799 | 0.0 | 0 | 4 |
| argumentationEvent | 13 | 0.047 | 113.782 | 60312.605 | 254404.727 | 281384.32 | 0.0 | 1 | 4 |
| gameWindowUnfocusEvent | 13 | 8.741 | 4839.984 | 66377.129 | 243173.44 | 323344.838 | 0.0 | 0 | 10 |
| gameStartEvent | 11 | 360.707 | 84816.132 | 79249.628 | 215466.463 | 241557.654 | 0.0 | 0 | 10 |
| argumentationToolEvent | 10 | 0.814 | 4.119 | 78402.292 | 274498.841 | 281614.321 | 0.0 | 0 | 3 |
| DaniEvent | 9 | 2.295 | 6.883 | 38750.629 | 202662.198 | 322834.668 | 0.0 | 0 | 3 |
| SolarStillDesignEvent | 7 | 1.153 | 3.069 | 6.386 | 17.399 | 21.508 | 9.4 | 0 | 0 |
| chatEvent | 6 | 6.042 | 3980.236 | 30027.196 | 117940.48 | 149785.859 | 0.0 | 0 | 4 |
| TerasGardenBox | 5 | 1.533 | 20.642 | 25.607 | 59.106 | 63.772 | 2.34 | 0 | 0 |
| EndOfUnit | 4 | 7303.704 | 218680.193 | 196221.285 | 331439.146 | 340221.047 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[10404] _id=6ad0203ede269131f9d9cbe3 ts=2026-10-15T00:37:17.2060000Z == 6ab9a9279a8420a1e6b56b77.jsonl[10405] _id=6ad0203ede269131f9d9cbe4 ts=2026-10-15T00:37:17.2060000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 51 group(s), 88 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[1443] _id=6ac7e69ade269131f9c5a90b ts=2026-10-08T18:53:11.4200000Z == 6ab9a9279a8420a1e6b56b77.jsonl[1444] _id=6ac7e69ade269131f9c5a90c ts=2026-10-08T18:53:11.4200000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[3375] _id=6acad7c6de269131f9cb442d ts=2026-10-11T00:26:44.0220000Z == 6ab9a9279a8420a1e6b56b77.jsonl[3376] _id=6acad7c6de269131f9cb4431 ts=2026-10-11T00:26:44.0220000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[3389] _id=6acad7c7de269131f9cb4433 ts=2026-10-11T00:26:45.7480000Z == 6ab9a9279a8420a1e6b56b77.jsonl[3377] _id=6acad7c7de269131f9cb4435 ts=2026-10-11T00:26:45.7480000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[14651] _id=6ad28fb4de269131f9e8224b ts=2026-10-16T20:57:24.1850000Z == 6ab9a9279a8420a1e6b56b77.jsonl[14652] _id=6ad28fb4de269131f9e8224c ts=2026-10-16T20:57:24.1850000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 52 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `985ms: 6ab9a9279a8420a1e6b56b77.jsonl[120] _id=6ac5413ede269131f9b6c465 ts=2026-10-06T18:43:10.0880000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[129] _id=6ac5413fde269131f9b6c477 ts=2026-10-06T18:43:11.0730000Z`; `308ms: 6ab9a9279a8420a1e6b56b77.jsonl[129] _id=6ac5413fde269131f9b6c477 ts=2026-10-06T18:43:11.0730000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[130] _id=6ac5413fde269131f9b6c481 ts=2026-10-06T18:43:11.3810000Z`; `243ms: 6ab9a9279a8420a1e6b56b77.jsonl[130] _id=6ac5413fde269131f9b6c481 ts=2026-10-06T18:43:11.3810000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[131] _id=6ac5413fde269131f9b6c485 ts=2026-10-06T18:43:11.6240000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `389ms: 6ab9a9279a8420a1e6b56b77.jsonl[2430] _id=6ac7eb7ade269131f9c66d8c ts=2026-10-08T19:14:01.1530000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[2438] _id=6ac7eb7ade269131f9c66da1 ts=2026-10-08T19:14:01.5420000Z`; `244ms: 6ab9a9279a8420a1e6b56b77.jsonl[2985] _id=6acad16bde269131f9cb411f ts=2026-10-10T23:59:38.9800000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[2976] _id=6acad16cde269131f9cb4121 ts=2026-10-10T23:59:39.2240000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `562ms: 6ab9a9279a8420a1e6b56b77.jsonl[13882] _id=6ad2717dde269131f9e757ad ts=2026-10-16T18:48:29.6290000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[13912] _id=6ad2717ede269131f9e757bd ts=2026-10-16T18:48:30.1910000Z`; `468ms: 6ab9a9279a8420a1e6b56b77.jsonl[13909] _id=6ad2717ede269131f9e757b3 ts=2026-10-16T18:48:29.9110000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[13914] _id=6ad2717ede269131f9e757bf ts=2026-10-16T18:48:30.3790000Z`; `563ms: 6ab9a9279a8420a1e6b56b77.jsonl[13920] _id=6ad27191de269131f9e7595b ts=2026-10-16T18:48:49.6400000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[13929] _id=6ad27192de269131f9e7596a ts=2026-10-16T18:48:50.2030000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `53ms: 6ab9a9279a8420a1e6b56b77.jsonl[6003] _id=6ace8116de269131f9d155a5 ts=2026-10-13T19:05:57.5360000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[6006] _id=6ace8116de269131f9d155a8 ts=2026-10-13T19:05:57.5890000Z`; `47ms: 6ab9a9279a8420a1e6b56b77.jsonl[12662] _id=6ad03072de269131f9da1d46 ts=2026-10-15T01:46:25.9220000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[12665] _id=6ad03072de269131f9da1d49 ts=2026-10-15T01:46:25.9690000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `361ms: 6ab9a9279a8420a1e6b56b77.jsonl[1197] _id=6ac69902de269131f9befb8a ts=2026-10-07T19:09:53.8210000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[1195] _id=6ac69903de269131f9befb94 ts=2026-10-07T19:09:54.1820000Z`; `333ms: 6ab9a9279a8420a1e6b56b77.jsonl[1199] _id=6ac6990cde269131f9befc26 ts=2026-10-07T19:10:03.7940000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[1201] _id=6ac6990cde269131f9befc32 ts=2026-10-07T19:10:04.1270000Z`; `852ms: 6ab9a9279a8420a1e6b56b77.jsonl[5097] _id=6acae489de269131f9cb50e3 ts=2026-10-11T01:21:12.7110000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[5098] _id=6acae48ade269131f9cb50e7 ts=2026-10-11T01:21:13.5630000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9279a8420a1e6b56b77.jsonl[14824] _id=6ad2919fde269131f9e824ee ts=2026-10-16T21:05:35.2560000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[14825] _id=6ad2919fde269131f9e824f0 ts=2026-10-16T21:05:35.2600000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `622ms: 6ab9a9279a8420a1e6b56b77.jsonl[12093] _id=6ad02b7bde269131f9da0450 ts=2026-10-15T01:25:14.4280000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[12094] _id=6ad02b7bde269131f9da0457 ts=2026-10-15T01:25:15.0500000Z`; `337ms: 6ab9a9279a8420a1e6b56b77.jsonl[12094] _id=6ad02b7bde269131f9da0457 ts=2026-10-15T01:25:15.0500000Z ~ 6ab9a9279a8420a1e6b56b77.jsonl[12104] _id=6ad02b7cde269131f9da045d ts=2026-10-15T01:25:15.3870000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 67h 5m 
  - Evidence: 67h 5m: 6ab9a9279a8420a1e6b56b77.jsonl[2687] _id=6acacac4de269131f9cb3eda ts=2026-10-10T23:31:15.5270000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5254] _id=6ace7a4ede269131f9d0fc0f ts=2026-10-13T18:37:01.7960000Z; 52h 35m: 6ab9a9279a8420a1e6b56b77.jsonl[1343] _id=6ac7e5a6de269131f9c58b7c ts=2026-10-08T18:49:09.5930000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2525] _id=6acac950de269131f9cb3dd0 ts=2026-10-10T23:25:03.6070000Z; 40h 45m: 6ab9a9279a8420a1e6b56b77.jsonl[12689] _id=6ad030a7de269131f9da1dde ts=2026-10-15T01:47:17.4110000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12986] _id=6ad26debde269131f9e705ed ts=2026-10-16T18:33:14.5430000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 89h 40m 
  - Evidence: 89h 40m: 6ab9a9279a8420a1e6b56b77.jsonl[4708] _id=6acae03dde269131f9cb4dd3 ts=2026-10-11T01:02:52.5090000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[7421] _id=6acfcd50de269131f9d76ad6 ts=2026-10-14T18:43:27.1770000Z; 6h 13m: 6ab9a9279a8420a1e6b56b77.jsonl[7422] _id=6acfcd52de269131f9d76b3f ts=2026-10-14T18:43:29.9270000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[11150] _id=6ad024d6de269131f9d9e479 ts=2026-10-15T00:56:53.4200000Z; 54m 13s: 6ab9a9279a8420a1e6b56b77.jsonl[3083] _id=6acad383de269131f9cb41fb ts=2026-10-11T00:08:34.8340000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[4706] _id=6acae039de269131f9cb4dcf ts=2026-10-11T01:02:48.0020000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 65h 9m 
  - Evidence: 65h 9m: 6ab9a9279a8420a1e6b56b77.jsonl[5249] _id=6acae62bde269131f9cb5220 ts=2026-10-11T01:28:10.1150000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5260] _id=6ace7a65de269131f9d0fcef ts=2026-10-13T18:37:24.1590000Z; 52h 16m: 6ab9a9279a8420a1e6b56b77.jsonl[2508] _id=6ac7ec20de269131f9c680f6 ts=2026-10-08T19:16:47.8040000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2709] _id=6acacb22de269131f9cb3f1e ts=2026-10-10T23:32:49.9890000Z; 40h 33m: 6ab9a9279a8420a1e6b56b77.jsonl[12985] _id=6ad033afde269131f9da29cb ts=2026-10-15T02:00:14.8560000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12995] _id=6ad26e08de269131f9e708fb ts=2026-10-16T18:33:44.6770000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 603 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[12625] _id=6ad03051de269131f9da1cb6 ts=2026-10-15T01:45:52.7370000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12626] _id=6ad03051de269131f9da1cb7 ts=2026-10-15T01:45:52.7370000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[12646] _id=6ad03062de269131f9da1cf6 ts=2026-10-15T01:46:09.2910000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12647] _id=6ad03062de269131f9da1cf7 ts=2026-10-15T01:46:09.2910000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[14574] _id=6ad28f4bde269131f9e82197 ts=2026-10-16T20:55:39.0680000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14575] _id=6ad28f4bde269131f9e82198 ts=2026-10-16T20:55:39.0680000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 30m 
  - Evidence: 94h 30m: 6ab9a9279a8420a1e6b56b77.jsonl[5253] _id=6acae62bde269131f9cb521e ts=2026-10-11T01:28:10.0790000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[9182] _id=6ad01728de269131f9d9b673 ts=2026-10-14T23:58:31.1260000Z; 78h 14m: 6ab9a9279a8420a1e6b56b77.jsonl[1274] _id=6ac699dfde269131f9bf0cab ts=2026-10-07T19:13:35.0410000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5253] _id=6acae62bde269131f9cb521e ts=2026-10-11T01:28:10.0790000Z; 43h 14m: 6ab9a9279a8420a1e6b56b77.jsonl[12984] _id=6ad033afde269131f9da29c7 ts=2026-10-15T02:00:14.8300000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14967] _id=6ad293d4de269131f9e82b56 ts=2026-10-16T21:15:00.1790000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 65h 12m 
  - Evidence: 65h 12m: 6ab9a9279a8420a1e6b56b77.jsonl[5236] _id=6acae612de269131f9cb5207 ts=2026-10-11T01:27:45.3340000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5302] _id=6ace7b23de269131f9d10ad8 ts=2026-10-13T18:40:34.6730000Z; 52h 8m: 6ab9a9279a8420a1e6b56b77.jsonl[2515] _id=6ac7ec34de269131f9c68392 ts=2026-10-08T19:17:07.6460000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2528] _id=6acac95dde269131f9cb3dd8 ts=2026-10-10T23:25:15.8450000Z; 40h 34m: 6ab9a9279a8420a1e6b56b77.jsonl[12971] _id=6ad0339ade269131f9da28e1 ts=2026-10-15T01:59:54.0780000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[13023] _id=6ad26e27de269131f9e70be4 ts=2026-10-16T18:34:15.1430000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 98 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[10404] _id=6ad0203ede269131f9d9cbe3 ts=2026-10-15T00:37:17.2060000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[10405] _id=6ad0203ede269131f9d9cbe4 ts=2026-10-15T00:37:17.2060000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[10829] _id=6ad022afde269131f9d9dc15 ts=2026-10-15T00:47:42.6200000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[10830] _id=6ad022afde269131f9d9dc16 ts=2026-10-15T00:47:42.6200000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[9385] _id=6ad01de6de269131f9d9c095 ts=2026-10-15T00:27:17.0770000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[9386] _id=6ad01de6de269131f9d9c096 ts=2026-10-15T00:27:17.0770000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 65h 25m 
  - Evidence: 65h 25m: 6ab9a9279a8420a1e6b56b77.jsonl[5000] _id=6acae3a0de269131f9cb5033 ts=2026-10-11T01:17:19.2730000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5350] _id=6ace7ba7de269131f9d11132 ts=2026-10-13T18:42:46.2070000Z; 53h 21m: 6ab9a9279a8420a1e6b56b77.jsonl[2236] _id=6ac7e890de269131f9c5f3b8 ts=2026-10-08T19:01:35.6480000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[3279] _id=6acad6ebde269131f9cb4365 ts=2026-10-11T00:23:06.3300000Z; 40h 36m: 6ab9a9279a8420a1e6b56b77.jsonl[12975] _id=6ad0339ede269131f9da28f0 ts=2026-10-15T01:59:57.0650000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[13193] _id=6ad26ebede269131f9e71ac2 ts=2026-10-16T18:36:45.5370000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[12293] _id=6ad02f6ede269131f9da197b ts=2026-10-15T01:42:05.7920000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12294] _id=6ad02f6ede269131f9da197c ts=2026-10-15T01:42:05.7920000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[12498] _id=6ad02f00de269131f9da1815 ts=2026-10-15T01:40:15.6500000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12499] _id=6ad02f00de269131f9da1816 ts=2026-10-15T01:40:15.6500000Z; 5ms: 6ab9a9279a8420a1e6b56b77.jsonl[795] _id=6ac69373de269131f9be0527 ts=2026-10-07T18:46:11.0060000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[792] _id=6ac69374de269131f9be0539 ts=2026-10-07T18:46:11.0110000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 52h 7m 
  - Evidence: 52h 7m: 6ab9a9279a8420a1e6b56b77.jsonl[2522] _id=6ac7ec61de269131f9c68814 ts=2026-10-08T19:17:52.8930000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2527] _id=6acac95dde269131f9cb3dd7 ts=2026-10-10T23:25:13.8060000Z; 23h 31m: 6ab9a9279a8420a1e6b56b77.jsonl[1333] _id=6ac69ac6de269131f9bf20b4 ts=2026-10-07T19:17:26.0800000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[1345] _id=6ac7e5a9de269131f9c58bb9 ts=2026-10-08T18:49:09.6030000Z; 23h 26m: 6ab9a9279a8420a1e6b56b77.jsonl[740] _id=6ac54952de269131f9b79c73 ts=2026-10-06T19:17:38.7670000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[748] _id=6ac692fdde269131f9bdf5e6 ts=2026-10-07T18:44:10.8040000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 66h 5m 
  - Evidence: 66h 5m: 6ab9a9279a8420a1e6b56b77.jsonl[4759] _id=6acae10dde269131f9cb4e5e ts=2026-10-11T01:06:20.1740000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[6207] _id=6ace8295de269131f9d18fc0 ts=2026-10-13T19:12:19.1700000Z; 53h 6m: 6ab9a9279a8420a1e6b56b77.jsonl[2191] _id=6ac7e83bde269131f9c5e60a ts=2026-10-08T19:00:08.6060000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[3036] _id=6acad2fcde269131f9cb4187 ts=2026-10-11T00:06:18.4990000Z; 41h 0m: 6ab9a9279a8420a1e6b56b77.jsonl[12362] _id=6ad02d46de269131f9da0f93 ts=2026-10-15T01:32:51.9770000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[13001] _id=6ad26e04de269131f9e7088c ts=2026-10-16T18:33:39.6230000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1496 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[10004] _id=6ad01ee3de269131f9d9c642 ts=2026-10-15T00:31:29.1730000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[10000] _id=6ad01ee3de269131f9d9c644 ts=2026-10-15T00:31:29.1730000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[10015] _id=6ad01efcde269131f9d9c698 ts=2026-10-15T00:31:54.6020000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[10009] _id=6ad01efcde269131f9d9c69a ts=2026-10-15T00:31:54.6020000Z; 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[10020] _id=6ad01efdde269131f9d9c6a3 ts=2026-10-15T00:31:55.5540000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[10021] _id=6ad01efdde269131f9d9c6a4 ts=2026-10-15T00:31:55.5540000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 66h 45m 
  - Evidence: 66h 45m: 6ab9a9279a8420a1e6b56b77.jsonl[3345] _id=6acad75dde269131f9cb43e5 ts=2026-10-11T00:25:00.4250000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[6137] _id=6ace8218de269131f9d17a3c ts=2026-10-13T19:10:15.6630000Z; 53h 21m: 6ab9a9279a8420a1e6b56b77.jsonl[2237] _id=6ac7e893de269131f9c5f412 ts=2026-10-08T19:01:38.5990000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[3278] _id=6acad6ebde269131f9cb4363 ts=2026-10-11T00:23:06.3250000Z; 29h 14m: 6ab9a9279a8420a1e6b56b77.jsonl[6189] _id=6ace826cde269131f9d187e6 ts=2026-10-13T19:11:39.4060000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[9342] _id=6ad01dbede269131f9d9c03c ts=2026-10-15T00:26:37.4500000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 65h 50m 
  - Evidence: 65h 50m: 6ab9a9279a8420a1e6b56b77.jsonl[4530] _id=6acadd97de269131f9cb4c6e ts=2026-10-11T00:51:34.3360000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5338] _id=6ace7b91de269131f9d10fd2 ts=2026-10-13T18:42:24.1070000Z; 52h 21m: 6ab9a9279a8420a1e6b56b77.jsonl[2458] _id=6ac7ebbdde269131f9c67563 ts=2026-10-08T19:15:08.7840000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2765] _id=6acacc02de269131f9cb3f7d ts=2026-10-10T23:36:33.8830000Z; 24h 2m: 6ab9a9279a8420a1e6b56b77.jsonl[5541] _id=6ace7e00de269131f9d12f2b ts=2026-10-13T18:52:47.5940000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[7877] _id=6acfd034de269131f9d7bc9e ts=2026-10-14T18:55:47.1590000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.019s..0.020s shown 
  - Evidence: 19ms: 6ab9a9279a8420a1e6b56b77.jsonl[2417] _id=6ac7eb3fde269131f9c66757 ts=2026-10-08T19:13:02.3370000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2421] _id=6ac7eb3fde269131f9c6675b ts=2026-10-08T19:13:02.3560000Z; 20ms: 6ab9a9279a8420a1e6b56b77.jsonl[2773] _id=6acacc3bde269131f9cb3f95 ts=2026-10-10T23:37:30.0550000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2774] _id=6acacc3bde269131f9cb3f96 ts=2026-10-10T23:37:30.0750000Z; 20ms: 6ab9a9279a8420a1e6b56b77.jsonl[2774] _id=6acacc3bde269131f9cb3f96 ts=2026-10-10T23:37:30.0750000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2778] _id=6acacc3bde269131f9cb3f9a ts=2026-10-10T23:37:30.0950000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 78h 11m 
  - Evidence: 78h 11m: 6ab9a9279a8420a1e6b56b77.jsonl[1212] _id=6ac69924de269131f9befe11 ts=2026-10-07T19:10:28.1430000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5123] _id=6acae4b9de269131f9cb5133 ts=2026-10-11T01:22:00.9420000Z; 65h 41m: 6ab9a9279a8420a1e6b56b77.jsonl[5169] _id=6acae522de269131f9cb516f ts=2026-10-11T01:23:45.3880000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5963] _id=6ace80e9de269131f9d1528d ts=2026-10-13T19:05:12.9510000Z; 43h 7m: 6ab9a9279a8420a1e6b56b77.jsonl[12661] _id=6ad03072de269131f9da1d44 ts=2026-10-15T01:46:25.9080000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14507] _id=6ad28ed9de269131f9e820e8 ts=2026-10-16T20:53:44.6410000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 78h 9m 
  - Evidence: 78h 9m: 6ab9a9279a8420a1e6b56b77.jsonl[1213] _id=6ac69925de269131f9befe15 ts=2026-10-07T19:10:28.1710000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5062] _id=6acae44dde269131f9cb50a8 ts=2026-10-11T01:20:12.4910000Z; 65h 40m: 6ab9a9279a8420a1e6b56b77.jsonl[5170] _id=6acae522de269131f9cb5171 ts=2026-10-11T01:23:45.4220000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5904] _id=6ace80a4de269131f9d14e76 ts=2026-10-13T19:04:03.7540000Z; 43h 6m: 6ab9a9279a8420a1e6b56b77.jsonl[12665] _id=6ad03072de269131f9da1d49 ts=2026-10-15T01:46:25.9690000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14477] _id=6ad28ea0de269131f9e82061 ts=2026-10-16T20:52:48.1400000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.047s..0.047s shown 
  - Evidence: 47ms: 6ab9a9279a8420a1e6b56b77.jsonl[12662] _id=6ad03072de269131f9da1d46 ts=2026-10-15T01:46:25.9220000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12665] _id=6ad03072de269131f9da1d49 ts=2026-10-15T01:46:25.9690000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 78h 9m 
  - Evidence: 78h 9m: 6ab9a9279a8420a1e6b56b77.jsonl[1210] _id=6ac69919de269131f9befd42 ts=2026-10-07T19:10:16.3310000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5063] _id=6acae450de269131f9cb50ad ts=2026-10-11T01:20:15.6310000Z; 65h 40m: 6ab9a9279a8420a1e6b56b77.jsonl[5157] _id=6acae51fde269131f9cb516d ts=2026-10-11T01:23:41.9160000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5917] _id=6ace80a9de269131f9d14ea6 ts=2026-10-13T19:04:08.6840000Z; 43h 6m: 6ab9a9279a8420a1e6b56b77.jsonl[12640] _id=6ad03071de269131f9da1d3e ts=2026-10-15T01:46:24.3490000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14479] _id=6ad28eaade269131f9e82070 ts=2026-10-16T20:52:58.0650000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 37 interval(s) ≤ 0.003s..0.017s shown 
  - Evidence: 3ms: 6ab9a9279a8420a1e6b56b77.jsonl[14562] _id=6ad28f3ede269131f9e82179 ts=2026-10-16T20:55:25.8400000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14563] _id=6ad28f3ede269131f9e8217b ts=2026-10-16T20:55:25.8430000Z; 7ms: 6ab9a9279a8420a1e6b56b77.jsonl[12604] _id=6ad03031de269131f9da1c08 ts=2026-10-15T01:45:20.1830000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12607] _id=6ad03031de269131f9da1c0a ts=2026-10-15T01:45:20.1900000Z; 17ms: 6ab9a9279a8420a1e6b56b77.jsonl[1142] _id=6ac698bbde269131f9bef48d ts=2026-10-07T19:08:42.4530000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[1170] _id=6ac698bbde269131f9bef48e ts=2026-10-07T19:08:42.4700000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 78h 13m 
  - Evidence: 78h 13m: 6ab9a9279a8420a1e6b56b77.jsonl[1155] _id=6ac698a8de269131f9bef2a1 ts=2026-10-07T19:08:23.9790000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5121] _id=6acae4b7de269131f9cb512f ts=2026-10-11T01:21:58.3000000Z; 73h 50m: 6ab9a9279a8420a1e6b56b77.jsonl[5962] _id=6ace80e6de269131f9d1525b ts=2026-10-13T19:05:09.2350000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14557] _id=6ad28f2fde269131f9e82169 ts=2026-10-16T20:55:11.3780000Z; 65h 43m: 6ab9a9279a8420a1e6b56b77.jsonl[5121] _id=6acae4b7de269131f9cb512f ts=2026-10-11T01:21:58.3000000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5951] _id=6ace80e1de269131f9d15220 ts=2026-10-13T19:05:04.5540000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 41h 36m 
  - Evidence: 41h 36m: 6ab9a9279a8420a1e6b56b77.jsonl[11154] _id=6ad024e3de269131f9d9e497 ts=2026-10-15T00:57:07.0370000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12990] _id=6ad26dfdde269131f9e707c4 ts=2026-10-16T18:33:32.8960000Z; 6h 13m: 6ab9a9279a8420a1e6b56b77.jsonl[7424] _id=6acfcd59de269131f9d76c36 ts=2026-10-14T18:43:36.2370000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[11153] _id=6ad024ddde269131f9d9e48b ts=2026-10-15T00:57:00.5800000Z; 1h 51m: 6ab9a9279a8420a1e6b56b77.jsonl[14147] _id=6ad27301de269131f9e77407 ts=2026-10-16T18:54:57.2670000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14298] _id=6ad28d15de269131f9e81e6d ts=2026-10-16T20:46:13.3680000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 67h 5m 
  - Evidence: 67h 5m: 6ab9a9279a8420a1e6b56b77.jsonl[2677] _id=6acacab9de269131f9cb3ed8 ts=2026-10-10T23:31:04.4700000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5256] _id=6ace7a4fde269131f9d0fc14 ts=2026-10-13T18:37:02.1240000Z; 52h 36m: 6ab9a9279a8420a1e6b56b77.jsonl[1339] _id=6ac7e591de269131f9c58a2e ts=2026-10-08T18:48:48.4910000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2552] _id=6acac950de269131f9cb3dd3 ts=2026-10-10T23:25:03.7630000Z; 42h 12m: 6ab9a9279a8420a1e6b56b77.jsonl[9192] _id=6ad01c6bde269131f9d9be3f ts=2026-10-15T00:20:58.4740000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12988] _id=6ad26debde269131f9e705f0 ts=2026-10-16T18:33:14.7150000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 65h 44m 
  - Evidence: 65h 44m: 6ab9a9279a8420a1e6b56b77.jsonl[4538] _id=6acaddcdde269131f9cb4c7c ts=2026-10-11T00:52:28.5050000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5255] _id=6ace7a4fde269131f9d0fc13 ts=2026-10-13T18:37:02.1240000Z; 52h 35m: 6ab9a9279a8420a1e6b56b77.jsonl[1347] _id=6ac7e5a9de269131f9c58bbb ts=2026-10-08T18:49:12.0810000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2551] _id=6acac950de269131f9cb3dd2 ts=2026-10-10T23:25:03.7630000Z; 40h 55m: 6ab9a9279a8420a1e6b56b77.jsonl[12449] _id=6ad02e71de269131f9da15cc ts=2026-10-15T01:37:52.3840000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12987] _id=6ad26debde269131f9e705ef ts=2026-10-16T18:33:14.7150000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 89h 49m 
  - Evidence: 89h 49m: 6ab9a9279a8420a1e6b56b77.jsonl[4532] _id=6acaddafde269131f9cb4c78 ts=2026-10-11T00:51:57.9010000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[7339] _id=6acfccbfde269131f9d75391 ts=2026-10-14T18:41:02.7390000Z; 52h 42m: 6ab9a9279a8420a1e6b56b77.jsonl[1346] _id=6ac7e5a9de269131f9c58bba ts=2026-10-08T18:49:12.0750000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2689] _id=6acacac7de269131f9cb3edf ts=2026-10-10T23:31:17.9170000Z; 41h 6m: 6ab9a9279a8420a1e6b56b77.jsonl[12442] _id=6ad02e65de269131f9da1586 ts=2026-10-15T01:37:40.0000000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[13769] _id=6ad2707cde269131f9e74262 ts=2026-10-16T18:44:12.6300000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 65h 12m 
  - Evidence: 65h 12m: 6ab9a9279a8420a1e6b56b77.jsonl[5247] _id=6acae624de269131f9cb5216 ts=2026-10-11T01:28:03.1830000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[5298] _id=6ace7b11de269131f9d109b2 ts=2026-10-13T18:40:16.0650000Z; 52h 12m: 6ab9a9279a8420a1e6b56b77.jsonl[2408] _id=6ac7eb27de269131f9c66471 ts=2026-10-08T19:12:38.6580000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[2563] _id=6acac95dde269131f9cb3dd9 ts=2026-10-10T23:25:15.8930000Z; 40h 33m: 6ab9a9279a8420a1e6b56b77.jsonl[12980] _id=6ad033a5de269131f9da292f ts=2026-10-15T02:00:04.1820000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[12991] _id=6ad26dffde269131f9e7080b ts=2026-10-16T18:33:33.1200000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b77.jsonl[14651] _id=6ad28fb4de269131f9e8224b ts=2026-10-16T20:57:24.1850000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14652] _id=6ad28fb4de269131f9e8224c ts=2026-10-16T20:57:24.1850000Z; 1ms: 6ab9a9279a8420a1e6b56b77.jsonl[1123] _id=6ac69858de269131f9beed10 ts=2026-10-07T19:07:03.5540000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[1124] _id=6ac69858de269131f9beed11 ts=2026-10-07T19:07:03.5550000Z; 4ms: 6ab9a9279a8420a1e6b56b77.jsonl[14824] _id=6ad2919fde269131f9e824ee ts=2026-10-16T21:05:35.2560000Z -> 6ab9a9279a8420a1e6b56b77.jsonl[14825] _id=6ad2919fde269131f9e824f0 ts=2026-10-16T21:05:35.2600000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[1127] _id=6ac6984ade269131f9beec48 ts=2026-10-07T19:06:49.3140000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1221] _id=6ac6993dde269131f9beffcb ts=2026-10-07T19:10:53.0390000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[2977] _id=6acad178de269131f9cb4123 ts=2026-10-10T23:59:51.1950000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[6006] _id=6ace8116de269131f9d155a8 ts=2026-10-13T19:05:57.5890000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[12665] _id=6ad03072de269131f9da1d49 ts=2026-10-15T01:46:25.9690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[12990] _id=6ad26dfdde269131f9e707c4 ts=2026-10-16T18:33:32.8960000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[14147] _id=6ad27301de269131f9e77407 ts=2026-10-16T18:54:57.2670000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[14298] _id=6ad28d15de269131f9e81e6d ts=2026-10-16T20:46:13.3680000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[1344] _id=6ac7e5a9de269131f9c58bb7 ts=?`; `6ab9a9279a8420a1e6b56b77.jsonl[2678] _id=6acacac7de269131f9cb3edc ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 42 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[3563] _id=6acad86cde269131f9cb458f ts=2026-10-11T00:29:29.6180000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[3565] _id=6acad86dde269131f9cb4595 ts=2026-10-11T00:29:29.7030000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[3577] _id=6acad86dde269131f9cb4597 ts=2026-10-11T00:29:29.7030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 94 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[1447] _id=6ac7e699de269131f9c5a8dc ts=2026-10-08T18:53:10.4460000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1442] _id=6ac7e69ade269131f9c5a90a ts=2026-10-08T18:53:10.6500000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[3376] _id=6acad7c6de269131f9cb4431 ts=2026-10-11T00:26:44.0220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[5961] _id=6ace80e4de269131f9d1524d ts=2026-10-13T19:05:07.9160000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[14558] _id=6ad28f32de269131f9e8216b ts=2026-10-16T20:55:14.1990000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[14560] _id=6ad28f39de269131f9e82171 ts=2026-10-16T20:55:20.7090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 392 start, 386 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 864 open, 852 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 9 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 47 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 347 of 14966 adjacent _id pairs reverse in client time; worst 32.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b77.jsonl[1520] _id=6ac7e730de269131f9c5bc0e ts=2026-10-08T18:55:43.1020000Z`; `6ab9a9279a8420a1e6b56b77.jsonl[1508] _id=6ac7e731de269131f9c5bc32 ts=2026-10-08T18:55:10.9030000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.97s, min -84677.21s, max -0.16s over 14967 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b77\coverage.yaml

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

### `InputEvent` — 5556 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dungeon Dev (1310); Unit 4 Dev - Dungeon (1282); Unit 2 Prod (Refactor) (910); Unit 3 Dev (551); Unit 1 Dev (479); Unit 5 Dev - Dungeon (404); Unit 4 Dev (333); Unit 5 Dev (247); Unit 4 Dev - Anderson Base (40)
- **Intervals:** median 1.15s (p5 0.16s / p95 13.16s, n=5555)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5556/5556 records)
    "pressed"  x5556
data.actionType  (string, 5556/5556 records)
    "Move"  x4515
    "Interact"  x608
    "Jump"  x296
    "Sprint"  x54
    "Ascend"  x35
    "Hoverboard"  x27
    "Map"  x10
    "Pause"  x6
    "Descend"  x2
    "SkipCinematic"  x2
    "ToggleDebug"  x1
data.key  (string, 5556/5556 records, 9 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5556/5556 records)
    "Player"  x5032
    "Drone"  x524
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3260 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1320); Unit 4 Dev (798); Unit 3 Dungeon Dev (676); Unit 5 Dev - Dungeon (466)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.45s, n=3259)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3260/3260 records)
    "BecameVisible"  x864
    "BecameInvisible"  x852
    "BecameCameraCentered"  x772
    "BecameCameraUncentered"  x772
data.pieceId  (string, 3260/3260 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3260/3260 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2785 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (829); Unit 1 Dev (420); Unit 3 Dev (336); Unit 4 Dev - Dungeon (319); Unit 3 Dungeon Dev (289); Unit 4 Dev (212); Unit 5 Dev (194); Unit 5 Dev - Dungeon (128); Unit 4 Dev - Anderson Base (58)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.09s, n=2773)
- **Fields under `data`:**

```text
data.position  (object, 2785/2785 records)
data.position.x  (number, 2785/2785 records)
    numeric range -829.459 .. 1558.17 (1085 unique)
data.position.y  (number, 2785/2785 records)
    numeric range -114.326 .. 222.005 (698 unique)
data.position.z  (number, 2785/2785 records)
    numeric range -1041.83 .. 2187.79 (1079 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2178 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (599); Unit 3 Dev (304); Unit 1 Dev (288); Unit 4 Dev (259); Unit 5 Dev (254); Unit 3 Dungeon Dev (188); Unit 4 Dev - Dungeon (123); Unit 4 Dev - Anderson Base (82); Unit 5 Dev - Dungeon (81)
- **eventKey:** present on 1400 of 2178 records
- **Intervals:** median 4.68s (p5 0.00s / p95 47.65s, n=2177)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1400; [conversationId, dialogueEventType] x778
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2178/2178 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2178/2178 records)
    "DialogueNodeEvent"  x1400
    "DialogueStartEvent"  x392
    "DialogueFinishEvent"  x386
data.nodeId  (number, 1400/2178 records)
    numeric range 0 .. 290 (229 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 376 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (127); Unit 3 Dungeon Dev (94); Unit 1 Dev (52); Unit 2 Prod (Refactor) (41); Unit 4 Dev (25); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (9); Unit 5 Dev - Dungeon (7)
- **Intervals:** median 12.40s (p5 0.19s / p95 376.28s, n=375)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 376/376 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 376/376 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 283 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 5 Dev (86); Unit 3 Dev (59); Unit 2 Prod (Refactor) (57); Unit 4 Dev - Anderson Base (51); Unit 1 Dev (30)
- **Intervals:** median 0.79s (p5 0.03s / p95 9.98s, n=282)
- **Fields under `data`:**

```text
data.actionType  (string, 283/283 records)
    "argumentationNodeHoverEnd"  x122
    "argumentationNodeHoverStart"  x122
    "argumentationNodeAdd"  x30
    "argumentationNodeRemove"  x9
data.argumentationTitle  (string, 283/283 records)
    "Unit 5"  x86
    "Unit 3 - Pollution Upstream"  x59
    "Unit 2 – Watershed"  x57
    "Unit 4 - Flooding"  x51
    "Unit 1 - Freshwater"  x17
    "Unit 1 - Argumentation Tutorial"  x13
data.nodeName  (string, 283/283 records)
    "1"  x41
    "3"  x35
    "A"  x35
    "2"  x31
    "I"  x31
    "4"  x26
    "II"  x25
    "B"  x20
    "C"  x20
    "D"  x14
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 121 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (89); Unit 3 Dev (26); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (2)
- **Intervals:** median 3.83s (p5 0.38s / p95 1315.54s, n=120)
- **`data` key-set variants:** [actionType, featureUsed] x50; [actionType, featureUsed, location] x49; [actionType, featureUsed, legendName] x22
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 121/121 records)
    "WaypointMoveEvent"  x42
    "MapCloseEvent"  x25
    "MapOpenEvent"  x25
    "Selected"  x16
    "Unselected"  x6
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x1
data.featureUsed  (string, 121/121 records)
    "Map"  x50
    "Waypoint"  x49
    "Legend"  x22
data.legendName  (string, 22/121 records)
    "90 ft"  x11
    "0 ft"  x2
    "330 ft"  x2
    "Water"  x2
    "150 ft"  x1
    "180 ft"  x1
    "210 ft"  x1
    "240 ft"  x1
    "270 ft"  x1
data.location  (object, 49/121 records)
data.location.x  (number, 49/121 records)
    numeric range -451.567 .. 138.914 (39 unique)
data.location.y  (number, 49/121 records)
    numeric range -273.176 .. 261.069 (42 unique)
data.location.z  (number, 49/121 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 102 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (52); Unit 3 Dev (42); Unit 4 Dev (8)
- **Intervals:** median 0.49s (p5 0.15s / p95 18.74s, n=101)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x94; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/102 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/102 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 94/102 records)
    "RightDrag"  x50
    "LeftDrag"  x44
data.currentSoilType  (string, 94/102 records)
    "CLAYSAND"  x21
    "CLAY"  x20
    "SAND"  x17
    "CLAYROCK"  x14
    "SANDGRAVEL"  x12
    "BEDROCK"  x5
    "GRAVEL"  x5
data.isCorrectSelection  (string, 94/102 records)
    "false"  x71
    "true"  x23
data.waterLevelStatus  (string, 94/102 records)
    "Proper"  x35
    "TooHigh"  x35
    "TooLow"  x24
data.waterRetentionChange  (string, 94/102 records)
    "Increase"  x38
    "Decrease"  x33
    "NoChange"  x23
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (17); Unit 3 Dev (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 254.71s (p5 0.01s / p95 84769.79s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x34
data.questID  (string, 81/81 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/81 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 57 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (57)
- **Intervals:** median 6.71s (p5 0.12s / p95 71.46s, n=56)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 57/57 records)
    "On"  x33
    "Off"  x24
data.floor  (string, 57/57 records)
    "3"  x43
    "4"  x7
    "2"  x4
    "1"  x3
data.machineNumber  (string, 57/57 records)
    "One"  x56
    "Two"  x1
data.machineType  (string, 57/57 records)
    "DualChamber_Evaporator"  x19
    "Condenser"  x18
    "DualChamber_Condenser"  x11
    "Evaporator"  x7
    "VentSwitch"  x2
data.room  (string, 57/57 records)
    "2"  x42
    "3"  x7
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 4 Dev (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 836.88s (p5 9.22s / p95 176574.95s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 22 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (12); Unit 2 Prod (Refactor) (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Transition (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 2547.87s (p5 16.80s / p95 189351.68s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 6.77s (p5 0.54s / p95 202.09s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x9
    "Gravel"  x4
    "Bedrock"  x2
    "Sand"  x1
data.floor  (string, 16/16 records)
    "5"  x10
    "3"  x4
    "4"  x2
data.machine  (string, 16/16 records)
    "1"  x15
    "2"  x1
data.row  (string, 16/16 records)
    "TopRow"  x12
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 15 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (6); Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 55.87s (p5 7.54s / p95 252239.40s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "submitAnswerEvent"  x15
data.answerSubmitted  (string, 15/15 records)
    "C,D,4,II"  x3
    "A,1,I"  x2
    "C,D,3,II"  x2
    "A,1,II"  x1
    "A,3,I"  x1
    "A,5,I"  x1
    "A,II"  x1
    "C,D,2,II"  x1
    "C,D,4,2,II"  x1
    "C,D,A,2,II"  x1
    "D,C,3,4,II"  x1
data.argumentationTitle  (string, 15/15 records)
    "Unit 5"  x6
    "Unit 4 - Flooding"  x3
    "Unit 2 – Watershed"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 113.78s (p5 0.05s / p95 254404.73s, n=13)
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

### `gameWindowUnfocusEvent` — 14 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Transition (1); Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 4839.98s (p5 150.42s / p95 243173.44s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    false  x14
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 12 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (12)
- **Intervals:** median 84816.13s (p5 1115.52s / p95 215466.46s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    true  x12
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 11 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (5); Unit 3 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 4.12s (p5 1.04s / p95 274498.84s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 11/11 records)
    "Unit 5"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x1
data.toolName  (string, 11/11 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 10 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (2)
- **Intervals:** median 6.88s (p5 2.31s / p95 202662.20s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "Close"  x5
    "Open"  x5
data.toolName  (string, 10/10 records, 10 empty-string)
    ""  x10
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 3.07s (p5 1.59s / p95 17.40s, n=7)
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
    "Flat"  x1
data.featureUsed  (string, 8/8 records)
    "RoofStyle"  x3
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "Submit"  x1
data.selectedOption  (string, 7/8 records, 1 empty-string)
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `chatEvent` — 7 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 3980.24s (p5 6.15s / p95 117940.48s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "Close"  x5
    "Open"  x2
data.chatID  (string, 7/7 records)
    "NA"  x5
    "[79-71, 79-74, 79-75, 79-76, 79-108]"  x1
    "[91-61, 91-56, 91-57, 91-59, 91-61]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 20.64s (p5 1.56s / p95 59.11s, n=5)
- **Open findings:** 1 — see sections 5-8
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
- **Intervals:** median 218680.19s (p5 29560.95s / p95 331439.15s, n=4)
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
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Pointer is already locked."  x1
    "The root document of this element is not valid for pointer lock."  x1
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
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (52 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (16x); "Unselected" (6x); "WaypointMoveEvent" (42x); "WaypointResetEvent" (1x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (22x); "Waypoint" (49x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (9x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*